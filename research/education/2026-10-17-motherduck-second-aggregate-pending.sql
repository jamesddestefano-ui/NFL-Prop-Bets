-- PRIME audit aggregate v2 metadata import; prepared only, NOT EXECUTED here.
-- Private audit blob SHA: e9029101ef21a881fd14b4577c7c1e91ce37be06
-- Private source: jamesddestefano-ui/-NFL-Prop-Odds-Data
-- Source path: audits/20261017T003305490539Z-quality.json
-- REVIEW_REQUIRED status. No raw prices, player identities or wagers.
-- Apply to existing my_db.main.prime_audit_aggregates only with MotherDuck write authorization.
INSERT INTO main.prime_audit_aggregates
(run_id, private_audit_path, audit_git_blob_sha, private_source_path,
 event_count, quote_side_count, clean_pair_count, nonclean_group_count,
 duplicate_side_count, postkickoff_quote_count, invalid_timestamp_count,
 source_update_missing_count, audit_status, provenance_basis,
 nj_executable_verified, prospectively_screened_count, eligible_for_profitability_claim)
SELECT
 '20261017T003305490539Z',
 'audits/20261017T003305490539Z-quality.json',
 'e9029101ef21a881fd14b4577c7c1e91ce37be06',
 'data/odds_api/runs/20261017T003305490539Z.json',
 13, 2444, 1160, 124, 0, 0, 0, 0,
 'REVIEW_REQUIRED', 'PRIVATE_AUDIT_SUMMARY_REPORTED_NOT_INDEPENDENTLY_RECALCULATED',
 FALSE, NULL, FALSE
WHERE NOT EXISTS
 (SELECT 1 FROM main.prime_audit_aggregates WHERE run_id='20261017T003305490539Z');

-- Expected after execution: two run IDs, no duplicates, and no research-safety violations.
SELECT run_id, event_count, quote_side_count, clean_pair_count,
 nonclean_group_count, audit_status, nj_executable_verified,
 prospectively_screened_count, eligible_for_profitability_claim
FROM main.prime_audit_aggregates ORDER BY run_id;
SELECT COUNT(*) AS n, COUNT(DISTINCT run_id) AS distinct_runs,
 SUM(CASE WHEN nj_executable_verified OR eligible_for_profitability_claim
 OR prospectively_screened_count IS NOT NULL THEN 1 ELSE 0 END) AS guard_violations
FROM main.prime_audit_aggregates;
