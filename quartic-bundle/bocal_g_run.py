import numpy as np
from scipy.special import gammaln
w1,w2=1.0,np.sqrt(2.0); g=0.05
def coh(al,N):
    n=np.arange(N); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
sysd={}
for N in [72,64,44]:
    dd=np.load(f'bq_{N}.npz'); sysd[N]=(dd['E'],dd['V'],(dd['n1']>34)|(dd['n2']>34))
print("caches charges (44, 64, 72)")
ts=np.linspace(0.5,40.0,60); svals=[0.5,0.7,0.9,1.1,1.3,1.5]
d=np.load('bocal_ab_data.npz'); gs=d['gs']; ssL=d['ssL']; tbA=d['tbA']; gi=np.argmin(np.abs(gs-0.05))
def tclas(s):
    v=tbA[gi,np.argmin(np.abs(ssL-s))]
    return f"{v:.0f}" if np.isfinite(v) else "inf"
def flux(N,s):
    E,V,ed=sysd[N]
    psi0=np.kron(coh(3*s*np.sqrt(w1/2),N),coh(-2*s*np.sqrt(w2/2),N))
    c=V.T@psi0; P=[]
    for t in ts:
        psi=V@(np.exp(-1j*E*t)*c); P.append(np.sum(np.abs(psi[ed])**2))
    P=np.array(P); m=(P>1e-8)&(P<0.02)
    if m.sum()>=6: sl=np.polyfit(ts[m],P[m],1)[0]
    else: sl=np.polyfit(ts[ts<=12],P[ts<=12],1)[0]
    return max(sl,1e-14)
print(f"\n  {'s':<6}{'G(N=44)':<12}{'G(N=64)':<12}{'G(N=72)':<12}{'64/72':<8}{'tau=1/G(72)':<13}{'t_blow class.'}")
G=[]
for s in svals:
    g44=flux(44,s) if s in (0.7,1.1) else None
    g64=flux(64,s); g72=flux(72,s); G.append(g72)
    s44=f"{g44:.2e}" if g44 else "--"
    print(f"  {s:<6.1f}{s44:<12}{g64:<12.2e}{g72:<12.2e}{g64/g72:<8.2f}{1/g72:<13.1e}{tclas(s)}")
G=np.array(G); sv=np.array(svals); lg=np.log(G)
print()
for name,xf in [("ln G = a - b/s^2",1/sv**2),("ln G = a - b/s",1/sv),("ln G = a + b ln s",np.log(sv))]:
    A=np.vstack([np.ones_like(xf),xf]).T
    coef,_,_,_=np.linalg.lstsq(A,lg,rcond=None)
    R2=1-np.sum((lg-A@coef)**2)/np.sum((lg-lg.mean())**2)
    print(f"  {name:<22} : a={coef[0]:+.2f}, b={coef[1]:+.2f}, R^2={R2:.4f}")
np.savez('bocal_gamma.npz',svals=sv,G72=G)
