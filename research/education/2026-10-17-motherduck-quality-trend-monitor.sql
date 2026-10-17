-- PRIME: read-only, reproducible audit quality trend monitor (2026-10-17).
-- Requires my_db.main.prime_audit_aggregates. No mutation, sportsbook prices or user tickets.
-- Coverage denominator is clean_pair_count + nonclean_group_count, NOT quote-side count.
-- A one-percentage-point decline is an operational watch threshold, not an EV gate.
WITH series AS (
 SELECT run_id, event_count, quote_side_count, clean_pair_count, nonclean_group_count,
        duplicate_side_count, postkickoff_quote_count, invalid_timestamp_count,
        source_update_missing_count, audit_status, audit_git_blob_sha,
        nj_executable_verified, prospectively_screened_count, eligible_for_profitability_claim,
        ROUND(100.0 * clean_pair_count / NULLIF(clean_pair_count + nonclean_group_count,0),2) AS coverage_pct,
        LAG(100.0 * clean_pair_count / NULLIF(clean_pair_count + nonclean_group_count,0))
          OVER (ORDER BY run_id) AS prior_coverage_pct
 FROM my_db.main.prime_audit_aggregates
)
SELECT run_id,event_count,quote_side_count,clean_pair_count,nonclean_group_count,
       coverage_pct,ROUND(coverage_pct-prior_coverage_pct,2) AS coverage_delta_pp,
       CASE WHEN audit_status <> 'REVIEW_REQUIRED'
                 OR nj_executable_verified OR eligible_for_profitability_claim
                 OR prospectively_screened_count IS NOT NULL
                 THEN 'REVIEW_METADATA_GUARD'
            WHEN duplicate_side_count > 0 OR postkickoff_quote_count > 0
                 OR invalid_timestamp_count > 0 OR source_update_missing_count > 0
                 THEN 'REVIEW_STRUCTURAL_ANOMALY'
            WHEN prior_coverage_pct IS NOT NULL AND coverage_pct < prior_coverage_pct - 1.0
                 THEN 'REVIEW_COVERAGE_DROP'
            WHEN nonclean_group_count > 0 THEN 'REVIEW_INCOMPLETE_PAIRS'
            ELSE 'NO_FLAG' END AS monitor_finding,
       audit_status,audit_git_blob_sha
FROM series ORDER BY run_id;

-- Assertions: expect 2 distinct rows, 0 provenance gaps, 0 flagged forbidden model claims.
SELECT COUNT(*) AS audit_rows,COUNT(DISTINCT run_id) AS unique_runs,
       SUM(CASE WHEN audit_git_blob_sha IS NULL OR LENGTH(audit_git_blob_sha)<>40 THEN 1 ELSE 0 END) AS provenance_gaps,
       SUM(CASE WHEN nj_executable_verified OR eligible_for_profitability_claim
                  OR prospectively_screened_count IS NOT NULL THEN 1 ELSE 0 END) AS claim_guard_violations
FROM my_db.main.prime_audit_aggregates;
