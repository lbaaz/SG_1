import numpy as np
from scipy.special import gammaln
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
w1,w2=1.0,np.sqrt(2.0); N=72
def coh(al):
    n=np.arange(N); lc=-0.5*abs(al)**2+n*np.log(abs(al)+1e-300)-0.5*gammaln(n+1)
    c=np.exp(lc)*np.exp(1j*n*np.angle(al)); return c/np.linalg.norm(c)
def psi0(s): return np.kron(coh(3*s*np.sqrt(w1/2)),coh(-2*s*np.sqrt(w2/2)))
chain=[(0.05,0.7),(0.025,0.98995),(0.0125,1.4)]
K3=[]
for gv,sv in chain:
    tag=f'bq72_g{gv}'.replace('.','p')
    d=np.load(tag+'.npz'); E,V,n1,n2=d['E'],d['V'],d['n1'],d['n2']
    ed=(n1>34)|(n2>34); c=V.T@psi0(sv); ts=np.linspace(0.5,40,80); P=[]
    for t in ts:
        psi=V@(np.exp(-1j*E*t)*c); P.append(np.sum(np.abs(psi[ed])**2))
    P=np.array(P); m=(P>1e-13)&(P<0.02)
    g_=max(np.polyfit(ts[m],P[m],1)[0],1e-18) if m.sum()>=6 else max(np.polyfit(ts,P,1)[0],1e-18)
    K3.append((gv,sv,g_,P[-1])); del E,V,d
print("K3 -- point classique FIXE (g s^2 = 0.0245), hbar_eff divise par 2 puis 4 :")
print(f"  {'g':<9}{'s':<9}{'1/hb_eff':<10}{'Gamma':<13}{'P_bord(40)'}")
for i,(gv,sv,g_,Pe) in enumerate(K3):
    print(f"  {gv:<9.4f}{sv:<9.3f}{2**i:<10}{g_:<13.2e}{Pe:.1e}")
r1=K3[0][2]/K3[1][2]; r2=K3[1][2]/max(K3[2][2],1e-18)
print(f"  chute hb -> hb/2  : x{r1:.1e}")
print(f"  chute hb/2 -> hb/4: x{r2:.1e}" + ("  (au plancher numerique -> borne inferieure)" if K3[2][2]<=2e-18 else ""))
np.savez('kill_k3.npz',K3=[(a,b,c) for a,b,c,_ in K3])

# figure de synthese
k1=np.load('kill_k1.npz',allow_pickle=True); k2=np.load('kill_k2.npz')
bg='#0f1117'; fig,axes=plt.subplots(1,3,figsize=(16.5,5.0)); fig.patch.set_facecolor(bg)
for ax in axes:
    ax.set_facecolor(bg); ax.tick_params(colors='#999'); ax.grid(alpha=0.15)
    [sp.set_color('#555') for sp in ax.spines.values()]
ax=axes[0]; ts=k1['ts_long']; res=k1['res'].item()
cm={0.6:'#4ec9b0',0.9:'#dcdcaa',1.2:'#f48771'}
for s in [0.6,0.9,1.2]:
    ax.loglog(ts,res[f'72_{s}'],color=cm[s],lw=1.3,label=f"s={s} (N=72)")
    ax.loglog(ts,res[f'44_{s}'],color=cm[s],lw=0.9,ls=':',alpha=0.8)
ax.set_xlabel("t",color='#bbb'); ax.set_ylabel("P(n>34)",color='#bbb')
ax.set_title("K1a — plateau sans retour (pointillé : N=44)",color='#e8e8e8',fontsize=10.5)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=8)
ax=axes[1]; ncs=k1['ncs']
ax.semilogy(ncs,k1['G07'],'o-',color='#4ec9b0',label='s=0.7')
ax.semilogy(ncs,k1['G11'],'s-',color='#f48771',label='s=1.1')
ax.semilogy([34,34],[k2['gt07'],k2['gh07']],'D',color='#dcdcaa',ms=7,label='K2 : dur vs doux')
ax.semilogy([34,34],[k2['gt11'],k2['gh11']],'D',color='#dcdcaa',ms=7)
ax.set_ylim(1e-6,1e-2); ax.set_xlabel("bord $n_c$",color='#bbb'); ax.set_ylabel("Γ",color='#bbb')
ax.set_title("K1b+K2 — flux traversant, robuste à la régularisation",color='#e8e8e8',fontsize=10.5)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=8)
ax=axes[2]; inv=[1,2,4]; gs3=[k[2] for k in K3]
ax.semilogy(inv,gs3,'o',color='#dcdcaa',ms=10,label='mesuré (point classique fixe)')
ax.semilogy(inv,[gs3[0]*(gs3[1]/gs3[0])**(x-1) for x in inv],'--',color='#4ec9b0',alpha=0.8,label='exponentiel en 1/ħ')
ax.semilogy(inv,[gs3[0]/x**3 for x in inv],':',color='#f48771',alpha=0.8,label='loi de puissance (ħ³)')
ax.set_xlabel("1/ħ_eff",color='#bbb'); ax.set_ylabel("Γ",color='#bbb')
ax.set_title("K3 — la signature ħ",color='#e8e8e8',fontsize=10.5)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=8)
fig.suptitle("Le kill : K1 fuite réelle — K2 robuste — K3 mécanisme",color='#f0f0f0',fontsize=12.5,y=1.02)
plt.tight_layout(); plt.savefig('bocal_kill.png',dpi=130,facecolor=bg,bbox_inches='tight')
print("figure : bocal_kill.png")
