# -*- coding: ascii -*-
"""G-4 / 4.4 : les ancres de la sonde dense DERIVEE, rejouees sur BOCAL4 (fils par defaut, comme le run), contre le depot du delta 98, avec la regle du gel (memes etiquettes, Gamma_2D(3) a 1e-3 relatif + 1e-12, energie a 1e-9),
appliquee par MA feuille (ancres_tiennent). Donne aussi les ecarts reels (pour voir la marge)."""
import json, sys, importlib.util
spec = importlib.util.spec_from_file_location('fi', 'feuille_independante_gel_loi_machine2_v1.py'); fi = importlib.util.module_from_spec(spec); spec.loader.exec_module(fi)
dense = json.load(open(sys.argv[1])); depot = json.load(open(sys.argv[2]))
table = {'points': [{'id': 'A1', 'role': 'ancre'}, {'id': 'A2', 'role': 'ancre'}]}
ok, motifs = fi.ancres_tiennent(table, dense, depot)
D = {p['id']: p for p in dense['points']}; R = {p['id']: p for p in depot['points']}
pire_rel = pire_abs = pire_e = 0.0; hors_plancher = 0
for i in ('A1', 'A2'):
    for u, v in zip(sorted(D[i]['etats'], key=lambda e: e['rang']), sorted(R[i]['etats'], key=lambda e: e['rang'])):
        a, b = u['Gamma_2D']['3'], v['Gamma_2D']['3']
        pire_abs = max(pire_abs, abs(a - b)); pire_e = max(pire_e, abs(u['E_re'] - v['E_re']))
        if b > 1.33e-12:
            pire_rel = max(pire_rel, abs(a / b - 1.0))
print('ancres de la sonde dense derivee contre le depot : %s ; motifs %s' % ('TIENNENT' if ok else 'NE TIENNENT PAS', motifs))
print('ecart relatif maximal de Gamma_2D(3) au-dessus de dix planchers %.2e (tolerance 1e-3) ; ecart absolu maximal %.2e (tolerance 1e-12 + relatif) ; ecart d energie maximal %.2e (tolerance 1e-9)' % (pire_rel, pire_abs, pire_e))
print('en-tete de la sortie : sonde %s, sonde_canon %s, table_canon %s, prevol %s, fils %s, duree C3/A1/A2 %s' % (dense.get('sonde'), dense.get('sonde_canon'), dense.get('table_canon'), dense.get('prevol'), dense.get('plateforme', {}).get('fils') if isinstance(dense.get('plateforme'), dict) else dense.get('plateforme'), [p.get('duree_s') for p in dense['points']]))
sys.exit(0 if ok else 1)
