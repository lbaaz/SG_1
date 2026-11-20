# -*- coding: ascii -*-
"""Deux controles des pieces de la seconde partie du gel "pont" -- machine 1, v1, 2026-11-17. Aucune 2D.
(1) chaine_cellules_pont_v1.json contre la table de la premiere partie (d03c9ca093ea5bfc), aux six cellules tirees.
(2) la sonde de densite contre la sortie de l'exploration du 17/11 au point sacrifie (absorbeur A, barreau k = 3).
Usage : python3 -I -B ce_script <table de la premiere partie.json> <chaine_cellules.json> <regression.json>
                                <lisse_2d_A_v1.json de l'exploration> <sortie.json>"""
import sys, json
T, CH, REG, EXP, SORTIE = sys.argv[1:6]
ref = {(c["w2"], x["m"]): x for cr in json.load(open(T))["creneaux"].values() for c in cr["candidats"] for x in c["cellules"]}
ch = json.load(open(CH))["cellules"]; p = 0.0; n = 0
for nom, c in sorted(ch.items()):
    r = ref.get((c["w2"], c["m"]))
    if r is None: continue
    assert r["g"] == c["g"] and r["m_bord"] == c["m_bord"]; n += 1
    p = max([p, abs(c["ln_G3"] - r["ln_G3"]), abs(c["e_bord"] - r["e_bord"]), abs(c["etendue_vide"] - r["etendue"])]
            + [abs(u - v) for u, v in zip(c["ln_rho3"], r["ln_rho3"])] + [abs(u - v) for u, v in zip(c["pas_2_3"], r["pas_2_3"])]
            + [abs(u - v) for u, v in zip(c["etendue_rho3"], r["etendue_rho3"])])
a = json.load(open(REG)); b = json.load(open(EXP)); ka, kb = a["k"]["3"], b["k"]["3"]
q = max([abs(u / v - 1.0) for u, v in zip(ka["rho_flux"], kb["rho_flux"])] + [abs(ka["E_vide"] - kb["E_vide"]), abs(ka["w0"] - kb["w0"]),
        abs(ka["gamma_vide"] / kb["gamma_vide"] - 1.0)])
out = {"cellules_comparees": n, "table_ecart_max": p, "regression_ecart_max": q, "regression_absorbeur": a["absorbeur"], "regression_k": 3}
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
print("(1) %d cellules contre la table de la premiere partie : plus grand ecart %g" % (n, p))
print("(2) sonde de densite contre l'exploration (absorbeur %s, k = 3) : plus grand ecart %g" % (a["absorbeur"], q))
