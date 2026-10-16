# Faster EV learning: power, probability sensitivity and a bounded Sunday test

Research: October 16, 2026, 17:54–17:57 UTC. NFL player props only. Educational supplement for review, not a change to controlling rules or a betting recommendation.

## Main findings

1. **VERIFIED MATHEMATICAL PRINCIPLE:** a fixed projected mean can imply materially different prop probabilities under different distributions. Declaring the family is necessary; declaring it does not validate it.
2. **VERIFIED MATHEMATICAL PRINCIPLE:** confidence-interval precision and statistical power are different design questions. A rough two-standard-error signal does not give an 80% chance of detecting an actual edge.
3. **UNTESTED HYPOTHESIS:** Sunday can accelerate learning by comparing independent frozen-input assessments and measuring coverage, disagreement, sensitivity and operational failures. Adding correlated contracts or lowering verification standards will not make evidence accumulate proportionally faster.

## Sources and access

Original public statistical education read October 16, 2026, approximately 17:54–17:57 UTC. Publication/update dates are not stated on the reviewed pages. Access was written HTML, not video playback or a transcript.

- NIST/SEMATECH, [Sample sizes required for proportions, section 7.2.4.2](https://itl.nist.gov/div898/handbook/prc/section2/prc242.htm), full page: normal-approximation sample sizing distinguishes false-positive risk, desired power and the alternative proportion. Its continuity correction is a further approximation, not an exact binomial calculation.
- NIST/SEMATECH, [Sample sizes required for means, section 7.2.2.2](https://www.itl.nist.gov/div898/handbook/prc/section2/prc222.htm), full page: interval precision and hypothesis-test power have different formulas; both need variance assumptions.
- NIST/SEMATECH, [Poisson distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366j.htm) and [Binomial distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366i.htm): mathematical distribution references. Neither establishes the correct family for NFL receptions.

No new original X evidence, current sportsbook quote, or empirical NFL dataset was admitted in this supplemental pass. Earlier records preserve their own source-access limits.

## Relation to current PRIME rules

Read current AGENTS.md, the adopted v2 overlay, methodology, advanced learning, positive-EV framework, account-accountability, sources, daily education, handoff and queue, plus the education index and today's threshold-coherence report. The v2 overlay already qualifies promotional value, dispersion, sample-size claims and basic probability safeguards. Those qualifications should remain. This supplement does not allege a production bug or re-adopt the overlay.

The earlier report at commit 728b27e1353fa03bd8d3ca257d9294cb97124d42 explains nested-event coherence. This note adds distribution sensitivity and power calculations rather than repeating its repair proposal. Basic probability/settlement checks are cheap admission checks; fitting advanced ensemble or monotone-repair models is separate work that can be deferred.

## Worked count example: same mean, different answer

**MODEL ASSUMPTION:** an invented active receiver has mean 4.8 receptions. Compare two hypothetical count models, neither fitted to NFL data:

- Poisson(4.8): P(R >= 5) = 0.5237412464; P(R = 5) = 0.1747476836; P(R >= 6) = 0.3489935627; P(R <= 4) = 0.4762587536.
- Binomial(8, 0.6): mean also 4.8, variance 1.92 rather than 4.8; P(R >= 5) = 0.5940864.

For hypothetical Over 4.5 at -110, decimal d = 21/11. The raw implied probability is 52.380952%. Assuming the opposing side is simultaneously -110, proportional no-vig probability is 50%. The two uncalibrated model probabilities produce ROI of -0.013035% and +13.416495%, respectively. Thus a mean alone cannot identify value. Neither family is a calibrated PRIME probability. Using the lower model probability as an illustrative adverse scenario fails conservative EV at that price, so PASS. This scenario minimum is not a statistical confidence bound.

For the Poisson Over 5 contract that refunds exactly five, fair decimal odds are (1 - p_push)/p_win = 2.364663434, or +136.4663. Over 4.5 and Over 5 are different contracts; the latter cannot use 1/p_win as fair decimal odds. The Over 4.5 Poisson value is approximately fair at -110, not exactly zero EV before rounding.

No operational maximum playable line or maximum acceptable juice is established because the input distributions are unvalidated. The arithmetic is a test fixture, not a player selection.

## Power is not a betting-volume target

**MODEL ASSUMPTION:** independent identically distributed binary wagers, all at -110, fixed unit stakes, no pushes, no selection/adaptive stopping and stationary win probability. At p = .55, ROI = p*(21/11)-1 = .05. This is 5% ROI, whereas probability edge is only .55-11/21 = 2.619048 percentage points.

A unit return has standard deviation d*sqrt(p*(1-p)) = .9497607354. Dividing by sqrt(n) gives the sample-mean standard error under these assumptions. At n=1,450, a true 5% ROI is about two standard errors from zero. That alone does not give a high probability that the realized sample will reject zero edge.

Using the NIST proportion approximation with p0=11/21, p1=.55, alpha=.05 and desired power .80:

n = [z_(1-alpha/2)*sqrt(p0*(1-p0)) + z_(.80)*sqrt(p1*(1-p1))]^2 / (p1-p0)^2.

The two-sided calculation is 2847.484, rounded up to 2848, or 2886 with the stated approximate continuity correction. A predeclared one-sided design gives 2243, or 2281 corrected. The normal-approximation upper rejection probability at n=1450 is about 51.48%; the opposite-tail rejection probability is negligible. These are illustrative planning approximations, not exact binomial results or universally required samples. Correlation, variable payouts, unequal stakes, nonstationarity and selective inclusion change the problem.

Do not place additional bets to meet a sample target. Screened candidates, hypothetical decisions, actual bets and independent game clusters are different denominators. Thirty alternate lines for one receiver do not supply thirty independent outcomes. A small Sunday comparison should remain operational and descriptive.

## Promotional value: compare expected conversion, not odds alone

**VERIFIED MATHEMATICAL PRINCIPLE:** for a stake-not-returned bonus of face amount B, expected cash proceeds are p*(d-1)*B under the stated win/lose rules. This is not ordinary cash-stake ROI. With a hypothetical +500 and p=.15, expected proceeds are .75B; +200 and p=.45 give .90B. Longer odds alone need not maximize conversion. On genuinely fair prices where p=1/d, expected proceeds are B*(1-1/d), which increases with d; that special relationship is an assumption, not a universal property of offered bets.

A hypothetical 25% profit boost on -110 changes decimal odds to 1 + 1.25*(100/110) = 2.136363636. At p=.45 its ordinary cash-stake ROI remains -3.863636%. An improved price need not cross fair value.

The current overlay already requires probability and promotional-term checks. No current promotion, entitlement, payout rule or executable price was verified here.

## Constructive counterargument

Accurate tracking cannot rescue an unsupported probability estimate. However, waiting for a fully validated custom model before collecting any evidence is also unhelpful: prospective paper observations can test data quality, identify disagreements and build the first honest comparison sample without asserting a profitable bet. Faster learning means fewer unresolved capture failures and more informative falsification, not automatic added stakes.

## Sunday protocol additions proposed for review

- Freeze the obtainable candidate list and screenshot timestamps before model verdicts. Aim for the existing v2 screening target only if actual evidence supports it. Record failures and missing inputs rather than inventing probabilities.
- Give each assessor identical source packets and contracts; preserve each answer before revealing the other. Shared source data still means their forecasts are not independent evidence about football truth. Missing assessor output stays missing.
- For each reception probability, record the distribution family and material role assumptions. Flag decision changes across reasonable prespecified alternatives, without choosing whichever family clears the gate.
- Measure completeness and time-to-verified-record, agreement on contract identity, gate arithmetic errors, unresolved-news cases, forecast coverage and closing-price coverage. These are the immediate learning endpoints.
- Compare paired Brier differences only on the same eligible, precommitted forecast basis; disclose missingness and counts of unique players/games. CLV on each assessor's BET subset is descriptive because subsets may differ. Also preserve the common-contract comparison; do not declare a model winner from Sunday's returns.
- Falsifiable operational hypothesis: frozen common inputs reduce disagreement caused by mismatched prices/contracts. Failure: material mismatches persist or coverage falls enough that the comparison becomes selected/unrepresentative. A clean capture still does not establish profitable forecasting.

## Verification and limitations

[check_math.py](check_math.py) and [math_results.json](math_results.json) reproduce eight synthetic assertions, executed during this review. No live player forecasts, probabilities, quoted bets, calibration, CLV or profit were created. Confidence is high for arithmetic, limited for operational usefulness, and unestablished for NFL predictive benefit. Further evidence requires timestamped same-contract quotes, genuine pregame model outputs and settlement outcomes over chronological future cohorts.

No controlling files, betting records, schedules, repairs or prior queue events are changed by this note. It is a research handoff only.
