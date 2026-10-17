# PRIME experimental review — 2026-10-16 late cycle

Scope: NFL player props only. Governing sources read directly on main before experiment: AGENTS.md, config/prime_ev_playbook_v2.md, config/positive_ev_framework.md, config/advanced_market_learning.md, config/methodology.md.

## Reproducible synthetic experiment

Local Python unittest suite: 15/15 passed. All observations below are deliberately synthetic and not live sportsbook observations, bets, calibrated player forecasts, or realized P/L.

- Push refunded: +100 odds, p(win)=0.46, p(push)=0.10 gives EV=0.46*2+0.10-1=+0.02 per staked dollar. Binary shortcut yields -0.08 and is wrong.
- Standard price gate: boundary p(win)=1/decimal(-110)+0.04 and conservative p=1/decimal(-110) satisfies the central 4 percentage-point edge and conservative EV=0. No separate 5% ROI gate.
- At -150 odds the same 4 pp central edge implies only about 6.67% central expected ROI; use v2 gate, not an additional arbitrary hurdle.
- TD +200 p(win)=1.15/3 and conservative p=1/3 hits +15% central ROI and zero conservative EV; p(win)=0.37 fails.
- Positive central EV with negative conservative EV fails.
- Uncalibrated model probability stays WATCH, never a formal BET.
- Quote event comparison using exact event/book/player/market/side/line/odds/settlement fields ignores timestamp-only refresh, but detects price and line changes.
- Missing source timestamps remain missing; response-received time should be captured AFTER response receipt, not before API call.
- Binary EV identity holds at illustrative -150, -110, +100, +150 and +200 prices.

## Pilot implications

Do not turn a timestamp-only refresh into a market movement or CLV observation. Preserve request start, response receipt and source last-update as distinct times, and preserve source timestamp missingness. All 10 AM Oct 18 candidate screenshots must be recorded prospectively, including PASS and WATCH. An Oct 18 9:30 AM kickoff does not enter a 10 AM freeze; only a genuine pre-kickoff candidate freeze permits it. No 30+ claim without 30 observed contracts. No Claude outputs or Dot schedule modifications were observed or asserted.

## Remaining gaps

No live Odds API request made; no new independently verified NJ executable sportsbook lines; no actual calibrated probability assessment or independent out-of-sample edge demonstrated; no real Brier/CLV measurement. This suite checks core arithmetic/data handling only. A future production implementation must confirm void/dead-heat/OT/book-specific settlement and quote comparability.

## Reproduction

Python 3 stdlib unittest only. See accompanying test_prime_experiment.py. Tests are pass/fail math invariants and synthetic examples, not an NFL backtest.
