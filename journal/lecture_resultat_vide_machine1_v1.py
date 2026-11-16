# -*- coding: ascii -*-
"""LECTURE DU RESULTAT DU GEL "LARGEUR DU VIDE" POUR L'ACTE -- machine 1, v1, 2026-11-16. Ecrite APRES reception et
authentification du lot de resultat (9a14bf95fa8c6d20). Elle ne juge rien : les jugements sont ceux de la feuille gelee,
rejouee par reception_resultat_gel_vide_machine1_v1.py. Elle met en table ce que l'acte cite, et RECOMPTE de son cote les
grandeurs consignees par la feuille. Aucun seuil nouveau, aucune autre chaine : les nombres d'ordre 2, d'ordre 1, de la loi
d'echelle et de la forme fermee sont ceux de la table gelee, consignes sans jugement.
Usage : python3 -I -B lecture_resultat_vide_machine1_v1.py <verdict rejoue.json> <table gelee.json> <dossier du run recu>
        <sortie.json>"""
import sys, os, json, math, statistics
VERDICT, TABLE, RUN, SORTIE = sys.argv[1:5]
V = json.load(open(VERDICT)); T = json.load(open(TABLE)); TC = {c["id"]: c for c in T["cellules"]}
C = V["cellules"]; assert len(C) == 28 and all("ln_q" in r for r in C), "toutes les cellules ne portent pas un ln q"
ORDRE = ("MG", "MP", "PP", "PG"); out = {"piece": "lecture_resultat_vide_machine1_v1", "verdict": V["verdict"]}
med = statistics.median

# --- 1. brut : les lectures du fantome et du jumeau, relues dans les fichiers de cellule
brut = {"lectures_fantome": 0, "suivies_fantome": 0, "lectures_jumeau": 0, "suivies_jumeau": 0, "residu_max_fantome": 0.0, "iterations_max_fantome": 0,
        "decalages_repris_fantome": 0, "poids_min_fantome": 1.0, "plateformes": []}
durees = {}
for r in C:
    S = json.load(open(os.path.join(RUN, "sonde_vide_%s.json" % r["id"])))
    pf = "%s python %s numpy %s scipy %s" % (S["plateforme"]["systeme"], S["plateforme"]["python"], S["plateforme"]["numpy"], S["plateforme"]["scipy"])
    if pf not in brut["plateformes"]:
        brut["plateformes"].append(pf)
    durees[r["id"]] = {"jumeau": S["jumeau"]["duree_s"], "fantome": S["fantome"]["duree_s"]}
    for nom in ("jumeau", "fantome"):
        for a in ("A", "B", "C", "D"):
            for k, x in S[nom]["traj"][a].items():
                brut["lectures_" + nom] += 1; brut["suivies_" + nom] += 1 if x.get("suivi") else 0
                if nom == "fantome":
                    brut["residu_max_fantome"] = max(brut["residu_max_fantome"], x["residu"]); brut["iterations_max_fantome"] = max(brut["iterations_max_fantome"], x["iterations"])
                    brut["decalages_repris_fantome"] += 1 if x.get("decalage_repris") else 0; brut["poids_min_fantome"] = min(brut["poids_min_fantome"], x["poids_site"])
out["brut"] = brut; out["durees_s"] = {"fantome_min": min(d["fantome"] for d in durees.values()), "fantome_max": max(d["fantome"] for d in durees.values()),
                                       "jumeau_min": min(d["jumeau"] for d in durees.values()), "jumeau_max": max(d["jumeau"] for d in durees.values())}

# --- 2. la table par cellule
cel = []
for r in C:
    c = TC[r["id"]]; P = r["lecteur"]["plateaux"]; k = r["consigne"]
    assert abs(r["ln_q"] - (c["ln_G3"] - r["ln_Gamma_pl"])) < 1e-12 and abs(r["bande"] - (c["etendue"] + r["etalement_du_lecteur"])) < 1e-15
    cel.append({"id": r["id"], "creneau": r["creneau"], "ligne": r["ligne"], "w2": r["w2"], "delta": r["delta"], "m": r["m"], "g": r["g"], "kappa": c["kappa"],
                "ln_Gamma_pl": r["ln_Gamma_pl"], "Gamma_pl": math.exp(r["ln_Gamma_pl"]), "s": r["etalement_du_lecteur"], "etendue": r["etendue"], "bande": r["bande"],
                "ln_q": r["ln_q"], "T": r["tolerance"], "marge": r["tolerance"] - r["bande"] - abs(r["ln_q"]), "jugement": r["jugement"],
                "statut_lecteur": r["lecteur"]["statut"], "plateaux": {a: P[a]["statut"] for a in "ABCD"}, "k0": {a: P[a]["k0"] for a in "ABCD"},
                "etalement_A": P["A"]["etalement"], "ecarts_ln_A": {a: P[a]["ecart_ln_A"] for a in "BCD"}, "suivies": r["lecteur"]["suivies"], "poids_min": r["lecteur"]["poids_min"],
                "temoin_rapport": r["temoin"]["rapport_au_plateau"], "temoin_suivies": r["temoin"]["suivies"], "temoin_tient": r["temoin"]["tient"],
                "sous_le_plancher": math.exp(r["ln_Gamma_pl"]) < 1.33e-12, "r3": c["r3"],
                "ln_q_ordre2": k["ln_q_ordre2"], "ln_q_ordre1": k["ln_q_ordre1"], "ln_q_loi": k["ln_q_loi_d_echelle"], "ln_q_forme": k["ln_q_forme_fermee"],
                "ln_Gamma_pl_sur_delta": k["ln_Gamma_pl_sur_delta"], "attente_b_mediane": c["attente"]["sous_correction_mediane"], "attente_b_pire": c["attente"]["sous_correction_pire"]})
out["cellules"] = cel
def ligne(nom):
    L = [x for x in cel if x["ligne"] == nom]; pire = max(L, key=lambda x: abs(x["ln_q"])); etroit = min(L, key=lambda x: x["marge"])
    d = {"cellules": len(L), "jugements": {j: sum(1 for x in L if x["jugement"] == j) for j in ("TIENT", "TOMBE", "NON JUGEABLE", "NON LUE")},
         "qualifiees": sum(1 for x in L if x["statut_lecteur"] == "QUALIFIE"), "temoins_tenus": sum(1 for x in L if x["temoin_tient"]),
         "abs_ln_q_max": abs(pire["ln_q"]), "abs_ln_q_max_cellule": pire["id"], "abs_ln_q_mediane": med(abs(x["ln_q"]) for x in L),
         "marge_min": etroit["marge"], "marge_min_cellule": etroit["id"], "bande_min": min(x["bande"] for x in L), "bande_max": max(x["bande"] for x in L),
         "s_min": min(x["s"] for x in L), "s_max": max(x["s"] for x in L), "s_mediane": med(x["s"] for x in L),
         "etendue_min": min(x["etendue"] for x in L), "etendue_max": max(x["etendue"] for x in L),
         "sous_l_etendue": sum(1 for x in L if abs(x["ln_q"]) < x["etendue"]), "sous_s": sum(1 for x in L if abs(x["ln_q"]) < x["s"]),
         "sous_le_plancher": [x["id"] for x in L if x["sous_le_plancher"]], "Gamma_pl_min": min(x["Gamma_pl"] for x in L), "Gamma_pl_max": max(x["Gamma_pl"] for x in L),
         "ln_Gamma_pl_min": min(x["ln_Gamma_pl"] for x in L), "ln_Gamma_pl_max": max(x["ln_Gamma_pl"] for x in L),
         "tenues_par_creneau": {s: sum(1 for x in L if x["creneau"] == s and x["jugement"] == "TIENT") for s in ORDRE}}
    for cle, nomc in (("ln_q_ordre2", "ordre2"), ("ln_q_ordre1", "ordre1"), ("ln_q_loi", "loi"), ("ln_q_forme", "forme")):
        p = max(L, key=lambda x: abs(x[cle])); d["%s_abs_max" % nomc] = abs(p[cle]); d["%s_abs_max_cellule" % nomc] = p["id"]; d["%s_abs_mediane" % nomc] = med(abs(x[cle]) for x in L)
        d["ordre3_plus_pres_que_%s" % nomc] = sum(1 for x in L if abs(x["ln_q"]) < abs(x[cle]))
    return d
out["lisible"] = ligne("lisible"); out["profonde"] = ligne("profonde")
tous = cel
out["ensemble"] = {"s_min": min(x["s"] for x in tous), "s_max": max(x["s"] for x in tous), "s_mediane": med(x["s"] for x in tous), "s_max_cellule": max(tous, key=lambda x: x["s"])["id"],
                   "decades": (max(x["ln_Gamma_pl"] for x in tous) - min(x["ln_Gamma_pl"] for x in tous)) / math.log(10.0),
                   "ln_q_mediane": med(x["ln_q"] for x in tous), "abs_ln_q_mediane": med(abs(x["ln_q"]) for x in tous),
                   "sous_la_bande": sum(1 for x in tous if abs(x["ln_q"]) < x["bande"]), "sous_l_etendue": sum(1 for x in tous if abs(x["ln_q"]) < x["etendue"]),
                   "sous_s": sum(1 for x in tous if abs(x["ln_q"]) < x["s"]), "temoin_rapport_max": max(x["temoin_rapport"] for x in tous),
                   "poids_min": min(x["poids_min"] for x in tous), "plateaux": sum(1 for x in tous for a in "ABCD" if x["plateaux"][a] == "PLATEAU"),
                   "sous_le_plancher": sum(1 for x in tous if x["sous_le_plancher"]), "etalement_A_max": max(x["etalement_A"] for x in tous),
                   "ecart_absorbeurs_max": max(x["ecarts_ln_A"][a] for x in tous for a in "BCD")}

# --- 3. signes (consigne) : recompte
sg = {"positifs": sum(1 for x in tous if x["ln_q"] > 0), "negatifs": sum(1 for x in tous if x["ln_q"] < 0),
      "du_signe_de_delta": sum(1 for x in tous if x["ln_q"] * x["delta"] > 0), "du_signe_de_la_lecture_b": sum(1 for x in tous if x["ln_q"] * x["attente_b_mediane"] > 0),
      "par_creneau": {s: {"positifs": sum(1 for x in tous if x["creneau"] == s and x["ln_q"] > 0), "cellules": sum(1 for x in tous if x["creneau"] == s),
                          "positifs_lisibles": sum(1 for x in tous if x["creneau"] == s and x["ligne"] == "lisible" and x["ln_q"] > 0)} for s in ORDRE},
      "delta_negatif": {"positifs": sum(1 for x in tous if x["delta"] < 0 and x["ln_q"] > 0), "cellules": sum(1 for x in tous if x["delta"] < 0)},
      "delta_positif": {"positifs": sum(1 for x in tous if x["delta"] > 0 and x["ln_q"] > 0), "cellules": sum(1 for x in tous if x["delta"] > 0)}}
lis = [x for x in tous if x["ligne"] == "lisible"]
dif = [x for x in lis if x["attente_b_mediane"] * x["delta"] < 0]; mem = [x for x in lis if x["attente_b_mediane"] * x["delta"] > 0]
sg["lisibles_ou_a_et_b_different"] = {"cellules": [x["id"] for x in dif], "du_signe_de_b": [x["id"] for x in dif if x["ln_q"] * x["attente_b_mediane"] > 0],
                                      "du_signe_de_a": [x["id"] for x in dif if x["ln_q"] * x["delta"] > 0]}
sg["lisibles_ou_a_et_b_coincident"] = {"cellules": [x["id"] for x in mem], "du_signe_commun": [x["id"] for x in mem if x["ln_q"] * x["delta"] > 0]}
mg = [x for x in lis if x["creneau"] == "MG"]
sg["MG_lisibles"] = [{"id": x["id"], "ln_q": x["ln_q"], "etendue": x["etendue"], "s": x["s"], "bande": x["bande"], "attente_b_mediane": x["attente_b_mediane"],
                      "attente_b_pire": x["attente_b_pire"], "r3": x["r3"], "part": (-x["ln_q"] / x["r3"]) / (1.0 - x["ln_q"] / x["r3"])} for x in mg]
out["signes"] = sg
k = V["consigne"]
out["recompte_de_la_consigne"] = {"ln_q_du_signe_de_delta": (sg["du_signe_de_delta"], k["ln_q_du_signe_de_delta"]),
                                  "ln_q_du_signe_de_la_sous_correction": (sg["du_signe_de_la_lecture_b"], k["ln_q_du_signe_de_la_sous_correction"]),
                                  "ordre3_plus_pres_que_ordre1": (out["lisible"]["ordre3_plus_pres_que_ordre1"] + out["profonde"]["ordre3_plus_pres_que_ordre1"], k["ordre3_plus_pres_que_ordre1"]),
                                  "ordre3_plus_pres_que_la_loi_d_echelle": (out["lisible"]["ordre3_plus_pres_que_loi"] + out["profonde"]["ordre3_plus_pres_que_loi"], k["ordre3_plus_pres_que_la_loi_d_echelle"]),
                                  "plus_grand_ln_q_forme_fermee": (max(out["lisible"]["forme_abs_max"], out["profonde"]["forme_abs_max"]), k["plus_grand_ln_q_forme_fermee"])}
assert all(a == b for a, b in out["recompte_de_la_consigne"].values()), out["recompte_de_la_consigne"]

# --- 4. superposition des creneaux en Gamma / |delta| (consigne) et corrections a la loi d'echelle
sup = {}
for m in sorted(set(x["m"] for x in tous)):
    L = sorted([x for x in tous if x["m"] == m], key=lambda x: ORDRE.index(x["creneau"])); assert len(L) == 4
    v = [x["ln_Gamma_pl_sur_delta"] for x in L]; kap = [x["kappa"] for x in L]
    sup[str(m)] = {"valeurs": dict((x["creneau"], x["ln_Gamma_pl_sur_delta"]) for x in L), "etendue": max(v) - min(v), "kappa_etendue_relative": max(kap) / min(kap) - 1.0,
                   "etendue_des_r3": max(x["r3"] for x in L) - min(x["r3"] for x in L),
                   "etendue_apres_la_chaine": max(x["ln_q"] for x in L) - min(x["ln_q"] for x in L)}
out["superposition"] = sup
out["corrections"] = {x["id"]: {"r3": x["r3"], "ln_q_loi": x["ln_q_loi"], "ln_q_ordre1": x["ln_q_ordre1"], "ln_q_ordre2": x["ln_q_ordre2"], "ln_q": x["ln_q"], "bande": x["bande"], "T": x["T"]}
                      for x in tous if x["id"] in ("MG12", "MG16", "MG6", "MG8")}

json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
B = brut
print("LECTURE DU RESULTAT (verdict rejoue : %s)" % V["verdict"])
print("brut : fantome %d lectures, %d suivies, residu au plus %.1e, %d iterations au plus, %d decalages repris, poids au moins %.6f ; jumeau %d lectures, %d suivies ; %s" % (
    B["lectures_fantome"], B["suivies_fantome"], B["residu_max_fantome"], B["iterations_max_fantome"], B["decalages_repris_fantome"], B["poids_min_fantome"], B["lectures_jumeau"],
    B["suivies_jumeau"], " | ".join(B["plateformes"])))
print("cellule  w2         m   ln Gamma_pl  s       etendue bande   ln q      T     marge   k0(A,B,C,D)     ordre2    ordre1    loi       forme     jugement")
for x in cel:
    print("%-7s  %-9s  %-2d  %+.4f     %.4f  %.4f  %.4f  %+.5f  %.2f  %.4f  %-14s  %+.4f   %+.4f   %+.4f   %+.4f   %s" % (
        x["id"], x["w2"], x["m"], x["ln_Gamma_pl"], x["s"], x["etendue"], x["bande"], x["ln_q"], x["T"], x["marge"], ",".join(str(x["k0"][a]) for a in "ABCD"),
        x["ln_q_ordre2"], x["ln_q_ordre1"], x["ln_q_loi"], x["ln_q_forme"], x["jugement"]))
for nom in ("lisible", "profonde"):
    d = out[nom]
    print("%s : %d cellules ; %s ; |ln q| au plus %.5f (%s), mediane %.5f ; plus petite marge %.4f (%s) ; s de %.4f a %.4f ; sous l'etendue %d, sous s %d ; sous le plancher %d" % (
        nom, d["cellules"], d["jugements"], d["abs_ln_q_max"], d["abs_ln_q_max_cellule"], d["abs_ln_q_mediane"], d["marge_min"], d["marge_min_cellule"], d["s_min"], d["s_max"],
        d["sous_l_etendue"], d["sous_s"], len(d["sous_le_plancher"])))
    print("    consigne : ordre 2 au plus %.4f (%s) ; ordre 1 au plus %.4f (%s) ; loi d'echelle au plus %.4f (%s) ; forme fermee au plus %.4f (%s) ; ordre 3 plus pres que l'ordre 2 a %d, que l'ordre 1 a %d, que la loi a %d" % (
        d["ordre2_abs_max"], d["ordre2_abs_max_cellule"], d["ordre1_abs_max"], d["ordre1_abs_max_cellule"], d["loi_abs_max"], d["loi_abs_max_cellule"], d["forme_abs_max"],
        d["forme_abs_max_cellule"], d["ordre3_plus_pres_que_ordre2"], d["ordre3_plus_pres_que_ordre1"], d["ordre3_plus_pres_que_loi"]))
e = out["ensemble"]
print("ensemble : s de %.4f a %.4f, mediane %.4f ; %.1f decades de largeur ; ln q median %+.5f ; sous la bande %d, sous l'etendue %d, sous s %d ; temoin au plus %.1e ; %d cellules sous le plancher" % (
    e["s_min"], e["s_max"], e["s_mediane"], e["decades"], e["ln_q_mediane"], e["sous_la_bande"], e["sous_l_etendue"], e["sous_s"], e["temoin_rapport_max"], e["sous_le_plancher"]))
print("signes : positifs %d, negatifs %d ; du signe de delta %d ; du signe de la lecture (b) %d ; par creneau %s ; delta < 0 : %d sur %d ; delta > 0 : %d sur %d" % (
    sg["positifs"], sg["negatifs"], sg["du_signe_de_delta"], sg["du_signe_de_la_lecture_b"], {s: "%d/%d" % (sg["par_creneau"][s]["positifs"], sg["par_creneau"][s]["cellules"]) for s in ORDRE},
    sg["delta_negatif"]["positifs"], sg["delta_negatif"]["cellules"], sg["delta_positif"]["positifs"], sg["delta_positif"]["cellules"]))
print("    lisibles ou (a) et (b) different : %s ; du signe de (b) : %s ; du signe de (a) : %s" % (" ".join(sg["lisibles_ou_a_et_b_different"]["cellules"]),
      " ".join(sg["lisibles_ou_a_et_b_different"]["du_signe_de_b"]), " ".join(sg["lisibles_ou_a_et_b_different"]["du_signe_de_a"]) or "aucune"))
print("    lisibles ou elles coincident : %s ; du signe commun : %s" % (" ".join(sg["lisibles_ou_a_et_b_coincident"]["cellules"]), " ".join(sg["lisibles_ou_a_et_b_coincident"]["du_signe_commun"]) or "aucune"))
for x in sg["MG_lisibles"]:
    print("    %s : ln q %+.5f ; etendue %.4f ; s %.4f ; attente sous (b) %.4f (mediane) a %.4f (pire) ; r3 %+.4f ; part manquee qui rendrait ce ln q : %.3f" % (
        x["id"], x["ln_q"], x["etendue"], x["s"], x["attente_b_mediane"], x["attente_b_pire"], x["r3"], x["part"]))
print("superposition en ln(Gamma_pl / |delta|), par profondeur (etendue sur les quatre creneaux ; etendue des r3 de la chaine ; etendue restante de ln q)")
for m, d in sup.items():
    print("    m = %-2s : %.4f ; %.4f ; %.4f   (kappa egal a %.1e pres)" % (m, d["etendue"], d["etendue_des_r3"], d["etendue_apres_la_chaine"], d["kappa_etendue_relative"]))
print("ecrit %s" % SORTIE)
