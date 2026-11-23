# -*- coding: ascii -*-
"""EPREUVE "Q" (QUALIFICATION DU LECTEUR CREUX AU SOMMET) demandee par machine 1 (22g, lot 423ec0fd24240977, note section 8) -- machine 2, 2026-11-22, hors chaine (classe 3) : AUCUN verdict de gel, AUCUN gel, AUCUN depot.
CE FICHIER EST ECRIT AVANT TOUTE LECTURE 2D AUX CINQ POINTS DE Q (je n'ai lu aucune sortie de Qa, Qc, Qd, Qe, Qf ; l'ordre de l'operateur est a citer dans l'enveloppe).
LES LECTURES sont faites par mon pilote lecteur_2D_pilote_machine2_v1.py (47a84eae6052f006, NON EDITE) : bloc LECTEUR CREUX de la sonde deposee d5cc48f48e37af99, moteur 82a0be882568fe0c, site (0, 0), energie de depart 0, signe -1 (fantome) puis +1 (jumeau),
quatre absorbeurs A (F2, bord r_c, 80), B (F2, r_c, 100), C (F1, r_c, 100), D (F2, r_c + 10, 80), douze barreaux k = -3 a 8, eta_k = eta0 2^(-k), r_c = 18 (= 2 (0 + max(8, 0)) + 2). UNE SEULE chose change par rapport au depot : eta0 = g X(w2) / (P kappa_3).
LES eta0 sont les siens, que j'ai recalcules (eta0_Q_machine2_v1.py : ecart relatif 0 aux cinq points, six chiffres). LE JUGE est la feuille deposee 83701094e6a2b965, fonction juger_etat, TELLE QUELLE, importee sans edition (canon controle ci-dessous) ;
sa tolerance de plateau est la sienne (5 pour cent, etalement 1.05) -- celle du depot, pas ma tolerance 1.25 des epreuves T. Pas de valeur du depot a ces points : g_dep3 = None (la lecture "lu sur le plateau" de la feuille n'est donc PAS evaluee).
SES ATTENDUS (note section 8.3, que je prends a la lettre, ecrits par elle avant) :
  Q-1  les cinq points sont QUALIFIES par juger_etat (fantome).
  Q-2  a chaque point qualifie, |ln(Gamma_pl / G3*)| <= 0.010, Gamma_pl = plateau de l'absorbeur A (celui de la feuille) ; G3* = 1.36076e-05, 5.44311e-05, 1.08861e-04, 1.20924e-05, 2.91470e-06 (Qa, Qc, Qd, Qe, Qf).
  Q-3  le temoin (jumeau) tient aux cinq points : 48 lectures suivies sur 48 ET plus grande largeur lue <= 1e-6 Gamma_pl.
  Q-4  fenetres retenues (k0) aux vingt (point, absorbeur) : A et B a k0 dans {-2, -1, 0} ; C dans {0, 1, 2} ; D dans {-3, -2, -1} ; au moins 16 sur 20 (une fenetre n'est retenue que si le statut est PLATEAU).
  Q-5  si Qa et Qd sont qualifies : |ln[(Gamma_pl / g)(Qd) / (Gamma_pl / g)(Qa)]| <= 0.005.
  SON "TORT" : un point qualifie ou |ln(Gamma_pl / G3*)| > 0.020 ; OU deux points ou plus sans plateau sous A.
MES REGLES, FIXEES ICI AVANT TOUT RESULTAT, que je n'ajusterai pas apres :
  (R1) CONTROLE : canons du moteur, du bloc, du pilote (47a84eae6052f006) et de la feuille (83701094e6a2b965) controles ; chaque JSON porte son eta0 attendu, r_c = 18, les quatre absorbeurs a la geometrie du depot (A 80 couches bord 18, B 100 bord 18, C 100 bord 18 F1, D 80 bord 28), les douze barreaux ; sinon RIEN ne se lit.
  (R2) UN attendu Q-i est dit TENU si et seulement s'il l'est a TOUS les cas qu'il vise, bornes incluses, par ma lecture du JSON et la feuille deposee ; sinon NON TENU, avec le cas. Q-2 et Q-5 sont dits "non evaluables" aux points non qualifies (Q-5 : si Qa ou Qd ne l'est pas) -- jamais bornes.
  (R3) Son tort est dit REALISE a la lettre, ou NON REALISE ; je ne mets pas d'autre seuil.
  (R4) SANS JUGEMENT, rapporte : Gamma_pl / g et Gamma_pl / t_0 (t_0 = g X(w2) / P) aux cinq points ; pour chaque absorbeur : statut, k0, etalement, Gamma_pl / G3* ; les ecarts ln(B, C, D / A) ; le poids du site (0, 0) minimal dans la fenetre retenue de A ; Gamma(k) / G3* sous A aux douze barreaux ; les largeurs du jumeau.
  (R5) Ce que Q ne dit pas, a ecrire dans la note : cinq points sacrifies, delta = 0 et 1e-4 seulement, profondeurs 1 et 2 non lues, delta < 0 non lu, aucune cellule d'un gel relue.
Usage : py -3.11 -P epreuve_Q_sommet_machine2_v1.py <dossier des lect2D_Q*.json> <feuille deposee lecture_lecteur_gel_loi_machine1_v1.py> <moteur m17_chaine_v17.py>"""
import hashlib
import importlib.util
import json
import math
import os
import sys
import unicodedata

DOS, FEUILLE, MOTEUR = sys.argv[1], sys.argv[2], sys.argv[3]
ICI = os.path.dirname(os.path.abspath(__file__))


def canon_B(chemin):
    t = unicodedata.normalize('NFC', open(chemin, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


for chemin, att, quoi in ((FEUILLE, '83701094e6a2b965', 'feuille'), (MOTEUR, '82a0be882568fe0c', 'moteur'), (os.path.join(ICI, 'lecteur_2D_pilote_machine2_v1.py'), '47a84eae6052f006', 'pilote')):
    if canon_B(chemin) != att:
        raise SystemExit('REFUS : canon de %s = %s, attendu %s' % (quoi, canon_B(chemin), att))
spec = importlib.util.spec_from_file_location('feuille', FEUILLE)
FE = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FE)
# t_0 = g X(w2) / P : X du moteur, P = 5 (lecture seule)
specm = importlib.util.spec_from_file_location('moteur', MOTEUR)
M = importlib.util.module_from_spec(specm)
specm.loader.exec_module(M)
from fractions import Fraction as F  # noqa: E402

PTS = [('Qa', 'Q-a', F(2), 2.5e-4, 9.73875e-04, 1.36076e-05), ('Qc', 'Q-c', F(2), 1e-3, 3.89550e-03, 5.44311e-05), ('Qd', 'Q-d', F(2), 2e-3, 7.79100e-03, 1.08861e-04),
       ('Qe', 'Q-e', F(20001, 10000), 3e-4, 1.16821e-03, 1.20924e-05), ('Qf', 'Q-f', F(20001, 10000), 1.5e-4, 5.84106e-04, 2.91470e-06)]
GEO = {'A': ('F2', 18, 80), 'B': ('F2', 18, 100), 'C': ('F1', 18, 100), 'D': ('F2', 28, 80)}
KS = list(range(-3, 9))
FEN_OK = {'A': (-2, -1, 0), 'B': (-2, -1, 0), 'C': (0, 1, 2), 'D': (-3, -2, -1)}
manque, bad = [], []
LU = {}
for ident, nom, w2, g, eta0, g3 in PTS:
    LU[ident] = {}
    for qui in ('fantome', 'jumeau'):
        p = os.path.join(DOS, 'lect2D_%s_%s.json' % (ident, qui))
        if not os.path.isfile(p):
            manque.append(p)
            continue
        d = json.load(open(p))
        LU[ident][qui] = d
        c = d['cellule']
        r = d['reglage']
        ok = (d['moteur_canon'] == '82a0be882568fe0c' and d['source_bloc_canon'] == 'd5cc48f48e37af99' and d['pilote_canon'] == '47a84eae6052f006'
              and F(c['w2']) == w2 and float(c['g']) == g and c['m'] == 0 and abs(c['eta0'] - eta0) <= 1e-12 * eta0 and c['r_c'] == 18 and r['ks'] == KS
              and sorted(d['lecture']['absorbeurs']) == ['A', 'B', 'C', 'D'] and all((x['forme'], x['bord'], x['couches']) == GEO[a] for a, x in d['lecture']['absorbeurs'].items())
              and d['lecture']['signe'] == (-1 if qui == 'fantome' else 1) and d['lecture']['site'] == [0, 0] and d['lecture']['E_depart'] == 0.0)
        if not ok:
            bad.append((ident, qui))
if manque or bad:
    print('R1 NON TENU : fichiers manquants %s ; en-tetes hors regle %s' % (manque, bad))
    raise SystemExit(1)
print('R1 TENU : 10 JSON (cinq points x fantome, jumeau), canons moteur/bloc/pilote/feuille controles, eta0 et geometrie du depot.\n')

R = {}
for ident, nom, w2, g, eta0, g3 in PTS:
    traj = LU[ident]['fantome']['lecture']['traj']
    J = FE.juger_etat({x: traj[x] for x in 'ABCD'}, None)
    tw = LU[ident]['jumeau']['lecture']['traj']
    nsuivi = sum(1 for x in 'ABCD' for k in KS if tw[x][str(k)]['suivi'])
    gam_tw = [abs(tw[x][str(k)]['gamma']) for x in 'ABCD' for k in KS if tw[x][str(k)]['suivi'] and tw[x][str(k)]['gamma'] is not None]
    PA = J['plateaux']['A']
    gpl = PA.get('Gamma_pl') if PA['statut'] == 'PLATEAU' else None
    X = M.X_saut_reel(5, 2, 1, 0, 0, w2)
    R[ident] = {'nom': nom, 'J': J, 'gpl': gpl, 'g': g, 'g3': g3, 'nsuivi_tw': nsuivi, 'maxtw': max(gam_tw) if gam_tw else None, 't0': g * X / 5.0, 'traj': traj}
    print('=== %s  w2 = %s  g = %.3g  eta0 = %.5e  statut %s ; non lisibles %s ; echecs %s' % (nom, w2, g, eta0, J['statut'], J['non_lisibles'], J['echecs']))
    for x in 'ABCD':
        P = J['plateaux'][x]
        if P['statut'] == 'AUCUNE FENETRE':
            print('   %s : AUCUNE FENETRE' % x)
            continue
        print('   %s : %-15s k0 = %+d  etalement %.4f  Gamma_pl = %.5e  Gamma_pl / G3* = %.4f  (ecart ln A : %s)' % (x, P['statut'], P['k0'], P['etalement'], P['Gamma_pl'], P['Gamma_pl'] / g3, ('%.4f' % P['ecart_ln_A']) if 'ecart_ln_A' in P else '-'))
    if gpl:
        k0 = PA['k0']
        pw = min(traj['A'][str(k)]['poids_site'] for k in range(k0, k0 + 5))
        print('   Gamma_pl(A) / g = %.6f ; / t_0 = %.6f ; ln(Gamma_pl / G3*) = %+.5f ; poids du site (0, 0) mini dans la fenetre de A : %.4f' % (gpl / g, gpl / R[ident]['t0'], math.log(gpl / g3), pw))
    print('   Gamma(k) / G3* sous A, k = -3..8 : %s' % ' '.join(('%.3f' % (traj['A'][str(k)]['gamma'] / g3)) if traj['A'][str(k)]['suivi'] and traj['A'][str(k)]['gamma'] else '  -  ' for k in KS))
    print('   jumeau : %d lectures suivies sur 48 ; plus grande largeur %.3e%s' % (nsuivi, R[ident]['maxtw'] or float('nan'), (' (= %.2e Gamma_pl)' % (R[ident]['maxtw'] / gpl)) if gpl and R[ident]['maxtw'] is not None else ''))
print('\n=== LES ATTENDUS DE MACHINE 1')
q1 = all(R[i]['J']['statut'] == 'QUALIFIE' for i, *_ in PTS)
print('Q-1  cinq points QUALIFIES : %s   (%s)' % ('TENU' if q1 else 'NON TENU', ' ; '.join('%s %s' % (R[i]['nom'], R[i]['J']['statut']) for i, *_ in PTS)))
qual = [i for i, *_ in PTS if R[i]['J']['statut'] == 'QUALIFIE' and R[i]['gpl']]
ec2 = {i: abs(math.log(R[i]['gpl'] / R[i]['g3'])) for i in qual}
q2 = bool(qual) and all(v <= 0.010 for v in ec2.values())
print('Q-2  |ln(Gamma_pl / G3*)| <= 0.010 aux points qualifies : %s   (%s ; %d points qualifies sur 5%s)' % ('TENU' if q2 and len(qual) == 5 else ('TENU sur les points qualifies seulement' if q2 else 'NON TENU'), ' ; '.join('%s %.5f' % (R[i]['nom'], v) for i, v in ec2.items()), len(qual), '' if len(qual) == 5 else ' : non evaluable aux autres'))
q3 = all(R[i]['nsuivi_tw'] == 48 and R[i]['gpl'] and R[i]['maxtw'] is not None and R[i]['maxtw'] <= 1e-6 * R[i]['gpl'] for i, *_ in PTS)
print('Q-3  temoin (jumeau) : 48 lectures suivies et largeur <= 1e-6 Gamma_pl aux cinq points : %s' % ('TENU' if q3 else 'NON TENU'))
nf, tot = 0, 0
det = []
for i, *_ in PTS:
    for x in 'ABCD':
        P = R[i]['J']['plateaux'][x]
        tot += 1
        okf = P['statut'] == 'PLATEAU' and P['k0'] in FEN_OK[x]
        nf += okf
        det.append('%s%s:%s' % (R[i]['nom'][2:], x, ('%+d' % P['k0']) if P['statut'] != 'AUCUNE FENETRE' and P['statut'] == 'PLATEAU' else 'x'))
print('Q-4  fenetres retenues dans les listes de sa note : %d sur %d (il en faut 16) : %s   [%s]' % (nf, tot, 'TENU' if nf >= 16 else 'NON TENU', ' '.join(det)))
if 'Qa' in qual and 'Qd' in qual:
    v = abs(math.log((R['Qd']['gpl'] / R['Qd']['g']) / (R['Qa']['gpl'] / R['Qa']['g'])))
    print('Q-5  |ln[(Gamma_pl / g)(Q-d) / (Gamma_pl / g)(Q-a)]| = %.5f (<= 0.005) : %s' % (v, 'TENU' if v <= 0.005 else 'NON TENU'))
else:
    print('Q-5  non evaluable (Q-a ou Q-d non qualifie)')
tort1 = [i for i in qual if ec2[i] > 0.020]
sans = [i for i, *_ in PTS if R[i]['J']['plateaux']['A']['statut'] != 'PLATEAU']
print('SON TORT : point qualifie a |ln| > 0.020 : %s ; points sans plateau sous A : %s -> %s' % (tort1 or 'aucun', sans or 'aucun', 'REALISE' if (tort1 or len(sans) >= 2) else 'NON REALISE'))
print('\nCe que Q ne dit pas : cinq points sacrifies, delta = 0 et 1e-4 seulement, profondeurs 1 et 2 non lues, delta < 0 non lu, aucune cellule d un gel relue.')
