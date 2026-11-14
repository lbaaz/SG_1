# -*- coding: ascii -*-
"""LECTURE PAR MACHINE 2 du resultat du run du gel "LA CHAINE E-A PAR ETAT, HORS PLAGE" (9df2702af59adbbc). ECRITE AVANT LE RUN.
Elle ne juge rien de nouveau : elle (1) recalcule des boites et des gardes du moteur SANS diagonalisation et les compare au JSON de la
sonde ; (2) dit le statut de la garde de domaine G-1 du moteur, point par point (ma reserve R-1) ; (3) relit les lectures declarees de la
section 9 du gel ; (4) note les annonces A-1 a A-8 de la section 10 ; (5) liste, par point, les etats et leur motif.
Usage : python -P lecture_resultat_chaine_par_etat_machine2_v1.py <moteur> <sonde.json> <verdict.json>"""
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


dire('LECTURE DE MACHINE 2 DU RUN (gel 9df2702af59adbbc ; sonde %s ; moteur %s)' % (S['sonde_canon'], S['moteur_canon']))
dire('plateforme : %s' % S['plateforme'])
dire('points joues : %s' % ' '.join(p['id'] for p in S['points']))
dire('durees (s) : %s' % ' '.join('%s %s' % (p['id'], p.get('duree_s')) for p in S['points']))
dire()
dire('1. BOITES ET REGLE g, RECALCULEES PAR MOI AVEC LE MOTEUR (aucune diagonalisation)')
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
    ok = (abs(p['g'] / g - 1) < 1e-12 and abs(p['g_regle'] / greg - 1) < 1e-12 and abs(p['s'] / s - 1) < 1e-12 and p['r_c'] == r_c
          and p['N'] == N and p['faisable'] == (N <= M.N_MAX_EB) and len(sites0) == p['card_barriere_graine'])
    bad += (not ok)
    dire('  %s w2=%s x%s : g %.6e s %.6f r_c %d N %d card %d ; JSON r_c %d N %d card %d -> %s' % (
        p['id'], p['w2'], p['facteur'], g, s, r_c, N, len(sites0), p['r_c'], p['N'], p['card_barriere_graine'], 'IDENTIQUE' if ok else 'ECART'))
dire('  ecarts : %d' % bad)
dire()
dire('2. GARDE DE DOMAINE G-1 DU MOTEUR (D1 <= 1/5, D2a <= 1/10), comme mesurer_point la calcule ; la sonde ne la consulte pas')
statut_g1 = {}
for p in S['points']:
    num, den = map(int, p['w2'].split('/'))
    w2 = F(num, den)
    Oc = M.Omega_du_canal(w2)[0]
    try:
        seuil = M.seuil_A4(w2, p['g'], lecture=M.LECTURE_OCCUPATIONS)
        gd = M.garde_domaine(w2, p['g'], seuil['S_det'], Oc)
        statut_g1[p['id']] = gd['statut']
        dire('  %s w2=%s x%s : D1 %.4f c_max %.4f (site %s) -> %s' % (p['id'], p['w2'], p['facteur'], gd['D1'], gd['c_max'], gd['site_c_max'], gd['statut']))
    except AssertionError as e:
        statut_g1[p['id']] = 'ARRET'
        dire('  %s : seuil_A4 arret : %s' % (p['id'], str(e)[:80]))
dire()
pts = {x['id']: x for x in V['points']}
dire('3. LECTURES DECLAREES (section 9 du gel) : verdict %s ; motifs %s' % (V['verdict'], V['motifs']))
for pid in [p['id'] for p in S['points']]:
    x = pts[pid]
    ex = {}
    for e in x['etats']:
        if e['exclu']:
            ex[e['exclu']] = ex.get(e['exclu'], 0) + 1
    if x['statut'] == 'NON LISIBLE':
        dire('  %s %-6s w2=%s x%s : NON LISIBLE (%s), %d juges ; exclus %s ; G-1 %s' % (pid, x['role'], x['w2'], x['facteur'], x['motif'], x['n_juges'], ex, statut_g1.get(pid)))
    else:
        dire('  %s %-6s w2=%s x%s : %s, %d juges, q min %.3f max %.3f median %.3f ; premier juge (%d,%d) q %.3f ; exclus %s ; G-1 %s' % (
            pid, x['role'], x['w2'], x['facteur'], x['statut'], x['n_juges'], x['q_min'], x['q_max'], x['q_median'], x['premier_juge']['n1'],
            x['premier_juge']['n2'], x['premier_juge']['q'], ex, statut_g1.get(pid)))
dire()
dire('4. ANNONCES DE LA SECTION 10 (jugees par machine 2 sur le verdict et le JSON de la feuille, sans seuil nouveau)')
verd = V['verdict']
proba = {'TENU EN PARTIE': 0.72, 'ORDRE DE GRANDEUR TENU HORS PLAGE': 0.17, "NON CONCLUANT D'INSTRUMENT": 0.05, 'NON LISIBLE': 0.03, 'NON TENU': 0.03}
dire('  A-1 verdict %s ; probabilite annoncee %.2f' % (verd, proba.get(verd, float('nan'))))
j2, j1 = pts['J2'], pts['J1']
dire('  A-2 (0.55) J2 est HORS DECADE : %s' % ('VRAIE' if j2['statut'] == 'HORS DECADE' else 'FAUSSE (J2 = %s)' % j2['statut']))
if j2['statut'] == 'NON LISIBLE':
    dire('  A-3 non jugee (J2 NON LISIBLE)')
else:
    q = j2['premier_juge']['q']
    dire('  A-3 (0.55) q du juge de plus grand recouvrement a J2 dans [2.3, 4.6] : q = %.3f -> %s' % (q, 'VRAIE' if 2.3 <= q <= 4.6 else 'FAUSSE'))
if j1['statut'] == 'NON LISIBLE':
    dire('  A-4 non jugee (J1 NON LISIBLE)')
else:
    q = j1['premier_juge']['q']
    dire('  A-4 (0.60) q du juge de plus grand recouvrement a J1 dans [0.70, 0.85] : q = %.3f -> %s' % (q, 'VRAIE' if 0.70 <= q <= 0.85 else 'FAUSSE'))
dire('  A-5 (0.40) J3 et J4 tous deux FACTEUR 2 : J3 %s, J4 %s -> %s' % (pts['J3']['statut'], pts['J4']['statut'],
     'VRAIE' if pts['J3']['statut'] == pts['J4']['statut'] == 'FACTEUR 2' else 'FAUSSE'))
lis = [pts[k] for k in ('J1', 'J2', 'J3', 'J4', 'J5', 'J6') if pts[k]['statut'] != 'NON LISIBLE']
if not lis:
    dire('  A-6 non jugee (aucun point juge lisible)')
else:
    viol = []
    for x in lis:
        num, den = map(int, x['w2'].split('/'))
        w = num / den
        if (w < 2 and not x['q_median'] < 1) or (w > 2 and not x['q_median'] > 1):
            viol.append('%s (w2 %s, q median %.3f)' % (x['id'], x['w2'], x['q_median']))
    dire('  A-6 (0.75) signe du q median (sous 1 si w2 < 2, au-dessus si w2 > 2) : %s' % ('VRAIE' if not viol else 'FAUSSE : ' + ' ; '.join(viol)))
dire('  A-7 (0.65) J5 est lisible : %s' % ('VRAIE' if pts['J5']['statut'] != 'NON LISIBLE' else 'FAUSSE'))
g4 = [m for m in V['motifs'] if m.startswith('G-4')]
dire('  A-8 (0.95) la garde G-4 tient : %s' % ('VRAIE' if not g4 else 'FAUSSE : %s' % g4))
dire()
dire('5. ETATS (rang, etiquette, Gamma_2D(3), q ou motif) -- consigne, non juge')
for pid in [p['id'] for p in S['points']]:
    x = pts[pid]
    dire('  %s :' % pid)
    for e in x['etats']:
        if e['exclu']:
            dire('     rang %2d (%d,%d) Gamma_2D(3) %.4e exclu : %s' % (e['rang'], e['n1'], e['n2'], e['Gamma_2D'], e['exclu']))
        else:
            dire('     rang %2d (%d,%d) Gamma_2D(3) %.4e chaine %.4e q %.3f %s' % (e['rang'], e['n1'], e['n2'], e['Gamma_2D'], e['Gamma_chaine'], e['q'], e['palier']))
dire()
dire('BILAN DE MA LECTURE : %d ecart(s) de boite/regle entre le JSON de la sonde et mon recalcul' % bad)
