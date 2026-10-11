# Review-only test protocols

These proposals refine the existing T2 exact-threshold forecast and T3 reference-quality studies. They do not change controlling policy, create a monitoring job, authorize data repairs, or initiate wagering. No empirical test below has run. All completed tests are explicitly synthetic and live in the accompanying calculator.

## Common design, before collecting or evaluating outcomes

1. **Define the target.** Identify player/game, statistic, exact threshold, side, settlement rules and forecast cutoff. Keep win, loss, push and void states before producing any conditional target. State whether the task is action eligibility, performance given action, or the full settlement vector.
2. **Define the cohort.** Prespecify candidate inclusion, primary checkpoint and quote age; retain serious passes, disappeared opportunities and missing outcomes. Repeated quotes do not create new independent player-game outcomes. Alternate contracts remain distinct but dependent.
3. **Freeze the procedure.** Fix features, role definitions, source families, update logic, calibrator, combination method, selection rule, comparison baselines, test horizon and a meaningful improvement criterion before the final outcomes are inspected. Record deviations rather than silently changing the test.
4. **Separate fitting from evaluation.** At each outer forecasting origin, all tuning and recalibration use only information available before that origin. Generate calibration/combination training forecasts without using each case’s outcome in its component-model fit, respecting forecasting time order and related-outcome groups; a legitimate held-out calibration segment is another option. This limits train/deployment mismatch; an untouched outer test is still needed to evaluate the full procedure. Keep a trace sufficient to reconstruct every forecast. Evaluating several variants and choosing the best on a final test consumes that test; subsequent claims need another untouched evaluation.
5. **Report evidence honestly.** Give paired score differences on identical eligible cases, denominators and missingness, reliability with counts, and uncertainty using a justified player/game/time dependence structure. Report all forecasts and the frozen selected subset. The raw count of quotes is not the effective sample size.
6. **Keep three performance objects separate.** Forecast scores concern probabilities; CLV concerns a specified later reference; realized return concerns settled wagers at actual terms. Hypothetical quote-based return is neither a fill nor user performance. A missing close is unmeasured rather than zero.

Sparse evidence may leave a test inconclusive. A point estimate of improvement is not an automatic pass. A calibrated uncertainty interval, desired detectable effect and data requirement must be justified rather than invented from today's fixtures.

## A. Incremental news updating

**Hypothesis:** a provenance-aware role/news update improves future exact-contract forecasts beyond an unchanged prior and the contemporaneous market benchmark.

**Evidence needed:** original report URL/author; report and retrieval timestamps; original/repost/unclear status; pre-report information set; role definition; report wording/class; role-state outcomes; exact-contract probabilities before and after; comparable cases across correct and incorrect reports and both role states. Record the no-report process when it is part of the model. Do not estimate likelihood ratios from highlighted successes only.

**Procedure:** estimate report likelihoods on past cases, carrying uncertainty; lock before later cases. Compute the posterior on the same prior information set. Compare no update, one legitimate incremental update, and an intentionally duplicated-input fixture. Evaluate role-state and prop-event forecasts separately. A current market-derived forecast may already contain the report, so use a distinct incremental comparison rather than treating market and news as independent sources.

**Completed synthetic checks:** exact copy leaves posterior unchanged; conditional likelihood ratio 1.5 gives a different result from a repeated unconditional ratio of three; impossible conditioning event is rejected; role mixtures equal joint-probability enumeration; same-threshold tails are monotone.

**Failure/inconclusive conditions:** duplicated evidence changes the answer; likelihoods cannot be reconstructed from pre-outcome records; wrong cases disappear from the denominator; no later paired improvement of meaningful size; uncertainty is too broad to distinguish the methods. A useful news source can still fail to add information beyond the market.

**Boundary:** role labels based solely on realized targets can confuse role with game script. More operational route/snap labels also require a documented measurement process. Independence is not established by different publisher names.

## B. Opportunity loss by delay and original edge

**Hypothesis:** favorable opportunities disappear nonrandomly, so original-price performance overstates the opportunity set available at later detection.

**Evidence needed:** the whole prespecified candidate cohort; source-time quote and timestamp; first detection and verification times; quote changes, suspension, rejection and missingness; exact matched contract; provider time versus local observation time and clock uncertainty. Original edge must be computed by a frozen model at that original cutoff, not using the later outcome.

**Procedure:** prespecify lag and original-edge groups; report coverage, sign reversals, remaining modeled EV and opportunity counts at each observation delay. Compare a fixed reference panel separately from changing available-book coverage. Keep all missing-at-detection opportunities in cohort denominators without scoring them as losing bets.

**Completed synthetic check:** removing the best 20 of 100 opportunities lowers remaining modeled ROI from 4% to 2%; removing exactly 20 uniformly at random preserves 4% in expectation. This establishes possibility, not observed NFL selection.

**Failure/inconclusive conditions:** apparent edge vanishes at verifiable available terms; source-time quotes cannot be verified; delay is confounded with different markets or news and the proposed explanation is unidentified. An observational association does not by itself establish that delay caused the change.

## C. Capacity-aware arithmetic and reference reliability

**Hypothesis:** keeping each same-contract price tier and its observable capacity avoids overstating value from a favorable headline quote; reference usefulness varies with market, timing and coverage.

**Evidence needed:** exact compatible contract, price, time, fees if applicable and observable size at each tier. Accepted amount and execution price require separate evidence; a screen limit is not a guarantee of a fill. Preserve all reference quotes and predeclared fallback choices.

**Procedure:** calculate incremental and aggregate payoff consistently. Evaluate each tier against all existing gates before any proposed allocation; preserve correlation/exposure constraints. Compare predeclared pre-close and closing references on identical later settlements as well as later price agreement. Do not choose a favorable reference after the outcome.

**Completed synthetic checks:** payoff-state enumeration equals weighted ROI; a favorable 10-unit tier plus unfavorable 90-unit tier cannot inherit the headline ROI; later repricing can reverse EV at unchanged probability.

**Failure conditions:** incompatible thresholds, settlement terms or times are pooled; capacity is inferred without evidence; an adverse marginal tier passes because of an attractive average; a benchmark is judged solely by agreement with another copied price. Any account-specific evidence needed for future work must be obtained through an authorized route.

## D. Diagnostic sensitivity and complete-procedure validation

**Hypothesis:** diagnostics aimed at plausible weaknesses detect failures that fitting-statistic checks miss, while a frozen full procedure earns better future scores than the baseline.

**Evidence needed:** model definition, prior, computational diagnostics, prediction task, retained fitting/tuning records, calibration data, outer split boundaries, later outcomes and reproducible forecast timestamps.

**Procedure:** first require code to detect deliberately wrong synthetic distributions. Use prior predictive checks for implausible opportunity allocations, then fitted predictive checks for zeros, dispersion, tails and relevant groups. Separately run a next-game replay with fitting, feature selection, weighting and recalibration entirely inside each training side. Group or otherwise account for related game/player outcomes when estimating uncertainty. New-player and new-role performance require separate generalization designs.

**Completed synthetic checks:** a Gamma–Poisson mean diagnostic is ordinary while zero frequency is grossly wrong; a perfectly fitted calibration map can fail later; predictive mixture density is averaged before the logarithm; the uniform-prior Bernoulli posterior denominator is n+2.

**Failure conditions:** checking only an already fitted mean misses the deliberate failure; test outcomes affect a model choice; a fitted reliability chart is called validation; simulation-based calibration is called evidence that NFL assumptions are true. Passing computational diagnostics is necessary for credible inference, not proof of forecasting skill.

**Current-method boundary:** historical PSIS guidance must be checked against current documentation and sample-size/effective-sample-size diagnostics. Approximate leave-one-out reliability does not settle the correct prediction unit. Rolling-origin replay prevents future information in the operational experiment; it is not claimed universally optimal for every model-selection question.

## E. Frozen ensemble and settlement-eligible calibration

**Hypothesis:** a specific combined/recalibrated forecast improves future probability quality on the intended settlement target, including the selected opportunities.

**Evidence needed:** component forecasts with shared-input provenance; fixed weights or training-only combination procedure; untouched later cases; complete win/loss/push/void outcomes; predeclared action, role and selection strata.

**Procedure:** compare components, exact pool and locked recalibration on the same eligible observations. Assess proper scores and calibration separately, including full probability-range coverage and counts. Evaluate action probability on the action cohort definition and conditional hit probability among the prespecified eligible settlements. Use full-vector scores when forecasting all settlement states. Never turn voids into losses or drop injury-affected valid losses after the result.

**Completed synthetic checks:** calibrated components can have a miscalibrated average despite improved Brier; independent and copied signals yield different joint probabilities; fictional refunded inactivity changes posted-stake EV but does not become a loss.

**Failure/inconclusive conditions:** aggregate calibration is inferred from component calibration; large weights are interpreted as source-truth probabilities; results rely on denominator changes; selected-group calibration worsens without disclosure; improvement is absent or too uncertain on identical later cases. Removing a source family is a sensitivity analysis, not an automatic cure or proof of causality.

## Review status

### Candidate data routes, not acquired datasets

**EMPIRICAL EVIDENCE, provider-documentation observations only.** The [nflreadr schedule](https://nflreadr.nflverse.com/articles/nflverse_data_schedule.html) says FTN participation from 2023 onward is released after the postseason, not in-season. Its [participation dictionary](https://nflreadr.nflverse.com/articles/dictionary_participation.html) defines the route field for the primary receiver. That field alone cannot supply current-week all-player route/TPRR denominators. Preserve original input snapshots and later corrections; the schedule recommends Wednesday-night/Thursday refreshes for corrected play-by-play.

The Odds API [advertises historical additional/player-prop markets](https://the-odds-api.com/historical-odds-data/) from May 3, 2023, five-minute snapshots, paid access and per-event queries, returning the nearest snapshot at or before the requested time. Sport/book/market coverage begins only when added. [NFL receptions and receiving yards are listed](https://the-odds-api.com/sports-odds-data/betting-markets.html). These are provider claims, not verified contract coverage, executable quotes or acquired API data. A one-game coverage audit would precede a panel. No subscription, purchase, account setup or implementation is authorized by this proposal.

Arithmetic and deliberately constructed failure cases: completed and reproducible. Empirical NFL likelihood estimation, execution/availability study, model comparison, ensemble calibration and settlement-scoring pilot: proposed only. Existing T1–T4 status remains unchanged except for these additional educational fixtures and design refinements.
