# -*- coding: ascii -*-
"""DIFFERENTIEL DES DEUX TIRAGES (machine 2, 2026-11-17) : la fonction tirer() de machine 1 (tirage_pont_machine1_v1.py, chargee depuis son texte sans l'editer) contre la mienne
(tirage_pont_machine2_v1.py), sur (a) la TABLE COMMUNE et N graines de six a douze chiffres ; (b) des tables d'eligibilite tirees AU HASARD (0 a 8 w2 eligibles par creneau), qui couvrent les
rangs de repli et PAS DE GEL. Sur chaque couple (graine, table) : meme decision (PAS DE GEL ou non), memes six cellules, memes couplages ecrits.
Usage : py -3.11 -I differentiel_tirage_machine2_v1.py <son script de tirage> <mon script de tirage> <table commune.json> <N graines> <N tables aleatoires>"""
import json
import random
import sys
from fractions import Fraction as F

executer = exec   # charge les definitions des deux scripts (texte relu, jamais edite) dans des espaces de noms separes
SON, MON, COMMUNE, N, NT = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
MUTATION = sys.argv[6] if len(sys.argv) > 6 else None            # optionnel : une faute introduite dans MON tirage (matrice de mutations du tirage)
src = open(SON, encoding='ascii').read(); coupe = src.index('if sys.argv[1] == "--autotest"')
sys.argv = ['son_script', '000000', COMMUNE]; ns = {}; executer(compile(src[:coupe], SON, 'exec'), ns)
son_tirer, LISTES, ORDRE = ns['tirer'], ns['LISTES'], ns['ORDRE']
src2 = open(MON, encoding='ascii').read(); coupe2 = src2.index("if sys.argv[2] == '--demonstration'")
sys.argv = ['mon_script'] + (['--mutation', MUTATION] if MUTATION else []) + [COMMUNE, '000000']; ns2 = {}; executer(compile(src2[:coupe2], MON, 'exec'), ns2)
mon_tirer = ns2['tirer']
T0 = json.load(open(COMMUNE))


def table_depuis(elig):                                   # elig : {creneau: ensemble de F eligibles}
    return {"creneaux": {s: {"candidats": [{"w2": "%d/%d" % (w.numerator, w.denominator), "eligible": w in elig[s],
                                           "cellules": [{"m": m, "g": "g%s_%d" % (w, m), "eligible": w in elig[s]} for m in (3, 4, 5)]} for w in sorted(LISTES[s])]} for s in ('MG', 'PG')}}


def son(graine, table):
    el = {}; cel = {}
    for s in ORDRE:
        for c in table['creneaux'][s]['candidats']:
            k = (s, F(c['w2'])); el[k] = bool(c['eligible']); cel[k] = {int(x['m']): str(x['g']) for x in c['cellules']}
    cs, jr = son_tirer(graine, lambda s, w: el[(s, w)], lambda s, w: [(m, cel[(s, w)][m]) for m in (3, 4, 5)])
    return None if cs is None else {c['id']: (F(c['w2']), c['g']) for c in cs}


def mon(graine, table):
    res, jr = mon_tirer(graine, table)
    return None if res is None else {k: (F(int(round(float(v[0]) * 1000)), 1000), v[1]) for k, v in res.items()}


rng = random.Random(20261117)
desaccords = 0; nbre = 0; pas_de_gel = 0; vus_w2 = {'MG': set(), 'PG': set()}
for i in range(N):
    graine = '%06d' % i if i % 2 == 0 else ''.join(rng.choice('0123456789') for _ in range(rng.randint(6, 12)))
    a, b = son(graine, T0), mon(graine, T0); nbre += 1
    if a != b:
        desaccords += 1
        if desaccords <= 5:
            print('DESACCORD (table commune) graine %s : %s | %s' % (graine, a, b))
    if a is None:
        pas_de_gel += 1
    else:
        vus_w2['MG'].add(a['MG3'][0]); vus_w2['PG'].add(a['PG3'][0])
print('(a) table commune : %d graines ; desaccords : %d ; PAS DE GEL : %d (%.4f) ; w2 de MG tires : %s ; w2 de PG tires : %s' % (
    nbre, desaccords, pas_de_gel, pas_de_gel / nbre, ' '.join('%.3f' % float(w) for w in sorted(vus_w2['MG'])), ' '.join('%.3f' % float(w) for w in sorted(vus_w2['PG']))))
d2 = 0; n2 = 0; pg2 = 0
for t in range(NT):
    elig = {s: set(w for w in LISTES[s] if rng.random() < rng.choice([0.0, 0.125, 0.25, 0.5, 0.75, 1.0])) for s in ('MG', 'PG')}
    T = table_depuis(elig)
    for i in range(200):
        graine = ''.join(rng.choice('0123456789') for _ in range(rng.randint(6, 10)))
        a, b = son(graine, T), mon(graine, T); n2 += 1
        if a != b:
            d2 += 1
            if d2 <= 5:
                print('DESACCORD (table aleatoire %d) graine %s : %s | %s' % (t, graine, a, b))
        if a is None:
            pg2 += 1
print('(b) %d tables aleatoires x 200 graines = %d tirages ; desaccords : %d ; PAS DE GEL : %d (%.3f)' % (NT, n2, d2, pg2, pg2 / n2))
