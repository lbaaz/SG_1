# -*- coding: ascii -*-
"""REJEU DE L'ETAPE 1 de la note hors chaine de machine 1 (loi de la largeur) -- machine 2, 2026-11-15. Hors chaine, lecture seule, AUCUN calcul 2D : de l'arithmetique sur des pieces.
Rejoue etape1_etalon_machine1_v1.py (sans le modifier) sur MES copies des pieces (registre clone neuf a 8d54bf9 ; MON verdict_ter.json du run E-B ter), compare sa sortie a celle de machine 1, refait les
tableaux de la note qui citent mes largeurs (section 0 point 1 : etendue de ln q2 par point ; section 3.5 : Gamma_pl(A) / |delta| de l'etiquette (6, 2) aux sept points) et mesure la dependance de ma
reference a l'absorbeur (|ln(Gamma_pl(X) / Gamma_pl(A))|, X = B, C, D) sur les etats QUALIFIES.
Usage : py -3.11 -P etape1_rejeu_machine2_v1.py <etape1_etalon_machine1_v1.py> <sonde_ordre2.json> <verdict_ordre2.json> <verdict_ter.json> <etape1_etalon_v1.json de machine 1> <sortie.json>"""
import json
import math
import statistics as st
import subprocess
import sys

SCRIPT, DEP, V98, VT, SIEN, SORTIE = sys.argv[1:7]
r = subprocess.run([sys.executable, '-I', '-B', SCRIPT, DEP, V98, VT, SORTIE], capture_output=True, text=True)
print('code retour du script de machine 1 :', r.returncode)
print(r.stdout)
if r.returncode:
    print(r.stderr[-800:])
    raise SystemExit(1)
mien, sien = json.load(open(SORTIE)), json.load(open(SIEN))


def feuilles(a, b, ch, out):
    if isinstance(a, dict):
        if sorted(a) != sorted(b):
            out.append((ch, 'CLES', None))
            return
        for k in a:
            feuilles(a[k], b[k], ch + [k], out)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append((ch, 'LONGUEUR', None))
            return
        for n, (x, y) in enumerate(zip(a, b)):
            feuilles(x, y, ch + [n], out)
    else:
        out.append((ch, a, b))


out = []
feuilles(mien, sien, [], out)
diff = [(c, a, b) for c, a, b in out if a != b]
pire = max([abs(a / b - 1.0) for c, a, b in diff if isinstance(a, float) and isinstance(b, float) and b != 0] + [0.0])
nonnum = [d for d in diff if not (isinstance(d[1], float) and isinstance(d[2], float))]
print('sortie de machine 1 contre la mienne : %d feuilles, %d differentes (non numeriques : %d), plus grand ecart relatif %.3e' % (len(out), len(diff), len(nonnum), pire))
Q = [x for x in mien['etats'] if x['statut'] == 'QUALIFIE']
print('etats juges %d, QUALIFIES %d' % (len(mien['etats']), len(Q)))
pts = sorted({x['id'] for x in Q})
for cle, nom in (('q2', 'lecture deposee'), ('q2p', 'plateau')):
    ext = [max(math.log(x[cle]) for x in Q if x['id'] == p) - min(math.log(x[cle]) for x in Q if x['id'] == p) for p in pts]
    print('etendue de ln q2 dans un point, contre la %-15s : mediane %.4f (de %.4f a %.4f)' % (nom, st.median(ext), min(ext), max(ext)))
print('tableau 3.5, etiquette (6, 2) : Gamma_pl(A) / |delta| aux sept points (QUALIFIES)')
for i in ('L2', 'M1', 'L1', 'M2', 'C4', 'C3', 'L3'):
    for x in [x for x in Q if x['id'] == i and (x['n1'], x['n2']) == (6, 2)]:
        print('  %s  delta %+.2f  rang %2d  Gamma_pl/|delta| = %.3e  q1 %.3f  q2 %.3f' % (i, x['delta'], x['rang'], x['G_pl'] / abs(x['delta']), x['q1p'], x['q2p']))
v = json.load(open(VT, encoding='utf-8'))
tous = [(p, e) for p, P in v['points'].items() for e in P['etats'] if e['statut'] == 'QUALIFIE']
dom = {'C1', 'C2', 'C3', 'C4', 'M1', 'M2'}
print('dependance de ma reference a l absorbeur, |ln(Gamma_pl(X) / Gamma_pl(A))| sur les %d etats QUALIFIES du verdict (et sur les %d des six points C1 C2 C3 C4 M1 M2)' % (
    len(tous), len([1 for p, e in tous if p in dom])))
for nom, sel in (('tous les points', tous), ('six points', [(p, e) for p, e in tous if p in dom])):
    for X in 'BCD':
        l = [abs(e['plateaux'][X]['ecart_ln_A']) for p, e in sel if e['plateaux'].get(X, {}).get('statut') == 'PLATEAU' and 'ecart_ln_A' in e['plateaux'][X]]
        print('  %-15s %s : %3d etats, mediane %.4f, p90 %.4f, max %.4f' % (nom, X, len(l), st.median(l), sorted(l)[int(0.9 * len(l))], max(l)))
