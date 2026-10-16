# Claude v2.2 technical protocol — PRIME review (2026-10-16)
Source: user-pasted Claude response. Research-only; no evidence of model edge or authority to replace v2 gates.
## Adopt for operational design
- Timestamp each API capture in UTC; separate observed_at from bookmaker/market last_update; reject post-kickoff observations as pregame closing prices; preserve missing checkpoint attempts.
- Pair sides by event, canonical player, market, threshold, bookmaker, settlement basis and compatible quote times. Preserve original bookmaker names and normalization mappings.
- Use aligned, fresh same-contract book prices; leave-one-book-out no-vig consensus for comparison; never call an outlier a proven edge. If different thresholds, do not map until the interpolation shape is validated.
- Blind ChatGPT/Claude forecasts, locked before seeing one another; include market-only benchmark, forecast sources, momentum/news tags and matched closing observations. Treat future-movement leader/stale classifications as retrospective research, never as known at entry.
- Preserve outcome proper scores as a separate endpoint; closing-move prediction is a hypothesis about market information, not proven betting profitability.
## Unresolved and cautions
- GitHub Actions schedule is best-effort. A :55 run can arrive after kickoff; actual capture time controls. Do not imply GitHub scheduled checkpoints are exact.
- Contract identity must account for provider event-id changes, player aliases and push/void rules; one side missing => no same-book de-vig, but other independent evidence can sometimes support a research benchmark.
- Claude's 300-forecast one-sided clustered regression is a preregistration *proposal*. Do not label failure to reject as proof of zero signal; evaluate confidence intervals, power and later-week validation.
- Logit p_cons = invlogit(l_central-z*sigma) with quadrature components assumes independent uncertainty on the same scale. Cross-book dispersion is not calibrated forecast error, and projection-source overlap matters. Do not deploy as a production bet gate without validation.
- The API's bookmaker market last_update can be different from an individual outcome price change. Preserve both times and quote-age limitations.
- Data retention and cost math require measured API credits and actual quote coverage. Free monthly headroom does not imply historical access at every requested market.
## Priorities
1. Test collector safety: UTC capture, pre-kickoff check, no accidental live-odds ingestion, exact contract side pairing, quote staleness, bounded quota.
2. Freeze October 18 candidate universe before seeing AI calls; record missing prices and real close coverage.
3. Compare locked deviations to subsequent market movement with momentum/news controls; separately score football outcomes when graded.
4. Evaluate cross-book NJ price parity and API quote latency before enabling frequent automatic collection.
No user bet history or governing model policy changed.
