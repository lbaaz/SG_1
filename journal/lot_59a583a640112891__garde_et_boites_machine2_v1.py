# -*- coding: ascii -*-
"""Recalcul par machine 2, SANS aucune diagonalisation, de ce que le gel 41153158190cf7f1 ("la chaine E-A au second ordre") ecrit sur la garde G-1 du moteur et
sur les boites, aux SEIZE points de la section 4 : g, graine, boite (r_c, N), faisabilite, garde G-1 (D1, c_max, site, statut), comme mesurer_point la calcule
(seuil_A4 en lecture reelle, puis garde_domaine avec Omega_du_canal) ; comparees, a six decimales, a la table du gel (LUE DANS LE TEXTE DU GEL). Lit aussi dans
la table le desaccord delta = w2 - 2 et la bande, et les recalcule. Imprime en plus D1 et c_max a tous les chiffres (repr), pour comparer deux nombres de fils.
Usage (depuis BOCAL4) : python -P ordre2/garde_et_boites_machine2_v1.py <moteur> <gel.md>"""
import importlib.util
import math
import os
import re
import sys
from fractions import Fraction as F

spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
GEL = open(sys.argv[2], encoding='ascii').read()
bad = 0


def dire(s=''):
    print(s, flush=True)


dire('fils : %s' % {k: os.environ.get(k) for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS')})
# ---- la table du gel, lue dans son texte (section 4) : id, w2, facteur, delta, D1, c_max, statut, N ; la bande est celle du titre de groupe
TAB, BANDE = {}, {}
cour = None
for ln in GEL.split('\n'):
    s = ln.strip()
    mb = re.match(r'^JUGES, bande (PROCHE|MOYENNE|LOINTAINE)', s)
    if mb:
        cour = mb.group(1)
    elif s.startswith('ANCRES'):
        cour = 'ANCRE'
    elif s.startswith('TEMOINS'):
        cour = 'TEMOIN'
    m = re.match(r'^(C\d|M\d|L\d|A\d|W\d)\s+w2 = (\d+/\d+)\s+facteur (\S+)\s+delta ([+-][0-9.]+)\s+D1 ([0-9.]+)\s+c_max ([0-9.]+)\s+(EN DOMAINE|HORS DOMAINE)\s+N (\d+)$', s)
    if m and cour:
        TAB[m.group(1)] = (m.group(2), m.group(3), m.group(4), m.group(5), m.group(6), m.group(7), int(m.group(8)))
        BANDE[m.group(1)] = cour
assert len(TAB) == 16 and len(BANDE) == 16, len(TAB)
LIM = {'PROCHE': F(6, 100), 'MOYENNE': F(10, 100), 'LOINTAINE': F(12, 100)}


def bande_de(delta):
    d = abs(delta)
    for nom in ('PROCHE', 'MOYENNE', 'LOINTAINE'):
        if d <= LIM[nom]:
            return nom
    return None


def calc(w2, fac):
    g = float(M.g_du_point(w2)) * float(fac)
    s = 0.70 * M.s_ff(w2, g)
    n1, n2 = M.appariement(s, w2)
    sites0 = M.barriere(n1, n2, w2, g, True)
    m2b = sites0[-1][0] if sites0 else 0
    r_c = int(math.ceil(n1)) + 2 * (m2b + max(8, m2b)) + 2
    N = r_c + 20
    Oc = M.Omega_du_canal(w2)[0]
    gd = M.garde_domaine(w2, g, M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"], Oc)
    return g, (n1, n2), r_c, N, gd, m2b, len(sites0)


dire('LES SEIZE POINTS : garde G-1 et boite, recalculees par moi, contre la table du gel (section 4), a six decimales ; delta et bande recalcules')
for pid in TAB:
    w, f, dl, d1t, cmt, st, Nt = TAB[pid]
    w2, fac = F(w), F(f)
    g, gr, r_c, N, gd, m2b, card = calc(w2, fac)
    delta = w2 - 2
    delta_ok = ('%+.2f' % float(delta)) == dl
    bd = bande_de(delta)
    bande_ok = (BANDE[pid] == bd) if BANDE[pid] in LIM else (BANDE[pid] in ('ANCRE', 'TEMOIN'))
    ok = ('%.6f' % gd['D1'] == d1t and '%.6f' % gd['c_max'] == cmt and N == Nt and gd['statut'] == st and delta_ok and bande_ok)
    ok = ok and (N <= M.N_MAX_EB)
    bad += (not ok)
    dire('  %s %-9s w2=%-8s x%-4s delta %+.2f (gel %s) bande %-9s g %.6e graine (%.3f, %.3f) m_bord %d r_c %d N %d (gel %d) ; D1 %.6f (gel %s) c_max %.6f (gel %s) site %s %s (gel %s) -> %s' % (
        pid, BANDE[pid], w, f, float(delta), dl, bd or '(hors bandes)', g, gr[0], gr[1], m2b, r_c, N, Nt, gd['D1'], d1t, gd['c_max'], cmt, gd['site_c_max'], gd['statut'], st,
        'IDENTIQUE' if ok else 'ECART'))
dire('TOUS CHIFFRES (repr), pour comparer deux nombres de fils :')
for pid in TAB:
    w, f = TAB[pid][0], TAB[pid][1]
    w2 = F(w)
    g = float(M.g_du_point(w2)) * float(F(f))
    gd = M.garde_domaine(w2, g, M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"], M.Omega_du_canal(w2)[0])
    dire('  %s %s %s %r %r %s' % (pid, w, f, float(gd['D1']), float(gd['c_max']), gd['statut']))
nb = {k: sum(1 for p in BANDE if BANDE[p] == k) for k in ('PROCHE', 'MOYENNE', 'LOINTAINE', 'ANCRE', 'TEMOIN')}
dire('GROUPES : %s ; points juges EN DOMAINE %d, HORS DOMAINE %d (le gel : "la garde dit HORS DOMAINE a quatre points juges")' % (
    nb, sum(1 for p in TAB if BANDE[p] in LIM and TAB[p][5] == 'EN DOMAINE'), sum(1 for p in TAB if BANDE[p] in LIM and TAB[p][5] == 'HORS DOMAINE')))
ok_g = (nb == {'PROCHE': 4, 'MOYENNE': 4, 'LOINTAINE': 4, 'ANCRE': 2, 'TEMOIN': 2}
        and sum(1 for p in TAB if BANDE[p] in LIM and TAB[p][5] == 'HORS DOMAINE') == 4)
bad += (not ok_g)
dire('BILAN : %d ecart(s) a la table des seize points ; groupes et quatre HORS DOMAINE : %s' % (bad, 'tiennent' if ok_g else 'ECART'))
sys.exit(1 if bad else 0)
