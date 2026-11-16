# -*- coding: ascii -*-
"""DERIVE controle_clone_neuf_delta102_machine2_v1.py de DEPOT_delta101/controle_clone_neuf_delta101_machine2_v1.py (NON EDITE : regle 17). Machine 2, 16/11/2026. Changements, tous nommes :
  (1) le numero 101 -> 102 ; le manifeste de depot est MANIFEST_DEPOT_delta102_machine2_v2.txt, le journal du perimetre ..._sur_acte_v2_machine2.log ;
  (2) la piece de depot est l'acte de machine 1, version 2 : journal_delta_102_largeur_vide_v2.md, canon 16ba5e594ab18717 ; sa version 1 est a cote (journal_delta_102_largeur_vide_v1.md, canon 464ba00a6905e3a5), comme au delta 100 : un controle de plus ;
  (3) le total des fichiers suivis avant le depot est 2465 (apres le 101) ;
  (4) un controle de plus : les six pieces NON DEPOSEES, ASSUMEES (vie privee) ne sont PAS au registre.
Le controle des lots extraits (controle_lots_entrants_machine2_v2.py, derive de la v1) se rejoue a part sur le clone neuf. Chaque remplacement doit se faire EXACTEMENT une fois, sinon arret.
Usage (depuis BOCAL4) : py -3.11 -P DEPOT_delta102/derive_controle_clone_neuf_delta102.py"""
import difflib
import os

ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(os.path.dirname(ICI), 'DEPOT_delta101', 'controle_clone_neuf_delta101_machine2_v1.py'), encoding='ascii', newline='').read().replace('\r\n', '\n')


def une_fois(s, a, b, nom):
    if s.count(a) != 1:
        raise SystemExit('ARRET : %s : %d occurrence(s) de %r' % (nom, s.count(a), a[:90]))
    return s.replace(a, b)


s = src
s = une_fois(s, "acte = os.path.join(CL, 'journal', 'journal_delta_101_complement_lots_deposes_99_100_v1.md')", "acte = os.path.join(CL, 'journal', 'journal_delta_102_largeur_vide_v2.md')", 'nom de la piece de depot')
s = une_fois(s, "'c12268765a199f7d'", "'16ba5e594ab18717'", 'canon de la piece de depot')
s = une_fois(s, "for nom, src in (('MANIFEST_DEPOT_delta101_machine2_v1.txt'",
             "v1 = os.path.join(CL, 'journal', 'journal_delta_102_largeur_vide_v1.md')\n"
             "chk('la v1 de l acte est a cote, au canon 464ba00a6905e3a5', os.path.isfile(v1) and emp(open(v1, 'rb').read())[0] == '464ba00a6905e3a5', '')\n"
             "_excl = ['af1b49cfdf3bde0c', '6412b757b22b3736', '6399794d3aa15110', '5a73b5a492d5d4a2', 'fcfa1e8671b724d1', '3c2704eb97619d75']\n"
             "_reg = set()\nfor _f in suivis:\n    _reg.update(emp(open(os.path.join(CL, _f), 'rb').read()))\n"
             "chk('les six pieces exclues (vie privee) ne sont PAS au registre', not [c for c in _excl if c in _reg], '%d exclues, aucune au registre' % len(_excl))\n"
             "for nom, src in (('MANIFEST_DEPOT_delta101_machine2_v1.txt'", 'v1 a cote et exclusions')
assert s.count("2330 + N + 2") == 2, s.count("2330 + N + 2")
s = s.replace("2330 + N + 2", "2465 + N + 2")
s = s.replace('MANIFEST_DEPOT_delta101_machine2_v1.txt', 'MANIFEST_DEPOT_delta102_machine2_v2.txt')
s = s.replace('perimetre_depot_delta101_sur_acte_v1_machine2.log', 'perimetre_depot_delta102_sur_acte_v2_machine2.log')
s = s.replace('plafond 101', 'plafond 102').replace('plafond == 101', 'plafond == 102').replace('delta 101', 'delta 102').replace('delta101', 'delta102')
open(os.path.join(ICI, 'controle_clone_neuf_delta102_machine2_v1.py'), 'w', encoding='ascii', newline='\n').write(s)
d = ''.join(difflib.unified_diff(src.splitlines(True), s.splitlines(True), 'delta101', 'delta102'))
open(os.path.join(ICI, 'diff_controle_clone_neuf_101_102.txt'), 'w', encoding='ascii', newline='\n').write(d)
print('controle_clone_neuf_delta102_machine2_v1.py ecrit ; diff joint')
