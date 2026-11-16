# -*- coding: ascii -*-
"""[ESSAIS CIBLES SUR LES LIMITES : derive de confrontation_feuilles_gel_loi_machine2_v1.py ; trois scenarios construits pour exercer les regles que les 40 essais aleatoires n'exercent pas :
la garde des deux tiers A L'EGALITE EXACTE (8 etats juges sur 12 lus), le minimum de 2 etats dans le domaine d'une cellule de bord (1 puis 2), le minimum de 2 etats hors du domaine (1 puis 2).]
CONFRONTATION DES DEUX FEUILLES D'ORDRE 3 (la mienne, la sienne) -- machine 2, 2026-11-16. AUCUN calcul 2D : les entrees sont des mesures de points DEJA JOUES
(depot du delta 98, verdict de mon run du gel ter), clonees sous les identifiants des douze cellules du gel (N1..N5, P1..P5, BN, BP), puis PERTURBEES par scenario
(plateaux multiplies, etats declares non qualifies, J flou, etiquette double). Ce sont des entrees sans aucun sens physique : on compare deux LOGIQUES, pas des cellules.
Pour chaque essai : la feuille de machine 1 (facd3ceeec07d3bf, lancee --prevol) et la mienne rendent-elles les memes comptes, exclusions, domaines, issues de cellule et issues globales ?
Usage : py -3.11 -P confrontation_feuilles_gel_loi_machine2_v1.py <moteur> <bloc2> <bloc3> <ordre3_machine2_v1.py> <feuille de m1> <depot> <verdict ter> <dossier (neuf)> <n essais> <graine> <sortie.json>"""
import concurrent.futures as cf
import copy
import hashlib
import importlib.util
import json
import math
import os
import random
import subprocess
import sys
import unicodedata

MOTEUR, BLOC2, BLOC3, SCRIPT3, FEUILLE_M1, DEPOT, VERDICT_TER, DOSSIER, NESSAIS, GRAINE, SORTIE = sys.argv[1:12]
NESSAIS, GRAINE = int(NESSAIS), int(GRAINE)
spec = importlib.util.spec_from_file_location('feuille_independante', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'feuille_independante_gel_loi_machine2_v1.py'))
MINE = importlib.util.module_from_spec(spec)
spec.loader.exec_module(MINE)
os.makedirs(DOSSIER, exist_ok=False)
ENV1 = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')


def canon_B(chemin):
    t = unicodedata.normalize('NFC', open(chemin, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


D0 = json.load(open(DEPOT))
V0 = json.load(open(VERDICT_TER))
POOL = ['C1', 'C2', 'C3', 'C4', 'M1', 'M2', 'M3', 'M4', 'L1', 'L2', 'L3', 'L4']
BONS = ['C1', 'C2', 'C3', 'C4', 'M1', 'M2']          # points exploitables comme lignes
BORDS_BONS = ['C4', 'M2']                             # points a >= 2 etats dans le domaine et >= 2 hors (exploitables comme bords)
CELLULES = [('N1', 'N'), ('N2', 'N'), ('N3', 'N'), ('N4', 'N'), ('N5', 'N'), ('P1', 'P'), ('P2', 'P'), ('P3', 'P'), ('P4', 'P'), ('P5', 'P'), ('BN', 'BN'), ('BP', 'BP')]
SCENARIOS = ['deux_tiers_exact', 'bord_dom', 'bord_hors', 'deux_tiers_exact', 'bord_dom', 'bord_hors', 'deux_tiers_exact', 'bord_dom', 'bord_hors', 'deux_tiers_exact', 'bord_dom', 'bord_hors']
RETRO = json.load(open('retro_machine2_v1.json'))
RET = {c['id']: c for c in RETRO['cellules']}
MOTIFS = {'non qualifie': 'non qualifie', 'J flou': 'J flou', 'etiquette double': 'etiquette double', 'barriere vide': 'barriere vide',
          'chaine du moteur instable': 'chaine du moteur instable', "chaine d'ordre 2 instable": "chaine d'ordre 2 instable"}


def dense_point(pid):
    return [p for p in D0['points'] if p['id'] == pid][0]


def fabriquer(k):
    rng = random.Random(GRAINE * 1000 + k)
    sc = SCENARIOS[k % len(SCENARIOS)]
    T = {'table': 'confrontation : points deja joues clones sous les identifiants des cellules', 'prevol': True, 'points': []}
    D = {kk: vv for kk, vv in D0.items() if kk != 'points'}
    D['points'] = []
    V = {kk: vv for kk, vv in V0.items() if kk != 'points'}
    V['points'] = {}
    sources = {}
    for cid, cr in CELLULES:
        if SCENARIOS[k % len(SCENARIOS)] == 'deux_tiers_exact':
            src = 'M1' if cr in ('N', 'P') else 'C4'
        else:
            src = 'M1' if cr in ('N', 'P') else 'C4'
        sources[cid] = src
        dp = copy.deepcopy(dense_point(src))
        dp['id'] = cid
        D['points'].append(dp)
        vp = copy.deepcopy(V0['points'][src])
        vp['id'] = cid
        V['points'][cid] = vp
        T['points'].append({'id': cid, 'role': 'juge', 'creneau': cr, 'w2': dp['w2'], 'facteur': dp['facteur']})
    for a in ('A1', 'A2'):
        dp = copy.deepcopy(dense_point(a))
        D['points'].append(dp)
        T['points'].append({'id': a, 'role': 'ancre', 'creneau': None, 'w2': dp['w2'], 'facteur': dp['facteur']})

    def etats_v(cid):
        return V['points'][cid]['etats']

    def toutes(cid, f):
        for e in etats_v(cid):
            e['plateaux']['A']['Gamma_pl'] *= f

    lignes = [c for c, cr in CELLULES if cr in ('N', 'P')]
    lignes_ids = lignes
    def juges_domaine(src):
        return [e['rang'] for e in RET[src]['etats'] if e['exclu'] is None and e['domaine']], [e['rang'] for e in RET[src]['etats'] if e['exclu'] is None and not e['domaine']]
    if sc == 'deux_tiers_exact':                          # M1 : 12 lus, 11 juges, tous dans le domaine ; r etats declares non qualifies : r = 3 donne 8 sur 12 = deux tiers EXACTEMENT
        for c in lignes_ids:
            r = rng.choice((2, 3, 3, 4))
            dom_, _h = juges_domaine('M1')
            for rg in rng.sample(dom_, r):
                [e for e in etats_v(c) if e['rang'] == rg][0]['statut'] = 'NON QUALIFIE'
    elif sc == 'bord_dom':                                # C4 : 13 lus, 5 dans le domaine, 8 hors ; on laisse 1 puis 2 etats dans le domaine (declares non qualifies : 4 puis 3)
        for c, restant in (('BN', 1), ('BP', 2)):
            dom_, _h = juges_domaine('C4')
            for rg in rng.sample(dom_, len(dom_) - restant):
                [e for e in etats_v(c) if e['rang'] == rg][0]['statut'] = 'NON QUALIFIE'
    elif sc == 'bord_hors':                               # C4 : on retire du verdict (etats non lus) les etats hors du domaine sauf 1 puis sauf 2
        for c, restant in (('BN', 1), ('BP', 2)):
            _d, hors_ = juges_domaine('C4')
            garder = set(rng.sample(hors_, restant))
            V['points'][c]['etats'] = [e for e in etats_v(c) if not (e['rang'] in hors_ and e['rang'] not in garder)]
    elif sc == 'chute1':
        toutes(rng.choice(lignes), math.exp(rng.choice((-1, 1)) * rng.uniform(0.15, 0.3)))
    elif sc == 'chute2':
        for c in rng.sample(lignes, 2):
            toutes(c, math.exp(rng.choice((-1, 1)) * rng.uniform(0.15, 0.3)))
    elif sc == 'chute_bord':
        toutes(rng.choice(('BN', 'BP')), math.exp(rng.choice((-1, 1)) * rng.uniform(0.15, 0.3)))
    elif sc == 'chute_E2':                                # change l'ordre de proximite sans toucher la tolerance
        for c in rng.sample([c for c, cr in CELLULES if cr == 'N'], 2):
            toutes(c, math.exp(rng.choice((-1, 1)) * rng.uniform(0.03, 0.12)))
    elif sc == 'peu_de_juges':
        for c in rng.sample(lignes + ['BN', 'BP'], 4):
            es = etats_v(c)
            for e in rng.sample(es, max(1, len(es) // 3 + rng.randint(0, 2))):
                e['statut'] = 'NON QUALIFIE'
    else:
        if sc == 'chaos':
            for cid, cr in CELLULES:
                if rng.random() < 0.6:
                    toutes(cid, math.exp(rng.uniform(-0.1, 0.1)))
                for e in etats_v(cid):
                    r = rng.random()
                    if r < 0.12:
                        e['plateaux']['A']['Gamma_pl'] *= math.exp(rng.choice((-1, 1)) * rng.uniform(0.03, 0.25))
                    elif r < 0.17:
                        e['statut'] = 'NON QUALIFIE'
            for cid, _cr in CELLULES:
                if rng.random() < 0.15:
                    dp = [p for p in D['points'] if p['id'] == cid][0]
                    dp['etats'][rng.randrange(len(dp['etats']))]['J_ecart_type'] = 0.25
                if rng.random() < 0.08:
                    dp = [p for p in D['points'] if p['id'] == cid][0]
                    lus = [e['rang'] for e in etats_v(cid)]
                    if len(lus) >= 2:
                        r1, r2 = rng.sample(lus, 2)
                        a, b = [e for e in dp['etats'] if e['rang'] == r1][0], [e for e in dp['etats'] if e['rang'] == r2][0]
                        b['n1'], b['n2'] = a['n1'], a['n2']
                        for e in etats_v(cid):
                            if e['rang'] == r2:
                                e['n1'], e['n2'] = a['n1'], a['n2']
    d = os.path.join(DOSSIER, 't%02d' % k)
    os.makedirs(d)
    ch = {}
    for nom, obj in (('table', T), ('dense', D), ('verdict', V)):
        ch[nom] = os.path.join(d, nom + '.json')
        json.dump(obj, open(ch[nom], 'w'), indent=1, sort_keys=True)
    return {'k': k, 'scenario': sc, 'sources': sources, 'dossier': d, 'fichiers': ch, 'T': T, 'D': D, 'V': V}


def sa_feuille(t):
    f = t['fichiers']
    sortie = os.path.join(t['dossier'], 'sortie_m1.json')
    r = subprocess.run([sys.executable, '-P', FEUILLE_M1, MOTEUR, BLOC2, BLOC3, f['table'], DEPOT, f['dense'], canon_B(f['dense']), f['verdict'], canon_B(f['verdict']), sortie, '--prevol'],
                       capture_output=True, text=True, env=ENV1)
    open(os.path.join(t['dossier'], 'sortie_m1.console.log'), 'w').write(r.stdout + r.stderr)
    return (json.load(open(sortie)) if r.returncode == 0 and os.path.exists(sortie) else None), r.returncode


def comparer(t, mine, his):
    dif = []
    if his is None:
        return ['sa feuille a plante']
    if his.get('instrument') != 'TIENT' or mine.get('instrument') != 'TIENT':
        return ['instrument : %s / %s' % (mine.get('instrument'), his.get('instrument'))]
    H = {c['id']: c for c in his['cellules']}
    for c in mine['cellules']:
        h = H[c['id']]
        for k in ('n_lus', 'n_juges', 'n_domaine', 'n_hors', 'exploitable', 'E1', 'E2', 'E3'):
            if c[k] != h[k]:
                dif.append((c['id'], k, c[k], h[k]))
        if c['n_pres'] != h['n_ordre3_plus_pres'] or c['seuil_E2'] != h['seuil_E2']:
            dif.append((c['id'], 'n_pres/seuil', (c['n_pres'], c['seuil_E2']), (h['n_ordre3_plus_pres'], h['seuil_E2'])))
        hh = {e['rang']: e for e in h['etats']}
        for e in c['etats']:
            x = hh[e['rang']]
            if e['exclu'] != x['exclu']:
                dif.append((c['id'], e['rang'], 'exclu', e['exclu'], x['exclu']))
            elif e['exclu'] is None:
                if bool(e['domaine']) != bool(x['dans_le_domaine']):
                    dif.append((c['id'], e['rang'], 'domaine'))
                if bool(e['tient_E1']) != bool(x['dans_la_tolerance']):
                    dif.append((c['id'], e['rang'], 'dans_la_tolerance', e['tient_E1'], x['dans_la_tolerance']))
                if bool(e['pres']) != bool(x['ordre3_plus_pres'] and x['dans_le_domaine']):
                    dif.append((c['id'], e['rang'], 'ordre3_plus_pres'))
                if bool(e['bande_ok']) != bool(x['dans_la_bande']):
                    dif.append((c['id'], e['rang'], 'bande'))
    for k in ('E1', 'E2', 'E1B', 'E3'):
        a, b = mine[k][0], his[k]['issue']
        if a != b or sorted(mine[k][1]) != sorted(his[k]['tombees']):
            dif.append(('global', k, mine[k], (his[k]['issue'], his[k]['tombees'])))
    return dif


def main():
    MINE.charger(MOTEUR, BLOC2, SCRIPT3)
    essais = [fabriquer(k) for k in range(NESSAIS)]
    print('%d essais fabriques dans %s' % (len(essais), DOSSIER), flush=True)
    with cf.ThreadPoolExecutor(max_workers=7) as ex:
        futs = [ex.submit(sa_feuille, t) for t in essais]
        mines = []
        for t in essais:
            mines.append(MINE.juger(t['T'], t['D'], t['V'], D0))
        res = [f.result() for f in futs]
    bilan, couverture = [], {'E1': {}, 'E2': {}, 'E1B': {}, 'E3': {}}
    n_cel = n_chute = n_inexpl = 0
    for t, mine, (his, code) in zip(essais, mines, res):
        dif = comparer(t, mine, his)
        bilan.append({'k': t['k'], 'scenario': t['scenario'], 'code_m1': code, 'differences': [str(x) for x in dif]})
        for kk in couverture:
            couverture[kk][mine[kk][0]] = couverture[kk].get(mine[kk][0], 0) + 1
        for c in mine['cellules']:
            n_cel += 1
            n_chute += (c['E1'] == 'TOMBE') + (c['E2'] == 'TOMBE')
            n_inexpl += (c['E1'] == 'INEXPLOITABLE')
        print('essai %02d %-13s : %s' % (t['k'], t['scenario'], 'IDENTIQUES' if not dif else 'DIFFERENCES %s' % dif[:3]), flush=True)
    n_dif = sum(1 for b in bilan if b['differences'])
    print('BILAN : %d essais, %d avec une difference ; cellules %d, E1/E2 tombees %d, E1 inexploitables %d' % (len(bilan), n_dif, n_cel, n_chute, n_inexpl))
    for kk, v in couverture.items():
        print('  issues %-3s rencontrees : %s' % (kk, ', '.join('%s x%d' % (a, b) for a, b in sorted(v.items()))))
    json.dump({'essais': bilan, 'couverture': couverture, 'n_dif': n_dif}, open(SORTIE, 'w'), indent=1, sort_keys=True)
    sys.exit(0 if n_dif == 0 else 1)


main()
