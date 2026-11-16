# -*- coding: ascii -*-
"""POINT (c) : la 'part' que m1 a ecrite dans sa note d'accompagnement de la v1 (0.023, 0.025, 0.024, 0.023 aux quatre MG lisibles). Dans mon contreseing de la v1 j'ai ecrit que c'etait des valeurs TRONQUEES de rho = |ln q / r3|
(0.0234, 0.0256, 0.0245, 0.0235). m1 repond (note de la v2, section 2) que ce sont deux grandeurs : rho et la part manquee f = rho / (1 + rho) (0.0229, 0.0250, 0.0239, 0.0230, arrondies a trois decimales).
Je refais f depuis MES donnees (ln q du run, mon r3) et je lis la ligne de definition dans le script de m1. Si m1 a raison, j'avais tort.
Usage : py -3.11 -I verifie_part_manquee_c_machine2_v1.py"""
import json
import os
import re

B = r'd:\devs\bocal\BOCAL4'
V = {c['id']: c for c in json.load(open(os.path.join(B, r'run_gel_vide_machine2\run_1\verdict_vide.json')))['cellules']}
P = {c['id']: c for c in json.load(open(os.path.join(B, r'certif_gel_vide_partie2_machine2\predictions_machine2_vide_v1.json')))['cellules']}
note_v1 = open(os.path.join(B, r'livraison_16j_acte_gel_vide\ext\lot_m1\lot_machine1_2026-11-16_acte_gel_vide_v1\POUR_MACHINE2_acte_gel_vide_machine1_v1.md'), encoding='utf-8').read()
note_v2 = open(os.path.join(B, r'livraison_16k_acte_gel_vide_v2\ext\lot_m1\lot_machine1_2026-11-16_acte_gel_vide_v2\POUR_MACHINE2_acte_gel_vide_machine1_v2.md'), encoding='utf-8').read()
script = open(os.path.join(B, r'livraison_16j_acte_gel_vide\ext\lot_m1\lot_machine1_2026-11-16_acte_gel_vide_v1\lecture_resultat_vide_machine1_v1.py'), encoding='utf-8').read()
ligne = [l for l in script.split('\n') if '"part":' in l][0].strip()
print('definition lue dans le script de m1 :', re.search(r'"part": \([^}]*', ligne).group(0)[:80])
print('note v1 de m1 (point c) :', re.search(r'part\s+manquee de ([0-9., et]+)\)', re.sub(r'\s+', ' ', note_v1)).group(1) if re.search(r'part\s+manquee de ([0-9., et]+)\)', re.sub(r'\s+', ' ', note_v1)) else '?')
print('note v2 de m1 (section 2) :', re.search(r'f = rho / \(1 \+ rho\) : ([0-9., et]+),', re.sub(r'\s+', ' ', note_v2)).group(1))
print()
ok = True
for i in ('MG3', 'MG4', 'MG5', 'MG6'):
    lq, r3 = V[i]['ln_q'], P[i]['r3']
    rho = abs(lq / r3)
    f = rho / (1 + rho)
    f_script = (-lq / r3) / (1.0 - lq / r3)
    print('%s : ln q %+.7f ; mon r3 %+.7f ; rho = %.5f ; f = rho/(1+rho) = %.5f -> %.3f (arrondi) ; formule du script de m1 : %.5f ; rho arrondi a 3 decimales %.3f ; rho tronque %.3f' % (
        i, lq, r3, rho, f, f, f_script, rho, int(rho * 1000) / 1000.0))
    ok = ok and abs(f - f_script) < 1e-12
print()
print('la formule de m1 (f = rho / (1 + rho)) redonne ses 0.0229 0.0250 0.0239 0.0230, soit 0.023 0.025 0.024 0.023 a trois decimales : %s' % ok)
print('=> la troncature de rho redonne les memes quatre nombres : mon hypothese "valeurs tronquees" etait arithmetiquement compatible, mais FAUSSE sur l origine : le script de m1 calcule f = rho / (1 + rho). m1 a raison sur la definition.')
