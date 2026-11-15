# --- CHAINE E-A AU SECOND ORDRE (bloc de machine 1, v1, 2026-11-14 ; insere tel quel dans la sonde) ---
# Hamiltonien effectif sur l'echelle resonante de l'etat (n1, n2), sites m : (n1 + CANAL[0] m, n2 + CANAL[1] m),
# a l'ordre g^2, forme symetrique, energies libres du moteur :
#   H_ab = E_a delta_ab + V_ab + (1/2) somme_q V_aq V_qb [ 1/(E_a - E_q) + 1/(E_b - E_q) ],  q hors echelle.
# La parite de x^P (P impair) ne laisse que le deplacement diagonal Sigma2(m) et le saut au second voisin u_m.
# Les sites m < 0 (jusqu'a epuisement de n1 ou de n2) sont gardes. Absorbeur, longueur et lecture de l'etat :
# ceux de gamma_chaine du moteur. Depend de M (le moteur), np et math, deja charges par la sonde.
SAUTS_HORS_ECHELLE = [(k, l) for k in range(-M.P, M.P + 1) for l in range(-M.P, M.P + 1)
                      if 0 < abs(k) + abs(l) <= M.P and (k + l) % 2 == M.P % 2
                      and (k, l) != (M.CANAL[0], M.CANAL[1]) and (k, l) != (-M.CANAL[0], -M.CANAL[1])]

def tables_ordre2(n1, n2, w2, g, sites, M_facteur=4):
    """Sauts t_m, deplacements Sigma2(m) et sauts au second voisin u_m, sites m_min..Mh."""
    w = float(w2); w1 = float(M.W1); c0, c1 = M.CANAL
    d = c1 * w - c0 * w1
    m2_bord = sites[-1][0]
    b_M = max(8, m2_bord)
    Mh = (m2_bord + b_M) * M_facteur
    m_min = -min(int(n1) // c0, int(n2) // c1)

    def V(k, l, a, b):
        if a < 0 or b < 0 or a + k < 0 or b + l < 0:
            return 0.0
        return (g / M.P) * M.X_saut_reel(M.P, k, l, float(a), float(b), w2)

    t, S, U = {}, {}, {}
    for m in range(m_min, Mh + 1):
        a, b = n1 + c0 * m, n2 + c1 * m
        t[m] = V(c0, c1, a, b); S[m] = 0.0; U[m] = 0.0
        for (k, l) in SAUTS_HORS_ECHELLE:
            v = V(k, l, a, b)
            if v == 0.0:
                continue
            ej = -w1 * k + w * l                    # energie libre de l'intermediaire, comptee du site m
            S[m] += v * v / (-ej)
            k2, l2 = 2 * c0 - k, 2 * c1 - l
            if abs(k2) + abs(l2) <= M.P and (k2, l2) != (c0, c1):
                U[m] += 0.5 * v * V(k2, l2, a + k, b + l) * (1.0 / (-ej) + 1.0 / (2.0 * d - ej))
    return {"d": d, "m2_bord": m2_bord, "b_M": b_M, "Mh": Mh, "m_min": m_min, "t": t, "S": S, "U": U}

def gamma_chaine_ordre2(tb, eta_facteur=1.0):
    """Largeur de l'etat de plus grand recouvrement avec le site 0, chaine d'ordre 2 complete.
    Rend Gamma_c2 = -2 Im E (la valeur lue), Gamma_flux = 2 <W> (meme quantite, autre arithmetique),
    dE = Re E + Sigma2(0) (decalage d'energie de l'etat, compte de l'energie libre du site 0)."""
    d, Mh, m_min = tb["d"], tb["Mh"], tb["m_min"]
    eta_c = abs(d) * eta_facteur
    debut_cap = tb["m2_bord"] + tb["b_M"] // 2
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + (tb["S"][m] - tb["S"][0])
        if m > debut_cap:
            Wd[i] = eta_c * (m - debut_cap) ** 2
            H[i, i] += -1j * Wd[i]
        if m < Mh:
            H[i, i + 1] = tb["t"][m]; H[i + 1, i] = tb["t"][m]
        if m + 2 <= Mh:
            H[i, i + 2] = tb["U"][m]; H[i + 2, i] = tb["U"][m]
    valeurs, vecteurs = np.linalg.eig(H)
    recs = np.abs(vecteurs[-m_min, :]) ** 2
    nu = np.lexsort((valeurs.real, -recs))[0]
    psi2 = np.abs(vecteurs[:, nu]) ** 2
    return {"Gamma_c2": float(-2.0 * valeurs[nu].imag), "Gamma_flux": float(2.0 * (Wd @ psi2) / psi2.sum()),
            "dE": float(valeurs[nu].real + tb["S"][0]), "recouvrement": float(recs[nu]), "M": Mh, "m_min": m_min}
# --- fin du bloc ---
