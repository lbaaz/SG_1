# -*- coding: ascii -*-
"""Profil hors gel : temps et remplissage de la factorisation creuse de la boite fermee selon l'ordre des colonnes,
au point sacrifie w2 = 101/50, 3 barreaux. Usage : python3 -I -B ce_script <registre> <cote> [<cote> ...]"""
import sys, time, importlib.util
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl
REG = sys.argv[1].rstrip("/")
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
src = open(REG + "/scripts/sonde_lecteur_gel_loi_machine1_v1.py", encoding="ascii").read()
i0 = src.index("# --- LECTEUR CREUX"); i1 = src.index("# --- fin du bloc ---", i0); exec(compile(src[i0:i1], "bloc", "exec"))
for N in [int(c) for c in sys.argv[2:]]:
    t = time.time(); H0, dg = assembler(F(101, 50), 5.53067e-03, N, signe=-1); H = (H0 + sp.diags(dg)).tocsc(); n = N * N
    print("cote %d : assemblage %.1f s ; non nuls %d (%.1f par ligne)" % (N, time.time() - t, H.nnz, H.nnz / n), flush=True)
    A = (H - (-0.05) * sp.identity(n, format="csc")).tocsc(); b = np.cos(np.arange(1, n + 1, dtype=float))
    for ordre in ("COLAMD", "MMD_AT_PLUS_A"):
        for seuil in (1.0, 0.1):
            t = time.time(); lu = sl.splu(A, permc_spec=ordre, diag_pivot_thresh=seuil); tf = time.time() - t
            t = time.time(); x = lu.solve(b); ts = time.time() - t
            print("   %-14s seuil de pivot %.1f : factorisation %.1f s ; non nuls de L + U %.2e ; une resolution %.3f s ; residu %.1e"
                  % (ordre, seuil, tf, lu.L.nnz + lu.U.nnz, ts, np.linalg.norm(A @ x - b) / np.linalg.norm(b)), flush=True)
            del lu
