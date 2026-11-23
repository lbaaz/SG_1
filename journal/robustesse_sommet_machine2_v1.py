# -*- coding: ascii -*-
"""ROBUSTESSE des choix NEUFS de la piece (certification (e), hors regle, aucune 2D) : ce que valent le facteur M, le seuil d'etendue 0.005, la garde e_bord < 0.7 et la formule de e_bord.
 (1) M_FACTEUR : a une cellule de barriere VIDE, M_facteur = 4 (ancien reglage) suffit-il ? (la plus longue variante va au site 0 + 10 + 24 = 34 ; Mh = (0 + 8) x 4 = 32). Et M_facteur 5 contre 6 : les largeurs changent-elles ? Echantillon : sept kappa a trois w2 (les deux bords et le milieu de chaque creneau : 12 w2, 84 cellules).
 (2) SEUIL D'ETENDUE : d'apres MA table (detail_machine2_sommet_v1.json), combien de w2 et de cellules l'eligibilite retirerait-elle pour des seuils de 0.0030 a 0.0050 ? Le seuil 0.005 est-il inerte ?
 (3) e_bord : ma formule |m_bord delta + Sigma2(m_bord) - Sigma2(0)| contre la valeur du moteur (sites[-1][1]) aux 160 cellules de barriere non vide ; et la garde 0.7 contre le plus grand e_bord.
Usage : py -3.11 -P robustesse_sommet_machine2_v1.py <dossier scripts du registre> <detail_machine2_sommet_v1.json>"""
import hashlib
import importlib.util
import json
import math
import os
import runpy
import statistics
import sys
import unicodedata
from fractions import Fraction as F

import numpy as np

REG, DETAIL = sys.argv[1], sys.argv[2]
MOTEUR, BLOC2, BLOC3 = (os.path.join(REG, n) for n in ('m17_chaine_v17.py', 'chaine_ordre2_bloc_machine1_v1.py', 'ordre3_bloc_machine1_v1.py'))
for p, c in ((MOTEUR, '82a0be882568fe0c'), (BLOC2, '7cd5977bc27bebc1'), (BLOC3, '534ba246aa3b8973')):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    assert hashlib.sha256(t.encode('utf-8')).hexdigest()[:16] == c, p
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('moteur', MOTEUR)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
g2 = runpy.run_path(BLOC2, init_globals={'M': M, 'np': np, 'math': math})
NS = runpy.run_path(BLOC3, init_globals=g2)
import table_eligibilite_sommet_machine2_v1 as T  # noqa: E402  (ma propre table ; matrice() et VARIANTES ; le chargement n'execute rien)
T.M, T.NS = M, NS
det = json.load(open(DETAIL))
KAPPAS = T.KAPPAS


def lnG(w2, gstr, sites_t, m_bord, mf):
    g = float(gstr)
    tb = NS['tables_ordre2'](0, 0, w2, g, sites_t, M_facteur=mf)
    t3 = NS['tables_ordre3'](0, 0, w2, g, tb)
    out = []
    for (a, c, L) in T.VARIANTES:
        H, W, i0 = T.matrice(tb, t3, m_bord, a, c, L)
        out.append(math.log(T.largeur(H, W, i0)[0]))
    return out


print('(1) M_FACTEUR')
cles = []
for nom in ('MP', 'PP', 'MG', 'PG'):
    ks = sorted(int(c.split('|')[1]) for c in det if c.startswith(nom + '|'))
    cles += [nom + '|%d' % k for k in (ks[0], ks[len(ks) // 2], ks[-1])]
n4 = n4_ok = 0
pire56 = 0.0
n56 = 0
for cle in cles:
    r = det[cle]
    w2 = F(r['w2'])
    for c in r['cellules']:
        g = float(c['g'])
        sites = M.barriere(0.0, 0.0, w2, g, True)
        vide = not sites
        sites_t = [(0, 0, abs(M.t_site(0, 0, 0, w2, g)))] if vide else sites
        mb = 0 if vide else sites[-1][0]
        a5 = lnG(w2, c['g'], sites_t, mb, 5)
        a6 = lnG(w2, c['g'], sites_t, mb, 6)
        pire56 = max(pire56, max(abs(x - y) for x, y in zip(a5, a6)))
        n56 += 1
        if vide:
            n4 += 1
            try:
                lnG(w2, c['g'], sites_t, mb, 4)
                n4_ok += 1
            except Exception as e:
                ex = type(e).__name__
print('    %d cellules (12 w2 x 7 kappa) ; plus grand |ln Gamma(M_facteur 5) - ln Gamma(M_facteur 6)| sur les dix-huit variantes : %.2e' % (n56, pire56))
print('    cellules a barriere VIDE de l echantillon : %d ; avec M_facteur = 4 : %d aboutissent, %d echouent (%s)' % (n4, n4_ok, n4 - n4_ok, ex if n4 - n4_ok else '-'))
print('\n(2) SEUIL D ETENDUE (ma table)')
et = {}
for cle, r in det.items():
    et[cle] = [c['etendue'] for c in r['cellules']]
tous = sorted(x for v in et.values() for x in v)
print('    etendue : minimum %.4f, mediane %.4f, maximum %.4f sur 560 cellules' % (tous[0], statistics.median(tous), tous[-1]))
for s in (0.0030, 0.0033, 0.0035, 0.0036, 0.0037, 0.0038, 0.0050, 0.0100, 0.0200):
    nc = sum(1 for x in tous if x > s)
    nw = sum(1 for v in et.values() if max(v) > s)
    print('    seuil %.4f : %3d cellules et %2d w2 sur 80 seraient retires' % (s, nc, nw))
mx = max(tous)
print('    tout seuil >= %.4f donne la meme table ; le seuil ecrit (0.005) est %.2f fois le maximum lu' % (mx, 0.005 / mx))
print('\n(3) e_bord')
n = 0
pe = 0.0
emax = 0.0
for cle, r in det.items():
    w2 = F(r['w2'])
    delta = float(w2) - 2.0
    for c in r['cellules']:
        emax = max(emax, c['e_bord'])
        if c['barriere_vide']:
            continue
        g = float(c['g'])
        sites = M.barriere(0.0, 0.0, w2, g, True)
        S2 = lambda mm: M.Sigma2_site(2 * mm, mm, w2, g)[0]
        mine = abs(sites[-1][0] * delta + S2(sites[-1][0]) - S2(0))
        pe = max(pe, abs(mine - sites[-1][1]))
        n += 1
print('    %d cellules de barriere non vide : plus grand ecart entre ma formule et la valeur du moteur : %.2e' % (n, pe))
print('    plus grand e_bord sur les 560 cellules : %.4f (garde : 0.7 : %.0f fois de marge)' % (emax, 0.7 / emax if emax else float('inf')))
