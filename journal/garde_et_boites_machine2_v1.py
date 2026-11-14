# -*- coding: ascii -*-
"""Recalcul par machine 2, SANS aucune diagonalisation, de ce que le gel b59651f99e60707a ecrit sur la garde G-1 du moteur et sur les boites.
  1. aux QUATORZE points de la section 4 : g, graine, boite (r_c, N), faisabilite, garde G-1 (D1, c_max, site, statut), comme mesurer_point la
     calcule (seuil_A4 en lecture reelle, puis garde_domaine avec Omega_du_canal) ; comparees, a six decimales, a la table du gel (LUE DANS
     LE TEXTE DU GEL) ;
  2. sur la GRILLE de la section 2 (26 valeurs de w2, six facteurs : 156 points) : les trois phrases de (i) -- D1 ne mord jamais (au plus
     0.1944), tous les HORS DOMAINE viennent de D2a, les intervalles EN DOMAINE par facteur -- et les deux points "non pris" de la section 4.
Usage (depuis BOCAL4) : python -P domaine_G1/garde_et_boites_machine2_v1.py <moteur> <gel.md>"""
import importlib.util
import math
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


# ---- la table du gel, lue dans son texte
TAB = {}
for m in re.finditer(r'^\s+(E\d|H\d|A\d)\s+w2 = (\d+/\d+)\s+facteur (\S+)\s+D1 ([0-9.]+)\s+c_max ([0-9.]+)\s+N (\d+)$', GEL, re.M):
    TAB[m.group(1)] = (m.group(2), m.group(3), m.group(4), m.group(5), int(m.group(6)))
st_gel = {}
cour = None
for ln in GEL.split('\n'):
    s = ln.strip()
    if s.startswith('JUGES, garde EN DOMAINE') or s.startswith('ANCRES'):
        cour = 'EN DOMAINE'
    elif s.startswith('JUGES, garde HORS DOMAINE'):
        cour = 'HORS DOMAINE'
    m = re.match(r'^(E\d|H\d|A\d)\s+w2 = ', s)
    if m and cour:
        st_gel[m.group(1)] = cour
assert len(TAB) == 14 and len(st_gel) == 14


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
    return g, (n1, n2), r_c, N, gd


dire('1. LES QUATORZE POINTS : garde G-1 et boite, recalculees par moi, contre la table du gel (section 4), a six decimales')
for pid in TAB:
    w, f, d1t, cmt, Nt = TAB[pid]
    w2, fac = F(w), F(f)
    g, gr, r_c, N, gd = calc(w2, fac)
    ok = ('%.6f' % gd['D1'] == d1t and '%.6f' % gd['c_max'] == cmt and N == Nt and gd['statut'] == st_gel[pid] and N <= M.N_MAX_EB)
    bad += (not ok)
    dire('  %s w2=%-8s x%-4s g %.6e graine (%.3f, %.3f) r_c %d N %d (gel %d) ; D1 %.6f (gel %s) c_max %.6f (gel %s) site %s %s (gel %s) -> %s' % (
        pid, w, f, g, gr[0], gr[1], r_c, N, Nt, gd['D1'], d1t, gd['c_max'], cmt, gd['site_c_max'], gd['statut'], st_gel[pid], 'IDENTIQUE' if ok else 'ECART'))
dire('  ecarts : %d' % bad)

dire()
dire('2. LA GRILLE DE LA SECTION 2 : 26 valeurs de w2 (1.86 a 1.98 et 2.02 a 2.14), six facteurs (1/2, 2/3, 1, 3/2, 2, 3), garde seule')
W2S = [F(n, 100) for n in list(range(186, 199)) + list(range(202, 215))]
FACS = [F(1, 2), F(2, 3), F(1), F(3, 2), F(2), F(3)]
G = {}
for fac in FACS:
    for w2 in W2S:
        gd = M.garde_domaine(w2, float(M.g_du_point(w2)) * float(fac), M.seuil_A4(w2, float(M.g_du_point(w2)) * float(fac), lecture=M.LECTURE_OCCUPATIONS)["S_det"],
                             M.Omega_du_canal(w2)[0])
        G[(w2, fac)] = (gd['D1'], gd['c_max'], gd['statut'])
dire('  %d points calcules' % len(G))
d1max = max(v[0] for v in G.values())
hors_d1 = [(k, v) for k, v in G.items() if v[0] > 0.2]
hors = [(k, v) for k, v in G.items() if v[2] == 'HORS DOMAINE']
hors_d2a_seul = [(k, v) for k, v in hors if v[0] <= 0.2]
dire('  D1 maximal sur la grille : %.4f (le gel dit 0.1944) ; points ou D1 > 1/5 : %d ; HORS DOMAINE : %d, dont par D2a seule %d' % (d1max, len(hors_d1), len(hors), len(hors_d2a_seul)))
for fac in (F(1), F(3, 2), F(2, 3)):
    en = [w2 for w2 in W2S if G[(w2, fac)][2] == 'EN DOMAINE']
    contigu = all(G[(w2, fac)][2] == 'EN DOMAINE' for w2 in W2S if en[0] <= w2 <= en[-1])
    dire('  facteur %-3s : EN DOMAINE de %.2f a %.2f (les valeurs de la grille entre les deux, toutes EN DOMAINE : %s)' % (fac, float(en[0]), float(en[-1]), contigu))
v1 = G[(F(192, 100), F(2, 3))]
v2 = G[(F(189, 100), F(3, 2))]
dire('  non pris : 1.92 a facteur 2/3 : c_max %.4f %s (le gel : 0.0927, EN DOMAINE) ; 1.89 a facteur 3/2 : c_max %.4f %s (le gel : 0.1017, HORS DOMAINE)' % (v1[1], v1[2], v2[1], v2[2]))
ok_gel = (round(d1max, 4) == 0.1944 and not hors_d1 and len(hors) == len(hors_d2a_seul)
          and ['%.2f' % float(w2) for w2 in W2S if G[(w2, F(1))][2] == 'EN DOMAINE'][0] == '1.90' and ['%.2f' % float(w2) for w2 in W2S if G[(w2, F(1))][2] == 'EN DOMAINE'][-1] == '2.09'
          and ['%.2f' % float(w2) for w2 in W2S if G[(w2, F(3, 2))][2] == 'EN DOMAINE'][-1] == '2.12'
          and ['%.2f' % float(w2) for w2 in W2S if G[(w2, F(2, 3))][2] == 'EN DOMAINE'][0] == '1.92' and ['%.2f' % float(w2) for w2 in W2S if G[(w2, F(2, 3))][2] == 'EN DOMAINE'][-1] == '2.07'
          and '%.4f' % v1[1] == '0.0927' and v1[2] == 'EN DOMAINE' and '%.4f' % v2[1] == '0.1017' and v2[2] == 'HORS DOMAINE')
dire('  LES PHRASES DE (i) ET LES DEUX POINTS NON PRIS, RECALCULES : %s' % ('TIENNENT' if ok_gel else 'UN ECART'))
dire()
dire('BILAN : %d ecart(s) a la table des quatorze points ; phrases de (i) : %s' % (bad, 'tiennent' if ok_gel else 'ECART'))
