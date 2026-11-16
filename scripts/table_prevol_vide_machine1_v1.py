# -*- coding: ascii -*-
"""TABLE DE PRE-VOL DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16. Aucun calcul de largeur.
Deux cellules a w2 = 101/50, QUI N'EST PAS UN CANDIDAT (centieme), aux profondeurs 3 et 8, au couplage de la regle des
cellules (premiere partie, section 2). Elles ne servent qu'au pre-vol : le jumeau sans fantome y est lu, le fantome jamais.
Usage : python3 -I -B table_prevol_vide_machine1_v1.py <moteur> <sortie.json>"""
import sys, json, importlib.util
from fractions import Fraction as F
MOTEUR, SORTIE = sys.argv[1:3]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
KAPPA = {3: "0.0262", 8: "0.00928"}; W2 = F(101, 50); d = float(W2) - 2.0
cellules = []
for m in (3, 8):
    g = "%.5e" % (float(F(KAPPA[m])) * abs(d) * M.P / M.X_saut_reel(M.P, M.CANAL[0], M.CANAL[1], 0.0, 0.0, W2))
    cellules.append({"id": "PV%d" % m, "creneau": "PV", "ligne": "pre-vol", "w2": "101/50", "delta": d, "m": m, "g": g, "r_c": 2 * (m + max(8, m)) + 2, "eta0": abs(d),
                     "tolerance": None, "etendue": None, "ln_G3": None})
json.dump({"gel": "largeur du vide -- PRE-VOL", "cellules": cellules,
           "regle": {"absorbeurs_du_lecteur": [["A", "F2", 0, 80], ["B", "F2", 0, 100], ["C", "F1", 0, 100], ["D", "F2", 10, 80]], "barreaux": list(range(-3, 9))}},
          open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit %s : %s" % (SORTIE, ", ".join("%s g = %s" % (c["id"], c["g"]) for c in cellules)))
