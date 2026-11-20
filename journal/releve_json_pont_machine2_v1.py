# -*- coding: ascii -*-
"""Releve mecanique du json de la seconde passe de m1 (machine 2, hors chaine). Usage : py -3.11 -I releve_json_pont_machine2_v1.py <pont_semiclassique_v1.json>"""
import sys, json, math
from collections import defaultdict
S = json.load(open(sys.argv[1]))
tous = [(c["id"], c["m_bord"], x) for c in S["cellules"] for x in c["croisements"]]
print("croisements :", len(tous), "| paires (cellule, N) distinctes :", len({(i, x["N"]) for i, m, x in tous}), "| configurations (profondeur, N) distinctes :", len({(m, x["N"]) for i, m, x in tous}))
# la meme (cellule, N) enregistree deux fois : identique ?
vus = defaultdict(list)
for i, m, x in tous:
    vus[(i, x["N"])].append(x["ln_R_T"])
dup = {k: v for k, v in vus.items() if len(v) > 1}
print("paires (cellule, N) enregistrees plus d'une fois :", len(dup), "| ecart maximal entre doublons :", max(max(v) - min(v) for v in dup.values()) if dup else 0)
# signe de ln_R_T et de ln(V^2 T / G)
lr = [x["ln_R_T"] for i, m, x in tous]
print("ln_R_T (= ln(2 pi V^2/D_T / G) = ln(V^2 T / G)) : min %+.4f max %+.4f  -> tous negatifs : %s" % (min(lr), max(lr), all(v < 0 for v in lr)))
chk = [abs(math.log(x["V"] ** 2 * (2 * math.pi / x["D_T"])) - c_lnG - x["ln_R_T"]) for c in S["cellules"] for x in c["croisements"] for c_lnG in [c["ln_G_absorbeur_ordre1"]]]
print("recalcul ln(V^2 T / G) depuis V, D_T, ln G : ecart max a ln_R_T = %.2e" % max(chk))
# champ 'Gamma_T_sur_V2' : G * T / V^2 ; la quantite sans dimension serait G / (V^2 T)
x0 = tous[0][2]; c0 = S["cellules"][0]; G0 = math.exp(c0["ln_G_absorbeur_ordre1"]); T0 = 2 * math.pi / x0["D_T"]
print("champ Gamma_T_sur_V2 =", x0["Gamma_T_sur_V2"], "| G*T/V^2 =", G0 * T0 / x0["V"] ** 2, "| G/(V^2 T) =", G0 / (x0["V"] ** 2 * T0), "| (unite : 1/energie^2 pour le premier)")
# les quatre desaccords a profondeur egale : meme residu ?
par = defaultdict(dict)
for i, m, x in tous:
    par[(m, x["N"])][i] = x["ln_R_T"]
ec = [max(v.values()) - min(v.values()) for v in par.values() if len(v) > 1]
print("a (profondeur, N) fixes, ecart maximal du residu entre cellules : %.2e (sur %d configurations)" % (max(ec), len(ec)))
# Gamma absorbeur de m1 contre la table gelee
T = json.load(open(sys.argv[1].replace("pont_semiclassique_v1.json", "table_cellules_gel_vide_v1.json"))) if False else None
