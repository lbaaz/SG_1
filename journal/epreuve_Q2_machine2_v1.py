# -*- coding: ascii -*-
"""EPREUVE "Q2" (QUATRE POINTS DE PLUS DE LA QUALIFICATION DU LECTEUR CREUX AU SOMMET) -- machine 1, 22h (lot 074b131287ad2b6f, note section 3 et 4) ; machine 2, 2026-11-22, hors chaine (classe 3) : AUCUN verdict de gel, AUCUN gel, AUCUN depot.
CE FICHIER EST ECRIT AVANT TOUTE LECTURE 2D AUX QUATRE POINTS DE Q2 (je n'ai lu aucune sortie de Q2a, Q2b, Q2c, Q2d ; l'ordre de l'operateur est a citer dans l'enveloppe).
Derive de epreuve_Q_sommet_machine2_v1.py (non edite). MEMES LECTURES : pilote lecteur_2D_pilote_machine2_v1.py (47a84eae6052f006, NON EDITE), bloc LECTEUR CREUX d5cc48f48e37af99, moteur 82a0be882568fe0c, site (0, 0), energie de depart 0, fantome (signe -1) puis jumeau (+1), quatre absorbeurs
A (F2, bord r_c, 80), B (F2, r_c, 100), C (F1, r_c, 100), D (F2, r_c + 10, 80), douze barreaux k = -3 a 8, eta_k = eta0 2^(-k). DEUX DIFFERENCES avec Q, dites par elle et que je suis : r_c = 2 (m + max(8, m)) + 2 avec m la profondeur de barriere de la regle de l'esquisse (r_c = 20 et 22 a Q2a et Q2b ;
18 a Q2c et Q2d) ; eta0 = max(|w2 - 2|, g X(w2) / (P kappa_3)) (la regle en absolu l'emporte aux quatre points). Mes eta0, m et r_c ont ete recalcules AVANT (verifie_Q2_1d_machine2_v1.py : ecart relatif 0 aux quatre eta0, profondeurs 1, 2, 0, 0, r_c 20, 22, 18, 18).
LE JUGE est la feuille deposee 83701094e6a2b965, juger_etat, TELLE QUELLE, g_dep3 = None (aucune valeur du depot a ces points ; "lu sur le plateau" non evalue).
SES ATTENDUS (note section 4, a la lettre, ecrits par elle avant) :
  Q2-1  les quatre points sont QUALIFIES par juger_etat (fantome).
  Q2-2  a chaque point qualifie, |ln(Gamma_pl / G3*)| <= 0.002, Gamma_pl = plateau de l'absorbeur A ; G3* = 4.94622e-08, 2.05449e-09, 1.21071e-05, 2.92086e-06 (Q2a, Q2b, Q2c, Q2d).
  Q2-3  le temoin (jumeau) tient aux quatre points : 48 lectures suivies sur 48 ET plus grande largeur lue <= 1e-6 Gamma_pl.
  Q2-4  LE SIGNE. Si Q2c et Q2d sont qualifies : ln[Gamma_pl(Q2c) / Gamma_pl(Q-e)] dans [+0.0007, +0.0017] et ln[Gamma_pl(Q2d) / Gamma_pl(Q-f)] dans [+0.0016, +0.0026], Gamma_pl(Q-e) et Gamma_pl(Q-f) etant MES plateaux de Q (A, relus dans Q_sorties par la meme feuille).
  SON "TORT" : un point qualifie ou |ln(Gamma_pl / G3*)| > 0.01 ; OU deux points ou plus sans plateau sous A ; OU un rapport de Q2-4 de signe NEGATIF.
MES REGLES, FIXEES ICI AVANT TOUT RESULTAT, que je n'ajusterai pas apres :
  (R1) CONTROLE : canons du moteur, du pilote et de la feuille ; chaque JSON porte son eta0, son r_c, w2, g, m, les quatre absorbeurs a la geometrie du depot (bords lus dans lecture.absorbeurs : r_c, r_c, r_c, r_c + 10), les douze barreaux, le signe, le site ; sinon RIEN ne se lit.
  (R2) UN attendu Q2-i est dit TENU si et seulement s'il l'est a TOUS les cas qu'il vise, bornes incluses ; Q2-2 et Q2-4 "non evaluables" aux points non qualifies (Q2-4 : si Q2c ou Q2d ne l'est pas, ou si Q-e ou Q-f ne se relit pas) -- jamais bornes.
  (R3) Son tort est dit REALISE a la lettre, ou NON REALISE ; je ne mets pas d'autre seuil.
  (R4) SANS JUGEMENT, rapporte : Gamma_pl / g et / t_0 (t_0 = g X(w2) / P) ; par absorbeur le statut, k0, l'etalement, Gamma_pl / G3* ; ln(B, C, D / A) ; le poids du site (0, 0) dans la fenetre de A ; Gamma(k) / G3* sous A ; l'etendue plate de A (barreaux consecutifs a 0.5 pour cent du plateau) ;
       les lectures non suivies ; iterations et residus ; les largeurs du jumeau ; les deux rapports de Q2-4 ET leur ecart a ses valeurs de chaine (+0.00121, +0.00211) ; le meme rapport lu sur les largeurs a k = 3 de A (sans plateau).
  (R5) Ce que Q2 ne dit pas, a ecrire dans la note : quatre points sacrifies, delta de signe +/- 1e-4 seulement, rien des kappa de l'esquisse, aucune cellule d'un gel relue.
Usage : py -3.11 -P epreuve_Q2_machine2_v1.py <dossier des lect2D_Q2*.json> <dossier des lect2D_Q*.json de Q (Q_sorties)> <feuille deposee> <moteur m17_chaine_v17.py>"""
import hashlib
import importlib.util
import json
import math
import os
import sys
import unicodedata
from fractions import Fraction as F

DOS, DOSQ, FEUILLE, MOTEUR = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
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
specm = importlib.util.spec_from_file_location('moteur', MOTEUR)
M = importlib.util.module_from_spec(specm)
specm.loader.exec_module(M)

# (id, nom, w2, g, m, r_c, eta0, G3*)
PTS = [('Q2a', 'Q2-a', F(20001, 10000), 6e-5, 1, 20, 2.33642e-04, 4.94622e-08), ('Q2b', 'Q2-b', F(20001, 10000), 4e-5, 2, 22, 1.55762e-04, 2.05449e-09),
       ('Q2c', 'Q2-c', F(19999, 10000), 3e-4, 0, 18, 1.16909e-03, 1.21071e-05), ('Q2d', 'Q2-d', F(19999, 10000), 1.5e-4, 0, 18, 5.84544e-04, 2.92086e-06)]
KS = list(range(-3, 9))
FORM = {'A': ('F2', 0, 80), 'B': ('F2', 0, 100), 'C': ('F1', 0, 100), 'D': ('F2', 10, 80)}
manque, bad = [], []
LU = {}
for ident, nom, w2, g, m, rc, eta0, g3 in PTS:
    LU[ident] = {}
    for qui in ('fantome', 'jumeau'):
        p = os.path.join(DOS, 'lect2D_%s_%s.json' % (ident, qui))
        if not os.path.isfile(p):
            manque.append(p)
            continue
        d = json.load(open(p))
        LU[ident][qui] = d
        c, r = d['cellule'], d['reglage']
        geo_ok = sorted(d['lecture']['absorbeurs']) == ['A', 'B', 'C', 'D'] and all((x['forme'], x['bord'], x['couches']) == (FORM[a][0], rc + FORM[a][1], FORM[a][2]) for a, x in d['lecture']['absorbeurs'].items())
        ok = (d['moteur_canon'] == '82a0be882568fe0c' and d['source_bloc_canon'] == 'd5cc48f48e37af99' and d['pilote_canon'] == '47a84eae6052f006'
              and F(c['w2']) == w2 and float(c['g']) == g and c['m'] == m and abs(c['eta0'] - eta0) <= 1e-12 * eta0 and c['r_c'] == rc and r['ks'] == KS and geo_ok
              and d['lecture']['signe'] == (-1 if qui == 'fantome' else 1) and d['lecture']['site'] == [0, 0] and d['lecture']['E_depart'] == 0.0)
        if not ok:
            bad.append((ident, qui))
if manque or bad:
    print('R1 NON TENU : fichiers manquants %s ; en-tetes hors regle %s' % (manque, bad))
    raise SystemExit(1)
print('R1 TENU : 8 JSON (quatre points x fantome, jumeau), canons moteur/bloc/pilote/feuille controles, eta0, m, r_c et geometrie des absorbeurs conformes.\n')


def plateau_A(dos, ident):
    t = json.load(open(os.path.join(dos, 'lect2D_%s_fantome.json' % ident)))['lecture']['traj']
    J = FE.juger_etat({x: t[x] for x in 'ABCD'}, None)
    PA = J['plateaux']['A']
    return (PA['Gamma_pl'] if PA['statut'] == 'PLATEAU' else None), J, t


R = {}
for ident, nom, w2, g, m, rc, eta0, g3 in PTS:
    gpl, J, traj = plateau_A(DOS, ident)
    tw = LU[ident]['jumeau']['lecture']['traj']
    nsuivi = sum(1 for x in 'ABCD' for k in KS if tw[x][str(k)]['suivi'])
    gam_tw = [abs(tw[x][str(k)]['gamma']) for x in 'ABCD' for k in KS if tw[x][str(k)]['suivi'] and tw[x][str(k)]['gamma'] is not None]
    X = M.X_saut_reel(5, 2, 1, 0, 0, w2)
    R[ident] = {'nom': nom, 'J': J, 'gpl': gpl, 'g': g, 'g3': g3, 'nsuivi_tw': nsuivi, 'maxtw': max(gam_tw) if gam_tw else None, 't0': g * X / 5.0, 'traj': traj}
    print('=== %s  w2 = %s  g = %.3g  m = %d  r_c = %d  eta0 = %.5e  statut %s ; non lisibles %s ; echecs %s' % (nom, w2, g, m, rc, eta0, J['statut'], J['non_lisibles'], J['echecs']))
    for x in 'ABCD':
        P = J['plateaux'][x]
        if P['statut'] == 'AUCUNE FENETRE':
            print('   %s : AUCUNE FENETRE' % x)
            continue
        print('   %s : %-15s k0 = %+d  etalement %.4f  Gamma_pl = %.5e  Gamma_pl / G3* = %.4f  (ecart ln A : %s)' % (x, P['statut'], P['k0'], P['etalement'], P['Gamma_pl'], P['Gamma_pl'] / g3, ('%.4f' % P['ecart_ln_A']) if 'ecart_ln_A' in P else '-'))
    if gpl:
        k0 = J['plateaux']['A']['k0']
        pw = min(traj['A'][str(k)]['poids_site'] for k in range(k0, k0 + 5))
        plat = [k for k in KS if traj['A'][str(k)]['suivi'] and traj['A'][str(k)]['gamma'] and abs(traj['A'][str(k)]['gamma'] / gpl - 1) <= 0.005]
        consec = bool(plat) and plat == list(range(plat[0], plat[-1] + 1))
        print('   Gamma_pl(A) / g = %.6f ; / t_0 = %.6f ; ln(Gamma_pl / G3*) = %+.5f ; poids du site (0, 0) mini dans la fenetre de A : %.4f' % (gpl / g, gpl / R[ident]['t0'], math.log(gpl / g3), pw))
        print('   etendue plate sous A (a 0.5 pour cent) : k = %s (%d barreaux%s)' % (plat, len(plat), ' consecutifs' if consec else ', NON consecutifs'))
    print('   Gamma(k) / G3* sous A, k = -3..8 : %s' % ' '.join(('%.3f' % (traj['A'][str(k)]['gamma'] / g3)) if traj['A'][str(k)]['suivi'] and traj['A'][str(k)]['gamma'] else '  -  ' for k in KS))
    nonsuiv = ['%s k=%+d' % (x, k) for x in 'ABCD' for k in KS if not traj[x][str(k)]['suivi']]
    L = [traj[x][str(k)] for x in 'ABCD' for k in KS if traj[x][str(k)]['suivi']]
    print('   lectures suivies (fantome) : %d sur 48 ; non suivies : %s ; iterations max %d ; residu max %.1e ; poids du site mini sur les suivies %.4f' % (len(L), nonsuiv or 'aucune', max(r['iterations'] for r in L), max(r['residu'] for r in L), min(r['poids_site'] for r in L)))
    print('   jumeau : %d lectures suivies sur 48 ; plus grande largeur %.3e%s' % (nsuivi, R[ident]['maxtw'] or float('nan'), (' (= %.2e Gamma_pl)' % (R[ident]['maxtw'] / gpl)) if gpl and R[ident]['maxtw'] is not None else ''))
print('\n=== LES ATTENDUS DE MACHINE 1')
q1 = all(R[i]['J']['statut'] == 'QUALIFIE' for i, *_ in PTS)
print('Q2-1  quatre points QUALIFIES : %s   (%s)' % ('TENU' if q1 else 'NON TENU', ' ; '.join('%s %s' % (R[i]['nom'], R[i]['J']['statut']) for i, *_ in PTS)))
qual = [i for i, *_ in PTS if R[i]['J']['statut'] == 'QUALIFIE' and R[i]['gpl']]
ec2 = {i: abs(math.log(R[i]['gpl'] / R[i]['g3'])) for i in qual}
q2 = bool(qual) and all(v <= 0.002 for v in ec2.values())
print('Q2-2  |ln(Gamma_pl / G3*)| <= 0.002 aux points qualifies : %s   (%s ; %d points qualifies sur 4%s)' % ('TENU' if q2 and len(qual) == 4 else ('TENU sur les points qualifies seulement' if q2 else 'NON TENU'), ' ; '.join('%s %.5f' % (R[i]['nom'], v) for i, v in ec2.items()), len(qual), '' if len(qual) == 4 else ' : non evaluable aux autres'))
q3 = all(R[i]['nsuivi_tw'] == 48 and R[i]['gpl'] and R[i]['maxtw'] is not None and R[i]['maxtw'] <= 1e-6 * R[i]['gpl'] for i, *_ in PTS)
print('Q2-3  temoin (jumeau) : 48 lectures suivies et largeur <= 1e-6 Gamma_pl aux quatre points : %s' % ('TENU' if q3 else 'NON TENU'))
rat = {}
if 'Q2c' in qual and 'Q2d' in qual:
    ge, _, _ = plateau_A(DOSQ, 'Qe')
    gf, _, _ = plateau_A(DOSQ, 'Qf')
    if ge and gf:
        rat['c'] = math.log(R['Q2c']['gpl'] / ge)
        rat['d'] = math.log(R['Q2d']['gpl'] / gf)
        oc = 0.0007 <= rat['c'] <= 0.0017
        od = 0.0016 <= rat['d'] <= 0.0026
        print('Q2-4  ln[Gamma_pl(Q2c) / Gamma_pl(Q-e)] = %+.5f dans [+0.0007, +0.0017] : %s ; ln[Gamma_pl(Q2d) / Gamma_pl(Q-f)] = %+.5f dans [+0.0016, +0.0026] : %s   ->   %s   (Gamma_pl(Q-e) = %.5e, Gamma_pl(Q-f) = %.5e, mes plateaux de Q)'
              % (rat['c'], 'oui' if oc else 'NON', rat['d'], 'oui' if od else 'NON', 'TENU' if (oc and od) else 'NON TENU', ge, gf))
        print('      valeurs de sa chaine : +0.00121 et +0.00211 ; ecarts de mes lectures a ces valeurs : %+.5f et %+.5f' % (rat['c'] - 0.00121, rat['d'] - 0.00211))
        a3c = math.log(R['Q2c']['traj']['A']['3']['gamma'] / json.load(open(os.path.join(DOSQ, 'lect2D_Qe_fantome.json')))['lecture']['traj']['A']['3']['gamma'])
        a3d = math.log(R['Q2d']['traj']['A']['3']['gamma'] / json.load(open(os.path.join(DOSQ, 'lect2D_Qf_fantome.json')))['lecture']['traj']['A']['3']['gamma'])
        print('      (R4, sans plateau) memes rapports lus a k = 3 sous A : %+.5f et %+.5f' % (a3c, a3d))
    else:
        print('Q2-4  non evaluable (plateau de Q-e ou Q-f non relu)')
else:
    print('Q2-4  non evaluable (Q2c ou Q2d non qualifie)')
tort1 = [i for i in qual if ec2[i] > 0.01]
sans = [i for i, *_ in PTS if R[i]['J']['plateaux']['A']['statut'] != 'PLATEAU']
neg = [k for k, v in rat.items() if v < 0]
print('SON TORT : point qualifie a |ln| > 0.010 : %s ; points sans plateau sous A : %s ; rapport de Q2-4 negatif : %s -> %s' % (tort1 or 'aucun', sans or 'aucun', neg or 'aucun', 'REALISE' if (tort1 or len(sans) >= 2 or neg) else 'NON REALISE'))
print('\nCe que Q2 ne dit pas : quatre points sacrifies, delta de signe +/- 1e-4 seulement, rien des kappa de l esquisse, aucune cellule d un gel relue.')
