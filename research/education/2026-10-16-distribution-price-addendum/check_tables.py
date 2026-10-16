import json, math
from scipy.stats import binom, poisson, nbinom, lognorm
D=21/11
rows=[]
for name,var in [('locked',.25),('poisson',7.5),('negative_binomial_2x',15),('negative_binomial_3x',22.5)]:
 if name=='locked': over=(binom.sf(4,7,.64)+binom.sf(4,8,.64))/2
 elif name=='poisson': over=poisson.sf(4,4.8)
 else:
  r=7.5**2/(var-7.5)
  over=nbinom.sf(4,r,r/(r+4.8))
 rows.append(dict(model=name,target_variance=var,reception_sd=math.sqrt(7.5*.64*.36+.64**2*var),over=float(over),under=float(1-over),over_roi=float(over*D-1),under_roi=float((1-over)*D-1)))
yards=[]
for cv in [.5,.7,.9]:
 sigma=math.sqrt(math.log(1+cv*cv));median=65/math.sqrt(1+cv*cv)
 yards.append(dict(cv=cv,median=median,over55_5=float(lognorm.sf(55.5,sigma,scale=median)),over60_5=float(lognorm.sf(60.5,sigma,scale=median)),over100=float(lognorm.sf(100,sigma,scale=median))))
assert abs(rows[0]['over']-.5970519937515522)<1e-12
assert rows[2]['under']>.5 and rows[2]['under_roi']<0
assert 0<rows[3]['under_roi'] and rows[3]['under']-1/D<.04
assert 0<(1-yards[1]['over55_5'])*D-1<.005
assert yards[2]['over100']>yards[0]['over100']
assert abs(yards[1]['over55_5']-.47387446436126474)<1e-12
print(json.dumps(dict(status='6 assertions passed',assumptions='Synthetic distributions; not historical NFL results or reproduction of claimed simulations.',receptions=rows,yardage=yards),indent=2))
