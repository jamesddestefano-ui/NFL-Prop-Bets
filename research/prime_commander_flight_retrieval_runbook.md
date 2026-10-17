# PRIME Commander — Flight retrieval runbook

Flight ID: `17b71f7e-0782-4cf6-95d6-2fbf7e066ea4`.

To evaluate ingestion health, Commander (or its authorized operator) must:

1. Query MotherDuck Flight runs for the ID above, sorted newest first.
2. Use the latest run, even if it is failed or pending; do not silently fall back to an older successful run.
3. Fetch logs for that exact run number.
4. Evaluate run metadata and logs using `scripts/prime_commander_flight_adapter.py` and `scripts/prime_commander_health_contract.py`.
5. Mark `UNKNOWN` for stale, incomplete, missing, or unsuccessful runs; `REVIEW_REQUIRED` for findings; `PASS` only when all synthetic checks pass.
6. Preserve run ID, observed time, and source references in the Commander report. Never label synthetic PASS as live market readiness.

**Retrieval limitation:** The connected MotherDuck tools can list runs and fetch logs during an authorized Commander execution, but the current GitHub code cannot invoke those connected tools automatically. This document is a retrieval contract, not a claim of unattended cross-platform integration.

Last verified source: MotherDuck Flight run #1, completed 2026-10-17T15:02:49Z, report PASS. This historical result must not be treated as fresh on subsequent runs.

The Flight has no schedule. A recurring Commander task would need to explicitly retrieve the latest run, and a separate cadence would be needed to produce fresh reports.
