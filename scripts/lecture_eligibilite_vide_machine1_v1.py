# -*- coding: ascii -*-
"""LECTURE DE L'ELIGIBILITE DES CELLULES CANDIDATES DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16.
Reunit les sorties par creneaux en UNE table (le format que lit tirage_vide_machine1_v1.py), l'ecrit, et imprime la
table de la piece. Aucun calcul de physique. Si une seconde serie de sorties est donnee (meme calcul sous un autre
reglage de numpy), dit de combien les deux different.
Usage : python3 -I lecture_eligibilite_vide_machine1_v1.py <sortie.json> <eligibilite A.json> <eligibilite B.json> [--autre <A'.json> <B'.json>]"""
import sys, json, math
from fractions import Fraction as F
SORTIE = sys.argv[1]; reste = sys.argv[2:]
autres = reste[reste.index("--autre") + 1:] if "--autre" in reste else []
fichiers = reste[:reste.index("--autre")] if "--autre" in reste else reste
ORDRE = ("MG", "MP", "PP", "PG"); LISIBLES = (3, 4, 5, 6); PROFONDES = (8, 12, 16)
def reunir(fs):
    T = {"creneaux": {}}; regle = None
    for f in fs:
        J = json.load(open(f))
        assert regle is None or regle == J["regle"], "les sorties n'ont pas la meme regle"
        regle = J["regle"]
        for s, v in J["creneaux"].items():
            assert s not in T["creneaux"]; T["creneaux"][s] = v
    assert sorted(T["creneaux"]) == sorted(ORDRE)
    T["regle"] = regle
    return T
T = reunir(fichiers)
n_w2 = n_cel = 0
for s in ORDRE:
    cands = T["creneaux"][s]["candidats"]
    assert [F(c["w2"]) for c in cands] == sorted(F(c["w2"]) for c in cands) and len(cands) == 9
    print("creneau %s : %d w2 eligibles sur %d ; cellules profondes retenues : %d sur %d" % (s, sum(c["eligible"] for c in cands), len(cands),
          sum(x["eligible"] for c in cands for x in c["cellules"] if not x["lisible"]), sum(1 for c in cands for x in c["cellules"] if not x["lisible"])))
    for c in cands:
        assert [x["m"] for x in c["cellules"]] == list(LISIBLES + PROFONDES)
        assert c["eligible"] == all(x["eligible"] for x in c["cellules"] if x["lisible"])
        n_w2 += 1; n_cel += len(c["cellules"])
        print("  %.3f  %s  %s" % (float(F(c["w2"])), "  ".join("m%d %s %s%s" % (x["m"], x["g"], ("%.4f" % x["etendue"]) if x.get("etendue") is not None else "----",
              "" if x["eligible"] else " !") for x in c["cellules"]), "ELIGIBLE" if c["eligible"] else "INELIGIBLE"))
print("en tout : %d w2 candidats, %d cellules" % (n_w2, n_cel))
print("par profondeur : m ; barreaux trouves ; plus grande etendue ; plus grand e_bord ; plus grande boite du lecteur ; largeur predite, de ... a ... ; methode")
resume = {}
for m in LISIBLES + PROFONDES:
    X = [x for s in ORDRE for c in T["creneaux"][s]["candidats"] for x in c["cellules"] if x["m"] == m]
    r = {"m_bord": sorted(set(x["m_bord"] for x in X)), "etendue_max": max(x["etendue"] for x in X), "e_bord_max": max(x["e_bord"] for x in X), "N_max": max(x["N_max"] for x in X),
         "G_min": math.exp(min(x["ln_G3"] for x in X)), "G_max": math.exp(max(x["ln_G3"] for x in X)), "methodes": sorted(set(y for x in X for y in x["methodes"])),
         "poids_min": min(x["poids_min"] for x in X), "eligibles": sum(x["eligible"] for x in X), "cellules": len(X)}
    resume[str(m)] = r
    print("  m = %-2d ; %s ; %.4f ; %.3f ; %d ; %.1e a %.1e ; %s ; %d eligibles sur %d" % (m, r["m_bord"], r["etendue_max"], r["e_bord_max"], r["N_max"], r["G_min"], r["G_max"], "/".join(r["methodes"]), r["eligibles"], r["cellules"]))
T["resume"] = resume; T["comptes"] = {"w2": n_w2, "cellules": n_cel}
if autres:
    U = reunir(autres); pire_ln = pire_et = 0.0; bascule = 0; g_diff = 0
    for s in ORDRE:
        for c, c2 in zip(T["creneaux"][s]["candidats"], U["creneaux"][s]["candidats"]):
            assert c["w2"] == c2["w2"]
            for x, y in zip(c["cellules"], c2["cellules"]):
                pire_ln = max(pire_ln, abs(x["ln_G3"] - y["ln_G3"])); pire_et = max(pire_et, abs(x["etendue"] - y["etendue"]))
                bascule += (x["eligible"] != y["eligible"]); g_diff += (x["g"] != y["g"])
    T["autre_reglage"] = {"ecart_ln_G3_max": pire_ln, "ecart_etendue_max": pire_et, "eligibilites_changees": bascule, "couplages_changes": g_diff}
    print("autre reglage de numpy : plus grand ecart sur ln G3 %.2e, sur l'etendue %.2e ; eligibilites changees : %d ; couplages ecrits changes : %d" % (pire_ln, pire_et, bascule, g_diff))
json.dump(T, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit : %s" % SORTIE)
