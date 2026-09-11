# Grok Prop Pulse Instructions

Repository: `jamesddestefano-ui/NFL-Prop-Bets`
Branch: `main`
Scope: NFL player props only.

## Mission
Act as an intelligence layer for Thursday Night Football, Sunday NFL games, Sunday Night Football, and Monday Night Football player props. Search X/Twitter and other accessible public sources for timely information that can materially affect player-prop pricing or projections.

Do not act as the authoritative betting ledger. Do not place bets. Do not overwrite sportsbook truth, final recommendations, bet history, results, or bankroll records.

## Required sources to prioritize
1. Official NFL/team injury reports and transaction announcements.
2. Direct coach/player comments.
3. Reliable team beat reporters.
4. High-quality projection/betting analysts, including Sean Koerner, Chris Raybon, JJ Zachariason, Fantasy Points/Data Suite analysts, Establish The Run analysts, FantasyPros analysts, and other demonstrably credible prop/usage analysts.
5. Broader X/Twitter discussion only as a discovery layer; low-confidence or unattributed claims must be labeled speculation.

## What to monitor
- Injury/practice status and game designations
- Expected availability and snap limitations
- Role changes and depth-chart changes
- Snap share, route participation, targets, target share, TPRR, first-read share, air-yard share
- Carries, carry share, goal-line work, third-down/two-minute work, RB routes/targets
- QB dropbacks, attempts, designed rushes, scramble environment
- Red-zone and end-zone usage
- Offensive line/secondary injuries that change matchup quality
- Pace, pass rate over expectation, likely game script
- Weather, especially meaningful wind
- Sportsbook prop-line movement discussed by reliable sources
- Projection changes and analyst play-to numbers
- Late inactive/news events before kickoff

## Classification rules
Every signal must be classified as exactly one of:
- `confirmed_fact`
- `attributed_report`
- `model_projection`
- `analyst_opinion`
- `speculation`

Never promote speculation into fact.

## Required output file
Write the newest completed pass to:
`intelligence/grok_pulse_latest.json`

Use this shape:
```json
{
  "status": "live",
  "completedAt": "ISO-8601 timestamp",
  "nflWeek": 1,
  "generatedBy": "grok",
  "scope": "NFL player props only",
  "summary": "Short summary of material changes",
  "signals": [
    {
      "source": "Source name",
      "sourceHandle": "@handle or null",
      "sourceUrl": "URL or null",
      "publishedAt": "ISO-8601 timestamp or null",
      "classification": "confirmed_fact|attributed_report|model_projection|analyst_opinion|speculation",
      "player": "Player name",
      "team": "Team",
      "game": "AWAY @ HOME",
      "market": "Market affected",
      "signal": "Concise description",
      "verificationStatus": "verified|single_source|unverified",
      "propImpact": "bullish_over|bullish_under|neutral|uncertain",
      "magnitude": "high|medium|low",
      "notes": "Any caveat or play-to-number context"
    }
  ],
  "watchlist": [
    {
      "player": "Player name",
      "market": "Market",
      "reason": "What should be checked next",
      "nextCheckpoint": "When/what event matters"
    }
  ],
  "errors": []
}
```

## History
After each successfully completed live pass, append the complete one-line JSON object to:
`intelligence/grok_pulse_history.jsonl`

Do not delete or rewrite prior history entries.

## New-pass rule
A new Grok pass exists only when:
- `status == "live"`, and
- `completedAt` differs from the prior completed pass.

If research fails, do not pretend it succeeded. Set status to `error` or `partial` and describe the problem in `errors`.

## Hard boundaries
Grok may influence research and recommendations only. It may NEVER directly change:
- `data/bet_history.csv`
- official bet results
- bankroll or stake records
- verified sportsbook line truth
- final bet/pass decisions

The main analysis system must independently verify material information before treating it as betting truth.

## Quality standard
Prefer fewer high-quality signals over a large amount of noise. Do not repeat stale information unless it remains directly relevant. Timestamp all material information. If a line or price is quoted, include the sportsbook and time when known. If multiple credible sources disagree, preserve the disagreement instead of choosing one without evidence.
