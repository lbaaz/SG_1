# -*- coding: ascii -*-
"""Rejeu, par MA chaine d'ordre 3 (celle de ordre3_machine2_v1.py, dont le texte est repris sans etre edite), du tableau d'exemple de la section 4 de la note de machine 1 'la carte du gel de la loi' :
l'etiquette (6, 2) a delta = -0.06 (w2 = 1.94) et +0.04 (w2 = 2.04), aux facteurs 1, 6/5, 4/3, 3/2, 5/3 : couplage g = facteur x g_du_point(w2), largeur d'ordre 3 predite, e_bord (le desaccord au
dernier site de la barriere). 1D seulement : AUCUN calcul 2D. Les parametres de la chaine (ef, M_facteur) sont ceux du depot (bloc d'ordre 2 depose 7cd5977bc27bebc1, ef = 0.0625).
Usage : py -3.11 -P verif_exemple_carte_machine2_v1.py <moteur_v17.py> <bloc ordre 2> <ordre3_machine2_v1.py> <note carte de machine 1 (.md)> <sortie.json>"""
import importlib.machinery
import importlib.util
import json
import math
import os
import re
import sys
import tempfile
from fractions import Fraction as F
import numpy as np

MOTEUR, BLOC2, SCRIPT3, NOTE, SORTIE = sys.argv[1:6]
spec = importlib.util.spec_from_file_location('moteur', MOTEUR)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
ld = importlib.machinery.SourceFileLoader('bloc2', BLOC2)
B2 = importlib.util.module_from_spec(importlib.util.spec_from_loader('bloc2', ld))
B2.M, B2.np, B2.math = M, np, math
ld.exec_module(B2)
# la classe Chaine et chaine3, reprises telles quelles du script de mon controle (i), entre 'les sauts hors echelle' et 'def epreuve_boite'
src = open(SCRIPT3, encoding='ascii').read()
a, b = src.index('# les sauts hors echelle'), src.index('def epreuve_boite')
ent = ("import math\nimport numpy as np\nfrom fractions import Fraction as F\nP = M.P\nW1 = float(M.W1)\nC0, C1 = M.CANAL\n")
with tempfile.TemporaryDirectory() as td:
    chem = os.path.join(td, 'chaine_reprise.py')
    open(chem, 'w', encoding='ascii').write(ent + src[a:b])
    ld3 = importlib.machinery.SourceFileLoader('chaine_reprise', chem)
    C = importlib.util.module_from_spec(importlib.util.spec_from_loader('chaine_reprise', ld3))
    C.M = M
    ld3.exec_module(C)
EF = 0.0625
FACS = [F(1), F(6, 5), F(4, 3), F(3, 2), F(5, 3)]
note = open(NOTE, encoding='utf-8').read()
# les lignes du tableau d'exemple : | delta | facteur | g | largeur | e_bord |
att = []
for l in note.split('\n'):
    m = re.match(r'\| ([+-]0,\d\d) \| ([\d/]+) \| ([\d,]+e-\d+) \| ([\d,]+e-\d+)( d)? \| ([\d,]+) \|$', l)
    if m:
        att.append((F(m.group(1).replace(',', '.')), F(m.group(2)), float(m.group(3).replace(',', '.')), float(m.group(4).replace(',', '.')), float(m.group(6).replace(',', '.')), bool(m.group(5))))
print('lignes du tableau d exemple lues chez machine 1 : %d (attendu 10)' % len(att))
res = []
pire = {'g': 0.0, 'largeur': 0.0, 'e_bord': 0.0}
for (d, f, g_att, G_att, e_att, disc) in att:
    w2 = F(2) + d
    g = float(f) * M.g_du_point(w2)
    n1, n2 = 6.0, 2.0
    sites = M.barriere(n1, n2, w2, g, True)
    tb = B2.tables_ordre2(n1, n2, w2, g, sites, M_facteur=4)
    ch = C.Chaine(n1, n2, w2, g)
    r3 = C.chaine3(tb, ch, EF)
    r2 = B2.gamma_chaine_ordre2(tb, EF)
    e_bord = sites[-1][1]
    ecart = {'g': abs(g / g_att - 1.0), 'largeur': abs(r3['Gamma_flux'] / G_att - 1.0), 'e_bord': abs(e_bord - e_att)}
    for k in pire:
        pire[k] = max(pire[k], ecart[k])
    res.append({'delta': str(d), 'facteur': str(f), 'g': g, 'G3': r3['Gamma_flux'], 'G2': r2['Gamma_flux'], 'e_bord': e_bord, 'm_bord': tb['m2_bord'], 'ln_2_sur_3': math.log(r2['Gamma_flux'] / r3['Gamma_flux'])})
    print('  delta %+.2f x%-4s : g %.3e (note %.3e) ; largeur ordre 3 %.3e (note %.3e%s) ; e_bord %.2f (note %.2f) ; |ln(ordre 2 / ordre 3)| %.3f%s' % (
        float(d), f, g, g_att, r3['Gamma_flux'], G_att, ' d' if disc else '', e_bord, e_att, abs(res[-1]['ln_2_sur_3']), ' -> discriminant a 5 pour cent : %s (note : %s)' % (
            'oui' if abs(res[-1]['ln_2_sur_3']) >= 0.05 else 'non', 'oui' if disc else 'non')))
    res[-1]['discriminant_mien'] = abs(res[-1]['ln_2_sur_3']) >= 0.05
    res[-1]['discriminant_sien'] = disc
print('plus grands ecarts : couplage (relatif) %.2e ; largeur d ordre 3 (relatif) %.2e ; e_bord (absolu, deux decimales de la note) %.3f' % (pire['g'], pire['largeur'], pire['e_bord']))
ok_disc = all(r['discriminant_mien'] == r['discriminant_sien'] for r in res)
print('marque "d" (discriminant a 5 pour cent) : %s' % ('IDENTIQUE aux dix lignes' if ok_disc else 'DIFFERENTE'))
print('EXEMPLE DE LA CARTE : %s' % ('TIENT' if len(att) == 10 and pire['g'] < 5e-4 and pire['largeur'] < 1e-2 and pire['e_bord'] <= 0.0051 and ok_disc else 'NE TIENT PAS'))
json.dump({'lignes': res, 'pire': pire}, open(SORTIE, 'w'), indent=1)
