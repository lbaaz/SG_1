# -*- coding: ascii -*-
"""Rejeu machine 2 de bissection_chaine_2D_machine1_v2.py (7cb9dcf62eccf90b), hors chaine, classe 3 : les trois points de la
note (1.95, 2.02, 2.05), variantes par defaut (complet, resonant). Sortie : chaine_EA_rejeu/bissection_<num>_<den>.log."""
import os, subprocess, sys, time
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
J = open('chaine_EA_rejeu/journal_bissection.log', 'a', newline='\n')
for num, den in ((39, 20), (101, 50), (41, 20)):
    t0 = time.time(); J.write('%s DEBUT %d/%d\n' % (time.strftime('%H:%M:%S'), num, den)); J.flush()
    with open('chaine_EA_rejeu/bissection_%d_%d.log' % (num, den), 'w', newline='\n') as f:
        rc = subprocess.run([sys.executable, '-P', 'chaine_EA_rejeu/bissection_chaine_2D_machine1_v2.py', 'm17_chaine_v17.py',
                             str(num), str(den)], stdout=f, stderr=subprocess.STDOUT).returncode
    J.write('%s FIN %d/%d code=%d duree=%.0f s\n' % (time.strftime('%H:%M:%S'), num, den, rc, time.time() - t0)); J.flush()
J.write('%s FIN\n' % time.strftime('%H:%M:%S')); J.flush()
