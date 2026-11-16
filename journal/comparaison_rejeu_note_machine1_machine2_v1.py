# -*- coding: ascii -*-
"""COMPARAISON du rejeu (i) de machine 2 (rejeu_absorbeurs_longs_machine2_v1.json) aux tableaux 4 et 5 et au temoin de la note de
machine 1 (42c822811167b826). HORS CHAINE. Ecrit APRES la fin du passage, avant d'en ouvrir le journal. Les valeurs de machine 1 sont LUES
DANS LA NOTE (canon verifie), pas recopiees ; les miennes viennent de mon JSON. Rien n'est recalcule.

SEUILS DECLARES AVANT LA PREMIERE LECTURE DES RESULTATS :
  C1  tableau 4, valeur (Gamma_pl / lecture de M17) : accord si |mien / machine 1 - 1| <= 0.002 (la note donne quatre decimales) ;
  C2  tableau 4, verdict PLATEAU (etalement <= 5 %) : identique ; etalement : ecart <= 0.10 point de pourcentage (la note donne deux
      decimales) ; compte de barreaux "dans 0.5 %" (a) : egal ; ces deux derniers sont des DESCRIPTIONS : ils sont comptes, pas jugees ;
  C3  tableau 5, etalement de la meilleure fenetre : egal a l'arrondi de la note (deux decimales), sur l'echelle B (k = -5..12, celle
      que la note nomme pour ce tableau) ; l'echelle A (k = -5..14) est comptee a cote ; comptes "N sur 6" egaux ;
  C4  temoin : la note dit "moins de 0,5 % de la reference sur 8 a 11 barreaux consecutifs depuis k = -5, pire ecart 0,13 %" : on
      compte combien de mes huit trajectoires ont leur nombre de barreaux dans [8, 11] et un pire ecart <= 0.13 % (0.0013) ;
  C5  ancrage : identite (3.9) avec l'etat de M17 >= 0.90 ; R3 (ancrage stable avec 2 K) ; residu <= 1e-9 ; gamma_E / gamma_W <= 1e-6.
Usage : py -3.11 -P lecteur_creux_m2/comparaison_rejeu_note_machine1_machine2_v1.py <note machine 1.md> <rejeu.json>"""
import hashlib
import json
import re
import sys
import unicodedata

NOTE, REJEU = sys.argv[1], sys.argv[2]
raw = open(NOTE, 'rb').read()
canon = hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]
print('canon de la note : %s (attendu 42c822811167b826) %s' % (canon, 'OK' if canon == '42c822811167b826' else 'MORD'))
if canon != '42c822811167b826':
    sys.exit(1)
txt = raw.decode('utf-8')
ORDRE = ['39_20', '197_100', '99_50', '101_50', '203_100', '41_20']
W2 = {'1,95': '39_20', '1,97': '197_100', '1,98': '99_50', '2,02': '101_50', '2,03': '203_100', '2,05': '41_20'}
COLS4 = ['F2_60', 'F2_80', 'F1_80', 'F3_60', 'F1T_60']
CELL = re.compile(r'^([\d,]+) \(([\d,]+) %, (\d+)\)$')
t4, t5 = {}, {}
for l in txt.split('\n'):
    p = [c.strip() for c in l.strip().strip('|').split('|')]
    if len(p) == 8 and p[0] in W2 and CELL.match(p[1]):
        row = []
        for c in p[1:6]:
            m = CELL.match(c)
            row.append((float(m.group(1).replace(',', '.')), float(m.group(2).replace(',', '.')), int(m.group(3))))
        t4[W2[p[0]]] = row
    if len(p) == 9 and p[0] in ('F1', 'F2', 'F3') and p[1].isdigit() and p[8].endswith('sur 6'):
        t5[(p[0], int(p[1]))] = ([float(x.replace(',', '.')) for x in p[2:8]], int(p[8].split()[0]))
assert sorted(t4) == sorted(ORDRE), t4.keys()
d = json.load(open(REJEU))
res = {(r['nom'], c): (r, x) for r in d['resultats'] if r['nature'] == 'pt' for c, x in r['configs'].items()}

print('')
print('TABLEAU 4 : Gamma_pl / M17, (etalement %, barreaux dans 0.5 % (a)) ; machine 1 puis machine 2, echelle A (k = -5..14)')
n = ok1 = ok_verdict = ok_etal = ok_cnt = 0
pire_val = 0.0
for p in ORDRE:
    for i, c in enumerate(COLS4):
        r, x = res[(p, c)]
        pl = x['resume']['plateau_A']
        v1, e1, c1 = t4[p][i]
        v2 = pl['Gamma_pl'] / r['m17_gamma_k3']
        e2 = 100 * pl['etalement']
        n += 1
        ok1 += abs(v2 / v1 - 1.0) <= 0.002
        pire_val = max(pire_val, abs(v2 / v1 - 1.0))
        ok_verdict += (e1 <= 5.0) == pl['plateau']
        ok_etal += abs(e2 - e1) <= 0.10
        ok_cnt += pl['compte_a'] == c1
        print('  %-8s %-7s m1 %.4f (%.2f, %d)   m2 %.4f (%.2f, %d)   ecart valeur %+.2e%s' % (
            p, c, v1, e1, c1, v2, e2, pl['compte_a'], v2 / v1 - 1.0,
            '' if (abs(v2 / v1 - 1.0) <= 0.002 and abs(e2 - e1) <= 0.10 and pl['compte_a'] == c1) else '   <-- ECART'))
print('C1 valeurs a 0.2 %% : %d sur %d (pire %.2e) ; C2 verdict PLATEAU : %d sur %d ; etalement a 0.10 point : %d sur %d ; compte (a) egal : %d sur %d'
      % (ok1, n, pire_val, ok_verdict, n, ok_etal, n, ok_cnt, n))

print('')
print('TABLEAU 5 : etalement de la meilleure fenetre de cinq barreaux (%) ; echelle B (k = -5..12) primaire, echelle A a cote')
nB = okB = okA = 0
for (forme, L), (row, n1) in sorted(t5.items()):
    cfg = '%s_%d' % (forme, L)
    if (ORDRE[0], cfg) not in res:
        continue
    mB = [100 * res[(p, cfg)][1]['resume']['plateau_B']['etalement'] for p in ORDRE]
    mA = [100 * res[(p, cfg)][1]['resume']['plateau_A']['etalement'] for p in ORDRE]
    pB = sum(1 for p in ORDRE if res[(p, cfg)][1]['resume']['plateau_B']['plateau'])
    pA = sum(1 for p in ORDRE if res[(p, cfg)][1]['resume']['plateau_A']['plateau'])
    print('  %s %2d couches  m1 %s  %d sur 6' % (forme, L, ' '.join('%6.2f' % x for x in row), n1))
    print('                  m2 B %s  %d sur 6' % (' '.join('%6.2f' % x for x in mB), pB))
    print('                  m2 A %s  %d sur 6' % (' '.join('%6.2f' % x for x in mA), pA))
    for a, b, c in zip(row, mB, mA):
        nB += 1
        okB += abs(round(b, 2) - a) < 1e-9
        okA += abs(round(c, 2) - a) < 1e-9
print('C3 cellules egales a l arrondi : echelle B %d sur %d, echelle A %d sur %d' % (okB, nB, okA, nB))

print('')
print('TEMOIN H+ (C4) : barreaux consecutifs a moins de 0.5 %% de la reference depuis k = -5, et pire ecart ; note : 8 a 11, 0.13 %%')
nt = nok = 0
for r in d['resultats']:
    if r['nature'] != 'tp':
        continue
    for c, x in sorted(r['configs'].items()):
        nt += 1
        bon = 8 <= x['consecutifs_depuis_m5'] <= 11 and x['pire_ecart_consecutifs'] <= 0.0013
        nok += bon
        pl = x['resume']['plateau_A']
        print('  %s %-6s L %d : %2d barreaux, pire %.3f %% ; plateau A %s etalement %.3f %% Gamma_pl/ref %.5f  %s' % (
            r['nom'], c, x['L'], x['consecutifs_depuis_m5'], 100 * x['pire_ecart_consecutifs'],
            'PLATEAU' if pl['plateau'] else 'pas de plateau', 100 * pl['etalement'], pl['Gamma_pl'] / r['Gamma_ref'], '' if bon else '<-- hors de la note'))
print('C4 : %d trajectoires sur %d dans la description de la note' % (nok, nt))

print('')
print('ANCRAGE ET LECTURE (C5), toutes trajectoires (points et temoin)')
tot = {'ident': [0, 0], 'R3': [0, 0], 'residu': [0, 0], 'EW': [0, 0], 'suivi': [0, 0]}
ident_min = (2.0, None)
marge = []
for r in d['resultats']:
    for c, x in r['configs'].items():
        m = x['resume']
        if 'identite_M17' in x:
            tot['ident'][1] += 1
            tot['ident'][0] += x['identite_M17'] >= 0.90
            if x['identite_M17'] < ident_min[0]:
                ident_min = (x['identite_M17'], (r['nom'], c))
        tot['R3'][1] += 1
        tot['R3'][0] += x['R3']
        tot['residu'][1] += 1
        tot['residu'][0] += m['pire_residu'] <= 1e-9
        tot['EW'][1] += 1
        tot['EW'][0] += m['pire_EW'] is None or m['pire_EW'] <= 1e-6
        tot['suivi'][1] += 1
        tot['suivi'][0] += not m['perdus']
        a = x['ancre']
        marge.append((a['recouvrement_graine'] / a['recouvrement_second'], r['nom'], c, x.get('identite_M17')))
for k, v in tot.items():
    print('  %-7s %d sur %d' % (k, v[0], v[1]))
print('  identite minimale avec l etat de M17 : %.6f en %s' % (ident_min[0], ident_min[1]))
marge.sort()
print('  marges d ancrage (recouvrement du premier / du second) les plus faibles :')
for m_, nom, c, idn in marge[:8]:
    print('     %.3f  %-8s %-7s identite %s' % (m_, nom, c, ('%.6f' % idn) if idn is not None else 'n/a'))
