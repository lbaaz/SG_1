# --- LECTEUR CREUX (bloc de machine 1, v1, 2026-11-15 ; insere tel quel dans la sonde) ---
# Le hamiltonien est celui de H_2D du moteur, element par element (X_saut_reel du moteur), assemble creux.
# UN etat par lecture : iteration inverse a decalage fixe (l'energie cible, reelle), factorisation creuse
# (scipy.sparse.linalg.splu, ordre MMD_ATA), depart au vecteur du barreau precedent ou au site de Fock de
# l'etiquette. Largeur : Gamma = 2 eta <x|W|x> / <x|x>, exacte pour un vecteur propre droit de H0 - i eta W
# quand H0 est hermitien ; -2 Im(lambda) est consignee a cote. Aucun tirage aleatoire. Si la factorisation
# se dit exactement singuliere, le decalage est repris une fois a 1e-12 pres ; un second echec rend "non suivi".
# Depend de M (le moteur), np, sp (scipy.sparse), sl (scipy.sparse.linalg) et math, charges par l'appelant.
ITER_MIN, ITER_MAX, TOL_RESIDU, POIDS_MIN = 2, 12, 1e-11, 0.5

def assembler(w2, g, Nmax, signe=-1):
    """H0 (partie hors diagonale, reelle symetrique, creuse) et diagonale libre, sur la boite Nmax x Nmax."""
    p = M.P; w = float(w2); W1 = float(M.W1)
    moitie = sorted((k, l) for k in range(-p, p + 1) for l in range(-p, p + 1)
                    if abs(k) + abs(l) <= p and (k + l) % 2 == p % 2 and (k, l) > (0, 0))
    I, J, V = [], [], []
    for a in range(Nmax):
        for b in range(Nmax):
            i = a * Nmax + b
            for (k, l) in moitie:
                a2, b2 = a + k, b + l
                if 0 <= a2 < Nmax and 0 <= b2 < Nmax:
                    v = (g / p) * M.X_saut_reel(p, k, l, float(a), float(b), w2)
                    if v:
                        j = a2 * Nmax + b2
                        I += [j, i]; J += [i, j]; V += [v, v]
    H0 = sp.csr_matrix((V, (I, J)), shape=(Nmax * Nmax, Nmax * Nmax), dtype=float)
    diag = np.array([signe * W1 * a + w * b for a in range(Nmax) for b in range(Nmax)])
    return H0, diag

def restreindre(H0max, diagmax, Nmax, N):
    sel = np.array([a * Nmax + b for a in range(N) for b in range(N)])
    return H0max[sel][:, sel].tocsc(), diagmax[sel]

def table_W(N, forme, r_c, L):
    """F1 : (r - r_c)^2 ; F2 : (r - r_c)^4 / L^2 ; r = max(a, b) ; nul si r <= r_c (gel bis, 3.4)."""
    W = np.zeros(N * N)
    for a in range(N):
        for b in range(N):
            x = max(a, b) - r_c
            if x > 0:
                W[a * N + b] = float(x * x) if forme == "F1" else float(x ** 4) / float(L * L)
    return W

def lire_etat(H0, diag, W, eta, N, site, E_cible, x0=None):
    A = (H0 + sp.diags(diag - 1j * eta * W)).tocsc().astype(complex)
    n = N * N; i0 = site[0] * N + site[1]
    lu, repris = None, False
    for E in (E_cible, E_cible + 1e-12 * max(1.0, abs(E_cible))):   # second essai seulement si la factorisation
        try:                                                        # rend "exactement singuliere"
            lu = sl.splu((A - E * sp.identity(n, format="csc", dtype=complex)).tocsc(), permc_spec="MMD_ATA")
            break
        except RuntimeError:
            repris = True
    if lu is None:
        return {"gamma": None, "gamma_im": None, "E_re": None, "poids_site": None, "residu": None, "iterations": 0,
                "suivi": False, "decalage_repris": True}, x0
    if x0 is None:
        x = np.zeros(n, dtype=complex); x[i0] = 1.0
    else:
        x = x0 / np.linalg.norm(x0)
    lam, res, it = complex(E_cible), float("inf"), 0
    for it in range(1, ITER_MAX + 1):
        y = lu.solve(x); x = y / np.linalg.norm(y)
        Ax = A @ x; lam = complex(np.vdot(x, Ax)); res = float(np.linalg.norm(Ax - lam * x))
        if it >= ITER_MIN and res <= TOL_RESIDU * max(1.0, abs(lam)):
            break
    poids = float(abs(x[i0]) ** 2)
    return {"gamma": float(2.0 * eta * np.sum(W * np.abs(x) ** 2)), "gamma_im": float(-2.0 * lam.imag),
            "E_re": float(lam.real), "poids_site": poids, "residu": res, "iterations": it, "decalage_repris": repris,
            "suivi": bool(res <= TOL_RESIDU * max(1.0, abs(lam)) and poids >= POIDS_MIN)}, x

def trajectoire(H0, diag, W, eta0, N, site, E_depart, ks):
    """Barreaux ks, parcourus de k = 3 vers les k croissants, puis de k = 2 vers les k decroissants ; l'energie
    cible et le vecteur de depart sont ceux du barreau voisin deja lu (ceux du depart a k = 3)."""
    out = {}
    haut = [k for k in sorted(ks) if k >= 3]; bas = [k for k in sorted(ks, reverse=True) if k < 3]
    for serie in (haut, bas):
        E, x = E_depart, None
        if serie is bas and haut and out[str(haut[0])]["suivi"]:
            E, x = out[str(haut[0])]["E_re"], x3
        for k in serie:
            r, xk = lire_etat(H0, diag, W, eta0 * 2.0 ** (-k), N, site, E, x)
            out[str(k)] = r
            if serie is haut and k == haut[0]:
                x3 = xk
            if r["suivi"]:
                E, x = r["E_re"], xk
    return out
# --- fin du bloc ---
