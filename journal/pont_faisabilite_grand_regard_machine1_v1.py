# -*- coding: ascii -*-
"""Regard de faisabilite : remplissage et duree de la factorisation creuse selon le cote, pour savoir si les cotes 300 et 400
tiennent dans ce conteneur. Et reference a deux amplitudes (parts exponentielles) pour le rapport R. machine 1, 2026-11-16.
Usage : python3 -I -B pont_faisabilite_grand_regard_machine1_v1.py <moteur> <sonde deposee du lecteur> <w2> <g> <cote> ..."""
import sys, math, time, random, importlib.util, resource
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl
MOTEUR, S_LECT, W2S, GS = sys.argv[1:5]; COTES = [int(x) for x in sys.argv[5:]]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
src = open(S_LECT, encoding="utf-8").read(); exec(compile(src[src.index("# --- LECTEUR CREUX"):src.index("# --- fin du bloc ---")], "bloc_lecteur", "exec"))
w2 = F(W2S); g = float(GS); ad = abs(float(w2) - 2.0)
random.seed(1)
def ipr(ys): s = sum(ys); return sum((y / s) ** 2 for y in ys)
print("reference a deux amplitudes (parts exponentielles) : R = IPR / (3 / (n + 2)) et participation d'UNE boite")
for n in (2, 3, 4, 6, 9, 11, 14, 22, 29):
    v = [ipr([random.expovariate(1.0) for _ in range(n)]) for _ in range(20000)]; p = [1.0 / q for q in v]; mp = sum(p) / len(p)
    print("   n = %2d : R = %.2f   participation %.2f +- %.2f" % (n, (sum(v) / len(v)) / (3.0 / (n + 2)), mp, math.sqrt(sum((q - mp) ** 2 for q in p) / len(p))))
H0m, dm = assembler(w2, g, max(COTES), signe=-1)
for N in COTES:
    H0, d = restreindre(H0m, dm, max(COTES), N); H = (H0 + sp.diags(d)).tocsc(); t0 = time.time()
    lu = sl.splu(H - (-2.0 * ad) * sp.identity(H.shape[0], format="csc")); dt = time.time() - t0
    nz = lu.L.nnz + lu.U.nnz
    print("cote %3d : %6d etats, %8d coefficients dans H, %10d dans L + U (%.2f Go), factorisation %5.1f s, memoire maximale du processus %.2f Go" % (
        N, H.shape[0], H.nnz, nz, nz * 12.0 / 1e9, dt, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6), flush=True)
    del lu
