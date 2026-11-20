# -*- coding: ascii -*-
"""Synthese de la matrice de mutations des FEUILLES de machine 1 (differentiel_feuilles_machine2_v1/v3/v4.py) : pour chaque alteration, le nombre de desaccords avec mes feuilles, au premier passage
(generateur v1, scenarios 1 a 6), au passage final (generateur v3, scenarios 1 a 14) et, pour les deux alterations de (S) que le passage final ne mord pas, au passage complementaire (generateur v4,
scenarios 101 a 112, sommes posees aux bords des bandes). Une alteration est MORDUE si le passage final OU le passage complementaire voit au moins un desaccord. Machine 2, 2026-11-17.
Usage : py -3.11 -P synthese_mutations_feuilles_machine2_v1.py <dossier journaux>"""
import os
import re
import sys

J = sys.argv[1]
MUT = ['plateau_105_en_110', 'etendue_002_en_003', 'etendue_inf_strict', 'mediane_en_moyenne', 'w0_sans_mediane', 'part_non_fiable_10', 'compte_sans_couverte', 'S_largeur_8', 'participation_inverse',
       'L_tol_006', 'L_min_ecarts_9', 'L2_x_4', 'L2_large', 'S_cellule_080', 'S_groupe_075', 'C_reduit_bas_030', 'C_rapport_haut_200', 'min_boites_7', 'famille_sans_creneau', 'famille_trois_cellules', 'groupe_UN_179']
FEUILLE = {'plateau': 'densite', 'etendue': 'densite', 'mediane': 'densite', 'w0': 'densite', 'part': 'boites', 'compte': 'boites', 'S_largeur': 'boites', 'participation': 'boites'}


def lit(d, nom):
    f = os.path.join(J, d, 'mutation_%s_machine2_v1.log' % nom)
    if not os.path.isfile(f):
        return None
    m = re.search(r'BILAN \(mutation [^)]*\) : (\d+) graines, (\d+) desaccords', open(f).read())
    return (int(m.group(1)), int(m.group(2))) if m else None


mordues = 0
print('alteration                 premier passage (generateur v1)    passage final (generateur v3)     passage complementaire (v4)')
for n in MUT:
    a, b, c = lit('mutations', n), lit('mutations_v3', n), lit('mutations_v4', n)
    sa = '%d graines : %d desaccords' % a if a else '-'
    sb = '%d graines : %d desaccords' % b if b else '-'
    sc = '%d graines : %d desaccords' % c if c else '-'
    verdict = 'MORDUE' if ((b and b[1] > 0) or (c and c[1] > 0)) else 'NON MORDUE'
    mordues += verdict == 'MORDUE'
    print('%-26s %-34s %-34s %-34s %s' % (n, sa, sb, sc, verdict))
print('alterations mordues (passage final ou complementaire) : %d sur %d' % (mordues, len(MUT)))
