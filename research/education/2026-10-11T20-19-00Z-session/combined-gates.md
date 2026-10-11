# Combined pricing gates for the same contract

Synthetic research fixtures, 2026-10-11. No live NFL prices or observed outcomes.

## Framework basis
Independently read config/positive_ev_framework.md on main, blob 662a497ecc8a0da54fe7e36deffc5cd66d993fd9, sections 2, 7 and 9. The standard-market starting gates are approximately 4 percentage points of central probability edge, approximately 5% central expected ROI, and positive conservative EV. Market grade A/B and unresolved-role/injury controls also remain necessary. The algebra below uses EXACT e=0.04 and r=0.05 only to create reproducible research fixtures. This is not adoption of hardcoded constants or a replacement for the controlling framework.

The framework defines probability edge against the offered price's break-even probability, p_internal - 1/d. It is NOT the same quantity as disagreement with the de-vigged benchmark p_market. Do not substitute the latter in these fixtures.

## 1 Combined no-push price boundary

Hold fixed the exact event, central probability p0 and adverse probabilities p_s. For decimal odds d>1:

```text
  Central edge: p0 - 1/d >= e.
  Central ROI:  p0*d - 1 >= r.
  Adverse EV:   min_s(p_s*d - 1) > 0.
```

For p0>e and all p_s>0, these are equivalent to:

```text
  d >= 1/(p0-e),
  d >= (1+r)/p0,
  d > max_s(1/p_s).
```

The last boundary is STRICT. Taking the maximum of all three numbers and allowing equality can accidentally admit zero conservative EV. The full accepted-price set is the intersection of the three inequalities. No finite price passes if p0<=e or an adverse scenario assigns zero chance to winning.

Example using the appendix's p0=0.55:

```text
  Central edge boundary: 1/(0.55-0.04)=1.960784314.
  Central ROI boundary: 1.05/0.55=1.909090909.
```

With narrow scenarios p=0.53 or 0.57:

```text
  Adverse boundary: d>1/0.53=1.886792453.
  The edge gate controls. The inclusive combined boundary is d=1.960784314, equivalent American -104.081633.
  At that boundary: central edge=4.00pp; central ROI=7.843137%; worst-scenario ROI=3.921569%.
  Whole-number -104 passes all numeric gates; -105 fails the central edge gate.
```

At -110, the same central 55% gives central ROI=5.00% and positive narrow-scenario EV, but central probability edge is only 2.619048pp. It therefore fails the nominal 4pp test. The original appendix's isolated 5% ROI boundaries should not be mislabeled as complete PRIME play-to prices.

With wide scenarios p=0.49 or 0.61:

```text
  Adverse boundary: d>1/0.49=2.040816327, equivalent American +104.081633.
  This strict adverse gate controls. Exact equality has zero conservative EV and fails. Whole-number +105 passes the numeric gates, while +104 fails.
```

Probability-point edge and ROI percentage are different units. In the no-push case, ROI=d*(probability edge). For e=0.04 and r=0.05, the central edge price bound is at least as restrictive as the central ROI bound when p0<=0.84; the ROI bound is more restrictive above 0.84. This comparison does not remove the adverse or non-price gates.

## 2 Proposed push-capable extension

The framework's displayed binary formulas do not settle the push-conditioning convention. The following is a proposed mathematically coherent clarification for review, not a claim that policy was changed:

```text
  Use q0=p_win0/(1-p_push0) for central probability edge against 1/d.
  Keep central ROI per ORIGINAL unit staked: p_win0*d+p_push0-1.
  Evaluate every adverse joint scenario (p_win_s,p_push_s), with p_loss_s=1-p_win_s-p_push_s.
```

For standard stake-refunded pushes, the proposed numeric gates are:

```text
  q0 - 1/d >= e,
  p_win0*d+p_push0-1 >= r,
  min_s[p_win_s*d+p_push_s-1] > 0.
```

For positive win probabilities, q0>e and p_push0<1, the price boundaries are:

```text
  d >= 1/(q0-e),
  d >= (1+r-p_push0)/p_win0,
  d > max_s[(1-p_push_s)/p_win_s].
```

This requires complete valid scenario vectors; 0<=p_win_s,p_push_s and p_win_s+p_push_s<=1. Do not independently combine the lowest win mass and lowest push mass from incompatible scenarios and call the result an observed downside case. Such a rectangular uncertainty set is a different modeling choice and may be more conservative.

## 3 Lowest win probability need not be worst EV

Scenario A: p_win=0.50, p_push=0.10, p_loss=0.40.
Scenario B: p_win=0.51, p_push=0.05, p_loss=0.44.

At -110:

```text
  A: ROI=+5.454545%.
  B: ROI=+2.363636%, the worse scenario despite its HIGHER win probability.
```

At decimal odds 1.85:

```text
  A: ROI=+2.50%.
  B: ROI=-0.65%.
```

Choosing only the lowest p_win scenario A would falsely pass the positive-conservative-EV gate. Evaluating both complete scenarios correctly fails it.

The conditional probabilities explain the positive-EV boundary:

```text
  q_A=0.50/0.90=55.555556%.
  q_B=0.51/0.95=53.684211%.
  EV_s=(1-p_push_s)*(q_s*d-1).
```

The lowest q_s sets the strongest zero-EV price boundary, but the smallest actual ROI at a given price should still be calculated from the complete scenario. Varying non-push mass can change ROI ranking away from the zero-EV boundary. For any nonzero adverse ROI hurdle, the complete scenario is again necessary.

This conditional argument requires p_push<1. An all-push scenario has EV=0 and cannot pass a strictly positive gate.

## 4 Combined push fixture

Hypothetical central vector: (p_win0,p_push0,p_loss0)=(0.54,0.10,0.36), so q0=0.60. Adverse vectors are A and B above.

```text
  Central edge boundary: d>=1/(0.60-0.04)=1.785714286.
  Central ROI boundary: d>=(1.05-0.10)/0.54=1.759259259.
  Adverse boundary: d>max(0.90/0.50,0.95/0.51)=1.862745098.
```

At d=1.85, central edge=5.945946pp and central ROI=9.90%, but scenario B ROI=-0.65%. It fails even though both central gates pass.

The strict combined boundary is d>1.862745098, equivalent American odds better than -115.909091. Whole-number -115 passes the numeric gates with worst-scenario ROI=+0.347826%; -116 fails with worst-scenario ROI=-0.034483%. Neither price is claimed to exist, nor does a numerical pass resolve role, evidence-quality or exposure gates.

For central non-push mass lambda0=1-p_push0, ROI=lambda0*(q0*d-1). At the central edge boundary, ROI=lambda0*e/(q0-e). Therefore the central edge bound is at least as restrictive as the central ROI bound only when q0<=e*(lambda0+r)/r. The crossover is 0.84 with no push and 0.76 with a 10% push probability. Treating conditional ROI as per-original-stake ROI would miss this distinction.

## Scoring reminder
If the conditional probability q is scored on non-push settlements, evaluate the predicted push probability on the FULL prespecified eligible cohort. It cannot be calibrated using only the subset with pushes excluded. Alternatively score the full win/loss/push probability vector. Conservative scenario bounds remain decision sensitivities, separate from central forecasts used in calibration analysis.

## Reproduction and evidence limit

Copy this directory to a working folder before rerunning. Run [combined_gate_checks.py](combined_gate_checks.py), which imports helpers from [verify_examples.py](verify_examples.py) and writes [combined_gate_results.json](combined_gate_results.json). Exact-Fraction fixtures, boundary assertions and 168 comparisons of direct versus inverted gate formulas all passed. The entire supplement is original mathematical synthesis of the stated framework and synthetic inputs; it establishes no empirical NFL calibration or profit. These scripts are educational examples, not installed decision-engine code.

## Framework source
https://github.com/jamesddestefano-ui/NFL-Prop-Bets/blob/main/config/positive_ev_framework.md

Keep probabilities fixed only for this local price inversion. Changed thresholds, material news, settlement terms or a revised probability model require a fresh calculation. A computed price boundary cannot make a stale or unverified quote executable.
