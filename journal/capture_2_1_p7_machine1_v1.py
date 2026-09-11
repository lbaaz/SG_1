# QUADRATURE C ET SEUIL DE CAPTURE (classe 3, zero run sur le moteur) -- machine 1, 11/09/2026.
# Forme normale resonante au premier ordre (delta 86 A-2, angle retrograde) pour la resonance 2:1 a p = 7, w2 = 2.50 :
#   actions normalisees J~ = J/s^2 ; I = J~1 - 2 J~2 conserve ; eps = g s^(p-2)/Delta, Delta = w2^2 - 1 ;
#   H = nu J~2 - eps c(J~) cos(phi), nu = a - b w2 = -0.5, phi = 2 theta1 + theta2, phi0(+1) = pi ;
#   c(J~) = (2/p) sum_{m+n=p, m>=2 pair, n>=1 impair} C(p,m) C(m,(m-2)/2) C(n,(n-1)/2) 2^-p (2J~1)^(m/2) (2J~2/w2)^(n/2).
#   J~2' = -eps c sin(phi) ; phi' = nu - eps (dc/dJ~2 le long du canal) cos(phi).
# Capture (T3 quantifiee) : eps dc/dJ~2 (J~0) >= |nu| ; en dessous, la phase tourne a nu et J~2 oscille faiblement :
# l'apex reste celui du mouvement libre. Au-dessus : libration, apex = extension de la ligne de niveau, t_apex = C/eps
# avec C la demi-periode de libration, quadrature du premier ordre. Confronte au balayage m2 (7|2.50|+1, T = 3000).
import numpy as np, math, json, sys
from math import comb
p, a, b, w2, g = 7, 2, 1, 2.50, 0.05
Delta = w2*w2 - 1; nu = a - b*w2
def c(J1, J2):
    X = 2*J1; Y = 2*J2/w2; tot = 0.0
    for m in range(a, p+1):
        n = p - m
        if n < b or (m - a) % 2 or (n - b) % 2: continue
        tot += comb(p, m) * comb(m, (m-a)//2) * comb(n, (n-b)//2) * 2.0**(-p) * X**(m/2) * Y**(n/2)
    return (2.0/p) * tot
def dc_canal(J2, I, h=1e-7):
    J1 = I + 2*J2
    return (c(I + 2*(J2+h), J2+h) - c(I + 2*(J2-h), J2-h)) / (2*h)
def S_max(J1, J2, phi):
    th2 = np.linspace(0, 2*np.pi, 4001); th1 = (phi - th2)/2
    S = np.sqrt(2*J1)*np.cos(th1) + np.sqrt(2*J2/w2)*np.cos(th2)
    return float(np.abs(S).max())
J10 = (1 + w2*w2)**2/(2*Delta*Delta); J20 = 2*w2/(Delta*Delta); I = J10 - 2*J20
print(f"p={p} w2={w2} nu={nu:+.2f} Delta={Delta} ; J~10={J10:.5f} J~20={J20:.5f} I={I:.5f} ; c(J~0)={c(J10,J20):.5f} ; dc/dJ~2|canal(J~0)={dc_canal(J20,I):.5f}")
s_open = (abs(nu)*Delta/(g*b*dc_canal(J20, I)))**(1.0/(p-2))
print(f"SEUIL DE CAPTURE derive : eps b dc/dJ~2 = |nu|  ->  s_open = {s_open:.4f}   (balayage m2 : apex x1.04 a s0 = 0.51, x1.58 a s0 = 0.65)")
lin = (3 + w2*w2)/Delta
print(f"excursion libre : {lin:.4f} s0 ; verifie S_max(J~0, phi0=pi) = {S_max(J10, J20, math.pi):.4f}")
def reduit(s0, T=3000.0, dt=0.05):
    eps = g*s0**(p-2)/Delta; J2 = J20; phi = math.pi; t = 0.0; apex = (S_max(J10, J20, phi), 0.0); Jmax = (J2, 0.0)
    def f(J2, phi):
        J1 = I + 2*J2
        return -eps*c(J1, J2)*math.sin(phi), nu - eps*dc_canal(J2, I)*math.cos(phi)
    n = int(T/dt)
    for i in range(n):
        k1 = f(J2, phi); k2 = f(J2 + dt/2*k1[0], phi + dt/2*k1[1]); k3 = f(J2 + dt/2*k2[0], phi + dt/2*k2[1]); k4 = f(J2 + dt*k3[0], phi + dt*k3[1])
        J2 += dt/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]); phi += dt/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1]); t += dt
        if J2 <= 0 or J2 > 1e3: break
        if J2 > Jmax[0]: Jmax = (J2, t)
        if i % 20 == 0:
            Sm = S_max(I + 2*J2, J2, phi)
            if Sm > apex[0]: apex = (Sm, t)
    return eps, apex, Jmax
print(f"\n{'s0':>5} {'eps':>9} {'eps c\'':>9} {'/|nu|':>6} | {'apex modele':>11} {'x libre':>7} {'t_apex':>7} | {'m2 apex':>8} {'x libre':>7} {'t_apex m2':>9}")
mes = {0.20: (0.3524, 1.00, None), 0.40: (0.7068, 1.00, None), 0.51: (0.9324, 1.04, None), 0.65: (1.8115, 1.58, 2450.0), 0.80: (1.7734, 1.26, None)}
out = []
for s0 in (0.20, 0.40, 0.51, 0.60, 0.65, 0.70, 0.80):
    eps, (Sm, ta), (Jm, tj) = reduit(s0)
    m = mes.get(s0); r = eps*dc_canal(J20, I)/abs(nu)
    print(f"{s0:5.2f} {eps:9.2e} {eps*dc_canal(J20,I):9.2e} {r:6.2f} | {Sm*s0:11.4f} {Sm/lin:7.2f} {ta:7.0f} | " + (f"{m[0]:8.4f} {m[1]:7.2f} {str(m[2]):>9}" if m else f"{'--':>8} {'--':>7} {'--':>9}"))
    out.append(dict(s0=s0, eps=eps, capture=r, apex_modele=Sm*s0, ratio_modele=Sm/lin, t_apex_modele=ta, mesure=m))
json.dump(dict(p=p, w2=w2, nu=nu, s_open=s_open, lignes=out), open('capture_2_1_p7_machine1_v1.json', 'w'), indent=1)
