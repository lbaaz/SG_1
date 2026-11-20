# -*- coding: ascii -*-
"""Section 12 (e) : MA table de la section 4 (chaine de machine 2, ecrite du texte, rejouee sur BOCAL4) contre le TEXTE du gel (section 4, canon 428ac47649de31f3), contre le JSON de machine 1
(chaine_cellules_pont_v1.json du lot, produit sur son poste) ET contre mes details de la premiere partie (G3*, etendues). Chaine seule, aucune 2D. Machine 2, 2026-11-17.
Usage : py -3.11 -P confronte_section4_machine2_v1.py <gel.md> <ma chaine.json> <chaine de m1.json> <mes details de la premiere partie.json>"""
import json
import math
import re
import sys
from fractions import Fraction as F

gel, ma, lui, det = sys.argv[1:5]
T = open(gel, encoding='ascii').read().split('\n')
MA = json.load(open(ma)); LUI = json.load(open(lui))['cellules']; DET = json.load(open(det))
NOMS = ['MG3', 'MG4', 'MG5', 'PG3', 'PG4', 'PG5']
# --- les deux tables a douze lignes du texte (section 4)
def table(depart):
    i = [k for k, l in enumerate(T) if l.strip().startswith(depart)][0]
    out = {}
    h = [k for k in range(i, i + 4) if T[k].split()[:1] == ['x']][0]
    for l in T[h + 1:h + 13]:
        p = l.split()
        out[float(p[0])] = [float(v) for v in p[1:7]]
    return out
t_ln = table('ln (rho_3 |delta|)')
t_pas = table('Le pas de l\'ordre 2')
X = sorted(t_ln)
print('texte : %d ecarts, %d colonnes' % (len(X), len(t_ln[X[0]])))
d_ln = d_pas = 0.0; d_lnL = d_pasL = 0.0; d_lnD = d_pasD = 0.0
for j, n in enumerate(NOMS):
    for i, x in enumerate(X):
        # ma chaine contre le texte (2 et 4 decimales) ; ma chaine contre le JSON de machine 1 (pleine precision)
        d_ln = max(d_ln, abs(MA[n]['ln_rho3_delta'][i] - t_ln[x][j])); d_pas = max(d_pas, abs(MA[n]['pas'][i] - t_pas[x][j]))
        d_lnL = max(d_lnL, abs(MA[n]['ln_rho3_delta'][i] - (LUI[n]['ln_rho3'][i] + math.log(abs(LUI[n]['delta'])))))
        d_pasL = max(d_pasL, abs(MA[n]['pas'][i] - (LUI[n]['ln_rho2'][i] - LUI[n]['ln_rho3'][i])))
print('ln(rho_3 |delta|) : ma chaine contre le TEXTE (arrondi a 2 decimales) : plus grand ecart %.4f (borne de l arrondi 0.005) ; contre le JSON de machine 1 : %.2e' % (d_ln, d_lnL))
print('pas (ordre 2 -> 3) : ma chaine contre le TEXTE (arrondi a 4 decimales) : plus grand ecart %.5f (borne 0.00005) ; contre le JSON de machine 1 : %.2e' % (d_pas, d_pasL))
# --- colonnes de la table de tete : m_bord, e_bord, r_c, G3*, etendue vide, etendue lisse, pas
lig = [l for l in T if re.match(r'\s+(MG|PG)[345]\s+[345]\s+0\.', l)]
print('lignes de la table de tete du texte :', len(lig))
for l, n in zip(lig, NOMS):
    p = l.split()
    m_bord, e_bord, rc, G3, ev, el, pas = int(p[1]), float(p[2]), int(p[3]), float(p[4]), float(p[5]), float(p[6]), float(p[7])
    cel = [d for d in DET if F(d['w2']) == F(MA[n]['w2']) and d['m'] == MA[n]['m']][0]
    rc_regle = 2 * (MA[n]['m'] + max(8, MA[n]['m'])) + 2
    print('%s : m_bord %d/%d ; e_bord texte %.4f ma %.4f ; r_c texte %d regle %d ; G3* texte %.4e mes details %.4e (rapport %.6f) ; etendue vide texte %.4f mes details %.4f ; etendue lisse %.4f / %.4f ; pas max %.4f / %.4f' % (
        n, m_bord, MA[n]['m_bord'], e_bord, MA[n]['e_bord'], rc, rc_regle, G3, cel['plateau'], cel['plateau'] / G3, ev, cel['etendue_vide'], el, MA[n]['etendue_lisse_max'], pas, MA[n]['pas_max']))
    assert m_bord == MA[n]['m_bord'] and rc == rc_regle
