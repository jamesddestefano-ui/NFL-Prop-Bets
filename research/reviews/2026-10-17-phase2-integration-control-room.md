# PRIME Phase 2 — Integration Control Room handoff

Date: 2026-10-17 UTC. Agent: PRIME Lead Software Engineering.
Result: **PASS — engineering, integration, CI and hosted reproduction**;
**BLOCKED — authenticated real outcome-matched model validation**.

## Exact commits and integrations

- [PR #1](https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/pull/1):
  independent review fixes `98ca873738006fc933ce3106940907bba874238b`;
  merged as `42b6f58709a8eec0423d2e3cc0967217020d5b32`.
- [PR #2](https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/pull/2):
  implementation `f37d3b484511e767ea122fe337131f4d97b252e9`;
  merged as `bdb9bbd0447794a5215ab1b30400af51b1da822e`.
- Both merges used ordinary SHA-bound calls after passing push/PR checks and
  independent software review. Main had no branch protection or rulesets at
  inspection; no required checks or protections were bypassed. The reviewer was
  a software subagent, not Claude/Dot or independent NFL model validation.
- Later collector/audit/research commits have advanced main. The inventory below
  is explicitly pinned to `f37d3b4...`, not a live count of those later captures.

## Tests, artifacts and reproducibility

Full command: `/workspace/prime-test-venv/bin/python -m unittest discover -s tests -v`.
**122 tests, OK**, plus existing module-level fixtures. Syntax compilation and
`git diff --check` passed. Two `phase2_report.py` executions produced directories
that matched byte-for-byte. No output or original evidence was overwritten.

PR #1 review fixed malformed training-ID/feature-ID types bypassing holdout
checks, and missing market-side diagnostics. Phase 2 review fixed arbitrary
coverage export fields, missing coverage integrity checks, and unchecked derived
handoffs during replay. Failing-first regressions reproduced each; reviewer
confirmed fixes and no remaining material findings.

[Main Phase 2 run 39072273491](https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/actions/runs/39072273491)
**SUCCESS** at `bdb9bbd0447794a5215ab1b30400af51b1da822e`.
Validation job `117512160496` passed full tests, two-report diff and upload.
Learning job `117512295239` passed registry processing and publication/no-op path;
completed 2026-10-17T21:46:19Z. Other main checks passed: research CI
`39072273573`, strict evaluator `39072273449`. Phase 2 push/PR runs
`39072086636` and `39072169437` also passed.

Main artifacts (metadata and successful upload verified; contents not independently
downloaded): `prime-phase2-39072273491`, ID `12115467080`, 55,779 bytes;
`prime-learning-status-39072273491`, ID `12115667443`, 230 bytes. Retention 30 days.

Reproduction files at `/workspace/phase2-final-artifacts/`, code commit `f37d3b4...`:

| Artifact | SHA-256 |
| --- | --- |
| Authentic legacy coverage | `3977f316b1443785589119ce3e6f511fb46aad29aaf180e0becf6c65f971f59f` |
| Synthetic comparison | `981781657f92c7a892502f2811357dead1503541ef0963b43eb404ca14758547` |
| Deepnote capsule | `b761978d1365e4559a71a0257d7ce9150846c2eea2d53dda8baa2a2c5fdd25f9` |
| Notebook reproduction code | `524d18a3fc1aa5ba87c7f37e9df94bd7aadf0efc9ddb4b985ad357fd009e7b64` |

Main-merge artifact source-commit metadata differs, so its coverage/capsule hashes
need not equal branch-revision hashes. Full local test log: `/tmp/phase2-full-tests.log`.

## Historical coverage and honest classification

At exact inventory revision `f37d3b484511e767ea122fe337131f4d97b252e9`:

| Evidence | Coverage | Limitation |
| --- | ---: | --- |
| nflverse-derived player-game statistics | 24,969 rows | IDs present; no duplicate player/game rows; no independently preserved official-final/publication attestations |
| Forecasts across existing versions | 473 rows | All identities `TEAM_MATCH_CANDIDATE_NOT_VERIFIED` |
| Original forecast input hash checks | 15/15 passed | Integrity does not authenticate source truth |
| Normalized sportsbook observations | 34,505 rows | Private observations, no NJ executability claim |
| Exact same-snapshot paired groups | 16,375 | No inferred settlement certification |
| Duplicate-sided groups | 0 | Not proof of complete market coverage |
| Candidate forecast player/date intersections | 0 | No canonical event join inferred |
| Authenticated legacy external lock receipts | 0 | Legacy schema contains none |
| Verified outcome-matched contracts | 0 | No real outcome performance computed |

Statistics span 2025-09-04 through 2026-10-15; forecasts concern later games.
Normalized files are hash-pinned. Raw-response hashes are retained, but original
HTTP response bytes are absent, so their hashes cannot be recomputed here.
Legacy inventory remains `RETROSPECTIVE_RESEARCH_NOT_ASOF_VERIFIED`; synthetic
fixtures remain explicitly synthetic. No missing odds, timestamps or outcomes invented.

Corrected legacy historical workflow `39071319109` succeeded after PR #1 merge;
artifact `12115596858`, 1,366,186 bytes. Download again returned HTTP 403 from
artifact storage. Its contents/empirical metrics were not independently inspected
here. Current writer passes executable JSON round-trip regression; original
malformed artifacts remain unchanged. This synthetic-threshold replay is not
externally locked real-contract performance.

## Evaluation and continuous learning delivered

The comparison reuses the strict single-model validator and shared scoring
modules: immutable source bytes, reviewed canonical identity, external receipt
binding, feature/model availability, held-out-game exclusion, expected model
versions and predefined out-of-time window. All eligibility/missingness remains
visible. Only identical eligible contracts/outcomes enter model comparisons.

Three-way model Brier/log loss includes pushes; classwise calibration/ECE,
per-market scores, model disagreement and whole-game paired bootstrap intervals
are implemented. Market comparisons require the same exact source snapshot across
models and use conditional non-push scores/calibration. Two-way odds cannot
identify unconditional push mass, so market three-way scores remain null.
Insufficient games produce explicit uncertainty limitations. No superiority is
inferred from market closeness.

Synthetic software test only: three invented games/contracts, one push.
v0 Brier `0.3466666666666667`, log loss `1.1473397920608035`; v1 Brier
`0.39666666666666667`, log loss `1.3391278403619908`. Market conditional scores
use two nonpush cases: Brier `0.25`, log loss `0.6931471805599453`.
These are **not NFL performance, independent model validation, profitability or EV**.

The production registry is intentionally empty. Reviewed real entries pin the
protocol, model versions and sources. Content fingerprints include all underlying
bytes, evaluation code and runtime. Atomic append-only output directories and
checks on every published artifact prevent duplicate scoring/report commits.
Main-only Actions publication writes Commander handoffs; PR validation is read-only.
Daily catch-up detects newly validated entries. Empty-registry no-op succeeded
live; nonempty publication is tested synthetically and awaits a real cohort.

Predeclared classwise ECE alerts recommend investigating input drift on a future
holdout. No automatic fitting, threshold optimization or model promotion. Real
degradation versus reference windows is unmeasured without a preregistered cohort.

## Deepnote hosted verification

Existing private project `3f1b1d1e-9704-4ac5-81ea-016c706f3028`; original v1
notebook preserved. New notebook:
[PRIME Phase 2 Reproduction](https://deepnote.com/workspace/james-4106-48eceaa3-2249-4b92-ab08-e63f2de0a40b/project/PRIME-NFL-Model-Lab-3f1b1d1e-9704-4ac5-81ea-016c706f3028/notebook/PRIME-Phase-2-Reproduction-e57c04c031ae457ba2b91e84f8caacc2),
ID `e57c04c031ae457ba2b91e84f8caacc2`.

Hosted run `18fa3790-460f-42a7-a3cb-59aa4a7f3a59`: **SUCCESS**, completed
2026-10-17T21:44:05.349Z. Snapshot outputs inspected. Printed
`PROJECT_FILE_MOUNT_VISIBLE` and exact comparison hash
`981781657f92c7a892502f2811357dead1503541ef0963b43eb404ca14758547`.
Uploaded project file `phase2/b761978d1365e4559a71a0257d7ce9150846c2eea2d53dda8baa2a2c5fdd25f9.json`
(34,134 bytes) was actually visible to the runtime. Earlier mount failure did not
recur for this run; no platform-wide repair is claimed. A verified inline fallback
was also tested locally and remains explicit.

Notebook imports exact hashed GitHub modules, displays authentic aggregate
coverage and reproduces synthetic scoring. Strict export schemas and hashes cover
archive/files/code/coverage/output. No duplicated hand-maintained scoring, raw
private odds/stat rows, credentials, external downloads or public sharing.
Used existing CPU (Basic), stopped after inspection. No purchase/upgrade or
Deepnote schedule; continuous GitHub-to-Deepnote delivery remains unverified.

## Remaining blockers and recommended Phase 3

1. Preserve genuine external pregame receipts, model versions/prompts and original
   forecast bytes prospectively; never backdate or relabel retrospective replays.
2. Review canonical player/game/event anchors and exact jurisdiction settlement.
   Archive licensed original response bytes plus official-final outcomes,
   publication/correction history and model/feature availability evidence.
3. Assemble a common v0/v1/market cohort with real outcomes. Pre-register realistic
   selection, holdout/reference windows, calibration thresholds, game-cluster sample
   sizes and uncertainty methods. Test improvements on a separate future holdout.
4. Supply independent push probabilities if unconditional three-way market scores
   are required; never infer them from ordinary paired two-way prices.
5. Register reviewed real inputs and verify a nonempty main learning publication.
   Empty no-op and synthetic publication tests do not establish live real scoring.
6. Resolve artifact-storage HTTP 403 for independent ZIP inspection if needed.
   Repository clone/read/push/merge access works; no new GitHub grant was needed.

No wagers, purchases, exposed credentials, API-credit consumption, authoritative
betting-record changes or model promotions. All models remain `MODEL_SUSPECT`,
`bet_eligible=false`.
