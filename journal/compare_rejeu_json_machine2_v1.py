# -*- coding: ascii -*-
"""Compare les JSON rejoues de l'eligibilite de machine 1 (son script, sur ma machine, sans l'editer) a son JSON (canon d03c9ca093ea5bfc) : octets identiques ? ; champs NON flottants differents
(eligibilite, couplages g, m, m_bord, w2, textes) ; nombre de flottants differents et plus grand ecart relatif. Machine 2.
Usage : py -3.11 -I compare_rejeu_json_machine2_v1.py <son json> <json rejoue> [<json rejoue> ...]"""
import json
import sys

SON = sys.argv[1]; sa = json.load(open(SON)); sab = open(SON, 'rb').read()
for f in sys.argv[2:]:
    a = json.load(open(f)); ab = open(f, 'rb').read().replace(b'\r\n', b'\n')
    nf = [0, 0]; mx = [0.0]; autres = []

    def rec(x, y, ch=''):
        if isinstance(x, dict):
            for k in x:
                rec(x[k], y[k], ch + '/' + k)
        elif isinstance(x, list):
            for i, (u, v) in enumerate(zip(x, y)):
                rec(u, v, ch + '[%d]' % i)
        elif isinstance(x, float) and isinstance(y, float):
            nf[0] += 1
            if x != y:
                nf[1] += 1; mx[0] = max(mx[0], abs(x - y) / max(abs(y), 1e-300))
        elif x != y:
            autres.append((ch, x, y))
    rec(a, sa)
    print('%-34s octets identiques (fins de ligne normalisees) : %-5s ; champs non flottants differents : %d ; flottants : %d compares, %d differents, plus grand ecart relatif %.2e' % (
        f, ab == sab.replace(b'\r\n', b'\n'), len(autres), nf[0], nf[1], mx[0]))
