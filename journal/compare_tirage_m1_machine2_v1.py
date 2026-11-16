# -*- coding: ascii -*-
"""Compare MON tirage (tirage_graine_479579_machine2_v1.json) au journal du script de tirage de m1 REJOUE par moi (tirage_m1_script_rejoue_graine_479579_machine2.log) :
creneaux (rang, w2), puis les 28 cellules (identifiant, w2, profondeur, couplage ecrit). Usage : py -3.11 -I compare_tirage_m1_machine2_v1.py"""
import json
import re

D = r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie1_machine2'
moi = json.load(open(D + r'\tirage_graine_479579_machine2_v1.json'))
t = open(D + r'\tirage_m1_script_rejoue_graine_479579_machine2.log', encoding='utf-8', errors='replace').read()
mauv = []
if 'graine : 479579' not in t:
    mauv.append('le journal de m1 ne porte pas la graine 479579')
cr = re.findall(r'^creneau (MG|MP|PP|PG) rang (\d+) : numero \d+ sur 9 -> w2 = (\S+) \(\S+\) : ELIGIBLE, retenu', t, flags=re.M)
print('creneaux lus dans le journal de m1 :', cr)
for nom, rang, w2 in cr:
    if moi['creneaux'][nom] != {'rang': int(rang), 'w2': w2}:
        mauv.append('creneau %s : m1 (%s, %s), moi %s' % (nom, rang, w2, moi['creneaux'][nom]))
if len(cr) != 4:
    mauv.append('quatre creneaux attendus, %d lus' % len(cr))
cel = re.findall(r'^\s+((?:MG|MP|PP|PG)\d+)\s+w2 = (\S+)\s+m = (\d+)\s+g = (\S+)\s+(lisible|profonde)', t, flags=re.M)
mien = [(c['id'], c['w2'], str(c['m']), c['g'], c['ligne']) for c in moi['cellules']]
print('cellules : m1 %d, moi %d ; identiques (identifiant, w2, m, couplage ecrit, ligne) : %s' % (len(cel), len(mien), cel == mien))
if cel != mien:
    mauv.append('les 28 cellules different')
print('MORSURES :', len(mauv))
for m in mauv:
    print('  -', m)
