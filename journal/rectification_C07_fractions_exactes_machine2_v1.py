# -*- coding: ascii -*-
"""RECTIFICATION de ma morsure C07 (contreseing e8ff4d600edf89ef) : recalcule en FRACTIONS EXACTES le plus grand ecart relatif des Gamma_pl et le plus grand ecart absolu des ecarts
logarithmiques entre MES deux verdicts JSON (run_EB_ter) et ceux que machine 1 a rejoues (lot de machine 1, lecture seule). Machine 1 contestait mon 7.216e-15 : abs(y/x - 1) en flottants.
Derive de scratch c07_fractions_exactes.py ; le verificateur scelle du lot e8ff4d600edf89ef n'est PAS edite (PB-1).
Usage depuis BOCAL4 : py -3.11 -I acte_EB_ter_contreseing/rectification_C07_fractions_exactes_machine2_v1.py"""
import json
import os
import zipfile
from fractions import Fraction as F

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.join(ROOT, 'run_EB_ter')
zl = zipfile.ZipFile(os.path.join(ROOT, 'lot_machine1_2026-11-15_acte_EB_ter_v1_recu.zip'))


def feuilles(a, b, chemin, out):
    if isinstance(a, dict):
        for k in a:
            feuilles(a[k], b[k], chemin + [k], out)
    elif isinstance(a, list):
        for n, (x, y) in enumerate(zip(a, b)):
            feuilles(x, y, chemin + [n], out)
    else:
        out.append((chemin, a, b))


paires = ((json.load(open(os.path.join(RUN, 'verdict_ter.json'), encoding='utf-8')), json.loads(zl.read('verdict_ter_rejoue_machine1.json'))),
          (json.load(open(os.path.join(RUN, 'verdict_ter_instrument.json'), encoding='utf-8')), json.loads(zl.read('verdict_ter_instrument_rejoue_machine1.json'))))
best = {'G_flt': (0.0, None), 'G_ex': (F(0), None), 'L_flt': (0.0, None), 'L_ex': (F(0), None)}
nd = 0
for A_, B_ in paires:
    out = []
    feuilles(A_, B_, [], out)
    for ch, a, b in out:
        if isinstance(a, float) and a != b:
            nd += 1
            cle = str(ch[-1])
            if cle == 'Gamma_pl':
                f = abs(a / b - 1.0)
                if f > best['G_flt'][0]:
                    best['G_flt'] = (f, (ch, a, b))
                r = abs(F(a) - F(b)) / min(abs(F(a)), abs(F(b)))
                if r > best['G_ex'][0]:
                    best['G_ex'] = (r, (ch, a, b))
            elif cle.startswith('ecart'):
                f = abs(a - b)
                if f > best['L_flt'][0]:
                    best['L_flt'] = (f, (ch, a, b))
                r = abs(F(a) - F(b))
                if r > best['L_ex'][0]:
                    best['L_ex'] = (r, (ch, a, b))
print('flottants differents : %d' % nd)
for k, (v, w) in best.items():
    print('%-6s %.6e  %s' % (k, float(v), w))
ch, a, b = best['G_flt'][1]
ex = abs(F(a) - F(b)) / min(abs(F(a)), abs(F(b)))
print('lecture du maximum en flottants (%s) : ecart relatif EXACT %.6e (la formule abs(a/b - 1) l arrondit a %.6e)' % (ch, float(ex), best['G_flt'][0]))
ch, a, b = best['G_ex'][1]
print('lecture du maximum EXACT (%s) : en flottants abs(a/b - 1) = %.6e, abs(b/a - 1) = %.6e' % (ch, abs(a / b - 1.0), abs(b / a - 1.0)))
print('65 * 2^-53 = %.6e' % (65 * 2.0 ** -53))
gx, lx = float(best['G_ex'][0]), float(best['L_ex'][0])
print('CONCLUSION : "7.2e-15 au plus" (relatif) %s ; "7.4e-15 au plus" (absolu) %s' % ('TIENT' if gx <= 7.2e-15 else 'MORD', 'TIENT' if lx <= 7.4e-15 else 'MORD'))
