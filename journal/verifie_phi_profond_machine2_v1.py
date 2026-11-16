# -*- coding: ascii -*-
"""MA VERIFICATION INDEPENDANTE de la reference du test 'procede du lecteur sur une barriere profonde' (note vide, section 2.2).
Question : ln Phi de la chaine de l'etat (0, 0) a 4, 8, 16, 32, 64, 128 barreaux, que m1 donne par fraction continue
(phi_fc, controlee contre phi_mp), est-il le meme par une AUTRE methode ? Methode : recurrence du DETERMINANT tridiagonal
D_n(E) = (E - h_n) D_{n-1}(E) - T_{n-1}^2 D_{n-2}(E), avec sa derivee, racine complexe la plus proche de 0 par Newton, en
precision arbitraire ; Phi = -2 Im E. Rien du code de phi_echelle n'est repris, SAUF le moteur (X_saut_reel, canon 82a0be88...)
qui donne les sauts, et le kappa lu dans la sortie de m1 (j'en reverifie le sens : ma propre regle de barriere doit rendre
m_bord = nombre de barreaux). Geometrie lue dans le TEXTE de la note : W_m = ef (m - cap)^2 pour m > cap, ef = 1/16,
b_M = max(8, m_bord), cap = m_bord + b_M // 2, chaine coupee a Mh = 4 (m_bord + b_M).
Usage : py -3.11 -P verifie_phi_profond_machine2_v1.py"""
import json
import math
import importlib.util
from fractions import Fraction as F
import mpmath as mp

BASE = r'd:\devs\bocal\BOCAL4'
spec = importlib.util.spec_from_file_location('moteur', BASE + r'\m17_chaine_v17.py')
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
assert M.P == 5 and tuple(M.CANAL) == (2, 1) and M.W1 == 1
J = json.load(open(BASE + r'\livraison_16e_vide_etape_sans_run\ext\lot_machine1_2026-11-16_vide_etape_sans_run_v1\procede_lecteur_profond_v1.json'))
EF = 0.0625
cache = {}


def tau(m):
    if m not in cache:
        cache[m] = M.X_saut_reel(M.P, 2, 1, float(2 * m), float(m), F(2)) / M.P
    return cache[m]


def m_bord_de(kappa):
    """Ma propre lecture de la regle de barriere : site m >= 1 dans la barriere si m > 2 kappa tau_m / tau_0 ;
    la barriere s'arrete apres trois sites consecutifs hors barriere (une fois commencee)."""
    t0 = tau(0)
    sites, neg = [], 0
    for m in range(1, 200000):
        if m > 2.0 * kappa * tau(m) / t0:
            sites.append(m)
            neg = 0
        elif sites:
            neg += 1
            if neg >= 3:
                break
        elif m > 8 and 2.0 * kappa * tau(m) / t0 > 4.0 * m:
            break
    return sites[-1]


def racine(kappa, mc):
    b_M = max(8, mc)
    Mh = 4 * (mc + b_M)
    cap = mc + b_M // 2
    t0 = tau(0)
    T = [kappa * tau(m) / t0 for m in range(Mh)]          # T[m] couple m et m+1
    ln10 = math.log(10.0)
    # profondeur grossiere attendue pour regler la precision : on la prend DANS la sortie de m1 (usage : seulement les chiffres)
    chiffres = int(abs(J_lnphi[mc]) / ln10) + 60
    mp.mp.dps = chiffres
    efm = mp.mpf(1) / 16
    T2 = [mp.mpf(t) ** 2 for t in T]
    h = [mp.mpc(m, -(efm * (m - cap) ** 2) if m > cap else 0) for m in range(Mh + 1)]

    def D(E):
        d0, d1 = mp.mpc(1), E - h[0]            # D_{-1} = 1 (convention), D_0 = E - h_0
        p0, p1 = mp.mpc(0), mp.mpc(1)           # derivees
        for n in range(1, Mh + 1):
            d2 = (E - h[n]) * d1 - T2[n - 1] * d0
            p2 = d1 + (E - h[n]) * p1 - T2[n - 1] * p0
            d0, d1, p0, p1 = d1, d2, p1, p2
        return d1, p1

    E = mp.mpc(0)
    for it in range(60):
        d, p = D(E)
        dE = -d / p
        if abs(dE) > mp.mpf('0.2'):
            dE = dE / abs(dE) * mp.mpf('0.2')
        E += dE
        if abs(dE) < mp.mpf(10) ** (-(chiffres - 10)):
            break
    # un pas de plus, par prudence (Im E se fixe apres Re E)
    d, p = D(E)
    E -= d / p
    return E, it + 1, chiffres, Mh


J_lnphi = {p['m_cible']: p['ln_Phi_fc'] for p in J['points']}
print(' barreaux  m_bord(ma regle)  sites   ln Phi (mon determinant)      ln Phi (m1, fc)         ln Phi (m1, lecteur)      mon - fc     mon - lecteur   Re E       iterations  chiffres')
pire_fc, pire_lec, ok_mbord = 0.0, 0.0, True
for p in J['points']:
    mc, k = p['m_cible'], p['kappa']
    mb = m_bord_de(k)
    if mb != mc:
        ok_mbord = False
    E, it, chiffres, Mh = racine(k, mc)
    assert Mh + 1 == p['sites'], (Mh + 1, p['sites'])
    lnphi = float(mp.log(-2 * E.imag))
    d_fc = lnphi - p['ln_Phi_fc']
    d_lec = lnphi - p['ln_Phi_lecteur']
    pire_fc = max(pire_fc, abs(d_fc))
    pire_lec = max(pire_lec, abs(d_lec))
    print('  %4d        %4d          %5d   %+20.10f   %+20.10f   %+20.10f   %+.1e   %+.1e   %+.3e   %3d     %4d' % (
        mc, mb, p['sites'], lnphi, p['ln_Phi_fc'], p['ln_Phi_lecteur'], d_fc, d_lec, float(E.real), it, chiffres))
print('ma regle de barriere rend m_bord = nombre de barreaux aux 6 points :', ok_mbord)
print('plus grand |mon - fc| : %.2e ; plus grand |mon - lecteur| : %.2e ; plus petite largeur : exp(%.1f) = %.0f decades' % (
    pire_fc, pire_lec, min(J_lnphi.values()), -min(J_lnphi.values()) / math.log(10.0)))
