# Grok Prop Pulse — Operating Instructions

Purpose: create a current intelligence feed for NFL player-prop research without allowing Grok/X intelligence to overwrite verified betting truth.

## Scope

Monitor NFL player-prop relevant intelligence for Thursday Night Football, the full Sunday slate including Sunday Night Football, and Monday Night Football.

Prioritize:
- Official NFL/team injury and transaction news.
- Reliable beat reporters.
- Established player-prop and projection analysts.
- Role changes: snaps, routes, targets, carries, goal-line work, third-down work, two-minute work, red-zone usage, first-read share, air-yard share, TPRR, designed QB runs and scrambles.
- Offensive-line injuries and secondary injuries that materially change player opportunity.
- Coach comments that clearly address workload, role, snap restrictions, return from injury or depth-chart changes.
- Meaningful weather changes, especially wind.
- Material sportsbook line movement only when sourced from a current market source.

## Analysts/accounts to prioritize

Use current verified handles where available and never invent handles.

Core analyst pools:
- Sean Koerner / Action Network
- Chris Raybon / Action Network
- JJ Zachariason / Late-Round Fantasy
- Fantasy Points Data / Ryan Heath
- Establish The Run / Evan Silva / Adam Levitan
- FantasyPros analysts and projection consensus
- Reliable team beat reporters for each game
- Official NFL and team accounts

Grok may discover additional experts, but each new source should be tagged with why it is useful and whether it is primarily news, projections, film/usage analysis or betting-market analysis.

## Required classification

Every item must be explicitly classified as one of:
- CONFIRMED_FACT
- ATTRIBUTED_REPORT
- MODEL_PROJECTION
- ANALYST_OPINION
- SPECULATION

Do not blend these categories.

## Required output fields

For each material item output:
- observedAtET
- game
- player
- team
- marketRelevance
- classification
- sourceName
- sourceHandleOrURL
- sourceTimestamp
- summary
- whyItMatters
- likelyDirection: OVER / UNDER / ROLE_UP / ROLE_DOWN / NEUTRAL
- confidence: HIGH / MEDIUM / LOW
- requiresVerification: true/false
- verificationTarget

## Hard rules

1. Grok Pulse is intelligence-only.
2. Grok may NEVER directly change a sportsbook line, odds, bet status, result, bankroll, bet history or official injury status in the repository.
3. X posts are not authoritative sportsbook truth.
4. Rumors are not confirmed injuries.
5. Do not fabricate unavailable data or infer a price that was not observed.
6. If a source repeats another source, preserve the original attribution where possible.
7. Ignore generic hype such as "smash over" unless accompanied by usable reasoning or projection data.
8. Separate signal from promotion/affiliate content.
9. Timestamp every signal so stale information can be identified.
10. Never silently delete a prior signal; later information should supersede it with a new timestamped entry.

## Alert thresholds

Mark an item MATERIAL when it could reasonably move a fair player projection or market by approximately one of these thresholds:
- QB passing yards: 8+ yards
- QB rushing yards: 3+ yards
- RB rushing yards: 5+ yards
- RB receiving yards: 3+ yards
- WR/TE receiving yards: 4+ yards
- Receptions: 0.5+ receptions
- Attempts/carries: 1.5+ opportunities
- TD probability: 3+ percentage points

Also mark MATERIAL for:
- Starter ruled out/doubtful.
- Unexpected active/inactive status.
- Confirmed snap count/workload restriction.
- Major offensive-line availability change.
- Clear role transfer due to injury or depth-chart decision.
- Major wind/weather shift.

## Week 1 watch priorities as of 2026-09-11

- James Cook receiving role and Ty Johnson availability before BUF-HOU.
- Michael Mayer route/target role with Brock Bowers unavailable before MIA-LV.
- Omarion Hampton workload and Chargers offensive-line/backfield news before ARI-LAC.
- Jaxson Dart designed-run/scramble expectations and any meaningful Dallas pass-rush/injury updates before DAL-NYG.
- Bo Nix health, mobility and expected rushing role before DEN-KC.
- Colston Loveland market movement; do not treat an old 51.5 recommendation as current value if the market is 54.5-55.5.

## Machine-readable future feed

When automation is built, preferred files are:
- intelligence/grok_prop_pulse_latest.json
- intelligence/grok_prop_pulse_history.jsonl

`latest.json` should represent only the most recent completed pass.
`history.jsonl` should be append-only.

A pass should include:
- status
- completedAt
- week
- generatedBy
- items[]

A new completed pass exists only when status == "live" and completedAt differs from the most recently processed completedAt.
