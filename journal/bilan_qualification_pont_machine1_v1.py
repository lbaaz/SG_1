# -*- coding: ascii -*-
"""BILAN DE LA QUALIFICATION des deux instruments du gel "pont" au point sacrifie -- machine 1, v1, 2026-11-17.
Juge, depuis les pieces, les attendus ecrits avant (attendu_qualification_instruments 7ed5e7b6d2b65623, son rectificatif
d'heure 7654c900f4725c5d, et attendu_groupe_UN_point_sacrifie). Ne recalcule aucune lecture.
Usage : python3 -I -B ce_script <dossier de la qualification> <dossier des boites de machine 2, 3 barreaux>
                                <dossier de faisabilite de machine 2> <sortie.json>"""
import sys, json, math
Q, G, FZ, SORTIE = [a.rstrip("/") for a in sys.argv[1:5]]
def lignes(f): return [json.loads(l) for l in open(f, encoding="ascii") if l.strip()]
out = {}
# A : densite 2D
A = {m: json.load(open("%s/lecture_densite_2d_SA%d_v1.json" % (Q, m))) for m in (3, 4, 5)}
for m in (3, 4, 5):
    px = A[m]["par_x"]
    out["SA%d" % m] = {"ecarts_lisibles": A[m]["ecarts_lisibles"], "ln_R3": [p["ln_R3"] for p in px], "ln_R2": [p["ln_R2"] for p in px],
                       "ln_R3_max_abs": A[m]["ln_R3_max_abs"], "etendue_absorbeurs_max": A[m]["etendue_absorbeurs_max"], "w0": A[m]["w0"],
                       "etalement_max": max(max(q["etalement"] for q in p["plateaux"].values()) for p in px),
                       "vide_ln_chaine3_sur_2d": {a: v["ln_chaine3_sur_2d"] for a, v in A[m]["vide"].items()},
                       "ordre3_plus_pres_x_ge_5": all(abs(p["ln_R3"]) < abs(p["ln_R2"]) for p in px if p["x"] >= 5.0),
                       "ordre3_plus_pres_x_ge_4": all(abs(p["ln_R3"]) < abs(p["ln_R2"]) for p in px if p["x"] >= 4.0),
                       "marge_x4": abs(px[7]["ln_R2"]) - abs(px[7]["ln_R3"])}
out["A1"] = {"tient": A[4]["ecarts_lisibles"] == 12}
out["A2"] = {"tient": A[5]["ecarts_lisibles"] == 12}
out["A3"] = {"tient": max(A[4]["ln_R3_max_abs"], A[5]["ln_R3_max_abs"]) <= 0.02, "max_4": A[4]["ln_R3_max_abs"], "max_5": A[5]["ln_R3_max_abs"]}
out["A4"] = {"tient": all(A[m]["par_x"][-1]["ln_R3"] < A[m]["par_x"][0]["ln_R3"] for m in (4, 5)),
             "R3_8_moins_R3_005": {str(m): A[m]["par_x"][-1]["ln_R3"] - A[m]["par_x"][0]["ln_R3"] for m in (3, 4, 5)}}
# B : boites fermees contre machine 2
mes = {}
for f in ("boite_SA3_200_v1.jsonl", "boite_SA3_300_v1.jsonl", "boite_SA4_300_v1.jsonl", "boite_SA5_300_v1.jsonl", "boites_SA3_UN_v1.jsonl"):
    for b in lignes("%s/%s" % (Q, f)): mes[(b["m"], b["cote"])] = b
ref = {}
for f in ["%s/gb200_w%d.jsonl" % (G, i) for i in (1, 2, 3, 4)] + ["%s/gb300_w%d.jsonl" % (G, i) for i in (1, 2, 3)] + \
         ["%s/boite300_4barreaux.jsonl" % FZ, "%s/boite300_5barreaux.jsonl" % FZ]:
    for r in lignes(f): ref[(r.get("barreaux", 3), r["cote"])] = r
conf = json.load(open("%s/lecture_boites_qualification_v1.json" % Q))["confrontation"]
lect = {(c["m"], b["cote"]): b for c in json.load(open("%s/lecture_boites_qualification_v1.json" % Q))["cellules"] for b in c["boites"]}
pire_brut = 0.0
for c in conf:
    b = mes[(c["m"], c["cote"])]; q = ref[(c["m"], c["cote"])]; L = lect[(c["m"], c["cote"])]
    yo = sorted(q["niveaux"], key=lambda v: -v["off"]); ym = sorted(zip(L["x"], L["y"], b["niveaux"]), key=lambda t: t[0])
    for o, (x, y, v) in zip(yo, ym):
        if o["fiable"]: pire_brut = max(pire_brut, abs(y * v["brut_a"] / v["c2_a"] / o["y1"] - 1.0))
out["confrontation"] = conf
out["B1"] = {"tient": all(c["n_m1"] == c["n_m2"] and c["ecart_x_max"] <= 1e-6 for c in conf), "boites": len(conf),
             "ecart_x_max": max(c["ecart_x_max"] for c in conf)}
out["B2"] = {"tient": pire_brut <= 0.02, "ecart_max_brut_contre_ses_fiables": pire_brut,
             "ecart_max_partition_contre_ses_fiables": max(c["ecart_y_max_fiables_m2"] for c in conf)}
bp3 = {k[1]: max(abs(v["brut_a"] / v["c2_a"] - 1.0) for v in b["niveaux"]) for k, b in mes.items() if k[0] == 3 and k[1] != 120}
out["B3"] = {"tient": max(bp3.values()) <= 1e-3, "boites": len(bp3), "max": max(bp3.values()), "cote_du_max": max(bp3, key=bp3.get),
             "mediane": sorted(bp3.values())[len(bp3) // 2], "au_dessus_de_1e-3": sorted(c for c, v in bp3.items() if v > 1e-3)}
b5 = mes[(5, 300)]; niv = min(b5["niveaux"], key=lambda v: abs(v["x"] - 6.699))
out["B4"] = {"tient": abs(niv["c2_b"] / niv["c2_a"] - 1.0) <= 1e-3, "x": niv["x"], "partition_a_b": abs(niv["c2_b"] / niv["c2_a"] - 1.0),
             "brut_a_b": abs(niv["brut_b"] / niv["brut_a"] - 1.0), "y_m2": [v for v in ref[(5, 300)]["niveaux"] if not v["fiable"]]}
out["accords"] = {str(m): {"partition_a_b_max": max(abs(v["c2_b"] / v["c2_a"] - 1.0) for v in mes[(m, 300)]["niveaux"]),
                           "brut_a_b_max": max(abs(v["brut_b"] / v["brut_a"] - 1.0) for v in mes[(m, 300)]["niveaux"]),
                           "rayon_max": max(abs(v["c2_a_large"] / v["c2_a"] - 1.0) for v in mes[(m, 300)]["niveaux"]),
                           "secondes": mes[(m, 300)]["secondes"]} for m in (3, 4, 5)}
out["rayon_max_toutes_boites"] = max(abs(v["c2_a_large"] / v["c2_a"] - 1.0) for b in mes.values() for v in b["niveaux"])
out["partition_a_b_max_toutes_boites"] = max(abs(v["c2_b"] / v["c2_a"] - 1.0) for b in mes.values() for v in b["niveaux"])
# U : groupe UN au point sacrifie
rep = [c for c in json.load(open("%s/lecture_boites_repetition_v1.json" % Q))["cellules"] if c["m"] == 3][0]
un = [b for b in rep["boites"] if 180 <= b["cote"] <= 189]; S = [b["S"] for b in un]; n = [b["n"] for b in un]
mo = sum(S) / len(S); sd = math.sqrt(sum((s - mo) ** 2 for s in S) / (len(S) - 1)); nm = sum(n) / len(n)
out["UN"] = {"boites": len(un), "S_moyenne": mo, "S_ecart_type": sd, "S_erreur": sd / math.sqrt(len(S)), "n_moyen": nm, "n_min": min(n), "n_max": max(n),
             "compte_reduit": nm / ((sum(b["cote"] for b in un) / len(un)) * 7.95 * 0.02), "tous_fiables": all(b["fiables"] == b["n"] for b in un),
             "secondes_par_boite": sum(mes[(3, c)]["secondes"] for c in range(180, 190)) / 10.0}
out["U1"] = {"tient": 8 <= nm <= 11}; out["U2"] = {"tient": 0.90 <= mo <= 1.15}; out["U3"] = {"tient": 0.08 <= sd <= 0.20}
out["U4"] = {"tient": out["UN"]["tous_fiables"]}
b300 = {m: lect[(m, 300)] for m in (3, 4, 5)}
out["cote_300"] = {str(m): {"n": b300[m]["n"], "S": b300[m]["S"], "compte_reduit": b300[m]["n"] / (300 * 7.95 * 0.02)} for m in (3, 4, 5)}
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
for k in ("A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "U1", "U2", "U3", "U4"):
    print("%s : %s   %s" % (k, "TIENT" if out[k]["tient"] else "TOMBE", json.dumps({a: b for a, b in out[k].items() if a not in ("tient", "y_m2")}, sort_keys=True)))
print("UN :", json.dumps(out["UN"], sort_keys=True)); print("accords :", json.dumps(out["accords"], sort_keys=True))
print("cote 300 :", json.dumps(out["cote_300"], sort_keys=True))
for m in (3, 4, 5): print("SA%d : |ln R3| max %.4f ; ordre 3 plus pres pour x >= 5 : %s ; pour x >= 4 : %s (marge a x = 4 : %.4f)"
                          % (m, out["SA%d" % m]["ln_R3_max_abs"], out["SA%d" % m]["ordre3_plus_pres_x_ge_5"], out["SA%d" % m]["ordre3_plus_pres_x_ge_4"], out["SA%d" % m]["marge_x4"]))
