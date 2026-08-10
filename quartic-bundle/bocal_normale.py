import numpy as np, sympy as sp

print("="*74)
print("[M1-a] LA FORME NORMALE AU 1:1 (convention symplectique reparee)")
print("="*74)
# Ghost = mode BAS (c1<0), tourne e^{+i w t}. x = k1(al e^{iwt}+conj) + k2(be e^{-iwt}+conj)
# => x = (k1*albar + k2*be) e^{-iwt} + c.c.  ==> partie lente de (g/4)x^4 :
k1,k2,g = sp.symbols('kappa1 kappa2 g', positive=True)
al,alb,be,beb = sp.symbols('alpha alphabar beta betabar')
w = k1*alb + k2*be; wb = k1*al + k2*beb
Vslow = sp.expand(sp.Rational(3,2)*g*(w*wb)**2)
print("  V_lent = (3g/2)|k1*conj(alpha) + k2*beta|^4 =")
print(f"    {Vslow}")
print("  Inventaire : actions (|a|^4,|b|^4,|a|^2|b|^2) + canaux m=1 (N*ab) + m=2 (a^2b^2). OK.")
print("  >>> VALLEE D'ANNULATION : V_lent = 0  <=>  k1*conj(alpha) = -k2*beta.")
print("      Ratio d'actions sur la vallee : k1^2 J_A = k2^2 J_B  <=>  J_A/J_B = w1/w2")
print("      (k_i^2 = 1/(2 Delta w_i)).  Charge conservee : M = J_A - J_B (tous les termes")
print("      lents ont charge (+m,+m)).  L'echappee = croissance jointe J_A,J_B le long de")
print("      la vallee : x s'annule, l'interaction devient aveugle, H_libre ne coute rien.")
print("      Le fantome s'echappe en se rendant INVISIBLE. Predictions : E1/E2 -> w1^2/w2^2,")
print("      et rho = max|x| / (amp1+amp2) -> petit, PENDANT le runaway quasi-degenere.\n")

print("="*74)
print("[M1-b] VERIFICATION : signatures de la vallee pendant le runaway")
print("="*74)
def run_track(w1,w2,gv,s,dt=0.002,tmax=600.0):
    W2=(w1*w2)**2; P2=w1**2+w2**2; D=w2**2-w1**2
    y=np.array([s,0.0,0.0,s]); t=0.0
    marks=[10.,30.,100.,300.,1000.]; mi=0; rows=[]
    hist=[]
    def f(y):
        q1,q2,p1,p2=y
        return np.array([q2,p2,W2*q1-gv*q1**3,-p1-P2*q2])
    while t<tmax and mi<len(marks):
        k1_=f(y);k2_=f(y+dt/2*k1_);k3_=f(y+dt/2*k2_);k4_=f(y+dt*k3_)
        y=y+dt/6*(k1_+2*k2_+2*k3_+k4_); t+=dt
        hist.append(abs(y[0]))
        if len(hist)>2000: hist.pop(0)
        if np.max(np.abs(y))>marks[mi]:
            q1,q2,p1,p2=y
            X1=(p2+w2**2*q1)/D; V1=(-p1-w1**2*q2)/D
            X2=(p2+w1**2*q1)/(-D); V2=(-p1-w2**2*q2)/(-D)
            E1=(V1**2+w1**2*X1**2)/2; E2=(V2**2+w2**2*X2**2)/2
            a1=np.sqrt(2*E1)/w1; a2=np.sqrt(2*E2)/w2
            rho=np.max(hist)/(a1+a2)
            rows.append((marks[mi],t,E1/E2,rho)); mi+=1
    return rows
for (W1,W2,s,name) in [(1.0,1.05,1.0,"quasi-1:1 (1,1.05)"),(1.0,2.85,9.0,"lointain (1,2.85)")]:
    print(f"  {name}, g=0.05, s={s} ; prediction vallee E1/E2 = {W1**2/W2**2:.3f}")
    rows=run_track(W1,W2,0.05,s)
    print(f"    {'|y| franchit':<14}{'t':<9}{'E1/E2':<10}{'rho = max|x|/(amp1+amp2)'}")
    for m,t,r,rho in rows:
        print(f"    {m:<14.0f}{t:<9.1f}{r:<10.3f}{rho:.3f}")
print()

print("="*74)
print("[M1-c] L'ANOMALIE : exposant de K(eps) jusqu'a la degenerescence EXACTE")
print("="*74)
def scan_col(w2v,gval,ss,T=400.0,dt=0.006,thresh=1e4,w1v=1.0):
    n=len(ss); W2=(w1v*w2v)**2; P2=w1v**2+w2v**2
    y=np.zeros((4,n)); y[0]=ss; y[3]=ss
    tb=np.full(n,np.inf); alive=np.ones(n,bool); t=0.0
    def f(y):
        q1,q2,p1,p2=y
        return np.array([q2,p2,W2*q1-gval*q1**3,-p1-P2*q2])
    for i in range(int(T/dt)):
        k1_=f(y);k2_=f(y+dt/2*k1_);k3_=f(y+dt/2*k2_);k4_=f(y+dt*k3_)
        yn=y+dt/6*(k1_+2*k2_+2*k3_+k4_)
        bad=alive&(np.max(np.abs(yn),axis=0)>thresh); tb[bad]=t; alive&=~bad
        yn[:,~alive]=0.0; y=np.where(np.isfinite(yn),yn,0.0); t+=dt
    idx=np.where(~np.isinf(tb))[0]
    return ss[idx[0]] if idx.size else np.nan
ss=np.linspace(0.05,3.0,60); g=0.05
print(f"  {'w2':<8}{'eps':<8}{'s*':<8}{'K=g s*^2':<12}{'K_loi=0.254 eps^2(w1+w2)':<26}{'K/K_loi'}")
Ke=[]
for w2v in [1.0,1.02,1.05,1.10,1.15,1.20,1.30]:
    sc=scan_col(w2v,g,ss); eps=w2v-1.0
    K=g*sc**2 if np.isfinite(sc) else np.nan
    Kl=0.254*eps**2*(1+w2v) if eps>0 else np.nan
    Ke.append((eps,K))
    rat=f"{K/Kl:.1f}" if eps>0 and np.isfinite(K) else "--"
    print(f"  {w2v:<8.2f}{eps:<8.2f}{sc:<8.2f}{K:<12.4f}{Kl:<26.5f}{rat}")
eps_a=np.array([e for e,k in Ke if e>=0.02 and np.isfinite(k)])
K_a=np.array([k for e,k in Ke if e>=0.02 and np.isfinite(k)])
p=np.polyfit(np.log(eps_a),np.log(K_a),1)[0]
print(f"\n  exposant mesure pres de la degenerescence : K ~ eps^{p:.2f}  (loi lointaine : eps^2)")
