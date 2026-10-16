# Distribution sensitivity: a more likely Under can still lose money at its price

Date: 2026-10-16. Status: public mathematical education and prospective test proposal. No empirical NFL fit, executable price or betting recommendation is established. This extends the existing v2 learning supplement without changing controlling rules.

## Material correction

**VERIFIED MATHEMATICAL PRINCIPLE.** At -110, decimal odds are 21/11 and break-even probability is 11/21, or 52.380952%. A hypothetical Under with 51.2% fair probability is more likely than its Over, but its expected ROI at -110 is about -2.25%. Calling it the value side confuses direction with price.

The precise synthetic reconstruction below gives 51.207608% and -2.240021% ROI. The conclusion also holds directly from rounded inputs: 51.2% × 21/11 − 1 = -2.254545%.

## Analytic reception reconstruction

**MODEL ASSUMPTIONS.** Let target count N have mean 7.5. Conditional on N, receptions R are Binomial(N, 0.64), with independent constant-probability catches. Then E[R]=4.8 and Var(R)=7.5×0.64×0.36+0.64² Var(N). These assumptions omit player/game variation in catch probability and its dependence on targets.

Four fully specified illustrative target models are:

1. Equal mixture: P(N=7)=P(N=8)=0.5; Var(N)=0.25.
2. Poisson mean 7.5; Var(N)=7.5.
3. Negative binomial mean 7.5, variance 15. SciPy shape r=7.5 and success parameter q=0.5; thinning gives reception shape r=7.5 and q=7.5/(7.5+4.8).
4. Negative binomial mean 7.5, variance 22.5. Target shape r=3.75 and q=1/3; reception shape r=3.75 and q=3.75/(3.75+4.8).

The negative-binomial family is an explicit reconstruction assumption. A mean and variance alone do not identify the probability of crossing a line. These are analytic computations, not a verification that another simulation was run.

| Target model | Reception SD | P(R≥5) | P(R≤4) | Under ROI at -110 |
|---|---:|---:|---:|---:|
| Equal 7/8 mixture | 1.352923 | 59.705199% | 40.294801% | -23.073562% |
| Poisson | 2.190890 | 52.374125% | 47.625875% | -9.077874% |
| Negative binomial, 2 x target variance | 2.805708 | 48.792392% | 51.207608% | -2.240021% |
| Negative binomial, 3 x target variance | 3.308172 | 46.369633% | 53.630367% | +2.385246% |

The last Under is positive EV under its assumed model, but its central probability edge is only 1.249414 percentage points, below PRIME's current 4 pp standard-price research gate. The stable-role Over has illustrative ROI +13.982653%; that does not establish calibrated fair probability or conservative eligibility for an actual player.

## Lognormal yardage reconstruction and limits

**MODEL ASSUMPTION.** For positive continuous yardage Y with mean 65 and coefficient of variation c, set sigma=sqrt(log(1+c²)) and median=65/sqrt(1+c²). Then P(Y>L)=1−Phi(log(L/median)/sigma). This stylized family does not represent a mass at zero or negative yardage.

| CV | Median | P(Y>55.5) | P(Y>60.5) |
|---|---:|---:|---:|
| 0.5 | 58.137767 | 53.915082% | 46.640376% |
| 0.7 | 53.250075 | 47.387446% | 41.990653% |
| 0.9 | 48.314120 | 42.857155% | 38.514401% |

At CV 0.7, the Under 55.5 has 52.612554% probability, +0.442148% ROI at -110, and only 0.231601 pp central edge. It fails the 4 pp gate even before uncertainty. CV 0.7 being typical for a given NFL population remains unverified; these labels require empirical calibration.

**VERIFIED MATHEMATICAL COUNTEREXAMPLE.** More volatility does not universally favor an Under. For the same mean 65 lognormal model, raising CV from 0.5 to 0.9 raises P(Y>100) from 12.545736% to 17.248376%, while lowering P(Y>55.5). The line's location matters. A lower alternate line may be easier to clear and still offer poor EV at its quoted price.

## What is resolved and what still needs testing

The approximate 2,900 independent-wager sample-power illustration is consistent with the earlier supplement's two-sided 5% significance/80% power calculation for stationary 55% wins at fixed -110, fixed stakes, binary outcomes. It is neither a universal proof threshold nor a target for increasing betting volume. CLV can be an earlier diagnostic but its calibration and stability depend on comparable exact contracts, closing-market quality and selection; faster convergence is not guaranteed.

**UNTESTED HYPOTHESIS.** Target-count dispersion conditional on projected role may improve reception-probability calibration. Before Sunday's paper exercise, record the explicit distribution family, target/catch parameters, plausible alternatives and exact-price gate result. A sensitivity flip should be recorded as uncertainty. Evaluate chronological held-out paired Brier/log scores, tail calibration and missingness against a simple baseline; retain failures. A small Sunday sample tests capture and calculation quality, not profitability or a fitted dispersion advantage.

Promo claims also still require probability and terms: a better payout does not automatically imply positive cash-bet EV, and positive expected bonus cash is not the same as optimal bonus use. The previous supplement supplies worked counterexamples.

## Public sources and reproducibility

- NIST, Lognormal Distribution: https://www.itl.nist.gov/div898/handbook/eda/section3/eda3669.htm — original HTML reviewed 2026-10-16 18:00 UTC; publication date absent. Supports the lognormal transformation, moments and survival function.
- SciPy, scipy.stats.nbinom reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nbinom.html — original HTML reviewed 2026-10-16 18:00 UTC; publication date absent. Supports the negative-binomial parameterization and survival-function calculation.
- Earlier public supplement: ../2026-10-16-v2-learning-supplement/README.md — assumptions and sample-power/promo checks retained.

Run check_tables.py with SciPy installed. table_results.json records deterministic outputs and six assertions. No new historical sample, simulation provenance, video playback or empirical betting edge is claimed.
