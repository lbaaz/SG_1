# -*- coding: ascii -*-
"""DERIVATION du pilote de machine 2 pour le gel "loi de la largeur, ordre 3, seconde partie" -- machine 2, 2026-11-16.
Le pilote de machine 1 (2882de31bc49ce2f) lance ses fils avec `python -I`. Sur BOCAL4 numpy et scipy sont dans le SITE UTILISATEUR
(installation du Store, comme au gel ter ou j'utilisais `py -3.11 -P`) : sous -I, `import numpy` echoue (verifie : ModuleNotFoundError).
Le pilote est donc DERIVE par UN SEUL remplacement de texte (chaque texte trouve une fois, sinon arret) : -I devient -P ; le reste est inchange.
Rien n'est edite (regle 17). Ecrit le pilote derive, son diff unifie, et affiche les canons.
Usage : py -3.11 -P derive_pilote_machine2_v1.py <pilote de machine 1> <dossier de sortie>"""
import difflib
import hashlib
import os
import sys
import unicodedata

SRC, OUT = sys.argv[1], sys.argv[2]
NOM = 'pilote_gel_loi_machine2_v1.py'


def canon_txt(t):
    t = unicodedata.normalize('NFC', t).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


s = open(SRC, 'rb').read().decode('utf-8')
assert canon_txt(s) == '2882de31bc49ce2f', canon_txt(s)
REMPL = [('subprocess.Popen([sys.executable, "-I"] + args,', 'subprocess.Popen([sys.executable, "-P"] + args,'),
         ('"""PILOTE DU RUN du gel "loi de la largeur, ordre 3" -- machine 1, v1, 2026-11-15. UN RUN, DEUX ETAGES.',
          '"""[DERIVE par machine 2 le 2026-11-16 du pilote de machine 1 (2882de31bc49ce2f) : UN SEUL changement de comportement, le drapeau des fils : -I devient -P,\n'
          'parce que numpy et scipy sont dans le site utilisateur de BOCAL4 ; voir derive_pilote_machine2_v1.py et le diff. Le texte ci-dessous est celui d\'origine.]\n'
          'PILOTE DU RUN du gel "loi de la largeur, ordre 3" -- machine 1, v1, 2026-11-15. UN RUN, DEUX ETAGES.')]
t = s
for i, (a, b) in enumerate(REMPL):
    assert t.count(a) == 1, 'remplacement %d : texte trouve %d fois' % (i + 1, t.count(a))
    t = t.replace(a, b)
t.encode('ascii')
os.makedirs(OUT, exist_ok=True)
p = os.path.join(OUT, NOM)
open(p, 'w', encoding='ascii', newline='\n').write(t)
d = list(difflib.unified_diff(s.split('\n'), t.split('\n'), 'pilote_gel_loi_machine1_v1.py', NOM, lineterm='', n=1))
open(os.path.join(OUT, NOM[:-3] + '.diff'), 'w', encoding='ascii', newline='\n').write('\n'.join(d) + '\n')
print('source %s ; derive %s canon %s ; %d remplacements ; diff %d lignes' % (canon_txt(s), NOM, canon_txt(t), len(REMPL), len(d)))
