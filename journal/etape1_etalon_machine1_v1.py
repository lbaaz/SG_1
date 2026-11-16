# -*- coding: ascii -*-
"""ETAPE 1 -- CHANGER D'ETALON. Hors chaine, apres coup, une plume. Aucun calcul : de l'arithmetique sur des pieces.
La comparaison du delta 98 (chaine E-A d'ordre 2 contre la lecture deposee a k = 3) est refaite contre la largeur de
plateau Gamma_pl(A) que le run du gel E-B ter a rendue aux memes etats.
Usage : python3 -I etape1_etalon_machine1_v1.py <sonde_ordre2.json> <verdict_ordre2.json> <verdict_ter.json> <sortie.json>"""
import sys, json, math, statistics
from fractions import Fraction as Fr
DEP, V98, VTER, SORTIE = sys.argv[1:5]
D = {p["id"]: p for p in json.load(open(DEP))["points"]}
V = {p["id"]: p for p in json.load(open(V98))["points"]}
T = json.load(open(VTER))["points"]
JUGES = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4"]
BANDES = (("proche", 1.25, 0.06), ("moyenne", 1.6, 0.10), ("lointaine", 2.0, 0.12))
med = statistics.median
rows = []
for i in JUGES:
    d = float(Fr(D[i]["w2"])) - 2.0
    bande = [b for b in BANDES if abs(d) <= b[2] + 1e-12][0]
    ter = {e["rang"]: e for e in T[i]["etats"]}
    dep = {e["rang"]: e for e in D[i]["etats"]}
    for e in V[i]["etats"]:
        if e["exclu"] is not None:
            continue
        r = e["rang"]; t = ter[r]; c2 = dep[r]["chaine2"]
        assert (t["n1"], t["n2"]) == (e["n1"], e["n2"]) and abs(c2["gammas_flux"][2] / e["Gamma_ordre2"] - 1) < 1e-14
        rows.append({"id": i, "rang": r, "n1": e["n1"], "n2": e["n2"], "delta": d, "g": D[i]["g"], "bande": bande[0], "borne": bande[1],
                     "m_bord": c2["m_bord"], "card": dep[r]["chaine"]["card"], "Lambda": dep[r]["chaine"]["Lambda"],
                     "G_dep": e["Gamma_2D"], "G_pl": t["plateaux"]["A"]["Gamma_pl"], "statut": t["statut"], "sur": t["lu_sur_le_plateau"],
                     "G_c1": e["Gamma_chaine"], "G_c2": e["Gamma_ordre2"], "q2": e["q2"], "q1": e["q1"],
                     "q2p": e["Gamma_ordre2"] / t["plateaux"]["A"]["Gamma_pl"], "q1p": e["Gamma_chaine"] / t["plateaux"]["A"]["Gamma_pl"]})
Q = [r for r in rows if r["statut"] == "QUALIFIE"]
def ajust(cle, rs):
    """ln q = c delta^2 m_bord, sans constante ; rend c, correlation, ecart-type restant."""
    x = [r["delta"] ** 2 * r["m_bord"] for r in rs]; y = [math.log(r[cle]) for r in rs]
    c = sum(a * b for a, b in zip(x, y)) / sum(a * a for a in x)
    mx, my = sum(x) / len(x), sum(y) / len(y)
    cor = sum((a - mx) * (b - my) for a, b in zip(x, y)) / math.sqrt(sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))
    res = [b - c * a for a, b in zip(x, y)]
    return c, cor, statistics.pstdev(res)
out = {"n_juges_98": len(rows), "n_qualifies": len(Q), "bandes": {}, "points": {}}
print("ETAPE 1 : la chaine d'ordre 2 contre la largeur de plateau (etats juges du delta 98 : %d, dont QUALIFIES : %d)" % (len(rows), len(Q)))
print("  bande      borne  etats   q2 contre la lecture deposee        q2 contre le plateau                  hors borne   (etats QUALIFIES)")
print("                            min     mediane max                 min     mediane max                  depose plateau")
for nom, borne, lim in BANDES:
    a = [r for r in Q if r["bande"] == nom]; b = a          # etats QUALIFIES seulement, des deux cotes
    o = {"borne": borne, "etats": len(a), "qualifies": len(b), "q2": [min(r["q2"] for r in a), med([r["q2"] for r in a]), max(r["q2"] for r in a)],
         "q2p": [min(r["q2p"] for r in b), med([r["q2p"] for r in b]), max(r["q2p"] for r in b)],
         "hors_depose": sum(not (1 / borne <= r["q2"] <= borne) for r in a), "hors_plateau": sum(not (1 / borne <= r["q2p"] <= borne) for r in b)}
    out["bandes"][nom] = o
    print("  %-9s  %-5s  %3d     %.3f   %.3f   %.3f               %.3f   %.3f   %.3f                %d      %d" % (
        nom, borne, len(a), o["q2"][0], o["q2"][1], o["q2"][2], o["q2p"][0], o["q2p"][1], o["q2p"][2], o["hors_depose"], o["hors_plateau"]))
print("  par point (QUALIFIES) : id, delta, etats, q2 depose min/med/max, q2 plateau min/med/max")
for i in JUGES:
    b = [r for r in Q if r["id"] == i]
    o = {"delta": b[0]["delta"], "etats": len(b), "q2": [min(r["q2"] for r in b), med([r["q2"] for r in b]), max(r["q2"] for r in b)],
         "q2p": [min(r["q2p"] for r in b), med([r["q2p"] for r in b]), max(r["q2p"] for r in b)]}
    out["points"][i] = o
    print("    %s  %+.2f  %2d   %.3f %.3f %.3f    %.3f %.3f %.3f" % (i, o["delta"], len(b), o["q2"][0], o["q2"][1], o["q2"][2], o["q2p"][0], o["q2p"][1], o["q2p"][2]))
for cle, nom in (("q2", "lecture deposee"), ("q2p", "plateau")):
    c, cor, s = ajust(cle, Q); out["ajust_" + cle] = {"c": c, "correlation": cor, "ecart_type_restant": s}
    print("  ajustement ln q = c delta^2 m_bord contre %-15s : c = %.3f, correlation %.3f, ecart-type restant %.4f" % (nom, c, cor, s))
out["q2_min"] = min(r["q2"] for r in Q); out["q2_max"] = max(r["q2"] for r in Q)
out["q2p_min"] = min(r["q2p"] for r in Q); out["q2p_max"] = max(r["q2p"] for r in Q)
out["q2p_sous_1"] = sum(r["q2p"] < 1 for r in Q); out["q2_sous_1"] = sum(r["q2"] < 1 for r in Q)
pire = max(Q, key=lambda r: r["q2p"]); out["pire_q2p"] = {"id": pire["id"], "rang": pire["rang"], "q2p": pire["q2p"], "q2": pire["q2"]}
ec = [abs(math.log(r["q2p"] / r["q2"])) for r in Q]
out["deplacement_ln"] = {"mediane": med(ec), "max": max(ec)}
print("  q2 depose : de %.3f a %.3f (%d sous 1) ; q2 plateau : de %.3f a %.3f (%d sous 1) ; pire : %s rang %d (%.3f, depose %.3f)" % (
    out["q2_min"], out["q2_max"], out["q2_sous_1"], out["q2p_min"], out["q2p_max"], out["q2p_sous_1"], pire["id"], pire["rang"], pire["q2p"], pire["q2"]))
print("  deplacement |ln(q2 plateau / q2 depose)| : mediane %.4f, plus grand %.4f" % (med(ec), max(ec)))
out["etats"] = rows
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
