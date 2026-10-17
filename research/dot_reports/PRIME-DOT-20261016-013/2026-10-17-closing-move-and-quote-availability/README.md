# Closing-move correlation can reward the wrong forecaster

**Task PRIME-DOT-20261016-013 · October 17, 2026 · morning research cycle (EDT).** Review-only educational protocol and deliberately synthetic tests. Source and verification windows are recorded in the [source register](source-register.md) and manifest. No prospective NFL experiment, current executable quote, model superiority or betting-rule change is claimed.

## What changed in our understanding

1. **A strong forecast-versus-move correlation can come from subtracting the same noisy starting market twice.** In a fully enumerated example, correlation is 0.80 even though the model's close forecast and the closing probability are independent. The model beats a no-change forecast but loses to a constant forecast. A test must measure incremental performance against plausible simple baselines, not just correlation with movement.
2. **A quote seen again five minutes later has not necessarily survived continuously.** It may have disappeared and returned between observations. Ordinary checkpoint data support availability-at-checkpoint measurements, with unknown observations retained. They do not establish executable lifetime or fills.
3. **More rows do not necessarily supply more independent evidence.** Alternate lines, books and repeated checkpoints from one game can be highly dependent. Paired forecast losses must retain that dependence, and game-weighted versus contract-weighted comparisons answer different questions.

**METHODOLOGY_CHALLENGE:** movement correlation alone is insufficient evidence of incremental forecast skill. **MODEL_UNCERTAINTY:** a closing benchmark remains an estimate, and observation gaps leave execution claims unresolved.

These extend the existing [October 16 review](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/b0c61f91b3b6bfa15bb724d24c3e3e8cafe7829a/research/reviews/2026-10-16-claude-advanced-assignment-final-review.md), which already rejected retrospective “leading versus stale” labels and a universal 200-observation rejection rule. The new contributions are an exact shared-baseline counterexample, reversible-quote observation limits, executable synthetic guards, and a falsifiable measurement protocol. Earlier reports are preserved rather than rewritten.

## Lesson 1: test incremental information, not a shared subtraction

**VERIFIED MATHEMATICAL PRINCIPLE.** Let A be a locked model probability, M the entry-market benchmark and C the later same-contract closing benchmark. On the probability scale,

Cov(A−M, C−M) = Cov(A,C) − Cov(A,M) − Cov(M,C) + Var(M).

This identity alone does not say the covariance is spurious in every dataset. It shows why the shared term must be examined. A noisy reference or simple mean reversion can produce apparently impressive association without incremental football information.

**MODEL ASSUMPTION: eight invented cases.** Independently choose u = ±0.02, e = ±0.01 and v = ±0.01, each sign with equal probability. Set M = 0.50 + u, A = 0.50 + e and C = 0.50 + v. These are toy probability-valued variables, not actual NFL forecasts or market quotes.

- Cov(A,C) = 0, but Cov(A−M,C−M) = 0.0004.
- Both difference variances equal 0.0005, so their correlation is 0.80.
- Expected squared error against C is 0.0005 for no-change M, 0.0002 for model A and 0.0001 for fixed 0.50.

The model genuinely improves on the noisy no-change baseline **in this constructed experiment**, yet adds nothing over the better trivial benchmark. Calling the whole improvement illusory would also be wrong. The proposed test therefore compares locked forecasts against no change, prespecified momentum and a frozen mean-reversion baseline on the same cases. A fitted baseline must use earlier data only; it cannot learn this week's close.

For baseline B, define paired improvement D = (B−C)² − (A−C)². Positive mean D means lower squared error for forecasting the chosen closing-market estimate. Equivalently, subtracting M from both prediction and target leaves this loss unchanged. This is a continuous-target squared-error comparison, **not a football-outcome Brier score or proof that C is the true win probability**.

The original statistical reading concerns baseline/change-score coupling, not sports prediction. Our three-variable construction and NFL protocol are independent extensions; source-specific cautions are retained in the register.

## Lesson 2: observe availability honestly

**VERIFIED MATHEMATICAL PRINCIPLE.** At a prespecified checkpoint, suppose ten originally eligible quotes yield six confirmed active observations, two confirmed inactive observations and two unknowns. The finite-cohort active proportion is bounded by 6/10 and 8/10. Reporting 6/8 = 75% describes only the successfully classified subset. The bounds are identification limits, not 95% confidence intervals or population estimates.

**MODEL ASSUMPTION / observation limit.** With reversible quotes, active at minute 2 and absent at minute 5 does not even establish that the *first* disappearance occurred between minutes 2 and 5: an earlier disappearance and return may have been missed. The usual bracket between last observed active and first observed inactive requires a no-reentry assumption or stronger event history. If lifetime is defined from confirmed-active entry t0, a later observed absence at U still gives the coarser first-loss bound (t0,U], despite possible re-entry. NIST's non-repairable-lifetime illustration is not automatically a quote-market model.

The [protocol](protocol.md) uses separate outcomes for (a) exact-contract source quote present, (b) original price or better at that checkpoint and (c) directly verified jurisdiction-specific active display if actually available. None implies an accepted fill, capacity, uninterrupted availability or permission to wager. Unknown is never silently converted to inactive, surviving or zero return.

## Lesson 3: compare like with like and preserve dependence

**ANALYST OPINION / proposed design.** Use paired comparisons on an identical, frozen eligibility mask. Primary summary averages contract-level loss differences within each game and then averages games equally. Report a contract-weighted secondary result separately. Repeated checkpoints and alternative books are not independent replications of the football event. Game clustering requires a defensible cross-game-independence approximation; week-level sensitivity matters when common shocks or repeated players span games.

Neither cluster labels nor a bootstrap manufacture information from a handful of games. Sunday's small pilot can establish capture feasibility and reveal contradictions. It cannot prove general AI superiority; a wide interval is inconclusive, not evidence that signal is absent.

## Current public evidence and the proposed next test

**EMPIRICAL EVIDENCE: access and provenance observations only.** The [October 17 public checkpoint](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/b0c61f91b3b6bfa15bb724d24c3e3e8cafe7829a/intelligence/archive/2026-10-17T12-14-21Z-week6-market-context.md) now records a historical named-book two-sided comparison. This review read that record, not the underlying live sportsbook: its quote values are not independently renewed here. An earlier task's zero-admitted-quote result is not a claim that today's repository contains no odds. A later matched close, actual delay checks and jurisdiction-specific execution evidence remain untested in this task.

Today's original X/official-source crosscheck, detailed in the source register, separates a confirmed injury designation from an analyst's predicted route redistribution. It supplies no verified pre/post book panel and cannot establish early-market leadership, calibrated player probabilities or a profitable source ranking.

**UNTESTED HYPOTHESIS.** A locked model forecast improves later matched-close prediction beyond the prespecified baselines on future weeks, and any useful apparent price discrepancy remains observable at realistic delays. The protocol specifies the universe, clocks, endpoints, missingness, uncertainty and rejection conditions before those data exist. No conclusion about either ChatGPT or Claude's actual performance follows today; missing external forecasts remain missing.

## Scope, confidence and handoff

- High confidence in checked algebra, finite synthetic fixtures and stated access observations; moderate confidence in the proposed design choices; NFL transfer and financial improvement unestablished.
- No current offered line/price, empirical fair probability, no-vig estimate for a live decision, central/conservative EV, operational play-to or stake is supplied. Those are unassessed, not zero.
- Current [v2 overlay](https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/b0c61f91b3b6bfa15bb724d24c3e3e8cafe7829a/config/prime_ev_playbook_v2.md) controls decisions. This report does not restore the older separate 5% ROI gate or change conservative-EV, settlement, source, news or exposure requirements.
- Task013's deliverable is a protocol and synthetic tests. A terminal queue event can mark that deliverable complete only after the report commit is known and read back; empirical execution remains future work. Tasks011 and012 are not implicitly completed, and the actual Sunday008 pregame/postgame work remains separate.

Reproduction: run `python -B verify.py`. The final package passes 31 unit tests, fresh-process byte comparisons, exact rational result checks and SHA-256 checks. These are synthetic measurement fixtures, not a full production validator or empirical NFL backtest.

See [source register](source-register.md), [proposed protocol and schema](protocol.md), [worked mathematical note](math_note.md), [script](fixture_math.py), [tests](test_fixture_math.py), and [saved results](results.json).
