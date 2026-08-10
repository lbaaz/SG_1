import numpy as np, sympy as sp
np.set_printoptions(precision=4, suppress=True)

print("="*74)
print("[1] DERIVATION MULTI-ECHELLES DES DECALAGES -- et correction de mon signe")
print("="*74)
# EOM exacte : (d2+w1^2)(d2+w2^2) x = g x^3   (verifie depuis H, cf. pu_test)
# x = A1 cos(th1) + A2 cos(th2). Partie resonante de x^3 a chaque frequence :
A1,A2,g,w1,w2 = sp.symbols('A1 A2 g omega1 omega2', positive=True)
D = w2**2 - w1**2
# coefficient resonant a th1 : 3/4 A1^3 + 3/2 A1 A2^2 ; a th2 : 3/4 A2^3 + 3/2 A1^2 A2
# F(nu)=(nu-w1^2)(nu-w2^2) ; F(w1^2+d1) ~ -D d1 ; F(w2^2+d2) ~ +D d2
d1 = -(g/D)*(sp.Rational(3,4)*A1**2 + sp.Rational(3,2)*A2**2)
d2 = +(g/D)*(sp.Rational(3,4)*A2**2 + sp.Rational(3,2)*A1**2)
print(f"  delta(w1^2) = {d1}   < 0  : la frequence BASSE descend")
print(f"  delta(w2^2) = {d2}   > 0  : la frequence HAUTE monte")
print("  >>> LES FREQUENCES SE REPOUSSENT. Le rapport w2eff/w1eff AUGMENTE avec l'amplitude.")
print("      Mon 'capture par derive vers le 1:1' du tour precedent etait FAUX (signe).")
print("      La proximite au 1:1 reste le facteur organisateur (donnees) -- le mecanisme")
print("      doit donc etre la LARGEUR de la zone resonante (appariement auto-parametrique")
print("      a cout nul, canal A^2B^2 du 1:1), pas la derive des centres.\n")

print("="*74)
print("[2] VERIFICATION NUMERIQUE DES DECALAGES (FFT sur trajectoires benignes)")
print("="*74)
def traj(w1v,w2v,gv,s,T=400.0,dt=0.002):
    W2=(w1v*w2v)**2; P2=w1v**2+w2v**2
    y=np.array([s,0.0,0.0,s]); n=int(T/dt); out=np.empty(n)
    def f(y):
        q1,q2,p1,p2=y
        return np.array([q2,p2,W2*q1-gv*q1**3,-p1-P2*q2])
    for i in range(n):
        k1=f(y);k2=f(y+dt/2*k1);k3=f(y+dt/2*k2);k4=f(y+dt*k3)
        y=y+dt/6*(k1+2*k2+2*k3+k4); out[i]=y[0]
    return out,dt
def peaks(x,dt):
    n=len(x); w=np.hanning(n); X=np.abs(np.fft.rfft(x*w)); fr=np.fft.rfftfreq(n,dt)*2*np.pi
    lo=(fr>0.4)&(fr<1.25); hi=(fr>1.25)&(fr<2.2)
    return fr[lo][np.argmax(X[lo])], fr[hi][np.argmax(X[hi])]
print(f"  systeme (1, sqrt2), g=0.05 ; A1=3s, A2=2s (des CI (s,0,0,s)) :")
print(f"  {'s':<6}{'w1_eff pred':<13}{'w1_eff mes':<13}{'w2_eff pred':<13}{'w2_eff mes'}")
for s in [0.3,0.5,0.7]:
    a1,a2=3*s,2*s; Dv=1.0; gv=0.05
    p1=np.sqrt(1.0 - gv/Dv*(0.75*a1**2+1.5*a2**2))
    p2=np.sqrt(2.0 + gv/Dv*(0.75*a2**2+1.5*a1**2))
    x,dt=traj(1.0,np.sqrt(2.0),gv,s)
    m1,m2=peaks(x,dt)
    print(f"  {s:<6.1f}{p1:<13.4f}{m1:<13.4f}{p2:<13.4f}{m2:.4f}")
print("  (test binaire : basse DESCEND sous 1.0, haute MONTE au-dessus de 1.414)\n")

print("="*74)
print("[3] LA LOI DE SEUIL, depuis les donnees cachees + candidats")
print("="*74)
d=np.load('bocal_ab_data.npz'); gs=d['gs']; ssL=d['ssL']; ssH=d['ssH']
systems=[("1.05",1.0,1.05,d['tbB'],ssL),("sqrt2",1.0,np.sqrt(2.0),d['tbA'],ssL),
         ("2.85",1.0,2.85,d['tbC'],ssH),("3.00",1.0,3.0,d['tbD'],ssH)]
def scrit(tb,ss,gi):
    col=tb[gi]; idx=np.where(~np.isinf(col))[0]
    return ss[idx[0]] if idx.size else np.nan
print(f"  exposant en g (fit log s* vs log g ; prediction loi-invariante : -1/2) :")
Ks={}
for name,W1,W2,tb,ss in systems:
    gv=[];sv=[]
    for gi in range(len(gs)):
        sc=scrit(tb,ss,gi)
        if np.isfinite(sc) and sc>ss[1]: gv.append(gs[gi]); sv.append(sc)
    gv=np.array(gv);sv=np.array(sv)
    slope=np.polyfit(np.log(gv),np.log(sv),1)[0]
    K=np.median(gv*sv**2); Ks[name]=(W1,W2,K)
    print(f"    ({name:>5}) : pente = {slope:+.2f}   K = median(g*s*^2) = {K:.3f}")
print()
print("  candidats pour K(w1,w2), normalises a (1,sqrt2) :")
obs={n:Ks[n][2]/Ks['sqrt2'][2] for n in Ks}
for lawname,law in [("eps^2*(w1+w2)  [largeur parametrique]", lambda w1,w2:(w2-w1)**2*(w1+w2)),
                    ("eps*Delta^2", lambda w1,w2:(w2-w1)*(w2**2-w1**2)**2),
                    ("eps^3", lambda w1,w2:(w2-w1)**3)]:
    ref=law(1.0,np.sqrt(2.0))
    pred={n:law(Ks[n][0],Ks[n][1])/ref for n in Ks}
    line="    "+lawname+" : "
    for n in ["1.05","sqrt2","2.85","3.00"]:
        line+=f"[{n}: pred {pred[n]:.3g} / obs {obs[n]:.3g}]  "
    print(line)
C=np.mean([Ks[n][2]/((Ks[n][1]-Ks[n][0])**2*(Ks[n][0]+Ks[n][1])) for n in ["sqrt2","2.85","3.00"]])
print(f"\n  => loi retenue (3 systemes non-degeneres) :  g s*^2 ~ C (w2-w1)^2 (w1+w2),  C = {C:.3f}")
anom=Ks['1.05'][2]/(C*(0.05)**2*(2.05))
print(f"     anomalie quasi-degeneree (1,1.05) : {anom:.0f}x PLUS STABLE que la loi")
print(f"     -> coherent avec l'auto-detuning : pres du 1:1 les decalages ~ g s^2/Delta^3 explosent")
print(f"        et desaccordent l'appariement avant qu'il ne s'emballe. A deriver proprement.\n")

print("="*74)
print("[4] TEST HORS ECHANTILLON -- predictions AVANT mesure")
print("="*74)
def scan_col(w1v,w2v,gval,ss,T=400.0,dt=0.006,thresh=1e4):
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
for (W1v,W2v) in [(1.0,1.8),(1.0,2.2)]:
    for gval in [0.05,0.15]:
        spred=np.sqrt(C*(W2v-W1v)**2*(W1v+W2v)/gval)
        ss=np.linspace(0.2,max(2.5*spred,3.0),60)
        smes=scan_col(W1v,W2v,gval,ss)
        err=100*(smes-spred)/spred if np.isfinite(smes) else np.nan
        print(f"  (1,{W2v}) g={gval:.2f} :  s* PREDIT = {spred:.2f}   s* MESURE = {smes:.2f}   ecart = {err:+.0f}%")
np.savez('bocal_loi.npz', C=C, Ks={k:v[2] for k,v in Ks.items()})
