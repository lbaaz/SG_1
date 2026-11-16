# -*- coding: ascii -*-
"""MARGES DE LA REGLE D'ANCRAGE (gel bis 3.7 : l'etat de plus grand recouvrement hermitien avec la graine), aux six points f070 de M17,
(F1, G20, k = 3) : les TROIS etats de plus grand recouvrement, leur energie, leur recouvrement et leur largeur 2 eta <W>. HORS CHAINE.
Configuration DEJA JOUEE par la nuit bis et par M17 ; aucun absorbeur long, aucun point neuf. Pourquoi : la validation montre que le
meilleur recouvrement ne bat le deuxieme que de 0.3 % a 3 % a plusieurs points ; reste a savoir si les deux ont des largeurs voisines.
Usage : python -P lecteur_creux_m2/ancrage_marges_machine2_v1.py <moteur> <sonde_etage2.json>"""
import json
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import lecteur_2D_creux_machine2_v1 as LC

M = LC.charger_moteur(sys.argv[1])
D = json.load(open(sys.argv[2]))['points']
print('(F1, G20, k = 3) aux six points : les trois etats de plus grand recouvrement avec la graine')
print('point      rang  E_re        recouvrement  gamma (2 eta <W>)   gamma / gamma du premier')
for nom in ('39_20', '197_100', '99_50', '101_50', '203_100', '41_20'):
    d = D[nom]
    idr = d['cfg']['F1G20']['traj']['3']['identite_reprise']
    w2 = Fraction(idr['w2'])
    N, r_c, g, s = idr['N'], idr['r_c'], idr['g'], idr['s']
    H0 = LC.assembler_H0(M, N, w2, g, idr['signe'])
    psi = M.graine_coherente(N, s, w2)
    W = LC.poids_absorbeur('F1', N, r_c)
    eta3 = d['eta0'] * 2.0 ** (-3)
    H = (H0 + LC.sp.diags(-1j * eta3 * W)).tocsc()
    sigma = float(np.real(np.vdot(psi, H0 @ psi)))
    vals, vecs = LC.voisins(H, sigma, LC.K_ANCRE)
    rec = np.abs(vecs.conj().T @ psi) ** 2
    o = np.lexsort((vals.real, -rec))
    g0 = None
    for rang in range(3):
        i = int(o[rang])
        p = np.abs(vecs[:, i]) ** 2
        gam = 2.0 * eta3 * float(np.sum(W * p) / np.sum(p))
        g0 = gam if g0 is None else g0
        print('%-9s  %d    %9.5f   %.5f      %.4e        %.3f' % (nom, rang + 1, vals[i].real, rec[i], gam, gam / g0))
