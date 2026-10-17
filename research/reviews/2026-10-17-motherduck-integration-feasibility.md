# PRIME MotherDuck integration feasibility — 2026-10-17

## Verified connector state
Authenticated MotherDuck connection responds. Databases visible: `my_db` (owned) and `sample_data` (shared sample). `my_db` contains 0 tables and 0 views at inspection. Query guide lists no existing organizational guides. This is an inventory, not an executed data import or statistical study.

## Scope and authority
Only NFL player props. Governing rules: AGENTS.md and config/prime_ev_playbook_v2.md. Private immutable source evidence stays in `jamesddestefano-ui/-NFL-Prop-Odds-Data`. Public `jamesddestefano-ui/NFL-Prop-Bets` retains permitted methodological findings and research handoffs. Do not copy provider-licensed raw quotes into MotherDuck without access/retention confirmation, or change public visibility.

## Proposed research schema (NOT DEPLOYED)
- `capture_runs`: source run ID; event IDs; request-start and response-complete UTC; SHA256; quota; source clock status; pregame eligibility.
- `contract_observations`: source-backed event/book/player/market/threshold/side/odds/settlement rule; explicit source time; missingness, duplicate status, NJ executability status; immutable provenance.
- `screened_cohort`: prospective freeze ID and timestamp, exact source screenshot reference, every screened contract (BET/PASS/WATCH/AVOID), inclusion/exclusion reason and source availability.
- `frozen_forecasts`: independent model version, exact p(win), p(push), p(loss), conservative range, uncertainty/calibration status, immutable as-of timestamp, no fabricated Claude results.
- `outcome_scores`: verified actual settlement, Brier on declared unconditional/conditional basis only, matched same-contract de-vigged CLV where observable, missingness.
Key constraints: never pair markets across lines/books/players or synthesize missing sides; detect duplicate sided contracts; exclude odds responses at/after kickoff as pregame; do not treat API US region as NJ executable; no user tickets from research-only captures.

## Acceptance checks before production import
1. Confirm account/database access policy and vendor licensing for analytics retention and external sharing.
2. Perform a synthetic-only schema fixture proving clean pair, missing-side, duplicate-side, post-kickoff, and timestamp-only-refresh behavior.
3. Import only an explicitly approved, provenance-complete minimal batch; validate source hash and original row counts against private GitHub.
4. Benchmark unique raw observations vs SCREENED contracts separately. Do not infer 300 screened contracts from thousands of API quote rows.
5. Document query reproducibility, immutable freeze cohort, matched CLV coverage, probability basis, conservative EV gate and prospective grading.
6. Keep PRIME v2 standard -150 to +150 central 4pp and conservative EV>=0, long odds/TD central ROI>=15% and conservative EV>=0, with no redundant 5% ROI gate.
7. Do not create production tables, jobs/flights, schedules or chargeable compute under this memo.

Status: CONNECTOR_VERIFIED; SCHEMA_NOT_CREATED; DATA_NOT_IMPORTED; NO_CLAIM_OF_PROFITABLE_EDGE. 
