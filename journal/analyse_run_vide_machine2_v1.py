# -*- coding: ascii -*-
"""ANALYSE DU RUN UNIQUE DU GEL 'LARGEUR DU VIDE' (run_gel_vide_machine2/run_1) -- machine 2, v1, 2026-11-16. Rien n'est juge ici : le verdict est celui de la feuille (V1 TENU ; VP TENU).
Ce script CONFRONTE et CONSIGNE :
 (1) ln q recalcule avec MES predictions (predictions_machine2_vide_v1.json, ordre 3 : ln_G3 de mon calcul) contre ln q de la feuille (ln_G3 de la table gelee de m1) ;
 (2) la qualite des lectures aux 28 cellules : statut du lecteur, echecs, cellules non lisibles, poids minimal, plateaux des quatre absorbeurs, temoin (jumeau) ;
 (3) les marges : |ln q| contre T - b ; |ln q| contre l'etendue de la chaine ;
 (4) les annonces A-1 a A-7 de la section 10 du gel, une a une, selon les mots de leur enonce ;
 (5) les signes de ln q selon le signe de delta (consigne, sans jugement).
Usage : py -3.11 -I analyse_run_vide_machine2_v1.py"""
import json
import math
import statistics as st

V = json.load(open(r'd:\devs\bocal\BOCAL4\run_gel_vide_machine2\run_1\verdict_vide.json'))
P = {c['id']: c for c in json.load(open(r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie2_machine2\predictions_machine2_vide_v1.json'))['cellules']}
T = {c['id']: c for c in json.load(open(r'd:\devs\bocal\BOCAL4\livraison_16h_gel_vide_partie2\ext\x_gel_vide_partie2\lot_machine1_2026-11-16_gel_vide_partie2_instrument_enonces_v1\table_cellules_gel_vide_v1.json'))['cellules']}
ordre = lambda s: (['MG', 'MP', 'PP', 'PG'].index(s[:2]), int(s[2:]))
C = sorted(V['cellules'], key=lambda c: ordre(c['id']))
print('V1 :', V['V1']['issue'], V['V1']['comptes'], '; VP :', V['VP']['issue'], V['VP']['comptes'], '; instrument :', V['instrument'], '; incomplet :', V['incomplet'])
print()
print('(1) ln q de la feuille (ln G3 de la table gelee - ln Gamma_pl) et ln q avec MES predictions (mon ln G3 - ln Gamma_pl)')
ecart = 0.0
for c in C:
    lq_m2 = P[c['id']]['ln_G3'] - c['ln_Gamma_pl']
    assert abs((c['ln_G3'] - c['ln_Gamma_pl']) - c['ln_q']) < 1e-12, c['id']
    ecart = max(ecart, abs(lq_m2 - c['ln_q']))
    c['ln_q_m2'] = lq_m2
print('    ecart max entre les deux ln q sur 28 cellules : %.2e (la table gelee et mes predictions different de 8.6e-9 au plus ; ln q = ln G3 - ln Gamma_pl, convention de la feuille verifiee)' % ecart)
print()
print('(2) qualite des lectures')
nq = sum(1 for c in C if c['lecteur']['statut'] == 'QUALIFIE')
ech = sum(len(c['lecteur']['echecs']) for c in C)
nl = sum(len(c['lecteur']['non_lisibles']) for c in C)
pw = min(c['lecteur']['poids_min'] for c in C)
print('    cellules QUALIFIEES : %d sur 28 ; echecs : %d ; non lisibles : %d ; poids minimal sur toutes les cellules : %.3f' % (nq, ech, nl, pw))
sui = [c['lecteur']['suivies'] for c in C]
print('    etats suivis par le lecteur (par cellule) : min %s max %s' % (min(sui), max(sui)))
statuts = {}
for c in C:
    for a, pl in c['lecteur']['plateaux'].items():
        statuts[(a, pl['statut'])] = statuts.get((a, pl['statut']), 0) + 1
print('    plateaux des quatre absorbeurs : %s' % sorted(statuts.items()))
tw = [c['temoin'] for c in C]
print('    temoin (jumeau sans fantome) : tient %d sur 28 ; lectures suivies %s ; plus grande largeur du jumeau %.2e ; plus grand rapport au plateau %.2e (seuil 1e-6)' % (
    sum(1 for t in tw if t['tient']), sorted(set((t['suivies'], t['lectures']) for t in tw)), max(t['plus_grande_largeur'] for t in tw), max(t['rapport_au_plateau'] for t in tw)))
etal = [c['etalement_du_lecteur'] for c in C]
print('    etalement s du lecteur au vide : min %.4f ; mediane %.4f ; max %.4f (m2 mesurait <= 0.0052 aux 144 etats joues du delta 100 : %s)' % (min(etal), st.median(etal), max(etal), 'dans cette borne' if max(etal) <= 0.0052 else 'AU-DESSUS'))
print()
print('(3) marges (lisibles T = 0.02, profondes T = 0.05)')
for ligne in ('lisible', 'profonde'):
    L = [c for c in C if c['ligne'] == ligne]
    mq = max(abs(c['ln_q']) for c in L)
    marge = min(c['tolerance'] - c['bande'] - abs(c['ln_q']) for c in L)
    cm = max(L, key=lambda c: abs(c['ln_q']))
    print('    %-8s %2d cellules : plus grand |ln q| %.4f (a %s) ; mediane |ln q| %.4f ; plus petite marge T - b - |ln q| %.4f ; bande b : %.4f a %.4f' % (
        ligne, len(L), mq, cm['id'], st.median(abs(c['ln_q']) for c in L), marge, min(c['bande'] for c in L), max(c['bande'] for c in L)))
sous = [c['id'] for c in C if abs(c['ln_q']) < c['etendue']]
print('    cellules ou |ln q| est sous l etendue de la chaine (le residu est alors a l interieur de ce que les 18 variantes d absorbeur laissent indetermine) : %d sur 28' % len(sous))
sous_b = [c['id'] for c in C if abs(c['ln_q']) < c['bande']]
print('    cellules ou |ln q| est sous la bande b = etendue + s : %d sur 28' % len(sous_b))
print()
print('(4) annonces de la plume (section 10), selon leurs mots')
lis = [c for c in C if c['ligne'] == 'lisible']
print('    A-1 instrument du lecteur tient : %s' % ('OUI' if V['instrument'] == 'TIENT' else 'NON'))
print('    A-2 temoin tient aux 28 cellules : %s' % ('OUI' if all(t['tient'] for t in tw) else 'NON'))
print('    A-3 le lecteur qualifie les 16 lisibles : %s (%d sur 16)' % ('OUI' if all(c['lecteur']['statut'] == 'QUALIFIE' for c in lis) else 'NON', sum(1 for c in lis if c['lecteur']['statut'] == 'QUALIFIE')))
print('    A-4 V1 : %s (annonce : TENU 0.50)' % V['V1']['issue'])
print('    A-5 VP : %s (annonce : TENU 0.35)' % V['VP']['issue'])
mq = max(abs(c['ln_q']) for c in lis)
print('    A-6 plus grand |ln q| aux lisibles lues : %.4f -> %s (annonce : sous 0.01)' % (mq, 'OUI' if mq < 0.01 else 'NON'))
mg = [c for c in lis if c['creneau'] == 'MG']
pos = [c['id'] for c in mg if c['ln_q'] > 0]
neg = [c['id'] for c in mg if c['ln_q'] < 0]
print('    A-7 signe de ln q aux cellules lisibles de MG : positif a %d %s ; negatif a %d %s -> %s' % (
    len(pos), pos, len(neg), neg, 'branche (b) : positif a trois au moins' if len(pos) >= 3 else ('branche (a) : negatif, comme delta, a trois au moins' if len(neg) >= 3 else 'aucune des deux branches')))
print('        tailles : ln q aux MG lisibles = %s ; etendue de la chaine = %s' % (['%+.4f' % c['ln_q'] for c in mg], ['%.4f' % c['etendue'] for c in mg]))
print()
print('(5) consigne : signe de ln q selon le signe de delta')
for cr in ('MG', 'MP', 'PP', 'PG'):
    L = [c for c in C if c['creneau'] == cr]
    p = sum(1 for c in L if c['ln_q'] > 0)
    print('    %s (delta %s) : ln q > 0 a %d cellules sur %d ; ln q de chaque cellule : %s' % (cr, '<0' if L[0]['delta'] < 0 else '>0', p, len(L), ' '.join('%+.4f' % c['ln_q'] for c in L)))
p = sum(1 for c in C if c['ln_q'] > 0)
print('    ensemble : ln q > 0 a %d cellules sur 28, ln q < 0 a %d ; mediane de ln q : %+.5f' % (p, sum(1 for c in C if c['ln_q'] < 0), st.median(c['ln_q'] for c in C)))
a_signe_delta = sum(1 for c in C if c['ln_q'] * c['delta'] > 0)
print('    ln q du signe de delta a %d cellules, du signe oppose a %d (la feuille consigne : 12 du signe de delta ; 19 du signe de la sous-correction)' % (a_signe_delta, sum(1 for c in C if c['ln_q'] * c['delta'] < 0)))
print('    ordre 3 plus pres de la mesure que l ordre 1 : %d cellules ; que la loi d echelle : %d (la feuille consigne 26 et 27)' % (
    sum(1 for c in C if abs(c['consigne']['ln_q_ordre1']) > abs(c['ln_q'])), sum(1 for c in C if abs(c['consigne']['ln_q_loi_d_echelle']) > abs(c['ln_q']))))
print('    plus grand |ln q| de la forme fermee (consigne, non jugee) : %.4f' % max(abs(c['consigne']['ln_q_forme_fermee']) for c in C))
