# -*- coding: ascii -*-
"""AUTOTEST de MA regle des rangs (section 6 de la piece) : la graine de DEMONSTRATION n'exerce pas les branches "w2 ineligible", "w2 deja retenu", "pas deux w2 eligibles distincts en dix rangs".
Je les exerce sur des tables COMMUNES MODIFIEES (copies temporaires, la vraie n'est pas touchee) et je compare la sortie de tirage_sommet_machine2_v1.py a une SECONDE ecriture de la regle, faite ici (boucle sur les rangs, listes explicites).
Usage : py -3.11 -I autotest_regle_rangs_sommet_machine2_v1.py <table commune JSON> <dossier temporaire>"""
import copy
import hashlib
import json
import os
import re
import subprocess
import sys
from fractions import Fraction as F

TABLE, TMP = sys.argv[1], sys.argv[2]
ICI = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(TABLE))
ORDRE = ('MP', 'PP', 'MG', 'PG')


def attendu(tab, graine, nom):
    """seconde ecriture : boucle explicite sur les rangs 0 a 9"""
    liste = sorted(F(c['w2']) for c in tab['creneaux'][nom]['candidats'])
    ok = {F(c['w2']): c['eligible'] for c in tab['creneaux'][nom]['candidats']}
    pris = []
    for r in range(10):
        n = int(hashlib.sha256(('%s|%s|%d' % (graine, nom, r)).encode('ascii')).hexdigest(), 16) % len(liste)
        w = liste[n]
        if ok[w] and w not in pris:
            pris.append(w)
        if len(pris) == 2:
            return pris
    return None


def lance(tab, graine, nom_fichier):
    p = os.path.join(TMP, nom_fichier)
    json.dump(tab, open(p, 'w'))
    r = subprocess.run([sys.executable, '-I', os.path.join(ICI, 'tirage_sommet_machine2_v1.py'), p, graine, '--demonstration'], capture_output=True, text=True)
    return r.returncode, r.stdout


def retenus(sortie):
    return {m[0] + m[1]: F(m[2]) for m in re.findall(r'=> (MP|PP|MG|PG)([ab]) : w2 = (\S+) =', sortie)}


def ineligible(tab, nom, w2s):
    t = copy.deepcopy(tab)
    for c in t['creneaux'][nom]['candidats']:
        if F(c['w2']) in w2s:
            c['eligible'] = False
    return t


tests = []
# T0 : table intacte
rc, out = lance(base, 'DEMONSTRATION', 't0.json')
r = retenus(out)
tests.append(('T0 table intacte : w2 retenus = seconde ecriture, quatre creneaux', rc == 0 and all([r[n + 'a'], r[n + 'b']] == attendu(base, 'DEMONSTRATION', n) for n in ORDRE)))
# T1 : le w2 du rang 0 de PP (2.00020) est ineligible -> rang 1 devient "a" ; le rang 2 retombe sur le meme w2 (deja retenu) ; il faut aller plus loin pour "b"
w_pp0 = F(10001, 5000)
t1 = ineligible(base, 'PP', {w_pp0})
rc, out = lance(t1, 'DEMONSTRATION', 't1.json')
r = retenus(out)
att = attendu(t1, 'DEMONSTRATION', 'PP')
tests.append(('T1 PP rang 0 ineligible : retenus %s = seconde ecriture %s ; a != b ; 2.00020 absent' % ([str(r['PPa']), str(r['PPb'])], [str(x) for x in att]), rc == 0 and [r['PPa'], r['PPb']] == att and r['PPa'] != r['PPb'] and w_pp0 not in (r['PPa'], r['PPb'])))
# T2 : le w2 du rang 1 de PP (2.00018) est ineligible aussi
w_pp1 = F(100009, 50000)
t2 = ineligible(base, 'PP', {w_pp0, w_pp1})
rc, out = lance(t2, 'DEMONSTRATION', 't2.json')
r = retenus(out)
att = attendu(t2, 'DEMONSTRATION', 'PP')
tests.append(('T2 PP rangs 0 et 1 ineligibles : retenus %s = seconde ecriture %s' % ([str(r['PPa']), str(r['PPb'])], [str(x) for x in att]), rc == 0 and [r['PPa'], r['PPb']] == att and not ({w_pp0, w_pp1} & {r['PPa'], r['PPb']})))
# T3 : un seul w2 eligible dans MP -> PAS DE GEL (code 2)
t3 = copy.deepcopy(base)
cs = t3['creneaux']['MP']['candidats']
for i, c in enumerate(cs):
    c['eligible'] = (i == 0)
rc, out = lance(t3, 'DEMONSTRATION', 't3.json')
tests.append(('T3 MP : un seul w2 eligible -> PAS DE GEL (code de sortie 2, message)', rc == 2 and 'PAS DE GEL' in out and attendu(t3, 'DEMONSTRATION', 'MP') is None))
# T4 : determinisme : deux executions identiques
rc1, o1 = lance(base, 'DEMONSTRATION', 't4a.json')
rc2, o2 = lance(base, 'DEMONSTRATION', 't4b.json')
tests.append(('T4 determinisme : deux executions donnent la meme sortie', rc1 == rc2 == 0 and o1 == o2))
for nom, ok in tests:
    print('%s : %s' % ('TIENT' if ok else 'ECHOUE', nom))
print('AUTOTEST : %s' % ('TIENT (%d sur %d)' % (sum(1 for _, ok in tests if ok), len(tests)) if all(ok for _, ok in tests) else 'ECHOUE'))
