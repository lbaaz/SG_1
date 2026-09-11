# DRIVER DE RE-DERIVATION DE L'ACTE R4/R5 (machine 1, 11/09/2026) : rejoue, dans l'ordre de l'acte, les feuilles de lecture
# de la sequence sur les pieces recues (chemins de la machine 1 ; machine 2 re-derive avec ses propres feuilles, comme au 88),
# et ecrit un log consolide. Chaque nombre de l'acte doit se retrouver ici.
import subprocess, sys, os
H = '/home/claude'; U = '/mnt/user-data/uploads'
P4J = f'{H}/P4/lot_machine2_2026-09-02_P4_run_v4/mesures_P4_jumeau_machine2_v1.json'
GELE2 = f'{H}/lots10/lot_machine2_2026-09-10_gel_volet_E_v2/gel_volet_E_flanc_machine2_v2.md'
etapes = [
 ("E, D, C, A -- lecture par enumeration du run R4", ['lecture_R4_machine1_v1.py', f'{H}/runR4', P4J, GELE2]),
 ("D -- t_exp bruts a 6400", ['rederive_D_6400_machine1_v1.py', f'{H}/cs/run_R4_voletD_machine2_v2.json', P4J]),
 ("R5 -- rho en fractions, p par enumeration", ['rederive_R5_machine1_v1.py', f'{H}/R5/lecture_R5_PD2_machine2_v1.json']),
 ("quadrature C -- seuil de capture 2:1 a 7|2.50", ['capture_2_1_p7_machine1_v1.py']),
 ("quadrature C -- enveloppes des sondes (loi 1/eps a cellule fixee)", ['enveloppes_apex_machine1_v1.py', f'{H}/runR4']),
 ("periode de libration 5|1.50 -- run", ['lecture_periode_libration_machine1_v1.py', f'{H}/runP/run_periode_libration_machine2_v1.json']),
 ("periode de libration 5|1.50 -- resolution a T = 4x", ['lecture_resolution_machine1_v1.py', f'{H}/corr/resolution_periodes_machine2_v1.json']),
 ("D2 -- premier ordre a 2:1, degre pair", ['D2_premier_ordre_2_1_pair_machine1_v1.py']),
 ("volet B -- lecture (P1, P2)", ['lecture_voletB_machine1_v1.py', f'{H}/vB/run_R4_voletB_machine2_v1.json', f'{H}/D2/D2_prediction_P_D1_5_machine1_v1.json']),
 ("volet B -- correction d'action (post hoc)", ['correction_action_P2_machine1_v1.py']),
 ("p = 8 -- prediction corrigee (a', b/a', bandes)", ['prediction_P2_p8_machine1_v1.py']),
 ("volet B -- K* a p = 6 (fait non predit)", ['-c', "s=1.0125856840741416; print(f'6|2.00 : s* = {s:.10f} ; K* = g s*^(p-2) = {0.05*s**4:.6f} ; p = 4 (4|2.00, s* = 2.63449) : K* = {0.05*2.63449**2:.3f}')"]),
 ("p = 8 -- lecture (corrigee vs naive)", ['lecture_P2_p8_machine1_v1.py', f'{H}/p8/run_P2_p8_machine2_v1.json', f'{H}/vB_rep/prediction_P2_p8_machine1_v1.json']),
 ("flanc -- table de parite et 31/31", ['direction_flanc_machine1_v1.py', f'{U}/lecture_parite_signe_machine2_v1.json']),
]
with open('rederive_acte_R4R5_machine1_v1.log', 'w') as L:
    for titre, cmd in etapes:
        L.write("=" * 96 + f"\n{titre}\n" + "=" * 96 + "\n")
        r = subprocess.run([sys.executable] + cmd, capture_output=True, text=True, cwd=os.getcwd())
        L.write(r.stdout + (("[stderr] " + r.stderr[-800:]) if r.returncode else "") + "\n")
        print(f"{'ok ' if r.returncode == 0 else 'ECHEC'} {titre}")
