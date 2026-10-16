import math,json
from statistics import NormalDist
N=NormalDist();d=21/11;p0=1/d;p1=.55
mass=lambda k: math.exp(-4.8)*4.8**k/math.factorial(k)
w45=1-sum(mass(k) for k in range(5));t=mass(5);w5=w45-t;l=1-w45
assert abs(w5+t+l-1)<1e-12
fair=(1-t)/w5
assert abs(w5*fair+t-1)<1e-12
assert abs(p1*d-1-.05)<1e-12
assert abs(.04*d-.07636363636363636)<1e-12
power_n=lambda z: ((z*math.sqrt(p0*(1-p0))+N.inv_cdf(.8)*math.sqrt(p1*(1-p1)))/(p1-p0))**2
n2=power_n(N.inv_cdf(.975));n1=power_n(N.inv_cdf(.95))
power=1-N.cdf((1450*p0+N.inv_cdf(.975)*math.sqrt(1450*p0*(1-p0))-1450*p1)/math.sqrt(1450*p1*(1-p1)))
assert 2847<n2<2848 and 2242<n1<2243 and .51<power<.52
# Same mean, different count families; invented, not empirical fits.
binomial=sum(math.comb(8,k)*.6**k*.4**(8-k) for k in range(5,9))
assert abs(binomial-.5940864)<1e-10
# Bonus conversion depends on probability, not longest odds alone.
assert .15*(6-1)<.45*(3-1)
assert abs(.45*(1+1.25*100/110)-1-(-.03863636363636369))<1e-12
r={'checks':'8 assertions passed','poisson_over4_5':w45,'push5':t,'over5':w5,'under5':l,'fair_over5_decimal':fair,'over4_5_roi_minus110':w45*d-1,'two_sided_80pct_n_unrounded':n2,'one_sided_80pct_n_unrounded':n1,'two_sided_power_n1450_normal_upper_tail':power,'binomial8_p06_over4_5':binomial}
print(json.dumps(r,indent=2))
