"""Offline synthetic PRIME ingestion rehearsal with machine-readable audit report.

No MotherDuck connection, live sportsbook calls, or account credentials.
"""
import argparse
import json
import pathlib
import sys
import traceback
from datetime import datetime, timezone
from scripts.prime_ingest_boundary import synthetic_fixture, validate_batch
from scripts.prime_ingest_persist import persist_synthetic_batch

class Cursor:
    def __init__(self, count=0):
        self.count = count
    def fetchone(self):
        return (self.count,)

class TransactionalFake:
    def __init__(self, fail_quote=False):
        self.statements = []
        self.fingerprints = set()
        self.pending = None
        self.fail_quote = fail_quote
    def execute(self, sql, params=None):
        self.statements.append(sql)
        if sql == "BEGIN TRANSACTION":
            self.pending = {"fingerprint": None, "quotes": 0}
        elif sql.startswith("SELECT COUNT(*)"):
            return Cursor(int(params[0] in self.fingerprints))
        elif "INSERT INTO my_db.prime_research.ingestion_batches" in sql:
            self.pending["fingerprint"] = params[0]
        elif "INSERT INTO my_db.prime_research.odds_quotes" in sql:
            if self.fail_quote:
                raise RuntimeError("synthetic injected write failure")
            self.pending["quotes"] += 1
        elif sql == "COMMIT":
            if self.pending["fingerprint"]:
                self.fingerprints.add(self.pending["fingerprint"])
            self.pending = None
        elif sql == "ROLLBACK":
            self.pending = None
        return Cursor()

def run():
    fixture = synthetic_fixture()
    validated = validate_batch(fixture)
    fake = TransactionalFake()
    first = persist_synthetic_batch(fake, fixture)
    repeat = persist_synthetic_batch(fake, fixture)
    failure = TransactionalFake(fail_quote=True)
    rolled_back = False
    try:
        persist_synthetic_batch(failure, fixture)
    except RuntimeError:
        rolled_back = failure.statements[-1] == "ROLLBACK" and failure.pending is None
    assert first["inserted"] == 2 and repeat["inserted"] == 0 and rolled_back
    return {"status": "PASS", "mode": "OFFLINE_SYNTHETIC_ONLY",
            "batch_sha256": validated["batch_sha256"],
            "validated_quotes": validated["record_count"],
            "first_insert": first["status"], "duplicate_attempt": repeat["status"],
            "rollback_injected_failure": rolled_back,
            "motherduck_writes": 0, "live_api_calls": 0}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/prime_ingest_e2e_audit.json")
    args = parser.parse_args()
    try:
        report = run()
    except Exception as exc:
        report = {"status": "FAIL", "mode": "OFFLINE_SYNTHETIC_ONLY",
                  "error_type": type(exc).__name__, "error": str(exc)}
    report["audited_at_utc"] = datetime.now(timezone.utc).isoformat()
    target = pathlib.Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
