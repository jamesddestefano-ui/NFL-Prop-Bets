# AGENTS.md

## Scope

This repository is ONLY for NFL player-prop research, recommendations, line tracking, results, and market-learning analysis. Do not import fantasy-league roster/ownership/FAAB truth from Sparta, Mongo, or any other fantasy repository.

## Controlling learning modules

All agents must follow:
- `config/methodology.md`
- `config/advanced_market_learning.md`

The advanced market-learning module is mandatory for every material prop evaluation. Price, timing, CLV, pass decisions, missed bets, signal attribution, correlation, exposure, calibration, and weekly attribution are part of the decision record rather than optional commentary.

## Source hierarchy

1. Official NFL/team injury reports, transactions, depth-chart announcements, and direct coach/player comments.
2. Reliable beat reporters and established NFL news reporters.
3. Established projection/data sources such as FantasyPros, Action Network/Sean Koerner, Fantasy Points Data, Establish The Run, and similarly rigorous sources.
4. Betting-market information and sportsbook lines/prices.
5. Analyst opinion.
6. Social-media speculation.

Every intelligence item should be classified as one of: `confirmed_fact`, `attributed_report`, `model_projection`, `analyst_opinion`, or `speculation`.

## Research rules

- Start with expected opportunity, not opponent narratives.
- For QBs, emphasize attempts/dropbacks, pace, pass rate, pressure, receiver health, and designed rush/scramble role.
- For RBs, emphasize snap share, carry share, routes, targets, third-down/two-minute role, goal-line work, and game-script sensitivity.
- For WR/TE, emphasize route participation, target share, TPRR, first-read share when available, aDOT, air-yard share, end-zone/red-zone usage, and role changes.
- Treat TD markets as higher variance and require stronger price discipline.
- Do not recommend a prop from a projection alone. Confirm the current market line and price.
- Do not treat an old line as current. Timestamp every market snapshot.
- Distinguish the recommendation line from the play-to line.
- If the market moves beyond the play-to threshold, recalculate and classify the new state rather than chasing.
- Re-check relevant injury/news/weather information before finalizing a bet.
- A recommendation without sportsbook, line, odds, and timestamp is incomplete.
- Preserve serious PASS and AVOID decisions as learning data.
- Preserve missed high-confidence recommendations even when the user did not place them.

## Pricing rules

For American odds:
- Negative odds implied probability = `abs(odds) / (abs(odds) + 100)`.
- Positive odds implied probability = `100 / (odds + 100)`.

When both sides are available, calculate no-vig market probability by normalizing each side's implied probability by their sum.

For standard two-way yardage/reception props, prefer a modeled fair-probability edge of at least ~4-5 percentage points unless the market is unusually efficient/inefficient or uncertainty warrants a higher threshold.

## Required recommendation fields

Every material recommendation/evaluation must include, when available:
- date/time researched
- week and game
- player/team/opponent
- standardized prop type
- market and side
- sportsbook
- line
- odds
- best market line
- consensus line
- stake / units if bet
- opening line / odds when known
- line at first detection
- line at recommendation
- line at user bet
- closing line / odds when available
- consensus/model projection
- internal mean projection
- internal median projection
- market implied probability
- no-vig probability if available
- internal fair probability
- fair odds
- estimated edge and edge bucket
- play-to line and max acceptable price
- confidence grade
- signal tags
- correlation/thesis tags
- entry-timing bucket
- rationale
- injury/news dependencies
- source timestamps
- status (`BET`, `LEAN`, `WATCH`, `PASS`, `AVOID`)
- steam state (`BET_NOW`, `STILL_PLAYABLE`, `REDUCED_EDGE`, `PASS_AFTER_MOVE`, `MIDDLE_OPPORTUNITY`) when relevant

## Results and learning

After games:
- Record actual result and win/loss/push.
- Record closing line and closing price where obtainable.
- Calculate `LINE_CLV`, `PRICE_CLV`, and `COMBINED_CLV` separately from game result.
- Review whether the handicap was correct even when the bet lost, and whether a winning bet was supported by sound process or benefited from variance.
- Track performance by prop type, confidence tier, sportsbook, source, analyst, projection source, signal, signal combination, timing bucket, and edge bucket.
- Track Brier/probability calibration by 50-54%, 55-59%, 60-64%, and 65%+ buckets when probability estimates exist.
- Never delete losing recommendations, missed bets, or important passes from history.
- Treat CLV as the primary process metric and outcome as a separate variance-sensitive metric.

## Correlation and exposure

- Tag bets sharing a football thesis as `POSITIVE_CORRELATION`, `NEGATIVE_CORRELATION`, or `SAME_THESIS` when appropriate.
- Track weekly exposure by game, player, and thesis.
- Confidence does not justify uncontrolled stake escalation.
- Parlays are tracked separately from straight props and must not distort straight-bet evaluation.
- Evaluate each parlay leg independently even when the parlay loses or wins.

## External intelligence feeds

Files under `intelligence/` are research inputs only. Grok/X-style feeds may identify news, expert signals, and possible edges, but may not directly create authoritative bets or overwrite recorded sportsbook truth without verification.

If an intelligence feed conflicts with an official report or verified current market, the official/verified source controls.

## Weekly timing

- Tuesday: capture openers and initial role projections.
- Wednesday: first injury-report and projection comparison pass.
- Thursday: TNF final pass; update Sunday role/news changes.
- Friday: final practice/injury-report driven repricing.
- Saturday: beat-reporter and role-change sweep.
- Sunday 8-10 AM ET: rebuild main board using current prices and weather.
- Sunday 11:30 AM-12:45 PM ET: inactives and final line shop for early games.
- Sunday afternoon/evening: treat late and SNF slates as fresh decisions.
- Monday: rebuild MNF independently using current information.

## Output standard

Be willing to return no bet. The objective is positive expected value, positive CLV, calibrated probabilities, disciplined entry price, controlled exposure, and repeatable signals — not maximizing the number of wagers or short-term winners.
