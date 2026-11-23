# -*- coding: ascii -*-
"""REJEU, SUR LE RUN REEL, de MON juge independant (juge_sommet de certification_feuille_sommet_machine2_v1.py, ecrit des sections 5 et 6 de la piece avant le run) et comparaison cellule par cellule a verdict_sommet.json (sa feuille, jouee dans le run).
Je ne change ni mon juge ni ses regles : je l'importe tel quel (son en-tete lit sys.argv : je lui donne des arguments, dont un dossier de travail neuf).
Compare : lue ou non, jugement, ln q, bande, ln Gamma_pl, etalement s, S1, portee, nombre de cellules par issue. Rapporte aussi, SANS JUGEMENT : lectures non suivies par cellule (fantome et jumeau), poids du site 0 minimal, plus grande largeur relative du jumeau, plus grand ecart ln(X / A) entre absorbeurs.
Usage : py -3.11 -P rejeu_juge_independant_run_machine2_v1.py <dossier du run> <table gelee JSON> <feuille deposee du lecteur> <modele : un lect2D de Q2> <dossier de travail neuf>"""
import importlib.util
import json
import math
import os
import sys

RUN, TABLE, FEUILLE_DEP, MODELE, TRAV = sys.argv[1:6]
ICI = os.path.dirname(os.path.abspath(__file__))
sys.argv = [sys.argv[0], 'sans-objet', FEUILLE_DEP, TABLE, MODELE, TRAV]
spec = importlib.util.spec_from_file_location('cert_feuille', os.path.join(ICI, 'certification_feuille_sommet_machine2_v1.py'))
CF = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CF)
V = json.load(open(os.path.join(RUN, 'verdict_sommet.json')))
mj = CF.juge_sommet(RUN, False)
print('MON JUGE sur le run reel : garde %s ; S1 %s ; portee %s ; comptes %s' % (mj['guard'], mj['S1'], mj['portee'], mj.get('comptes')))
print('SA FEUILLE (verdict_sommet.json) : verdict %r ; S1 %s ; portee %s ; comptes %s' % (V['verdict'], V['S1']['issue'], V['S1']['portee_kappa'], V['S1']['comptes']))
pire = {'ln_q': 0.0, 'bande': 0.0, 'ln_Gamma_pl': 0.0, 's': 0.0}
ko = []
for c in V['cellules']:
    m = mj['cells'][c['id']]
    if bool(c['lu']) != m['lu'] or c['jugement'] != m['jug']:
        ko.append((c['id'], c['lu'], c['jugement'], m['lu'], m['jug']))
        continue
    if m['lu']:
        pire['ln_q'] = max(pire['ln_q'], abs(c['ln_q'] - m['lnq']))
        pire['bande'] = max(pire['bande'], abs(c['bande'] - m['bande']))
        pire['ln_Gamma_pl'] = max(pire['ln_Gamma_pl'], abs(c['ln_Gamma_pl'] - math.log(m['gam'])))
        pire['s'] = max(pire['s'], abs(c['etalement_du_lecteur'] - m['s']))
print('56 cellules comparees : differences de lecture ou de jugement : %s ; plus grands ecarts : ln q %.1e ; bande %.1e ; ln Gamma_pl %.1e ; etalement s %.1e' % (ko or 'AUCUNE', pire['ln_q'], pire['bande'], pire['ln_Gamma_pl'], pire['s']))
ok = (not ko and mj['S1'] == V['S1']['issue'] and sorted(mj['portee']) == sorted(V['S1']['portee_kappa']) and mj['guard'] == 'TIENT' and max(pire.values()) < 1e-9)
print('ACCORD DE MON JUGE ET DE SA FEUILLE SUR LE RUN REEL : %s' % ('OUI' if ok else 'NON'))
# sans jugement : etat des lectures
nonsuiv_f, nonsuiv_j, pw, tw, ec = [], [], 1.0, 0.0, 0.0
for c in CF.T['cellules']:
    for signe, liste in ((-1, nonsuiv_f), (1, nonsuiv_j)):
        traj = json.load(open(os.path.join(RUN, CF.nom({'id': c['id']}, signe))))['lecture']['traj']
        for x in 'ABCD':
            for k in CF.KS:
                r = traj[x][str(k)]
                if not r['suivi']:
                    liste.append('%s %s k=%+d' % (c['id'], x, k))
                elif signe == -1 and r['poids_site'] is not None:
                    pw = min(pw, r['poids_site'])
nl = [i for i, x in mj['cells'].items() if x['lu']]
print('\nSANS JUGEMENT : lectures non suivies du fantome : %d sur %d ; du jumeau : %d sur %d' % (len(nonsuiv_f), 56 * 48, len(nonsuiv_j), 56 * 48))
if nonsuiv_f:
    print('    fantome non suivies : %s' % '; '.join(nonsuiv_f[:40]))
print('    poids du site (0, 0) minimal sur toutes les lectures suivies du fantome : %.4f' % pw)
print('    cellules lues : %d ; plus grand |ln q| : %.5f ; plus petite marge T - b - |ln q| : %.5f' % (len(nl), max(abs(mj['cells'][i]['lnq']) for i in nl), min(0.01 - mj['cells'][i]['bande'] - abs(mj['cells'][i]['lnq']) for i in nl)))
print('    plus grand etalement s du lecteur : %.5f ; plus grande bande b : %.5f' % (max(mj['cells'][i]['s'] for i in nl), max(mj['cells'][i]['bande'] for i in nl)))
