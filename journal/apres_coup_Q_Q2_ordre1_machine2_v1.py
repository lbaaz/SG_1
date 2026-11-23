# -*- coding: ascii -*-
"""APRES COUP, HORS REGLE, SANS VALEUR D'EPREUVE : le plateau du lecteur (absorbeur A, feuille deposee 83701094e6a2b965) aux NEUF points lus (Q : cinq ; Q2 : quatre), compare a MA chaine du premier ordre (chaine_premier_ordre_machine2_v1 : echelle de x^5 au canal (2, 1), absorbeur lisse, largeur lue comme le pole)
ET a la colonne G3* de machine 1 (chaine d'ordre 3, dix-huit variantes). Question : a quelle chaine le lecteur est-il le plus proche, aux quatre points de barriere et aux cinq autres ? Je rapporte les trois logarithmes, sans juger ; l'etendue de la chaine de machine 1 (0.0024 a 0.0033 a Q2, 0.0016 a 0.0032 a Q) est a comparer.
Aucun nouveau calcul 2D : les plateaux sont relus dans les JSON de Q et de Q2 par la meme feuille.
Usage : py -3.11 -P apres_coup_Q_Q2_ordre1_machine2_v1.py <Q_sorties> <Q2_sorties> <feuille deposee>"""
import importlib.util
import json
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chaine_premier_ordre_machine2_v1 as C  # noqa: E402

DQ, DQ2, FEUILLE = sys.argv[1], sys.argv[2], sys.argv[3]
spec = importlib.util.spec_from_file_location('feuille', FEUILLE)
FE = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FE)
# (dossier, id, nom, w2, g, G3*, etendue de sa chaine)
PTS = [(DQ, 'Qa', 'Q-a', F(2), 2.5e-4, 1.36076e-05, 0.0030), (DQ, 'Qc', 'Q-c', F(2), 1e-3, 5.44311e-05, 0.0016), (DQ, 'Qd', 'Q-d', F(2), 2e-3, 1.08861e-04, 0.0028),
       (DQ, 'Qe', 'Q-e', F(20001, 10000), 3e-4, 1.20924e-05, 0.0026), (DQ, 'Qf', 'Q-f', F(20001, 10000), 1.5e-4, 2.91470e-06, 0.0032),
       (DQ2, 'Q2a', 'Q2-a', F(20001, 10000), 6e-5, 4.94622e-08, 0.0026), (DQ2, 'Q2b', 'Q2-b', F(20001, 10000), 4e-5, 2.05449e-09, 0.0024),
       (DQ2, 'Q2c', 'Q2-c', F(19999, 10000), 3e-4, 1.21071e-05, 0.0030), (DQ2, 'Q2d', 'Q2-d', F(19999, 10000), 1.5e-4, 2.92086e-06, 0.0033)]
print('%-5s %-12s %-8s %-12s %-12s %-12s | %-11s %-11s %-11s | etendue de sa chaine' % ('pt', 'w2', 'g', 'lecteur', 'mon 1er ordre', 'sa G3*', 'ln(L/1er)', 'ln(L/G3*)', 'ln(G3*/1er)'))
for dos, ident, nom, w2, g, g3, ete in PTS:
    t = json.load(open(os.path.join(dos, 'lect2D_%s_fantome.json' % ident)))['lecture']['traj']
    gl = FE.juger_etat({x: t[x] for x in 'ABCD'}, None)['plateaux']['A']['Gamma_pl']
    tau = C.echelle(float(w2), 2, 1, 200)
    g1 = C.largeur(tau, (float(w2) - 2.0) / g)[0] * g
    print('%-5s %-12s %-8.3g %-12.5e %-12.5e %-12.5e | %-+11.5f %-+11.5f %-+11.5f | %.4f' % (nom, w2, g, gl, g1, g3, math.log(gl / g1), math.log(gl / g3), math.log(g3 / g1), ete))
print('\nLecture a faire par le lecteur du journal, pas ici : un ecart entre deux chaines plus petit que l etendue de la chaine de machine 1 ne dit rien de laquelle des deux est la plus proche du modele ; ce tableau ne separe pas les ordres.')
