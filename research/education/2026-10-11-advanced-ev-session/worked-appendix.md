# Five checks for role news and executable EV

Prepared October 11, 2026. Educational arithmetic using invented NFL inputs only.

## Evidence classification

Each calculation below is a **VERIFIED MATHEMATICAL PRINCIPLE** under explicit **MODEL ASSUMPTION** inputs. No new **EMPIRICAL EVIDENCE** of NFL forecasting or betting performance is supplied. Source interpretations are **ANALYST OPINION** where not mathematical; proposed empirical applications remain **UNTESTED HYPOTHESIS**. Source/access observations are separately scoped in the registers.

## Main result

A coherent Bayesian update can still have unjustified inputs. A copied report supplies no new evidence. A current market forecast may already contain the report. A favorable old price may have negative modeled EV at the price available later. Individually calibrated forecasts can also produce a miscalibrated average.

These examples turn those statements into reproducible counterexamples. They do not estimate any player's chances, validate source skill, establish an executable opportunity, recommend a wager, or change PRIME's rules. None of the synthetic returns is a realized return. Existing news, contract, price, uncertainty, and other policy gates remain separate requirements.

Run `python verify_new_lessons.py`. The Python standard-library script writes `new_lesson_results.json`; rational calculations retain exact fractions. The Gamma–Poisson numerical tail is independently computed by recurrence and a log-gamma formula. All 68 named checks pass. Source scope and access are recorded in [the mathematical source register](mathematical-sources.md).

## 1 Update role probabilities with new evidence at the exact threshold

An invented WR has either a high-target role H or an ordinary role L. Both states involve playing, so there is no inactive-player void in this fixture. Assume eight targets in H, six in L, independent catches with a common probability of .65, and a contract of Over 4.5 receptions.

The conditional probabilities are:

- P(Over 4.5 | H) = .7063994361
- P(Over 4.5 | L) = .3190799219

Assume P(H) = .40. A positive role report E has invented likelihoods P(E | H) = .75 and P(E | L) = .25. Bayes' rule gives P(H | E) = (.40 × .75) / (.40 × .75 + .60 × .25) = 2/3. The event probability is then (2/3) × .7063994361 + (1/3) × .3190799219 = .5772929314. These are different quantities: a probability of the role state and a probability of clearing the reception line. The distinction follows the posterior-predictive construction in MIT's [probabilistic prediction notes](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_class12-prep-a.pdf).

| Information treatment | P(H) after information | P(Over 4.5) | Modeled ROI at −110 |
|---|---:|---:|---:|
| Before the report | .400000 | .474008 | −9.5076% |
| One positive report | .666667 | .577293 | +10.2105% |
| Exact copy of that report, handled correctly | .666667 | .577293 | +10.2105% |
| Copy incorrectly treated as conditionally independent | .857143 | .651068 | +24.2948% |
| A genuine additional report with conditional likelihood ratio 1.5 | .750000 | .609570 | +16.3724% |
| Invented sensitivity case with H weight .50 | .500000 | .512740 | −2.1133% |

The correct sequential multiplier is P(E2 | H, E1, prior information) / P(E2 | L, E1, prior information). For an exact deterministic copy already known through E1, both conditional probabilities are one, so the ratio is one. The partial-dependence row assumes .90 versus .60 after E1. Those invented conditional probabilities give a multiplier of 1.5; counting two publisher names does not establish it. MIT's [odds-form notes](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_class12-prep-b.pdf) support posterior odds as prior odds times a likelihood ratio.

The same caution applies when a market-derived prior already includes E. In this hypothetical model, starting from P(H | E) = 2/3 and applying E's original ratio of three again gives the same false 6/7. A current market price is not directly a probability of H; using it that way would itself require an outcome/role/price model. Preserve the information cutoff and test incremental information beyond the contemporaneous reference.

The mixture calculation additionally assumes E changes role weights without changing the reception distribution inside each role: R is conditionally independent of E given the role and stated prior information. A report about a player's health could also change catch probability, available targets, or in-game exit risk. Then the conditional distributions must change too. A DNP-void contract would require an action-eligibility model, rather than putting DNP into the ordinary low-performance state.

For a compact settlement guard, assume a fictional contract that fully refunds the stake when inactive, with an invented 80% chance of action eligibility. If .5772929314 is the win probability conditional on action, the unconditional win/loss/void vector is (.4618343451, .3381656549, .20). At −110 the expected ROI per posted unit is .80 × 10.2105% = +8.1684%; per active unit it remains +10.2105%. Incorrectly treating the .20 void mass as losses yields −11.8316%. No actual sportsbook rule is represented: participation criteria, early exits and void clauses require direct verification for the exact contract.

### Why averaging role lines does not price the offered line

A separate exact yardage guard uses an invented high-role uniform integer distribution from 61 through 100 yards and a limited-role distribution from 1 through 60. Their 50/50 half-yard lines are 80.5 and 30.5. With equal role weights, their midpoint is 55.5, but P(Y > 55.5) = 13/24 = 54.1667%, not 50%. At the actual offered 59.5 line, the probability is 61/120 = 50.8333%. The weighted average must be taken over state probabilities at the same offered contract. Midpoint lines are a different operation.

### What would justify the news likelihoods

The .75/.25 likelihoods and .50 stress weight were supplied, not estimated. An empirical estimate needs a prospectively specified role definition, report wording/classification and cutoff, original source and repost lineage, comparable player/role contexts, and later role labels. The denominator includes both realized role states, reports that were wrong, negative reports and the stated no-report process. Looking only at publicized correct tips cannot estimate both likelihoods. Role labels based on realized targets can conflate opportunity with game script; operational labels such as routes or snaps also have measurement and selection limits. Source age, wording, author, team, injury situation and information already public can matter. A sparse sample cannot support finely sliced precise rates. Freeze the estimator on past data, assess later cases, and retain uncertainty and missingness.

## 2 A conservative endpoint depends on the uncertainty set

Using the same fixed role-specific reception probabilities, consider two wholly invented joint scenarios. The quoted prices represent possible future executable prices before quote verification, not uncertainty about a payout after acceptance.

| Scenario | Prior P(H) | P(E | H) | P(E | L) | Decimal price | Posterior P(H) | Event probability | Modeled ROI |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | .30 | .65 | .15 | 1.90 | .650000 | .570838 | +8.4591% |
| B | .50 | .85 | .35 | 1.70 | .708333 | .593431 | +0.8833% |

The minimum ROI over these two pairs is +0.8833%. Combining the lowest event probability from A with the lowest price from B instead gives −2.9576%. This is a valid adverse stress if that extra pair is allowed, but it is not the minimum over the original two-scenario set.

Now independently combine each coordinate's endpoints. This enlarged rectangular set has 16 corners. Its worst corner uses prior .30, sensitivity .65, false-positive rate .35, and decimal 1.70. It gives posterior P(H) = 39/88, event probability .4907328884, and ROI −16.5754%. That combination was absent from A and B.

The point is not that the rectangular stress is wrong or that the smaller set is sufficient. A rectangular envelope can be deliberately prudent. A small correlated scenario set can dangerously omit feasible combinations. The construction, dependence assumptions and intended coverage must be explicit. All these endpoints remain assumption-driven; none is a 95% interval. Marginal intervals for separate inputs do not automatically form a joint interval at the same coverage. A lower posterior quantile also depends on the prior, likelihood, structural model and information set; it does not certify NFL calibration.

Once an exact current price is available, evaluate plausible event probabilities at that price. If the line or settlement contract changes, recompute the event distribution as well. If reference probabilities are uncertain, keep their role clear: the central event probability .5772929314 is +2.7293 percentage points above a hypothetical .55 reference, but −1.2707 points below a .59 reference. Neither reference is the true probability by definition. Neither replaces the offered price in the payoff calculation. Shared news can make internal-model and reference errors dependent.

## 3 Price latency and limited capacity change the opportunity

For the one-report event probability .5772929314, a stale −110 price implies modeled ROI +10.2105%. At a hypothetical later executable decimal price of 1.70, the same probability gives −1.8602%. This demonstrates why an old screen price cannot stand in for an available quote.

A separate fixed-allocation stress assumes p = .55, a displayed +110 price (decimal 2.10) available for only 10 illustrative currency units, and another 90 units at −125 (decimal 1.80). The headline price has modeled ROI +15.5%, while the whole 100-unit allocation has effective decimal odds 1.83 and ROI +0.65%. At p = .52, the allocation's ROI becomes −4.84%. The second price alone has −1% modeled ROI at p = .55; there is no mathematical reason here to fill the remaining desired amount. The allocation is an arithmetic stress test, not an execution plan or assumed fill.

Selection through delay can matter even without repricing. Imagine 100 one-unit research opportunities: 20 have modeled ROI 12% and 80 have 2%. Their average is 4%, for four modeled profit units. If precisely the best 20 disappear before detection, the available 80 average 2%, for 1.6 modeled profit units per original 100 opportunities. If exactly 20 are missing uniformly at random, expected remaining profit is 3.2 units and expected ROI across the 80 remains 4%. Missing opportunities are not losing bets. This fixture distinguishes nonrandom loss of opportunity from a random loss of sample size.

For a future empirical test, preserve the entire candidate cohort with source timestamp, first detection, verification, exact contract, quote age, hypothetical accessible size, repricing, suspension, rejection and missingness. Where possible distinguish provider time from observation time and account for clock error. A hypothetical executable-at-detection quote is still not a fill. Prespecify lag and original-edge groups; compare how opportunity loss varies across them. Delayed or selected quotes can distort the reference panel too. No timing, liquidity, quote, allocation or actual wager was observed in these calculations.

## 4 A fitted predictive check is not later forecast validation

Invent 100 reception counts: 50 zeros and 50 tens. Fit a homogeneous Poisson model with Gamma(shape 1, rate 1) prior for its intensity. Under that model the posterior is Gamma(shape 501, rate 101). The observed mean is five, and the posterior predictive mean is 501/101 = 4.960396. The probability that a replicated 100-game mean is at least five is .449965964, so the mean-only check is unremarkable.

The zero-frequency check tells a different story. The predicted chance of zero receptions is (101/102)^501 = .0071832704, versus the observed .50. Expected zeros in 100 replications are .7183. Because all replicated observations share the same latent intensity draw, they must not be treated as unconditionally independent. A union bound that integrates over that shared intensity gives P(at least 50 replicated zeros) ≤ C(100,50) × (101/151)^501 = 3.17257 × 10^−59. This is an upper bound under the fitted model, not an exact tail probability or a classical uniformly calibrated p-value.

Derivation: for any fixed set of 50 observations, the chance they are all zero conditional on intensity λ is exp(−50λ). Its posterior expectation is (101/151)^501. At least 50 zeros means some set of 50 is all zero, so sum this probability over the C(100,50) possible sets. The replicated-total tail uses the integrated Poisson–Gamma negative-binomial distribution; recurrence and log-gamma implementations agree within 5.1 × 10^−14.

This deliberately extreme counterexample shows that checking a fitted mean can miss the shape failure relevant to a tail contract. It does not say Poisson models always fail for reception counts. Stan's [predictive-check guide](https://mc-stan.org/docs/stan-users-guide/posterior-predictive-checks.html) distinguishes model checking through replicated data from a proof of predictive performance and warns that its posterior tail statistics are not classical p-values.

There is a second reuse problem when a calibration display is evaluated on the same observations used to fit its correction. Suppose raw forecasts .40 and .60 each have 20 cases in a calibration window, with four and 16 successes. A binwise fitted map sends .40 to .20 and .60 to .80. Its displayed in-window calibration error is zero by construction. Lock that map. In a later invented window with ten successes out of 20 in each group, the calibrated map's weighted absolute calibration error is .30, versus .10 for the raw forecasts; its Brier loss is .34 versus .26. This only falsifies the inference that a perfect fitted display proves later calibration. It is not evidence that recalibration generally hurts. The base model, calibration mapping, bins, time split and selection procedure all require distinct evaluation roles. See the [official calibration guidance](https://scikit-learn.org/stable/modules/calibration.html) and [Stan's held-out evaluation chapter](https://mc-stan.org/docs/stan-users-guide/cross-validation.html).

The script also contains two small formula guards. A uniform-prior Bernoulli model with three successes in three observations has posterior mean 4/5, not 4/4: generally (successes + 1)/(n + 2). An apparent n + 1 denominator in the available MIT lecture transcript should not be copied unchecked; audio was not inspected, so no claim is made about who introduced the discrepancy. For two equally weighted posterior draws assigning likelihoods .2 and .8 to an observed event, the predictive log score is log((.2 + .8)/2) = −.693147, not (log .2 + log .8)/2 = −.916291. Stan's held-out chapter gives the average-density-before-log construction.

## 5 Calibrated sources do not guarantee a calibrated average

Let Y be an invented NFL prop's win indicator with base probability .50. Each signal A and B has sensitivity .80 and specificity .80, meaning 80% accuracy conditional on either outcome; the signals are conditionally independent given Y. A source reports .80 after its positive signal and .20 after its negative signal. Each source is exactly calibrated in this constructed population.

The following table is an exact 50-row representation of the population proportions, not a sample of actual forecasts:

| Signal A | Signal B | Wins | Losses | Equal-average forecast | Actual conditional win probability |
|---|---|---:|---:|---:|---:|
| Positive | Positive | 16 | 1 | .80 | 16/17 = .941176 |
| Positive | Negative | 4 | 4 | .50 | .50 |
| Negative | Positive | 4 | 4 | .50 | .50 |
| Negative | Negative | 1 | 16 | .20 | 1/17 = .058824 |

For example, source A's positive cases contain 20 wins and five losses, so its .80 forecast is calibrated. Source B is symmetric. But when both say positive, the average is still .80 while the correct probability under this joint model is .941176. The equal-average ensemble's population weighted absolute calibration error is .096. Its expected Brier loss nevertheless improves from .16 for either source to .1312, while the correctly fused conditional forecast achieves 2/17 = .117647. Averaging is not necessarily worse overall; it simply does not preserve this calibration property. Berkeley's [forecast calibration notes](https://www.stat.berkeley.edu/~ryantibs/statlearn-s23/lectures/calibration.pdf), sections 3.4 and 5.1, give the relevant conditional-calibration definition and aggregation result.

If B instead exactly copies A, seeing two positives leaves the probability at .80. A .941176 update would then be double counting. Thus individually calibrated source histories alone cannot determine the correct agreement update: their joint information matters. Equal averaging and multiplying likelihood ratios are both modeling choices with different assumptions. The combined forecast and decision subset need their own later evaluation.

## What the checks establish and what remains open

The script verifies exact internal arithmetic, falsifies several tempting shortcuts, and records its assumptions. Binomial probabilities were cross-checked with independent polynomial convolution. The role-event mixture was cross-checked through a joint-probability enumeration. Price allocations were checked against win/loss payoff enumeration. The scenario minimum was checked over all 16 rectangular corners. The posterior-predictive tail used two independent numerical formulas. The calibrated-source construction was enumerated over all eight outcome/signal cells.

It does not provide estimated NFL report likelihoods, a calibrated uncertainty region, verified source independence, live reference accuracy, executable quotes, historical user performance, or a held-out NFL forecast test. Those are empirical tasks requiring timestamped data. No code, records, source authority, bankroll policy, threshold, or controlling repository file was changed.
