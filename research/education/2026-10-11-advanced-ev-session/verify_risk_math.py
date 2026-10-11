"""Reproduce synthetic educational examples; no external data or real bets."""
import json
import math
from fractions import Fraction as Q

p, b = Q(11, 20), Q(91, 100)
edge = p * b - (1 - p)
f_star = edge / b
assert edge == Q(101, 2000)
assert f_star == Q(101, 1820)

def growth(f, prob=p):
    f, prob = float(f), float(prob)
    return prob * math.log1p(float(b) * f) + (1 - prob) * math.log1p(-f)

single = []
for name, f in [('half_log_optimum', f_star / 2), ('log_optimum', f_star), ('oversized', Q(1, 5))]:
    mu, g = float(edge * f), growth(f)
    single.append(dict(name=name, exposure=float(f), arithmetic_mean=mu,
                       expected_log_growth=g, five_loss_wealth=float((1-f)**5),
                       mean_wealth_100=(1+mu)**100,
                       exp_expected_log_wealth_100=math.exp(100*g)))
assert growth(f_star) > growth(f_star/2) > 0 > growth(Q(1,5))

pair = []
f = Q(3, 100)
returns = [2*b*f, (b-1)*f, (b-1)*f, -2*f]
distributions = {
    'independent': [p*p, p*(1-p), (1-p)*p, (1-p)**2],
    'positively_dependent': [Q(45,100), Q(1,10), Q(1,10), Q(35,100)]
}
for name, probabilities in distributions.items():
    assert sum(probabilities) == 1
    assert probabilities[0] + probabilities[1] == p
    assert probabilities[0] + probabilities[2] == p
    mean = sum(q*r for q,r in zip(probabilities, returns))
    variance = sum(q*(r-mean)**2 for q,r in zip(probabilities, returns))
    rho = (probabilities[0]-p*p)/(p*(1-p))
    assert mean == Q(303, 100000)
    pair.append(dict(name=name, mean=float(mean), variance=float(variance),
                     sd=math.sqrt(float(variance)), correlation=float(rho),
                     expected_log_growth=sum(float(q)*math.log1p(float(r))
                                             for q,r in zip(probabilities, returns))))

loss_probability_100 = sum(math.comb(100,k)*.55**k*.45**(100-k) for k in range(58))
assert .69 < loss_probability_100 < .70
assert Q(55,100) == Q(550,1000) == p
print(json.dumps(dict(single=single, pair=pair,
                     oversized_terminal_loss_probability_100=loss_probability_100,
                     exact_half_growth_ratio=growth(f_star/2)/growth(f_star)), indent=2))
