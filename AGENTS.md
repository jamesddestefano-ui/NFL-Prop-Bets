# AGENTS.md

## Scope

This repository is ONLY for NFL player-prop research, recommendations, line tracking, and results. Do not import fantasy-league roster/ownership/FAAB truth from Sparta, Mongo, or any other fantasy repository.

## Source hierarchy

1. Official NFL/team injury reports, transactions, depth-chart announcements, and direct coach/player comments.
2. Reliable beat reporters and established NFL news reporters.
3. Established projection/data sources such as FantasyPros, Action Network/Sean Koerner, Fantasy Points Data, Establish The Run, and similarly rigorous sources.
4. Betting-market information and sportsbook lines/prices.
5. Analyst opinion.
6. Social-media speculation.

Every intelligence item should be classified as one of: `confirmed_fact`, `projection`, `analyst_opinion`, or `speculation`.

## Research rules

- Start with expected opportunity, not opponent narratives.
- For QBs, emphasize attempts/dropbacks, pace, pass rate, pressure, receiver health, and designed rush/scramble role.
- For RBs, emphasize snap share, carry share, routes, targets, third-down/two-minute role, goal-line work, and game-script sensitivity.
- For WR/TE, emphasize route participation, target share, TPRR, first-read share when available, aDOT, air-yard share, end-zone/red-zone usage, and role changes.
- Treat TD markets as higher variance and require stronger price discipline.
- Do not recommend a prop from a projection alone. Confirm the current market line and price.
- Do not treat an old line as current. Timestamp every market snapshot.
- Distinguish the recommendation line from the play-to line.
- If the market moves beyond the play-to threshold, mark the prop `PASS_PRICE_LOST` rather than chasing.
- Re-check relevant injury/news/weather information before finalizing a bet.

## Pricing rules

For American odds:
- Negative odds implied probability = `abs(odds) / (abs(odds) + 100)`.
- Positive odds implied probability = `100 / (odds + 100)`.

When both sides are available, calculate no-vig market probability by normalizing each side's implied probability by their sum.

For standard two-way yardage/reception props, prefer a modeled fair-probability edge of at least ~4-5 percentage points unless the market is unusually efficient/inefficient or uncertainty warrants a higher threshold.

## Required recommendation fields

A formal recommendation should include:
- date/time researched
- week and game
- player/team/opponent
- market type and side
- sportsbook
- line
- odds
- consensus/model projection
- internal fair projection
- market implied probability
- no-vig probability if available
- internal fair probability
- estimated edge
- play-to line and max acceptable price
- confidence grade
- rationale
- injury/news dependencies
- source timestamps
- status (`BET`, `WATCH`, `PASS_PRICE_LOST`, `PASS_NEWS`, `PASS_EDGE`, `CLOSED`)

## Results and learning

After games:
- Record actual result and win/loss/push.
- Record closing line and closing price where obtainable.
- Calculate closing-line value separately from game result.
- Review whether the handicap was correct even when the bet lost, and whether a winning bet was supported by sound process or benefited from variance.
- Track performance by market type, confidence tier, source, analyst, projection source, timing, and edge bucket.
- Never delete losing recommendations from history.

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

Be willing to return no bet. The objective is expected value and process quality, not forcing action on every game or slate.
