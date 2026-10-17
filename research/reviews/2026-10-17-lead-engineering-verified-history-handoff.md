# PRIME Lead Engineering — verified historical evaluation handoff

Execution: 2026-10-17 UTC. Scope: NFL player-prop research only.

## Delivered for review

[Draft PR #1](https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/pull/1)
adds a separate offline provenance-pinned evaluation path in the private evidence
repository. It preserves existing rolling diagnostics, model versions, original
sportsbook observations and authoritative betting records. It is not merged.

Exact private commits:
- `6a03e4655617c6dcbe674f1c94c6cb37f9bbdd37`: evaluator, schema, synthetic
  bundle, regressions and Actions integration.
- `6359eca0711480218aeb7ff08a4fbe082021fb54`: review fixes and future legacy
  historical-manifest serialization repair (current PR head).
- Base: `bc134b0b95677c282accd5bd8bd3092ad126e4ad`.

Contract: hash-pin original source artifacts and input documents; reviewed exact
player/event-to-canonical-game identity; generation <= reviewed external lock
receipt < kickoff; historical feature/model availability checks and held-out-game
exclusion; explicit abstention/missingness denominator. Source authenticity and
timestamps remain reviewer attestations backed by pinned evidence, not claims
derived from a VERIFIED label or Git commit date.

Scoring: WIN/PUSH/LOSS half-sum Brier, capped log loss, classwise calibration,
and exact-book/line/rule market no-vig comparison conditional on non-push.
No unconditional market push probability is fabricated. Missing/stale markets
do not erase eligible model outcomes. Void/unsupported contracts fail closed.

## Executed validation

- Full private repository command: `/workspace/prime-test-venv/bin/python -m
  unittest discover -s tests -v` — **100 tests, OK**, including 21 evaluator
  tests and 1 executable legacy workflow-writer regression. Python 3.12 locally;
  GitHub workflow uses Python 3.11. Initial workspace lacked polars/duckdb;
  installed the existing research requirements in an isolated environment.
- Syntax compilation and `git diff --check` passed.
- Separate code reviewer reproduced three defects (near-certain-push numerical
  instability, provider aliases duplicating canonical contracts, ignored extra
  lock receipts). Added failing tests, fixed each, and reviewer independently
  reran all 22 targeted tests. No remaining important review findings. This was
  a software-review subagent, not Claude/Dot or independent model validation.
- Two CLI executions at final head produced identical synthetic reports:
  SHA-256 `d4681e2490c88f2f4aacd17658046133b822b3adc969b6594c1ce52dc8b0b3b5`.
  Bundle: `tests/fixtures/verified_history_v1/manifest.json` at that commit.
  Local reports: `/workspace/prime-validation-artifacts/final-evaluation.json`
  and `final-reproduced.json`; test log and environment snapshot alongside them.

## Verified GitHub CI and artifacts

[Push run 39070559714](https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/actions/runs/39070559714)
completed **SUCCESS**, exact head `6359eca0711480218aeb7ff08a4fbe082021fb54`.
Job `117507096332` confirms offline regressions, two-run byte comparison and
artifact upload all succeeded (completed 2026-10-17T21:21:11Z).

Artifact: `prime-verified-history-39070559714`, ID `12115051988`, 4,667 bytes,
not expired at inspection, 30-day retention. Contains evaluation/reproduced JSON,
SHA256SUMS and Python version. Artifact metadata and successful upload were
verified; hosted artifact contents were not independently downloaded. The new
PR check also succeeded: run `39070579432`, job `117507158113`.

Synthetic expected output: 3 scored invented contracts, 1 push included,
three-way Brier `0.39666666666666667`, log loss `1.3391278403619908`.
Matched non-push comparison has 2 cases: model Brier `0.2777777777777778`,
market `0.25`; model log loss `0.752038698388137`, market `0.6931471805599453`.
**These are software fixture values, not historical NFL performance or evidence
of positive expected value.** Do not infer improvement or sample independence.

## Reconciled historical handoff

Read the existing
`2026-10-17-model-development-historical-provenance-artifact-audit.md` rather
than duplicate its metric claims. Independently verified original historical
run `39052407959` and all job steps succeeded; artifact `12107713980` exists.
This environment's attempt to download that old artifact returned HTTP 403 from
artifact storage, so its empirical contents/metrics were not independently
revalidated here. The existing handoff's malformed writer was independently
reproduced by executing the current workflow's actual embedded Python on local
synthetic inputs (strict JSON `Extra data` failure). The PR now writes a real
newline, asserts the JSON round trip and tests source-hash reconciliation.
Old artifacts remain unchanged. A fresh real historical workflow has not been
dispatched; the repair is verified in local tests and new branch CI only.

## Remaining blockers and next owners

1. Integration Control Room: review/merge PR #1; current changes are branch-only.
2. Identity/Audit owners: assemble a common cohort of reviewed canonical
   player/game mappings, final official outcomes and exact paired market source
   records. Do not infer missing identities from names or cross-line quotes.
3. Forecast/Model owners: supply genuine external pregame lock receipts and
   original as-of feature/model availability evidence. Legacy date-only replay
   cannot be promoted into prospective evidence. Training/model selection
   membership and source truth require independent review.
4. After merge, run the corrected historical workflow to create a new immutable
   artifact and verify strict provenance parsing; retain its synthetic-threshold
   limitations. No prospective pilot freeze or protocol was changed.

No API credits, purchases, wagers, account actions, repository-access changes,
collector dispatches, model promotions or authoritative record changes.
`MODEL_SUSPECT` and `bet_eligible=false` remain in force. No claim that a Dot
task was picked up or that Claude supplied a forecast/review.

## PRIME HANDOFF

- **AGENT:** PRIME Lead Software Engineering
- **TASK:** Reproducible identity/provenance-safe historical evaluation pipeline
- **RESULT:** PASS (software tests and branch CI); BLOCKED (real cohort evidence)
- **COMMIT SHA:** private head `6359eca0711480218aeb7ff08a4fbe082021fb54`
- **MODEL / DATA VERSION:** `verified-history-v1`; synthetic fixture only;
  existing NFL models unchanged
- **NEXT ACTION:** Review PR; collect independently authenticated cohort evidence
- **USER INTERVENTION REQUIRED:** No new GitHub grant needed; merge/review and
  real evidence ownership remain outstanding
