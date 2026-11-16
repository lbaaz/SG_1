# -*- coding: ascii -*-
"""FORME FERMEE ET PENTES -- machine 1, v1, 2026-11-15. Hors chaine, apres coup, une plume. Chaines 1D seulement.
Pour chaque etat juge du delta 98 : la barriere (sites, desaccord e_m = m delta + Sigma2(m) - Sigma2(0), saut t_m),
l'action de WKB discret  Lambda_w = somme sur la barriere de arccosh(|e_m| / (2 racine(t_{m-1} t_m))),
l'action du moteur Lambda_m = somme de ln(|e_m| / (2 t_m)), le produit perturbatif, la chaine tridiagonale avec
deplacement (sans second voisin), et les pentes d ln Gamma / d ln g de la chaine d'ordre 2 et de -2 Lambda_w
(difference centree a g (1 +- H), etat et desaccord fixes).
Usage : python3 -I forme_fermee_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <sonde_ordre2.json>
        <verdict_ordre2.json> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
MOTEUR, BLOC2, BLOC3, DEP, V98, SORTIE = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):
    c = (k, l, n1, n2, w2)
    if c not in _cache:
        _cache[c] = _brut(p, k, l, n1, n2, w2)
    return _cache[c]
M.X_saut_reel = _X
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec")); exec(compile(open(BLOC3, encoding="ascii").read(), BLOC3, "exec"))
D = {p["id"]: p for p in json.load(open(DEP))["points"]}; V = {p["id"]: p for p in json.load(open(V98))["points"]}
JUGES = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4"]
EF = 0.0625; H = 0.02
VIDE = {"T3": {}, "W3": {}}

def actions(n1, n2, w2, g):
    sites = M.barriere(n1, n2, w2, g, True)
    if not sites:
        return None
    tb = tables_ordre2(n1, n2, w2, g, sites, M_facteur=4); d = tb["d"]; mb = tb["m2_bord"]
    e = {m: m * d + tb["S"][m] - tb["S"][0] for m in range(tb["m_min"], mb + 3)}; t = tb["t"]
    ms = [s[0] for s in sites]
    Lw = sum(math.acosh(max(1.0, abs(e[m]) / (2.0 * math.sqrt(abs(t[m - 1] * t[m]))))) for m in ms)
    Lm = sum(math.log(abs(e[m]) / (2.0 * abs(t[m]))) for m in ms)
    Lp = sum(math.log(abs(e[m]) / abs(t[m - 1])) for m in ms)          # produit perturbatif : somme de ln(|e_m| / t_{m-1})
    r2 = gamma_chaine_ordre2(tb, EF)
    return {"tb": tb, "sites": ms, "Lw": Lw, "Lm": Lm, "Lp": Lp, "G_c2": r2["Gamma_flux"], "e": e, "mb": mb, "d": d}

out = {"reglage": {"ef": EF, "pas_relatif_g": H}, "etats": []}
for pid in JUGES:
    _cache.clear(); p = D[pid]; w2 = F(p["w2"]); g = p["g"]; dep = {e["rang"]: e for e in p["etats"]}
    for ev in V[pid]["etats"]:
        if ev["exclu"] is not None:
            continue
        e = dep[ev["rang"]]; n1, n2 = float(e["n1"]), float(e["n2"])
        a = actions(n1, n2, w2, g); tb = a["tb"]; mb = a["mb"]
        tri = gamma_chaine_ordre3(tb, {"T3": {}, "W3": {}, "W5": {}}, EF, avec_T3=False, avec_W3=False, avec_U=False, avec_W5=False)["Gamma_flux"]
        ap, am = actions(n1, n2, w2, g * (1 + H)), actions(n1, n2, w2, g * (1 - H))
        dl = math.log((1 + H) / (1 - H))
        out["etats"].append({"id": pid, "rang": e["rang"], "n1": e["n1"], "n2": e["n2"], "delta": a["d"], "g": g, "m_bord": mb, "card": len(a["sites"]),
            "contigue": a["sites"] == list(range(1, mb + 1)),
            "e_bord": abs(a["e"][mb]), "t_bord": abs(tb["t"][mb]), "t_0": abs(tb["t"][0]), "e_1": abs(a["e"][1]),
            "somme_t2": sum(tb["t"][m] ** 2 for m in range(0, mb + 1)),
            "Lw": a["Lw"], "Lm": a["Lm"], "Lp": a["Lp"], "G_c2": a["G_c2"], "G_tri": tri,
            "pente_c2": math.log(ap["G_c2"] / am["G_c2"]) / dl, "pente_Lw": -2.0 * (ap["Lw"] - am["Lw"]) / dl,
            "m_bord_plus": ap["mb"], "m_bord_moins": am["mb"]})
    print(pid, "fait", flush=True)
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
