# -*- coding: ascii -*-
"""EQUIVALENCE DES HAMILTONIENS aux deux signes de delta (preserve l'aveugle de machine 1 : on compare des MATRICES, jamais un niveau, une densite ni une part).
La sonde de machine 1 assemble H avec la fonction assembler(W2, g, N, signe=-1) du bloc "LECTEUR CREUX" depose (sonde_lecteur_gel_loi_machine1_v1.py, canon d5cc48f48e37af99) ; ma boite
(boite_creuse de grandes_boites_machine2_v1.py, ecrite du texte de la note de machine 1) est la mienne : diagonale -a + w2 b ; sauts (k, l) du demi-plan, |k|+|l| <= 5, k+l impair, V = (g/5) X_saut_reel.
On compare les deux matrices, entree par entree, a w2 = 101/50 (delta > 0, le point sacrifie : controle de la methode) puis a w2 = 197/100 (delta < 0, un w2 qui n'est PAS candidat ; m1 y a fait son essai a l'aveugle),
pour N = 40 et g = 5.0e-3 (une valeur quelconque, qui n'est celle d'aucune cellule). Aucune 2D du systeme a fantome n'est calculee.
Usage : py -3.11 -P equivalence_hamiltonien_machine2_v1.py <registre>"""
import importlib.util
import sys
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp

executer = exec
REG = sys.argv[1].rstrip('/\\')
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
src = open(REG + "/scripts/sonde_lecteur_gel_loi_machine1_v1.py", encoding="ascii").read()
i0 = src.index("# --- LECTEUR CREUX"); i1 = src.index("# --- fin du bloc ---", i0)
import math, json, time
import scipy.sparse.linalg as sl
ns = {"M": M, "np": np, "sp": sp, "sl": sl, "math": math, "json": json, "time": time, "F": F, "Fraction": F}
executer(compile(src[i0:i1], "bloc_lecteur_depose", "exec"), ns)
P5 = 5
SAUTS = sorted((k, l) for k in range(-P5, P5 + 1) for l in range(-P5, P5 + 1) if abs(k) + abs(l) <= P5 and (k + l) % 2 == P5 % 2 and (k, l) > (0, 0))


def ma_boite(N, W2, g):
    W2F = float(W2)
    li, co, va = [], [], []
    di = np.array([-(i // N) + W2F * (i % N) for i in range(N * N)])
    for a in range(N):
        for b in range(N):
            i = a * N + b
            for (k, l) in SAUTS:
                a2, b2 = a + k, b + l
                if 0 <= a2 < N and 0 <= b2 < N:
                    V = (g / P5) * M.X_saut_reel(P5, k, l, float(a), float(b), W2)
                    if V:
                        j = a2 * N + b2; li += [i, j]; co += [j, i]; va += [V, V]
    return (sp.csr_matrix((va, (li, co)), shape=(N * N, N * N)) + sp.diags(di)).tocsc()


N, g = 40, 5.0e-3
for W2 in (F(101, 50), F(197, 100)):
    H0, dg = ns["assembler"](W2, g, N, signe=-1)
    H_lui = (H0.tocsc() + sp.diags(dg)).tocsc()
    H_moi = ma_boite(N, W2, g)
    D = (H_lui - H_moi).tocoo()
    ecart = float(np.max(np.abs(D.data))) if D.nnz else 0.0
    print('w2 = %s (delta = %+.3f) : N = %d, entrees non nulles %d (lui) / %d (moi), plus grand |H(lui) - H(moi)| = %.3e, plus grande entree %.3e' % (
        W2, float(W2) - 2.0, N, H_lui.nnz, H_moi.nnz, ecart, float(np.max(np.abs(H_moi.data)))))
    print('    symetrie : lui %.2e, moi %.2e ; diagonale (0,0) %.3e / %.3e ; diagonale (0,N-1) %.6f / %.6f' % (
        float(abs(H_lui - H_lui.T).max()), float(abs(H_moi - H_moi.T).max()), H_lui[0, 0], H_moi[0, 0], H_lui[N - 1, N - 1], H_moi[N - 1, N - 1]))
