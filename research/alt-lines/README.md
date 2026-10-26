# B18 — isolated alternate-line research (draft scaffold)

Status: **capture scaffold only; unvalidated; no official PRIME picks**.
The Claude artifact supplied for the controlling specification was not readable from this environment, and `docs/PRIME_PLAN.md` was not found in either accessible branch. Reconcile the implementation against those authoritative documents before live deployment.

## Boundaries
- Separate manual workflow, explicitly dispatched per NFL event and snapshot.
- Three main markets and their three corresponding alternate markets, seven configured books.
- Sunday / Thursday / Monday require separate manual dispatches at freeze and T−30 / T−15 / T−5.
- Missing API market/book coverage is reported, never fabricated.
- A dry-run preflight does not call a billable endpoint. Live capture requires `--execute`.
- Responses live in `data/alt_lines/runs` on the runner and an isolated workflow artifact. No commit, no official dataset mutation.
- Retain original API response and request coverage; API observations are not executable prices.

## Incomplete / gated
- Freeze definition and seven book IDs need reconciliation to B18 spec.
- API cost estimation and permissions/credit budget pending.
- nflverse pbp ingest, Bayesian shape fitting, anchor pricer, Monte Carlo bootstrap, rung selector, 2025 OOS checks, and report generator have **not** been implemented here.
- Nov 1 dry run is not an evaluated forecast; preregistration requires James's approval by Nov 6.
- Untrusted or missing historical data must never be silently replaced with synthetic observations.

No files in `scripts/` or official PRIME workflows are changed.
