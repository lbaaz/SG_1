# -*- coding: ascii -*-
"""Lecture de l'emulation hors echantillon : la chaine en boite rend-elle la variation de la lecture 2D entre k = 2, 3, 4 ?"""
import sys, json, math
from fractions import Fraction as F
D = json.load(open(sys.argv[1]))["etats"]
def med(x):
    x = sorted(x); n = len(x); return x[n // 2] if n % 2 else 0.5 * (x[n // 2 - 1] + x[n // 2])
def q(x, f):
    x = sorted(x); return x[min(len(x) - 1, int(f * len(x)))]
rows = []
for e in D:
    G = e["G2D"]
    if any(G.get(k) is None or G[k] <= 0 for k in ("2", "3", "4")):
        continue
    if abs(math.log(e["intr"][0] / e["intr"][1])) > 5e-3:      # la chaine sans boite n'a pas de plateau : ecartee, comptee
        e["sans_plateau"] = True
    w2 = F(e["w2"]); d = float(w2) - 2.0
    r = {"id": e["id"], "sonde": e["sonde"], "d": d, "n": (e["n1"], e["n2"]), "t_rc": e["t_rc"], "m_bord": e["m_bord"], "m_rc": e["m_rc"],
         "s2": math.log(G["2"] / G["3"]), "s4": math.log(G["4"] / G["3"]), "sans_plateau": e.get("sans_plateau", False),
         "Jet": e["J_ecart_type"], "G3": G["3"]}
    for v in ("o2", "o2b"):
        E = e["emu"][v]
        r[v + "_s2"] = math.log(E["2"] / E["3"]); r[v + "_s4"] = math.log(E["4"] / E["3"])
        r[v + "_q3"] = E["3"] / G["3"]; r[v + "_C3"] = E["3"] / e["intr"][1]
    r["q_intr"] = e["intr"][1] / G["3"]
    r["q_gel"] = (e["chaine2_flux"][2] / G["3"]) if e.get("chaine2_flux") else None
    rows.append(r)
print("etats lus :", len(rows), "; chaine sans boite sans plateau (ecart > 5e-3 entre ef 1/16 et 1/64) :", sum(r["sans_plateau"] for r in rows))
rows = [r for r in rows if not r["sans_plateau"] and (r["Jet"] is None or r["Jet"] < 0.25)]
print("retenus :", len(rows))
def bilan(nom, sel):
    if len(sel) < 3:
        print("%-34s n=%3d" % (nom, len(sel))); return
    for cle, lab in (("s2", "k=2 contre k=3"), ("s4", "k=4 contre k=3")):
        raw = [abs(r[cle]) for r in sel]
        line = "%-34s n=%3d %s : |brut| med %.4f q90 %.4f max %.4f" % (nom, len(sel), lab, med(raw), q(raw, 0.9), max(raw))
        for v in ("o2b", "o2"):
            res = [abs(r[cle] - r[v + "_" + cle]) for r in sel]
            mx = sum(r[cle] for r in sel) / len(sel); my = sum(r[v + "_" + cle] for r in sel) / len(sel)
            sxx = sum((r[cle] - mx) ** 2 for r in sel); syy = sum((r[v + "_" + cle] - my) ** 2 for r in sel)
            sxy = sum((r[cle] - mx) * (r[v + "_" + cle] - my) for r in sel)
            cor = sxy / math.sqrt(sxx * syy) if sxx > 0 and syy > 0 else float("nan")
            line += " | reste %s med %.4f q90 %.4f max %.4f corr %+.2f" % (v, med(res), q(res, 0.9), max(res), cor)
        print(line)
bilan("tous", rows)
for lab, f in (("|d| <= 0.03", lambda r: abs(r["d"]) <= 0.0301), ("0.03 < |d| <= 0.06", lambda r: 0.0301 < abs(r["d"]) <= 0.0601),
               ("0.06 < |d| <= 0.10", lambda r: 0.0601 < abs(r["d"]) <= 0.1001), ("|d| > 0.10", lambda r: abs(r["d"]) > 0.1001)):
    bilan(lab, [r for r in rows if f(r)])
for lab, f in (("t_rc <= 0.3", lambda r: r["t_rc"] <= 0.3), ("0.3 < t_rc <= 0.6", lambda r: 0.3 < r["t_rc"] <= 0.6),
               ("0.6 < t_rc <= 1.2", lambda r: 0.6 < r["t_rc"] <= 1.2), ("t_rc > 1.2", lambda r: r["t_rc"] > 1.2)):
    bilan(lab, [r for r in rows if f(r)])
print()
print("FACTEUR DE BOITE selon la chaine, C3 = emulation(k=3) / chaine sans boite, et residus :")
for lab, f in (("tous", lambda r: True), ("|d| <= 0.03", lambda r: abs(r["d"]) <= 0.0301), ("0.03 < |d| <= 0.06", lambda r: 0.0301 < abs(r["d"]) <= 0.0601),
               ("0.06 < |d| <= 0.10", lambda r: 0.0601 < abs(r["d"]) <= 0.1001), ("|d| > 0.10", lambda r: abs(r["d"]) > 0.1001)):
    sel = [r for r in rows if f(r)]
    if not sel: continue
    C = [r["o2b_C3"] for r in sel]; qi = [r["q_intr"] for r in sel]; qc = [r["o2b_q3"] for r in sel]
    print("  %-20s n=%3d  C3 : min %.3f med %.3f max %.3f | chaine sans boite / 2D(k=3) : min %.3f med %.3f max %.3f | emulation / 2D (k=3) : min %.3f med %.3f max %.3f" % (
        lab, len(sel), min(C), med(C), max(C), min(qi), med(qi), max(qi), min(qc), med(qc), max(qc)))
