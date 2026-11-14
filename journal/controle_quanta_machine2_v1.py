# -*- coding: ascii -*-
"""controle_quanta_machine2_v1 : hors chaine, classe 3, machine 2. L'explication "E-A a l'occupation moyenne, E-B a l'etat modal"
(note 9322566db2546adb, 1.3) est-elle QUANTITATIVE ? Predit Gamma_c / Gamma_LS = r^(ntot_graine - ntot_lu) x q_lu, avec r = rapport de
la chaine entre (n1 + 1, n2) et (n1, n2) a l'etat lu, q_lu = chaine/2D de l'etat lu ; compare au rapport lu au run (table de
lire_m17_EA_EB_machine1_v1.py sur MON dossier manche_m17_v17, colonne Gc/GLS). Lit mes journaux de rejeu. Usage depuis BOCAL4 :
python -P chaine_EA_rejeu/controle_quanta_machine2_v1.py"""
import os
import re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUN = {'1.95': 28.43, '1.97': 47.03, '1.98': 62.04, '2.02': 220.12, '2.03': 312.45, '2.05': 29.28}
print('point  ntot_graine  etat_lu  ntot_lu  r_chaine  q_lu    prediction  rapport_du_run  prediction/run')
for p, w in (('39_20', '1.95'), ('197_100', '1.97'), ('99_50', '1.98'), ('101_50', '2.02'), ('203_100', '2.03'), ('41_20', '2.05')):
    t = open('chaine_EA_rejeu/point_%s.log' % p).read()
    nt = float(re.search(r'ntot_moyen=([0-9.]+)', t).group(1))
    rows = []
    for ln in t.splitlines():
        m = re.match(r'^\s*(\d+)\s+0\.\d+\s+(\d+)\s+(\d+)\s+(\d+)\s+[0-9.]+\s+([0-9.e+-]+)\s+([0-9.e+-]+)\s+[0-9.]+\s+([0-9.]+)', ln)
        if m:
            rows.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), float(m.group(5)), float(m.group(6)), float(m.group(7))))
    lu = rows[0]
    ch = {(r[1], r[2]): r[4] for r in rows}
    n1, n2 = lu[1], lu[2]
    r = ch[(n1 + 1, n2)] / ch[(n1, n2)]
    pred = r ** (nt - (n1 + n2)) * lu[5]
    print('%s   %.3f        (%d,%d)    %d        %.2f      %.3f   %9.1f   %9.2f       %.2f' % (
        w, nt, n1, n2, n1 + n2, r, lu[5], pred, RUN[w], pred / RUN[w]))
