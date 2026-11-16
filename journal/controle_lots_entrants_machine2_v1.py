# -*- coding: ascii -*-
"""CONTROLE QUI M'A MANQUE AUX DEPOTS 99 ET 100 -- machine 2, 2026-11-16. Pour un dossier DEPOT_delta<nn>/ : chaque lot de son sous-dossier entrants/ (un dossier par lot, manifeste a cote de ses pieces) a-t-il son
MANIFESTE au registre (par canon B ou brut) et chacune de ses pieces de table au registre ? Lit un clone du registre, ne l'ecrit pas. Mon controle d'avant verifiait les lignes du manifeste de depot ; il ne verifiait pas
que tous les lots que j'avais extraits pour ce depot y etaient entres : c'est ce qui a laisse sept lots dehors (releve de machine 1, 16/11).
Usage (depuis BOCAL4) : py -3.11 -P certif_depot_99_100_machine2/controle_lots_entrants_machine2_v1.py <clone du registre> <DEPOT_delta<nn>>"""
import hashlib
import os
import re
import subprocess
import sys
import unicodedata

CL, DD = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16]
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h


REG = set()
for f in subprocess.check_output(['git', '-C', CL, 'ls-files']).decode().split('\n'):
    if f:
        REG.update(emp(open(os.path.join(CL, f), 'rb').read()))
print('registre : tete %s, %d canons' % (subprocess.check_output(['git', '-C', CL, 'rev-parse', '--short', 'HEAD']).decode().strip(), len(REG)))
ent = os.path.join(DD, 'entrants')
manques = []
for lot in sorted(os.listdir(ent)):
    d = os.path.join(ent, lot)
    mans = [f for f in os.listdir(d) if f.startswith('MANIFEST_') and f.endswith('.txt')]
    if len(mans) != 1:
        print('  %-70s manifeste : %d trouve(s)' % (lot, len(mans)))
        manques.append(lot)
        continue
    mp = os.path.join(d, mans[0])
    c = emp(open(mp, 'rb').read())
    pieces = []
    for l in open(mp, encoding='utf-8', errors='replace'):
        if re.match(r'^[0-9a-f]{16}\s', l):
            ch = l.split()
            pieces.append([x for x in ch[:2] if re.fullmatch(r'[0-9a-f]{16}', x)])
    abs_ = [p for p in pieces if not any(j in REG for j in p)]
    man_ok = any(x in REG for x in c)
    print('  %-70s lot %s  manifeste au registre : %-3s  pieces de table %2d, absentes %2d' % (lot, c[0], 'oui' if man_ok else 'non', len(pieces), len(abs_)))
    if not man_ok or abs_:
        manques.append(lot)
print('LOTS A MANQUE : %d %s' % (len(manques), manques))
sys.exit(0 if not manques else 1)
