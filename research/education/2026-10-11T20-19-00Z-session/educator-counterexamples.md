# Original educational counterexamples for PRIME

Prepared: 2026-10-11. Scope: NFL player-prop research. These examples are original mathematical constructions. All probabilities, payouts and groups below are hypothetical. They are not named-player forecasts, live quotes or evidence of an empirical betting edge. Arithmetic was checked independently using exact rational calculations where applicable.

## 1. Aggregate calibration can conceal a losing selected subset

### Assumptions

- There are two equally frequent groups of eligible binary, no-push prop observations, A and B.
- The model predicts 55% for every observation.
- True probabilities are 45% in A and 65% in B.
- Available decimal odds are 2.00 for A and 5/3 (American −150) for B.
- The selection rule accepts observations when estimated unit-stake EV = predicted probability × decimal odds − 1 is positive.
- This is a population-level construction. A finite sample need not realize these frequencies exactly.

### Calculation

Across both groups, the true mean event probability is:

0.5 × 0.45 + 0.5 × 0.65 = 0.55.

Thus, the set of 55% forecasts is calibrated in aggregate. But the model selects only A:

| Group | Model probability | True probability | Decimal odds | Estimated EV | True EV |
|---|---:|---:|---:|---:|---:|
| A | 55% | 45% | 2.00 | +10.00% | −10.00% |
| B | 55% | 65% | 5/3 | −8.33333% | +8.33333% |

The true win rate of the selected observations is 45%, despite a predicted 55%. Available prices identify a subgroup with systematically negative model errors. No general theorem allows aggregate calibration to be transferred unchanged to a subset selected using additional information.

**VERIFIED MATHEMATICAL PRINCIPLE — high confidence:** aggregate calibration is insufficient for positive EV on a price-selected subset. It also does not prove every individual probability is accurate. Conversely, a miscalibrated model can still make some profitable decisions: predicting 55% when truth is 65% at even money understates an actually positive EV.

### NFL application and falsifiable test

Freeze the exact eligibility and price-selection rules before evaluating outcomes. Report calibration for all eligible forecasts and the selected subset separately, with prespecified reception/yardage/TD groups, threshold bands, quote timing and role-uncertainty conditions. Preserve serious passes and unavailable quotes so execution selection remains visible.

**UNTESTED HYPOTHESIS:** selection-conditioned evaluation will reveal errors hidden by overall calibration. A failure case is persistent selected-subset miscalibration despite acceptable overall results. Estimate uncertainty with game/week and repeated-player dependence accounted for; do not select favorable subgroups after seeing results. This supplements PRIME's existing calibration rules.

## 2. Posted two-sided odds do not uniquely identify fair probability

### Assumptions

- Over −120 and Under +100 are simultaneous quotes from one reference book for exactly the same binary, no-push contract.
- Both outcomes exhaust all settlement possibilities.
- For the interval calculation only, assume the bookmaker has nonnegative expected profit on each individual side at the unknown true probability p.
- That last assumption is not guaranteed by posted odds. A stale or mistaken reference may offer positive EV on one side.

### Derivation

Reference decimal prices are dO = 11/6 and dU = 2. Their raw implied probabilities are qO = 6/11 and qU = 1/2.

For the bookmaker's expected profit on an Over bet to be nonnegative:

1 − p × dO ≥ 0, so p ≤ 1/dO = 6/11.

For its expected profit on an Under bet to be nonnegative:

1 − (1 − p) × dU ≥ 0, so p ≥ 1 − 1/dU = 1/2.

The assumptions therefore allow every probability in:

50% ≤ p ≤ 54.54545%.

Proportional de-vigging picks one point:

p_normalized = (6/11) / ((6/11) + (1/2)) = 12/23 = 52.17391%.

Now suppose a different book offers the same Over at −105, decimal odds 41/21:

| Probability used | EV = p × (41/21) − 1 |
|---|---:|
| 1/2 | −1/42 = −2.38095% |
| 12/23 | 3/161 = +1.86335% |
| 6/11 | 5/77 = +6.49351% |

**VERIFIED MATHEMATICAL PRINCIPLE — high confidence:** the same reference quotes can be compatible with probabilities producing opposite EV signs under different margin allocations. Normalization is an estimation choice, not identification of truth.

This interval is neither a statistical confidence interval nor a universal no-arbitrage bound on true probability. It follows from the explicit per-side nonnegative-margin assumption. It is not proposed as an automatic replacement for PRIME's uncertainty method. Pushes, voids, partial settlements and fees require a different contract calculation.

### NFL application and falsifiable test

Preserve both reference sides, book, threshold, timestamp and settlement rules. Separate player-model uncertainty from uncertainty about market reference and margin allocation. Test competing reference/de-vig approaches on untouched NFL-prop outcomes and compare selection-conditioned calibration, proper scores and executable-price results. Agreement among methods using the same underlying quotes is not independent confirmation.

**UNTESTED HYPOTHESIS:** some apparent small edges will disappear under defensible reference assumptions. Record those sign reversals; do not retrofit the method to retain a desired bet.

## 3. Exact-threshold probabilities must form a coherent survival ladder

### Assumptions and identities

Let Y be the integer-valued receiving-yard outcome under a specified settlement rule. Define S(k) = P(Y ≥ k).

Because {Y ≥ k + 1} is a subset of {Y ≥ k}:

- 1 ≥ S(k) ≥ S(k + 1) ≥ 0.
- P(Y = k) = S(k) − S(k + 1).
- P(a ≤ Y ≤ b) = S(a) − S(b + 1) for integers a ≤ b.

For example, S(50) = 0.60 and S(60) = 0.40 imply a 20% probability of 50–59 yards. Conversely, S(50) = 0.55 and S(60) = 0.60 imply a negative 5% probability for that band, which is impossible.

For an integer Over 50 contract with refunds on an exact-50 push:

- p_win = S(51).
- p_push = S(50) − S(51).
- p_loss = 1 − S(50).
- EV = p_win × (d − 1) − p_loss.

A coherent illustrative ladder with S(50) = 0.60 and S(51) = 0.58 gives p_win = 0.58, p_push = 0.02 and p_loss = 0.40. At decimal odds 1.90, EV = 0.58 × 0.90 − 0.40 = +0.122, or +12.2%. The assumed probabilities are illustrative, not calibrated NFL estimates.

**VERIFIED MATHEMATICAL PRINCIPLE — high confidence:** independent threshold predictions must satisfy these identities to represent one distribution. Coherence is necessary, but does not establish accuracy.

### NFL application and falsifiable test

Run synthetic and frozen-forecast checks for monotonicity, probability bounds, nonnegative point mass, and win/loss/push probabilities summing to one. Check after any calibration or shrinkage stage, not merely before it. Apply only across matching player/event/stat/period/settlement contracts; Over 50, 50+ and Over 50.5 are different propositions.

**UNTESTED HYPOTHESIS:** a ladder-integrity check can prevent mathematically impossible exact-threshold prices. Any negative mass or increasing survival probability is a deterministic failure. If a repair method is proposed, fit it without test-set outcomes and compare its held-out calibration; monotonic repair alone is not proof of improved forecasts.

## Evidence status and preservation

The mathematical examples are completed arithmetic checks. No empirical NFL test, production gate, model weight, reference-book authority or methodology change was implemented. Test designs require complete timestamped forecasts, quotes, settlements, prespecified exclusions and adequate independent observations. Preserve original failed predictions and proposed repairs separately.
