# -*- coding: ascii -*-
"""LE PONT : le lisse de l'ordre 1 contre le lisse de l'ordre 3, loin du vide. machine 1, v1, 2026-11-16. Hors chaine, classe 3.
La statistique reponderee de pont_2d_force_machine1_v2.py met la chaine FERMEE d'ordre 1 a 0.78 - 0.87 du lisse d'ordre 3.
Est-ce du bruit, ou le lisse d'ordre 1 est-il vraiment plus faible sur la fenetre ? Calcul sans bruit : densite locale du site 0
sous absorbeur adapte (a = 2, c = 8, L = 24), ordre 1 et ordre 3, a ecart au vide egal, de 0.05 a 8 |delta| du cote oppose a delta.
Si rho_1 / rho_3 est plat a 0.8 - 0.9, la statistique voit une vraie difference et la boite 2D se range avec l'ordre 3.
Usage : python3 -I -B pont_lisse_ordres_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <w2> <sortie.json> <g> ..."""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
MOTEUR, BLOC2, BLOC3, BLOC_A, W2S, SORTIE = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in (BLOC2, BLOC3, BLOC_A):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))
w2 = F(W2S); delta = float(w2) - 2.0; ad = abs(delta); sg = 1.0 if delta > 0 else -1.0; out = {"piece": "pont_lisse_ordres_machine1_v1", "w2": W2S, "points": []}
XS = [0.05, 0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0]
for GS in sys.argv[7:]:
    g = float(GS); sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites); t3 = tables_ordre3(0, 0, w2, g, tb)
    def chaine(N, ordre, absorbe):
        H = np.zeros((N + 1, N + 1), dtype=complex)
        for m in range(N + 1):
            H[m, m] = m * tb["d"] + ((tb["S"][m] - tb["S"][0]) if ordre == 3 else 0.0)
            if m > absorbe[0]:
                H[m, m] += -1j * absorbe[1] * abs(tb["t"][m]) * ((m - absorbe[0]) / float(absorbe[2])) ** 2
            if m < N:
                x = tb["t"][m] + (t3["T3"][m] if ordre == 3 else 0.0); H[m, m + 1] = x; H[m + 1, m] = x
            if ordre == 3:
                for pas, tab in ((2, tb["U"]), (3, t3["W3"]), (5, t3["W5"])):
                    if m + pas <= N:
                        H[m, m + pas] = tab[m]; H[m + pas, m] = tab[m]
        return H
    debut = tb["m2_bord"] + 8; res = {}
    for ordre in (1, 3):
        Ha = chaine(debut + 24, ordre, (debut, 2.0, 24)); va, ve = np.linalg.eig(Ha); ia = int(np.argmax(np.abs(ve[0, :]) ** 2)); Ea = float(va[ia].real); Gv = -2.0 * float(va[ia].imag)
        r = []
        for x in XS:
            E = Ea - sg * x * ad; y = np.linalg.solve(E * np.eye(Ha.shape[0]) - Ha, np.eye(Ha.shape[0])[:, 0]); r.append(-float(y[0].imag) / math.pi)
        res[ordre] = (Gv, r)
    rap = [res[1][1][i] / res[3][1][i] for i in range(len(XS))]
    out["points"].append({"g": GS, "Gamma_ordre1": res[1][0], "Gamma_ordre3": res[3][0], "x": XS, "rho1_sur_rho3": rap})
    print("g = %s : Gamma ordre 1 / ordre 3 au vide = %.4f ; rho_1 / rho_3 a ecart egal : %s" % (GS, res[1][0] / res[3][0], "  ".join("%.2f:%.3f" % (XS[i], rap[i]) for i in range(len(XS)))))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
