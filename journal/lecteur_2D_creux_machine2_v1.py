# -*- coding: ascii -*-
"""LECTEUR 2D CREUX de machine 2, v1 (15/11/2026). HORS CHAINE : un outil prepare d'avance, NON CERTIFIE, qui ne lit aucun objet
du gel a venir. Ecrit du texte du gel bis (dcda1611adf5f8fd, 3.3 a 3.8) et du moteur (82a0be882568fe0c) ; n'a pas vu le lecteur de
machine 1 (note 42c822811167b826, piste 0) avant d'etre fini : il est donc independant de lui par construction.

Ce qu'il fait. H(eta) = H0 - i eta diag(W) (gel bis 3.3, 3.4). H0 = H_2D(N, w2, g, signe, "x5", eta = 0) du moteur, assemble CREUX,
element par element, par les memes fonctions du moteur (X_saut_reel, memes boucles, meme ordre) ; il ne reecrit AUCUN element de
matrice. W : F1, F2, F3 du gel bis 3.4. Un SEUL etat est cherche par decalage-inversion (scipy.sparse.linalg.eigs, sigma reel) :
  - ANCRAGE (3.7) a k = 3 : parmi les K_ANCRE valeurs propres les plus proches de sigma = Re <psi|H0|psi>, l'etat de plus grand
    recouvrement hermitien |<v|psi>|^2 avec la graine psi (vecteurs propres droits, normes L2 ; lexsort sur la partie reelle,
    comme le moteur) ;
  - SUIVI (3.8) : de k a k+1 (puis de k a k-1), parmi les K_SUIVI valeurs propres les plus proches de Re E du pas precedent,
    l'etat de plus grand |<v'|v>| ; si ce maximum est < 0.90 : SUIVI PERDU, la trajectoire s'arrete de ce cote.
Deux lectures de la largeur, qui ne se confondent pas : gamma_E = -2 Im E, et gamma_W = 2 eta <W>, avec <W> = sum W |v|^2 / sum |v|^2.
L'identite Im E = -eta <W> est EXACTE pour un vecteur propre droit de H0 - i eta W (H0 hermitien, W reel diagonal) : elle donne la
largeur sans le plancher de la decomposition dense. Les deux sont consignees, aucune n'est choisie ici.
Usage : importe par validation_lecteur_creux_machine2_v1.py. Python 3.11, numpy 2.2.6, scipy 1.15.3 sur BOCAL4."""
import hashlib
import importlib.util
import unicodedata

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla

CANON_MOTEUR = '82a0be882568fe0c'
SEUIL_SUIVI = 0.90
K_ANCRE = 80
K_SUIVI = 12
K_MIN, K_MAX, K_ANCRAGE = -5, 12, 3
ORDRE_K = [3] + list(range(4, 13)) + [2, 1, 0, -1, -2, -3, -4, -5]      # gel bis 3.6


def empreinte_B(chemin):
    raw = open(chemin, 'rb').read()
    t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
    return hashlib.sha256(t).hexdigest()[:16]


def charger_moteur(chemin):
    """Le moteur est charge en LECTURE SEULE, son canon verifie avant tout calcul (gel bis 3.1, G-Q1)."""
    c = empreinte_B(chemin)
    if c != CANON_MOTEUR:
        raise SystemExit('ARRET : canon du moteur %s, attendu %s' % (c, CANON_MOTEUR))
    spec = importlib.util.spec_from_file_location('m17_chaine_v17', chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def assembler_H0(M, N, w2, g, signe):
    """H0 creux (CSC, reel) : memes boucles et memes appels que M.H_2D(N, w2, g, signe, 'x5', 0.0, None), p = M.P."""
    P = M.P
    moitie = sorted((k, l) for k in range(-P, P + 1) for l in range(-P, P + 1)
                    if abs(k) + abs(l) <= P and (k + l) % 2 == P % 2 and ((k, l) > (0, 0)))
    rows, cols, vals = [], [], []
    diag = np.empty(N * N)
    for a in range(N):
        for b in range(N):
            i = a * N + b
            diag[i] = signe * float(M.W1) * a + float(w2) * b
            for (k, l) in moitie:
                a2, b2 = a + k, b + l
                if 0 <= a2 < N and 0 <= b2 < N:
                    V = (g / P) * M.X_saut_reel(P, k, l, float(a), float(b), w2)
                    if V:
                        j = a2 * N + b2
                        rows += [j, i]
                        cols += [i, j]
                        vals += [V, V]
    H = sp.coo_matrix((vals, (rows, cols)), shape=(N * N, N * N)).tocsr() + sp.diags(diag)
    return H.tocsc()


def poids_absorbeur(forme, N, r_c):
    """W des formes du gel bis 3.4 ; a, b = occupations des modes 1 et 2 ; indice i = a * N + b ; L = N - r_c."""
    a = np.repeat(np.arange(N), N)
    b = np.tile(np.arange(N), N)
    L = N - r_c
    if forme == 'F1':
        m = np.maximum(a, b)
        return np.where(m > r_c, (m - r_c).astype(float) ** 2, 0.0)
    if forme == 'F2':
        m = np.maximum(a, b)
        return np.where(m > r_c, (m - r_c).astype(float) ** 4 / float(L * L), 0.0)
    if forme == 'F3':
        rho = np.maximum(a, 2 * b)
        return np.where(rho > r_c, (rho - r_c).astype(float) ** 2, 0.0)
    raise SystemExit('ARRET : forme inconnue %r' % (forme,))


def _v0(n):
    """Vecteur de depart d'ARPACK, FIXE : une lecture donne toujours le meme resultat."""
    rng = np.random.RandomState(20261115)
    return rng.standard_normal(n) + 1j * rng.standard_normal(n)


def voisins(H, cible, K):
    """Les K valeurs propres de H les plus proches de la cible (reelle), vecteurs propres droits normes L2."""
    vals, vecs = sla.eigs(H, k=K, sigma=float(cible), which='LM', v0=_v0(H.shape[0]), tol=0)
    vecs = vecs / np.linalg.norm(vecs, axis=0)
    return vals, vecs


def _lecture(H, W, eta, E, v):
    """Les deux largeurs, le residu et le poids dans l'absorbeur, pour un vecteur propre droit norme."""
    p = np.abs(v) ** 2
    s = float(p.sum())
    return {'E_re': float(E.real), 'E_im': float(E.imag), 'gamma_E': float(-2.0 * E.imag),
            'gamma_W': float(2.0 * eta * float(np.sum(W * p)) / s),
            'residu': float(np.linalg.norm(H @ v - E * v)), 'p_abs': float(np.sum(p[W > 0]) / s)}


def trajectoire(H0, W, psi, eta0, K_ancre=K_ANCRE, K_suivi=K_SUIVI, ks=None):
    """Lit l'etat d'ancrage (k = 3) puis le suit sur l'echelle eta_k = eta0 * 2^(-k) (exacte). Rend (dict k -> lecture, v3).
    Les k non atteints (suivi perdu) portent suivi = False et le recouvrement qui a fait perdre."""
    ks = list(ORDRE_K) if ks is None else list(ks)
    sigma = float(np.real(np.vdot(psi, H0 @ psi)))
    eta = lambda k: eta0 * 2.0 ** (-k)
    Hk = lambda k: (H0 + sp.diags(-1j * eta(k) * W)).tocsc()
    out = {}
    H3 = Hk(K_ANCRAGE)
    vals, vecs = voisins(H3, sigma, K_ancre)
    rec = np.abs(vecs.conj().T @ psi) ** 2
    o = np.lexsort((vals.real, -rec))
    nu = int(o[0])
    rep = _lecture(H3, W, eta(K_ANCRAGE), vals[nu], vecs[:, nu])
    rep.update({'suivi': True, 'ov': None, 'recouvrement_graine': float(rec[nu]), 'recouvrement_second': float(rec[o[1]]),
                'sigma': sigma, 'K_ancre': K_ancre, 'dist_sigma': float(abs(vals[nu].real - sigma)),
                'dist_max': float(np.abs(vals.real - sigma).max()), 'somme_rec_candidats': float(rec.sum())})
    out[K_ANCRAGE] = rep
    v3, E3 = vecs[:, nu], vals[nu]
    for sens, bornes in ((+1, range(K_ANCRAGE + 1, K_MAX + 1)), (-1, range(K_ANCRAGE - 1, K_MIN - 1, -1))):
        E, v = E3, v3
        perdu = False
        for k in bornes:
            if k not in ks:
                continue
            if perdu:
                out[k] = {'suivi': False, 'ov_max': None, 'motif': 'apres un suivi perdu'}
                continue
            H = Hk(k)
            vals, vecs = voisins(H, E.real, K_suivi)
            ov = np.abs(vecs.conj().T @ v)
            o = np.lexsort((vals.real, -ov))
            j = int(o[0])
            if ov[j] < SEUIL_SUIVI:
                perdu = True
                out[k] = {'suivi': False, 'ov_max': float(ov[j]), 'motif': 'suivi perdu'}
                continue
            rep = _lecture(H, W, eta(k), vals[j], vecs[:, j])
            rep.update({'suivi': True, 'ov': float(ov[j])})
            out[k] = rep
            E, v = vals[j], vecs[:, j]
    return out, v3


def restreindre(v, N, r0):
    """Restriction au bloc interieur max(a, b) <= r0, renormee (gel bis 3.9)."""
    A = v.reshape(N, N)[:r0 + 1, :r0 + 1].ravel()
    return A / np.linalg.norm(A)


def identite(va, Na, vb, Nb, r0):
    """Recouvrement hermitien restreint au bloc interieur entre deux etats d'ancrage (gel bis 3.9)."""
    return float(abs(np.vdot(restreindre(va, Na, r0), restreindre(vb, Nb, r0))))
