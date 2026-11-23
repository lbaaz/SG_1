# -*- coding: ascii -*-
"""APRES COUP, HORS GEL, SANS VALEUR D'EPREUVE (le run est joue ; E19 ne porte plus sur les cellules) : le RESIDU PAR KAPPA de l'acte (nn.6) a-t-il une cause lisible a UNE dimension ?
Je compare, aux 56 cellules, trois largeurs : le plateau LU (verdict de la feuille jouee dans le run), la colonne G3* de la table gelee (chaine d'ordre 3 sous l'absorbeur ADAPTE de machine 1, mediane de dix-huit variantes) et MA chaine du PREMIER ordre (chaine_premier_ordre_machine2_v1 :
echelle de x^5 au canal (2, 1), absorbeur lisse a W = 0.5, M = 200, L = 80 ; largeur lue comme le pole). Je rapporte, par kappa : ln(lu / ma chaine), ln(G3* / ma chaine), ln(G3* / lu) = ln q (le residu de l'acte). Aucun calcul 2D : les chaines sont a une dimension, le lu est relu dans le verdict.
Si le lecteur s'accorde a ma chaine a 1e-4 pres aux 56 cellules alors que G3* s'en ecarte comme le residu, le residu par kappa est une propriete de l'absorbeur adapte de la chaine de machine 1 (la mediane de ses dix-huit variantes), pas du lecteur 2D : c'est ce que ses notes 22h et 22i disaient aux barrieres.
Usage : py -3.11 -P residu_par_kappa_apres_coup_machine2_v1.py <dossier du run> <chaine_premier_ordre_machine2_v1.py : dossier qui le porte>"""
import json
import math
import os
import sys
from fractions import Fraction as F

RUN, DOSCH = sys.argv[1:3]
sys.path.insert(0, DOSCH)
import chaine_premier_ordre_machine2_v1 as C  # noqa: E402

V = json.load(open(os.path.join(RUN, 'verdict_sommet.json')))
KN = ['0.0363', '0.0530', '0.0800', '0.1300', '0.2000', '0.4000', '1.0000']
res = {k: [] for k in KN}
tau_cache = {}
for c in V['cellules']:
    w2 = F(c['w2'])
    w = float(w2)
    if w not in tau_cache:
        tau_cache[w] = C.echelle(w, 2, 1, 200)
    g = float(c['g'])
    g1 = C.largeur(tau_cache[w], (w - 2.0) / g)[0] * g
    lu = math.exp(c['ln_Gamma_pl'])
    g3 = math.exp(c['ln_G3'])
    res[c['kappa']].append((c['id'], math.log(lu / g1), math.log(g3 / g1), math.log(g3 / lu), c['etendue']))
print('%-7s %-34s %-34s %-34s' % ('kappa', 'ln(lu / ma chaine 1er ordre)', 'ln(G3* / ma chaine 1er ordre)', 'ln q = ln(G3* / lu) [residu de l acte]'))
print('%-7s %-34s %-34s %-34s' % ('', 'min, max, moyenne', 'min, max, moyenne', 'min, max, moyenne'))
tout = []
for k in KN:
    r = res[k]
    f = lambda i: (min(x[i] for x in r), max(x[i] for x in r), sum(x[i] for x in r) / len(r))
    a, b, d = f(1), f(2), f(3)
    tout += [abs(x[1]) for x in r]
    print('%-7s %+.5f %+.5f %+.5f      %+.5f %+.5f %+.5f      %+.5f %+.5f %+.5f' % (k, a[0], a[1], a[2], b[0], b[1], b[2], d[0], d[1], d[2]))
print('\nplus grand |ln(lu / ma chaine du premier ordre)| aux 56 cellules : %.5f ; mediane : %.5f' % (max(tout), sorted(tout)[len(tout) // 2]))
pg = max((abs(x[2]), x[0]) for k in KN for x in res[k])
print('plus grand |ln(G3* / ma chaine du premier ordre)| : %.5f (cellule %s)' % (pg[0], pg[1]))
# le residu de l'acte contre l'ecart G3* / ma chaine : correlation cellule a cellule
xs = [x[3] for k in KN for x in res[k]]
ys = [x[2] for k in KN for x in res[k]]
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
cov = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
r_ = cov / math.sqrt(sum((a - mx) ** 2 for a in xs) * sum((b - my) ** 2 for b in ys))
print('correlation, cellule par cellule, entre ln q (residu de l acte) et ln(G3* / ma chaine) : %.4f' % r_)
print('\nCe que ceci ne dit pas : que le premier ordre est meilleur que l ordre 3 (les deux chaines different de 0.0003 au plus et ont chacune son absorbeur) ; que le lecteur lit juste (il partage le moteur avec les chaines) ; rien du systeme ferme.')
