# -*- coding: ascii -*-
"""PLATEAUX (gel bis 3.11) lus par la sonde dense deposee et par le lecteur creux de machine 2, sur les 34 trajectoires de la validation,
et temoin positif contre la reference du gel bis (5.1, ETAT AU 13/11). HORS CHAINE. Lit mon JSON de validation ; rien n'est recalcule.
Les deux references du temoin sont celles que le gel bis imprime (j = 6 : 5.3688e-10 ; j = 8 : 6.4279e-09, quatre decimales : la table
exacte est tp_reference_machine2_v1.json, non rouverte ici) : l'ecart a elle est donc a lire a 1e-4 pres.
Usage : python -P lecteur_creux_m2/plateaux_et_temoin_machine2_v1.py <validation.json>"""
import json
import math
import sys

REF = {'j06': 5.3688e-10, 'j08': 6.4279e-09}
d = json.load(open(sys.argv[1]))
n = n_verdict = n_k0 = n_gpl = 0
pire_gpl = 0.0
print('trajectoire                  dense : verdict  k0  etalement%   mien : verdict  k0  etalement%    Gamma_pl mien/dense - 1')
for r in d['resultats']:
    for cfg, c in r['configs'].items():
        m = c['cmp']
        pd, pw = m['plateau_dense'], m['plateau_W']
        n += 1
        v_d = 'PLATEAU' if (pd['fenetre'] and pd['plateau']) else 'non'
        v_w = 'PLATEAU' if (pw['fenetre'] and pw['plateau']) else 'non'
        n_verdict += v_d == v_w
        n_k0 += (pd['k0'] == pw['k0']) if (pd['fenetre'] and pw['fenetre']) else 0
        rap = pw['Gamma_pl'] / pd['Gamma_pl'] - 1.0 if (pd['fenetre'] and pw['fenetre']) else float('nan')
        if v_d == 'PLATEAU' and v_w == 'PLATEAU':
            n_gpl += 1
            pire_gpl = max(pire_gpl, abs(rap))
        print('%-8s %-8s            %-8s %3d  %8.3f         %-8s %3d  %8.3f          %+.2e'
              % (r['nom'], cfg, v_d, pd['k0'], 100 * pd['etalement'], v_w, pw['k0'], 100 * pw['etalement'], rap))
print('verdict (PLATEAU ou non) identique : %d sur %d ; meme depart k0 de la fenetre retenue : %d sur %d ; Gamma_pl : %d plateaux de part et d autre, ecart relatif max %.2e'
      % (n_verdict, n, n_k0, n, n_gpl, pire_gpl))
print('')
print('TEMOIN POSITIF (jumeau H+), Gamma_pl contre la reference du gel bis : |ln(Gamma_pl / Gamma_ref)|')
for r in d['resultats']:
    if r['genre'] == 'tp':
        c = list(r['configs'].values())[0]['cmp']
        j = r['nom'].split('_')[0]
        print('%-10s  mien %.5e  dense %.5e  ref %.4e   mien %.1e   dense %.1e'
              % (r['nom'], c['plateau_W']['Gamma_pl'], c['plateau_dense']['Gamma_pl'], REF[j], abs(math.log(c['plateau_W']['Gamma_pl'] / REF[j])),
                 abs(math.log(c['plateau_dense']['Gamma_pl'] / REF[j]))))
