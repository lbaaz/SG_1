# -*- coding: ascii -*-
"""Essai de la partie FEUILLES du pilote du run (run_pont_machine2_v1.feuilles) sur les sorties de QUALIFICATION de machine 1 au point sacrifie (cellule SA3, douze barreaux, quatre absorbeurs, boites 180 a 189 et 300),
rangees sous les noms que le pilote attend. Machine 2, 2026-11-17. Aucune 2D nouvelle : on relit des fichiers. Le verdict n'est pas passe (il exige les six cellules du gel).
Usage : py -3.11 -P essai_feuilles_pilote_machine2_v1.py <registre> <lot de m1 a plat> <dossier neuf>"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_pont_machine2_v1 as R

reg, lot, out = sys.argv[1].rstrip('/\\'), sys.argv[2].rstrip('/\\'), sys.argv[3]
os.makedirs(os.path.join(out, 'journaux'))
for a in 'ABCD':
    shutil.copy(os.path.join(lot, 'densite_2d_SA3_%s_v1.json' % a), os.path.join(out, 'densite_2d_SA3_%s.json' % a))
shutil.copy(os.path.join(lot, 'boites_SA3_UN_v1.jsonl'), os.path.join(out, 'boites_SA3_UN1.jsonl'))
shutil.copy(os.path.join(lot, 'boite_SA3_300_v1.jsonl'), os.path.join(out, 'boites_SA3_DEUX1.jsonl'))
shutil.copy(os.path.join(lot, 'chaine_cellules_pont_v1.json'), os.path.join(out, 'chaine_cellules_pont_v1.json'))
jfile = os.path.join(out, 'essai_feuilles.log')
R.feuilles(reg, lot, out, R.ESSAI_CELLULES, jfile, False)
print('fichiers produits :', sorted(f for f in os.listdir(out) if f.startswith('lecture') or f == 'feuilles_machine2'))
print('fichiers de mes feuilles :', sorted(os.listdir(os.path.join(out, 'feuilles_machine2'))))
