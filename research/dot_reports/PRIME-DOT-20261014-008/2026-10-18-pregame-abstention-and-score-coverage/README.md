# A better score on fewer forecasts can still be a worse forecasting policy

**Task:** PRIME-DOT-20261014-008 · **Research date:** October 18, 2026 (EDT).

## Useful result first

A model that forecasts only the easiest cases can post a lower average Brier score while losing to the market on the same covered cohort's average. Even a fair comparison restricted to shared forecasts does not rank two different abstention policies. Report **coverage, same-case score differences and the whole predeclared fallback policy** as separate quantities.

For today's pregame work, keep official availability, an attributed playing expectation and a defensible workload forecast separate. The [bounded public-source ledger](news-ledger.md) preserves the fresh original reporter update, official status, observation times and unresolved role uncertainty. It supplies no current executable price or calibrated player probability.

**Status: pregame educational deliverable; actual pilot assessment INCONCLUSIVE.** This package contains synthetic tests and a review-only scoring proposal. It contains no actual frozen cohort, genuine independent model submissions, matched closing panel or final outcomes. It cannot establish that the pilot succeeded, either model is superior, or a bet has positive EV. The requested postgame critique remains future work; retain this version unchanged.

## 1. Define what a selective score measures

**VERIFIED MATHEMATICAL PRINCIPLE.** For binary no-push outcomes, let `L(p,y)=(p−y)²`. Let `g=1` mean a model provides a usable forecast and `g=0` mean it abstains. Its covered risk is `E[gL]/E[g]`, provided coverage `E[g]>0`. That is a score on the accepted cases, not the entire eligible universe. At zero coverage the score is undefined, not zero.

This is the relevant distinction from the [original selective-prediction reading](source-register.md). The paper's classification guarantees are not guarantees for NFL Brier scores. We use the risk/coverage distinction and independently derive the examples below.

**MODEL ASSUMPTION, invented finite fixture.** There are 50 binary settled cases: ten in an “easy” stratum with nine positives, and forty in a “hard” stratum with twenty positives. These labels and probabilities are deliberately constructed, not NFL estimates. The market forecast is 0.90 for each easy case and 0.50 for each hard case. A selective model supplies 0.70 only for the ten easy cases and abstains on the remaining forty. Membership and the abstention rule are fixed before evaluating the invented outcomes; an empirical implementation must really satisfy that timing condition.

| Comparison | Coverage | Mean Brier loss, lower is better |
|---|---:|---:|
| Selective model on its supplied forecasts | 10/50 = 20% | 0.1300 |
| Market on all eligible cases | 50/50 | 0.2180 |
| Market on the same ten model-covered cases | 10/50 | 0.0900 |
| Model where supplied, otherwise market | 50/50 | 0.2260 |
| 25% model / 75% market where supplied, otherwise market | 50/50 | 0.2185 |

The first two rows create a misleading apparent model advantage by changing the comparison set. On matched cases the model is worse by 0.0400; under the declared market fallback it is worse by 0.0080 across the full cohort. The fixed mixture uses `0.75×0.90 + 0.25×0.70 = 0.85` on the easy cases. It reduces this model's damage but does not beat the market. These are exact finite-fixture scores, not estimated effects or significance tests. [Reproducible derivations and log-loss checks](DERIVATION.md) preserve the assumptions.

**Counterargument:** abstaining can be beneficial when missing inputs make a forecast unreliable. The problem is not abstention itself; it is claiming improvement from incomparable denominators, or ignoring what happens on abstained cases. A low covered loss is useful descriptive evidence when its population and coverage are honestly specified.

## 2. A paired model comparison and a routing-policy comparison answer different questions

**VERIFIED MATHEMATICAL PRINCIPLE.** Let `m_i` be the frozen market forecast and `p_i` the model forecast when supplied. A hard-routing research policy uses `h_i=p_i` on accepted cases and `h_i=m_i` elsewhere. On a common outcome-observed cohort of size `N`,

`mean[L(h_i,y_i)−L(m_i,y_i)] = (1/N) Σ g_i[L(p_i,y_i)−L(m_i,y_i)]`.

This identity holds case by case. It does not assume that the market is true probability. The contribution from abstained cases is zero because the specified fallback equals the benchmark there. It does **not** mean that abstention itself earned a perfect forecast or that a missing model output can be entered as `p=0`.

A common-case comparison isolates forecast quality where both models spoke. It intentionally omits cases only one model covered. If the two selectors differ, those omitted cases can reverse the end-to-end policy ranking, even at identical overall coverage. The [additional exact synthetic example](DERIVATION.md) tests that distinction. Neither comparison supersedes the other; publish the estimand each answers.

The fallback here is a **research forecast**, not a wager. If the real objective is sparse advice with no forecast on rejected cases, a hypothetical market fallback answers a different question. Preserve the actual abstention objective and distinguish source-forecast coverage, composite-forecast coverage and betting selection rate. A fallback that is unavailable on a row cannot silently supply 100% coverage.

**ANALYST OPINION / METHODOLOGY_CHALLENGE.** For a future frozen comparison, preserve the original model, an explicitly named fallback policy, and a separately named fixed-weight mixture. Do not silently replace missing Claude output with the market and label the result “Claude.” Record `NOT_RECEIVED`, deliberate `ABSTAIN`, malformed submission, unavailable source and rejected timing as different states. A fallback result evaluates a composite policy and must retain those causes. Unknown model/version/training metadata stays unknown; never invent it to satisfy an intake schema.

**UNTESTED HYPOTHESIS.** A predeclared selector might add value by choosing cases where the model improves on the market, rather than merely choosing outcomes that are inherently easy to predict. Test that on later held-out games; low uncertainty or confident prose alone does not establish relative advantage.

## 3. Missing outcomes require bounds, not invented scores

**VERIFIED MATHEMATICAL PRINCIPLE.** For a fixed binary forecast `p` with unobserved outcome, its Brier loss is one of `p²` or `(1−p)²`. Summing the smaller and larger values across missing cases yields a finite-cohort identification interval once the observed losses are added. These are bounds on this fixed cohort's still-unknown average, not a confidence interval, a population guarantee or proof that missingness is random.

For paired score differences, the two forecasts share the **same** missing outcome; evaluate the two possible differences directly. Subtracting separate marginal bounds can be needlessly loose. The fixtures test sharp bounds for unconstrained binary completions and preserve unknown outcomes as unknown. Nested thresholds, complementary sides or shared settlement can constrain joint completions; simple per-row extrema then remain outer bounds but need not be attainable together.

Log loss needs additional care. Unrestricted forecasts admit no uniform finite worst-case upper bound; endpoint forecasts can incur infinite loss. A paired difference of two infinite losses is undefined and must not be reported as a tie or a numeric gain. Fixed forecasts strictly inside `(0,1)` nevertheless have finite forecast-specific bounds. A prospectively declared epsilon constraint supplies a uniform bound, but clipping changes the forecasts and cannot be installed after seeing the losses. No clipping policy is adopted here.

**MODEL ASSUMPTION.** These identities concern a binary no-push target. Integer thresholds, inactivity refunds, early-win terms or other settlement variants require the correctly defined probability basis and scoring categories. Conditional win probability cannot be compared to an unconditional hit label. Duplicating complementary Over/Under rows does not create independent evidence, and game/player dependence remains relevant to uncertainty.

## Bounded falsifiable test proposal

This extends existing [Sunday pilot guidance](../../../pilots/2026-10-18/PLAN.md) and [task013's paired-comparison safeguards](../../PRIME-DOT-20261016-013/2026-10-17-closing-move-and-quote-availability/protocol.md); it changes neither protocol nor any production gate.

1. Preserve **all eligible frozen contracts**, their stable identities, exact source times and exclusions. Keep the side-level inventory; declare the analysis unit and weights before scoring so complementary sides and repeated books do not multiply the independent sample count.
2. Record each genuine model's original probability basis, pre-outcome selection decision and missingness reason. Preserve source overlap, news cutoff and all forecasts, including passes. Do not infer agreement from an absent response.
3. First publish coverage by model and cause. Then publish paired market/model and model/model losses on named shared cohorts, with exact denominators. Publish a full-cohort fallback-policy comparison only if its routing rule, benchmark and required outcomes were prospectively specified and observed. Otherwise report it as unavailable, or use clearly labeled identification bounds where valid.
4. If testing the 0.25 mixture, freeze that weight before outcomes and keep it separate from raw model and market forecasts. Do not tune it on this Sunday and call the result out-of-sample. The example demonstrates no general superiority of that weight.
5. The claim “a lower selective score proves a better deployed predictor” fails if a paired or declared whole-policy comparison reverses it. Empirical improvement remains unresolved when required inputs/outcomes are missing, common coverage is empty, or uncertainty is too wide. One Sunday provides an operational/descriptive check, not permission to promote a model.

## Evidence, confidence and scope

Evidence labels are **VERIFIED MATHEMATICAL PRINCIPLE**, **EMPIRICAL EVIDENCE**, **MODEL ASSUMPTION**, **ANALYST OPINION**, and **UNTESTED HYPOTHESIS**. Empirical evidence in this package concerns source/access observations and public pregame status, not NFL forecasting performance. Disagreements are labeled **METHODOLOGY_CHALLENGE**, **MODEL_UNCERTAINTY** or **UNVERIFIED_CLAIM** where relevant.

Confidence is qualitative and scope-specific: **high** means direct source access or reproduced conditional mathematics; **moderate** means a supported interpretation with material assumptions; **low/unestablished** means the needed evidence is missing. Source-specific access, claim and NFL-transfer assessments appear in the [technical register](source-register.md) and [news ledger](news-ledger.md). These are research assessments, not audit certifications.

The novel contribution beyond task013 is the separation of model-conditional scores from complete routing-policy performance, including equal-coverage ranking reversals and outcome-missingness score bounds. Earlier selection, clustering, settlement and source-independence protections remain in force. Tasks011/012 are not marked completed by this bounded contribution. No private source material, actual ticket information or live provider data is included.

## Reproduce the synthetic checks

From this package directory, run `python -m unittest -v` for the **34 tests** and `python score_fixture.py` to regenerate the invented fixture/results. Python's standard library is sufficient. [Recorded results](results.json), [math-file hashes](SHA256SUMS.json) and the [package manifest](manifest.json) preserve verification scope. Test success establishes consistency of these fixtures and guards; it is not a deployed simulator, a calibrated forecasting model or an NFL backtest.
