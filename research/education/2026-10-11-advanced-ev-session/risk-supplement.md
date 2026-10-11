# Optional lesson: positive EV does not settle portfolio risk

This supplement extends the correlation and uncertainty discussion. Every price, probability, joint outcome and exposure fraction below is an invented **MODEL ASSUMPTION**. It is not a stake recommendation or an estimate of an actual NFL market. Decimal 1.91 is this supplement’s separate assumed price; it is not the exact −110 price of 21/11 used in the core fixture. The [risk-source register](risk-sources.md) distinguishes two additional transcript reviews from academic papers and preserves the source limitations.

## Same expected profit, different joint downside

**VERIFIED MATHEMATICAL PRINCIPLE.** Imagine two separately settled same-game props, a quarterback passing-yards Over and a receiver receiving-yards Over. Each has stipulated win probability .55, decimal odds 1.91 and no push. Assign an illustrative .03 of starting model wealth to each simultaneously. Both settle against the same starting wealth, rather than being compounded sequentially.

The portfolio returns +.0546 if both win, −.0027 if exactly one wins, and −.06 if both lose.

| Joint event | Independent model | Positively dependent model |
|---|---:|---:|
| Both win | .3025 | .45 |
| First only wins | .2475 | .10 |
| Second only wins | .2475 | .10 |
| Both lose | .2025 | .35 |

Both models retain the same .55 marginal probabilities. The second has indicator correlation about .596; that number is constructed, not estimated.

| Portfolio result | Independent | Positively dependent |
|---|---:|---:|
| Expected return on starting wealth | +.303% | +.303% |
| Return standard deviation | 4.0314% | 5.0929% |
| Expected log growth | .00221329 | .00172558 |
| Probability of losing the full 6% exposure | 20.25% | 35.00% |

Linearity preserves expected profit. It does not preserve variance, loss clustering or expected log growth. For simultaneous positions, a joint calculation uses E[log(1 + f1R1 + f2R2)]. Independent sizing from each marginal probability misses that joint payoff.

**UNTESTED HYPOTHESIS.** Shared pace, weather and opportunity could connect NFL props, but a common narrative supplies no numerical correlation. Compare explicit game/role scenarios and later joint outcomes before attaching precision to that story. This reinforces existing player/game/thesis exposure controls without replacing them.

## Positive arithmetic EV can coexist with negative log growth

**VERIFIED MATHEMATICAL PRINCIPLE.** One invented binary prop at p=.55 and decimal 1.91 has unit EV .0505. With a deliberately oversized fraction f=.20, expected return on model wealth is +1.01%, but expected log growth is:

`g(f) = .55 log(1 + .91f) + .45 log(1 − f) = −.00845024`.

Under the additional assumption of 100 IID repetitions at unchanged terms, mean terminal wealth is 2.73173 times starting wealth while the exact model probability of finishing below the start is about 69.13%. This illustrates the difference between arithmetic mean wealth and the distribution of compound outcomes. Real NFL opportunities do not satisfy those assumptions automatically.

Neither a growth optimum nor an invented exposure fraction is a personal recommendation. Reducing a positive stake cannot change the sign of a negative unit EV.

## Wider parameter uncertainty does not create an automatic one-step penalty

**VERIFIED MATHEMATICAL PRINCIPLE / MODEL ASSUMPTION.** If Y conditional on p is Bernoulli(p) and m is the posterior mean of p, then P(Y=1 | data)=m. For fixed payout b and fixed fraction f, one-step expected log growth is:

`m log(1 + bf) + (1 − m) log(1 − f)`.

Thus two posterior distributions with the same mean produce the same one-step predictive EV and expected-log objective. Merely observing a wider posterior does not, by itself, derive a fractional-exposure rule from this objective.

This does not make model risk irrelevant. A misspecified posterior can be confidently wrong. Future outcomes sharing an unknown p can also be dependent: under conditional independence given p, Cov(Yi,Yj | data)=Var(p | data). Matching single-event means does not match portfolio downside. The earlier known-p IID terminal-loss calculation must not be transferred unchanged to this shared-latent-p model.

**VERIFIED MATHEMATICAL PRINCIPLE**, distinguishing decision criteria. Keep three choices distinct: Bayesian averaging under a model; worst-case optimization over an explicitly chosen uncertainty set; and a preference or constraint on downside. They answer different decision questions. For example, a robust set containing p=.51 at decimal 1.91 includes a negative-EV model; with only that bet and cash permitted, the worst-case log criterion selects no positive exposure.

The academic risk-constraint paper reviewed here controls falling below a fraction of **initial** wealth under its assumptions. That is not a universal ceiling on peak-to-trough drawdown. No paper or interview in this review establishes a safe universal betting fraction.

## Review-only clarification of existing policy

**VERIFIED MATHEMATICAL PRINCIPLE; review-only METHODOLOGY_CHALLENGE.** Section 15 of the existing framework cautions that full Kelly assumes a known true edge. That is a useful warning about a simple plug-in calculation. The narrower clarification is that posterior-predictive expected-log optimization can also be mathematically coherent without knowing a latent probability, conditional on its model and objective. It does not establish model accuracy or justify increasing exposure. Current small-unit, fractional-reference and player/game/thesis caps remain controlling and unchanged.

## Status

These are educational payoff calculations and review proposals. They introduce no bankroll amount, live wager, revised exposure cap or automated sizing procedure. The [standard-library risk calculator](verify_risk_math.py) passes its payoff-invariant assertions; its [results](risk_results.json) pass [37 independent high-precision checks](risk_crosscheck.py), with [separate outputs](risk_crosscheck_results.json). Reproduce them with `python verify_risk_math.py > risk_results.json`. Package-level verification is recorded in the final manifest.
