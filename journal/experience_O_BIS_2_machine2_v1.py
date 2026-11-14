# -*- coding: ascii -*-
"""EXPERIENCE HORS GEL, NON OPPOSABLE, machine 2, 2026-11-13 : cause de O-BIS-2 (acte nn bis) -- ma sonde et mon diagnostic
different de 3.6e-03 au plus (j = 6, G30, k = -2, N = 70) ; eta est IDENTIQUE (0.2) des deux cotes. La sonde pose la partie
hermitienne UNE fois puis la diagonale d0 + (-1j eta) w ; le diagnostic appelle H_2D(..., eta, r_c). Trois decompositions de
CE point, dans un meme processus : (A) la voie du diagnostic, (B) la voie de la sonde, (C) A de nouveau (determinisme).
Usage : python -P experience_O_BIS_2_machine2_v1.py > experience_O_BIS_2/experience_O_BIS_2.log"""
import hashlib, importlib.util, json, os, platform, time, unicodedata
from fractions import Fraction
import numpy as np
ICI = os.path.dirname(os.path.abspath(__file__))
os.chdir(ICI)
def cB(p):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n')
    return hashlib.sha256(t.encode()).hexdigest()[:16]
assert cB('m17_chaine_v17.py') == '82a0be882568fe0c'
spec = importlib.util.spec_from_file_location('m', 'm17_chaine_v17.py'); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
w2, g, r_c, N, k = Fraction(39, 20), 0.08408964152537146, 40, 70, -2
eta = 0.05 * 2.0 ** (-k)
print('plateforme : %s %s, python %s, numpy %s ; j = 6, G30, N = %d, k = %d, eta = %r' % (platform.system(), platform.machine(), platform.python_version(), np.__version__, N, k, eta), flush=True)
def absorbeur_F1(r_c, N):
    w = np.zeros(N * N)
    for a in range(N):
        for b in range(N):
            m = max(a, b)
            if m > r_c:
                w[a * N + b] = float((m - r_c) ** 2)
    return w
def lire(H, nom, t0):
    vals, vecs = np.linalg.eig(H)
    ov = np.abs(vecs[0, :]) ** 2 / np.sum(np.abs(vecs) ** 2, axis=0)
    i = int(np.argmax(ov))
    print('%s : gamma = %.12e  E_re = %.15e  recouvrement %.6f  (%.0f s)' % (nom, -2.0 * vals[i].imag, vals[i].real, ov[i], time.time() - t0), flush=True)
    return -2.0 * vals[i].imag
t0 = time.time(); HA = M.H_2D(N, w2, g, +1, 'x5', eta, r_c)[0]; gA = lire(HA, 'A voie du diagnostic (H_2D avec eta)', t0)
t0 = time.time(); H0 = M.H_2D(N, w2, g, +1, 'x5', 0.0, None)[0]; d0 = H0.diagonal().copy(); w = absorbeur_F1(r_c, N)
np.fill_diagonal(H0, d0 + (-1j * eta) * w); gB = lire(H0, 'B voie de la sonde (d0 + (-1j eta) w)', t0)
print('matrices : plus grand |HA - HB| = %.3e ; nombre d elements differents = %d ; |H|max = %.3e' % (np.abs(HA - H0).max(), int(np.count_nonzero(HA != H0)), np.abs(HA).max()), flush=True)
t0 = time.time(); gA2 = lire(HA, 'C voie A de nouveau, meme matrice', t0)
print('A - A2 = %.3e (determinisme) ; B/A - 1 = %.3e ; diagnostic de la nuit 5.378534999e-10, sonde de la nuit 5.398020792e-10' % (gA - gA2, gB / gA - 1), flush=True)
