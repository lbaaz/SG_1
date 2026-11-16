# -*- coding: ascii -*-
"""STRUCTURE DU DEVELOPPEMENT -- machine 1, v1, 2026-11-15. Hors chaine. Chaines 1D seulement, aucun calcul 2D.
A etiquette (n1, n2) fixee et a kappa = t_0 / |delta| fixe (saut du site 0 rapporte au desaccord), on fait varier
delta : si la chaine est un developpement en delta a kappa fixe, alors
  Gamma_1 / |delta| ne depend (presque) plus de delta ;  ln(Gamma_2 / Gamma_1) est lineaire en delta (il change de
  signe avec lui) ;  ln(Gamma_3 / Gamma_2) est quadratique en delta.
Gamma_1 : sauts du premier ordre seuls (avec les sites bas) ; Gamma_2 : ordre 2 complet ; Gamma_3 : ordre 3 complet.
Les w2 parcourus ne sont pas des points de la campagne : aucune largeur 2D n'y est lue ni predite ici.
Usage : python3 -I structure_en_delta_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
MOTEUR, BLOC2, BLOC3, SORTIE = sys.argv[1:5]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec")); exec(compile(open(BLOC3, encoding="ascii").read(), BLOC3, "exec"))
EF = 0.0625
DELTAS = [F(1, 80), F(1, 40), F(1, 20), F(3, 40), F(1, 10)]
out = {"series": []}
for (n1, n2, kappa) in ((6, 2, 0.30), (6, 2, 0.22), (10, 3, 0.20), (5, 1, 0.26)):
    lignes = []
    for sg in (-1, 1):
        for da in DELTAS:
            w2 = F(2) + sg * da; d = float(w2) - 2.0
            tau0 = M.X_saut_reel(M.P, M.CANAL[0], M.CANAL[1], float(n1), float(n2), w2) / M.P     # t_0 = g tau0
            g = kappa * abs(d) / tau0
            sites = M.barriere(float(n1), float(n2), w2, g, True)
            if not sites:
                lignes.append({"delta": d, "g": g, "vide": True}); continue
            tb = tables_ordre2(float(n1), float(n2), w2, g, sites, M_facteur=4); t3 = tables_ordre3(float(n1), float(n2), w2, g, tb)
            g1 = gamma_chaine_ordre3(tb, t3, EF, avec_T3=False, avec_W3=False, avec_S=False, avec_U=False, avec_W5=False)["Gamma_flux"]
            g2 = gamma_chaine_ordre2(tb, EF)["Gamma_flux"]; g3 = gamma_chaine_ordre3(tb, t3, EF)["Gamma_flux"]
            mb = tb["m2_bord"]
            lignes.append({"delta": d, "g": g, "vide": False, "m_bord": mb, "e_bord": abs(mb * d + tb["S"][mb] - tb["S"][0]), "G1_sur_delta": g1 / abs(d),
                           "ln_21": math.log(g2 / g1), "ln_32": math.log(g3 / g2)})
    out["series"].append({"n1": n1, "n2": n2, "kappa": kappa, "lignes": lignes})
    print("etiquette (%d, %d), kappa = t_0 / |delta| = %.2f" % (n1, n2, kappa))
    print("   delta     g          m_bord  e_bord   Gamma_1/|delta|   ln(G2/G1)   /delta     ln(G3/G2)   /delta^2")
    for l in lignes:
        if l["vide"]:
            print("   %+.4f  %.3e  barriere vide" % (l["delta"], l["g"])); continue
        print("   %+.4f  %.3e   %2d     %.3f    %.4e        %+.4f     %+.3f     %+.5f    %+.3f" % (l["delta"], l["g"], l["m_bord"], l["e_bord"], l["G1_sur_delta"],
              l["ln_21"], l["ln_21"] / l["delta"], l["ln_32"], l["ln_32"] / l["delta"] ** 2))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
