# PRIME NFL PROP WATCH — Advanced Market Learning Module

This module is mandatory for the NFL Player Prop learning system. It extends the base methodology with market-aware decision tracking, CLV, calibration, timing, specialization, exposure, pass/missed-bet learning, and parlay separation.

## 1. Price is part of the bet

Never record only `OVER` or `UNDER`.

Every material recommendation must preserve:
- sportsbook
- market
- line
- odds
- timestamp_et
- stake
- best_market_line
- consensus_line

A player-prop recommendation without its price is incomplete.

## 2. Line history

For every serious candidate preserve, when obtainable:
- opening_line
- line_at_first_detection
- line_at_recommendation
- line_at_user_bet
- closing_line
- opening_odds
- bet_odds
- closing_odds

Calculate:
- `LINE_CLV`
- `PRICE_CLV`
- `COMBINED_CLV`

Do not infer missing market states. Unknown values remain blank/null and should be backfilled only from reliable evidence.

## 3. Bet / pass threshold

Every evaluated prop receives one primary decision classification:
- `BET`
- `LEAN`
- `WATCH`
- `PASS`
- `AVOID`

Always preserve the reason. A disciplined pass is a decision outcome and belongs in the learning record.

## 4. Fair-line estimation

When sufficient information exists estimate:
- `our_mean_projection`
- `our_median_projection`
- `market_line`
- `estimated_over_probability`
- `estimated_under_probability`
- `fair_odds`
- `market_odds`
- `estimated_edge`

Do not recommend a wager merely because a point projection sits above/below the market line. The modeled probability advantage must be sufficient to overcome uncertainty and sportsbook pricing.

## 5. Edge buckets

Classify the estimated fair-probability edge as:
- `<2%`
- `2-4%`
- `4-6%`
- `6-8%`
- `8%+`

Track results and CLV independently by bucket to determine empirically what minimum edge is sustainable.

## 6. CLV as primary process metric

Track:
- average CLV
- median CLV
- CLV hit rate
- CLV by confidence
- CLV by market
- CLV by sportsbook
- CLV by timing

A losing bet with excellent CLV may represent stronger process than a winning bet entered at a poor number.

## 7. Entry timing model

Tag every recommendation and bet with one timing bucket:
- `OPEN`
- `EARLY_WEEK`
- `MIDWEEK`
- `SATURDAY`
- `SUNDAY_MORNING`
- `PRE_GAME`

Measure CLV generated at each stage. Learn which market types should be attacked early and which benefit from waiting for news/inactives.

## 8. Prop-type specialization

Use standardized prop types:
- `PASS_YARDS`
- `PASS_ATTEMPTS`
- `PASS_TDS`
- `RUSH_YARDS`
- `RUSH_ATTEMPTS`
- `RECEPTIONS`
- `RECEIVING_YARDS`
- `LONGEST_RECEPTION`
- `ANYTIME_TD`
- `OTHER`

Do not assume equal edge in every market. Increase attention only where accumulated evidence supports stronger process and/or performance.

## 9. Signal attribution

Tag every serious evaluation with one or more of:
- `INJURY`
- `ROLE_CHANGE`
- `SNAP_SHARE`
- `ROUTE_SHARE`
- `TARGET_SHARE`
- `RUSH_SHARE`
- `RED_ZONE`
- `MATCHUP`
- `COVERAGE`
- `PACE`
- `GAME_SCRIPT`
- `WEATHER`
- `OL_INJURY`
- `DEFENSIVE_INJURY`
- `COACH_COMMENT`
- `MARKET_MOVE`
- `PROJECTION_DISAGREEMENT`
- `GROK_PULSE`
- `EXPERT_CONSENSUS`

Track CLV, process grade, and outcome by individual signal and common signal combinations.

## 10. Correlated prop detection

Identify when multiple wagers depend on substantially the same football thesis.

Tag as applicable:
- `POSITIVE_CORRELATION`
- `NEGATIVE_CORRELATION`
- `SAME_THESIS`

Account for correlation when determining total exposure. Multiple correlated wagers are not equivalent to multiple independent edges.

## 11. Bankroll and unit discipline

Track:
- stake
- units
- total weekly exposure
- exposure by game
- exposure by player
- exposure by thesis
- open risk
- settled P/L

Confidence never automatically justifies uncontrolled stake increases.

## 12. Steam-chasing protection

If the market moves materially after the original signal, recalculate the wager at the new line and price.

Never assume `GOOD AT 61.5 = GOOD AT 65.5`.

Classify the moved market:
- `BET_NOW`
- `STILL_PLAYABLE`
- `REDUCED_EDGE`
- `PASS_AFTER_MOVE`
- `MIDDLE_OPPORTUNITY`

Maintain an explicit maximum playable line and maximum acceptable juice when possible.

## 13. Missed-bet ledger

Track high-confidence recommendations that were not placed.

Record at minimum:
- recommended_line
- recommended_odds
- closing_line
- closing_odds
- result
- reason_not_bet

This prevents evaluating the system only from wagers the user happened to place.

## 14. Pass ledger

Preserve important `PASS` and `AVOID` decisions.

Afterward grade both:
- `PROCESS`
- `OUTCOME`

A disciplined pass can be a successful decision regardless of whether the prop later would have won.

## 15. Parlay separation

Track parlays separately from straight props.

Record:
- legs
- individual odds
- combined odds
- correlation
- stake
- payout
- result

Do not allow parlay wins/losses to distort straight-prop performance. Grade each underlying leg independently.

## 16. Market agreement / disagreement

Compare our projection/probability against:
- sportsbook line
- consensus market
- major projection sources
- Grok/Pulse information

Flag material disagreements. Afterward determine whether the disagreement represented genuine edge or model error.

## 17. Brier / probability calibration

When probability estimates are available, score them using Brier score:

`(predicted_probability - outcome)^2`

where outcome is `1` for hit and `0` for miss (pushes excluded or handled separately).

Maintain calibration buckets:
- `50-54%`
- `55-59%`
- `60-64%`
- `65%+`

Compare predicted probability with actual hit rate over meaningful samples.

## 18. Weekly prop attribution

After every NFL week report:
- STRAIGHT BET P/L
- PARLAY P/L
- TOTAL P/L
- ROI
- CLV
- BEST BET
- WORST BET
- BEST PROCESS LOSS
- WORST PROCESS WIN
- BEST SIGNAL
- WORST SIGNAL
- BEST PROP MARKET
- WORST PROP MARKET
- TIMING PERFORMANCE
- MISSED OPPORTUNITIES
- CORRECT PASSES
- MODEL CHANGES

## 19. Final objective

Do not optimize for number of winning bets.

Optimize for:
- positive expected value
- positive CLV
- calibrated probabilities
- disciplined entry price
- controlled exposure
- repeatable signals

Short-term results contain variance. Long-term improvement must be demonstrated through the durable ledger.

## Required durable ledgers

Use these files as the primary learning records:
- `data/decision_ledger.csv` — every material BET/LEAN/WATCH/PASS/AVOID decision
- `data/line_history.csv` — timestamped market snapshots
- `data/bet_history.csv` — actually placed straight wagers and settlements
- `data/missed_bets.csv` — recommended but unplaced wagers
- `data/pass_ledger.csv` — important passes/avoids and postgame review
- `data/parlay_history.csv` — parlays only
- `data/weekly_attribution.csv` — one row per weekly system review

Do not delete losing, missed, passed, or stale decisions. Append or update with outcome/closing information after the fact.