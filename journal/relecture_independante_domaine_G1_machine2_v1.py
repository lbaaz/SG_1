# -*- coding: ascii -*-
"""Relecture du JSON REEL de la sonde par mon lecteur independant (celui du banc, ecrit du texte du gel) : memes verdict, rivale, paires, a et b, statuts, nombres
d'etats juges et motifs que la feuille de machine 1 ? Usage (depuis BOCAL4) : python -P domaine_G1/relecture_independante_domaine_G1_machine2_v1.py <sonde.json> <verdict.json>"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SONDE, VERDICT = sys.argv[1:3]
sys.argv = ['banc', os.path.join(HERE, 'lecture_domaine_G1_machine1_v1.py'), os.path.join(HERE, 'gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md')]    # le banc lit sa ligne de commande a l'import
sp = importlib.util.spec_from_file_location('banc', os.path.join(HERE, 'banc_feuille_domaine_G1_machine2_v1.py'))
B = importlib.util.module_from_spec(sp)
sp.loader.exec_module(B)
S = json.load(open(SONDE, encoding='ascii'))
V = json.load(open(VERDICT, encoding='ascii'))
mien, rm = B.lecteur(S)
v_f = B.TRAD[V['verdict']]
ecarts = 0
print('verdict de la feuille de machine 1 : %s ; de mon lecteur independant : %s -> %s' % (V['verdict'], mien['v'], 'MEME' if mien['v'] == v_f else 'DIFFERENT'))
ecarts += (mien['v'] != v_f)
if mien['v'] != 'NCI' and v_f != 'NCI':
    pa = {k: B.TRADPAIRE[x] for k, x in V['paires'].items()}
    riv = B.TRADRIV[V['rivale']]
    ok = (pa == mien['pa'] and riv == mien['riv'] and V['a_EN_tombes'] == mien['a'] and V['b_HORS_tenus'] == mien['b'])
    ecarts += (not ok)
    print('  a = %d, b = %d ; paires %s ; rivale %s -> feuille a %d, b %d, paires %s, rivale %s : %s' % (
        mien['a'], mien['b'], mien['pa'], mien['riv'], V['a_EN_tombes'], V['b_HORS_tenus'], pa, riv, 'MEME' if ok else 'DIFFERENT'))
pts = {x['id']: x for x in V['points']}
for pid, (st, nj, cl, ms) in rm.items():
    x = pts[pid]
    ok = (B.TRADP.get(x['statut']) == st and x['n_juges'] == nj)
    ecarts += (not ok)
    print('  %s : feuille %s (%d juges) ; lecteur %s (%d juges) -> %s' % (pid, x['statut'], x['n_juges'], st, nj, 'MEME' if ok else 'DIFFERENT'))
    for e, m in zip(x['etats'], ms):
        if B.MOTIF_FEUILLE[e['exclu']] != m:
            ecarts += 1
            print('      rang %d : motif feuille %s, lecteur %s -> DIFFERENT' % (e['rang'], e['exclu'], m))
print('ECARTS : %d' % ecarts)
