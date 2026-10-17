# PRIME — BetRivers player-receptions missing-side investigation

## Verified evidence

GitHub manual Odds API diagnostic run #5:
https://github.com/jamesddestefano-ui/NFL-Prop-Bets/actions/runs/39048234890

At 2026-10-17T16:10:21Z, the diagnostic recorded:
- 311 observed quotes; 149 clean Over/Under pairs; 13 unmatched groups.
- All 13 missing opposite-side groups attributed to bookmaker key `betrivers` and market `player_receptions`.
- Zero invalid rows, duplicate-sided groups, or excess/conflicting groups.
- Quota remaining: 19,597.
- The 13 missing-side groups are not evidence that BetRivers itself, rather than its upstream API representation, caused the omissions.

## Current enhancement

Commit `c5f367b49e546d8ecc780d0dcf637d7cda9fcd73` adds aggregate logs for missing-side direction and sportsbook-market group coverage. CI run 39048336214 passed. The new direction and denominator metrics have not yet been observed in a real API capture.

## Next test

Manually dispatch the Odds API collector workflow on `main` once. Read the resulting log lines:
- `Missing side direction by book and market`
- `Book market group coverage`

Preserve source run URL, timestamp, exact bookmaker key, market, numerator, denominator, and side direction. Compare with run #5 without assuming the same exact player/line identity or market persistence. Do not copy raw odds or player names into this public research note. Do not calculate no-vig probabilities for unmatched groups or label API prices executable in NJ. Do not create a scheduled live ingestion job from this diagnostic.
