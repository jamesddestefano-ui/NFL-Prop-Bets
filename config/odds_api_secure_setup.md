# PRIME: The Odds API secure connection checklist
Date: 2026-10-16. Scope: NFL player props only.

## Security prerequisite
The initial API key appeared in a user-shared screenshot. Treat it as exposed. Rotate/revoke it through The Odds API account/support and create a new key. Never paste keys in ChatGPT, Dot, Claude, GitHub source, issue text, PRs, Actions logs, screenshots or reports. Never reuse the exposed key. If provider rotation is unavailable, request revocation/reissue.

## Configure the repository secret
Repository: jamesddestefano-ui/NFL-Prop-Bets
GitHub web UI: Settings -> Secrets and variables -> Actions -> New repository secret
Name: ODDS_API_KEY
Value: the NEW, rotated key only.
Do not put it in a GitHub Actions *variable* or a checked-in .env file. Only the user/authorized admin can securely enter it; PRIME does not have a GitHub Actions secret-write integration in this chat.

## Minimum safe collector architecture (pending implementation)
- GitHub Actions workflow triggered manually first (workflow_dispatch), with read-only repo access and no automatic betting actions.
- Inject secret via environment variable `ODDS_API_KEY: ${{ secrets.ODDS_API_KEY }}` only inside a trusted script; never echo/print request URLs containing keys, exceptions with full URL, or raw response headers.
- Prefer Authorization header if officially supported; otherwise carefully redact API-key query parameters from all logs and error paths.
- Begin with one low-credit NFL event/market/region query. Confirm exact vendor documentation and request-cost formula before scheduling.
- Collect event id, kickoff, home/away, bookmaker key, jurisdiction/region, player name, market key, outcome side, point, American odds, source last_update if provided, observed_at UTC, and API quota headers/remaining credits when available. Preserve same-contract opposite side; missing values null.
- Never assume US regional quotes equal a live New Jersey DraftKings screen; compare contemporaneous screenshots.
- Exclude pre-kickoff contamination and never infer a historical quote from a new response.
- Write sanitized, append-only data to a separate `data/odds_api/` namespace (or an immutable research archive), no secrets or account data, with data retention and GitHub Actions permissions considered. Never overwrite canonical bet_history, user tickets, results, or model decisions.
- Run first manually, inspect quota and captured contract completeness, then consider a low-frequency schedule. Free credits can exhaust quickly. No subscription purchase is required for initial validation.
- Dot reads only sanitized GitHub outputs; direct API access from Dot is not established. Claude also receives only user-shared, frozen price observations.

## Readiness checklist
[ ] Initial key rotated/revoked
[ ] New key saved as ODDS_API_KEY GitHub Actions secret
[ ] One trusted collector workflow implemented and reviewed
[ ] Manual test run verified with sanitized logs
[ ] Quote coverage compared against actual NJ sportsbook screenshots
[ ] Credit consumption checked before enabling recurring sweeps

No API key is stored in this document.
