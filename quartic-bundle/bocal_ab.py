import numpy as np, sympy as sp
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------- 1. SYMBOLIQUE : quels monomes survivent a la moyenne, selon le rapport ----------
cA,cB = sp.symbols('c_A c_B', positive=True)
A,Ac,B,Bc,z1,z2 = sp.symbols('A Abar B Bbar z1 z2')
x = cA*(A*z1 + Ac/z1) + cB*(B/z2 + Bc*z2)
V4 = sp.expand((x**4)/4)
Vp = sp.Poly(sp.expand(V4*z1**4*z2**4),(z1,z2))
def resonants(ratio_num, ratio_den):  # w2/w1 = num/den ; zero freq <=> (a-b)*den = (c-d)*num... via powers
    out=[]
    for mono,coef in zip(Vp.monoms(),Vp.coeffs()):
        P,Q = mono; k=(P-4); l=(Q-4)   # facteur temps: e^{-i(k w1 + l w2)t}
        if k*ratio_den + l*ratio_num == 0 and not (k==0 and l==0):
            out.append((coef, k, l))
    return out
r3 = resonants(3,1); r1 = resonants(1,1)
print("monomes resonants NON-action pour w2/w1=3 :", [(str(c),k,l) for c,k,l in r3])
print("monomes resonants NON-action pour w2/w1=1 :", len(r1), "termes (ex:",[(str(c),k,l) for c,k,l in r1[:3]],")")
print("=> 3:1 : UN canal (A^3 B + c.c., cree 3 quanta+ et 1 quantum- a cout nul).")
print("   1:1 : NOMBREUX canaux (N_A*A*Bbar etc.) -> le point de Jordan est le carrefour resonant.\n")

# ---------- 2. NUMERIQUE : A/B controle, raideur appariee ----------
def scan_pu(w1,w2,gs,ss,T=400.0,dt=0.006,thresh=1e4):
    G,S=np.meshgrid(gs,ss,indexing='ij'); g=G.ravel(); n=g.size
    W2=(w1*w2)**2; P2=w1**2+w2**2
    y=np.zeros((4,n)); y[0]=S.ravel(); y[3]=S.ravel()
    tb=np.full(n,np.inf); alive=np.ones(n,bool)
    def f(y):
        q1,q2,p1,p2=y
        return np.array([q2,p2,W2*q1-g*q1**3,-p1-P2*q2])
    t=0.0
    for i in range(int(T/dt)):
        k1=f(y);k2=f(y+dt/2*k1);k3=f(y+dt/2*k2);k4=f(y+dt*k3)
        yn=y+dt/6*(k1+2*k2+2*k3+k4)
        bad=alive&(np.max(np.abs(yn),axis=0)>thresh); tb[bad]=t; alive&=~bad
        yn[:,~alive]=0.0; y=np.where(np.isfinite(yn),yn,0.0); t+=dt
    return tb.reshape(len(gs),len(ss))

gs=np.linspace(0.002,0.25,46)
ssL=np.linspace(0.2,3.2,46)     # paire basse raideur
ssH=np.linspace(0.5,10.0,46)    # paire haute raideur
print("scan (1, 1.414) generique bas..."); tbA=scan_pu(1.0,np.sqrt(2.0),gs,ssL)
print("scan (1, 1.05) quasi-1:1 / EP...");  tbB=scan_pu(1.0,1.05,gs,ssL)
print("scan (1, 2.85) generique haut...");  tbC=scan_pu(1.0,2.85,gs,ssH)
print("scan (1, 3.00) resonant 3:1...");    tbD=scan_pu(1.0,3.0,gs,ssH)

def frac(tb): return np.mean(np.isinf(tb))
def scrit(tb,ss,gval):
    gi=np.argmin(np.abs(gs-gval)); col=tb[gi]; idx=np.where(~np.isinf(col))[0]
    return ss[idx[0]] if idx.size else np.nan
print(f"\n  paire BASSE raideur :  benin(1,1.414)={frac(tbA):.1%}   benin(1,1.05)={frac(tbB):.1%}")
print(f"    s* a g=0.05 :  1.414 -> {scrit(tbA,ssL,0.05):.2f}    1.05 -> {scrit(tbB,ssL,0.05):.2f}")
print(f"  paire HAUTE raideur :  benin(1,2.85)={frac(tbC):.1%}   benin(1,3.00)={frac(tbD):.1%}")
print(f"    s* a g=0.05 :  2.85 -> {scrit(tbC,ssH,0.05):.2f}    3.00 -> {scrit(tbD,ssH,0.05):.2f}")
print(f"    s* a g=0.15 :  2.85 -> {scrit(tbC,ssH,0.15):.2f}    3.00 -> {scrit(tbD,ssH,0.15):.2f}")

# ---------- figure ----------
bg='#0f1117'; fig,axes=plt.subplots(2,2,figsize=(12.5,9.5)); fig.patch.set_facecolor(bg)
cmap=plt.cm.inferno.copy()
def panel(ax,tb,ss,title):
    Z=np.where(np.isinf(tb),np.nan,np.log10(np.maximum(tb,1e-2))).T
    ax.set_facecolor('#123c37')
    im=ax.imshow(Z,origin='lower',aspect='auto',extent=[gs[0],gs[-1],ss[0],ss[-1]],cmap=cmap,vmin=0.3,vmax=2.6)
    ax.set_title(title,color='#e8e8e8',fontsize=11); ax.tick_params(colors='#999')
    [s.set_color('#555') for s in ax.spines.values()]; return im
panel(axes[0,0],tbA,ssL,"$\\omega_2/\\omega_1=\\sqrt{2}$  (générique, près du 1:1)")
panel(axes[0,1],tbB,ssL,"$\\omega_2/\\omega_1=1.05$  (quasi-EP : prédiction = très malin)")
panel(axes[1,0],tbC,ssH,"$\\omega_2/\\omega_1=2.85$  (générique, loin du 1:1)")
im=panel(axes[1,1],tbD,ssH,"$\\omega_2/\\omega_1=3$  (résonant 3:1 : canal unique)")
for ax in axes[1]: ax.set_xlabel("couplage g",color='#bbb')
for ax in axes[:,0]: ax.set_ylabel("amplitude s",color='#bbb')
cb=fig.colorbar(im,ax=axes,fraction=0.025,pad=0.01); cb.set_label("log$_{10}$ t$_{fuite}$",color='#bbb'); cb.ax.tick_params(colors='#999')
fig.suptitle("Test A/B à raideur appariée : la malignité est-elle organisée par la distance au 1:1 (le point de Jordan) ?",
             color='#f0f0f0',fontsize=12.5,y=0.995)
plt.savefig('bocal_ab.png',dpi=130,facecolor=bg,bbox_inches='tight')
np.savez("bocal_ab_data.npz",tbA=tbA,tbB=tbB,tbC=tbC,tbD=tbD,gs=gs,ssL=ssL,ssH=ssH)
print("figure sauvee : bocal_ab.png ; donnees cachees : bocal_ab_data.npz")
