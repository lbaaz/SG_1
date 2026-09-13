#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CONSTRUCTION DU BANC v11 = v10 (f65eccbfcdea91c1, CERTIFIE par machine 1, non edite) + la levee
de D-v10-1. machine 2, v1, 13/09/2026. Deux remplacements a ancre UNIQUE, asseres.

D-v10-1, MESUREE (mesure_9bis_tuple_machine2_v1.py, 11/11) : le controle 9bis compare un OBJET
PYTHON (le resultat en memoire) a une REFERENCE lue dans un FICHIER JSON. Or la serialisation
JSON change des types : un tuple devient une liste, une cle entiere devient une chaine. Neuf cles
du perimetre valent un tuple en memoire (/T1/A/etat, /T1/{A,B}/pics[0..1], /T1/B/etat,
/T1b/recherches/{a,b,c}/encadrement) : la comparaison finale `a != b` oppose alors (1.0, 0.0)
a [1.0, 0.0] et MORD, alors que les valeurs sont identiques. Le meme JSON, compare a la meme
reference par la meme marche, rend ZERO ecart. Le controle etait donc INSATISFIABLE : aucun run
ne pouvait le passer, quelle que soit sa mesure -- meme famille que le controle M du gel v4.

CORRECTIF : la comparaison se fait sur la SERIALISATION, c'est-a-dire sur ce que le run ECRIRA
dans son JSON -- exactement la fonction `assainir` de la sortie (dict a cles str, tuple et set en
liste, non-fini en repr), suivie d'un aller-retour json. Ce n'est pas une tolerance : rien n'est
relache, les valeurs se comparent toujours au bit. C'est la regle du 28/08 etendue d'un cran :
une empreinte sans sa serialisation n'est pas une empreinte ; une COMPARAISON non plus.
Le gel n'est pas touche (il dit "comparees par enumeration a profondeur declaree", il ne dit rien
des types du langage) : le pin reste le v7, a2b8463372e1f906.

Usage : construction_banc_v11_machine2_v1.py <banc_v10.py> <sortie banc_v11.py>
"""
import hashlib, os, sys, unicodedata

SRC, OUT = sys.argv[1], sys.argv[2]
raw = open(SRC, 'rb').read()
assert hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16] == 'f65eccbfcdea91c1', 'le v10 au poste n est pas le v10 certifie'
s = raw.decode('utf-8')

ANCRE = '''    DECLAREE ; exemptions duree/chemins A L'INTERIEUR ; tout le reste
    HORS PERIMETRE PAR CONSTRUCTION. Rend la liste des ecarts."""
    ecarts = []
'''
NEUF = '''    DECLAREE ; exemptions duree/chemins A L'INTERIEUR ; tout le reste
    HORS PERIMETRE PAR CONSTRUCTION. Rend la liste des ecarts.

    v11 (D-v10-1) : la reference est lue dans un FICHIER JSON, L est un objet
    Python. La serialisation change des types -- un tuple devient une liste,
    une cle entiere une chaine -- et la comparaison finale (a != b) opposait
    (1.0, 0.0) a [1.0, 0.0] : NEUF cles du perimetre valent un tuple en
    memoire, si bien qu'AUCUN run ne pouvait passer ce controle, quelle que
    soit sa mesure. La comparaison se fait donc sur la SERIALISATION -- ce
    que le run ECRIRA dans son JSON, meme fonction que la sortie. Rien n'est
    relache : les valeurs se comparent toujours au bit."""
    def _ser(o):
        if isinstance(o, dict):
            return {str(k): _ser(v) for k, v in o.items()}
        if isinstance(o, (list, tuple, set)):
            return [_ser(v) for v in o]
        if isinstance(o, float) and not math.isfinite(o):
            return repr(o)
        if isinstance(o, (np.floating, np.integer, np.bool_)):
            return _ser(o.item())
        if isinstance(o, np.ndarray):
            return _ser(o.tolist())
        if isinstance(o, Fraction):
            return str(o)
        return o

    L, reference = _ser(L), _ser(reference)
    ecarts = []
'''
REMPL = [
    (ANCRE, NEUF),
    ('DE LA CONSTANTE A (delta\' = 1/44100 ; v9 = v8 certifie re-parametre au gel v6 ;',
     'DE LA CONSTANTE A (delta\' = 1/44100 ; v11 = v10 certifie + levee de D-v10-1 : le\n'
     'controle 9bis compare sur la SERIALISATION, construction_banc_v11_machine2_v1.py ;\n'
     'v9 = v8 certifie re-parametre au gel v6 ;'),
]
for a, b in REMPL:
    assert s.count(a) == 1, 'ancre non unique ou absente : %r' % a[:70]
    s = s.replace(a, b)
s = s.replace('VERSION = "banc_qualification_machine1_v10"', 'VERSION = "banc_qualification_machine1_v11"')
assert 'banc_qualification_machine1_v11' in s
open(OUT, 'w', encoding='utf-8', newline='\n').write(s)
c = hashlib.sha256(unicodedata.normalize('NFC', s).encode()).hexdigest()[:16]
print('v11 ecrit : %s canon %s ; %d remplacements + VERSION ; pin du gel INCHANGE (v7)'
      % (os.path.basename(OUT), c, len(REMPL)))
