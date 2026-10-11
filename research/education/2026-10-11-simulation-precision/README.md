# More simulations do not make a wrong probability right

Written-source mathematical follow-on, checked 2026-10-11. Entire numerical example is invented. No video reviewed; no NFL calibration or performance assessed. A source article's mention of 10,000 simulations does not establish independent draws, correct inputs, model calibration, or real-world accuracy. The example below does not assert those properties of that article's actual simulator.

## The compact lesson

Suppose a fixed simulator produces 5,280 hits in 10,000 independent trials. Its estimated hit probability is 52.8%. At a hypothetical decimal price of 21/11 (about 1.90909), break-even is 52.381%. The estimated expected net return is +0.8% per accounting unit, but its Monte Carlo standard error is about 0.953 percentage points. An approximate 95% numerical interval for expected return runs from −1.070% to +2.666%.

Thus this run has not numerically resolved which side of break-even its own fixed-model probability lies on. Even numerically resolving that sign would not establish that the probability is accurate for real games. Increasing independent simulations from 10,000 to 1,000,000 reduces numerical standard error roughly tenfold at the same probability; it does not repair model misspecification or add real-world observations.

## Assumptions and calculation

Let Y_i be the hit indicator, with Y_i iid Bernoulli(p_M), where p_M is the fixed model-implied probability. N and the evaluated event/price are fixed before seeing simulation output. Settlement is binary with no push, void, fee or price change. One accounting unit is solely a mathematical normalization, not a stake recommendation.

- Estimate: p_hat = sum(Y_i)/N = 0.528.
- Exact fixed-model variance: Var(p_hat | model) = p_M(1−p_M)/N.
- Plug-in MCSE: sqrt[p_hat(1−p_hat)/N] = 0.004992154, or 0.499215 percentage points of probability.
- Decimal gross return d = 21/11; net payoff is d−1 on a hit and −1 otherwise.
- EV(p) = p(d−1)−(1−p) = dp−1. Break-even p* = 1/d = 11/21 = 0.523809524.
- Estimated EV = d × 0.528−1 = 0.008, or +0.8% per accounting unit.
- Because this mapping is linear, MCSE(EV_hat) = d × MCSE(p_hat) = 0.009530476, or 0.953048 percentage points of expected return.

Optional interval check: invert the large-sample binomial score test with z=1.959963984540054. The Wilson endpoints are

[p_hat + z²/(2N) ± z sqrt(p_hat(1−p_hat)/N + z²/(4N²))] / [1+z²/N].

This gives [0.518206679, 0.537771817]. Transform both endpoints with dp−1 to obtain [−0.010696340, 0.026655287]. This is an approximate fixed-N, repeated-simulation confidence interval for p_M and its EV, not an interval proven to cover a real-world probability. Coverage is not exactly 95%; the oracle test below checks its actual coverage at one invented p_M.

At N=1,000,000 and the same underlying p near 0.528, projected MCSE(p_hat) is approximately 0.000499215; MCSE(EV_hat) is approximately 0.000953048. A new realization need not have exactly the same estimated mean.

## Four distinctions that prevent overclaiming

1. **Independent simulations versus MCMC.** The binomial formula assumes independent hit indicators. For correlated MCMC output, use a justified effective sample size and MCSE for the actual estimated quantity, alongside convergence diagnostics. Raw iteration count is not effective sample size. Positive correlation often reduces ESS; anticorrelation can increase it. A generic parameter's bulk ESS is not automatically the appropriate ESS for a transformed hit indicator.
2. **Numerical error versus uncertain model inputs.** For a shared uncertain latent state Θ, write p_Θ for its hit probability. If a run samples Θ once and then draws outcomes conditionally independently, total variance is Var(p_hat) = E[p_Θ(1−p_Θ)]/N + Var(p_Θ). The second term does not vanish with more inner simulations. If instead each replicate independently redraws Θ from a specified posterior and then an outcome, the marginal hit indicators can be iid with probability E[p_Θ]. More draws accurately integrate that model's posterior predictive mean; they do not collapse uncertainty about p_Θ or establish the posterior/model is correct.
3. **Model uncertainty versus model error.** Even a small MCSE and narrow model-based posterior can coexist with omitted variables, biased data, an inappropriate distribution or changed conditions. Real-world validation needs relevant held-out outcomes and a justified evaluation design. No such evidence was collected here.
4. **One fixed check versus selection and optional stopping.** An ordinary fixed-N interval does not automatically keep its advertised coverage if repeatedly checked until favorable, or if the most favorable of many props is selected. Precommit to the estimand and simulation budget, or use an appropriate sequentially valid procedure and address multiplicity. A confidence sequence addresses repeated looks for its covered estimand; it does not automatically correct selection across arbitrary many estimands or validate the sports model.

## Evidence labels

- **VERIFIED MATHEMATICAL PRINCIPLE:** Conditional iid Bernoulli variance, the linear EV map and variance propagation, the inverse-square-root sample-size relationship, and the shared-latent total-variance decomposition. The binomial calculation was also checked numerically against all possible counts.
- **MODEL ASSUMPTION:** Fixed p_M; independent, identically distributed hit indicators; a preselected event and fixed N; fixed decimal price; binary settlement without pushes, voids or fees. None is verified for the article's actual simulator.
- **EMPIRICAL EVIDENCE:** None about NFL outcomes, calibration or actual betting performance was gathered. The saved numerical oracle result is computational validation of an invented mathematical example, not empirical sports evidence.
- **ANALYST OPINION:** Reporting numerical precision separately from model/input uncertainty is the recommended presentation choice for this lesson. The interval crossing break-even is a mathematical result, not an opinion about a wager.
- **UNTESTED HYPOTHESIS:** None is advanced about a particular NFL model. Any claim that the article's 10,000 simulations deliver calibrated or accurate real-world probabilities remains untested by this review.

## Source cards

Publication dates for the current NIST and Stan documentation pages below are unknown/undated. Displayed software versions identify the retrieved documentation, not its publication date.

- **NIST/SEMATECH, Binomial Distribution.** [Official handbook](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366i.htm). **Access:** 2026-10-11 22:07 UTC. **Review scope:** complete retrieved handbook page, including PMF and summary statistics; no linked pages reviewed. Supplies the fixed-p binomial PMF, mean, standard deviation and count/N estimate. Our iid variance, linear EV propagation and numeric example are direct algebraic derivations, not sports evidence.
- **Stan Reference Manual, Posterior Analysis, version 2.40 displayed at retrieval.** [Official reference](https://mc-stan.org/docs/reference-manual/analysis.html). **Access:** 2026-10-11 22:06 UTC. **Review scope:** retrieved chapter text, focused on convergence, ESS and MCMC standard-error sections; no cited papers or linked implementation files reviewed. Distinguishes convergence and correlation issues in MCMC; defines ESS through autocorrelation and MCSE as posterior standard deviation divided by sqrt(ESS). It also notes that finite-run diagnostics cannot guarantee convergence. Scope: computational estimation of a specified target distribution.
- **posterior package 1.7.1, mcse_mean.** [Official API documentation](https://mc-stan.org/posterior/reference/mcse_mean.html). **Access:** 2026-10-11 22:06 UTC. **Review scope:** complete retrieved API documentation page; linked R source and cited book not reviewed. Documents MCSE for an expectation from draws, including iterations-by-chains input. Constant chain values return NA because genuine constancy cannot be distinguished from sampling/convergence failure. The API is not an NFL accuracy or calibration certificate.
- **Howard, Ramdas, McAuliffe and Sekhon, Time-uniform, nonparametric, nonasymptotic confidence sequences.** [Authors' paper, arXiv version 9](https://arxiv.org/abs/1810.08240v9), published in Annals of Statistics 49(2), 2021. **Access:** 2026-10-11 22:07 UTC. **Publication/version dates:** journal publication April 2021; arXiv v9 revised 2022-08-06. **Review scope:** abstract and bibliographic landing-page metadata only; paper body, proofs and implementation not reviewed. Introduces confidence sequences valid uniformly over time under stated assumptions. This supports the availability of sequential methods; none is implemented or claimed for the example.

## Falsifiable numerical validation

The accompanying validate_precision.py enumerates all 10,001 possible binomial hit counts at a deliberately known toy p_M=0.528, rather than trusting one random run. It checks that the summed mean is 0.528, Var(p_hat)=p_M(1−p_M)/10,000, and Var(EV_hat)=d² Var(p_hat), to explicitly stated tolerances. It also checks that Wilson coverage at this particular p and N is between 94.8% and 95.2% and that the example interval contains break-even. Failure falsifies at least the toy calculation/implementation or its numerical assumptions; passage does not validate any NFL probability.

Executed result: PASS. Exact-binomial summation gives Wilson coverage 0.9491935484 at this p and N. Full outputs are in validation_results.json. This is a deterministic floating-point oracle calculation, not a new forecast dataset or a simulation of actual players.

## Evidence and confidence

- High confidence: the conditional iid Bernoulli variance identity and linear EV propagation; formulas independently checked by binomial enumeration.
- Qualified approximation: the Wilson interval has approximate nominal 95% coverage; verified 94.919% coverage only at this example's p and N.
- No assessed evidence: whether the article's simulations are independent, whether its underlying probabilities are calibrated, or whether any actual NFL prop has positive EV. No inference about those questions follows from the 10,000 count.
