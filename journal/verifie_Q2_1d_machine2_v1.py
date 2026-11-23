# -*- coding: ascii -*-
"""VERIFICATION A UNE DIMENSION (aucun etat, aucune lecture 2D) de la section 3 de la note de machine 1 (22h, lot 074b131287ad2b6f) : les quatre points "Q2".
(1) ses eta0 = max(|w2 - 2|, g X(w2) / (P kappa_3)), P = 5, kappa_3 = 0.0262, X = X_saut_reel(5, 2, 1, 0, 0, w2) du moteur depose, ecrits a six chiffres ;
(2) la PROFONDEUR de barriere (m = 1, 2, 0, 0) et r_c = 2 (m + max(8, m)) + 2 (20, 22, 18, 18) par MES seuils de premier ordre 2 tau_m / m, comparee a |d| / g ;
(3) un recoupement de sa colonne G3* par MA chaine du premier ordre (largeur lue comme le pole, absorbeur lisse) : |ln(G3* / G1er)| a comparer a ce qu'elle annonce (|ln(G3 / G1)| de 0.0043 au plus sur sa grille) ; et le rapport de signe ln[G(1.9999) / G(2.0001)] au premier ordre,
a comparer a ses +0.00121 et +0.00211 (qui sont des rapports de G3*).
Je ne lis aucune sortie 2D de Q2 (il n'y en a pas). Usage : py -3.11 -P verifie_Q2_1d_machine2_v1.py <moteur m17_chaine_v17.py>"""
import hashlib
import importlib.util
import math
import os
import sys
import unicodedata
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chaine_premier_ordre_machine2_v1 as C  # noqa: E402

MOTEUR = sys.argv[1]
t = unicodedata.normalize('NFC', open(MOTEUR, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
assert hashlib.sha256(t.encode('utf-8')).hexdigest()[:16] == '82a0be882568fe0c', 'canon du moteur'
spec = importlib.util.spec_from_file_location('moteur', MOTEUR)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
P, K3 = 5, 0.0262
# (id, w2, g, m (sa colonne), r_c (sa colonne), eta0 (sa colonne), G3* (sa colonne), point de Q correspondant pour le signe)
PTS = [('Q2-a', F(20001, 10000), 6e-5, 1, 20, 2.33642e-04, 4.94622e-08), ('Q2-b', F(20001, 10000), 4e-5, 2, 22, 1.55762e-04, 2.05449e-09),
       ('Q2-c', F(19999, 10000), 3e-4, 0, 18, 1.16909e-03, 1.21071e-05), ('Q2-d', F(19999, 10000), 1.5e-4, 0, 18, 5.84544e-04, 2.92086e-06)]
print('(1) eta0 et (2) profondeur de barriere, r_c')
pire = 0.0
for nom, w2, g, m_s, rc_s, eta_s, g3 in PTS:
    X = M.X_saut_reel(P, 2, 1, 0, 0, w2)
    eta = max(abs(float(w2) - 2.0), g * X / (P * K3))
    e6 = float('%.5e' % eta)
    rel = abs(e6 - eta_s) / eta_s
    pire = max(pire, rel)
    tau = C.echelle(float(w2), 2, 1, 60)
    d = abs(float(w2) - 2.0) / g
    prof = C.rungs(tau, d)
    rc = 2 * (prof + max(8, prof)) + 2
    print('%-5s w2 = %-9s g = %-7.3g |d|/g = %.3f  seuils 1er ordre des sites 1..3 : %s  -> profondeur %d (sa colonne : %d) ; r_c = %d (sa colonne : %d) ; eta0 = %.5e (sa colonne %.5e, ecart relatif %.1e)'
          % (nom, w2, g, d, ' '.join('%.4f' % s for s in C.seuils(tau, 3)), prof, m_s, rc, rc_s, e6, eta_s, rel))
print('plus grand ecart relatif sur eta0 : %.1e' % pire)
print('\n(3) recoupement de sa colonne G3* par ma chaine du premier ordre (absorbeur lisse, pole)')
G1 = {}
for nom, w2, g, m_s, rc_s, eta_s, g3 in PTS:
    tau = C.echelle(float(w2), 2, 1, 200)
    delta = float(w2) - 2.0                       # desaccord du canal (2, 1) : -2 + w2
    gam = C.largeur(tau, delta / g)[0] * g
    G1[nom] = gam
    print('%-5s Gamma_1er = %.5e ; sa G3* = %.5e ; ln(G3* / G1er) = %+.5f' % (nom, gam, g3, math.log(g3 / gam)))
print('\nrapports de signe au premier ordre (ma chaine) : ln[G(Q2-c) / G(Q-e)] et ln[G(Q2-d) / G(Q-f)] ; je calcule G(Q-e), G(Q-f) au meme premier ordre')
for nom, wp, g, cmp_ in (('Q2-c', F(20001, 10000), 3e-4, 'Q-e'), ('Q2-d', F(20001, 10000), 1.5e-4, 'Q-f')):
    tau = C.echelle(float(wp), 2, 1, 200)
    gp = C.largeur(tau, (float(wp) - 2.0) / g)[0] * g
    print('%-5s ln[G1er(%s) / G1er(%s, w2 = 2.0001)] = %+.5f   (ses rapports de G3* : +0.00121 pour Q2-c, +0.00211 pour Q2-d)' % (nom, nom, cmp_, math.log(G1[nom] / gp)))
print('\nCe que ce script ne dit pas : rien d un etat 2D, rien de la feuille deposee, rien de sa chaine d ordre 3 elle-meme (je n en ai que le premier ordre).')
