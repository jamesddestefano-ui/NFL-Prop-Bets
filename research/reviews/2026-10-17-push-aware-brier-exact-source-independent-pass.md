# PRIME push-aware Brier benchmark — exact-source independent reproduction
Date: 2026-10-17 ET
Result: **PASS** on seven synthetic tests; GitHub Actions status **UNVERIFIED**; historical predictive benefit **UNVERIFIED**.

## Exact sources
Private repository `jamesddestefano-ui/-NFL-Prop-Odds-Data`, main, accessed with the authenticated GitHub connector on 2026-10-17 ET.
- `scripts/backtest_benchmark.py` Git blob SHA `2036afe2bcd3f758472bb3a9489a99884cc599ca`, introducing `compare_push_aware`.
- `tests/test_backtest_benchmark_push_aware.py` Git blob SHA `2f9bd97367682e9752faf9faf87be4981ed6ff45`.
- Original implementation commit `a111ab9b4b7ec1c73c7b47bce2aabf118505d207`, regression commit `9be59f941f9bf55f16dc947ec07263df9d97a2f2`, CI configuration commit `9ff7a6f86a76c8a11a04f4b358bfe4d010001467`.

## Independent reproduction
The *exact connector-returned source contents* were written to a temporary isolated local filesystem tree. Before execution `git hash-object` produced **both** blob hashes above, matching GitHub. No external dependency, private odds, database, keys, actual bet history or network calls were involved.

Command:
```bash
cd /mnt/data/prime_brier_check
python -m unittest discover -s tests -p 'test_backtest_benchmark_push_aware.py' -v
```
Actual test result: seven cases PASS (all pushes rejected as unscorable; baseline already conditional; equal model/baseline conditional probability yields no artificial gain; invalid probability mass rejected; missing baseline basis rejected; missing baseline push probability rejected; pushes excluded and counted). Output: `Ran 7 tests in 0.001s`, `OK`.

## Scope and unresolved evidence
This validates the synthetic correctness of the **new** `compare_push_aware` API, not the legacy `compare` behavior, and not the validity or timing of the baseline forecasts. Live/historical Brier improvements, prospective calibration, cross-game correlation, market executability and settlement contract matching have not been validated.

GitHub combined statuses for the CI commit returned `[]`; the commit-associated workflow run lookup also returned `[]`, but is limited to pull-request-triggered runs. Neither establishes successful or failed push-triggered Actions execution. A CI job ID, conclusion and actual job log are still required before reporting CI PASS.

`MODEL_SUSPECT` remains; no wagers, production gates, paid compute, original snapshots or authoritative betting records changed.
