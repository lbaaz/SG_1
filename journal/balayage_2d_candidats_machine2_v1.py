# -*- coding: ascii -*-
"""BALAYAGE (12 f, E19) : dans les dossiers donnes, aucun fichier JSON/JSONL AU FORMAT D'UNE SORTIE 2D (cle "k" des sondes de densite, "niveaux" des sondes de boite, "par_x" des feuilles de densite) ne porte
un w2 candidat du gel "pont" (les seize de la section 2 de la premiere partie, en fraction). Une recherche de structure n'est pas une preuve d'absence ; elle liste, elle ne juge pas.
Machine 2, 2026-11-17. Usage : py -3.11 -I balayage_2d_candidats_machine2_v1.py <dossier> [<dossier> ...]   (les chemins ne sont pas imprimes : seulement leur nombre et les touches, en relatif)"""
import json
import os
import sys
from fractions import Fraction as F

CANDS = set()
for k in (1981, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 2011, 2012, 2013, 2014, 2015, 2016, 2018, 2019):
    f = F(k, 1000)
    CANDS.add('%d/%d' % (f.numerator, f.denominator))
    CANDS.add('%.3f' % float(f))
vus = 0
touches = []
for r in sys.argv[1:]:
    for dp, dn, fn in os.walk(r):
        for f in fn:
            p = os.path.join(dp, f)
            if not f.endswith(('.json', '.jsonl')) or os.path.getsize(p) > 20000000:
                continue
            vus += 1
            try:
                txt = open(p, encoding='utf-8').read()
            except (OSError, UnicodeDecodeError):
                continue
            for l in (txt.split('\n') if f.endswith('.jsonl') else [txt]):
                if not l.strip():
                    continue
                try:
                    o = json.loads(l)
                except ValueError:
                    continue
                for ob in (o if isinstance(o, list) else [o]):
                    if isinstance(ob, dict) and str(ob.get('w2')) in CANDS and ('k' in ob or 'niveaux' in ob or 'par_x' in ob):
                        touches.append((os.path.relpath(p, r).replace(os.sep, '/'), ob.get('w2')))
print('%d fichiers JSON/JSONL lus dans %d dossier(s)' % (vus, len(sys.argv) - 1))
print('fichiers au format 2D portant un w2 candidat : %d' % len(touches))
for t in touches[:30]:
    print('   ', t)
