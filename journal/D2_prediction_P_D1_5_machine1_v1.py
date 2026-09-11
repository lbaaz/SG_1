# D2 -- PREDICTIONS GELEES POUR LA CELLULE P-D1-5 (p = 6, w2 = 2.00, sgn +1, vierge), derivees du premier ordre.
# (1) r1(p) = b'/a' le long du canal a 2:1 pour p pair : ile tant que r1 < 1 ; p_c ou r1 atteint 1 (extrapolation derivee, pas de parametre).
# (2) SOUS LE SEUIL, l'enveloppe max|S| est modulee par la rotation lente de la phase resonante phi = 2 theta1 + theta2 :
#     phi' = -(g/(p Delta)) a'(J2)  (a' = 2 da/dJ1 + da/dJ2, derivee le long du canal, b' <= 0.1 a' a p = 6),
#     periode de l'enveloppe P(s) = 2 pi p Delta / (g a'(J~0) s^(p-2))  [J~ = J/s^2] : une loi en 1/K, coefficient DERIVE.
import numpy as np, json, math
from math import comb
exec(open('D2_premier_ordre_2_1_pair_machine1_v1.py').read().split("w2 = 2.0; Delta")[0])   # reprend coeffs, ev, dev
w2 = 2.0; Delta = w2*w2 - 1; g = 0.05
J1 = (1 + w2*w2)**2/(2*Delta*Delta); J2 = 2*w2/(Delta*Delta); I = J1 - 2*J2; X2, Y2 = 2*J1, 2*J2/w2
print("(1) r1(p) = b'/a' au point initial et p_c :")
rs = {}
for p in range(4, 41, 2):
    A, B = coeffs(p, w2); da, db = dev(A, X2, Y2, w2), dev(B, X2, Y2, w2); rs[p] = db/da
pc = next(p for p in sorted(rs) if rs[p] >= 1.0)
print("   " + "  ".join(f"p={p}:{rs[p]:.3f}" for p in sorted(rs) if p <= 30))
print(f"   p_c = {pc} (premier p pair avec b'/a' >= 1 au point initial) ; r1({pc-2}) = {rs[pc-2]:.3f}, r1({pc}) = {rs[pc]:.3f}")
print("\n(2) periode de l'enveloppe sous le seuil, p = 6, w2 = 2.00, +1 :")
p = 6; A, B = coeffs(p, w2); da = dev(A, X2, Y2, w2); db = dev(B, X2, Y2, w2)
print(f"   a'(J~0) = {da:.6f} ; b'(J~0) = {db:.6f} ; b'/a' = {db/da:.4f} ; excursion libre max|S| = (3 + w2^2)/Delta = {(3+w2*w2)/Delta:.4f} s")
pred = []
# M(phi) = max|S| a phi fixe est pi-PERIODIQUE en phi (verifie numeriquement : M(0) = M(pi) = X+Y, M(pi/2) = 0.868 (X+Y)) :
# la periode de l'ENVELOPPE est donc pi/|phi'| = pi p Delta/(g a' s^(p-2)), la moitie de la periode de phi.
for s in (0.40, 0.50, 0.60):
    K = g*s**(p-2); phidot = g*da*s**(p-2)/(p*Delta); P = math.pi/phidot
    pred.append(dict(s=s, K=K, phi_point=phidot, periode_enveloppe_predite=P, bande=[0.8*P, 1.25*P], T_min=4*1.25*P))
    print(f"   s = {s:.2f}  K = {K:.5f}  |phi'| = {phidot:.5f}  P_env(s) = {P:7.1f}  bande [{0.8*P:.0f}, {1.25*P:.0f}]  T >= {4*1.25*P:.0f}")
print("   profondeur de modulation derivee (premier ordre, independante de s) : max|S| de 2.333 s a 2.024 s, rapport 0.868")
out = dict(objet="D2 -- PREDICTIONS GELEES pour P-D1-5 (p = 6, w2 = 2.00, sgn = +1), cellule VIERGE, derivees du premier ordre a 2:1 (angle retrograde, harmonique (4,2)). Rien n'est ajuste : les coefficients a', b' sont des combinatoires de S^6.",
  cellule="6|2.00|+1", conditions="moteur c8ed357b120352c4, g = 0.05, dt = 0.006, condition initiale de la campagne (x1 = s (1+w2^2)/Delta, x2 = -2s/Delta, v = 0)",
  P1=dict(enonce="ILE au premier ordre : b'/a' = 0.094 << 1 ; le seuil s*(T) est T-INDEPENDANT a un pas de grille pres (s*(1600)/s*(400) = 1) et SIGNE-independant (parite exacte a degre pair). C'est l'attendu de P-D1-5 ; D2 en donne la RAISON derivee.", falsifieur="ratio 4^(-1/4) = 0.707 a 5 pour cent (canal direct), ou s*(+1) != s*(-1) de plus d'un pas"),
  P2=dict(enonce="SOUS LE SEUIL, l'enveloppe max|S| par tranches est MODULEE avec la periode P_env(s) = pi p Delta/(g a'(J~0) s^(p-2)), a'(J~0) = %.6f (M(phi) est pi-periodique) : loi en 1/K, coefficient derive, aucun parametre ; profondeur derivee : max|S| entre 2.024 s et 2.333 s (rapport 0.868)." % da,
          lecture="enveloppe max|S| par tranches de 10 (une periode rapide entiere ; P_env de 100 a 500), maxima locaux > 1.03 x min, periode = moyenne des ecarts sur >= 4 maxima ; T >= 4 x borne haute ; sgn = +1",
          predictions=pred, bande="[0.8 P, 1.25 P] fixee AVANT run : le premier ordre est exact a O(K) pres, K <= 0.0065 ici ; profondeur 0.868 : grandeur annoncee, non falsifiante seule",
          falsifieur="periode hors bande a DEUX des trois s ; a un seul, ecart a verser ; enveloppe NON periodique (pas de maxima) a un s : NI SUCCES NI ECHEC, se verse (le regime pourrait etre celui de 7|2.50)"),
  P3=dict(enonce="p_c = %d : premier degre pair ou la (4,2) l'emporte sur le shift (b'/a' >= 1) et ou le site 2:1 s'ouvre au premier ordre (canal direct, nombres de fenetre, ratio 4^(-1/(p-2))). Hors perimetre de B ; prediction annexe, a geler a part si l'operateur la joue." % pc, r1={str(k): v for k, v in rs.items() if k <= 30}),
  hors_perimetre="la VALEUR de s*(6|2.00) n'est PAS predite : elle est hors du premier ordre (a p = 4, K* = 0.347 mesure ; le mecanisme au-dela du premier ordre n'est pas derive)")
json.dump(out, open('D2_prediction_P_D1_5_machine1_v1.json', 'w'), indent=1)
