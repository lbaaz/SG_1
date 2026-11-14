# -*- coding: ascii -*-
"""PILOTE de machine 2 pour le gel "LA CHAINE E-A PAR ETAT, HORS PLAGE" (9df2702af59adbbc). Un seul run, aucun argument.
Il ne decide rien : il verifie les canons (gel, sonde, feuille, moteur), lance la sonde aux douze points, puis la feuille, et consigne.
Pas de reprise : si la sonde s'arrete, le run se declare interrompu et se rejoue en entier (gel, section 12 ; note de machine 1, section 4).
Les variables de fils BLAS ne sont PAS fixees (comme le run de M17 et la nuit bis) ; la sonde les consigne dans son JSON.
Usage depuis BOCAL4 : python -P chaine_EA_par_etat/lancer_chaine_par_etat_machine2_v1.py"""
import hashlib
import os
import subprocess
import sys
import time
import unicodedata

RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAC)
D = 'chaine_EA_par_etat'
SORTIE = os.path.join(D, 'sortie')
os.makedirs(SORTIE, exist_ok=True)
CANONS = {os.path.join(D, 'gel_chaine_EA_par_etat_pre_enregistrement_v1.md'): '9df2702af59adbbc',
          os.path.join(D, 'sonde_chaine_par_etat_machine1_v1.py'): 'acf7e26dedfa8abc',
          os.path.join(D, 'lecture_chaine_par_etat_machine1_v1.py'): 'f94ab05f69e9bf2f',
          'm17_chaine_v17.py': '82a0be882568fe0c'}
J = open(os.path.join(SORTIE, 'console_chaine_par_etat.log'), 'a', newline='\n')


def dire(s):
    ligne = '%s %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), s)
    print(ligne, flush=True)
    J.write(ligne + '\n')
    J.flush()


def canon(p):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


dire('DEBUT DU PILOTE machine 2, gel 9df2702af59adbbc ; python %s ; cwd %s' % (sys.version.split()[0], RAC))
for p, att in CANONS.items():
    c = canon(p)
    dire('canon %-70s %s (attendu %s) %s' % (p, c, att, 'OK' if c == att else 'ECART'))
    if c != att:
        dire('ARRET : une piece n est pas au canon, rien n est joue')
        raise SystemExit(2)
if os.path.exists(os.path.join(SORTIE, 'sonde_chaine_par_etat.json')):
    dire('ARRET : une sortie existe deja ; un seul run (gel, section 12). Rien n est joue.')
    raise SystemExit(3)
t0 = time.time()
dire('LANCEMENT DE LA SONDE aux douze points')
with open(os.path.join(SORTIE, 'sonde_chaine_par_etat.log'), 'w', newline='\n') as f:
    rc = subprocess.run([sys.executable, '-P', os.path.join(D, 'sonde_chaine_par_etat_machine1_v1.py'), 'm17_chaine_v17.py',
                         os.path.join(SORTIE, 'sonde_chaine_par_etat.json')], stdout=f, stderr=subprocess.STDOUT).returncode
dire('FIN DE LA SONDE code=%d duree=%.0f s' % (rc, time.time() - t0))
if rc != 0:
    dire('SONDE INTERROMPUE : le run se declare interrompu, la feuille ne lit pas')
    raise SystemExit(4)
dire('LANCEMENT DE LA FEUILLE (selftest puis lecture)')
with open(os.path.join(SORTIE, 'lecture_chaine_par_etat.log'), 'w', newline='\n') as f:
    rc2 = subprocess.run([sys.executable, '-P', os.path.join(D, 'lecture_chaine_par_etat_machine1_v1.py'),
                          os.path.join(SORTIE, 'sonde_chaine_par_etat.json'), os.path.join(SORTIE, 'verdict_chaine_par_etat.json')],
                         stdout=f, stderr=subprocess.STDOUT).returncode
dire('FIN DE LA FEUILLE code=%d' % rc2)
dire('FIN DU PILOTE')
