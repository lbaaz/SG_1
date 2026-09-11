# PREDICTION GELEE (classe 3) : periode de l'enveloppe sous le seuil a 8|2.00|+1 (cellule VIERGE), premier ordre AVEC la correction d'action
# (J2(phi) = J2_0 + (b/a')(1 - cos 2phi)), derivee sans parametre. Bande [0.9 P, 1.1 P] fixee AVANT run ; profondeur annoncee.
import json, math, sys, numpy as np
src = open('/home/claude/D2/D2_premier_ordre_2_1_pair_machine1_v1.py').read().split("w2 = 2.0; Delta")[0]; exec(src)
p, w2, g = 8, 2.0, 0.05; D = w2*w2 - 1
J10 = (1 + w2*w2)**2/(2*D*D); J20 = 2*w2/(D*D); I = J10 - 2*J20
A, Bc = coeffs(p, w2)
ap0 = dev(A, 2*J10, 2*J20/w2, w2); b0 = ev(Bc, 2*J10, 2*J20/w2); r1 = dev(Bc, 2*J10, 2*J20/w2, w2)/ap0
def periode_env(s):
    phis = np.linspace(0, math.pi, 20001); tot = 0.0
    for i in range(len(phis)-1):
        ph = 0.5*(phis[i]+phis[i+1]); J2 = J20 + (b0/ap0)*(1 - math.cos(2*ph)); J1 = I + 2*J2
        rate = (g/(p*D))*(dev(A, 2*J1, 2*J2/w2, w2) + dev(Bc, 2*J1, 2*J2/w2, w2)*math.cos(2*ph))*s**(p-2); tot += (phis[i+1]-phis[i])/rate
    return tot
def M(J1, J2, phi):
    th2 = np.linspace(0, 4*np.pi, 20001); th1 = (phi - th2)/2; return float(np.abs(np.sqrt(2*J1)*np.cos(th1) + np.sqrt(2*J2/w2)*np.cos(th2)).max())
Jm = J20 + 2*b0/ap0; prof = M(I + 2*Jm, Jm, math.pi/2)/M(J10, J20, math.pi)
print(f"p = 8, w2 = 2.00 : a'(J~0) = {ap0:.4f} ; b(J~0) = {b0:.4f} ; b'/a' = {r1:.4f} (ile) ; b/a' = {b0/ap0:.5f} (deplacement d'action {100*b0/ap0/J20:.1f} pour cent de J~2_0) ; profondeur corrigee {prof:.4f}")
pred = []
for s in (0.35, 0.45, 0.55):
    P = periode_env(s); Pn = math.pi*p*D/(g*ap0*s**(p-2))
    pred.append(dict(s=s, K=g*s**(p-2), periode_predite=P, periode_naive=Pn, bande=[0.9*P, 1.1*P], T_min=4*1.1*P, tranche=10))
    print(f"  s = {s:.2f}  K = {g*s**(p-2):.2e}  P_env corrigee = {P:7.1f} (naive {Pn:7.1f})  bande [{0.9*P:.0f}, {1.1*P:.0f}]  T >= {4*1.1*P:.0f}")
json.dump(dict(objet="PREDICTION GELEE : periode de l'enveloppe max|S| sous le seuil a 8|2.00|+1 (VIERGE), premier ordre avec correction d'action (derivee sans parametre apres le volet B, ou elle rend 476/195/94 pour 477.5/195/95 mesures a p = 6). Bande [0.9 P, 1.1 P] fixee AVANT run.",
   cellule="8|2.00|+1", conditions="moteur c8ed357b120352c4, g = 0.05, dt = 0.006, condition initiale de la campagne, sgn = +1 ; s = 0.35, 0.45, 0.55, tous sous le seuil de p = 6 (1.0126) et avec P_env >= 90 (>= 9 tranches de 10 par periode) -- le seuil de p = 8 n'est pas predit",
   lecture="enveloppe max|S| par tranches de 10 ; maxima locaux > 1.03 x min ; periode = moyenne des ecarts sur >= 4 maxima ; T >= 4 x borne haute",
   predictions=pred, profondeur_annoncee=prof, falsifieur="periode hors bande a DEUX des trois s ; a un seul, ecart a verser ; enveloppe non periodique a un s : ni succes ni echec, se verse ; explosion a un s : se verse, la cellule n'est pas sous le seuil (a re-poser plus bas)",
   coefficients=dict(a_prime=ap0, b=b0, r1=r1)), open('prediction_P2_p8_machine1_v1.json', 'w'), indent=1)
