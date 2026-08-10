import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---- scan du paysage s*(w2) a g=0.05, w1=1 ----
def scan_col(w2v,gval,ss,T=400.0,dt=0.006,thresh=1e4,w1v=1.0):
    n=len(ss); W2=(w1v*w2v)**2; P2=w1v**2+w2v**2
    y=np.zeros((4,n)); y[0]=ss; y[3]=ss
    tb=np.full(n,np.inf); alive=np.ones(n,bool); t=0.0
    def f(y):
        q1,q2,p1,p2=y
        return np.array([q2,p2,W2*q1-gval*q1**3,-p1-P2*q2])
    for i in range(int(T/dt)):
        k1=f(y);k2=f(y+dt/2*k1);k3=f(y+dt/2*k2);k4=f(y+dt*k3)
        yn=y+dt/6*(k1+2*k2+2*k3+k4)
        bad=alive&(np.max(np.abs(yn),axis=0)>thresh); tb[bad]=t; alive&=~bad
        yn[:,~alive]=0.0; y=np.where(np.isfinite(yn),yn,0.0); t+=dt
    idx=np.where(~np.isinf(tb))[0]
    return ss[idx[0]] if idx.size else np.nan

w2s=np.linspace(1.25,3.25,41); g=0.05; ss=np.linspace(0.2,12.0,60)
print("scan du paysage s*(w2)..."); sstar=np.array([scan_col(w,g,ss) for w in w2s])
C=0.254
law=np.sqrt(C*(w2s-1.0)**2*(1.0+w2s)/g)
for w,sv,lv in zip(w2s[::5],sstar[::5],law[::5]):
    print(f"  w2={w:.2f}  s*={sv:.2f}  loi={lv:.2f}")
np.savez('bocal_paysage.npz',w2s=w2s,sstar=sstar,law=law)

# ---- figure 3 panneaux ----
bg='#0f1117'; fig,axes=plt.subplots(1,3,figsize=(17,5.2)); fig.patch.set_facecolor(bg)
for ax in axes:
    ax.set_facecolor(bg); ax.tick_params(colors='#999'); ax.grid(alpha=0.15)
    [s.set_color('#555') for s in ax.spines.values()]

# (a) repulsion des frequences : pred vs mesure
sv=np.array([0.3,0.5,0.7]); A1,A2=3*sv,2*sv
p1=np.sqrt(1.0-g*(0.75*A1**2+1.5*A2**2)); p2=np.sqrt(2.0+g*(0.75*A2**2+1.5*A1**2))
m1=np.array([0.9739,0.9425,0.9111]); m2=np.array([1.4294,1.4608,1.4923])
ax=axes[0]
ax.plot(sv,p1,'-',color='#4ec9b0',label='basse, prédite'); ax.plot(sv,m1,'o',color='#4ec9b0',ms=8,label='basse, mesurée (FFT)')
ax.plot(sv,p2,'-',color='#f48771',label='haute, prédite'); ax.plot(sv,m2,'s',color='#f48771',ms=8,label='haute, mesurée (FFT)')
ax.axhline(1.0,color='#4ec9b0',ls=':',alpha=0.4); ax.axhline(np.sqrt(2),color='#f48771',ls=':',alpha=0.4)
ax.set_xlabel("amplitude s",color='#bbb'); ax.set_ylabel("fréquence effective",color='#bbb')
ax.set_title("(a) Les fréquences se REPOUSSENT\n(signe corrigé, vérifié)",color='#e8e8e8',fontsize=11)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=8)

# (b) l'invariant K vs la loi, 6 systemes
eps=np.array([0.05,0.4142,0.8,1.2,1.85,2.0])
Kobs=np.array([0.029,0.084,0.267,0.44,3.554,4.631])
ax=axes[1]
ee=np.linspace(0.03,2.2,200); ax.plot(ee,C*ee**2*(2+ee),'-',color='#dcdcaa',label="loi  C·ε²(ω₁+ω₂), C=0.254")
ax.plot(eps[1:],Kobs[1:],'o',color='#4ec9b0',ms=9,label="mesuré (5 systèmes)")
ax.plot(eps[0],Kobs[0],'D',color='#f48771',ms=10,label="quasi-dégénéré : 22× au-dessus")
ax.set_xscale('log'); ax.set_yscale('log')
ax.set_xlabel("ε = ω₂ − ω₁",color='#bbb'); ax.set_ylabel("K = g·s*²  (invariant mesuré)",color='#bbb')
ax.set_title("(b) L'invariant K : loi ~ ok, structure réelle\n(pente en g : −0.47…−0.50 = −½ ✓)",color='#e8e8e8',fontsize=11)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=8)

# (c) le paysage s*(w2) et les resonances
ax=axes[2]
ax.plot(w2s,law,'-',color='#dcdcaa',lw=1.2,label="loi lisse")
ax.plot(w2s,sstar,'o-',color='#4ec9b0',ms=4,lw=1,label="s* mesuré")
for r,lab in [(1.0,'1:1'),(2.0,'2:1'),(3.0,'3:1'),(1.5,'3:2')]:
    ax.axvline(r,color='#f48771',ls='--',alpha=0.45); ax.text(r,ax.get_ylim()[1]*0.02+11.2,lab,color='#f48771',ha='center',fontsize=9)
ax.set_xlabel("ω₂  (ω₁=1, g=0.05)",color='#bbb'); ax.set_ylabel("amplitude critique s*",color='#bbb')
ax.set_title("(c) Le paysage de stabilité du fantôme\ncreux aux résonances ?",color='#e8e8e8',fontsize=11)
ax.legend(facecolor=bg,labelcolor='#ccc',edgecolor='#555',fontsize=8,loc='upper left')
fig.suptitle("Le critère, calculé : répulsion vérifiée — invariant K=g·s*² exact en g — le paysage des résonances",
             color='#f0f0f0',fontsize=13,y=1.02)
plt.tight_layout()
plt.savefig('bocal_critere.png',dpi=130,facecolor=bg,bbox_inches='tight')
print("figure sauvee : bocal_critere.png")
