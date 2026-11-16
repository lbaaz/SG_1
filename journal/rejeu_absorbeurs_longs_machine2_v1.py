# -*- coding: ascii -*-
"""REJEU (i) de machine 2 : le lecteur creux de machine 2 (lecteur_2D_creux_machine2_v1.py, lot c8164e6d80ee0b60, NON CERTIFIE) sous les
absorbeurs LONGS de la note hors chaine de machine 1 (42c822811167b826), aux SIX points f070 de M17 et au temoin positif H+. HORS CHAINE,
POST HOC, NON OPPOSABLE, classe 3 ; demande par l'operateur le 15/11/2026 ("Oui rejoue"), ce qui leve E19 pour ces seuls calculs.
PERIMETRE (E19) : les six points 1.95, 1.97, 1.98, 2.02, 2.03, 2.05 (39_20, 197_100, 99_50, 101_50, 203_100, 41_20) et le jumeau H+
(j = 6 et j = 8). Aucun point des deltas 96, 97, 98, aucun point neuf, un seul etat par point (l'etat lu) : ce script n'en connait pas d'autre.

Configurations (forme, decalage du bord r_c - r0, longueur L = N - r_c ; N = r0 + decalage + L) :
  note 4 (cinq absorbeurs longs) : F2_60, F2_80, F1_80, F3_60, F1T_60 (F1, r_c = r0 + 10, L = 60) ;
  note 5 (longueurs) : F1_40, F1_60, F2_30, F2_40, F3_30, F3_40 en plus (F1_80, F2_60, F2_80, F3_60 sont deja dans la liste ci-dessus ;
  les lignes de 20 et 30 couches sont des configurations de la nuit bis, deja rejouees par la validation).
Temoin : j = 6 et j = 8, F1 et F2, L = 60 et 80, bord r_c du banc (idr de la sonde etage 1), depart du vide, reference par rotation
complexe (tp_reference_machine2_v1.json, formule rotation-complexe-v1).
Echelle : eta_k = eta0 * 2^(-k) exacte, eta0 du point (sonde etage 2) ; k = -5 a 14 (echelle de la note 4) ; la lecture des plateaux est
donnee sur k = -5..14 (A) et sur k = -5..12 (B, echelle du gel bis), a partir de la MEME trajectoire.

SEUILS ET CONVENTIONS DECLARES AVANT LE PREMIER PASSAGE (rien n'est choisi apres lecture) :
  R1  canons : moteur 82a0be882568fe0c, sonde etage 2 c110c6286157b025, sonde etage 1 1ae4b5b2f9ff0e70, reference TP 4d51dd58ef456fe9 ;
      arret si l'un differe.
  R2  residu du vecteur propre <= 1e-9 a chaque barreau suivi ; ecart relatif entre les deux lectures gamma_E et gamma_W <= 1e-6.
  R3  ancrage stable : E_re de l'etat d'ancrage identique (1e-12) avec K_ANCRE = 80 et avec 160 candidats.
  R4  identite (gel bis 3.9, bloc interieur max(a,b) <= r0) entre l'etat d'ancrage de la configuration et l'etat lu par M17 (F1, G20, k = 3,
      meme ancrage par ma regle 3.7) : >= 0.90 = "meme etat" ; en dessous, la configuration est SIGNALEE, pas ecartee.
  R5  plateau = regle 3.11 du gel bis sur gamma_W (2 eta <W>), lisible si gamma > 1e-12, rationnels exacts, fenetre de cinq k consecutifs,
      meilleure fenetre = plus petit rapport max/min, a egalite le plus petit k de depart ; PLATEAU si rapport <= 21/20.
      Comptes "dans 0.5 %" : (a) plus longue suite de k consecutifs lisibles dont le rapport max/min <= 201/200 ; (b) plus longue suite
      de k consecutifs lisibles tous a moins de 0.5 % de Gamma_pl. Les deux sont donnees ; (a) est le compte retenu pour la comparaison.
  R6  temoin : ecart relatif de gamma_W a la reference, barreau par barreau ; nombre de barreaux consecutifs a moins de 0.5 % de la
      reference en partant de k = -5, et pire ecart sur ces barreaux.
  La valeur rendue pour chaque case est Gamma_pl / (lecture de M17 : gamma de la sonde dense deposee a (F1, G20, k = 3)).
Le comparateur a la note de machine 1 est un second script, ecrit apres ce passage.
Usage (depuis BOCAL4) : py -3.11 -P lecteur_creux_m2/rejeu_absorbeurs_longs_machine2_v1.py <moteur> <sonde_etage2.json> <sonde_etage1.json>
                        <tp_reference.json> <dossier_sortie> [points|-] [configs|-] [avec_tp|sans_tp]"""
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

LC.K_MAX = 14                      # echelle de la note 4 ; ORDRE_K du lecteur s'arrete a 12, on passe la liste explicite
K_MIN, K_MAX = -5, 14
KS = [3] + list(range(4, K_MAX + 1)) + [2, 1, 0, -1, -2, -3, -4, -5]
PLANCHER = 1e-12
CANONS = {'sonde2': 'c110c6286157b025', 'sonde1': '1ae4b5b2f9ff0e70', 'tp_ref': '4d51dd58ef456fe9'}
POINTS = ['39_20', '197_100', '99_50', '101_50', '203_100', '41_20']
# nom : (forme, decalage du bord, longueur)
CONFIGS = {'F2_60': ('F2', 0, 60), 'F2_80': ('F2', 0, 80), 'F1_80': ('F1', 0, 80), 'F3_60': ('F3', 0, 60), 'F1T_60': ('F1', 10, 60),
           'F1_40': ('F1', 0, 40), 'F1_60': ('F1', 0, 60), 'F2_30': ('F2', 0, 30), 'F2_40': ('F2', 0, 40),
           'F3_30': ('F3', 0, 30), 'F3_40': ('F3', 0, 40)}
TP_CONFIGS = {'F1_60': ('F1', 60), 'F2_60': ('F2', 60), 'F1_80': ('F1', 80), 'F2_80': ('F2', 80)}


def plateau(serie, kmax):
    """Regle 3.11 du gel bis sur k = K_MIN..kmax ; serie = {k: gamma ou None}."""
    meilleur = None
    for k0 in range(K_MIN, kmax - 3):
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
    out = {'fenetre': True, 'plateau': bool(r <= Fraction(21, 20)), 'k0': k0, 'etalement': float(r) - 1.0, 'Gamma_pl': gpl}
    ks = [k for k in range(K_MIN, kmax + 1)]
    # (a) plus longue suite dont le rapport max/min <= 201/200
    best_a = 0
    for i in range(len(ks)):
        if serie.get(ks[i]) is None:
            continue
        mx = mn = Fraction(serie[ks[i]])
        n = 1
        for j in range(i + 1, len(ks)):
            v = serie.get(ks[j])
            if v is None:
                break
            f = Fraction(v)
            if max(mx, f) / min(mn, f) > Fraction(201, 200):
                break
            mx, mn = max(mx, f), min(mn, f)
            n += 1
        best_a = max(best_a, n)
    # (b) plus longue suite tous a moins de 0.5 % de Gamma_pl
    best_b, cur = 0, 0
    for k in ks:
        v = serie.get(k)
        if v is not None and abs(v / gpl - 1.0) < 0.005:
            cur += 1
            best_b = max(best_b, cur)
        else:
            cur = 0
    out['compte_a'] = best_a
    out['compte_b'] = best_b
    return out


def series(lect):
    sw, se = {}, {}
    for k in range(K_MIN, K_MAX + 1):
        r = lect.get(k, {'suivi': False})
        ok = bool(r['suivi'])
        sw[k] = r['gamma_W'] if (ok and r['gamma_W'] > PLANCHER) else None
        se[k] = r['gamma_E'] if (ok and r['gamma_E'] > PLANCHER) else None
    return sw, se


def resume(lect):
    """Plateaux (A et B), pires residus et ecarts E/W d'une trajectoire."""
    sw, se = series(lect)
    res = {'plateau_A': plateau(sw, 14), 'plateau_B': plateau(sw, 12), 'plateau_E_A': plateau(se, 14)}
    suivis = [k for k in range(K_MIN, K_MAX + 1) if lect.get(k, {}).get('suivi')]
    res['suivis'] = suivis
    res['perdus'] = [k for k in range(K_MIN, K_MAX + 1) if not lect.get(k, {}).get('suivi')]
    res['pire_residu'] = max(lect[k]['residu'] for k in suivis)
    ew = [abs(lect[k]['gamma_E'] - lect[k]['gamma_W']) / lect[k]['gamma_W'] for k in suivis if lect[k]['gamma_W'] > PLANCHER]
    res['pire_EW'] = max(ew) if ew else None
    res['nb_lisibles'] = sum(1 for k in sw if sw[k] is not None)
    res['p_abs_k3'] = lect[3]['p_abs']
    return res


def tache(arg):
    moteur, f2, f1, nature, nom, N_sel, cfgs, tpref = arg
    LC.K_MAX = 14
    t0 = time.time()
    M = LC.charger_moteur(moteur)
    from fractions import Fraction as Fr
    sortie = {'nature': nature, 'nom': nom, 'N': N_sel, 'configs': {}}
    if nature == 'pt':
        d = json.load(open(f2))['points'][nom]
        r0, eta0 = d['r0'], d['eta0']
        idr = d['cfg']['F1G20']['traj']['3']['identite_reprise']
        w2 = Fr(idr['w2'])
        g, s, signe = idr['g'], idr['s'], idr['signe']
        m17 = d['cfg']['F1G20']['traj']['3']['etats'][0]['gamma']
        sortie['m17_gamma_k3'] = m17
        sortie['r0'] = r0
        # l'etat lu par M17 : meme regle d'ancrage, configuration F1 G20 de la nuit bis
        Nref = idr['N']
        H0r = LC.assembler_H0(M, Nref, w2, g, signe)
        psir = M.graine_coherente(Nref, s, w2)
        Wr = LC.poids_absorbeur('F1', Nref, idr['r_c'])
        lr, v_ref = LC.trajectoire(H0r, Wr, psir, eta0, ks=[3])
        sortie['ref_ancre'] = {'E_re': lr[3]['E_re'], 'gamma_W': lr[3]['gamma_W'], 'rec': lr[3]['recouvrement_graine'],
                               'rec2': lr[3]['recouvrement_second']}
        del H0r, Wr
        H0 = LC.assembler_H0(M, N_sel, w2, g, signe)
        psi = M.graine_coherente(N_sel, s, w2)
        for c in cfgs:
            forme, dec, L = CONFIGS[c]
            r_c = r0 + dec
            assert r_c + L == N_sel
            W = LC.poids_absorbeur(forme, N_sel, r_c)
            lect, v3 = LC.trajectoire(H0, W, psi, eta0, ks=KS)
            lect2, _ = LC.trajectoire(H0, W, psi, eta0, K_ancre=2 * LC.K_ANCRE, ks=[3])
            ident = LC.identite(v_ref, Nref, v3, N_sel, r0)
            a = lect[3]
            sortie['configs'][c] = {'forme': forme, 'r_c': r_c, 'N': N_sel, 'L': L, 'lect': lect, 'identite_M17': ident,
                                    'R3': bool(abs(lect2[3]['E_re'] - lect[3]['E_re']) <= 1e-12), 'E_re_2K': lect2[3]['E_re'],
                                    'ancre': {x: a[x] for x in ('recouvrement_graine', 'recouvrement_second', 'dist_sigma', 'dist_max',
                                                                'somme_rec_candidats', 'sigma', 'E_re')},
                                    'resume': resume(lect)}
    else:                                                       # temoin H+
        e1 = json.load(open(f1))['TP'][nom]
        idr = e1['traj']['F1G20']['3']['identite_reprise']
        w2 = Fr(idr['w2'])
        g, signe, eta0, r_c = idr['g'], idr['signe'], idr['eta0'], idr['r_c']
        ref = [b for b in json.load(open(tpref))['balayage'] if b['j'] == e1['j'] and b.get('raffine')][0]
        sortie.update({'Gamma_ref': ref['Gamma_ref'], 'u_ref': ref['u_ref'], 'r_c': r_c, 'eta0': eta0, 'g': g})
        H0 = LC.assembler_H0(M, N_sel, w2, g, signe)
        psi = np.zeros(N_sel * N_sel)
        psi[0] = 1.0
        for c in cfgs:
            forme, L = TP_CONFIGS[c]
            assert r_c + L == N_sel
            W = LC.poids_absorbeur(forme, N_sel, r_c)
            lect, v3 = LC.trajectoire(H0, W, psi, eta0, ks=KS)
            lect2, _ = LC.trajectoire(H0, W, psi, eta0, K_ancre=2 * LC.K_ANCRE, ks=[3])
            a = lect[3]
            dev = {k: (lect[k]['gamma_W'] / ref['Gamma_ref'] - 1.0) for k in range(K_MIN, K_MAX + 1) if lect.get(k, {}).get('suivi')}
            n_dans, pire = 0, 0.0
            for k in range(K_MIN, K_MAX + 1):
                if k in dev and abs(dev[k]) < 0.005:
                    n_dans += 1
                    pire = max(pire, abs(dev[k]))
                else:
                    break
            sortie['configs'][c] = {'forme': forme, 'r_c': r_c, 'N': N_sel, 'L': L, 'lect': lect, 'ecart_ref': dev,
                                    'consecutifs_depuis_m5': n_dans, 'pire_ecart_consecutifs': pire,
                                    'R3': bool(abs(lect2[3]['E_re'] - lect[3]['E_re']) <= 1e-12), 'E_re_2K': lect2[3]['E_re'],
                                    'ancre': {x: a[x] for x in ('recouvrement_graine', 'recouvrement_second', 'dist_sigma', 'dist_max',
                                                                'somme_rec_candidats', 'sigma', 'E_re')},
                                    'resume': resume(lect)}
    sortie['duree_s'] = round(time.time() - t0, 1)
    return sortie


def main():
    moteur, f2, f1, tpref, sortie = [os.path.abspath(a) for a in sys.argv[1:6]]
    pts = POINTS if len(sys.argv) < 7 or sys.argv[6] == '-' else sys.argv[6].split(',')
    cfgsel = list(CONFIGS) if len(sys.argv) < 8 or sys.argv[7] == '-' else sys.argv[7].split(',')
    avec_tp = not (len(sys.argv) > 8 and sys.argv[8] == 'sans_tp')
    os.makedirs(sortie, exist_ok=True)
    nomlog = 'rejeu_absorbeurs_longs_machine2_v1' + ('' if (len(sys.argv) < 7 or (sys.argv[6:8] == ['-', '-'])) else '_partiel')
    log = open(os.path.join(sortie, nomlog + '.log'), 'w', encoding='ascii', newline='\n')

    def P(*a):
        t = ' '.join(str(x) for x in a)
        print(t)
        log.write(t + '\n')
        log.flush()
    import scipy
    P('REJEU (i) DE MACHINE 2 : absorbeurs longs, six points de M17 et temoin H+ ; HORS CHAINE, POST HOC, NON OPPOSABLE ; lecteur NON CERTIFIE')
    P('python %s, numpy %s, scipy %s' % (sys.version.split()[0], np.__version__, scipy.__version__))
    P('canon du moteur : %s (attendu %s)' % (LC.empreinte_B(moteur), LC.CANON_MOTEUR))
    for nomf, f, att in (('sonde2', f2, CANONS['sonde2']), ('sonde1', f1, CANONS['sonde1']), ('tp_ref', tpref, CANONS['tp_ref'])):
        c = LC.empreinte_B(f)
        P('canon de %s : %s (attendu %s)' % (nomf, c, att))
        if c != att:
            raise SystemExit('ARRET : canon de %s %s, attendu %s' % (nomf, c, att))
    P('perimetre E19 : points %s ; temoin H+ j = 6 et 8 ; configurations %s' % (','.join(pts), ','.join(cfgsel)))
    taches = []
    for p in pts:
        r0 = json.load(open(f2))['points'][p]['r0']
        groupes = {}
        for c in cfgsel:
            forme, dec, L = CONFIGS[c]
            groupes.setdefault(r0 + dec + L, []).append(c)
        for N, cs in groupes.items():
            taches.append((moteur, f2, f1, 'pt', p, N, cs, tpref))
    if avec_tp:
        for jn in ('j06', 'j08'):
            r_c = json.load(open(f1))['TP'][jn]['traj']['F1G20']['3']['identite_reprise']['r_c']
            for L in (60, 80):
                taches.append((moteur, f2, f1, 'tp', jn, r_c + L, [c for c in TP_CONFIGS if TP_CONFIGS[c][1] == L], tpref))
    taches.sort(key=lambda t: -t[5])
    P('taches : %d (les plus grandes d abord)' % len(taches))
    t0 = time.time()
    with multiprocessing.Pool(min(len(taches), 8)) as pool:
        res = pool.map(tache, taches, chunksize=1)
    P('duree totale : %.1f s' % (time.time() - t0))
    ordre = {p: i for i, p in enumerate(POINTS)}
    res.sort(key=lambda r: (r['nature'] != 'pt', ordre.get(r['nom'], 0) if r['nature'] == 'pt' else r['nom'], r['N']))
    R2ok, R3ok = [], []
    for r in res:
        P('')
        P('== %s %s N = %d  (%.1f s)' % (r['nature'], r['nom'], r['N'], r['duree_s']))
        if r['nature'] == 'pt':
            P('   lecture de M17 (sonde dense, F1 G20, k = 3) : %.6e ; mon ancrage de la nuit bis : E_re %.6f, recouvrement %.4f (second %.4f)'
              % (r['m17_gamma_k3'], r['ref_ancre']['E_re'], r['ref_ancre']['rec'], r['ref_ancre']['rec2']))
        else:
            P('   reference Gamma_ref %.6e (incertitude declaree %.2e relatif), bord r_c %d, eta0 %g' % (r['Gamma_ref'], r['u_ref'], r['r_c'], r['eta0']))
        for c, x in r['configs'].items():
            m = x['resume']
            a = x['ancre']
            R2ok.append(m['pire_residu'] <= 1e-9 and (m['pire_EW'] is None or m['pire_EW'] <= 1e-6))
            R3ok.append(x['R3'])
            P('  %-7s %s r_c %d L %d | ancrage k=3 : E_re %.6f rec %.4f second %.4f (rapport %.3f) dist_sigma %.3f/%.2f cand %.3f | R3 %s'
              % (c, x['forme'], x['r_c'], x['L'], a['E_re'], a['recouvrement_graine'], a['recouvrement_second'],
                 a['recouvrement_graine'] / a['recouvrement_second'], a['dist_sigma'], a['dist_max'], a['somme_rec_candidats'], x['R3']))
            if 'identite_M17' in x:
                P('          identite avec l etat de M17 (3.9) : %.6f  %s' % (x['identite_M17'], 'meme etat' if x['identite_M17'] >= 0.90 else 'SIGNALE (< 0.90)'))
            P('          suivis %d sur %d, perdus %s | residu max %.1e | gamma_E vs gamma_W max %s | poids dans l absorbeur (k=3) %.3e'
              % (len(m['suivis']), K_MAX - K_MIN + 1, m['perdus'], m['pire_residu'],
                 ('%.1e' % m['pire_EW']) if m['pire_EW'] is not None else 'n/a', m['p_abs_k3']))
            for tag, pl in (('A (k -5..14)', m['plateau_A']), ('B (k -5..12)', m['plateau_B'])):
                if not pl['fenetre']:
                    P('          plateau %s : aucune fenetre' % tag)
                    continue
                rap = pl['Gamma_pl'] / r['m17_gamma_k3'] if r['nature'] == 'pt' else pl['Gamma_pl'] / r['Gamma_ref']
                P('          plateau %s : %s k0 %d etalement %.3f %% Gamma_pl %.6e | /%s %.4f | dans 0.5 %% : (a) %d (b) %d'
                  % (tag, 'PLATEAU' if pl['plateau'] else 'pas de plateau', pl['k0'], 100 * pl['etalement'], pl['Gamma_pl'],
                     'M17' if r['nature'] == 'pt' else 'ref', rap, pl['compte_a'], pl['compte_b']))
            if r['nature'] == 'tp':
                P('          temoin : %d barreaux consecutifs a moins de 0.5 %% de la reference depuis k = -5, pire ecart %.3f %% ; ecart a k = -5, 0, 3, 6 : %s'
                  % (x['consecutifs_depuis_m5'], 100 * x['pire_ecart_consecutifs'],
                     ' '.join('%+.3f%%' % (100 * x['ecart_ref'][k]) if k in x['ecart_ref'] else 'n/a' for k in (-5, 0, 3, 6))))
    P('')
    P('R2 : %d sur %d configurations ; R3 : %d sur %d' % (sum(R2ok), len(R2ok), sum(R3ok), len(R3ok)))
    json.dump({'declare': {'K_MIN': K_MIN, 'K_MAX': K_MAX, 'PLANCHER': PLANCHER, 'configs': CONFIGS, 'tp_configs': TP_CONFIGS}, 'resultats': res},
              open(os.path.join(sortie, nomlog + '.json'), 'w', encoding='ascii', newline='\n'),
              indent=1, sort_keys=True, default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))
    log.close()


if __name__ == '__main__':
    main()
