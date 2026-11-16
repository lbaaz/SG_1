# -*- coding: ascii -*-
"""Lecture de l'exploration de reglage par les fonctions de la feuille ter (juger_etat), etat par etat.
Usage : python3 -I lecture_exploration_etats_machine1_v1.py <feuille.py> <exploration.json> [...]"""
import sys, json, math, importlib.util
spec = importlib.util.spec_from_file_location("feuille", sys.argv[1])
Fe = importlib.util.module_from_spec(spec); spec.loader.exec_module(Fe)
P = {}
for f in sys.argv[2:]:
    P.update(json.load(open(f))["points"])
def med(x):
    x = sorted(x); n = len(x); return x[n // 2] if n % 2 else 0.5 * (x[n // 2 - 1] + x[n // 2])
tous = []
for pid in P:
    p = P[pid]; d = float(eval(p["w2"].replace("/", "*1.0/"))) - 2.0
    print("=== %s w2 = %s (delta %+.2f) facteur %s r_c %d : %d etats" % (pid, p["w2"], d, p["facteur"], p["r_c"], len(p["etats"])))
    for cle, e in sorted(p["etats"].items(), key=lambda kv: kv[1]["rang"]):
        j = Fe.juger_etat(e["cfg"], e["G2D"]["3"])
        pl = j["plateaux"]
        tous.append((pid, e["rang"], j, e["G2D"]["3"], d))
        print("  rang %2d (%2d,%d) G_dep %.3e %-13s %s | depot/plateau %s%s" % (
            e["rang"], e["n1"], e["n2"], e["G2D"]["3"], j["statut"],
            " ".join("%s %.4f k0=%+d" % (x, pl[x]["etalement"], pl[x]["k0"]) if "k0" in pl[x] else "%s --" % x for x in "ABCD"),
            "%.4f" % (e["G2D"]["3"] / pl["A"]["Gamma_pl"]) if pl["A"]["statut"] == "PLATEAU" else "-",
            "".join(" ; " + x for x in j["echecs"])))
print()
n = len(tous); print("ETATS :", n, "; QUALIFIES", sum(1 for t in tous if t[2]["statut"] == "QUALIFIE"), "; NON QUALIFIES", sum(1 for t in tous if t[2]["statut"] == "NON QUALIFIE"),
      "; NON LISIBLES", sum(1 for t in tous if t[2]["statut"] == "NON LISIBLE"))
for x in "ABCD":
    es = [t[2]["plateaux"][x]["etalement"] for t in tous if "k0" in t[2]["plateaux"][x]]
    print("  etalement sous %s : mediane %.4f, max %.4f ; au-dessus de 0.01 : %d ; au-dessus de 0.02 : %d ; au-dessus de 0.05 : %d" % (
        x, med(es), max(es), sum(e > 0.01 for e in es), sum(e > 0.02 for e in es), sum(e > 0.05 for e in es)))
for x in "BCD":
    ec = [t[2]["plateaux"][x]["ecart_ln_A"] for t in tous if "ecart_ln_A" in t[2]["plateaux"][x]]
    print("  accord %s / A : |ln| mediane %.4f, max %.4f" % (x, med(ec), max(ec)))
dp = [t[2]["ecart_ln_depot"] for t in tous if t[2]["ecart_ln_depot"] is not None]
print("  |ln(depot / plateau A)| : mediane %.4f, max %.4f ; au-dessus de 0.05 : %d sur %d ; au-dessus de 0.02 : %d" % (med(dp), max(dp), sum(e > 0.05 for e in dp), len(dp), sum(e > 0.02 for e in dp)))
r0 = [t for t in tous if t[1] == 0]
print("  etats de rang 0 :", [(t[0], t[2]["statut"]) for t in r0])
