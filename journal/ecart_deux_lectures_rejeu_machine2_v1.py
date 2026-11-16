# -*- coding: ascii -*-
"""OU SE LOGE L'ECART entre les deux lectures de la largeur (gamma_E = -2 Im E et gamma_W = 2 eta <W>) dans le rejeu (i) de machine 2.
HORS CHAINE. Lit rejeu_absorbeurs_longs_machine2_v1.json ; rien n'est recalcule. Ecrit APRES que le seuil R2 (1e-6 relatif, sans terme
absolu) a mordu sur 25 trajectoires sur 74 : ce script ne change pas R2, il dit d'ou vient la morsure.
Question posee : l'ecart |gamma_E - gamma_W| est-il borne en ABSOLU (precision de la valeur propre, ~ eps |E|), donc relatif surtout aux
barreaux ou gamma est tres petit ? On compte, par decade de gamma_W, le pire ecart absolu et le pire ecart relatif.
Usage : py -3.11 -P lecteur_creux_m2/ecart_deux_lectures_rejeu_machine2_v1.py <rejeu.json>"""
import json
import math
import sys

d = json.load(open(sys.argv[1]))
decades = {}
pire_abs = (0.0, None)
n_mord = 0
n_traj = 0
lignes = []
for r in d['resultats']:
    for c, x in r['configs'].items():
        n_traj += 1
        mord = False
        for ks, rec in x['lect'].items():
            if not rec.get('suivi'):
                continue
            gw, ge = rec['gamma_W'], rec['gamma_E']
            if gw <= 1e-12:
                continue
            da = abs(ge - gw)
            dr = da / gw
            dec = int(math.floor(math.log10(gw)))
            t = decades.setdefault(dec, [0, 0.0, 0.0])
            t[0] += 1
            t[1] = max(t[1], da)
            t[2] = max(t[2], dr)
            if da > pire_abs[0]:
                pire_abs = (da, (r['nom'], c, int(ks), gw))
            if dr > 1e-6:
                mord = True
                lignes.append((dr, r['nom'], c, int(ks), gw, da))
        n_mord += mord
print('trajectoires : %d ; dont au moins un barreau a plus de 1e-6 relatif : %d' % (n_traj, n_mord))
print('par decade de gamma_W : lectures, pire ecart ABSOLU, pire ecart RELATIF')
for dec in sorted(decades):
    t = decades[dec]
    print('  1e%+03d : %5d lectures   abs %.2e   rel %.2e' % (dec, t[0], t[1], t[2]))
print('pire ecart absolu : %.3e en %s' % (pire_abs[0], pire_abs[1]))
lignes.sort(reverse=True)
print('barreaux a plus de 1e-6 relatif : %d ; les plus forts :' % len(lignes))
for dr, nom, c, k, gw, da in lignes[:6]:
    print('   %.2e  %-8s %-7s k = %2d  gamma_W %.3e  abs %.2e' % (dr, nom, c, k, gw, da))
ks_mord = sorted(set(l[3] for l in lignes))
print('k concernes : %s ; gamma_W max parmi les barreaux mordants : %.3e' % (ks_mord, max(l[4] for l in lignes)))
