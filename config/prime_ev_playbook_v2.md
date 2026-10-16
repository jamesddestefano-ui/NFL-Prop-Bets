# PRIME NFL Player Prop EV Playbook v2.0 — adopted operating overlay
Adopted from user-supplied six-page "PRIME NFL Player Prop EV Playbook v2.0" dated October 16, 2026. Scope: NFL player props only. This is a user-directed operational update; research hypotheses remain unvalidated until prospective testing. Read alongside AGENTS.md, config/positive_ev_framework.md, config/advanced_market_learning.md and config/methodology.md. Where the prior policy has a redundant 5% ROI gate, this v2 overlay supersedes it. Never weaken quote-verification, injury/settlement, provenance, or historical-integrity controls.

## Exact-contract mathematical requirements
- Decimal odds d: -A => 1+100/A; +A => 1+A/100. Break-even probability = 1/d.
- Binary no-push net EV per unit stake = p_win*d-1. Probability edge = p_win-1/d. EV = edge*d.
- Push-refunded contract: EV = p_win*d+p_push-1 (equivalently p_win*(d-1)-p_loss). Do not use a binary shortcut with unconditional p_win when pushes or voids apply. Determine exact book/jurisdiction contract settlement.
- Two-sided overround = q_over+q_under-1; theoretical hold under proportionate balanced action = 1-1/(q_over+q_under). Do not equate these quantities.
- Parlay EV = joint probability*combined decimal odds-1. Do not multiply marginal probabilities without a defensible independence assumption. Same-game and shared-thesis correlations need joint modeling or PASS.
- Full Kelly for binary/no-push = (p*d-1)/(d-1), with no staking when conservative EV is negative. Push/void and promotional contracts require settlement-specific sizing.
- Bonus bets with stake not returned: expected cash payout p*(d-1)*bonus face amount before terms/opportunity costs; this is NOT net cash profit on an equivalent ordinary stake. Profit boosts require recalculation of boosted price, limits and eligibility.

## Probability from a projection
Never convert a point mean directly into an Over probability without stating and defending a distribution (e.g. illustrative Poisson for receptions; actual reception counts may be under/overdispersed). Calculate P(win), P(push), P(loss), plus void/refund if relevant, at the EXACT line and contract. State model family, parameters, calibration status, and source. Different thresholds require different probabilities. Preserve coherence of elementary event probabilities; advanced coherence optimization can await data.

## Source priority for practical edge discovery
1. Verified promos, profit boosts, and bonus-bet terms (value still depends on defensible fair probability and actual constraints).
2. Time-aligned same-contract line shopping among available NJ books.
3. Verifiably stale, still-active lines following independently confirmed news.
4. Sharper/reference book comparisons after proper same-contract de-vigging and freshness checks.
5. Independent football distribution model, initially unvalidated; shrink uncertainty appropriately.
A claimed sharp book or profitable X account is not automatically reliable. Do not invent an executable quote, fill, promotional entitlement or account access.

## V2 betting decision gates (provisional research policy)
- For standard prices from -150 through +150 inclusive: CENTRAL probability edge at least 4 percentage points above exact-price break-even AND conservative EV >= 0. Do not separately require 5% central ROI (redundant across this price range). Still require market-truth A/B, role/settlement validation, no unresolved material news, and appropriate correlation/price safeguards.
- For longer odds beyond that range and high-variance touchdown props: central expected ROI >= 15% AND conservative EV >= 0, with independent evidence and stronger caution.
- Boosts/bonus bets: positive estimated EV against a credible de-vigged reference and correct promo payout rules; zero cost alone is not proof of an exploitable edge, and restrictions/opportunity costs matter.
- An edge estimate without calibrated probabilities is not a formal BET; WATCH/PASS when evidence is insufficient. Do not use 4pp as a guarantee of profitability.

## Bankroll and risk
Use a dedicated bankroll the user can afford to lose entirely. If an actual user-approved stake is contemplated, suggested upper limits: quarter Kelly, max 2% of CURRENT bankroll per bet and max 5% combined exposure per game, including correlated bets. Never chase losses or automatically place wagers. Caps are ceilings, not target stakes. Track exposure and settlement separately from hypothetical/paper results.

## Performance measurement
For early prospective cohorts prioritize (1) complete, source-verified contract capture, (2) matched de-vigged closing-line value when actually available, and (3) proper Brier/probability scoring for precommitted unconditional/conditional forecast basis. Do not assert CLV always converges faster than ROI; measure its coverage and bias. Hypothetical outcomes are not actual profit. About 1,450 independent, comparable -110 bets may be needed for a rough two-standard-error separation of 5% ROI from zero under simplifying assumptions; this is NOT a universal sample-size guarantee (correlation, selection, pricing and variance matter). Ten contracts test operations only.

## Sunday October 18 prospective paper pilot
- Aim for >=30 *screened* contracts if observable, not >=30 wagers. Preserve every screened prop, including PASS, WATCH, failed price attempts and missing-data reasons. Freeze a clearly defined screenshot-sourced candidate list before reviewing model verdicts, without post-hoc cherry-picking. Never fabricate additional candidates to hit a target.
- International 9:30 AM ET kickoff can enter only with a genuine timestamped pre-kickoff freeze; otherwise exclude.
- 10:00 AM ET capture screenshots across accessible books and freeze the cohort; 10–11 AM compare independent ChatGPT and Claude assessments of the SAME screenshot contracts. Claude is a separate service: PRIME cannot claim its output unless user provides it or an actually authorized connector returns it.
- 11:30 AM ET official early-window inactives; 12:30 PM ET refreshed price screenshots; approximately 12:55 PM ET closing screenshots where possible; late games/SNF/MNF separate pregame mini-slates.
- Per contract record exact book, line, side, price, observation/source times, push rule, p_fair and its evidence basis, probability edge in pp, central/conservative EV, BET/PASS (retain granular internal LEAN/WATCH/AVOID), stake if actually placed, correlated exposure, closing line/price, outcome, payout, and ticket screenshot reference only if real. Log each model's forecast/decision independently; missing Claude output = unavailable, not agreement.
- Grade Monday: all frozen predictions, Brier where defined, matched de-vigged CLV where verified, capture/price coverage and model disagreements. Do not optimize thresholds using the same pilot and then claim out-of-sample success.

## Deferred versus nondeferrable
Until >=300 screened contracts, defer *advanced optimization* of analyst rankings, combined CLV composites, de-vig-method tournaments and threshold-coherence repairs. Do NOT defer basic mathematical coherence checks, same-contract price integrity, safe settlement handling, source staleness detection, user-ticket truth or repair planning for malformed CSVs. Grok Pulse from September is stale and never production-current; monitor it as a data-integrity issue but do not waste research cycles recycling it.

## Required conduct
Preserve GitHub main as durable NFL-only record. Read latest AGENTS.md and governing configs before analysis. Never overwrite existing bet/ticket facts from Grok, external analysts or synthetic research. Preserve immutable research and status evidence, verify every GitHub commit by read-back, and do not claim changes to a separate Dot schedule or Claude workflow unless actually verified.
