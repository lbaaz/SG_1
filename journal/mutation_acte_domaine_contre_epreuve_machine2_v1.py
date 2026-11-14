# -*- coding: ascii -*-
"""CONTRE-EPREUVE de verification_acte_domaine_G1_machine2_v1.py : fabrique une COPIE MUTEE du lot de l'acte (dix-sept chiffres ou mots de l'acte changes d'une
unite, vises sur douze controles) ; le verificateur, lance avec LOT_ALT=<cette copie> et SUFFIXE_SORTIE=_sur_acte_mute, doit mordre sur C01, C02 (l'acte n'est plus
au canon) et sur chaque controle vise. Le lot recu n'est que lu.
Usage depuis BOCAL4 : python -P acte_domaine_contreseing/mutation_acte_domaine_contre_epreuve_machine2_v1.py"""
import os
import zipfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'lot_machine1_2026-11-14_acte_domaine_G1_chaine_EA_v1_recu.zip')
DST = os.path.join(ROOT, 'mute_acte_domaine_contre_epreuve.zip')
MUTS = [('1.888  2.832  2.529', '1.888  2.832  2.539', 'C10'),                  # nn.4, mediane de E1
        ('H4  sous dix planchers 7', 'H4  sous dix planchers 6', 'C10'),        # nn.4, exclusion de H4
        ('1.292  1.629  1.505', '1.292  1.639  1.505', 'C10'),                  # nn.4, q max de A2
        ('borne de 11.0 pour cent', 'borne de 12.0 pour cent', 'C11'),          # nn.5, marge de E2
        ('les 12 etats juges hors de la demi-decade', 'les 11 etats juges hors de la demi-decade', 'C11'),   # nn.5, E4
        ('5.24e-12, q = 3.1688,', '5.24e-12, q = 3.1689,', 'C12'),              # nn.6, l etat de H1
        ('vaut 1.4 pour cent de cette lecture', 'vaut 1.5 pour cent de cette lecture', 'C12'),
        ('1.77 a 2.10', '1.78 a 2.10', 'C12'),                                  # nn.6, rapport des q medians
        ('est 5.5 pour cent, a E6 rang 8', 'est 5.6 pour cent, a E6 rang 8', 'C13'),   # nn.7 (d)
        ('FAUSSE (2.867)', 'FAUSSE (2.868)', 'C14'),                            # nn.8, A-9
        ('Neuf sur treize', 'Dix sur treize', 'C14'),
        ('depuis le 14/11 a 14 h 12 et 14 h 13. Aucun', 'depuis le 14/11 a 14 h 15 et 14 h 13. Aucun', 'C15'),   # nn.0
        ('trente et une attendent', 'trente attendent', 'C15'),                 # nn.12
        ('sonde code 0 en 3028 s', 'sonde code 0 en 3038 s', 'C08'),            # nn.2
        ('5e-7 pres', '5e-6 pres', 'C09'),                                      # nn.3
        ('sonde_domaine_G1.json  d51a9c6ce98b0452', 'sonde_domaine_G1.json  d51a9c6ce98b0453', 'C04'),   # nn.1, un canon
        ('(b) (m2, m1) Un critere', '(b) (m1) Un critere', 'C16')]              # nn.12, une origine
z = zipfile.ZipFile(SRC)
nom = 'journal_delta_nn_domaine_G1_chaine_EA_v1.md'
a = z.read(nom).decode('utf-8')
for x, y, c in MUTS:
    assert a.count(x) >= 1, (x, a.count(x))
    a = a.replace(x, y, 1)
with zipfile.ZipFile(DST, 'w') as zo:
    for n in z.namelist():
        zo.writestr(n, a.encode('utf-8') if n == nom else z.read(n))
print('copie mutee ecrite : %s (%d mutations, visant %s)' % (DST, len(MUTS), sorted(set(c for *_, c in MUTS))))
