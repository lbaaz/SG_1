# -*- coding: ascii -*-
"""Triage du balayage E19 (2e passage, propre) : dans les dossiers de la CAMPAGNE 2D (DEPOT_delta94..101, certifications, runs, ordre2, lecteur creux, domaine G1, chaine EA, nuit EB),
HORS les dossiers de cette etape (qui portent des w2 candidats par construction ou dans leurs propres journaux), classe chaque jeton candidat a trois decimales :
mantisse d'un nombre en notation scientifique, ou valeur isolee ; liste les valeurs isolees avec leur ligne.
Usage : py -3.11 -I triage_E19_contexte_machine2_v1.py"""
import os
import re
from fractions import Fraction as F

R = r'd:\devs\bocal\BOCAL4'
cands = [F(n, 1000) for n in list(range(1981, 1990)) + list(range(1991, 2000)) + list(range(2001, 2010)) + list(range(2011, 2020))]
dec = ['%.3f' % float(c) for c in cands]
re_dec = re.compile(r'(?<![0-9.])(' + '|'.join(re.escape(d) for d in dec) + r')(?![0-9])')
sci = re.compile(r'(?<![0-9.])(' + '|'.join(re.escape(d) for d in dec) + r')[eE][-+]?\d+')
ECARTES = ('certif_gel_vide_partie1_machine2', 'rejeu_vide_machine2', 'livraison_16e_vide_etape_sans_run', 'livraison_16f_gel_vide_partie1')
EXT = ('.json', '.log', '.py', '.md', '.txt')
dossiers = [d for d in os.listdir(R) if d not in ECARTES and re.match(r'^(DEPOT_delta(9[4-9]|10[01])|run_|certif_|ordre2|nuit_EB|chaine_EA|domaine_G1|lecteur_creux)', d)]
tot_f = tot_h = tot_sci = 0
isoles = []
for d in sorted(dossiers):
    for dos, _, fs in os.walk(os.path.join(R, d)):
        for f in fs:
            if os.path.splitext(f)[1].lower() not in EXT:
                continue
            p = os.path.join(dos, f)
            try:
                t = open(p, 'rb').read().decode('utf-8', 'replace')
            except Exception:
                continue
            tot_f += 1
            for ligne in t.split('\n'):
                for m in re_dec.finditer(ligne):
                    tot_h += 1
                    if sci.match(ligne[m.start():]):
                        tot_sci += 1
                    else:
                        isoles.append((os.path.relpath(p, R), m.group(1), ligne.strip()[:200]))
print('dossiers de la campagne examines :', len(dossiers), '; fichiers texte :', tot_f, '; jetons :', tot_h, ', dont mantisses en notation scientifique :', tot_sci, '; isoles :', len(isoles))
cl = {'rapport/trajectoire/duree/pourcentage (autres)': 0}
w2_ligne = [x for x in isoles if re.search(r'w\s*_?2|omega', x[2], re.I)]
print('valeurs isolees dont la ligne parle de w2 ou omega :', len(w2_ligne))
for nom, j, l in w2_ligne:
    print('  [%s] %s :: %s' % (j, nom[:110], l))
fichiers = sorted(set(x[0] for x in isoles))
print('fichiers distincts portant une valeur isolee :', len(fichiers))
