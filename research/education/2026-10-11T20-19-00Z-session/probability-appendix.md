# PRIME probability and price stress tests

Prepared 2026-10-11. Synthetic demonstration, not historical NFL evidence.

## Purpose
These deliberately constructed examples test mathematical consistency. They do not estimate any NFL player's distribution, validate a profitable strategy, or authorize a live bet. Every probability, role scenario and price is hypothetical. The current report's emphasis on exact contracts, uncertainty and correlation is supported; these fixtures make common failure modes observable. No PRIME code or configuration was changed.

## Reproduction

Copy this directory to a working folder before rerunning, so the preserved research record stays unchanged. The scripts write their result files beside themselves.

Run [verify_examples.py](verify_examples.py) with Python 3. It uses standard-library Fraction arithmetic for the discrete examples and writes [results.json](results.json). Joint-correlation calculations use a square root in double precision. All implemented assertions passed. For the independent distribution check, run [crosscheck_scipy.py](crosscheck_scipy.py) in an environment with SciPy installed; the recorded run used SciPy 1.17.0. It matched every checked PMF cell and threshold survival probability for the binomial and beta-binomial examples within 1e-12; maximum PMF error was 1.11e-16. Details are in [crosscheck_scipy.json](crosscheck_scipy.json). These checks validate the calculations, not the modeling assumptions.

## Convention
Decimal odds d include returned stake. For a binary, no-push, unit-stake contract, ROI = p*d - 1. At -110, d=21/11 and break-even p=11/21=52.38095238%. A zero-EV price is a boundary, not a positive edge. Apply an explicit margin if a policy requires one.

## 1 Receiving yards with the same mean and median

Hypothetical WR, Over 49.5 receiving yards at -110.

Distribution A: Y=20 with probability 0.40; Y=60 with 0.20; Y=100 with 0.40.
Distribution B: Y=40 with probability 0.49; Y=60 with 0.02; Y=80 with 0.49.

Both have E[Y]=60 and unique median 60. But the exact contract is Y>=50:

```text
  A: p=0.60; ROI=0.60*(21/11)-1=+14.545455%.
  B: p=0.51; ROI=0.51*(21/11)-1=-2.636364%.
```

Conclusion: neither a mean, a median, nor both together identify this threshold probability. Replacing the mean with the median does not solve the missing-distribution problem. This is a mathematical counterexample, not a proposed three-point yardage model. A sportsbook line and its price are also distinct inputs; a posted line need not equal a true median.

Test priority: a forecast cannot acquire a numeric edge merely because a projected mean or median exceeds the offered line. Require an auditable distribution/CDF or an independently justified direct event-probability model. Original calculation; no external performance claim.

## 2 Receptions with fixed or random opportunity

Hypothetical WR, Over 4.5 receptions at -110. Let R be receptions.

A. Fixed targets: N=8 and R|N ~ Binomial(8,0.65).

```text
  P(R>=5)=sum[r=5..8] choose(8,r)*0.65^r*0.35^(8-r)
          =0.7063994361328125.
  E[R]=5.2; Var(R)=1.82; ROI=+34.858074%.
```

B. Random targets: choose N=4 or N=12 with equal probability before the game's catches, then use R|N ~ Binomial(N,0.65).

```text
  E[N]=8, the same as A; E[R]=5.2, also the same.
  P(R>=5)=0.5*P(Binomial(4,0.65)>=5)
         +0.5*P(Binomial(12,0.65)>=5)
         =0.4872462715005457.
  Var(R)=0.65*0.35*E[N]+0.65^2*Var(N)
        =1.82+0.4225*16=8.58.
  ROI=-6.980257%.
```

Replacing N by its mean reversed the sign of EV. The mixture is intentionally broad to expose the failure; it is not evidence that real target forecasts have this distribution.

C. Shared catch probability: fix N=8, draw one common theta~Beta(6.5,3.5), then let catches be conditionally independent Bernoulli(theta). The marginal R is beta-binomial:

```text
  P(R=r)=choose(8,r)*B(r+6.5,8-r+3.5)/B(6.5,3.5).
  E[theta]=0.65; E[R]=5.2.
  Var(R)=8*0.65*0.35*[1+7/(6.5+3.5+1)]=2.9781818182.
  P(R>=5)=0.6699981689453125; ROI=+27.908741%.
```

More dispersion does not raise every upper-tail probability: compared with A, model C reduces P(R>=5) from 70.64% to 67.00%, but increases P(R>=8) from 3.19% to 8.18%.

Assumptions/failure modes:
  - A binomial requires a fixed count and equal independent success probabilities under the conditioning used. Real targets can depend on game script, role, previous plays and opponent response.
  - Beta-binomial overdispersion here requires a COMMON theta across targets. Drawing a fresh independent theta_i from the same beta distribution for each target leaves the marginal catches independent Bernoulli(0.65), hence a binomial count.
  - A shared theta can represent game-level heterogeneity or uncertainty about a common parameter. Their marginal predictive mathematics may match, but their interpretation and dependence across future games need not.
  - If N and theta are dependent, integrate their JOINT distribution. E[N*theta] is not generally E[N]*E[theta]. Do not stack arbitrary variance inflations and count the same uncertainty twice.
  - A general conditional-binomial model uses P(R>=k|data)=sum_n integral P(Binomial(n,theta)>=k)*p(n,theta|data) dtheta. Its realism still needs held-out tests.

References for the calculations: Penn State's binomial conditions [1], official SciPy beta-binomial PMF [2], and Harvard's conditional-variance identity [3]. None establishes the best NFL model.

## 3 Rushing yards and probability uncertainty

Hypothetical RB, Over 59.5 rushing yards at -110. Suppose uncertainty about the event probability p is represented by two equally weighted parameter scenarios:

- Narrow: p is 0.53 or 0.57.
- Wide: p is 0.49 or 0.61.

Both have E[p]=0.55, so the probability-weighted expected ROI is +5.00% in both cases. For the single win indicator X|p~Bernoulli(p):

```text
  Var(X)=E[p*(1-p)]+Var(p)=E[p]*(1-E[p])=0.2475.
  Narrow: 0.2471+0.0004=0.2475.
  Wide:   0.2439+0.0036=0.2475.
```

Wider parameter uncertainty has not changed this single-bet predictive variance or expected ROI. It has changed how robust the claimed edge is to the supplied scenarios. If a separately chosen decision policy uses the worst supplied scenario p_L:

```text
  Narrow p_L=0.53: ROI at -110 is +1.181818%.
  Wide p_L=0.49: ROI at -110 is -6.454545%.
```

For a required expected ROI r under p_L, minimum acceptable decimal odds are d_min=(1+r)/p_L. Higher decimal odds are better for the bettor.

```text
  At r=0:
    Narrow: d_min=1.886792453, equivalent American -112.765957.
    Wide: d_min=2.040816327, equivalent American +104.081633.
  At an ILLUSTRATIVE r=5%:
    Narrow: d_min=1.981132075, equivalent American -101.923077.
    Wide: d_min=2.142857143, equivalent American +114.285714.
```

These are exact boundaries, not rounded executable quotes. For a whole-number quote to satisfy the 5% hurdle here, -101 is sufficient in the narrow case and +115 in the wide case; -102 and +114 respectively are insufficient. The 5% hurdle is illustrative and does not create a new universal PRIME rule.

These are isolated adverse-ROI boundaries, not complete PRIME play-to prices. The [combined-gate supplement](combined-gates.md) applies the distinct central-edge, central-ROI and positive adverse-EV checks together, producing different boundaries under its stated nominal gates.

Assumptions/failure modes: these two-point scenarios are not a statistically estimated confidence interval. Neither the central 55% nor its low scenario is validated. A conservative haircut, posterior quantile or worst-case bound is an explicit decision rule; its calibration and rationale must be tested. Do not score a lower-bound decision probability as though it were the central predictive probability. Wider parameter uncertainty does not mechanically force lower expected EV when the mean is unchanged. Shared uncertainty can still induce dependence across repeated bets. The variance identity follows from [3]; prices and scenarios are original calculations.

## 4 QB and WR joint probability and payout

Hypothetical same-game events A=QB Over 249.5 passing yards and B=WR Over 69.5 receiving yards. Assume p_A=0.60 and p_B=0.55. Proposed combined payout is +200, d=3. The independence product is 0.33 and ROI=-1.00%.

For CORRELATION OF THE TWO WIN INDICATORS, rho:

```text
  j=P(A and B)=p_A*p_B+rho*sqrt[p_A*(1-p_A)*p_B*(1-p_B)].
  rho=-0.20: j=0.2812557696; ROI at +200=-15.623269%.
  rho= 0.00: j=0.3300000000; ROI at +200= -1.000000%.
  rho=+0.20: j=0.3787442304; ROI at +200=+13.623269%.
```

Every row defines a valid 2x2 probability table with cells j, p_A-j, p_B-j and 1-p_A-p_B+j. The permitted joint range from the marginals alone is [max(0,p_A+p_B-1),min(p_A,p_B)]=[0.15,0.55]. A sensitivity range is not an estimated rho.

A concrete dependence mechanism: let high/low passing scripts each have 50% probability. Under high script, use (P(A),P(B))=(0.80,0.75); under low script use (0.40,0.35). Assume the two events independent CONDITIONAL on script. The unconditional marginals remain (0.60,0.55), but j=0.5*(0.80*0.75)+0.5*(0.40*0.35)=0.37. ROI is +11.00% at +200 and -7.50% at +150. Positive dependence is not a free edge when the book changes the payout.

Assumptions/failure modes: never plug the Pearson correlation of the underlying yard totals into the binary-indicator formula. Tail dependence at these exact thresholds must be estimated or simulated from a specified joint model. Changing a line changes the event and generally its indicator correlation. With three or more legs, pairwise correlations do not in general identify the full joint win probability. Voids, pushes and settlement repricing must match the actual contract. Covariance/correlation definitions are supported by Penn State [4]; all scenarios are invented.

## Brier score and calibration

Construct 200 synthetic binary prop outcomes, with 20 wins among the first 100 and 80 among the second 100. This is an arithmetic fixture, not a historical sample.

```text
  Model A predicts 50% for every event: Brier=0.25; reliability=0; resolution=0.
  Model B predicts 30% for the first group and 70% for the second: Brier=0.17; reliability=0.01; resolution=0.09.
  Model C predicts 20% and 80%: Brier=0.16; reliability=0; resolution=0.09.
```

The sample outcome-uncertainty term is 0.25 for all three, and Brier=reliability-resolution+uncertainty. Model B has a better Brier score than A despite WORSE reliability in the distinct-probability bins. C improves on B without sacrificing resolution. Exact forecast values define the bins here; arbitrary coarse binning has additional caveats.

Brier remains a useful proper score; this example is a warning against naming it a pure calibration metric. In genuine testing, report reliability curves, counts and uncertainty alongside proper scores. Perfect reliability in this invented sample says nothing about NFL population calibration. Use held-out central forecasts, preserve selection rules, and handle clustering and outcome eligibility prospectively. Original fixture, consistent with original scoring-rule research [5] and official calibration documentation [6].

## Pushes and conditional market probabilities

Hypothetical integer line with p_win=0.50, p_loss=0.40, p_push=0.10 at -110:

```text
  Correct ROI=0.50*(10/11)-0.40=+5.454545%.
  Incorrect p_win*d-1=-4.545455%, which silently treats the push as a loss.
  q=P(win|no push)=0.50/0.90=55.555556%.
  ROI=(1-p_push)*(q*d-1).
```

At a fair price d=(1-p_push)/p_win, so 1/d is the conditional-on-no-push win probability. On push-capable, complementary same-line contracts, normalized two-sided reciprocal prices are interpreted on this conditional scale under the margin-removal assumptions, not automatically as unconditional p_win.

For example, hypothetical same-book, same-time Over -120 / Under +100 yields multiplicative normalized over probability (6/11)/[(6/11)+(1/2)]=12/23=52.173913%. If push probability were 10%, the corresponding unconditional over probability would be 0.9*(12/23)=46.956522%. The assumed 10% push probability cannot be recovered from those two prices alone. De-vig method and market informativeness remain assumptions. Compare conditional with conditional; alternatively compare full outcome distributions with an independently modeled push mass. Do not silently drop pushes and retain unconditional probabilities for scoring.

## Proposed test order

1. Deterministic contract/pricing fixtures: exact integer vs half-line thresholds, push/void behavior, odds conversion, no-vig conditional scale, d_min and quote rounding, lower-scenario positive-EV gate. Test that a smaller stake cannot turn negative ROI positive.
2. Predictive-distribution checks: PMFs sum to one and are nonnegative; tail probabilities decrease with threshold; marginals from simulations match stated models; random-opportunity mixtures differ from plug-in expected opportunities; confirm beta-binomial's shared-latent assumption.
3. Joint-model checks: valid 2x2 cells, matching marginals, feasible joint bounds, separation of yard correlation from event correlation, and contract-specific combined prices.
4. Prespecified NFL shadow evaluation: freeze forecasts and exact quotes before decisions; compare fixed-opportunity, opportunity-mixture and other justified models on the same eligible, time-ordered holdout. Use proper scores plus reliability/counts/uncertainty; separate point forecasts from conservative decision bounds. Account for shared-game and repeated-player dependence when quantifying error. Do not infer a model winner or required sample size from this synthetic exercise.

## Technical references

Retrieved October 11, 2026. See the [session source register](source-register.md) for full access and evidence distinctions.

[1] Penn State, STAT 414, Lesson 10: The Binomial Distribution. University-authored probability course, fixed-count/independence/equal-probability assumptions and PMF. Search retrieval succeeded; direct page open intermittently returned an error.
https://online.stat.psu.edu/stat414/Lesson10

[2] SciPy developers, scipy.stats.betabinom, official technical documentation, Notes/PMF. Accessed current docs; independent local cross-check used installed SciPy 1.17.0. Formula verification, not NFL model validation.
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.betabinom.html

[3] Blitzstein and Hwang, Introduction to Probability, selected solutions, Chapter 9: Conditional Expectation. Harvard-hosted author solutions explicitly state the law of total variance and the missing between-component term.
https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/selected_solutions_blitzstein_hwang_probability_01.pdf

[4] Penn State, STAT 414, Lesson 18: The Correlation Coefficient. University-authored definitions Cov(X,Y)=E[XY]-E[X]E[Y] and Corr=Cov/(SD_X*SD_Y).
https://online.stat.psu.edu/stat414/Lesson18

[5] Gneiting and Raftery (2007), Strictly Proper Scoring Rules, Prediction, and Estimation, Journal of the American Statistical Association 102:359-378. Author-hosted paper, binary quadratic/Brier scoring rule. Complementary primary paper: Broecker (2008), Reliability, Sufficiency, and the Decomposition of Proper Scores.
https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf
https://arxiv.org/abs/0806.0813

[6] scikit-learn developers, Probability calibration, official documentation, introductory scoring-rule caveat and calibration-curve sections. Explains why Brier loss alone does not isolate reliability.
https://scikit-learn.org/stable/modules/calibration.html

## Bottom line
The examples establish identities and counterexamples under stated assumptions. They establish no historical NFL edge, no live available price, no profitability, and no validated uncertainty interval. The most defensible improvement is to make PRIME's existing probability, contract, uncertainty and joint-price reasoning reproducible before changing the modeling method.
