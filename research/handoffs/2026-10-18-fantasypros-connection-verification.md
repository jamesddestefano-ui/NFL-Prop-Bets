# PRIME Commander — verified FantasyPros connection and activation blockers

## Verified result

The user-configured GitHub Actions secret successfully accessed the documented NFL news endpoint with header-only x-api-key authentication. Exactly one request was made: `GET /nfl/news?category=injury&limit=1`. HTTP200; one news item; full supplied response-schema validation passed. No retry, other endpoint probe, purchase or subscription change occurred.

- Private draft PR: https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/pull/4
- Final reviewed implementation commit: `1330aba989793b9371ac0262fdb2a6d87f945bb3`.
- Original implementation: `1eb1e4f36644b975272a2aa3c8178da1aebe9b5e`.
- Authenticated Actions source commit: `4afa8f6158c50fef9697e52f28d755c5de028c20`.
- Durable reservation commit, published before the provider call: `520aa2f03ba9d01321fc71e54caf8a531302eab3`.
- Preserved response/result commit: `82b457557bfb0f01204fd7266dfa17609ea68514`.
- Actions run: https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/actions/runs/39082676184 — validate and connection-verification jobs succeeded.
- Request sent: `2026-10-18T00:25:47.563704Z`; completed receipt: `2026-10-18T00:25:47.793609Z`.
- Original response body SHA-256: `aa8ac8b6ccfefa9dd91935d73afd2488995d0b8c466928546e3907c0dd09f7ba`.
- Capture/derived identity SHA-256: `f0edeb26534964e9b2f8e361802c24a53c8b7d88aab22acebc16a1a2c26285cf`.
- Private artifacts: `12119343078` (single connection evidence), `12120040483` (boolean-only readiness). Git source/result files were fetched back and body/receipt hashes verified. Artifact ZIP download is not separately claimed.

The configured key works for this tested endpoint. **Rotation/revocation remains UNVERIFIED.** A successful request cannot prove that the earlier exposed key was revoked. Secret metadata listing returned403; subsequent Actions boolean checks confirmed a nonempty secret was available without revealing it. No key was printed, copied into source or passed in a URL.

## Endpoint and usage status

| Endpoint | Implemented and offline contract-tested | Live access verified |
| --- | --- | --- |
| `/nfl/news` | Yes | HTTP200, one injury-news item |
| `/nfl/injuries` | Yes | Not individually tested |
| `/nfl/players` | Yes | Not individually tested |
| `/nfl/{season}/projections` | Yes | Not individually tested |
| `/nfl/{season}/consensus-rankings` | Yes | Not individually tested |
| `/nfl/{season}/player-points` | Yes | Not individually tested; fantasy scoring only |

No recognized usage-limit headers were retained in the response. Numeric provider quotas, request costs, plan terms and access permissions for the other endpoints remain UNKNOWN. The user-supplied contract supplies no numeric request entitlement. Do not infer unlimited or cost-free usage from HTTP200. Local safety ceilings are three attempted requests per UTC day and a 900-second identical-request interval; they are not provider limits. HTTP429 creates a conservative global cooldown with Retry-After respected and no automatic retry. HTTP401/403 cannot be cleared by unrelated policy edits; genuinely newer reviewed key-rotation evidence is required.

The user-authorized connection exception permits only this fixed single request on the exact feature branch. Its reservation is committed before the provider call, preventing failed result publication from erasing consumed budget. Routine ingestion remains enabled=false, standard probe allow_probe=false; no production activation or model-feature promotion occurred. The PR remains draft/unmerged to isolate the secondary source from Sunday's prospective pilot.

## Tests and independent engineering review

Full local suite: **197 tests passed**, including **31 FantasyPros offline tests**. Compileall, workflow YAML syntax and whitespace checks passed. Final implementation CI passed: FantasyPros validation39082869009, shared Phase2 validation39082869019 and prospective safety validation39082869031. Automatic events skip the live verification job; only the explicit manual event can call the provider.

Independent internal review found and fixed injury-year scope loss, authentication-block bypass through unrelated policy edits, and alternate-branch verification replay. All31 FantasyPros tests were independently rerun successfully after fixes; no material finding remains. This internal engineering review is not an external model response or independent predictive validation. Live access facts above were verified by the lead agent from actual Actions and Git evidence.

## Data integrity and research integration

Original user contract SHA-256 `d76e56d4486716edb6d17137c68d27c4924b111f500abe1cd9e223fb1690adcd` is pinned with exact original YAML and derived JSON. Schema compatibility repairs only unquoted YAML null type tokens and specializes documented NFL unions; strict values/oneOf are not weakened. Projection/schema inconsistencies remain documented blockers for affected payloads.

Ingestion preserves original private response bodies, source URL, HTTP receipt time, provider timestamps as supplied, provider IDs, team/season/week where available and source/code/policy hashes. Missing, date-only and timezone-naive publication times remain unknown rather than fabricated UTC values. Raw and normalized source artifacts live under data/fantasypros, separate from data/odds_api.

Canonical IDs require reviewed exact player-ID crosswalks and game context, source hashes, reviewed team/week/season and pregame availability. Changed normalized values cannot inherit original source hashes. FantasyPros projections/rankings are research benchmarks, not verified outcomes; fantasy points cannot settle NFL prop contracts. No mean-to-probability conversion, fuzzy identity promotion, private league import, roster/transaction change, or betting-record modification occurs. Out-of-time evaluation remains required before any production probability use.

## Remaining blockers and next actions

1. Independently establish exposed-key revocation/rotation through authorized owner evidence; do not ask for or publish key values.
2. Obtain reviewed actual provider quota/retention/usage terms and endpoint permissions before routine ingestion. The single test does not verify every subscription scope.
3. After Sunday-critical operations, review the separate draft PR. Standard live probes/ingestion require genuine rotation and usage evidence; do not reopen this one-time exception for extra calls.
4. Capture bounded injury/player/projection data only once those gates are met, review canonical mappings and conduct out-of-time projection/calibration studies. Do not retrofit this new source into the already-defined pilot.

All models remain MODEL_SUSPECT, bet_eligible=false and production_feature_eligible=false. Existing sportsbook observations, The Odds API frequency and Sunday pilot workflows are unchanged. No wagers or additional purchases.

This public handoff contains only derived verification metadata and source hashes. Original API content, credentials, account details and raw player/news records remain private.
