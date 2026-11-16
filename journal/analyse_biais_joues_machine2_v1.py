# -*- coding: ascii -*-
# Lecture seule : sortie JSON de m1 (controle_joues_absorbeur_v1.json). Residu chaine - 2D par signe de delta, par cellule.
import json, statistics as st
P = r'd:\devs\bocal\BOCAL4\livraison_16e_vide_etape_sans_run\ext\lot_machine1_2026-11-16_vide_etape_sans_run_v1\controle_joues_absorbeur_v1.json'
D = json.load(open(P))
E = D['etats']
print('etats', len(E), '; cles du premier :', sorted(E[0].keys()))
def q(e, k):
    return e[k] - e['ln_Gpl']
for sg, nom in ((-1, 'delta < 0'), (1, 'delta > 0')):
    S = [e for e in E if (e['delta'] < 0) == (sg < 0)]
    for k, lab in (('ln_G3_depose', 'deposee'), ('ln_G3_etoile', 'adaptee')):
        v = [q(e, k) for e in S]
        print('%-9s regle %-8s n=%3d  ln q3 : moy %+.4f  med %+.4f  min %+.4f  max %+.4f  |max| %.4f  ecart-type %.4f' % (nom, lab, len(S), st.mean(v), st.median(v), min(v), max(v), max(abs(x) for x in v), st.pstdev(v)))
print()
print('par cellule (source id) : n, delta, med ln q3 depose, med ln q3 adapte, max etendue, pire |ln q3| depose / adapte')
cel = {}
for e in E:
    cel.setdefault((e['source'], e['id']), []).append(e)
for key, S in sorted(cel.items(), key=lambda kv: kv[1][0]['delta']):
    qd = [q(e, 'ln_G3_depose') for e in S]; qa = [q(e, 'ln_G3_etoile') for e in S]
    print('%-9s %-3s n=%2d d=%+.4f  med q depose %+.4f  med q adapte %+.4f  etendue max %.3f  pire %.4f / %.4f' % (key[0], key[1], len(S), S[0]['delta'], st.median(qd), st.median(qa), max(e['etendue'] for e in S), max(abs(x) for x in qd), max(abs(x) for x in qa)))
print()
bp = [e for e in E if e['id'] == 'BP']
for e in bp:
    print('BP rang', e['rang'], 'delta', e['delta'], 'q depose %+.5f  q adapte %+.5f  etendue %.4f' % (q(e, 'ln_G3_depose'), q(e, 'ln_G3_etoile'), e['etendue']))
