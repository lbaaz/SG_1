import numpy as np
from scipy.special import gammaln
w1,w2=1.0,np.sqrt(2.0); N=72
d=np.load('bq_72.npz'); E,V,n1,n2=d['E'],d['V'],d['n1'],d['n2']
ed=(n1>34)|(n2>34); isl=(n1<=20)&(n2<=20)
def coh1(al):
    n=np.arange(N); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def st(s): return np.kron(coh1(3*s*np.sqrt(w1/2)),coh1(-2*s*np.sqrt(w2/2)))
ts=np.concatenate([np.linspace(0.25,24,144),np.linspace(26,48,8)])
# tclas : integration directe au point exact (erratum : l'ancienne version lisait
# bocal_ab_data au plus proche voisin -- g=0.0516, s=1.333... -- en zone frontaliere fractale)
def tclas(s,T=400.0,dt=0.006,blow=1e4):
    P2c,W2c=w1*w1+w2*w2,(w1*w2)**2; g=0.05
    def fc(y):
        q1,q2,p1,p2=y
        return np.array([q2,p2,W2c*q1-g*q1**3,-p1-P2c*q2])
    y=np.array([s,0.0,0.0,s])
    for i in range(int(T/dt)):
        k1=fc(y);k2=fc(y+0.5*dt*k1);k3=fc(y+0.5*dt*k2);k4=fc(y+dt*k3)
        y=y+(dt/6.0)*(k1+2*k2+2*k3+k4)
        if np.max(np.abs(y))>blow: return f"{(i+1)*dt:.0f}"
    return "inf"
print("="*78)
print("K6 -- TAUX UNIFORMES, IMMUNISES AU FRONT (bord adaptatif + survie insulaire)")
print("="*78)
print(f"  {'s':<6}{'G_bord(adapt)':<15}{'G_ile(decroiss.)':<17}{'accord':<8}{'tau_ile':<10}{'t_blow cl.'}")
res=[]
for s in [0.5,0.7,0.9,1.1,1.2,1.3,1.4,1.5,1.6]:
    c=V.T@st(s); Pe=[]; Pi=[]
    for t in ts:
        psi=V@(np.exp(-1j*E*t)*c); p=np.abs(psi)**2
        Pe.append(p[ed].sum()); Pi.append(p[isl].sum())
    Pe=np.array(Pe); Pi=np.array(Pi)
    # bord adaptatif : apres le front, avant saturation
    ge=np.nan
    ifr=np.where(Pe>1e-6)[0]
    if ifr.size:
        t0=ts[ifr[0]]+4.0; m=(ts>=t0)&(Pe<0.05)
        if m.sum()>=8: ge=np.polyfit(ts[m],Pe[m],1)[0]
    # survie insulaire : exponentielle si assez de decroissance, sinon pente de (1-P_I)
    mi=(Pi<0.95)&(Pi>0.45)&(ts>=0.5)
    if mi.sum()>=6: gi_=-np.polyfit(ts[mi],np.log(Pi[mi]),1)[0]
    else:
        m2=(ts>=2)&(ts<=24); gi_=np.polyfit(ts[m2],1.0-Pi[m2],1)[0]
    acc=f"{ge/gi_:.2f}" if np.isfinite(ge) and gi_>0 else "--"
    res.append((s,ge,gi_))
    print(f"  {s:<6.1f}{(f'{ge:.2e}' if np.isfinite(ge) else '--'):<15}{gi_:<17.2e}{acc:<8}{1/gi_:<10.1e}{tclas(s)}")
mono=all(res[i][2]<=res[i+1][2]*1.05 for i in range(len(res)-1))
print(f"\n  monotonie de G_ile(s) : {'OUI (la non-monotonie etait l artefact de fenetre)' if mono else 'NON -- structure reelle a examiner'}")
np.savez('kill_k6.npz',res=np.array(res))

print()
print("="*78)
print("K5b -- LE COEFFICIENT C : re-fit avec barre d erreur, test des formes pures")
print("="*78)
try:
    dp=np.load('bocal_paysage.npz'); print("  cles paysage :",dp.files)
    # heuristique : trouver le tableau des omega2 et des s*
    keys=dp.files
    om=None; sst=None
    for k in keys:
        a=dp[k]
        if a.ndim==1 and a.size>=8:
            if om is None and a.min()>1.0 and a.max()<=4.0: om=a; continue
            if sst is None: sst=a
    if om is not None and sst is not None and om.size==sst.size:
        mask=(((om>=1.25)&(om<=1.5))|((om>=2.75)&(om<=3.25)))&np.isfinite(sst)
        K=0.05*sst[mask]**2; x=(om[mask]-1.0)**2*(1.0+om[mask])
        C=K/x
        print(f"  points de bord utilises : {mask.sum()}")
        print(f"  C = {C.mean():.4f} +/- {C.std():.4f}  (min {C.min():.3f}, max {C.max():.3f})")
        for name,val in [("1/4",0.25),("3/(4pi)",3/(4*np.pi)),("1/(2e)",1/(2*np.e)),("0.254 (fit v1)",0.254)]:
            z=(C.mean()-val)/max(C.std(),1e-9)
            print(f"    {name:<16}= {val:.4f} : ecart {z:+.1f} sigma")
        print(f"  forme fermee candidate si C=1/4 : g s*^2 = (w2-w1)^2 (w1+w2)/4 = Delta^2/(4(w1+w2))")
    else:
        print("  introspection paysage : structure non reconnue -- refit saute (donnees dans le npz)")
except Exception as e:
    print("  paysage indisponible :",e)
