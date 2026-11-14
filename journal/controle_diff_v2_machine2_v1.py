# -*- coding: ascii -*-
"""Controle du diff v1 -> v2 de l'acte (machine 2). Arguments : v1 v2 diff."""
import difflib
import hashlib
import re
import sys
import unicodedata

v1p, v2p, dfp = sys.argv[1:4]


def emp(raw):
    t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
    return hashlib.sha256(t).hexdigest()[:16]


r1, r2, rd = open(v1p, 'rb').read(), open(v2p, 'rb').read(), open(dfp, 'rb').read()
print('canons : v1 %s (attendu c396a00095a0b9e3) ; v2 %s (attendu bdf8c5a0c73096a4) ; diff %s' % (emp(r1), emp(r2), emp(rd)))
v1 = r1.decode('utf-8').split('\n')
v2 = r2.decode('utf-8').split('\n')
# 1. mon propre diff
sm = difflib.SequenceMatcher(None, v1, v2, autojunk=False)
ops = [o for o in sm.get_opcodes() if o[0] != 'equal']
print('mon diff : %d blocs ; lignes otees %d, posees %d' % (len(ops), sum(o[2] - o[1] for o in ops), sum(o[4] - o[3] for o in ops)))
for o in ops:
    print('   %s v1[%d:%d] -> v2[%d:%d]' % (o[0], o[1] + 1, o[2], o[3] + 1, o[4]))
# 2. application du diff de m1 a la v1, a ma facon (blocs @@ -a,b +c,d @@)
d = rd.decode('utf-8').split('\n')
i = 2                                   # saute les deux lignes d'en-tete
res = list(v1)
decal = 0
blocs = 0
ok = True
while i < len(d):
    m = re.match(r'@@ -(\d+),(\d+) \+(\d+),(\d+) @@', d[i])
    if not m:
        i += 1
        continue
    blocs += 1
    a, b, c, dd = map(int, m.groups())
    i += 1
    vieux, neuf = [], []
    while i < len(d) and not d[i].startswith('@@'):
        t = d[i]
        if t.startswith('-'):
            vieux.append(t[1:])
        elif t.startswith('+'):
            neuf.append(t[1:])
        elif t.startswith(' '):
            vieux.append(t[1:])
            neuf.append(t[1:])
        i += 1
    while vieux and vieux[-1] == '' and d and i >= len(d):
        break
    # le bloc remplace v1[a-1 : a-1+b] (+decal) par neuf
    seg = res[a - 1 + decal: a - 1 + decal + b]
    if [s for s in seg] != [s for s in vieux][:b]:
        ok = False
        print('   bloc %d : le contexte de la v1 ne colle pas' % blocs)
    res[a - 1 + decal: a - 1 + decal + b] = neuf[:dd]
    decal += dd - b
print('application du diff de m1 a la v1 : %d blocs ; resultat == v2 : %s ; contexte coherent : %s' % (blocs, res == v2, ok))
# 3. textes ajoutes : ASCII, <= 100 colonnes, pas de pour cent
poses = [l for o in ops for l in v2[o[3]:o[4]]]
print('lignes posees : %d ; non ASCII %d ; > 100 col %d ; avec %% %d' % (len(poses), sum(any(ord(c) > 127 for c in l) for l in poses),
      sum(len(l) > 100 for l in poses), sum('%' in l for l in poses)))
# 4. empreintes de 16 hex nouvelles
h = lambda t: set(re.findall(r'\b[0-9a-f]{16}\b', t))
n1, n2 = h('\n'.join(v1)), h('\n'.join(v2))
print('empreintes : v1 %d, v2 %d ; nouvelles %s ; disparues %s' % (len(n1), len(n2), sorted(n2 - n1), sorted(n1 - n2)))
