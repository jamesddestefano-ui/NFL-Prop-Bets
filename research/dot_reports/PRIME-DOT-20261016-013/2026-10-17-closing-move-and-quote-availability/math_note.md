# Task013: shared-baseline correlation is not incremental forecasting skill

All names, prices/probabilities, contracts, observations, and timestamps below are invented educational fixtures. No current quote, private data, placement, or betting recommendation is included. Python standard library only; exact rational arithmetic for all population moments and losses.

## 1. Eight-point counterexample

Take three independent equally likely signs: u = ±0.02, e = ±0.01, v = ±0.01. Give each of their eight combinations weight 1/8. Define initial market probability m0 = 0.5 + u, locked model probability a = 0.5 + e, and matched later-close probability mc = 0.5 + v. The probabilities are stipulated, not inferred from real odds.

| u | e | v | m0 | a | mc | a−m0 | mc−m0 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| −.02 | −.01 | −.01 | .48 | .49 | .49 | .01 | .01 |
| −.02 | −.01 | +.01 | .48 | .49 | .51 | .01 | .03 |
| −.02 | +.01 | −.01 | .48 | .51 | .49 | .03 | .01 |
| −.02 | +.01 | +.01 | .48 | .51 | .51 | .03 | .03 |
| +.02 | −.01 | −.01 | .52 | .49 | .49 | −.03 | −.03 |
| +.02 | −.01 | +.01 | .52 | .49 | .51 | −.03 | −.01 |
| +.02 | +.01 | −.01 | .52 | .51 | .49 | −.01 | −.03 |
| +.02 | +.01 | +.01 | .52 | .51 | .51 | −.01 | −.01 |

Let d = a−m0 = e−u and y = mc−m0 = v−u. Using population moments with denominator 8:

- Cov(d,y) = Cov(e−u,v−u) = Var(u) = 0.0004.
- Var(d) = Var(y) = 0.0001 + 0.0004 = 0.0005.
- Corr(d,y) = 0.0004/0.0005 = 0.8.
- a and mc are independent: every one of their four level pairs occurs twice. Zero covariance alone would not generally establish independence.

The common noisy subtracted baseline creates the association. In this population E[mc | a,m0] = 0.5; a adds no information about mc conditional on m0 and the known fixture distribution.

## 2. Use paired forecast-loss comparisons

For the same eight rows and weights, squared close-forecast loss L(f) = mean[(mc−f)²] is:

| Forecast | Exact mean loss | Decimal |
|---|---:|---:|
| Model a | 1/5000 | 0.0002 |
| No-change m0 | 1/2000 | 0.0005 |
| Predeclared constant 0.5 | 1/10000 | 0.0001 |

The model beats no-change by 0.0003 but loses to the constant by 0.0001. The constant is specified before the fixture; it is not estimated from held-out closes. Raw move correlation and beating no-change do not establish incremental intelligence beyond a simple competing forecast.

For any baseline b, the per-row paired improvement is

Δ(b) = (mc−b)² − (mc−a)² = (a−b)(2mc−a−b).

Positive means the model helps. With b=m0 this is 2dy−d². Its average is 2(0.0004)−0.0005 = 0.0003. With b=0.5 the average is −0.0001. Compare models on identical eligible rows and weights; averages from differently selected cohorts are not a paired comparison. Baselines, loss, exclusion rules, forecast version, and evaluation window should be fixed before observing the close. This fixture measures proximity to a later market quote, not outcome calibration, profit, causal skill, or true event probability.

## 3. Sparse checkpoints: availability, missingness, and continuity

At one prespecified checkpoint per attempted quote, 10 attempts yield 6 active, 2 inactive, and 2 unknown. Counting all attempted quotes, active prevalence is bounded by 6/10 = 0.6 and (6+2)/10 = 0.8. These are missing-status identification bounds for this finite cohort, not confidence intervals or estimates of uninterrupted survival. Treating all unknown as inactive gives the lower bound, not a known point estimate.

Complete-case 6/(6+2)=0.75 describes attempts with observed status. Applying it to all attempts requires an assumption about missingness that the fixture does not supply. A timeout is unknown, not evidence of inactivity. With zero attempts there is no prevalence estimate; with all unknown the bounds are [0,1] and complete-case is undefined.

“Active” must be defined in advance for the exact contract, side, price/stake requirement, book, and region. A displayed active quote is not proof a wager would be accepted. The flags here are assumed correct classifications at the prescribed checkpoint; asynchronous responses may require interval/uncertain timing instead.

Active → inactive → active refutes uninterrupted survival even if the quote returns at the final checkpoint. Active endpoints alone also cannot prove continuity: an always-active path and an unobserved interruption between endpoints generate the same recorded endpoints. Do not infer continuous tradability from sparse snapshots.

## 4. The game is the dependence cluster

Invent four game-level paired-loss differences +0.01, −0.01, +0.02, −0.02. Repeat each exact row 10 times. There are 40 rows but only four distinct games, and both means are zero. The naive row-level variance-of-the-mean estimate is 1/156000; the equal-game estimate is 1/12000, 13 times larger. Their standard errors are about 0.00253185 and 0.00912871 in loss units. Duplication adds no independent evidence.

The demonstration assumes independent games and perfect dependence among each game's duplicate rows. Four games are far too few to support a reliable asymptotic confidence claim. Real data can share dependence across games/dates/players; choose the dependence unit and weighting for the target estimand. Unequal replication can also change row-weighted means. Do not multiply confidence merely by retaining more same-game snapshots or alternate lines.

## 5. Timestamp and exact-contract guards

The executable valid fixture uses synthetic January 1, 2026 UTC times: forecast recorded 12:00:00, initial request 12:00:03–12:00:05, decision 12:00:10, close request 12:58:58–12:59:00, and kickoff 13:00:00. Exact observed close lag is 60 seconds. Both sides in a phase are assumed co-observed in that phase's response.

Guards require forecast recording strictly before the decision; request start no later than completion; initial response available by the decision; each request completed strictly before kickoff; and a later close request. A pre-kickoff request whose response arrives at/after kickoff fails. Timestamp equality is not “before.” Source timestamps and capture timestamps must be reliable; invented timestamps cannot establish real-world provenance.

Matching first requires known, nonempty event, participant, market, period, book, region, and settlement strings, a finite numeric threshold, and a side explicitly equal to “over” or “under.” Equality between missing values is never sufficient. Timestamp fields must be present, typed datetimes with time zones; lag fields must be finite nonnegative numbers. Matching then requires equality of event, participant, market, period, threshold, book, region, and settlement definition. The later close uses the original side; paired quotes must be the opposite side on the identical contract. A missing threshold remains unmatched; a different threshold, book, region, settlement, or side is rejected. There is no interpolation or substitute-line repair.

The actual kickoff-minus-completion lag must equal the stored lag exactly. This example additionally selects a prespecified 60-second target. That exact target is a fixture convention, not a universal definition of “close”; a real protocol may predeclare a window and retain each exact observed lag, never silently round it into a different checkpoint.

## Assumptions, limits, and reproducibility

This is a finite equally weighted counterexample, not empirical evidence that actual models lack skill. Independence, the known constant center, synthetic exact probabilities, correct checkpoint labels, faithful clocks, co-observed opposite sides, and game independence are explicit assumptions. No outcomes, fills, limits, costs, no-vig estimation, or data-integrity service are modeled. The guards demonstrate particular rejection rules, not a production validation system. They do not establish source freshness, authenticity, separately timed opposite-side observations, stable model provenance, request payload integrity, or actual book acceptance. The opposite sides' co-observation is an explicit input assumption. Review-driven regression tests cover the dangerous cases where all books or all sides are unknown; these cases now remain unmatched, as do missing/invalid thresholds and unsuitable timestamps.

Controls v2 are context only: standard American odds −150 through +150, central edge at least 4 percentage points, conservative EV at least zero, and no separate 5% ROI gate. These controls are not evaluated by the synthetic probability examples and create no recommendation.

Files: fixture_math.py computes the fixtures; test_fixture_math.py holds independent exact-value and negative-control tests; results.json records deterministic full outputs; verify.py reruns the full local suite, generates outputs in two fresh Python processes, checks their byte equality against results.json, checks independent artifact oracles, and verifies SHA256SUMS. SHA256SUMS covers the five named source/output files, excluding the manifest itself. The distributable math package contains those five files plus SHA256SUMS. The full local suite has 31 test methods, including parameterized malformed-input and contract-mismatch cases. Verification logs are kept outside the distributable package.

Run: python -B verify.py. No network or third-party dependencies are used.
