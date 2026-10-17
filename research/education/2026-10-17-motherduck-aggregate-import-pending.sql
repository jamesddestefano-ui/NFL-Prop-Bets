-- PRIME metadata-only MotherDuck import migration — NOT EXECUTED
-- Intended database: my_db
-- Historical private source: jamesddestefano-ui/-NFL-Prop-Odds-Data
-- audits/20261016T212437180951Z-quality.json, Git blob SHA aeb40c29e6cb99e0220be83587f91d74eda42a77
-- This snapshot has REVIEW_REQUIRED status; it is NOT a calibrated model, prospective screening,
-- verified NJ offer, or proof of profitable EV. Does not include player data, prices, or raw quotes.
-- Execute only after MotherDuck write authorization and separate approval.

CREATE TABLE IF NOT EXISTS prime_audit_aggregates (
  run_id VARCHAR PRIMARY KEY,
  private_audit_path VARCHAR NOT NULL,
  audit_git_blob_sha VARCHAR NOT NULL,
  private_source_path VARCHAR NOT NULL,
  event_count BIGINT NOT NULL,
  quote_side_count BIGINT NOT NULL,
  clean_pair_count BIGINT NOT NULL,
  nonclean_group_count BIGINT NOT NULL,
  duplicate_side_count BIGINT NOT NULL,
  postkickoff_quote_count BIGINT NOT NULL,
  invalid_timestamp_count BIGINT NOT NULL,
  source_update_missing_count BIGINT NOT NULL,
  audit_status VARCHAR NOT NULL,
  provenance_basis VARCHAR NOT NULL,
  nj_executable_verified BOOLEAN NOT NULL DEFAULT FALSE,
  prospectively_screened_count BIGINT,
  eligible_for_profitability_claim BOOLEAN NOT NULL DEFAULT FALSE,
  CHECK (quote_side_count >= clean_pair_count * 2),
  CHECK (event_count >= 0 AND clean_pair_count >= 0 AND nonclean_group_count >= 0),
  CHECK (nj_executable_verified = FALSE AND eligible_for_profitability_claim = FALSE)
);

INSERT INTO prime_audit_aggregates (
  run_id, private_audit_path, audit_git_blob_sha, private_source_path,
  event_count, quote_side_count, clean_pair_count, nonclean_group_count,
  duplicate_side_count, postkickoff_quote_count, invalid_timestamp_count,
  source_update_missing_count, audit_status, provenance_basis,
  nj_executable_verified, prospectively_screened_count, eligible_for_profitability_claim
)
SELECT
  '20261016T212437180951Z',
  'audits/20261016T212437180951Z-quality.json',
  'aeb40c29e6cb99e0220be83587f91d74eda42a77',
  'data/odds_api/runs/20261016T212437180951Z.json',
  12, 2277, 1079, 119, 0, 0, 0, 0,
  'REVIEW_REQUIRED', 'PRIVATE_AUDIT_SUMMARY_REPORTED_NOT_INDEPENDENTLY_RECALCULATED',
  FALSE, NULL, FALSE
WHERE NOT EXISTS (
 SELECT 1 FROM prime_audit_aggregates WHERE run_id='20261016T212437180951Z'
);

-- Expected one historical aggregate row; audit remains REVIEW_REQUIRED.
SELECT run_id, event_count, quote_side_count, clean_pair_count,
       nonclean_group_count, audit_status, nj_executable_verified,
       prospectively_screened_count, eligible_for_profitability_claim
FROM prime_audit_aggregates
WHERE run_id='20261016T212437180951Z';
