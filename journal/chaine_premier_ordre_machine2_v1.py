# -*- coding: ascii -*-
"""Echelle de PREMIER ORDRE du vide au canal (a, b) de x^5/5 (convention de la note de machine 1 du 21/11 ; x_i = (a_i + a_i^dagger) / sqrt(2 w_i (w2^2 - 1)) ; desaccord -a + b w2 par barreau),
fermee par un absorbeur complexe lisse, largeur lue comme le POLE E* = Sigma(E*). Fonctions RECOPIEES de largeur_vide_premier_ordre_machine2_v1.py (non edite) et de verifie_reponse_21c_machine2_v1.py : aucun calcul au chargement.
Usage : import chaine_premier_ordre_machine2_v1 as C ; C.echelle(w2, a, b, M) ; C.largeur(tau, delta_sur_g, M, L, W) -> (Gamma/g, Re E/g) ; C.seuils(tau) ; C.rungs(tau, d)."""
import math

import numpy as np


def op(n, c):
    a = np.zeros((n, n))
    for k in range(1, n):
        a[k - 1, k] = math.sqrt(k)
    return c * (a + a.T)


def echelle(w2, a, b, M):
    D = w2 * w2 - 1.0
    c1, c2 = 1.0 / math.sqrt(2.0 * D), 1.0 / math.sqrt(2.0 * w2 * D)
    N = max(a, b) * (M + 2) + 16
    X1, X2 = op(N, c1), op(N, c2)
    ks = [k for k in range(0, 6) if k >= a and (k - a) % 2 == 0 and (5 - k) >= b and (5 - k - b) % 2 == 0]
    P1 = {k: np.linalg.matrix_power(X1, k) for k in ks}
    P2 = {5 - k: np.linalg.matrix_power(X2, 5 - k) for k in ks}
    out = []
    for m in range(M + 1):
        v = 0.0
        for k in ks:
            v += math.comb(5, k) * P1[k][a * m + a, a * m] * P2[5 - k][b * m + b, b * m]
        out.append(v / 5.0)
    return out


def sigma(E, tau, d, M, L, W):
    m0 = M - L
    G = 0.0 + 0.0j
    for m in range(M, 0, -1):
        cap = -1j * W * tau[m] * ((m - m0) / L) ** 2 if m > m0 else 0.0
        G = 1.0 / (E - m * d - cap - (tau[m] ** 2) * G)
    return tau[0] ** 2 * G


def largeur(tau, d, M=200, L=80, W=0.5):
    s0 = sigma(0.0 + 0.0j, tau, d, M, L, W)
    E = -1j * abs(s0.imag) + (s0.real if abs(s0.real) < abs(d) else 0.0)
    for _ in range(60):
        f = E - sigma(E, tau, d, M, L, W)
        h = 1e-7 * max(1.0, abs(E))
        fp = 1.0 - (sigma(E + h, tau, d, M, L, W) - sigma(E - h, tau, d, M, L, W)) / (2 * h)
        dE = f / fp
        E -= dE
        if abs(dE) < 1e-14 * max(1e-30, abs(E)):
            break
    return -2.0 * E.imag, E.real


def seuils(tau, n=12):
    """|delta|/g au-dela duquel le site m est dans la barriere : 2 tau_m / m."""
    return [2.0 * tau[m] / m for m in range(1, n + 1)]


def rungs(tau, d):
    """nombre de barreaux : sites m >= 1 dont le seuil est sous |delta|/g, comptes depuis m = 1 tant que consecutifs."""
    n = 0
    for s in seuils(tau, 40):
        if s < abs(d):
            n += 1
        else:
            break
    return n
