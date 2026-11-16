# -*- coding: ascii -*-
"""CHAINE D'ORDRE 3 AUX ETATS JUGES DU DELTA 98 -- machine 1, v1, 2026-11-15. Hors chaine, apres coup, une plume.
Chaines a une dimension seulement (matrices de quelques dizaines de sites) : AUCUN calcul 2D, aucune largeur 2D lue.
Variantes : T3 seul, W3 seul, sans W5 (sauts d'ordre 3 retires un a un), absorbeur de chaine double, divise par deux, recule.
Pour chaque etat juge par le delta 98 : la chaine d'ordre 2 du bloc depose est refaite (controle contre le depot),
puis la chaine d'ordre 3 (bloc ordre3_bloc_machine1_v1.py), ses variantes partielles et ses controles de stabilite.
Usage : python3 -I calcul_ordre3_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sonde_ordre2.json>
        <verdict_ordre2.json> <sortie.json> <id> [<id> ...]"""
import sys, math, json, time, importlib.util
from fractions import Fraction as F
import numpy as np
MOTEUR, BLOC2, BLOC3, DEP, V98, SORTIE = sys.argv[1:7]; IDS = sys.argv[7:]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):                      # memoire des elements de x^5 : memes valeurs, moins d'appels
    c = (k, l, n1, n2, w2)
    if c not in _cache:
        _cache[c] = _brut(p, k, l, n1, n2, w2)
    return _cache[c]
M.X_saut_reel = _X
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec")); exec(compile(open(BLOC3, encoding="ascii").read(), BLOC3, "exec"))
D = {p["id"]: p for p in json.load(open(DEP))["points"]}; V = {p["id"]: p for p in json.load(open(V98))["points"]}
EF = 0.0625
out = {"points": {}, "reglage": {"ef": EF, "M_facteur": 4}}
for pid in IDS:
    t0 = time.time(); _cache.clear()
    p = D[pid]; w2 = F(p["w2"]); g = p["g"]; d = float(w2) - 2.0; etats = []
    dep = {e["rang"]: e for e in p["etats"]}
    for ev in V[pid]["etats"]:
        if ev["exclu"] is not None:
            continue
        e = dep[ev["rang"]]; n1, n2 = float(e["n1"]), float(e["n2"])
        sites = M.barriere(n1, n2, w2, g, True)
        tb = tables_ordre2(n1, n2, w2, g, sites, M_facteur=4)
        r2 = gamma_chaine_ordre2(tb, EF)
        ref2 = e["chaine2"]["gammas_flux"][2]
        t3 = tables_ordre3(n1, n2, w2, g, tb)
        r3 = gamma_chaine_ordre3(tb, t3, EF)
        var = {"T3_seul": gamma_chaine_ordre3(tb, t3, EF, avec_W3=False, avec_W5=False)["Gamma_flux"],
               "W3_seul": gamma_chaine_ordre3(tb, t3, EF, avec_T3=False, avec_W5=False)["Gamma_flux"],
               "sans_W5": gamma_chaine_ordre3(tb, t3, EF, avec_W5=False)["Gamma_flux"],
               "ef_double": gamma_chaine_ordre3(tb, t3, 2 * EF)["Gamma_flux"], "ef_demi": gamma_chaine_ordre3(tb, t3, EF / 2)["Gamma_flux"],
               "recul_4": gamma_chaine_ordre3(tb, t3, EF, recul=4)["Gamma_flux"]}
        mb = tb["m2_bord"]
        bar = [{"m": m, "e": m * d + tb["S"][m] - tb["S"][0], "t": tb["t"][m], "t_avant": tb["t"][m - 1], "U_avant": tb["U"][m - 2] if m - 2 >= tb["m_min"] else 0.0,
                "T3_sur_t_avant": t3["T3"][m - 1] / tb["t"][m - 1], "W3_avant": t3["W3"][m - 3] if m - 3 >= tb["m_min"] else 0.0,
                "T3_sur_t": t3["T3"][m] / tb["t"][m], "T3_BB_sur_t": t3["T3_BB"][m] / tb["t"][m], "T3_A_sur_t": t3["T3_A"][m] / tb["t"][m]}
               for m in range(1, mb + 4)]
        etats.append({"rang": e["rang"], "n1": e["n1"], "n2": e["n2"], "m_bord": mb, "m_min": tb["m_min"], "card": len(sites),
                      "sites_barriere": [s[0] for s in sites],
                      "G_c2": r2["Gamma_flux"], "G_c2_depose": ref2, "ecart_c2_depot": abs(r2["Gamma_flux"] / ref2 - 1.0),
                      "dE_c2": r2["dE"], "G_c3": r3["Gamma_flux"], "G_c3_im": r3["Gamma_im"], "dE_c3": r3["dE"], "recouvrement_c3": r3["recouvrement"],
                      "variantes": var, "barriere": bar,
                      "T3_sur_t_max_barriere": max(abs(b["T3_sur_t_avant"]) for b in bar[:mb]),
                      "W3_sur_t_max_barriere": max(abs(t3["W3"][m] / tb["t"][m]) for m in range(0, mb + 1)),
                      "W5_sur_t_max_barriere": max(abs(t3["W5"][m] / tb["t"][m]) for m in range(0, mb + 1)),
                      "E_re": e["E_re"], "E_libre": e["E_libre"], "Sigma2_0": tb["S"][0]})
        print("  %s rang %2d (%d,%d) : ordre 2 %.4e (depot : ecart %.1e), ordre 3 %.4e, rapport %.4f" % (
            pid, e["rang"], e["n1"], e["n2"], r2["Gamma_flux"], etats[-1]["ecart_c2_depot"], r3["Gamma_flux"], r3["Gamma_flux"] / r2["Gamma_flux"]), flush=True)
    out["points"][pid] = {"w2": p["w2"], "g": g, "delta": d, "etats": etats, "duree_s": round(time.time() - t0, 1)}
    json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
    print("%s : %d etats, %.0f s" % (pid, len(etats), time.time() - t0), flush=True)
