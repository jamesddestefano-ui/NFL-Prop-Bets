# PRIME synthetic ingest CI evidence gap — 2026-10-17

Status: INCONCLUSIVE for CI execution / real database persistence. Research-only, no model promotion.

## Sources inspected on main
- Governing public AGENTS.md blob 4ce3ff619aab07f33f71bc150812fa2b908c9ad0 and v2 playbook blob 19fbe1fdf186efcfd9b4faad8a46843a4702518c.
- Private AGENTS.md and research/PLUGIN_RESEARCH_INTEGRATION.md and research/AUTOPILOT_GOVERNANCE.md reviewed before this assessment; private raw odds not used.
- Source workflow change commit a7f17de6d3993b6e5495bbb378353bfaf6481014, adding runner tests to .github/workflows/prime-ingest-e2e-validation.yml.
- Source runner file blob 155d6fb8cca6b559511c6dcabca08167dff69848.
- Source runner test blob 89c42ef9cf1e974a9995e14a7bcae52637c1f095.
- Source fake connection blob 463197a93c54f2c9ff8cee942a5f28b1267e2541.
- Source boundary blob c2a90dc573e19232fd19c36e1b7e5564e413e9fc and persistence blob 16b36397e7587099e0503214a91f8c5710df6a99.
- GitHub connector read of current main and commit metadata during 2026-10-17 ET research session.

## Observations and proof limits
1. Workflow-source change is CONFIRMED by fetched commit diff. The GitHub combined status endpoint returned zero statuses for a7f17de6d3993b6e5495bbb378353bfaf6481014. This is NOT proof that GitHub Actions passed or failed. Workflow run/job logs were not independently obtained.
2. The new runner unit test declares two methods: success/duplicate audit and failure classification/audit. This is a static source inspection, not an independently executed run. Do not claim a local or CI PASS here.
3. tests_support_prime.FakeConnection only stores a pending batch fingerprint and never persists or validates individual quote rows; it ignores the odds_quotes INSERT SQL. Thus the fake-DB passing tests could not prove that actual MotherDuck quote rows were persisted or that the production schema matches. This is a falsifiable coverage limitation, not an observed live failure.
4. The run_ingestion append-only audit uses a filesystem append with flush+fsync, but a DB commit followed by audit write failure can cause a committed batch without a corresponding audit record. This cross-system atomicity limitation merits explicit retry/reconciliation coverage before relying on the audit as complete evidence.
5. None of these source changes establish unattended EV Learning provenance. MD-EV-HANDOFF-001 remains UNVERIFIED pending independently attributable EV Learning run/commit evidence.
6. MODEL_SUSPECT and settlement-aware v2 gates remain unchanged; no bet, actual quote import, or live database operation was attempted.

## Next falsifiable checks
- Fetch actual GitHub Actions workflow run ID, conclusion, job step outputs and artifact SHA for the specific commit; separately reproduce all offline tests with exact fetched source files.
- Add a stateful fake that records each quote row and tests rollback, duplicate batch, failure between COMMIT and audit append, and reconciliation on retry.
- Run disposable DB schema integration tests with synthetic-only fixtures if an authenticated and approved test environment permits; assert both batch and quote row counts, foreign keys, constraints, and duplicate behavior.
- Do not claim unattended EV Learning output without schedule/run attribution, timestamp and source SHA. Do not publish raw private odds.
