# PRIME Odds API diagnostic capture — October 17, 2026

## Verified last capture

GitHub Actions manual diagnostic run #3:
https://github.com/jamesddestefano-ui/NFL-Prop-Bets/actions/runs/39046079643

Log evidence: 311 observed quote rows; 149 clean Over/Under pairs; 13 review findings; remaining API quota 19,603. Classification REVIEW_REQUIRED. The raw capture was runner-local and discarded. These 13 findings cannot be reliably split by cause after the fact.

## Current readiness

Collector screening reason codes now distinguish:
- MISSING_OPPOSITE_SIDE
- DUPLICATE_SIDE
- EXCESS_OR_CONFLICTING_ROWS
- Invalid-row categories (identity/market, side, identifier, point, price, receipt).

Commit ec4febde64fe56e118644db7f2e3905179dc6615 adds aggregate reason counts to runner logs. GitHub collector validation run 39046380279 passed. **This is offline validation, not a new live capture.**

## Next controlled step

Manually dispatch `.github/workflows/odds-api-collector.yml` on main. It will attempt one upcoming NFL event, three player-prop markets, US region, and may consume API credits. Read the latest job logs for the 'Screened', 'Screening failure counts', and 'Screening invalid-row reasons' lines. Preserve only source-verified aggregate results and run URL in research; do not copy raw odds into the public repository or treat API-observed odds as executable NJ prices.

If no upcoming event exists, do not infer a zero-quality result. If API quota or market access fails, preserve the blocker and stop; no repeated blind retries. No automatic schedule or MotherDuck live ingestion is authorized by this note.
