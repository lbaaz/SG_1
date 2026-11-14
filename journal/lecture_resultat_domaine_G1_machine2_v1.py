# -*- coding: ascii -*-
"""LECTURE PAR MACHINE 2 du resultat du run du gel "LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT" (b59651f99e60707a). ECRITE AVANT LE RUN.
Elle ne juge rien de nouveau : elle (1) recalcule, SANS diagonalisation, les boites et la garde G-1 du moteur aux quatorze points et les compare au JSON
de la sonde ; (2) relit les lectures declarees de la section 10 du gel ; (3) note les annonces A-1 a A-13 de la section 11, sur le verdict et le JSON de la
feuille, sans seuil nouveau ; (4) liste, par point, les etats et leur motif. Elle ne rejoue aucun point et ne relit sous aucun autre palier (gel, section 13).
Usage : python -P domaine_G1/lecture_resultat_domaine_G1_machine2_v1.py <moteur> <sonde.json> <verdict.json>"""
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


dire('LECTURE DE MACHINE 2 DU RUN (gel b59651f99e60707a ; sonde %s ; moteur %s)' % (S['sonde_canon'], S['moteur_canon']))
dire('plateforme : %s' % S['plateforme'])
dire('points joues : %s' % ' '.join(p['id'] for p in S['points']))
dire('durees (s) : %s' % ' '.join('%s %s' % (p['id'], p.get('duree_s')) for p in S['points']))
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
dire('2. LECTURES DECLAREES (section 10 du gel) : verdict %s ; motifs %s' % (V['verdict'], V['motifs']))
for pid in [p['id'] for p in S['points']]:
    x = pts[pid]
    ex = {}
    for e in x['etats']:
        if e['exclu']:
            ex[e['exclu']] = ex.get(e['exclu'], 0) + 1
    if x['statut'] == 'NON LISIBLE':
        dire('  %s %-5s w2=%s x%s garde %s : NON LISIBLE (%s), %d juges ; exclus %s' % (pid, x['role'], x['w2'], x['facteur'], x['garde_moteur'], x['motif'], x['n_juges'], ex))
    else:
        dire('  %s %-5s w2=%s x%s garde %s : %s %s, %d juges, q min %.3f max %.3f median %.3f ; premier juge (%d,%d) q %.3f ; exclus %s' % (
            pid, x['role'], x['w2'], x['facteur'], x['garde_moteur'], x['statut'], x['classe'], x['n_juges'], x['q_min'], x['q_max'], x['q_median'],
            x['premier_juge']['n1'], x['premier_juge']['n2'], x['premier_juge']['q'], ex))
if 'paires' in V:
    dire('  paires : ' + ' ; '.join('%s %s' % (k, V['paires'][k]) for k in sorted(V['paires'])))
    dire('  a (EN DOMAINE tombes) %s, b (HORS DOMAINE tenus) %s, EN lisibles %s, HORS lisibles %s ; rivale %s' % (
        V['a_EN_tombes'], V['b_HORS_tenus'], V['EN_lisibles'], V['HORS_lisibles'], V['rivale']))
    for k in sorted(V['paires']):
        pass
dire()
dire('3. ANNONCES DE LA SECTION 11 (jugees par machine 2 sur le verdict et le JSON de la feuille, sans seuil nouveau)')
verd = V['verdict']
proba = {'LA GARDE NE TIENT PAS': 0.74, 'LA GARDE SUFFIT': 0.10, 'LA GARDE SEPARE': 0.03, 'NON LISIBLE': 0.07, "NON CONCLUANT D'INSTRUMENT": 0.06}
dire('  A-1 verdict %s ; probabilite annoncee %.2f' % (verd, proba.get(verd, float('nan'))))


def nl(pid):
    return pts[pid]['statut'] == 'NON LISIBLE'


def une(nom, p, cond_pts, f, txt):
    if any(nl(k) for k in cond_pts):
        dire('  %s (%.2f) %s : NON JUGEE (un point nomme est NON LISIBLE)' % (nom, p, txt))
    else:
        dire('  %s (%.2f) %s : %s' % (nom, p, txt, 'VRAIE' if f() else 'FAUSSE'))


une('A-2', 0.75, ['E3'], lambda: pts['E3']['statut'] == 'HORS DECADE', 'E3 est HORS DECADE')
une('A-3', 0.85, ['E4'], lambda: pts['E4']['statut'] == 'HORS DECADE', 'E4 est HORS DECADE')
une('A-4', 0.55, ['E2'], lambda: pts['E2']['statut'] == 'HORS DECADE', 'E2 est HORS DECADE')
une('A-5', 0.75, ['E1'], lambda: pts['E1']['statut'] == 'DECADE', 'E1 est DECADE')
une('A-6', 0.70, ['H1'], lambda: pts['H1']['classe'] == 'TENU', 'H1 est TENU')
une('A-7', 0.75, ['H6'], lambda: pts['H6']['classe'] == 'TENU', 'H6 est TENU')
if 'rivale' in V and V['rivale'] != 'NON LISIBLE':
    dire('  A-8 (0.40) la rivale est TENUE : %s' % ('VRAIE' if V['rivale'] == 'TENUE' else 'FAUSSE'))
else:
    dire('  A-8 (0.40) la rivale est TENUE : NON JUGEE (rivale NON LISIBLE ou verdict non lu)')
une('A-9', 0.60, ['E3'], lambda: 3.0 <= pts['E3']['q_median'] <= 4.5, 'a E3 le q median est entre 3.0 et 4.5')
une('A-10', 0.80, ['E5', 'E6'], lambda: pts['E5']['classe'] == 'TENU' and pts['E6']['classe'] == 'TENU', 'E5 et E6 sont tous les deux TENUS')
hd45 = [k for k in ('H4', 'H5') if pts[k]['statut'] == 'HORS DECADE']
if hd45:
    dire('  A-11 (0.50) H4 ou H5, l un au moins, est HORS DECADE : VRAIE (%s)' % ', '.join(hd45))
elif any(nl(k) for k in ('H4', 'H5')):
    dire('  A-11 (0.50) H4 ou H5, l un au moins, est HORS DECADE : NON JUGEE (aucun HORS DECADE et l un des deux NON LISIBLE)')
else:
    dire('  A-11 (0.50) H4 ou H5, l un au moins, est HORS DECADE : FAUSSE')
viol = []
for k in ('E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6'):
    x = pts[k]
    if x['statut'] == 'NON LISIBLE':
        continue
    num, den = map(int, x['w2'].split('/'))
    w = num / den
    if (w < 2 and not x['q_median'] < 1) or (w > 2 and not x['q_median'] > 1):
        viol.append('%s (w2 %s, q median %.3f)' % (k, x['w2'], x['q_median']))
dire('  A-12 (0.85) signe du q median aux points juges lisibles : %s' % ('VRAIE' if not viol else 'FAUSSE : ' + ' ; '.join(viol)))
g4 = [m for m in V['motifs'] if m.startswith('G-4')]
g6 = [m for m in V['motifs'] if m.startswith('G-6')]
dire('  A-13 (0.95) la garde G-4 tient : %s ; (0.97) la garde G-6 tient : %s' % ('VRAIE' if not g4 else 'FAUSSE : %s' % g4, 'VRAIE' if not g6 else 'FAUSSE : %s' % g6))
dire()
dire('4. ETATS (rang, etiquette, Gamma_2D(3), q ou motif) -- consigne, non juge')
for pid in [p['id'] for p in S['points']]:
    x = pts[pid]
    dire('  %s :' % pid)
    for e in x['etats']:
        if e['exclu']:
            dire('     rang %2d (%d,%d) Gamma_2D(3) %.4e exclu : %s' % (e['rang'], e['n1'], e['n2'], e['Gamma_2D'], e['exclu']))
        else:
            dire('     rang %2d (%d,%d) Gamma_2D(3) %.4e chaine %.4e q %.3f %s' % (e['rang'], e['n1'], e['n2'], e['Gamma_2D'], e['Gamma_chaine'], e['q'], e['palier']))
dire()
dire('BILAN DE MA LECTURE : %d ecart(s) de boite, de regle ou de garde entre le JSON de la sonde et mon recalcul' % bad)
