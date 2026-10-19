# Frozen four-arm probability study: exact educational fixtures

All identities, dates, probabilities and outcomes are invented. No current odds, private inputs, model API calls, fitted production scorer, or empirical model-performance claim appears here. Python 3, standard library only.

Run from this lesson directory:

```sh
python -m unittest -v test_frozen_study
python run_checks.py > results.json
```

The suite has **33 named tests**. `run_checks.py` emits deterministic JSON, including every test name and exact fractions. `fixture.json` is the inspectable invented record. `frozen_study.py` deliberately supports one unique canonical half-line contract per game. The generated results are arithmetic illustrations, not evidence of actual model skill.

## 1. A worse raw forecast can improve a fixed market blend

For binary outcome Y, market M, raw model A, and fixed S=M+w(A−M),

Brier(S)−Brier(M) = 2w·mean[(A−M)(M−Y)] + w²·mean[(A−M)²].

This follows by expanding [(M−Y)+w(A−M)]². The same identity holds for any common, fixed nonnegative observation weights summing to one.

Use two independent-game placeholders:

| Game | Y | M | G (ChatGPT arm label) | C (Claude arm label) | S=¾M+¼G |
|---|---:|---:|---:|---:|---:|
| 1 | 0 | 1/10 | 7/10 | 1/5 | 1/4 |
| 2 | 1 | 1/2 | 9/10 | 4/5 | 3/5 |

Equal-game Brier scores and paired differences versus M:

| Arm | Brier | Arm minus M |
|---|---:|---:|
| M | 13/100 | 0 |
| G | 1/4 | +3/25 |
| C | 1/25 | −9/100 |
| S | 89/800 | −3/160 |

Lower Brier is better. Thus G is worse than M, yet the prospectively fixed quarter-weight blend improves M.

Here cross-term c=−7/100 and movement d=13/50, giving Δ(w)=−7w/50+13w²/50. Improvement holds for 0<w<7/13. Raw weight w=1 is outside that interval; fixed w=1/4 is inside it. The constrained ex-post oracle is clip(−c/d,0,1)=7/26. This is a diagnostic calculated using the outcomes, never the study's selected weight or a deployable result. If d=0, all weights are equivalent and the oracle is non-unique.

S is anchored to G by the stated pre-event protocol even though C happens to win this invented example. A separate ¾M+¼C result is permitted only if that secondary was prespecified; its synthetic Brier would be 157/1600. The main four-arm result never replaces S with it.

## 2. A common cohort and an actual contract

The invented universe contains four rows. The pre-event complete-case rule freezes toy-1 and toy-2 for **all** M/G/C/S comparisons. toy-3 has no C record (MISSING); toy-4 has an explicit C ABSTAIN with no probability. Neither becomes 0, ½ or a loss. Both exclusions remain visible and distinct. M is not scored on all four rows while its competitors are scored on only two.

This estimates skill conditional on common coverage. It does not establish performance on missing/abstained cases; report the complete-case coverage (2/4 here). The criterion, exclusions, arm identities, shrinkage, endpoints and aggregation must be fixed before labels. Complete-case eligibility can be frozen from availability at the prediction cutoff, under an earlier declared rule.

A forecast and settlement must identify the same event, subject, market, threshold, orientation, period, book-settlement rule and probability target. G/C receive an identical price-blind evidence packet and identical shared prompt, checked by canonical hashes. M is obtained separately from a frozen market snapshot, which is never a model evidence field. Changing the evidence, prompt hash, or market snapshot without matching its record fails validation. Hash equality does not make different models identical or prove access to the same training information.

Metadata order is protocol lock ≤ evidence/market capture ≤ forecast generation ≤ common-cohort lock ≤ prediction lock < event start < observed settlement. Model evidence and the baseline market snapshot have separate hashes and capture records. The checker rejects inconsistent claimed times, mismatched model prompts and explicit market fields in the minimal model-evidence schema. It **cannot prove** historical existence, unedited timestamps, authentic provider outputs, no hidden leakage, or real settlement correctness. An actual study needs auditable pre-event locked records and source provenance. Editing the protocol flag after outcomes and supplying an earlier timestamp is not prespecification.

## 3. The probability target must match

For integer-count half-lines, pushes are structurally impossible; a binary win probability conditional on a nonvoid settlement can match a decisive 0/1 outcome. A void must follow its prespecified treatment, never become a loss. This toy has only decisive outcomes and does not implement real void handling.

For a contract allowing pushes, q=P(W | W or L) does not identify the full distribution. With push mass p:

(W,L,P)=((1−p)q,(1−p)(1−q),p).

At q=3/5, both (3/5,2/5,0) and (3/10,1/5,1/2) have the same q. At invented decimal odds 2 with one unit initially staked and pushes refunded, expected net ROI is W(2−1)−L: respectively 1/5 and 1/10. A neutral push contributes zero, but its probability changes the unconditional return magnitude. Conditional probability alone does not determine that magnitude. This example has no separate void state and assumes no fees. The all-push case makes q undefined.

## 4. Opposite sides are dependent and can change the estimand

Per-game S−M Brier deltas are +21/400 and −9/100. Their equal-game mean is −3/160. Complementing both p and Y leaves (p−Y)² unchanged. Adding the opposite side of game 1 therefore copies its evidence; the naive three-row mean becomes +1/200 and reverses sign.

A deliberately predeclared contract-weighted estimand is not mathematically wrong. It is different from equal-game skill, and complements are not independent observations. For the intended primary study, equal-weight games; within each game equal-weight unique subject/market/threshold/book-rule groups in canonical Over orientation, retaining Under for audit only. Same-event sources and quotes remain dependent. This toy has one such group per game, and its helper averages duplicate contributions within games to illustrate the weighting distinction.

Resample whole games with all their paired arm results and within-game weights intact. For the two invented game deltas, the four equally likely ordered two-draw bootstrap means are 21/400, −3/160, −3/160 and −9/100. They illustrate mechanics only. Two games do not validate a confidence interval, asymptotic approximation, population generalization, or an independence assumption across real games.

## 5. Log-loss endpoints

Natural-log loss is −log(probability assigned to the observed outcome). Assigning that outcome probability zero has **infinite** loss, not a finite clipped penalty. Correct certainty has zero loss. Near-one finite probabilities use a numerically stable log1p calculation; arithmetic is still finite-precision for log loss. If both arms have infinite loss, infinity minus infinity is undefined; the helper rejects that comparison. Any finite epsilon-clipping rule would be a different, prospectively specified metric, never a silent repair after results.
