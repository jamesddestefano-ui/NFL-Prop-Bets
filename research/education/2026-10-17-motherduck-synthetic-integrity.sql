-- PRIME MotherDuck synthetic validation (read-only)
-- Database: my_db. Expected fixture: 2 runs, 7 quotes, 4 screens, 2 forecasts, 2 unsettled results.
-- NO raw sportsbook data, DDL/DML, authenticated wagers or scheduled jobs.
-- Test 1: expect groups_total=4, clean_pairs=1, duplicate_groups=1, missing_opposite_groups=2.
WITH g AS (
 SELECT run_id, bookmaker, player_key, market, threshold, settlement_rule,
 count(*) FILTER (WHERE side='Over') AS o,
 count(*) FILTER (WHERE side='Under') AS u
 FROM prime_test_contract_observations
 GROUP BY ALL
)
SELECT count(*) AS groups_total,
 sum(CASE WHEN o=1 AND u=1 THEN 1 ELSE 0 END) AS clean_pairs,
 sum(CASE WHEN o>1 OR u>1 THEN 1 ELSE 0 END) AS duplicate_groups,
 sum(CASE WHEN o=0 OR u=0 THEN 1 ELSE 0 END) AS missing_opposite_groups
FROM g;

-- Test 2: expect F1 central=0.10727 conservative=0.01182 pregame=true;
-- F2 central=0.02 conservative=0 pregame=false; both calibrated=false.
SELECT f.forecast_id,
 round(f.p_win * (CASE WHEN f.odds_american<0 THEN 1+100.0/abs(f.odds_american) ELSE 1+f.odds_american/100.0 END) + f.p_push - 1, 5) AS central_ev,
 round(f.p_conservative_win * (CASE WHEN f.odds_american<0 THEN 1+100.0/abs(f.odds_american) ELSE 1+f.odds_american/100.0 END) + f.p_push - 1, 5) AS conservative_ev,
 f.calibrated,
 r.response_received_utc < r.kickoff_utc AS pregame
FROM prime_test_frozen_forecasts f
JOIN prime_test_screened_cohort s USING(screen_id)
JOIN prime_test_capture_runs r ON s.run_id = r.run_id
ORDER BY f.forecast_id;

-- Test 3: expect 1 postkickoff run, 0 improperly scored rows, 0 non-synthetic/executable quotes.
SELECT (SELECT count(*) FROM prime_test_capture_runs WHERE response_received_utc>=kickoff_utc) AS postkickoff_runs,
(SELECT count(*) FROM prime_test_outcome_scores WHERE result='UNSETTLED' AND (brier IS NOT NULL OR matched_devig_clv IS NOT NULL)) AS improperly_scored,
(SELECT count(*) FROM prime_test_contract_observations WHERE source_type<>'SYNTHETIC' OR is_nj_executable) AS non_synthetic_or_executable;
