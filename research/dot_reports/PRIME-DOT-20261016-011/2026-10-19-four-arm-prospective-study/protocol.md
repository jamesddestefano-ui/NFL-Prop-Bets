# Proposed four-arm frozen-contract study

**Task 011; design dated October 19, 2026. Research proposal only.** This is not an amendment, activation or replacement of an approved pilot. Any execution needs its own prospectively accepted manifest and all existing quote, identity, settlement and timing gates. The [retained Monday decision](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/0c8b758162fa442df899cdf9c8ef7b09e350f34f/research/decisions/2026-10-18-retain-current-monday-protocol.md) remains controlling for that pilot. No experiment or genuine model forecasts were obtained for this report.

## 1. Question, four arms and success criteria

**UNTESTED HYPOTHESIS:** a fixed market-model combination improves future probability accuracy on the same eligible NFL contracts. Standalone superiority and useful combination are separate hypotheses.

Four primary arms, fixed before any test outcome:

1. **M:** proportional no-vig market probability from a frozen, simultaneous, exact same-book Over/Under pair.
2. **G:** original genuine ChatGPT probability for that event and target.
3. **C:** original genuine Claude probability for that event and target.
4. **S_G = 0.75M + 0.25G.** The 0.25 coefficient is an experiment, never a production weight or stake. Choosing G as the anchor is an explicit arbitrary design convention, not evidence it is stronger. Do not swap to C after results. A Claude-shrunk or symmetric blend requires its own prospectively declared secondary analysis; neither is included in the primary family here.

The test is against realized official outcomes, not a market close treated as truth. Compare G−M, C−M and S_G−M on **one common four-arm cohort**, using lower-is-better loss. Primary endpoint is equal-game average Brier difference; log loss, coverage and calibration are secondary diagnostics. Predeclared practical-improvement margin: **0.001 Brier units** (analyst-chosen research tolerance, not a universal economically meaningful threshold). A primary superiority claim requires its multiplicity-adjusted upper interval bound to be below −0.001, adequate preregistered precision and no unresolved material cohort/target violations. Otherwise report inconclusive or worse as warranted. No scoring result alone establishes positive EV or adoption.

Proposed future assessment window is **2026 regular-season Weeks 7–12**, only if approved and frozen before its first eligible event. If readiness misses that start, register a new future window before its outcomes; do not backfill. No early success stop or weight/prompt/baseline selection on these outcomes. Week 6 is not a reconstructed holdout. An a priori precision simulation using earlier, legitimately available data must specify game counts, dependence sensitivity and desired interval width before an empirical claim is attempted; these inputs are not currently established. A small operational pilot can test capture without satisfying this performance requirement.

## 2. Population, orientation and exact market baseline

Freeze the approved screened universe and deterministic selection algorithm before viewing any model output. Initially study integer-valued receptions, receiving yards and rushing yards at **half-point** lines with supported rules; exclude touchdowns from this primary stratum. Preserve all screened and excluded rows. Do not alter a current three-book eligibility gate to make a study feasible.

One primary orientation is Over per unique event/player/statistic/threshold/book/jurisdiction/rule-version group. Retain Under and repeated quote snapshots as audit evidence, not extra independent trials. Within each game, equal-weight these unique groups; equal-weight eligible games in the primary score. Also report separately labelled contract-weighted results, whose estimand differs. A maximum-number selector, if needed for capacity, must be committed independently of price favorability, model confidence or later result.

For decimal O/U prices d_O,d_U at the same book, q_O=1/d_O, q_U=1/d_U; M=q_O/(q_O+q_U). This is a transformation assumption, not identified true probability. Proposed registration defaults: freeze once at scheduled kickoff minus 60 minutes; require each quote update within 10 minutes of observation, opposite-side observations within 30 seconds, and receipt before freeze. Missing or imprecise timing that cannot prove these bounds excludes the pair. Among books passing the separately governing exact-contract eligibility requirements, choose the smallest SHA-256 of the canonical book/jurisdiction/rule ID, not the most favorable price. No outage substitution after freeze. These are analyst-chosen experimental defaults requiring prospective acceptance, not claims of executable freshness or amendments to Monday controls. No cross-book synthetic pair. Keep exact original prices and opposite side, quote/source update time, actual observation/receipt, suspension state and jurisdiction applicability. API-observed is not proof of user executability. Unsupported book/rule/source identity excludes the row before forecasts. Missing input is never zero.

## 3. Matching the probability target, including push and void

**VERIFIED MATHEMATICAL PRINCIPLE:** a half-point threshold for an integer statistic has no threshold push. It can still have contractual void/refund conditions. The primary target is **P(Over win | contract is action/settled win or loss)** for a rule-supported no-push contract. All arms must explicitly forecast that same conditional target. Score only W/L outcomes, report void count and probability/coverage separately, and describe the result as conditional performance. This does not assess a model's unconditional activation or void forecast.

A full four-class W/L/push/void extension is separate: all arms need comparable nonnegative normalized vectors and supported labels. Two-way de-vig prices alone do not identify push or void mass. Do not synthesize a market vector by borrowing the AI's push estimate. With independently justified and prospectively fixed full vectors, use half-sum multiclass Brier (so binary reduction equals ordinary Brier) and −log(probability of actual class). Otherwise the multiclass **four-arm** comparison is unavailable, even if AI-only vector scores can be described separately.

For a genuinely known decimal offer d, ordinary unit-stake ROI with neutral refunded push/void is p_W(d−1)−p_L = d p_W+p_P+p_V−1. If action mass a=1−p_P−p_V and conditional q=p_W/a, ROI=a(dq−1). The sign agrees with conditional edge when a>0, but its magnitude is not identified by q alone. Conditional scoring neither estimates action probability nor verifies payout terms. Early-exit protection, resettlement and promotions require their actual rules. Keep initial official result and later corrections as new dated versions; never overwrite the forecast or original label.

## 4. Identical inputs and genuinely separate forecasts

Deliver one immutable **price-blind** packet, with identical prompt bytes and evidence, into two genuinely separate sessions. This is a proposed study condition, not retroactive evidence any pilot met it. The exact threshold, statistic and rule target remain visible. Hide current/closing odds, M, any other model forecast and any outcome. If general market knowledge is already in the model, do not claim it has been erased.

The packet identifies event/player, supported contract/rules and all permitted pre-cutoff public features. Any browsing must be disabled or constrained to exactly this shared snapshot; unequal external research is a different experiment. Record source URLs, publication/first-observed availability, retrieval, full permitted packet hash, prompt hash and explicit upstream-source families. Two sites quoting one team announcement count as one underlying fact. Identical input plus separate sessions establishes controlled input equality, **not statistically independent errors** or independent football evidence.

Proposed defaults: shared public evidence cutoff kickoff minus 90 minutes, delivery after the validated market/contract freeze at minus 60 minutes, and both original replies saved verbatim with immutable server possession strictly before kickoff minus 30 minutes. Both must lock before disclosure to the other model. Existing pilots retain their actual approved deadlines. Record actual delivery, observed completed-reply receipt and independently re-queried server possession times separately. Model-declared generation time, UI label, operator attestation and server receipt are distinct evidence. Unknown backend build/training membership stays unknown. No invented model metadata, silent probability edits, retries selected for favorable answers or reconstructed earlier responses. A visible model/service change creates a version stratum; unobserved internal changes remain a limitation.

Exact contract match does not imply equal feature packets. Require equality of canonical packet AND prompt hashes, not only contract IDs; see the existing [public boundary review](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/0c8b758162fa442df899cdf9c8ef7b09e350f34f/research/reviews/2026-10-19-model-development-identical-input-feature-packet-review.md). The instructional fixture demonstrates this research requirement; it does not install a production guard or independently certify source truth.

## 5. Minimum as-of schema

| Block | Required content |
|---|---|
| Registration | study_id/version; acceptance and independent possession receipt; future window; market/book/no-vig selector; numerical age/skew thresholds; forecast deadlines; weight/anchor; primary contrasts; weighting; practical margin; multiplicity; inference/precision plan; missingness/fallback policy; correction policy |
| Identity | official event and kickoff UTC; stable player/team/opponent; statistic/unit; exact numeric threshold/side; book/jurisdiction; supported rule version/hash; settlement target/conditioning; canonical contract and group IDs |
| Market | original paired quote references/hashes; both prices and sides; publication/update/observation/receipt times with known precision; source/book IDs; presence/suspension/executability as distinct fields; transformation and output M |
| Shared evidence | packet/prompt bytes and hashes; feature availability bound; publication/retrieval; upstream family links; versioned official news; unresolved contradictions; source allowances |
| Model record | genuine source/session attribution; visible model label/build if known; original response/hash; FORECAST/ABSTAIN/NOT_RECEIVED/LATE/INVALID; stated target; raw probability/vector; distribution and assumptions; uncertainty representation; delivery/receipt/lock evidence |
| Derived arm | exact arithmetic S_G and component IDs/hashes; weight fixed by registration; absent if G or M absent; no standalone claimed session for a calculated blend |
| Outcome | official final-stat URL/body hash and retrieval; statistic; exact-rule label W/L/P/V/UNRESOLVED; correction history; join reviewer and reason; no wager inferred |
| Accounting | screened/eligible/attempted/locked/scoreable/common counts; missing reason; model availability by game/market/role; all score denominators and cluster IDs |

A schema-valid record is not proof its timestamps, identity or quotations are true. Independent source verification is still needed. The local demonstration validates selected invariants, not this whole production schema.

## 6. Missingness, proper loss and coverage

Every frozen row stays in the denominator ledger. Genuine ABSTAIN is distinct from no Claude response, late transport, invalid output, absent quote and unresolved outcome. Do not treat missing C as agreement, supply C from G or drop the row invisibly. The primary common cohort requires valid M/G/C/S_G and resolved eligible target. Publish its retained fraction of the **entire frozen eligible universe**, plus per-arm coverage and exclusions. It describes covered cases, not all candidates; no missing-at-random assumption is asserted.

Any pair-specific supplemental analysis names its own cohort and cannot support one all-universe ranking. A secondary fallback policy (use M when a model is absent) must be specified before test outcomes and evaluated over a denominator where M and outcomes exist; it tests that deployed policy, not raw model skill. The [October 18 coverage lesson](../../PRIME-DOT-20261014-008/2026-10-18-pregame-abstention-and-score-coverage/README.md) supplies the detailed selection counterexample rather than duplicating it here.

For binary Y, Brier=(p−Y)^2; log loss=−[Y log p+(1−Y)log(1−p)], with natural log and proper endpoint conventions. Zero probability on a realized event gives infinite log loss. Two infinite aggregate losses have undefined paired difference; no quiet clipping or conversion to a tie. Publish such failures separately, and withhold a finite log-loss interval unless its estimand is well-defined. Any clipped secondary score must declare its cap prospectively and cannot be called the unchanged proper log score.

## 7. Dependence, inference and calibration

Compute each paired difference on the same rows, average within game and then across games. Resample **whole games with all paired arms together**, never individual props. For the three primary Brier contrasts, proposed simultaneous reporting uses Bonferroni-adjusted **98⅓% two-sided intervals** per contrast, giving a nominal family error bound of 5% only if each interval has its claimed coverage. Proposed seed = 20261019 and 20,000 paired whole-game resamples are fixed in the future registration; Monte Carlo precision is separate from statistical validity. The present two-game enumeration is a mechanics illustration, not valid NFL confidence evidence.

Game independence is a **MODEL ASSUMPTION**. Shared weather/news/model versions and adjacent weeks can induce broader dependence. Predeclare week-block sensitivity and leave-one-game/week-out stability, report numbers of games/weeks, and withhold strong claims if too few effective clusters or unstable intervals. More bootstrap draws cannot create independent games. A six-week window does not automatically justify reliable week-cluster inference. Do not import an asymptotic forecast-comparison theorem without its estimation, dependence and stationarity assumptions.

Raw and calibrated tracks must be separate. For future learned calibration or combination, use only earlier training weeks and out-of-sample/rolling-origin component predictions within training (or a valid held-out calibration split). Freeze the map before the outer test; all selection/tuning stays inside training. Report reliability, proper scores and sharpness together, with denominator and uncertainty. A lower realized Brier score is not by itself a calibration proof, and calibrated probabilities need not be useful enough to overcome margin or execution costs.

## 8. Falsification and next decision

- Reject the *identical-input* claim if packet/prompt/availability differs; preserve data as a separately labelled study rather than quietly repair.
- Reject a four-arm superiority claim if its primary cohort, target or multiplicity rule changes after outcomes; retain descriptive results with the limitation.
- A blend failing the locked margin/interval criterion does not establish improvement, even if one alternate weight looks good retrospectively.
- Missing outcomes, genuine C or exact settlement are evidence gaps, not negative results about model ability.
- Evaluate official outcomes and matched closes separately. No current quotes, no fair NFL probability, no conservative probability and no executable play-to price were established here; their values remain **unavailable**, not zero. Operational recommendation remains PASS for this research artifact.

**ANALYST OPINION:** prioritize one auditable prospective comparison over more unverified probability rows. **UNTESTED HYPOTHESIS:** the design will reveal useful complementary information, if any, beyond M. Neither the design nor passing synthetic tests promotes a model or changes current PRIME controls.
