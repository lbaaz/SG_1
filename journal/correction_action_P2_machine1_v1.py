# La correction du premier ordre que la prediction P2 omettait : le terme resonant deplace l'action le long de la rotation.
# J2' = -(2g/(p Delta)) b sin 2phi, phi' = -(g/(p Delta)) a'  =>  dJ2/dphi = 2 b sin(2phi)/a'  =>  J2(phi) = J2_0 + (b/a')(1 - cos 2phi) >= J2_0
# (depart a phi0 = pi). L'action moyenne sur une rotation est J2_0 + b/a' ; a' (croissant en J) est donc plus grand en moyenne :
# periode plus COURTE ; et a phi = pi/2 (minimum de M) J est maximal : modulation moins PROFONDE. Deux corrections, meme cause, sans parametre.
import json, math, sys, numpy as np
sys.path.insert(0, '/home/claude/D2')
src = open('/home/claude/D2/D2_premier_ordre_2_1_pair_machine1_v1.py').read().split("w2 = 2.0; Delta")[0]; exec(src)
p, w2, g = 6, 2.0, 0.05; D = w2*w2 - 1
J10 = (1 + w2*w2)**2/(2*D*D); J20 = 2*w2/(D*D); I = J10 - 2*J20
A, Bc = coeffs(p, w2)
def a_prime(J2): J1 = I + 2*J2; return dev(A, 2*J1, 2*J2/w2, w2)
def b_of(J2): J1 = I + 2*J2; return ev(Bc, 2*J1, 2*J2/w2)
ap0 = a_prime(J20); b0 = b_of(J20)
print(f"a'(J~0) = {ap0:.4f} ; b(J~0) = {b0:.4f} ; deplacement moyen d'action b/a' = {b0/ap0:.5f} (J~2_0 = {J20:.5f}, soit {100*b0/ap0/J20:.1f} pour cent)")
# periode : phi' = -(g/(p Delta)) [a'(J2(phi)) + b'(J2) cos 2phi] avec J2(phi) = J20 + (b/a')(1 - cos 2phi) ; periode de l'enveloppe = temps pour phi : pi -> 0 (une demi-rotation)
def periode_env(s):
    phis = np.linspace(0, math.pi, 20001); tot = 0.0
    for i in range(len(phis)-1):
        ph = 0.5*(phis[i]+phis[i+1]); J2 = J20 + (b0/ap0)*(1 - math.cos(2*ph)); J1 = I + 2*J2
        rate = (g/(p*D))*(dev(A, 2*J1, 2*J2/w2, w2) + dev(Bc, 2*J1, 2*J2/w2, w2)*math.cos(2*ph))*s**(p-2)
        tot += (phis[i+1]-phis[i])/rate
    return tot
def M(J1, J2, phi):
    th2 = np.linspace(0, 4*np.pi, 20001); th1 = (phi - th2)/2
    return float(np.abs(np.sqrt(2*J1)*np.cos(th1) + np.sqrt(2*J2/w2)*np.cos(th2)).max())
mes = {0.40: (477.5, 0.8972), 0.50: (195.0, 0.8991), 0.60: (95.0, 0.9051)}
print(f"\n{'s':>5} {'P naif':>7} {'P corrige':>9} {'P mesure':>8} {'ecart naif':>10} {'ecart corr':>10} | {'prof naive':>10} {'prof corr':>9} {'prof mes':>8}")
for s in (0.40, 0.50, 0.60):
    Pn = math.pi*p*D/(g*ap0*s**4); Pc = periode_env(s)
    Jmax2 = J20 + 2*b0/ap0; Mmin_c = M(I + 2*Jmax2, Jmax2, math.pi/2); Mmax = M(J10, J20, math.pi)
    prof_c = Mmin_c/Mmax; prof_n = M(J10, J20, math.pi/2)/Mmax
    print(f"{s:5.2f} {Pn:7.1f} {Pc:9.1f} {mes[s][0]:8.1f} {100*(Pn/mes[s][0]-1):+9.1f} pc {100*(Pc/mes[s][0]-1):+9.1f} pc | {prof_n:10.4f} {prof_c:9.4f} {mes[s][1]:8.4f}")
print("\n(pc = ecart relatif en pour cent)")
