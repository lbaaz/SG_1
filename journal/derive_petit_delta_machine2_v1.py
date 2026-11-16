# -*- coding: ascii -*-
"""Derive de faisabilite_profondeur_jumeau_machine2_v1.py (deja derive de celui de m1) DEUX scripts qui ne different que par w2 :
w2 = 3999/2000 (1.9995) et w2 = 4001/2000 (2.0005), |delta| = 0.0005, deux fois plus petit que le plus petit delta des cellules du gel (0.001) ;
ce ne sont PAS des candidats (quatre decimales). Reponse a M-6 de la note de m1 : le lecteur creux gene-t-il aux tres petits |delta| ? On ne lit que
le JUMEAU sans fantome (signe +1), comme la section 8 du gel. Remplacement 'exactement une fois'. Usage : py -3.11 -I derive_petit_delta_machine2_v1.py"""
import os
import difflib

D = r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie1_machine2'
src = open(os.path.join(D, 'faisabilite_profondeur_jumeau_machine2_v1.py'), 'rb').read().decode('ascii').replace('\r\n', '\n')
ancien = 'W2 = F(101, 50)\n'
if src.count(ancien) != 1:
    raise SystemExit('REFUS : W2 apparait %d fois' % src.count(ancien))
for nom, num, den in (('1_9995', 3999, 2000), ('2_0005', 4001, 2000)):
    t = src.replace(ancien, 'W2 = F(%d, %d)\n' % (num, den))
    if not all(ord(c) < 128 for c in t):
        raise SystemExit('REFUS : non ASCII')
    p = os.path.join(D, 'faisabilite_petit_delta_w2_%s_machine2_v1.py' % nom)
    open(p, 'w', newline='\n').write(t)
    d = ''.join(difflib.unified_diff(src.splitlines(True), t.splitlines(True), 'faisabilite_machine2_v1', 'petit_delta_%s' % nom))
    open(p[:-3] + '.diff', 'w', newline='\n').write(d)
    print('ecrit :', p, ';', d.count('\n'), 'lignes de diff')
