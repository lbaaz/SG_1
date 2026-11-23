# -*- coding: ascii -*-
"""VERIFICATION, par moi, du REJEU de machine 1 (22g, lot 423ec0fd24240977) de mes 96 diagonalisations du pole court.
Je ne lis pas son script : je lis ses 8 JSON de sortie (rejeu_m1/) comme des donnees et je les compare, cas par cas, a mes 8 JSON (pole_court_sorties/).
Cle d'un cas : (boite, g, a, m0). Grandeurs comparees : Gamma / g, Re E / g, poids au site (0, 0) (module). Rien d'autre.
Usage : py -3.11 -I verifie_rejeu_m1_pole_court_machine2_v1.py <dossier des JSON de m1 (rejeu_m1)> <dossier de mes JSON (pole_court_sorties)>"""
import glob
import json
import os
import sys

DM1, DM2 = sys.argv[1], sys.argv[2]
mes, siens = {}, {}
for f in sorted(glob.glob(os.path.join(DM2, 'pole_court_b*_g*.json'))):
    d = json.load(open(f, encoding='ascii'))
    for c in d['cas']:
        mes[(d['boite'], float(d['g']), c['a'], c['m0'])] = c
for f in sorted(glob.glob(os.path.join(DM1, 'rejeu_m1_b*_g*.json'))):
    d = json.load(open(f, encoding='ascii'))
    g = float(os.path.basename(f).split('_g')[1].replace('.json', ''))
    for c in d['cas']:
        siens[(d['boite'], g, c['a'], c['m0'])] = c
print('cas chez moi : %d ; cas chez elle : %d ; cles communes : %d' % (len(mes), len(siens), len(set(mes) & set(siens))))
ec = {'gamma_sur_g': 0.0, 're_sur_g': 0.0, 'poids_abs': 0.0}
pire = {}
for k in sorted(set(mes) & set(siens)):
    for q in ec:
        e = abs(mes[k][q] - siens[k][q])
        if e > ec[q]:
            ec[q], pire[q] = e, k
for q in ec:
    print('plus grand ecart sur %-12s : %.2e   (cas %s)' % (q, ec[q], pire.get(q)))
ok = len(mes) == 96 and len(siens) == 96 and len(set(mes) & set(siens)) == 96
print('96 cles communes : %s ; ecarts de elle a moi plus petits que 1e-9 : %s' % (ok, all(v < 1e-9 for v in ec.values())))
