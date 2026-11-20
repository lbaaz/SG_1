# -*- coding: ascii -*-
"""Compare deux JSON de meme structure nombre par nombre (relatif) : sert a R11 du releve de machine 1, rejoue sur BOCAL4 (sortie deposee differente ?). Machine 2, 2026-11-17.
Usage : py -3.11 -P compare_json_nombres_machine2_v1.py <a.json> <b.json>"""
import json
import sys

a, b = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
pire = [0.0, None]
n = 0
diffs = []
autres = []


def marche(x, y, ch=''):
    global n
    if isinstance(x, dict):
        assert sorted(x) == sorted(y), ch
        for k in x:
            marche(x[k], y[k], ch + '/' + k)
    elif isinstance(x, list):
        assert len(x) == len(y), ch
        for i, (u, v) in enumerate(zip(x, y)):
            marche(u, v, ch + '[%d]' % i)
    elif isinstance(x, float):
        n += 1
        if x != x and y != y:
            return
        d = abs(x - y) / max(abs(y), 1e-300)
        if d > pire[0]:
            pire[0], pire[1] = d, ch
        if x != y:
            diffs.append(ch)
    elif x != y:
        autres.append(ch)


marche(a, b)
print('%d nombres compares (NaN contre NaN tenus pour egaux) ; nombres differents : %d ; plus grand ecart relatif %.2e (%s)' % (n, len(diffs), pire[0], pire[1]))
print('differences non numeriques : %d' % len(autres))
