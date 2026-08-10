import numpy as np
from scipy.special import gammaln
w1,w2=1.0,np.sqrt(2.0)
ts=np.unique(np.concatenate([np.linspace(1,20,10),np.geomspace(22,400,40),np.geomspace(450,2e4,30)]))
def coh1(al,Nl):
    n=np.arange(Nl); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def build_state(kind,Nl,s=None,ncut=None):
    if kind=='coh': return np.kron(coh1(3*s*np.sqrt(w1/2),Nl),coh1(-2*s*np.sqrt(w2/2),Nl))
    if kind=='fock00':
        v=np.zeros(Nl*Nl); v[0]=1.0; return v
    if kind=='cohcut':
        psi=np.kron(coh1(3*s*np.sqrt(w1/2),Nl),coh1(-2*s*np.sqrt(w2/2),Nl))
        n1=np.repeat(np.arange(Nl),Nl); n2=np.tile(np.arange(Nl),Nl)
        psi=psi*((n1<=ncut)&(n2<=ncut)); return psi/np.linalg.norm(psi)
def rate_curves(tag,psi):
    d=np.load(tag); E,V,n1,n2=d['E'],d['V'],d['n1'],d['n2']
    isl=(n1<=20)&(n2<=20); ed=(n1>34)|(n2>34)
    c=V.T@psi; QI=[]; QE=[]
    for t in ts:
        p=np.abs(V@(np.exp(-1j*E*t)*c))**2
        QI.append(1.0-p[isl].sum()); QE.append(p[ed].sum())
    del E,V,d; return np.array(QI),np.array(QE)
def rate(Q):
    L=np.mean(Q[ts>1e4]); ifr=np.where(Q>max(1e-12,1e-3*L))[0]
    lo=max(6.0,1.5*ts[ifr[0]]) if ifr.size else 6.0
    ihi=np.where(Q>=0.25*L)[0]; hi=min(200.0, ts[ihi[0]] if ihi.size else 200.0)
    m=(ts>=lo)&(ts<=hi)&(Q<=0.3*L)
    if m.sum()<5: return None,np.nan,np.nan
    A=np.polyfit(ts[m],Q[m],1)
    osc=np.std(Q[m]-np.polyval(A,ts[m]))/max(A[0]*(ts[m][-1]-ts[m][0]),1e-300)
    return A[0],osc,L
tests=[("coh s=0.30 (ref)",dict(kind='coh',s=0.30)),
       ("coh s=0.20",dict(kind='coh',s=0.20)),
       ("coh s=0.15",dict(kind='coh',s=0.15)),
       ("Fock |0,0>",dict(kind='fock00')),
       ("cut(0.30,n<=4)",dict(kind='cohcut',s=0.30,ncut=4)),
       ("cut(0.30,n<=2)",dict(kind='cohcut',s=0.30,ncut=2))]
print("SONDES DU PLANCHER  (surv + bord, N=72 ; N=64 pour |0,0> et s=0.20)")
print(f"  {'etat':<20}{'G_surv':<11}{'G_bord':<11}{'b/s':<7}{'osc':<7}{'plateau':<10}")
out={}
for name,kw in tests:
    psi=build_state(Nl=72,**kw)
    QI,QE=rate_curves('bq_72.npz',psi)
    gI,oI,L=rate(QI); gE,oE,_=rate(QE)
    out[name]=(gI,gE)
    print(f"  {name:<20}{gI:<11.2e}{gE:<11.2e}{(gE/gI):<7.2f}{oI:<7.2f}{L:<10.1e}")
print("\n  invariance de boite (N=64) :")
for name,kw in [("Fock |0,0>",dict(kind='fock00')),("coh s=0.20",dict(kind='coh',s=0.20))]:
    psi=build_state(Nl=64,**kw)
    QI,_=rate_curves('bq_64.npz',psi); g4,_,_=rate(QI)
    print(f"    {name:<18} G64={g4:.2e}   64/72 = {g4/out[name][0]:.2f}")
np.savez('tir1_plancher.npz',out={k:v for k,v in out.items()})
