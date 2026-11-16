# -*- coding: ascii -*-
"""Controle (information, le gel fige les decimales et pas la derivation) : les kappa_m de la section 2 sont-ils, a trois chiffres, le milieu
geometrique de l'intervalle de kappa ou la barriere de l'etat (0, 0), a la limite delta -> 0, finit au site m ? Regle de barriere LUE dans le moteur
(site m >= 1 dans la barriere si m > 2 kappa tau_m / tau_0 ; arret apres trois sites hors barriere), saut tau_m = X_saut_reel(P, 2, 1, 2m, m, w2 = 2)/P.
Les bornes sont trouvees par bissection sur kappa (en log). Plus : accord mp-flux de MA table, par profondeur (cellules ou les deux sont fiables).
Usage : py -3.11 -P controle_kappa_m_machine2_v1.py"""
import importlib.util
import json
import math
from fractions import Fraction as F

BASE = r'd:\devs\bocal\BOCAL4'
spec = importlib.util.spec_from_file_location('moteur', BASE + r'\m17_chaine_v17.py')
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
cache = {}


def tau(m):
    if m not in cache:
        cache[m] = M.X_saut_reel(M.P, 2, 1, float(2 * m), float(m), F(2)) / M.P
    return cache[m]


def m_bord(kappa):
    t0 = tau(0)
    sites, neg = [], 0
    for m in range(1, 5000):
        if m > 2.0 * kappa * tau(m) / t0:
            sites.append(m)
            neg = 0
        elif sites:
            neg += 1
            if neg >= 3:
                break
        elif m > 8 and 2.0 * kappa * tau(m) / t0 > 4.0 * m:
            break
    return sites[-1] if sites else 0


def bord_inf(m):
    """plus petit kappa de la bande ou m_bord == m : on part d'un kappa interieur et on descend."""
    lo, hi = 1e-6, None
    return None


KAPPA = {3: 0.0262, 4: 0.0200, 5: 0.0159, 6: 0.0130, 8: 0.00928, 12: 0.00558, 16: 0.00382}
print('  m   kappa du gel   m_bord(kappa gel)   bande de kappa ou m_bord = m : de ... a ...   milieu geometrique   ecart au kappa du gel')
for m, k in KAPPA.items():
    if m_bord(k) != m:
        print('  %2d   %.5f   m_bord = %d  (PAS m)' % (m, k, m_bord(k)))
        continue
    # bornes par bissection en log (m_bord est monotone decroissant en kappa sur cette plage : verifie par balayage)
    a, b = k * 0.5, k
    for _ in range(60):
        c = math.sqrt(a * b)
        if m_bord(c) == m:
            b = c
        else:
            a = c
    inf = b
    a, b = k, k * 2.0
    for _ in range(60):
        c = math.sqrt(a * b)
        if m_bord(c) == m:
            a = c
        else:
            b = c
    sup = a
    mil = math.sqrt(inf * sup)
    print('  %2d   %.5f        %d             de %.5f a %.5f                    %.5f             %+.2f %%' % (m, k, m_bord(k), inf, sup, mil, 100.0 * (mil / k - 1.0)))

D = json.load(open(BASE + r'\certif_gel_vide_partie1_machine2\detail_machine2_vide_v1.json'))
print()
print('accord de ln Gamma entre ma racine en precision arbitraire et le flux de la double precision (mon seuil mp : Gamma/|delta| < 1e-11), par profondeur :')
for m in (6, 8, 12, 16):
    v = [c['ecart_mp_flux_max'] for r in D.values() for c in r['cellules'] if c['m'] == m and c.get('ecart_mp_flux_max') is not None]
    print('  m = %2d : plus grand ecart %.2e  (mediane %.2e) sur %d cellules' % (m, max(v), sorted(v)[len(v) // 2], len(v)))
