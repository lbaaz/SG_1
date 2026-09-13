#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CONSTRUCTION DU BANC v10 = v9 (9b3ec0b0c4978158, emis par machine 1, non edite) + la levee de
D-v9-1 + le PIN sur le gel v7. machine 2, v2, 13/09/2026. Quatre remplacements a ancre UNIQUE,
asseres. v2 = v1 (trois remplacements, pin encore sur le v6 : le brouillon qui a valide la levee
de D-v9-1 -- banc 56/56, G11/G12 MORDENT) + le pin sur le gel v7 (canon et taille en arguments,
verifies sur le fichier avant d'etre ecrits).

D-v9-1, CAUSE MESUREE (harness du 13/09, cellule par cellule) : au reglage v6 la trajectoire
synthetique de BASE (dep = 0) rend deja 148 points dans la fenetre pour n_min = 179 (plan) et 296
pour 359 (G-dt) -- pas seulement G11/G12. SynthAlpha demarre sa phase 2 a l'instant de bascule
ARRONDI a la grille de phase 1 (n = round(tb / DT1), DT1 = 0.006), et au reglage v6 la duree
k tau_dom' = 4.77e-03 est PLUS PETITE que DT1 : l'arrondi place le depart jusqu'a 0.003 apres tb,
c'est-a-dire A L'INTERIEUR de la fenetre [t* - tau_dom', t* - tau_CAP'], dont une partie des
points manque. Au reglage v8 (k tau_dom' = 3.1e-03) les t* du synthetique tombaient de sorte que
la fenetre restait couverte ; c'etait une coincidence de grille, pas une propriete. L'arrondi
vers le BAS (floor) garantit t0 <= tb, donc la serie couvre la fenetre entiere a tout reglage.
Le vrai moteur n'est pas concerne (sa phase 1 detecte la bascule 5.3 a k tau_dom_0 = 0.05, bien
avant, et l'etage 2a descend jusqu'a la bascule 2b sur sa propre grille).
Usage : construction_banc_v10_machine2_v2.py <banc_v9.py> <sortie banc_v10.py> <gel v7.md>
"""
import hashlib, os, sys, unicodedata

SRC, OUT, GEL = sys.argv[1], sys.argv[2], sys.argv[3]


def canon(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


assert canon(SRC) == '9b3ec0b0c4978158', 'le v9 au poste n est pas le v9 emis'
cg, tg = canon(GEL), os.path.getsize(GEL)
assert os.path.basename(GEL) == 'constante_A_pre_enregistrement_v7.md'
s = open(SRC, 'rb').read().decode('utf-8')
REMPL = [
    ('            n = int(round(tb / DT1))\n',
     '            n = int(math.floor(tb / DT1))   # v10 (D-v9-1) : floor, jamais round -- t0 <= tb, la fenetre est couverte a tout reglage\n'),
    ('VERSION = "banc_qualification_machine1_v9"', 'VERSION = "banc_qualification_machine1_v10"'),
    ('DE LA CONSTANTE A (delta\' = 1/44100 ; v9 = v8 certifie re-parametre au gel v6)',
     'DE LA CONSTANTE A (delta\' = 1/44100 ; v9 = v8 certifie re-parametre au gel v6 ;\nv10 = v9 + levee de D-v9-1 : le synthetique du banc demarre sa phase 2 au pas de\ngrille INFERIEUR a la bascule ; pin sur le gel v7 = v6 + 5 hunks derives ou mesures ;\nconstruction_banc_v10_machine2_v2.py, machine 2)'),
    ('GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v6.md", "847bb3bb2dd19f87", 40158)',
     'GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v7.md", "%s", %d)' % (cg, tg)),
]
for a, b in REMPL:
    assert s.count(a) == 1, 'ancre non unique ou absente : %r' % a[:60]
    s = s.replace(a, b)
open(OUT, 'w', encoding='utf-8', newline='\n').write(s)
c = hashlib.sha256(unicodedata.normalize('NFC', s).encode()).hexdigest()[:16]
print('v10 ecrit : %s canon %s ; %d remplacements ; pin gel v7 %s %d o' % (os.path.basename(OUT), c, len(REMPL), cg, tg))
