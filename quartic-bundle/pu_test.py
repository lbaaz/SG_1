# pu_test.py -- scan de reference benin/malin du PU quartique
# (reconstruction du meme jour, validee contre bocal_ab_data.npz -- cf. README)
# Systeme canonique identique a bocal_ab.py :
#   y=(q1,q2,p1,p2) ; q1'=q2 ; q2'=p2 ; p1'=W2*q1-g*q1^3 ; p2'=-p1-P2*q2
#   soit x'''' + (w1^2+w2^2) x'' + w1^2 w2^2 x = g x^3, jet initial (x,x',x'',x''')=(s,0,s,0)
#   [tuple canonique (q1,q2,p1,p2)=(s,0,0,s) ; modes A1=3s, A2=-2s]
import numpy as np
w1, w2 = 1.0, np.sqrt(2.0); g = 0.05
P2, W2 = w1*w1 + w2*w2, (w1*w2)**2
def f(y):
    q1,q2,p1,p2 = y
    return np.array([q2, p2, W2*q1 - g*q1**3, -p1 - P2*q2])
def run(s, T=400.0, dt=0.006, blow=1e4):
    y = np.array([s, 0.0, 0.0, s])
    for i in range(int(T/dt)):
        k1=f(y); k2=f(y+0.5*dt*k1); k3=f(y+0.5*dt*k2); k4=f(y+dt*k3)
        y = y + (dt/6.0)*(k1+2*k2+2*k3+k4)
        if np.max(np.abs(y)) > blow: return (i+1)*dt
    return None
print(f"PU quartique (w1,w2)=({w1},{w2:.4f}), g={g} -- famille canonique (s,0,0,s), T=400")
print(f"  {'s':<7}{'verdict':<12}{'t_blow'}")
sstar=None
for s in np.arange(0.50, 2.01, 0.05):
    tb = run(s)
    print(f"  {s:<7.2f}{('MALIN' if tb else 'benin'):<12}{f'{tb:.0f}' if tb else '--'}")
    if tb and sstar is None: sstar = s
print(f"\n  seuil : premier blow-up a s = {sstar:.2f}  (s* dans ({sstar-0.05:.2f}, {sstar:.2f}])")
print("  ancres directes (g=0.05) : s* ~ 1.27 ; t_blow(1.3/1.4/1.5/1.6) = 54/25/52/14")
print("  (les 111/17 de l archive bocal_ab_data = plus proche voisin g=0.0516, s=1.333/1.533)")
