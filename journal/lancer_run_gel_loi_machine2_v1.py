# -*- coding: ascii -*-
"""LANCEUR du run du gel "loi de la largeur, ordre 3, seconde partie" -- machine 2, 2026-11-16. UN SEUL RUN (gel, section 11). Il n'edite rien et ne mesure rien : il verifie que la machine est sur secteur,
interdit la mise en veille PENDANT le run (SetThreadExecutionState, qui cesse avec ce processus : aucun reglage de Windows n'est change), puis lance le pilote derive de machine 2 (pilote_gel_loi_machine2_v2.py)
sur la TABLE GELEE (35fa7b73f2b7f8eb), SANS --prevol, dans un dossier NEUF, avec 12 processus. Si le dossier du run existe deja, il s'arrete sans rien jouer (un pilote arrete par une panne se relance ENTIER dans un
dossier neuf, et l'acte le dit). Le journal du lanceur dit l'etat de la machine au depart et a la fin.
Usage : py -3.11 -P lancer_run_gel_loi_machine2_v1.py <dossier du run (neuf)>"""
import ctypes
import os
import platform
import subprocess
import sys
import time

RUN = os.path.abspath(sys.argv[1])
ICI = os.path.dirname(os.path.abspath(__file__))
BOCAL4 = os.path.dirname(ICI)
S = r'C:\Users\bazil\AppData\Local\Temp\claude\75adcc7f3c1d08bf\7d33635e-8345-4a2c-a69e-f6a51f9d8fa7\scratchpad\reg_neuf98'
L = os.path.join(BOCAL4, 'livraison_16a_gel_loi_partie2', 'ext', 'lot_m1')
J = os.path.join(S, 'journal')
ARGS = [os.path.join(ICI, 'pilote_gel_loi_machine2_v2.py'), L, os.path.join(S, 'scripts', 'm17_chaine_v17.py'), os.path.join(S, 'scripts', 'chaine_ordre2_bloc_machine1_v1.py'),
        os.path.join(L, 'ordre3_bloc_machine1_v1.py'), os.path.join(J, 'sonde_ordre2.json'), os.path.join(J, 'tp_retenus_machine2_v1.json'), os.path.join(J, 'tp_reference_machine2_v1.json'),
        os.path.join(BOCAL4, 'certif_EB_ter', 'lot_m1', 'reference_ancres_ter_machine1_v1.json'), os.path.join(L, 'table_points_gel_loi_ordre3_v1.json'), RUN, '12']
JOURNAL = os.path.join(ICI, 'lanceur_run_gel_loi_machine2_v1.log')


def dire(s):
    ligne = '%s %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), s)
    print(ligne, flush=True)
    open(JOURNAL, 'a', newline='\n').write(ligne + '\n')


class SPS(ctypes.Structure):
    _fields_ = [('ACLineStatus', ctypes.c_ubyte), ('BatteryFlag', ctypes.c_ubyte), ('BatteryLifePercent', ctypes.c_ubyte), ('SystemStatusFlag', ctypes.c_ubyte),
                ('BatteryLifeTime', ctypes.c_ulong), ('BatteryFullLifeTime', ctypes.c_ulong)]


def secteur():
    s = SPS()
    ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(s))
    return s.ACLineStatus, s.BatteryLifePercent


if os.path.exists(RUN):
    dire('ARRET : %s existe deja ; un seul run, dossier neuf (gel, section 11). Rien n est joue.' % RUN)
    raise SystemExit(3)
ac, pct = secteur()
dire('LANCEUR DU RUN : secteur %s (ACLineStatus %d), charge %d %% ; python %s ; %s ; %d coeurs logiques' % ('BRANCHE' if ac == 1 else 'ABSENT', ac, pct, sys.version.split()[0], platform.platform(), os.cpu_count()))
if ac != 1:
    dire('ARRET : la machine n est pas sur secteur ; rien n est joue.')
    raise SystemExit(4)
for p in ARGS[:10]:                       # le pilote, le dossier des scripts, le moteur, les blocs, le depot, les references, la table (pas le dossier du run ni le nombre de processus)
    if not os.path.exists(p):
        dire('ARRET : piece absente %s' % p)
        raise SystemExit(5)
ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
dire('mise en veille interdite pendant ce processus (SetThreadExecutionState) ; aucun reglage de Windows modifie')
dire('pilote : %s' % ' '.join(ARGS[:1]))
t0 = time.time()
code = subprocess.run([sys.executable, '-P'] + ARGS).returncode
dire('FIN DU PILOTE : code %d, duree %.0f s' % (code, time.time() - t0))
ac, pct = secteur()
dire('secteur a la fin : ACLineStatus %d, charge %d %%' % (ac, pct))
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
raise SystemExit(code)
