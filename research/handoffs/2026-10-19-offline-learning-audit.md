# PRIME offline learning audit — no authenticated performance cohort

Executed October19 UTC (October18 EDT); exact test and diagnostic execution times are in the accompanying aggregate artifact. Source snapshot: private repository `ae28a7e0d378cefd8a8fecea2a397cd879b737b9`;172 audited local code/test/data paths match its remote Git blobs. Public governance baseline: `ec07a1cd7bd39195d17f20e31930b5a1c9b7a474`. This is an offline evidence audit, not pilot activation or a new scoring framework.

## Capabilities reused and verified

| Capability | Classification | Existing implementation / evidence |
|---|---|---|
| Three-way Brier, push accounting, log loss | IMPLEMENTED AND TESTED | `settlement_calibration.py`, `verified_historical_evaluation.py`; half-sum Brier, capped NLL and zero-probability-outcome count. No void-to-loss substitution. |
| Reliability buckets / classwise calibration | IMPLEMENTED AND TESTED | `verified_historical_evaluation.calibration`, `compare_model_bundles`; real calibration BLOCKED BY DATA. |
| Model/market matched comparison and disagreement | IMPLEMENTED AND TESTED | `compare_model_bundles`; exact canonical contracts/outcomes and identical market snapshot required. Two-way market scores remain conditional on non-push; no inferred market push mass. |
| Game-clustered uncertainty | IMPLEMENTED AND TESTED | Seeded whole-game paired bootstrap; insufficient-game refusal; preserves within-game dependence. Intervals are descriptive and do not repair selection bias. |
| Leakage and outcome-join guards | IMPLEMENTED AND TESTED | Source hashes, reviewed identity, exact event/player/market/line/book/side/settlement keys, lock-before-kickoff, feature availability/publication before generation, training-game/holdout exclusions, duplicate/conflicting-identity rejection. |
| Version tracking and deduplicated evaluation | IMPLEMENTED AND TESTED | `learning_pipeline`: source/code/protocol/Python fingerprints; expected model version; append-only artifacts and replay tamper checks. Existing registry is empty; no authenticated evaluation run exists. |
| Forecast → lock → reviewed outcomes → scoring | IMPLEMENTED AND TESTED | `pilot_evaluation`, shared verified evaluator; original forecast-byte preservation tested. Actual end-to-end NFL cohort is BLOCKED BY DATA. |
| FantasyPros feature adapter | IMPLEMENTED AND TESTED | Original-body membership, reviewed ID/team/season/week context, receipt-as-availability, no naive-publication inference; fantasy points excluded from official outcomes. |
| Identical feature-packet assertion across model comparisons | GENUINELY MISSING for identical-input experiments | Synthetic probe changed one model's feature manifest and still matched3contracts. General comparator permits different model inputs by design; contract matching must not be called identical-input evidence. No production change made. |
| Independent truth of reviewed source/receipt attestations | IMPLEMENTED BUT NOT VERIFIED on legacy records | Schemas/hash checks enforce structure/integrity, not external truth. Human/provider authentication cannot be invented by code. |

Audited schema boundaries are existing strict manifests/array validation, fixture protocols, registry schema_version checks and FantasyPros OpenAPI/adapter contracts. No parallel schema or scorer was created.

## Read-only reconciliation of all473 legacy forecast rows

Five files contain101+101+101+82+88 rows. All473 original identities are `TEAM_MATCH_CANDIDATE_NOT_VERIFIED`. There are **0 authenticated forecasts with verified outcomes**,0 reviewed legacy lock receipts, and0 player/date candidate outcome intersections in the retained statistics. These are not forecasts eligible for a retrospective reconstruction of a prospective cohort. Declared generation times remain declared, not converted into observed receipt times. GitHub possession evidence, where available, is not asserted to be nonexistent; no reviewed binding pregame receipt is registered for this legacy schema.

The files cover101 logical event/player/market/line/kickoff groups, not101 fully specified sportsbook contracts. Grouping additionally by declared model label, explicit document version and code-hash evidence yields271 groups and**202 repeat rows beyond the first**, all from repeated v0 snapshots. No within-file duplicate logical rows or conflicting probability groups under that grouping were found. Every row is retained with original file hash, row index/hash, original status, identity status and explicit exclusion reasons in the private compressed inventory. These group counts are diagnostic keys, not authenticated independent-sample counts.

Only88rows carry a declared model-code hash and explicit document version(v1.1). Grouping on the model label alone would collapse189groups and wrongly conflate versions: v1 andv1.1 reuse the same row-level label. Neither timestamps nor missing code hashes are inferred. Original classifications and source records were not changed.

## Player intelligence and available data

Retained nflverse-derived history has24,969 player-game rows, no duplicated player/game keys, with targets/receptions/receiving yards; snap shares, carries and routes are absent from these legacy files. Its game dates and capture times do not establish historical publication availability or authoritative official-final outcomes.

Two genuine retained FantasyPros news captures normalize to two rows but the same single body/item; both bodies were hash-verified. Publication timezone is unresolved, and receipt time remains the conservative availability bound. There are no retained injury-endpoint or projection-endpoint captures and no reviewed canonical FantasyPros feature rows admitted by this audit. No StatsHawk artifact was found in the audited repository tree; connected access is not assumed. **Comparable provider-disagreement pairs=0**, not evidence that providers agree. No NFL, FantasyPros, StatsHawk, MotherDuck or Deepnote paid/API requests were made; repository tools suffice for this diagnostic.

Existing reports already label82model comparisons as descriptive disagreement,101market comparisons as experimental, all101later closes missing, and six negative-yardage input issues for review. Those records remain unchanged; none is a calibration or predictive-superiority result.

## Learning-cycle audit, gaps and minimal next actions

The existing `.github/workflows/phase2-learning.yml` validates, reproduces artifacts, then evaluates newly reviewed registry fingerprints and publishes only new outputs. A temporary offline run of the actual empty registry returned0new/0skipped/0pending; no model promotion or fake evaluation was created. Existing synthetic comparison reproduced byte-identically twice:3matched SYNTHETIC contracts, deterministic canonical hash `a5d6ca1d0c98f04a016121b1303605198ed9d360a35049707de7d0e5c1ddf642`. This tests mechanics only; synthetic probabilities/outcomes do not measure NFL performance.

- **P0:** keep unauthenticated history out of scoring, retain exact identity/as-of guards, and do not describe contract-only comparisons as identical-input experiments. Missing original locks, feature-availability evidence and official outcomes are data blockers, not broken scoring functions.
- **P1 proposal requiring independent architecture review before engineering:** add an explicit protocol-specific identical-input packet assertion when such an experiment is required; preserve legitimate different-feature v0/v1 comparisons. Do not change the general comparator automatically.
- **P1 documentation gap:** the existing inventory emits a stale blanket blocker saying original odds bytes are absent, although retained raw response files now exist. This audit does not adopt that sentence as fact or claim all market originals were authenticated. Scoped source-presence verification is a minimal future correction; no unrelated implementation performed.
- **P2:** no new dashboard needed. Publish aggregate diagnostics using the existing report/capsule route when authentic samples arrive. Hosted analytics were not executed or claimed current.

## Checks and disposition

**74targeted offline tests passed**,0failures/errors/skips,2026-10-19T01:08:44.943650Z–01:08:46.605391Z,elapsed1.662seconds. Tested verified evaluation, Phase2 comparison, learning pipeline, historical integration, pilot bridge, FantasyPros adapter/client and Deepnote capsule. Additional checks verified all473 row references/hashes, compressed-inventory roundtrip, deterministic fixture output and172 remote Git blob matches. No full suite rerun or new CI result is claimed.

Measurable improvement: a complete traceable473-row evidence inventory, explicit202repeat-row accounting, honest version separation, provider deduplication and a demonstrated identical-input diagnostic boundary. **No authenticated Brier/log-loss/calibration or provider-disagreement performance can be reported.** Original evidence was preserved; no material engineering was performed, so no architecture approval was assumed.

MODEL_SUSPECT=true;bet_eligible=false;qualifying_groups=0;three-book protocol unchanged;prospective runtime disabled. No wagers, purchases, credential exposure, retrospective promotion or authoritative-record changes.

Private row-level evidence and reproducibility artifacts: commit `562270a5f6c4d5cd3588f3c6e4680a20d0c3bafd`, folder `research/reviews/2026-10-19-offline-learning-audit/`. Only sanitized aggregate diagnostics accompany this public handoff.
