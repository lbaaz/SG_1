# -*- coding: ascii -*-
"""Derive (regle 17 : la piece de m1 n'est pas editee) essai_refus_machine2_v1.py de essai_refus_machine1_v1.py : SEULE difference, le drapeau d'isolement des appels,
-I (qui cache numpy, installe au site utilisateur de BOCAL4 : la sonde echouerait a l'import AVANT son refus) devient -P. Remplacement exactement une fois ; diff ecrit a cote.
Usage : py -3.11 -I derive_essai_refus_machine2_v1.py"""
import difflib
import hashlib
import os
import unicodedata

SRC = r'd:\devs\bocal\BOCAL4\livraison_16h_gel_vide_partie2\ext\x_gel_vide_partie2\lot_machine1_2026-11-16_gel_vide_partie2_instrument_enonces_v1\essai_refus_machine1_v1.py'
DST = r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie2_machine2\essai_refus_machine2_v1.py'
raw = open(SRC, 'rb').read()
t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n')
c = hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]
print('canon de la piece de m1 :', c, '(attendu 7d18a4b4cb13316f)')
if c != '7d18a4b4cb13316f':
    raise SystemExit('REFUS : canon')
ancien = 'p = subprocess.run([sys.executable, "-I", "-B"] + args, capture_output=True, text=True)'
nouveau = 'p = subprocess.run([sys.executable, "-P", "-B"] + args, capture_output=True, text=True)'
if t.count(ancien) != 1:
    raise SystemExit('REFUS : %d occurrences' % t.count(ancien))
n = t.replace(ancien, nouveau)
if not all(ord(ch) < 128 for ch in n):
    raise SystemExit('REFUS : non ASCII')
d = ''.join(difflib.unified_diff(t.splitlines(True), n.splitlines(True), 'machine1_v1', 'machine2_v1'))
open(DST, 'w', newline='\n').write(n)
open(DST[:-3] + '.diff', 'w', newline='\n').write(d)
print('ecrit', DST, ';', d.count('\n'), 'lignes de diff')
