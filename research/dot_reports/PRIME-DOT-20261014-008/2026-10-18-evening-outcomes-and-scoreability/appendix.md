# Settlement-label ambiguity can reverse a forecast ranking

Synthetic education example for 18 October 2026. No real bookmaker rule, football event, price, bet, or provider data is used. This is a scoring illustration, not betting advice.

## 1. Define the target before scoring

Suppose settlement has exactly three mutually exclusive and exhaustive states:
- W: win
- L: loss
- V: full stake refund, zero net profit

Knowing a football statistic is not, by itself, enough to assign a bookmaker-specific settlement label when the applicable contract and settlement evidence remain unverified. That mapping is a separate evidentiary step. In this example, assume W has been ruled out but the label is unresolved between L and V. “Unknown” is a status of our evidence, not another outcome and not a synonym for loss.

Freeze two full three-state forecasts before resolution, in W, L, V order:
- A = (1/2, 1/5, 3/10)
- B = (1/2, 2/5, 1/10)

Each contains finite nonnegative probabilities summing exactly to one.

## 2. Calculate every possible realized score

Use the unnormalized categorical Brier loss for one observation:

BS(p, y) = sum over k in {W,L,V} of (p[k] − indicator(y=k))².

“Unnormalized” here means no division by two and no averaging over the three classes. Lower is better. Its range is 0 to 2. The [official scikit-learn definition](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss) states the categorical formula as a sum across classes, averaged across observations; here there is only one observation.

| Realized state | A | B | Paired A − B | Lower loss |
|---|---:|---:|---:|---|
| W | 19/50 = 0.38 | 21/50 = 0.42 | −1/25 = −0.04 | A |
| L | 49/50 = 0.98 | 31/50 = 0.62 | 9/25 = 0.36 | B |
| V | 39/50 = 0.78 | 61/50 = 1.22 | −11/25 = −0.44 | A |

Independent algebraic check: BS(p,y) = 1 + sum(p[k]²) − 2p[y]. The squared-probability sums are 19/50 for A and 21/50 for B.

If the true label remains in {L,V}, the exact set of possible realized paired differences is {−11/25, 9/25}; its sharp enclosing interval is [−0.44, 0.36]. Compare both forecasts under the same candidate label. The interval straddles zero, so the ranking is unresolved: B wins if L is correct; A wins if V is correct. These are label-ambiguity bounds, not a sampling confidence interval. Intermediate interval points are not additional realized labels.

If a separately justified probability r is assigned to L conditional on {L,V}, the expected paired loss is 0.80r − 0.44. It is zero at r = 11/20. This sensitivity calculation supplies no reason to assume r = 1/2 or to invent an evidence-based r.

## 3. Keep conditional and full forecasts distinct

A conditional-on-action binary forecast concerns W given W or L:

q = P(W) / [P(W) + P(L)].

Thus q_A = 5/7 and q_B = 5/9. These are different targets from the full vectors above, despite both forecasts assigning unconditional win probability 1/2. The conditional forecast is undefined when P(W)+P(L)=0. It contains no standalone forecast of refunds.

A predeclared conditional evaluation can score q on verified W/L cases, report its coverage and exclusions, and keep V cases in the audit record. Its common binary Brier loss is (q−indicator(W))², with range 0 to 1. It is not numerically interchangeable with the three-class sum. Do not retrospectively discard refunds to improve the apparent performance of a full three-state forecast, or silently switch targets after seeing results. For the full target, V is a legitimate scored outcome. An unresolved label should remain unresolved, with bounds if appropriate; it must not automatically map to L.

## 4. Optional expected-value identity

For one unit staked, fictional decimal odds d, and the full-refund scheme defined above, net payoffs are d−1 at W, −1 at L, and 0 at V:

EV = (d−1)P(W) − P(L).

When action probability a=P(W)+P(L)>0, the equivalent identity is EV = a(dq−1). Using q alone in dq−1 gives expected net profit conditional on action, not unconditional net profit per unit initially staked. At an entirely illustrative d=2, A gives EV=3/10 and B gives EV=1/10. These are hypothetical model outputs, not actual prices, settlement rules, or evidence of an available edge.

## 5. Reproduce

Run `python3 settlement_label_bounds.py` from this directory. It requires only the Python standard library. Ten tests check the six scores against fixed exact fractions and an independent identity, paired bounds and ranking reversal, unknown-label rejection, forecast state schema, normalization, nonnegativity, finite/exact inputs, candidate states, conditional probabilities, EV, and Brier extremes. The script rejects floats rather than silently importing binary rounding into exact rational calculations. See `test_results.txt` for the captured successful run.

The tests validate this deliberately small synthetic calculation. They do not validate any live dataset, bookmaker settlement, production implementation, model calibration, or profitable strategy.
