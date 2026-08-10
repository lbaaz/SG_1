import numpy as np, os, sys, time
w1,w2=1.0,np.sqrt(2.0); D=1.0; N=72
gv=float(sys.argv[1]); tag=f'bq72_g{gv}'.replace('.','p')
if os.path.exists(tag+'.npz'): print(tag,"deja la"); sys.exit()
t0=time.time()
a=np.zeros((N,N))
for n in range(1,N): a[n-1,n]=np.sqrt(n)
x1=(a+a.T)/np.sqrt(2*D*w1); x2=(a+a.T)/np.sqrt(2*D*w2)
nv=np.arange(N); I=np.eye(N)
X=np.kron(x1,I)+np.kron(I,x2)
H=np.kron(np.diag(-w1*nv),I)+np.kron(I,np.diag(w2*nv))
X=X@X          # x^2
H+=(gv/4.0)*(X@X); del X
E,V=np.linalg.eigh(H); del H
np.savez(tag+'.npz',E=E,V=V,n1=np.repeat(nv,N),n2=np.tile(nv,N))
print(f"{tag} ok ({time.time()-t0:.0f}s)")
