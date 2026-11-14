# -*- coding: ascii -*-
"""BANC DE MACHINE 2 pour la feuille de lecture de machine 1 (lecture_domaine_G1_machine1_v1.py), gel b59651f99e60707a
"la garde G-1 du moteur et la chaine E-A par etat". Deux parties, toutes deux sur des sondes SYNTHETIQUES (aucune mesure) :
  A. LECTEUR INDEPENDANT, ecrit par machine 2 du TEXTE du gel (sections 4 a 9) ; le tableau de la section 4 (points, garde, D1, c_max),
     les paires et les deux lectures d'ancre sont LUS DANS LE TEXTE DU GEL, pas recopies. Compare a la feuille sur N sondes tirees au
     hasard aux bords exacts des seuils : verdict, rivale, paires, a et b, statut de chaque point, nombre d'etats juges, motif de chaque etat.
  B. MUTATIONS : alterations d'une ligne de la feuille ; pour chacune, le selftest de machine 1 (74 cas) mord-il ? mon banc A mord-il ?
Usage (depuis BOCAL4) : python -P domaine_G1/banc_feuille_domaine_G1_machine2_v1.py <feuille.py> <gel.md> [N_sondes]   (graine fixe)."""
import importlib.util
import math
import os
import random
import re
import subprocess
import sys
import tempfile

FEUILLE = os.path.abspath(sys.argv[1])
GEL = open(sys.argv[2], encoding='ascii').read()
NSONDES = int(sys.argv[3]) if len(sys.argv) > 3 else 3000


def charger(chemin, nom):
    sp = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


# ------------------------------------------------------------------ le tableau du gel, LU dans son texte (section 4)
PTS = {}          # id -> (role, w2, facteur, garde ("EN"/"HORS"), D1, c_max, N)
PAIRES = {}       # nom -> (id EN, id HORS)
cour = None
dans4 = False
for ln in GEL.split('\n'):
    if ln.startswith('4. LES QUATORZE POINTS'):
        dans4 = True
        continue
    if dans4 and ln.startswith('5. '):
        break
    if not dans4:
        continue
    s = ln.strip()
    if s.startswith('JUGES, garde EN DOMAINE'):
        cour = ('juge', 'EN')
    elif s.startswith('JUGES, garde HORS DOMAINE'):
        cour = ('juge', 'HORS')
    elif s.startswith('ANCRES'):
        cour = ('ancre', 'EN')
    m = re.match(r'^(E\d|H\d|A\d)\s+w2 = (\d+/\d+)\s+facteur (\S+)\s+D1 ([0-9.]+)\s+c_max ([0-9.]+)\s+N (\d+)$', s)
    if m and cour:
        f = m.group(3) if '/' in m.group(3) else m.group(3) + '/1'
        PTS[m.group(1)] = (cour[0], m.group(2), f, cour[1], float(m.group(4)), float(m.group(5)), int(m.group(6)))
    for mm in re.finditer(r'P(\d) = \((\w+), (\w+)\)', s):
        PAIRES['P' + mm.group(1)] = (mm.group(2), mm.group(3))
RIV = ('P1', 'P2', 'P3')                                                          # section 8 : "Elle se lit sur les trois paires P1, P2, P3"
mref = re.search(r"a A1 l'etat d'etiquette \((\d+),(\d+)\), a A2 l'etat d'etiquette \((\d+),(\d+)\).*?: ([0-9]\.[0-9]+e-[0-9]+)\s+et\s+([0-9]\.[0-9]+e-[0-9]+)", GEL, re.S)
REFS = {'A1': (int(mref.group(1)), int(mref.group(2)), float(mref.group(5))), 'A2': (int(mref.group(3)), int(mref.group(4)), float(mref.group(6)))}
CANON = '82a0be882568fe0c'
assert len(PTS) == 14 and len(PAIRES) == 5, (len(PTS), len(PAIRES))


# ------------------------------------------------------------------ A. le lecteur independant
def motif(e):
    """Section 5, criteres (1) a (8), dans l'ordre ; None = juge. Les mots 'strictement positives' de (6) et (8) sont appliques."""
    if not e['J_ecart_type'] < 0.2:
        return '(1)'
    if e['n1'] < 0 or e['n2'] < 0:
        return '(2)'
    if not e['poids_site'] >= 0.5:
        return '(3)'
    if not e['Gamma_2D']['3'] > 1.33e-12:
        return '(4)'
    if e['suivi']['2'] < 0.9 or e['suivi']['4'] < 0.9:
        return '(5)'
    g = [e['Gamma_2D'][k] for k in ('2', '3', '4')]
    if not (min(g) > 0 and max(g) / min(g) <= 2.0):
        return '(6)'
    c = e['chaine']
    if c['erreur'] is not None or c['vide'] or not c['definie']:
        return '(7)'
    if not (min(c['gammas']) > 0 and max(c['gammas']) / min(c['gammas']) <= 2.0):
        return '(8)'
    return None


MOTIF_FEUILLE = {'J flou': '(1)', 'etiquette hors domaine': '(2)', 'site minoritaire': '(3)', 'sous dix planchers': '(4)', 'etat non suivi': '(5)',
                 'cible instable': '(6)', 'chaine en erreur': '(7)', 'barriere vide': '(7)', 'chaine instable': '(8)', 'etiquette en double': '(9)', None: None}


def gardes(s):
    mot = []
    if s['moteur_canon'] != CANON:
        mot.append('G1')
    pts = {p['id']: p for p in s['points']}
    if len(s['points']) != 14 or set(pts) != set(PTS):
        return mot + ['G2']
    for pid, (r, w, f, st, d1, cm, n) in PTS.items():
        p = pts[pid]
        if (p['role'], p['w2'], p['facteur']) != (r, w, f):
            mot.append('G2')
        a, b = f.split('/')
        if abs(p['g'] - p['g_regle'] * int(a) / int(b)) > 1e-12 * p['g_regle']:
            mot.append('G2g')
        if p['faisable'] and len(p['etats']) != 14:
            mot.append('G3')
        gm = p.get('garde_moteur')
        if not isinstance(gm, dict) or gm.get('erreur') or gm.get('statut') != (st + ' DOMAINE') or gm.get('D1') is None or gm.get('c_max') is None \
                or abs(gm['D1'] - d1) > 5e-5 or abs(gm['c_max'] - cm) > 5e-5:
            mot.append('G6' + pid)
    for pid, (n1, n2, ref) in REFS.items():
        p = pts[pid]
        tr = [e for e in p['etats'] if e['n1'] == n1 and e['n2'] == n2]
        if not p['faisable'] or len(tr) != 1 or abs(tr[0]['Gamma_2D']['3'] / ref - 1) > 1e-2:
            mot.append('G4' + pid)
    return mot


def lecteur(s):
    mot = gardes(s)
    pts = {p['id']: p for p in s['points']}
    res = {}
    for pid, p in pts.items():
        if pid not in PTS:
            continue
        if not p['faisable']:
            res[pid] = ('NL', 0, None, [])
            continue
        cnt = {}
        for e in p['etats']:
            cnt[(e['n1'], e['n2'])] = cnt.get((e['n1'], e['n2']), 0) + 1
        ms, qs = [], []
        for e in p['etats']:
            m = motif(e)
            if m is None and cnt[(e['n1'], e['n2'])] >= 2:
                m = '(9)'
            ms.append(m)
            if m is None:
                qs.append(e['chaine']['gammas'][2] / e['Gamma_2D']['3'])
        if len(qs) < 6:
            res[pid] = ('NL', len(qs), None, ms)
        elif all(0.5 <= q <= 2.0 for q in qs):
            res[pid] = ('F2', len(qs), 'TENU', ms)
        elif all(0.1 <= q * q <= 10.0 for q in qs):
            res[pid] = ('DEC', len(qs), 'TENU', ms)
        else:
            res[pid] = ('HD', len(qs), 'TOMBE', ms)
    if mot:
        return {'v': 'NCI'}, res
    en = [k for k, v in PTS.items() if v[0] == 'juge' and v[3] == 'EN']
    hors = [k for k, v in PTS.items() if v[0] == 'juge' and v[3] == 'HORS']
    en_l = [k for k in en if res[k][2] is not None]
    hors_l = [k for k in hors if res[k][2] is not None]
    a = sum(1 for k in en_l if res[k][2] == 'TOMBE')
    b = sum(1 for k in hors_l if res[k][2] == 'TENU')
    if len(en_l) < 4 or len(hors_l) < 4:
        v = 'NL'
    elif a == 0 and b == 0:
        v = 'SEP'
    elif a == 0:
        v = 'SUF'
    else:
        v = 'NTP'
    pa = {}
    for nom, (x, y) in PAIRES.items():
        cx, cy = res[x][2], res[y][2]
        pa[nom] = 'NL' if (cx is None or cy is None) else ('HOM' if cx == cy else 'HET')
    lis = [pa[k] for k in RIV if pa[k] != 'NL']
    riv = 'NL' if len(lis) < 2 else ('TENUE' if all(x == 'HOM' for x in lis) else 'NON')
    return {'v': v, 'a': a, 'b': b, 'pa': pa, 'riv': riv}, res


TRAD = {'LA GARDE SEPARE': 'SEP', 'LA GARDE SUFFIT': 'SUF', 'LA GARDE NE TIENT PAS': 'NTP', 'NON LISIBLE': 'NL', "NON CONCLUANT D'INSTRUMENT": 'NCI'}
TRADP = {'FACTEUR 2': 'F2', 'DECADE': 'DEC', 'HORS DECADE': 'HD', 'NON LISIBLE': 'NL'}
TRADPAIRE = {'HOMOGENE': 'HOM', 'HETEROGENE': 'HET', 'NON LISIBLE': 'NL'}
TRADRIV = {'TENUE': 'TENUE', 'NON TENUE': 'NON', 'NON LISIBLE': 'NL'}


# ------------------------------------------------------------------ sondes synthetiques
def etat_alea(R, rang, n1, n2, q0, ref=None, psain=0.80):
    """Un etat dont chaque champ est tire AUX BORDS des seuils du gel, avec probabilite 0.80 d'etre sain."""
    sain = R.random() < psain
    noms = ['sig', 'ps', 'g3', 'sv2', 'sv4', 'f2', 'f4', 'q', 'etal', 'neg']
    mauvais = set() if sain else set(R.sample(noms, R.choice([1, 1, 2])))
    pick = lambda nom, sainv, bords: R.choice(bords) if nom in mauvais else sainv
    sig = pick('sig', R.uniform(0.01, 0.15), [0.19999999, 0.2, 0.25, 0.5])
    ps = pick('ps', R.uniform(0.6, 1.0), [0.49999999, 0.5, 0.3])
    g3 = ref if ref is not None else pick('g3', 10 ** R.uniform(-10, -6), [1.33e-12, 1.3300001e-12, 1.0e-12, 1.4e-12])
    sv2 = pick('sv2', R.uniform(0.95, 0.9999), [0.9, 0.89999, 0.5])
    sv4 = pick('sv4', R.uniform(0.95, 0.9999), [0.9, 0.89999, 0.5])
    f2 = pick('f2', R.uniform(0.7, 1.4), [2.0, 2.0000001, 0.5, 0.49999, 1.0])
    f4 = pick('f4', R.uniform(0.7, 1.4), [2.0, 2.0000001, 0.5, 0.49999, 1.0])
    q = pick('q', q0 * 10 ** R.uniform(-0.12, 0.12), [0.5, 0.49999, 2.0, 2.0000001, 0.316227, 0.316228, 0.3162, 0.3163, 3.162277, 3.162278, 3.1622, 3.1624, 4.0, 0.2])
    etal = pick('etal', R.uniform(1.0, 1.3), [2.0, 2.0000001, 1.9999, 3.0])
    ch = {'definie': True, 'vide': False, 'gammas': None, 'Lambda': 1.0, 'card': 5, 'erreur': None}
    if not sain and R.random() < 0.12:
        ch['vide'] = True
        ch['definie'] = False
    if not sain and R.random() < 0.08:
        ch['erreur'] = 'SystemExit: x'
        ch['definie'] = False
    if not sain and not ch['vide'] and ch['erreur'] is None and R.random() < 0.12:
        ch['definie'] = False                              # critere (7) : "chaine definie" ; ni vide ni en erreur, mais non definie
    lu = q * g3
    ch['gammas'] = [lu * etal, lu * (1.0 + 0.5 * (etal - 1.0)), lu, lu]
    g2d = {'2': g3 * f2, '3': g3, '4': g3 * f4}
    if 'neg' in mauvais:                                   # 'strictement positives' : une valeur nulle ou negative, de la cible ou de la chaine
        c = R.choice(['cible2', 'cible4', 'ch0', 'ch3', 'chneg'])
        if c == 'cible2':
            g2d['2'] = R.choice([0.0, -1e-9])
        elif c == 'cible4':
            g2d['4'] = R.choice([0.0, -1e-9])
        elif c == 'ch0':
            ch['gammas'] = [lu, lu, lu, 0.0]
        elif c == 'ch3':
            ch['gammas'] = [0.0, lu, lu, lu]
        else:
            ch['gammas'] = [lu, -lu, lu, lu]
    e = {'rang': rang, 'recouvrement': 0.03, 'E_re': 0.0, 'J_moyen': 0.0, 'J_ecart_type': sig, 'n1_moyen': n1, 'n2_moyen': n2,
         'n1': n1, 'n2': n2, 'poids_site': ps, 'poids_Fock_max': ps, 'Gamma_2D': g2d, 'suivi': {'2': sv2, '4': sv4}, 'chaine': ch}
    if not sain and R.random() < 0.10:
        if R.random() < 0.5:
            e['n1'] = -1
        else:
            e['n2'] = -1
    return e


def sonde_alea(R):
    pts = []
    scen = R.choice(['sep', 'suf', 'ntp', 'hom1', 'hom5', 'libre', 'libre'])        # scenarios : la cascade doit rendre ses cinq issues, pas seulement NON CONCLUANT
    pas_sain = R.random() < (0.30 if scen == 'libre' else 0.10)
    psain = 0.80 if scen == 'libre' else 0.985
    id_suf = set(R.sample(['H1', 'H2', 'H3', 'H4', 'H5', 'H6'], R.choice([1, 2, 3])))
    id_ntp = R.choice(['E1', 'E2', 'E3', 'E4', 'E5', 'E6'])
    mal_ancre = [0.0] * 14 + [0.004, 0.0099999, -0.0099999, 0.0100001, 0.03] if scen == 'libre' else [0.0] * 30 + [0.004, 0.0099999, -0.0099999, 0.0100001, 0.03]
    for pid, (r, w, f, st, d1, cm, n) in PTS.items():
        a, b = f.split('/')
        g_regle = 10 ** R.uniform(-3, -2)
        if scen == 'libre':
            if st == 'EN':
                q0 = R.choices([1.0, 2.5, 5.0], [0.65, 0.15, 0.20])[0]
            else:
                q0 = R.choices([1.0, 2.5, 5.0], [0.40, 0.15, 0.45])[0]
        else:
            q0 = 1.0 if st == 'EN' else 5.0
            if scen == 'hom1':
                q0 = 1.0
            if scen == 'hom5':
                q0 = 5.0
            if scen == 'suf' and pid in id_suf:
                q0 = R.choice([1.0, 2.5])
            if scen == 'ntp' and pid == id_ntp:
                q0 = 5.0
        dup = R.random() < (0.20 if scen == 'libre' else 0.03)
        etats = [etat_alea(R, rang, 5 + rang // (2 if dup else 1), 2, q0, psain=psain) for rang in range(14)]
        if R.random() < (0.20 if scen == 'libre' else 0.06):                              # un point a 4..7 etats juges seulement (bord de 6)
            for rang in R.sample(range(14), 14 - R.choice([4, 5, 6, 7])):
                etats[rang]['Gamma_2D'] = {'2': 1e-13, '3': 1e-13, '4': 1e-13}
        if pid in REFS:
            (n1, n2, ref) = REFS[pid]
            for rang in range(1, 14):
                etats[rang]['n1'], etats[rang]['n2'] = 20 + rang, 2
            etats[0] = etat_alea(R, 0, n1, n2, 1.0, ref=ref * (1.0 + R.choice(mal_ancre)))
            etats[0]['poids_site'] = 0.9
        gm = {'Omega_c': 1.0, 'D1': d1 + R.choice([0.0, 0.0, 4.9e-5, -4.9e-5]), 'c_max': cm + R.choice([0.0, 0.0, 4.9e-5, -4.9e-5]), 'site_c_max': 3,
              'statut': st + ' DOMAINE', 'erreur': None}
        p = {'id': pid, 'role': r, 'w2': w, 'facteur': f, 'g_regle': g_regle, 'g': g_regle * int(a) / int(b), 'faisable': True, 'etats': etats,
             'garde_moteur': gm}
        if R.random() < (0.04 if scen == 'libre' else 0.01):
            p['faisable'] = False
        pts.append(p)
    s = {'moteur_canon': CANON, 'points': pts}
    if pas_sain:
        c = R.choice(['moteur', 'manque', 'g', 'g_fin', 'role', 'ancre_absent', 'ancre_double', 'n_etats', 'g6_statut', 'g6_D1', 'g6_cmax', 'g6_erreur',
                      'g6_absente', 'g6_bord_dedans', 'w2'])
        i = R.randrange(14)
        if c == 'moteur':
            s['moteur_canon'] = '0000000000000000'
        elif c == 'manque':
            s['points'] = [p for p in pts if p['id'] != R.choice(['E1', 'H3', 'A1', 'H6'])]
        elif c == 'g':
            pts[i]['g'] *= 1.001
        elif c == 'g_fin':
            pts[i]['g'] *= 1.0 + R.choice([5e-13, 2e-12])
        elif c == 'role':
            pts[i]['role'] = 'juge' if pts[i]['role'] == 'ancre' else 'ancre'
        elif c == 'ancre_absent':
            pts[12]['etats'][0]['n1'] = 99
        elif c == 'ancre_double':                          # G-4 : l'etat d'etiquette de l'ancre "existe une seule fois"
            ia = R.choice([12, 13])
            (n1a, n2a, _) = REFS[pts[ia]['id']]
            jd = R.randrange(1, 14)
            pts[ia]['etats'][jd]['n1'], pts[ia]['etats'][jd]['n2'] = n1a, n2a
        elif c == 'n_etats':
            pts[i]['etats'] = pts[(i + 1) % 14]['etats'][:13]
        elif c == 'g6_statut':
            pts[i]['garde_moteur']['statut'] = 'HORS DOMAINE' if pts[i]['garde_moteur']['statut'] == 'EN DOMAINE' else 'EN DOMAINE'
        elif c == 'g6_D1':
            pts[i]['garde_moteur']['D1'] = PTS[pts[i]['id']][4] + R.choice([1e-4, -1e-4, 5.1e-5, -5.1e-5])
        elif c == 'g6_cmax':
            pts[i]['garde_moteur']['c_max'] = PTS[pts[i]['id']][5] + R.choice([1e-4, -1e-4, 5.1e-5, -5.1e-5])
        elif c == 'g6_erreur':
            pts[i]['garde_moteur']['erreur'] = 'AssertionError: x'
        elif c == 'g6_absente':
            del pts[i]['garde_moteur']
        elif c == 'g6_bord_dedans':
            pts[i]['garde_moteur']['D1'] = PTS[pts[i]['id']][4] + 4.9e-5
        elif c == 'w2':
            pts[i]['w2'] = '1/2'
    return s


def sien(F, s):
    r = F.cascade(s)
    v = TRAD[r['verdict']]
    sp = {x['id']: (TRADP.get(x['statut']), x['n_juges'], [MOTIF_FEUILLE[e['exclu']] for e in x['etats']]) for x in r['points']}
    out = {'v': v}
    if v != 'NCI':
        out.update({'a': r['a_EN_tombes'], 'b': r['b_HORS_tenus'], 'pa': {k: TRADPAIRE[x] for k, x in r['paires'].items()}, 'riv': TRADRIV[r['rivale']]})
    return out, sp


def comparer(F, nsondes, graine=20261114):
    R = random.Random(graine)
    n_ecarts, repart, rep_riv, exemples = 0, {}, {}, []
    for i in range(nsondes):
        s = sonde_alea(R)
        mien, rm = lecteur(s)
        try:
            theirs, sp = sien(F, s)
        except Exception as ex:
            theirs, sp = {'v': 'EXC:' + type(ex).__name__}, {}
        repart[mien['v']] = repart.get(mien['v'], 0) + 1
        if 'riv' in mien:
            rep_riv[mien['riv']] = rep_riv.get(mien['riv'], 0) + 1
        ok = (mien == theirs)
        if ok:
            for pid, (st, nj, cl, ms) in rm.items():
                x = sp.get(pid)
                if x is None or x[0] != st or x[1] != nj or (mien['v'] != 'NCI' and x[2] != ms):
                    ok = False
                    break
        if not ok:
            n_ecarts += 1
            if len(exemples) < 4:
                exemples.append((i, mien['v'], theirs['v']))
    return n_ecarts, repart, rep_riv, exemples


MUT = [
    ('SIGMA_J_MAX = 0.2', 'SIGMA_J_MAX = 0.25'), ('POIDS_SITE_MIN = 0.5', 'POIDS_SITE_MIN = 0.45'), ('DIX_PLANCHERS = 1.33e-12', 'DIX_PLANCHERS = 1.0e-12'),
    ('SUIVI_MIN = 0.9', 'SUIVI_MIN = 0.8'), ('STABILITE_CIBLE = 2.0', 'STABILITE_CIBLE = 2.5'), ('ETALEMENT_CHAINE = 2.0', 'ETALEMENT_CHAINE = 3.0'),
    ('MIN_JUGES = 6', 'MIN_JUGES = 5'), ('MIN_EN_LISIBLES = 4', 'MIN_EN_LISIBLES = 3'), ('MIN_HORS_LISIBLES = 4', 'MIN_HORS_LISIBLES = 3'),
    ('MIN_PAIRES_RIVALE = 2', 'MIN_PAIRES_RIVALE = 3'), ('TOL_ANCRE = 1e-2', 'TOL_ANCRE = 2e-2'), ('TOL_GARDE = 5e-5', 'TOL_GARDE = 1e-4'),
    ('N_ETATS = 14\n', 'N_ETATS = 13\n'),
    ('if 0.5 <= q <= 2.0:', 'if 0.5 < q <= 2.0:'), ('if q * q >= 0.1 and q * q <= 10.0:', 'if q * q > 0.1 and q * q <= 10.0:'),
    ('q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"]', 'q = e["chaine"]["gammas"][1] / e["Gamma_2D"]["3"]'),
    ('q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"]', 'q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["2"]'),
    ('vus[(e["n1"], e["n2"])] > 1', 'vus[(e["n1"], e["n2"])] > 2'), ('if len(juges) < MIN_JUGES:', 'if len(juges) <= MIN_JUGES:'),
    ('pire = max(juges, key=lambda x: ORDRE_PALIER[x["palier"]])', 'pire = min(juges, key=lambda x: ORDRE_PALIER[x["palier"]])'),
    ('min(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN', 'max(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN'),
    ('gs = [e["Gamma_2D"][k] for k in ("2", "3", "4")]', 'gs = [e["Gamma_2D"][k] for k in ("3", "4")]'),
    ('if e["n1"] < 0 or e["n2"] < 0:', 'if e["n1"] < 0:'), ('motifs += garde_ancres(pts)', 'pass'),
    ('if not (g3 > DIX_PLANCHERS):', 'if not (g3 >= DIX_PLANCHERS):'),
    ('if min(cg) <= 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:', 'if min(cg) < 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:'),
    ('if min(gs) <= 0 or max(gs) / min(gs) > STABILITE_CIBLE:', 'if min(gs) < 0 or max(gs) / min(gs) > STABILITE_CIBLE:'),
    ('if not (e["J_ecart_type"] < SIGMA_J_MAX):', 'if not (e["J_ecart_type"] <= SIGMA_J_MAX):'),
    ('if not (e["poids_site"] >= POIDS_SITE_MIN):', 'if not (e["poids_site"] > POIDS_SITE_MIN):'),
    ('if ch.get("vide") or not ch.get("definie"):', 'if ch.get("vide"):'),
    ('"DECADE": "TENU"', '"DECADE": "TOMBE"'),
    ('a = sum(1 for x in en_l if x["classe"] == "TOMBE")', 'a = sum(1 for x in en_l if x["classe"] == "TENU")'),
    ('b = sum(1 for x in hors_l if x["classe"] == "TENU")', 'b = sum(1 for x in hors_l if x["classe"] == "TOMBE")'),
    ('if len(en_l) < MIN_EN_LISIBLES or len(hors_l) < MIN_HORS_LISIBLES:', 'if len(en_l) < MIN_EN_LISIBLES and len(hors_l) < MIN_HORS_LISIBLES:'),
    ('elif a == 0 and b == 0:', 'elif a == 0 or b == 0:'), ('    elif a == 0:\n        v = "LA GARDE SUFFIT"', '    elif a <= 1:\n        v = "LA GARDE SUFFIT"'),
    ('ATTENDUS[k][0] == "juge" and ATTENDUS[k][3] == EN]', 'ATTENDUS[k][3] == EN]'),
    ('rivale = "TENUE" if all(x == "HOMOGENE" for x in lisibles) else "NON TENUE"', 'rivale = "TENUE" if any(x == "HOMOGENE" for x in lisibles) else "NON TENUE"'),
    ('if len(lisibles) < MIN_PAIRES_RIVALE:', 'if len(lisibles) <= MIN_PAIRES_RIVALE:'),
    ('PAIRES_RIVALE = ("P1", "P2", "P3")', 'PAIRES_RIVALE = ("P1", "P2", "P3", "P4")'),
    ('out[nom] = "HOMOGENE" if ca == cb else "HETEROGENE"', 'out[nom] = "HOMOGENE" if ca != cb else "HETEROGENE"'),
    ('if ca is None or cb is None:', 'if ca is None and cb is None:'),
    ('"P2": ("E3", "H2")', '"P2": ("E3", "H1")'),
    ('if gm.get("statut") != statut:', 'if False:'),
    ('abs(gm["D1"] - d1) > TOL_GARDE or abs(gm["c_max"] - cmax) > TOL_GARDE', 'abs(gm["D1"] - d1) > TOL_GARDE and abs(gm["c_max"] - cmax) > TOL_GARDE'),
    ('abs(gm["c_max"] - cmax) > TOL_GARDE', 'abs(gm["c_max"] - d1) > TOL_GARDE'),
    ('if gm.get("erreur"):', 'if False:'), ('if not isinstance(gm, dict):', 'if False:'),
    ('"E2": ("juge", "209/100", "1/1", EN, 0.090000, 0.093558)', '"E2": ("juge", "209/100", "1/1", EN, 0.090000, 0.093658)'),
    ('"H1": ("juge", "52/25", "2/3", HORS, 0.080000, 0.103309)', '"H1": ("juge", "52/25", "2/3", EN, 0.080000, 0.103309)'),
    ('2.1623273017950654e-10', '2.2623273017950654e-10'),
    ('lisibles = [paires[k] for k in PAIRES_RIVALE if paires[k] != "NON LISIBLE"]', 'lisibles = [paires[k] for k in PAIRES_RIVALE]'),
    ('"E3": ("juge", "21/10", "3/2", EN, 0.100000, 0.077751)', '"E3": ("juge", "21/10", "3/2", EN, 0.100000, 0.087751)'),
    ('if len(tr) != 1:', 'if len(tr) < 1:'), ('if ecart > TOL_ANCRE:', 'if ecart >= TOL_ANCRE * 2:'),
    ('if m is None and vus[(e["n1"], e["n2"])] > 1:', 'if vus[(e["n1"], e["n2"])] > 1:'),
    ('if abs(p["g"] - p["g_regle"] * eval_fraction(fac)) > 1e-12 * p["g_regle"]:', 'if abs(p["g"] - p["g_regle"] * eval_fraction(fac)) > 1e-9 * p["g_regle"]:'),
    ('if s.get("moteur_canon") != MOTEUR_CANON:', 'if False:'),
    ('if (p["role"], p["w2"], p["facteur"]) != (role, w2, fac):', 'if (p["w2"], p["facteur"]) != (w2, fac):'),
]


def main():
    F = charger(FEUILLE, 'feuille_m1')
    print('A. LECTEUR INDEPENDANT (gel b59651f99e60707a, sections 4 a 9) CONTRE LA FEUILLE %s' % os.path.basename(FEUILLE))
    print('   tableau lu dans le texte du gel : %d points, %d paires, ancres %s' % (len(PTS), len(PAIRES), REFS))
    # le tableau du gel, comparaison avec celui de la feuille
    ecarts_tab = []
    for pid, (r, w, f, st, d1, cm, n) in PTS.items():
        a = F.ATTENDUS[pid]
        if not (a[0] == r and a[1] == w and a[2] == f and a[3] == (st + ' DOMAINE') and abs(a[4] - d1) < 1e-12 and abs(a[5] - cm) < 1e-12):
            ecarts_tab.append(pid)
    print('   tableau de la feuille == tableau du gel, aux 14 points : %s ; ecarts %s ; paires de la feuille == paires du gel : %s' % (
        not ecarts_tab, ecarts_tab, F.PAIRES == PAIRES))
    ne, rep, rep_riv, ex = comparer(F, NSONDES)
    print('   %d sondes synthetiques aux bords des seuils ; verdicts du lecteur independant : %s ; rivale : %s' % (NSONDES, dict(sorted(rep.items())), dict(sorted(rep_riv.items()))))
    print('   ecarts feuille / lecteur : %d%s' % (ne, '' if ne == 0 else '  exemples ' + str(ex)))
    qe = math.sqrt(10.0)
    print('   BORD EXACT, hors tirage : q = sqrt(10) = %r ; q x q = %r ; feuille : %s ; le gel (section 6) ecrit la demi-decade en flottants, 0.1 <= q x q <= 10' % (
        qe, qe * qe, F.palier(qe)))
    src = open(FEUILLE, encoding='ascii').read()
    print("B. MUTATIONS DE LA FEUILLE : %d alterations d'une ligne ; le selftest de machine 1 mord-il ? mon banc A mord-il ?" % len(MUT))
    surv_selftest, surv_banc, surv_deux, absents = [], [], [], []
    for i, (a, b) in enumerate(MUT, 1):
        if src.count(a) < 1:
            print('   M%02d  MOTIF ABSENT : %s' % (i, a))
            absents.append(i)
            continue
        t = src.replace(a, b, 1)
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'feuille_mutee.py')
            open(p, 'w', encoding='ascii', newline='\n').write(t)
            rc = subprocess.run([sys.executable, '-P', p, '--selftest'], capture_output=True, text=True).returncode
            mord_self = (rc != 0)
            Fm = charger(p, 'feuille_mutee_%d' % i)
            ne2, _, _, _ = comparer(Fm, 1200)
            mord_banc = ne2 > 0
        print('   M%02d  selftest m1 : %-8s  banc m2 : %-8s  %s  ->  %s' % (i, 'MORD' if mord_self else 'survit', 'MORD' if mord_banc else 'survit',
              a[:56].strip().replace('\n', ' '), b[:50].strip().replace('\n', ' ')))
        if not mord_self:
            surv_selftest.append(i)
        if not mord_banc:
            surv_banc.append(i)
        if not mord_self and not mord_banc:
            surv_deux.append(i)
    print('   BILAN : %d alterations ; motifs absents %s ; survivent au selftest de machine 1 : %s ; survivent a mon banc : %s ; survivent aux deux : %s' % (
        len(MUT), absents, surv_selftest, surv_banc, surv_deux))


if __name__ == '__main__':
    main()
