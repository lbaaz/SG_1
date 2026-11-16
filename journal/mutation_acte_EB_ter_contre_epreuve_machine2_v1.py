# -*- coding: ascii -*-
"""CONTRE-EPREUVE de verification_acte_EB_ter_machine2_v1.py : fabrique une COPIE MUTEE du lot de l'acte (chiffres ou mots de l'acte changes d'une unite, vises sur quatorze
controles) ; le verificateur, lance avec LOT_ALT=<cette copie> et SUFFIXE_SORTIE=_sur_acte_mute, doit mordre sur C01, C02 (l'acte n'est plus au canon) et sur chaque controle vise.
Chaque cible doit apparaitre UNE SEULE FOIS dans l'acte (blancs libres) : sinon la mutation pourrait toucher une autre occurrence que celle que le controle lit ; le script s'arrete.
Le lot recu n'est que lu.
Usage depuis BOCAL4 : py -3.11 -I acte_EB_ter_contreseing/mutation_acte_EB_ter_contre_epreuve_machine2_v1.py"""
import os
import re
import zipfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'lot_machine1_2026-11-15_acte_EB_ter_v1_recu.zip')
DST = os.path.join(ROOT, 'mute_acte_EB_ter_contre_epreuve.zip')
MUTS = [('QUALIFIE 1.012e-11 +0.0076', 'QUALIFIE 1.012e-11 +0.0077', 'C06'),                                  # nn.4, premier tableau, C1
        ('0.0154 0.0227', '0.0154 0.0228', 'C06'),                                                            # nn.4, second tableau, C1
        ('31 sous dix planchers', '30 sous dix planchers', 'C06'),                                           # nn.4
        ('pour un seuil de 124. Issue', 'pour un seuil de 123. Issue', 'C06'),                                # nn.0
        ('lot scelle a 13 h 42 min 03 s', 'lot scelle a 13 h 42 min 04 s', 'C08'),                           # nn.2
        ('de 3772 s (M3) a 3981 s', 'de 3772 s (M3) a 3982 s', 'C08'),
        ('ancres (362 s)', 'ancres (363 s)', 'C08'),
        ('au point L3 (14 etats, 672 lectures)', 'au point L3 (14 etats, 673 lectures)', 'C09'),            # nn.2 (b)
        ('Sur les 1392 lectures', 'Sur les 1393 lectures', 'C09'),
        ('plus grand ecart absolu 5.80e-13', 'plus grand ecart absolu 5.81e-13', 'C10'),                     # nn.3
        ('au plus 0.0007 a j = 6', 'au plus 0.0008 a j = 6', 'C10'),
        ('6461 en deux iterations', '6462 en deux iterations', 'C10'),
        ('poids au site au moins 0.656', 'poids au site au moins 0.657', 'C10'),
        ('G_dep 7.94e-06', 'G_dep 7.95e-06', 'C11'),                                                        # nn.6
        ('est a 0.0008 de A', 'est a 0.0009 de A', 'C11'),
        ('0.0025 et 0.0376 sous C', '0.0025 et 0.0377 sous C', 'C11'),                                       # nn.5
        ('L4 rang 1 (0.1023)', 'L4 rang 1 (0.1024)', 'C13'),                                                # nn.7
        ('au-dessus du plateau a 61 etats, au-dessous a 76', 'au-dessus du plateau a 62 etats, au-dessous a 76', 'C13'),
        ('VRAIE (0.0193)', 'VRAIE (0.0194)', 'C14'),                                                         # nn.8
        ('pour une somme de probabilites de 5.96', 'pour une somme de probabilites de 5.97', 'C14'),
        ('va de 1.003 (L1)', 'va de 1.004 (L1)', 'C15'),                                                     # nn.9
        ('soit 0.0022 en relatif', 'soit 0.0023 en relatif', 'C15'),
        ("a 124 d'entre eux", "a 123 d'entre eux", 'C16'),                                                   # nn.10
        ('origin/main 8d54bf9, plafond 98', 'origin/main 8d54bf9, plafond 97', 'C17'),                       # nn.0
        ('le resultat 1f057651c8f69eb6.', 'le resultat 1f057651c8f69eb7.', 'C18'),                           # nn.13 (et C05)
        ("garde son statut : elle n'est pas qualifiee.", "garde son statut : elle est qualifiee.", 'C19'),   # nn.10, la citation du delta 98
        ('de 7 pour cent', 'de 7 %', 'C03'),                                                                  # nn.7 (et C13)
        ('etiquette (7, 2)', 'etiquette (7, 3)', 'C11')]                                                      # nn.6
z = zipfile.ZipFile(SRC)
nom = 'journal_delta_nn_qualification_EB_ter_v1.md'
a = z.read(nom).decode('utf-8')
echecs, ambigus = [], []
for x, y, c in MUTS:                                          # les blancs (et les fins de ligne) de la cible sont libres
    pat = r'\s+'.join(re.escape(w) for w in x.split())
    n = len(re.findall(pat, a))
    if n != 1:
        (echecs if n == 0 else ambigus).append((x, n))
        continue
    a = re.sub(pat, lambda _m, y=y: y, a, count=1)
assert not echecs and not ambigus, ('cibles absentes', echecs, 'cibles multiples', ambigus)
with zipfile.ZipFile(DST, 'w') as zo:
    for n in z.namelist():
        zo.writestr(n, a.encode('utf-8') if n == nom else z.read(n))
print('copie mutee ecrite : %s (%d mutations, visant %s)' % (DST, len(MUTS), sorted(set(c for *_, c in MUTS))))
