# Settlement evidence correction handoff — NO-GO unchanged

Append-only. This adds to, and does not edit, `2026-10-18-phase5-settlement-compatibility-resolution.md` (commit 2c406d3) and `2026-10-18-settlement-evidence-audit-correction.md` (commit 430463a). Earlier wording stays in history; where this file differs from them, this file controls. Machine-readable record: `2026-10-18-evidence-correction-verification.json`. No selector, protocol, runtime or code change. Phase 5 is not restarted.

## What was and was not available

- The Protocol Evaluation Audit text, its FanDuel capture (reported 590,076 bytes, 7:08:03 PM EDT) and its DraftKings Terms hash were **not available** in this session. Checks covered every branch and issue in this repository, plus the account's repository list. No private evidence repository is reachable, and private commit `bad2a46` is not in this clone. Those audit identifiers remain **UNVERIFIED claims**. No missing timestamp or hash is reconstructed.

## Verified evidence

| Artifact | Bytes | SHA-256 | Actual time | Result |
|---|---|---|---|---|
| FanDuel NJ policy, https://policies.fanduel.com/SB/NJ/2026-10-15T12-42-58.html (recorded original) | 683,885 | `025c74df6a37f9a46d6d0c4929667f03ae34e052704f12badd50985c18e42f72` | original receipt 2026-10-18T21:15:15.531343Z (existing retrieval.json) | Independent re-fetch at 23:29:50.607974Z returned **identical bytes and hash**. Original preserved unchanged. |
| DraftKings NJ Terms of Use, https://sportsbook.draftkings.com/legal/nj-terms-of-use (new capture, not the audit's) | 495,683 | `cd03210b9695210720a85d0a9bdc2fe7003851f880d0e4dc43fa63b39e00fa4c` | 2026-10-18T23:30:16.299769Z | Genuine NJ Terms (Crown NJ Gaming Inc.; NJ DGE). No NFL prop settlement or Early Exit eligibility rules. This hash is specific to this capture of a dynamic page, so it neither confirms nor refutes the audit's hash. |
| DraftKings Early Exit article KB0012329 (support.draftkings.com) | 469,339 | `644218af768fbb6d9ae5d41459fd0d57b5e70be6f09d616967d28b290879db1c` | 2026-10-18T23:30:32.034173Z | Shell page only. **Article body not captured.** |

The table cites FanDuel sections only where they were located in the verified bytes:
- **Part B › General Rules › Results and Market Settlement**: markets settle on the official result "at the time of settlement, regardless of any subsequent disqualification or amendment". The same section also says FanDuel "may amend or reverse the settlement of a market where the official result differs from the result used for initial settlement". The paragraph contains merged, redline-like duplicate text. **The correction-rule conflict remains UNRESOLVED.**
- **Part C › American Football › Proposition bets**: player props are void "only when a player does not play a snap". In an abandoned game, an Over that is already won is settled as the winner.
- **Promotions**: Odds Boosts settle under standard rules "unless otherwise specified". Part F (Master Offer and Promotions Terms) exists. **Whether it applies to the protocol's contracts remains UNRESOLVED.**

## Corrected findings, reconciled to the compatibility matrix

| Book | Prior matrix | Corrected status | Basis |
|---|---|---|---|
| FanDuel NJ | EXCLUDE (2c406d3) / CONDITIONAL, not admitted (430463a) | **CONDITIONAL, not admitted** | Rules are verified. The correction conflict and promotional applicability are open. |
| DraftKings NJ | EXCLUDE | **EXCLUDE, Early Exit basis UNVERIFIED** | The reported incompatibility is on the **Over** side: an eligible injured-player Over may have its stake returned while the Under is graded normally. 2c406d3's "Over-void/Under-exclusion" wording is kept only as an attributed claim. The primary article is uncaptured, so the specific terms and their NJ applicability are not verified. The archived Virginia terms are still not NJ terms. |
| BetRivers NJ | EXCLUDE / INCOMPLETE | **INCOMPLETE; settlement assertions UNVERIFIED** | No scoped NFL settlement rules have been captured. |
| BetMGM NJ | EXCLUDE | **Settlement assertions UNVERIFIED** | Existing NJ captures (football page `6b37e69e…2483`) were not re-reviewed here. 2c406d3's "Over can void while Under wins" claim and its unknown protection eligibility are not adopted as verified conclusions. |

No three compatible books exist, so **qualifying_groups=0**. The three-book protocol and the deterministic selector are unchanged.

## Limitations and required next evidence

- Raw bodies are not committed here, following the public-repository convention. The FanDuel body can be reproduced from its versioned URL and hash.
- To resolve the open items, Central Command must supply the audit's original FanDuel and DraftKings files with their acquisition records, and the rendered text of the DraftKings Early Exit article (KB0012329).

**Status:** MODEL_SUSPECT=true · bet_eligible=false · pilot_activation=disabled · qualifying_groups=0. No wagers, purchases or approvals requested.
