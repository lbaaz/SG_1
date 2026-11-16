# -*- coding: ascii -*-
"""Emulation, sur la chaine d'ordre 2, de l'absorbeur de la lecture 2D (hors chaine, classe 3, post hoc).
Usage : python3 -I emulation_absorbeur_machine1_v1.py <moteur_v17.py> <sonde_etage2.json> <sortie.json>
Aucune diagonalisation 2D : la chaine seule, sur l'echelle (n1 + 2m, n2 + m) de l'etat lu, tronquee a la
boite de la lecture 2D (a, b < N) et munie du MEME absorbeur -i eta W(a, b) que la sonde de la nuit bis
(formes F1, F2, F3 ; geometries G20, G30, GT). Trois variantes :
  o1    : chaine du moteur (ordre 1), absorbeur sur l'echelle seule ;
  o2    : chaine d'ordre 2 du gel 41153158190cf7f1 (Sigma2, u), intermediaires libres, absorbeur sur l'echelle ;
  o2b   : idem, intermediaires restreints a la boite et portant leur absorbeur (energies complexes).
Lecture : etat de plus grand poids au site 0 ; Gamma = -2 <psi|A|psi> / <psi|psi>, A = (H - H^dag) / 2i."""
import sys, json, math, importlib.util
from fractions import Fraction as F
import numpy as np

MOTEUR, DONNEES, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR)
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
P = M.P; C0, C1 = M.CANAL; W1 = float(M.W1)
ETAT_LU = {"39_20": (7, 2), "197_100": (7, 2), "99_50": (7, 2), "101_50": (7, 2), "203_100": (7, 2), "41_20": (8, 2)}
SAUTS = [(k, l) for k in range(-P, P + 1) for l in range(-P, P + 1)
         if 0 < abs(k) + abs(l) <= P and (k + l) % 2 == P % 2 and (k, l) != (C0, C1) and (k, l) != (-C0, -C1)]

def W_forme(forme, a, b, r_c, L):
    if forme == "F1":
        r = max(a, b); return float((r - r_c) ** 2) if r > r_c else 0.0
    if forme == "F2":
        r = max(a, b); return float((r - r_c) ** 4) / float(L * L) if r > r_c else 0.0
    if forme == "F3":
        r = max(a, 2 * b); return float((r - r_c) ** 2) if r > r_c else 0.0
    raise ValueError(forme)

def chaine_en_boite(n1, n2, w2, g, N, r_c, forme, eta, variante):
    w = float(w2); d = C1 * w - C0 * W1; L = N - r_c
    m_min = -min(n1 // C0, n2 // C1)
    m_max = min((N - 1 - n1) // C0, (N - 1 - n2) // C1)
    dans = (lambda a, b: 0 <= a < N and 0 <= b < N) if variante == "o2b" else (lambda a, b: a >= 0 and b >= 0)
    def V(k, l, a, b):
        if a < 0 or b < 0 or a + k < 0 or b + l < 0:
            return 0.0
        return (g / P) * M.X_saut_reel(P, k, l, float(a), float(b), w2)
    def E(a, b):                                  # energie libre, avec l'absorbeur si la variante le porte
        e = -W1 * a + w * b
        if variante == "o2b":
            return e - 1j * eta * W_forme(forme, a, b, r_c, L)
        return e + 0j
    n = m_max - m_min + 1
    H = np.zeros((n, n), dtype=complex)
    e0 = -W1 * n1 + w * n2
    for m in range(m_min, m_max + 1):
        i = m - m_min; a, b = n1 + C0 * m, n2 + C1 * m
        H[i, i] = (-W1 * a + w * b - e0) - 1j * eta * W_forme(forme, a, b, r_c, L)
        if m < m_max:
            t = V(C0, C1, a, b); H[i, i + 1] += t; H[i + 1, i] += t
        if variante == "o1":
            continue
        Ea = E(a, b); S = 0j; U = 0j
        for (k, l) in SAUTS:
            aq, bq = a + k, b + l
            if not dans(aq, bq):
                continue
            v = V(k, l, a, b)
            if v == 0.0:
                continue
            Eq = E(aq, bq)
            S += v * v / (Ea - Eq)
            if m + 2 <= m_max:
                k2, l2 = 2 * C0 - k, 2 * C1 - l
                if abs(k2) + abs(l2) <= P and (k2, l2) != (C0, C1):
                    Ec = E(a + 2 * C0, b + 2 * C1)
                    U += 0.5 * v * V(k2, l2, aq, bq) * (1.0 / (Ea - Eq) + 1.0 / (Ec - Eq))
        H[i, i] += S
        if m + 2 <= m_max:
            H[i, i + 2] += U; H[i + 2, i] += U
    return H, m_min, m_max

def lire(H, m_min, S0=None):
    val, vec = np.linalg.eig(H)
    poids = np.abs(vec[-m_min, :]) ** 2 / np.sum(np.abs(vec) ** 2, axis=0)
    nu = np.lexsort((val.real, -poids))[0]
    psi = vec[:, nu]
    A = (H - H.conj().T) / 2j
    g_flux = float(-2.0 * np.real(np.vdot(psi, A @ psi)) / np.real(np.vdot(psi, psi)))
    return {"gamma_im": float(-2.0 * val[nu].imag), "gamma": g_flux, "E_re": float(val[nu].real), "poids0": float(poids[nu])}

# --- la chaine d'ordre 2 du gel, longue, a son propre absorbeur : la valeur "sans boite" ---
def chaine_longue(n1, n2, w2, g):
    sites = M.barriere(float(n1), float(n2), w2, g, True)
    w = float(w2); d = C1 * w - C0 * W1
    m_bord = sites[-1][0]; b_M = max(8, m_bord); Mh = (m_bord + b_M) * 4
    m_min = -min(n1 // C0, n2 // C1)
    def V(k, l, a, b):
        if a < 0 or b < 0 or a + k < 0 or b + l < 0:
            return 0.0
        return (g / P) * M.X_saut_reel(P, k, l, float(a), float(b), w2)
    out = {}
    for ef in (0.25, 0.0625):
        n = Mh - m_min + 1
        H = np.zeros((n, n), dtype=complex); S = {}; U = {}
        for m in range(m_min, Mh + 1):
            a, b = n1 + C0 * m, n2 + C1 * m; S[m] = 0.0; U[m] = 0.0
            for (k, l) in SAUTS:
                v = V(k, l, a, b)
                if v == 0.0:
                    continue
                ej = -W1 * k + w * l
                S[m] += v * v / (-ej)
                k2, l2 = 2 * C0 - k, 2 * C1 - l
                if abs(k2) + abs(l2) <= P and (k2, l2) != (C0, C1):
                    U[m] += 0.5 * v * V(k2, l2, a + k, b + l) * (1.0 / (-ej) + 1.0 / (2.0 * d - ej))
        debut = m_bord + b_M // 2
        for m in range(m_min, Mh + 1):
            i = m - m_min; a, b = n1 + C0 * m, n2 + C1 * m
            H[i, i] = m * d + (S[m] - S[0])
            if m > debut:
                H[i, i] += -1j * abs(d) * ef * (m - debut) ** 2
            if m < Mh:
                t = V(C0, C1, a, b); H[i, i + 1] = t; H[i + 1, i] = t
            if m + 2 <= Mh:
                H[i, i + 2] = U[m]; H[i + 2, i] = U[m]
        out[ef] = lire(H, m_min)["gamma"]
    return {"m_bord": m_bord, "Mh": Mh, "gamma_025": out[0.25], "gamma_00625": out[0.0625]}

def main():
    D = json.load(open(DONNEES))
    sortie = {"points": {}}
    for nom, p in D["points"].items():
        num, den = p["w2"].split("/"); w2 = F(int(num), int(den))
        g = float(M.g_du_point(w2)); n1, n2 = ETAT_LU[nom]
        long_ = chaine_longue(n1, n2, w2, g)
        pt = {"w2": p["w2"], "g": g, "etat": [n1, n2], "G_run": p["G_run"], "eta0": p["eta0"], "longue": long_, "cfg": {}}
        for cfg, c in p["cfg"].items():
            N, r_c, forme = c["N"], c["r_c"], c["forme"]
            lignes = {}
            for ks, tr in c["traj"].items():
                e0 = tr["etats"][0]
                lig = {"eta": tr["eta"], "g2D": e0["gamma"] if e0.get("suivi", True) else None}
                for var in ("o1", "o2", "o2b"):
                    H, m_min, m_max = chaine_en_boite(n1, n2, w2, g, N, r_c, forme, tr["eta"], var)
                    r = lire(H, m_min)
                    lig[var] = r["gamma"]; lig[var + "_im"] = r["gamma_im"]; lig[var + "_p0"] = r["poids0"]
                lig["m_max"] = m_max
                lignes[ks] = lig
            pt["cfg"][cfg] = {"N": N, "r_c": r_c, "forme": forme, "traj": lignes}
        sortie["points"][nom] = pt
    json.dump(sortie, open(SORTIE, "w"), indent=1, sort_keys=True)
    print("ecrit", SORTIE)

main()
