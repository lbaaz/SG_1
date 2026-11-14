# -*- coding: ascii -*-
"""CONTRE-EPREUVE de verification_acte_chaine_EA_par_etat_machine2_v1.py : fabrique une COPIE MUTEE du lot de l'acte (quinze chiffres ou mots
de l'acte changes d'une unite, vises sur quinze controles) ; le verificateur, lance avec LOT_ALT=<cette copie> et SUFFIXE_SORTIE=_sur_acte_mute,
doit mordre sur C01, C02 (l'acte n'est plus au canon) et sur chaque controle vise. Le lot recu n'est que lu.
Usage depuis BOCAL4 : python -P acte_chaine_contreseing/mutation_acte_chaine_contre_epreuve_machine2_v1.py"""
import os
import zipfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'lot_machine1_2026-11-14_acte_chaine_EA_par_etat_v1_recu.zip')
DST = os.path.join(ROOT, 'mute_acte_chaine_contre_epreuve.zip')
MUTS = [('0.621    1.161', '0.631    1.161', 'C11'),                                   # nn.4, q min de J1
        ('J5  sous dix planchers 6', 'J5  sous dix planchers 5', 'C12'),              # nn.4, exclusion de J5
        ('(q de 0.395 a 0.470)', '(q de 0.395 a 0.480)', 'C13'),                      # nn.5, J5
        ('7.3e-14 en absolu sur la cible', '7.4e-14 en absolu sur la cible', 'C14'),  # nn.6 (d)
        ('0.0407', '0.0417', 'C15'),                                                  # nn.7, c_max de J3
        ('FAUSSE (0.950)', 'FAUSSE (0.951)', 'C16'),                                  # nn.8, A-4
        ('13 chez machine 2', '12 chez machine 2', 'C17'),                            # nn.9, D-CH-8
        ('T1, 0.4977, a 0.5', 'T1, 0.4987, a 0.5', 'C18'),                            # nn.9, R-4
        ('fe10bfe, plafond 94', 'fe10bff, plafond 94', 'C20'),                        # nn.0, le registre
        ('a 10:37:31 ;', 'a 10:37:32 ;', 'C08'),                                      # nn.2, le run
        ('5d80bf2edd26a6c1', '5d80bf2edd26a6c2', 'C04'),                              # nn.1, un canon
        ('le selftest de la feuille 15', 'le selftest de la feuille 16', 'C09'),      # nn.2, le banc
        ('ecart relatif NUL', 'ecart relatif NEGLIGEABLE', 'C10'),                    # nn.3, G-4
        ('0.499 a 1.642', '0.499 a 1.652', 'C19'),                                    # nn.10
        ('Sept sur huit.', 'Six sur huit.', 'C16')]                                   # nn.8
z = zipfile.ZipFile(SRC)
nom = 'journal_delta_nn_chaine_EA_par_etat_v1.md'
a = z.read(nom).decode('utf-8')
for x, y, c in MUTS:
    assert a.count(x) >= 1, (x, a.count(x))
    a = a.replace(x, y, 1)
with zipfile.ZipFile(DST, 'w') as zo:
    for n in z.namelist():
        zo.writestr(n, a.encode('utf-8') if n == nom else z.read(n))
print('copie mutee ecrite : %s (%d mutations, visant %s)' % (DST, len(MUTS), sorted(set(c for *_, c in MUTS))))
