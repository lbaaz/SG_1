# -*- coding: ascii -*-
"""OBSERVATION (hors regle, aucune 2D) sur la regle de eta0 de la piece : eta0 = max(|w2 - 2|, g X(w2) / (P kappa_3)) avec g = kappa |w2 - 2| P / X(w2) donne, en reportant g : g X / (P kappa_3) = (kappa / kappa_3) |w2 - 2|, INDEPENDANT DE X (et du couplage) ;
comme kappa / kappa_3 >= 0.0363 / 0.0262 = 1.385 > 1, le second terme l'emporte aux 560 cellules et eta0 = (kappa / kappa_3) |w2 - 2|, a l'arrondi pres (g ecrit a six chiffres). Je le verifie sur MA table (detail_machine2_sommet_v1.json) : plus grand ecart relatif entre eta0 ecrit et (kappa / kappa_3)|w2 - 2|,
et nombre de cellules ou le premier terme |w2 - 2| l'emporterait. Consequence pour la piece : deux w2 de meme |w2 - 2| (par exemple 1.99989 et 2.00011) ont le meme eta0 pour un meme kappa, a l'arrondi pres du dernier chiffre, bien que leurs couplages different (X differe).
Usage : py -3.11 -I verifie_eta0_forme_sommet_machine2_v1.py <detail_machine2_sommet_v1.json>"""
import json
import sys
from fractions import Fraction as F

det = json.load(open(sys.argv[1]))
K3 = 0.0262
pire = 0.0
n_prem = 0
n = 0
egaux = {}
for r in det.values():
    d = float(abs(F(r['w2']) - 2))
    for c in r['cellules']:
        n += 1
        forme = float(c['kappa']) / K3 * d
        pire = max(pire, abs(float(c['eta0']) - forme) / forme)
        if d >= float(c['eta0']):
            n_prem += 1
        egaux.setdefault((round(d * 1e5), c['kappa']), set()).add(c['eta0'])
print('cellules : %d ; plus grand ecart relatif entre eta0 ecrit et (kappa / kappa_3) |w2 - 2| : %.2e (arrondi du g ecrit a six chiffres) ; cellules ou |w2 - 2| l emporterait : %d' % (n, pire, n_prem))
dist = [len(v) for v in egaux.values()]
print('couples (|w2 - 2| au cent-millieme, kappa) : %d ; avec UN SEUL eta0 ecrit pour les deux signes de delta : %d ; avec deux eta0 ecrits (dernier chiffre, arrondi de g) : %d' % (len(dist), sum(1 for x in dist if x == 1), sum(1 for x in dist if x == 2)))
