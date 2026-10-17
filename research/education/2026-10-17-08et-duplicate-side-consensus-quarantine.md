# PRIME 08 ET learning — duplicate-sided book can manufacture a player-prop consensus edge
Date: 2026-10-17 (Saturday), morning America/New_York. Classification: **VERIFIED CODE DEFECT / SYNTHETIC DEMONSTRATION / NO VALIDATED BETTING EDGE**.

## Provenance and external instruction
- Official provider specification: https://the-odds-api.com/liveapi/guides/v4/ (retrieved Oct 17, 2026). Its *market-level* `last_update` is the last time the provider **saw** that market's odds at the bookmaker, not necessarily the time a specific price changed; bookmaker-level `last_update` is deprecated. Suspended/closed markets stop advancing and disappear from the feed after roughly 15 minutes. It is not NJ account-level executability verification.
- Additional technical-market context: Unabated's methodology discusses vig-free book consensus and the need to compare prices, https://www.unabated.com/post/what-is-the-unabated-line (retrieved Oct 17, 2026). This commercial explanation is a conceptual reference, not independently verified profitability evidence. No accessible recent X post added a verifiable novel claim.
- Source inspected on GitHub main, Oct 17: private `scripts/validate_consensus.py`, blob `07dec02487ce973b262b7ae3840ae1a01ff2749d`, and `scripts/quote_persistence.py`, blob `6de765474c5ef63698b32011f9e8599878bccd88` (both under `jamesddestefano-ui/-NFL-Prop-Odds-Data`). `scripts/matched_book_closing.py`, blob `a4461aebdf1ba041021f096aa0805d9a62897d54`, **already excludes** books with duplicate sides and demonstrates the appropriate quarantine pattern.

## Verified defect (source inspection)
Both `validate_consensus.py` and `quote_persistence.load` accumulate sides with a `defaultdict(dict)`; if `side in pairs[key]`, they silently discard the extra quote and retain the first price, then **accept the remaining Over/Under pair as valid**. Thus a book with two conflicting prices for the same side is eligible for the three-book same-threshold leave-one-out (LOO) consensus. The script may report an apparent research edge or later quote-survival rate even though its first retained quote was ambiguous. The general quality audit's stricter duplicate quarantine does not automatically protect these separate consumers.

## Reproducible synthetic counterexample (not real odds)
One event/player/receptions threshold 4.5, all observations pre-kickoff, same market:
- Book A: Over +150, **duplicate Over -110**, Under -110.
- Books B and C: Over -110, Under -110 each.
- Existing `validate_consensus.py` keeps A's first +150 Over and counts A/B/C as three paired books. B and C's two-sided normalized fair Over is 0.50, so A's LOO model is p=0.50.
- At +150, decimal odds=2.50, break-even p=0.40, **apparent edge=+10 percentage points** and binary central EV=0.50×2.50−1=**+25%**. This is an artifact of accepting a contaminated pair, NOT an actionable bet. No conservative p, live book quote, or account acceptance is established.
- Correct policy: quarantine **all sides** of A's exact pair group if *either* side repeats; only B/C remain. Under the present three-independent-book consensus minimum, no valid LOO candidate survives. In `quote_persistence.py`, the same quarantine must apply at **each** snapshot so an ambiguous price cannot falsely count as a persistent opportunity.

## Proposed smallest safe correction
In each consumer, initialize `duplicate_groups=set()`. On detecting a repeated (event, market, player, threshold, book, side), add that exact *pair* key to `duplicate_groups` and keep the duplicate count. At the pair-to-group conversion stage, `continue` for all keys in `duplicate_groups`, incrementing `duplicate_group_quarantined` diagnostics. Do not choose the first/last/highest price, collapse thresholds, repair aliases on guesswork, or rewrite existing audit artifacts. Maintain immutable output reports; if old and corrected aggregates differ, issue separately versioned corrected research outputs after testing, not a silent overwrite.

### Regression contract
1. Duplicate Over at A plus clean B/C => `consensus == 0` and no positive LOO offers, even though A's initial +150 looked favorable.
2. Identical fixture without the duplicate => `consensus == 1`, and A's Over may be flagged as a **research-only** +10pp apparent LOO deviation. This clean control demonstrates that quarantine is targeted.
3. Repeat the duplicate fixture through `quote_persistence.load/flags` and verify no candidate survives; check both snapshots individually.
4. Preserve pre-kickoff `response_received_utc < commence_time` and exact player/threshold/book/side matching. Treat source-age separately from economic price changes.

## PRIME challenge / falsification
A provider may return repeated identical rows due to duplication upstream; dropping the full pair conservatively reduces sample coverage. That is preferable to treating an ambiguous first/last side as two independently defensible quotes, but quantify real duplicate-group incidence and reason codes before changing minimum book-count policy. If a documented vendor-specific canonicalization rule later proves identical economics, evaluate it prospectively with a versioned protocol. Also test source-age buckets against subsequent *price-content changes*; market `last_update` movement alone does not certify a price move or true staleness.

**Status / control:** Research finding source-verified, synthetic EV arithmetic exact, actual book exploit unverified. Do not promote any LOO result into BET, change model safety gates, wager, spend API credits, change immutable captures, or edit authoritative ledgers. Corrected production behavior and CI results require independent validation. 8 AM education only; does not replace the separate 2 PM testing or 8 PM critical-review cycles.
