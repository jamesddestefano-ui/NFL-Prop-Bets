# PRIME durable audit writer integration gap — 2026-10-17

Status: SOURCE-VERIFIED FINDING; CI EXECUTION UNVERIFIED; research only.

## Source and provenance
Authenticated GitHub main read, 2026-10-17 ET. Durable writer `scripts/prime_ingest_audit_db.py` blob `2bba9ad926a9e0cae10fc0a9116a3a493ccd68b1`; tests `tests/test_prime_ingest_audit_db.py` blob `713c55c94c050c339fdbe4624956480b1b4ee964`; workflow `.github/workflows/prime-ingest-e2e-validation.yml` blob `b74afcadca0a207a60d3f643fa3facb933d35b04`. Workflow change commit `7f08f2a857874e6e8a4db4f08a0020b28624b0b5`.

## Material review findings
1. The database audit writer is a separate function `persist_audit_event(connection,event)`; the reviewed existing `scripts/prime_ingest_runner.py` uses filesystem `append_audit`, not this database writer. Therefore the audit writer's existence does not by itself reconcile the prior database-commit/file-audit failure window. Integration and a post-commit failure-injection test are still necessary.
2. The audit event ID includes `observed_at_utc`. When `make_event` is called without a preserved timestamp, a retry gets a new timestamp and potentially a new ID even for the same status/attempt. `persist_audit_event` is idempotent for replay of the **same event object**, not automatically for logically equivalent regenerated attempts. Tests should explicitly exercise regenerated events and ensure original event timestamps/IDs are preserved.
3. GitHub Actions workflow source includes the new audit writer tests. Combined GitHub status endpoint for commit `7f08f2a857874e6e8a4db4f08a0020b28624b0b5` returned an empty statuses array. No passing job logs were inspected. CI outcome: UNVERIFIED.
4. This review is based on source inspection, not independently executed exact-source tests. No live data, keys, bets or database mutations were used.

## Bounded next tests
- Inject failure after a committed synthetic quote transaction but before audit-file append; confirm that the durable database audit event can be reconciled without altering the quote batch.
- Replay the same audit event after a simulated connection failure: expect one event row. Regenerate from identical logical fields with an omitted timestamp: document and test distinct IDs (or revise event identity prospectively with explicit attempt ID).
- Establish actual GitHub Actions run ID, conclusion and logs for this workflow. Run a disposable synthetic schema integration test with no live sportsbook data.
- Preserve original event/observation timestamps, no duplicate routine commits, MODEL_SUSPECT and v2 exact-contract safety gates.

No unattended EV Learning handoff provenance is implied by these commits.
