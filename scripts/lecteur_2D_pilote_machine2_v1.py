# -*- coding: ascii -*-
"""PILOTE DE LECTURE 2D DU VIDE, machine 2, 2026-11-21, hors chaine (classe 3) : exploration, AUCUN verdict, AUCUN gel, AUCUN depot.
DERIVE de la sonde deposee lot_b1919dc9468dc437__sonde_vide_machine1_v1.py (NON EDITEE). Ce qui est identique : le moteur (canon controle), le bloc "LECTEUR CREUX" de sonde_lecteur_gel_loi_machine1_v1.py (canon controle ;
le texte du bloc est ecrit tel quel dans un fichier de travail puis IMPORTE comme un module, avec ses dependances M, np, sp, sl, math posees avant l'import : assembler, restreindre, table_W, lire_etat, trajectoire),
les quatre absorbeurs A, B, C, D, les douze barreaux k = -3 a 8 (eta_k = eta0 2^(-k)), le site (0, 0), l'energie de depart 0, la geometrie r_c = 2 (m + max(8, m)) + 2 (sauf --rc).
Ce qui est LIBRE (la sonde deposee le refuse hors de la table du gel) : la cellule (w2 en fraction, g, m), eta0 (la sonde fixe |w2 - 2|, echelle du canal 2:1 ; ici donne en argument, prevu |delta| du canal lu), le signe
(un processus = une cellule et un signe, comme "les appels sont independants"), et le sous-ensemble d'absorbeurs.
Signe -1 = le fantome (diagonale -W1 a + w2 b : canal (a, b) de desaccord -a + b w2) ; signe +1 = le jumeau sans fantome (largeur fabriquee par l'absorbeur seul).
Usage : py -3.11 -P lecteur_2D_pilote_machine2_v1.py <moteur> <bloc source> <dossier de sortie> <id> <w2 en fraction> <g> <m> <eta0> <signe +1 ou -1> [--rc N] [--abs ABCD]
Ecrit lect2D_<id>_<fantome ou jumeau>.json ; imprime Gamma par absorbeur."""
import hashlib
import importlib.util
import json
import math
import os
import platform
import sys
import time
import unicodedata
from fractions import Fraction as F

import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as sl

MOTEUR, SOURCE_BLOC, DOSSIER, IDENT, W2S, GS, MS, ETA0S, SIGNES = sys.argv[1:10]
OPT = sys.argv[10:]
CANON_MOTEUR, CANON_SOURCE_BLOC = "82a0be882568fe0c", "d5cc48f48e37af99"
KS = list(range(-3, 9))
ABSORBEURS_TOUS = [("A", "F2", 0, 80), ("B", "F2", 0, 100), ("C", "F1", 0, 100), ("D", "F2", 10, 80)]


def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


for chemin, attendu, quoi in ((MOTEUR, CANON_MOTEUR, "moteur"), (SOURCE_BLOC, CANON_SOURCE_BLOC, "la sonde deposee du lecteur")):
    if canon_B(chemin) != attendu:
        raise SystemExit("REFUS : le canon de %s (%s) n'est pas %s" % (quoi, canon_B(chemin), attendu))
w2 = F(W2S)
g = float(GS)
m = int(MS)
eta0 = float(ETA0S)
signe = int(SIGNES)
assert signe in (-1, 1)
r_c = 2 * (m + max(8, m)) + 2
if "--rc" in OPT:
    r_c = int(OPT[OPT.index("--rc") + 1])
noms_abs = OPT[OPT.index("--abs") + 1] if "--abs" in OPT else "ABCD"
ABSORBEURS = [a for a in ABSORBEURS_TOUS if a[0] in noms_abs]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
src = open(SOURCE_BLOC, encoding="ascii").read()
i0 = src.index("# --- LECTEUR CREUX")
i1 = src.index("# --- fin du bloc ---", i0)
texte_bloc = src[i0:i1]
CANON_BLOC = hashlib.sha256(texte_bloc.encode("ascii")).hexdigest()[:16]
os.makedirs(DOSSIER, exist_ok=True)
fichier_bloc = os.path.join(DOSSIER, "bloc_lecteur_depose_%s_%s_%d.py" % (CANON_BLOC, IDENT, signe))
open(fichier_bloc, "w", encoding="ascii", newline="\n").write(texte_bloc)
assert hashlib.sha256(open(fichier_bloc, "rb").read()).hexdigest()[:16] == CANON_BLOC
spec_b = importlib.util.spec_from_file_location("bloc_lecteur_depose", fichier_bloc)
B = importlib.util.module_from_spec(spec_b)
for nom, val in (("M", M), ("np", np), ("sp", sp), ("sl", sl), ("math", math)):
    setattr(B, nom, val)
spec_b.loader.exec_module(B)
assembler, restreindre, table_W, trajectoire = B.assembler, B.restreindre, B.table_W, B.trajectoire
ITER_MIN, ITER_MAX, TOL_RESIDU, POIDS_MIN = B.ITER_MIN, B.ITER_MAX, B.TOL_RESIDU, B.POIDS_MIN
os.remove(fichier_bloc)

t0 = time.time()
geo = [(a, forme, r_c + dr, L, r_c + dr + L) for a, forme, dr, L in ABSORBEURS]
Nmax = max(x[4] for x in geo)
H0m, dm = assembler(w2, g, Nmax, signe=signe)
rec = {"signe": signe, "site": [0, 0], "E_depart": 0.0, "traj": {}, "absorbeurs": {a: {"forme": forme, "bord": bord, "couches": L, "N": N} for a, forme, bord, L, N in geo}}
for a, forme, bord, L, N in geo:
    H0, dg = restreindre(H0m, dm, Nmax, N)
    rec["traj"][a] = trajectoire(H0, dg, table_W(N, forme, bord, L), eta0, N, (0, 0), 0.0, KS)
    g3 = rec["traj"][a]["3"]["gamma"]
    p3 = rec["traj"][a]["3"]["poids_site"]
    print("  %s signe %+d absorbeur %s : suivi %d/%d ; Gamma(k = 3) = %s ; poids du site %s (%.0f s)" % (
        IDENT, signe, a, sum(rec["traj"][a][str(k)]["suivi"] for k in KS), len(KS), ("%.4e" % g3) if g3 is not None else "None", ("%.6f" % p3) if p3 is not None else "None", time.time() - t0), flush=True)
rec["duree_s"] = round(time.time() - t0, 1)
sortie = {"pilote": "lecteur_2D_pilote_machine2_v1", "pilote_canon": canon_B(os.path.abspath(__file__)), "moteur_canon": canon_B(MOTEUR), "source_bloc_canon": canon_B(SOURCE_BLOC), "bloc_sha256_16": CANON_BLOC,
          "cellule": {"id": IDENT, "w2": str(w2), "m": m, "g": GS, "r_c": r_c, "eta0": eta0, "P": int(M.P), "W1": float(M.W1)},
          "reglage": {"ks": KS, "absorbeurs": [list(a) for a in ABSORBEURS], "iter_min": ITER_MIN, "iter_max": ITER_MAX, "tol_residu": TOL_RESIDU, "poids_min": POIDS_MIN},
          "plateforme": {"systeme": platform.system(), "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__, "coeurs": os.cpu_count()},
          "lecture": rec, "duree_s": round(time.time() - t0, 1)}
chemin = os.path.join(DOSSIER, "lect2D_%s_%s.json" % (IDENT, "fantome" if signe == -1 else "jumeau"))
json.dump(sortie, open(chemin, "w"), indent=1, sort_keys=True)
print("ecrit lect2D_%s_%s.json (%.0f s)" % (IDENT, "fantome" if signe == -1 else "jumeau", time.time() - t0))
