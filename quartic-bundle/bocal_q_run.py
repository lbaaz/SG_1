import numpy as np
from scipy.special import gammaln
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

w1,w2=1.0,np.sqrt(2.0); g=0.05
d44=np.load('bq_44.npz'); E,V,X,n1,n2=d44['E'],d44['V'],d44['X'],d44['n1'],d44['n2']
d36=np.load('bq_36.npz'); E4,V4,n1b,n2b=d36['E'],d36['V'],d36['n1'],d36['n2']
N=44; N4=36
ndiag=(n1+n2).astype(float); edge=(n1>38)|(n2>38)
ndiag4=(n1b+n2b).astype(float); edge4=(n1b>30)|(n2b>30)

def coherent(alpha,Nn):
    n=np.arange(Nn)
    lc=-0.5*abs(alpha)**2+n*np.log(abs(alpha)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(alpha)); return c/np.linalg.norm(c)
def psi0_of(s,Nn):
    return np.kron(coherent(3*s*np.sqrt(w1/2.0),Nn),coherent(-2*s*np.sqrt(w2/2.0),Nn))
def evolve(E,V,psi0,ts,ndiag,edge,Xop=None):
    c=V.T@psi0; Nt=[];Ed=[];Xt=[]
    for t in ts:
        psi=V@(np.exp(-1j*E*t)*c); p=np.abs(psi)**2
        Nt.append(np.sum(ndiag*p)); Ed.append(np.sum(p[edge]))
        if Xop is not None: Xt.append(np.real(np.vdot(psi,Xop@psi)))
    return np.array(Nt),np.array(Ed),(np.array(Xt) if Xop is not None else None)

svals=[0.6,0.9,1.1,1.2,1.3,1.4,1.6]; ts=np.linspace(0,300,200)
res={}
print(f"  {'s':<6}{'<N>_0':<8}{'max<N>/<N>0':<13}{'pop bord':<11}{'verdict quantique':<22}{'classique (grille)'}")
cl={0.6:'benin',0.9:'benin',1.1:'benin',1.2:'benin',1.3:'MALIN',1.4:'MALIN',1.6:'MALIN'}
for s in svals:
    Nt,Ed,_=evolve(E,V,psi0_of(s,N),ts,ndiag,edge)
    N0=Nt[0]; r=Nt/N0; mal=(Ed.max()>1e-3)or(r.max()>3.0)
    tq=ts[np.argmax((Ed>1e-3)|(r>3.0))] if mal else np.inf
    res[s]=(Nt,Ed,N0,mal,tq)
    print(f"  {s:<6.1f}{N0:<8.1f}{r.max():<13.2f}{Ed.max():<11.1e}{('MALIN t~%.0f'%tq) if mal else 'benin':<22}{cl[s]}")

# Ehrenfest s=0.8
ts2=np.linspace(0,60,400)
_,_,Xq=evolve(E,V,psi0_of(0.8,N),ts2,ndiag,edge,Xop=X)
def classical(s,T,dt=0.002):
    W2=(w1*w2)**2;P2=w1**2+w2**2;y=np.array([s,0,0,s]);n=int(T/dt);out=np.empty(n)
    def f(y):
        q1,q2,p1,p2=y
        return np.array([q2,p2,W2*q1-g*q1**3,-p1-P2*q2])
    for i in range(n):
        k1=f(y);k2=f(y+dt/2*k1);k3=f(y+dt/2*k2);k4=f(y+dt*k3);y=y+dt/6*(k1+2*k2+2*k3+k4);out[i]=y[0]
    return np.arange(n)*dt,out
tc,xc=classical(0.8,60)

# troncature s=1.3
Nt4,Ed4,_=evolve(E4,V4,psi0_of(1.3,N4),ts,ndiag4,edge4)
Nt6=res[1.3][0]
dv=np.abs(Nt4-Nt6)/Nt6[0]; i=np.argmax(dv>0.05); tdiv=ts[i] if i>0 else ts[-1]
print(f"\n  controle troncature (s=1.3) : accord N=36/N=44 a 5% jusqu'a t~{tdiv:.0f}")

bg='#0f1117'; fig,axes=plt.subplots(1,3,figsize=(17,5.2)); fig.patch.set_facecolor(bg)
for ax in axes:
    ax.set_facecolor(bg); ax.tick_params(colors='#999'); ax.grid(alpha=0.15)
    [sp.set_color('#555') for sp in ax.spines.values()]
ax=axes[0]
ax.plot(tc,xc,color='#dcdcaa',lw=1.0,label='classique x(t)')
ax.plot(ts2,Xq,'--',color='#4ec9b0',lw=1.1,label='quantique ⟨x⟩(t)')
ax.set_xlabel("t",color='#bbb'); ax.set_ylabel("x",color='#bbb')
ax.set_title("(a) Ehrenfest, s=0.8 : accord puis étalement",color='#e8e8e8',fontsize=11)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=8)
ax=axes[1]
cm=plt.cm.viridis(np.linspace(0.15,0.95,len(svals)))
for c,s in zip(cm,svals):
    Nt,Ed,N0,mal,tq=res[s]
    ax.plot(ts,Nt/N0,color=c,lw=1.2,label=f"s={s}"+(" ✗" if mal else ""))
ax.plot(ts,Nt4/Nt4[0],':',color='#f48771',lw=1.2,label='s=1.3, N=36 (contrôle)')
ax.axhline(3.0,color='#f48771',ls='--',alpha=0.5)
ax.set_yscale('log'); ax.set_xlabel("t",color='#bbb'); ax.set_ylabel("⟨N⟩/⟨N⟩₀",color='#bbb')
ax.set_title("(b) Occupation : bénin vs fuite quantique",color='#e8e8e8',fontsize=11)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=7,ncol=2)
ax=axes[2]
sm=[s for s in svals if res[s][3]]; sb=[s for s in svals if not res[s][3]]
ax.scatter(sb,[300]*len(sb),color='#4ec9b0',s=80,label='bénin (t>300)')
if sm: ax.scatter(sm,[res[s][4] for s in sm],color='#f48771',s=80,label='malin (t de fuite)')
ax.axvline(1.27,color='#dcdcaa',ls='--',label='frontière classique s*=1.27')
ax.set_xlabel("amplitude s",color='#bbb'); ax.set_ylabel("t de fuite quantique",color='#bbb')
ax.set_title("(c) Frontière quantique vs classique",color='#e8e8e8',fontsize=11)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=8)
fig.suptitle("P1 — le fantôme PU en interaction, quantifié exactement (hermitien indéfini, dim 1936, contrôle 1296)",
             color='#f0f0f0',fontsize=12.5,y=1.02)
plt.tight_layout()
plt.savefig('bocal_quantum.png',dpi=130,facecolor=bg,bbox_inches='tight')
print("figure sauvee : bocal_quantum.png")
