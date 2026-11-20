# -*- coding: ascii -*-
"""Compare les pieces de machine 1 (lot mis a plat, celui que le run a utilise) a son manifeste : canon B (sha256 NFC UTF-8, CRLF->LF, 16 hex) de chaque piece. Machine 2, 2026-11-18.
Lu APRES le run (le dossier du lot n'a pas ete touche entre-temps : aucun script de ma part ne l'ecrit).
Usage : py -3.11 -P verifie_pieces_m1_machine2_v1.py <manifeste de m1> <lot a plat>"""
import hashlib
import os
import re
import sys
import unicodedata

man = open(sys.argv[1], encoding='utf-8').read().split('\n')
lot = sys.argv[2]
att = {}
for ligne in man:
    p = ligne.split()
    if len(p) >= 5 and re.fullmatch('[0-9a-f]{16}', p[0]):
        att[p[-1]] = p[0]


def emp(chemin):
    brut = open(chemin, 'rb').read()
    try:
        t = unicodedata.normalize('NFC', brut.decode('utf-8')).replace('\r\n', '\n').encode()
    except UnicodeDecodeError:
        t = brut
    return hashlib.sha256(t).hexdigest()[:16]


differentes, absentes, vues = [], [], 0
for k, h in sorted(att.items()):
    p = os.path.join(lot, os.path.basename(k))
    if not os.path.isfile(p):
        absentes.append(os.path.basename(k))
        continue
    vues += 1
    if emp(p) != h:
        differentes.append(os.path.basename(k))
print('pieces au manifeste : %d ; presentes dans le lot a plat : %d ; absentes : %d ; de canon different : %d' % (len(att), vues, len(absentes), len(differentes)))
for n in absentes + differentes:
    print('   ', n)
