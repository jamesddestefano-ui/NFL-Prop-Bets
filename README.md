# NFL-Prop-Bets

Private research repository for NFL player-prop analysis and tracking.

## Purpose

This repository is the durable system of record for NFL player-prop research. It is separate from fantasy-football league repositories and must not import Sparta or Mongo ownership/FAAB/roster data as authoritative prop data.

The operating goal is to price player opportunity better than the market by combining:
- role and usage data
- multiple independent projections
- injuries and late news
- game environment and matchup context
- sportsbook lines, prices, and line movement
- expert and beat-reporter intelligence
- post-game grading and closing-line-value review

## Core workflow

1. Establish expected role and opportunity before matchup narratives.
2. Compare multiple independent projections against the market.
3. Convert prices to implied probability and remove vig where possible.
4. Record a fair line, fair probability, and play-to number before recommending a bet.
5. Re-check injuries, weather, inactives, and current sportsbook prices before execution.
6. Grade every tracked recommendation and measure closing-line value over time.

## Repository structure

- `AGENTS.md` — operating rules for ChatGPT/Codex/Grok-style research agents.
- `config/methodology.md` — scoring framework, metrics, pricing rules, and workflow.
- `config/sources.md` — preferred public research sources and intelligence hierarchy.
- `data/live_prop_board.csv` — current actionable/watchlist prop board.
- `data/bet_history.csv` — executed or formally tracked recommendations and results.
- `data/expert_signals.csv` — timestamped expert/model/beat-reporter signals.
- `data/news_injuries.csv` — injury, role, weather, and late-news events.
- `data/line_history.csv` — sportsbook line/price snapshots and movement.
- `research/weekly/` — weekly research notes and slate-specific analysis.
- `intelligence/` — machine-readable external intelligence feeds; intelligence only, never authoritative market truth by itself.

## Key principle

A prop is not simply an Over or Under. A complete recommendation includes the line, odds, sportsbook, fair projection/probability, edge, and a play-to number. A good bet at 51.5 can be a pass at 55.5.
