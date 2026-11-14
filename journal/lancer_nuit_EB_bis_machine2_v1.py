# -*- coding: ascii -*-
"""PILOTE DE LA NUIT E-B BIS -- machine 2, 2026-11-13. Enchaine les quatre commandes du gel bis (note de machine 1,
section 4) SANS rien y changer : sonde v3 etage 1 -> feuille v2 etage 1 -> (si, et seulement si, le verdict de
l'etage 1 est TIENT) sonde v3 etage 2 -> feuille v2 etage 2. Il s'ARRETE au premier code de sortie non nul : un ARRET
(code 2 ou 3) se lit, il ne se contourne pas. Il ne decide d'aucun verdict : il lit celui que la feuille ecrit.
Il empeche la veille du poste tant qu'il tourne. Chaque etape ecrit sa console dans nuit_EB_bis/ ; le journal du pilote
est nuit_EB_bis/console_nuit.log (une ligne horodatee par evenement ; marqueurs : DEBUT, FIN ETAGE, VERDICT ETAGE 1,
ETAGE 2 NON LANCE, FIN DE LA NUIT, ARRET). Reprise apres coupure : relancer CE script sur le MEME dossier (les fichiers
deja calcules sont repris sous identite). Usage depuis BOCAL4 : python -P nuit_EB_bis/lancer_nuit_EB_bis_machine2_v1.py"""
import json
import os
import subprocess
import sys
import time

sys.dont_write_bytecode = True
RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAC)
N = 'nuit_EB_bis'
S = N + '/sortie'
SC = N + '/scripts'
SONDE = SC + '/sonde_qualification_EB_machine1_v3.py'
LECT = SC + '/lecture_qualification_EB_machine1_v2.py'
COMMUN = ['--moteur', 'm17_chaine_v17.py', '--run', 'manche_m17_v17', '--manifeste',
          'manche_m17_v17_MANIFEST_machine2.txt', '--sortie', S]
JOURNAL = open(N + '/console_nuit.log', 'a', encoding='ascii', newline='\n')


def log(s):
    JOURNAL.write('%s %s\n' % (time.strftime('%Y-%m-%d %H:%M:%S'), s))
    JOURNAL.flush()


def courir(nom, args):
    log('DEBUT %s' % nom)
    t0 = time.time()
    with open('%s/console_%s.log' % (N, nom), 'a', encoding='utf-8', errors='replace', newline='\n') as f:
        rc = subprocess.run([sys.executable, '-P'] + args, stdout=f, stderr=subprocess.STDOUT).returncode
    log('FIN %s code=%d duree=%.0f s' % (nom, rc, time.time() - t0))
    return rc


try:                                    # pas de veille tant que ce processus vit (ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
    import ctypes
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000001)
    log('veille empechee (SetThreadExecutionState)')
except Exception as e:                  # le poste est deja regle sur "jamais" sur secteur : on le consigne, on continue
    log('veille : SetThreadExecutionState indisponible (%s)' % type(e).__name__)
log('PILOTE DEMARRE : gel bis dcda1611adf5f8fd ; sonde v3 555146abd2192f79 ; feuille v2 c14dafffc5f84c97')

rc = courir('etage1', [SONDE] + COMMUN + ['--etage', '1', '--retenus', 'tp_retenus_machine2_v1.json'])
if rc != 0:
    log('ARRET : sonde etage 1, code %d (voir %s/console_etage1.log)' % (rc, N))
    sys.exit(rc)
rc = courir('lecture_etage1', [LECT, '--etage', '1', '--sortie', S, '--reference', 'tp_reference_machine2_v1.json'])
if rc != 0:
    log('ARRET : feuille etage 1, code %d (voir %s/console_lecture_etage1.log)' % (rc, N))
    sys.exit(rc)
v1 = json.load(open(S + '/verdict_etage1.json')).get('etage1')
log('VERDICT ETAGE 1 : %s' % v1)
if v1 != 'TIENT':
    log('ETAGE 2 NON LANCE : le verdict de l etage 1 n est pas TIENT (regle du gel, section 9)')
    sys.exit(0)
rc = courir('etage2', [SONDE] + COMMUN + ['--etage', '2', '--verdict1', S + '/verdict_etage1.json'])
if rc != 0:
    log('ARRET : sonde etage 2, code %d (voir %s/console_etage2.log)' % (rc, N))
    sys.exit(rc)
rc = courir('lecture_etage2', [LECT, '--etage', '2', '--sortie', S])
if rc != 0:
    log('ARRET : feuille etage 2, code %d (voir %s/console_lecture_etage2.log)' % (rc, N))
    sys.exit(rc)
try:
    v2 = json.load(open(S + '/verdict_qualification_EB.json')).get('verdict')
except Exception:
    v2 = None
log('VERDICT DE LA QUALIFICATION : %s' % v2)
log('FIN DE LA NUIT')
