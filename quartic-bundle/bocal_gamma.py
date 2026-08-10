import numpy as np
from scipy.special import gammaln

w1,w2=1.0,np.sqrt(2.0); D=1.0; g=0.05
def build(N):
    a=np.zeros((N,N))
    for n in range(1,N): a[n-1,n]=np.sqrt(n)
    x1=(a+a.T)/np.sqrt(2*D*w1); x2=(a+a.T)/np.sqrt(2*D*w2)
    nv=np.arange(N); I=np.eye(N)
    X=np.kron(x1,I)+np.kron(I,x2)
    H0=np.kron(np.diag(-w1*nv),I)+np.kron(I,np.diag(w2*nv))
    X2=X@X; H=H0+(g/4.0)*(X2@X2); del X2,X
    n1=np.repeat(nv,N); n2=np.tile(nv,N)
    return H,n1,n2
def coh(al,N):
    n=np.arange(N); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)

sysd={}
for N in [80,56]:
    H,n1,n2=build(N); E,V=np.linalg.eigh(H)
    sysd[N]=(E,V,(n1>34)|(n2>34)); del H
    print(f"N={N} (dim {N*N}) diag ok")

ts=np.linspace(0.5,40.0,100); svals=[0.5,0.7,0.9,1.1,1.3,1.5]
d=np.load('bocal_ab_data.npz'); gs=d['gs']; ssL=d['ssL']; tbA=d['tbA']; gi=np.argmin(np.abs(gs-0.05))
def tclas(s):
    si=np.argmin(np.abs(ssL-s)); v=tbA[gi,si]
    return f"{v:.0f}" if np.isfinite(v) else "inf"
def gamma_of(P,ts):
    m=(P>1e-8)&(P<0.02)
    if m.sum()>=6: sl=np.polyfit(ts[m],P[m],1)[0]
    else:
        m=ts<=12.0; sl=np.polyfit(ts[m],P[m],1)[0]
    return max(sl,1e-14)
print(f"\n  {'s':<6}{'Gamma N=56':<13}{'Gamma N=80':<13}{'ratio':<8}{'tau=1/G':<11}{'t_blow class.'}")
G80=[]
for s in svals:
    Gs={}
    for N in [80,56]:
        E,V,ed=sysd[N]
        psi0=np.kron(coh(3*s*np.sqrt(w1/2),N),coh(-2*s*np.sqrt(w2/2),N))
        c=V.T@psi0; P=[]
        for t in ts:
            psi=V@(np.exp(-1j*E*t)*c); P.append(np.sum(np.abs(psi[ed])**2))
        Gs[N]=gamma_of(np.array(P),ts)
    G80.append(Gs[80])
    print(f"  {s:<6.1f}{Gs[56]:<13.2e}{Gs[80]:<13.2e}{Gs[56]/Gs[80]:<8.2f}{1/Gs[80]:<11.1e}{tclas(s)}")
G80=np.array(G80); sv=np.array(svals); lg=np.log(G80)
fits={}
for name,xf in [("ln G = a - b/s^2",1/sv**2),("ln G = a - b/s",1/sv),("ln G = a + b ln s",np.log(sv))]:
    A=np.vstack([np.ones_like(xf),xf]).T
    coef,res,_,_=np.linalg.lstsq(A,lg,rcond=None)
    pred=A@coef; R2=1-np.sum((lg-pred)**2)/np.sum((lg-lg.mean())**2)
    fits[name]=(coef,R2)
    print(f"  {name:<22} : a={coef[0]:+.2f}, b={coef[1]:+.2f}, R^2={R2:.4f}")
best=max(fits,key=lambda k:fits[k][1])
print(f"\n  meilleur ansatz : {best}")
np.savez('bocal_gamma.npz',svals=sv,G80=G80,ts=ts)
