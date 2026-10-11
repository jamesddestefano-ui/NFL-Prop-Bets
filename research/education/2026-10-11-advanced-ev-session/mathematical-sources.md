# Mathematical sources and scope

Access date: October 11, 2026, approximately 21:21–21:28 UTC. This numerical review used primary mathematical text and official documentation. It involved no video playback. Candidate mechanisms and invented inputs were drawn from the separately documented educator review; this mathematical review independently recalculated them. Sources do not supply or validate the invented NFL inputs.

## Bayes and posterior prediction

1. Jeremy Orloff and Jonathan Bloom, MIT 18.05, Spring 2022, **Bayesian Updating Probabilistic Prediction**, Class 12.
   - https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_class12-prep-a.pdf
   - Official four-page PDF text inspected, including prior/posterior predictive mixtures on pages 2–3. Supports using state weights to average conditional probabilities of the same future event. It supplies no NFL target or injury model.

2. Jeremy Orloff and Jonathan Bloom, MIT 18.05, Spring 2022, **Bayesian Updating Odds**, Class 12.
   - https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_class12-prep-b.pdf
   - Official nine-page PDF text inspected, especially odds updating and likelihood ratios on pages 2–5. The conditional dependence extensions and duplicated-report fixture in this appendix are original applications of Bayes' rule.

3. Philippe Rigollet, MIT 18.650, Fall 2016, Bayesian Statistics.
   - See [the single source card](source-register.md) for transcript/caption access and discrepancy. Mathematical review checked the relevant Bayes/Beta sections; no audio review.

4. MIT 18.05, Spring 2022, **Conjugate Priors Beta and Normal**, Class 15.
   - https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_class15-prep.pdf
   - Official ten-page PDF text opened and relevant conjugate-update material inspected. General conjugacy support only; the independent all-success integration check is sufficient to verify the formula guard. Not used to infer any injury-report likelihood.

## Predictive checking and held-out evaluation

5. Stan Development Team, **Posterior and Prior Predictive Checks**.
   - https://mc-stan.org/docs/stan-users-guide/posterior-predictive-checks.html
   - Official chapter inspected on posterior-replicate construction, mean/dispersion checks and non-classical posterior tail probabilities. The zero/ten count data, Gamma prior, exact tail calculations and union-bound demonstration are original synthetic analysis. Publication date not asserted.

6. Stan Development Team, **Held-Out Evaluation and Cross-Validation**.
   - https://mc-stan.org/docs/stan-users-guide/cross-validation.html
   - Official sections inspected on test/train separation, predictive log densities and time/structured splits. Supports averaging likelihoods before taking the log and matching the validation split to the forecasting goal. Does not establish an NFL evaluation result or specific suitable split length.

7. scikit-learn developers, **Probability Calibration**.
   - https://scikit-learn.org/stable/modules/calibration.html
   - Official sections 1.16.1–1.16.3 inspected. Supports binwise reliability interpretation, counts, independent calibration fitting and the difference between proper scores and calibration alone. No scikit-learn package is required or invoked by the script. Its toy fitted-map counterexample is original, and does not evaluate the library's implementation.

8. Andrew Gelman, Xiao-Li Meng and Hal Stern, **Posterior Predictive Assessment of Model Fitness via Realized Discrepancies**, Statistica Sinica 6 (1996), 733–807.
   - https://stat.columbia.edu/~gelman/research/published/A6n41.pdf
   - Author-hosted paper opened and relevant predictive-discrepancy passages inspected, not the entire 76-page paper/discussion. Background primary research for predictive checks; the report uses Stan's concise current exposition for its limited sourced description.

## Calibration under aggregation

9. Ryan Tibshirani, Berkeley, **Forecast Scoring and Calibration**.
   - See [the shared W3 source card](source-register.md). Mathematical review focused on §§3.4 and 5.1; the exact signal construction is original.

10. Tilmann Gneiting and Adrian E. Raftery, **Strictly Proper Scoring Rules Prediction and Estimation**, JASA 102 (2007), 359–378.
    - https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf
    - Author-hosted paper opened; definition and relevant score context consulted, not newly reviewed in full. This is a carried-forward primary background reference for the Brier calculation, rather than an additional empirical lesson or source of the invented calibration outcomes.

## Arithmetic and scope boundaries

The joint uncertainty-set counterexample, quote-capacity arithmetic, latency-selection expected values and midpoint-line construction are self-contained exact calculations. They require no empirical authority for their stated algebra. Practical mechanisms were suggested by the separately documented educator review; creator profits and market claims are not adopted here.

No source estimates the .75/.25 report likelihoods, the selected uncertainty scenarios, .80 signal accuracy, correlation structure, quote age, capacity or future executable price. No source establishes any actual NFL probability or profitable strategy. The script proves results conditional on these invented inputs. All method choices remain proposals for review.
