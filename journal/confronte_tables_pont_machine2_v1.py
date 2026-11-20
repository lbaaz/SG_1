# -*- coding: ascii -*-
"""CONFRONTATION de ma table d'eligibilite (eligibilite_pont_machine2_v1.py) a celle de machine 1 (eligibilite_pont_MG_PG_v1.json) et aux nombres de la section 7 du gel, puis TABLE COMMUNE (section 5 :
un w2 candidat y est eligible si et seulement s'il l'est dans les deux tables ET si les couplages ecrits de ses trois cellules sont les memes dans les deux). Machine 2, 2026-11-17.
Usage : py -3.11 -I confronte_tables_pont_machine2_v1.py <ma table.json> <mes details.json> <sa table.json> <gel.md> <table commune.json>"""
import json
import re
import sys

MA, MESD, SA, GEL, COMMUNE = sys.argv[1:6]
mine, det, sa = json.load(open(MA)), json.load(open(MESD)), json.load(open(SA))
texte = open(GEL, encoding='utf-8').read()
diffs = []


def cellules(t):
    out = {}
    for s, d in t['creneaux'].items():
        for c in d['candidats']:
            for ce in c['cellules']:
                out[(s, c['w2'], ce['m'])] = (ce['g'], ce['eligible'])
    return out


def w2s(t):
    return {s: [(c['w2'], c['eligible']) for c in d['candidats']] for s, d in t['creneaux'].items()}


print('1. STRUCTURE')
print('   creneaux : moi %s ; lui %s' % (sorted(mine['creneaux']), sorted(sa['creneaux'])))
for s in sorted(mine['creneaux']):
    a, b = w2s(mine)[s], w2s(sa)[s]
    print('   %s : w2 (fractions) identiques : %s ; eligibilite par w2 identique : %s' % (s, [x[0] for x in a] == [x[0] for x in b], a == b))
cm, cs = cellules(mine), cellules(sa)
print('   48 cellules : moi %d, lui %d ; memes cles : %s' % (len(cm), len(cs), set(cm) == set(cs)))
gdiff = [(k, cm[k][0], cs[k][0]) for k in cm if k in cs and cm[k][0] != cs[k][0]]
ediff = [(k, cm[k][1], cs[k][1]) for k in cm if k in cs and cm[k][1] != cs[k][1]]
print('2. COUPLAGES ECRITS : %d cellules avec un g different' % len(gdiff))
for x in gdiff:
    print('     ', x)
print('3. ELIGIBILITE PAR CELLULE : %d cellules ou nos eligibilites different' % len(ediff))
for x in ediff:
    print('     ', x)
print('4. NOMBRES DE LA SECTION 7 DU GEL (etendue au vide, plus grande etendue du lisse, plus grand pas ; 4 decimales) CONTRE MES DETAILS')
lignes = re.findall(r'^\s{2}(\d\.\d{3})\s+m3 (\d\.\d{4}) (\d\.\d{4}) (\d\.\d{4})(!?)\s+m4 (\d\.\d{4}) (\d\.\d{4}) (\d\.\d{4})(!?)\s+m5 (\d\.\d{4}) (\d\.\d{4}) (\d\.\d{4})(!?)\s+(INELIGIBLE|ELIGIBLE)', texte, re.M)
print('   lignes de cellules lues dans la section 7 : %d (attendu 16)' % len(lignes))
D = {(d['w2'], d['m']): d for d in det}
n_ok = n_tot = 0; ecarts = []
for l in lignes:
    w2 = '%d/%d' % (int(round(float(l[0]) * 1000)), 1000)
    from fractions import Fraction
    fr = Fraction(int(round(float(l[0]) * 1000)), 1000); cle = str(fr)
    for m, k in ((3, 1), (4, 5), (5, 9)):
        d = D[(cle, m)]
        lui = (float(l[k]), float(l[k + 1]), float(l[k + 2]))
        moi = (round(d['etendue_vide'], 4), round(d['etendue_lisse_max'], 4), round(d['pas_max'], 4))
        for nom, a, b in zip(('etendue au vide', 'etendue du lisse', 'pas'), moi, lui):
            n_tot += 1
            if abs(a - b) < 5e-5:
                n_ok += 1
            else:
                ecarts.append((l[0], 'm%d' % m, nom, a, b))
print('   %d nombres sur %d identiques a 4 decimales' % (n_ok, n_tot))
for e in ecarts:
    print('      ECART %s %s %s : moi %.4f ; lui %.4f' % e)
print('5. ECARTS DE DOUBLE PRECISION : plus grand ecart relatif de Gamma lu en double precision (-2 Im E) et en precision etendue : %.2e' % max(d.get('gamma_double_vs_hp_rel', 0.0) for d in det))
commun = {"creneaux": {}}
for s, d in mine['creneaux'].items():
    cand = []
    for c in d['candidats']:
        autre = [x for x in sa['creneaux'][s]['candidats'] if x['w2'] == c['w2']][0]
        memes_g = all(a['g'] == b['g'] for a, b in zip(c['cellules'], autre['cellules']))
        el = bool(c['eligible'] and autre['eligible'] and memes_g)
        cand.append({"w2": c['w2'], "eligible": el, "cellules": [{"m": a['m'], "g": a['g'], "eligible": bool(a['eligible'] and b['eligible'] and a['g'] == b['g'])} for a, b in zip(c['cellules'], autre['cellules'])]})
    commun["creneaux"][s] = {"candidats": cand}
json.dump(commun, open(COMMUNE, 'w', encoding='ascii'), indent=1, sort_keys=True)
print('6. TABLE COMMUNE : %s' % ' ; '.join('%s : %d eligibles sur %d' % (s, sum(1 for c in d['candidats'] if c['eligible']), len(d['candidats'])) for s, d in sorted(commun['creneaux'].items())))
for s, d in sorted(commun['creneaux'].items()):
    print('   %s eligibles : %s' % (s, ' '.join(c['w2'] for c in d['candidats'] if c['eligible'])))
