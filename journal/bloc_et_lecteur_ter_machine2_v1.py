# -*- coding: ascii -*-
"""LE BLOC DU LECTEUR de machine 1 (9b0f95f3e10e9b0d), eprouve par machine 2 : HORS DES DOUZE POINTS (aucun calcul 2D sous absorbeur long a l'un d'eux).
  B1  le bloc est dans la sonde TEL QUEL (G-T2) : le texte entre les deux marques est le fichier du bloc, octet pour octet ;
  B2  IDENTITE DE MATRICE (G-T8) : assembler + diagonale == H_2D du moteur (eta = 0), dense, N = 36 et 40, signes -1 et +1, w2 et g des deux
      ancres et d'un point juge (seulement la matrice, aucune diagonalisation) ; restreindre(Nmax -> N) == assemblage direct a N ;
  B3  table_W == mon poids_absorbeur (lot c8164e6d80ee0b60) pour F1 et F2 aux quatre geometries du gel, aux tailles reelles ;
  B4  GARDE DE SINGULARITE (M-7, jamais eprouvee par machine 1) : une factorisation qui echoue une fois (puis passe) donne decalage_repris = True
      et la meme largeur ; qui echoue deux fois donne suivi = False, gamma = None ;
  B5  MON LECTEUR (valeurs propres par decalage-inversion, ancrage par recouvrement avec la graine) contre le bloc de machine 1, a l'etat de rang 0
      des deux ancres sous les quatre absorbeurs, et au temoin positif (vide) sous les quatre absorbeurs ; douze barreaux. Les sorties de machine 1
      lues : reference_ancres_ter_machine1_v1.json et essai_m1_sonde_ter_etage1.json ; si fournies, celles de MA passe du pre-vol de SA sonde.
      Seuils declares avant : B2 ecart max <= 1e-15 ; B3 ecart max <= 1e-12 relatif ; B5 ecart relatif de gamma <= 1e-8 a chaque barreau suivi.
Usage : py -3.11 -P bloc_et_lecteur_ter_machine2_v1.py <dossier lot m1> <moteur> <sonde_ordre2.json> <dossier machine 2 (lecteur creux)> <sortie.json> [<prevol>]"""
import importlib.util
import json
import math
import multiprocessing
import os
import sys
import time
from fractions import Fraction as F

os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('MKL_NUM_THREADS', '1')
import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as sl

LOT, MOTEUR, DEPOT, DLEC, SORTIE = [os.path.abspath(a) for a in sys.argv[1:6]]
PREVOL = os.path.abspath(sys.argv[6]) if len(sys.argv) > 6 else None
sys.path.insert(0, DLEC)
import lecteur_2D_creux_machine2_v1 as LC

KS = list(range(-3, 9))
ORDRE = [3, 4, 5, 6, 7, 8, 2, 1, 0, -1, -2, -3]
ABS = [('A', 'F2', 0, 80), ('B', 'F2', 0, 100), ('C', 'F1', 0, 100), ('D', 'F2', 10, 80)]


def charger_bloc(M):
    spec = importlib.util.spec_from_file_location('bloc_m1', os.path.join(LOT, 'lecteur_plateau_bloc_machine1_v1.py'))
    mod = importlib.util.module_from_spec(spec)
    mod.M, mod.np, mod.sp, mod.sl, mod.math = M, np, sp, sl, math      # ce que le bloc dit recevoir de l'appelant
    spec.loader.exec_module(mod)
    return mod


def P(*a):
    print(' '.join(str(x) for x in a), flush=True)


def tache(arg):
    """Mon lecteur sur une trajectoire : ('anc', id, absorbeur) ou ('tp', j, absorbeur)."""
    genre, ident, nom = arg
    LC.K_MAX = 8
    LC.K_MIN = -3
    M = LC.charger_moteur(MOTEUR)
    dep = {p['id']: p for p in json.load(open(DEPOT))['points']}
    forme, dr, L = [(f, d, l) for n, f, d, l in ABS if n == nom][0]
    t0 = time.time()
    if genre == 'anc':
        p = dep[ident]
        r_c, eta0, g = p['r_c'], p['eta0'], p['g']
        w2 = F(int(p['w2'].split('/')[0]), int(p['w2'].split('/')[1]))
        N = r_c + dr + L
        H0 = LC.assembler_H0(M, N, w2, g, -1)
        psi = M.graine_coherente(N, p['s'], w2)
    else:
        retenus = {r['j']: r['g'] for r in json.load(open(os.path.join(os.path.dirname(DEPOT), 'tp_retenus_machine2_v1.json')))['retenus']}
        r_c, eta0, w2 = 40, 0.05, F(39, 20)
        g = retenus[ident]
        N = r_c + dr + L
        H0 = LC.assembler_H0(M, N, w2, g, +1)
        psi = np.zeros(N * N)
        psi[0] = 1.0
    W = LC.poids_absorbeur(forme, N, r_c + dr)
    lect, _ = LC.trajectoire(H0, W, psi, eta0, ks=ORDRE)
    a = lect[3]
    return {'genre': genre, 'id': ident, 'abs': nom, 'N': N, 'lect': {str(k): {'gamma_W': v.get('gamma_W'), 'E_re': v.get('E_re'), 'suivi': v['suivi']}
                                                                       for k, v in lect.items() if k in KS},
            'rec': a['recouvrement_graine'], 'rec2': a['recouvrement_second'], 'duree_s': round(time.time() - t0, 1)}


def main():
    sortie = {}
    M = LC.charger_moteur(MOTEUR)
    P('BLOC ET LECTEUR de machine 1, eprouves par machine 2 ; python %s, numpy %s, scipy %s' % (sys.version.split()[0], np.__version__, scipy.__version__))
    # ---- B1
    bloc_txt = open(os.path.join(LOT, 'lecteur_plateau_bloc_machine1_v1.py'), 'rb').read().decode('utf-8').replace('\r\n', '\n')
    sonde_txt = open(os.path.join(LOT, 'sonde_qualification_EB_ter_machine1_v1.py'), 'rb').read().decode('utf-8').replace('\r\n', '\n')
    i0 = sonde_txt.index('# --- LECTEUR CREUX')
    i1 = sonde_txt.index('# --- fin du bloc ---') + len('# --- fin du bloc ---\n')
    b1 = sonde_txt[i0:i1] == bloc_txt
    P('B1  le bloc est dans la sonde tel quel : %s' % ('OUI' if b1 else 'NON'))
    sortie['B1'] = bool(b1)
    # ---- B2
    B = charger_bloc(M)
    dep = {p['id']: p for p in json.load(open(DEPOT))['points']}
    pire2 = 0.0
    n2 = 0
    for pid in ('A1', 'A2', 'C3'):
        p = dep[pid]
        w2 = F(int(p['w2'].split('/')[0]), int(p['w2'].split('/')[1]))
        for N in (36, 40):
            for signe in (-1, +1):
                Hd, _ = M.H_2D(N, w2, p['g'], signe, 'x5', 0.0, None)
                H0, dg = B.assembler(w2, p['g'], N, signe)
                H1 = H0.toarray() + np.diag(dg)
                ecart = float(np.abs(Hd - H1).max())
                H0m, dm = B.assembler(w2, p['g'], 50, signe)
                H0r, dr_ = B.restreindre(H0m, dm, 50, N)
                ecart_r = float(abs(H0r - H0).max()) if H0r.nnz or H0.nnz else 0.0
                ecart_d = float(np.abs(dr_ - dg).max())
                pire2 = max(pire2, ecart, ecart_r, ecart_d)
                n2 += 1
    P('B2  identite de matrice : %d assemblages (w2, g de A1, A2, C3 ; N 36 et 40 ; signes -1 et +1), ecart max a H_2D, et de restreindre a l assemblage direct : %.2e (seuil 1e-15) : %s'
      % (n2, pire2, 'TIENT' if pire2 <= 1e-15 else 'MORD'))
    sortie['B2'] = {'assemblages': n2, 'ecart_max': pire2}
    # ---- B3
    pire3 = 0.0
    for r_c in (34, 40, 54):
        for nom, forme, dr, L in ABS:
            N = r_c + dr + L
            Wm = B.table_W(N, forme, r_c + dr, L)
            Wl = LC.poids_absorbeur(forme, N, r_c + dr)
            m = float(np.abs(Wm - Wl).max() / max(1.0, np.abs(Wl).max()))
            pire3 = max(pire3, m)
    P('B3  table_W contre mon poids_absorbeur (r_c 34, 40, 54 ; quatre geometries) : ecart relatif max %.2e (seuil 1e-12) : %s' % (pire3, 'TIENT' if pire3 <= 1e-12 else 'MORD'))
    sortie['B3'] = pire3
    # ---- B4 : garde de singularite
    N = 12
    p = dep['A1']
    w2 = F(39, 20)
    H0, dg = B.assembler(w2, p['g'], N, -1)
    W = B.table_W(N, 'F1', 6, 6)
    site = (3, 2)
    Ad = H0.toarray() + np.diag(dg - 1j * 0.02 * W)               # un etat propre exact de cette petite matrice, par decomposition dense
    lam, vec = np.linalg.eig(Ad)
    i = int(np.argmax(np.abs(vec[site[0] * N + site[1], :]) ** 2 / np.sum(np.abs(vec) ** 2, axis=0)))
    E0 = float(lam[i].real) - 1e-3
    ref, _ = B.lire_etat(H0, dg, W, 0.02, N, site, E0 + 1e-3)

    class SLFaux:
        def __init__(self, echecs):
            self.restants = echecs

        def splu(self, A, permc_spec=None):
            if self.restants > 0:
                self.restants -= 1
                raise RuntimeError('Factor is exactly singular')
            return sl.splu(A, permc_spec=permc_spec)
    vrai_sl = B.sl
    B.sl = SLFaux(1)
    r1, _ = B.lire_etat(H0, dg, W, 0.02, N, site, E0 + 1e-3)
    B.sl = SLFaux(2)
    r2, _ = B.lire_etat(H0, dg, W, 0.02, N, site, E0 + 1e-3)
    B.sl = vrai_sl
    ok1 = r1['decalage_repris'] is True and r1['gamma'] is not None and abs(r1['gamma'] / ref['gamma'] - 1.0) < 1e-6 and not ref['decalage_repris']
    ok2 = r2['suivi'] is False and r2['gamma'] is None and r2['decalage_repris'] is True
    P('B4  garde de singularite : un echec -> decalage_repris %s, gamma %.6e contre %.6e sans echec (suivi %s / %s) : %s ; deux echecs -> suivi %s, gamma %s : %s'
      % (r1['decalage_repris'], r1['gamma'], ref['gamma'], r1['suivi'], ref['suivi'], 'TIENT' if ok1 else 'MORD', r2['suivi'], r2['gamma'], 'TIENT' if ok2 else 'MORD'))
    sortie['B4'] = {'un_echec': bool(ok1), 'deux_echecs': bool(ok2)}
    # ---- B5 : mon lecteur contre le bloc
    taches = [('anc', a, n) for a in ('A1', 'A2') for n, _, _, _ in ABS] + [('tp', j, n) for j in (6, 8) for n, _, _, _ in ABS]
    t0 = time.time()
    with multiprocessing.Pool(6) as pool:
        res = pool.map(tache, taches, chunksize=1)
    P('B5  mon lecteur : %d trajectoires en %.0f s' % (len(res), time.time() - t0))
    ref_anc = json.load(open(os.path.join(LOT, 'reference_ancres_ter_machine1_v1.json')))
    ref_e1 = json.load(open(os.path.join(LOT, 'essai_m1_sonde_ter_etage1.json')))
    sources = {'m1 (lot)': (ref_anc, ref_e1)}
    if PREVOL:
        sources['sa sonde, MA passe'] = (json.load(open(os.path.join(PREVOL, 'sonde_ter_ancres.json'))), json.load(open(os.path.join(PREVOL, 'sonde_ter_etage1.json'))))
    sortie['B5'] = {}
    for nomsrc, (anc, e1) in sources.items():
        pire_tot, nmes, hors = 0.0, 0, 0
        P('    contre %s :' % nomsrc)
        for r in res:
            if r['genre'] == 'anc':
                pt = [q for q in anc['points'] if q['id'] == r['id']][0]
                et = [e for e in pt['etats'] if e['rang'] == 0][0]
                traj = et['traj'][r['abs']]
            else:
                v = [q for q in e1['temoin'] if q['j'] == r['id']][0]
                traj = v['traj'][r['abs']]
            pire, n, nh = 0.0, 0, 0
            for k in KS:
                a, b = traj[str(k)], r['lect'][str(k)]
                if a.get('suivi') and b['suivi']:
                    rel = abs(b['gamma_W'] / a['gamma'] - 1.0)
                    pire = max(pire, rel)
                    n += 1
                    nh += rel > 1e-8
                elif bool(a.get('suivi')) != bool(b['suivi']):
                    nh += 1
            pire_tot = max(pire_tot, pire)
            nmes += n
            hors += nh
            P('       %-3s %-2s %-2s N %3d : %2d barreaux suivis des deux cotes, ecart relatif max %.2e, hors seuil %d ; recouvrement graine %.4f / second %.4f (%.1f s)'
              % (r['genre'], r['id'], r['abs'], r['N'], n, pire, nh, r['rec'], r['rec2'], r['duree_s']))
        P('    BILAN contre %s : %d lectures comparees, ecart relatif max %.2e, hors du seuil 1e-8 : %d : %s' % (nomsrc, nmes, pire_tot, hors, 'TIENT' if hors == 0 else 'MORD'))
        sortie['B5'][nomsrc] = {'lectures': nmes, 'ecart_max': pire_tot, 'hors': hors}
    json.dump(sortie, open(SORTIE, 'w'), indent=1, sort_keys=True)


if __name__ == '__main__':
    main()
