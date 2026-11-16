# -*- coding: ascii -*-
"""Lecteur 2D creux (hors chaine, classe 3) : la largeur d'UN etat du H 2D du moteur sous un absorbeur quelconque,
par decalage-inversion autour de l'energie de l'etat (scipy.sparse.linalg.eigs), sans decomposition complete.
Le hamiltonien est celui de H_2D du moteur, element par element (X_saut_reel du moteur), assemble creux.
Etat lu : parmi les etats voisins de l'energie cible, celui de plus grand poids au site de Fock (n1, n2).
Largeur : Gamma = 2 eta <psi|W|psi> / <psi|psi> (identite exacte pour un vecteur propre droit, H0 hermitien).
N'est PAS la sonde certifiee : outil d'exploration, valide contre les sorties de la nuit bis (voir validation)."""
import math, importlib.util
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl

def charger_moteur(chemin):
    spec = importlib.util.spec_from_file_location("moteur", chemin)
    M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
    return M

class Point:
    def __init__(self, M, w2, g, Nmax):
        self.M, self.w2, self.g, self.Nmax = M, w2, g, Nmax
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
        self.H0max = sp.csr_matrix((V, (I, J)), shape=(Nmax * Nmax, Nmax * Nmax), dtype=float)
        self.diag = np.array([-W1 * a + w * b for a in range(Nmax) for b in range(Nmax)])

    def bloc(self, N):
        sel = np.array([a * self.Nmax + b for a in range(N) for b in range(N)])
        H0 = self.H0max[sel][:, sel].tocsc()
        return H0, self.diag[sel]

def W_table(N, forme, r_c, L=None, param=None):
    """W(a, b) sur la boite N x N. Formes : F1, F2, F3 du gel bis ; Pn (puissance n sur max(a, b))."""
    L = (N - r_c) if L is None else L
    W = np.zeros(N * N)
    for a in range(N):
        for b in range(N):
            if forme == "F3":
                r = max(a, 2 * b)
            else:
                r = max(a, b)
            x = r - r_c
            if x <= 0:
                continue
            if forme in ("F1", "F3"):
                W[a * N + b] = float(x * x)
            elif forme == "F2":
                W[a * N + b] = float(x ** 4) / float(L * L)
            elif forme == "P":                       # puissance param, normee pour valoir L^2 a la distance L
                W[a * N + b] = float(x) ** param / float(L) ** (param - 2.0)
            else:
                raise ValueError(forme)
    return W

def lire_etat(H0, diag, W, eta, N, site, E_cible, n_voisins=6):
    A = (H0 + sp.diags(diag - 1j * eta * W)).tocsc().astype(complex)
    val, vec = sl.eigs(A, k=n_voisins, sigma=E_cible, which="LM", tol=0)
    i0 = site[0] * N + site[1]
    poids = np.abs(vec[i0, :]) ** 2 / np.sum(np.abs(vec) ** 2, axis=0)
    nu = int(np.argmax(poids))
    psi = vec[:, nu]; n2 = float(np.real(np.vdot(psi, psi)))
    gam = 2.0 * eta * float(np.sum(W * np.abs(psi) ** 2)) / n2
    res = float(np.linalg.norm(A @ psi - val[nu] * psi) / math.sqrt(n2))
    return {"gamma": gam, "gamma_im": float(-2.0 * val[nu].imag), "E_re": float(val[nu].real), "poids_site": float(poids[nu]), "residu": res}
