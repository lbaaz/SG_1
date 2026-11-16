# -*- coding: ascii -*-
"""CONTRE-EPREUVE de verification_gel_loi_partie1_machine2_v1.py : fabrique une COPIE MUTEE du gel 'loi, ordre 3', premiere partie (chiffres ou mots changes d'une unite, vises sur les neuf controles) ; le
verificateur, lance sur cette copie, doit mordre sur C01 (le canon n'est plus celui du gel) et sur chaque controle vise. Chaque cible doit apparaitre UNE SEULE FOIS dans le gel (blancs libres) : sinon la
mutation pourrait toucher une autre occurrence que celle que le controle lit ; le script s'arrete. Le gel recu n'est que lu.
Usage : py -3.11 -I mutation_gel_loi_partie1_contre_epreuve_machine2_v1.py <gel.md> <sortie : copie mutee .md>"""
import re
import sys

GEL, DST = sys.argv[1:3]
MUTS = [('w2 = 1.931 a 1.939', 'w2 = 1.931 a 1.938', 'C03'),                                      # section 2, liste de N
        ('modulo  9 =  4 -> w2 = 1.935', 'modulo  9 =  5 -> w2 = 1.936', 'C04'),                 # section 3, exemple
        ('N <= 74, au moins 8 etiquettes jugeables sur les 14', 'N <= 75, au moins 8 etiquettes jugeables sur les 14', 'C05'),   # 4.5
        ('e_bord < 0.7', 'e_bord < 0.8', 'C05'),                                                   # 4.4
        ('Au plus cinq rangs, de 0 a 4', 'Au plus six rangs, de 0 a 5', 'C06'),                  # section 6
        ('1.931  x3/4 68 11/11', '1.931  x3/4 68 11/10', 'C07'),                                  # section 7, N
        ('1.917  x1 60 11/5/6', '1.917  x1 60 11/5/7', 'C07'),                                    # section 7, BN
        ('creneau BN : 7 w2 eligibles sur 8', 'creneau BN : 8 w2 eligibles sur 8', 'C08'),       # section 7
        ('152 cellules candidates (44 w2)', '151 cellules candidates (44 w2)', 'C08'),            # section 5
        ('8ae603f6af71abd7  eligibilite_creneaux_machine1_v1.py', '8ae603f6af71abd8  eligibilite_creneaux_machine1_v1.py', 'C09'),   # section 11
        ('82a0be882568fe0c scripts/m17_chaine_v17.py', '82a0be882568fe0d scripts/m17_chaine_v17.py', 'C02')]                      # section 1
a = open(GEL, 'rb').read().decode('utf-8')
echecs, ambigus = [], []
for x, y, c in MUTS:                                          # les blancs (et les fins de ligne) de la cible sont libres
    pat = r'\s+'.join(re.escape(w) for w in x.split())
    n = len(re.findall(pat, a))
    if n != 1:
        (echecs if n == 0 else ambigus).append((x, n))
        continue
    a = re.sub(pat, lambda _m, y=y: y, a, count=1)
assert not echecs and not ambigus, ('cibles absentes', echecs, 'cibles multiples', ambigus)
open(DST, 'wb').write(a.encode('utf-8'))
print('copie mutee ecrite : %s (%d mutations, visant %s)' % (DST, len(MUTS), sorted(set(c for *_, c in MUTS))))
