# PRIME exact-contract as-of pairing gap — 2026-10-17

**Finding:** SOURCE-VERIFIED POTENTIAL DATA INTEGRITY DEFECT; test execution and impact on actual observations INCONCLUSIVE. Research only; MODEL_SUSPECT remains unchanged.

## Source access and immutable references
Access method: authenticated GitHub connector, on 2026-10-17 ET. Private source file paths and Git blob hashes:
- `scripts/quote_persistence.py` — `5fbda78894d84c0113990492cbe60c6c029fdc78`.
- `scripts/validate_consensus.py` — `73f7b1c5dd27c06dc2d185716dcdeab5047a29e9`.
- Duplicate-side corrections previously verified by commits `c783aaeba71bdfb086a5a40c14d3c288f20966e0` and `ec6e7c25daa1bceee285bc330db84881775d3a09`; these protections must remain intact.

## Code-inspection finding
Both consumers aggregate sides under keys containing `event_id`, `market`, `player_id`, `point` and `bookmaker`, but not `response_received_utc`, market last-update, kickoff identity or settlement terms. They individually check `received < kickoff`, which does **not** ensure two sides were contemporaneously observed. For example, synthetic identical-contract Over received at 12:00 UTC and Under received at 12:45 UTC (kickoff 17:00 UTC) meet the current per-row pregame test and can form a pair with noncontemporaneous prices. Duplicate-sided quarantine does not close this separate gap.

Consequences if such input is present: mixed-time no-vig probabilities may enter consensus or persistence flags, manufacturing or distorting apparent edge. This is **not** proof that actual stored provider snapshots contain mixed-time rows or that any real recommendation was affected.

## Falsifiable regression protocol (not yet executed)
1. Construct a six-row, three-book **synthetic-only** clean same-line fixture; each book has Over/Under sharing `response_received_utc`. Expect three eligible books and six evaluated research sides.
2. Change just one Under receipt time to 45 minutes after its Over (both still pre-kickoff). Expect that bookmaker to be quarantined as `ASOF_MISMATCH`, leaving at most two books and zero three-book consensus candidates.
3. Test both permutations of mismatched Over/Under and mismatched `commence_time`, plus timezone-offset-equivalent strings (compare normalized instants, not raw strings).
4. Confirm all prior duplicate-Over and duplicate-Under regressions still PASS and the original snapshots remain immutable.
5. Predeclare the allowed pairing clock policy (exact same capture timestamp or a small documented bound) using provider response semantics. Do not silently choose or change a numeric tolerance after seeing candidate EV results.

## Acceptance criteria and blockers
Implementation requires an explicit, v1-compatible pairing policy and independently executed regression evidence against exact GitHub source revisions. GitHub status queries for the prior private CI workflow returned no confirmed check results; workflow source existing is not CI PASS. Review of raw private historical quote data is intentionally excluded from this public review. Do not copy raw provider prices or secrets to this repository.

**Result:** INCONCLUSIVE for measured data impact and dynamic repro; SOURCE-VERIFIED for missing cross-side as-of check. No wagers, model promotion, historical rewrite, paid requests, or changes to authoritative records.
