# -*- coding: ascii -*-
"""Exploration de reglage (hors chaine, classe 3) : les etats de points DEJA JOUES, hors des douze points juges du
delta 98, sous les quatre absorbeurs DU GEL. Lecteur : le bloc du gel, tel quel.
  A : F2, bord r_c, 80 couches ; B : F2, r_c, 100 ; C : F1, r_c, 100 ; D : F2, r_c + 10, 80.
Un premier jeu (A a 60 couches, B a 80, C = F1 a 80, D a 60) a ete explore par exploration_etats_machine1_v1.py ;
il a conduit a allonger chaque absorbeur de 20 couches (voir la note d'accompagnement).
Usage : python3 -I exploration_etats_machine1_v2.py <moteur.py> <bloc.py> <sortie.json> <sonde.json>:<id>[:<rang max>] [...]"""
import sys, json, math, time, importlib.util
from fractions import Fraction as F
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sl
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(sys.argv[2]).read(), sys.argv[2], "exec"))
SORTIE = sys.argv[3]; DEMANDES = sys.argv[4:]
KS = list(range(-3, 9))
CONFIGS = [("A", "F2", 0, 80), ("B", "F2", 0, 100), ("C", "F1", 0, 100), ("D", "F2", 10, 80)]
PLANCHER10 = 1.33e-12
try:
    sortie = json.load(open(SORTIE))
except Exception:
    sortie = {"points": {}}
t0 = time.time()
for dem in DEMANDES:
    morceaux = dem.split(":"); chemin, pid = morceaux[0], morceaux[1]; rang_max = int(morceaux[2]) if len(morceaux) > 2 else 99
    p = [q for q in json.load(open(chemin))["points"] if q["id"] == pid][0]
    num, den = p["w2"].split("/"); w2 = F(int(num), int(den)); g = p["g"]; r_c = p["r_c"]; eta0 = p["eta0"]
    Nmax = r_c + 100
    H0m, dm = assembler(w2, g, Nmax)
    pt = sortie["points"].setdefault(pid, {"w2": p["w2"], "facteur": p["facteur"], "g": g, "r_c": r_c, "eta0": eta0, "rang_max": rang_max, "etats": {}})
    blocs = {}
    for nom, forme, dr, L in CONFIGS:
        N = r_c + dr + L; H0, dg = restreindre(H0m, dm, Nmax, N); blocs[nom] = (H0, dg, table_W(N, forme, r_c + dr, L), N)
    print("%s : assemblage Nmax = %d, %.0f s" % (pid, Nmax, time.time() - t0), flush=True)
    for e in p["etats"]:
        G = e.get("Gamma_2D") or {}
        if G.get("3") is None or G["3"] <= PLANCHER10 or e["rang"] > rang_max:
            continue
        cle = "%d_%d" % (int(e["n1"]), int(e["n2"]))
        if cle in pt["etats"]:
            continue
        rec = {"rang": e["rang"], "n1": int(e["n1"]), "n2": int(e["n2"]), "E_re": e["E_re"], "G2D": G, "J_ecart_type": e.get("J_ecart_type"),
               "poids_site_dense": e.get("poids_site"), "cfg": {}}
        for nom, forme, dr, L in CONFIGS:
            H0, dg, W, N = blocs[nom]
            tr = trajectoire(H0, dg, W, eta0, N, (int(e["n1"]), int(e["n2"])), e["E_re"], KS)
            rec["cfg"][nom] = tr
        pt["etats"][cle] = rec
        json.dump(sortie, open(SORTIE, "w"), indent=1, sort_keys=True)
        s = "  %s rang %2d (%2d,%d) G3 %.3e :" % (pid, e["rang"], e["n1"], e["n2"], G["3"])
        for nom in "ABCD":
            v = [rec["cfg"][nom][str(k)]["gamma"] / G["3"] for k in KS]; ok = sum(rec["cfg"][nom][str(k)]["suivi"] for k in KS)
            best = min(max(v[i:i + 5]) / min(v[i:i + 5]) - 1.0 for i in range(len(KS) - 4))
            s += " %s %.4f(%d) " % (nom, best, ok)
        print(s + " (%.0f s)" % (time.time() - t0), flush=True)
print("fini %.0f s" % (time.time() - t0))
