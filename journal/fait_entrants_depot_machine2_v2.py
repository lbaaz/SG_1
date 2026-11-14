# -*- coding: ascii -*-
"""EXTRAIT LES LOTS d'un depot (un dossier par lot, manifeste a cote de ses pieces) dans DEPOT_delta<nn>/entrants/, depuis les ZIP recus et emis a la racine
de BOCAL4. Un lot dont le zip ne porte pas son manifeste (lots de machine 1) recoit le manifeste pose a cote du zip, a la racine ; son canon est recalcule
et affiche. Rien n'est edite, les zips ne sont que lus. machine 2, v2 (v1 : deltas 95 et 96, non editee ; v2 = v1 + le delta 97), 14/11/2026.
Usage (depuis BOCAL4) : python -P fait_entrants_depot_machine2_v2.py 95 | 96 | 97"""
import hashlib
import os
import re
import shutil
import sys
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NN = sys.argv[1]
LOTS = {
    '95': ['lot_machine1_2026-11-13_gel_EB_bis_v1_recu', 'lot_machine1_2026-11-13_acte_qualification_EB_bis_v1_recu',
           'lot_machine1_2026-11-13_acte_qualification_EB_bis_v2_recu', 'lot_machine1_2026-11-13_chaine_EA_par_etat_v1_recu',
           'lot_machine1_2026-11-13_envoi_chaine_et_lectures_v1_recu', 'lot_machine2_2026-11-13_certification_gel_EB_bis_v1',
           'lot_machine2_2026-11-13_contreseing_acte_nn_EB_bis_v1', 'lot_machine2_2026-11-13_diagnostic_TP_echelle_forte_v1',
           'lot_machine2_2026-11-13_rejeu_chaine_EA_par_etat_v1', 'lot_machine2_2026-11-13_resultat_nuit_EB_bis_v1',
           'lot_machine2_2026-11-14_contreseing_acte_nn_EB_bis_v2_v1'],
    '96': ['lot_machine1_2026-11-13_reponse_rejeu_chaine_EA_v1_recu', 'lot_machine1_2026-11-14_gel_chaine_EA_par_etat_v1_recu',
           'lot_machine1_2026-11-14_acte_chaine_EA_par_etat_v1_recu', 'lot_machine2_2026-11-14_certification_gel_chaine_EA_par_etat_v1',
           'lot_machine2_2026-11-14_resultat_chaine_EA_par_etat_v1', 'lot_machine2_2026-11-14_contreseing_acte_chaine_EA_par_etat_v1'],
    '97': ['lot_machine1_2026-11-14_gel_domaine_G1_chaine_EA_v1_recu', 'lot_machine1_2026-11-14_acte_domaine_G1_chaine_EA_v1_recu',
           'lot_machine2_2026-11-14_certification_gel_domaine_G1_chaine_EA_v1', 'lot_machine2_2026-11-14_resultat_domaine_G1_chaine_EA_v1',
           'lot_machine2_2026-11-14_contreseing_acte_domaine_G1_chaine_EA_v1'],
}[NN]
OUT = os.path.join(ICI, 'DEPOT_delta%s' % NN, 'entrants')


def canon(raw):
    t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
    return hashlib.sha256(t).hexdigest()[:16]


os.makedirs(OUT, exist_ok=True)
for nom in LOTS:
    zp = os.path.join(ICI, nom + '.zip')
    d = os.path.join(OUT, nom)
    if os.path.exists(d):
        raise SystemExit('ARRET : %s existe deja' % d)
    z = zipfile.ZipFile(zp)
    z.extractall(d)
    mans = [n for n in z.namelist() if n.startswith('MANIFEST_') and '/' not in n]
    if not mans:
        base = re.sub(r'^lot_(machine\d)_\d{4}-\d\d-\d\d_', r'lot_\1_', nom).replace('_recu', '')
        src = os.path.join(ICI, 'MANIFEST_' + base + '.txt')
        if not os.path.isfile(src):
            raise SystemExit('ARRET : pas de manifeste pour %s (cherche %s)' % (nom, src))
        shutil.copyfile(src, os.path.join(d, os.path.basename(src)))
        mans = [os.path.basename(src)]
        prov = 'manifeste pose a cote du zip'
    else:
        prov = 'manifeste dans le zip'
    c = canon(open(os.path.join(d, mans[0]), 'rb').read())
    print('%-70s %2d membres  canon du lot %s  (%s)' % (nom, len(z.namelist()), c, prov))
