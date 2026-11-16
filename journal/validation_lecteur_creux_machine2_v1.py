# -*- coding: ascii -*-
"""VALIDATION du lecteur 2D creux de machine 2 (lecteur_2D_creux_machine2_v1.py) CONTRE LA SONDE DENSE DEPOSEE (nuit bis). HORS CHAINE.

Rien n'est calcule hors des configurations que la nuit bis a jouees (F1 G20, F1 G30, F1 GT, F2 G20, F3 G20 aux six points f070 de M17 ;
le jumeau H+ j = 6 et j = 8 en F1 G20 et G30) : aucun absorbeur long, aucun point neuf (E19 : ce qui s'ecrit ici ne brule aucun point).
Les references sont les deux sorties de la sonde dense deposees au registre (lots a01598ec24237921 : etage 2 et etage 1), canon verifie.

SEUILS DECLARES AVANT LE PREMIER PASSAGE (aucun n'est choisi apres lecture ; ce sont des seuils d'outil, pas ceux d'un gel) :
  V1  H0 creux - i eta W_F1 == H_2D(N, w2, g, signe, 'x5', eta, r_c) du moteur, element par element (G-Q3) : ecart max <= 1e-15
  V2  memes barreaux suivis que la sonde dense a chaque (point, configuration, k)
  V3  energie de l'etat lu : |E_re - E_re dense| <= 1e-8 a chaque barreau suivi
  V4  largeur : |gamma - gamma dense| <= 0.01 * gamma dense + 5e-13 a chaque barreau suivi ; gamma est gamma_W (2 eta <W>) ; gamma_E
      (-2 Im E) est consignee a cote, avec son ecart a gamma_W
  V5  plateau (gel bis 3.11, en rationnels exacts) : meme verdict, meme depart k0, Gamma_pl a 0.01 pres, par (point, configuration)
  V6  identite entre configurations (3.9) : |identite - identite dense| <= 1e-6
  V7  residu du vecteur propre <= 1e-9 (norme L2, vecteur norme) a chaque barreau suivi
  V8  l'ancrage est le meme avec K_ANCRE et 2 K_ANCRE candidats (ancrage non tributaire du nombre de candidats)
Usage (depuis BOCAL4) : python -P lecteur_creux_m2/validation_lecteur_creux_machine2_v1.py <moteur> <sonde_etage2.json> <sonde_etage1.json> <dossier_sortie> [point ...]"""
import os
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('MKL_NUM_THREADS', '1')
import json
import math
import multiprocessing
import sys
import time
from fractions import Fraction

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import numpy as np
import lecteur_2D_creux_machine2_v1 as LC

PLANCHER = 1e-12
CONFIGS = ('F1G20', 'F1G30', 'F1GT', 'F2G20', 'F3G20')
SEUILS = {'V1': 1e-15, 'V3': 1e-8, 'V4_rel': 0.01, 'V4_abs': 5e-13, 'V5_gpl': 0.01, 'V6': 1e-6, 'V7': 1e-9}


def plateau(serie):
    """Gel bis 3.11 : serie = {k: gamma ou None (non lisible)} ; fenetre = cinq k consecutifs lisibles ; rapport max/min en
    rationnels exacts ; PLATEAU si rapport <= 21/20 ; retenue = plus petit rapport, a egalite le plus petit k de depart."""
    meilleur = None
    for k0 in range(LC.K_MIN, LC.K_MAX - 3):
        vals = [serie.get(k) for k in range(k0, k0 + 5)]
        if any(v is None for v in vals):
            continue
        fr = [Fraction(v) for v in vals]
        r = max(fr) / min(fr)
        if meilleur is None or r < meilleur[0]:
            meilleur = (r, k0, vals)
    if meilleur is None:
        return {'fenetre': False}
    r, k0, vals = meilleur
    gpl = math.exp(sum(math.log(v) for v in vals) / 5.0)
    return {'fenetre': True, 'plateau': bool(r <= Fraction(21, 20)), 'k0': k0, 'etalement': float(r) - 1.0, 'Gamma_pl': gpl}


def serie_dense(traj):
    s, suivis = {}, {}
    for ks, rec in traj.items():
        k = int(ks)
        e = rec.get('etats') or []
        ok = bool((not rec.get('saute')) and e and e[0].get('suivi'))
        suivis[k] = ok
        s[k] = e[0]['gamma'] if (ok and e[0]['gamma'] > PLANCHER) else None
    return s, suivis


def comparer(nom, traj_dense, lect, identite_dense=None, identite_mienne=None):
    """Compare une configuration : rend les lignes par barreau et les pires ecarts."""
    sd, suivis_d = serie_dense(traj_dense)
    lignes, pire = [], {'V3': 0.0, 'V4': 0.0, 'V4rel': 0.0, 'V7': 0.0, 'EW': 0.0}
    v2 = True
    sm_w, sm_e = {}, {}
    for k in range(LC.K_MIN, LC.K_MAX + 1):
        r = lect.get(k, {'suivi': False})
        d = traj_dense[str(k)]['etats'][0] if suivis_d.get(k) else None
        if bool(r['suivi']) != bool(suivis_d.get(k)):
            v2 = False
        if r['suivi']:
            sm_w[k] = r['gamma_W'] if r['gamma_W'] > PLANCHER else None
            sm_e[k] = r['gamma_E'] if r['gamma_E'] > PLANCHER else None
        else:
            sm_w[k] = sm_e[k] = None
        if r['suivi'] and d is not None:
            dE = abs(r['E_re'] - d['E_re'])
            dg = abs(r['gamma_W'] - d['gamma'])
            rel = dg / d['gamma'] if d['gamma'] else float('inf')
            # ecart a la tolerance declaree, pour le pire en valeur de tolerance
            marge = dg / (SEUILS['V4_rel'] * d['gamma'] + SEUILS['V4_abs'])
            pire['V3'] = max(pire['V3'], dE)
            pire['V4'] = max(pire['V4'], marge)
            if d['gamma'] > PLANCHER:
                pire['V4rel'] = max(pire['V4rel'], rel)
            pire['V7'] = max(pire['V7'], r['residu'])
            if r['gamma_W'] > PLANCHER:
                pire['EW'] = max(pire['EW'], abs(r['gamma_E'] - r['gamma_W']) / r['gamma_W'])
            lignes.append({'k': k, 'E_re': r['E_re'], 'E_re_dense': d['E_re'], 'gamma_W': r['gamma_W'], 'gamma_E': r['gamma_E'],
                           'gamma_dense': d['gamma'], 'rel_W': rel, 'marge_V4': marge, 'residu': r['residu'], 'ov': r['ov'],
                           'p_abs': r['p_abs']})
        else:
            lignes.append({'k': k, 'suivi_mien': bool(r['suivi']), 'suivi_dense': bool(suivis_d.get(k))})
    pd, pw, pe = plateau(sd), plateau(sm_w), plateau(sm_e)
    v5 = (pd['fenetre'] == pw['fenetre']) and (not pd['fenetre'] or (pd['plateau'] == pw['plateau'] and pd['k0'] == pw['k0'] and
          abs(pw['Gamma_pl'] / pd['Gamma_pl'] - 1.0) <= SEUILS['V5_gpl']))
    v6 = True if identite_dense is None else abs(identite_mienne - identite_dense) <= SEUILS['V6']
    return {'nom': nom, 'lignes': lignes, 'pire': pire, 'V2': v2, 'V3': pire['V3'] <= SEUILS['V3'], 'V4': pire['V4'] <= 1.0,
            'V5': bool(v5), 'V6': bool(v6), 'V7': pire['V7'] <= SEUILS['V7'], 'plateau_dense': pd, 'plateau_W': pw, 'plateau_E': pe,
            'identite_dense': identite_dense, 'identite_mienne': identite_mienne}


def tache(arg):
    """Un travail par processus : un point f070 (cinq configurations de la nuit bis) ou un couple (jumeau H+, geometrie)."""
    moteur, f2, f1, genre, nom = arg
    t0 = time.time()
    M = LC.charger_moteur(moteur)
    from fractions import Fraction as Fr
    sortie = {'genre': genre, 'nom': nom, 'configs': {}}
    if genre == 'pt':
        d = json.load(open(f2))['points'][nom]
        etat = {}
        for cfg in CONFIGS:
            tr = d['cfg'][cfg]['traj']
            idr = tr['3']['identite_reprise']
            w2 = Fr(idr['w2'])
            N, r_c, g, s, forme = idr['N'], idr['r_c'], idr['g'], idr['s'], idr['forme']
            if N not in etat:
                etat[N] = (LC.assembler_H0(M, N, w2, g, idr['signe']), M.graine_coherente(N, s, w2))
            H0, psi = etat[N]
            W = LC.poids_absorbeur(forme, N, r_c)
            if cfg == 'F1G20':                                   # V1 : G-Q3, a k = 3
                eta3 = d['eta0'] * 2.0 ** (-3)
                Hd, _ = M.H_2D(N, w2, g, idr['signe'], 'x5', eta3, r_c)
                Hd -= (H0 + LC.sp.diags(-1j * eta3 * W)).toarray()          # en place : un seul tableau dense de plus
                sortie['V1_ecart_max'] = float(np.abs(Hd).max())
                del Hd
            lect, v3 = LC.trajectoire(H0, W, psi, d['eta0'])
            lect2, _ = LC.trajectoire(H0, W, psi, d['eta0'], K_ancre=2 * LC.K_ANCRE, ks=[3])   # V8
            etat[(cfg, 'v3')] = (v3, N)
            sortie['configs'][cfg] = {'lect': lect, 'N': N, 'r_c': r_c, 'forme': forme,
                                      'V8': bool(abs(lect2[3]['E_re'] - lect[3]['E_re']) <= 1e-12), 'ancre_E_re_2K': lect2[3]['E_re'],
                                      'ancre': {x: lect[3][x] for x in ('recouvrement_graine', 'recouvrement_second', 'dist_sigma', 'dist_max',
                                                                        'somme_rec_candidats', 'sigma', 'E_re')}}
        r0 = d['r0']
        v_ref, N_ref = etat[('F1G20', 'v3')]
        for cfg in CONFIGS:
            tr = d['cfg'][cfg]['traj']
            v3, N = etat[(cfg, 'v3')]
            ident = 1.0 if cfg == 'F1G20' else LC.identite(v_ref, N_ref, v3, N, r0)
            sortie['configs'][cfg]['cmp'] = comparer(cfg, tr, sortie['configs'][cfg]['lect'], d['cfg'][cfg].get('identite'), ident)
            del sortie['configs'][cfg]['lect']
    else:                                                       # jumeau H+ : nom = 'j06_F1G20' etc.
        jn, cfg = nom.split('_')
        d = json.load(open(f1))['TP'][jn]
        tr = d['traj'][cfg]
        idr = tr['3']['identite_reprise']
        w2 = Fr(idr['w2'])
        N, r_c, g, forme = idr['N'], idr['r_c'], idr['g'], idr['forme']
        H0 = LC.assembler_H0(M, N, w2, g, idr['signe'])
        psi = np.zeros(N * N)
        psi[0] = 1.0                                            # le vide de Fock |0, 0>, indice a = 0, b = 0
        W = LC.poids_absorbeur(forme, N, r_c)
        lect, _ = LC.trajectoire(H0, W, psi, idr['eta0'])
        sortie['configs'][cfg] = {'cmp': comparer(nom, tr, lect), 'N': N, 'r_c': r_c, 'forme': forme}
    sortie['duree_s'] = round(time.time() - t0, 1)
    return sortie


def main():
    moteur, f2, f1, sortie = [os.path.abspath(a) for a in sys.argv[1:5]]
    points = sys.argv[5:] or ['39_20', '41_20', '99_50', '101_50', '197_100', '203_100']
    os.makedirs(sortie, exist_ok=True)
    log = open(os.path.join(sortie, 'validation_lecteur_creux_machine2_v1.log'), 'w', encoding='ascii', newline='\n')

    def P(*a):
        t = ' '.join(str(x) for x in a)
        print(t)
        log.write(t + '\n')
        log.flush()
    P('VALIDATION DU LECTEUR CREUX DE MACHINE 2 (v1), HORS CHAINE, NON CERTIFIEE ; contre la sonde dense deposee')
    import scipy
    P('python %s, numpy %s, scipy %s' % (sys.version.split()[0], np.__version__, scipy.__version__))
    P('canon du moteur : %s (attendu %s)' % (LC.empreinte_B(moteur), LC.CANON_MOTEUR))
    for nomf, f in (('sonde etage 2', f2), ('sonde etage 1', f1)):
        P('canon de la %s : %s' % (nomf, LC.empreinte_B(f)))
    P('seuils declares avant le premier passage : %s' % json.dumps(SEUILS, sort_keys=True))
    taches = [(moteur, f2, f1, 'pt', p) for p in points]
    if not sys.argv[5:]:
        taches += [(moteur, f2, f1, 'tp', '%s_%s' % (j, c)) for j in ('j06', 'j08') for c in ('F1G20', 'F1G30')]
    t0 = time.time()
    with multiprocessing.Pool(min(len(taches), 10)) as pool:
        res = pool.map(tache, taches)
    P('duree totale : %.1f s' % (time.time() - t0))
    tot = {'V1': [], 'V2': [], 'V3': [], 'V4': [], 'V5': [], 'V6': [], 'V7': [], 'V8': []}
    for r in res:
        P('')
        P('== %s %s  (%.1f s)' % (r['genre'], r['nom'], r['duree_s']))
        if 'V1_ecart_max' in r:
            ok = r['V1_ecart_max'] <= SEUILS['V1']
            tot['V1'].append(ok)
            P('  V1 H0 creux - i eta W_F1 contre H_2D du moteur, k = 3, G20 : ecart max %.3e  %s' % (r['V1_ecart_max'], 'PASSE' if ok else 'MORD'))
        for cfg, c in r['configs'].items():
            m = c['cmp']
            for v in ('V2', 'V3', 'V4', 'V5', 'V6', 'V7'):
                tot[v].append(m[v])
            if 'V8' in c:
                tot['V8'].append(c['V8'])
            pd, pw = m['plateau_dense'], m['plateau_W']
            P('  %-6s  V2 %-5s V3 %-5s V4 %-5s V5 %-5s V6 %-5s V7 %-5s%s | pire dE_re %.1e | pire dgamma/tol %.2f (rel %.2e) | gW vs gE %.1e | residu %.1e'
              % (cfg, m['V2'], m['V3'], m['V4'], m['V5'], m['V6'], m['V7'], (' V8 %s' % c['V8']) if 'V8' in c else '',
                 m['pire']['V3'], m['pire']['V4'], m['pire']['V4rel'], m['pire']['EW'], m['pire']['V7']))
            P('          plateau dense : %s | mien : %s' % (
                ('PLATEAU k0=%d etal=%.3f%% Gpl=%.6e' % (pd['k0'], 100 * pd['etalement'], pd['Gamma_pl']) if pd['fenetre'] and pd['plateau']
                 else ('pas de plateau, meilleur etal=%.3f%%' % (100 * pd['etalement']) if pd['fenetre'] else 'aucune fenetre')),
                ('PLATEAU k0=%d etal=%.3f%% Gpl=%.6e' % (pw['k0'], 100 * pw['etalement'], pw['Gamma_pl']) if pw['fenetre'] and pw['plateau']
                 else ('pas de plateau, meilleur etal=%.3f%%' % (100 * pw['etalement']) if pw['fenetre'] else 'aucune fenetre'))))
            if m['identite_dense'] is not None:
                P('          identite (3.9) : dense %.6f  mienne %.6f' % (m['identite_dense'], m['identite_mienne']))
            if 'ancre' in c:
                a = c['ancre']
                P('          ancrage (3.7) : recouvrement avec la graine %.4f, second %.4f (rapport %.3f) ; etat a %.3f de sigma, candidats jusqu a %.2f ; '
                  'somme des recouvrements des %d candidats %.3f' % (a['recouvrement_graine'], a['recouvrement_second'],
                                                                      a['recouvrement_graine'] / a['recouvrement_second'], a['dist_sigma'], a['dist_max'],
                                                                      LC.K_ANCRE, a['somme_rec_candidats']))
    P('')
    for v in ('V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'):
        P('TOTAL %s : %d sur %d' % (v, sum(tot[v]), len(tot[v])))
    allok = all(all(x) for x in tot.values())
    P('TOUTES LES EPREUVES PASSENT' if allok else 'AU MOINS UNE EPREUVE MORD')
    json.dump({'seuils': SEUILS, 'resultats': res, 'totaux': {k: [sum(v), len(v)] for k, v in tot.items()}},
              open(os.path.join(sortie, 'validation_lecteur_creux_machine2_v1.json'), 'w', encoding='ascii', newline='\n'),
              indent=1, sort_keys=True, default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))
    log.close()
    sys.exit(0 if allok else 1)


if __name__ == '__main__':
    main()
