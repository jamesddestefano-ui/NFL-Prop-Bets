# PRIME data-feasibility audit

## Finding

The inspected CSV files are useful research records, but they are not currently a clean, joined retrospective validation dataset. A confirmed header/record-width problem can shift probability and decision fields during automated ingestion. Separately, the inspected records lack a complete frozen-forecast/outcome/closing-reference panel.

This does **not** establish that recorded bets or settlements are false. No records were repaired, deleted, reclassified or backfilled.

- Repository: jamesddestefano-ui/NFL-Prop-Bets
- Pinned commit: `36bcb5eab6fdad040dddcc0214c7897657db5249`
- Read window: 2026-10-11 20:06–20:09 UTC (16:06–16:09 EDT)
- Scope: eight CSV files listed below. Full contents were read for structural counts; selected records were inspected for meaning. No unrelated repository sweep, original-ticket verification, immutable-archive reconstruction or historical model backtest was performed.
- Evidence classification: observed file contents and parser results are **empirical repository evidence**. The proposed next experiment and repair workflow are **untested proposals**.

## Parsing method

Two independent parsers agreed: a JavaScript quote-state parser and Python's standard-library `csv.reader(io.StringIO(text), strict=True)`. Both honor quoted commas and doubled quote escapes; Python's `reader.line_num` recorded physical record boundaries. Blank physical lines were excluded from data-row counts.

No quoted multiline records or unterminated-quote failure were found in these eight files. Successful CSV syntax parsing does not enforce consistent field counts. An unquoted comma in prose can parse successfully as an extra field.

All anomaly locations below are physical source line numbers; those anomalous records each occupy one physical line. They include the header at line 1. Do not assume all logical-record numbers equal physical lines, because blank lines are possible.

### Reproduce the read-only audit

Use the accompanying standard-library [audit_csv.py](audit_csv.py) with an explicit local checkout root:

```text
python /path/to/audit_csv.py /path/to/NFL-Prop-Bets
```

The script writes JSON to stdout only. It makes no network requests, invokes no subprocesses, performs no repairs, and writes no files. A caller can redirect stdout to a chosen research-results file outside the source checkout if desired.

Before parsing, it verifies the exact Git blob SHA of all eight files against the recorded baseline. Missing files or changed bytes cause a clear error on stderr, exit status 2, and no partial audit output. Checkout HEAD is not inspected: the eight verified blob identities are the input contract. Line-ending conversion also changes these hashes; the script does not silently normalize or repair it.

The CLI reproduced the 8-file/117-record/14-width-anomaly result using temporary copies of the previously retrieved, hash-verified input bytes. Tests also covered unchanged source bytes/file sets, wrong-hash and missing-input failures, quoted commas and escaped quotes, quoted newlines, blank-line numbering, and unterminated quotes. Temporary ledger copies were removed. See [audit-script-verification.json](audit-script-verification.json) for the script fingerprint and test results. These are parser/arithmetic checks, not production or model validation.

## Structural counts and source identities

| File | Header fields | Data records | Width-mismatched records | Blob SHA |
|---|---:|---:|---:|---|
| [data/line_history.csv](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/36bcb5eab6fdad040dddcc0214c7897657db5249/data/line_history.csv) | 15 | 56 | 0 | `2acb68477aaf34f6a11d69d981111e85a6399c71` |
| [data/decision_ledger.csv](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/36bcb5eab6fdad040dddcc0214c7897657db5249/data/decision_ledger.csv) | 60 | 26 | 6 | `82f1a4297ee7e7c64dc1f2d37f78ec19729ef416` |
| [data/pass_ledger.csv](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/36bcb5eab6fdad040dddcc0214c7897657db5249/data/pass_ledger.csv) | 25 | 17 | 3 | `e1644b9ee70ba6b39aa1579eae1e03b22151265c` |
| [data/bet_history.csv](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/36bcb5eab6fdad040dddcc0214c7897657db5249/data/bet_history.csv) | 26 | 5 | 5 | `9035f654eff5fb3a0be188542593c62c3ba00b05` |
| [data/ev_source_signals.csv](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/36bcb5eab6fdad040dddcc0214c7897657db5249/data/ev_source_signals.csv) | 45 | 0 | 0 | `4f4326f53f6d9955e0277ff9617443c8d97ccdb3` |
| [data/weekly_attribution.csv](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/36bcb5eab6fdad040dddcc0214c7897657db5249/data/weekly_attribution.csv) | 27 | 1 | 0 | `36a9212ca43dd37011eaa4d2deaed9eee7973ad1` |
| [data/missed_bets.csv](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/36bcb5eab6fdad040dddcc0214c7897657db5249/data/missed_bets.csv) | 27 | 5 | 0 | `a35dd76bc078d6667dd344ebf901cfe05928d5c6` |
| [data/expert_signals.csv](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/36bcb5eab6fdad040dddcc0214c7897657db5249/data/expert_signals.csv) | 17 | 7 | 0 | `5b087aaefb301d6c5b179beccd4f5475cbb60ef9` |

### Confirmed anomalies

- decision_ledger: physical lines 6, 7, 12 and 13 contain 61 fields against a 60-field header; lines 26 and 27 contain 59.
- pass_ledger: physical lines 15, 16 and 17 contain 26 fields against a 25-field header.
- bet_history: physical lines 2–6 all contain 27 fields against a 26-field header.

The [machine-readable audit](data-feasibility-results.json) includes exact first-field IDs and all header names. IDs are read directly from the first field; no shifted-field reconstruction was used.

### Minimal, material example

At [decision_ledger.csv line 7](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/36bcb5eab6fdad040dddcc0214c7897657db5249/data/decision_ledger.csv#L7), the first field is `2026W1-OTTON-RECYDS-20260912-0453`. A straightforward header-to-position mapping yields:

| Header | Literal parsed value |
|---|---|
| estimated_over_probability | 29.5 |
| estimated_under_probability | 57.5 |
| market_implied_probability | -135.3 |
| decision_status | 4-6% |
| decision_reason | BET |

These are evidence of field drift, **not** endorsed probabilities or a repaired decision. In particular, a negative implied probability and an edge bucket in the decision-status column make the mapping unusable.

The Cook record at [line 6](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/36bcb5eab6fdad040dddcc0214c7897657db5249/data/decision_ledger.csv#L6) contains an unquoted comma in its trailing result prose, splitting it into extra fields. Other width differences involve empty-field alignment; their intended repair should not be guessed.

The five bet_history rows have a surplus trailing field. Their win/loss text appears in the expected outcome position; this audit does not show that the settlement prefix is wrong. Dropping surplus fields would nevertheless lose material provenance/review text, so silent truncation is inappropriate.

## What is populated, and what remains unknown

### Line history

- 56 records; all have a recorded capture timestamp.
- 54 have odds and implied probability.
- 23 have opposite-side line/odds and a no-vig probability; each records matching thresholds on the two sides.
- 52 have a source URL.
- Captures run from September 11 through October 8, 2026.
- The schema has no explicit opening/entry/closing snapshot-type field, separate source-update timestamp, game-date/season field, or stable contract/decision foreign key. Some source-update times and archive references appear only in notes.
- A populated capture timestamp is not proof of quote freshness. Named aggregates appear alongside named books. The latest available snapshot must not automatically be called the close.

### Decisions

Among the **20 header-width-consistent records**, 12 contain both over and under probability values. These span seven distinct week/game/player/prop groups, so 12 rows are already fewer than 12 distinct underlying player-prop opportunities. This grouping is descriptive, not a proven independence structure.

Across those 20 records, actual_result, outcome, brier_score, closing_line and closing_odds are all blank. Probability examples include backfilled records and labels such as “conservative”; their point-forecast versus robustness role and original pre-outcome provenance must be resolved before scoring. Width consistency alone does not certify correct field semantics.

### Passes and missed recommendations

Among 14 width-consistent pass records, no closing_line, closing_odds or would_have_won value is populated. One actual_result describes an injury exit rather than a complete statistical result.

missed_bets contains five structurally consistent records. Three have recorded LOSS outcomes; two remain blank. All closing-line/price fields are blank. One settled Stafford note states a 58% fair Under probability, but this is not proof that the probability was frozen before the outcome. Reconstructing that provenance would require its original timestamped source.

### Placed bets

bet_history contains five records, each with a trailing surplus field. Settlement text is present in the expected prefix positions, and some cash-stake/payout evidence is in the surplus narrative rather than structured unit fields. Only one internal_fair_probability entry is populated in its expected position. This is inadequate for automated probability calibration, and cash returns should not be reconstructed by silently discarding text or inventing a unit definition.

### Sources and calibration

- ev_source_signals.csv is **present and header-only**, with zero data records. It cannot currently support a source-performance ranking.
- expert_signals.csv has seven recorded Week 1 research signals. Its schema lacks settled outcome, closing-odds and explicit precommitted fair-probability fields. It provides research context rather than a complete analyst scorecard.
- weekly_attribution.csv has one Week 2 review. Closing metrics are blank. Its calibration note gives Stafford 58% Under, 0/1, Brier 0.3364, and excludes Dart after injury. This supports checking that single arithmetic identity; it is not a calibration sample or evidence that the exclusion was prespecified.
- No dedicated calibration CSV appears in the inspected data-directory listing. That is **absence from this directory listing**, not proof that no calibration evidence exists in archives or elsewhere. Those other sources are **unknown to this bounded audit**.

## What can be tested legitimately now

1. **Structural integrity and deterministic arithmetic:** the width checks above are completed. Recomputing from recorded line_history odds gives 54 implied probabilities within 0.00455 percentage points of the stored values. For 23 multiplicative no-vig calculations, maximum absolute difference is 0.01685 percentage points. Two differ by more than ordinary 0.005-point rounding tolerance: physical lines 16 and 27; see JSON. These small differences are arithmetic observations, not measured betting edge.
2. **Case-level record reconciliation:** after checking original pre-outcome archives and settlement evidence, selected forecast/outcome pairs may support transparent case studies. The present audit has not completed that provenance work.
3. **Not yet justified from these CSVs alone:** a reliable paired model-versus-market Brier comparison; calibrated uncertainty bounds; source rankings; matched closing-line performance; or a profitability backtest. Missing data, repeated observations, ambiguous forecast roles and structural anomalies remain unresolved. This is not a claim that a wider authorized archive audit could never recover the needed evidence.

## Minimal safe next experiment

**Untested proposal: a prospective data-completeness pilot for one narrowly defined half-point, two-way NFL prop market.** The first endpoint should be whether a usable evaluation record can be assembled, not whether a small sample looks profitable.

Before outcomes:
- Define the eligible candidate universe and one primary forecast checkpoint.
- Preserve every eligible candidate, including passes; exact book, side, threshold, odds and settlement rules; capture and source quote times; stable game/player/contract IDs; the central forecast, market baseline and conservative scenario input separately; model/scenario versions and source clusters.
- Obtain a fixed, prespecified closing panel and cutoff, or explicitly record unavailable closes.
- Reject malformed research records rather than silently shifting/truncating them. Treat alternate lines and timing snapshots as related records, not independent observations.

After settlement:
- Join verified outcomes without dropping unfavorable injuries; apply predeclared void/push eligibility.
- Publish completeness, attrition, distinct games/players/weeks, and reasons for unavailable values.
- Calculate exploratory paired scores only for eligible, validated records. Keep effect-size uncertainty and selected-subgroup diagnostics; do not declare model success from the pilot.
- Set the sample/precision target for a later efficacy test from the chosen paired endpoint and its dependence structure.

This proposes collection and validation requirements only. No pilot, schema change, watcher or new bet policy was installed.

## Proposed repair workflow, requiring separate authorization

Preserve original bytes and pinned SHAs. Make a derived review copy; resolve each anomalous row against authoritative original messages/tickets/archives rather than assuming which empty field or comma to remove. Use a CSV serializer, explicit column types/scales, enumerated statuses, unique-key checks and contract-aware probability checks. Review the resulting diff and run a read-only lint round-trip before any approved replacement.

Do not automatically pad, truncate, shift, merge narrative fields, delete records, infer missing closes, or manufacture probability estimates. Existing bet truth and provenance must remain recoverable.

