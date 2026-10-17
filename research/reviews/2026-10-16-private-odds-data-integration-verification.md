# PRIME private raw-odds handoff — verified 2026-10-16

Scope: NFL player props only. This is a metadata-only coordination note, **not** a replicated sportsbook quote dataset.

## Verified access and actual architecture

- Public decision/research repository: `jamesddestefano-ui/NFL-Prop-Bets` (main).
- **Private** raw-evidence repository: `jamesddestefano-ui/-NFL-Prop-Odds-Data` (main). Authenticated GitHub connector showed private visibility and write access.
- Private repo already has `scripts/odds_api_collect_v2.py`, `.github/workflows/odds-api-collector-v2.yml`, `AGENTS.md`, run files under `data/odds_api/runs/`, and audits. Do **not** replace this infrastructure with the older public collector.
- Private v2 workflow at inspection has existing cron expressions, contents-write permission and private-run commits. This research did **not** change those schedules, workflow, API credentials, raw observations or user betting history.
- Public v1 diagnostic workflow was previously modified to prevent raw data publication. It is not the private production writer.

## Evidence available from private audit (not independently rerun)
- Private `audits/20261016T212437180951Z-quality.json` reports 12 events; 2,277 player-prop sides; 1,079 matched two-sided pairs, 119 unpaired contract groups, 90.07% pair coverage, 0 flagged post-kickoff quotes, 0 invalid timestamps. Status REVIEW_REQUIRED, not vetted NFL EV.
- Private `audits/20261016T212437180951Z-consensus-validation.json` reports 135 consensus player-markets (187 no consensus), 842 evaluated sides, 16 illustrative positive deviations. It explicitly disclaims NJ executability, and leave-one-out consensus is not proven fair probability.
- The 2,277-side sample already exceeds a *count* of 300 raw side observations but does NOT automatically satisfy v2's threshold of **300 prospectively screened, exact-contract candidate records** for deferring advanced optimization.

## Cross-repository contract
- Keep raw API JSON and source hashes private subject to vendor license review.
- Publish only license-permitted aggregates, methodological code, provenance pointers, missingness and independently reproducible research to public main.
- For Sunday Oct 18, user screenshot-sourced contemporaneous NJ quotes control executable candidate truth; private API is supplementary reference data.
- Do not assume separate agents/Claude can read private repository without verified authorization. Preserve immutable run IDs and source receipt timestamps, pair status, source timestamp coverage, and pre-kickoff exclusion.
- Do not issue additional live collection or alter private scheduling for this handoff. Verify exposed API key rotation and Actions-secret presence *without revealing secrets* before ramping collection.

No wagers, API credit spends, new raw-data copies, or model gate changes are asserted in this handoff.
