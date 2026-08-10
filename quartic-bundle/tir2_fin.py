import numpy as np
from scipy.special import gammaln
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
w1,w2=1.0,np.sqrt(2.0)
ts=np.unique(np.concatenate([np.linspace(1,20,10),np.geomspace(22,400,40),np.geomspace(450,2e4,30)]))
def coh1(al,Nl):
    n=np.arange(Nl); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def rate_or_bound(Q):
    L=np.mean(Q[ts>1e4]); ifr=np.where(Q>max(1e-14,1e-3*L))[0]
    lo=max(6.0,1.5*ts[ifr[0]]) if ifr.size else 6.0
    ihi=np.where(Q>=0.25*L)[0]; hi=min(200.0, ts[ihi[0]] if ihi.size else 200.0)
    m=(ts>=lo)&(ts<=hi)&(Q<=0.3*L)
    if m.sum()>=5: return np.polyfit(ts[m],Q[m],1)[0], False
    mb=(ts>=6)&(ts<=2000)
    return max(np.max(Q[mb]/ts[mb]),1e-18), True   # borne sup honnete
d=np.load('bq72_g0p0125.npz'); E,V,n1,n2=d['E'],d['V'],d['n1'],d['n2']
isl=(n1<=20)&(n2<=20); ed=(n1>34)|(n2>34)
res={}
for name,psi in [('fock00',(lambda v: v)(np.eye(1,72*72,0).ravel())),
                 ('s0.7',np.kron(coh1(3*0.7*np.sqrt(w1/2),72),coh1(-2*0.7*np.sqrt(w2/2),72)))]:
    c=V.T@psi; QI=[]; QE=[]
    for t in ts:
        p=np.abs(V@(np.exp(-1j*E*t)*c))**2
        QI.append(1.0-p[isl].sum()); QE.append(p[ed].sum())
    gi,bi=rate_or_bound(np.array(QI)); ge,be=rate_or_bound(np.array(QE))
    res[name]=(gi,bi,ge,be)
    print(f"  g=0.0125 {name:<8}: surv {'<=' if bi else '='} {gi:.2e}   bord {'<=' if be else '='} {ge:.2e}")
del E,V,d
G0=[1.62e-6,1.02e-9,res['fock00'][0]]; G0b=[False,False,res['fock00'][1]]
Gs=[1.31e-4,1.75e-7,res['s0.7'][0]]
print(f"\n  G0 : 1.62e-6 -> 1.02e-9 ({'borne' if G0b[2] else 'val'}: {G0[2]:.1e})  |  chute mesuree x1590 ; si e^-c/g : c=0.37, predit G0(0.0125)~4e-16")
np.savez('tir2_final.npz',G0=G0,G0_borne=G0b,Gs07=Gs,gvals=[0.05,0.025,0.0125])
# figure
sv=np.array([0.15,0.20,0.30,0.35,0.40,0.45,0.5,0.7]); gm=np.array([1.42e-6,1.65e-6,2.49e-6,2.99e-6,4.13e-6,7.36e-6,1.25e-5,1.31e-4])
arch={0.5:9.8e-6,0.7:9.8e-5,0.9:7.1e-4,1.1:1.2e-3}
bg='#0f1117'; fig,ax=plt.subplots(1,2,figsize=(13,4.8)); fig.patch.set_facecolor(bg)
for a in ax:
    a.set_facecolor(bg); a.tick_params(colors='#999'); a.grid(alpha=0.15)
    [sp.set_color('#555') for sp in a.spines.values()]
a=ax[0]
a.loglog(sv,gm,'o-',color='#dcdcaa',ms=7,label='mesuré (protocole gardé)')
a.loglog(list(arch.keys()),list(arch.values()),'s',color='#4ec9b0',ms=6,alpha=0.7,label='archive K6')
sf=np.geomspace(0.14,0.8,100)
a.loglog(sf,9.8e-6*np.exp(-1.18*(1/sf**2-4)),':',color='#f48771',alpha=0.8,label='e^{-b/s²} (mort)')
a.loglog(sf,9.8e-6*(sf/0.5)**6.8,'--',color='#c586c0',alpha=0.8,label='s^p (mort)')
a.axhline(1.4e-6,color='#888',lw=0.8,ls='-.'); a.text(0.155,1.7e-6,'plancher Γ₀',color='#bbb',fontsize=8)
a.set_xlabel("s",color='#bbb'); a.set_ylabel("Γ",color='#bbb'); a.set_ylim(3e-7,3e-4)
a.set_title("Tir 1 — trois formes mortes, un plancher découvert",color='#e8e8e8',fontsize=10.5)
a.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=7.5)
a=ax[1]; gv=np.array([0.05,0.025])
a.loglog(gv,G0[:2],'o-',color='#dcdcaa',ms=8,label='Γ₀(g) mesuré')
a.errorbar([0.0125],[G0[2]],yerr=[[G0[2]*0.9],[0]],uplims=True,color='#dcdcaa',fmt='v',ms=8,label='borne (0.0125)')
gf=np.geomspace(0.011,0.06,50)
a.loglog(gf,1.62e-6*(gf/0.05)**2,'--',color='#4ec9b0',alpha=0.8,label='g² (mort ×400)')
a.loglog(gf,1.62e-6*(gf/0.05)**4,':',color='#f48771',alpha=0.8,label='g⁴ (mort ×100)')
a.loglog(gf,1.62e-6*np.exp(-0.369*(1/gf-20)),'-',color='#c586c0',alpha=0.7,lw=1,label='e^{-c/g}, c=0.37')
a.set_xlabel("g",color='#bbb'); a.set_ylabel("Γ₀",color='#bbb'); a.set_ylim(1e-17,1e-5)
a.set_title("Tir 2 — le plancher est NON-PERTURBATIF en g",color='#e8e8e8',fontsize=10.5)
a.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=7.5)
fig.suptitle("Γ(s,g) tranché : plancher fondamental non-perturbatif + excès résonant en loi de puissance",color='#f0f0f0',fontsize=11.5)
plt.tight_layout(); plt.savefig('bocal_tirs12.png',dpi=130,facecolor=bg,bbox_inches='tight')
print("figure : bocal_tirs12.png")
