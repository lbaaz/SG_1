# lecture_apres_coup_pole_court_machine1_v1.py -- machine 1, 2026-11-22
# LECTURE D'APRES COUP, SANS VALEUR D'EPREUVE, des 96 poles a deux dimensions (mon rejeu, identique a
# machine 2 a 2e-10 pres) contre deux chaines a une dimension :
#   C1 = chaine du PREMIER ordre sous absorbeur court (recalculee ici, pleine precision) ;
#   C2 = ma table d'ordre 2 de la section 5 de la note 6eae3f6860a46eef (cinq decimales).
# Question : a absorbeur faible, ou je n'avais ecrit aucun attendu, que vaut l'ecart, et a quoi ressemble-t-il ?
# Usage : python3 -I lecture_apres_coup_pole_court_machine1_v1.py <dossier de mon rejeu>
import sys, os, json, math, re
import numpy as np

DOS = sys.argv[1]

TABLE_TEXTE = """
    g = 5e-04          a = 2                      a = 4
    m_c = 10    0.05435 0.05435 0.05422    0.05436 0.05453 0.05440
    m_c = 11    0.05443 0.05450 0.05454    0.05439 0.05447 0.05435
    m_c = 12    0.05439 0.05442 0.05436    0.05439 0.05445 0.05441
    m_c = 13    0.05442 0.05446 0.05446    0.05440 0.05445 0.05443
    g = 1e-03          a = 2                      a = 4
    m_c = 10    0.05435 0.05435 0.05422    0.05436 0.05453 0.05440
    m_c = 11    0.05443 0.05450 0.05454    0.05439 0.05447 0.05435
    m_c = 12    0.05439 0.05442 0.05437    0.05439 0.05445 0.05441
    m_c = 13    0.05442 0.05446 0.05445    0.05440 0.05445 0.05443
    g = 5e-04          a = 0.5                    a = 1
    m_c = 10    0.04161 0.03937 0.03687    0.05253 0.05171 0.05054
    m_c = 11    0.06964 0.07371 0.07901    0.05584 0.05654 0.05749
    m_c = 12    0.04482 0.04306 0.04106    0.05342 0.05299 0.05235
    m_c = 13    0.06472 0.06725 0.07042    0.05515 0.05551 0.05599
    g = 1e-03          a = 0.5                    a = 1
    m_c = 10    0.04171 0.03947 0.03697    0.05255 0.05174 0.05058
    m_c = 11    0.06916 0.07301 0.07793    0.05581 0.05650 0.05743
    m_c = 12    0.04500 0.04326 0.04128    0.05345 0.05303 0.05240
    m_c = 13    0.06413 0.06644 0.06930    0.05513 0.05547 0.05592
"""
C2, g, ag, ad = {}, None, None, None
for l in TABLE_TEXTE.strip("\n").split("\n"):
    m = re.match(r"\s*g = (\S+)\s+a = (\S+)\s+a = (\S+)\s*$", l)
    if m:
        g, ag, ad = float(m.group(1)), float(m.group(2)), float(m.group(3))
        continue
    m = re.match(r"\s*m_c = (\d+)\s+(\S+) (\S+) (\S+)\s+(\S+) (\S+) (\S+)\s*$", l)
    v = [float(m.group(k)) for k in range(2, 8)]
    for i, m0 in enumerate((2, 3, 4)):
        C2[(g, int(m.group(1)), ag, m0)] = v[i]
        C2[(g, int(m.group(1)), ad, m0)] = v[3 + i]
assert len(C2) == 96

def tau(m):
    return (11.0 * m + 9.0) * (m + 1.0) * math.sqrt(2.0 * m + 1.0) / (36.0 * math.sqrt(6.0))

def chaine1(a, mc, m0):
    A = np.zeros((mc + 1, mc + 1), dtype=complex)
    for m in range(mc):
        A[m, m + 1] = A[m + 1, m] = tau(m)
    for m in range(m0 + 1, mc + 1):
        A[m, m] = -1j * a * tau(m) * ((m - m0) / float(mc - m0)) ** 2
    val, vec = np.linalg.eig(A)
    w = vec[0, :] ** 2 / np.einsum("ij,ij->j", vec, vec)
    return -2.0 * val[int(np.argmax(np.abs(w)))].imag

D2 = {}
for f in sorted(os.listdir(DOS)):
    s = json.load(open(os.path.join(DOS, f)))
    for c in s["cas"]:
        D2[(s["g"], s["m_coupe"], c["a"], c["m0"])] = c["gamma_sur_g"]
assert len(D2) == 96 and set(D2) == set(C2)
pire = max(max(json.load(open(os.path.join(DOS, f)))[k] for k in ("pire_ecart_gamma", "pire_ecart_re", "pire_ecart_poids")) for f in os.listdir(DOS))
print("=== 0. mon rejeu : 96 cas ; plus grand ecart a machine 2 (Gamma / g, Re E / g, poids) : %.1e" % pire)

print()
print("=== 1. 2D moins chaine : C1 (premier ordre) et C2 (ordre 2, table), par force d'absorbeur")
print("    a      g       max|2D - C1|  max|2D - C2|   cas ou C1 est plus pres que C2")
for a in (0.5, 1.0, 2.0, 4.0):
    for g in (5e-4, 1e-3):
        k = [x for x in D2 if x[2] == a and x[0] == g]
        d1 = [D2[x] - chaine1(a, x[1], x[3]) for x in k]
        d2 = [D2[x] - C2[x] for x in k]
        print("    %.1f  %.0e   %.2e      %.2e       %d sur %d" % (a, g, max(abs(v) for v in d1), max(abs(v) for v in d2), sum(1 for u, v in zip(d1, d2) if abs(u) < abs(v)), len(k)))

print()
print("=== 2. croissance avec g, cas par cas : (ecart a g = 1e-03) / (ecart a g = 5e-04) ; 4 = terme en g^2")
for a in (0.5, 1.0):
    r1, r2 = [], []
    for mc in (10, 11, 12, 13):
        for m0 in (2, 3, 4):
            c1 = chaine1(a, mc, m0)
            r1.append((D2[(1e-3, mc, a, m0)] - c1) / (D2[(5e-4, mc, a, m0)] - c1))
            r2.append((D2[(1e-3, mc, a, m0)] - C2[(1e-3, mc, a, m0)]) / (D2[(5e-4, mc, a, m0)] - C2[(5e-4, mc, a, m0)]))
    print("    a = %.1f : 2D - C1 : de %.2f a %.2f ; 2D - C2 : de %.2f a %.2f (C2 a cinq decimales)" % (a, min(r1), max(r1), min(r2), max(r2)))

print()
print("=== 3. signes a a = 0.5 : (2D - C1), (C2 - C1), par parite de coupe")
for par, nom in ((0, "paires  "), (1, "impaires")):
    k = [x for x in D2 if x[2] == 0.5 and x[1] % 2 == par]
    s1 = [D2[x] - chaine1(0.5, x[1], x[3]) for x in k]
    s2 = [C2[x] - chaine1(0.5, x[1], x[3]) for x in k]
    print("    coupes %s : 2D - C1 : %d negatifs, %d positifs ; C2 - C1 : %d negatifs, %d positifs" % (nom, sum(v < 0 for v in s1), sum(v > 0 for v in s1), sum(v < 0 for v in s2), sum(v > 0 for v in s2)))

for par, nom in ((0, "paires  "), (1, "impaires")):
    k = [x for x in D2 if x[2] == 1.0 and x[1] % 2 == par]
    s1 = [D2[x] - chaine1(1.0, x[1], x[3]) for x in k]
    print("    a = 1, coupes %s : 2D - C1 : %d negatifs, %d positifs" % (nom, sum(v < 0 for v in s1), sum(v > 0 for v in s1)))
fort1 = [abs(D2[x] - chaine1(x[2], x[1], x[3])) for x in D2 if x[2] in (2.0, 4.0)]
print("    48 cas forts : plus grand |2D - C1| = %.2e ; cas au-dessus de 2.5e-04 : %d" % (max(fort1), sum(v > 2.5e-4 for v in fort1)))
print()
print("=== 4. l'ecart 2D - C1 lu comme un changement de force d'absorbeur : d ln a = (2D - C1) / (dC1 / d ln a)")
print("    (derivee par differences centrees, pas 1e-4 en ln a) ; en unites de g^2 : d ln a / g^2")
print("    a     m_c  m0    d ln a (5e-04)  d ln a (1e-03)   / g^2 (5e-04)   / g^2 (1e-03)")
tout = {5e-4: [], 1e-3: []}
for a in (0.5, 1.0):
    for mc in (10, 11, 12, 13):
        for m0 in (2, 3, 4):
            c1 = chaine1(a, mc, m0)
            pente = (chaine1(a * math.exp(1e-4), mc, m0) - chaine1(a * math.exp(-1e-4), mc, m0)) / 2e-4
            d = [(D2[(g, mc, a, m0)] - c1) / pente for g in (5e-4, 1e-3)]
            tout[5e-4].append(d[0] / 25e-8)
            tout[1e-3].append(d[1] / 1e-6)
            print("    %.1f   %d   %d    %+.5f        %+.5f         %+.0f          %+.0f" % (a, mc, m0, d[0], d[1], d[0] / 25e-8, d[1] / 1e-6))
for g in (5e-4, 1e-3):
    v = tout[g]
    print("    g = %.0e : d ln a / g^2 de %+.0f a %+.0f ; tous negatifs : %s" % (g, min(v), max(v), "oui" if all(x < 0 for x in v) else "non"))
for mc in (10, 11, 12, 13):
    v = []
    for a in (0.5, 1.0):
        for m0 in (2, 3, 4):
            c1 = chaine1(a, mc, m0)
            pente = (chaine1(a * math.exp(1e-4), mc, m0) - chaine1(a * math.exp(-1e-4), mc, m0)) / 2e-4
            for g in (5e-4, 1e-3):
                v.append((D2[(g, mc, a, m0)] - c1) / pente / g ** 2)
    print("    m_c = %d : d ln a / g^2 de %+.0f a %+.0f (12 valeurs)" % (mc, min(v), max(v)))

print()
print("=== 5. le plateau a deux dimensions, a absorbeur fort (48 cas)")
fort = [D2[x] for x in D2 if x[2] in (2.0, 4.0)]
print("    de %.6f a %.6f ; moyenne %.6f ; reference absorbeur long, premier ordre : 0.054432" % (min(fort), max(fort), sum(fort) / 48.0))
for g in (5e-4, 1e-3):
    v = [D2[x] for x in D2 if x[2] in (2.0, 4.0) and x[0] == g]
    print("    g = %.0e : moyenne %.6f" % (g, sum(v) / 24.0))
v4 = [D2[x] for x in D2 if x[2] == 4.0 and x[1] in (12, 13)]
print("    a = 4, coupes 12 et 13 (12 cas) : de %.6f a %.6f ; moyenne %.6f" % (min(v4), max(v4), sum(v4) / 12.0))
d = [abs(D2[(1e-3, x[1], x[2], x[3])] - D2[x]) for x in D2 if x[0] == 5e-4 and x[2] in (2.0, 4.0)]
print("    |Gamma / g (1e-03) - Gamma / g (5e-04)|, 24 couples a absorbeur fort : plus grand %.2e ; moyenne %.2e" % (max(d), sum(d) / 24.0))
d4 = [abs(D2[(1e-3, x[1], x[2], x[3])] - D2[x]) for x in D2 if x[0] == 5e-4 and x[2] == 4.0]
print("    idem a a = 4 seul (12 couples) : plus grand %.2e" % max(d4))
