# -*- coding: ascii -*-
"""Emulation de l'absorbeur sur les etats des trois sondes deposees (deltas 96, 97, 98) : k = 2, 3, 4, forme F1.
Aucune diagonalisation 2D. Hors chaine, classe 3, post hoc. Ces donnees n'ont pas servi a ecrire l'emulation.
Usage : python3 -I emulation_hors_echantillon_machine1_v1.py <moteur_v17.py> <sortie.json> <sonde.json> [...]"""
import sys, json, math, time, importlib.util
from fractions import Fraction as F
import numpy as np
MOTEUR, SORTIE, SONDES = sys.argv[1], sys.argv[2], sys.argv[3:]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR)
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
P = M.P; C0, C1 = M.CANAL; W1 = float(M.W1)
SAUTS = [(k, l) for k in range(-P, P + 1) for l in range(-P, P + 1)
         if 0 < abs(k) + abs(l) <= P and (k + l) % 2 == P % 2 and (k, l) != (C0, C1) and (k, l) != (-C0, -C1)]

def Vg(g, w2, k, l, a, b):
    if a < 0 or b < 0 or a + k < 0 or b + l < 0:
        return 0.0
    return (g / P) * M.X_saut_reel(P, k, l, float(a), float(b), w2)

def lire(H, i0):
    val, vec = np.linalg.eig(H)
    poids = np.abs(vec[i0, :]) ** 2 / np.sum(np.abs(vec) ** 2, axis=0)
    nu = np.lexsort((val.real, -poids))[0]
    psi = vec[:, nu]
    A = (H - H.conj().T) / 2j
    return float(-2.0 * np.real(np.vdot(psi, A @ psi)) / np.real(np.vdot(psi, psi))), float(poids[nu])

def en_boite(n1, n2, w2, g, N, r_c, eta, variante):
    w = float(w2)
    m_min = -min(n1 // C0, n2 // C1); m_max = min((N - 1 - n1) // C0, (N - 1 - n2) // C1)
    Wf = lambda a, b: float((max(a, b) - r_c) ** 2) if max(a, b) > r_c else 0.0
    dans = (lambda a, b: 0 <= a < N and 0 <= b < N) if variante == "o2b" else (lambda a, b: a >= 0 and b >= 0)
    E = (lambda a, b: -W1 * a + w * b - 1j * eta * Wf(a, b)) if variante == "o2b" else (lambda a, b: -W1 * a + w * b + 0j)
    n = m_max - m_min + 1; H = np.zeros((n, n), dtype=complex); e0 = -W1 * n1 + w * n2
    for m in range(m_min, m_max + 1):
        i = m - m_min; a, b = n1 + C0 * m, n2 + C1 * m
        H[i, i] = (-W1 * a + w * b - e0) - 1j * eta * Wf(a, b)
        if m < m_max:
            t = Vg(g, w2, C0, C1, a, b); H[i, i + 1] += t; H[i + 1, i] += t
        Ea = E(a, b); S = 0j; U = 0j
        for (k, l) in SAUTS:
            aq, bq = a + k, b + l
            if not dans(aq, bq):
                continue
            v = Vg(g, w2, k, l, a, b)
            if v == 0.0:
                continue
            Eq = E(aq, bq); S += v * v / (Ea - Eq)
            if m + 2 <= m_max:
                k2, l2 = 2 * C0 - k, 2 * C1 - l
                if abs(k2) + abs(l2) <= P and (k2, l2) != (C0, C1):
                    U += 0.5 * v * Vg(g, w2, k2, l2, aq, bq) * (1.0 / (Ea - Eq) + 1.0 / (E(a + 2 * C0, b + 2 * C1) - Eq))
        H[i, i] += S
        if m + 2 <= m_max:
            H[i, i + 2] += U; H[i + 2, i] += U
    return lire(H, -m_min)

def sans_boite(n1, n2, w2, g, m_bord):
    """Chaine d'ordre 2 longue ; absorbeur lointain et faible : debut m_bord + 16, 256 sites au-dela, ef 1/16 et 1/64."""
    w = float(w2); d = C1 * w - C0 * W1
    m_min = -min(n1 // C0, n2 // C1); debut = m_bord + 16; Mh = debut + 256
    t, S, U = {}, {}, {}
    for m in range(m_min, Mh + 1):
        a, b = n1 + C0 * m, n2 + C1 * m
        t[m] = Vg(g, w2, C0, C1, a, b); S[m] = 0.0; U[m] = 0.0
        for (k, l) in SAUTS:
            v = Vg(g, w2, k, l, a, b)
            if v == 0.0:
                continue
            ej = -W1 * k + w * l; S[m] += v * v / (-ej)
            k2, l2 = 2 * C0 - k, 2 * C1 - l
            if abs(k2) + abs(l2) <= P and (k2, l2) != (C0, C1):
                U[m] += 0.5 * v * Vg(g, w2, k2, l2, a + k, b + l) * (1.0 / (-ej) + 1.0 / (2.0 * d - ej))
    out = []
    for ef in (1.0 / 16, 1.0 / 64):
        n = Mh - m_min + 1; H = np.zeros((n, n), dtype=complex)
        for m in range(m_min, Mh + 1):
            i = m - m_min
            H[i, i] = m * d + (S[m] - S[0])
            if m > debut:
                H[i, i] += -1j * abs(d) * ef * (m - debut) ** 2
            if m < Mh:
                H[i, i + 1] = t[m]; H[i + 1, i] = t[m]
            if m + 2 <= Mh:
                H[i, i + 2] = U[m]; H[i + 2, i] = U[m]
        out.append(lire(H, -m_min)[0])
    return out, {"t_rc": None}

def main():
    sortie = {"etats": []}; t0 = time.time()
    for chemin in SONDES:
        D = json.load(open(chemin)); nom_sonde = D.get("sonde")
        for p in D["points"]:
            if not p.get("faisable", True):
                continue
            num, den = p["w2"].split("/"); w2 = F(int(num), int(den)); g = p["g"]; N = p["N"]; r_c = p["r_c"]; eta0 = p["eta0"]
            for e in p["etats"]:
                G = e.get("Gamma_2D") or {}
                if "3" not in G or G["3"] is None or G["3"] <= 1.33e-12:
                    continue
                if not e.get("chaine", {}).get("definie"):
                    continue
                n1, n2 = int(e["n1"]), int(e["n2"])
                sites = M.barriere(float(n1), float(n2), w2, g, True)
                if not sites:
                    continue
                m_bord = sites[-1][0]
                try:
                    intr, _ = sans_boite(n1, n2, w2, g, m_bord)
                    emu = {}
                    for var in ("o2", "o2b"):
                        emu[var] = {str(k): en_boite(n1, n2, w2, g, N, r_c, eta0 * 2.0 ** (-k), var)[0] for k in (2, 3, 4)}
                except Exception as x:
                    print("ERREUR", p["id"], n1, n2, type(x).__name__, str(x)[:100]); continue
                m_rc = (r_c - n1) // C0 + 1                       # premier site de l'echelle dans l'absorbeur
                t_rc = Vg(g, w2, C0, C1, n1 + C0 * m_rc, n2 + C1 * m_rc)
                sortie["etats"].append({"sonde": nom_sonde, "id": p["id"], "role": p.get("role"), "w2": p["w2"], "facteur": p["facteur"],
                                        "g": g, "N": N, "r_c": r_c, "eta0": eta0, "n1": n1, "n2": n2, "rang": e.get("rang"),
                                        "J_ecart_type": e.get("J_ecart_type"), "poids_site": e.get("poids_site"),
                                        "m_bord": m_bord, "m_rc": m_rc, "t_rc": t_rc, "G2D": G, "intr": intr, "emu": emu,
                                        "chaine2_flux": (e.get("chaine2") or {}).get("gammas_flux")})
            print("%s %s : %d etats cumules, %.0f s" % (nom_sonde, p["id"], len(sortie["etats"]), time.time() - t0), flush=True)
    json.dump(sortie, open(SORTIE, "w"), indent=1, sort_keys=True)
    print("ecrit", SORTIE, len(sortie["etats"]))
main()
