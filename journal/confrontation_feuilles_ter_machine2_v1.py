# -*- coding: ascii -*-
"""CONFRONTATION de MA feuille (feuille_independante_ter_machine2_v1.py) a celle de machine 1 (lecture_qualification_EB_ter_machine1_v1.py,
canon b2d6d7cfaf30f1cf), sans aucun calcul 2D. Trois terrains :
  F1  les 38 etats REELS du reglage de machine 1 (reglage_p1.json, reglage_p2.json) : statut, echecs, plateau (k0, Gamma_pl), consigne (e) ;
      et les chiffres de la section 4 (ii) du gel recalcules par MA feuille (35/3/0, comptes par point, medianes et maxima) ;
  F2  20000 etats synthetiques bati autour des seuils (graine fixe) : plateau a 21/20 +- quelques ulp, accord a tau +- 1e-6, non suivis, valeurs
      nulles, negatives, infinies, absentes ; statut, echecs, non lisibles, consigne (e), plateaux ;
  F3  la cascade : les 3^12 vecteurs de statuts de l'etat de rang 0 des douze points x quatre totaux d'etats qualifies (dont les deux cotes de
      124 sur 137) x instrument TIENT/NE TIENT PAS, et un point manquant ; l'issue de la consigne (e) pour tous les couples (npl, nlu) jusqu'a 140.
SEUIL DE LA CONFRONTATION, declare avant : zero desaccord ; Gamma_pl a 1e-12 relatif ; ce qui differe est montre.
Usage : py -3.11 -I confrontation_feuilles_ter_machine2_v1.py <dossier lot m1> <sortie.json>"""
import importlib.util
import itertools
import json
import math
import os
import random
import statistics
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import feuille_independante_ter_machine2_v1 as MA

LOT = sys.argv[1]
spec = importlib.util.spec_from_file_location('feuille_m1', os.path.join(LOT, 'lecture_qualification_EB_ter_machine1_v1.py'))
M1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M1)
sortie = {'desaccords': []}


def P(*a):
    print(' '.join(str(x) for x in a), flush=True)


def lettres_m1(echecs):
    out = []
    for e in echecs:
        out.append(e[1] + ('-accord' if ' accord ' in e else ''))
    return sorted(out)


def comparer_etat(trajs, g_dep, cle):
    a = M1.juger_etat(trajs, g_dep)
    b = MA.juger_etat(trajs, g_dep)
    pb = []
    if a['statut'] != b['statut']:
        pb.append('statut %s / %s' % (a['statut'], b['statut']))
    if lettres_m1(a['echecs']) != b['echecs']:
        pb.append('echecs %s / %s' % (lettres_m1(a['echecs']), b['echecs']))
    if sorted(a['non_lisibles']) != sorted(b['sans_fenetre']):
        pb.append('non lisibles %s / %s' % (a['non_lisibles'], b['sans_fenetre']))
    if a['lu_sur_le_plateau'] != b['lu']:
        pb.append('consigne e %s / %s' % (a['lu_sur_le_plateau'], b['lu']))
    for x in MA.ABSORBEURS:
        pa, pm = a['plateaux'][x], b['plateaux'][x]
        if pa['statut'] != pm['statut']:
            pb.append('plateau %s : %s / %s' % (x, pa['statut'], pm['statut']))
        elif 'k0' in pa and (pa['k0'] != pm['k0'] or abs(pa['Gamma_pl'] / pm['Gamma_pl'] - 1.0) > 1e-12 or abs(pa['etalement'] - pm['etalement']) > 1e-12):
            pb.append('plateau %s : k0 %s / %s, Gamma_pl %.3e / %.3e' % (x, pa['k0'], pm['k0'], pa['Gamma_pl'], pm['Gamma_pl']))
    if pb:
        sortie['desaccords'].append({'cle': str(cle), 'ecarts': pb})
    return a, b, pb


# ---------------------------------------------------------------- F1 : les 38 etats reels
P('F1  les etats reels du reglage de machine 1')
pts = {}
for f in ('reglage_p1.json', 'reglage_p2.json'):
    pts.update(json.load(open(os.path.join(LOT, f)))['points'])
tous, n_dis = [], 0
for pid in sorted(pts):
    for cle, e in sorted(pts[pid]['etats'].items(), key=lambda kv: kv[1]['rang']):
        a, b, pb = comparer_etat(e['cfg'], e['G2D']['3'], (pid, e['rang']))
        n_dis += bool(pb)
        tous.append((pid, e['rang'], b, e['G2D']['3']))
P('   etats : %d ; desaccords entre les deux feuilles : %d' % (len(tous), n_dis))
q = sum(1 for t in tous if t[2]['statut'] == 'QUALIFIE')
nq = sum(1 for t in tous if t[2]['statut'] == 'NON QUALIFIE')
nl = sum(1 for t in tous if t[2]['statut'] == 'NON LISIBLE')
P('   MA feuille : %d QUALIFIES, %d NON QUALIFIES, %d NON LISIBLES (le gel, section 4 (ii) : 35, 3, 0)' % (q, nq, nl))
par_point = {}
for pid, rang, j, g in tous:
    par_point.setdefault(pid, [0, 0])
    par_point[pid][1] += 1
    par_point[pid][0] += j['statut'] == 'QUALIFIE'
P('   par point (QUALIFIES / juges) : %s (le gel : A1 3/3, A2 3/3, J1 3/3, J2 7/7, J3 3/3, J5 2/2, E4 11/14, H1 3/3)' %
  ', '.join('%s %d/%d' % (k, v[0], v[1]) for k, v in sorted(par_point.items())))
lus0 = [(pid, j['statut']) for pid, rang, j, g in tous if rang == 0]
P('   etat lu (rang 0) : %s' % lus0)
for x in MA.ABSORBEURS:
    es = [j['plateaux'][x]['etalement'] for _, _, j, _ in tous if 'k0' in j['plateaux'][x]]
    P('   etalement sous %s : mediane %.4f, plus grand %.4f (%d etats avec fenetre)' % (x, statistics.median(es), max(es), len(es)))
for x in 'BCD':
    ec = []
    for _, _, j, _ in tous:
        pa, px = j['plateaux']['A'], j['plateaux'][x]
        if pa['statut'] == 'PLATEAU' and px['statut'] == 'PLATEAU':
            ec.append(abs(math.log(px['Gamma_pl'] / pa['Gamma_pl'])))
    P('   accord %s / A : |ln| mediane %.4f, plus grand %.4f' % (x, statistics.median(ec), max(ec)))
dp = [abs(math.log(g / j['plateaux']['A']['Gamma_pl'])) for _, _, j, g in tous if j['plateaux']['A']['statut'] == 'PLATEAU']
P('   consigne (e) : |ln(G_dep / Gamma_pl(A))| mediane %.4f, plus grand %.4f, au-dessus de tau : %d sur %d' % (
    statistics.median(dp), max(dp), sum(1 for e in dp if e > 0.05), len(dp)))
sortie['F1'] = {'etats': len(tous), 'desaccords': n_dis, 'QUALIFIES': q, 'NON_QUALIFIES': nq, 'NON_LISIBLES': nl,
                'par_point': {k: v for k, v in par_point.items()}, 'consigne_mediane': statistics.median(dp), 'consigne_max': max(dp),
                'consigne_au_dessus_de_tau': sum(1 for e in dp if e > 0.05)}

# ---------------------------------------------------------------- F2 : 20000 etats aux bords des seuils
P('F2  etats synthetiques aux bords des seuils')
rng = random.Random(20261115)
KS = list(range(-3, 9))
AMPS = [0.0, 1e-9, 0.005, 0.0200, 0.0240, 0.0243, 0.0245, 0.0247, 0.0250, 0.0260, 0.05, 0.2]


def serie_vals(base):
    kind = rng.choice(['plat', 'plat', 'plat', 'lin', 'fort', 'faible', 'bord', 'bord_ulp'])
    if kind == 'plat':
        a = rng.choice(AMPS)
        v = [base * (1.0 + rng.uniform(-a, a)) for _ in KS]
    elif kind == 'lin':
        v = [base * 2.0 ** (-k) for k in KS]
    elif kind == 'fort':                  # plateau du cote fort puis proportionnel
        m = rng.randint(0, 6)
        v = [base if k <= KS[m] else base * 2.0 ** (-(k - KS[m])) for k in KS]
    elif kind == 'faible':
        m = rng.randint(2, 8)
        v = [base if k >= KS[m] else base * (1.0 + 0.3 * (KS[m] - k)) for k in KS]
    elif kind == 'bord':                  # rapport exactement 21/20 entre deux entiers, a un endroit au hasard
        v = [base * 20.0] * len(KS)
        i = rng.randint(0, 11)
        v[i] = base * 21.0
    else:                                 # un ulp au dessus de la borne
        v = [20.0 * base] * len(KS)
        i = rng.randint(0, 11)
        v[i] = math.nextafter(21.0 * base, math.inf) if rng.random() < 0.5 else 21.0 * base
        if v[i] / (20.0 * base) == 1.05 and rng.random() < 0.5:
            v[i] = math.nextafter(v[i], math.inf)
    return v


def abimer(v):
    """Rend des valeurs non suivies, nulles, negatives, infinies, absentes."""
    rec = {}
    for k, x in zip(KS, v):
        r = rng.random()
        if r < 0.04:
            rec[str(k)] = {'gamma': x, 'suivi': False}
        elif r < 0.06:
            rec[str(k)] = {'gamma': 0.0, 'suivi': True}
        elif r < 0.07:
            rec[str(k)] = {'gamma': -x, 'suivi': True}
        elif r < 0.08:
            rec[str(k)] = {'gamma': float('inf'), 'suivi': True}
        elif r < 0.09:
            rec[str(k)] = {'gamma': None, 'suivi': True}
        else:
            rec[str(k)] = {'gamma': x, 'suivi': True}
    return rec


DELTAS = [0.0, 1e-6, 0.01, 0.05 - 1e-6, 0.05 + 1e-6, -(0.05 - 1e-6), -(0.05 + 1e-6), 0.3]
n_ok, stat = 0, {}
for i in range(20000):
    base = 10.0 ** rng.uniform(-13, -7)
    vA = serie_vals(base)
    trajs = {'A': abimer(vA)}
    plA = MA.plateau(trajs['A'])
    for x in 'BCD':
        r = rng.random()
        if r < 0.6 and 'Gamma_pl' in plA:             # meme forme que A, deplacee de delta
            d = rng.choice(DELTAS)
            trajs[x] = abimer([v * math.exp(d) for v in vA])
        else:
            trajs[x] = abimer(serie_vals(base * math.exp(rng.uniform(-0.1, 0.1))))
    g_dep = (plA['Gamma_pl'] * math.exp(rng.choice(DELTAS)) if 'Gamma_pl' in plA else base)
    a, b, pb = comparer_etat(trajs, g_dep, ('F2', i))
    stat[b['statut']] = stat.get(b['statut'], 0) + 1
    n_ok += not pb
P('   %d etats ; accord complet : %d ; statuts de MA feuille : %s' % (20000, n_ok, stat))
sortie['F2'] = {'etats': 20000, 'accord': n_ok, 'statuts': stat}

# ---------------------------------------------------------------- F3 : cascade
P('F3  cascade et issue de la consigne (e)')
NJ = [8, 11, 14, 13, 12, 14, 8, 9, 14, 11, 14, 9]
STAT = ['QUALIFIE', 'NON QUALIFIE', 'NON LISIBLE']
n, bad, issues = 0, 0, {}
for vec in itertools.product(STAT, repeat=12):
    for tot in (30, 123, 124, 137):
        for inst in ((True, False) if tot == 124 else (True,)):
            # repartition des qualifies : un par point d'etat lu qualifie, puis au hasard deterministe
            q = [1 if s == 'QUALIFIE' else 0 for s in vec]
            reste = tot - sum(q)
            if reste < 0:
                continue
            for i in range(12):
                add = min(reste, NJ[i] - q[i])
                q[i] += add
                reste -= add
            if reste:
                continue
            pts3 = {j: {'etat_lu': vec[i], 'n_juges': NJ[i], 'n_qualifies': q[i]} for i, j in enumerate(M1.JUGES)}
            r1 = M1.cascade('TIENT' if inst else 'NE TIENT PAS', pts3)
            r2 = MA.cascade(inst, {j: vec[i] for i, j in enumerate(MA.JUGES)}, sum(NJ), sum(q))
            n += 1
            issues[r2] = issues.get(r2, 0) + 1
            if r1 != r2:
                bad += 1
                if bad < 6:
                    P('   DESACCORD', vec, tot, inst, r1, r2)
    if n > 200000 and False:
        break
inc = {j: {'etat_lu': 'QUALIFIE', 'n_juges': 10, 'n_qualifies': 10} for j in M1.JUGES if j != 'L4'}
n += 1
bad += M1.cascade('TIENT', inc) != MA.cascade(True, {j: 'QUALIFIE' for j in MA.JUGES if j != 'L4'}, 110, 110)
P('   cascade : %d cas, %d desaccords ; issues atteintes par MA feuille : %s' % (n, bad, issues))
nbi = 0
for npl in range(0, 141):
    for nlu in range(0, npl + 1):
        nbi += M1.issue_depot({'x': {'n_plateau_A': npl, 'n_lus_sur_le_plateau': nlu}})[0] != MA.issue_consigne(npl, nlu)
P('   issue de la consigne (e) : %d couples (npl, nlu), %d desaccords' % (sum(range(1, 142)), nbi))
sortie['F3'] = {'cas': n, 'desaccords': bad, 'issues': issues, 'consigne_desaccords': nbi}
tot_dis = len(sortie['desaccords']) + bad + nbi
sortie['desaccords_total'] = tot_dis
P('')
P('DESACCORDS ENTRE LES DEUX FEUILLES, tous terrains : %d' % tot_dis)
for d in sortie['desaccords'][:8]:
    P('   ', d)
json.dump(sortie, open(sys.argv[2], 'w'), indent=1, sort_keys=True, default=str)
sys.exit(0 if tot_dis == 0 else 1)
