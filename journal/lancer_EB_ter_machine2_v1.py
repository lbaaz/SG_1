# -*- coding: ascii -*-
"""PILOTE de machine 2 pour le gel "QUALIFICATION E-B TER" (432319b9feb34b82). Un seul run, aucun argument.
Derive de ordre2/lancer_ordre2_machine2_v1.py (le pilote du run precedent, NON EDITE : regle 17) : memes gestes, autres noms, plus de parallelisme.
Il ne decide rien. Il verifie les canons (gel, sonde, bloc, feuille, banc, reference des ancres, moteur, depot, retenus, tables du temoin), puis, dans l'ordre du gel
(section 12) : (1) la sonde en modes etage0, ancres et etage1 (trois processus) ; (2) la feuille, etape "instrument" ; (3) SI ET SEULEMENT SI elle rend TIENT, la sonde
en mode point aux DOUZE points (un processus par point, sans tirage, appels independants) ; (4) la feuille, etape "verdict". Il consigne chaque appel avec son heure et son
code de sortie, et l'etat de la machine. UNE SEULE EXECUTION : si le dossier de sortie existe, il s'arrete sans rien jouer. Un appel interrompu ne se rejoue pas
ici : le run se declare interrompu et l'appel se relance ENTIER, a la main, et l'acte le dit (gel, section 12).
Fils : un par processus (OPENBLAS, OMP, MKL = 1), comme au pre-vol et comme chez machine 1. Python : py -3.11 -P (BOCAL4 : le site utilisateur porte numpy et scipy).
Usage depuis BOCAL4 : py -3.11 -P certif_EB_ter/lancer_EB_ter_machine2_v1.py <clone registre>"""
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
import unicodedata

RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAC)
CLONE = os.path.abspath(sys.argv[1])
LOT = 'certif_EB_ter/lot_m1'
SORTIE = 'run_EB_ter'
JUGES = ['C1', 'C2', 'C3', 'C4', 'M1', 'M2', 'M3', 'M4', 'L1', 'L2', 'L3', 'L4']
J = os.path.join(CLONE, 'journal')
CANONS = {os.path.join(LOT, 'qualification_EB_ter_pre_enregistrement_v1.md'): '432319b9feb34b82',
          os.path.join(LOT, 'sonde_qualification_EB_ter_machine1_v1.py'): 'b5616dcf858e8801',
          os.path.join(LOT, 'lecteur_plateau_bloc_machine1_v1.py'): '9b0f95f3e10e9b0d',
          os.path.join(LOT, 'lecture_qualification_EB_ter_machine1_v1.py'): 'b2d6d7cfaf30f1cf',
          os.path.join(LOT, 'banc_feuille_ter_machine1_v1.py'): '6b63a9de25107ae4',
          os.path.join(LOT, 'reference_ancres_ter_machine1_v1.json'): '6600fb8418c79930',
          'm17_chaine_v17.py': '82a0be882568fe0c',
          os.path.join(J, 'sonde_ordre2.json'): '10887c60d5f55bcf',
          os.path.join(J, 'tp_retenus_machine2_v1.json'): '69b3bab3bb8480b7',
          os.path.join(J, 'tp_reference_machine2_v1.json'): '4d51dd58ef456fe9'}
SONDE = os.path.join(LOT, 'sonde_qualification_EB_ter_machine1_v1.py')
FEUILLE = os.path.join(LOT, 'lecture_qualification_EB_ter_machine1_v1.py')
ENV = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')


def canon(p):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


if os.path.exists(SORTIE):
    print('ARRET : %s existe deja ; un seul run (gel, section 12). Rien n est joue.' % SORTIE)
    raise SystemExit(3)
os.makedirs(SORTIE)
Jr = open(os.path.join(SORTIE, 'pilote_EB_ter.log'), 'a', newline='\n')


def dire(s):
    ligne = '%s %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), s)
    print(ligne, flush=True)
    Jr.write(ligne + '\n')
    Jr.flush()


def appel(mode, ids=()):
    nom = mode + ''.join('_' + i for i in ids)
    f = open(os.path.join(SORTIE, 'console_%s.log' % nom), 'w', newline='\n')
    cmd = [sys.executable, '-P', SONDE, 'm17_chaine_v17.py', os.path.join(J, 'sonde_ordre2.json'), os.path.join(J, 'tp_retenus_machine2_v1.json'), SORTIE, mode] + list(ids)
    return {'nom': nom, 'debut': time.time(), 'proc': subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT, env=ENV), 'f': f}


def attendre(appels):
    for a in appels:
        rc = a['proc'].wait()
        a['f'].close()
        a['rc'] = rc
        dire('FIN  %-14s code=%d duree=%.0f s' % (a['nom'], rc, time.time() - a['debut']))
    return all(a['rc'] == 0 for a in appels)


dire('DEBUT DU PILOTE machine 2, gel 432319b9feb34b82 ; python %s ; numpy/scipy lus par la sonde ; cwd %s' % (sys.version.split()[0], RAC))
dire('machine : %s %s, %s coeurs, %s' % (platform.system(), platform.version(), os.cpu_count(), platform.processor()))
try:
    bat = subprocess.run(['powershell', '-NoProfile', '-Command', '(Get-CimInstance Win32_Battery | Select-Object -ExpandProperty BatteryStatus) -join \',\''],
                         capture_output=True, text=True, timeout=30).stdout.strip()
    dire('batterie (BatteryStatus WMI, 2 = secteur, 1 = batterie, vide = pas de batterie) : %r' % bat)
except Exception as e:
    dire('batterie : non lue (%s)' % e)
for p, att in CANONS.items():
    c = canon(p)
    dire('canon %-76s %s (attendu %s) %s' % (p, c, att, 'OK' if c == att else 'ECART'))
    if c != att:
        dire('ARRET : une piece n est pas au canon, rien n est joue')
        raise SystemExit(2)
t_run = time.time()
dire('ETAPE 1 : la sonde en modes etage0, ancres, etage1 (trois processus)')
ok1 = attendre([appel('etage0'), appel('ancres'), appel('etage1')])
if not ok1:
    dire('RUN INTERROMPU a l etape 1 : un appel de l instrument a echoue ; il se relance entier, a la main, et l acte le dit')
    raise SystemExit(4)
dire('ETAPE 2 : la feuille, etape instrument')
with open(os.path.join(SORTIE, 'lecture_ter_instrument.console.log'), 'w', newline='\n') as f:
    rc = subprocess.run([sys.executable, '-I', FEUILLE, 'instrument', SORTIE, os.path.join(J, 'sonde_ordre2.json'), os.path.join(J, 'tp_reference_machine2_v1.json'),
                         os.path.join(LOT, 'reference_ancres_ter_machine1_v1.json')], stdout=f, stderr=subprocess.STDOUT, env=ENV).returncode
dire('FIN  feuille instrument code=%d' % rc)
vi = None
if rc == 0:
    vi = json.load(open(os.path.join(SORTIE, 'verdict_ter_instrument.json')))['instrument']
dire('VERDICT DE L INSTRUMENT : %s' % vi)
if vi != 'TIENT':
    dire('L INSTRUMENT NE TIENT PAS (ou la feuille a refuse) : l etage 2 n est PAS joue ; verdict NON CONCLUANT D INSTRUMENT')
    raise SystemExit(5)
dire('ETAPE 3 : la sonde en mode point aux douze points (un processus par point) ; ordre de lancement : les plus lourds d abord')
ordre = ['M3', 'L4', 'C1', 'M4', 'C2', 'C3', 'C4', 'M1', 'M2', 'L1', 'L2', 'L3']
assert sorted(ordre) == sorted(JUGES)
ok3 = attendre([appel('point', (i,)) for i in ordre])
if not ok3:
    dire('RUN INTERROMPU a l etape 3 : au moins un point a echoue ; l appel se relance ENTIER, a la main, et l acte le dit ; la feuille ne lit pas')
    raise SystemExit(6)
dire('ETAPE 4 : la feuille, etape verdict')
with open(os.path.join(SORTIE, 'lecture_ter.console.log'), 'w', newline='\n') as f:
    rc2 = subprocess.run([sys.executable, '-I', FEUILLE, 'verdict', SORTIE, os.path.join(J, 'sonde_ordre2.json')], stdout=f, stderr=subprocess.STDOUT, env=ENV).returncode
dire('FIN  feuille verdict code=%d' % rc2)
dire('DUREE TOTALE DU RUN : %.0f s' % (time.time() - t_run))
dire('FIN DU PILOTE')
