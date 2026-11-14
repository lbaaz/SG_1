# -*- coding: ascii -*-
"""Relecture du JSON REEL de la sonde par mon lecteur independant (celui du banc, ecrit du texte du gel) : meme verdict, memes statuts et memes
nombres d'etats juges que la feuille de machine 1 ? Usage : python -P relecture_independante_machine2_v1.py <banc.py> <sonde.json> <verdict.json>"""
import importlib.util, json, sys
BANC, SONDE, VERDICT = sys.argv[1:4]
sys.argv = [BANC, 'chaine_EA_par_etat/lecture_chaine_par_etat_machine1_v1.py']      # le banc lit sa propre ligne de commande a l'import
sp = importlib.util.spec_from_file_location('banc', BANC); B = importlib.util.module_from_spec(sp); sp.loader.exec_module(B)
S = json.load(open(SONDE, encoding='ascii')); V = json.load(open(VERDICT, encoding='ascii'))
mien, rm = B.lecteur(S)
sien = B.TRAD[V['verdict']]
print('verdict de la feuille de machine 1 : %s ; de mon lecteur independant : %s -> %s' % (V['verdict'], mien, 'MEME' if mien == sien else 'DIFFERENT'))
pts = {x['id']: x for x in V['points']}
ecarts = 0
for pid, (st, nj, ms) in rm.items():
    x = pts[pid]
    ok = (B.TRADP.get(x['statut']) == st and x['n_juges'] == nj)
    ecarts += (not ok)
    print('  %s : feuille %s (%d juges) ; lecteur %s (%d juges) -> %s' % (pid, x['statut'], x['n_juges'], st, nj, 'MEME' if ok else 'DIFFERENT'))
    # motif par etat
    for e, m in zip(x['etats'], ms):
        mm = {None: None, '(1)': 'J flou', '(2)': 'etiquette hors domaine', '(3)': 'site minoritaire', '(4)': 'sous dix planchers', '(5)': 'etat non suivi',
              '(6)': 'cible instable', '(7)': None, '(8)': 'chaine instable', '(9)': 'etiquette en double'}.get(m, '?')
        if m == '(7)':
            ok2 = e['exclu'] in ('barriere vide', 'chaine en erreur')
        else:
            ok2 = (e['exclu'] == mm)
        if not ok2:
            ecarts += 1
            print('      rang %d : motif feuille %s, lecteur %s -> DIFFERENT' % (e['rang'], e['exclu'], m))
print('ECARTS : %d' % ecarts)
