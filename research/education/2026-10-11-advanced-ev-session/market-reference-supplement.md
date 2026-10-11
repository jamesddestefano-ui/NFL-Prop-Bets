# Optional lesson: a no-vig estimate is still a model

This supplement reinforces the existing sensitivity/PASS rule in Section 5 of PRIME's framework. Its new contribution is a sharper asymmetric-price counterexample, binary method-equivalence checks and a narrower description of the empirical evidence. No controlling file is changed.

## A method-sensitive price can fail before uncertainty is considered

**MODEL ASSUMPTION.** Invent a matched same-book, same-time Over 99.5 receiving yards at +280 and Under at −400. A second fictional book offers the identical Over at +320. Assume compatible settlement, action eligibility, no push and no fees. None of these quotes or their availability was observed.

**VERIFIED MATHEMATICAL PRINCIPLE.** Raw implied probabilities are .26315789 and .80, totaling 1.06315789. The offered +320 price has break-even probability 23.80952381%. Different margin-removal assumptions produce:

| Transformation | Modeled Over probability | Modeled ROI at +320 |
|---|---:|---:|
| Proportional normalization | 24.75247525% | +3.96039604% |
| Additive / binary Shin | 23.15789474% | −2.73684211% |
| Power, exponent 1.12649999174229 | 22.22663835% | −6.64811892% |

These are transformed market estimates, not verified event probabilities. Even the favorable proportional row has only +.94295144 percentage points over break-even and falls below PRIME's ordinary approximate +4-point / +5%-ROI starting gates. Selecting the transformation that creates a positive number would not establish value. The existing rule already calls for downgrading or passing when reasonable methods materially change the decision.

## What the transformations assume

We evaluate these standard transformations and independently derive the comparisons below; they are not empirical performance claims. For valid mutually exclusive and exhaustive outcomes, let q_i=1/d_i, Q=sum(q_i), and m=Q−1>0.

- Proportional: p_i=q_i/Q. It removes the same relative share and preserves probability ratios.
- Additive: p_i=q_i−m/n. It removes the same absolute amount. It can create negative values in a multiway market; for exactly two q_i in [0,1], outputs stay in [0,1].
- Power: p_i=q_i^k, where the outputs sum to one. Positive overround and 0<q_i<1 imply k>1; smaller q_i receive a larger relative reduction. This is an assumed adjustment pattern, not a measurement of the true bias.
- Binary Shin equals additive. Agreement between those two is algebraic equivalence, not independent corroboration. The model's inferred insider parameter is not an observed count of informed bettors.

For a binary pair, direct substitution gives `p_proportional − p_additive = m × (.5 − p_proportional)`. Agreement on symmetric −110/−110 quotes is therefore unsurprising; it does not show that an NFL event is truly 50/50.

Over 49.5 and Over 99.5 are overlapping events, not mutually exclusive selections to normalize together. Pair each half-point Over with its complementary Under at the same venue and time; then check that Over probabilities do not increase with the threshold. Integer-line pushes require a separately modeled push mass or an explicitly conditional probability basis. Missing margins or quotes remain missing.

## Source cards and evidence limits

### Circles Off episode 169: Wall Street to Bookmaking

- [Original video](https://www.youtube.com/watch?v=C0mTsB3t3GY), Rob Pizzola/Johnny with Henry Kerins, introduced as Novig's head of trading; [publisher transcript](https://www.betstamp.com/education/circles-off-episode-169-wall-street-to-bookmaking).
- Direct YouTube metadata check: upload August 29, 2024, runtime 1:14:05; publisher date August 30. Recording date unknown. A misleading iframe accessibility title was resolved by the matching original watch page.
- **Access:** focused transcript sections 22:14–43:50, plus opening/disclosures/ending context; full transcript accessible, no end-to-end review or playback claim. Readable YouTube captions were not obtained. Locators are publisher markers.
- Relevant anchors: 26:09 commission/margin; 28:41–30:11 price/quantity; 31:01–31:56 market information; 33:23–38:59 inventory and cross-threshold pricing.
- **ANALYST OPINION:** historical operator testimony, including speculation about competitors, not audited NFL evidence or a de-vig derivation. Pinnacle sponsorship, Betstamp interests, signup links and the guest's Novig affiliation create commercial context. Same source cluster as other Circles Off interviews.

### Clarke, Kovalchik and Ingram (2017): Adjusting Bookmaker's Odds to Allow for Overround

- [Publisher record](https://www.sciencepg.com/article/10.11648/j.ajss.20170506.12), published December 25, 2017; [author-uploaded original full text](https://www.researchgate.net/publication/326510904_Adjusting_Bookmaker%27s_Odds_to_Allow_for_Overround), all sections/tables/appendix reviewed. PDF/image verification failed; page references came from text extraction.
- **EMPIRICAL EVIDENCE, non-NFL and author-reported:** one 14,925-match ATP dataset of averaged bookmaker odds and two racing tote datasets. Power beats proportional on the displayed measures, but does not dominate every alternative. Gallop log loss favors additive/Shin. Greyhound narrative and table counts differ; part of the narrative method ranking conflicts with the table. No NFL, profit test or confidence interval for method differences was established.
- Disclosures: commercial affiliations/implementation discussion and Xtrade racing-data acknowledgement; no explicit funding/conflict declaration located. That is limited disclosure information, not proof of absent conflicts.
- **Review-only evidence wording:** this paper supports a claim about one ATP bookmaker-average dataset and two racing tote datasets, not NFL player props or a general collection of sportsbook datasets. Keep the existing sensitivity/PASS instruction intact.

Targeted source review: October 11, 2026, approximately 21:39–21:48 UTC. No new dedicated de-vig-method video with a verified substantive transcript was located in this pass; formulas rest on original technical material and independent mathematics. This adds one focused video-linked transcript review, separate from the five earlier transcript sources, one of which is an unlinked-to-YouTube podcast transcript.

## Review-only empirical test

**UNTESTED HYPOTHESIS.** Compare fixed book/method combinations by prop type, timing and odds range on the same future eligible rows. Separate near-even lines from asymmetric alternatives. Freeze method choice and weights before evaluation; report proper scores, calibration, selected-subset results, coverage and dependence-aware uncertainty. Track later-price agreement separately from settlement accuracy. Evaluate any hypothetical monetary consequences at verifiably available terms, including delay and costs, rather than retrospective best prices.

No reviewed source identifies the best current NFL venue/method pair. Low hold, price leadership, a fitted exponent or agreement across copied feeds cannot replace held-out evidence. The [standard-library verifier](verify_devig_sensitivity.py) passes 10 checks, with [exact/floating-point outputs](devig_sensitivity_verified.json). They do not validate the NFL hypothesis.
