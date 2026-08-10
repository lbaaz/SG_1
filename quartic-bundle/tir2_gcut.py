import numpy as np
from scipy.special import gammaln
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
w1,w2=1.0,np.sqrt(2.0)
ts=np.unique(np.concatenate([np.linspace(1,20,10),np.geomspace(22,400,40),np.geomspace(450,2e4,30)]))
def coh1(al,Nl):
    n=np.arange(Nl); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def rate(Q):
    L=np.mean(Q[ts>1e4]); ifr=np.where(Q>max(1e-12,1e-3*L))[0]
    lo=max(6.0,1.5*ts[ifr[0]]) if ifr.size else 6.0
    ihi=np.where(Q>=0.25*L)[0]; hi=min(200.0, ts[ihi[0]] if ihi.size else 200.0)
    m=(ts>=lo)&(ts<=hi)&(Q<=0.3*L)
    if m.sum()<5: return None
    return np.polyfit(ts[m],Q[m],1)[0]
def meas(tag,states):
    d=np.load(tag); E,V,n1,n2=d['E'],d['V'],d['n1'],d['n2']
    isl=(n1<=20)&(n2<=20); ed=(n1>34)|(n2>34); res={}
    for name,psi in states.items():
        c=V.T@psi; QI=[]; QE=[]
        for t in ts:
            p=np.abs(V@(np.exp(-1j*E*t)*c))**2
            QI.append(1.0-p[isl].sum()); QE.append(p[ed].sum())
        res[name]=(rate(np.array(QI)),rate(np.array(QE)))
    del E,V,d; return res
def states72(s_list,fock00=True):
    st={}
    if fock00:
        v=np.zeros(72*72); v[0]=1.0; st['fock00']=v
    for s in s_list:
        st[f's{s}']=np.kron(coh1(3*s*np.sqrt(w1/2),72),coh1(-2*s*np.sqrt(w2/2),72))
    return st
print("PRE-ENREGISTRE : G0(0.025)=3.5e-7 et G0(0.0125)=8.8e-8 si g^2 ; 8.8e-8 / 5.5e-9 si g^4")
print("                 G(0.025, s=0.7) ~ 8-9e-7 si effondrement hbar^4.4 x F(K/K*) + G0\n")
print(f"  {'g':<9}{'etat':<10}{'G_surv':<11}{'G_bord':<11}{'b/s'}")
allr={}
for gv,tag in [(0.05,'bq_72.npz'),(0.025,'bq72_g0p025.npz'),(0.0125,'bq72_g0p0125.npz')]:
    r=meas(tag,states72([0.7]))
    allr[gv]=r
    for k,(gi,ge) in r.items():
        f=lambda v: f"{v:<11.2e}" if v is not None else f"{'--':<11}"
        print(f"  {gv:<9.4f}{k:<10}"+f(gi)+f(ge)+(f"{ge/gi:.2f}" if (gi and ge) else "--"))
G0=[(allr[g]['fock00'][0] if allr[g]['fock00'][0] is not None else np.nan) for g in (0.05,0.025,0.0125)]
print(f"\n  G0(g) : {G0[0]:.2e} -> {G0[1]:.2e} -> {G0[2]:.2e}")
print(f"  chutes : x{G0[0]/G0[1]:.2f} puis {(f'x{G0[1]/G0[2]:.2f}' if np.isfinite(G0[2]) else '-- (sous le seuil de detection de cette fenetre ; voir tir2_fin)')}   (g^2 attendait x4, x4 ; g^4 : x16, x16)")
gm=np.isfinite(G0); p_eff=np.polyfit(np.log(np.array([0.05,0.025,0.0125])[gm]),np.log(np.array(G0)[gm]),1)[0] if np.sum(gm)>=2 else np.nan
print(f"  exposant effectif G0 ~ g^{p_eff:.2f}  (sur les points detectes)")
Gs=[(allr[g]['s0.7'][0] if allr[g]['s0.7'][0] is not None else np.nan) for g in (0.05,0.025,0.0125)]
print(f"\n  G(g, s=0.7) : {Gs[0]:.2e} -> {Gs[1]:.2e} -> {Gs[2]:.2e}")
np.savez('tir2_gcut.npz',G0=G0,Gs07=Gs,gvals=[0.05,0.025,0.0125])
print("\n(figure de synthese : produite par tir2_fin.py -- version finale avec la borne a g=0.0125)")
