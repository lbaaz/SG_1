import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def scan_pu(w1, w2, gs, ss, T=250.0, dt=0.004, thresh=1e4):
    G, S = np.meshgrid(gs, ss, indexing='ij')
    g = G.ravel(); n = g.size
    W2 = (w1*w2)**2; P2 = w1**2 + w2**2
    y = np.zeros((4, n)); y[0] = S.ravel(); y[3] = S.ravel()
    tb = np.full(n, np.inf); alive = np.ones(n, bool)
    def f(y):
        q1,q2,p1,p2 = y
        return np.array([q2, p2, W2*q1 - g*q1**3, -p1 - P2*q2])
    t = 0.0; steps = int(T/dt)
    for i in range(steps):
        k1=f(y); k2=f(y+dt/2*k1); k3=f(y+dt/2*k2); k4=f(y+dt*k3)
        ynew = y + dt/6*(k1+2*k2+2*k3+k4)
        bad = alive & (np.max(np.abs(ynew),axis=0)>thresh)
        tb[bad] = t; alive &= ~bad
        ynew[:,~alive] = 0.0
        y = np.where(np.isfinite(ynew), ynew, 0.0); t += dt
    return tb.reshape(len(gs), len(ss))

def scan_dimer(gammas, Ps, kappa=1.0, chi=1.0, T=200.0, dt=0.004, thresh=1e6):
    Gm, Pm = np.meshgrid(gammas, Ps, indexing='ij')
    gam = Gm.ravel(); n = gam.size
    a = np.sqrt(Pm.ravel()/2)*(1+0j); b = a.copy()
    tb = np.full(n, np.inf); alive = np.ones(n, bool)
    def f(a,b):
        return (gam*a - 1j*kappa*b - 1j*chi*np.abs(a)**2*a,
                -gam*b - 1j*kappa*a - 1j*chi*np.abs(b)**2*b)
    t=0.0; steps=int(T/dt)
    for i in range(steps):
        k1a,k1b=f(a,b); k2a,k2b=f(a+dt/2*k1a,b+dt/2*k1b)
        k3a,k3b=f(a+dt/2*k2a,b+dt/2*k2b); k4a,k4b=f(a+dt*k3a,b+dt*k3b)
        an=a+dt/6*(k1a+2*k2a+2*k3a+k4a); bn=b+dt/6*(k1b+2*k2b+2*k3b+k4b)
        N=np.abs(an)**2+np.abs(bn)**2
        bad = alive & (N>thresh); tb[bad]=t; alive &= ~bad
        an[~alive]=0; bn[~alive]=0
        a=np.where(np.isfinite(an),an,0); b=np.where(np.isfinite(bn),bn,0); t+=dt
    return tb.reshape(len(gammas), len(Ps))

gs = np.linspace(0.002, 0.25, 56); ss = np.linspace(0.2, 3.2, 56)
print("scan PU generique (w2/w1 = sqrt2)...");  tb_gen = scan_pu(1.0, np.sqrt(2.0), gs, ss)
print("scan PU resonant (w2/w1 = 3)...");       tb_res = scan_pu(1.0, 3.0, gs, ss)
gammas = np.linspace(0.0, 1.15, 56); Ps = np.linspace(0.05, 6.0, 56)
print("scan dimere PT+Kerr (gamma, P)...");     tb_dim = scan_dimer(gammas, Ps)

frac_gen = np.mean(np.isinf(tb_gen)); frac_res = np.mean(np.isinf(tb_res))
print(f"\nfraction BENIGNE :  PU generique = {frac_gen:.2%}   PU resonant 3:1 = {frac_res:.2%}")
# seuil d'amplitude malin a petit g, pour chiffrer la prediction RWA
def s_crit(tb, gi):
    col = tb[gi]; idx = np.where(~np.isinf(col))[0]
    return ss[idx[0]] if idx.size else np.nan
gi = np.argmin(np.abs(gs-0.05))
print(f"a g=0.05 : amplitude critique  generique s*={s_crit(tb_gen,gi):.2f}   resonant s*={s_crit(tb_res,gi):.2f}")
col0 = tb_dim[0]; print(f"dimere a gamma=0 (conservatif) : {np.mean(np.isinf(col0)):.0%} borne (prediction: 100%)")

# --- figure ---
bg='#0f1117'; fig,axes=plt.subplots(1,3,figsize=(16.5,5.2)); fig.patch.set_facecolor(bg)
cmap = plt.cm.inferno.copy()
def panel(ax, tb, ex, xlab, ylab, title):
    Z = np.where(np.isinf(tb), np.nan, np.log10(np.maximum(tb,1e-2))).T
    ax.set_facecolor('#123c37')  # vert sombre = BENIN (borne)
    im = ax.imshow(Z, origin='lower', aspect='auto', extent=ex, cmap=cmap, vmin=0.3, vmax=2.4)
    ax.set_xlabel(xlab,color='#bbb'); ax.set_ylabel(ylab,color='#bbb')
    ax.set_title(title,color='#e8e8e8',fontsize=11.5)
    ax.tick_params(colors='#999')
    [s.set_color('#555') for s in ax.spines.values()]
    return im
im1=panel(axes[0], tb_gen, [gs[0],gs[-1],ss[0],ss[-1]], "couplage g", "amplitude s",
      "PU generique  ($\\omega_2/\\omega_1=\\sqrt{2}$)\nfond vert = benin ; couleur = log$_{10}$ t$_{fuite}$")
im2=panel(axes[1], tb_res, [gs[0],gs[-1],ss[0],ss[-1]], "couplage g", "amplitude s",
      "PU RESONANT  ($\\omega_2/\\omega_1=3$)\nprediction RWA : malin bien plus tot")
im3=panel(axes[2], tb_dim, [gammas[0],gammas[-1],Ps[0],Ps[-1]], "gain/perte $\\gamma$  ($\\kappa=1$)", "puissance P",
      "dimere PT + Kerr\ncanal de la norme : seuil lisse ; $\\gamma=0$ tout benin")
cb=fig.colorbar(im3, ax=axes, fraction=0.025, pad=0.01); cb.set_label("log$_{10}$ t$_{fuite}$",color='#bbb')
cb.ax.tick_params(colors='#999')
fig.suptitle("Le bocal, calculé : deux canaux pour payer le moins — résonances (indéfini conservatif) vs norme (gain/perte)",
             color='#f0f0f0', fontsize=13, y=1.02)
plt.savefig('bocal_phases.png', dpi=130, facecolor=bg, bbox_inches='tight')
print("figure sauvee : bocal_phases.png")
