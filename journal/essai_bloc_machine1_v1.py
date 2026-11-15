# -*- coding: ascii -*-
"""Essai du bloc d'ordre 2 contre la note 022d32238a66df6b (hors chaine, classe 3, machine 1, 2026-11-14).
Le bloc doit redonner q2_bas et dE_2_bas du JSON de la note ; on lit aussi Gamma_flux et sa stabilite.
usage : python3 -I essai_bloc_machine1_v1.py <moteur> <bloc> <ordre2_par_etat_v3.json>"""
import sys, json, math, importlib.util
from fractions import Fraction as F
import numpy as np
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1]); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(sys.argv[2], encoding="ascii").read(), "bloc", "exec"))
D = json.load(open(sys.argv[3], encoding="ascii"))["points"]
eq, ee, fl, fl8, im8, neg = [], [], [], [], [], 0
for p in D:
    w2 = F(p["w2"])
    for e in p["etats"]:
        n1, n2 = float(e["n1"]), float(e["n2"]); sites = M.barriere(n1, n2, w2, p["g"], True)
        tb = tables_ordre2(n1, n2, w2, p["g"], sites); r = gamma_chaine_ordre2(tb, 0.0625)
        eq.append(abs(r["Gamma_c2"] / e["Gamma_2D"] / e["q2_bas"] - 1.0)); ee.append(abs(r["dE"] - e["dE_2_bas"]))
        fl.append((abs(r["Gamma_flux"] / r["Gamma_c2"] - 1.0), e["Gamma_2D"], p["id"], e["n1"], e["n2"]))
        if p["id"] not in ("T3", "T4"):
            tb8 = tables_ordre2(n1, n2, w2, p["g"], sites, M_facteur=8); r8 = gamma_chaine_ordre2(tb8, 0.0625)
            fl8.append(abs(r8["Gamma_flux"] / r["Gamma_flux"] - 1.0)); im8.append(abs(r8["Gamma_c2"] / r["Gamma_c2"] - 1.0))
print("%d etats ; ecart max du bloc a la note : sur q2 %.1e (relatif), sur dE %.1e (absolu)" % (len(eq), max(eq), max(ee)))
A = np.array([x[0] for x in fl]); print("Gamma_flux contre -2 Im E, au reglage de la sonde : mediane %.1e  p90 %.1e  max %.1e" % (np.median(A), np.percentile(A, 90), A.max()))
for x in sorted(fl, reverse=True)[:5]: print("   %.3e  Gamma_2D %.1e  %s (%d,%d)" % x)
B = np.array([x[0] for x in fl if x[2] not in ("T3", "T4")])
print("le meme ecart sur les %d etats hors T3 et T4 : mediane %.1e  p90 %.1e  max %.1e" % (len(B), np.median(B), np.percentile(B, 90), B.max()))
print("chaine deux fois plus longue (M_facteur 8), 243 etats : -2 Im E bouge de mediane %.1e  max %.1e ; Gamma_flux de mediane %.1e  max %.1e" % (
    np.median(im8), max(im8), np.median(fl8), max(fl8)))
