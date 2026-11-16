# -*- coding: ascii -*-
"""RECOUPEMENT DES DEUX TABLES D'ELIGIBILITE DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16. Aucun calcul de physique.
Compare la table de machine 1 et celle de machine 2 champ par champ (w2, eligibilite du w2, et par cellule : m, couplage
ecrit, eligibilite), puis ecrit LA TABLE COMMUNE (le ET, section 5 du gel) au format de la section 5.
Si le detail de machine 2 est donne, compare aussi l'etendue et le logarithme du plateau.
Usage : python3 -I -B recoupe_tables_vide_machine1_v1.py <table machine 1.json> <table machine 2.json> <sortie table commune.json> [<detail machine 2.json>]"""
import sys, json
from fractions import Fraction as F
T1 = json.load(open(sys.argv[1])); T2 = json.load(open(sys.argv[2])); SORTIE = sys.argv[3]
ORDRE = ("MG", "MP", "PP", "PG"); LIS = (3, 4, 5, 6)
n_w2 = n_cel = d_w2 = d_g = d_el = d_m = 0; commune = {"creneaux": {}}; el_c = 0; prof_c = 0
for s in ORDRE:
    a, b = T1["creneaux"][s]["candidats"], T2["creneaux"][s]["candidats"]
    assert [F(x["w2"]) for x in a] == [F(x["w2"]) for x in b], "listes de w2 differentes au creneau %s" % s
    cands = []
    for x, y in zip(a, b):
        n_w2 += 1; d_w2 += (bool(x["eligible"]) != bool(y["eligible"])); cs = []; memes_g = True
        assert len(x["cellules"]) == len(y["cellules"]) == 7
        for u, v in zip(x["cellules"], y["cellules"]):
            n_cel += 1; d_m += (int(u["m"]) != int(v["m"])); d_g += (str(u["g"]) != str(v["g"])); d_el += (bool(u["eligible"]) != bool(v["eligible"]))
            memes_g = memes_g and str(u["g"]) == str(v["g"])
            cs.append({"m": int(u["m"]), "g": str(u["g"]), "eligible": bool(u["eligible"]) and bool(v["eligible"])})
        el = bool(x["eligible"]) and bool(y["eligible"]) and memes_g and all(c["eligible"] for c in cs if c["m"] in LIS)
        el_c += el; prof_c += sum(c["eligible"] for c in cs if c["m"] not in LIS)
        cands.append({"w2": x["w2"], "eligible": el, "cellules": cs})
    commune["creneaux"][s] = {"candidats": cands}
print("w2 compares : %d ; cellules comparees : %d" % (n_w2, n_cel))
print("desaccords : eligibilite d'un w2 %d ; profondeur %d ; couplage ecrit %d ; eligibilite d'une cellule %d" % (d_w2, d_m, d_g, d_el))
print("TABLE COMMUNE : %d w2 eligibles sur %d ; cellules profondes retenues : %d sur %d" % (el_c, n_w2, prof_c, 3 * n_w2))
if len(sys.argv) > 4:
    DT = json.load(open(sys.argv[4])); pire_e = pire_l = 0.0; vus = 0
    def cellules_du_detail(o):
        if isinstance(o, dict):
            if "etendue" in o and "m" in o:
                yield o
            for v in o.values():
                for z in cellules_du_detail(v): yield z
        elif isinstance(o, list):
            for v in o:
                for z in cellules_du_detail(v): yield z
    mien = {}
    for s in ORDRE:
        for x in T1["creneaux"][s]["candidats"]:
            for u in x["cellules"]:
                mien[(str(u["g"]), int(u["m"]))] = u
    for z in cellules_du_detail(DT):
        cle = (str(z.get("g")), int(z["m"]))
        if cle in mien:
            vus += 1; pire_e = max(pire_e, abs(z["etendue"] - mien[cle]["etendue"]))
            for nom in ("ln_G3", "ln_plateau", "ln_G3_etoile", "ln_G"):
                if nom in z:
                    pire_l = max(pire_l, abs(z[nom] - mien[cle]["ln_G3"])); break
    print("detail de machine 2 : %d cellules retrouvees par (couplage ecrit, m) ; plus grand ecart d'etendue %.1e ; du logarithme du plateau %.1e" % (vus, pire_e, pire_l))
json.dump(commune, open(SORTIE, "w"), indent=1, sort_keys=True)
ok = (d_w2, d_m, d_g, d_el) == (0, 0, 0, 0)
print("RECOUPEMENT : %s" % ("AUCUN DESACCORD" if ok else "DES DESACCORDS"))
