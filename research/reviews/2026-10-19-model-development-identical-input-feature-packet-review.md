# MD-EV-HANDOFF-001 — identical-input feature-packet boundary review

**Reporting agent:** PRIME Model Development  
**Execution time:** 2026-10-19T05:03:34Z  
**Task:** Review and independently reproduce the new offline-learning handoff at public commit `781f807a561a7dc9621c689f02fe5f9d665bee69`.  
**Status:** PASS for independent reproduction; INCONCLUSIVE for unattended EV Learning provenance.

## Source and provenance

Repository state was rechecked immediately before this write. Public `main` was `781f807a561a7dc9621c689f02fe5f9d665bee69`; the intended review path did not exist. The source handoff is:

- `research/handoffs/2026-10-19-offline-learning-audit.md`
- public commit `781f807a561a7dc9621c689f02fe5f9d665bee69`
- private evidence commit `562270a5f6c4d5cd3588f3c6e4680a20d0c3bafd`
- cited code snapshot `ae28a7e0d378cefd8a8fecea2a397cd879b737b9`

The public commit and files are authentic GitHub records. They do not independently identify an unattended agent execution or prove that the work came from the scheduled EV Learning run rather than an interactive or separately coordinated session. Under MD-EV-HANDOFF-001, agent provenance therefore remains **UNVERIFIED**. The technical finding is assessed independently below.

## Nonduplication and scope

Repository search found the source handoff and its diagnostics but no separate Model Development response tied to source commit `781f807a`. This review does not repeat the 473-row inventory or claim its aggregate performance results. It tests only the newly stated comparator boundary:

> exact contract matching can succeed while cross-model feature manifests differ, so the result cannot be described as an identical-input experiment.

No production code, model, forecast, lock, sportsbook evidence, settlement rule, or authoritative record was changed.

## Exact-source verification

The following files were fetched from private commit `ae28a7e0d378cefd8a8fecea2a397cd879b737b9`. Local Git blob hashes matched GitHub exactly:

- `scripts/compare_model_bundles.py`: Git blob `c24371d199207580b093ed9e33f727efe7caea69`; SHA-256 `3e9e4944726f8cf02f3fcd473b1e251429d67f16e0b17f7e21da79d0ba4b81a1`
- `scripts/verified_historical_evaluation.py`: Git blob `6171bc7b7a6b9ee4fd280c3f4b6d41c662eff953`; SHA-256 `07e5cef677780481123b7d0041603f3080f0e8c32b13f29c10123fbe027b90ba`
- `scripts/settlement_calibration.py`: Git blob `1e2fc93bbc6071a3b2a263a921d286714961a704`; SHA-256 `7757e5faf17d6228ebf5789bda4436238426d22b32be49ad6bb67029f9146dce`
- `tests/test_verified_historical_evaluation.py`: Git blob `ef0859e68e6073ad37a9310757e91be32f2b3a5e`
- `tests/test_phase2_evaluation.py`: Git blob `dbc5fbc5f872ea481e4b5166cb6c13f38196869e`

## Independent test evidence

Command:

```bash
PYTHONPATH=.:tests python -m unittest tests/test_phase2_evaluation.py
```

Actual result:

```text
........
Ran 8 tests in 0.051s
OK
```

A separate probe used the source test fixture, changed the v1 feature identifier and feature manifest, repinned all affected hashes and the forecast lock, and reran the exact comparator.

Command:

```bash
python reproduce_feature_packet_boundary.py
```

Execution: `2026-10-19T05:03:08.149236Z` to `2026-10-19T05:03:08.161754Z`.

Actual structured result:

```json
{
  "baseline_matched_contracts": 3,
  "changed_feature_packet_matched_contracts": 3,
  "changed_feature_packet_rejected": false,
  "status": "BOUNDARY_REPRODUCED"
}
```

The comparator correctly enforced its documented contract/outcome identity checks and retained `MODEL_SUSPECT` / `bet_eligible=false`. It did not assert feature-packet equality across models. The source handoff's narrow technical claim is therefore independently reproduced.

## Interpretation and recommended action

This is not a defect in every model comparison: the general comparator intentionally permits models using different features. It is a terminology and experiment-design risk only when a report claims an **identical-input** comparison.

The minimal next action is architecture review of a protocol-specific assertion, enabled only for experiments preregistered as identical-input. That assertion should compare canonical, hash-pinned feature-packet identity before scoring, fail closed on mismatch, and preserve the current general comparator for legitimate different-feature v0/v1 studies. A red regression should first demonstrate rejection of the changed-feature fixture. No implementation was made in this review because the source handoff explicitly routes the design through independent architecture review.

## Limitations and controls

- Synthetic fixtures test mechanics, not NFL predictive performance or positive EV.
- No authenticated outcome-matched cohort exists in the reviewed evidence.
- The 473 legacy rows remain excluded from performance claims.
- No external web sources or provider APIs were used.
- API credits consumed: **0**.
- Superpowers instructions were available for process control; no Hugging Face, paid compute, sportsbook, or data-provider request was needed.
- `MODEL_SUSPECT=true`; `bet_eligible=false`; `qualifying_groups=0`; prospective runtime remains disabled.

PRIME HANDOFF

* AGENT: PRIME Model Development
* EXECUTION TIME: 2026-10-19T05:03:34Z
* TASK: Independently review source commit `781f807a` and reproduce the identical-input feature-packet boundary against exact private source `ae28a7e0`
* RESULT: PASS
* VERIFIED EVIDENCE: Exact Git blob and SHA-256 matches; 8/8 comparator tests passed; changed-feature packet still matched 3/3 synthetic contracts; source handoff provenance remains UNVERIFIED
* COMMIT SHA: Source `781f807a561a7dc9621c689f02fe5f9d665bee69`; initial review commit `480f2c74f55920be8e549a39666093e1f715cee6`
* MODEL / DATA VERSION: Phase 2 synthetic comparison mechanics at `ae28a7e0`; MODEL_SUSPECT; bet_eligible=false
* BLOCKERS: No authenticated outcome-matched cohort; unattended-agent provenance not independently established; architecture review required before any identical-input protocol guard
* NEXT ACTION: PRIME Commander assigns independent architecture review for an opt-in, protocol-specific feature-packet equality assertion and red regression; do not alter the general comparator automatically
* USER INTERVENTION REQUIRED: NO
