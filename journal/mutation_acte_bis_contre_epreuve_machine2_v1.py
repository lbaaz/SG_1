# -*- coding: ascii -*-
"""CONTRE-EPREUVE de verification_acte_nn_qualification_EB_bis_machine2_v1.py : fabrique une COPIE MUTEE du lot de l'acte
(sept chiffres de l'acte changes d'une unite, un par controle vise) ; le verificateur, lance avec LOT_ALT=<cette copie>, doit
mordre. Rien n'est edite : le lot recu n'est que lu. Usage depuis BOCAL4 : python -P mutation_acte_bis_contre_epreuve_machine2_v1.py"""
import os
import zipfile
ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, 'lot_machine1_2026-11-13_acte_qualification_EB_bis_v1_recu.zip')
DST = os.path.join(ICI, 'mute_acte_bis_contre_epreuve.zip')
MUTS = [('1.95  2.162e-10  PL 0.0454  0', '1.95  2.162e-10  PL 0.0455  0'),            # tableau nn.6, un etalement
        ('au moins 493 fois', 'au moins 494 fois'),                                      # nn.13
        ('vingt-huit candidates', 'vingt-sept candidates'),                              # nn.12, la revue (X)
        ('vrai sur UN point (1.95, k0 = 0)', 'vrai sur UN point (1.95, k0 = 1)'),        # nn.8, A-7
        ('sauf 27 flottants', 'sauf 26 flottants'),                                      # nn.9, la feuille rejouee
        ('pire ecart relatif a BOCAL4 4.948e-04', 'pire ecart relatif a BOCAL4 4.958e-04'),   # nn.9, le scelle ouvert
        ('3.6e-03 au plus', '3.7e-03 au plus')]                                          # nn.10, O-BIS-2
z = zipfile.ZipFile(SRC)
a = z.read('journal_delta_nn_qualification_EB_bis_v1.md').decode('utf-8')
for x, y in MUTS:
    assert a.count(x) == 1, (x, a.count(x))
    a = a.replace(x, y)
with zipfile.ZipFile(DST, 'w') as zo:
    for n in z.namelist():
        zo.writestr(n, a.encode('utf-8') if n == 'journal_delta_nn_qualification_EB_bis_v1.md' else z.read(n))
print('copie mutee ecrite : %s (%d mutations)' % (DST, len(MUTS)))
