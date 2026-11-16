# -*- coding: ascii -*-
"""Essai de reglage : la forme F1 a plus de 80 couches, sur une echelle prolongee, a des etats de points de reglage.
Usage : python3 -I essai_forme_longue_machine1_v1.py <moteur.py> <bloc.py> <sonde.json> <id> <n1_n2> [<n1_n2> ...] -- <L> [<L> ...]"""
import sys, json, math, time, importlib.util
from fractions import Fraction as F
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sl
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(sys.argv[2]).read(), sys.argv[2], "exec"))
i = sys.argv.index("--"); pid = sys.argv[4]; sites = sys.argv[5:i]; Ls = [int(x) for x in sys.argv[i + 1:]]
p = [q for q in json.load(open(sys.argv[3]))["points"] if q["id"] == pid][0]
num, den = p["w2"].split("/"); w2 = F(int(num), int(den)); r_c = p["r_c"]; eta0 = p["eta0"]
KS = list(range(-3, 12)); t0 = time.time()
H0m, dm = assembler(w2, p["g"], r_c + max(Ls))
for s in sites:
    n1, n2 = [int(x) for x in s.split("_")]
    e = [x for x in p["etats"] if int(x["n1"]) == n1 and int(x["n2"]) == n2][0]
    for L in Ls:
        N = r_c + L; H0, dg = restreindre(H0m, dm, r_c + max(Ls), N)
        tr = trajectoire(H0, dg, table_W(N, "F1", r_c, L), eta0, N, (n1, n2), e["E_re"], KS)
        v = [tr[str(k)]["gamma"] for k in KS]; ref = v[KS.index(7)]
        fen = [(max(v[j:j + 5]) / min(v[j:j + 5]) - 1.0, KS[j]) for j in range(len(KS) - 4)]
        print("%s (%d,%d) F1 L=%d N=%d : %s | meilleure fenetre %.4f a k0=%+d ; sur k=-3..8 : %.4f ; sur k=-3..10 : %.4f  (%.0f s)" % (
            pid, n1, n2, L, N, " ".join("%.4f" % (x / ref) for x in v), min(fen)[0], min(fen)[1],
            min(f for f in fen if f[1] <= 4)[0], min(f for f in fen if f[1] <= 6)[0], time.time() - t0), flush=True)
