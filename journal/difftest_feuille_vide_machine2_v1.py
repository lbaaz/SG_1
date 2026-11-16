# -*- coding: ascii -*-
"""TEST DIFFERENTIEL des deux feuilles du gel 'largeur du vide' : celle de machine 1 (feuille_vide_machine1_v1.py, canon ac39a24def6c7420) et la MIENNE (feuille_vide_machine2_v1.py), sur des dossiers de run SYNTHETIQUES
ecrits par MON generateur (meme schema de fichier que la sonde : la forme est celle que la feuille de m1 controle). Aucune mesure, aucun fantome : des plateaux poses a la main autour de la prediction de chaque cellule.
Chaque run tire au hasard (graine donnee) : un regime (proportion de cellules bonnes / mauvaises / sur la limite de la bande / illisibles), puis par cellule un ln q, des ecarts des absorbeurs B, C, D a A, une ondulation du plateau A,
une derive (aucun plateau), une lecture non suivie, un jumeau (rapport au plateau, une lecture du jumeau non suivie) ; et par run : l'instrument (TIENT ou non), un fichier absent, une alteration de la forme (canon, couplage, boite, mode).
Les cas LIMITES sont fabriques pour que |ln q| = T - b +- 1e-9 (b = etendue + s predit) afin d'eprouver <= contre <.
Compare : code de sortie, verdict, V1 et VP (issue, comptes, tombees), par cellule jugement / statut du lecteur / temoin / ln q / bande / s (1e-12), liste des cellules incompletes.
Usage : py -3.11 -I difftest_feuille_vide_machine2_v1.py <feuille m1> <ma feuille> <feuille deposee du lecteur> <table> <dossier de travail (neuf)> <N> <graine>"""
import copy
import hashlib
import json
import math
import os
import random
import shutil
import subprocess
import sys
import unicodedata
from multiprocessing import Pool

F1, F2, FL, TABLE, TRAVAIL, N, GRAINE = sys.argv[1:8]
N, GRAINE = int(N), int(GRAINE)
KS = list(range(-3, 9))
ABS = [['A', 'F2', 0, 80], ['B', 'F2', 0, 100], ['C', 'F1', 0, 100], ['D', 'F2', 10, 80]]


def canon(p):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


TAB = json.load(open(TABLE))
CEL = TAB['cellules']
ENTETE = {'sonde': 'sonde_vide_machine1_v1', 'sonde_canon': '0f82986cca133330', 'table_canon': canon(TABLE), 'prevol': False, 'moteur_canon': '82a0be882568fe0c',
          'source_bloc_canon': 'd5cc48f48e37af99', 'reglage': {'ks': KS, 'absorbeurs': ABS}}


def lecture(g, suivi=True):
    return {'gamma': g, 'gamma_im': g, 'E_re': 0.0, 'poids_site': 0.999, 'residu': 1e-13, 'iterations': 2, 'suivi': suivi, 'decalage_repris': False}


def fichier(c, r):
    gpl = math.exp(c['ln_G3'] - r['ln_q'])
    geo = {a: {'forme': f, 'bord': c['r_c'] + dr, 'couches': L, 'N': c['r_c'] + dr + L} for a, f, dr, L in ABS}

    def traj(nom):
        base = gpl * (math.exp(r['ecarts'][nom]) if nom != 'A' else 1.0)
        t = {}
        for i, k in enumerate(KS):
            g = base
            if nom == 'A' and r['ondulation_A']:
                g = base * (1.0 + r['ondulation_A'] * (i % 2))
            if nom == 'A' and r['derive_A']:
                g = base * math.exp(0.05 * i)
            t[str(k)] = lecture(g, suivi=(r['non_suivi'] != nom))
        return t
    jum = {a: {str(k): lecture(r['jumeau_rapport'] * gpl) for k in KS} for a in 'ABCD'}
    if r['jumeau_non_suivi']:
        jum[r['jumeau_non_suivi'][0]][str(r['jumeau_non_suivi'][1])]['suivi'] = False
    return dict(copy.deepcopy(ENTETE), cellule={'id': c['id'], 'w2': c['w2'], 'm': c['m'], 'g': c['g'], 'r_c': c['r_c'], 'eta0': c['eta0']},
                jumeau={'signe': 1, 'site': [0, 0], 'E_depart': 0.0, 'traj': jum, 'absorbeurs': geo},
                fantome={'signe': -1, 'site': [0, 0], 'E_depart': 0.0, 'traj': {a: traj(a) for a in 'ABCD'}, 'absorbeurs': geo})


def tire_run(rng):
    regime = rng.choice([(0, 0, 0), (0.05, 0.1, 0.0), (0.15, 0.2, 0.05), (0.3, 0.4, 0.1), (0.0, 0.5, 0.0), (0.02, 0.0, 0.3), (0.0, 0.0, 0.6)])
    p_mauv, p_lim, p_ill = regime
    par = {}
    for c in CEL:
        r = {'ln_q': rng.choice([0.0, 0.0005, -0.002, 0.004, -0.007, 0.003]), 'ecarts': {x: rng.choice([0.0, 0.001, -0.001, 0.002]) for x in 'BCD'}, 'ondulation_A': 0.0, 'derive_A': False,
             'non_suivi': None, 'jumeau_rapport': rng.choice([1e-70, 1e-20, 1e-9, 1e-6, 1e-6]), 'jumeau_non_suivi': None, 'tag': 'bonne'}
        u = rng.random()
        if u < p_mauv:
            r['ln_q'] = rng.choice([1, -1]) * rng.choice([0.03, 0.05, 0.09, 0.2])
            r['tag'] = 'mauvaise'
        elif u < p_mauv + p_lim:
            ec = {x: rng.choice([0.0, 0.001, 0.004, 0.009, -0.006, 0.0141]) for x in 'BCD'}
            s = max(abs(v) for v in ec.values())
            b = c['etendue'] + s
            eps = rng.choice([-1e-9, 1e-9, -1e-7, 1e-7, 0.0])
            T = c['tolerance']
            cible = rng.choice([T - b + eps, T + b + eps])          # limite TIENT / NON JUGEABLE, ou NON JUGEABLE / TOMBE
            r['ln_q'] = rng.choice([1, -1]) * cible
            r['ecarts'] = ec
            r['tag'] = 'limite'
        elif u < p_mauv + p_lim + p_ill:
            k = rng.choice(['ecart', 'derive', 'non_suivi', 'jumeau', 'jumeau_ns', 'ondule'])
            if k == 'ecart':
                r['ecarts'] = {x: rng.choice([0.0, 0.04, 0.051, -0.06, 0.08]) for x in 'BCD'}
            elif k == 'derive':
                r['derive_A'] = True
            elif k == 'non_suivi':
                r['non_suivi'] = rng.choice(list('ABCD'))
            elif k == 'jumeau':
                r['jumeau_rapport'] = rng.choice([9.99e-7, 1.0001e-6, 1e-3, 2e-6, 1.0])
            elif k == 'jumeau_ns':
                r['jumeau_non_suivi'] = (rng.choice(list('ABCD')), rng.choice(KS))
            else:
                r['ondulation_A'] = rng.choice([0.004, 0.01, 0.02, 0.04, 0.049, 0.0501, 0.06])
            r['tag'] = 'illisible:' + k
        par[c['id']] = r
    if rng.random() < 0.10:                       # la ligne profonde entiere sans plateau (VP NON LUE), ou presque
        gardees = rng.choice([0, 0, 1, 5, 6, 7])
        profondes = [c['id'] for c in CEL if c['ligne'] == 'profonde']
        rng.shuffle(profondes)
        for i in profondes[gardees:]:
            par[i]['derive_A'] = True
            par[i]['tag'] = 'illisible:derive'
    if rng.random() < 0.08:                       # la ligne lisible entiere sans plateau (V1 : aucune cellule jugee)
        for c in CEL:
            if c['ligne'] == 'lisible':
                par[c['id']]['derive_A'] = True
                par[c['id']]['tag'] = 'illisible:derive'
    mut = {}
    if rng.random() < 0.08:
        mut['absent'] = rng.choice(CEL)['id']
    if rng.random() < 0.08:
        mut['forme'] = (rng.choice(CEL)['id'], rng.choice(['canon', 'couplage', 'boite', 'prevol', 'signe', 'barreaux', 'absorbeur_manquant', 'energie']))
    return {'par': par, 'mut': mut, 'instrument': 'TIENT' if rng.random() < 0.93 else rng.choice(['NE TIENT PAS', 'ABSENT'])}


def ecrire(run, d):
    os.makedirs(d)
    if run['instrument'] != 'ABSENT':
        json.dump({'instrument': run['instrument']}, open(os.path.join(d, 'verdict_ter_instrument.json'), 'w'))
    for c in CEL:
        if run['mut'].get('absent') == c['id']:
            continue
        S = fichier(c, run['par'][c['id']])
        m = run['mut'].get('forme')
        if m and m[0] == c['id']:
            if m[1] == 'canon':
                S['sonde_canon'] = '0' * 16
            elif m[1] == 'couplage':
                S['cellule']['g'] = '1.00000e-03'
            elif m[1] == 'boite':
                S['fantome']['absorbeurs']['B']['N'] += 1
            elif m[1] == 'prevol':
                S['prevol'] = True
            elif m[1] == 'signe':
                S['fantome']['signe'] = +1
            elif m[1] == 'barreaux':
                del S['fantome']['traj']['C']['5']
            elif m[1] == 'absorbeur_manquant':
                del S['jumeau']['traj']['D']
            else:
                S['fantome']['E_depart'] = 0.1
        json.dump(S, open(os.path.join(d, 'sonde_vide_%s.json' % c['id']), 'w'))


def lancer(feuille, d, sortie):
    p = subprocess.run([sys.executable, '-I', '-B', feuille, FL, TABLE, d, sortie], capture_output=True, text=True)
    V = json.load(open(sortie)) if os.path.exists(sortie) else None
    return p.returncode, V


def proche(a, b):
    if a is None or b is None:
        return a is None and b is None
    return abs(a - b) <= 1e-12 * max(1.0, abs(a), abs(b))


def compare(A, B):
    (ca, Va), (cb, Vb) = A, B
    ecarts = []
    if ca != cb:
        ecarts.append('code %s vs %s' % (ca, cb))
    if (Va is None) != (Vb is None):
        return ecarts + ['un verdict existe, pas l autre']
    if Va is None:
        return ecarts
    if Va['verdict'] != Vb['verdict']:
        ecarts.append('verdict %r vs %r' % (Va['verdict'], Vb['verdict']))
    ia = sorted(x.split(' :')[0] for x in Va.get('incomplet', []))
    ib = sorted(x.split(' :')[0] for x in Vb.get('incomplet', []))
    if ia != ib:
        ecarts.append('incomplet %s vs %s' % (ia, ib))
    for k in ('V1', 'VP'):
        if (k in Va) != (k in Vb):
            ecarts.append('%s present d un seul cote' % k)
        elif k in Va:
            for f in ('issue', 'comptes', 'tombees'):
                if Va[k][f] != Vb[k][f]:
                    ecarts.append('%s.%s %r vs %r' % (k, f, Va[k][f], Vb[k][f]))
    if 'V1' not in Va or 'V1' not in Vb:        # run incomplet, instrument qui ne tient pas, pre-vol : aucune cellule n'est jugee ; les deux feuilles ne representent pas les cellules de la meme facon
        return ecarts
    ma = {x['id']: x for x in Va['cellules']}
    mb = {x['id']: x for x in Vb['cellules']}
    for i in ma:
        x, y = ma[i], mb[i]
        if x.get('jugement') != y.get('jugement'):
            ecarts.append('%s jugement %s vs %s' % (i, x.get('jugement'), y.get('jugement')))
        if (x.get('lecteur') or {}).get('statut') != (y.get('lecteur') or {}).get('statut'):
            ecarts.append('%s statut du lecteur' % i)
        if (x.get('temoin') or {}).get('tient') != (y.get('temoin') or {}).get('tient'):
            ecarts.append('%s temoin' % i)
        for f, g in (('ln_q', 'ln_q'), ('bande', 'bande'), ('etalement_du_lecteur', 'etalement_du_lecteur')):
            if not proche(x.get(f), y.get(g)):
                ecarts.append('%s %s %r vs %r' % (i, f, x.get(f), y.get(g)))
    return ecarts


def un_run(i):
    rng = random.Random(GRAINE * 100003 + i)
    run = tire_run(rng)
    d = os.path.join(TRAVAIL, 'r%04d' % i)
    ecrire(run, d)
    A = lancer(F1, d, os.path.join(d, 'verdict_m1.json'))
    B = lancer(F2, d, os.path.join(d, 'verdict_m2.json'))
    e = compare(A, B)
    V = A[1] or {}
    res = {'i': i, 'ecarts': e, 'verdict': V.get('verdict', 'AUCUN'), 'tags': sorted(set(r['tag'].split(':')[0] for r in run['par'].values())), 'mut': list(run['mut']),
           'jugements': {c['jugement']: 0 for c in V.get('cellules', []) if 'jugement' in c}}
    for c in V.get('cellules', []):
        res['jugements'][c.get('jugement')] = res['jugements'].get(c.get('jugement'), 0) + 1
    if not e:
        shutil.rmtree(d)
    return res


if __name__ == '__main__':
    os.makedirs(TRAVAIL, exist_ok=False)
    print('feuille m1 canon %s ; ma feuille canon %s ; %d runs, graine %d' % (canon(F1), canon(F2), N, GRAINE))
    with Pool(10) as pool:
        res = pool.map(un_run, range(N))
    mal = [r for r in res if r['ecarts']]
    print('RUNS : %d ; AVEC ECART : %d' % (len(res), len(mal)))
    for r in mal[:15]:
        print('  run %d :' % r['i'], '; '.join(r['ecarts'][:4]))
    issues = {}
    for r in res:
        issues[r['verdict']] = issues.get(r['verdict'], 0) + 1
    print('verdicts rencontres (couverture) :')
    for k, v in sorted(issues.items(), key=lambda kv: -kv[1]):
        print('   %4d  %s' % (v, k))
    cum = {}
    for r in res:
        for k, v in r['jugements'].items():
            cum[k] = cum.get(k, 0) + v
    print('jugements de cellules rencontres :', cum)
    print('runs avec fichier absent / forme alteree :', sum(1 for r in res if r['mut']))
    json.dump({'res': res}, open(os.path.join(TRAVAIL, 'resume.json'), 'w'))
