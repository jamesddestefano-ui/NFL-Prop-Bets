# PRIME cross-book as-of alignment — independent source review (2026-10-17)

**Status:** SOURCE-VERIFIED RESEARCH RISK; dynamic reproduction INCONCLUSIVE; model remains MODEL_SUSPECT.

## Source provenance
Authenticated GitHub connector review of private main on 2026-10-17 ET:
- `scripts/quote_persistence.py` Git blob `ba70b1fed0e59b4751f226c98830f28cabdf6996`.
- `scripts/validate_consensus.py` Git blob `2f89f1548a5298375a8d166af59ffcbf3995639b`.
- `tests/test_pair_asof_quarantine_20261017.py` blob `4c8baaeb87313c80d8036c4c3861c948cfcac531`.
- Private workflow `.github/workflows/duplicate-side-quarantine-regression.yml` blob `c1d8577edcf4ce621f820087966f34f5d0fa2c3c`.

## Distinct remaining gap
Both consumers now reject malformed and timezone-less timestamps and prevent *within-book* Over/Under receipt/kickoff mismatches. However, consensus grouping across books uses `(event, market, player)` with a modal line and ignores the relative `response_received_utc` of different books. As a result, independently internally-valid pairs observed at materially different times (e.g. synthetic TEST_A at 12:00 UTC, TEST_B at 12:45, TEST_C at 13:30) can contribute to the same leave-one-out 'fair' probability. Likewise the quote-survival consumer's `flags(groups)` function does not enforce cross-book time alignment. These are *not* contemporaneous consensus snapshots merely because individual book pairs are clean.

This observation is supported by inspected code structure, **not** by a run on actual sportsbook observations. No executable opportunity is established.

## Proposed falsifiable guarded protocol (not executed)
1. In a synthetic three-book fixture, vary both sides' timestamps together per book while keeping side pairing intact; the current same-book validation should accept all three. Document that this is not a valid time-aligned comparison.
2. Pre-register acceptable time-alignment window and reference-as-of strategy based on source semantics before inspecting EV results. Prefer fail-closed `INSUFFICIENT_TIME_ALIGNED_BOOKS` rather than zero-filling stale quotes.
3. Test offsets (same instant different timezone strings), freshness failure, future receipt, source market-update lag, bookmaker composition changes and latest-prelock versus after-kickoff close.
4. Make a bounded research-only change; preserve original immutable snapshots and all existing duplicate and within-book-as-of regressions. Report cohort exclusions and coverage.
5. Independently run exact-source tests; capture real GitHub Actions job/conclusion separately. No CI pass was verified by combined statuses for the previous test change.

Do not choose a permissible maximum age by optimizing the same pilot's detected edges. Do not infer EV or positive CLV from source alignment alone. This review changes no forecast, odds, actual bet, threshold or model gate.
