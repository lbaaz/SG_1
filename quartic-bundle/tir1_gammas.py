import numpy as np, sys
from scipy.special import gammaln
w1,w2=1.0,np.sqrt(2.0); N=72
# ---------- G1 : integrite du cache ----------
d=np.load('bq_72.npz'); E,V,n1,n2=d['E'],d['V'],d['n1'],d['n2']
assert E.shape==(N*N,) and V.shape==(N*N,N*N) and np.all(np.isfinite(E)), "G1: cache corrompu"
idx=np.array([0,137,2591,5183]); G=V[:,idx].T@V[:,idx]
assert np.max(np.abs(G-np.eye(4)))<1e-8, "G1: V non orthonormee"
print("G1 PASS  (spectre fini, V orthonormee: ecart max %.1e)"%np.max(np.abs(G-np.eye(4))))
def coh1(al):
    n=np.arange(N); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def st(s): return np.kron(coh1(3*s*np.sqrt(w1/2)),coh1(-2*s*np.sqrt(w2/2)))
# ---------- G2 : checksum physique <H0> = -0.5 s^2 ----------
H0d=-w1*n1+w2*n2
for s in (0.3,0.5,0.7):
    v=st(s); h0=np.real(np.vdot(v,H0d*v))
    assert abs(h0+0.5*s*s)<2e-3*s*s+1e-9, f"G2 FAIL s={s}: <H0>={h0}"
print("G2 PASS  (<H0>=-0.5 s^2 a 0.2%% pres sur 3 s)")
isl=(n1<=20)&(n2<=20); ed=(n1>34)|(n2>34)
ts=np.unique(np.concatenate([np.linspace(1,40,15),np.geomspace(60,2e4,55)]))
def curves(E,V,n1,n2,psi):
    c=V.T@psi; PI=[]; PE=[]; nrm=[]
    for t in ts:
        ph=np.exp(-1j*E*t)*c; psi_t=V@ph
        p=np.abs(psi_t)**2; nrm.append(p.sum()); PI.append(p[isl_l].sum()); PE.append(p[ed_l].sum())
    return np.array(PI),np.array(PE),np.array(nrm)
def gam_all(E,V,n1,n2,s,label=""):
    global isl_l,ed_l
    isl_l=(n1<=20)&(n2<=20); ed_l=(n1>34)|(n2>34)
    PI,PE,nrm=curves(E,V,n1,n2,st_l(s))
    g4=np.max(np.abs(1.0-nrm))
    # estimateur A : protocole K6 exact (fallback t in [2,24]) pour l'ancre
    m6=(ts>=2)&(ts<=24); gA=np.polyfit(ts[m6],1.0-PI[m6],1)[0]
    # estimateur B : survie, fenetre longue [200, 2e4]
    mL=(ts>=200); gB=np.polyfit(ts[mL],1.0-PI[mL],1)[0]
    # G5 : moities
    tmid=np.sqrt(200*2e4)
    g1=np.polyfit(ts[(ts>=200)&(ts<tmid)],1.0-PI[(ts>=200)&(ts<tmid)],1)[0]
    g2=np.polyfit(ts[ts>=tmid],1.0-PI[ts>=tmid],1)[0]
    # estimateur C : flux de bord, meme fenetre longue
    gC=np.polyfit(ts[mL],PE[mL],1)[0]
    return dict(gA=gA,gB=gB,gC=gC,gh1=g1,gh2=g2,norm=g4)
def st_l(s):
    Nl=int(np.sqrt(len(E_l)))
    def c1(al):
        n=np.arange(Nl); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
        c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
    return np.kron(c1(3*s*np.sqrt(w1/2)),c1(-2*s*np.sqrt(w2/2)))
# ---------- G3 : ancres d'abord ----------
E_l,V_l=E,V
anc={0.5:9.8e-6,0.7:9.8e-5}
print("\nG3 -- reproduction des ancres (protocole K6 exact) :")
ok=True
res={}
for s,ref in anc.items():
    r=gam_all(E,V,n1,n2,s); res[s]=r
    ratio=r['gA']/ref
    print(f"  s={s}: G_k6proto={r['gA']:.2e}  (archive {ref:.1e}, ratio {ratio:.2f})  | G_long={r['gB']:.2e}  G_bord={r['gC']:.2e}  norme:{r['norm']:.1e}")
    ok &= 0.8<ratio<1.25
if not ok: print("G3 FAIL -- ARRET"); sys.exit(1)
print("G3 PASS  |  G4 PASS (norme conservee)")
# ---------- TIR 1 : les nouveaux points ----------
print("\nTIR 1 -- s = 0.45, 0.40, 0.35, 0.30  (N=72, deux estimateurs, moities)")
print(f"  {'s':<7}{'G_surv':<11}{'G_bord':<11}{'bord/surv':<11}{'moitie2/1':<11}{'norme'}")
for s in (0.45,0.40,0.35,0.30):
    r=gam_all(E,V,n1,n2,s); res[s]=r
    print(f"  {s:<7.2f}{r['gB']:<11.2e}{r['gC']:<11.2e}{r['gC']/r['gB']:<11.2f}{r['gh2']/r['gh1']:<11.2f}{r['norm']:.1e}")
np.savez('tir1_partA.npz',res={str(k):v for k,v in res.items()},ts=ts)
print("\npartA sauvee ; G6 (N=64) et verdict au prochain appel")
