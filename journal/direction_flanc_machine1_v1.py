# DERIVATION AU PREMIER ORDRE DE LA DIRECTION DE L'ASYMETRIE DE SIGNE PRES D'UNE RESONANCE a:b (classe 3, zero run).
# Angle du mode fantome RETROGRADE (theta2' = -w2) ; phase resonante phi = a theta1 + b theta2 ; forme normale
# H = I + delta J - kappa(J) cos(phi), kappa > 0, delta = a - b w2 ; J' = -kappa sin(phi) (J croit ssi sin phi < 0) ;
# phi' = delta - kappa'(J) cos(phi). Condition initiale v = 0, x1(0) = sgn s (1+w2^2)/Delta > 0 pour +1, x2(0) = -sgn 2s/Delta :
# theta1(0) = 0 / pi, theta2(0) = pi / 0 pour sgn = +1 / -1, donc phi0(+1) = b pi, phi0(-1) = a pi : deux points ou sin phi = 0.
# Signe FRAGILE (seuil le plus bas) = celui dont phi' initial l'emporte vers le demi-plan sin phi < 0 :
#   delta > 0 (w2 < a/b) : fragile si cos(phi0) = -1 (phi0 = pi) ; delta < 0 (w2 > a/b) : fragile si cos(phi0) = +1 (phi0 = 0).
# A la resonance exacte (delta = 0) les deux signes sont images l'un de l'autre par phi -> -phi : AUCUNE asymetrie (theoreme).
import json, math, sys
def phi0(sgn, a, b): return (b % 2) * math.pi if sgn == +1 else (a % 2) * math.pi
def fragile(a, b, cote):
    """cote = -1 (w2 < a/b) ou +1 (w2 > a/b) ; rend '+1', '-1' ou 'aucune' (deux signes au meme point)."""
    c = {s: math.cos(phi0(s, a, b)) for s in (+1, -1)}
    if c[+1] == c[-1]: return 'aucune'
    cible = -1.0 if cote < 0 else +1.0
    return '+1' if c[+1] == cible else '-1'
print("TABLE DERIVEE : signe fragile (seuil le plus bas) sur chaque flanc, par parite de (a, b)")
print(f"  {'a:b':>5} {'phi0(+1)':>9} {'phi0(-1)':>9} {'w2 < a/b':>9} {'w2 > a/b':>9}")
for a, b in ((2, 1), (3, 2), (4, 1), (5, 2), (5, 4), (6, 1), (7, 2), (4, 3), (3, 1), (5, 3), (1, 1)):
    print(f"  {a}:{b:<3} {phi0(+1,a,b)/math.pi:>8.0f}pi {phi0(-1,a,b)/math.pi:>8.0f}pi {fragile(a,b,-1):>9} {fragile(a,b,+1):>9}")
# confrontation POST HOC avec les cellules archivees du flanc de 2:1 (lecture m2 c8219ff40e8a783c) : la derivation n'a aucun parametre
D = json.load(open(sys.argv[1] if len(sys.argv) > 1 else '/mnt/user-data/uploads/lecture_parite_signe_machine2_v1.json'))['detail']
n = ok = 0; ex = []
for r in D:
    w2 = r['w2']
    if 1.80 <= w2 <= 2.30 and abs(w2 - 2.0) > 1e-9:
        pred = fragile(2, 1, -1 if w2 < 2 else +1); mes = '+1' if r['ln'] < 0 else '-1'; n += 1; ok += (pred == mes)
        if pred != mes: ex.append((r['p'], w2))
print(f"\nFLANC DE 2:1, cellules archivees hors resonance exacte (1.80..2.30) : {n} cellules, direction derivee retrouvee {ok}/{n}, exceptions {ex}")
z = [(r['p'], r['ln']) for r in D if abs(r['w2'] - 2.0) < 1e-9]
print(f"RESONANCE EXACTE 2:00 (asymetrie nulle derivee) : " + ", ".join(f"p={p} A={A:+.4f}" for p, A in z) + "  (contre 0.13 a 0.56 sur les flancs)")
r95 = next(r for r in D if r['p'] == 9 and abs(r['w2'] - 2.5) < 1e-9)
print(f"9|2.50 : derive '-1' si le flanc droit de 2:1 domine a dw2 = +0.5 ; mesure {'+1' if r95['ln'] < 0 else '-1'} (A = {r95['ln']:+.3f})")
print("\nPREDICTIONS DE DIRECTION POUR LES CELLULES VIERGES (a geler par m2 ; porte : asymetrie mesuree > 2 pour cent, sinon 'sans porte') :")
for cell, a, b, cote in (('7|1.45', 3, 2, -1), ('7|1.55', 3, 2, +1), ('7|3.90', 4, 1, -1), ('7|4.10', 4, 1, +1)):
    print(f"  {cell} : fragile {fragile(a, b, cote)} (flanc {'gauche' if cote < 0 else 'droit'} de {a}:{b})  ->  A = ln(s+/s-) {'< 0' if fragile(a,b,cote)=='+1' else '> 0'}")
print("  7|2.50|+1 : fragile -1 si le flanc droit de 2:1 domine a dw2 = +0.5 (comme a 9|2.50) -> s*(+1) > s*(-1) = 1.198113 ; la 5:2 exacte est symetrique au premier ordre")
print("  13|1.90 et 13|2.10 : signes A < 0 et A > 0 (derives) ; |A| dans [0.095, 0.125] (grandeur, NON derivee, tolerance fixee AVANT run) ; le test de la variable (p-1)/(p-2) n'est PAS a p = 13")
