# -*- coding: ascii -*-
"""DERIVATION (v2) du pilote de machine 2 pour le gel "loi de la largeur, ordre 3, seconde partie" -- machine 2, 2026-11-16.
Le pilote de machine 1 (2882de31bc49ce2f) est DERIVE par remplacements de texte (chaque texte trouve UNE fois, sinon arret) ; rien n'est edite (regle 17).
Deux ecarts de comportement, tous deux dus a BOCAL4 et chacun aligne sur la reference qu'il rejoue :
  (1) `python -I` devient `python -P` : numpy et scipy sont dans le SITE UTILISATEUR de BOCAL4 (installation du Store) ; sous -I, `import numpy` echoue
      (verifie : ModuleNotFoundError). C'etait aussi mon choix au run du gel ter et au run de l'ordre 2.
  (2) fils BLAS : les appels de la sonde du lecteur et des feuilles tournent avec OPENBLAS/OMP/MKL_NUM_THREADS = 1 (comme mon run du gel ter, dont le
      pre-vol du mode point doit rendre les memes octets : condition C4) ; l'appel de la sonde DENSE garde l'environnement de l'appelant, c'est-a-dire les
      fils par defaut (comme mon run de l'ordre 2, qui a produit le depot sonde_ordre2.json auquel les ancres de la sonde dense sont comparees).
Usage : py -3.11 -P derive_pilote_machine2_v2.py <pilote de machine 1> <dossier de sortie>"""
import difflib
import hashlib
import os
import sys
import unicodedata

SRC, OUT = sys.argv[1], sys.argv[2]
NOM = 'pilote_gel_loi_machine2_v2.py'


def canon_txt(t):
    t = unicodedata.normalize('NFC', t).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


s = open(SRC, 'rb').read().decode('utf-8')
assert canon_txt(s) == '2882de31bc49ce2f', canon_txt(s)
REMPL = [
    ('"""PILOTE DU RUN du gel "loi de la largeur, ordre 3" -- machine 1, v1, 2026-11-15. UN RUN, DEUX ETAGES. Il ne mesure ni ne',
     '"""[DERIVE par machine 2 le 2026-11-16 du pilote de machine 1 (2882de31bc49ce2f) ; deux ecarts de comportement dus a BOCAL4 : -I devient -P (numpy est dans le site\n'
     'utilisateur) ; les fils BLAS valent 1 pour tous les appels SAUF la sonde dense (fils par defaut, comme au run de l\'ordre 2). Voir derive_pilote_machine2_v2.py et le diff.\n'
     'Le texte ci-dessous est celui d\'origine.]\n'
     'PILOTE DU RUN du gel "loi de la largeur, ordre 3" -- machine 1, v1, 2026-11-15. UN RUN, DEUX ETAGES. Il ne mesure ni ne'),
    ('PV = ["--prevol"] if PREVOL else []\n',
     'PV = ["--prevol"] if PREVOL else []\nENV_UN_FIL = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")\n'),
    ('subprocess.Popen([sys.executable, "-I"] + args, stdout=open(os.path.join(RUN, console), "w"), stderr=subprocess.STDOUT))',
     'subprocess.Popen([sys.executable, "-P"] + args, stdout=open(os.path.join(RUN, console), "w"), stderr=subprocess.STDOUT,\n'
     '                                                  env=(None if args[0] == S_DENSE else ENV_UN_FIL)))'),
]
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
