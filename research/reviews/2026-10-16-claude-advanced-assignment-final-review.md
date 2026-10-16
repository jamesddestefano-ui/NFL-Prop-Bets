# PRIME review — Claude advanced assignment, complete response
Date: 2026-10-16. Scope NFL player props only. This is a review of user-pasted Claude research, supplemented by direct public documentation checks. It does NOT replace controlling v2 betting gates, approve a paid data purchase, establish live EV, or record wagers.

## High-value conclusions accepted as research priorities
1. Source-verified, timestamped multi-book prop quotes and a frozen universe are the primary infrastructure blocker. A quote's display, underlying bookmaker update, eligibility, settlement and real NJ availability must not be conflated.
2. Keep market-only, ChatGPT, Claude, and precommitted market-anchored blends as separate candidate forecasters. Neither AI is calibrated; shared public evidence means their agreement is not independent corroboration.
3. Evaluate forecast-to-close information and forecast-to-outcome predictive quality separately, with no hindsight selection, cluster-aware inference, complete missingness and no retroactive tuning.
4. Treat player props as volume × efficiency distributions with scenario uncertainty; a mean alone is not a win probability.
5. Keep promos and line shopping in practical research priority, but promotions still require defensible fair probabilities and terms.

## Independently verified API detail — two similarly named services
- **The Odds API**: https://the-odds-api.com/ (hyphenated domain) official pricing as checked 2026-10-16: free 500 credits/month, Starter 20K $30/month, 100K $59/month; all betting markets on free plan but NO historical access. https://the-odds-api.com/historical-odds-data/ says player-prop history starts May 3, 2023, with 5-minute snapshots, on paid plans only; historical event-odds cost **10 credits per region per market per event per timestamp**. Thus Claude's 272 games ×3 markets ×10 = 8160 credits is a theoretical ONE-snapshot-per-game estimate only, excluding repeated checkpoints, event discovery, missing markets and retries. The live event odds endpoint may be charged per event/market/region; verify the exact billable request semantics before budgeting. Neither a free key nor live NJ parity has been verified in this workflow.
- **TheOddsAPI**: https://theoddsapi.com/ (unhyphenated) is a DIFFERENT provider, with different plans and free-tier limitations. Never mix these companies' prices, API keys, coverage, or endpoints.
- The existence of historical snapshot intervals does not prove every NFL prop and bookmaker is present in every snapshot or that source quote update timestamps are sufficiently fresh.

## Important challenges and corrections
- Claude's retrospective rule 'if other books moved toward the outlier it was leading; otherwise stale' is useful for post-hoc classification, but **future movement cannot establish that a quote was safely bettable at decision time**. Require as-of signals and survival after realistic execution latency; don't label the opportunity as a known stale bet using future observations.
- Missing opposite-side quote, by itself, is not a universal automatic PASS if independent credible same-contract market evidence exists; absent a defensible fair p, PASS remains appropriate. A fixed 10-minute quote expiry is an experimental parameter, not a universally proven limit. Fast-breaking injury markets may require much shorter.
- 'Cross-book dispersion' is market disagreement, not an independently calibrated confidence interval for p_true. p_market + w(p_model-p_market) - z*dispersion can be negative or uncalibrated and is NOT guaranteed to be a conservative probability. Distinguish uncertainty in a probability estimate from outcome variance of yards.
- Outcome Brier/log-loss and CLV/closing-move prediction are separate endpoints. The closing market may absorb new injuries or react to public opinion; predictive movement alone is not a verified long-run betting edge. For an AI's deviation vs subsequent closing move, control for original quote source, time-to-kickoff, line/price identity, vig, baseline market anchoring, news and within-game clustering. Rejecting an AI after exactly 200 zero-correlation cases has no guaranteed power; require a precommitted confidence interval/effect size and later-week holdout.
- For discrete count models (receptions), naive continuous PIT need not be uniform even under a correct model; use randomized PIT or discrete calibration diagnostics and proper scores.
- A purported flat PIT histogram or 'no worse than market' log-loss alone does not establish added predictive value; seek an out-of-sample improvement against a frozen baseline with uncertainty.
- Claude's bonus-bet hedged conversion formula assumes complete two-outcome coverage, consistent settlement, no restrictions and hedging cash cost. 72.7% is an idealized worked example, not a guaranteed cash conversion. Promo refunds in bonus credit require estimated realizable credit value, not face value.
- The proposed 2–5-minute delay survival study is operationally valuable, but no empirical NJ edge frequency or optimal delay is yet established.
- Threshold-coherence math and de-vig sensitivity can be DEPRIORITIZED as research, but elementary contract coherence, push/void grading and data integrity cannot be suspended.
- The proposed '30+ every prop, 80%+ closes' are pilot targets, not evidence of data availability or a reason to fabricate records.
- The user's earlier Claude report asserts 2026 US gambling-tax changes; verify primary law separately before any tax planning. No tax policy was adopted in PRIME.

## Next experiments
A. **Vendor feasibility and NJ parity:** inspect one actual live NFL player-prop event-odds response from a legitimately authorized API key (if user supplies/connects it), preserve event/book/market/threshold/side/price/update times and compare with simultaneous NJ DraftKings screenshots; record both successes and missing markets. Do not purchase, request or expose secret keys in public GitHub.
B. **Blind dual forecast + market baseline:** frozen contract universe, identical quotes, separate model answers, missing forecasts explicit, no edits after kickoff. Score outcomes when known and matched market closing moves when real closing quotes exist.
C. **Price survival:** record original quotes and +2/+5/+15/+60 minute rechecks where actually captured; calculate quote survival at exact contract, do not assume a price remained executable from a board's general timestamp.

## Disposition
ACCEPT as high-priority *test designs*; NOT an empirical positive-EV validation or authorization to change v2 governing rules. Dot tasks 010–012 already cover vendor feasibility, AI comparison, and conservative/gate design. Add one focused, nonduplicate operational task for closing-move prediction and outlier lookahead controls if appropriate.
