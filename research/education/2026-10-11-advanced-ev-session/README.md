# PRIME EV education: new evidence, available prices, and honest validation

October 11, 2026 · NFL player-prop education · Evening follow-on session

## The three takeaways

1. **Count information, not agreeing names.** Update a forecast only for evidence that is genuinely new to its existing information set. A role probability, a prop-hit probability, and a probability that the wager has action are different targets.
2. **An attractive published price is only the beginning.** Delay can selectively remove the best opportunities, and a good price available for a small amount does not price a larger allocation. Evaluate the exact contract at each available price tier.
3. **Validate the whole forecasting procedure.** A model can fit a selected feature of past data while missing the outcome distribution. Individually calibrated forecasts need not produce a calibrated average. Model fitting, combination, recalibration, and bet selection all belong inside the evaluation design.

These are new, reproducible extensions of the earlier session's exact-contract, source-dependence and calibration lessons. They do not establish calibrated NFL probabilities, a profitable strategy, or a current bet. The most useful next step is a frozen, timestamped research pilot, subject to review, rather than a new probability or stake rule.

## What was studied and checked

**EMPIRICAL EVIDENCE, limited to source/access observations.** Three core educational transcript sources were reviewed: Philippe Rigollet's MIT Bayesian statistics lecture, the Circles Off interview with Calvin and Hobo, and Jack Andrews's *5 Ways Pro Bettors Are Beating You*. Official written material from Aalto, CIRM and Berkeley adds model checking, model selection and calibration. Recordings located for written lectures were not counted as watched or as transcript reviews.

The [source register](source-register.md) distinguishes transcript reading, caption checks, written teaching material and recording metadata; it preserves dates, review windows, commercial ties and unresolved discrepancies. No continuous video-playback duration is claimed. An [optional risk supplement](risk-supplement.md) adds two further transcript reviews and primary papers on portfolio dependence, growth objectives and model uncertainty; its [separate register](risk-sources.md) preserves their access details. A [market-reference supplement](market-reference-supplement.md) adds one focused Circles Off transcript review and a primary-paper audit, demonstrating how de-vig assumptions can reverse an apparent edge.

The [worked appendix](worked-appendix.md) provides five substantial invented examples, compact settlement/formula guards, exact fractions and derivations. Its [standard-library script](verify_new_lessons.py) passes 68 named arithmetic checks; [outputs](new_lesson_results.json) are preserved. An [independent SciPy cross-check](crosscheck_scipy.py) passes 14 additional comparisons, with [separate outputs](crosscheck_scipy.json). The [verification manifest](verification-manifest.json) records reproduction, links and file hashes. These are synthetic consistency checks, not tests of a production PRIME engine or an empirical NFL model.

### Evidence language

- **VERIFIED MATHEMATICAL PRINCIPLE:** an identity or counterexample under its stated assumptions.
- **MODEL ASSUMPTION:** supplied probabilities, distributions, dependence, settlement terms or opportunity constraints.
- **EMPIRICAL EVIDENCE:** an observed record or measured finding, with population and access limits. Here source/access observations are not empirical NFL-performance evidence.
- **ANALYST OPINION:** an interpretation, self-report or commercial claim without an independently checked relevant dataset.
- **UNTESTED HYPOTHESIS:** a proposed improvement awaiting time-appropriate data and evaluation.

The repository's existing information taxonomy still applies. None of these labels turns a source claim into a verified current market quote.

## Lesson 1: update for genuinely new information, on the right probability target

### A second publisher is not necessarily a second observation

**VERIFIED MATHEMATICAL PRINCIPLE.** Bayesian updating multiplies prior odds by a likelihood ratio. For a second report, the likelihood ratio must condition on the first report and all information already used. A deterministic copy of a report already observed contributes a conditional ratio of one. The result follows from [MIT's odds-form teaching notes](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_class12-prep-b.pdf); the football application is our own construction.

In the invented reception example, a WR has either eight or six targets, with independent catch probability .65 per target. Both role states involve playing. A prior 40% chance of the high-target role and an assumed report likelihood of .75 in that role versus .25 otherwise produce:

| Information treatment | Chance of high role | Chance of Over 4.5 receptions | Modeled ROI at −110 |
|---|---:|---:|---:|
| Before the report | 40.00% | 47.40% | −9.51% |
| One report, or that report plus an exact copy | 66.67% | 57.73% | +10.21% |
| Copy wrongly treated as independent | 85.71% | 65.11% | +24.29% |

The headline, role state and prop event are separate objects. After updating the role weights, average each role's probability of clearing the **same offered threshold**. Do not average the role-specific fair lines: the appendix gives an exact counterexample where their midpoint is not the mixture's 50% line.

**MODEL ASSUMPTION.** The .75/.25 report likelihoods, target counts, catch rate and within-role stability are invented. A health report could change conversion or exit risk as well as the role weights. A downside role weight of .50 gives only a 51.27% prop probability and −2.11% ROI at −110. That weight is a stress case, not a validated lower bound. The central arithmetic does not clear the remaining PRIME uncertainty and role gates.

### Avoid counting information already in the market

**VERIFIED MATHEMATICAL PRINCIPLE**, conditional on a specified information model. If a forecast already includes report E, applying E's original likelihood ratio again double-counts it. This can also happen when the starting forecast is market-derived and the market already reflects the news. A market price is not directly a probability of a high-role state; a model must connect those quantities. Preserve the forecast's information cutoff and the report's original lineage. Distinct authors alone cannot establish independence.

### Eligibility is part of the forecast target

**VERIFIED MATHEMATICAL PRINCIPLE / MODEL ASSUMPTION**, under a fictional contract. Suppose a separate fixture has an 80% chance of action, full refund when inactive, and a 57.73% win probability conditional on action. At −110, modeled ROI is +10.21% per active unit but +8.17% per posted unit. Treating void probability as losing probability instead produces −11.83%.

That refund clause is invented, not a verified sportsbook rule. Actual participation, early-exit, push and void clauses determine the target and denominator. Evaluate action eligibility separately from conditional performance; preserve all settlement states before any conditional scoring.

**PRIME challenge: MODEL_UNCERTAINTY / UNVERIFIED_CLAIM.** What evidence estimates the report's incremental likelihood after existing public information? What is the exact settlement-eligible target? Resolve with original-source lineage, a predeclared role definition, timestamped comparable cases including wrong reports, and later outcomes. Bayes' rule cannot supply the missing likelihoods.

### One complete hypothetical evaluation card

**VERIFIED MATHEMATICAL PRINCIPLE / MODEL ASSUMPTION.** This card returns to the original **active-WR, no-push/no-void** Over 4.5 fixture. “Fictional Book A” offers Over −110 and Under −110 at the same invented snapshot t0. No real book, timestamp, available quote or fill is represented. The matching Under is introduced only to demonstrate a complete two-sided no-vig calculation.

| Field | Hypothetical value |
|---|---|
| Exact contract | Active WR, Over 4.5 receptions; both role states play |
| Offered decimal / raw break-even probability | 1.90909091 / 52.38095238% |
| Same-book two-sided no-vig Over | 50.0000%, using proportional normalization of the two −110 implied probabilities |
| Raw/central model probability | 57.72929314%, from the explicit role mixture; uncalibrated |
| Calibrated/shrunk PRIME probability | Not established by this synthetic example |
| Assumption-only adverse probability | 51.27396790%, using .50 high-role weight; not a confidence bound |
| Central edge versus offered break-even | +5.34834076 percentage points |
| Central difference versus no-vig benchmark | +7.72929314 percentage points; a distinct comparison |
| Central / adverse modeled ROI at −110 | +10.21046872% / −2.11333401% |
| Central zero-EV boundary | Decimal 1.73222284, equivalent to American −136.57045 |
| Adverse zero-EV boundary | Decimal 1.95030742, equivalent to American −105.22911 |
| Operational play-to line / maximum juice | Not established; no live playable line or price exists until market, role, calibration, uncertainty and exposure gates clear |

Equality at either arithmetic boundary means zero EV, not positive EV. Holding this same probability and contract fixed, the adverse case gives +.10631828% at whole-number −105 but −.35436427% at −106. Those are break-even calculations, not permission to bet or evidence that all gates pass. The −110 example fails its supplied adverse-EV condition. The fictitious no-vig number is a market-model assumption, not verified truth. [Exact card outputs](evaluation_card_verified.json) and the [11-check verifier](verify_evaluation_card.py) preserve the inputs and boundaries.

## Lesson 2: measure the opportunity that remains available

The Circles Off interview describes followers missing favorable prices; Unabated discusses small-capacity quotes and timing. These are **ANALYST OPINION / UNTESTED HYPOTHESIS**, not independently verified NFL execution results. Their value here is to motivate falsifiable measurements.

### Missingness can change the opportunity mix

**VERIFIED MATHEMATICAL PRINCIPLE**, demonstrated by an original invented counterexample. Imagine 100 one-unit research opportunities: 20 with modeled ROI 12% and 80 with 2%. Their average is 4%. If the best 20 disappear before detection, the available set averages 2%, with 1.6 modeled profit units per original 100 opportunities. If exactly 20 disappear uniformly at random, expected ROI among the remaining 80 stays 4%, with 3.2 modeled profit units.

This does not count a missing opportunity as a losing wager. It shows why an original-price record cannot establish attainable performance, and why one overall availability percentage may hide selective loss of the most favorable prices.

### Size and price must stay together

**VERIFIED MATHEMATICAL PRINCIPLE**, demonstrated by an original invented counterexample. Assume the same contract offers 10 illustrative currency units at +110 and another 90 at −125. At assumed win probability .55, the first price has +15.5% modeled ROI. The full 100-unit allocation has effective decimal odds 1.83 and only +0.65% ROI. At probability .52, it is −4.84%.

The −125 increment by itself has −1% ROI at .55. Nothing in this example calls for filling a desired amount at the worse price. Every proposed increment still needs its own complete gate. Capacity, quotes and fills were invented, not observed.

Even without size limits, repricing can reverse the sign: the lesson-1 probability gives +10.21% ROI at stale −110, but −1.86% at hypothetical later decimal odds 1.70. If the line changes too, recompute the event probability.

**PRIME challenge: PRICE_CONFLICT / METHODOLOGY_CHALLENGE.** Preserve original publication, first detection, verification and any accepted-fill timestamps separately. Keep exact contract, observable size, suspension/rejection, changed prices and missingness. A verified available quote is still not proof of a fill. Test reference quality by market and timing; neither a universal “sharp book” label nor a universal pre-close cutoff is established here.

## Lesson 3: check the model's weaknesses, then test forecasts on unseen outcomes

### Fitting a mean does not test the relevant tail

**VERIFIED MATHEMATICAL PRINCIPLE**, demonstrated by an original invented counterexample. Invent 100 reception counts, half zero and half ten. A homogeneous Poisson model with Gamma(1, rate 1) prior yields Gamma(501, rate 101) posterior. Its predictive mean is 4.9604, close to the observed five. The posterior probability that a replicated 100-case mean is at least five is about .450, so that chosen diagnostic looks ordinary.

But the model predicts a zero fraction of only .00718 against the observed .50. The appendix's shared-parameter-aware bound for at least 50 replicated zeros is less than 3.18 × 10^−59. The model plainly misses an important feature even though the mean check is unremarkable. This deliberately extreme construction does not establish that Poisson models always fail for receptions.

**VERIFIED MATHEMATICAL PRINCIPLE.** Predictive checks compare replicated data with relevant features of the observed data. Their tail statistics are not generally classical uniformly calibrated p-values, nor probabilities that the model is true. [Stan's guide](https://mc-stan.org/docs/stan-users-guide/posterior-predictive-checks.html) and Aalto's model-checking material explain the distinction. Check zeros, dispersion, tails, role groups and dependence that matter to the proposed contracts; then evaluate genuine later predictions separately.

### Combining calibrated forecasts creates a new object to evaluate

**VERIFIED MATHEMATICAL PRINCIPLE**, demonstrated by an original invented counterexample. In an invented balanced population, each signal has sensitivity .80 and specificity .80, and the two signals are independent **conditional on the outcome**. Each individual forecast is calibrated at .80 after a positive signal and .20 after a negative one. When both signals are positive, the equal average is .80 but the correct joint-model probability is 16/17, about .9412. If one signal merely copies the other, the correct probability stays .80.

Averaging still improves expected Brier loss in this construction, from .1600 to .1312; the correctly fused forecast gives .11765. The lesson is not that averaging is bad. It is that improved overall score, component calibration and ensemble calibration are different claims. [Berkeley's calibration notes](https://www.stat.berkeley.edu/~ryantibs/statlearn-s23/lectures/calibration.pdf) give the relevant definitions and aggregation discussion.

### Evaluate the entire procedure without reuse of the test answers

**ANALYST OPINION / UNTESTED HYPOTHESIS.** Separate four questions:

1. Does the code correctly compute the stipulated model?
2. Does that model reproduce important observed features?
3. Do forecasts made without later outcomes predict those outcomes well?
4. Does the frozen decision policy work at verified executable prices and settlement rules?

Passing one does not establish the next. Simulation-based calibration concerns inference under simulated data from the assumed model; it is not empirical NFL forecast calibration.

Fit the base model, choose inputs and weights, fit recalibration and select thresholds using only the training side of each outer evaluation. Train calibration/combination on time-appropriate out-of-sample component forecasts within that training side, or on a legitimate held-out calibration segment, then evaluate the locked procedure on the outer test. In a compact appendix fixture, a fitted binwise calibration map has zero displayed calibration error on its own fitting data, then worse Brier on later invented data (.34 versus .26 for the raw forecasts). This falsifies the inference that a perfect fitted display proves later calibration; it does not show that recalibration generally harms.

For a next-game execution replay, use a timestamp-respecting rolling origin and keep related player/game outcomes together in the uncertainty analysis. Predicting a new player, a new role and another game for a known player are different tasks. Other model-selection partitions can answer different questions; this report does not claim chronological splitting is universally optimal for every statistical task.

**PRIME challenge: METHODOLOGY_CHALLENGE.** Evaluate the frozen combined forecast and selected subset, not only its ingredients. Retain all eligible predictions, sample counts, missingness, paired baselines and failed variants. A large ensemble weight is neither a probability that its model is true nor proof of source independence.

## Proposed tests, with clear failure conditions

These refine the earlier T2 probability-validation and T3 benchmark proposals. They are not installed rules or scheduled jobs. See [the detailed protocol](test-proposals.md).

| Proposal | Required evidence | What would count against it |
|---|---|---|
| Incremental news updating | Frozen information cutoffs, original/repost lineage, role labels and exact-contract forecasts | No later paired-score improvement over unchanged prior and contemporaneous market baseline; or updates cannot be reconstructed without future information |
| Price-disappearance selection | Full candidate cohort, fixed observation delays, quote and missingness states | Apparent advantage disappears after accessible-price and coverage controls; missingness explanation remains unidentified |
| Capacity-aware evaluation | Same-contract verified price/size tiers, separate accepted-fill evidence if present | A worse tier is accepted because a tiny favorable tier lifts the average; incompatible contracts or unavailable sizes are combined |
| Model-check and validation separation | Deliberate synthetic failure fixtures, frozen outer splits, full fitting/recalibration history | Mean-only check misses the designed shape failure; held-out outcomes influence any fitted choice |
| Ensemble and eligibility evaluation | Exact frozen combination, later settlements, action/push/void labels and source families | Claimed gain is absent on identical later cases, poorly calibrated in the target group, or depends on double-counted sources or wrong eligibility denominators |

Before interpreting an empirical comparison, prespecify a practically meaningful improvement, uncertainty method and observation horizon. No favorable threshold, sample size or stopping rule is chosen after seeing results. Sparse or missing data can make a result inconclusive rather than a success or a failure.

## What remains unresolved

- No report-likelihood model, uncertainty region, source ranking, NFL distribution or ensemble has been validated here.
- A conservative endpoint depends on the supplied joint uncertainty set. The appendix shows that two joint scenarios, a componentwise stress and a rectangular envelope can give different signs; none has demonstrated coverage.
- Betting educators' timing, liquidity and profitability claims remain scoped opinions or self-reports. Academic teaching supplies methods, not an NFL advantage.
- The earlier data-feasibility findings remain in the [prior report](../2026-10-11T20-19-00Z-session/README.md). This session neither re-audits nor repairs those records.

## Governance and preservation

The drafting baseline was `main` at `06f5e1f08f13ef886087eff58cccc7b28fb5a5e6`. Fresh reads covered [AGENTS](../../../AGENTS.md), [methodology](../../../config/methodology.md), [advanced market learning](../../../config/advanced_market_learning.md), [positive EV](../../../config/positive_ev_framework.md), [account accountability](../../../config/ev_account_accountability.md), [daily education](../../../config/ev_daily_education_directive.md), [sources](../../../config/sources.md), the existing education index and earlier reports.

This package is educational research for review. Controlling files, decision thresholds, bankroll policy, ledgers, historical results and prior reports are unchanged. It contains public educational sources, public repository governance and invented examples only. Its presence in the repository does not establish adoption by another workflow.
