# -*- coding: ascii -*-
"""Section 7.2 du gel : 'la part manquee, (r - r de la chaine) / r, vaut 0.071 en mediane, et de 0.010 a 0.237 selon la cellule (mediane par cellule)' et 'a 184 de ces etats la chaine rend une correction trop petite'.
Recalcule depuis MES sorties (rejeu_vide_machine2/sortie/controle_joues_absorbeur_v1.json : ln(G3*/|delta|) sous l'absorbeur adapte et ln(Gamma_pl/|delta|)) et la superposition de la note d'echelle (ln Phi, domaine) :
r = ln Gamma_pl - ln|delta| - ln Phi ; r de la chaine = ln(G3*/|delta|) - ln Phi ; part manquee f = (r - r_chaine)/r = (ln Gamma_pl - ln(G3*/|delta|... )) / r.
Usage : py -3.11 -I part_manquee_joues_machine2_v1.py"""
import json
import statistics as st

B = r'd:\devs\bocal\BOCAL4'
J = json.load(open(B + r'\rejeu_vide_machine2\sortie\controle_joues_absorbeur_v1.json'))['etats']
S = json.load(open(B + r'\livraison_16e_vide_etape_sans_run\ext\lot_machine1_2026-11-16_vide_etape_sans_run_v1\superposition_v1.json'))['etats']
sup = {(e['source'], e['id'], e['rang']): e for e in S if e['domaine']}
print('etats du domaine :', len(J), '; dans la superposition :', len(sup))
f_tous, par_cellule, trop_petite, signe_r = [], {}, 0, {'r_oppose_a_delta': 0}
for e in J:
    s = sup[(e['source'], e['id'], e['rang'])]
    ln_phi = s['ln_Phi']
    r = e['ln_Gpl'] - ln_phi                 # ln(Gamma_pl / (|delta| Phi))
    r_ch = e['ln_G3_etoile'] - ln_phi        # ln(G3* / (|delta| Phi))
    f = (r - r_ch) / r
    f_tous.append(f)
    par_cellule.setdefault((e['source'], e['id']), []).append(f)
    if abs(r_ch) < abs(r) and r * r_ch > 0:
        trop_petite += 1
    if r * e['delta'] < 0:
        signe_r['r_oppose_a_delta'] += 1
print('part manquee f : mediane %.6f (gel : 0.0714629785415121)' % st.median(f_tous))
med_c = {k: st.median(v) for k, v in par_cellule.items()}
print('mediane par cellule : min %.6f (%s), max %.6f (%s)   (gel : 0.010002 a 0.237166)' % (
    min(med_c.values()), min(med_c, key=med_c.get)[1], max(med_c.values()), max(med_c, key=max(med_c, key=med_c.get) and med_c.get)[1], ))
print('cellules :', len(med_c))
print('etats ou la chaine rend une correction a la loi d echelle trop petite (|r_chaine| < |r|, meme signe) : %d sur %d  (gel : 184)' % (trop_petite, len(J)))
print('etats ou r a le signe oppose a delta : %d sur %d' % (signe_r['r_oppose_a_delta'], len(J)))
print('etats ou f < 0 ou f > 1 (la chaine corrige a l envers ou trop) :', sum(1 for f in f_tous if f < 0 or f > 1))
