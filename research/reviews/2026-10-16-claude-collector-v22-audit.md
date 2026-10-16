# Claude v2.2 collector audit — user-provided handoff, 2026-10-16

Source: Claude report pasted by user. Reported test counts and numerical market findings are Claude's claims, not independently reproduced in this handoff. Four code files were described as "attached" but their contents were not supplied in the conversation; do not claim they are installed.

## Priority defects
1. v1 captures only upcoming[0], which can be the 9:30 AM London game and cannot enter a 10 AM pregame cohort.
2. v1 uses string membership `market.get("key") not in MARKETS` rather than exact market-key set membership.
3. v1 timestamps observations before HTTP calls; v2 must preserve request_sent_utc and response_received_utc for each event and compare the latter strictly against kickoff.
4. Concurrent direct-to-main pushes can conflict; use workflow concurrency and bounded rebase/retry, or separate immutable artifacts.
5. GitHub scheduled workflows are best-effort; never equate intended cron time with actual capture or closing quote time.
6. Quote age should use market_last_update when bookmaker last_update is absent; older markets are AGE_SUSPECT, not automatically exploitable stale prices.
7. Review raw odds redistribution rights before publishing further snapshots in a public repository; prefer private raw storage or permitted derived statistics plus hashes.

## Proposed contract and capture schema
run_id, event_id, commence_time, normalized player_id (with alias mapping and collision controls), market_key, point, bookmaker, side, pair_id, contract_id, paired, missing_side_reason, region and NJ executability classification, request_sent_utc, response_received_utc, market_last_update, raw_response_sha256, is_pregame, credits_last. Side is part of contract_id but not pair_id. Normalize with care: removing Jr/Sr/II/III can collapse distinct players; do not assume normalized name alone is a globally unique player identifier.

## Claude's reported sample findings (not independently reproduced here)
361 side quotes, 174 pairs and 13 unpaired; 31 player-markets, 29 with 3+ book modal-line consensus; 252 side prices evaluated; two small positive apparent edges (+1.31pp and +0.28pp), neither near v2's 4pp gate. NJ-only book filtering reportedly reduces consensus coverage to 16/31. Do not treat these as current executable bets.

## Market methodology proposed for prospective testing
Pair exact two-sided quotes. Proportional de-vig per book. Compare same-line books only; modal line and >=3 books for LOO consensus. Use equal-weight logit consensus initially, preserve dispersion, and classify AGE_SUSPECT/FRESH_DIVERGENT/STALE_CANDIDATE/NORMAL as *research flags*. A 0.05 logit dispersion floor is a heuristic, not a validated statistical threshold. Do not map different lines without actual alt ladders and validation. Offshore prices can be reference-only if legally permitted; never label them NJ executable.

## Sunday protocol
Pre-register eligible 1 PM games and exact markets, freeze cohort before 10:15 AM ET; user-provided Claude outputs and PRIME outputs must be independently locked before 11:30 AM; 12:56 close attempt must use actual response_received_utc strictly before kickoff. Compare Over-only AI logit deviation to matched closing movement with no post-kickoff backfill. Missing line match => missing close. Report denominators and news/market momentum; descriptive only for one slate.

## Preconditions for implementation
Obtain actual Claude files (odds_api_collect_v2.py, market_consensus.py, odds-api-collector-v2.yml, test_collector_v2.py), inspect for secrets, cost controls, external calls, exact contract identity, and legal data handling. Run local tests then bounded live validation before enabling a schedule. Do not overwrite v1 until v2 passes A1-A4 and quota checks. Do not purchase anything or place wagers.

Status: DESIGN RECEIVED; SOURCE FILES NOT RECEIVED; NO V2 DEPLOYMENT.
