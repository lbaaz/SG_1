# -*- coding: ascii -*-
"""Compare, pour l'ETAGE A (instrument du depot : sonde en modes etage0, ancres, etage1) et pour l'ETAGE A' (les 18 lectures des neuf temoins positifs), le PRE-VOL (prevol_run) et le RUN REEL (run_sommet_2026-11-23), joues a deux heures de distance par le meme pilote sur la meme machine.
Rien n'est juge ici. Je montre ce qui change (les durees seulement, attendu) et ce qui ne change pas (les trajectoires des temoins, a l'octet).
Usage : py -3.11 -I comparaison_etage_A_prevol_run_machine2_v1.py <dossier du pre-vol> <dossier du run>"""
import hashlib
import json
import os
import sys

P, R = sys.argv[1:3]


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]


def diff(x, y, ch=''):
    out = []
    if isinstance(x, dict) and isinstance(y, dict):
        for k in sorted(set(x) | set(y)):
            if k not in x or k not in y:
                out.append(ch + '/' + k + ' (absent d un cote)')
            else:
                out += diff(x[k], y[k], ch + '/' + k)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        for i, (u, v) in enumerate(zip(x, y)):
            out += diff(u, v, ch + '[%d]' % i)
    elif x != y:
        out.append('%s : %r  vs  %r' % (ch, str(x)[:50], str(y)[:50]))
    return out


print('ETAGE A : fichiers de l instrument, pre-vol contre run :')
for f in ('sonde_ter_etage0.json', 'sonde_ter_ancres.json', 'sonde_ter_etage1.json', 'verdict_ter_instrument.json'):
    a, b = open(os.path.join(P, f), 'rb').read(), open(os.path.join(R, f), 'rb').read()
    if a == b:
        print('  %-30s IDENTIQUES (%s)' % (f, sha(os.path.join(P, f))))
        continue
    d = diff(json.load(open(os.path.join(P, f))), json.load(open(os.path.join(R, f))))
    autres = [x for x in d if 'duree_s' not in x and not x.startswith('/canons/')]
    print('  %-30s DIFFERENTS : %d champ(s) ; hors durees et hors empreintes des fichiers precedents : %d %s' % (f, len(d), len(autres), autres[:4] if autres else ''))
print('\nETAGE A\' : les 18 lectures des 9 temoins, pre-vol contre run (trajectoires) :')
n = ndiff = 0
for q in ('Qa', 'Qc', 'Qd', 'Qe', 'Qf', 'Q2a', 'Q2b', 'Q2c', 'Q2d'):
    for s in ('fantome', 'jumeau'):
        a = json.load(open(os.path.join(P, 'lect2D_%s_%s.json' % (q, s))))['lecture']['traj']
        b = json.load(open(os.path.join(R, 'lect2D_%s_%s.json' % (q, s))))['lecture']['traj']
        n += 1
        ndiff += (a != b)
print('  %d fichiers compares : trajectoires identiques (gamma, suivi, poids, iterations, residu : a l octet) : %d ; differentes : %d' % (n, n - ndiff, ndiff))
