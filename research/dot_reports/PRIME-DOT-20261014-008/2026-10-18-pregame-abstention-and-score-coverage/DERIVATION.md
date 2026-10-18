# A selective score is not an end-to-end forecasting score

## Scope and status

This is an invented, deterministic teaching fixture. It contains no observed sports data, provider calls, bankroll simulation, profitability estimate, significance test, or production change. Every conclusion below describes these specific invented rows or a mathematical identity. No out-of-sample result is established.

All 50 units are distinct binary, no-push events. A probability always means the affirmative event occurs, and each underlying event receives equal weight once. “Market” is just the name of the supplied synthetic reference probability. No implied-price, de-vig, or conditional-on-no-push conversion is performed or validated here.

We use the Bernoulli Brier loss L(p,y)=(p−y)², with range [0,1]. Summing squared errors for both entries of a two-class probability vector would double this convention. Log loss is −y ln p−(1−y) ln(1−p), in natural-log nats. Lower is better for both.

## Contract fixed before labels

The cohort, canonical event IDs, event orientation, reference forecasts, model forecasts, model abstention mask, fallback rule, 25% model mixture weight, and optional missing-outcome mask are specified before the invented outcomes are attached. This ordering documents the lesson's contract; it does not create prospective empirical evidence.

- Easy: 10 cases; market p=0.9; model p=0.7; labels are 9 ones and 1 zero.
- Hard: 40 cases; market p=0.5; model deliberately ABSTAINS; labels are 20 ones and 20 zeros.
- Model coverage: 10/50=20%.
- End-to-end fallback: use the model on its covered cases and the reference elsewhere.
- Fixed mixture: on covered cases use 0.25×0.7+0.75×0.9=0.85, and elsewhere use the reference.

An ABSTAIN has a null model probability. It is neither p=0 nor an omitted observation from the full-policy score. The policy forecast on an abstention is the separately specified fallback probability.

## Exact Brier arithmetic

Easy reference mean: [9(0.1²)+0.9²]/10=9/100=0.09.

Easy model mean: [9(0.3²)+0.7²]/10=13/100=0.13.

Easy mixture mean: [9(0.15²)+0.85²]/10=37/400=0.0925.

Every hard-case Brier loss is 0.25. Therefore:

| Quantity | Denominator | Exact value | Decimal |
|---|---:|---:|---:|
| Reference on all cases | 50 | 109/500 | 0.218 |
| Model on covered cases only | 10 | 13/100 | 0.130 |
| Reference on those same covered cases | 10 | 9/100 | 0.090 |
| Model-or-reference full policy | 50 | 113/500 | 0.226 |
| Fixed mixture on covered cases | 10 | 37/400 | 0.0925 |
| Fixed mixture-or-reference full policy | 50 | 437/2000 | 0.2185 |

Comparing 0.130 with 0.218 mixes two populations. The paired covered comparison instead yields 0.130−0.090=0.040 against the model. The full fallback policy loses by 0.226−0.218=0.008. The mixture fallback loses by 0.2185−0.218=0.0005. Positive differences here mean higher loss.

The full-policy difference is exactly coverage times its covered-case difference because fallback and reference are identical elsewhere: 0.2×0.04=0.008, and 0.2×0.0025=0.0005. This is an accounting identity for this policy and fixed cohort, not an estimated causal effect or evidence of future performance.

## Proper log-loss arithmetic

Let h(p)=−0.9 ln p−0.1 ln(1−p) for the fixed easy outcomes. Then h(0.9)=0.3250829733914482, h(0.7)=0.4414047299774528, and h(0.85)=0.33597903503658555. Every hard-case log loss is ln 2.

| Quantity | Exact mathematical expression | Value (nats) |
|---|---|---:|
| Reference, covered | h(0.9) | 0.3250829733914482 |
| Model, covered | h(0.7) | 0.4414047299774528 |
| Mixture, covered | h(0.85) | 0.33597903503658555 |
| Reference, all | 0.2h(0.9)+0.8 ln 2 | 0.6195343391262459 |
| Model-or-reference, all | 0.2h(0.7)+0.8 ln 2 | 0.6427986904434468 |
| Mixture-or-reference, all | 0.2h(0.85)+0.8 ln 2 | 0.6217135514552734 |

The full-policy log-loss differences are +0.02326435131720095 and +0.0021792123290275134 nats. The program computes finite sums; displayed decimal representations are floating-point approximations to the stated exact logarithmic expressions.

## What propriety does and does not establish

If a real binary outcome had a true conditional probability q, its expected Brier loss would be q(1−q)+(p−q)². Its expected log loss would be H(q)+KL(Bernoulli(q) || Bernoulli(p)), subject to endpoint conventions. These identities explain strict propriety on a fixed target distribution.

Here the 9/10 and 20/40 proportions are imposed labels, not estimates of validated real conditional probabilities. The finite empirical loss is minimized by the within-group sample frequency, but that does not establish the reference as the true data-generating probability. No sampling scheme, effective independent sample size, uncertainty interval, p-value, calibration claim, future edge, or financial expectation follows from this fixture.

Proper scoring of a selected population does not by itself fix selection into that population. A model comparison on the common covered cases answers a conditional forecast question. A full-cohort, frozen-fallback score answers a policy question. Report both with their distinct denominators. Equal coverage rates alone would not imply equal selected populations.

A predeclared probability mixture is a genuine forecast. Convexity makes its loss no worse than the corresponding weighted average of its component losses on a given case; it does not ensure improvement over the better component. The mixture weight cannot be tuned on these evaluated outcomes and then reported as predeclared.

## Optional check: even equal coverage and a common-case win are insufficient

A separate compact construction has 30 equal-weight invented cases: 10 easy (9 positives), 10 common (7 positives), and 10 hard (5 positives). Reference probabilities are 0.90, 0.65, and 0.65. A predicts 0.85 on easy and 0.68 on common, then abstains on hard. B abstains on easy, then predicts 0.66 on common and 0.50 on hard. Each source covers 20/30 cases; both policies use the same reference whenever their source abstains.

A has the lower own-covered Brier (0.15145 versus 0.2308), and also wins on the 10 common covered cases (0.2104 versus 0.2116). Yet A's full-policy Brier is 0.1918 and B's is 0.1838666667. The reference-only policy scores 0.1916666667. Thus the different routing decisions reverse the full-policy ranking even after the conditional common-case comparison has been made correctly. Full-policy log losses similarly favor B: A 0.5626918590 versus B 0.5442446210 nats.

For any two frozen policies using the same fallback m, partition events into both-covered, A-only, B-only, and neither. Their full-cohort total loss difference is:

N×(policy A mean − policy B mean) = Σboth(L_A−L_B) + ΣA-only(L_A−L_m) + ΣB-only(L_m−L_B), with zero contribution from neither.

Here the exact Brier contributions are −3/250, +1/40, and +9/40. Their sum divided by 30 is 119/15000=0.0079333333 against A. A's small common-case advantage does not compensate for missing the cases where B improves most on the reference. This demonstrates why conditional model quality and full-policy value are different questions; no empirical effect is claimed.

## Missing outcomes: identification intervals, not confidence intervals

Let N be the fixed target-cohort size, O the observed-outcome IDs, M the missing-outcome IDs, and p_i a known, already fixed forecast for every ID. Missing outcomes remain null; neither y=0 nor a loss of zero may be substituted.

For Brier loss, define S_O=Σ(i∈O)(p_i−y_i)². With no assumptions on missing binary outcomes, the sharp full-cohort bounds are:

Lower = [S_O+Σ(i∈M) min{p_i²,(1−p_i)²}]/N.

Upper = [S_O+Σ(i∈M) max{p_i²,(1−p_i)²}]/N.

They are sharp because, absent cross-case restrictions, each missing binary label can attain its lower or upper endpoint. This construction has no linked-outcome restrictions. For nested thresholds, complementary sides, or contracts with a shared settlement, feasibility can constrain joint completions: summing per-row extrema then gives valid outer bounds, but the endpoints need not be jointly attainable. Sharp linked-contract bounds must optimize over the allowed joint outcomes. They are tighter than the coarse [S_O/N,(S_O+|M|)/N] bounds. The denominator stays N. If forecasts themselves are unavailable, these fixed-forecast bounds are not applicable until the predeclared policy defines those forecasts; an unrecorded prediction is not an outcome-missingness problem.

For a paired comparison of fixed forecasts p_i and q_i on the same outcome, use d_i(y)=(p_i−y)²−(q_i−y)². An unknown label contributes either d_i(0)=p_i²−q_i² or d_i(1)=(1−p_i)²−(1−q_i)². Sum the smaller/larger of these two values per missing event, plus observed differences, and divide by N. Subtracting separate score intervals can be unnecessarily loose because both forecasts share the same unknown outcome. In particular, p_i=q_i gives an exactly zero paired difference even when y_i is missing.

### Masked demonstration

The optional demonstration fixes the mask from event IDs before labels: hide ID suffixes divisible by 10. This hides 1 easy and 4 hard outcomes, leaving 45 observed outcomes in a 50-case target population. This is a deterministic illustration, not a missing-at-random assertion.

- Observed-only reference Brier: 0.202 on 45 cases.
- Full-50 reference Brier identification interval: [0.202, 0.218].
- Observed-only fallback Brier: 0.218 on 45 cases.
- Full-50 fallback Brier identification interval: [0.218, 0.226].
- Paired full-50 fallback-minus-reference interval: [0.008, 0.016].

Some observed-only numbers happen to coincide with interval endpoints; the denominators and meanings remain different. The known labels in the complete invented fixture attain the stated upper score bounds and lower paired-difference bound. Do not present these identification intervals as statistical confidence intervals.

## Log-loss bounds and ex ante clipping

If both paired aggregate log losses are infinite, their difference is undefined; the implementation rejects that comparison rather than returning NaN or silently treating it as a tie. A one-sided infinite aggregate gives the corresponding positive or negative infinite difference. Neither case licenses retroactive clipping.

Log loss without a probability restriction has no uniform finite upper bound: a confidently wrong p=0 or p=1 produces infinity, and approaching the wrong endpoint produces arbitrarily large loss. For fixed known probabilities strictly between 0 and 1, finite forecast-specific bounds do exist without clipping. That narrower mathematical fact is distinct from a guaranteed uniform bound for an unrestricted forecasting system.

If the protocol declares 0<epsilon<1/2 and guarantees p_i∈[epsilon,1−epsilon], every loss lies between −ln(1−epsilon) and −ln epsilon. Each missing outcome contributes a sharp lower bound −ln max(p_i,1−p_i) and upper bound −ln min(p_i,1−p_i). Add observed losses and divide by the original N.

The demonstration declares epsilon=0.01 for its bound checks. Every existing probability already satisfies that envelope, so no fixture forecast changes. The bound function validates the declaration and rejects out-of-envelope forecasts; it never clips automatically.

If clipping is needed, p'_i=min(1−epsilon,max(epsilon,p_i)) is a different forecast. Both the transformation and epsilon must be fixed before the evaluation outcomes, applied consistently to all compared systems, and disclosed. Retroactive clipping to remove infinite losses or change a ranking is forbidden. A purely mathematical post-hoc sensitivity calculation, if separately labeled, cannot replace the original forecast's score or be represented as prospective evidence.

## Abstention, operational missingness, and observation are different

1. Chosen abstention: a pre-outcome decision under a recorded policy. Report its coverage and score the declared fallback over the full eligible cohort.
2. Operational prediction missingness: a request failure, timeout, invalid schema, unavailable input, or unrecorded output. Preserve a distinct status and reason. Do not relabel it ABSTAIN after the fact. A protocol may predeclare a fallback for these failures, but this fixture does not; its validator stops on MISSING.
3. Outcome missingness: the forecast exists, but the settlement or label is unavailable at the evaluation cutoff. Retain the event in the target cohort; report the observed mask and identification bounds unless a separately justified estimation method applies.

Eligibility, prediction-time status, fallback policy, and planned observation process must be frozen before outcomes are used for selection. A planned observation mask is not proof that all labels will arrive: unexpected post-freeze availability failures remain separately logged missing outcomes. In a real retrospective extraction, record the availability mask before unblinding or using outcome values; do not claim this makes the missingness random. Pushes or multi-outcome settlements require an appropriately declared probability/settlement model; silently dropping them after the fact changes the estimand.

## Complementary sides and denominator discipline

An affirmative row (p,y) and its complementary row (1−p,1−y) have identical Brier and log losses. They are two encodings of one binary outcome, not two independent observations. Counting both uniformly may leave the numerical mean unchanged while falsely inflating the sample count; unequal side duplication can also change the mean. The fixture uses one canonical row per underlying event and rejects duplicate IDs and noncanonical sides.

Every paired score requires an explicit, nonempty, duplicate-free cohort with both forecasts and an observed outcome for every included ID. It does not silently intersect available keys, drop null outcomes, turn abstentions into probabilities, or mix probability bases.

## Reproduction and relation to prior material

Run `python -m unittest -v` and `python score_fixture.py` from this directory. Only the Python standard library is used. `fixture.json` contains the 50 invented records; `results.json` records exact Brier fractions and approximate log losses. `SHA256SUMS.json` covers the stable source, test, fixture, results, and this note. Verification evidence records an initial expected-red suite followed by the passing suite. The final suite has 34 tests, including an independently identified infinity-minus-infinity regression. Hashes identify the recorded bytes; regeneration is checked in the current Python runtime. Last-digit floating-point log representations can differ across mathematical-library implementations, while the displayed exact Brier fractions and symbolic logarithmic expressions do not.

The distinct lesson is selection/coverage, frozen fallback policy evaluation, and missing-label partial identification under proper losses. It does not repeat a shared-baseline correlation analysis and makes no claim that correlation or a weak baseline establishes edge.
