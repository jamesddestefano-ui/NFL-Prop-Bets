# PRIME Commander — Ingestion health handoff

## Authoritative source

MotherDuck Flight: `PRIME Ingestion Health Report Read Only`
Flight ID: `17b71f7e-0782-4cf6-95d6-2fbf7e066ea4`
Database: `my_db`
Mode: `SYNTHETIC_TEST_ONLY`
Schedule: **none (on-demand)**.

The Flight checks the live MotherDuck synthetic research tables and prints one machine-readable log line prefixed `PRIME_HEALTH_REPORT=`. Commander must fetch the **latest completed Flight run and its logs** before treating a report as current. Never use the dated example below as current state.

Last verified run: #1, 2026-10-17T15:02:49Z, status `SUCCEEDED`, exit code 0, report `PASS`.

## Fail-closed consumption contract

1. Verify the run is `SUCCEEDED` and exit code `0`.
2. Parse the `PRIME_HEALTH_REPORT=` JSON from the same run's logs. Reject absent, malformed, or multiple conflicting report lines.
3. Require `mode=SYNTHETIC_TEST_ONLY`, `database_writes=0`, `automatic_reimports=0`, and all integrity, reconciliation, orphan-audit, and recovery statuses `PASS`.
4. If run is stale, missing, failed, or reports `REVIEW_REQUIRED`, mark health `UNKNOWN` or `REVIEW_REQUIRED` respectively. Never infer `PASS` from prior successful runs.
5. Distinguish synthetic-data health from live production readiness. This Flight does **not** validate real sportsbook prices, quote executability, model profitability, or API collection freshness.
6. Never place bets, retry imports, modify authoritative ledgers, or mutate MotherDuck in response to the health report.
7. Record run number, timestamp, GitHub commit, observed metrics, and the source run link when publishing a Commander summary.

## Known gaps

The Flight is not scheduled and does not push reports to GitHub or Commander automatically. The handoff is a documented read contract, not a new autonomous agent integration. Adding persistent snapshots, alerts, or a schedule requires separate implementation and validation.
