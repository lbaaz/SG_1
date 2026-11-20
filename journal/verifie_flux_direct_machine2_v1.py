# -*- coding: ascii -*-
"""Choix C1 de ma certification : dans les sorties de densite de machine 1 (qualification, SA3 a SA5, quatre absorbeurs, douze barreaux, douze ecarts), rho_flux et rho_direct s'accordent-elles ?
Rend le plus grand |ln(rho_flux / rho_direct)|. Machine 2, 2026-11-17. Usage : py -3.11 -P verifie_flux_direct_machine2_v1.py <dossier du lot de machine 1>"""
import glob
import json
import math
import os
import sys

pire, n = 0.0, 0
for f in sorted(glob.glob(os.path.join(sys.argv[1], 'densite_2d_SA*_v1.json'))):
    d = json.load(open(f))
    for k, v in d['k'].items():
        if v.get('suivi'):
            for a, b in zip(v['rho_flux'], v['rho_direct']):
                pire = max(pire, abs(math.log(a / b)))
                n += 1
print('%d valeurs de rho lues dans les sorties de densite de qualification ; plus grand |ln(rho_flux / rho_direct)| : %.2e' % (n, pire))
