# PRIME Model Development — historical backtest artifact audit and malformed provenance JSON
Execution: 2026-10-17T21:09:09Z. Addressed to: PRIME Integration Control Room via GitHub.
Scope: NFL player-prop model diagnostics only. Source: private `jamesddestefano-ui/-NFL-Prop-Odds-Data`; research report: public `jamesddestefano-ui/NFL-Prop-Bets`. No private raw sportsbook quotes, odds, credentials, or player-level historical data reproduced.

## New verified findings, not a duplicate of earlier CI status reports
**Research-only historical workflow actually completed.** GitHub Actions run [39052407959](https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/actions/runs/39052407959) at private commit `5e6e84c9fb525f8486554983352a8bcadd5f3ca9` completed SUCCESS. Job 117453473490: historical tests, input ingestion, backtest and artifact upload all succeeded. Artifact ID `12107713980`, `prime-historical-backtest-39052407959`, was retrieved and inspected independently. Workflow produced actual 2024/2025 synthetic-threshold diagnostic predictions, not prospective locks or actual executable bookmaker contracts. A second run [39052300932](https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/actions/runs/39052300932) also succeeded; no claim of independent dataset replication.

**Defect — invalid JSON provenance manifest despite green CI.** Extracting the original ZIP and running strict Python `json.loads` on its `provenance.json` failed: `JSONDecodeError: Extra data: line 14 column 2 (char 380)`. The artifact contains literal backslash-plus-n after a complete JSON object (`...}\n` rather than an actual newline). Current workflow `.github/workflows/historical-backtest-2025.yml`, observed blob `0e4ab0279ea8406f8dd907b4fe9d9be955d2312d`, has `write_text(json.dumps(manifest,indent=2)+"\\n")`; this generates invalid JSON. Its pipeline does not parse-check the manifest before upload. Existing success therefore does not ensure machine-readable provenance. This is a reproducibility/integration defect, not a finding of leaked outcome data.

**Red/green reproduction without modifying preserved evidence.** RED: original artifact's strict JSON parser failed. GREEN: on a local synthetic manifest, writing a real newline and checking `json.loads(path.read_text())==manifest` passed; the bad double-escaped newline failed. For read-only input-hash verification of the existing artifact, a one-off in-memory removal of only the offending trailing literal `\\n` permitted manifest parsing, and SHA-256 recomputation of `2024.json` and `2025.json` exactly matched both recorded source hashes. Original artifact ZIP was never changed. This is a diagnostic recovery, not a silently repaired official artifact.

## Independently recomputed historical metrics
Using the retrieved `2025-backtest.json`, independent per-row `(p_baseline - y)^2 - (p_model/(1-p_push) - y)^2` over nonpush cases reproduced model-minus-baseline improvements to floating tolerance:
- Attempted synthetic contracts: **259,308**; graded **73,829**; excluded **185,479** (**71.5285%**); pushes **0** (half-point synthetic lines).
- Scored: **56,497** receptions and **17,332** receiving-yards thresholds, representing **8,071 distinct player-games** and **886 distinct players**. Each player-game generates multiple correlated thresholds, so the contract count is *not* an independent-trials sample size.
- Model Brier **0.05332872836118**; player-history empirical baseline Brier **0.05857317755482**; baseline-minus-model Brier **+0.00524444919364**. Model log loss **0.16923423337235**.
- Receptions Brier **0.03241214008642** versus baseline **0.03700096792203**; receiving-yards **0.12151038585939** versus baseline **0.12889195943942**.
- Outcome distribution: **8,499 WIN / 65,330 LOSS**, a synthetic-threshold selection distribution. A player-cluster descriptive bootstrap (886 groups; 1,000 resamples, fixed seed 20261017) gave Brier-difference 95% percentile interval roughly **+0.00472 to +0.00576**, but ignores shared real-game/team dependencies and any post-selection effects. Not a formal production edge test.

**Interpretation:** Historical model-versus-training-baseline Brier appears better on this derived diagnostic sample, but future publication-time, market-price, game-ID/kickoff verification and independent realistic contract sampling are absent. Never promote model beyond `MODEL_SUSPECT`; `bet_eligible=false`. The lower scores are strongly influenced by correlated thresholds and low observed WIN prevalence (about 11.51%). Do not infer betting profitability, calibrated NJ prices, or prospective improvement.

## Blocked correction / recommended minimal repair
Attempted an authorized private GitHub workflow update after fetching latest source; the tool returned `blocked by OpenAI's safety checks` before providing any resulting commit. **Do not claim the patch was written or deployed.** The minimal proposed repair is to serialize with an actual newline, not a literal backslash/n suffix, then immediately parse the written manifest and assert equality with the object before artifact upload:
```python
provenance_path = pathlib.Path("/tmp/prime-history/provenance.json")
provenance_path.write_text(json.dumps(manifest, indent=2) + "\n")
assert json.loads(provenance_path.read_text()) == manifest, "PROVENANCE_JSON_ROUNDTRIP_FAILURE"
```
Owner: PRIME Commander / model-maintenance code writer with authorized GitHub access. A new workflow execution must produce a fresh, separately versioned valid artifact. Do NOT retroactively rewrite immutable run 39052407959. This report is a handoff, not workflow deployment.

## Provenance, tests, costs, and next action
Source accessed through authenticated GitHub connector at this execution; logs/job and artifact were fetched from private GitHub, with local Python stdlib `zipfile`, `json`, `hashlib`, and NumPy for independent arithmetic. No external NFL reporting or Hugging Face model data was used. No Odds API/Firecrawl credits, paid compute, wagers, or API purchases were consumed (**0**). Exact public research HEAD before this handoff: `967f304cad42a0e964a609d1b4242db12c27181e`. Source observation time: 2026-10-17T21:09Z.

Next: independently re-run historical workflow after valid manifest serialization; verify strict parse and all source hashes, capture new artifact IDs; then challenge calibration on a truly prospective, kickoff-verified exact-contract cohort and preserve every screened PASS/missing row. MD-EV-HANDOFF-001 unattended authorship remains UNVERIFIED, with no new demonstrated unattended EV Learning artifact since previously reviewed 08 ET note. No Sunday October 18 lock was changed.

## PRIME HANDOFF
- **AGENT:** PRIME Model Development
- **EXECUTION TIME:** 2026-10-17T21:09:09Z
- **TASK:** Inspect real historical workflow artifact; reproduce aggregate model scores; diagnose provenance serialization
- **RESULT:** FAIL (strict JSON provenance); PASS (artifact/hash/Brier recomputation)
- **VERIFIED EVIDENCE:** Actions run 39052407959 and job 117453473490 SUCCESS; artifact 12107713980 retrieved; strict manifest JSON parse FAIL; source hashes 2/2 PASS after in-memory diagnostic suffix isolation; synthetic red/green serializer test PASS; independent 73,829-row Brier recomputation PASS
- **COMMIT SHA:** private source `5e6e84c9fb525f8486554983352a8bcadd5f3ca9`; public source HEAD `967f304cad42a0e964a609d1b4242db12c27181e`; handoff commit obtainable from GitHub history/read-back
- **MODEL / DATA VERSION:** v1 historical synthetic-threshold experiment, 2024/2025 nflverse-derived inputs; `MODEL_SUSPECT`, `bet_eligible=false`
- **BLOCKERS:** malformed immutable historic manifest; private workflow update blocked by connector safety check; no real pregame publication/price provenance or NFL game-ID anchors; EV Learning unattended attribution unverified
- **NEXT ACTION:** Authorized owner patch current workflow JSON writer + parse assertion, rerun and inspect new artifact; continue prospective lock discipline
- **USER INTERVENTION REQUIRED:** NO (Commander can coordinate a permitted repair; escalate if access remains blocked)
