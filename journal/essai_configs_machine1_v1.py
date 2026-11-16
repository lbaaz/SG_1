# -*- coding: ascii -*-
"""Essai de reglage : des etats de points de reglage sous une liste d'absorbeurs (forme:decalage du bord:couches),
sur l'echelle k = -3 a 10. Usage : <moteur.py> <bloc.py> <sonde.json> <id> <n1_n2> [...] -- <F:dr:L> [...]"""
import sys, json, math, time, importlib.util
from fractions import Fraction as F
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sl
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(sys.argv[2]).read(), sys.argv[2], "exec"))
i = sys.argv.index("--"); pid = sys.argv[4]; sites = sys.argv[5:i]
CF = [(c.split(":")[0], int(c.split(":")[1]), int(c.split(":")[2])) for c in sys.argv[i + 1:]]
p = [q for q in json.load(open(sys.argv[3]))["points"] if q["id"] == pid][0]
num, den = p["w2"].split("/"); w2 = F(int(num), int(den)); r_c = p["r_c"]; eta0 = p["eta0"]
KS = list(range(-3, 11)); t0 = time.time(); Nmax = r_c + max(dr + L for _, dr, L in CF)
H0m, dm = assembler(w2, p["g"], Nmax)
print("%s w2 %s facteur %s g %.3e r_c %d eta0 %.2f" % (pid, p["w2"], p["facteur"], p["g"], r_c, eta0), flush=True)
for s in sites:
    n1, n2 = [int(x) for x in s.split("_")]
    e = [x for x in p["etats"] if int(x["n1"]) == n1 and int(x["n2"]) == n2][0]
    ref = None
    for forme, dr, L in CF:
        N = r_c + dr + L; H0, dg = restreindre(H0m, dm, Nmax, N)
        tr = trajectoire(H0, dg, table_W(N, forme, r_c + dr, L), eta0, N, (n1, n2), e["E_re"], KS)
        v = [tr[str(k)]["gamma"] for k in KS]
        fen = [(max(v[j:j + 5]) / min(v[j:j + 5]) - 1.0, KS[j], math.exp(sum(math.log(x) for x in v[j:j + 5]) / 5.0)) for j in range(len(KS) - 4)]
        b8 = min(f for f in fen if f[1] <= 4); b10 = min(fen)
        if ref is None: ref = b8[2]
        print("  rang %2d (%d,%d) %s:%+d:%3d : %s | k<=8 : %.4f a k0=%+d val %.4f | k<=10 : %.4f a k0=%+d | suivis %d (%.0f s)" % (
            e["rang"], n1, n2, forme, dr, L, " ".join("%.3f" % (x / ref) for x in v), b8[0], b8[1], b8[2] / ref, b10[0], b10[1],
            sum(tr[str(k)]["suivi"] for k in KS), time.time() - t0), flush=True)
