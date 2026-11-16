# -*- coding: ascii -*-
# Recompte INDEPENDANT, depuis les sorties de MON rejeu, des nombres-titres de la note (verdicts 4 et 6, sections 4 et 5).
import json, statistics as st
BASE = r'd:\devs\bocal\BOCAL4\rejeu_vide_machine2\sortie'
J = json.load(open(BASE + r'\controle_joues_absorbeur_v1.json'))['etats']
C = json.load(open(BASE + r'\carte_adaptee_v1.json'))
print('ETATS JOUES (domaine 98 et 100) :', len(J))
neg = sum(1 for e in J if e['ln_G3_etoile'] - e['ln_G3_depose'] < 0)
d = [e['ln_G3_etoile'] - e['ln_G3_depose'] for e in J]
print('  adapte < depose : %d sur %d ; mediane %+.4f ; de %+.4f a %+.4f   (note : 168/185 ; -0,0094 ; -0,023 a +0,005)' % (neg, len(J), st.median(d), min(d), max(d)))
qd = [abs(e['ln_G3_depose'] - e['ln_Gpl']) for e in J]; qa = [abs(e['ln_G3_etoile'] - e['ln_Gpl']) for e in J]
print('  |ln q3| : mediane depose %.4f adapte %.4f ; pire %.4f / %.4f   (note : 0,0192 / 0,0159 ; 0,0996 / 0,0902)' % (st.median(qd), st.median(qa), max(qd), max(qa)))
plus_pres = [(e['delta'] > 0, abs(e['ln_G3_etoile'] - e['ln_Gpl']) < abs(e['ln_G3_depose'] - e['ln_Gpl'])) for e in J]
pos = [x for x in plus_pres if x[0]]; ng = [x for x in plus_pres if not x[0]]
print('  adapte plus pres de la 2D : total %d ; delta>0 %d/%d ; delta<0 %d/%d   (note : 78 ; 71/81 ; 7/104)' % (
    sum(1 for x in plus_pres if x[1]), sum(1 for x in pos if x[1]), len(pos), sum(1 for x in ng if x[1]), len(ng)))
et = [e['etendue'] for e in J]; et.sort()
print('  etendue adaptee : mediane %.3f ; 9e decile %.3f ; max %.2f   (note : 0,021 ; 0,064 ; 0,33)' % (st.median(et), et[int(0.9 * len(et))], max(et)))
hors = sum(1 for e in J if abs(e['ln_G3_etoile'] - e['ln_Gpl']) > e['tolerance_E1']), sum(1 for e in J if abs(e['ln_G3_depose'] - e['ln_Gpl']) > e['tolerance_E1'])
print('  hors tolerance E1 : adapte %d, depose %d   (note : 0 et 0)' % hors)
bip = [(e['id'], e['rang'], abs(e['ln_G3_depose'] - e['ln_Gpl']), e['tolerance_E1']) for e in J if e['id'] == 'BP']
print('  BP : |ln q3| depose / tolerance E1 :', [('rang %d' % b[1], round(b[2], 5), b[3]) for b in bip])
print()
P = C['points']
calc = [p for p in P if not p.get('vide') or True]
print('CARTE ADAPTEE : comptes', C['comptes'])
keys = sorted(P[0].keys()); print('  cles d un point :', keys[:24])
