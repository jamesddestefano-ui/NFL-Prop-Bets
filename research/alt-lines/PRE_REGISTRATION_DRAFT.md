# B18 pre-registration — DRAFT, not approved

Owner: James. Target approval: Friday, November 6, 2026.
Status: NOT APPROVED; no live betting eligibility; not official PRIME.

## Frozen scope (proposed)
- Receiving yards, receptions, rushing yards, with corresponding alternate ladders.
- Seven predeclared sportsbooks, three base and three alternate markets.
- Snapshot windows: manual Sunday/Thursday/Monday freeze, then T−30/T−15/T−5. Timezone: America/New_York for freeze; kickoff-relative closes use authoritative UTC kickoff.
- Isolated price capture; Nov 1 is a non-scored dry run.

## Modeling hypotheses (to be implemented/reviewed)
- Fit a single monotone market-anchored outcome CDF per player / market.
- Reconcile both sides and their vig; don't equate main-line threshold to median without interpolation.
- Estimate distribution shape from prior nflverse observations, shrink role/position distributions toward player evidence.
- Candidate distributions: discrete count overdispersion for receptions; zero-inflated positive skew for yards.
- Bootstrap entire modeling pipeline, using lower confidence-bound win probability `p_low`, including parameter and missingness uncertainty.
- Rank by conservative expected return per dollar; pass unless conservative ROI is greater than +5%.
- One rung per player; exposure rules and max quarter-Kelly stake apply only if separately authorized.
- No post-outcome edits to forecasts or frozen assumptions.

## Prospective evaluation / adoption gate (proposed, requires numeric calibration bound)
- Predeclare shape parameters, training cutoff, transformations, and missing-market treatment.
- Use season 2025 time-ordered out-of-sample replay only if no tuning leakage.
- Run 8–10 weeks prospective without official PRIME inclusion.
- Primary process measure: alternate-line CLV at identical threshold, vig-aware and game-clustered CI.
- Secondary: calibration, missingness, realized results, and selection-versus-pass rates.
- Adopt only if positive CLV with game-clustered confidence interval lower bound > 0, calibration below predeclared tolerance, adequate market coverage, and no protocol exceptions.
- Report every screened rung, rejection, estimated probability, uncertainty, and missing quote.

## Approval checklist
- [ ] Read controlling Claude artifact and B18 plan entry
- [ ] Approve seven bookmaker keys and API request/credit budget
- [ ] Approve exact freeze definition and capture coverage
- [ ] Approve bootstrap coverage level / calibration threshold and validation sample
- [ ] Approve model family and drift handling
- [ ] Approve signing / immutable freeze mechanism
- [ ] James signs and dates before any prospective scored research
