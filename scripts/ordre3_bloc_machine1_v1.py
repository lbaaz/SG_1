# --- CHAINE E-A AU TROISIEME ORDRE (bloc de machine 1, v1, 2026-11-15 ; hors chaine, non certifie) ---
# Complete le bloc d'ordre 2 depose (chaine_ordre2_bloc_machine1_v1.py) par le terme d'ordre g^3 du hamiltonien
# effectif sur l'echelle, forme symetrique (Lowdin, Winkler eq. B.15c ; A = sites de l'echelle, B = le reste) :
#   H3_mm' = -(1/2) somme_{l dans B, m'' dans A} [ V_ml V_lm'' V_m''m' / ((E_m' - E_l)(E_m'' - E_l))
#                                                 + V_mm'' V_m''l V_lm' / ((E_m - E_l)(E_m'' - E_l)) ]
#            +(1/2) somme_{l, l' dans B} V_ml V_ll' V_l'm' [ 1/((E_m - E_l)(E_m - E_l')) + 1/((E_m' - E_l)(E_m' - E_l')) ]
# La parite de x^P (P impair) ne laisse a l'ordre 3 que des sauts a un nombre impair de barreaux : la correction T3_m
# du saut entre voisins (m, m+1), un saut au troisieme voisin W3_m (m, m+3) et un saut au cinquieme voisin W5_m
# (m, m+5 : trois pas de P quanta, tous hors echelle). Au-dela (m, m+7) il faudrait plus de 3 P quanta : rien.
# Energies libres du moteur. Depend de M, np, math et du bloc d'ordre 2.
PAS_IMPAIRS = [(k, l) for k in range(-M.P, M.P + 1) for l in range(-M.P, M.P + 1)
               if 0 < abs(k) + abs(l) <= M.P and (k + l) % 2 == M.P % 2]

def tables_ordre3(n1, n2, w2, g, tb):
    """T3[m] (correction du saut m -> m+1), W3[m] (saut m -> m+3) et W5[m] (saut m -> m+5), sur les sites de tb.
    Rend aussi le detail de T3 : part des chemins B-B, part des chemins passant par un site de l'echelle."""
    w = float(w2); w1 = float(M.W1); c0, c1 = M.CANAL; d = tb["d"]; m_min, Mh = tb["m_min"], tb["Mh"]

    def V(k, l, a, b):
        if a < 0 or b < 0 or a + k < 0 or b + l < 0 or abs(k) + abs(l) > M.P or (k == 0 and l == 0):
            return 0.0
        return (g / M.P) * M.X_saut_reel(M.P, k, l, float(a), float(b), w2)

    def e(k, l):                       # energie libre d'un deplacement (k, l), comptee du site de depart
        return -w1 * k + w * l

    def sur_echelle(k, l):             # le deplacement cumule (k, l) retombe-t-il sur l'echelle ?
        return k * c1 == l * c0 and k % c0 == 0

    def t_voisin(m):                   # saut du premier ordre entre m et m + 1 (0 si l'un des deux n'existe pas)
        if m < m_min:
            return 0.0
        return V(c0, c1, n1 + c0 * m, n2 + c1 * m)

    T3, W3, W5, T3_BB, T3_A = {}, {}, {}, {}, {}
    for m in range(m_min, Mh + 1):
        a, b = n1 + c0 * m, n2 + c1 * m
        for s, cible in ((1, T3), (3, W3), (5, W5)):
            bb = 0.0; pa = 0.0
            # chemins B-B : m -> l -> l' -> m + s, l et l' hors de l'echelle
            for (k1, l1) in PAS_IMPAIRS:
                if sur_echelle(k1, l1):
                    continue
                v1 = V(k1, l1, a, b)
                if v1 == 0.0:
                    continue
                e1 = e(k1, l1)
                for (k2, l2) in PAS_IMPAIRS:
                    K, L = k1 + k2, l1 + l2
                    if sur_echelle(K, L):
                        continue
                    k3, l3 = s * c0 - K, s * c1 - L
                    if abs(k3) + abs(l3) > M.P or (k3 + l3) % 2 != M.P % 2:
                        continue
                    v2 = V(k2, l2, a + k1, b + l1)
                    if v2 == 0.0:
                        continue
                    v3 = V(k3, l3, a + K, b + L)
                    if v3 == 0.0:
                        continue
                    e2 = e(K, L)
                    bb += 0.5 * v1 * v2 * v3 * (1.0 / ((-e1) * (-e2)) + 1.0 / ((s * d - e1) * (s * d - e2)))
            # chemins m -> l -> m'' -> m + s, m'' sur l'echelle, voisin de m + s
            for j in (0, 2, -2):
                if abs((m + j) - (m + s)) != 1 or m + j < m_min:
                    continue
                tv = t_voisin(min(m + j, m + s))
                if tv == 0.0:
                    continue
                for (k1, l1) in PAS_IMPAIRS:
                    if sur_echelle(k1, l1):
                        continue
                    v1 = V(k1, l1, a, b)
                    if v1 == 0.0:
                        continue
                    v2 = V(j * c0 - k1, j * c1 - l1, a + k1, b + l1)
                    if v2 == 0.0:
                        continue
                    e1 = e(k1, l1)
                    pa += -0.5 * v1 * v2 * tv / ((s * d - e1) * (j * d - e1))
            # chemins m -> m'' -> l -> m + s, m'' sur l'echelle, voisin de m
            for mm in (m + 1, m - 1):
                j = (m + s) - mm
                if j not in (0, 2, -2) or mm < m_min:
                    continue
                tv = t_voisin(min(m, mm))
                if tv == 0.0:
                    continue
                aa, bb2 = n1 + c0 * mm, n2 + c1 * mm
                for (k1, l1) in PAS_IMPAIRS:
                    if sur_echelle(k1, l1):
                        continue
                    v1 = V(k1, l1, aa, bb2)
                    if v1 == 0.0:
                        continue
                    v2 = V(j * c0 - k1, j * c1 - l1, aa + k1, bb2 + l1)
                    if v2 == 0.0:
                        continue
                    e1 = e(k1, l1)                         # compte du site mm
                    pa += -0.5 * tv * v1 * v2 / ((-(mm - m) * d - e1) * (-e1))
            cible[m] = bb + pa
            if s == 1:
                T3_BB[m] = bb; T3_A[m] = pa
    return {"T3": T3, "W3": W3, "W5": W5, "T3_BB": T3_BB, "T3_A": T3_A}

def gamma_chaine_ordre3(tb, t3, eta_facteur=1.0, avec_T3=True, avec_W3=True, avec_S=True, avec_U=True, recul=0, avec_W5=True):
    """Largeur de l'etat de plus grand recouvrement avec le site 0, chaine d'ordre 3 (ou une variante partielle).
    Memes absorbeur, longueur et lecture que gamma_chaine_ordre2. recul : sites ajoutes avant le debut de l'absorbeur."""
    d, Mh, m_min = tb["d"], tb["Mh"], tb["m_min"]
    eta_c = abs(d) * eta_facteur
    debut_cap = tb["m2_bord"] + tb["b_M"] // 2 + recul
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + ((tb["S"][m] - tb["S"][0]) if avec_S else 0.0)
        if m > debut_cap:
            Wd[i] = eta_c * (m - debut_cap) ** 2
            H[i, i] += -1j * Wd[i]
        if m < Mh:
            x = tb["t"][m] + (t3["T3"][m] if avec_T3 else 0.0)
            H[i, i + 1] = x; H[i + 1, i] = x
        if m + 2 <= Mh and avec_U:
            H[i, i + 2] = tb["U"][m]; H[i + 2, i] = tb["U"][m]
        if m + 3 <= Mh and avec_W3:
            H[i, i + 3] = t3["W3"][m]; H[i + 3, i] = t3["W3"][m]
        if m + 5 <= Mh and avec_W5:
            H[i, i + 5] = t3["W5"][m]; H[i + 5, i] = t3["W5"][m]
    valeurs, vecteurs = np.linalg.eig(H)
    recs = np.abs(vecteurs[-m_min, :]) ** 2
    nu = np.lexsort((valeurs.real, -recs))[0]
    psi2 = np.abs(vecteurs[:, nu]) ** 2
    return {"Gamma_im": float(-2.0 * valeurs[nu].imag), "Gamma_flux": float(2.0 * (Wd @ psi2) / psi2.sum()),
            "dE": float(valeurs[nu].real + (tb["S"][0] if avec_S else 0.0)), "recouvrement": float(recs[nu])}
# --- fin du bloc ---
