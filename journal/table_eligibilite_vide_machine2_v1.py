# -*- coding: ascii -*-
"""MA TABLE D'ELIGIBILITE des 252 cellules candidates du gel 'largeur du vide' (partie 1, canon b57c9ccdd3946261), certification (b).
Ecrite a partir du TEXTE du gel (sections 2 et 4) et des blocs DEPOSES du registre (moteur 82a0be88..., ordre 2 7cd5977b..., ordre 3 534ba246...),
SANS avoir lu eligibilite_vide_machine1_v1.py ni chaine_adaptee_bloc_machine1_v1.py ni la table de m1 (JSON) : le recoupement vient APRES.
Aucun calcul 2D. Chaines a une dimension seulement.
Largeur (4.4) : valeur propre de la matrice (4.3) dont le vecteur propre norme pese le plus sur le site 0 ; Gamma = -2 Im E.
 - Gamma/|delta| >= 1e-11 (flux) : Gamma = 2 <x|W|x>/<x|x> sur le vecteur propre de la diagonalisation dense (exact, H0 reelle symetrique).
 - en dessous : racine complexe de det(H - E) par secante, determinant par elimination en bande SANS pivot (largeur de bande 5),
   precision arbitraire (80 chiffres), depart = valeur propre de la double precision.  (Ma methode : pas de quotient de Rayleigh.)
Sortie : table_machine2_vide_v1.json (format de la section 5), detail_machine2_vide_v1.json, journal.
Usage : py -3.11 -P table_eligibilite_vide_machine2_v1.py"""
import os
for _k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import hashlib
import importlib.util
import json
import math
import runpy
import statistics
import sys
import time
import unicodedata
from fractions import Fraction as F
from multiprocessing import Pool

import mpmath as mp
import numpy as np

BASE = r'd:\devs\bocal\BOCAL4'
MOTEUR = BASE + r'\m17_chaine_v17.py'
BLOC2 = BASE + r'\ordre2\chaine_ordre2_bloc_machine1_v1.py'
BLOC3 = BASE + r'\livraison_16a_gel_loi_partie2\ext\lot_m1\ordre3_bloc_machine1_v1.py'
SORTIE = BASE + r'\certif_gel_vide_partie1_machine2'
CANONS = ((MOTEUR, '82a0be882568fe0c'), (BLOC2, '7cd5977bc27bebc1'), (BLOC3, '534ba246aa3b8973'))

# section 2 du gel
CRENEAUX = [('MG', range(1981, 1990)), ('MP', range(1991, 2000)), ('PP', range(2001, 2010)), ('PG', range(2011, 2020))]
PROFONDEURS = [(3, 0.0262), (4, 0.0200), (5, 0.0159), (6, 0.0130), (8, 0.00928), (12, 0.00558), (16, 0.00382)]
VARIANTES = [(a, c, L) for a in (1, 2, 4) for c in (6, 8, 10) for L in (16, 24)]   # 4.3
E_BORD_MAX, ETENDUE_MAX = 0.7, 0.02                                                  # 4.6
SEUIL_FLUX = 1e-11                                                                   # a moi : en dessous, precision arbitraire
DPS = 80

M = None
NS = None


def canon(p):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


def init():
    """Charge le moteur (canon verifie), puis les deux blocs deposes dans un espace de noms qui porte M, np et math."""
    global M, NS
    for p, c in CANONS:
        if canon(p) != c:
            raise SystemExit('REFUS : canon de %s' % p)
    spec = importlib.util.spec_from_file_location('moteur', MOTEUR)
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)
    brut = M.X_saut_reel
    cache = {}

    def X(p, k, l, n1, n2, w2):          # cache pur : memes valeurs, moins d'appels
        c = (p, k, l, n1, n2, w2)
        if c not in cache:
            cache[c] = brut(p, k, l, n1, n2, w2)
        return cache[c]

    M.X_saut_reel = X
    g2 = runpy.run_path(BLOC2, init_globals={'M': M, 'np': np, 'math': math})
    NS = runpy.run_path(BLOC3, init_globals=g2)


def matrice(tb, t3, m_bord, a, c, L):
    """4.3 : diagonale m delta + S_m - S_0 - i W_m ; hors diagonale t_m + T3_m (m,m+1), U_m (m,m+2), W3_m (m,m+3), W5_m (m,m+5) ;
    W_m = a |t_m| ((m - debut)/L)^2 pour debut < m <= debut + L ; debut = m_bord + c ; sites de m_min a debut + L."""
    d, m_min = tb['d'], tb['m_min']
    debut = m_bord + c
    Mh = debut + L
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex)
    W = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + (tb['S'][m] - tb['S'][0])
        if m > debut:
            W[i] = a * abs(tb['t'][m]) * ((m - debut) / float(L)) ** 2
            H[i, i] += -1j * W[i]
        if m < Mh:
            x = tb['t'][m] + t3['T3'][m]
            H[i, i + 1] = x
            H[i + 1, i] = x
        if m + 2 <= Mh:
            H[i, i + 2] = tb['U'][m]
            H[i + 2, i] = tb['U'][m]
        if m + 3 <= Mh:
            H[i, i + 3] = t3['W3'][m]
            H[i + 3, i] = t3['W3'][m]
        if m + 5 <= Mh:
            H[i, i + 5] = t3['W5'][m]
            H[i + 5, i] = t3['W5'][m]
    return H, W, -m_min


def det_bande(A0, E, n, bw=5):
    A = [row[:] for row in A0]
    for i in range(n):
        A[i][i] = A[i][i] - E
    det = mp.mpc(1)
    for i in range(n):
        p = A[i][i]
        det *= p
        if i == n - 1:
            break
        hi = min(i + bw, n - 1)
        for r in range(i + 1, hi + 1):
            f = A[r][i] / p
            if f != 0:
                Ai = A[i]
                Ar = A[r]
                for c in range(i, hi + 1):
                    Ar[c] -= f * Ai[c]
    return det


def racine_mp(H, E0):
    mp.mp.dps = DPS
    n = H.shape[0]
    A0 = [[mp.mpc(float(H[i, j].real), float(H[i, j].imag)) for j in range(n)] for i in range(n)]
    x0 = mp.mpc(float(E0.real), 0)
    x1 = x0 + mp.mpf('1e-9')
    f0, f1 = det_bande(A0, x0, n), det_bande(A0, x1, n)
    for it in range(80):
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        x0, f0 = x1, f1
        x1 = x2
        if abs(x1 - x0) < mp.mpf(10) ** (-(DPS - 20)):
            break
        f1 = det_bande(A0, x1, n)
    else:
        return None, it + 1
    return x1, it + 1


def largeur(H, W, i0, d_abs):
    """rend (Gamma, methode, poids du site 0 de l'etat choisi, flux de reference si mp)."""
    vals, vecs = np.linalg.eig(H)
    rec = np.abs(vecs[i0, :]) ** 2
    nu = int(np.argmax(rec))
    psi2 = np.abs(vecs[:, nu]) ** 2
    flux = 2.0 * float(W @ psi2) / float(psi2.sum())
    E = vals[nu]
    if np.isfinite(flux) and flux > 0 and flux / d_abs >= SEUIL_FLUX:
        return flux, 'flux', float(rec[nu]), None
    x, it = racine_mp(H, E)
    if x is None:
        return None, 'mp-echec', float(rec[nu]), None
    if abs(float(x.real) - float(E.real)) > 1e-6:
        return None, 'mp-autre-racine', float(rec[nu]), None
    return (float(-2 * x.imag) if x.imag != 0 else None), 'mp', float(rec[nu]), float(flux)


def traite(w2n):
    if M is None:
        init()
    w2 = F(w2n, 1000)
    delta = float(w2) - 2.0
    X = M.X_saut_reel(M.P, 2, 1, 0, 0, w2)
    Xf = M.X_saut_reel(M.P, 2, 1, 0.0, 0.0, w2)
    out = {'w2': str(w2), 'w2n': w2n, 'X': X, 'X_entier_vs_flottant_egal': X == Xf, 'cellules': []}
    for m, kappa in PROFONDEURS:
        g1 = kappa * abs(delta) * M.P / X
        g2 = kappa * float(abs(w2 - 2)) * M.P / X
        gstr = '%.5e' % g1
        cel = {'m': m, 'kappa': kappa, 'g': gstr, 'g_variante_delta_exact': '%.5e' % g2, 'g_diff': gstr != '%.5e' % g2}
        g = float(gstr)
        sites = M.barriere(0.0, 0.0, w2, g, True)
        if not sites:
            cel.update({'m_bord': None, 'eligible': False, 'raison': 'aucun site', 'etendue': None})
            out['cellules'].append(cel)
            continue
        m_bord = sites[-1][0]
        S2 = lambda mm: M.Sigma2_site(2 * mm, mm, w2, g)[0]
        e_bord = abs(m_bord * delta + S2(m_bord) - S2(0))
        cel.update({'m_bord': m_bord, 'e_bord': e_bord, 'e_bord_moteur': sites[-1][1]})
        tb = NS['tables_ordre2'](0, 0, w2, g, sites, M_facteur=4)
        t3 = NS['tables_ordre3'](0, 0, w2, g, tb)
        lns, methodes, poids, ecarts = [], [], [], []
        defini = True
        for (a, c, L) in VARIANTES:
            H, W, i0 = matrice(tb, t3, m_bord, a, c, L)
            G, meth, rec, flux_ref = largeur(H, W, i0, abs(delta))
            methodes.append(meth)
            poids.append(rec)
            if G is None or not (G > 0):
                defini = False
                lns.append(None)
            else:
                lns.append(math.log(G))
                if flux_ref is not None and flux_ref > 0:
                    ecarts.append(abs(math.log(G) - math.log(flux_ref)))
        cel['methodes'] = {k: methodes.count(k) for k in sorted(set(methodes))}
        cel['poids_site0_min'] = min(poids)
        cel['ecart_mp_flux_max'] = max(ecarts) if ecarts else None
        if defini:
            et = max(lns) - min(lns)
            cel['etendue'] = et
            cel['ln_plateau'] = statistics.median(lns)
            cel['G3_plateau'] = math.exp(cel['ln_plateau'])
            cel['lnG'] = lns
        else:
            cel['etendue'] = None
        cel['eligible'] = bool(m_bord == m and e_bord < E_BORD_MAX and defini and cel['etendue'] <= ETENDUE_MAX)
        cel['conditions'] = {'i_m_bord_egal_m': m_bord == m, 'ii_e_bord_lt_0.7': e_bord < E_BORD_MAX,
                             'iii_etendue_definie_et_le_0.02': bool(defini and cel['etendue'] <= ETENDUE_MAX)}
        out['cellules'].append(cel)
    lisibles = [c for c in out['cellules'] if c['m'] in (3, 4, 5, 6)]
    out['eligible'] = all(c['eligible'] for c in lisibles)
    return out


def main():
    t0 = time.time()
    init()
    taches = [n for (_, rg) in CRENEAUX for n in rg]
    print('canons des entrees : OK ; %d w2, %d cellules' % (len(taches), len(taches) * len(PROFONDEURS)), flush=True)
    res = {}
    with Pool(10, initializer=init) as pool:
        for r in pool.imap_unordered(traite, taches):
            res[r['w2n']] = r
            print('  %s fait (%d/%d, %.0f s)' % (r['w2'], len(res), len(taches), time.time() - t0), flush=True)
    table = {'creneaux': {}}
    detail = {}
    for nom, rg in CRENEAUX:
        cand = []
        for n in rg:
            r = res[n]
            cand.append({'w2': r['w2'], 'eligible': r['eligible'],
                         'cellules': [{'m': c['m'], 'g': c['g'], 'eligible': c['eligible']} for c in r['cellules']]})
            detail['%s|%d' % (nom, n)] = r
        table['creneaux'][nom] = {'candidats': cand}
    json.dump(table, open(SORTIE + r'\table_machine2_vide_v1.json', 'w'), indent=1, sort_keys=True)
    json.dump(detail, open(SORTIE + r'\detail_machine2_vide_v1.json', 'w'), indent=1, sort_keys=True)
    print()
    for nom, rg in CRENEAUX:
        ok = sum(1 for n in rg if res[n]['eligible'])
        pro = sum(1 for n in rg for c in res[n]['cellules'] if c['m'] in (8, 12, 16) and c['eligible'])
        print('creneau %s : %d w2 eligibles sur %d ; cellules profondes retenues : %d sur %d' % (nom, ok, len(rg), pro, 3 * len(rg)))
        for n in rg:
            r = res[n]
            print('  %s  ' % r['w2'] + '  '.join('m%d %s' % (c['m'], ('%.4f' % c['etendue']) if c.get('etendue') is not None else 'indef.') for c in r['cellules']) + ('  ELIGIBLE' if r['eligible'] else '  INELIGIBLE'))
    print()
    print('par profondeur, sur les 36 w2 :')
    for m, _ in PROFONDEURS:
        cs = [c for n in taches for c in res[n]['cellules'] if c['m'] == m]
        mb = sorted(set(c['m_bord'] for c in cs))
        print('  m=%2d  barreaux %s  etendue max %.4f  e_bord max %.3f  poids site 0 min %.4f  G3* %.2e a %.2e  methodes %s' % (
            m, mb, max(c['etendue'] for c in cs), max(c['e_bord'] for c in cs), min(c['poids_site0_min'] for c in cs),
            min(c['G3_plateau'] for c in cs), max(c['G3_plateau'] for c in cs),
            {k: sum(c['methodes'].get(k, 0) for c in cs) for k in ('flux', 'mp', 'mp-echec', 'mp-autre-racine')}))
    n_gdiff = sum(1 for n in taches for c in res[n]['cellules'] if c['g_diff'])
    print('couplages ecrits dont l ecriture depend de |delta| calcule en flottant ou en exact :', n_gdiff)
    print('X entier == X flottant partout :', all(res[n]['X_entier_vs_flottant_egal'] for n in taches))
    print('ecart e_bord (ma formule) - e_bord (moteur) max : %.2e' % max(abs(c['e_bord'] - c['e_bord_moteur']) for n in taches for c in res[n]['cellules']))
    em = [c['ecart_mp_flux_max'] for n in taches for c in res[n]['cellules'] if c.get('ecart_mp_flux_max') is not None]
    print('ecart mp vs flux de la double precision (variantes en mp) : max %.2e sur ln Gamma, %d cellules' % (max(em) if em else float('nan'), len(em)))
    print('FIN en %.0f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
