# -*- coding: ascii -*-
"""COMPARAISON DU REJEU DE MACHINE 1 AU RUN JUGE DE BOCAL4 -- gel E-B ter, section 12 : apres reception et
authentification du lot de resultat, machine 1 "peut ensuite rejouer, et compare alors a 1e-6 en relatif sur les
lectures suivies". Non opposable.
Deux rejeux : (1) la sonde certifiee, telle quelle, en mode point a L3 (sonde_ter_point_L3.json) ; (2) le code de la
sonde restreint a des etats choisis d'autres points (rejeu_partiel_<id>.json).
Usage : python3 -I comparaison_rejeu_machine1_v1.py <dossier du run> <sortie de la sonde rejouee a L3 (.json)>
        <dossier des rejeu_partiel_<id>.json> <sortie.json>"""
import sys, os, json, math, glob
RUN, RL3, RPA, SORTIE = sys.argv[1:5]
TOL = 1e-6
KS = [str(k) for k in range(-3, 9)]
def charger_run(pid):
    s = json.load(open(os.path.join(RUN, "sonde_ter_point_%s.json" % pid)))
    return s, {e["rang"]: e for e in s["points"][0]["etats"]}
def comparer(pid, mes_etats, bilan):
    s, run = charger_run(pid)
    for e in mes_etats:
        r = run[e["rang"]]
        assert (e["n1"], e["n2"]) == (r["n1"], r["n2"]) and e["E_depart"] == r["E_depart"], (pid, e["rang"])
        pire = 0.0
        for x in "ABCD":
            for k in KS:
                a, b = e["traj"][x][k], r["traj"][x][k]
                bilan["lectures"] += 1
                if a["suivi"] != b["suivi"]:
                    bilan["statuts_differents"].append([pid, e["rang"], x, int(k)]); continue
                if not a["suivi"]:
                    bilan["non_suivies"] += 1; continue
                d = abs(a["gamma"] - b["gamma"]) / abs(b["gamma"]); pire = max(pire, d)
                bilan["pire_E"] = max(bilan["pire_E"], abs(a["E_re"] - b["E_re"]))
                bilan["iterations_differentes"] += (a["iterations"] != b["iterations"])
                if d > TOL:
                    bilan["hors"].append([pid, e["rang"], x, int(k), d])
        bilan["etats"].append([pid, e["rang"], pire]); bilan["pire"] = max(bilan["pire"], pire)
B = {"tolerance": TOL, "lectures": 0, "non_suivies": 0, "statuts_differents": [], "hors": [], "pire": 0.0, "pire_E": 0.0,
     "iterations_differentes": 0, "etats": [], "rejeu_L3": None, "rejeu_partiel": []}
f = RL3
if os.path.exists(f):
    m = json.load(open(f)); sr, _ = charger_run("L3")
    assert m["mode"] == "point" and m["ids"] == ["L3"] and m["sonde_canon"] == sr["sonde_canon"] == "b5616dcf858e8801"
    assert m["reglage"] == sr["reglage"] and m["depot_canon"] == sr["depot_canon"]
    assert [e["rang"] for e in m["points"][0]["etats"]] == [e["rang"] for e in sr["points"][0]["etats"]]
    n0 = B["lectures"]; comparer("L3", m["points"][0]["etats"], B)
    B["rejeu_L3"] = {"etats": len(m["points"][0]["etats"]), "lectures": B["lectures"] - n0, "duree_s": m["duree_s"], "plateforme": m["plateforme"]}
for f in sorted(glob.glob(os.path.join(RPA, "rejeu_partiel_*.json"))):
    m = json.load(open(f)); assert m["sonde_canon"] == "b5616dcf858e8801" and m["rejeu_partiel"] is True
    assert sorted(e["rang"] for e in m["point"]["etats"]) == sorted(m["rangs"])
    n0 = B["lectures"]; comparer(m["id"], m["point"]["etats"], B)
    B["rejeu_partiel"].append({"id": m["id"], "rangs": sorted(m["rangs"]), "lectures": B["lectures"] - n0, "duree_s": m["point"]["duree_s"]})
B["n_etats"] = len(B["etats"]); B["points"] = sorted(set(e[0] for e in B["etats"]))
B["tient"] = (not B["statuts_differents"]) and (not B["hors"]) and B["lectures"] > 0
json.dump(B, open(SORTIE, "w"), indent=1, sort_keys=True)
print("REJEU DE MACHINE 1 CONTRE LE RUN DE BOCAL4 (tolerance %g en relatif sur les lectures suivies)" % TOL)
if B["rejeu_L3"]:
    print("  sonde certifiee en mode point a L3 : %d etats, %d lectures, %.0f s" % (B["rejeu_L3"]["etats"], B["rejeu_L3"]["lectures"], B["rejeu_L3"]["duree_s"]))
for r in B["rejeu_partiel"]:
    print("  code de la sonde restreint, %s rangs %s : %d lectures, %.0f s" % (r["id"], r["rangs"], r["lectures"], r["duree_s"]))
print("  %d etats de %d points, %d lectures ; non suivies %d ; statuts de suivi differents %d ; hors tolerance %d" % (
    B["n_etats"], len(B["points"]), B["lectures"], B["non_suivies"], len(B["statuts_differents"]), len(B["hors"])))
print("  pire ecart relatif de largeur %.2e ; pire ecart d'energie %.2e ; lectures au nombre d'iterations different %d" % (
    B["pire"], B["pire_E"], B["iterations_differentes"]))
print("COMPARAISON : %s" % ("TIENT" if B["tient"] else "NE TIENT PAS"))
sys.exit(0 if B["tient"] else 1)
