# -*- coding: ascii -*-
"""TEMPS d'une factorisation creuse complexe d'une boite 2D sous absorbeur (gel "pont", section 8 : densite 2D sous absorbeur hors du vide), AU POINT SACRIFIE w2 = 101/50 (jamais a un w2 candidat).
Boite N x N, H reel (moteur, g de la note de m1) + absorbeur quadratique -i eta (max(a, b) - r_c)^2 pour max(a, b) > r_c, r_c = 2 (m_bord + max(8, m_bord)) + 2 ; on mesure : construction de H,
factorisation LU creuse de (E - H) a une energie proche du vide (E = E_v - x delta, x = 8), une resolution. Rien n'est juge : c'est un cout. Machine 2.
Usage : py -3.11 -P temps_factorisation_absorbeur_machine2_v1.py <registre clone> <barreaux 3|4|5> <cote> [cote ...]"""
import importlib.util
import math
import sys
import time
from fractions import Fraction as F
import numpy as np
import mpmath as mp
import scipy.sparse as sp
from scipy.sparse.linalg import splu

REG, NB = sys.argv[1].rstrip('/\\'), int(sys.argv[2]); COTES = [int(x) for x in sys.argv[3:]]
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
W2 = F(101, 50); W2F = float(W2); P5 = 5; DELTA = W2F - 2.0
G = {3: 5.53067e-03, 4: 4.22189e-03, 5: 3.35640e-03}[NB]; MBORD = NB; RC = 2 * (MBORD + max(8, MBORD)) + 2
SAUTS = sorted((k, l) for k in range(-P5, P5 + 1) for l in range(-P5, P5 + 1) if abs(k) + abs(l) <= P5 and (k + l) % 2 == P5 % 2 and (k, l) > (0, 0))
print('barreaux %d ; r_c = %d ; point sacrifie w2 = 101/50 ; E = E_v - 8 delta (E_v pris egal a 0 : c est un cout)' % (NB, RC))
print('cote   dimension   construction H (s)   factorisation LU (s)   resolution (s)   remplissage (Mo de facteurs)')
for N in COTES:
    t0 = time.time(); li, co, va = [], [], []
    for a in range(N):
        for b in range(N):
            i = a * N + b
            for (k, l) in SAUTS:
                a2, b2 = a + k, b + l
                if 0 <= a2 < N and 0 <= b2 < N:
                    V = (G / P5) * M.X_saut_reel(P5, k, l, float(a), float(b), W2)
                    if V:
                        j = a2 * N + b2; li += [i, j]; co += [j, i]; va += [V, V]
    di = np.array([-(i // N) + W2F * (i % N) for i in range(N * N)], dtype=complex)
    eta = 1e-3
    for i in range(N * N):
        r = max(i // N, i % N)
        if r > RC:
            di[i] += -1j * eta * (r - RC) ** 2
    H = (sp.csr_matrix((va, (li, co)), shape=(N * N, N * N), dtype=complex) + sp.diags(di)).tocsc(); t1 = time.time()
    E = -(-8.0 * DELTA)
    A = (E * sp.identity(N * N, dtype=complex, format='csc') - H).tocsc(); t2 = time.time()
    lu = splu(A); t3 = time.time(); b = np.zeros(N * N, dtype=complex); b[0] = 1.0; x = lu.solve(b); t4 = time.time()
    remp = (lu.L.nnz + lu.U.nnz) * 16 / 1e6
    print('%-6d %-11d %-20.1f %-22.1f %-16.2f %.0f' % (N, N * N, t1 - t0, t3 - t2, t4 - t3, remp), flush=True)
