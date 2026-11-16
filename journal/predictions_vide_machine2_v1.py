# -*- coding: ascii -*-
"""MES PREDICTIONS des 28 cellules du gel 'largeur du vide' (partie 2, eebd979f18d8db48), certification (b) et (d). Ecrites du TEXTE du gel (sections 3, 7) et de la note sur le vide (3.2, 4.1 de la note d'echelle),
avec mes fonctions de la certification de la partie 1 (table_eligibilite_vide_machine2_v1.py : tables des blocs deposes, matrice de la chaine, largeur par flux ou determinant en bande en mp), SANS lire predictions_vide_machine1_v1.py
ni la table gelee avant d'avoir ecrit ma sortie. Aucune 2D. Par cellule :
  ln G3, ln G2, ln G1 : mediane des 18 ln Gamma des variantes (a, c, L) de l'absorbeur adapte, chaine d'ordre 3 / 2 / 1 ; etendues ;
  ln Phi* : mediane des 18 ln Gamma de la chaine de la LIMITE delta -> 0 (diagonale m, sauts kappa tau_m / tau_0 a w2 = 2, absorbeur adapte a |T_m|), en unites de |delta| ;
  r3 = ln G3 - ln |delta| - ln Phi* ; forme fermee : -B M0 + c ln M0 + d, M0 = (2 lambda)^(-2/3), lambda = g X_c / (5 |delta|).
Usage : py -3.11 -P predictions_vide_machine2_v1.py"""
import json
import math
import os
import statistics
import sys
import time
from fractions import Fraction as F
from multiprocessing import Pool

sys.path.insert(0, r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie1_machine2')
import numpy as np
import table_eligibilite_vide_machine2_v1 as T

D1 = r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie1_machine2'
D2 = r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie2_machine2'
VARIANTES = T.VARIANTES
FORME_PHI = r'd:\devs\bocal\BOCAL4\livraison_16e_vide_etape_sans_run\ext\lot_machine1_2026-11-16_vide_etape_sans_run_v1\forme_phi_v1.json'   # canon 2e2ed5b9b745790c


def matrice_ordre(tb, t3, m_bord, a, c, L, ordre):
    """meme chaine que T.matrice, mais l'ordre est un parametre : 1 = diagonale m delta et sauts t_m ; 2 = + S_m - S_0 et U_m ; 3 = + T3, W3, W5."""
    d, m_min = tb['d'], tb['m_min']
    debut = m_bord + c
    Mh = debut + L
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex)
    W = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + ((tb['S'][m] - tb['S'][0]) if ordre >= 2 else 0.0)
        if m > debut:
            W[i] = a * abs(tb['t'][m]) * ((m - debut) / float(L)) ** 2
            H[i, i] += -1j * W[i]
        if m < Mh:
            x = tb['t'][m] + (t3['T3'][m] if ordre == 3 else 0.0)
            H[i, i + 1] = x
            H[i + 1, i] = x
        if ordre >= 2 and m + 2 <= Mh:
            H[i, i + 2] = tb['U'][m]
            H[i + 2, i] = tb['U'][m]
        if ordre == 3 and m + 3 <= Mh:
            H[i, i + 3] = t3['W3'][m]
            H[i + 3, i] = t3['W3'][m]
        if ordre == 3 and m + 5 <= Mh:
            H[i, i + 5] = t3['W5'][m]
            H[i + 5, i] = t3['W5'][m]
    return H, W, -m_min


def plateau(tb, t3, m_bord, ordre, d_abs):
    lns = []
    for (a, c, L) in VARIANTES:
        H, W, i0 = matrice_ordre(tb, t3, m_bord, a, c, L, ordre)
        G, meth, rec, ref = T.largeur(H, W, i0, d_abs)
        if G is None or not G > 0:
            return None, None
        lns.append(math.log(G))
    return statistics.median(lns), max(lns) - min(lns)


def tau(m):
    return T.M.X_saut_reel(T.M.P, 2, 1, float(2 * m), float(m), F(2)) / T.M.P


def m_bord_limite(kappa):
    """ma lecture de la regle de barriere du moteur appliquee a la chaine de la limite (cf. verifie_phi_profond_machine2_v1.py)."""
    t0 = tau(0)
    sites, neg = [], 0
    for m in range(1, 200000):
        if m > 2.0 * kappa * tau(m) / t0:
            sites.append(m)
            neg = 0
        elif sites:
            neg += 1
            if neg >= 3:
                break
        elif m > 8 and 2.0 * kappa * tau(m) / t0 > 4.0 * m:
            break
    return sites[-1]


def phi_etoile(kappa):
    """ln Phi* : mediane sur les 18 variantes de ln Gamma (unites de |delta|) de la chaine de la limite."""
    mb = m_bord_limite(kappa)
    t0 = tau(0)
    lns = []
    for (a, c, L) in VARIANTES:
        cap = mb + c
        Mh = cap + L
        n = Mh + 1
        H = np.zeros((n, n), dtype=complex)
        W = np.zeros(n)
        Tm = [kappa * tau(m) / t0 for m in range(Mh + 1)]
        for m in range(0, Mh + 1):
            H[m, m] = float(m)
            if m > cap:
                W[m] = a * Tm[m] * ((m - cap) / float(L)) ** 2
                H[m, m] += -1j * W[m]
            if m < Mh:
                H[m, m + 1] = Tm[m]
                H[m + 1, m] = Tm[m]
        G, meth, rec, ref = T.largeur(H, W, 0, 1.0)
        if G is None or not G > 0:
            return None, mb
        lns.append(math.log(G))
    return statistics.median(lns), mb


def traite(cel):
    if T.M is None:
        T.init()
    M = T.M
    w2 = F(cel['w2'])
    delta = float(w2) - 2.0
    d_abs = abs(delta)
    g = float(cel['g'])
    X = M.X_saut_reel(M.P, 2, 1, 0, 0, w2)
    kappa = g * X / (M.P * d_abs)
    sites = M.barriere(0.0, 0.0, w2, g, True)
    m_bord = sites[-1][0]
    S2 = lambda mm: M.Sigma2_site(2 * mm, mm, w2, g)[0]
    e_bord = abs(m_bord * delta + S2(m_bord) - S2(0))
    tb = T.NS['tables_ordre2'](0, 0, w2, g, sites, M_facteur=4)
    t3 = T.NS['tables_ordre3'](0, 0, w2, g, tb)
    out = {'id': cel['id'], 'w2': str(w2), 'delta': delta, 'm': cel['m'], 'g': cel['g'], 'kappa': kappa, 'm_bord': m_bord, 'e_bord': e_bord, 'r_c': 2 * (cel['m'] + max(8, cel['m'])) + 2}
    out['N_max'] = out['r_c'] + 100
    for o in (1, 2, 3):
        ln, et = plateau(tb, t3, m_bord, o, d_abs)
        out['ln_G%d' % o] = ln
        out['etendue_ordre%d' % o] = et
    out['etendue'] = out['etendue_ordre3']
    out['ln_Phi_etoile'], out['m_bord_limite'] = phi_etoile(kappa)
    out['r3'] = out['ln_G3'] - math.log(d_abs) - out['ln_Phi_etoile']
    # forme fermee
    XC = float(M.coeff_homogene_X_s(F(2)))
    B = math.gamma(1.0 / 3.0) * math.gamma(0.5) / math.gamma(5.0 / 6.0)
    lam = g * XC / (5.0 * d_abs)
    M0 = (2.0 * lam) ** (-2.0 / 3.0)
    out['X_c'] = XC
    out['B'] = B
    out['M0_formule'] = M0
    # DEUXIEME DEFINITION de M0, celle qui rend la table de m1 : lambda = kappa X_c / (P tau_0(w2 = 2)) (la limite exacte), au lieu de g X_c / (5 |delta|) (qui porte X(0,0; w2) et non X(0,0; 2))
    lam2 = kappa * XC / (M.P * tau(0))
    M0b = (2.0 * lam2) ** (-2.0 / 3.0)
    out['M0'] = M0b
    FP = json.load(open(FORME_PHI))
    ref = [x for x in FP['B'] if (x['n1'], x['n2'], x['M0']) == (0, 0, 4096)][0]
    out['c_FF'], out['d_FF'] = ref['c_L'], -ref['reste3']
    out['ln_forme_fermee'] = math.log(d_abs) - B * M0b + out['c_FF'] * math.log(M0b) + out['d_FF']
    out['ln_forme_fermee_def_g'] = math.log(d_abs) - B * M0 + out['c_FF'] * math.log(M0) + out['d_FF']
    out['X0_w2'] = X
    out['X0_2'] = tau(0) * M.P
    return out


def main():
    t0 = time.time()
    T.init()
    tir = json.load(open(D1 + r'\tirage_graine_479579_machine2_v1.json'))['cellules']
    with Pool(10, initializer=T.init) as pool:
        res = pool.map(traite, tir)
    json.dump({'cellules': res}, open(D2 + r'\predictions_machine2_vide_v1.json', 'w', newline='\n'), indent=1, sort_keys=True)
    print('cellules calculees :', len(res), '; %.0f s' % (time.time() - t0))
    print('id      kappa           m_bord  e_bord    ln G1       ln G2       ln G3       ln Phi*     r3        etendue  M0(formule)')
    for r in res:
        print('%-5s %.12f   %d    %.5f  %+.6f  %+.6f  %+.6f  %+.6f  %+.5f  %.4f   %.5f' % (r['id'], r['kappa'], r['m_bord'], r['e_bord'], r['ln_G1'], r['ln_G2'], r['ln_G3'], r['ln_Phi_etoile'], r['r3'], r['etendue'], r['M0_formule']))


if __name__ == '__main__':
    main()
