#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CONSTRUCTION DU BANC v12 = v11 (a9f3fa1d639107d2) + la levee de D-v11-1. machine 2, v1,
13/09/2026. Deux remplacements a ancre UNIQUE, asseres.

D-v11-1, MESUREE (mesure_jumelle_machine2_v1.py, 20/20) : au run REEL du volet A, la trajectoire
JUMELLE (G-dt) est jouee a pas moitie -- l'argument vaut dt2 / 2 -- mais l'appel n'arme pas
`jumelle=True`. Le facteur `fac` reste donc a 1, l'etage 2a garde le pas NOMINAL, et le compte de
l'etage 2b (mesure de 721 a 760, double par construction) est compare a l'intervalle du pas
nominal [360, 381] : les 18 trajectoires jumelles rendent G-fen, `exploitable` est faux aux trois
degres, et la cascade rend branche 3 -- AUCUN run ne pouvait conclure. Le gel v7 4.8 dit
pourtant, et c'est ce que l'instrument doit faire : "la trajectoire jumelle divise par 2 le pas
de CHAQUE etage (2a ET 2b sur-seuil) ... pour la jumelle, leurs DEUX bornes sont multipliees par
2". Les 18 comptes mesures tombent tous dans l'intervalle jumelle du gel, [720, 762] : la mesure
etait conforme, c'est la comparaison qui ne l'etait pas.
Le mecanisme existait deja (parametre `jumelle`, `fac = 2 if jumelle else 1`) ; il n'etait arme
nulle part. Le PRE-VOL ne pouvait pas l'attraper : son synthetique joue une seule phase et
declare les gardes de compte d'etage NON JOUEES. Seul un run reel le montre.

CORRECTIF : armer `jumelle=True` a l'appel de la jumelle DU RUN REEL. Rien d'autre ne bouge : le
banc synthetique ne joue pas les etages (le facteur y serait sans effet), le gel n'est pas touche
(c'est lui qui prescrit ce que l'instrument omettait), le pin reste le v7.

Usage : construction_banc_v12_machine2_v1.py <banc_v11.py> <sortie banc_v12.py>
"""
import hashlib, os, sys, unicodedata

SRC, OUT = sys.argv[1], sys.argv[2]
raw = open(SRC, 'rb').read()
assert hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16] == 'a9f3fa1d639107d2', 'le v11 au poste n est pas le v11 attendu'
s = raw.decode('utf-8')
REMPL = [
    ('                gdt[cle] = trajectoire_plan(w2, p, s, dt2 / 2, K_BASC, compteur, sortie, "p%d_w%.2f_c%.2f_dt2s2_k2" % (p, w2, c), synth, sgn=sg)\n',
     '                # v12 (D-v11-1) : la jumelle divise par 2 le pas de CHAQUE etage et ses intervalles de\n'
     '                # compte doublent (gel v7, 4.8). Sans jumelle=True le facteur reste a 1 : l etage 2a\n'
     '                # garde le pas nominal et le compte de 2b, double, est compare a [360, 381] -- les 18\n'
     '                # trajectoires rendaient G-fen et aucun run ne pouvait conclure.\n'
     '                gdt[cle] = trajectoire_plan(w2, p, s, dt2 / 2, K_BASC, compteur, sortie, "p%d_w%.2f_c%.2f_dt2s2_k2" % (p, w2, c), synth, sgn=sg, jumelle=True)\n'),
    ("DE LA CONSTANTE A (delta' = 1/44100 ; v11 = v10 certifie + levee de D-v10-1 : le",
     "DE LA CONSTANTE A (delta' = 1/44100 ; v12 = v11 + levee de D-v11-1 : la jumelle du\n"
     "run reel est jouee COMME une jumelle (jumelle=True), construction_banc_v12_machine2_v1.py ;\n"
     "v11 = v10 certifie + levee de D-v10-1 : le"),
]
for a, b in REMPL:
    assert s.count(a) == 1, 'ancre non unique ou absente : %r' % a[:70]
    s = s.replace(a, b)
s = s.replace('VERSION = "banc_qualification_machine1_v11"', 'VERSION = "banc_qualification_machine1_v12"')
# la garde compte les APPELS armes, pas les occurrences du texte : sa premiere version comptait
# aussi le mot dans le commentaire qu'elle venait d'inserer, et elle a mordu (bruyamment : rien
# n'a ete ecrit). Une garde se compare a ce qu'elle veut mesurer, pas a une sous-chaine nue.
assert 'banc_qualification_machine1_v12' in s and s.count('sgn=sg, jumelle=True)') == 1
open(OUT, 'w', encoding='utf-8', newline='\n').write(s)
c = hashlib.sha256(unicodedata.normalize('NFC', s).encode()).hexdigest()[:16]
print('v12 ecrit : %s canon %s ; %d remplacements + VERSION ; pin du gel INCHANGE (v7)'
      % (os.path.basename(OUT), c, len(REMPL)))
