import numpy as np
from scipy.special import gammaln
w1,w2=1.0,np.sqrt(2.0)
ts=np.unique(np.concatenate([np.linspace(1,20,10),np.geomspace(22,400,40),np.geomspace(450,2e4,30)]))
def coh1(al,Nl):
    n=np.arange(Nl); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def st(s,Nl): return np.kron(coh1(3*s*np.sqrt(w1/2),Nl),coh1(-2*s*np.sqrt(w2/2),Nl))
CACHE={}
def curves(tag,s):
    if (tag,s) in CACHE: return CACHE[(tag,s)]
    d=np.load(tag); E,V,n1,n2=d['E'],d['V'],d['n1'],d['n2']; Nl=int(np.sqrt(len(E)))
    isl=(n1<=20)&(n2<=20); ed=(n1>34)|(n2>34)
    c=V.T@st(s,Nl); QI=[]; QE=[]
    for t in ts:
        p=np.abs(V@(np.exp(-1j*E*t)*c))**2
        QI.append(1.0-p[isl].sum()); QE.append(p[ed].sum())
    del E,V,d
    CACHE[(tag,s)]=(np.array(QI),np.array(QE)); return CACHE[(tag,s)]
def rate(Q):
    L=np.mean(Q[ts>1e4])
    ifr=np.where(Q>max(1e-12,1e-3*L))[0]
    lo=max(6.0,1.5*ts[ifr[0]]) if ifr.size else 6.0
    ihi=np.where(Q>=0.25*L)[0]
    hi=min(200.0, ts[ihi[0]] if ihi.size else 200.0)
    m=(ts>=lo)&(ts<=hi)&(Q<=0.3*L)
    if m.sum()<5: return dict(g=None,L=L,n=int(m.sum()))
    A=np.polyfit(ts[m],Q[m],1); g=A[0]
    res=Q[m]-np.polyval(A,ts[m]); osc=np.std(res)/max(g*(ts[m][-1]-ts[m][0]),1e-300)
    tm=ts[m]; tmid=tm[len(tm)//2]; m1=m&(ts<tmid); m2=m&(ts>=tmid)
    hr=(np.polyfit(ts[m2],Q[m2],1)[0]/np.polyfit(ts[m1],Q[m1],1)[0]) if (m1.sum()>=3 and m2.sum()>=3) else np.nan
    return dict(g=g,L=L,n=int(m.sum()),hr=hr,osc=osc,lo=lo,hi=hi)
pred={0.45:(2.9e-6,4.0e-6,4.7e-6),0.40:(7.0e-7,1.3e-6,2.1e-6),
      0.35:(7.4e-8,3.1e-7,8.5e-7),0.30:(2.3e-9,4.5e-8,3.0e-7)}
anc={0.5:9.8e-6,0.7:9.8e-5}
print("ANCRES (estimateur front->quart-de-plateau, deux observables, N=72) :")
ok=True
for s,ref in anc.items():
    QI,QE=curves('bq_72.npz',s); rI=rate(QI); rE=rate(QE)
    print(f"  s={s}: surv G={rI['g']:.2e} (ratio {rI['g']/ref:.2f}, fen[{rI['lo']:.0f},{rI['hi']:.0f}], moit {rI['hr']:.2f}, osc {rI['osc']:.2f}) | bord G={rE['g']:.2e} (ratio {rE['g']/ref:.2f})")
    ok &= 0.7<rI['g']/ref<1.4 and 0.6<rE['g']/ref<1.7
print("  ->","ANCRES PASS\n" if ok else "ANCRES FAIL\n"); assert ok
print("TIR 1 -- points bas, tous gardes :")
print(f"  {'s':<6}{'G_surv72':<11}{'G_bord72':<11}{'b/s':<7}{'moit':<7}{'osc':<7}{'G_surv64':<11}{'64/72':<7}{'guards'}")
out={}
for s in (0.45,0.40,0.35,0.30):
    QI,QE=curves('bq_72.npz',s); rI=rate(QI); rE=rate(QE)
    QI4,_=curves('bq_64.npz',s); r4=rate(QI4)
    be=rE['g']/rI['g'] if (rI['g'] and rE['g']) else np.nan
    rN=r4['g']/rI['g'] if (rI['g'] and r4['g']) else np.nan
    gok=(rI['g'] is not None) and np.isfinite(be) and 0.4<be<2.5 and 0.5<rI['hr']<2.0 and rI['osc']<0.5 and np.isfinite(rN) and 0.6<rN<1.6
    out[s]=dict(g=rI['g'],ge=rE['g'],hr=rI['hr'],osc=rI['osc'],g64=r4['g'],ok=bool(gok))
    print(f"  {s:<6.2f}{rI['g']:<11.2e}{rE['g']:<11.2e}{be:<7.2f}{rI['hr']:<7.2f}{rI['osc']:<7.2f}{r4['g']:<11.2e}{rN:<7.2f}{'PASS' if gok else 'MARGINAL'}")
print("\nVERDICT vs predictions PRE-ENREGISTREES :")
for s in (0.45,0.40,0.35,0.30):
    r=out[s]
    if not r['ok']:
        print(f"  s={s}: guards marginaux -> BORNE seulement (G <~ {max(r['g'],r['ge']):.1e})"); continue
    B=np.exp(max(abs(np.log(r['ge']/r['g'])),abs(np.log(r['hr'])),abs(np.log(r['g64']/r['g'])))); lim=3*B
    vs=[]
    for p,name in zip(pred[s],("e^-b/s2","e^-b/s","s^p")):
        rat=r['g']/p; vs.append(f"{name}:{'OK' if 1/lim<rat<lim else 'EXCLU'}({rat:.2g}x)")
    print(f"  s={s}: G={r['g']:.2e}  B={B:.2f}  "+"  ".join(vs))
np.savez('tir1_final.npz',out={str(k):v for k,v in out.items()},pred=pred)
