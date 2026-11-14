# -*- coding: ascii -*-
"""compare_predictions_machine2_v1 : hors chaine, classe 3, machine 2. Mon rejeu de predictions_chaine_points_neufs_machine1_v1.py
(3b09ad4a0cdfc0c4) aux trois points 49/25, 51/25, 21/10 contre le journal de machine 1 (2eb0149e5f19660c). Ne mesure rien.
Usage depuis BOCAL4 : python -P chaine_EA_rejeu/compare_predictions_machine2_v1.py"""
import os
import re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def lire(p):
    out, cur = [], None
    for ln in open(p, encoding='utf-8'):
        m = re.match(r'^POINT w2=(\S+)', ln)
        if m:
            cur = m.group(1)
        m = re.match(r'^\s*(\d+)\s+(\d+)\s+([0-9.e+-]+)\s+(\S+)', ln)
        if m:
            out.append((cur, int(m.group(1)), int(m.group(2)), float(m.group(3))))
    return out


a = lire('chaine_EA_rejeu/predictions_chaine_points_neufs_machine1_v1.log')
b = lire('chaine_EA_rejeu/predictions_chaine_points_neufs_machine2.log')
assert [x[:3] for x in a] == [y[:3] for y in b]
print('PREDICTIONS de la chaine aux points neufs : %d largeurs, machine 1 contre mon rejeu' % len(a))
for s in (1e-11, 1e-10, 1e-9):
    d = [(abs(x[3] / y[3] - 1), x[:3]) for x, y in zip(a, b) if y[3] > s]
    print('  au-dessus de %.0e : %d largeurs, ecart relatif max %.2e (%s)' % (s, len(d), max(d)[0], max(d)[1]))
print('  plus grand ecart absolu : %.2e ; les largeurs sous 2e-14 sont du bruit de la chaine (valeur et signe changent)' % max(abs(x[3] - y[3]) for x, y in zip(a, b)))
print('CE QUE CE LOG NE JOUE PAS : aucune mesure ; il relit des journaux.')
