# PRIME Positive Expected Value Framework

Version: 1.0
Adopted: 2026-10-10
Scope: NFL player props only

## 1. Core objective

PRIME does not optimize for hit rate, number of bets, or whether a projection is merely above or below a sportsbook line.

The objective is to identify executable wagers whose offered sportsbook line and price are better than PRIME's conservative estimate of fair value, while controlling model uncertainty, market staleness, correlation, timing, and bankroll exposure.

A bet is attractive only at a specific:
- sportsbook
- market
- threshold
- price
- timestamp

“Over” or “Under” without price is not a complete wager.

## 2. Expected value is the primary bet gate

Convert American odds to decimal odds:

- positive American odds A: decimal = 1 + A/100
- negative American odds A: decimal = 1 + 100/abs(A)

Break-even probability:

- decimal odds d: p_break_even = 1/d
- negative American odds A: abs(A)/(abs(A)+100)
- positive American odds A: 100/(A+100)

Expected ROI per unit staked:

EV = p_fair * decimal_odds - 1

Equivalent net-odds form:

EV = p_fair * b - (1-p_fair)

where b = decimal_odds - 1.

A negative American price can still be an excellent bet. The sign of the odds does not determine value. Value exists when PRIME's calibrated fair probability is high enough relative to the offered price.

Track both:
- probability edge = p_fair - p_break_even
- expected ROI = p_fair * decimal_odds - 1

Probability edge remains useful for calibration, but expected ROI is the more economically meaningful cross-price comparison.

## 3. Market truth must be verified before value is calculated

Every actionable market observation receives a Market Truth Confidence grade.

### A — direct / executable
Examples:
- user sportsbook screenshot or bet slip
- direct sportsbook page with current exact line and price
- authenticated live sportsbook feed

May support a BET if all other conditions are satisfied.

### B — fresh timestamped market board
A reputable multi-book board with:
- named sportsbook
- exact line
- exact odds
- explicit recent update time

May support a BET, but an unusually favorable outlier should still be verified in the live app when practical.

### C — secondary / partially stale
Examples:
- article mentioning a line
- aggregator lacking a precise refresh time
- search snippet
- market quote old enough that material movement is plausible

May support WATCH/LEAN/research only. Do not promote to BET solely from a C-grade quote.

### D — stale / unverified
Examples:
- undated price
- old article reused as current
- inferred line
- Google summary with unclear market timestamp
- a line remembered from an earlier checkpoint

Cannot support an actionable wager.

## 4. Outlier-line verification protocol

A single sportsbook line that is materially better than the rest of the market can be valuable or stale.

Treat a quote as PRICE_VERIFY_REQUIRED when it is approximately:
- 1 or more full yards/receptions/carries better than the market center, or
- 10 or more cents better at the same threshold, or
- otherwise an obvious isolated outlier

Before a formal BET:
1. verify freshness;
2. verify the exact sportsbook;
3. verify the exact threshold;
4. verify the exact odds;
5. verify the market is still offered and not suspended;
6. preserve the timestamp.

Never construct a recommendation from a stale outlier merely because it creates a large modeled edge.

## 5. No-vig market probability

Raw sportsbook implied probability includes margin.

When both sides of the SAME sportsbook, SAME threshold, SAME market, and SAME timestamp are available, remove the vig before using the market as a fair-value benchmark.

### Baseline two-way method
For raw implied probabilities q1 and q2:

p1 = q1 / (q1 + q2)
p2 = q2 / (q1 + q2)

This multiplicative normalization is the default quick method for standard binary props.

### Sensitivity method
Where feasible, also calculate a power-method de-vig estimate.

Research comparing de-vig techniques shows that simple normalization can miss favorite-longshot effects and that power methods can outperform multiplicative normalization across sportsbook datasets.

If the betting decision changes materially depending on reasonable de-vig method, downgrade confidence or PASS rather than selecting the method that creates the desired edge.

Do not fabricate a no-vig probability when only one side of the market is known.

## 6. Multi-book consensus

There is no single universal “sharp book” for NFL player props.

For standard props, PRIME should prefer a timestamp-aligned consensus:
1. collect multiple books at the same threshold where possible;
2. de-vig each book separately when both sides are available;
3. preserve each book's quote;
4. use the median or robust central estimate of the resulting fair probabilities;
5. track dispersion across books.

Do not take an Over price from one book and an Under price from another and pretend they are one two-sided sportsbook market.

When thresholds differ across books, preserve the different thresholds. If alternate-line data is sufficient, infer a market distribution; otherwise do not manufacture a consensus probability at a threshold the market did not actually quote.

Over time, weight reference books by demonstrated predictive value for that prop type and timing bucket, measured by their relationship to later consensus/close—not by a permanent label such as “sharp” or “soft.”

## 7. Internal fair probability

PRIME should preserve four distinct probability concepts:

- p_market: de-vigged market benchmark
- p_model_raw: probability implied by independent football/projection modeling
- p_internal: calibrated/shrunk PRIME fair probability
- p_conservative: downside-case fair probability after reasonable model uncertainty

Do not invent a precise percentage from narrative confidence.

The model path should begin with opportunity and role:
- snaps
- routes
- targets / TPRR / first-read share
- carries / rush share
- third-down and two-minute work
- goal-line / red-zone usage
- expected plays / pace / PROE
- injuries and lineup changes
- QB and OL environment
- weather
- game script

Projection sources are inputs, not authority.

Because player performance distributions are not always symmetric, distinguish mean from median. Yardage means can be pulled upward by long-tail outcomes; a sportsbook threshold is closer to a median/quantile question than a simple average-projection comparison.

Where sufficient data exists, convert the internal performance distribution to the probability of clearing the exact sportsbook threshold.

## 8. Shrinkage toward market and uncertainty

Public models and short samples can create exaggerated apparent edges.

When PRIME lacks demonstrated out-of-sample calibration for a prop type, shrink the raw model probability toward the de-vigged market rather than accepting the model probability at face value.

A practical representation is:

p_internal = p_market + w * (p_model_calibrated - p_market)

where w is larger only when PRIME has:
- reliable role data,
- multiple independent projection paths,
- strong historical calibration in that prop type,
- low unresolved injury/usage uncertainty,
- and a verified market.

Do not set w mechanically without evidence. Preserve the reason for the chosen degree of shrinkage.

Create a reasonable probability range using:
- independent models,
- model variants,
- market de-vig methods,
- role uncertainty,
- news uncertainty.

Use the adverse end of that reasonable range as p_conservative for the bet side.

## 9. Initial bet thresholds

Until PRIME accumulates enough data to learn better thresholds from its own ledger, use both probability edge and expected ROI.

### Standard two-way yardage / attempts / receptions
A normal BET should generally require:
- Market Truth Confidence A or B
- central probability edge approximately 4 percentage points or greater
- positive conservative EV
- expected ROI approximately 5% or greater
- no unresolved material role/injury dependency

### High-variance markets such as anytime TD
Require stronger pricing discipline:
- multiple independent support paths
- central probability edge generally at least about 5 percentage points
- expected ROI generally at least about 8%
- positive conservative EV

These are starting gates, not eternal constants. Re-estimate them from actual PRIME CLV, calibration, and outcomes by prop type.

A wager can be PASS even when its central estimated EV is positive if model uncertainty is too large.

## 10. Line shopping

Line shopping is part of the model, not an administrative step after analysis.

For every serious candidate:
1. find the best threshold;
2. compare price at that threshold;
3. compare alternate thresholds;
4. calculate EV for each executable option.

A lower Over line with worse juice can be better than a higher line with cheaper juice. The only correct comparison is expected value at each exact line/price.

Never treat two prices as equivalent simply because they concern the same player and stat.

## 11. Steam and repricing

Once the market moves, the old bet no longer exists.

Recalculate from scratch at the new line/price and classify:
- BET_NOW
- STILL_PLAYABLE
- REDUCED_EDGE
- PASS_AFTER_MOVE
- MIDDLE_OPPORTUNITY

Never transfer an old fair probability mechanically across a materially different threshold.

The stored play-to number is a precommitment device against chasing.

## 12. Closing-line value

CLV remains PRIME's primary process metric, but the close is a benchmark, not an oracle.

For player props:
- preserve line CLV separately from price CLV;
- prefer a multi-book consensus close when available;
- de-vig the closing market before treating it as fair-value evidence;
- note whether late injury/news information arrived after the bet;
- preserve the exact settlement rules.

Positive CLV means the market moved in the bettor's favor after entry. It does not prove the handicap was correct, and negative CLV does not by itself prove it was wrong.

Because prop markets are fragmented and lower-liquidity than main NFL sides/totals, evaluate CLV by market type and sportsbook rather than assuming one close is universally efficient.

## 13. Calibration over hit rate

PRIME should optimize probability quality, not merely prediction accuracy.

Track:
- Brier score
- calibration by probability bucket
- observed hit rate vs predicted hit rate
- expected ROI vs realized ROI
- CLV by probability bucket
- CLV by prop type

A 60% forecast must be judged differently from a 52% forecast even if both ultimately win or lose.

Use out-of-sample / forward-looking evaluation. Do not recalibrate a model on the same observations used to claim improved performance.

## 14. Book and source learning

For each sportsbook and prop type, learn:
- frequency of stale/outlier quotes
- average subsequent consensus movement
- average CLV if entered there
- limit/availability reliability when observable
- predictive relationship to later market consensus

For each projection source, learn:
- Brier score
- directional bias
- calibration
- CLV when PRIME follows its disagreement
- performance by prop type

No book or expert receives permanent authority.

## 15. Bankroll and fractional Kelly

The full Kelly criterion assumes the true edge is known. In practice PRIME estimates the edge, which creates model-risk and overbetting risk.

If bankroll-based sizing is used, calculate full Kelly only as a reference:

f* = (p*b - (1-p)) / b

Then apply a conservative fraction rather than full Kelly until the probability model is well calibrated.

Default policy:
- continue to use small fixed units while sample size is limited;
- treat 0.25 Kelly as an upper reference for ordinary calibrated straight props, not an automatic stake;
- cap exposure by player/game/thesis;
- use smaller sizing for TD markets and other high-variance props;
- never increase stake merely because the last bets won.

If the user's bankroll is not defined, use units rather than inventing a bankroll.

## 16. Correlation and portfolio EV

A set of individually +EV bets can still create poor portfolio risk if they share one football thesis.

For every bet, preserve:
- player exposure
- game exposure
- thesis exposure
- correlation tags

Reduce combined stake when multiple wagers depend on the same injury, game script, target concentration, or backfield assumption.

For parlays:
- calculate each leg's standalone edge first;
- treat correlation explicitly;
- compare parlay payout with the joint fair probability;
- do not assume a same-game parlay is +EV because every leg is individually attractive.

## 17. Required new evaluation outputs

For every material candidate, preserve when available:
- market_truth_confidence
- devig_method
- p_break_even
- p_market
- p_model_raw
- p_internal
- p_conservative
- fair_odds
- probability_edge_pct
- expected_roi_pct
- conservative_ev_pct
- market_dispersion
- line_shop_advantage
- reference_market_quality
- play_to_line
- max_acceptable_odds
- steam_state
- correlation/thesis exposure

Until ledger schemas are expanded, preserve these values in the immutable archive and/or structured decision_reason rather than omitting them.

## 18. Decision sequence

Every PRIME candidate should follow this order:

1. Verify current market truth.
2. Confirm settlement rules and exact threshold.
3. Capture both sides and multiple books where possible.
4. De-vig the relevant market.
5. Establish multi-book consensus and dispersion.
6. Build football opportunity projection.
7. Convert the projection to a probability distribution.
8. Calibrate/shrink against historical performance and the market.
9. Calculate fair odds, probability edge, EV, and conservative EV.
10. Compare all executable books/thresholds.
11. Apply news, uncertainty, and correlation controls.
12. Set play-to line and maximum juice.
13. Classify BET / LEAN / WATCH / PASS / AVOID.
14. After entry, track movement and CLV.
15. After settlement, grade probability calibration and process separately from result.

## 19. Governing principle

PRIME is not a pick generator.

PRIME is a price-discovery and probability-calibration system for NFL player props.

The correct question is not:
“Do we think this goes Over?”

The correct question is:
“At this exact line and price, is the sportsbook offering a better deal than our conservative estimate of the true probability, after accounting for vig, market information, uncertainty, timing, and portfolio exposure?”
