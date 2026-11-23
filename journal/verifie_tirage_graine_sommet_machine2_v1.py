# -*- coding: ascii -*-
"""VERIFICATION de mon tirage reel (graine de l'operateur) du gel "sommet" : (1) une SECONDE ecriture de la regle (boucle sur les rangs 0 a 9, section 6 de la piece) depuis la table commune ; (2) les huit w2 et les 56 cellules du journal de mon tirage retrouves dans MA table et dans CELLE de machine 1
(chaines identiques : g, eta0, r_c) ; (3) le hachage recalcule ici par hashlib, hors de mon script de tirage. Je ne lis pas le tirage de machine 1 : elle n'a peut-etre pas encore tire.
Usage : py -3.11 -I verifie_tirage_graine_sommet_machine2_v1.py <graine> <table commune JSON> <ma table JSON> <table JSON de machine 1> <mon journal de tirage>"""
import hashlib
import json
import re
import sys
from fractions import Fraction as F

GRAINE, COM, MA, SA, JOURNAL = sys.argv[1:6]
assert re.fullmatch(r'[0-9]{6,}', GRAINE), 'graine non conforme'
com = json.load(open(COM))['creneaux']
ma = json.load(open(MA))['creneaux']
sa = json.load(open(SA))['creneaux']
txt = open(JOURNAL, encoding='ascii').read()
res = {}
for nom in ('MP', 'PP', 'MG', 'PG'):
    liste = sorted(F(c['w2']) for c in com[nom]['candidats'])
    ok = {F(c['w2']): c['eligible'] for c in com[nom]['candidats']}
    pris, trace = [], []
    for r in range(10):
        n = int(hashlib.sha256(('%s|%s|%d' % (GRAINE, nom, r)).encode('ascii')).hexdigest(), 16)
        w = liste[n % len(liste)]
        trace.append((r, n % len(liste), str(w), ok[w], w in pris))
        if ok[w] and w not in pris:
            pris.append(w)
        if len(pris) == 2:
            break
    res[nom] = pris
    print('%s : rangs lus %d ; w2 retenus %s ; trace (rang, indice, w2, eligible, deja) %s' % (nom, len(trace), [str(w) for w in pris], trace))
journal_w = {m[0] + m[1]: m[2] for m in re.findall(r'=> (MP|PP|MG|PG)([ab]) : w2 = (\S+) =', txt)}
seconde = {nom + l: str(w) for nom, ws in res.items() for l, w in zip('ab', ws)}
print('\n(1) seconde ecriture contre le journal de mon tirage : %s' % ('IDENTIQUES' if journal_w == seconde and len(seconde) == 8 else 'DIFFERENTES %s %s' % (journal_w, seconde)))
cm = {m[0] + m[1] + m[2]: (m[3], m[4], m[5], m[6]) for m in re.findall(r'(MP|PP|MG|PG)([ab])(\d)\s+kappa ([0-9.]+)\s+g = ([0-9.e+-]+)\s+eta0 = ([0-9.e+-]+)\s+r_c = (\d+)', txt)}


def cherche(table, nom, w2):
    return [c for c in table[nom]['candidats'] if F(c['w2']) == F(w2)][0]['cellules']


nbm = nbs = 0
for cle, (kappa, g, e, rc) in sorted(cm.items()):
    nom, lettre, j = cle[:2], cle[2], int(cle[3:])
    w2 = seconde[nom + lettre]
    for table, nomt in ((ma, 'ma table'), (sa, 'table de machine 1')):
        c = cherche(table, nom, w2)[j - 1]
        if (c['kappa'], c['g'], c['eta0'], str(c['r_c'])) != (kappa, g, e, rc):
            print('DIFFERENCE %s %s : %s' % (nomt, cle, (c, kappa, g, e, rc)))
        elif nomt == 'ma table':
            nbm += 1
        else:
            nbs += 1
print('(2) cellules du journal : %d ; retrouvees identiques dans ma table : %d ; dans la table de machine 1 : %d' % (len(cm), nbm, nbs))
print('(3) hachages recalcules ici : %s' % ' ; '.join('%s|%s|%d -> %s' % (GRAINE, nom, r, hashlib.sha256(('%s|%s|%d' % (GRAINE, nom, r)).encode('ascii')).hexdigest()[:16]) for nom in ('MP', 'PP', 'MG', 'PG') for r in (0, 1)))
print('\nTIENT' if journal_w == seconde and len(cm) == 56 == nbm == nbs else '\nECHOUE')
