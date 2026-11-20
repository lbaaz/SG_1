# -*- coding: ascii -*-
"""Section 12 (c) : ce qu'un run complet coute sur BOCAL4, estime depuis MES temps mesures au point sacrifie (sonde de boite : secondes par boite ; sonde de densite : secondes par barreau), la geometrie
de la section 5 et une loi d'echelle declaree (cout ~ cote^3 pour la factorisation creuse en 2D). Ce n'est pas une mesure du run : c'est une estimation, avec ses hypotheses imprimees.
Machine 2, 2026-11-17. Usage : py -3.11 -P cout_run_machine2_v1.py <dossier des sorties du point sacrifie>"""
import glob
import json
import os
import re
import sys

D = sys.argv[1]
def boites(m, cote):
    out = []
    for f in glob.glob(os.path.join(D, 'boite_SA%d_%d_machine2.jsonl' % (m, cote))):
        for l in open(f):
            if l.strip():
                b = json.loads(l)
                if b['cote'] == cote:
                    out.append(b['secondes'])
    return out
T = {}
for m in (3, 4, 5):
    for c in (185, 300):
        v = boites(m, c)
        if v:
            T[(m, c)] = v[0]
print('temps mesures (secondes par boite, une boite par essai, plusieurs jobs en parallele sur la machine) :', {k: round(v) for k, v in sorted(T.items())})
logd = open(os.path.join(D, 'densite_2d_SA5_A_machine2.log')).read()
tk = [int(x) for x in re.findall(r'\((\d+) s\)', logd)]
tk_barreau = tk[:-1] if 'ecrit' in logd.split('\n')[-2] else tk       # le dernier '(.. s)' est le total
tk_barreau = [int(x) for x in re.findall(r'k = *-?\d+ : .*\((\d+) s\)', logd)]
print('densite, absorbeur A, 5 barreaux : %d barreaux lus, %.0f s au total (moyenne %.0f s par barreau)' % (len(tk_barreau), sum(tk_barreau), sum(tk_barreau) / len(tk_barreau)))
tA = sum(tk_barreau) / len(tk_barreau) * 12.0
N = {m: {'A': 2 * (m + max(8, m)) + 2 + 80, 'B': 2 * (m + max(8, m)) + 2 + 100, 'C': 2 * (m + max(8, m)) + 2 + 100, 'D': 2 * (m + max(8, m)) + 12 + 80} for m in (3, 4, 5)}
dens_cpu = sum(tA * (N[m][a] / N[5]['A']) ** 3 for m in (3, 4, 5) for a in 'ABCD') * 2          # deux cellules par profondeur (MG et PG)
def t_box(m, c):
    if (m, c) in T:
        return T[(m, c)]
    ref = [(mm, cc) for (mm, cc) in T if cc == c]
    return sum(T[k] for k in ref) / len(ref) if ref else float('nan')
box_cpu = 0.0
for m in (3, 4, 5):
    box_cpu += 2 * (10 * t_box(m, 185) + 10 * t_box(m, 300))
print('estimation : densite %.1f h de coeur, boites %.1f h de coeur, total %.1f h de coeur (hypotheses : cout ~ cote^3 entre absorbeurs ; boites UN ~ la boite 185 mesuree, DEUX ~ la 300 mesuree ; 2 cellules par profondeur)' % (dens_cpu / 3600, box_cpu / 3600, (dens_cpu + box_cpu) / 3600))
for p in (4, 8, 12):
    print('   avec %2d jobs en parallele : environ %.1f h (en negligeant la contention memoire et le desequilibre)' % (p, (dens_cpu + box_cpu) / 3600 / p))
# pics de memoire mesures (mesure_pic_memoire_machine2_v1.py : interpreteur lance directement, PeakWorkingSetSize)
for nom, cle in (('pic_densite_B_k8_machine2.log', 'densite, absorbeur B (le plus grand : boite 128 x 128), 5 barreaux, un barreau'), ('pic_boite_300_machine2.log', 'boite de cote 300, 5 barreaux')):
    f = os.path.join(D, 'pic_memoire', nom)
    if os.path.isfile(f):
        print('pic de memoire, %s : %s' % (cle, [l for l in open(f).read().split('\n') if l.startswith('code de sortie')][0]))
