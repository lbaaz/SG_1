# -*- coding: ascii -*-
"""REJEU, sur ma machine, des scripts du lot HORS CHAINE de m1 'vide, etape sans run' (livraison 16e).
Aucun script de m1 n'est edite : on les LANCE tels quels (canon des entrees verifie avant). Les chaines sont a une
dimension ; le seul calcul 2D est le jumeau SANS fantome (temoin_lecteur_vide). Aucune largeur du systeme a fantome.
Chaque script ecrit sa sortie sous sortie/ et sa console sous sortie/<nom>.log. Sept processus en parallele, un fil BLAS chacun.
Usage : py -3.11 -I rejeu_vide_machine2_v1.py"""
import hashlib
import os
import subprocess
import sys
import time
import unicodedata

BASE = r'd:\devs\bocal\BOCAL4'
LOT = os.path.join(BASE, 'livraison_16e_vide_etape_sans_run', 'ext', 'lot_machine1_2026-11-16_vide_etape_sans_run_v1')
L16A = os.path.join(BASE, 'livraison_16a_gel_loi_partie2', 'ext', 'lot_m1')
MOTEUR = os.path.join(BASE, 'm17_chaine_v17.py')
BLOC2 = os.path.join(BASE, 'ordre2', 'chaine_ordre2_bloc_machine1_v1.py')
BLOC3 = os.path.join(L16A, 'ordre3_bloc_machine1_v1.py')
SONDE = os.path.join(L16A, 'sonde_lecteur_gel_loi_machine1_v1.py')
OUT = os.path.join(BASE, 'rejeu_vide_machine2', 'sortie')


def canon(p):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


def L(n):
    return os.path.join(LOT, n)


def O(n):
    return os.path.join(OUT, n)


ENTREES = [(MOTEUR, '82a0be882568fe0c'), (BLOC2, '7cd5977bc27bebc1'), (BLOC3, '534ba246aa3b8973'), (SONDE, 'd5cc48f48e37af99'),
           (L('phi_echelle_machine1_v1.py'), '8859a0c49b854d6f'), (L('carte_machine1_v1.py'), '6abf1d8b59bf41dc'),
           (L('absorbeur_adapte_machine1_v1.py'), 'f5dece5de40e95bd'), (L('forme_phi_v1.json'), '2e2ed5b9b745790c'),
           (L('carte_v1.json'), '406f13baa939eded'), (L('superposition_v1.json'), 'aeb9fc40ecc43899')]
for p, c in ENTREES:
    if canon(p) != c:
        raise SystemExit('REFUS : canon de %s != %s' % (p, c))
print('entrees aux canons attendus :', len(ENTREES))
os.makedirs(OUT, exist_ok=True)
PHI, CARTE, ADAPTE = L('phi_echelle_machine1_v1.py'), L('carte_machine1_v1.py'), L('absorbeur_adapte_machine1_v1.py')
BASE_ARGS = [MOTEUR, BLOC2, BLOC3, PHI, CARTE]
JOBS = [
    ('temoin_lecteur_vide', [L('temoin_lecteur_vide_machine1_v1.py'), MOTEUR, SONDE, O('temoin_lecteur_vide_v1.json')]),
    ('controle_joues_absorbeur', [L('controle_joues_absorbeur_machine1_v1.py')] + BASE_ARGS + [ADAPTE, L('superposition_v1.json'), O('controle_joues_absorbeur_v1.json')]),
    ('carte_adaptee', [L('carte_adaptee_machine1_v1.py')] + BASE_ARGS + [ADAPTE, L('carte_v1.json'), O('carte_adaptee_v1.json')]),
    ('absorbeur_adapte', [L('absorbeur_adapte_machine1_v1.py')] + BASE_ARGS + [L('forme_phi_v1.json'), O('absorbeur_adapte_v1.json')]),
    ('apres_barriere', [L('apres_barriere_machine1_v1.py')] + BASE_ARGS + [ADAPTE, L('carte_v1.json'), L('superposition_v1.json'), O('apres_barriere_v1.json')]),
    ('procede_lecteur_profond', [L('procede_lecteur_profond_machine1_v1.py'), MOTEUR, SONDE, PHI, CARTE, BLOC2, BLOC3, O('procede_lecteur_profond_v1.json')]),
    ('mandataire_absorbeur_2D', [L('mandataire_absorbeur_2D_machine1_v1.py')] + BASE_ARGS + [ADAPTE, O('mandataire_absorbeur_2D_v1.json')]),
]
env = dict(os.environ)
for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    env[k] = '1'
procs = []
t0 = time.time()
for nom, args in JOBS:
    f = open(O(nom + '.log'), 'wb')
    p = subprocess.Popen([sys.executable, '-P'] + args, stdout=f, stderr=subprocess.STDOUT, env=env, cwd=OUT)
    procs.append((nom, p, f, time.time()))
    print('lance :', nom, 'pid', p.pid, flush=True)
bad = 0
restants = list(procs)
while restants:
    time.sleep(2)
    for e in list(restants):
        nom, p, f, ts = e
        if p.poll() is not None:
            f.close()
            restants.remove(e)
            print('FINI : %-28s code %s en %.0f s' % (nom, p.returncode, time.time() - ts), flush=True)
            if p.returncode != 0:
                bad += 1
print('FIN DU REJEU : %d job(s) en echec, %.0f s en tout' % (bad, time.time() - t0))
