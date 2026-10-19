# A weak standalone forecast can still improve a fixed market blend

**October 19, 2026 morning EV education · task PRIME-DOT-20261016-011**  
Research began 12:09 UTC /08:09 EDT. Primary-source study and public news review were performed during this session; exact access windows are in [sources](sources.md) and [news ledger](news-and-access.md). This package completes a **review-only study design and synthetic consistency tests**, not the empirical NFL study or pilot readiness.

## Useful result first

A model can have a worse Brier score than the market and still improve a **small, prespecified combination**. Conversely, fitting the best combination after seeing the results does not validate that combination. The proposed test must distinguish:

1. Raw ChatGPT/Claude versus market accuracy.
2. Future performance of the already fixed 25% blend.
3. Incremental information under a specified fitted encompassing model.

Today's two original statistical readings explain why these are different questions. They provide methodology, not evidence either language model has NFL edge. [Source versions and confidence](sources.md).

## 1. Worked lesson: useful disagreement is more than agreement

**VERIFIED MATHEMATICAL PRINCIPLE.** For binary outcome Y, market M, rival G, displacement D=G−M and S=M+wD,

> mean Brier(S) − mean Brier(M) = 2w mean[D(M−Y)] + w² mean[D²].

This identity is algebra, requiring no independent forecast errors or unbiasedness. The first term measures whether the displacement corrects the market's residual error; the second penalizes how far it moves. Forecast correlation or repeated agreement alone does not identify that balance.

**Entirely invented two-case example; no NFL forecast or quote:**

| Case | Y | M | G | Fixed S=.75M+.25G |
|---|---:|---:|---:|---:|
| 1 | 0 | .10 | .70 | .25 |
| 2 | 1 | .50 | .90 | .60 |
| Mean Brier | | **.13000** | **.25000** | **.11125** |

Here mean[D(M−Y)]=−.07 and mean[D²]=.26. Therefore Δ(w)=−.14w+.26w²; at w=.25, Δ=−.01875. Raw G loses, but the fixed blend wins this toy. The ex-post minimizing weight 7/26 is only an oracle illustration. It was not an estimated NFL parameter or a permission to tune on the assessment set. The two observations establish no sampling confidence, calibration or practical edge.

**MODEL ASSUMPTION:** the future protocol assigns 25% to G by convention. **UNTESTED HYPOTHESIS:** a similar beneficial cross-moment persists on future, genuine NFL forecasts. Source overlap, model distortion, leakage or plain luck could explain apparent success. An actually efficient market forecast may leave no exploitable residual signal.

## 2. The comparison needs the right target and denominator

The [full protocol](protocol.md) freezes four primary arms M/G/C/S_G, one common covered cohort, exact settlement identity, identical price-blind input/prompt hashes and genuine separate outputs. Missing Claude is unavailable, never agreement. Forecast receipt, server possession and model-declared times remain different facts.

Two-way no-vig probability does not identify push/void mass. The initial primary stratum therefore uses supported half-point integer-stat contracts and explicitly **conditional-on-action W/L** probabilities. Voids are reported, not scored as losses. Full-vector comparison is unavailable unless every arm has a justified comparable vector. Exact ROI still needs the original payout rule and action probability. [Settlement and schema detail](protocol.md#3-matching-the-probability-target-including-push-and-void).

Prior education already demonstrated selective-coverage bias; this adds the four-arm contract, source-overlap and fixed-combination design rather than reproducing that earlier lesson. Packet equality controls input variation; it cannot make shared facts or model errors independent.

## 3. More rows can change weighting without adding information

In the toy, S−M losses are +.0525 and −.09 in the two games. Their equal-game mean is −.01875. Repeating the first game's complementary Under row makes the naive row mean **+.005**, reversing the comparison while adding no new independent result. The row-weighted arithmetic is valid for that different weighting; it is not the same equal-game estimand.

**METHODOLOGY_CHALLENGE:** freeze orientation and weighting first, preserve all screened cases, and keep paired forecasts together when resampling whole games. Week/common-source dependence and small cluster counts can still invalidate nominal intervals. The proposed inference is conditional on explicit assumptions, not automatic confidence from a large row count. No number of bootstrap draws repairs missing authentic forecasts.

## What would change our mind?

The proposed Weeks 7–12 holdout, if prospectively approved, tests three primary Brier contrasts against M with fixed weighting, a declared practical margin and multiplicity accounting. Genuine source/receipt/contract violations defeat the experiment claim; failure of the registered improvement criterion defeats a superiority claim. Learned calibration, alternate weights or conditional routing discovered later require a new held-out test. [Complete proposal and falsification rules](protocol.md).

**ANALYST OPINION:** this is a more useful next research step than assuming model consensus establishes an edge. **EMPIRICAL EVIDENCE:** today's actual observations are limited to source access, official status announcements and synthetic test execution. There is no empirical NFL model-accuracy result.

## Current NFL application and limits

The [bounded MNF refresh](news-and-access.md) retains unresolved receiver/backfield availability and workload questions. A public role analogy is a feature hypothesis, not a quantified opportunity distribution. No comparable current sportsbook quotes or original NFL model forecasts were obtained; implied/no-vig/fair/conservative probability, EV and play-to fields are unavailable. No betting recommendation follows.

Existing Monday three-book gates and disabled/readiness status are unchanged. This package does not activate a pilot, alter production controls or repair any record.

## Reproducibility and review

See [worked tests](math-note.md), [fixture](fixture.json), [instructional validator](frozen_study.py), [test suite](test_frozen_study.py), [saved results](results.json) and [manifest](manifest.json). All probabilities, contracts and outcomes in those fixtures are invented. Test pass counts, actual independent review and file hashes are recorded in the final manifest; they establish only the stated mathematical/guard consistency scope.
