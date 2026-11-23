# -*- coding: ascii -*-
"""BALAYAGE DE VIRGINITE DU GEL "SOMMET" -- machine 1, v1, 2026-11-22. Recherche de texte ; aucun calcul de physique.
Derive de balayage_virginite_pont_machine1_v1.py (registre). Cherche, dans tous les fichiers d'une arborescence, les 80 w2
candidats du gel, PUIS les deux w2 retires de la liste (3999/2000 et 4001/2000, comptes a part) : (a) leur fraction irreductible, isolee ; (b) leur ecriture decimale (cinq decimales, ou sans ses zeros
de fin) a moins de seize caracteres apres "w2" ; (c) dans les JSON, une cle "delta" de valeur w2 - 2 (ecriture decimale ou
a exposant) ; (d) leur ecriture a cinq decimales, isolee, ou qu'elle soit. Dit, par fichier touche, s'il a le NOM d'une sortie 2D (sonde_, verdict, gb<chiffre>, boite, lisse_2d,
pont_2d, lect2D) : c'est un nom, pas une preuve. Une recherche de texte n'est pas une preuve d'absence.
Usage : python3 -I balayage_virginite_sommet_machine1_v1.py <arborescence> <sortie.json> [<sous-dossier a exclure> ...]"""
import sys, os, re, json
from fractions import Fraction as F
RACINE, SORTIE = sys.argv[1].rstrip("/"), sys.argv[2]; EXCLUS_D = [os.path.normpath(os.path.join(RACINE, x)) for x in sys.argv[3:]]
PAS = F(1, 100000)
CAND = sorted([F(2) + s * k * PAS for s in (-1, 1) for k in range(5, 21) if k != 10] + [F(2) + s * k * PAS for s in (-1, 1) for k in range(25, 50)])
RETIRES = [F(3999, 2000), F(4001, 2000)]
assert len(CAND) == 80 and all(w not in CAND for w in RETIRES) and F(20001, 10000) not in CAND and F(19999, 10000) not in CAND and F(2) not in CAND
motifs = {}
for w in CAND + RETIRES:
    fr = "%d/%d" % (w.numerator, w.denominator); dec = "%.5f" % float(w); court = dec.rstrip("0"); d = float(w) - 2.0
    dd = sorted(set([("%.5f" % d), ("%.5f" % d).rstrip("0"), repr(float("%.5e" % d)), "%.0e" % d, ("%.1e" % d)]))
    motifs[str(w)] = [re.compile(r"(?<![0-9/.])" + re.escape(fr) + r"(?![0-9/])"),
                      re.compile(r"w2[^0-9\n]{0,16}(?:" + re.escape(dec) + "|" + re.escape(court) + r")(?![0-9])"),
                      re.compile(r"\"delta\"\s*:\s*(?:" + "|".join(re.escape(x) for x in dd) + r")(?![0-9])"),
                      re.compile(r"(?<![0-9.eE+-])" + re.escape(dec) + r"(?![0-9])")]
NOM_2D = re.compile(r"sonde_|verdict|gb[0-9]|boite|lisse_2d|pont_2d|lect2D")
lus = 0; touches = {}
for d, ds, fs in os.walk(RACINE):
    ds[:] = [x for x in ds if x != ".git" and os.path.normpath(os.path.join(d, x)) not in EXCLUS_D]
    for f in fs:
        p = os.path.join(d, f)
        try: t = open(p, "rb").read().decode("utf-8", "replace")
        except OSError: continue
        lus += 1
        for w, ms in motifs.items():
            formes = [i for i, m in enumerate(ms) if m.search(t)]
            if formes: touches.setdefault(os.path.relpath(p, RACINE), {})[w] = formes
print("arborescence : %s ; exclus : %s" % (RACINE, sys.argv[3:] or "aucun"))
ret = {str(w): sorted(p for p in touches if str(w) in touches[p]) for w in RETIRES}
for p in list(touches):
    touches[p] = {w: v for w, v in touches[p].items() if w not in ret}
    if not touches[p]: del touches[p]
n2d = sorted(p for p in touches if NOM_2D.search(os.path.basename(p)))
par_w = {str(w): sum(1 for p in touches if str(w) in touches[p]) for w in CAND}
print("fichiers lus : %d ; fichiers qui portent un w2 candidat : %d ; dont au nom d'une sortie 2D : %d" % (lus, len(touches), len(n2d)))
print("w2 candidats touches : %d sur %d : %s" % (sum(1 for v in par_w.values() if v), len(CAND), "  ".join("%s %d" % (w, v) for w, v in par_w.items() if v) or "aucun"))
noms = sorted(set(os.path.basename(p) for p in touches))
print("noms distincts des fichiers touches (%d) :" % len(noms))
for n in noms: print("   %s  [formes %s ; %d w2]" % (n, sorted(set(i for p in touches if os.path.basename(p) == n for v in touches[p].values() for i in v)),
                                                  len(set(w for p in touches if os.path.basename(p) == n for w in touches[p]))))
for w in ret: print("w2 RETIRE %s : %d fichiers : %s" % (w, len(ret[w]), ", ".join(sorted(set(os.path.basename(p) for p in ret[w]))) or "aucun"))
for p in n2d: print("AU NOM D'UNE SORTIE 2D : %s -> %s" % (p, sorted(touches[p])))
json.dump({"racine": RACINE, "lus": lus, "touches": touches, "noms": noms, "nom_2d": n2d, "par_w2": par_w, "retires": ret, "exclus": sys.argv[3:]}, open(SORTIE, "w"), indent=1, sort_keys=True)
