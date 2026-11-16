# -*- coding: ascii -*-
"""COMPARAISON de mes lectures aux lignes du paragraphe 5 de la note de machine 1 (42c822811167b826) qui portent sur des
configurations de la NUIT BIS (F1 a 20 et 30 couches, F2 a 20 couches) : aucun absorbeur long, aucun point neuf. HORS CHAINE.
Les valeurs de machine 1 sont LUES DANS LA NOTE (son canon est verifie), pas recopiees ; les miennes viennent de mon JSON de
validation (meilleur etalement de la fenetre de cinq barreaux, gel bis 3.11, gamma = 2 eta <W>). Les lignes de 40 couches et plus,
F3 a 60 couches et les bords decales ne sont PAS rejouees ici : elles demandent que l'operateur le demande.
Usage : python -P lecteur_creux_m2/comparaison_tableau5_machine2_v1.py <note machine 1.md> <validation.json>"""
import hashlib
import json
import re
import sys
import unicodedata

NOTE, VAL = sys.argv[1], sys.argv[2]
raw = open(NOTE, 'rb').read()
canon = hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]
print('canon de la note : %s (attendu 42c822811167b826) %s' % (canon, 'OK' if canon == '42c822811167b826' else 'MORD'))
if canon != '42c822811167b826':
    sys.exit(1)
txt = raw.decode('utf-8')
ordre = ['39_20', '197_100', '99_50', '101_50', '203_100', '41_20']          # 1,95 1,97 1,98 2,02 2,03 2,05
LIGNES = {('F1', 20): 'F1G20', ('F1', 30): 'F1G30', ('F2', 20): 'F2G20'}
m1 = {}
for l in txt.split('\n'):
    p = [c.strip() for c in l.strip().strip('|').split('|')]
    if len(p) == 9 and p[0] in ('F1', 'F2', 'F3') and p[1].isdigit() and (p[0], int(p[1])) in LIGNES and p[8].endswith('sur 6'):
        m1[(p[0], int(p[1]))] = ([float(x.replace(',', '.')) for x in p[2:8]], int(p[8].split()[0]))
assert sorted(m1) == sorted(LIGNES), m1
d = json.load(open(VAL))
res = {r['nom']: r for r in d['resultats'] if r['genre'] == 'pt'}
ok = tot = 0
pire = 0.0
for (forme, L), cfg in LIGNES.items():
    row, n1 = m1[(forme, L)]
    mien = [100.0 * res[p]['configs'][cfg]['cmp']['plateau_W']['etalement'] for p in ordre]
    nplat = sum(1 for p in ordre if res[p]['configs'][cfg]['cmp']['plateau_W']['plateau'])
    print('%s %d couches (%s)' % (forme, L, cfg))
    print('   machine 1 (note) : %s  plateaux %d sur 6' % (' '.join('%6.2f' % x for x in row), n1))
    print('   machine 2        : %s  plateaux %d sur 6' % (' '.join('%6.2f' % x for x in mien), nplat))
    for a, b in zip(row, mien):
        tot += 1
        ok += abs(round(b, 2) - a) < 1e-9
        pire = max(pire, abs(b - a))
    assert nplat == n1, (cfg, nplat, n1)
print('cellules identiques a l arrondi de la note (deux decimales) : %d sur %d ; ecart max %.4f point de pourcentage ; comptes de plateau identiques : 3 sur 3'
      % (ok, tot, pire))
sys.exit(0 if ok == tot else 1)
