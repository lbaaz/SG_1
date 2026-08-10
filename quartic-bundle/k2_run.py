import numpy as np
from scipy.special import gammaln
w1,w2=1.0,np.sqrt(2.0); D=1.0; N=64; g=0.05
def coh(al):
    n=np.arange(N); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def psi0(s): return np.kron(coh(3*s*np.sqrt(w1/2)),coh(-2*s*np.sqrt(w2/2)))
def gam(E,V,n1,n2,s,nc=34):
    ed=(n1>nc)|(n2>nc); c=V.T@psi0(s); ts=np.linspace(0.5,40,80); P=[]
    for t in ts:
        psi=V@(np.exp(-1j*E*t)*c); P.append(np.sum(np.abs(psi[ed])**2))
    P=np.array(P); m=(P>1e-11)&(P<0.02)
    return max(np.polyfit(ts[m],P[m],1)[0],1e-18) if m.sum()>=6 else max(np.polyfit(ts,P,1)[0],1e-18)
# mur dur (cache)
d=np.load('bq_64.npz'); Eh,Vh,n1,n2=d['E'],d['V'],d['n1'],d['n2']
gh={s:gam(Eh,Vh,n1,n2,s) for s in (0.7,1.1)}
del Eh,Vh,d
# capuchon doux
a=np.zeros((N,N))
for n in range(1,N): a[n-1,n]=np.sqrt(n)
x1=(a+a.T)/np.sqrt(2*D*w1); x2=(a+a.T)/np.sqrt(2*D*w2)
nv=np.arange(N); I=np.eye(N)
X=np.kron(x1,I)+np.kron(I,x2)
H=np.kron(np.diag(-w1*nv),I)+np.kron(I,np.diag(w2*nv))
F=(1.0/(1.0+np.exp((np.maximum(n1,n2)-48.0)/3.0)))
X=X@X; X=X@X                      # x^4
H+=(g/4.0)*(F[:,None]*X*F[None,:]); del X
Et,Vt=np.linalg.eigh(H); del H
gt={s:gam(Et,Vt,n1,n2,s) for s in (0.7,1.1)}
print("K2 -- mur dur vs capuchon doux (quartique eteint au-dela de n~48) :")
print(f"  {'s':<6}{'G dur':<13}{'G doux':<13}{'ratio dur/doux'}")
for s in (0.7,1.1):
    print(f"  {s:<6.1f}{gh[s]:<13.2e}{gt[s]:<13.2e}{gh[s]/gt[s]:.2f}")
np.savez('kill_k2.npz',gh07=gh[0.7],gt07=gt[0.7],gh11=gh[1.1],gt11=gt[1.1])
