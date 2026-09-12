#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""D'OU VIENNENT LES NOMBRES DE LA BORNE : SA NOTE DE LECTURE EST A CORRIGER.
machine 2, v1, 12/09/2026.

Sa cloture (section 3) porte : "ratios() lit les logs a trois decimales -- assez pour la
classe, pas pour un bit ; LES GRANDEURS DE LA BORNE, ELLES, VIENNENT DES JSON EN PLEINE
PRECISION."

La premiere moitie est juste et bien vue. LA SECONDE EST FAUSSE : borne() divise DP par
le ratio issu de ratios(), c'est-a-dire PAR LE NOMBRE A TROIS DECIMALES. Seuls les e de
la correction conservatrice viennent des JSON.

Cette feuille le montre, et le CHIFFRE : elle recalcule INF des deux facons.

L'ISSUE QUI MORD, ecrite avant : si l'ecart depassait la largeur de la fenetre (x1.04,
soit 4 pour cent), la carte des marges changerait et la correction ne serait plus de
forme mais de fond.

Les chemins sont des ARGUMENTS.
"""
import json, re, sys
from fractions import Fraction as F

if len(sys.argv) < 5:
    sys.exit("usage : precision_de_la_borne_machine2_v1.py <log prevol m2> "
             "<json prevol m2> <json reference> <sup m=2>")
LOG, JPRE, JREF, SUP2 = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4])
OK, MORD = [], []


def chk(q, c, d=''):
    OK.append(bool(c))
    if not c:
        MORD.append((q, d))
    print("  [%s] %-56s %s" % ("OK  " if c else "MORD", q[:56], d))


def ratios_du_log(log):
    L = [l for l in open(log, encoding="utf-8") if "T2-" in l and "e/seuil" in l]
    return {re.search(r"T2-(\S+)", l).group(1):
            float(re.search(r"e/seuil=([0-9.]+)", l).group(1)) for l in L}


PRE = json.load(open(JPRE, encoding="utf-8"))["T2"]["points"]
REF = json.load(open(JREF, encoding="utf-8"))["T2"]["points"]
R_LOG = ratios_du_log(LOG)
R_JSON = {k: PRE[k]["ratio_seuil"] for k in PRE}
DP = float(F(1, 102400))

print("=" * 92)
print("D'OU VIENNENT LES NOMBRES DE LA BORNE")
print("=" * 92)

print("\n[1] LES DEUX SOURCES, CELLULE PAR CELLULE")
print("      %-9s %14s %20s   %s" % ("cellule", "log (3 dec.)", "JSON (pleine prec.)",
                                     "ecart rel."))
for k in sorted(R_LOG, key=lambda c: (int(c.split("|")[0]), float(c.split("|")[1]))):
    print("      %-9s %14.3f %20.14f   %.2e"
          % (k, R_LOG[k], R_JSON[k], abs(R_JSON[k] / R_LOG[k] - 1)))
chk("le log tronque bien a trois decimales",
    all(abs(R_LOG[k] - round(R_LOG[k], 3)) < 1e-12 for k in R_LOG))


def borne(rt):
    d = {}
    for k in rt:
        r = rt[k] * min(PRE[k]["err"]["dt2/2"]["e"], REF[k]["err"]["dt2/2"]["e"]) \
            / PRE[k]["err"]["dt2/2"]["e"]
        d[k] = DP / r
    return d


print("\n[2] INF, CALCULE DES DEUX FACONS")
dl, dj = borne(R_LOG), borne(R_JSON)
il, ij = max(dl.values()), max(dj.values())
kl, kj = max(dl, key=dl.get), max(dj, key=dj.get)
print("      depuis le LOG  (ce que la feuille fait) : %.9e  porte par %s" % (il, kl))
print("      depuis le JSON (pleine precision)       : %.9e  porte par %s" % (ij, kj))
print("      ecart relatif                            : %.3e" % abs(ij / il - 1))
chk("le meme point porte la borne dans les deux", kl == kj, kl)
chk("SA PHRASE 'les grandeurs de la borne viennent des JSON' est JUSTE",
    il == ij,
    "FAUSSE : le RATIO vient du log a 3 decimales ; seuls les e de la correction "
    "conservatrice viennent des JSON. Ecart sur INF : %.3e" % abs(ij / il - 1))

print("\n[3] L'EFFET SUR LA CARTE -- de forme, ou de fond ?")
print("      fenetre a m=2, kT=1 : x%.4f (log)   x%.4f (JSON)" % (SUP2 / il, SUP2 / ij))
chk("l'ecart reste tres inferieur a la largeur de la fenetre",
    abs(ij / il - 1) < 0.01 * (SUP2 / il - 1),
    "%.3e contre une marge de %.3e -- la correction est de FORME"
    % (abs(ij / il - 1), SUP2 / il - 1))
for kT in (1.00, 1.15, 1.30):
    a = "x%.4f" % (SUP2 / (kT * il)) if kT * il <= SUP2 else "VIDE"
    b = "x%.4f" % (SUP2 / (kT * ij)) if kT * ij <= SUP2 else "VIDE"
    print("      kT=%.2f, m=2 : %-8s (log)   %-8s (JSON)   %s"
          % (kT, a, b, "identique" if a == b or (a == "VIDE" and b == "VIDE") else "DIFFERE"))
chk("aucune cellule de la carte ne change de statut",
    all((kT * il <= SUP2) == (kT * ij <= SUP2) for kT in (1.00, 1.15, 1.30, 1.50, 1.74)))

print("\n[4] CE QUE J'EN TIRE")
print("      La correction est GRATUITE : le JSON est a mon poste, en pleine precision,")
print("      et c'est deja lui qui fournit les e de la correction conservatrice. Lire")
print("      le ratio au meme endroit ne coute pas un run.")
print("      MAIS elle ne se fait pas ici : la feuille de derivation est DEPOSEE au lot")
print("      7883311c6e363b02 et relue par machine 1 ; l'editer perimerait sa lecture.")
print("      Elle se fait a l'acte constante A, avec le reste -- et c'est la que la")
print("      borne sera CITEE, donc le bon endroit pour qu'elle soit exacte.")

print("\n" + "=" * 92)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s" % q)
    print("         %s" % d)
print("(le mordant de [2] est la correction elle-meme : il DOIT mordre)")
print("=" * 92)
