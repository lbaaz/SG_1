import numpy as np, os
from scipy.special import gammaln
w1,w2=1.0,np.sqrt(2.0); D=1.0; g=0.05
def build(N):
    a=np.zeros((N,N))
    for n in range(1,N): a[n-1,n]=np.sqrt(n)
    x1=(a+a.T)/np.sqrt(2*D*w1); x2=(a+a.T)/np.sqrt(2*D*w2)
    nv=np.arange(N); I=np.eye(N)
    X=np.kron(x1,I)+np.kron(I,x2)
    H=np.kron(np.diag(-w1*nv),I)+np.kron(I,np.diag(w2*nv))
    X=X@X; H+=(g/4.0)*(X@X); del X
    E,V=np.linalg.eigh(H); del H
    np.savez(f'bq_{N}.npz',E=E,V=V,n1=np.repeat(nv,N),n2=np.tile(nv,N))
def get(N):
    if not os.path.exists(f'bq_{N}.npz'): print(f"(re)build N={N}"); build(N)
    d=np.load(f'bq_{N}.npz'); return d['E'],d['V'],d['n1'],d['n2']
def coh(al,N):
    n=np.arange(N); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def psi0(s,N): return np.kron(coh(3*s*np.sqrt(w1/2),N),coh(-2*s*np.sqrt(w2/2),N))

print("="*74); print("K1a -- TEMPS LONG : saturation (fuite) ou retour (ballottement) ?"); print("="*74)
ts_long=np.unique(np.concatenate([np.linspace(1,40,20),np.geomspace(60,20000,50)]))
res={}
for N in [72,44]:
    E,V,n1,n2=get(N); ed=(n1>34)|(n2>34)
    for s in [0.6,0.9,1.2]:
        c=V.T@psi0(s,N); P=[]
        for t in ts_long:
            psi=V@(np.exp(-1j*E*t)*c); P.append(np.sum(np.abs(psi[ed])**2))
        P=np.array(P); res[(N,s)]=P
late=ts_long>1000
print(f"  {'':<10}{'P(40)':<11}{'P(1e3)':<11}{'P(1e4)':<11}{'P(2e4)':<11}{'min/max (t>1e3)':<17}{'moy t>1e3'}")
for s in [0.6,0.9,1.2]:
    for N in [72,44]:
        P=res[(N,s)]
        i40=np.argmin(np.abs(ts_long-40)); i1k=np.argmin(np.abs(ts_long-1e3)); i10k=np.argmin(np.abs(ts_long-1e4))
        rmm=P[late].min()/P[late].max(); moy=P[late].mean()
        print(f"  s={s} N={N:<3}{P[i40]:<11.2e}{P[i1k]:<11.2e}{P[i10k]:<11.2e}{P[-1]:<11.2e}{rmm:<17.2f}{moy:.2e}")
print("  lecture : fuite -> montee puis PLATEAU stable (min/max ~ 1), niveau plus HAUT a N=72")
print("            ballottement -> retours profonds (min/max << 1)\n")

print("="*74); print("K1b -- DEPLACEMENT DU BORD : flux traversant ou queue evanescente ?"); print("="*74)
N=72; E,V,n1,n2=get(N)
ncs=[26,30,34,38,42]; masks=[(n1>nc)|(n2>nc) for nc in ncs]
ts=np.linspace(0.5,40,80)
print(f"  {'s':<6}"+ "".join([f"G(nc={nc})   " for nc in ncs]))
G_nc={}
for s in [0.7,1.1]:
    c=V.T@psi0(s,N); Ps=[[] for _ in ncs]
    for t in ts:
        psi=V@(np.exp(-1j*E*t)*c); p=np.abs(psi)**2
        for i,m in enumerate(masks): Ps[i].append(np.sum(p[m]))
    row=f"  {s:<6.1f}"; gg=[]
    for i in range(len(ncs)):
        P=np.array(Ps[i]); m=(P>1e-11)&(P<0.02)
        sl=np.polyfit(ts[m],P[m],1)[0] if m.sum()>=6 else np.polyfit(ts[ts<=12],P[ts<=12],1)[0]
        gg.append(max(sl,1e-16)); row+=f"{gg[-1]:<12.1e}"
    G_nc[s]=gg; print(row)
    r=np.array(gg); print(f"         chute totale 26->42 : x{r[0]/r[-1]:.1f} ; par pas de 4 : x{(r[0]/r[-1])**0.25:.2f}")
np.savez('kill_k1.npz',ts_long=ts_long,res={f"{k[0]}_{k[1]}":v for k,v in res.items()},ncs=ncs,G07=G_nc[0.7],G11=G_nc[1.1])
print("\n  lecture : flux traversant -> G(nc) ~ plat (facteur <~3 sur toute la gamme)")
print("            queue evanescente -> effondrement exponentiel (x10+ par pas)")
