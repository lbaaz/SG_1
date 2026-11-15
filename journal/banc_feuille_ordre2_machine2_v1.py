# -*- coding: ascii -*-
"""BANC DE MACHINE 2 pour la feuille de lecture de machine 1 (lecture_ordre2_machine1_v1.py), gel 41153158190cf7f1 "la chaine E-A au second ordre".
Deux parties, toutes deux sur des sondes SYNTHETIQUES (aucune mesure) :
  A. LECTEUR INDEPENDANT, ecrit par machine 2 du TEXTE du gel (sections 4 a 10) ; le tableau de la section 4, les bornes de la section 6, les seuils des
     sections 5 a 10, les canons et les quatre constantes des ancres (G-4, G-8) sont LUS DANS LE TEXTE DU GEL, pas recopies. Compare a la feuille sur N sondes tirees
     au hasard aux bords exacts des seuils : verdict, issue de chaque bande, comparaison au pire etat, energies, lecture sans marge et etats gardes par la marge,
     et, a chaque point : statut, nombre d'etats juges, motif de chaque etat, palier, comparaisons, loi apres coup, arithmetique.
  B. MUTATIONS : alterations d'une ligne de la feuille ; pour chacune, le selftest de machine 1 (160 cas) mord-il ? mon banc A mord-il ?
Usage (depuis BOCAL4) : python -P ordre2/banc_feuille_ordre2_machine2_v1.py <feuille.py> <gel.md> [N_sondes] [N_sondes_par_mutation]   (graine fixe)."""
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
GN = re.sub(r'\s+', ' ', GEL)
NSONDES = int(sys.argv[3]) if len(sys.argv) > 3 else 3000
NMUT = int(sys.argv[4]) if len(sys.argv) > 4 else 600


def charger(chemin, nom):
    sp = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


# ------------------------------------------------------------------ le texte du gel : tableau (section 4), seuils (sections 5 a 10)
PTS = {}          # id -> (role, w2, facteur, statut de la garde, D1, c_max, N, bande)
cour = None
for ln in GEL.split('\n'):
    s = ln.strip()
    mb = re.match(r'^JUGES, bande (PROCHE|MOYENNE|LOINTAINE)', s)
    if mb:
        cour = ('juge', mb.group(1).lower())
    elif s.startswith('ANCRES'):
        cour = ('ancre', None)
    elif s.startswith('TEMOINS'):
        cour = ('temoin', None)
    m = re.match(r'^(C\d|M\d|L\d|A\d|W\d)\s+w2 = (\d+/\d+)\s+facteur (\S+)\s+delta ([+-][0-9.]+)\s+D1 ([0-9.]+)\s+c_max ([0-9.]+)\s+(EN DOMAINE|HORS DOMAINE)\s+N (\d+)$', s)
    if m and cour:
        f = m.group(3) if '/' in m.group(3) else m.group(3) + '/1'
        PTS[m.group(1)] = (cour[0], m.group(2), f, m.group(7), float(m.group(5)), float(m.group(6)), int(m.group(8)), cour[1])
assert len(PTS) == 16, len(PTS)
BORNE = {}
for mm in re.finditer(r'^\s+(PROCHE|MOYENNE|LOINTAINE)\s+(?:[0-9.]+ < )?\|delta\| <= ([0-9.]+)\s+B = ([0-9.]+)$', GEL, re.M):
    BORNE[mm.group(1).lower()] = float(mm.group(3))
assert BORNE == {'proche': 1.25, 'moyenne': 1.6, 'lointaine': 2.0}, BORNE
ORDRE_BANDES = ['proche', 'moyenne', 'lointaine']
LIMITE = {'proche': '0.06', 'moyenne': '0.10', 'lointaine': '0.12'}


def lire(motif, groupe=1, cast=float):
    m = re.search(motif, GN)
    assert m, motif
    return cast(m.group(groupe))


SIGMA = lire(r'ecart-type de J < ([0-9.]+) ;')
POIDS = lire(r'poids sur le site \(n1, n2\) >= ([0-9.]+) ;')
DIXP = lire(r'Gamma_2D\(3\) > ([0-9.e-]+) ;')
SUIVI = lire(r'recouvrements de suivi >= ([0-9.]+) ;')
STAB = lire(r'max / min <= ([0-9.]+) ;')
PLANC = lire(r'ou p = ([0-9.e-]+) est le plancher')
TOLE = lire(r'si tous ses etats juges ont un ecart <= ([0-9.]+)\.')
MINJ = lire(r'ou compte moins de ([0-9]+) etats juges', 1, int)
MINL = lire(r'si moins de ([0-9]+) de ses 4 points sont lisibles', 1, int)
CAN_M = lire(r'G-1\s+le moteur lu par la sonde est au canon ([0-9a-f]{16})', 1, str)
CAN_S = lire(r'G-7\s+la sonde qui a produit le JSON est au canon ([0-9a-f]{16})', 1, str)
TOL_G6 = lire(r'a ([0-9.e-]+) pres\. G-7')
TOL_G4 = lire(r"lecture du run de M17 a ([0-9.e-]+) pres en relatif")
TOL_G8 = lire(r'Gamma_flux a ([0-9.e-]+) pres en relatif')
TOL_G8E = lire(r'dE a ([0-9.e-]+) pres en relatif')
mref4 = re.search(r"a A1 l'etat d'etiquette \((\d+),(\d+)\), a A2 l'etat d'etiquette \((\d+),(\d+)\), existe .*? relatif : ([0-9]\.[0-9]+e-[0-9]+) et ([0-9]\.[0-9]+e-[0-9]+)\.", GN)
mref8 = re.search(r'Gamma_flux a [0-9.e-]+ pres en relatif, ([0-9]\.[0-9]+e-[0-9]+) et ([0-9]\.[0-9]+e-[0-9]+) ; dE a [0-9.e-]+ pres en relatif, ([-0-9.]+) et ([-0-9.]+)\.', GN)
assert mref4 and mref8
REFS = {'A1': (int(mref4.group(1)), int(mref4.group(2)), float(mref4.group(5)), float(mref8.group(1)), float(mref8.group(3))),
        'A2': (int(mref4.group(3)), int(mref4.group(4)), float(mref4.group(6)), float(mref8.group(2)), float(mref8.group(4)))}
B_LOI = lire(r'exp\(([0-9.]+) delta\^2 m_bord\)')
assert (SIGMA, POIDS, DIXP, SUIVI, STAB, PLANC, TOLE, MINJ, MINL) == (0.2, 0.5, 1.33e-12, 0.9, 2.0, 1.33e-13, 0.01, 6, 3), (SIGMA, POIDS, DIXP, SUIVI, STAB, PLANC, TOLE, MINJ, MINL)
assert (TOL_G6, TOL_G4, TOL_G8, TOL_G8E, B_LOI) == (5e-5, 1e-2, 1e-3, 1e-6, 2.87)


# ------------------------------------------------------------------ A. le lecteur independant
def fr(t):
    a, b = t.split('/')
    return int(a) / int(b)


def motif(e):
    """Section 5, criteres (1) a (11), dans l'ordre ; None = juge ; (12), l'etiquette unique, est ajoute par le lecteur de point."""
    if not e['J_ecart_type'] < SIGMA:
        return 1
    if e['n1'] < 0 or e['n2'] < 0:
        return 2
    if not e['poids_site'] >= POIDS:
        return 3
    if not e['Gamma_2D']['3'] > DIXP:
        return 4
    if e['suivi']['2'] < SUIVI or e['suivi']['4'] < SUIVI:
        return 5
    g = [e['Gamma_2D'][k] for k in ('2', '3', '4')]
    if not (min(g) > 0 and max(g) / min(g) <= STAB):
        return 6
    c = e['chaine']
    if c['erreur'] is not None or c['vide'] or not c['definie']:
        return 7
    if not (min(c['gammas']) > 0 and max(c['gammas']) / min(c['gammas']) <= STAB):
        return 8
    c2 = e.get('chaine2')
    if c2 is None:
        return 10
    if c2['erreur'] is not None:
        return 9
    if not c2['definie']:
        return 10
    f = c2['gammas_flux']
    if not (min(f) > 0 and max(f) / min(f) <= STAB):
        return 11
    return None


def lecteur_point(pid, p):
    role, w2, fac, st, d1, cm, N, bande = PTS[pid]
    borne = BORNE.get(bande)
    if not p['faisable']:
        return {'statut': 'NL', 'nj': 0, 'motifs': []}
    delta = fr(p['w2']) - 2.0
    cnt = {}
    for e in p['etats']:
        cnt[(e['n1'], e['n2'])] = cnt.get((e['n1'], e['n2']), 0) + 1
    motifs, J = [], []
    for e in p['etats']:
        m = motif(e)
        if m is None and cnt[(e['n1'], e['n2'])] >= 2:
            m = 12
        motifs.append(m)
        if m is None:
            g3 = e['Gamma_2D']['3']
            q1 = e['chaine']['gammas'][2] / g3
            c2 = e['chaine2']
            q2 = c2['gammas_flux'][2] / g3
            g2 = c2['gammas_flux'][2]
            de2d = e['E_re'] - e['E_libre']
            de2 = c2['dE'][2]
            ecart = abs(de2 - de2d) / abs(de2d) if de2d != 0.0 else float('inf')
            pal = None
            for b in (1.25, 1.6, 2.0):
                if (g3 - PLANC) / b <= g2 <= b * (g3 + PLANC):
                    pal = b
                    break
            J.append({'rang': e['rang'], 'n1': e['n1'], 'n2': e['n2'], 'q1': q1, 'q2': q2, 'g3': g3, 'g2': g2, 'ecart': ecart, 'pal': pal,
                      'dans': (borne is not None and (g3 - PLANC) / borne <= g2 <= borne * (g3 + PLANC)),
                      'nue': (borne is not None and g3 / borne <= g2 <= borne * g3),
                      'loi': q2 / math.exp(B_LOI * delta * delta * c2['m_bord']),
                      'fim': abs(c2['gammas_im'][2] / g2 - 1.0)})
    out = {'nj': len(J), 'motifs': motifs}
    if len(J) < MINJ:
        out['statut'] = 'NL'
        return out
    xs = sorted(j['q2'] for j in J)
    out['statut'] = 'LU' if borne is None else ('TENU' if all(j['dans'] for j in J) else 'TOMBE')
    out['hors'] = None if borne is None else sum(1 for j in J if not j['dans'])
    out['snm'] = None if borne is None else ('TENU' if all(j['nue'] for j in J) else 'TOMBE')
    out['marge'] = [] if borne is None else [(pid, j['n1'], j['n2']) for j in J if j['dans'] and not j['nue']]
    out['pal'] = None if any(j['pal'] is None for j in J) else max(j['pal'] for j in J)
    out['q2'] = (xs[0], xs[-1], 0.5 * (xs[(len(xs) - 1) // 2] + xs[len(xs) // 2]))
    x1 = sorted(j['q1'] for j in J)
    out['q1'] = (x1[0], x1[-1], 0.5 * (x1[(len(x1) - 1) // 2] + x1[len(x1) // 2]))
    p1 = max(abs(math.log(j['q1'])) for j in J)
    p2 = max(abs(math.log(j['q2'])) for j in J)
    out['pire'] = (p1, p2)
    out['comp'] = 'MIEUX' if p2 < p1 else 'PAS'
    out['ener'] = 'T' if all(j['ecart'] <= TOLE for j in J) else 'N'
    out['ecart_max'] = max(j['ecart'] for j in J)
    ls = sorted(j['loi'] for j in J)
    out['loi'] = 0.5 * (ls[(len(ls) - 1) // 2] + ls[len(ls) // 2])
    out['fim'] = max(j['fim'] for j in J)
    return out


def gardes(s):
    """G-1, G-2, G-3, G-4, G-6, G-7, G-8 (G-5 est le selftest). Rend l'ensemble des gardes qui mordent."""
    mot = set()
    if s.get('moteur_canon') != CAN_M:
        mot.add('G1')
    if s.get('sonde_canon') != CAN_S:
        mot.add('G7')
    pts = {p['id']: p for p in s['points']}
    ids = [p['id'] for p in s['points']]
    obligatoires = [k for k, v in PTS.items() if v[0] != 'temoin']
    if len(ids) != len(set(ids)) or any(k not in PTS for k in ids) or any(k not in pts for k in obligatoires):
        return mot | {'G2'}
    for pid, p in pts.items():
        role, w2, fac, st, d1, cm, N, bande = PTS[pid]
        if (p['role'], p['w2'], p['facteur']) != (role, w2, fac):
            mot.add('G2')
        if abs(p['g'] - p['g_regle'] * fr(fac)) > 1e-12 * p['g_regle']:
            mot.add('G2')
        if p['faisable'] and len(p['etats']) != 14:
            mot.add('G3')
        gm = p.get('garde_moteur')
        if not isinstance(gm, dict) or gm.get('erreur') or gm.get('statut') != st or gm.get('D1') is None or gm.get('c_max') is None \
                or abs(gm['D1'] - d1) > TOL_G6 or abs(gm['c_max'] - cm) > TOL_G6:
            mot.add('G6')
    for pid, (n1, n2, ref, ref2, refe) in REFS.items():
        p = pts[pid]
        if not p['faisable']:
            mot.add('G4')
            continue
        tr = [e for e in p['etats'] if e['n1'] == n1 and e['n2'] == n2]
        if len(tr) != 1:
            mot.add('G4')
            continue
        if abs(tr[0]['Gamma_2D']['3'] / ref - 1) > TOL_G4:
            mot.add('G4')
        c2 = tr[0].get('chaine2') or {}
        if not c2.get('definie') or c2.get('erreur'):
            mot.add('G8')
        else:
            if abs(c2['gammas_flux'][2] / ref2 - 1) > TOL_G8 or abs(c2['dE'][2] / refe - 1) > TOL_G8E:
                mot.add('G8')
    return mot


def lecteur(s):
    mot = gardes(s)
    res = {pid: lecteur_point(pid, p) for pid, p in {p['id']: p for p in s['points']}.items() if pid in PTS}
    if mot:
        return {'v': 'NCI'}, res
    juges = [k for k, v in PTS.items() if v[0] == 'juge']
    bandes = {}
    for b in ORDRE_BANDES:
        lis = [k for k in juges if PTS[k][7] == b and res[k]['statut'] != 'NL']
        if len(lis) < MINL:
            bandes[b] = 'NL'
        elif all(res[k]['statut'] == 'TENU' for k in lis):
            bandes[b] = 'T'
        else:
            bandes[b] = 'N'

    v = None
    if bandes['proche'] == 'NL':
        v = 'NL'
    elif bandes['proche'] == 'N':
        v = 'NTP'
    elif bandes['moyenne'] != 'T':
        v = 'J06'
    elif bandes['lointaine'] != 'T':
        v = 'J10'
    else:
        v = 'TIENT'
    lis = [k for k in juges if res[k]['statut'] != 'NL']
    comp = 'NL' if not lis else ('MIEUX' if all(res[k]['comp'] == 'MIEUX' for k in lis) else 'PAS')
    ener = 'NL' if not lis else ('T' if all(res[k]['ener'] == 'T' for k in lis) else 'N')
    # lecture sans marge : meme cascade sur le statut 'snm'
    bn = {}
    for b in ORDRE_BANDES:
        l2 = [k for k in juges if PTS[k][7] == b and res[k]['statut'] != 'NL']
        bn[b] = 'NL' if len(l2) < MINL else ('T' if all(res[k]['snm'] == 'TENU' for k in l2) else 'N')
    if bn['proche'] == 'NL':
        vn = 'NL'
    elif bn['proche'] == 'N':
        vn = 'NTP'
    elif bn['moyenne'] != 'T':
        vn = 'J06'
    elif bn['lointaine'] != 'T':
        vn = 'J10'
    else:
        vn = 'TIENT'
    marge = [x for k in juges if res[k]['statut'] != 'NL' for x in res[k]['marge']]
    return {'v': v, 'bandes': bandes, 'comp': comp, 'ener': ener, 'vnu': vn, 'marge': marge}, res


TRAD = {"L'ORDRE 2 TIENT": 'TIENT', "L'ORDRE 2 TIENT JUSQU'A 0.06": 'J06', "L'ORDRE 2 TIENT JUSQU'A 0.10": 'J10', "L'ORDRE 2 NE TIENT PAS": 'NTP',
        'NON LISIBLE': 'NL', "NON CONCLUANT D'INSTRUMENT": 'NCI'}
TRADB = {'TENUE': 'T', 'NON TENUE': 'N', 'NON LISIBLE': 'NL'}
TRADC = {"L'ORDRE 2 FAIT MIEUX PARTOUT": 'MIEUX', 'PAS PARTOUT': 'PAS', 'NON LISIBLE': 'NL'}
TRADE = {"L'ENERGIE TIENT": 'T', "L'ENERGIE NE TIENT PAS": 'N', 'NON LISIBLE': 'NL'}
TRADP = {'TENU': 'TENU', 'TOMBE': 'TOMBE', 'LU': 'LU', 'NON LISIBLE': 'NL'}
MOTIF_F = {'J flou': 1, 'etiquette hors domaine': 2, 'site minoritaire': 3, 'sous dix planchers': 4, 'etat non suivi': 5, 'cible instable': 6, 'chaine en erreur': 7,
           'barriere vide': 7, 'chaine instable': 8, 'ordre 2 en erreur': 9, 'ordre 2 non defini': 10, 'ordre 2 instable': 11, 'etiquette en double': 12, None: None}


def sien(Fm, s):
    r = Fm.cascade(s)
    out = {'v': TRAD[r['verdict']]}
    if out['v'] != 'NCI':
        out.update({'bandes': {k: TRADB[x['issue']] for k, x in r['bandes'].items()}, 'comp': TRADC[r['comparaison']['issue']], 'ener': TRADE[r['energie']['issue']],
                    'vnu': TRAD[r['verdict_sans_marge']], 'marge': [tuple(x) for x in r['gardes_par_la_marge']]})
    sp = {}
    for x in r['points']:
        d = {'statut': TRADP[x['statut']], 'nj': x['n_juges'], 'motifs': [MOTIF_F[e['exclu']] for e in x['etats']]}
        if x['statut'] != 'NON LISIBLE':
            d.update({'hors': x['hors_borne'], 'snm': x['statut_sans_marge'], 'pal': x['palier'], 'comp': 'MIEUX' if x['comparaison'] == 'MIEUX' else 'PAS',
                      'ener': 'T' if x['energie'] == 'TENUE' else 'N', 'q2': (x['q2_min'], x['q2_max'], x['q2_median']), 'q1': (x['q1_min'], x['q1_max'], x['q1_median']),
                      'pire': (x['pire_ordre1'], x['pire_ordre2']), 'ecart_max': x['ecart_energie_max'], 'loi': x['q2_sur_loi_median'], 'fim': x['flux_contre_im_max']})
        sp[x['id']] = d
    return out, sp


def proche(a, b):
    if isinstance(a, tuple):
        return all(proche(x, y) for x, y in zip(a, b))
    if isinstance(a, float) or isinstance(b, float):
        return a == b or (a is not None and b is not None and abs(a - b) <= 1e-9 * max(abs(a), abs(b), 1e-300))
    return a == b


# ------------------------------------------------------------------ sondes synthetiques
def paires_exactes():
    """Huit couples (dE_2D, dE_2) dont l'ecart relatif |dE_2 - dE_2D| / |dE_2D| vaut exactement 0.01 en flottants, cherches par un tirage fixe."""
    R = random.Random(7)
    out = []
    while len(out) < 8:
        d = R.uniform(1e-4, 5e-3) * R.choice([1, -1])
        for s in (1, -1):
            for e in (d * (1 + 0.01 * s), d + 0.01 * s * abs(d)):
                if abs(e - d) / abs(d) == 0.01:
                    out.append((d, e))
                    break
    return out


EXACT_E = paires_exactes()


def etat_alea(R, rang, n1, n2, w2, B, q0, psain, mode, ref=None, ref2=None, refe=None, q2_force=None):
    """Un etat dont chaque champ est tire AUX BORDS des seuils du gel, avec probabilite psain d'etre sain."""
    sain = R.random() < psain
    noms = ['sig', 'ps', 'g3', 'sv2', 'sv4', 'f2', 'f4', 'etal1', 'neg1', 'c1', 'c2err', 'c2def', 'etal2', 'neg2', 'c2abs']
    mauvais = set() if sain else set(R.sample(noms, R.choice([1, 1, 2])))
    pick = lambda nom, sainv, bords: R.choice(bords) if nom in mauvais else sainv
    sig = pick('sig', R.uniform(0.01, 0.15), [0.19999999, 0.2, 0.25, 0.5])
    ps = pick('ps', R.uniform(0.6, 1.0), [0.49999999, 0.5, 0.3])
    if ref is not None:
        g3 = ref
    else:
        base = 10 ** R.uniform(-10.5, -6.5) if R.random() < 0.8 else R.uniform(1.34e-12, 4e-12)
        g3 = pick('g3', base, [1.33e-12, 1.3300001e-12, 1.0e-12, 1.4e-12])
    sv2 = pick('sv2', R.uniform(0.95, 0.9999), [0.9, 0.89999, 0.5])
    sv4 = pick('sv4', R.uniform(0.95, 0.9999), [0.9, 0.89999, 0.5])
    f2 = pick('f2', R.uniform(0.7, 1.4), [2.0, 2.0000001, 0.5, 0.49999, 1.0])
    f4 = pick('f4', R.uniform(0.7, 1.4), [2.0, 2.0000001, 0.5, 0.49999, 1.0])
    # q2 : dedans ou aux bords de la borne, de la borne nue, de la borne a marge d'un plancher
    p = PLANC
    haut, bas = B * (g3 + p) / g3, (g3 - p) / (B * g3)
    bords = [B, B * (1 + 1e-9), B * (1 - 1e-9), 1 / B, (1 / B) * (1 + 1e-9), (1 / B) * (1 - 1e-9), haut * (1 + 1e-9), haut * (1 - 1e-9), bas * (1 + 1e-9), bas * (1 - 1e-9),
             B * 1.05, 1 / (B * 1.05), B * 1.3, 1 / (B * 1.3), B * 3.0]
    if mode == 'dedans':
        q2 = B ** R.uniform(-0.85, 0.85)
    elif mode == 'bord':
        q2 = R.choice(bords)
    else:
        q2 = R.choice(bords) if R.random() < 0.25 else q0 * 10 ** R.uniform(-0.15, 0.15)
    if ref2 is not None:
        q2 = ref2 / g3
    if q2_force is not None:
        q2 = q2_force
    g2 = q2 * g3
    if mode != 'dedans' and ref2 is None and q2_force is None and R.random() < 0.10:
        g2 = R.choice([B * (g3 + p), (g3 - p) / B, B * g3, g3 / B])      # l'egalite exacte aux quatre bords (borne a marge, borne nue), en flottants
        q2 = g2 / g3
    # q1 : par rapport a q2 (pire etat)
    q1 = R.choice([q2, q2 * (1 + 1e-9), q2 * (1 - 1e-9), 1 / q2, 1.0 / (q2 * (1 + 1e-9)), q2 * 3.0, q2 / 3.0, 10 ** R.uniform(-0.5, 0.5), 1.0, 0.7, 1.4])
    etal1 = pick('etal1', R.uniform(1.0, 1.3), [2.0, 2.0000001, 1.9999, 3.0])
    etal2 = pick('etal2', R.uniform(1.0, 1.3), [2.0, 2.0000001, 1.9999, 3.0])
    ch = {'definie': True, 'vide': False, 'gammas': None, 'Lambda': 1.0, 'card': 5, 'erreur': None}
    if 'c1' in mauvais:
        k = R.choice(['vide', 'erreur', 'nondef'])
        ch['vide'] = (k == 'vide')
        ch['erreur'] = 'SystemExit: x' if k == 'erreur' else None
        ch['definie'] = False
    lu1 = q1 * g3
    ch['gammas'] = [lu1 * etal1, lu1 * (1.0 + 0.5 * (etal1 - 1.0)), lu1, lu1]
    if 'neg1' in mauvais:
        c = R.choice(['ch0', 'ch3', 'chneg'])
        ch['gammas'] = [lu1, lu1, lu1, 0.0] if c == 'ch0' else ([0.0, lu1, lu1, lu1] if c == 'ch3' else [lu1, -lu1, lu1, lu1])
    c2 = {'definie': True, 'm_bord': R.randrange(3, 13), 'm_min': -2, 'gammas_flux': [g2 * etal2, g2 * (1.0 + 0.5 * (etal2 - 1.0)), g2, g2],
          'gammas_im': [g2 * x * (1.0 + R.choice([0.0, 1e-3, -2e-3, 0.02])) for x in (1.0, 1.0, 1.0, 1.0)], 'dE': None, 'Sigma2_0': 1e-4, 'erreur': None}
    if 'neg2' in mauvais:
        c = R.choice(['f0', 'f3', 'fneg'])
        c2['gammas_flux'] = [g2, g2, g2, 0.0] if c == 'f0' else ([0.0, g2, g2, g2] if c == 'f3' else [g2, -g2, g2, g2])
    if 'c2err' in mauvais:
        c2['erreur'] = 'LinAlgError: x'
        c2['definie'] = False
    elif 'c2def' in mauvais:
        c2['definie'] = False
    # energie
    el = -float(n1) + fr(w2) * n2
    de2d = R.choice([1, -1]) * R.uniform(1e-4, 5e-3) if R.random() > 0.02 else 0.0
    ecart = R.choice([0.0, 0.001, 0.0099999, 0.0100001, 0.02, -0.0099999, -0.0100001, -0.02, R.uniform(-0.01, 0.01)])
    de2 = de2d * (1.0 + ecart) if de2d != 0.0 else R.choice([0.0, 1e-4])
    if R.random() < 0.05:
        de2d, de2 = R.choice(EXACT_E)                      # l'ecart relatif d'energie vaut EXACTEMENT 0.01 en flottants (borne du gel, section 9)
    if refe is not None:
        de2d, de2 = 1.0e-3, refe
    c2['dE'] = [de2 * 1.5, de2 * 1.2, de2, de2 * 1.1]
    e = {'rang': rang, 'recouvrement': 0.03, 'E_re': el + de2d, 'E_libre': el, 'J_moyen': 0.0, 'J_ecart_type': sig, 'n1_moyen': n1, 'n2_moyen': n2, 'n1': n1, 'n2': n2,
         'poids_site': ps, 'poids_Fock_max': ps, 'Gamma_2D': {'2': g3 * f2, '3': g3, '4': g3 * f4}, 'suivi': {'2': sv2, '4': sv4}, 'chaine': ch}
    if 'c2abs' not in mauvais or R.random() < 0.7:
        e['chaine2'] = c2
    if not sain and R.random() < 0.10:
        if R.random() < 0.5:
            e['n1'] = -1
        else:
            e['n2'] = -1
    if 'neg1' in mauvais and R.random() < 0.3:
        e['Gamma_2D']['2'] = R.choice([0.0, -1e-9])
    return e


def sonde_alea(R):
    scen = R.choice(['tient', 'tient', 'proche_tombe', 'moyenne_tombe', 'lointaine_tombe', 'libre', 'libre', 'libre', 'bords', 'rares', 'rares'])
    rares = set(R.sample([k for k, v in PTS.items() if v[0] == 'juge'], R.choice([1, 2, 3, 3, 4]))) if scen == 'rares' else set()   # seuls ces points juges restent lisibles
    pas_sain = R.random() < (0.30 if scen == 'libre' else 0.10)
    psain = 0.80 if scen == 'libre' else 0.985
    ancre_mal = R.random() < 0.10                         # les ancres ne sont fautives que dans une sonde sur dix
    mal = [0.0] * 6 + [0.004, 0.0099999, -0.0099999] + ([0.0100001, 0.03] if ancre_mal else [])
    mal2 = [0.0] * 6 + [0.0005, 0.00099, -0.00099] + ([0.00101, 0.01] if ancre_mal else [])
    male = [0.0] * 6 + [5e-7, 9e-7, -9e-7] + ([1.1e-6, 1e-4] if ancre_mal else [])
    cible = {'tient': None, 'proche_tombe': 'proche', 'moyenne_tombe': 'moyenne', 'lointaine_tombe': 'lointaine'}.get(scen)
    id_tombe = R.choice([k for k, v in PTS.items() if v[0] == 'juge' and v[7] == cible]) if cible else None
    pts = []
    for pid, (role, w, f, st, d1, cm, N, bande) in PTS.items():
        a, b = f.split('/')
        g_regle = 10 ** R.uniform(-3, -2)
        B = BORNE.get(bande, 1.6)
        mode = 'dedans' if scen in ('tient', 'proche_tombe', 'moyenne_tombe', 'lointaine_tombe', 'rares') else ('bord' if scen == 'bords' else 'libre')
        q0 = 1.0 if R.random() < 0.5 else R.uniform(1.0, 0.9 * B)
        dup = R.random() < (0.20 if scen == 'libre' else 0.03)
        etats = [etat_alea(R, rang, 5 + rang // (2 if dup else 1), 2, w, B, q0, psain, mode) for rang in range(14)]
        if pid == id_tombe:                                   # un etat juge sort de la borne, par le haut ou par le bas
            k = R.randrange(14)
            hors = B * R.choice([1.02, 1.1, 1.5, 3.0])
            etats[k] = etat_alea(R, k, 5 + k, 2, w, B, q0, 1.0, 'dedans', q2_force=(hors if R.random() < 0.5 else 1.0 / hors))
            etats[k]['n1'], etats[k]['n2'] = 40 + k, 2
        if scen == 'rares' and role == 'juge' and pid not in rares:               # moins de 6 etats juges : le point est NON LISIBLE
            for rang in R.sample(range(14), 14 - R.choice([2, 3, 4, 5])):
                etats[rang]['Gamma_2D'] = {'2': 1e-13, '3': 1e-13, '4': 1e-13}
        if R.random() < (0.20 if scen == 'libre' else 0.06):
            for rang in R.sample(range(14), 14 - R.choice([4, 5, 6, 7, 8])):
                etats[rang]['Gamma_2D'] = {'2': 1e-13, '3': 1e-13, '4': 1e-13}
        if pid in REFS:
            (n1, n2, ref, ref2, refe) = REFS[pid]
            for rang in range(1, 14):
                etats[rang]['n1'], etats[rang]['n2'] = 20 + rang, 2
            etats[0] = etat_alea(R, 0, n1, n2, w, B, 1.0, 1.0, 'dedans', ref=ref * (1.0 + R.choice(mal)), ref2=ref2 * (1.0 + R.choice(mal2)), refe=refe * (1.0 + R.choice(male)))
            etats[0]['poids_site'] = 0.9
        gm = {'Omega_c': 1.0, 'D1': d1 + R.choice([0.0, 0.0, 4.9e-5, -4.9e-5]), 'c_max': cm + R.choice([0.0, 0.0, 4.9e-5, -4.9e-5]), 'site_c_max': 3, 'statut': st, 'erreur': None}
        p = {'id': pid, 'role': role, 'w2': w, 'facteur': f, 'g_regle': g_regle, 'g': g_regle * int(a) / int(b), 'faisable': True, 'etats': etats, 'garde_moteur': gm}
        if R.random() < (0.04 if scen == 'libre' else 0.01):
            p['faisable'] = False
        pts.append(p)
    s = {'moteur_canon': CAN_M, 'sonde_canon': CAN_S, 'points': pts}
    if R.random() < 0.12:
        s['points'] = [p for p in pts if p['id'] != R.choice(['W1', 'W2', 'W2'])]       # les temoins sont facultatifs
    if pas_sain:
        c = R.choice(['moteur', 'sonde', 'manque', 'g', 'g_fin', 'role', 'ancre_absent', 'ancre_double', 'n_etats', 'g6_statut', 'g6_D1', 'g6_cmax', 'g6_erreur',
                      'g6_absente', 'g6_bord_dedans', 'w2', 'fac', 'inconnu', 'doublon', 'g8_flux', 'g8_dE', 'g8_nondef', 'g4_flux', 'g4_infaisable', 'g8_erreur'])
        i = R.randrange(len(s['points']))
        P = s['points']
        if c == 'moteur':
            s['moteur_canon'] = '0000000000000000'
        elif c == 'sonde':
            s['sonde_canon'] = '0000000000000000'
        elif c == 'manque':
            s['points'] = [p for p in P if p['id'] != R.choice(['C1', 'L3', 'A1', 'A2', 'M4'])]
        elif c == 'g':
            P[i]['g'] *= 1.001
        elif c == 'g_fin':
            P[i]['g'] *= 1.0 + R.choice([5e-13, 2e-12])
        elif c == 'role':
            P[i]['role'] = 'juge' if P[i]['role'] != 'juge' else 'temoin'
        elif c == 'ancre_absent':
            for p in P:
                if p['id'] == 'A2':
                    p['etats'][0]['n1'] = 99
        elif c == 'ancre_double':
            ia = R.choice(['A1', 'A2'])
            (n1a, n2a) = REFS[ia][0:2]
            for p in P:
                if p['id'] == ia:
                    jd = R.randrange(1, 14)
                    p['etats'][jd]['n1'], p['etats'][jd]['n2'] = n1a, n2a
        elif c == 'n_etats':
            P[i]['etats'] = P[i]['etats'][:13]
        elif c == 'g6_statut':
            P[i]['garde_moteur']['statut'] = 'HORS DOMAINE' if P[i]['garde_moteur']['statut'] == 'EN DOMAINE' else 'EN DOMAINE'
        elif c == 'g6_D1':
            P[i]['garde_moteur']['D1'] = PTS[P[i]['id']][4] + R.choice([1e-4, -1e-4, 5.1e-5, -5.1e-5])
        elif c == 'g6_cmax':
            P[i]['garde_moteur']['c_max'] = PTS[P[i]['id']][5] + R.choice([1e-4, -1e-4, 5.1e-5, -5.1e-5])
        elif c == 'g6_erreur':
            P[i]['garde_moteur']['erreur'] = 'AssertionError: x'
        elif c == 'g6_absente':
            del P[i]['garde_moteur']
        elif c == 'g6_bord_dedans':
            P[i]['garde_moteur']['D1'] = PTS[P[i]['id']][4] + 4.9e-5
        elif c == 'w2':
            P[i]['w2'] = '1/2'
        elif c == 'fac':
            P[i]['facteur'] = '5/7'
        elif c == 'inconnu':
            import copy
            q = copy.deepcopy(P[0])
            q['id'] = 'Z9'
            P.append(q)
        elif c == 'doublon':
            import copy
            P.append(copy.deepcopy(P[i]))
        elif c in ('g8_flux', 'g8_dE', 'g8_nondef', 'g4_flux', 'g8_erreur'):
            for p in P:
                if p['id'] == R.choice(['A1', 'A2']):
                    e0 = p['etats'][0]
                    if c == 'g8_flux':
                        e0['chaine2']['gammas_flux'][2] *= R.choice([1.002, 0.998, 1.0005])
                    elif c == 'g8_dE':
                        e0['chaine2']['dE'][2] *= R.choice([1.00001, 0.99999, 1.0000001])
                    elif c == 'g8_nondef':
                        e0['chaine2']['definie'] = False
                    elif c == 'g8_erreur':
                        e0['chaine2']['erreur'] = 'X: y'
                    else:
                        e0['Gamma_2D']['3'] *= R.choice([1.02, 0.97, 1.005])
        elif c == 'g4_infaisable':
            for p in P:
                if p['id'] == R.choice(['A1', 'A2']):
                    p['faisable'] = False
    return s


def comparer(Fm, nsondes, graine=20261114):
    R = random.Random(graine)
    n_ecarts, repart, exemples = 0, {}, []
    for i in range(nsondes):
        s = sonde_alea(R)
        mien, rm = lecteur(s)
        try:
            theirs, sp = sien(Fm, s)
        except Exception as ex:
            theirs, sp = {'v': 'EXC:' + type(ex).__name__ + str(ex)[:60]}, {}
        repart[mien['v']] = repart.get(mien['v'], 0) + 1
        ok = (mien['v'] == theirs['v'])
        if ok and mien['v'] != 'NCI':
            for k in ('bandes', 'comp', 'ener', 'vnu'):
                if mien[k] != theirs[k]:
                    ok = False
            if sorted(mien['marge']) != sorted(theirs['marge']):
                ok = False
        if ok:
            for pid, d in rm.items():
                x = sp.get(pid)
                if x is None or x['statut'] != d['statut'] or x['nj'] != d['nj'] or x['motifs'] != d['motifs']:
                    ok = False
                    break
                if mien['v'] != 'NCI' and d['statut'] != 'NL':
                    for k in ('hors', 'snm', 'pal', 'comp', 'ener', 'q2', 'q1', 'pire', 'ecart_max', 'loi', 'fim'):
                        if not proche(d[k], x[k]):
                            ok = False
                            break
                if not ok:
                    break
        if not ok:
            n_ecarts += 1
            if len(exemples) < 4:
                exemples.append((i, mien['v'], theirs['v']))
    return n_ecarts, repart, exemples


MUT = [
    ('SIGMA_J_MAX = 0.2', 'SIGMA_J_MAX = 0.25'), ('POIDS_SITE_MIN = 0.5', 'POIDS_SITE_MIN = 0.45'), ('DIX_PLANCHERS = 1.33e-12', 'DIX_PLANCHERS = 1.0e-12'),
    ('SUIVI_MIN = 0.9', 'SUIVI_MIN = 0.8'), ('STABILITE_CIBLE = 2.0', 'STABILITE_CIBLE = 2.5'), ('ETALEMENT_CHAINE = 2.0', 'ETALEMENT_CHAINE = 3.0'),
    ('TOL_ENERGIE = 1e-2', 'TOL_ENERGIE = 2e-2'), ('MIN_JUGES = 6', 'MIN_JUGES = 5'), ('MIN_LISIBLES_BANDE = 3', 'MIN_LISIBLES_BANDE = 2'),
    ('PLANCHER = 1.33e-13', 'PLANCHER = 1.0e-13'), ('B_LOI = 2.87', 'B_LOI = 2.5'), ('N_ETATS = 14\n', 'N_ETATS = 13\n'), ('TOL_ANCRE = 1e-2', 'TOL_ANCRE = 2e-2'),
    ('TOL_ANCRE_O2 = 1e-3', 'TOL_ANCRE_O2 = 2e-3'), ('TOL_ANCRE_DE = 1e-6', 'TOL_ANCRE_DE = 1e-5'), ('TOL_GARDE = 5e-5', 'TOL_GARDE = 1e-4'),
    ('(PROCHE, 1.25, "0.06")', '(PROCHE, 1.3, "0.06")'), ('(MOYENNE, 1.6, "0.10")', '(MOYENNE, 1.7, "0.10")'), ('(LOINTAINE, 2.0, "0.12")', '(LOINTAINE, 2.1, "0.12")'),
    ('MOTEUR_CANON = "82a0be882568fe0c"', 'MOTEUR_CANON = "82a0be882568fe0d"'), ('SONDE_CANON = "24315c52b234319c"', 'SONDE_CANON = "24315c52b234319d"'),
    ('"C1": ("juge", "197/100", "2/3", PROCHE, EN, 0.031915, 0.039186)', '"C1": ("juge", "197/100", "2/3", PROCHE, EN, 0.031915, 0.039196)'),
    ('"M4": ("juge", "21/10", "3/4", MOYENNE, HORS, 0.100000, 0.130464)', '"M4": ("juge", "21/10", "3/4", MOYENNE, EN, 0.100000, 0.130464)'),
    ('"W2": ("temoin", "209/100", "1/2", None, HORS, 0.090000, 0.139955)', '"W2": ("temoin", "209/100", "1/2", None, HORS, 0.090000, 0.139965)'),
    ('"L3": ("juge", "211/100", "3/2", LOINTAINE, EN, 0.110000, 0.086367)', '"L3": ("juge", "211/100", "3/2", LOINTAINE, HORS, 0.110000, 0.086367)'),
    ('"C4": ("juge", "103/50", "4/3", PROCHE, EN, 0.060000, 0.046008)', '"C4": ("juge", "103/50", "4/3", MOYENNE, EN, 0.060000, 0.046008)'),
    ('"M2": ("juge", "48/25", "4/3", MOYENNE, EN, 0.095238, 0.069702)', '"M2": ("juge", "48/25", "3/4", MOYENNE, EN, 0.095238, 0.069702)'),
    ('"L1": ("juge", "189/100", "4/3", LOINTAINE, HORS, 0.141026, 0.102322)', '"L1": ("juge", "189/100", "4/3", LOINTAINE, HORS, 0.141026, 0.102312)'),
    ('"A2": ("ancre", "41/20", "1/1", None, EN, 0.050000, 0.051012)', '"A2": ("temoin", "41/20", "1/1", None, EN, 0.050000, 0.051012)'),
    ('"W1": ("temoin", "107/50", "1/1", None, HORS, 0.140000, 0.148692)', '"W1": ("ancre", "107/50", "1/1", None, HORS, 0.140000, 0.148692)'),
    ('2.1623273017950654e-10', '2.2623273017950654e-10'), ('2.3236497766513317e-10', '2.4236497766513317e-10'), ('0.002118984943055927', '0.003118984943055927'),
    ('-0.0028201377357584354', '-0.0038201377357584354'), ('2.6613925716641374e-09', '2.7613925716641374e-09'), ('"A1": ((7, 2), ', '"A1": ((7, 3), '),
    ('if not (e["J_ecart_type"] < SIGMA_J_MAX):', 'if not (e["J_ecart_type"] <= SIGMA_J_MAX):'), ('if e["n1"] < 0 or e["n2"] < 0:', 'if e["n1"] < 0:'),
    ('if not (e["poids_site"] >= POIDS_SITE_MIN):', 'if not (e["poids_site"] > POIDS_SITE_MIN):'), ('if not (g3 > DIX_PLANCHERS):', 'if not (g3 >= DIX_PLANCHERS):'),
    ('if min(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:', 'if max(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:'),
    ('gs = [e["Gamma_2D"][k] for k in ("2", "3", "4")]', 'gs = [e["Gamma_2D"][k] for k in ("3", "4")]'),
    ('if min(gs) <= 0 or max(gs) / min(gs) > STABILITE_CIBLE:', 'if min(gs) < 0 or max(gs) / min(gs) > STABILITE_CIBLE:'),
    ('if min(gs) <= 0 or max(gs) / min(gs) > STABILITE_CIBLE:', 'if min(gs) <= 0 or max(gs) / min(gs) >= STABILITE_CIBLE:'),
    ('if ch.get("erreur"):', 'if False:'), ('if ch.get("vide") or not ch.get("definie"):', 'if ch.get("vide"):'),
    ('if min(cg) <= 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:', 'if min(cg) < 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:'),
    ('if min(cg) <= 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:', 'if min(cg) <= 0 or max(cg) / min(cg) >= ETALEMENT_CHAINE:'),
    ('if c2.get("erreur"):', 'if False:'), ('if not c2.get("definie"):', 'if False:'),
    ('if min(fg) <= 0 or max(fg) / min(fg) > ETALEMENT_CHAINE:', 'if min(fg) < 0 or max(fg) / min(fg) > ETALEMENT_CHAINE:'),
    ('if min(fg) <= 0 or max(fg) / min(fg) > ETALEMENT_CHAINE:', 'if min(fg) <= 0 or max(fg) / min(fg) >= ETALEMENT_CHAINE:'),
    ('fg = c2["gammas_flux"]', 'fg = c2["gammas_flux"][:3]'), ('cg = ch["gammas"]', 'cg = ch["gammas"][:3]'),
    ('return (g3 - PLANCHER) / borne <= g2 <= borne * (g3 + PLANCHER)', 'return (g3 + PLANCHER) / borne <= g2 <= borne * (g3 + PLANCHER)'),
    ('return (g3 - PLANCHER) / borne <= g2 <= borne * (g3 + PLANCHER)', 'return (g3 - PLANCHER) / borne < g2 < borne * (g3 + PLANCHER)'),
    ('return (g3 - PLANCHER) / borne <= g2 <= borne * (g3 + PLANCHER)', 'return g3 / borne <= g2 <= borne * g3'),
    ('return (g3 - PLANCHER) / borne <= g2 <= borne * (g3 + PLANCHER)', 'return (g3 - PLANCHER) / borne <= g2 <= borne * (g3 - PLANCHER)'),
    ('for (_, borne, _) in BANDES:\n        if dans_borne(g2, g3, borne):', 'for (_, borne, _) in BANDES[::-1]:\n        if dans_borne(g2, g3, borne):'),
    ('return float(int(a)) / float(int(b))', 'return float(int(b)) / float(int(a))'),
    ('return 0.5 * (xs[(len(xs) - 1) // 2] + xs[len(xs) // 2])', 'return xs[len(xs) // 2]'),
    ('g1 = e["chaine"]["gammas"][2]', 'g1 = e["chaine"]["gammas"][1]'), ('g2 = c2["gammas_flux"][2]', 'g2 = c2["gammas_flux"][1]'),
    ('de_c2 = c2["dE"][2]', 'de_c2 = c2["dE"][1]'), ('de_2d = e["E_re"] - e["E_libre"]', 'de_2d = e["E_re"]'),
    ('ecart_e = abs(de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else float("inf")', 'ecart_e = abs(de_c2 - de_2d) / abs(de_c2) if de_2d != 0.0 else float("inf")'),
    ('ecart_e = abs(de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else float("inf")', 'ecart_e = (de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else float("inf")'),
    ('ecart_e = abs(de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else float("inf")', 'ecart_e = abs(de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else 0.0'),
    ('"energie_tenue": bool(ecart_e <= TOL_ENERGIE)', '"energie_tenue": bool(ecart_e < TOL_ENERGIE)'),
    ('delta = eval_fraction(pt["w2"]) - 2.0', 'delta = eval_fraction(pt["w2"]) + 2.0'),
    ('math.exp(B_LOI * delta * delta * c2["m_bord"])', 'math.exp(B_LOI * delta * delta * c2["m_min"])'),
    ('"flux_contre_im": abs(c2["gammas_im"][2] / g2 - 1.0)', '"flux_contre_im": abs(c2["gammas_im"][1] / g2 - 1.0)'),
    ('"flux_contre_im": abs(c2["gammas_im"][2] / g2 - 1.0)', '"flux_contre_im": abs(c2["gammas_im"][2] / g3 - 1.0)'),
    ('if len(juges) < MIN_JUGES:', 'if len(juges) <= MIN_JUGES:'),
    ('pire2 = max(abs(math.log(q)) for q in q2s)', 'pire2 = max(math.log(q) for q in q2s)'), ('pire1 = max(abs(math.log(q)) for q in q1s)', 'pire1 = max(math.log(q) for q in q1s)'),
    ('"MIEUX" if pire2 < pire1 else "PAS MIEUX"', '"MIEUX" if pire2 <= pire1 else "PAS MIEUX"'),
    ('("TENU" if all(x["dans_borne"] for x in juges) else "TOMBE")', '("TENU" if any(x["dans_borne"] for x in juges) else "TOMBE")'),
    ('("TENU" if all(x["dans_borne_nue"] for x in juges) else "TOMBE")', '("TENU" if any(x["dans_borne_nue"] for x in juges) else "TOMBE")'),
    ('if x["dans_borne"] and not x["dans_borne_nue"]]', 'if not x["dans_borne"] and x["dans_borne_nue"]]'),
    ('else max(paliers))', 'else min(paliers))'), ('"energie": ("TENUE" if all(x["energie_tenue"] for x in juges) else "NON TENUE")', '"energie": ("TENUE" if any(x["energie_tenue"] for x in juges) else "NON TENUE")'),
    ('"ecart_energie_max": max(x["ecart_energie"] for x in juges)', '"ecart_energie_max": min(x["ecart_energie"] for x in juges)'),
    ('if m is None and vus[(e["n1"], e["n2"])] > 1:', 'if m is None and vus[(e["n1"], e["n2"])] > 2:'), ('if m is None and vus[(e["n1"], e["n2"])] > 1:', 'if vus[(e["n1"], e["n2"])] > 1:'),
    ('if len(tr) != 1:', 'if len(tr) < 1:'), ('if ecart > TOL_ANCRE:', 'if ecart > 2 * TOL_ANCRE:'),
    ('if not c2.get("definie") or c2.get("erreur"):', 'if False:'),
    ('if abs(c2["gammas_flux"][2] / ref_o2 - 1.0) > TOL_ANCRE_O2:', 'if abs(c2["gammas_flux"][1] / ref_o2 - 1.0) > TOL_ANCRE_O2:'),
    ('if abs(c2["dE"][2] / ref_de - 1.0) > TOL_ANCRE_DE:', 'if abs(c2["dE"][1] / ref_de - 1.0) > TOL_ANCRE_DE:'),
    ('if p is None or not p.get("faisable"):', 'if p is None:'),
    ('if gm.get("statut") != statut:', 'if False:'), ('if gm.get("erreur"):', 'if False:'), ('if not isinstance(gm, dict):', 'if False:'),
    ('abs(gm["D1"] - d1) > TOL_GARDE or abs(gm["c_max"] - cmax) > TOL_GARDE', 'abs(gm["D1"] - d1) > TOL_GARDE and abs(gm["c_max"] - cmax) > TOL_GARDE'),
    ('abs(gm["c_max"] - cmax) > TOL_GARDE', 'abs(gm["c_max"] - d1) > TOL_GARDE'),
    ('if s.get("moteur_canon") != MOTEUR_CANON:', 'if False:'), ('if s.get("sonde_canon") != SONDE_CANON:', 'if False:'),
    ('if (p["role"], p["w2"], p["facteur"]) != (role, w2, fac):', 'if (p["w2"], p["facteur"]) != (w2, fac):'),
    ('if p.get("faisable") and len(p["etats"]) != N_ETATS:', 'if False:'),
    ('if abs(p["g"] - p["g_regle"] * eval_fraction(fac)) > 1e-12 * p["g_regle"]:', 'if abs(p["g"] - p["g_regle"] * eval_fraction(fac)) > 1e-9 * p["g_regle"]:'),
    ('obligatoires = [k for k in ATTENDUS if ATTENDUS[k][0] != "temoin"]', 'obligatoires = [k for k in ATTENDUS]'),
    ('if len(ids) != len(set(ids)) or any(k not in ATTENDUS for k in ids) or any(k not in pts for k in obligatoires):', 'if any(k not in ATTENDUS for k in ids) or any(k not in pts for k in obligatoires):'),
    ('motifs += garde_ancres(pts)', 'pass'),
    ('if len(lis) < MIN_LISIBLES_BANDE:', 'if len(lis) <= MIN_LISIBLES_BANDE:'),
    ('issue = "TENUE" if not tombes else "NON TENUE"', 'issue = "TENUE" if len(tombes) < 2 else "NON TENUE"'),
    ('tombes = sorted(x["id"] for x in lis if x[cle] == "TOMBE")', 'tombes = sorted(x["id"] for x in pts if x[cle] == "TOMBE")'),
    ('v = "L\'ORDRE 2 TIENT JUSQU\'A " + BANDES[i - 1][2]', 'v = "L\'ORDRE 2 TIENT JUSQU\'A " + BANDES[i][2]'),
    ('elif bandes[BANDES[0][0]]["issue"] == "NON LISIBLE":', 'elif bandes[BANDES[0][0]]["issue"] != "NON TENUE":'),
    ('juges = [par_id[k] for k in sorted(ATTENDUS) if ATTENDUS[k][0] == "juge"]', 'juges = [par_id[k] for k in sorted(ATTENDUS) if ATTENDUS[k][0] != "temoin"]'),
    ('pas_mieux = sorted(x["id"] for x in lis if x["comparaison"] != "MIEUX")', 'pas_mieux = sorted(x["id"] for x in juges if x["comparaison"] != "MIEUX")'),
    ('sans_energie = sorted(x["id"] for x in lis if x["energie"] != "TENUE")', 'sans_energie = sorted(x["id"] for x in lis if x["energie"] == "NON LISIBLE")'),
    ('v_nu, _ = lire_bandes(juges, "statut_sans_marge")', 'v_nu, _ = lire_bandes(juges, "statut")'),
    ('("NON LISIBLE" if not lis else\n                             ("L\'ORDRE 2 FAIT MIEUX PARTOUT" if not pas_mieux else "PAS PARTOUT"))', '("NON LISIBLE" if len(lis) < 4 else\n                             ("L\'ORDRE 2 FAIT MIEUX PARTOUT" if not pas_mieux else "PAS PARTOUT"))'),
    ('if not pt.get("faisable", False):', 'if False:'),
]


def main():
    Fm = charger(FEUILLE, 'feuille_m1')
    print('A. LECTEUR INDEPENDANT (gel 41153158190cf7f1, sections 4 a 10) CONTRE LA FEUILLE %s' % os.path.basename(FEUILLE))
    print('   tableau lu dans le texte du gel : %d points ; bornes %s ; seuils lus : sigma %s, poids %s, dix planchers %s, suivi %s, stabilite %s, plancher %s, energie %s, juges %d, lisibles %d' % (
        len(PTS), BORNE, SIGMA, POIDS, DIXP, SUIVI, STAB, PLANC, TOLE, MINJ, MINL))
    print('   canons lus : moteur %s, sonde %s ; G-4 %s ; G-8 %s' % (CAN_M, CAN_S, {k: v[2] for k, v in REFS.items()}, {k: v[3:] for k, v in REFS.items()}))
    ecarts_tab = []
    for pid, (r, w, f, st, d1, cm, N, bande) in PTS.items():
        a = Fm.ATTENDUS[pid]
        if not (a[0] == r and a[1] == w and a[2] == f and a[3] == bande and a[4] == st and abs(a[5] - d1) < 1e-12 and abs(a[6] - cm) < 1e-12):
            ecarts_tab.append(pid)
    ok_ref = all(Fm.ANCRES[k][0] == (v[0], v[1]) and Fm.ANCRES[k][1] == v[2] and Fm.ANCRES[k][2] == v[3] and Fm.ANCRES[k][3] == v[4] for k, v in REFS.items())
    ok_const = (Fm.SIGMA_J_MAX, Fm.POIDS_SITE_MIN, Fm.DIX_PLANCHERS, Fm.SUIVI_MIN, Fm.STABILITE_CIBLE, Fm.ETALEMENT_CHAINE, Fm.TOL_ENERGIE, Fm.MIN_JUGES, Fm.MIN_LISIBLES_BANDE,
                Fm.PLANCHER, Fm.B_LOI, Fm.TOL_ANCRE, Fm.TOL_ANCRE_O2, Fm.TOL_ANCRE_DE, Fm.TOL_GARDE, Fm.MOTEUR_CANON, Fm.SONDE_CANON, Fm.N_ETATS) == (
        SIGMA, POIDS, DIXP, SUIVI, STAB, STAB, TOLE, MINJ, MINL, PLANC, B_LOI, TOL_G4, TOL_G8, TOL_G8E, TOL_G6, CAN_M, CAN_S, 14)
    ok_bornes = [(b[0], b[1], b[2]) for b in Fm.BANDES] == [(b, BORNE[b], LIMITE[b]) for b in ORDRE_BANDES]
    print('   tableau de la feuille == tableau du gel, aux 16 points (role, w2, facteur, bande, garde, D1, c_max) : %s ; ecarts %s' % (not ecarts_tab, ecarts_tab))
    print('   references des ancres de la feuille == celles du gel (G-4 et G-8, etiquettes, Gamma_2D, Gamma d\'ordre 2, dE) : %s ; seuils et canons de la feuille == ceux du gel : %s ; '
          'bandes et bornes de la feuille == celles du gel : %s' % (ok_ref, ok_const, ok_bornes))
    ne, rep, ex = comparer(Fm, NSONDES)
    print('   %d sondes synthetiques aux bords des seuils ; verdicts du lecteur independant : %s' % (NSONDES, dict(sorted(rep.items()))))
    print('   ecarts feuille / lecteur : %d%s' % (ne, '' if ne == 0 else '  exemples ' + str(ex)))
    src = open(FEUILLE, encoding='ascii').read()
    if NMUT == 0:
        return
    print("B. MUTATIONS DE LA FEUILLE : %d alterations d'une ligne ; le selftest de machine 1 mord-il ? mon banc A (%d sondes) mord-il ?" % (len(MUT), NMUT))
    surv_selftest, surv_banc, surv_deux, absents = [], [], [], []
    for i, (a, b) in enumerate(MUT, 1):
        if src.count(a) < 1:
            print('   M%03d  MOTIF ABSENT : %s' % (i, a[:70]))
            absents.append(i)
            continue
        t = src.replace(a, b, 1)
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'feuille_mutee.py')
            open(p, 'w', encoding='ascii', newline='\n').write(t)
            try:
                rc = subprocess.run([sys.executable, '-P', p, '--selftest'], capture_output=True, text=True, timeout=300).returncode
            except subprocess.TimeoutExpired:
                rc = 99
            mord_self = (rc != 0)
            try:
                Fmu = charger(p, 'feuille_mutee_%d' % i)
                ne2, _, _ = comparer(Fmu, NMUT)
                mord_banc = ne2 > 0
            except Exception:
                mord_banc = True
        print('   M%03d  selftest m1 : %-8s  banc m2 : %-8s  %s  ->  %s' % (i, 'MORD' if mord_self else 'survit', 'MORD' if mord_banc else 'survit',
              a[:56].strip().replace('\n', ' '), b[:50].strip().replace('\n', ' ')), flush=True)
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
