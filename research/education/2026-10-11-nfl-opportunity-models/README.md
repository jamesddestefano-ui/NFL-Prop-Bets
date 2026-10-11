# NFL opportunity distributions: routes, usage transitions and game script

Research continuation · 11 October 2026 · Public written sources

## Bottom line

An NFL role change should alter the opportunity-generating process: which plays the team runs, which packages the player joins, which routes they run, and which opportunities they earn. Carry that process through to the exact reception, carry or yardage threshold. Simply scaling yesterday’s average can miss both the target rate and the distribution’s shape.

This is an educational extension, not a fitted NFL model, current pick, validated edge or stake recommendation. It adds football-specific mechanisms to the earlier report without changing it. All numbers in the worked applications are invented. Expert methods, analyst interpretations and proposed extensions are distinguished below.

These are probability and usage illustrations without offered prices. Implied probabilities, no-vig probabilities, EV and play-to quantities are unassessed. PRIME already takes a usage-first approach; this continuation makes that existing approach more explicit through an opportunity decomposition, auditable distribution calculations and a falsification test. It does not introduce a replacement framework.

## Evidence labels and confidence

- **EMPIRICAL EVIDENCE — high confidence in direct review:** The cited original written passages and official documentation were accessible and reviewed on October 11, 2026, approximately 21:57–21:59 UTC. This grade covers what the sources say and their observed access state, not independent replication of their NFL findings. No exact publication time is inferred where unavailable.
- **VERIFIED MATHEMATICAL PRINCIPLE — high confidence conditional on the inputs:** Finite-sum floating-point calculations and separate SciPy tail calculations agree for the invented fixtures. A separate reviewer’s rational-arithmetic audit also passes 21 checks. These establish computational consistency only.
- **MODEL ASSUMPTION — stipulated, not estimated:** Opportunity counts, probabilities, independence, route categories and scenario weights in the examples are supplied teaching inputs. Their empirical accuracy has no evidence grade.
- **ANALYST OPINION — moderate confidence as a research interpretation:** Decomposing usage changes may expose assumptions hidden by aggregate projections; it also increases data and estimation demands. This interpretation is not a measured advantage.
- **UNTESTED HYPOTHESIS — NFL transfer unestablished:** Whether this additional detail improves PRIME’s later prop probabilities or betting performance remains untested. No performance-confidence grade is warranted.

## Two source cards

### 1. Sean Koerner: changing usage and simulated outcomes

- **Original:** [Koerner: My Favorite NFL Prop Bets & Picks for Saturday](https://www.actionnetwork.com/nfl/nfl-prop-bets-picks-saturday-week16-koerner-2019), Action Network.
- **Date:** 2019 Week 16 context; exact initial publication date unverified. Page displays updated September 23, 2021, 11:29 PM EDT.
- **Reviewed:** Official article’s Justin Watson, Devin Singletary and Brandin Cooks sections, including surrounding methodology and disclosure. Public text extraction; the embedded interactive distribution was not opened. No video watched, no transcript or playback timestamps claimed.
- **Method:** Watson’s depleted receiving group changes projected route participation, alignment and targets. Singletary’s route involvement, quarterback behavior and receiving efficiency feed a stated 10,000-simulation distribution. The reported yardage mean exceeds its median. Cooks illustrates separate win/push/loss masses.
- **Assumptions/limits:** The full distribution family, dependence structure, parameter estimation and validation are undisclosed. The article acknowledges difficult usage projection. Historical reported probabilities are the author’s outputs, not independently validated facts; no betting-performance claim is adopted. Commercial affiliate disclosure is present.
- **Invented application:** Example A below supplies an explicit route-type model rather than attempting to reverse-engineer his simulator.

### 2. Marius Ötting: serially dependent run/pass probabilities

- **Original:** [Predicting play calls in the National Football League using hidden Markov models](https://arxiv.org/html/2003.10791); [version record](https://arxiv.org/abs/2003.10791).
- **Date:** March 24, 2020, arXiv v1.
- **Reviewed:** Author’s full paper text, sections 1–5; emphasis on sections 2–3’s data, transitions, likelihood and forecasting equations, and section 4’s evaluation. No video/timestamps.
- **Method:** Team-specific two-state HMM; Bernoulli run/pass emissions; covariate-dependent multinomial-logit transitions; estimated initial state probabilities; forward-algorithm likelihood and numerical maximum likelihood. Inputs include down, distance and intermediate score. AIC selects covariates; training spans 2009–2017 and testing 2018.
- **Assumptions/limits:** Conditional dependence is represented by the hidden Markov state; matches are treated independently. This is next-play forecasting with available situational inputs, not a validated pregame player-prop simulator. Formation and future score cannot simply be known in advance. Reported classification evaluation does not establish calibrated player-count tails. Individual opportunity allocation remains absent. Full-dataset exploratory plots inform interaction choices; the paper does not establish training-only feature development throughout.
- **Invented application:** Example B isolates script-dependent carries. It is a deliberately simpler two-scenario construction, not the paper’s fitted HMM or an implementation of it.

## Start with the right denominators

For a receiving player and a specified collection of eligible dropbacks:

- **Route participation:** player routes / team dropbacks. A snap on which the player blocks is not automatically a route.
- **Route-type distribution:** each route category’s share of that player’s routes, including routes that never receive a target.
- **TPRR:** player targets / player routes. This measures target earning conditional on running a route; it is neither participation nor target share.
- **Target share:** player targets / an explicitly defined team-target or pass-attempt denominator. State which convention and exclusions are used.

With consistently matched records, targets = dropbacks × route participation × TPRR is an accounting identity when the denominators are nonzero. It does not mean the product of three separately forecast averages equals expected targets. The factors can co-move with personnel, score and play selection.

A usable generative specification would condition on a scenario or evolving game state Z: generate team opportunities; generate player routes/packages; assign route types; generate targets and catches; then generate yards conditional on the actual opportunities. For an entire receiving corps, allocate at most one target per eligible pass through a joint categorical mechanism, including a no-target outcome. Independent target draws for every receiver would permit impossible simultaneous targets. For rushing, distinguish designed player carries, scrambles and other rush categories rather than silently treating all team rushes as interchangeable.

**Current public-data guard:** The [nflreadr participation loader](https://nflreadr.nflverse.com/reference/load_participation.html) says FTN data from 2023 onward are provided after all postseason games finish. This is a release-timing limitation for current-week research. Its [participation dictionary](https://nflreadr.nflverse.com/articles/dictionary_participation.html) describes the route field as the primary receiver’s route. Presence on the field and one primary-receiver route label do not establish every player’s routes, full route tree or TPRR. This documentation check does not audit every released file or establish current-week coverage. A retrospective feature unavailable at the forecast cutoff is not a live input.

## Example A: more routes, lower TPRR, different receiving tails

**MODEL ASSUMPTION.** All inputs are invented. A fictional WR has 40 team dropbacks, with exactly 18 short routes and six deep routes. After a package expansion, short routes remain 18 but deep routes become 18. Each short route independently draws a target with probability .30 and, conditional on that target, a catch with probability .80 for exactly eight yards. A deep route uses .10, .40 and exactly 30 yards. These are teaching inputs, not estimates or expert probabilities.

Thus catches are the sum of independent Binomial(18, .24) and Binomial(deep routes, .04) variables. Yardage is eight times short catches plus 30 times deep catches. Finite-sum convolution, evaluated in floating-point arithmetic, gives:

| Quantity | Initial role | Expanded deep-route role |
|---|---:|---:|
| Route participation | 60% | 90% |
| Expected targets per route | .25 | .20 |
| Expected targets | 6.00 | 7.20 |
| Mean receptions | 4.56 | 5.04 |
| Chance of over 4.5 receptions | 49.28% | 58.81% |
| Mean receiving yards | 41.76 | 56.16 |
| Chance of over 49.5 receiving yards | 27.82% | 52.01% |

**VERIFIED MATHEMATICAL PRINCIPLE.** Conditional on the stated assumptions, routes rise 50%, but targets rise 20% because the added routes have lower target probability. Receptions and yards do not increase proportionately. Holding aggregate TPRR fixed would manufacture extra expected targets. Route composition is therefore a separate question from participation.

**LIMITATIONS.** Fixed route counts, identical within-type probabilities, independent outcomes and deterministic catch yardage are intentionally crude. A genuine model needs uncertain route counts, target competition, quarterback/coverage context and a catch-yardage distribution. This example proves possibility, not that deep routes universally have these rates or that either fictional threshold is a betting opportunity.

## Example B: game script changes both carry opportunities and allocation

**MODEL ASSUMPTION.** All inputs are invented. There are exactly 60 eligible run/pass plays. A run-heavy script and pass-heavy script each have probability .50. In the run-heavy case, run probability is .60 and the RB receives .70 of runs. In the pass-heavy case they are .30 and .50. Within a script, these per-play trials are independent. All remaining runs go to other players. Neither state is an injury or inactive state.

The RB’s carry distribution is therefore half Binomial(60, .42), half Binomial(60, .15). It has mean 17.1 carries, variance 76.743 and a 46.69% chance of more than 19.5 carries. A single Binomial(60, .285) has exactly the same 17.1 mean, but variance 12.2265 and only a 24.29% chance of clearing 19.5.

**VERIFIED MATHEMATICAL PRINCIPLE.** Conditional on the stated assumptions, both between-script variation and within-script variation matter. Multiplying average run probability (.45) by average player share (.60) by 60 would even misstate the mean as 16.2: the two rates are positively associated through script.

**LIMITATIONS.** A real game can change script repeatedly; total plays, clock, score, substitutions and injuries are stochastic. A pregame implementation must generate those future states rather than inject their realized values. Example B is not an empirical finding or proof an HMM improves prop forecasts.

## One falsification test: do usage transitions add predictive value?

**UNTESTED HYPOTHESIS.** A pregame opportunity model that allows route composition and script-dependent allocation improves later reception/carry distributions over a matched model that freezes those components.

1. Freeze the eligible player-game cohort, forecast cutoff, role-transition definition, data-availability checks, model fitting procedure and evaluation horizon before seeing outcomes. Save both models’ full probability distributions on identical cases. Label role changes from information available at the cutoff, not realized usage.
2. Compare the expanded model with an otherwise matched frozen-usage baseline. Keep fitting/recalibration inside the training window. For count forecasts, use paired ranked probability score (RPS) on a common prespecified count support or truncation rule; lower is better. Any truncation must preserve an overflow category and be labeled as scoring a coarsened target, without deleting or silently renormalizing tail outcomes. An RPS gain does not establish calibration at every prop threshold. Inspect preregistered threshold Brier scores and coverage of predictive intervals within the transition subgroup. Prespecify game/week blocking and treatment of recurring player/team dependence for uncertainty; game clustering alone may not capture all relevant dependence.
3. Before testing, choose a minimum useful improvement and uncertainty procedure. Evidence against the claimed useful improvement is an uncertainty interval whose upper bound for baseline-minus-expanded score gain is below that minimum. An interval wholly below zero supports harm; a negative point estimate alone does not. A lower bound above the minimum useful gain supports the stronger improvement claim. Wide intervals spanning the target are inconclusive, not success.
4. Fail the intended live-use claim immediately if essential full-route inputs were unavailable at prediction time, or future formation/score was supplied as known. Good retrospective fits cannot repair that leak.

No empirical cohort was collected or tested here. Neither source establishes profitable NFL prop selection. The concrete research gain is a testable specification of what “usage changed” must mean.

## Reproduction

Run `python verify_examples.py`. It uses only the Python standard library, writes `example_results.json`, and passes 13 arithmetic/normalization checks. `python crosscheck_examples.py` additionally passes six SciPy tail comparisons. `python independent_rational_checks.py` runs a separate reviewer’s implementation using exact rational arithmetic and passes 21 named checks, without importing either other script. All 40 checks verify the invented calculations, not source accuracy, calibration or an NFL production model.
