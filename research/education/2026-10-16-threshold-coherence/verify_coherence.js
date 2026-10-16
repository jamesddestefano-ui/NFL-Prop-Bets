// Synthetic NFL reception-ladder checks. No observed prices or empirical outcomes.
// Run: node verify_coherence.js
const A=[.3,.1,.6], B=[.6,.1,.3]; // count support 4,5,6
const mix=(a,b,w)=>a.map((v,i)=>w*v+(1-w)*b[i]);
const tail=(pmf,k)=>pmf.reduce((s,p,i)=>s+(i+4>=k?p:0),0);
const close=(a,b)=>Math.abs(a-b)<1e-10;
let checks=0;function check(x,label){if(!x)throw Error(label);checks++;}
for(const w of [0,.1,.3,.5,.7,.9,1]){
 const p=mix(A,B,w);
 check(close(p.reduce((a,b)=>a+b,0),1),"mass");
 check(p.every(x=>x>=0),"nonnegative");
 check(tail(p,5)>=tail(p,6),"nested");
}
const incoherent=[.1*.7+.9*.4,.9*.6+.1*.3];
check(incoherent[0]<incoherent[1],"deliberate crossing");
check(close(incoherent[0]-incoherent[1],-.14),"negative mass");
const central=tail(mix(A,B,.7),5),adverse=tail(mix(A,B,.3),5),d=21/11;
check(close(central,.61),"central");
check(close(adverse,.49),"adverse");
check(close(central*d-1,.16454545454545455),"central ROI");
check(close(adverse*d-1,-.06454545454545455),"adverse ROI");
check(close(1/d,11/21),"break even");
check(close((11/21)/(22/21),.5),"two sided no vig");
check(close(tail(mix(A,B,.7),6),.51),"higher line");
check(tail(mix(A,B,.7),6)*d-1<0,"higher line negative");
check(close(100*central/(1-central),156.4102564102564),"central fair juice");
check(close(100*(1-adverse)/adverse,104.08163265306123),"adverse positive fair odds");
const project=(incoherent[0]+incoherent[1])/2;
check(close(project,.5),"two point equal weight monotone projection");
check(close((project-incoherent[0])**2+(project-incoherent[1])**2,.0098),"projection displacement");
console.log(JSON.stringify({checks,central,adverse,central_roi:central*d-1,adverse_roi:adverse*d-1,incoherent,project},null,2));
