# -*- coding: ascii -*-
"""Statistiques du journal ordre3_toutes_cellules.log (machine 2). Usage : py -3.11 -I stat_ordre3_machine2_v1.py <journal>"""
import sys, re
import numpy as np
R = []
for ligne in open(sys.argv[1], encoding="ascii", errors="replace"):
    m = re.match(r"^(\d)\s+(\w+)\s+(\d)\s+(\d+)\s+(\d\.\d+e[-+]\d+)\s+(\S+)\s+(\S+)\s+([-+]\d\.\d+)\s+(\d\.\d+) \((\d\.\d+)\.\.(\d\.\d+)\) (\d+)\s+([-+]\d\.\d+)\s+(.*)$", ligne)
    if m:
        R.append(dict(ordre=int(m.group(1)), cel=m.group(2), prof=int(m.group(3)), N=int(m.group(4)), V=m.group(5), V1=m.group(6), res=float(m.group(8)),
                      r=float(m.group(9)), corr=float(m.group(13)), mono=m.group(14).strip().startswith("monotone")))
print("lignes lues :", len(R), "| V identique a celui de m1 (chaine) :", sum(1 for x in R if x["V"] == x["V1"]), "sur", len(R))
for o in (1, 3):
    for lab, filtre in (("monotones", lambda x: x["mono"]), ("non monotones", lambda x: not x["mono"])):
        S = [x for x in R if x["ordre"] == o and filtre(x)]
        if not S:
            continue
        a = np.array([x["res"] for x in S]); b = np.array([x["corr"] for x in S]); r = np.array([x["r"] for x in S])
        print("ordre %d %-13s n=%2d  residu brut : min %+.4f max %+.4f moy %+.4f | r : %.3f..%.3f | residu corrige : min %+.4f max %+.4f moy %+.4f" % (o, lab, len(S), a.min(), a.max(), a.mean(), r.min(), r.max(), b.min(), b.max(), b.mean()))
# ordre 3 moins ordre 1, memes (cellule, N)
d1 = {(x["cel"], x["N"]): x for x in R if x["ordre"] == 1 and x["mono"]}
dd = [(x["res"] - d1[(x["cel"], x["N"])]["res"], x["cel"], x["N"]) for x in R if x["ordre"] == 3 and x["mono"] and (x["cel"], x["N"]) in d1]
a = np.array([v for v, c, n in dd])
print("residu(ordre 3) - residu(ordre 1), memes (cellule, N) : n=%d  min %+.4f max %+.4f moy %+.4f ; |ecart| > 0.01 : %d" % (len(a), a.min(), a.max(), a.mean(), int((abs(a) > 0.01).sum())))
for v, c, n in sorted(dd, key=lambda t: -abs(t[0]))[:4]:
    print("   plus grand ecart :", c, n, "%+.4f" % v)
