"""Independent high-precision arithmetic review of the optional risk appendix.
Uses no functions from the reviewed script; all probability/moment algebra exact.
"""
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import json
from math import comb
from pathlib import Path

ROOT=Path(__file__).resolve().parent
given=json.loads((ROOT/'risk_results.json').read_text())
checks=[]
def test(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)
def dec(q):
    if isinstance(q,F):return D(q.numerator)/D(q.denominator)
    return D(q)
def close(a,b,tolerance=D('1e-13')):return abs(dec(a)-D(str(b)))<tolerance

with localcontext() as context:
    context.prec=70
    p,b=F(11,20),F(91,100)
    decimal=1+b
    edge=p*b-(1-p)
    star=edge/b
    growth=lambda f,m=p:dec(m)*(1+dec(b*f)).ln()+dec(1-m)*(1-dec(f)).ln()
    single=[]
    for i,(label,f) in enumerate([('half_log_optimum',star/2),('log_optimum',star),('oversized',F(1,5))]):
        mean=edge*f
        g=growth(f)
        mean100=dec((1+mean)**100)
        exp100=(100*g).exp()
        expected=given['single'][i]
        test(label+' exact mean',close(mean,expected['arithmetic_mean']))
        test(label+' Decimal log growth',close(g,expected['expected_log_growth']))
        test(label+' exact compounded arithmetic mean',close(mean100,expected['mean_wealth_100']))
        test(label+' exponentiated expected log',close(exp100,expected['exp_expected_log_wealth_100']))
        single.append({'name':label,'fraction_exact':str(f),'mean_exact':str(mean),'log_growth_70_digit':str(g),'mean_terminal_wealth_100':str(mean100),'exponentiated_expected_log_100':str(exp100)})
    derivative_at_star=p*b/(1+b*star)-(1-p)/(1-star)
    test('analytical first derivative zero at optimum',derivative_at_star==0)
    test('positive arithmetic EV but negative log growth at .20',edge*F(1,5)>0 and growth(F(1,5))<0)
    half_ratio=growth(star/2)/growth(star)
    test('exact half-growth ratio matches reported value',close(half_ratio,given['exact_half_growth_ratio']))
    f=F(1,5)
    wealth=lambda k, exposure=f:(1+b*exposure)**k*(1-exposure)**(100-k)
    test('57 wins lose and 58 wins gain',wealth(57)<1<wealth(58))
    test('wealth is strictly increasing in win count',all(wealth(k)<wealth(k+1) for k in range(100)))
    threshold=-D(100)*(1-dec(f)).ln()/((1+dec(b*f)).ln()-(1-dec(f)).ln())
    terminal_loss=sum((F(comb(100,k))*p**k*(1-p)**(100-k) for k in range(58)),F())
    test('exact rational terminal loss probability agrees',close(terminal_loss,given['oversized_terminal_loss_probability_100']))
    test('55-win path equals exponentiated expected log',close(dec(wealth(55)),(100*growth(f)).exp()))
    test('five-loss decline exact',1-(1-f)**5==F(67232,100000))
    pairs=[]
    f=F(3,100)
    for index,(label,ww) in enumerate([('independent',p*p),('positively_dependent',F(45,100))]):
        cells=[ww,p-ww,p-ww,1-2*p+ww]
        returns=[2*b*f,(b-1)*f,(b-1)*f,-2*f]
        covariance=ww-p*p
        mean=2*f*edge
        # Independent route: moments of affine Bernoulli indicators, not payoff enumeration.
        variance=f*f*decimal*decimal*(2*p*(1-p)+2*covariance)
        rho=covariance/(p*(1-p))
        g=sum((dec(q)*(1+dec(r)).ln() for q,r in zip(cells,returns)),D(0))
        sd=dec(variance).sqrt()
        expected=given['pair'][index]
        test(label+' joint distribution valid',sum(cells)==1 and min(cells)>=0)
        test(label+' shared-time payoff mean',mean==F(303,100000) and close(mean,expected['mean']))
        test(label+' covariance-based variance',close(variance,expected['variance']))
        test(label+' high-precision standard deviation',close(sd,expected['sd']))
        test(label+' indicator correlation',close(rho,expected['correlation']))
        test(label+' high-precision joint expected log',close(g,expected['expected_log_growth']))
        pairs.append({'name':label,'joint_cells_exact':list(map(str,cells)),'mean_exact':str(mean),'variance_exact':str(variance),'standard_deviation':str(sd),'correlation_exact':str(rho),'expected_log_growth':str(g)})
    # Same-mean integration check with two distinct discrete posteriors.
    # This is enough to verify the claimed algebra; Beta means/variances below are exact too.
    f=F(1,10)
    wide=(F(3,10),F(4,5))
    narrow=(F(54,100),F(56,100))
    test('distinct posterior fixtures share mean .55',sum(wide)/2==sum(narrow)/2==p)
    wide_g=sum((growth(f,m) for m in wide),D(0))/2
    narrow_g=sum((growth(f,m) for m in narrow),D(0))/2
    test('same posterior mean gives identical one-step expected log',abs(wide_g-narrow_g)<D('1e-65') and abs(wide_g-growth(f))<D('1e-65'))
    beta_means=[F(55,100),F(550,1000)]
    beta_variances=[F(55*45,100**2*101),F(550*450,1000**2*1001)]
    test('reported Beta posteriors have same mean but different variance',beta_means[0]==beta_means[1]==p and beta_variances[0]>beta_variances[1])
    low=F(51,100)
    robust_derivative_zero=low*b-(1-low)
    test('worst-case .51 model has negative derivative at zero',robust_derivative_zero==F(-259,10000))
    test('robust no-positive-exposure result matches numerical checks',all(growth(f,low)<0 for f in (F(1,1000),F(1,100),star,F(1,5),F(9,10))))
    result={'status':'PASS','named_check_count':len(checks),'checks':checks,'single_prop':single,'half_growth_ratio':str(half_ratio),'terminal_loss':{'break_even_win_count':str(threshold),'wealth_57_wins':str(dec(wealth(57))),'wealth_58_wins':str(dec(wealth(58))),'probability_exact':str(terminal_loss),'probability_decimal':str(dec(terminal_loss))},'two_prop':pairs,'same_mean_posteriors':{'Beta_means':list(map(str,beta_means)),'Beta_variances':list(map(str,beta_variances)),'robust_derivative_at_zero_p_51':str(robust_derivative_zero)},'scope':'Independent arithmetic and stated-assumption review only. No empirical NFL model, actual bankroll advice or source-transcript audit. Brownian example excluded.'}
    (ROOT/'risk_crosscheck_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(checks)} independent high-precision checks; {ROOT / "risk_crosscheck_results.json"}')
