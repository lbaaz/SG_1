# -*- coding: ascii -*-
"""SONDE DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16. CLASSE 2. Elle MESURE et ne juge pas.
Lit, par le LECTEUR CREUX DEPOSE, l'etat que porte le site (0, 0) a UNE cellule de la table gelee :
  "fantome" : le hamiltonien 2D du moteur (signe -1), depuis l'energie 0 ;
  "jumeau"  : le jumeau sans fantome (signe +1), meme couplage, meme geometrie : une largeur que seul l'absorbeur fabrique.
Le lecteur n'est pas recopie : le bloc "LECTEUR CREUX" est lu dans sonde_lecteur_gel_loi_machine1_v1.py (registre), dont le
canon est controle, et execute tel quel (assembler, restreindre, table_W, lire_etat, trajectoire).
Geometrie, la meme pour les deux : r_c = 2 (m + max(8, m)) + 2 ; eta0 = |w2 - 2| ; absorbeurs A (F2, 80 couches), B (F2, 100),
C (F1, 100), D (F2, bord r_c + 10, 80) ; boite N = bord + couches ; barreaux k = -3 a 8, eta_k = eta0 2^(-k).
Aucun etage dense : l'etiquette est (0, 0), l'energie de depart 0.
--prevol : la table n'est PAS celle du gel ; le FANTOME N'EST PAS LU (aucune largeur 2D du vide du fantome avant le run), le
jumeau seul l'est ; un w2 candidat du gel est refuse. Sans --prevol la table doit etre au canon du gel.
Usage : python -I sonde_vide_machine1_v1.py <moteur_v17.py> <sonde_lecteur_gel_loi_machine1_v1.py> <table des cellules.json>
        <dossier de sortie> <id de la cellule> [--prevol]
Ecrit sonde_vide_<id>.json. Les appels sont independants : un processus par cellule."""
import sys, os, math, json, time, hashlib, unicodedata, importlib.util, platform
from fractions import Fraction as F
import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as sl
MOTEUR, SOURCE_BLOC, TABLE, DOSSIER, IDENT = sys.argv[1:6]
PREVOL = "--prevol" in sys.argv[6:]
CANON_MOTEUR, CANON_SOURCE_BLOC, CANON_TABLE = "82a0be882568fe0c", "d5cc48f48e37af99", "b71206e5daf6c741"
KS = list(range(-3, 9))
ABSORBEURS = [("A", "F2", 0, 80), ("B", "F2", 0, 100), ("C", "F1", 0, 100), ("D", "F2", 10, 80)]

def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

for chemin, attendu, quoi in ((MOTEUR, CANON_MOTEUR, "moteur"), (SOURCE_BLOC, CANON_SOURCE_BLOC, "la sonde deposee du lecteur")):
    if canon_B(chemin) != attendu:
        raise SystemExit("REFUS : le canon de %s (%s) n'est pas %s" % (quoi, canon_B(chemin), attendu))
if (canon_B(TABLE) == CANON_TABLE) == PREVOL:
    raise SystemExit("REFUS : sans --prevol la table doit etre au canon %s ; avec --prevol elle ne doit pas l'etre" % CANON_TABLE)
T = json.load(open(TABLE)); CELLULES = {str(c["id"]): c for c in T["cellules"]}
if IDENT not in CELLULES:
    raise SystemExit("REFUS : la cellule %s n'est pas dans la table" % IDENT)
C = CELLULES[IDENT]
w2 = F(str(C["w2"])); m = int(C["m"]); g = float(str(C["g"])); r_c = 2 * (m + max(8, m)) + 2; eta0 = abs(float(w2) - 2.0)
if "%.5e" % g != str(C["g"]) or int(C["r_c"]) != r_c or abs(float(C["eta0"]) - eta0) > 0.0 or [list(a) for a in ABSORBEURS] != T["regle"]["absorbeurs_du_lecteur"] or T["regle"]["barreaux"] != KS:
    raise SystemExit("REFUS : la cellule %s de la table ne suit pas la regle (couplage ecrit, r_c, eta0, absorbeurs, barreaux)" % IDENT)
candidat = (w2 * 1000).denominator == 1 and (w2 * 100).denominator != 1 and abs(w2 - 2) < F(2, 100)
if PREVOL and candidat:
    raise SystemExit("REFUS : en pre-vol le w2 ne doit pas etre un candidat du gel")
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
src = open(SOURCE_BLOC, encoding="ascii").read()
i0 = src.index("# --- LECTEUR CREUX"); i1 = src.index("# --- fin du bloc ---", i0)
CANON_BLOC = hashlib.sha256(src[i0:i1].encode("ascii")).hexdigest()[:16]
exec(compile(src[i0:i1], "bloc_lecteur_depose", "exec"))

def lire(signe, nom):
    t0 = time.time()
    geo = [(a, forme, r_c + dr, L, r_c + dr + L) for a, forme, dr, L in ABSORBEURS]
    Nmax = max(x[4] for x in geo)
    H0m, dm = assembler(w2, g, Nmax, signe=signe)
    rec = {"signe": signe, "site": [0, 0], "E_depart": 0.0, "traj": {},
           "absorbeurs": {a: {"forme": forme, "bord": bord, "couches": L, "N": N} for a, forme, bord, L, N in geo}}
    for a, forme, bord, L, N in geo:
        H0, dg = restreindre(H0m, dm, Nmax, N)
        rec["traj"][a] = trajectoire(H0, dg, table_W(N, forme, bord, L), eta0, N, (0, 0), 0.0, KS)
    rec["duree_s"] = round(time.time() - t0, 1)
    print("  %s %s : %s (%.0f s)" % (IDENT, nom, " ".join("%s %d/%d" % (a, sum(rec["traj"][a][str(k)]["suivi"] for k in KS), len(KS)) for a, _, _, _, _ in geo), rec["duree_s"]), flush=True)
    return rec

sortie = {"sonde": "sonde_vide_machine1_v1", "sonde_canon": canon_B(os.path.abspath(__file__)), "table_canon": canon_B(TABLE), "prevol": PREVOL,
          "moteur_canon": canon_B(MOTEUR), "source_bloc_canon": canon_B(SOURCE_BLOC), "bloc_sha256_16": CANON_BLOC,
          "cellule": {"id": IDENT, "w2": str(C["w2"]), "m": m, "g": str(C["g"]), "r_c": r_c, "eta0": eta0},
          "reglage": {"ks": KS, "absorbeurs": [list(a) for a in ABSORBEURS], "iter_min": ITER_MIN, "iter_max": ITER_MAX, "tol_residu": TOL_RESIDU, "poids_min": POIDS_MIN},
          "plateforme": {"systeme": platform.system(), "machine": platform.machine(), "python": platform.python_version(),
                         "numpy": np.__version__, "scipy": scipy.__version__, "coeurs": os.cpu_count(),
                         "fils": {v: os.environ.get(v) for v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                         "levier": os.environ.get("NPY_DISABLE_CPU_FEATURES")}}
t0 = time.time()
sortie["jumeau"] = lire(+1, "jumeau")
sortie["fantome"] = None if PREVOL else lire(-1, "fantome")
sortie["duree_s"] = round(time.time() - t0, 1)
os.makedirs(DOSSIER, exist_ok=True)
chemin = os.path.join(DOSSIER, "sonde_vide_%s.json" % IDENT)
json.dump(sortie, open(chemin, "w"), indent=1, sort_keys=True)
print("ecrit %s (%.0f s)" % (chemin, time.time() - t0))
