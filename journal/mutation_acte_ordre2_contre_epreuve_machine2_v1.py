# -*- coding: ascii -*-
"""CONTRE-EPREUVE de verification_acte_ordre2_machine2_v1.py : fabrique une COPIE MUTEE du lot de l'acte (chiffres ou mots de l'acte changes d'une unite, vises sur treize
controles) ; le verificateur, lance avec LOT_ALT=<cette copie> et SUFFIXE_SORTIE=_sur_acte_mute, doit mordre sur C01, C02 (l'acte n'est plus au canon) et sur chaque controle
vise. Le lot recu n'est que lu.
Usage depuis BOCAL4 : python -P acte_ordre2_contreseing/mutation_acte_ordre2_contre_epreuve_machine2_v1.py"""
import os
import re
import zipfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'lot_machine1_2026-11-15_acte_ordre2_chaine_EA_v1_recu.zip')
DST = os.path.join(ROOT, 'mute_acte_ordre2_contre_epreuve.zip')
MUTS = [('C1    0.444   0.600   0.676', 'C1    0.444   0.600   0.677', 'C06'),                          # nn.4, q1 max de C1
        ('C2  97/50    3/4   -0.06  proche     1.25    11     1.044  1.099  1.136', 'C2  97/50    3/4   -0.06  proche     1.25    11     1.044  1.099  1.137', 'C06'),   # nn.4, q2 max de C2
        ('168 etats, 132 juges, 36 exclus', '168 etats, 133 juges, 36 exclus', 'C06'),                              # nn.4
        ('4195583a970eaf70\n        la feuille rejouee', '4195583a970eaf71\n        la feuille rejouee', 'C05'),   # nn.1, un canon
        ('le run\n  en a pris 3177 et 1346.', 'le run\n  en a pris 3187 et 1346.', 'C08'),                # nn.2, duree des quinze
        ('batterie a 100 pour cent au\n  lancement, a 62', 'batterie a 100 pour cent au\n  lancement, a 63', 'C08'),
        ('a 8e-11 pres pour Gamma_flux', 'a 9e-11 pres pour Gamma_flux', 'C09'),                       # nn.3, G-8
        ('1.136 pour une borne de\n  1.25', '1.137 pour une borne de\n  1.25', 'C10'),                  # nn.5
        ('L2 (0.273 pour l\'ordre 2 contre 0.300)', 'L2 (0.274 pour l\'ordre 2 contre 0.300)', 'C10'),    # nn.6
        ('(7.50e-05, 1.84e-05, 4.59e-06 a', '(7.50e-05, 1.84e-05, 4.60e-06 a', 'C11'),                 # nn.6, energie exacte
        ('4.37e-02, "u seul"', '4.38e-02, "u seul"', 'C11'),
        ('sept sont\n  au-dela de 1.6, deux au-dela de 2', 'huit sont\n  au-dela de 1.6, deux au-dela de 2', 'C12'),   # nn.7, W1
        ('(5.12e-13) ; a partir de huit fois (5.86e-13)', '(5.12e-13) ; a partir de huit fois (5.96e-13)', 'C12'),      # nn.7, bruit
        ('A-11 (0.60) la mediane de q2 / loi est entre 0.93 et 1.15  FAUSSE (L2 : 0.889)', 'A-11 (0.60) la mediane de q2 / loi est entre 0.93 et 1.15  VRAIE (L2 : 0.889)', 'C13'),   # nn.8
        ('est 15.2 pour 18 vraies', 'est 15.3 pour 18 vraies', 'C13'),
        ('22 des 115\n    alterations', '21 des 115\n    alterations', 'C14'),                             # nn.9, D-O2-2
        ('(131 alterations sur 131)', '(130 alterations sur 131)', 'C14'),
        ('trente-quatre attendent', 'trente-trois attendent', 'C14'),                                   # nn.12
        ('machine 1 -- le gel et ses instruments\n  3bc363266957de56', 'machine 1 -- le gel et ses instruments\n  3bc363266957de57', 'C15')]    # nn.13, un canon
z = zipfile.ZipFile(SRC)
nom = 'journal_delta_nn_ordre2_chaine_EA_v1.md'
a = z.read(nom).decode('utf-8')
echecs = []
for x, y, c in MUTS:                                          # les blancs (et les fins de ligne) de la cible sont libres
    pat = r'\s+'.join(re.escape(w) for w in x.split())
    a, n = re.subn(pat, lambda _m, y=y: y, a, count=1)
    if n != 1:
        echecs.append(x)
assert not echecs, echecs
with zipfile.ZipFile(DST, 'w') as zo:
    for n in z.namelist():
        zo.writestr(n, a.encode('utf-8') if n == nom else z.read(n))
print('copie mutee ecrite : %s (%d mutations, visant %s)' % (DST, len(MUTS), sorted(set(c for *_, c in MUTS))))
