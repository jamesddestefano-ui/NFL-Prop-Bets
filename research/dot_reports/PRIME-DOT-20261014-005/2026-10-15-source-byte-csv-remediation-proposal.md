# PRIME task005: source-byte-verified CSV remediation proposal

Research time: 2026-10-15 12:18–12:25 UTC (08:18–08:25 EDT). Scope: NFL player props, research only. Production repairs remain unapproved. This is a completed audit/proposal, not a completed repair or validated historical performance analysis.

## Finding and evidence classification

**EMPIRICAL EVIDENCE — verified bounded source audit:** all three retrieved CSV payloads match their Git blob IDs byte-for-byte after UTF-8 materialization. They contain 14 width-invalid records: six of 26 decision records (60-column header), all five bet records (26-column header), and three of 17 pass records (25-column header). The totals independently reproduce task004's text-only audit, now with verified source bytes. This does not upgrade task004 retroactively or establish factual correctness of any recorded ticket, projection, settlement or price.

**MODEL ASSUMPTION / REVIEW-ONLY INFERENCE:** five structural patterns explain these 14 records with candidate delimiter/blank corrections. All candidates remain subject to human review. No missing numeric value was invented, no nonempty fact was deleted, and no recommendation was converted into a ticket. Synthetic parser tests and width checks do not prove the intended column semantics.

## Exact source identity

Pinned main commit re-read after initial fetch: `46526c2f2758be375609eff8c15fd60e7caeaa50`. Each pinned payload was compared with the initial current-main payload and found identical. Retrieval: 2026-10-15 approximately 12:18–12:19 UTC. Medium: GitHub connector file contents and commit/tree API responses; no video reviewed for this audit.

- [Decision ledger](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/46526c2f2758be375609eff8c15fd60e7caeaa50/data/decision_ledger.csv): 29,728 bytes; Git blob `82f1a4297ee7e7c64dc1f2d37f78ec19729ef416`.
- [Bet ledger](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/46526c2f2758be375609eff8c15fd60e7caeaa50/data/bet_history.csv): 3,807 bytes; Git blob `9035f654eff5fb3a0be188542593c62c3ba00b05`.
- [Pass ledger](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/46526c2f2758be375609eff8c15fd60e7caeaa50/data/pass_ledger.csv): 12,448 bytes; Git blob `e1644b9ee70ba6b39aa1579eae1e03b22151265c`.

Verification formula: SHA-1 of ASCII `blob `, decimal byte length, a NUL byte, then exact file bytes. An initial local patch helper added one newline. That materialization failed hash comparison; removing only that helper-added byte reproduced every expected Git hash. Neither failed materialization nor normalization was accepted on trust. SHA-256 fingerprints are also recorded in `results/audit-results.json`. No source was edited remotely.

Read AGENTS, all six controlling config modules and the [task004 report](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/46526c2f2758be375609eff8c15fd60e7caeaa50/research/dot_reports/PRIME-DOT-20261013-004/2026-10-14-candidate-universe-manifest.md). Original forecasts and prior audit limitations remain preserved.

## Before/after proposal and explicit manual-review list

Record numbers include the header as record 1. Original token indexes below are zero-based. The immutable locator is the source blob plus record number; the JSON sidecar additionally contains a SHA-256 of the original record token sequence and a hashed original identifier. Public outputs omit ticket identifiers, amounts and narrative ticket facts. The sidecar gives the full before/after token-index mapping for every affected record. Local private candidate files and unified byte diffs were generated solely for review, with all unaffected physical records byte-identical; they are intentionally excluded from this public package.

| Source / record | Original → proposed width | Candidate structural operation | Unresolved review requirement |
|---|---:|---|---|
| decision / 6 | 61 → 60 | Join original tokens 58 and 59 with their original comma; quote merged result_notes | Confirm the sentence continuation belongs entirely to result_notes and reviewed_at remains empty. |
| decision / 7 | 61 → 60 | Remove empty token 24, shifting subsequent tokens left | Verify intended mean/median and probability mappings against the original recommendation. Numeric plausibility alone is insufficient. |
| decision / 12 | 61 → 60 | Remove empty token 29 | Verify implied-probability alignment. Separately, existing line_at_user_bet is populated despite NO_BET_RECORDED; preserve it but quarantine its meaning pending source review. |
| decision / 13 | 61 → 60 | Remove empty token 24 | Verify mean-versus-median and existing bet_odds meaning in this PASS record; do not assume a placed wager. |
| decision / 26 | 59 → 60 | Insert empty unknown token before original token 25 | Archive supports fair-event probability and pricing sequence, but YES/NO touchdown semantics under Over/Under column names still require explicit approval. |
| decision / 27 | 59 → 60 | Insert empty unknown token before original token 25 | Same semantic issue as record 26; no event probability is recalculated or replaced. |
| bets / 2 | 27 → 26 | Remove empty token 24 | Verify process_review versus notes assignment against original ticket/result review; original ticket not re-accessed. |
| bets / 3 | 27 → 26 | Remove empty token 24 | Same requirement, independently for this record. |
| bets / 4 | 27 → 26 | Remove empty token 24 | Same requirement, independently for this record. |
| bets / 5 | 27 → 26 | Remove empty token 24 | Same requirement, independently for this record. |
| bets / 6 | 27 → 26 | Remove empty token 24 | Same requirement, independently for this record. |
| passes / 15 | 26 → 25 | Remove empty token 23 | Confirm narrative belongs to notes, leaving reviewed_at empty. |
| passes / 16 | 26 → 25 | Remove empty token 23 | Same requirement, independently for this record. |
| passes / 17 | 26 → 25 | Remove empty token 23 | Same requirement, independently for this record. |

These are candidate proposals, not 14 automatically safe fixes. Adjacent empty tokens can be observationally indistinguishable. Header-width matching cannot identify the intended missing field. The zero-based insertion/deletion positions are explicit operational hypotheses; review must resolve the resulting column assignment, not merely approve a delimiter count.

## Archive comparison and limits

The three supporting archive JSON files were also re-hashed during independent review. Their local materializations initially carried the same helper-added terminal newline; after removing only that added byte, each matched its connector-reported Git blob ID below. Archive content comparisons are of recorded claims, not independent verification of historical prices or user actions.

The original [September 22 21:48 EDT archive](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/46526c2f2758be375609eff8c15fd60e7caeaa50/intelligence/archive/2026-09-23T01-48-51Z-prime-watch.json) and [September 23 02:37 EDT archive](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/46526c2f2758be375609eff8c15fd60e7caeaa50/intelligence/archive/2026-09-23T06-37-26Z-prime-watch.json) explicitly identify fair-event probability, implied probability, fair odds, edge and BET recommendation status for the two short decision rows. They also state no authoritative user placement was supplied. This corroborates the proposed numeric sequence; it does not resolve whether a touchdown YES probability should live in an Over-named field. Archive blob IDs: `327c5509fe7b8bab94717be49a764f7148321d93`, `7219f4d107ef01530d82cf5278d141d9175d17a6`.

The [October 4 19:28 EDT archive](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/46526c2f2758be375609eff8c15fd60e7caeaa50/intelligence/archive/2026-10-04T23-28-07Z-prime-watch.json), blob `a38a1ac8dc340667035ee9af1752fbf945e8aeb3`, explicitly records all three affected passes and no inferred user bet. It supports decision identity/status, not exact intended CSV placement of every blank.

Other candidate alignments are inferred from current field sequences and their stored narrative, with no independent original screenshot review. The original user-confirmed ticket evidence and fuller archive history must be checked before approval. No newly authenticated account data or paid-source material was accessed. This bounded audit does not certify all width-valid rows: semantic anomalies can survive correct width, and existing monetary fields are preserved without interpreting units.

## Reversible implementation proposal, only after separate approval

1. Freeze source commit and exact three blob hashes; preserve immutable originals and existing append-only provenance. If current main differs, re-read and rebase the proposal; never fuzzy-apply by line number alone.
2. Resolve each manual-review entry using the original recommendation, ticket and grading evidence. Approve per-record token-to-column maps. Unknowns remain blank; never infer fills, stakes, units, settlement or historical quotes.
3. Prepare a separate review branch/patch with only approved rows changed. Preserve nonempty token sequence, raw ticket facts, all IDs and record ordering. The note-comma merge must preserve both substrings and their delimiter exactly.
4. Check width, unique IDs, expected enums, numeric ranges and units, probability basis, and chronological status semantics. Test the production reader separately: correctly quoted CSV may still be misread by naive comma splitting. Reject missing/extra fields before dictionary conversion; never silently discard overflow.
5. Run the read-only fixtures against the exact source and candidate; confirm unchanged rows byte-identical, approved changes only, reversible original archive, and no new facts. Obtain explicit approval of the exact diff before merging to main; then verify remote readback and compare expected blob hashes. No such approval or merge occurred here.
6. If rollback becomes necessary, use a new reviewable revert of this specific repair, retaining intervening writes. Never reset main or overwrite later records. A later production repair needs its own authorization.

## Reproducible tests and analytical significance

`verify_csv_proposal.py` runs 12 synthetic unittest cases: quoted commas, embedded newlines, escaped quotes, malformed quotes, refusal to delete nonempty values, preservation of unknown blanks, newline-sensitive hash identity, ambiguity in blank positions, insertion ambiguity, width detection, reversible operations and CSV writer round-trip. With `--source-dir` it additionally verifies all three exact source hashes/counts, all 14 candidate widths, ID uniqueness, nonempty-token preservation except the explicitly lossless note merge, reverse reconstruction and status anchors. `candidate-byte-provenance.json` records local candidate hashes and unaffected-record byte checks. These are engineering checks, not NFL profitability or calibration results.

Technical source review, retrieved 2026-10-15 12:21 UTC, article/documentation medium: [Python csv documentation](https://docs.python.org/3/library/csv.html), Python Software Foundation, publication date not displayed; [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180), Y. Shafranovich, October 2005. CSV readers can return extra or missing fields without rejecting schema width; quotation and embedded newlines require a real parser. A header-width check must therefore be explicit. The RFC documents conventional escaping and record structure, but does not determine this repository's financial semantics.

**VERIFIED MATHEMATICAL PRINCIPLE:** an observed outcome and forecast must refer to the same event before computing a Brier score; an unverified shifted column can create a meaningless score even when arithmetic succeeds. **UNTESTED HYPOTHESIS:** schema validation plus review of original evidence will reduce ingestion errors in future records. Test with precommitted malformed/semantic fixtures and rejected-row logs, not retrospective win rate. Restoring CSV shape alone cannot reconstruct unobserved prices, determine actual fills or remove historical selection bias. ROI, CLV and calibration remain unavailable until their independent evidence gates are met.

Confidence: high in byte identities, counts and reproducible transformations; moderate in proposed semantic mappings; insufficient to approve any production repair or historical performance claim. PRIME retains evaluation authority.
