# -*- coding: ascii -*-
"""BALAYAGE DE VIRGINITE DU GEL "PONT" -- machine 1, v1, 2026-11-17. Recherche de texte ; aucun calcul de physique.
Cherche, dans tous les fichiers d'une arborescence, les seize w2 candidats du gel : (a) leur fraction irreductible, isolee ;
(b) leur ecriture au millieme a moins de seize caracteres apres "w2" ; (c) dans les JSON, une cle "delta" de valeur w2 - 2.
Dit, par fichier touche, s'il a le NOM d'une sortie 2D (sonde_, verdict, gb<chiffre>, boite, lisse_2d, pont_2d) : c'est un
nom, pas une preuve. Une recherche de texte n'est pas une preuve d'absence.
Usage : python3 -I balayage_virginite_pont_machine1_v1.py <arborescence> <sortie.json> [<sous-dossier a exclure> ...]"""
import sys, os, re, json
from fractions import Fraction as F
RACINE, SORTIE = sys.argv[1].rstrip("/"), sys.argv[2]; EXCLUS_D = [os.path.normpath(os.path.join(RACINE, x)) for x in sys.argv[3:]]
EXCLUS = (F(1982, 1000), F(2017, 1000))
CAND = [F(k, 1000) for k in list(range(1981, 1990)) + list(range(2011, 2020)) if F(k, 1000) not in EXCLUS]
assert len(CAND) == 16
motifs = {}
for w in CAND:
    fr = "%d/%d" % (w.numerator, w.denominator); dec = "%.3f" % float(w); d = float(w) - 2.0
    motifs[str(w)] = [re.compile(r"(?<![0-9/.])" + re.escape(fr) + r"(?![0-9/])"),
                      re.compile(r"w2[^0-9\n]{0,16}" + re.escape(dec) + r"(?![0-9])"),
                      re.compile(r"\"delta\"\s*:\s*" + re.escape("%.3f" % d if d < 0 else "0.%03d" % round(d * 1000)) + r"0*(?![0-9])")]
NOM_2D = re.compile(r"sonde_|verdict|gb[0-9]|boite|lisse_2d|pont_2d")
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
n2d = sorted(p for p in touches if NOM_2D.search(os.path.basename(p)))
print("arborescence : %s ; fichiers lus : %d ; fichiers qui portent un w2 candidat : %d ; dont au nom d'une sortie 2D : %d" % (RACINE, lus, len(touches), len(n2d)))
par_w = {str(w): sum(1 for p in touches if str(w) in touches[p]) for w in CAND}
print("par w2 candidat (fichiers) : %s" % "  ".join("%s %d" % (str(w), par_w[str(w)]) for w in CAND))
noms = sorted(set(os.path.basename(p) for p in touches))
print("noms distincts des fichiers touches (%d) :" % len(noms))
for n in noms: print("   %s" % n)
for p in n2d: print("AU NOM D'UNE SORTIE 2D : %s -> %s" % (p, sorted(touches[p])))
json.dump({"racine": RACINE, "lus": len([0]) and lus, "touches": touches, "noms": noms, "nom_2d": n2d, "par_w2": par_w, "exclus": sys.argv[3:]}, open(SORTIE, "w"), indent=1, sort_keys=True)
