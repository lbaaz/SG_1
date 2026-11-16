# -*- coding: ascii -*-
"""LECTURE DU RESULTAT du gel "loi de la largeur, ordre 3" -- machine 1, v1, 2026-11-16. Arithmetique sur des fichiers ;
aucun calcul de chaine ni de 2D. Entrees : le verdict d'ordre 3 du run (feuille jouee par machine 2), les marges gelees
(marges_cellules_tirees_v1.json, seconde partie), les chaines predites (eligibilite_*.json, premiere partie).
Rend, pour l'acte : les classes de e_bord ; les regularites de la section 7.2 du gel relues sur les etats du run ; les
attentes de 7.3 contre le realise ; les signes ; les marges de E3 ; les etiquettes predites contre les etiquettes lues.
Usage : python3 -I lecture_resultat_gel_loi_machine1_v1.py <verdict_ordre3 du run> <marges gelees.json> <sortie.json>
        <eligibilite_*.json> [...]"""
import sys, json, math
from fractions import Fraction as F
RUN, MARGES, SORTIE = sys.argv[1:4]; ENTREES = sys.argv[4:]
A = json.load(open(RUN)); MG = json.load(open(MARGES)); mg = {r["id"]: r for r in MG["cellules"]}; ET = MG["etalonnage"]; out = {}
def med(v):
    v = sorted(v); n = len(v); return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])
J = [(c, e) for c in A["cellules"] for e in c["etats"] if e["exclu"] is None]; DOM = [(c, e) for c, e in J if e["dans_le_domaine"]]; HORS = [(c, e) for c, e in J if not e["dans_le_domaine"]]
print("ETATS : %d juges, %d dans le domaine, %d hors" % (len(J), len(DOM), len(HORS)))
# classes de e_bord
out["classes"] = []
for lo, hi in ((0.0, 0.3), (0.3, 0.5), (0.5, 0.7)):
    v = [abs(e["ln_q3"]) for c, e in DOM if lo <= e["e_bord"] < hi]; out["classes"].append({"lo": lo, "hi": hi, "n": len(v), "med": med(v), "max": max(v)})
    print("  e_bord dans [%.1f, %.1f[ : %3d etats du domaine ; |ln q3| mediane %.4f, plus grand %.4f" % (lo, hi, len(v), med(v), max(v)))
lig = [abs(e["ln_q3"]) for c, e in DOM if c["role"] == "ligne"]; out["ligne"] = {"n": len(lig), "med": med(lig), "max": max(lig)}
print("  cellules de ligne : %d etats du domaine ; |ln q3| mediane %.4f, plus grand %.4f ; au-dela de e_bord = %.3f (le plus grand vu avant le run) : %d etats du domaine" % (
    len(lig), med(lig), max(lig), ET["e_bord_max_vu"], sum(e["e_bord"] > ET["e_bord_max_vu"] for c, e in DOM)))
out["au_dela"] = [(c["id"], e["rang"], e["e_bord"], e["ln_q3"]) for c, e in DOM if e["e_bord"] > ET["e_bord_max_vu"]]
# regularites
neg = [(c, e, math.log(e["G3"] / e["G2"])) for c, e in DOM if c["delta"] < 0]; pos = [(c, e) for c, e in DOM if c["delta"] > 0]
kk = [(-e["ln_q3"] / d ** 2, c["id"]) for c, e, d in neg if abs(d) >= 0.05]; ks = [x[0] for x in kk]
print("REGULARITE a delta < 0 : %d etats du domaine, ln q3 negatif a %d ; k aux %d etats ou |ln(G3/G2)| >= 0.05 : mediane %.2f, de %.2f a %.2f (avant le run : mediane %.2f, de %.2f a %.2f) ; k > %.2f a %d etats" % (
    len(neg), sum(e["ln_q3"] < 0 for c, e, d in neg), len(ks), med(ks), min(ks), max(ks), ET["k_med"], ET["k_min"], ET["k_max"], ET["k_max"], sum(k > ET["k_max"] for k in ks)))
out["k"] = {"n_neg": len(neg), "n_negatifs": sum(e["ln_q3"] < 0 for c, e, d in neg), "n": len(ks), "med": med(ks), "min": min(ks), "max": max(ks), "au_dessus": sum(k > ET["k_max"] for k in ks)}
c2 = [e["ln_q3"] / c["delta"] ** 2 for c, e in pos]; c3 = [e["ln_q3"] / c["delta"] ** 3 for c, e in pos]
print("REGULARITE a delta > 0 : %d etats du domaine, ln q3 positif a %d ; ln q3 / delta^2 : mediane %.1f, plus grand %.1f (avant : au plus %.1f) -> depasse a %d etats ; ln q3 / delta^3 : mediane %.0f, plus grand %.0f (avant : au plus %.0f) -> depasse a %d etats" % (
    len(pos), sum(e["ln_q3"] > 0 for c, e in pos), med(c2), max(c2), ET["c2_max"], sum(x > ET["c2_max"] for x in c2), med(c3), max(c3), ET["c3_max"], sum(x > ET["c3_max"] for x in c3)))
out["pos"] = {"n": len(pos), "n_positifs": sum(e["ln_q3"] > 0 for c, e in pos), "c2_med": med(c2), "c2_max": max(c2), "c3_med": med(c3), "c3_max": max(c3), "c2_depasse": sum(x > ET["c2_max"] for x in c2),
              "c3_depasse": sum(x > ET["c3_max"] for x in c3)}
for cr in ("P", "BP"):
    v = [(e["ln_q3"] / c["delta"] ** 3, e["ln_q3"] / c["delta"] ** 2) for c, e in pos if c["creneau"] == cr]
    print("     %-2s : %2d etats ; ln q3 / delta^3 de %.0f a %.0f ; ln q3 / delta^2 de %.1f a %.1f" % (cr, len(v), min(x[0] for x in v), max(x[0] for x in v), min(x[1] for x in v), max(x[1] for x in v)))
    out["pos_" + cr] = {"n": len(v), "c3_min": min(x[0] for x in v), "c3_max": max(x[0] for x in v), "c2_min": min(x[1] for x in v), "c2_max": max(x[1] for x in v)}
# attentes de 7.3 contre le realise
print("ATTENTES GELEES (7.3, regle la plus defavorable) contre le REALISE (pire |ln q3| du domaine) :")
out["attentes"] = []
for c in A["cellules"]:
    m = mg[c["id"]]; att = (m["attentes"]["pire"] if m["delta"] < 0 else m["attentes"]["p3_pire"])["attente_pire"]; rea = c["pire_ln_q3_domaine"]
    dom = [e for e in c["etats"] if e["exclu"] is None and e["dans_le_domaine"]]; d32 = med([math.log(e["G3"] / e["G2"]) for e in dom])
    r = {"id": c["id"], "attente": att, "realise": rea, "sous_attente": rea <= att, "n_dom_predit": m["n_domaine"], "n_dom": c["n_domaine"], "n_lus": c["n_lus"], "n_juges": c["n_juges"], "d32_med": d32, "d32_med_predit": m["d32_med"]}
    if m["delta"] > 0:
        r["attente_p2"] = m["attentes"]["p2_pire"]["attente_pire"]
    out["attentes"].append(r)
    print("  %-3s attente %.4f ; realise %.4f ; %s ; domaine predit %2d, lu %2d ; ln(G3/G2) median predit %+.4f, lu %+.4f" % (c["id"], att, rea, "sous l'attente" if rea <= att else "AU-DESSUS de l'attente", m["n_domaine"], c["n_domaine"], m["d32_med"], d32))
# signes par ligne
for cr in ("N", "P"):
    v = [e["ln_q3"] for c, e in DOM if c["creneau"] == cr]; out["signes_" + cr] = {"n": len(v), "neg": sum(x < 0 for x in v), "pos": sum(x > 0 for x in v)}
    print("SIGNES ligne %s : %d etats du domaine, %d negatifs, %d positifs" % (cr, len(v), sum(x < 0 for x in v), sum(x > 0 for x in v)))
# E2 et E3
e2 = [(c["id"], c["n_ordre3_plus_pres"], c["n_domaine"], c["seuil_E2"]) for c in A["cellules"] if c["creneau"] == "N"]; out["E2"] = e2
print("E2 : " + " ; ".join("%s %d sur %d (seuil %d)" % x for x in e2) + " ; total %d sur %d" % (sum(x[1] for x in e2), sum(x[2] for x in e2)))
out["E3"] = []
for cr in ("N", "P", "BN", "BP"):
    v = [(math.log(c["bande"]) - abs(e["ln_q2"]), abs(e["ln_q2"])) for c, e in J if c["creneau"] == cr]; B = [c["bande"] for c in A["cellules"] if c["creneau"] == cr][0]
    out["E3"].append({"creneau": cr, "bande": B, "n": len(v), "pire": max(x[1] for x in v), "marge": min(x[0] for x in v)})
    print("E3 %-2s : borne %.2f (ln = %.3f) ; %3d etats juges ; plus grand |ln q2| %.4f ; plus petite marge %.3f" % (cr, B, math.log(B), len(v), max(x[1] for x in v), min(x[0] for x in v)))
# hors du domaine
out["hors"] = {"n": len(HORS), "ordre3_plus_loin": sum(1 for c, e in HORS if e["ln_q3"] is None or abs(e["ln_q3"]) > abs(e["ln_q2"])), "q3_max": max(abs(e["ln_q3"]) for c, e in HORS), "q2_max": max(abs(e["ln_q2"]) for c, e in HORS),
               "e_bord_min": min(e["e_bord"] for c, e in HORS), "e_bord_max": max(e["e_bord"] for c, e in HORS), "par_stabilite": sum(e["e_bord"] < 0.7 for c, e in HORS)}
print("HORS DU DOMAINE : %d etats (e_bord de %.3f a %.3f ; %d exclus du domaine par la stabilite seule) ; ordre 3 plus loin que l'ordre 2 a %d ; |ln q3| au plus %.4f ; |ln q2| au plus %.4f" % (
    len(HORS), out["hors"]["e_bord_min"], out["hors"]["e_bord_max"], out["hors"]["par_stabilite"], out["hors"]["ordre3_plus_loin"], out["hors"]["q3_max"], out["hors"]["q2_max"]))
# etiquettes predites contre lues
cells = []
for f in ENTREES:
    cells += json.load(open(f))["cellules"]
tot = dans = 0; out["etiquettes"] = []
for c in A["cellules"]:
    p = [x for x in cells if F(x["w2"]) == F(c["w2"]) and F(x["facteur"]) == F(c["facteur"])][0]
    pred = set((s["n1"], s["n2"]) for s in p["etats"] if s["rang_predit"] is not None and s["rang_predit"] < 14); lus = [(e["n1"], e["n2"]) for e in c["etats"]]
    n_in = sum(l in pred for l in lus); tot += len(lus); dans += n_in; out["etiquettes"].append({"id": c["id"], "lus": len(lus), "dans_predits": n_in})
print("ETIQUETTES : %d etats lus, dont %d portent une etiquette parmi les 14 predites de leur cellule ; par cellule : %s" % (tot, dans, " ".join("%s %d/%d" % (x["id"], x["dans_predits"], x["lus"]) for x in out["etiquettes"])))
out["etiquettes_total"] = [dans, tot]
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
