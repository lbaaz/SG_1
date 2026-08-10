import numpy as np
from scipy.special import gammaln
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

w1,w2=1.0,np.sqrt(2.0); D=1.0; g=0.05
def build(N):
    a=np.zeros((N,N))
    for n in range(1,N): a[n-1,n]=np.sqrt(n)
    x1=(a+a.T)/np.sqrt(2*D*w1); x2=(a+a.T)/np.sqrt(2*D*w2)
    nv=np.arange(N); I=np.eye(N)
    X=np.kron(x1,I)+np.kron(I,x2)
    H0=np.kron(np.diag(-w1*nv),I)+np.kron(I,np.diag(w2*nv))
    X2=X@X; H=H0+(g/4.0)*(X2@X2); del X2
    return H,np.repeat(nv,N),np.tile(nv,N)
def coh(al,N):
    n=np.arange(N); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def psi0(s,N): return np.kron(coh(3*s*np.sqrt(w1/2),N),coh(-2*s*np.sqrt(w2/2),N))

sys={}
for N in [64,52]:
    H,n1,n2=build(N); E,V=np.linalg.eigh(H)
    sys[N]=(E,V,(n1+n2).astype(float),(n1>34)|(n2>34))   # bord PHYSIQUE commun n>34
    print(f"N={N} diag ok (dim {N*N})")

ts=np.linspace(0,120,160); svals=[0.6,1.0,1.3,1.6]
d=np.load('bocal_ab_data.npz'); gs=d['gs']; ssL=d['ssL']; tbA=d['tbA']
gi=np.argmin(np.abs(gs-0.05))
def tclas(s):
    si=np.argmin(np.abs(ssL-s)); v=tbA[gi,si]; return v
curves={}
print(f"\n  {'s':<5}{'t_conf (5%)':<12}{'max<N>/<N>0 (fenetre)':<23}{'fuite bord @t=15: N=52 / N=64':<32}{'t_blow classique'}")
for s in svals:
    r={}
    for N in [64,52]:
        E,V,nd,ed=sys[N]
        c=V.T@psi0(s,N); Nt=[];Ed=[]
        for t in ts:
            psi=V@(np.exp(-1j*E*t)*c); p=np.abs(psi)**2
            Nt.append(np.sum(nd*p)); Ed.append(np.sum(p[ed]))
        r[N]=(np.array(Nt),np.array(Ed))
    dv=np.abs(r[64][0]-r[52][0])/r[64][0][0]
    i=np.argmax(dv>0.05); ttr=ts[i] if i>0 else ts[-1]
    win=ts<=ttr
    ratio=(r[64][0]/r[64][0][0])[win].max()
    i15=np.argmin(np.abs(ts-15.0))
    l52,l64=r[52][1][i15],r[64][1][i15]
    tc=tclas(s); tcs=f"{tc:.0f}" if np.isfinite(tc) else ">400 (benin)"
    print(f"  {s:<5.1f}{ttr:<12.0f}{ratio:<23.2f}{l52:.1e} / {l64:.1e}{'  (ratio %.1f)'%(l52/max(l64,1e-30)):<12}{tcs}")
    curves[s]=(r,ttr)

# figure corrigee
bg='#0f1117'; fig,axes=plt.subplots(1,2,figsize=(13,5.2)); fig.patch.set_facecolor(bg)
for ax in axes:
    ax.set_facecolor(bg); ax.tick_params(colors='#999'); ax.grid(alpha=0.15)
    [sp.set_color('#555') for sp in ax.spines.values()]
cm=plt.cm.viridis(np.linspace(0.2,0.95,len(svals)))
ax=axes[0]
for c,s in zip(cm,svals):
    r,ttr=curves[s]
    ax.plot(ts,r[64][0]/r[64][0][0],color=c,lw=1.3,label=f"s={s} (N=64)")
    ax.plot(ts,r[52][0]/r[52][0][0],color=c,lw=1.0,ls=':',alpha=0.7)
    ax.axvline(ttr,color=c,ls='--',alpha=0.3)
ax.set_xlabel("t",color='#bbb'); ax.set_ylabel("⟨N⟩/⟨N⟩₀",color='#bbb')
ax.set_title("(a) Occupation, N=64 (plein) vs N=52 (pointillé)\ntirets verticaux : fin de fenêtre de confiance",color='#e8e8e8',fontsize=10.5)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=8)
ax=axes[1]
for c,s in zip(cm,svals):
    r,_=curves[s]
    ax.plot(ts,np.maximum(r[64][1],1e-16),color=c,lw=1.3,label=f"s={s} N=64")
    ax.plot(ts,np.maximum(r[52][1],1e-16),color=c,lw=1.0,ls=':',alpha=0.7)
ax.set_yscale('log'); ax.set_xlabel("t",color='#bbb'); ax.set_ylabel("population au-delà de n=34",color='#bbb')
ax.set_title("(b) Le flux de bord : artefact (dépend de N)\nou fuite physique (indépendant de N) ?",color='#e8e8e8',fontsize=10.5)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=8)
fig.suptitle("P1, manche sauvée — critère corrigé, bord physique commun (n>34), test d'artefact N=52 vs N=64",
             color='#f0f0f0',fontsize=12,y=1.02)
plt.tight_layout()
plt.savefig('bocal_quantum.png',dpi=130,facecolor=bg,bbox_inches='tight')
print("\nfigure corrigee sauvee : bocal_quantum.png")
