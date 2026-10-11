"""Secondary tail cross-check using SciPy; run verify_examples.py first."""
from scipy.stats import binom
from math import isclose
import json
from pathlib import Path
p=Path(__file__).parent
r=json.loads((p/'example_results.json').read_text())
tests={
 'carry_mixture_tail':isclose(.5*binom.sf(19,60,.42)+.5*binom.sf(19,60,.15),r['carry_mixture']['p_over_19_5'],abs_tol=1e-12),
 'same_mean_tail':isclose(binom.sf(19,60,.285),r['carry_same_mean_binomial']['p_over_19_5'],abs_tol=1e-12)}
for n,key in [(6,'receiver_baseline'),(18,'receiver_expanded_deep_routes')]:
 rec=sum(binom.pmf(k,18,.24)*binom.sf(4-k,n,.04) for k in range(19))
 yd=sum(binom.pmf(k,18,.24)*binom.sf((49-8*k)//30,n,.04) for k in range(19))
 tests[key+'_rec_tail']=isclose(rec,r[key]['p_over_4_5_receptions'],abs_tol=1e-12)
 tests[key+'_yards_tail']=isclose(yd,r[key]['p_over_49_5_yards'],abs_tol=1e-12)
assert all(tests.values())
(p/'crosscheck_results.json').write_text(json.dumps({'method':'SciPy binomial PMF and survival function, six tail comparisons','checks':tests},indent=2)+'\n')
print('Passed',len(tests),'tail cross-checks')
