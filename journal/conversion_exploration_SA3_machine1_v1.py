# -*- coding: ascii -*-
"""Remet au format de sonde_densite_2d_pont_machine1_v1.py les sorties de l'exploration du 17/11 au point sacrifie, 3
barreaux (lisse_2d_<absorbeur>_v1.json et lisse_2d_<absorbeur>_bords_v1.json, lot 55612644fc4ca279) : les deux fichiers
d'un absorbeur sont reunis, les cles de la cellule ajoutees. Aucun nombre n'est recalcule.
Usage : python3 -I -B ce_script <dossier de l'exploration> <dossier de sortie>"""
import sys, json
SRC, DST = sys.argv[1].rstrip("/"), sys.argv[2].rstrip("/")
for a in "ABCD":
    u = json.load(open("%s/lisse_2d_%s_v1.json" % (SRC, a))); v = json.load(open("%s/lisse_2d_%s_bords_v1.json" % (SRC, a)))
    assert all(u[c] == v[c] for c in ("absorbeur", "forme", "bord", "couches", "N", "X", "r_c", "eta0")) and not set(u["k"]) & set(v["k"])
    u["k"].update(v["k"]); assert sorted(int(k) for k in u["k"]) == list(range(-3, 9))
    u.update({"w2": "101/50", "m": 3, "g": "5.53067e-03", "delta": 101 / 50 - 2.0})
    json.dump(u, open("%s/densite_2d_SA3_%s_v1.json" % (DST, a), "w"), indent=1, sort_keys=True)
    print("absorbeur %s : %d barreaux reunis" % (a, len(u["k"])))
