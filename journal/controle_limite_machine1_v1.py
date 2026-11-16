# -*- coding: ascii -*-
"""CONTROLE DE LA LIMITE -- machine 1, v1, 2026-11-16. Hors chaine. Aucun 2D.
Phi (phi_echelle, fraction continue, w2 = 2 exactement) contre Gamma_1 / |delta| du BLOC DEPOSE (sauts du premier
ordre seuls, sites bas compris, tables et barriere du moteur avec Sigma2) a tres petit desaccord, kappa fixe.
Les deux codes ne partagent que les elements de matrice du moteur. Attendu : ecart qui s'annule comme delta.
Usage : python3 -I controle_limite_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <phi_echelle.py> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
MOTEUR, BLOC2, BLOC3, PHI, SORTIE = sys.argv[1:6]
spec = importlib.util.spec_from_file_location("phi_echelle", PHI); PH = importlib.util.module_from_spec(spec); spec.loader.exec_module(PH)
M = PH.charger(MOTEUR)
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec")); exec(compile(open(BLOC3, encoding="ascii").read(), BLOC3, "exec"))
EF = 0.0625
out = []
print(" etiquette  kappa     ln Phi (limite)   delta        ln(Gamma_1/|delta|) du bloc   ecart       ecart / delta")
for (n1, n2, kappa) in ((9, 3, 0.29860947027095935), (6, 2, 0.22), (10, 3, 0.30), (0, 0, 0.03)):
    lp = PH.phi_fc(kappa, n1, n2)["ln_Phi"]
    for d in (F(-1, 1000), F(1, 1000), F(-1, 10000), F(1, 10000)):
        w2 = F(2) + d; df = float(w2) - 2.0
        tau0 = M.X_saut_reel(M.P, 2, 1, float(n1), float(n2), w2) / M.P
        g = kappa * abs(df) / tau0
        sites = M.barriere(float(n1), float(n2), w2, g, True)
        tb = tables_ordre2(float(n1), float(n2), w2, g, sites, M_facteur=4); t3 = tables_ordre3(float(n1), float(n2), w2, g, tb)
        g1 = gamma_chaine_ordre3(tb, t3, EF, avec_T3=False, avec_W3=False, avec_S=False, avec_U=False, avec_W5=False)["Gamma_flux"]
        lb = math.log(g1 / abs(df))
        out.append({"n1": n1, "n2": n2, "kappa": kappa, "ln_Phi": lp, "delta": df, "ln_G1_sur_delta": lb, "ecart": lb - lp})
        print(" (%2d,%2d)   %.4f   %+.8f     %+.5f     %+.8f                 %+.2e   %+.3f" % (n1, n2, kappa, lp, df, lb, lb - lp, (lb - lp) / df))
pire = max(abs(x["ecart"]) for x in out if abs(x["delta"]) < 2e-4)
print("plus grand ecart a |delta| = 0.0001 : %.1e" % pire)
json.dump({"points": out, "pire_a_1e-4": pire}, open(SORTIE, "w"), indent=1, sort_keys=True)
