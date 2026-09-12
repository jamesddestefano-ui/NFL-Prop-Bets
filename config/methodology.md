# Methodology

## Decision model

Use a 100-point review framework as a disciplined checklist, not as fake precision:

- Role/opportunity: 30
- Independent projections: 25
- Market/price: 20
- Injury/news: 10
- Game environment: 10
- Matchup-specific adjustment: 5

A strong prop should normally have support from role, price, and at least one independent projection path. Matchup is an adjustment, not the starting point.

`config/advanced_market_learning.md` is mandatory and extends this methodology. Where this file is less specific, the advanced market-learning rules control.

## Preferred metrics by market

### QB passing yards / completions / attempts
- expected offensive plays
- pace
- pass rate / PROE
- dropbacks and attempts
- pressure and sack environment
- receiver availability
- aDOT / completion profile
- game spread and trailing probability

### QB rushing
- designed runs
- scrambles
- pressure rate
- man-coverage exposure
- kneel-down/sack grading rules by sportsbook

### RB rushing
- snap share
- carry share
- early-down role
- goal-line share
- offensive line availability
- projected game script

### RB receiving
- route participation
- target share / TPRR
- third-down and two-minute role
- pass-protection responsibilities
- status of competing passing-down backs

### WR/TE receptions and receiving yards
- route participation
- target share
- TPRR
- first-read share when available
- aDOT
- air-yard share
- slot/wide alignment when relevant
- red-zone/end-zone target share
- target competition and injuries

### Touchdowns
- team implied scoring environment
- red-zone/inside-10 role
- end-zone targets
- goal-line carries
- route/carry participation
- price discipline because variance is high

## Market rules

At -110, raw break-even probability is 52.38%.

Use current odds, not memory. When both sides are available, remove vig before comparing the market to the internal fair probability.

A formal play should define:
- sportsbook
- timestamp_et
- recommended line
- recommended odds
- best market line
- consensus line
- play-to line
- max acceptable juice
- fair odds
- estimated edge
- edge bucket
- entry timing bucket

Every material evaluation must end in one of: `BET`, `LEAN`, `WATCH`, `PASS`, `AVOID`.

If a favorable line has already moved materially, recalculate at the new number and classify the state as `BET_NOW`, `STILL_PLAYABLE`, `REDUCED_EDGE`, `PASS_AFTER_MOVE`, or `MIDDLE_OPPORTUNITY`. Record value lost rather than chasing.

## Fair-line framework

When sufficient data exists, estimate both central tendency and probability:
- mean projection
- median projection
- estimated Over probability
- estimated Under probability
- fair odds
- no-vig market probability
- estimated edge

A point projection being above/below the line is not enough by itself. The probability edge must clear pricing and uncertainty.

## Confidence grades

- A: unusually strong alignment of role, projection, price, and news; still not a guarantee.
- B: meaningful edge with manageable uncertainty.
- C: small edge, high uncertainty, or price-sensitive watchlist only.
- PASS: no sufficient edge, stale number, unresolved news, or excessive variance.

Confidence and stake are separate. Higher confidence does not automatically justify uncontrolled exposure.

## Closing-line value

Track CLV separately from win/loss.

At minimum preserve:
- opening line / odds
- first-detection line
- recommendation line
- user-bet line
- closing line / odds

Calculate `LINE_CLV`, `PRICE_CLV`, and `COMBINED_CLV` when sufficient information exists.

Examples:
- Bet over 14.5, closes 17.5: positive line CLV.
- Bet over 14.5 -105, closes over 14.5 -130: positive price CLV.

CLV is the primary process metric. A losing bet with strong CLV may still reflect a good process; a winning bet with poor CLV may require process review.

## Probability calibration

When a fair probability is recorded, preserve it for calibration. After settlement compute Brier score and review predicted-vs-actual hit rate in buckets:
- 50-54%
- 55-59%
- 60-64%
- 65%+

## Correlation / exposure

Tag same-thesis and correlated bets. Track exposure by game, player, and thesis. Parlays remain separate from straight-prop performance, and each parlay leg must also be graded independently.

## Weekly learning

After every NFL week produce a system review covering straight-bet P/L, parlay P/L, ROI, CLV, process wins/losses, signal performance, prop-type specialization, timing performance, missed opportunities, correct passes, calibration, and model changes.
