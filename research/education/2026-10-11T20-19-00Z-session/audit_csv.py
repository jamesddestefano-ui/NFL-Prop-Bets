#!/usr/bin/env python3
"""Read-only, pinned-input PRIME CSV integrity/coverage audit.

Usage: python audit_csv.py /path/to/local/checkout
Outputs JSON to stdout. Errors go to stderr with exit status 2.
No network requests, subprocesses, repairs, or file writes are performed.
"""

import argparse
import csv
import hashlib
import io
import json
from fractions import Fraction
from pathlib import Path
import sys


REFERENCE_COMMIT = "36bcb5eab6fdad040dddcc0214c7897657db5249"
EXPECTED_BLOBS = {
    "data/line_history.csv": "2acb68477aaf34f6a11d69d981111e85a6399c71",
    "data/decision_ledger.csv": "82f1a4297ee7e7c64dc1f2d37f78ec19729ef416",
    "data/pass_ledger.csv": "e1644b9ee70ba6b39aa1579eae1e03b22151265c",
    "data/bet_history.csv": "9035f654eff5fb3a0be188542593c62c3ba00b05",
    "data/ev_source_signals.csv": "4f4326f53f6d9955e0277ff9617443c8d97ccdb3",
    "data/weekly_attribution.csv": "36a9212ca43dd37011eaa4d2deaed9eee7973ad1",
    "data/missed_bets.csv": "a35dd76bc078d6667dd344ebf901cfe05928d5c6",
    "data/expert_signals.csv": "5b087aaefb301d6c5b179beccd4f5475cbb60ef9",
}


def git_blob_sha(data):
    prefix = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(prefix + data).hexdigest()


def read_verified_inputs(root):
    """Verify all eight byte-level Git blob identities before parsing any."""
    payloads = {}
    errors = []
    for relative, expected in EXPECTED_BLOBS.items():
        path = (root / relative).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            errors.append({"path": relative, "error": "Input resolves outside the supplied root"})
            continue
        try:
            data = path.read_bytes()
        except OSError as exc:
            errors.append({"path": relative, "error": str(exc)})
            continue
        actual = git_blob_sha(data)
        if actual != expected:
            errors.append({
                "path": relative,
                "error": "Git blob SHA mismatch; no audit performed",
                "expected_sha": expected,
                "actual_sha": actual,
            })
        else:
            payloads[relative] = data
    if errors:
        raise ValueError(json.dumps({"input_verification_errors": errors}))
    return payloads


def parse_csv_bytes(data):
    """Keep physical line spans; ignore only completely empty records."""
    reader = csv.reader(io.StringIO(data.decode("utf-8"), newline=""), strict=True)
    records = []
    previous_end = 0
    for cells in reader:
        start, end = previous_end + 1, reader.line_num
        previous_end = end
        if not any(cells):
            continue
        records.append({"start_line": start, "end_line": end, "cells": cells})
    if not records:
        raise ValueError("No nonempty header record")
    header = records[0]["cells"]
    if len(set(header)) != len(header):
        raise ValueError("Duplicate header names")
    rows = records[1:]
    consistent = [r for r in rows if len(r["cells"]) == len(header)]
    anomalies = [
        {
            "start_line": r["start_line"],
            "end_line": r["end_line"],
            "field_count": len(r["cells"]),
            "first_field_id": r["cells"][0],
        }
        for r in rows if len(r["cells"]) != len(header)
    ]
    mapped = [
        {"source_start_line": r["start_line"], **dict(zip(header, r["cells"]))}
        for r in consistent
    ]
    summary = {
        "header_fields": len(header),
        "headers": header,
        "data_records": len(rows),
        "header_width_consistent_records": len(consistent),
        "width_mismatched_records": len(anomalies),
        "anomalies": anomalies,
        "multiline_records": [
            {"start_line": r["start_line"], "end_line": r["end_line"]}
            for r in records if r["start_line"] != r["end_line"]
        ],
        "nonempty_counts_consistent_width_only": {
            name: sum(row[name] != "" for row in mapped) for name in header
        },
    }
    return summary, mapped, records


def american_probability(value):
    odds = Fraction(value)
    if odds == 0:
        raise ValueError("Zero American odds are undefined")
    return 100 / (odds + 100) if odds > 0 else -odds / (100 - odds)


def arithmetic_checks(rows):
    implied, no_vig = [], []
    for row in rows:
        if row["odds"] and row["implied_probability"]:
            calc = 100 * american_probability(row["odds"])
            recorded = Fraction(row["implied_probability"])
            implied.append({
                "source_line": row["source_start_line"],
                "recorded_percentage": float(recorded),
                "recomputed_percentage": float(calc),
                "absolute_difference_percentage_points": float(abs(recorded - calc)),
            })
        if row["odds"] and row["opposite_side_odds"] and row["no_vig_probability"]:
            p1 = american_probability(row["odds"])
            p2 = american_probability(row["opposite_side_odds"])
            calc = 100 * p1 / (p1 + p2)
            recorded = Fraction(row["no_vig_probability"])
            error = abs(recorded - calc)
            no_vig.append({
                "source_line": row["source_start_line"],
                "recorded_thresholds_match": row["line"] == row["opposite_side_line"],
                "recorded_percentage": float(recorded),
                "recomputed_percentage": float(calc),
                "absolute_difference_percentage_points": float(error),
                "exceeds_0_005_percentage_points": error > Fraction(1, 200),
            })
    def summarize(values):
        return {
            "records": len(values),
            "max_absolute_difference_percentage_points": max(
                (x["absolute_difference_percentage_points"] for x in values), default=None
            ),
            "details": values,
        }
    return {
        "scope": "Recorded-odds arithmetic only; not quote, settlement, model or profitability verification",
        "implied_probability": summarize(implied),
        "multiplicative_no_vig": summarize(no_vig),
    }


def audit(payloads):
    files, mapped, raw = [], {}, {}
    for path, data in payloads.items():
        summary, mapped[path], raw[path] = parse_csv_bytes(data)
        files.append({"path": path, "verified_git_blob_sha": git_blob_sha(data), **summary})
    decisions = mapped["data/decision_ledger.csv"]
    probability_rows = [
        r for r in decisions
        if r["estimated_over_probability"] != "" and r["estimated_under_probability"] != ""
    ]
    groups = {
        tuple(r[k] for k in ["nfl_week", "game", "player", "prop_type"])
        for r in probability_rows
    }
    header = raw["data/decision_ledger.csv"][0]["cells"]
    example = next(r for r in raw["data/decision_ledger.csv"] if r["start_line"] == 7)
    literal_mapping = dict(zip(header, example["cells"]))
    example_keys = [
        "estimated_over_probability", "estimated_under_probability",
        "market_implied_probability", "decision_status", "decision_reason",
    ]
    return {
        "audit_schema_version": 1,
        "repository": "jamesddestefano-ui/NFL-Prop-Bets",
        "reference_commit": REFERENCE_COMMIT,
        "verification": "Exact Git blob bytes for all eight files; HEAD is not inspected",
        "read_only": True,
        "limitations": [
            "Record counts are not independent outcome counts.",
            "Width consistency does not certify semantic correctness.",
            "Coverage excludes malformed records rather than guessing their field alignment.",
            "The line-7 mapping is shown only to demonstrate drift, not endorse its values.",
            "No historical quote, original forecast, ticket or settlement source was verified.",
        ],
        "files": files,
        "totals": {
            "files": len(files),
            "data_records": sum(f["data_records"] for f in files),
            "width_mismatched_records": sum(f["width_mismatched_records"] for f in files),
        },
        "decision_coverage_consistent_width_only": {
            "records": len(decisions),
            "records_with_both_probability_fields": len(probability_rows),
            "distinct_week_game_player_prop_groups": len(groups),
            "nonempty": {
                key: sum(r[key] != "" for r in decisions)
                for key in ["actual_result", "outcome", "brier_score", "closing_line", "closing_odds"]
            },
        },
        "literal_drift_example_not_reconstruction": {
            "path": "data/decision_ledger.csv",
            "source_line": 7,
            "header_fields": len(header),
            "record_fields": len(example["cells"]),
            "first_field_id": example["cells"][0],
            "header_position_mapping": {k: literal_mapping[k] for k in example_keys},
        },
        "arithmetic_checks": arithmetic_checks(mapped["data/line_history.csv"]),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path, help="Local repository root containing the pinned eight CSV files")
    args = parser.parse_args()
    try:
        payloads = read_verified_inputs(args.checkout.expanduser().resolve())
        result = audit(payloads)
    except (OSError, UnicodeError, csv.Error, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"audit_failed": True, "reason": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
