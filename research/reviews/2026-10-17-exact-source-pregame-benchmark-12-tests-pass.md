# PRIME pregame benchmark — exact-source independent synthetic verification
Date: 2026-10-17 ET
Status: **PASS (12/12 locally)**, GitHub Actions **UNVERIFIED**, MODEL_SUSPECT.

## Source and reproducibility
Private GitHub `jamesddestefano-ui/-NFL-Prop-Odds-Data` main, retrieved by authenticated connector 2026-10-17 ET. Exact Git blob identities checked with `git hash-object` on copied source:
- `scripts/pregame_benchmark_gate.py`: `15d320763c4af234ae3a5c29f5116d582b4a29f1`
- `scripts/backtest_benchmark.py`: `fe66a2be630d8a99245b859bbdecc3269747aa73`
- `tests/test_pregame_benchmark_gate.py`: `57df5805801a4f9b7f207990433fe6485f0b0f45`

Command, from isolated local tree `/mnt/data/prime_pregame_verify`:
```
python -m unittest discover -s tests -p test_pregame_benchmark_gate.py -v
```
Actual output ended `Ran 12 tests in 0.001s\n\nOK`. Tests exercised boolean/nonfinite thresholds, unsupported market and side, duplicate identity, date-only source, forecast at kickoff, training leakage, missing timezone/book/baseline basis, and a valid synthetic scored row.

## Interpretation
PASS applies only to exact-byte local synthetic unit tests. No private raw odds, real betting opportunities, historical forecast outcomes, costs or authoritative betting records were used or altered. No claim of historical Brier improvement. Actual GitHub Actions job/run conclusion has not been observed. The pregame provenance gate is opt-in and a declared source label alone does not prove that a forecast's timestamps or sources were independently authenticated.

Next: independently verify the workflow run logs, enforce immutable externally evidenced lock/source references where possible, and evaluate out-of-time coverage on actual provenance-verified nonauthoritative data. Remain `MODEL_SUSPECT`.
