# -*- coding: ascii -*-
"""Regard : sauts t_m de l'echelle du vide et decalages d'ordre 2 au point sacrifie, pour situer ou le dehors cesse d'etre une
echelle (|t_m| de l'ordre du desaccord 1 des echelles voisines). machine 1, 2026-11-16, hors chaine, classe 3.
Usage : python3 -I -B pont_sauts_regard_machine1_v1.py <moteur> <bloc ordre 2> <w2> <sortie.json> <g> [<g> ...]"""
import sys, math, json, importlib.util
from fractions import Fraction as F
MOTEUR, BLOC2, W2S, SORTIE = sys.argv[1:5]; out = {"piece": "pont_sauts_regard_machine1_v1", "w2": W2S, "points": []}
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec"))
w2 = F(W2S)
for GS in sys.argv[5:]:
    g = float(GS); sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites)
    ms = sorted(m for m in tb["t"] if m >= 0)
    print("g = %s ; sites tabules : %d a %d ; bord de barriere m2_bord = %s" % (GS, ms[0], ms[-1], tb["m2_bord"]))
    print("  m : |t_m| ; S_m - S_0   " + "   ".join("%d : %.3f ; %+.4f" % (m, abs(tb["t"][m]), tb["S"][m] - tb["S"][0]) for m in ms if m in (2, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 20, 22, 25, 28, 31) and m in tb["S"]))
    rec = {"g": GS, "m_bord": tb["m2_bord"], "t": {str(m): abs(tb["t"][m]) for m in ms}, "S": {str(m): tb["S"][m] - tb["S"][0] for m in ms if m in tb["S"]}, "seuils": {}}; out["points"].append(rec)
    for seuil in (0.25, 0.5, 1.0):
        mm = [m for m in ms if abs(tb["t"][m]) >= seuil]; rec["seuils"]["%.2f" % seuil] = mm[0] if mm else None; print("  premier m ou |t_m| >= %.2f : %s  (boite de cote %s)" % (seuil, mm[0] if mm else "aucun", (2 * mm[0] + 1) if mm else "-"))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
