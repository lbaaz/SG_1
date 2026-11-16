# -*- coding: ascii -*-
"""BRUIT DE LA SONDE DENSE, PAR BARREAU : ecart relatif entre la largeur de la sonde dense deposee (nuit bis) et celle du lecteur
creux de machine 2 (gamma_W = 2 eta <W>), a chaque k, sur toutes les trajectoires comparees (les 30 des six points, les 4 du jumeau
H+), aux barreaux ou la largeur dense depasse le plancher 1e-12 (gel bis 3.10). HORS CHAINE. Lit mon JSON de validation.
Ce que cela dit : si l'ecart ne depend pas de k, c'est un plancher en absolu (le plancher des gels precedents) ; s'il croit avec eta, le
bruit de la decomposition dense croit avec la force de l'absorbeur. Ce que cela ne dit pas : lequel des deux lecteurs est juste ;
les deux lectures de mon lecteur (-2 Im E et 2 eta <W>) concordent entre elles a 7e-6 au pire (relatif), la dense n'a pas de seconde lecture.
Usage : python -P lecteur_creux_m2/bruit_dense_par_barreau_machine2_v1.py <validation.json>"""
import json
import statistics
import sys

d = json.load(open(sys.argv[1]))
par_k = {}
for r in d['resultats']:
    for c in r['configs'].values():
        for l in c['cmp']['lignes']:
            if 'gamma_W' in l and l['gamma_dense'] > 1e-12:
                par_k.setdefault(l['k'], []).append((abs(l['rel_W']), abs(l['gamma_W'] - l['gamma_dense'])))
print('k     eta/eta0   n    ecart relatif median   ecart relatif max    ecart absolu max')
for k in sorted(par_k):
    v = par_k[k]
    print('%3d  %9.4g  %3d    %.2e            %.2e           %.2e' % (k, 2.0 ** (-k), len(v), statistics.median(x[0] for x in v), max(x[0] for x in v), max(x[1] for x in v)))
forts = [x for k in par_k if k <= -1 for x in par_k[k]]
faibles = [x for k in par_k if k >= 3 for x in par_k[k]]
print('k <= -1 (eta >= 2 eta0) : %d lectures, ecart relatif median %.2e, max %.2e' % (len(forts), statistics.median(x[0] for x in forts), max(x[0] for x in forts)))
print('k >=  3 (eta <= eta0/8) : %d lectures, ecart relatif median %.2e, max %.2e' % (len(faibles), statistics.median(x[0] for x in faibles), max(x[0] for x in faibles)))
