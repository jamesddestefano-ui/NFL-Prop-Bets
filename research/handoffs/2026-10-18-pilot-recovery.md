# PRIME Central Command — October18 incident recovery

Original pilot: **PILOT_INCOMPLETE**. Zero actual sportsbook receipts during 09:30–10:00 EDT (13:30–14:00 UTC), no official cohort in Git history, zero freeze workflow runs (387169622), zero independent publication-receipt runs (388044703). The original protocol is unchanged; successful safety CI is not freeze evidence.

Corrective PR: https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/pull/5
Incident implementation/evidence commit: `8e03788b82056955870997a94f6b5da4163d5028`.
Published head: `5c671abf60edd21b0edb7fdef57b467731ecda56` (includes the genuine main-branch incomplete-status publication).

Changed files: `.github/workflows/pilot-lifecycle.yml`; private `research/handoffs/2026-10-18-pilot-recovery.md`; private incident `evidence-audit.json`, `collector-github-runs.json`, `freeze-github-runs.json`, `receipt-github-runs.json`. Private source records remain private.

The latest pre-window capture arrived 07:18 EDT; the next arrived 10:10 EDT. All seven October18 collector executions are inventoried privately, ending at run39134764635. No freeze execution exists to diagnose as validation/permission failure. Actual Actions schedules correctly map EDT; missing schedule events and absent in-window coverage are confirmed. GitHub's internal reason for absent events remains UNKNOWN, and API outage is not established. Cutoff lifecycle monitoring also did not execute until manual recovery.

Manual lifecycle run39140164818 published PILOT_INCOMPLETE at commit `d16d456` and deliberately failed only at deadline surfacing. This is expected incident signalling. Corrective code invokes existing offline readiness after collector completion (including failure); it does not call the Odds API or change collection cadence. Existing Commander publication deduplicates unchanged evidence. Best-effort GitHub scheduling still cannot guarantee timely execution.

Supplemental evidence: all542 unique contract IDs reproduce from the 10:10 EDT capture; referenced raw response hashes verify. Original manifest commit `4599d11c14bf39da5b896e91862a8c19ccfc29d6`; capture commit `2d54190aa0c7d309decbe5fbebdd02779e946f49`. Classification remains NONQUALIFYING_RESEARCH_ONLY. No genuine independent supplemental forecasts were received by incident review; no reconstructed submissions will be accepted.

Validation:198 local regression tests passed. Push safety CI39140554912 succeeded; PR safety CI39141325784 was running at this handoff. Final merge/CI evidence will be appended after verification.

Next prospective recommendation: October25 Sunday, subject to actual provider kickoff verification and a separately committed dated protocol. Require explicit ET/UTC capture, publication, forecast and outcome deadlines; genuine independent model submissions and GitHub-server publication receipts; verified source hashes, reviewed identity, quota/dedup safeguards and operator fallback. Do not reuse October18 evidence. Detailed next-pilot monitoring readiness will follow this publication/CI milestone.

MODEL_SUSPECT; bet_eligible=false. No API-frequency expansion, purchases, wagers, credentials, authoritative betting-record edits, backdating or source overwrites.


## Final incident publication and monitoring hardening

Incident PR5 merged at `49a994878ffd4d779e650f4e613d32025ad8287a`. Push CI39140554912, PR CI39141325784 and post-merge safety CI39141586271 passed. Follow-up PR6 https://github.com/jamesddestefano-ui/-NFL-Prop-Odds-Data/pull/6 merged at `c08016565637a65e9808c53d9280e206e3e0a0be`, reviewed code `397334938fb7c18baac0ffa6fa2752773c655883`. 205 full local tests passed, including7 new tests for actual receipt windows, absent/tampered/future evidence, separate cohort authentication, missing/late locks and idempotent warning publication. Independent read-only review found no material defects. PR6 safety CI39142428312 and Phase2 CI39142428320 passed. Main checks and live readiness verification are recorded below when complete.

Additional capture metadata records the Sunday :47 schedule expression and a1392.966873-second delay relative to the most recent nominal tick for the10:10 capture. This supports delayed execution of the nominal09:47 tick. It is a derived delay, not a GitHub server scheduled-at receipt; internal schedule/drop reasons remain unknown. All seven retained October18 runs have zero recorded API errors; the late capture skipped no events and provider credits were above reserve. There is no evidence that exhausted quota, auth failure or duplicate suppression inside the missing window caused the incident. No freeze execution exists to diagnose as a job permission/validation failure. Correct ET/UTC conversion is verified. Cutoff-monitor schedules also did not run until manual recovery. These distinguish confirmed facts from the still-unknown GitHub internal cause.

Monitoring now warns at actual source gaps while the window remains open, after missing it, when cohort publication is unauthenticated, and when model locks are absent/late. Raw hashes and exact-pair eligibility must validate before capture warnings clear. Planned schedule timestamps cannot substitute for receipt evidence; capture diagnostics never establish publication. Unchanged evidence is deduplicated; late deadlines still fail closed. Invocation coverage is collector completion (including failure), genuine publication receipt completion, manual dispatch and existing cutoff schedules. This is all offline: no Odds API requests or collection cadence changes. An absent GitHub execution cannot detect itself; an independently verified observer/operator remains a deployment blocker.

### Next prospective candidate — Monday October19

Washington Commanders at San Francisco49ers is scheduled Monday20:15 EDT / Tuesday00:15 UTC, matching independently preserved provider and ESPN schedule records. ESPN event401873008, source https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates=20261019, retrieved2026-10-18T15:45:59.464718Z, original SHA256 `853718ccf09d9e54a5aa9d19333a4c8669bcf15c6b58969dbd83c261180b0858`. Reconfirm the official NFL kickoff before activation.

Proposed actual capture18:00–19:00 EDT (22:00–23:00 UTC); warn18:30; freeze attempts19:03/07/11; independently recorded cohort strictly before19:15; missing-lock warning19:30; genuine forecast receipt and independent lock strictly before19:45; kickoff20:15. Official final-outcome review target Tuesday10:00 EDT /14:00 UTC, pending independently reviewed actual final statistics. Missing or corrected results remain pending/append-only; the target never authorizes invented outcomes.

CANDIDATE_NOT_ACTIVATED. Private Monday plan and original schedule bytes are under research/pilots/2026-10-19. The existing freeze/submission/publication implementation is October18-specific. A separate Monday protocol and tested date adaptation, canonical identity/settlement review, independently proven observer/operator fallback and genuine independent model access are still required. These are unresolved readiness gates, not verified integrations. Existing budgeted18:17/18:47 collector ticks fall inside the proposed window; no increased frequency is authorized. If gates cannot pass prospectively, abandon Monday and preregister October25 using actual verified kickoffs. Do not reuse October18 cohort IDs, source timestamps or forecast locks.

Original October18 protocol and supplemental records remain unchanged. All models remain MODEL_SUSPECT; bet_eligible=false. No positive-EV claim, wager, purchase, credential exposure or authoritative betting-record changes.
