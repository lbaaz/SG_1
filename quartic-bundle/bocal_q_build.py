import numpy as np, time
w1,w2=1.0,np.sqrt(2.0); D=w2**2-w1**2; g=0.05
def build(N):
    a=np.zeros((N,N))
    for n in range(1,N): a[n-1,n]=np.sqrt(n)
    x1=(a+a.T)/np.sqrt(2*D*w1); x2=(a+a.T)/np.sqrt(2*D*w2)
    nvec=np.arange(N); I=np.eye(N)
    X=np.kron(x1,I)+np.kron(I,x2)
    H0=np.kron(np.diag(-w1*nvec),I)+np.kron(I,np.diag(w2*nvec))
    X2=X@X; H=H0+(g/4.0)*(X2@X2); del X2
    n1=np.repeat(nvec,N); n2=np.tile(nvec,N)
    return H,X,n1,n2
t0=time.time()
for N in [44,36]:
    H,X,n1,n2=build(N)
    E,V=np.linalg.eigh(H)
    np.savez(f'bq_{N}.npz',E=E,V=V,X=(X if N==44 else np.zeros(1)),n1=n1,n2=n2)
    print(f"N={N} (dim {N*N}) : diag ok, E in [{E[0]:.1f},{E[-1]:.1f}], t={time.time()-t0:.0f}s")
