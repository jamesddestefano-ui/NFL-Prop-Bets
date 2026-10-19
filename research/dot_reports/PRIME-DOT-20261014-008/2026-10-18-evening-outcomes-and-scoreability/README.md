# A final box score does not complete a forecast evaluation

**October 18, 2026, evening EDT. Task PRIME-DOT-20261014-008, bounded followthrough.** Review began 23:54 UTC / 7:54 PM EDT. Source-specific clocks are preserved in the [source register](source-register.md).

## Useful result first

**EMPIRICAL EVIDENCE, completed-game facts only.** Pittsburgh beat Tampa Bay **26–19 in overtime**. The official gamebook lists Pat Freiermuth as the starting tight end: **3 targets, 2 receptions, 11 receiving yards, 0 receiving TDs**. DK Metcalf had **15 targets, 11 receptions, 93 yards, 0 receiving TDs**. The [gamebook](https://static.clubs.nfl.com/image/upload/steelers/n4pv5ptycmudhebdsnee) and [Buccaneers box score](https://www.buccaneers.com/game-day/2026/reg-week6/steelers-at-buccaneers/box-score) agree on the receiving lines; the latter does not display targets.

This closes a specific morning question: Freiermuth did participate. It does not resolve his routes, route participation, TPRR, first-read share or injury effect. Low production alone cannot identify whether the calf injury reduced opportunity, whether coverage or game script mattered, or whether ordinary variance dominated.

**Task008 remains INCONCLUSIVE for the prospective pilot/model comparison.** This is a completed one-game source followthrough, not a full Sunday or weekly grade. SNF, MNF and unreviewed games are not graded. No authoritative results ledger, original forecast, governing rule or prior report is changed.

## 1. Compare only with what was actually preserved

The [immutable morning news ledger](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/f50ef0e09f103fcea622e13c4c43ca1fd87a9c5f/research/dot_reports/PRIME-DOT-20261014-008/2026-10-18-pregame-abstention-and-score-coverage/news-ledger.md) recorded official QUESTIONABLE status, an attributed Rapoport expectation of playing, and unresolved workload. It supplied **no calibrated numerical player forecast or executable price**.

| Preserved pregame information | Subsequent evidence | Permitted conclusion |
|---|---|---|
| Freiermuth questionable; reporter said the team was optimistic he would play | Absent from official inactive list; starting lineup and receiving statistics establish participation | Playing expectation was consistent with the observed participation; no numerical probability score exists |
| Workload unresolved | Three targets and two catches are available; advanced usage was not obtained | Production is observed; an opportunity distribution cannot be reconstructed from it |
| Metcalf had no injury designation in the morning review | Final receiving line is available | An outcome observation; no preserved forecast error, priced edge or CLV can be calculated here |

The [original Rapoport post](https://x.com/RapSheet/status/2111782850705932467), published **2026-10-18T11:34:01Z**, was read again during this review. This is one original attributed report, not a second independent signal. The official inactive list alone would not prove snaps; the gamebook supplies actual participation.

**METHODOLOGY_CHALLENGE / ANALYST OPINION.** Do not manufacture a probability from words such as “optimistic,” count WATCH/PASS as a successful binary forecast, or claim that a later non-TD proves the earlier decision had positive expected value. Without the original numerical probability and compatible target, Brier loss is **unavailable**, not zero. Without matched original and closing contracts, CLV is unavailable. No pregame line, odds, no-vig probability, central/conservative ROI, play-to limit, fill or profit is inferred in this report.

This review follows two named players from the morning note. That is a **follow-up inventory**, not a frozen predictive cohort or a denominator for a model win rate. The separately published [rehearsal intake](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/9563ef206f900dbaaa170cb894ef6f4733000293/research/handoffs/2026-10-18-phase4-submission-intake.md) is explicitly REHEARSAL_ONLY; toy responses are not forecasts of this completed game and must not be joined to its box score.

## 2. Football outcome, settlement label and scoring target are separate

**VERIFIED MATHEMATICAL PRINCIPLE.** Even if a statistic is known, unresolved contract rules can leave the settlement label unresolved. A score requires both a preserved forecast of the specified target and the corresponding realized label. Half-point thresholds remove threshold pushes for integer counts; they do not, by themselves, eliminate inactivity, refund, promotion or correction questions.

**MODEL ASSUMPTION, entirely invented example.** Suppose a contract has mutually exclusive, exhaustive states W=win, L=loss and V=full refund. Two pre-resolution probability vectors are A=(0.50,0.20,0.30) and B=(0.50,0.40,0.10), in W/L/V order. Use categorical Brier loss, summing squared errors across all three classes, with **no division by two**.

| Possible actual state | A loss | B loss | A minus B |
|---|---:|---:|---:|
| L | 0.98 | 0.62 | +0.36 |
| V | 0.78 | 1.22 | −0.44 |

If the evidence establishes only L or V, the possible paired differences are −0.44 and +0.36. Their sharp enclosing interval **[−0.44,+0.36]** crosses zero, so the ranking cannot be resolved. The interval describes uncertainty about this label, not sampling uncertainty; its interior points are not additional observed outcomes. Assigning “unknown” to L selects the winner by an unsupported data decision.

The [worked appendix](appendix.md) derives every state, the conditional-on-action targets 5/7 and 5/9, and the full-refund EV identity. Conditional binary scoring and full three-state scoring answer different questions; neither may replace the other after outcomes. Ten exact-rational tests reproduce the arithmetic and reject unknown labels. These are synthetic consistency checks, with no actual book rule or NFL performance validation.

**Counterargument.** An experiment can legitimately target a football event such as a fixed statistical threshold, independent of a sportsbook payoff. Then a verified football result may resolve its label even when settlement is unknown. That does not establish settled return. Conversely, an expressly settlement-aware forecast needs the applicable contract label. Define the target prospectively and preserve both layers rather than making every statistical forecast depend on an irrelevant bookmaker rule.

## 3. What would make the next comparison answerable?

**ANALYST OPINION, review-only proposal.** Preserve four linked records: (a) the unchanged pregame forecast and target, (b) the dated official football result, (c) exact-contract settlement evidence and any unresolved questions, and (d) the scoring decision and missingness reason. Record a later correction as a new version with its discovery time; retain the original evaluation and explain which labels or scores change. Do not overwrite evidence to make the history look complete.

**UNTESTED HYPOTHESIS.** A separate label-resolution audit may change comparative forecast scores even when numerical forecasts and football statistics are unchanged. A falsifiable test would freeze the forecast cohort and label-review procedure, blind label reviewers to model identity and preferred ranking, enumerate admissible labels for unresolved cases, and report score coverage and paired differences before and after genuine resolution. Report linked-outcome constraints; per-case extremes need not be jointly attainable across related contracts. This test is proposed, not run on NFL data.

The current [public settlement correction](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/9563ef206f900dbaaa170cb894ef6f4733000293/research/handoffs/2026-10-18-settlement-evidence-audit-correction.md) retains FanDuel CONDITIONAL, DraftKings EXCLUDE pending reconciliation, BetRivers INCOMPLETE and BetMGM exact-contract applicability UNVERIFIED. In particular, reported DraftKings Over-side incompatibility is **unverified**, not an established rule finding. This review does not reopen that investigation. The [decision to retain the Monday protocol](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/9563ef206f900dbaaa170cb894ef6f4733000293/research/decisions/2026-10-18-retain-current-monday-protocol.md) remains controlling; no eligibility or activation is inferred.

## Scope, confidence and remaining work

- **High confidence:** stated official tabular results and reproduced conditional arithmetic, within the access limits in the register.
- **Moderate confidence:** methodological usefulness for a future study; it depends on a properly specified target and admissible-label set.
- **Unestablished:** NFL forecasting advantage, causal injury effect, executable edge, settlement of any actual user wager or model superiority.
- Current source conflicts are preserved: Steelers recap prose reverses Metcalf/Bernard yardage; the Buccaneers box-score page title says 2025 despite its 2026 URL. The dated gamebook and agreeing table govern this bounded comparison. No silent source correction was made.
- HIGH task011 remains a pending study-design assignment. Its design is feasible without live data, but the actual four-way comparison needs genuine frozen forecasts and market evidence. This time-specific task008 followthrough does not complete 011; 012 also remains separate.

Morning daily education already ran. This is an additive evening followthrough, not a second claimed full daily cycle or video review. Run `python3 settlement_label_bounds.py` to reproduce [the ten tests and exact results](test_results.txt). See [manifest](manifest.json) for hashes and actual verification scope.
