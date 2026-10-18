# PRIME Central Command — Monday controls deployed; external activation gates remain

Original October18 status remains PILOT_INCOMPLETE. Its original protocol and542 supplemental nonqualifying IDs are unchanged.

## Completed engineering and verification

PR7: https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/pull/7
Reviewed code: `c7a57f469cd2e66a64fefe3fc264e29c8b66f371`.
Merge: `015992e2a94c25f7ea4bd15412ecd6f672d9daa7`.

Implemented explicit Monday event/date/capture/freeze/lock contexts in shared validators; immutable full-cohort freeze and retries; hash-verified originals; shared canonical identity/input leakage checks; separate GitHub-server publication receiver; reviewed activation gate and successful pre-window registration requirement. Sunday defaults are preserved. No duplicated scoring, invented probabilities or retrospective relabeling.

217 full local regression tests passed, including12 Monday timing, identity, source, activation and retry cases. Independent review fixed one per-step token-scope issue; no remaining material findings. PR safety39144613240 and Phase2 CI39144613236 passed. Post-merge research39144729566, safety39144729689 and Phase2 CI39144729587 passed.

Read-only main Actions preflight https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/actions/runs/39144751389 succeeded. Artifact12142842981; immutable evidence commit `caa1804fbb1829e51a9ddaafb013e1d545a7acb9`; GitHub-server creation2026-10-18T16:23:06Z. Registration SHA256 `9e0fb01a76c34cc286ac1de11160ac3de3761d8c2abfe10b7902e49fc7dd4594` fetched/read back; all70 registered source hashes independently recomputed at its exact head. Preflight registration eligibility is false; runtime enabled=false and readiness_review=null. This proves permission/artifact/source-binding plumbing, not independent model access, external observer coverage or activated predictions.

Official schedule evidence PR8 https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/pull/8 merged at `e543f0449c7e948700e10f9b822e856967e9ee43`. Reviewed evidence commit `3267b3e1553323f28bd37ebc827d1be8450bbe8d`; safety CI39145548205 and push CI39145369090 passed. Private source bytes and retrieval record retained. Official https://www.49ers.com/schedule/ returned200 at2026-10-18T16:26:09.729225Z, SHA256 `4210b358d101e206d1bd4d4e9e4aa921d5d2da6e8db0cd050e691769408aaad5`, uniquely identifying Washington atSanFrancisco, official game `aad58635-4feb-11f1-abca-2c54536568a9`, kickoffOct20 00:15UTC /MondayOct19 20:15EDT. This matches independently retained provider and ESPN schedules. Publication/update timestamp is unknown. Schedule evidence does not verify player mappings or final statistics.

## Candidate schedule and invocation coverage

America/New_York (EDT): actual receiptsMonday18:00–19:00; warn18:30; freeze attempts19:03/07/11; independently received cohort strictly before19:15; missing-model warning19:30; genuine forecast receipt/server-lock strictly before19:45; kickoff20:15. Outcome-review targetTuesday10:00EDT, contingent on genuinely final authoritative NFL sources; missing/corrected results remain pending or append-only.

Readiness is invoked by existing collector completion, publication-receiver completion, explicit manual dispatch and dated warning/cutoff schedules. It reads actual receipt times and validates raw hashes and shared pair eligibility; scheduled time never qualifies a capture. Repeated unchanged evidence deduplicates. No provider requests or frequency increase are performed by the controls. Best-effort GitHub scheduling cannot independently detect its own absence.

## Remaining true blockers — activation stays disabled

Tracked privately in https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/issues/9 :

- Independently verified observer/operator and proven quota-respecting fallback execution.
- Genuine independent Claude submission channel and actual external model response. No usable Claude connector/CLI was available; internal agents are not substitutes.
- Reviewed canonical player/game/settlement mappings and feature availability for actual frozen contracts.

Do not mark these verified from successful tests or preflight. Preserve genuine reviewed source evidence, then commit a readiness review and rerun an eligible pre-window registration beforeMonday18:00EDT. Policy/control changes invalidate prior source registration. If these prerequisites cannot be satisfied prospectively, leave disabled, mark missing evidence, and preregister a subsequent slate. Never reconstruct missed locks.

All models remain MODEL_SUSPECT and bet_eligible=false. No wagers, account actions, additional purchases, exposed credentials, expanded Odds API collection or authoritative betting-record edits. Source bytes stay private; this handoff is sanitized derived evidence only.
