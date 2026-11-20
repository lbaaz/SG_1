# -*- coding: ascii -*-
"""Prepare, pour rejouer SON releve de l'acte (releve_acte_pont_machine1_v1.py) sur MON poste, les deux listes de chemins qu'il lit (liste des pieces, liste des manifestes) : les siennes portent les chemins de son poste ;
les miennes portent des chemins RELATIFS a la racine de mon depot de travail (a lancer depuis cette racine). Je garde ses etiquettes de groupe et ses noms de fichier, dans son ordre. Machine 2, 2026-11-18.
Usage (depuis la racine) : py -3.11 -P prepare_releve_m1_chemins_machine2_v1.py <son liste_pieces_acte_v1.json> <son manifestes_v1.json> <dossier de sortie>"""
import json
import os
import sys

LISTE, MANIFS, SORTIE = sys.argv[1:4]
A, B, C = 'livraison_17a_gel_pont_partie1', 'livraison_17b_gel_pont_partie2', 'livraison_17c_rectificatif_gel_pont_partie2'
RUN, MA, LOTA = 'run_gel_pont_machine2_2026-11-18', 'run_gel_pont_machine2_2026-11-18/feuilles_machine2', 'livraison_18a_acte_gel_pont/ext/lot_m1'
CE = 'certif_gel_pont_partie2_machine2'
DOSS = {'premiere partie du gel': lambda n: SORTIE.rstrip('/') + '/' + n, 'seconde partie du gel': lambda n: B + '/' + n,
        "rectificatif d'avant run": lambda n: C + '/ext/lot_m1/' + n, 'instrument': lambda n: B + '/ext/lot_m1/' + n, 'note de machine 2': lambda n: n,
        'pilote de machine 2': lambda n: CE + '/' + n, 'lot de machine 2, run': lambda n: RUN + '/' + n, 'lot de machine 2, sa propre feuille': lambda n: MA + '/' + n,
        'ce lot, rejeu de machine 1': lambda n: LOTA + '/' + n}
liste = json.load(open(LISTE))
neuf = []
for chemin, groupe in liste:
    neuf.append([DOSS[groupe](os.path.basename(chemin)), groupe])
man = json.load(open(MANIFS))
cle = {'m1_p1': A + '/ext/MANIFEST_lot_machine1_gel_pont_partie1_regle_tirage_v1.txt', 'm1_p2': B + '/ext/MANIFEST_lot_machine1_gel_pont_partie2_instrument_enonces_v1.txt',
       'm1_rectificatif': C + '/ext/MANIFEST_lot_machine1_rectificatif_gel_pont_partie2_v1.txt', 'm2_certif_p1': 'MANIFEST_lot_machine2_certification_gel_pont_partie1_v1.txt',
       'm2_tirage': 'MANIFEST_lot_machine2_tirage_graine_456823_gel_pont_v1.txt', 'm2_certif_p2': 'MANIFEST_lot_machine2_certification_gel_pont_partie2_v1.txt',
       'm2_resultats': 'MANIFEST_lot_machine2_resultats_run_gel_pont_v1.txt'}
assert sorted(man) == sorted(cle), sorted(man)
os.makedirs(SORTIE, exist_ok=True)
# son releve compare le NOM du fichier a celui de nn.12 ; ma copie installee de la premiere partie s'appelle ..._recu.md : j'en pose une COPIE octet pour octet sous le nom attendu
import shutil
src1 = A + '/gel_pont_partie1_regle_tirage_pre_enregistrement_v1_recu.md'
dst1 = SORTIE.rstrip('/') + '/gel_pont_partie1_regle_tirage_pre_enregistrement_v1.md'
shutil.copyfile(src1, dst1)
assert open(src1, 'rb').read() == open(dst1, 'rb').read()
json.dump(neuf, open(os.path.join(SORTIE, 'liste_pieces_acte_machine2.json'), 'w', encoding='ascii', newline='\n'), indent=1)
json.dump(cle, open(os.path.join(SORTIE, 'manifestes_machine2.json'), 'w', encoding='ascii', newline='\n'), indent=1, sort_keys=True)
print('%d pieces, %d manifestes : chemins relatifs a la racine, ecrits dans %s' % (len(neuf), len(cle), os.path.basename(SORTIE.rstrip('/\\'))))
