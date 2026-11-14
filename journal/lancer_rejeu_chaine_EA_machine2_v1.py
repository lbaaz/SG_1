# -*- coding: ascii -*-
"""Rejeu machine 2 de comparaison_par_etat_machine1_v1.py (4eaef82543e4f76f), hors chaine, classe 3, demande par m1.
Un appel par point, sortie dans chaine_EA_rejeu/point_<num>_<den>.log ; aucun argument change. Usage depuis BOCAL4 :
python -P chaine_EA_rejeu/lancer_rejeu_chaine_EA_machine2_v1.py"""
import os, subprocess, sys, time
RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAC)
J = open('chaine_EA_rejeu/journal_rejeu.log', 'a', newline='\n')
for num, den in ((39, 20), (197, 100), (99, 50), (101, 50), (203, 100), (41, 20)):
    t0 = time.time()
    J.write('%s DEBUT %d/%d\n' % (time.strftime('%H:%M:%S'), num, den)); J.flush()
    with open('chaine_EA_rejeu/point_%d_%d.log' % (num, den), 'w', newline='\n') as f:
        rc = subprocess.run([sys.executable, '-P', 'chaine_EA_rejeu/comparaison_par_etat_machine1_v1.py',
                             'm17_chaine_v17.py', str(num), str(den)], stdout=f, stderr=subprocess.STDOUT).returncode
    J.write('%s FIN %d/%d code=%d duree=%.0f s\n' % (time.strftime('%H:%M:%S'), num, den, rc, time.time() - t0)); J.flush()
J.write('%s FIN DU REJEU\n' % time.strftime('%H:%M:%S')); J.flush()
