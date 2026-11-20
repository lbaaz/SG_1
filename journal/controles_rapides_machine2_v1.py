# -*- coding: ascii -*-
"""CONTROLES RAPIDES du gel "pont", partie 1 (machine 2, 2026-11-17), avant la certification complete. Lit le gel, ne l'edite pas.
(1) hachages de la section 3 sur la graine de demonstration ; (2) couplage g de la section 2 au point sacrifie w2 = 101/50, m = 3 ; (3) la liste des w2 candidats (section 2) recalculee ;
(4) probabilite de la section 7 ; (5) canon de ma note citee a la section 1 (b9dd39f6c4ffa922) dans le manifeste de mon lot.
Usage : py -3.11 -P controles_rapides_machine2_v1.py <registre clone> <gel.md> <manifeste de mon lot grandes boites>"""
import hashlib
import importlib.util
import re
import sys
import unicodedata
from fractions import Fraction as F

REG, GEL, MANI = sys.argv[1].rstrip('/\\'), sys.argv[2], sys.argv[3]
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
print('(1) hachages de la graine de demonstration (section 3) :')
LISTE = {'MG': [F(x, 1000) for x in (1981, 1983, 1984, 1985, 1986, 1987, 1988, 1989)], 'PG': [F(x, 1000) for x in (2011, 2012, 2013, 2014, 2015, 2016, 2018, 2019)]}
texte = open(GEL, encoding='utf-8').read()
for s in ('MG', 'PG'):
    for r in (0, 1):
        h = hashlib.sha256(('DEMONSTRATION|%s|%d' % (s, r)).encode('ascii')).hexdigest(); n = int(h, 16) % 8
        ligne = 'sha256("DEMONSTRATION|%s|%d") = %s... ; modulo  8 =  %d -> w2 = %s' % (s, r, h[:16], n, ('%.3f' % float(LISTE[s][n])))
        print('    %s   | dans le gel : %s' % (ligne, 'OUI' if re.sub(r'\s+', ' ', ligne) in re.sub(r'\s+', ' ', texte) else 'NON'))
print('(3) w2 candidats recalcules depuis la section 2 : 0.01 < |w2 - 2| < 0.02, au millieme, moins {1.982, 2.017}')
for s, sg in (('MG', -1), ('PG', 1)):
    c = [F(k, 1000) for k in range(1000, 3000) if F(1, 100) < abs(F(k, 1000) - 2) < F(2, 100) and (F(k, 1000) < 2) == (sg < 0) and F(k, 1000) not in (F(1982, 1000), F(2017, 1000))]
    print('    %s : %d w2 : %s | identique a la liste du gel : %s' % (s, len(c), ' '.join('%.3f' % float(x) for x in c), c == LISTE[s]))
print('(2) couplage au point sacrifie (section 2) : g = kappa_m |w2 - 2| P / X(w2), X = X_saut_reel(P, 2, 1, 0, 0, w2), "%.5e" :')
KAP = {3: 0.0262, 4: 0.0200, 5: 0.0159}
w2 = F(101, 50); X = M.X_saut_reel(5, 2, 1, 0, 0, w2)
for m in (3, 4, 5):
    print('    m = %d : g = %s' % (m, '%.5e' % (KAP[m] * abs(float(w2) - 2.0) * 5 / X)))
print('    (note de machine 1 : 5.53067e-03, 4.22189e-03, 3.35640e-03)')
print('(4) probabilite qu un creneau n ait aucun w2 eligible en cinq rangs, MG : (3/8)^5 = %.4f (gel : 0.0074)' % ((3 / 8.0) ** 5))
print('(5) canon de ma note dans le manifeste de mon lot :')
for l in open(MANI, encoding='utf-8'):
    p = l.split()
    if len(p) == 5 and p[4].startswith('POUR_MACHINE1_grandes_boites'):
        print('    %s  %s  (gel : b9dd39f6c4ffa922)' % (p[0], p[4]))
b = open(MANI, 'rb').read().decode('utf-8'); raw = unicodedata.normalize('NFC', b).replace('\r\n', '\n').encode()
print('    canon de mon lot (manifeste) : %s  (gel : dce7431e7a8b4a8c)' % hashlib.sha256(raw).hexdigest()[:16])
