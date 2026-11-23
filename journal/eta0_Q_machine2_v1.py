# -*- coding: ascii -*-
"""LES eta0 DES CINQ POINTS DE LA QUALIFICATION "Q" de machine 1 (22g), recalcules par moi AVANT toute lecture a deux dimensions a ces points.
Regle en absolu de sa note, section 8.2 : eta0 = g X(w2) / (P kappa_3), kappa_3 = 0.0262, P = 5, X(w2) = X_saut_reel(P, 2, 1, 0, 0, w2) du moteur depose (82a0be882568fe0c) ; ecrit a six chiffres.
Je compare aux valeurs de sa section 8.1. Je ne lis rien d'autre : c'est de l'arithmetique a une dimension, aucun etat.
Usage : py -3.11 -P eta0_Q_machine2_v1.py <moteur m17_chaine_v17.py>"""
import hashlib
import importlib.util
import sys
import unicodedata
from fractions import Fraction as F

MOTEUR = sys.argv[1]
t = unicodedata.normalize('NFC', open(MOTEUR, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
assert hashlib.sha256(t.encode('utf-8')).hexdigest()[:16] == '82a0be882568fe0c', 'canon du moteur'
spec = importlib.util.spec_from_file_location('moteur', MOTEUR)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
P, KAPPA3 = 5, 0.0262
POINTS = [('Q-a', F(2), '2.5e-04', 9.73875e-04), ('Q-c', F(2), '1e-03', 3.89550e-03), ('Q-d', F(2), '2e-03', 7.79100e-03),
          ('Q-e', F(20001, 10000), '3e-04', 1.16821e-03), ('Q-f', F(20001, 10000), '1.5e-04', 5.84106e-04)]
print('P = %d ; kappa_3 = %s ; tau_0 = X(2)/P = %.9f (sa forme close : 0.102062073)' % (P, KAPPA3, M.X_saut_reel(P, 2, 1, 0, 0, F(2)) / P))
pire = 0.0
for nom, w2, gs, ref in POINTS:
    g = float(gs)
    X = M.X_saut_reel(P, 2, 1, 0, 0, w2)
    eta0 = g * X / (P * KAPPA3)
    e6 = float('%.5e' % eta0)
    rel = abs(e6 - ref) / ref
    pire = max(pire, rel)
    print('%-4s w2 = %-9s g = %-8s X = %.9f  eta0 = %.5e  (sa valeur %.5e, ecart relatif %.1e)  eta0/g = %.5f  |w2-2| = %.1e' % (nom, w2, gs, X, e6, ref, rel, e6 / g, abs(float(w2) - 2.0)))
print('plus grand ecart relatif entre mes eta0 (six chiffres) et les siens : %.1e' % pire)
