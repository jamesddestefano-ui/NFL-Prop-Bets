# MotherDuck schema reconciliation — 2026-10-17

Status: READ_ONLY_VERIFIED; NO IMPORT OR DDL EXECUTED. NFL player props only.

## Observed MotherDuck workspace
Database `my_db`: five original `main.prime_test_*` synthetic fixture tables and four newer `prime_research` tables: `odds_quotes`, `ingestion_batches`, `forecast_predictions`, `graded_outcomes`. Direct read-only SQL confirmed 0 rows in each of the four `prime_research` tables. No aggregate-only table named `prime_audit_aggregates` was present.

## Reconciliation finding
`prime_research.odds_quotes` is intended for individual quote rows, not audit summaries; `ingestion_batches` records ingestion metadata but its observed columns (batch_sha256, source_path, source_type, ingested_at_utc, record_count) cannot faithfully represent full clean-pair/duplicate/invalid-timestamp audit metrics. Therefore do NOT put the aggregate into `odds_quotes`, re-purpose `ingestion_batches`, or imply any existing production data. The staged migration in `research/education/2026-10-17-motherduck-aggregate-import-pending.sql` targets a distinct aggregate table; keep it PENDING, not deployed.

## Verified historical source, not recomputed
Private repo `jamesddestefano-ui/-NFL-Prop-Odds-Data`, `audits/20261016T212437180951Z-quality.json`, Git blob SHA `aeb40c29e6cb99e0220be83587f91d74eda42a77`. Historical audit reports 12 events, 2277 side quotes, 1079 clean pairs, 119 non-clean groups and REVIEW_REQUIRED. Do not treat 2277 quotes as 2277 prospective screened contracts or verified NJ executable offers. Newer private capture audit and independently recalculated aggregate remain pending.

## Next execution gates
1. Confirm database writer authorization through the proper user-mediated access route; do not bypass any declined access.
2. Recheck current schema before any eventual DDL; don't collide with concurrently created production tables.
3. If separately authorized, create one dedicated aggregate table in a clearly selected schema, then insert one historical aggregate report under immutable source run ID, preserving audit status and source Git SHA.
4. Verify exact row count and all metrics by read-only SQL; do not import raw prices, names or bets, create flights or schedules, or change canonical records.
5. Keep v2 settlement-aware EV and prospective pilot safeguards unchanged.

Sources: authenticated GitHub file reads for controlling `AGENTS.md`, `config/prime_ev_playbook_v2.md`, and staged migration; MotherDuck list_tables and read-only aggregate count query during this interaction. Actual write access not exercised.
