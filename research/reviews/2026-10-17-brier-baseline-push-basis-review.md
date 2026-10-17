# PRIME historical Brier benchmark: push-basis comparability — 2026-10-17

Status: SOURCE-VERIFIED METHODOLOGY RISK; historical impact INCONCLUSIVE; MODEL_SUSPECT.

Source reviewed via authenticated GitHub connector on 2026-10-17 ET. Private `scripts/backtest_benchmark.py` Git blob `2dc388c8607a1b4d6679cc3ca46136f144573b65` (source commit `caef056813f4bec97a48f8c7cfa353e63c24b62b`). Private `tests/test_backtest_benchmark.py` blob `ceedaa064d6ec38417cd5fed3cad2e7efd6aa8f9` (source commit `d22be33d5b5947747a2cb21dbb78cdd4985d90f1`).

## Falsifiable comparison-basis gap
The implementation skips PUSH rows and computes model Brier with conditional probability `p_win / (1-p_push)`. It calculates baseline Brier with `baseline_p_win` directly. The baseline field has no enforced conditional-vs-unconditional basis. If baseline is an unconditional win probability and push mass is nonzero, these squared errors are not comparable. A positive `brier_improvement` could therefore partly reflect incompatible scoring bases rather than predictive superiority.

Illustrative synthetic case: outcome WIN, model p_win=.4, p_push=.5, p_loss=.1, giving conditional .8. Baseline unconditional p_win=.4, and hypothetical baseline p_push=.5 would also give conditional .8. Implementation scores model Brier .04 versus baseline .36, falsely implying a .32 improvement although conditional probabilities are equal. These are synthetic numbers, not betting or historical observations.

## Required guard before model claims
Specify `baseline_p_win_basis` explicitly (`CONDITIONAL_NON_PUSH` or `UNCONDITIONAL`) and require a valid baseline push probability when conditionalization is needed. Alternatively accept only already-conditional baseline inputs under an explicit validated schema. Test pushes, no-push, zero/invalid probability mass, and missing baseline push fields; preserve out-of-time baseline construction and all skipped-row counts. Do not make changes to settled observations, original forecasts or Sunday locks. A separate settlement-aware multiclass score may complement rather than silently replace the predeclared binary metric.

The source test only exercises p_push=0 and cannot reveal this flaw. No exact-source execution, Github Actions result, or historical magnitude is claimed in this review. No private odds are copied.
