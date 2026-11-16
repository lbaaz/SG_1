# --- CHAINE D'ORDRE 3 SOUS ABSORBEUR ADAPTE AU SAUT (bloc de machine 1, v1, 2026-11-16 ; a certifier) ---
# Les tables et la matrice sont celles des blocs deposes (tables_ordre2, tables_ordre3 : decalage S, sauts t, U, T3,
# W3, W5). Deux choses changent, et elles seules : l'absorbeur et la longueur de la chaine.
#   debut = m_bord + c ; la chaine va du site m_min des tables au site debut + L ;
#   W_m = a |t_m| ((m - debut) / L)^2  pour  debut < m <= debut + L ,  0 ailleurs ;   H_mm porte  -i W_m .
# t_m est le saut du premier ordre entre les sites m et m + 1 (tb["t"][m]). Dix-huit variantes (a, c, L).
# LARGEUR d'une variante : -2 Im(E), E etant la valeur propre de la matrice dont le vecteur propre porte le plus
# grand poids sur le site 0 (a poids egal, la plus petite partie reelle). En double precision elle est lue par le
# flux, 2 <W> ; quand flux / |delta| <= 1e-15 la valeur propre est reprise en precision arbitraire (quotient de
# Rayleigh bilineaire, 100 chiffres) sur la MEME matrice, depuis le meme vecteur.
# PLATEAU : mediane des dix-huit logarithmes (moyenne des deux valeurs centrales) ; ETENDUE : max - min.
# Depend de M, np, math, mp (mpmath) et des blocs d'ordre 2 et d'ordre 3.
VARIANTES_ADAPTEES = [(a, c, L) for a in (1.0, 2.0, 4.0) for c in (6, 8, 10) for L in (16, 24)]
SEUIL_FLUX_ADAPTE = 1e-15
CHIFFRES_ADAPTE = 100

def matrice_adaptee(tb, t3, a, c, L, ordre=3):
    """Matrice de la chaine (ordre 2 ou 3) sous l'absorbeur adapte ; rend (H, W diagonal, indice du site 0)."""
    d, m_min = tb["d"], tb["m_min"]; debut = tb["m2_bord"] + c; Mh = debut + L
    if Mh > tb["Mh"]:
        raise RuntimeError("tables trop courtes : %d > %d" % (Mh, tb["Mh"]))
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + (tb["S"][m] - tb["S"][0])
        if m > debut:
            Wd[i] = a * abs(tb["t"][m]) * ((m - debut) / float(L)) ** 2
            H[i, i] += -1j * Wd[i]
        if m < Mh:
            x = tb["t"][m] + (t3["T3"][m] if ordre == 3 else 0.0)
            H[i, i + 1] = x; H[i + 1, i] = x
        if m + 2 <= Mh:
            H[i, i + 2] = tb["U"][m]; H[i + 2, i] = tb["U"][m]
        if ordre == 3 and m + 3 <= Mh:
            H[i, i + 3] = t3["W3"][m]; H[i + 3, i] = t3["W3"][m]
        if ordre == 3 and m + 5 <= Mh:
            H[i, i + 5] = t3["W5"][m]; H[i + 5, i] = t3["W5"][m]
    return H, Wd, -m_min

def _resoudre_bande(lignes, second, b):
    """Elimination de Gauss a pivot partiel sur une matrice bande (lignes : dictionnaires colonne -> valeur)."""
    n = len(lignes); Lg = [dict(r) for r in lignes]; x = list(second)
    for k in range(n):
        p = max(range(k, min(n, k + b + 1)), key=lambda i: abs(Lg[i].get(k, 0)))
        if p != k:
            Lg[k], Lg[p] = Lg[p], Lg[k]; x[k], x[p] = x[p], x[k]
        piv = Lg[k][k]
        for i in range(k + 1, min(n, k + b + 1)):
            f = Lg[i].get(k, 0)
            if f != 0:
                f = f / piv
                for col, v in Lg[k].items():
                    if col > k:
                        Lg[i][col] = Lg[i].get(col, 0) - f * v
                del Lg[i][k]; x[i] -= f * x[k]
    for k in range(n - 1, -1, -1):
        s = x[k]
        for col, v in Lg[k].items():
            if col > k:
                s -= v * x[col]
        x[k] = s / Lg[k][k]
    return x

def _valeur_propre_mp(H, psi0, b=5):
    """Valeur propre de H (symetrique complexe) depuis le vecteur psi0 : quotient de Rayleigh bilineaire, iteration inverse."""
    mp.mp.dps = CHIFFRES_ADAPTE
    n = H.shape[0]
    lignes = [{j: mp.mpc(H[i, j]) for j in range(max(0, i - b), min(n, i + b + 1)) if (H[i, j] != 0 or j == i)} for i in range(n)]
    psi = [mp.mpc(z) for z in psi0]
    def quotient(v):
        num = mp.mpc(0); den = mp.mpc(0)
        for i in range(n):
            s = mp.mpc(0)
            for j, x in lignes[i].items():
                s += x * v[j]
            num += v[i] * s; den += v[i] * v[i]
        return num / den
    mu = quotient(psi)
    for it in range(12):
        dec = [dict(r) for r in lignes]
        for i in range(n):
            dec[i][i] = dec[i][i] - mu
        y = _resoudre_bande(dec, psi, b)
        nrm = max(abs(z) for z in y)
        psi = [z / nrm for z in y]
        nouveau = quotient(psi)
        ecart = abs(nouveau - mu); mu = nouveau
        if ecart < mp.mpf(10) ** (-(CHIFFRES_ADAPTE - 12)):
            return mu, it + 1
    raise RuntimeError("_valeur_propre_mp : pas de convergence")

def largeur_adaptee(tb, t3, a, c, L, ordre=3):
    """Largeur de la chaine sous la variante (a, c, L) ; rend (Gamma, methode, poids du site 0)."""
    H, Wd, i0 = matrice_adaptee(tb, t3, a, c, L, ordre)
    val, vec = np.linalg.eig(H)
    poids = np.abs(vec[i0, :]) ** 2
    nu = np.lexsort((val.real, -poids))[0]
    psi2 = np.abs(vec[:, nu]) ** 2
    flux = float(2.0 * (Wd @ psi2) / psi2.sum())
    if flux / abs(tb["d"]) > SEUIL_FLUX_ADAPTE:
        return flux, "flux", float(poids[nu])
    mu, it = _valeur_propre_mp(H, vec[:, nu])
    return float(-2 * mu.imag), "mp%d" % it, float(poids[nu])

def plateau_adapte(tb, t3, ordre=3):
    """Plateau (mediane des logarithmes) et etendue (max - min) de la largeur aux dix-huit variantes."""
    v, methodes, poids = [], [], []
    for (a, c, L) in VARIANTES_ADAPTEES:
        G, meth, p = largeur_adaptee(tb, t3, a, c, L, ordre)
        v.append(math.log(G) if (G > 0.0 and math.isfinite(G)) else None); methodes.append(meth); poids.append(p)
    if any(x is None for x in v):
        return {"ln_G": None, "etendue": None, "valeurs": v, "methodes": methodes, "poids_min": min(poids)}
    s = sorted(v); n = len(s); mediane = 0.5 * (s[n // 2 - 1] + s[n // 2])
    return {"ln_G": mediane, "etendue": s[-1] - s[0], "valeurs": v, "methodes": methodes, "poids_min": min(poids)}
# --- fin du bloc ---
