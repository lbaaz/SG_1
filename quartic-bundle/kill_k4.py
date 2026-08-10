import numpy as np
from scipy.linalg import expm
from scipy.special import gammaln
w1,w2=1.0,np.sqrt(2.0); N=72
d=np.load('bq_72.npz'); E,V,n1,n2=d['E'],d['V'],d['n1'],d['n2']
ed=(n1>34)|(n2>34)
a=np.zeros((N,N))
for n in range(1,N): a[n-1,n]=np.sqrt(n)
e0=np.zeros(N); e0[0]=1.0
def coh1(al): 
    n=np.arange(N); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def sqcoh1(al,r):
    S=expm(0.5*r*(a@a-a.T@a.T)); D=expm(al*a.T-np.conj(al)*a)
    v=D@(S@e0); return v/np.linalg.norm(v)
def st_coh(s): return np.kron(coh1(3*s*np.sqrt(w1/2)),coh1(-2*s*np.sqrt(w2/2)))
def st_sq(s,r): return np.kron(sqcoh1(3*s*np.sqrt(w1/2),r),sqcoh1(-2*s*np.sqrt(w2/2),r))
def st_cut(s,ncut):
    psi=st_coh(s); m=(n1<=ncut)&(n2<=ncut); psi=psi*m
    return psi/np.linalg.norm(psi)
def st_fock(m1,m2):
    v=np.zeros(N*N); v[m1*N+m2]=1.0; return v
def gam(psi0):
    P0=np.sum(np.abs(psi0[ed])**2)
    c=V.T@psi0; ts=np.linspace(0.5,40,80); P=[]
    for t in ts:
        psi=V@(np.exp(-1j*E*t)*c); P.append(np.sum(np.abs(psi[ed])**2))
    P=np.array(P); m=(P>1e-13)&(P<0.02)
    g=np.polyfit(ts[m],P[m],1)[0] if m.sum()>=6 else np.polyfit(ts,P,1)[0]
    return max(g,1e-16),P0

print("="*74)
print("K4 -- FAMILLES D'ETATS (rivage classique : s*=1.27 <-> n1*~7.3, n2*~2.2)")
print("="*74)
g07,_=gam(st_coh(0.7)); g11,_=gam(st_coh(1.1))
rows=[("coherent s=0.7 (ref)",st_coh(0.7),g07),
      ("squeeze r=+0.4 (radial-)",st_sq(0.7,0.4),g07),
      ("squeeze r=+0.7 (radial--)",st_sq(0.7,0.7),g07),
      ("squeeze r=-0.4 (controle+)",st_sq(0.7,-0.4),g07),
      ("coupe n<=12  s=0.7",st_cut(0.7,12),g07),
      ("coupe n<=8   s=0.7 (=rivage)",st_cut(0.7,8),g07),
      ("Fock |2,1>",st_fock(2,1),g07),
      ("Fock |4,2>",st_fock(4,2),g07),
      ("Fock |7,3> (rivage)",st_fock(7,3),g07),
      ("coherent s=1.1 (ref)",st_coh(1.1),g11),
      ("coupe n<=16  s=1.1",st_cut(1.1,16),g11)]
print(f"  {'etat':<30}{'P0(n>34)':<11}{'Gamma':<12}{'ratio/ref'}")
out={}
for name,psi,ref in rows:
    g,P0=gam(psi); out[name]=g
    print(f"  {name:<30}{P0:<11.1e}{g:<12.2e}{g/ref:.2f}")
print("\n  lecture : queues coupables -> effondrement de Gamma pour coupes/squeeze")
print("            ile qui fuit     -> meme ordre partout, anti-squeeze un peu au-dessus\n")

print("="*74)
print("K4-E -- RECENSEMENT SPECTRAL : existe-t-il des etats propres lies dans l'ile ?")
print("="*74)
mI=(n1<=10)&(n2<=10); mIn=~ed
wI=(V[mI,:]**2).sum(axis=0)
wE=1.0-(V[mIn,:]**2).sum(axis=0)   # poids au-dela du bord n=34
sel=wI>0.5
print(f"  etats propres a poids insulaire >0.5 : {sel.sum()} / {N*N}")
if sel.sum():
    w=wE[sel]
    print(f"  poids oceanique (n>34) de ces etats : min={w.min():.1e}  mediane={np.median(w):.1e}  max={w.max():.1e}")
    print(f"  nombre avec poids oceanique < 1e-12 (lies numeriquement) : {(w<1e-12).sum()}")
    print(f"  nombre avec poids oceanique < 1e-9  : {(w<1e-9).sum()}")
np.savez('kill_k4.npz',gammas=list(out.values()),names=list(out.keys()),wI=wI[sel],wE=wE[sel])
print("\n  lecture : 0 etat lie -> la fuite est STRUCTURELLE (aucun etat de l'ile n'y echappe)")
print("            des etats lies existent -> des etats insulaires immortels existent, claim a rescoper")
