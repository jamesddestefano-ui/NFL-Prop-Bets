# Collector observation-time boundary review

Research-only supplement to PRIME-DOT-20261016-010. Prepared 2026-10-16. Source cutoff: 2026-10-16 19:47 UTC (15:47 EDT). Current main inspected at a1e4d217c57f3c7a5874e038153c2f25e590f999. This note proposes a correction for review; it does not implement a production change or change the assignment's queue status.

## Verified finding

**EMPIRICAL EVIDENCE (code inspection):** The collector assigns a single UTC `now` before its event-list request and odds request. It filters upcoming games against that initial time and writes the same value into `observed_at_utc` and `captured_at`. It does not record completed odds-response receipt or recheck kickoff after receipt. The current main collector blob is 51c556cfa3236bfa766e81c2e5d8aa2e64c77541; the reviewed flaw remained present at the source cutoff.

A request started before scheduled kickoff can therefore receive odds at or after kickoff and retain a pre-kickoff observation label. This is a verified possible failure of the code path, not proof that an existing capture arrived after kickoff. It also prevents precise measurement of news-to-observation and quote-survival latency from the stored observation field alone.

## Sources and original provenance

Access medium for all sources: repository file text retrieved through the GitHub connector on 2026-10-16. No video playback, Odds API request, secret retrieval, or raw quote redistribution was performed.

- [Original collector source at 5323b330f168ac7517b7089f7adf9a9b8f609f46](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/5323b330f168ac7517b7089f7adf9a9b8f609f46/scripts/odds_api_collect.py).
- [Collector verified at the current source cutoff](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/a1e4d217c57f3c7a5874e038153c2f25e590f999/scripts/odds_api_collect.py#L21-L40).
- [Original sample at 7dc0af3257ea58b254dd767d747abca44c70ccad](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/7dc0af3257ea58b254dd767d747abca44c70ccad/data/odds_api/2026-10-16T19-03-02Z-sample.json).
- [Workflow at the verified source cutoff](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/a1e4d217c57f3c7a5874e038153c2f25e590f999/.github/workflows/odds-api-collector.yml).
- [V2 controlling overlay](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/a1e4d217c57f3c7a5874e038153c2f25e590f999/config/prime_ev_playbook_v2.md).
- [Research handoff protocol](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/a1e4d217c57f3c7a5874e038153c2f25e590f999/config/agent_research_handoff.md).
- [Preserved earlier feasibility report](2026-10-16-capture-feasibility.md).

The sample's recorded capture value is 2026-10-16T19:03:02.636483+00:00; scheduled kickoff is 2026-10-18T13:30:00Z. An independent aggregate-only parse found 361 side rows, seven bookmaker keys and three markets. Grouping by event, bookmaker, player, market and point gives 174 Over/Under pairs and 13 one-sided groups. All observation values equal the recorded capture value. Completed receipt timing is unknown.

The sample supplies new evidence of an existing artifact after the earlier feasibility report's cutoff; it does not erase that report's original knowledge state. Neither the counts nor the timestamps prove NJ executability, historical close coverage, key rotation, a profitable wager, or an actual post-kickoff response. The inspected workflow is manually dispatched and has no recurring trigger; it grants GitHub contents-write permission to save outputs. Read-only sportsbook retrieval does not mean read-only repository permissions.

## Minimal correction proposed for review

**MODEL ASSUMPTION / PROPOSED VALIDATION POLICY:** Treat completed response-body receipt as the conservative time the odds became observable to PRIME. Preserve request start, receipt completion, parsing completion if separately measured, and file-write time as distinct events.

1. Record UTC request-start and response-complete values separately for the event-list and odds requests. Do not relabel request start as completed observation.
2. Check the scheduled kickoff before requesting odds and again after the odds response is complete. Admit a pregame observation only when completed receipt is strictly earlier than the scheduled cutoff; equality fails.
3. Keep the scheduled cutoff conservative when actual kickoff is delayed. Do not infer permission to extend the pregame window merely because the game appears not to have started. Any future alternate cutoff needs explicit authoritative evidence and reviewed rules.
4. Keep provider `market_last_update` and `book_last_update` distinct from PRIME receipt time. A source update timestamp does not establish when PRIME obtained the data.
5. Record monotonic elapsed duration alongside wall-clock UTC timestamps. Flag and quarantine inconsistent ordering, negative wall-clock elapsed time, or material wall-clock/monotonic disagreement. Monotonic duration detects inconsistencies; it does not itself establish absolute UTC accuracy.
6. If boundary-rejected responses are retained for diagnostics, label the exclusion reason and keep them out of pregame forecast, closing-line and latency cohorts.
7. Preserve all existing sample bytes. A separate provenance note may explain that the old observation timestamp represents collection start and receipt completion is unavailable. Do not manufacture replacement receipt times.

These are review proposals, not adopted methodology or deployed code. They support the existing same-contract, timestamp-integrity and genuine pre-kickoff requirements.

## Deterministic boundary checks performed

**VERIFIED MATHEMATICAL PRINCIPLE:** For kickoff K, initial time S and completed receipt R, S < K does not imply R < K.

Four synthetic UTC predicate cases were executed in JavaScript with K = 2026-10-18T13:30:00Z. The current predicate was represented as S < K; the proposed receipt predicate was represented as R < K.

| Request start | Completed receipt | Current predicate | Proposed receipt predicate |
|---|---|---|---|
| 13:29:50Z | 13:29:55Z | Admit | Admit |
| 13:29:50Z | 13:30:00Z | Admit | Reject |
| 13:29:50Z | 13:30:05Z | Admit | Reject |
| 13:30:00Z | 13:30:05Z | Reject | Reject |

All four proposed expectations passed. These are deterministic synthetic predicate checks, not production Python tests, HTTP integration tests, historical replay, or empirical NFL performance evidence. They demonstrate the boundary logic only. Delayed event-list responses, delayed response bodies, missing or malformed kickoff values, and clock rollback remain proposed integration cases.

## Confidence, limits and next decision

Confidence is high in the inspected timestamp assignment and the synthetic counterexample. Existing captures' true completed receipt times remain unknown. No claim is made that a specific stored sample was post-kickoff or that any betting recommendation was affected.

PRIME should review the minimal correction before relying on these observation labels for precise pregame eligibility or latency analysis. Until corrected and tested, treat existing observation values as collection-start timestamps with unknown receipt completion. No production code, workflow, authoritative record, sample, controlling rule, or queue status is changed by this supplement.
