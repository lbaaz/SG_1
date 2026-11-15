# -*- coding: ascii -*-
"""RELECTURE INDEPENDANTE du JSON de la sonde par MON lecteur (celui de mon banc, ecrit du texte du gel), contre le verdict de la feuille de machine 1.
Meme comparaison que le banc, sur UN seul objet : le JSON reel. Ne rejoue rien, ne relit sous aucun autre critere.
Usage (depuis BOCAL4) : python -P ordre2/relecture_independante_ordre2_machine2_v1.py <feuille.py> <gel.md> <sonde.json>"""
import importlib.util
import json
import os
import sys

feuille, gel, sonde = sys.argv[1], sys.argv[2], sys.argv[3]
sys.argv = ['banc', feuille, gel]                                    # le banc lit ses deux premiers arguments a l'import
sp = importlib.util.spec_from_file_location('banc_m2', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'banc_feuille_ordre2_machine2_v1.py'))
B = importlib.util.module_from_spec(sp)
sp.loader.exec_module(B)
Fm = B.charger(feuille, 'feuille_m1')
S = json.load(open(sonde, encoding='ascii'))
mien, rm = B.lecteur(S)
theirs, sp_ = B.sien(Fm, S)
ok = (mien['v'] == theirs['v'])
diffs = []
if mien['v'] != theirs['v']:
    diffs.append(('verdict', mien['v'], theirs['v']))
if mien['v'] != 'NCI':
    for k in ('bandes', 'comp', 'ener', 'vnu'):
        if mien[k] != theirs[k]:
            diffs.append((k, mien[k], theirs[k]))
    if sorted(mien['marge']) != sorted(theirs['marge']):
        diffs.append(('marge', mien['marge'], theirs['marge']))
for pid, d in rm.items():
    x = sp_.get(pid)
    if x is None or x['statut'] != d['statut'] or x['nj'] != d['nj'] or x['motifs'] != d['motifs']:
        diffs.append((pid, 'statut/nj/motifs', d['statut'], d['nj']))
        continue
    if mien['v'] != 'NCI' and d['statut'] != 'NL':
        for k in ('hors', 'snm', 'pal', 'comp', 'ener', 'q2', 'q1', 'pire', 'ecart_max', 'loi', 'fim'):
            if not B.proche(d[k], x[k]):
                diffs.append((pid, k, d[k], x[k]))
print('RELECTURE INDEPENDANTE (mon lecteur, ecrit du texte du gel) du JSON %s contre la feuille %s' % (sonde, os.path.basename(feuille)))
print('  mon verdict : %s ; celui de la feuille : %s' % (mien['v'], theirs['v']))
if mien['v'] != 'NCI':
    print('  bandes : mienne %s ; feuille %s' % (mien['bandes'], theirs['bandes']))
    print('  comparaison au pire etat : %s / %s ; energies : %s / %s ; lecture sans marge : %s / %s ; etats gardes par la marge : %s / %s' % (
        mien['comp'], theirs['comp'], mien['ener'], theirs['ener'], mien['vnu'], theirs['vnu'], sorted(mien['marge']), sorted(theirs['marge'])))
for pid in sorted(rm):
    d = rm[pid]
    print('  %s : statut %s, %d juges' % (pid, d['statut'], d['nj']) + ('' if d['statut'] == 'NL' or mien['v'] == 'NCI' else ' ; palier %s ; q2 %.3f %.3f %.3f ; %s ; energie %s' % (d['pal'], d['q2'][0], d['q2'][2], d['q2'][1], d['comp'], d['ener'])))
print('  ECARTS ENTRE MON LECTEUR ET LA FEUILLE : %d %s' % (len(diffs), diffs[:6]))
sys.exit(1 if diffs else 0)
