# -*- coding: ascii -*-
"""MARGES AUX DOUZE CELLULES TIREES -- machine 1, v1, 2026-11-15. Arithmetique ; aucun calcul 2D, aucune chaine nouvelle.
Entrees : (a) les chaines aux cellules candidates (eligibilite_*.json, premiere partie) aux quatorze etiquettes PREDITES ;
(b) l'etalonnage RETROSPECTIF aux points DEJA JOUES : la feuille d'ordre 3 jouee sur les douze points du delta 98 contre
les largeurs de plateau du run ter (56 etats du domaine), et les deux etats lus de chaque ancre (plateau de la reference
de machine 1). Aucune largeur 2D des cellules tirees n'existe, et aucune n'est lue ici.
Deux regles d'attente, ecrites ici avant de regarder leur resultat aux cellules :
  delta < 0 : ln q3 = -k (ln(G3/G2))^2, k lu etat par etat aux points joues (mediane, plus grand), aux seuls etats ou
              |ln(G3/G2)| >= 0.05 : au-dessous, k est le rapport de deux petits nombres et ne se lit pas ;
  delta > 0 : ln q3 = c delta^p, p = 2 puis p = 3, c lu etat par etat aux points joues (mediane, plus grand).
Usage : python3 -I marges_cellules_tirees_machine1_v1.py <table du gel.json> <feuille retrospective.json>
        <ancres retrospectif.json> <sortie.json> <eligibilite_*.json> [...]"""
import sys, json, math
from fractions import Fraction as F
TABLE, RETRO, ANCRES, SORTIE = sys.argv[1:5]; ENTREES = sys.argv[5:]
E_MAX, STAB_MAX, PLANCHER10, E_BAS, T_BAS, T_HAUT, N_ETATS = 0.7, 0.05, 1.33e-12, 0.3, 0.05, 0.10, 14
def med(x):
    x = sorted(x); n = len(x); return x[n // 2] if n % 2 else 0.5 * (x[n // 2 - 1] + x[n // 2])
# --- etalonnage retrospectif ---
neg, pos = [], []                                   # (point, delta, ln q3, ln(G3/G2), e_bord)
for c in json.load(open(RETRO))["cellules"]:
    for r in c["etats"]:
        if r["exclu"] is None and r["dans_le_domaine"]:
            (neg if c["delta"] < 0 else pos).append((c["id"], c["delta"], r["ln_q3"], math.log(r["G3"] / r["G2"]), r["e_bord"]))
for r in json.load(open(ANCRES))["etats"]:
    if r["plateau"] and r["dans_le_domaine"]:
        (neg if r["delta"] < 0 else pos).append((r["id"], r["delta"], r["plateau"]["ln_q3"], r["ln_G3_G2"], r["e_bord"]))
D32_MIN = 0.05
neg_k = [r for r in neg if abs(r[3]) >= D32_MIN]; ks = [-r[2] / r[3] ** 2 for r in neg_k]; K_MED, K_MAX = med(ks), max(ks)
c2 = [r[2] / r[1] ** 2 for r in pos]; c3 = [r[2] / r[1] ** 3 for r in pos]
print("ETALONNAGE aux points deja joues (etats du domaine) : delta < 0 : %d etats (%s) ; delta > 0 : %d etats (%s)" % (
    len(neg), " ".join(sorted(set(r[0] for r in neg))), len(pos), " ".join(sorted(set(r[0] for r in pos)))))
print("  delta < 0 : ln q3 negatif a %d etats sur %d ; k = -ln q3 / (ln(G3/G2))^2, lu aux %d etats ou |ln(G3/G2)| >= %.2f (%s) : mediane %.2f, de %.2f a %.2f" % (
    sum(r[2] < 0 for r in neg), len(neg), len(neg_k), D32_MIN, " ".join(sorted(set(r[0] for r in neg_k))), K_MED, min(ks), K_MAX))
for pid in sorted(set(r[0] for r in neg)):
    v = [r for r in neg if r[0] == pid]
    print("     %-3s delta %+.2f : %2d etats ; ln q3 mediane %+.4f ; ln(G3/G2) mediane %+.4f ; k de %.2f a %.2f" % (pid, v[0][1], len(v), med([r[2] for r in v]), med([r[3] for r in v]),
          min(-r[2] / r[3] ** 2 for r in v), max(-r[2] / r[3] ** 2 for r in v)))
print("  delta > 0 : ln q3 positif a %d etats sur %d ; c2 = ln q3 / delta^2 : mediane %.1f, plus grand %.1f ; c3 = ln q3 / delta^3 : mediane %.0f, plus grand %.0f" % (
    sum(r[2] > 0 for r in pos), len(pos), med(c2), max(c2), med(c3), max(c3)))
for pid in sorted(set(r[0] for r in pos)):
    v = [r for r in pos if r[0] == pid]
    print("     %-3s delta %+.2f : %2d etats ; ln q3 de %+.4f a %+.4f" % (pid, v[0][1], len(v), min(r[2] for r in v), max(r[2] for r in v)))
print("  plus grand e_bord d'un etat du domaine aux points joues : %.3f" % max(r[4] for r in neg + pos))
E_VU = max(r[4] for r in neg + pos)
# --- les douze cellules ---
cells = []
for f in ENTREES:
    cells += json.load(open(f))["cellules"]
out = {"etalonnage": {"n_neg": len(neg), "n_pos": len(pos), "n_neg_k": len(neg_k), "d32_min": D32_MIN, "k_med": K_MED, "k_max": K_MAX, "k_min": min(ks), "c2_med": med(c2), "c2_max": max(c2), "c3_med": med(c3), "c3_max": max(c3),
                      "e_bord_max_vu": E_VU, "neg_tous_negatifs": all(r[2] < 0 for r in neg), "pos_tous_positifs": all(r[2] > 0 for r in pos)}, "cellules": []}
print("CELLULES TIREES (etiquettes PREDITES ; T = %.2f si e_bord < %.1f, %.2f sinon) : attente du pire |ln q3| du domaine, et marge T / attente" % (T_BAS, E_BAS, T_HAUT))
for pt in json.load(open(TABLE))["points"]:
    if pt["role"] != "juge":
        continue
    c = [x for x in cells if F(x["w2"]) == F(pt["w2"]) and F(x["facteur"]) == F(pt["facteur"])]; assert len(c) == 1, pt; c = c[0]; d = float(F(pt["w2"])) - 2.0
    dom, hors, sous = [], [], 0
    for e in [e for e in c["etats"] if e["rang_predit"] is not None and e["rang_predit"] < N_ETATS]:
        if e["vide"]:
            sous += 1; continue
        dans = e["e_bord"] < E_MAX and e["stab3"] is not None and e["stab3"] <= STAB_MAX; G = e["G3"] if dans else e["G2"][2]
        if not (e["stable1"] and e["stable2"] and G > PLANCHER10):
            sous += 1; continue
        (dom if dans else hors).append(e)
    lignes = {}
    for e in dom:
        e["_T"] = T_BAS if e["e_bord"] < E_BAS else T_HAUT; e["_d32"] = math.log(e["G3"] / e["G2"][2])
    if d < 0:
        for nom, k in (("mediane", K_MED), ("pire", K_MAX)):
            att = [k * e["_d32"] ** 2 for e in dom]
            lignes[nom] = {"attente_pire": max(att), "marge": min(e["_T"] / a for e, a in zip(dom, att)),
                           "ordre2_plus_pres": sum(1 for e, a in zip(dom, att) if a > abs(-a - e["_d32"]))}
    else:
        for nom, c_, p in (("p2_mediane", med(c2), 2), ("p2_pire", max(c2), 2), ("p3_mediane", med(c3), 3), ("p3_pire", max(c3), 3)):
            a = c_ * d ** p; lignes[nom] = {"attente_pire": a, "marge": min(e["_T"] for e in dom) / a}
    r = {"id": pt["id"], "creneau": pt["creneau"], "delta": d, "facteur": pt["facteur"], "N": c["N"], "n_domaine": len(dom), "n_hors": len(hors), "n_non_jugeables": sous,
         "e_bord_min": min(e["e_bord"] for e in dom), "e_bord_max": max(e["e_bord"] for e in dom), "n_T_bas": sum(e["_T"] == T_BAS for e in dom),
         "n_au_dela_du_vu": sum(e["e_bord"] > E_VU for e in dom), "stab3_max": max(e["stab3"] for e in dom), "d32_med": med([e["_d32"] for e in dom]),
         "d32_min": min(e["_d32"] for e in dom), "d32_max": max(e["_d32"] for e in dom), "attentes": lignes, "seuil_E2": -(-3 * len(dom) // 4)}
    out["cellules"].append(r)
    print("  %-3s delta %+.3f x%-4s N %d : domaine %2d (dont %d a T = %.2f ; %d au-dela du plus grand e_bord vu), hors %d ; e_bord %.3f a %.3f ; ln(G3/G2) mediane %+.4f, extreme %+.4f" % (
        pt["id"], d, pt["facteur"], c["N"], len(dom), r["n_T_bas"], T_BAS, r["n_au_dela_du_vu"], len(hors), r["e_bord_min"], r["e_bord_max"], r["d32_med"], r["d32_min"]))
    print("        " + " ; ".join("%s : attente %.4f, marge %.2f%s" % (k, v["attente_pire"], v["marge"], (", ordre 2 plus pres a %d etats sur %d (seuil E2 : %d plus pres pour l'ordre 3)" % (
        v["ordre2_plus_pres"], len(dom), r["seuil_E2"])) if "ordre2_plus_pres" in v else "") for k, v in lignes.items()))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
