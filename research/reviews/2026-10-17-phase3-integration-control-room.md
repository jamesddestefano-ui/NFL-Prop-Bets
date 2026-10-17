# PRIME Integration Control Room — Phase 3 engineering deployment

Engineering is deployed. The prospective pilot is NOT complete: deployed readiness at 2026-10-17T23:19:04.434991Z is PRE_PILOT_PENDING_EVIDENCE. No genuine frozen cohort, ChatGPT/Claude submission pair, official final outcomes, verified predictive scores or profitability exists yet.

## Exact integration and review evidence

- PR: https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/pull/3
- Final reviewed implementation head: `47b67bd65eda09d8f378aef616b00b391e571e00`.
- Merge: `d28a35525b040d405a32f7b6e15a7319bedb6c21`, merged 2026-10-17T23:18:39Z.
- Live Commander evidence commit: `2b5bba89acacd94aea3d8c472eb45556723d8a77`.
- Internal independent agent review, not external Claude validation: response-hash, full-universe/baseline source reconciliation, and paid-failed-response quota findings fixed. Final reviewer independently ran 48 relevant tests with no new material defect. GitHub review `5560586065` records the review process; final follow-up review is summarized here.
- Repository protection/ruleset checks found no required formal review or branch rules. All final-head checks passed before an ordinary SHA-bound merge. No checks or protections bypassed. No raw commercial source rows or credentials are republished here.

## Tests, CI and artifacts

Full local command `python -m unittest discover -s tests`: 166 tests passed. `compileall`, workflow YAML parsing and `git diff --check` passed. Two shared Phase 2 exports reproduced byte-for-byte; comparison SHA-256 `981781657f92c7a892502f2811357dead1503541ef0963b43eb404ca14758547` is SYNTHETIC scoring, not NFL predictive performance.

Final-head safety CI 39077928806 and learning validation 39077928838 succeeded. Main safety CI https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/actions/runs/39078525120 succeeded; artifact `12118335938`, `prime-pilot-safety-39078525120`, 112566 bytes, unexpired at verification. CI executes the full suite and deterministic artifact diff.

Deployed readiness-only lifecycle https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/actions/runs/39078539997 succeeded. Artifact `12118201149`, `prime-pilot-lifecycle-39078539997`, 2891 bytes. Remote Git evidence was fetched and read back: `research/pilots/2026-10-18/commander/666998e80ceecaff927c0c67fb4b697357c24ea33da68cb9f48771511d28509e/readiness.json`, SHA-256 `c5715cabb7e9e50f4b1c98fd09dcb3caa5111410043833d03908acc20917d1db`. Artifact existence/metadata and CI diff are verified; artifact ZIP downloads are not separately claimed.

## Sunday readiness and exact boundaries

America/New_York is EDT (UTC-04:00) on October 18. Actual receipt window 09:30–10:00 ET / 13:30–14:00 UTC. Existing collector ticks inside it: 09:37/09:47 ET. Freeze attempts: 10:03/10:07/10:11 ET. Cohort GitHub dispatch creation must be strictly before 10:15 ET; independent forecasts strictly before 11:30 ET. Eligible kickoff 13:00 ET. Wrong date/year and exact-cutoff arrivals reject. Missing evidence after cutoff yields PILOT_INCOMPLETE; it must never be reconstructed later.

Original companions are hash-bound to GitHub's server-created dispatch metadata and immutable source commit, validated against the complete exact frozen universe and canonical identity/input-source evidence. Earliest valid receipt per model is selected prospectively. Missing rows remain explicit abstentions. GitHub possession is independently time-evidenced; external model authorship and identity/source truth still require genuine reviewed evidence. No external model service was invoked or fabricated.

Outcome matching is implemented against preserved official NFL bytes/URLs, actual retrieval time, official/canonical IDs, review attestation and settlement rules. Missing, nonfinal, ambiguous and void records are excluded. Corrections append sources/reviews/evaluations. New committed outcome reviews trigger the shared scorer; schedules provide catch-up and manual dispatch remains available. Scoring preserves original forecast bytes and Git hashes, three-way Brier/log loss, calibration, matched non-push market comparisons, missingness, disagreement and game-cluster uncertainty. The fixed protocol suppresses intervals below 20 games. Exact later pregame closing pairs are used only where genuine observations exist; hypothetical unit returns never become actual profit or bet records.

## Odds API operating directive

Existing subscription and cron frequency are preserved. Monthly slate envelopes, emergency reserve, duplicate/request-window suppression, actual returned quota accounting and failed-response retention are deployed. No manual Odds API requests, purchases, plan changes or frequency increases were made by this engineering work. Previously exposed-key rotation remains UNVERIFIED and blocks expansion. Detailed quota/source evidence remains private. Original observations are append-only; unavailable older source bytes are not reconstructed.

## Deepnote

Existing private PRIME NFL Model Lab, project `3f1b1d1e-9704-4ac5-81ea-016c706f3028`; notebook `e57c04c031ae457ba2b91e84f8caacc2`. Hosted run `1c10667f-1a72-4b99-868f-bf9f8eb51df3` succeeded, zero failed code blocks; actual readiness file was mounted and its SHA verified. Basic machine stopped afterward; no upgrades or purchases. Static sharing/viewer API remain disabled. Reader for future aggregate `deepnote-sanitized.json` uses original GitHub checksums and contains no scoring duplication. Automatic GitHub-to-Deepnote transfer is not configured; actual pilot results cannot be transferred before they exist.

## Blockers and next actions

1. Verify actual capture, frozen cohort and successful independent receipts on Sunday; monitor scheduler delays and strict cutoffs.
2. Obtain genuine independent ChatGPT/Claude responses and reviewed identity, settlement and model-input provenance before 11:30 ET. Unknown training/source metadata must not be invented.
3. Verify exposed-key rotation through authorized owner secret management and GitHub Actions before any collection expansion.
4. After final games, preserve/review official results, append real outcome reviews and inspect shared-scoring artifacts. Transfer only sanitized verified outputs into Deepnote.
5. Accumulate multiple prospective slates before calibration/refit decisions or interval claims; preregister improvements on future holdouts. Consider reviewed unused-slate budget reallocation, explicit missing-run detection and authenticated automated Deepnote transfer as Phase 4 work.

All models remain MODEL_SUSPECT and bet_eligible=false. No wagers, positive-EV claims, additional spending, credentials, raw public data exports or authoritative betting-record changes.
