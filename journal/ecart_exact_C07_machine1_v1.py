# -*- coding: ascii -*-
"""ECART EXACT ENTRE DEUX VERDICTS (reponse a la morsure C07 du contreseing e8ff4d600edf89ef) -- machine 1, v1, 2026-11-15.
Pour chaque feuille flottante Gamma_pl qui differe entre le verdict de BOCAL4 (x) et celui que machine 1 a rejoue (y) :
l'ecart relatif en ARITHMETIQUE EXACTE (fractions : un double est un rationnel), rapporte a x puis a y ; et les deux
quotients calcules en flottants, |x/y - 1| et |y/x - 1|, qui tombent sur la grille des doubles voisins de 1 (pas 2^-53
sous 1, 2^-52 au-dessus). Aucune largeur n'est calculee : deux fichiers JSON sont compares.
Usage : python3 -I ecart_exact_C07_machine1_v1.py <verdict de BOCAL4> <verdict rejoue> [<verdict de BOCAL4> <verdict rejoue> ...]"""
import sys, json
from fractions import Fraction as F
L = []
def marche(x, y, ch):
    if isinstance(x, dict):
        for k in x:
            marche(x[k], y[k], ch + "/" + str(k))
    elif isinstance(x, list):
        assert len(x) == len(y), ch
        for i, (u, v) in enumerate(zip(x, y)):
            marche(u, v, ch + "/%d" % i)
    elif isinstance(x, float) and x != y and ch.endswith("/Gamma_pl"):
        ex = abs(F(x) - F(y))
        L.append({"chemin": ch, "x": x, "y": y, "exact_sur_x": float(ex / abs(F(x))), "exact_sur_y": float(ex / abs(F(y))), "q_xy": abs(x / y - 1.0), "q_yx": abs(y / x - 1.0)})
args = sys.argv[1:]
for a, b in zip(args[0::2], args[1::2]):
    marche(json.load(open(a)), json.load(open(b)), "")
m = max(L, key=lambda l: l["exact_sur_x"])
print("feuilles Gamma_pl differentes : %d" % len(L))
print("plus grand ecart relatif EXACT : %.6e rapporte a BOCAL4, %.6e rapporte au rejeu" % (max(l["exact_sur_x"] for l in L), max(l["exact_sur_y"] for l in L)))
print("plus grand quotient en flottants : |x/y - 1| = %.6e ; |y/x - 1| = %.6e" % (max(l["q_xy"] for l in L), max(l["q_yx"] for l in L)))
print("etat du maximum exact : %s" % m["chemin"])
print("  x (BOCAL4) = %r ; y (rejeu) = %r" % (m["x"], m["y"]))
print("  exact %.6e ; |x/y - 1| = %.6e = %.1f x 2^-53 ; |y/x - 1| = %.6e = %.1f x 2^-53" % (m["exact_sur_x"], m["q_xy"], m["q_xy"] / 2.0 ** -53, m["q_yx"], m["q_yx"] / 2.0 ** -53))
print("L'ACTE ECRIT \"7.2e-15 au plus\" : %s" % ("VRAI (le maximum exact ne depasse pas 7.2e-15)" if max(max(l["exact_sur_x"], l["exact_sur_y"]) for l in L) <= 7.2e-15 else "FAUX"))
