# -*- coding: ascii -*-
"""Compare les JOURNAUX produits en rejouant les scripts de machine 1 (sans les editer) a ses propres journaux : identiques octet pour octet ? aux fins de ligne pres ? sinon, quelles lignes different
(durees, nom du fichier de sortie) ? Machine 2, 2026-11-17.
Usage : py -3.11 -I compare_journaux_rejeu_machine2_v1.py <dossier du lot de m1> <dossier de mes rejeux>"""
import os
import re
import sys

LOT, MOI = sys.argv[1], sys.argv[2]
PAIRES = [('tirage_pont_machine1_v1_autotest.log', 'tirage_autotest_rejeu_m2.log'),
          ('tirage_pont_machine1_v1_demonstration.log', 'tirage_demo_rejeu_m2_sa_table.log'),
          ('tirage_pont_machine1_v1_demonstration.log', 'tirage_demo_rejeu_m2_table_commune.log'),
          ('eligibilite_pont_MG_PG_v1.log', 'eligibilite_pont_MG_PG_rejeu_m2.log'),
          ('eligibilite_pont_MG_PG_sans_levier_v1.log', 'eligibilite_pont_MG_PG_rejeu_m2.log')]
for s, m in PAIRES:
    a = open(os.path.join(LOT, s), 'rb').read(); b = open(os.path.join(MOI, m), 'rb').read()
    la = a.decode('utf-8').replace('\r\n', '\n').split('\n'); lb = b.decode('utf-8').replace('\r\n', '\n').split('\n')
    diff = [(x, y) for x, y in zip(la, lb) if x != y] + ([('(longueurs)', '%d / %d lignes' % (len(la), len(lb)))] if len(la) != len(lb) else [])
    hors_duree = [(x, y) for x, y in diff if not (re.search(r'\d+ s\s*$', x) and re.search(r'\d+ s\s*$', y)) and not (x.startswith('ecrit :') and y.startswith('ecrit :'))]
    print('%-46s contre %-40s : octets identiques %-5s ; aux fins de ligne pres %-5s ; lignes differentes %d dont hors durees et nom de fichier %d' % (s, m, a == b, a.replace(b'\r\n', b'\n') == b.replace(b'\r\n', b'\n'), len(diff), len(hors_duree)))
