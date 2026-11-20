# -*- coding: ascii -*-
"""Liste, champ par champ, les nombres de ses sorties REJOUEES (lot de l'acte) qui different de ceux de ses feuilles passees par mon pilote sur le run (dossier du run) de plus de 1e-12 : confronte la phrase de nn.4 (les ecarts sont sur des
nombres derives et non juges). Machine 2, 2026-11-18.
Usage : py -3.11 -P champs_au_dessus_de_1e12_machine2_v1.py <dossier du run> <dossier lot_m1 de l'acte>"""
import collections
import json
import re
import sys

RUN, LOTA = [a.rstrip('/\\') for a in sys.argv[1:3]]
FICHIERS = ['verdict.json', 'lecture_boites.json'] + ['lecture_densite_2d_%s.json' % c for c in ('MG3', 'MG4', 'MG5', 'PG3', 'PG4', 'PG5')]


def feuilles(a, b, p=''):
    if isinstance(a, dict):
        assert sorted(a) == sorted(b), p
        for k in a:
            yield from feuilles(a[k], b[k], p + '/' + k)
    elif isinstance(a, list):
        assert len(a) == len(b), p
        for u, v in zip(a, b):
            yield from feuilles(u, v, p + '[]')
    elif isinstance(a, (int, float)) and not isinstance(a, bool):
        yield (p, abs(a - b))


total = 0
cnt = collections.defaultdict(lambda: [0, 0.0])
for nom in FICHIERS:
    for p, d in feuilles(json.load(open(RUN + '/' + nom)), json.load(open(LOTA + '/' + nom))):
        total += 1
        if d > 1e-12:
            k = nom.split('_')[0] + ':' + re.sub(r'/(MG|PG)\d', '/<cellule>', p)
            cnt[k][0] += 1
            cnt[k][1] = max(cnt[k][1], d)
print('%d nombres compares ; champs au-dessus de 1e-12 : %d' % (total, len(cnt)))
for k, v in sorted(cnt.items(), key=lambda kv: -kv[1][1]):
    print('   %-70s %4d nombres, plus grand ecart %.2e' % (k, v[0], v[1]))
