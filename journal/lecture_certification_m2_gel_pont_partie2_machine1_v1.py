# -*- coding: ascii -*-
"""Lecture par machine 1 de la certification par machine 2 de la seconde partie du gel "pont" -- v1, 2026-11-17.
Aucun script de machine 2 n'est lance ; ses sorties sont lues comme des donnees. Aucune 2D.
(1) Ses sorties de sondes au point sacrifie contre les miennes, nombre par nombre.
(2) Son fait 2.5 : ma feuille de densite accepte-t-elle en silence une sortie tronquee (barreaux -3 a 5) ?
Usage : python3 -I -B ce_script <dossier sacrifie de machine 2> <dossier qualif de machine 1> <dossier partie2 de machine 1>
                                <sortie.json>"""
import sys, os, json, math, subprocess, tempfile, shutil
S2, QU, P2, SORTIE = [a.rstrip("/") for a in sys.argv[1:5]]
out = {}
a = json.load(open(S2 + "/densite_2d_SA5_A_machine2.json")); b = json.load(open(QU + "/densite_2d_SA5_A_v1.json"))
assert sorted(a["k"]) == sorted(b["k"]) and len(a["k"]) == 12
out["densite_SA5_A"] = {"barreaux": len(a["k"]),
    "ln_rho_ecart_max": max(abs(math.log(u / v)) for k in a["k"] for u, v in zip(a["k"][k]["rho_flux"], b["k"][k]["rho_flux"])),
    "gamma_vide_ecart_relatif_max": max(abs(a["k"][k]["gamma_vide"] / b["k"][k]["gamma_vide"] - 1.0) for k in a["k"]),
    "w0_ecart_max": max(abs(a["k"][k]["w0"] - b["k"][k]["w0"]) for k in a["k"])}
def boite(f, cote):
    for l in open(f, encoding="ascii"):
        if l.strip():
            r = json.loads(l)
            if r["cote"] == cote: return r
bo = {}
for nom2, nom1, cote in (("boite_SA3_185_machine2.jsonl", "boites_SA3_UN_v1.jsonl", 185), ("boite_SA3_300_machine2.jsonl", "boite_SA3_300_v1.jsonl", 300),
                         ("boite_SA4_300_machine2.jsonl", "boite_SA4_300_v1.jsonl", 300), ("boite_SA5_300_machine2.jsonl", "boite_SA5_300_v1.jsonl", 300)):
    u = boite(S2 + "/" + nom2, cote); v = boite(QU + "/" + nom1, cote)
    assert u["n"] == v["n"] and u["listes_identiques"] and v["listes_identiques"]
    bo["%s cote %d" % (nom2[6:9], cote)] = {"n": u["n"], "fiables_m2": u["fiables"], "fiables_m1": v["fiables"],
        "x": max(abs(p["x"] - q["x"]) for p, q in zip(u["niveaux"], v["niveaux"])),
        "c2_a": max(abs(p["c2_a"] / q["c2_a"] - 1.0) for p, q in zip(u["niveaux"], v["niveaux"])),
        "c2_b": max(abs(p["c2_b"] / q["c2_b"] - 1.0) for p, q in zip(u["niveaux"], v["niveaux"])),
        "brut_a": max(abs(p["brut_a"] / q["brut_a"] - 1.0) for p, q in zip(u["niveaux"], v["niveaux"])),
        "w0": abs(u["w0"] - v["w0"]), "secondes_m2": u["secondes"]}
out["boites"] = bo
with tempfile.TemporaryDirectory() as tmp:
    fs = []
    for ab in "ABCD":
        d = json.load(open("%s/densite_2d_SA5_%s_v1.json" % (QU, ab))); d["k"] = {k: v for k, v in d["k"].items() if int(k) <= 5}
        json.dump(d, open("%s/t_%s.json" % (tmp, ab), "w")); fs.append("%s/t_%s.json" % (tmp, ab))
    r = subprocess.run([sys.executable, "-I", "-B", P2 + "/lecture_densite_2d_pont_machine1_v1.py", P2 + "/chaine_cellules_pont_v1.json", "SA5", tmp + "/l.json"] + fs,
                       capture_output=True, text=True)
    out["sortie_tronquee"] = {"barreaux_gardes": 9, "code_de_sortie": r.returncode}
    if r.returncode == 0:
        t = json.load(open(tmp + "/l.json")); ref = json.load(open(QU + "/lecture_densite_2d_SA5_v1.json"))
        out["sortie_tronquee"].update({"ecarts_lisibles": t["ecarts_lisibles"],
            "ln_R3_ecart_max_a_la_lecture_complete": max(abs(p["ln_R3"] - q["ln_R3"]) for p, q in zip(t["par_x"], ref["par_x"]) if p["lisible"] and q["lisible"])})
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True); print(json.dumps(out, indent=1, sort_keys=True))
