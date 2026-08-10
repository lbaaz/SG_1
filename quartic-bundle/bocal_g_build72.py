import numpy as np, time
w1,w2=1.0,np.sqrt(2.0); D=1.0; g=0.05
N=72
t0=time.time()
a=np.zeros((N,N))
for n in range(1,N): a[n-1,n]=np.sqrt(n)
x1=(a+a.T)/np.sqrt(2*D*w1); x2=(a+a.T)/np.sqrt(2*D*w2)
nv=np.arange(N); I=np.eye(N)
X=np.kron(x1,I)+np.kron(I,x2)
H=np.kron(np.diag(-w1*nv),I)+np.kron(I,np.diag(w2*nv))
X=X@X          # X devient x^2
H+= (g/4.0)*(X@X); del X
print(f"H construit ({time.time()-t0:.0f}s)")
E,V=np.linalg.eigh(H); del H
print(f"diag ok ({time.time()-t0:.0f}s), E in [{E[0]:.1f},{E[-1]:.1f}]")
np.savez('bq_72.npz',E=E,V=V,n1=np.repeat(nv,N),n2=np.tile(nv,N))
print(f"cache bq_72.npz ecrit ({time.time()-t0:.0f}s)")
