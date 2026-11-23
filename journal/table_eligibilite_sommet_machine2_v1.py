# -*- coding: ascii -*-
"""MA TABLE D'ELIGIBILITE des 560 cellules candidates du gel "SOMMET" (partie 1, piece 1e5039cade55d13f, lot 3ba4618d7976c6ea), certification (b).
Ecrite a partir du TEXTE de la piece (sections 2, 4 et 5) et des blocs DEPOSES du registre (moteur 82a0be882568fe0c, ordre 2 7cd5977bc27bebc1, ordre 3 534ba246aa3b8973),
SANS avoir lu eligibilite_sommet_machine1_v1.py, ni chaine_adaptee_bloc_machine1_v1.py, ni la table JSON de machine 1 (le recoupement vient APRES). J'ai LU la piece, y compris les chiffres de sa section 7 (etendues par w2 et par kappa) : cela se dit.
Aucun calcul 2D. Chaines a une dimension seulement.
Cellule (w2, kappa) : g = kappa |w2 - 2| P / X(w2) (X = X_saut_reel(P, 2, 1, 0, 0, w2) du moteur, w2 en Fraction, P = 5), ARRONDI a six chiffres ('%.5e') ; eta0 = max(|w2 - 2|, g X(w2) / (P kappa_3)), kappa_3 = 0.0262, calcule avec le g ECRIT puis ecrit ('%.5e') ;
r_c = 2 (m_bord + max(8, m_bord)) + 2. Barriere (4.1) : sites = barriere(0, 0, w2, g, True) du moteur ; liste VIDE -> m_bord = 0, e_bord = 0, liste a un seul site (0, 0, |t_site(0, 0, 0, w2, g)|) ; sinon m_bord = dernier site, e_bord = |m_bord delta + Sigma2(m_bord) - Sigma2(0)|, delta = w2 - 2.
Tables (4.2) : tables_ordre2(0, 0, w2, g, sites, M_facteur = 5) puis tables_ordre3. Matrice (4.3) : dix-huit variantes (a, c, L), a = 1, 2, 4 ; c = 6, 8, 10 ; L = 16, 24 ; debut = m_bord + c.
Largeur (4.4) : valeur propre de la matrice complexe symetrique dont le vecteur propre norme pese le plus sur le site 0 ; Gamma = -2 Im E. MA METHODE : diagonalisation dense (numpy), Gamma = 2 <x|W|x> / <x|x> sur ce vecteur (exact : H0 reelle symetrique, W diagonale reelle),
et, A COTE, Gamma_eig = -2 Im E lu sur la valeur propre ; l'ecart des deux est rapporte. Plateau G3* = exp(mediane des dix-huit ln Gamma) ; etendue = max - min de ln Gamma (4.5).
Eligible (4.6) : (i) m_bord = profondeur cible du kappa (2, 1, 0, 0, 0, 0, 0) ; (ii) e_bord < 0.7 ; (iii) etendue definie et <= 0.005. Un w2 est eligible si ses sept cellules le sont (4.7).
Sortie : table_machine2_sommet_v1.json (format de la section 5), detail_machine2_sommet_v1.json, journal.
Usage : py -3.11 -P table_eligibilite_sommet_machine2_v1.py <dossier scripts du registre (moteur et blocs)> <dossier de sortie>"""
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

import numpy as np

REG, SORTIE = sys.argv[1], sys.argv[2]
MOTEUR = os.path.join(REG, 'm17_chaine_v17.py')
BLOC2 = os.path.join(REG, 'chaine_ordre2_bloc_machine1_v1.py')
BLOC3 = os.path.join(REG, 'ordre3_bloc_machine1_v1.py')
CANONS = ((MOTEUR, '82a0be882568fe0c'), (BLOC2, '7cd5977bc27bebc1'), (BLOC3, '534ba246aa3b8973'))

# section 2 de la piece : w2 = 2 +/- k / 100000
CRENEAUX = [('MP', -1, [k for k in range(5, 21) if k != 10]), ('PP', +1, [k for k in range(5, 21) if k != 10]),
            ('MG', -1, list(range(25, 50))), ('PG', +1, list(range(25, 50)))]
KAPPAS = [('0.0363', 0.0363, 2), ('0.0530', 0.0530, 1), ('0.0800', 0.0800, 0), ('0.1300', 0.1300, 0), ('0.2000', 0.2000, 0), ('0.4000', 0.4000, 0), ('1.0000', 1.0000, 0)]
KAPPA3 = 0.0262
VARIANTES = [(a, c, L) for a in (1, 2, 4) for c in (6, 8, 10) for L in (16, 24)]
E_BORD_MAX, ETENDUE_MAX, M_FACTEUR = 0.7, 0.005, 5

M = None
NS = None


def canon(p):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


def init():
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
    """4.3 : diagonale m delta + S_m - S_0 - i W_m ; hors diagonale t_m + T3_m (m, m+1), U_m (m, m+2), W3_m (m, m+3), W5_m (m, m+5) ;
    W_m = a |t_m| ((m - debut) / L)^2 pour debut < m <= debut + L ; debut = m_bord + c ; sites de m_min a debut + L."""
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


def largeur(H, W, i0):
    vals, vecs = np.linalg.eig(H)
    rec = np.abs(vecs[i0, :]) ** 2
    nu = int(np.argmax(rec))
    psi2 = np.abs(vecs[:, nu]) ** 2
    flux = 2.0 * float(W @ psi2) / float(psi2.sum())
    eig = -2.0 * float(vals[nu].imag)
    return flux, eig, float(rec[nu]), float(np.sort(rec)[-2])


def traite(cle):
    nom, signe, k = cle
    if M is None:
        init()
    w2 = F(2) + signe * F(k, 100000)
    delta = float(w2) - 2.0
    dabs_exact = float(abs(w2 - 2))
    X = M.X_saut_reel(M.P, 2, 1, 0, 0, w2)
    out = {'w2': str(w2), 'creneau': nom, 'k': k, 'X': X, 'cellules': []}
    for kn, kappa, cible in KAPPAS:
        gstr = '%.5e' % (kappa * dabs_exact * M.P / X)
        gstr_flt = '%.5e' % (kappa * abs(delta) * M.P / X)
        g = float(gstr)
        eta0 = max(dabs_exact, g * X / (M.P * KAPPA3))
        estr = '%.5e' % eta0
        sites = M.barriere(0.0, 0.0, w2, g, True)
        if not sites:
            m_bord, e_bord = 0, 0.0
            sites_t = [(0, 0, abs(M.t_site(0, 0, 0, w2, g)))]
            vide = True
        else:
            m_bord = sites[-1][0]
            S2 = lambda mm: M.Sigma2_site(2 * mm, mm, w2, g)[0]
            e_bord = abs(m_bord * delta + S2(m_bord) - S2(0))
            sites_t = sites
            vide = False
        rc = 2 * (m_bord + max(8, m_bord)) + 2
        cel = {'kappa': kn, 'g': gstr, 'eta0': estr, 'r_c': rc, 'g_diff_flottant': gstr != gstr_flt, 'cible': cible, 'm_bord': m_bord, 'e_bord': e_bord, 'barriere_vide': vide, 'eta0_sur_g': float(estr) / g,
               'eta0_sur_delta': float(estr) / dabs_exact}
        tb = NS['tables_ordre2'](0, 0, w2, g, sites_t, M_facteur=M_FACTEUR)
        t3 = NS['tables_ordre3'](0, 0, w2, g, tb)
        lns, lns_eig, poids, second = [], [], [], []
        defini = True
        for (a, c, L) in VARIANTES:
            H, W, i0 = matrice(tb, t3, m_bord, a, c, L)
            flux, eig, rec, rec2 = largeur(H, W, i0)
            poids.append(rec)
            second.append(rec2)
            if not (flux > 0) or not math.isfinite(flux):
                defini = False
                lns.append(None)
                lns_eig.append(None)
            else:
                lns.append(math.log(flux))
                lns_eig.append(math.log(eig) if eig > 0 else None)
        cel['poids_site0_min'] = min(poids)
        cel['second_poids_max'] = max(second)
        if defini:
            et = max(lns) - min(lns)
            cel['etendue'] = et
            cel['ln_plateau'] = statistics.median(lns)
            cel['G3_plateau'] = math.exp(cel['ln_plateau'])
            cel['ecart_flux_eig_max'] = max(abs(x - y) for x, y in zip(lns, lns_eig)) if all(v is not None for v in lns_eig) else None
            cel['lnG'] = lns
        else:
            cel['etendue'] = None
        cel['eligible'] = bool(m_bord == cible and e_bord < E_BORD_MAX and defini and cel['etendue'] <= ETENDUE_MAX)
        cel['conditions'] = {'i_m_bord_egal_cible': m_bord == cible, 'ii_e_bord_lt_0.7': e_bord < E_BORD_MAX, 'iii_etendue_definie_et_le_0.005': bool(defini and cel['etendue'] <= ETENDUE_MAX)}
        out['cellules'].append(cel)
    out['eligible'] = all(c['eligible'] for c in out['cellules'])
    return out


def main():
    t0 = time.time()
    init()
    taches = [(nom, s, k) for (nom, s, ks) in CRENEAUX for k in ks]
    print('canons des entrees : OK ; %d w2, %d cellules' % (len(taches), len(taches) * len(KAPPAS)), flush=True)
    res = {}
    with Pool(12, initializer=init) as pool:
        for r in pool.imap_unordered(traite, taches):
            res[(r['creneau'], r['k'])] = r
            if len(res) % 10 == 0:
                print('  %d/%d (%.0f s)' % (len(res), len(taches), time.time() - t0), flush=True)
    table = {'creneaux': {}}
    detail = {}
    for nom, s, ks in CRENEAUX:
        cand = []
        for k in sorted(ks, key=lambda x: (x if s > 0 else -x)):       # liste CROISSANTE en w2
            r = res[(nom, k)]
            cand.append({'w2': r['w2'], 'eligible': r['eligible'],
                         'cellules': [{'kappa': c['kappa'], 'g': c['g'], 'eta0': c['eta0'], 'r_c': c['r_c'], 'eligible': c['eligible']} for c in r['cellules']]})
            detail['%s|%d' % (nom, k)] = r
        table['creneaux'][nom] = {'candidats': cand}
    json.dump(table, open(os.path.join(SORTIE, 'table_machine2_sommet_v1.json'), 'w'), indent=1, sort_keys=True)
    json.dump(detail, open(os.path.join(SORTIE, 'detail_machine2_sommet_v1.json'), 'w'), indent=1, sort_keys=True)
    print()
    ntot = nel = 0
    for nom, s, ks in CRENEAUX:
        cs = table['creneaux'][nom]['candidats']
        print('creneau %s : %d w2 eligibles sur %d' % (nom, sum(1 for c in cs if c['eligible']), len(cs)))
        ntot += len(cs)
        nel += sum(1 for c in cs if c['eligible'])
        for c in cs:
            r = [res[(nom, k)] for k in ks if str(F(2) + (1 if s > 0 else -1) * F(k, 100000)) == c['w2']][0]
            print('  %s  ' % ('%.5f' % float(F(c['w2']))) + ' '.join('%.4f' % x['etendue'] if x.get('etendue') is not None else 'indef.' for x in r['cellules']) + ('  ELIGIBLE' if c['eligible'] else '  INELIGIBLE !'))
    print('\nw2 eligibles : %d sur %d ; cellules : %d sur %d' % (nel, ntot, sum(1 for r in res.values() for c in r['cellules'] if c['eligible']), 560))
    print('\npar kappa, sur les 80 w2 :')
    for kn, kappa, cible in KAPPAS:
        cs = [c for r in res.values() for c in r['cellules'] if c['kappa'] == kn]
        print('  kappa %s cible %d  m_bord trouves %s  r_c %s  etendue max %.4f  e_bord max %.3f  poids site 0 min %.4f  g %.5e a %.5e  G3* %.4e a %.4e  eta0/g %.4f a %.4f  eta0/|d| %.3f a %.2f  barriere vide %d'
              % (kn, cible, sorted(set(c['m_bord'] for c in cs)), sorted(set(c['r_c'] for c in cs)), max(c['etendue'] for c in cs), max(c['e_bord'] for c in cs), min(c['poids_site0_min'] for c in cs),
                 min(float(c['g']) for c in cs), max(float(c['g']) for c in cs), min(c['G3_plateau'] for c in cs), max(c['G3_plateau'] for c in cs),
                 min(c['eta0_sur_g'] for c in cs), max(c['eta0_sur_g'] for c in cs), min(c['eta0_sur_delta'] for c in cs), max(c['eta0_sur_delta'] for c in cs), sum(1 for c in cs if c['barriere_vide'])))
    cs = [c for r in res.values() for c in r['cellules']]
    print('\ncouplages ecrits dont l ecriture depend de |delta| calcule en flottant ou en exact :', sum(1 for c in cs if c['g_diff_flottant']))
    print('second plus grand poids du site 0 (parmi les etats propres), maximum sur les 560 cellules x 18 variantes : %.4f' % max(c['second_poids_max'] for c in cs))
    ef = [c['ecart_flux_eig_max'] for c in cs if c.get('ecart_flux_eig_max') is not None]
    print('ecart |ln Gamma_flux - ln Gamma_eig| maximal : %.2e sur %d cellules' % (max(ef), len(ef)))
    print('cellules dont Gamma_eig n est pas strictement positif ou lisible : %d' % sum(1 for c in cs if c.get('ecart_flux_eig_max') is None))
    print('FIN en %.0f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
