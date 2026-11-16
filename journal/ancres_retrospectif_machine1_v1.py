# -*- coding: ascii -*-
"""ANCRES, RETROSPECTIF -- machine 1, v1, 2026-11-15. Aucun calcul 2D : chaines (moteur, ordre 2, ordre 3) aux etiquettes
des deux ancres A1 (w2 = 39/20) et A2 (41/20), DEJA JOUEES, contre (a) la largeur de plateau sous l'absorbeur A des etats
de rang 0 et 1, relue par la feuille du gel ter dans la reference de machine 1 (reference_ancres_ter_machine1_v1.json) ;
(b) a titre indicatif, la largeur deposee a k = 3 (decomposition dense) de tous leurs etats au-dessus de dix planchers.
Usage : python3 -I ancres_retrospectif_machine1_v1.py <moteur> <bloc2> <bloc3> <sonde_ordre2.json> <reference ancres.json>
        <feuille du gel ter.py> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
MOTEUR, BLOC2, BLOC3, DEPOT, REF, FEUILLE, SORTIE = sys.argv[1:8]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec")); exec(compile(open(BLOC3, encoding="ascii").read(), BLOC3, "exec"))
spec = importlib.util.spec_from_file_location("feuille_ter", FEUILLE); FT = importlib.util.module_from_spec(spec); spec.loader.exec_module(FT)
EF = 0.0625; ETAS = (0.25, 0.125, 0.0625, 0.03125)
def chaine(w2, g, a, b):
    d = float(w2) - 2.0; sites = M.barriere(float(a), float(b), w2, g, True)
    if not sites:
        return None
    g1 = [float(M.gamma_chaine(float(a), float(b), w2, g, sites, eta_facteur=x, M_facteur=4)["Gamma_c"]) for x in ETAS]
    tb = tables_ordre2(float(a), float(b), w2, g, sites, M_facteur=4); g2 = [gamma_chaine_ordre2(tb, x)["Gamma_flux"] for x in ETAS]
    t3 = tables_ordre3(float(a), float(b), w2, g, tb); G3 = gamma_chaine_ordre3(tb, t3, EF)["Gamma_flux"]
    var = [gamma_chaine_ordre3(tb, t3, 2 * EF)["Gamma_flux"], gamma_chaine_ordre3(tb, t3, EF / 2)["Gamma_flux"], gamma_chaine_ordre3(tb, t3, EF, recul=4)["Gamma_flux"]]
    mb = tb["m2_bord"]
    return {"G2": g2[2], "G3": G3, "e_bord": abs(mb * d + tb["S"][mb] - tb["S"][0]), "stab3": max(abs(math.log(x / G3)) for x in var) if G3 > 0 and all(x > 0 for x in var) else None,
            "stables": bool(all(x > 0 for x in g1) and max(g1) / min(g1) <= 2 and all(x > 0 for x in g2) and max(g2) / min(g2) <= 2)}
D = {p["id"]: p for p in json.load(open(DEPOT))["points"]}; R = {p["id"]: p for p in json.load(open(REF))["points"]}; out = []
for pid in ("A1", "A2"):
    p = D[pid]; w2 = F(p["w2"]); g = p["g"]; lus = {e["rang"]: e for e in R[pid]["etats"]}
    for e in p["etats"]:
        G3d = e["Gamma_2D"]["3"]
        if G3d <= 1.33e-12:
            continue
        c = chaine(w2, g, e["n1"], e["n2"])
        if c is None or not c["stables"]:
            continue
        r = {"id": pid, "delta": float(w2) - 2.0, "rang": e["rang"], "n1": e["n1"], "n2": e["n2"], "e_bord": c["e_bord"], "stab3": c["stab3"],
             "dans_le_domaine": bool(c["e_bord"] < 0.7 and c["stab3"] is not None and c["stab3"] <= 0.05), "ln_q2_depot": math.log(c["G2"] / G3d), "ln_q3_depot": math.log(c["G3"] / G3d),
             "ln_G3_G2": math.log(c["G3"] / c["G2"]), "plateau": None}
        if e["rang"] in lus:
            j = FT.juger_etat(lus[e["rang"]]["traj"], G3d); pl = j["plateaux"]["A"]
            if j["statut"] == "QUALIFIE" and "Gamma_pl" in pl:
                r["plateau"] = {"Gamma_pl": float(pl["Gamma_pl"]), "ln_q2": math.log(c["G2"] / float(pl["Gamma_pl"])), "ln_q3": math.log(c["G3"] / float(pl["Gamma_pl"])), "ln_depot_plateau": math.log(G3d / float(pl["Gamma_pl"]))}
        out.append(r)
        print("%s delta %+.2f rang %2d (%2d,%d) e_bord %.3f stab3 %s %s ; contre le depot k = 3 : ln q2 %+.4f ln q3 %+.4f ; ln(G3/G2) %+.4f%s" % (
            pid, r["delta"], e["rang"], e["n1"], e["n2"], c["e_bord"], ("%.4f" % c["stab3"]) if c["stab3"] is not None else "-", "DOMAINE" if r["dans_le_domaine"] else "hors   ", r["ln_q2_depot"], r["ln_q3_depot"],
            r["ln_G3_G2"], (" ; PLATEAU A : ln q2 %+.4f ln q3 %+.4f (depot / plateau %+.4f)" % (r["plateau"]["ln_q2"], r["plateau"]["ln_q3"], r["plateau"]["ln_depot_plateau"])) if r["plateau"] else ""))
json.dump({"etats": out}, open(SORTIE, "w"), indent=1, sort_keys=True)
