# -*- coding: ascii -*-
"""Compare deux JSON de sonde (memes points) etat par etat : etiquettes, Gamma_2D a k = 2, 3, 4, recouvrements de suivi, chaine.
Usage : python -P compare_essais_machine2_v1.py <a.json> <b.json> [etiquette_a] [etiquette_b]"""
import json, sys
A = json.load(open(sys.argv[1], encoding='ascii')); B = json.load(open(sys.argv[2], encoding='ascii'))
na = sys.argv[3] if len(sys.argv) > 3 else 'a'; nb = sys.argv[4] if len(sys.argv) > 4 else 'b'
print('plateformes : %s %s | %s %s' % (na, A['plateforme']['fils'], nb, B['plateforme']['fils']))
pb = {p['id']: p for p in B['points']}
tot = {'etiq': 0, 'n': 0}
pire_abs, pire_rel, pire_rel_haut = 0.0, 0.0, 0.0
pire_ch = 0.0
for pa in A['points']:
    p2 = pb.get(pa['id'])
    if p2 is None:
        continue
    print('== %s : g %.6e/%.6e r_c %d/%d N %d/%d graine (%.4f,%.4f)/(%.4f,%.4f)' % (pa['id'], pa['g'], p2['g'], pa['r_c'], p2['r_c'], pa['N'], p2['N'],
          pa['graine'][0], pa['graine'][1], p2['graine'][0], p2['graine'][1]))
    for ea, eb in zip(pa['etats'], p2['etats']):
        tot['n'] += 1
        if (ea['n1'], ea['n2']) != (eb['n1'], eb['n2']):
            tot['etiq'] += 1
            print('   rang %d : etiquettes differentes %s %s' % (ea['rang'], (ea['n1'], ea['n2']), (eb['n1'], eb['n2'])))
        for k in ('2', '3', '4'):
            x, y = ea['Gamma_2D'][k], eb['Gamma_2D'][k]
            d = abs(x - y); r = d / max(abs(x), 1e-300)
            pire_abs = max(pire_abs, d); pire_rel = max(pire_rel, r)
            if min(x, y) > 1e-10:
                pire_rel_haut = max(pire_rel_haut, r)
        ca, cb = ea['chaine'].get('gammas'), eb['chaine'].get('gammas')
        if ca and cb:
            pire_ch = max(pire_ch, max(abs(a - b) / a for a, b in zip(ca, cb)))
        if ea['Gamma_2D']['3'] < 3e-11 or abs(ea['Gamma_2D']['3'] / eb['Gamma_2D']['3'] - 1) > 3e-3:
            print('   rang %2d (%d,%d) G3 %.4e / %.4e  rel %.2e  abs %.2e ; G2 %.4e/%.4e ; G4 %.4e/%.4e' % (ea['rang'], ea['n1'], ea['n2'], ea['Gamma_2D']['3'], eb['Gamma_2D']['3'],
                  abs(ea['Gamma_2D']['3'] / eb['Gamma_2D']['3'] - 1), abs(ea['Gamma_2D']['3'] - eb['Gamma_2D']['3']), ea['Gamma_2D']['2'], eb['Gamma_2D']['2'],
                  ea['Gamma_2D']['4'], eb['Gamma_2D']['4']))
print('BILAN : %d etats, %d etiquettes differentes ; ecart absolu max de Gamma_2D (k = 2, 3, 4) %.2e ; relatif max %.2e ; relatif max au-dessus de 1e-10 %.2e ; chaine : ecart relatif max %.2e'
      % (tot['n'], tot['etiq'], pire_abs, pire_rel, pire_rel_haut, pire_ch))
