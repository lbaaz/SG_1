# -*- coding: ascii -*-
"""LECTURE PAR MACHINE 2 du resultat du run du gel "LA CHAINE E-A AU SECOND ORDRE" (41153158190cf7f1). ECRITE AVANT LE RUN.
Elle ne juge rien de nouveau : elle (1) recalcule, SANS diagonalisation, les boites, la regle g et la garde G-1 du moteur aux points joues et les compare au JSON de la
sonde ; (2) relit les lectures declarees de la section 11 du gel ; (3) note les annonces A-1 a A-15 de la section 12, sur le verdict et le JSON de la feuille, SANS seuil
nouveau : les seuils sont ceux que chaque annonce ecrit (1.5, 1.9, 1.35, 1.55, 0.95, 0.93, 1.15, 1.6, 2.5, 0.05, 0.006) ; une annonce qui nomme un point NON LISIBLE
est non jugee (gel, section 12) ; (4) liste, par point, les etats et leur motif. Elle ne rejoue aucun point et ne relit sous aucun autre palier (gel, section 14).
Usage : python -P ordre2/lecture_resultat_ordre2_machine2_v1.py <moteur> <sonde.json> <verdict.json>"""
import importlib.util
import json
import math
import sys
from fractions import Fraction as F

spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
S = json.load(open(sys.argv[2], encoding='ascii'))
V = json.load(open(sys.argv[3], encoding='ascii'))
bad = 0


def dire(s=''):
    print(s, flush=True)


dire('LECTURE DE MACHINE 2 DU RUN (gel 41153158190cf7f1 ; sonde %s ; moteur %s)' % (S['sonde_canon'], S['moteur_canon']))
dire('plateforme : %s' % S['plateforme'])
dire('points joues : %s' % ' '.join(p['id'] for p in S['points']))
dire('durees (s) : %s ; total %.0f' % (' '.join('%s %s' % (p['id'], p.get('duree_s')) for p in S['points']), sum(p.get('duree_s') or 0 for p in S['points'])))
dire()
dire('1. BOITES, REGLE g ET GARDE G-1 DU MOTEUR, RECALCULEES PAR MOI AVEC LE MOTEUR (aucune diagonalisation), contre le JSON de la sonde')
for p in S['points']:
    num, den = map(int, p['w2'].split('/'))
    w2 = F(num, den)
    fa, fb = map(int, p['facteur'].split('/'))
    greg = float(M.g_du_point(w2))
    g = greg * float(F(fa, fb))
    s = 0.70 * M.s_ff(w2, g)
    n1, n2 = M.appariement(s, w2)
    sites0 = M.barriere(n1, n2, w2, g, True)
    m2b = sites0[-1][0] if sites0 else 0
    r_c = int(math.ceil(n1)) + 2 * (m2b + max(8, m2b)) + 2
    N = r_c + 20
    Oc = M.Omega_du_canal(w2)[0]
    gd = M.garde_domaine(w2, g, M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"], Oc)
    gm = p.get('garde_moteur') or {}
    ok = (abs(p['g'] / g - 1) < 1e-12 and abs(p['g_regle'] / greg - 1) < 1e-12 and abs(p['s'] / s - 1) < 1e-12 and p['r_c'] == r_c and p['N'] == N
          and p['faisable'] == (N <= M.N_MAX_EB) and len(sites0) == p['card_barriere_graine']
          and gm.get('statut') == gd['statut'] and abs(gm.get('D1', 9) - float(gd['D1'])) < 1e-12 and abs(gm.get('c_max', 9) - float(gd['c_max'])) < 1e-12)
    bad += (not ok)
    dire('  %s w2=%s x%s : g %.6e r_c %d N %d ; garde recalculee %s D1 %.6f c_max %.6f ; JSON r_c %d N %d garde %s D1 %.6f c_max %.6f -> %s' % (
        p['id'], p['w2'], p['facteur'], g, r_c, N, gd['statut'], gd['D1'], gd['c_max'], p['r_c'], p['N'], gm.get('statut'), gm.get('D1', float('nan')),
        gm.get('c_max', float('nan')), 'IDENTIQUE' if ok else 'ECART'))
dire('  ecarts : %d' % bad)
dire()
pts = {x['id']: x for x in V['points']}
dire('2. LECTURES DECLAREES (section 11 du gel) : verdict %s ; motifs %s' % (V['verdict'], V['motifs']))
for pid in [p['id'] for p in S['points']]:
    x = pts[pid]
    ex = {}
    for e in x['etats']:
        if e['exclu']:
            ex[e['exclu']] = ex.get(e['exclu'], 0) + 1
    if x['statut'] == 'NON LISIBLE':
        dire('  %s %-6s w2=%s x%s garde %s : NON LISIBLE (%s), %d juges ; exclus %s' % (pid, x['role'], x['w2'], x['facteur'], x['garde_moteur'], x['motif'], x['n_juges'], ex))
    else:
        dire('  %s %-6s w2=%s x%s bande %s garde %s : %s %d juges ; q2 %.3f %.3f %.3f ; q1 %.3f %.3f %.3f ; pire o2 %.3f o1 %.3f %s ; energie %.2e %s ; palier %s ; q2/loi %.3f ; flux/im %.1e ; sans marge %s ; exclus %s' % (
            pid, x['role'], x['w2'], x['facteur'], x['bande'], x['garde_moteur'], x['statut'], x['n_juges'], x['q2_min'], x['q2_median'], x['q2_max'], x['q1_min'], x['q1_median'],
            x['q1_max'], x['pire_ordre2'], x['pire_ordre1'], x['comparaison'], x['ecart_energie_max'], x['energie'], x['palier'], x['q2_sur_loi_median'], x['flux_contre_im_max'],
            x['statut_sans_marge'], ex))
if 'bandes' in V:
    for nom in ('proche', 'moyenne', 'lointaine'):
        b = V['bandes'][nom]
        dire('  bande %-9s (|delta| <= %s, borne %s) : %-11s %d lisibles ; tombes : %s' % (nom, b['limite'], b['borne'], b['issue'], b['lisibles'], ' '.join(b['tombes']) or 'aucun'))
    dire('  comparaison au pire etat : %s ; pas mieux : %s' % (V['comparaison']['issue'], V['comparaison']['pas_mieux']))
    dire('  energies : %s ; non tenue : %s' % (V['energie']['issue'], V['energie']['non_tenue']))
    dire('  lecture SANS MARGE (declaree) : %s ; etats gardes par la marge : %s' % (V['verdict_sans_marge'], V['gardes_par_la_marge']))
dire()
dire('3. ANNONCES DE LA SECTION 12 (jugees par machine 2 sur le verdict et le JSON de la feuille, sans seuil nouveau)')
verd = V['verdict']
proba = {"L'ORDRE 2 TIENT": 0.45, "L'ORDRE 2 TIENT JUSQU'A 0.10": 0.27, "L'ORDRE 2 TIENT JUSQU'A 0.06": 0.10, "L'ORDRE 2 NE TIENT PAS": 0.08, 'NON LISIBLE': 0.04,
         "NON CONCLUANT D'INSTRUMENT": 0.06}
dire('  A-1 verdict %s ; probabilite annoncee %.2f' % (verd, proba.get(verd, float('nan'))))
if V.get('motifs'):
    dire('  (le verdict est NON CONCLUANT : les annonces A-2 a A-14 ne sont pas jugees)')


def nl(pid):
    return pid not in pts or pts[pid]['statut'] == 'NON LISIBLE'


def juges(pid):
    return [e for e in pts[pid]['etats'] if not e['exclu']]


def une(nom, p, cond_pts, f, txt):
    if V.get('motifs'):
        dire('  %s (%.2f) %s : NON JUGEE (NON CONCLUANT D\'INSTRUMENT)' % (nom, p, txt))
    elif any(nl(k) for k in cond_pts):
        dire('  %s (%.2f) %s : NON JUGEE (un point nomme est NON LISIBLE ou absent)' % (nom, p, txt))
    else:
        dire('  %s (%.2f) %s : %s' % (nom, p, txt, 'VRAIE' if f() else 'FAUSSE'))


LJ = [k for k in pts if pts[k]['role'] == 'juge']
une('A-2', 0.85, [], lambda: V['bandes']['proche']['issue'] == 'TENUE', 'la bande PROCHE est TENUE')
une('A-3', 0.80, [], lambda: V['bandes']['moyenne']['issue'] == 'TENUE', 'la bande MOYENNE est TENUE')
une('A-4', 0.60, [], lambda: V['bandes']['lointaine']['issue'] == 'TENUE', 'la bande LOINTAINE est TENUE')
une('A-5', 0.70, ['L2'], lambda: pts['L2']['statut'] == 'TENU', 'L2 est TENU')
if not V.get('motifs') and not nl('L2') and pts['L2']['statut'] == 'TOMBE':
    hors = [e for e in juges('L2') if not e['dans_borne']]
    dire('       L2 est tombe : etats hors de la borne %s (q2 %s) ; trop BAS (q2 < 1) pour tous : %s (annonce : 0.80 que ce soit par un etat trop bas)' % (
        [(e['n1'], e['n2']) for e in hors], ['%.3f' % e['q2'] for e in hors], all(e['q2'] < 1 for e in hors)))
une('A-6', 0.80, ['L4'], lambda: pts['L4']['statut'] == 'TENU', 'L4 est TENU')
une('A-6b', 0.65, ['L4'], lambda: 1.5 <= pts['L4']['q2_max'] <= 1.9, 'a L4 le plus grand q2 est entre 1.5 et 1.9')
une('A-7', 0.80, ['M4'], lambda: pts['M4']['statut'] == 'TENU', 'M4 est TENU')
une('A-7b', 0.65, ['M4'], lambda: 1.35 <= pts['M4']['q2_max'] <= 1.55, 'a M4 le plus grand q2 est entre 1.35 et 1.55')
if not V.get('motifs'):
    dire('  A-8 (0.85) L\'ORDRE 2 FAIT MIEUX PARTOUT : %s (%s)' % ('VRAIE' if V['comparaison']['issue'] == "L'ORDRE 2 FAIT MIEUX PARTOUT" else 'FAUSSE ou NON LISIBLE', V['comparaison']['issue']))
    dire('  A-9 (0.90) L\'ENERGIE TIENT : %s (%s)' % ('VRAIE' if V['energie']['issue'] == "L'ENERGIE TIENT" else 'FAUSSE ou NON LISIBLE', V['energie']['issue']))
LJL = [k for k in LJ if not nl(k)]
if not V.get('motifs') and LJL:
    mx = max(pts[k]['ecart_energie_max'] for k in LJL)
    dire('  A-9b (0.70) le plus grand ecart d energie des points juges est < 0.006 : %s (%.4f, au point %s)' % ('VRAIE' if mx < 0.006 else 'FAUSSE', mx, max(LJL, key=lambda k: pts[k]['ecart_energie_max'])))
    viol = [(k, pts[k]['q2_min']) for k in LJL if not pts[k]['q2_min'] >= 0.95]
    dire('  A-10 (0.70) a chaque point juge lisible le plus petit q2 est >= 0.95 : %s %s' % ('VRAIE' if not viol else 'FAUSSE', viol))
    viol = [(k, round(pts[k]['q2_sur_loi_median'], 3)) for k in LJL if not 0.93 <= pts[k]['q2_sur_loi_median'] <= 1.15]
    dire('  A-11 (0.60) a chaque point juge lisible la mediane de q2 / loi est entre 0.93 et 1.15 : %s %s' % ('VRAIE' if not viol else 'FAUSSE', viol))
    viol = [(k, round(pts[k]['flux_contre_im_max'], 4)) for k in LJL if not pts[k]['flux_contre_im_max'] < 0.05]
    dire('  A-14 (0.65) a chaque point juge lisible -2 Im E et Gamma_flux different de moins de 0.05 en relatif : %s %s' % ('VRAIE' if not viol else 'FAUSSE', viol))
if not V.get('motifs'):
    if nl('W1'):
        dire('  A-12 (0.75 ; 0.70) W1 : NON JUGEE (W1 est NON LISIBLE ou absent)')
    else:
        jw = juges('W1')
        hors16 = [e for e in jw if e['palier'] is None or e['palier'] > 1.6]
        dire('  A-12 (0.75) W1 a un etat juge hors de 1.6 : %s (%d etats, q2 de %.3f a %.3f ; etats hors du palier 1.6 : %s)' % (
            'VRAIE' if hors16 else 'FAUSSE', len(jw), min(e['q2'] for e in jw), max(e['q2'] for e in jw), [(e['n1'], e['n2'], round(e['q2'], 3)) for e in hors16]))
        dire('  A-12b (0.70) tous les etats juges de W1 sont sous 2.5 : %s (plus grand q2 %.3f)' % ('VRAIE' if all(e['q2'] < 2.5 for e in jw) else 'FAUSSE', max(e['q2'] for e in jw)))
    if 'W2' not in pts:
        dire('  A-13 (0.65) W2 est joue et lisible : FAUSSE (W2 n est pas joue)')
    elif nl('W2'):
        dire('  A-13 (0.65) W2 est joue et lisible : FAUSSE (W2 est joue mais NON LISIBLE : %s)' % pts['W2'].get('motif'))
    else:
        dire('  A-13 (0.65) W2 est joue et lisible : VRAIE')
        dire('  A-13b (0.60) tous les q2 de W2 sont sous 1.6 : %s (plus grand q2 %.3f)' % ('VRAIE' if pts['W2']['q2_max'] < 1.6 else 'FAUSSE', pts['W2']['q2_max']))
        dire('  A-13c (0.80) W2 est MIEUX : %s' % ('VRAIE' if pts['W2']['comparaison'] == 'MIEUX' else 'FAUSSE'))
g4 = [m for m in V['motifs'] if m.startswith('G-4')]
g8 = [m for m in V['motifs'] if m.startswith('G-8')]
g6 = [m for m in V['motifs'] if m.startswith('G-6')]
dire('  A-15 (0.95) la garde G-4 tient : %s ; (0.93) la garde G-8 tient : %s ; (0.97) la garde G-6 tient : %s' % (
    'VRAIE' if not g4 else 'FAUSSE : %s' % g4, 'VRAIE' if not g8 else 'FAUSSE : %s' % g8, 'VRAIE' if not g6 else 'FAUSSE : %s' % g6))
dire()
dire('4. ETATS (rang, etiquette, Gamma_2D(3), q1, q2 ou motif) -- consigne, non juge')
for pid in [p['id'] for p in S['points']]:
    x = pts[pid]
    dire('  %s :' % pid)
    for e in x['etats']:
        if e['exclu']:
            dire('     rang %2d (%d,%d) Gamma_2D(3) %.4e exclu : %s' % (e['rang'], e['n1'], e['n2'], e['Gamma_2D'], e['exclu']))
        else:
            dire('     rang %2d (%d,%d) Gamma_2D(3) %.4e q1 %.3f q2 %.3f palier %s dE_2D %.4e dE_2 %.4e ecart %.4f %s' % (
                e['rang'], e['n1'], e['n2'], e['Gamma_2D'], e['q1'], e['q2'], e['palier'], e['dE_2D'], e['dE_ordre2'], e['ecart_energie'],
                '' if e['dans_borne'] is None else ('DANS' if e['dans_borne'] else 'HORS')))
dire()
dire('BILAN DE MA LECTURE : %d ecart(s) de boite, de regle ou de garde entre le JSON de la sonde et mon recalcul' % bad)
