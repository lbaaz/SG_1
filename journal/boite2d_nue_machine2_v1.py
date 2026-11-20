# -*- coding: ascii -*-
"""BOITE 2D FERMEE NUE au point sacrifie w2 = 101/50, REFAITE PAR MACHINE 2 (hors chaine, classe 3) : compte de niveaux, somme repondere, participation, a partir
du texte de la note de machine 1 (v2/v3, sections 2, 3, 4) ; ses scripts 2D ne sont PAS lus avant la comparaison.
Boite : etats (a, b), 0 <= a, b < N, paroi dure ; diagonale E = -W1 a + w2 b ; sauts (k, l) du demi-plan, |k|+|l| <= 5, k+l impair, V = (g/5) X_saut_reel(5, k, l, a, b, w2) (moteur du registre).
Etat du vide : (0, 0). Niveau-vide = niveau de plus grand poids sur (0, 0) ; c_k^2 = poids du niveau k sur (0, 0).
Fenetre : de 0.05 a 8 |delta| du niveau-vide, du cote OPPOSE a delta (delta = w2 - 2 = +0.02 : energies plus basses que le vide).
Densite lisse rho(E) : LDOS du site 0 de la chaine d'ordre 3 sous absorbeur adapte (18 variantes, mediane), lue a ECART au vide egal (le vide de chaque variante = sa valeur propre de plus grand poids sur le site 0).
Part y_k = c_k^2 / (w0 rho(E_k)) en unites de |delta| (m1) ; je donne aussi la version sans le poids du vide w0. Somme de y_k / largeur de la fenetre : attendu 1.
Usage : py -3.11 -P boite2d_nue_machine2_v1.py <registre> <barreaux 3|4|5> <cote_min> <cote_max> [pas]      (sortie : une ligne par cote)
        py -3.11 -P boite2d_nue_machine2_v1.py <registre> test                                   (compare ma boite a H_2D du moteur, N = 7)"""
import importlib.util
import math
import sys
import time
from fractions import Fraction as F
import numpy as np
import mpmath as mp
from scipy.linalg import eigh

executer = exec
REG = sys.argv[1].rstrip('/\\')
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = REG + "/scripts/" + bloc; executer(compile(open(p, encoding="ascii").read(), p, "exec"))
W2 = F(101, 50); W2F = float(W2); DELTA = W2F - 2.0; AD = abs(DELTA); P5 = 5
G_DE = {3: 5.53067e-03, 4: 4.22189e-03, 5: 3.35640e-03}          # g de la note de m1 (texte)
SAUTS = sorted((k, l) for k in range(-P5, P5 + 1) for l in range(-P5, P5 + 1) if abs(k) + abs(l) <= P5 and (k + l) % 2 == P5 % 2 and (k, l) > (0, 0))


def boite(N, g):
    """H reel symetrique de la boite N x N (indice a*N + b)."""
    H = np.zeros((N * N, N * N))
    for a in range(N):
        for b in range(N):
            i = a * N + b; H[i, i] = -a + W2F * b
            for (k, l) in SAUTS:
                a2, b2 = a + k, b + l
                if 0 <= a2 < N and 0 <= b2 < N:
                    V = (g / P5) * M.X_saut_reel(P5, k, l, float(a), float(b), W2)
                    if V:
                        j = a2 * N + b2; H[i, j] += V; H[j, i] += V
    return H


if len(sys.argv) > 2 and sys.argv[2] == 'test':
    for nb in (3, 4, 5):
        g = G_DE[nb]; Hm = boite(7, g); He, idx = M.H_2D(7, W2, g)
        print('barreaux %d : N = 7, max |H(moi) - Re H_2D(moteur)| = %.3e, max |Im H_2D| = %.3e, symetrie de ma boite %.3e' % (nb, np.max(np.abs(Hm - He.real)), np.max(np.abs(He.imag)), np.max(np.abs(Hm - Hm.T))))
    raise SystemExit(0)

CREUX = sys.argv[2] == 'creux'
if CREUX:
    NB = int(sys.argv[3]); COTES = [int(x) for x in sys.argv[4:]]; CMIN, CMAX, PAS = 0, -1, 1
else:
    NB = int(sys.argv[2]); CMIN, CMAX = int(sys.argv[3]), int(sys.argv[4]); PAS = int(sys.argv[5]) if len(sys.argv) > 5 else 1
g = G_DE[NB]
sites = M.barriere(0, 0, W2, g, True); tb = tables_ordre2(0, 0, W2, g, sites); t3 = tables_ordre3(0, 0, W2, g, tb)
OFFS = -np.logspace(math.log10(0.04 * AD), math.log10(9.0 * AD), 3000)[::-1]        # ecarts au vide, du plus lointain au plus proche (negatifs : cote oppose a delta)
OFFS = np.sort(OFFS)
LOGRHO = []
for (a, c, L) in VARIANTES_ADAPTEES:
    H, Wd, i0 = matrice_adaptee(tb, t3, a, c, L, 3)
    val, vec = np.linalg.eig(H); nu = int(np.lexsort((val.real, -np.abs(vec[i0, :]) ** 2))[0]); Ev = float(val[nu].real)
    r = []
    for dE in OFFS:
        x = np.linalg.solve((Ev + dE) * np.eye(len(H)) - H, np.eye(len(H))[:, i0]); r.append(-x[i0].imag / math.pi)
    LOGRHO.append(np.log(np.maximum(np.array(r), 1e-300)))
LOGRHO = np.median(np.array(LOGRHO), axis=0)
print('# barreaux %d  g = %.5e  m_bord = %d  rho lisse : %d variantes, ecart au vide de %.3f a %.3f |delta|' % (NB, g, tb["m2_bord"], len(VARIANTES_ADAPTEES), OFFS[0] / AD, OFFS[-1] / AD))
print('# cote  dim   w0          E_vide       n_tous  n_y>1e-3max  Somme/larg (m1: avec 1/w0)  Somme/larg (sans w0)  participation(y)  y_min/mediane')
def boite_creuse(N, g):
    """Meme boite, en matrice creuse (CSR)."""
    import scipy.sparse as sp
    li, co, va = [], [], []
    di = np.array([-(i // N) + W2F * (i % N) for i in range(N * N)])
    for a in range(N):
        for b in range(N):
            i = a * N + b
            for (k, l) in SAUTS:
                a2, b2 = a + k, b + l
                if 0 <= a2 < N and 0 <= b2 < N:
                    V = (g / P5) * M.X_saut_reel(P5, k, l, float(a), float(b), W2)
                    if V:
                        j = a2 * N + b2; li += [i, j]; co += [j, i]; va += [V, V]
    return (sp.csr_matrix((va, (li, co)), shape=(N * N, N * N)) + sp.diags(di)).tocsc()


def niveaux_creux(N, g):
    """Niveaux et poids c_k^2 sur (0,0) : le niveau-vide (sigma = 0), puis TOUS les niveaux de la fenetre (sigma au centre, k doublee tant que la fenetre n'est pas strictement
    contenue dans les niveaux trouves). Rend (E, c2) restreints au vide et a la fenetre."""
    from scipy.sparse.linalg import eigsh
    H = boite_creuse(N, g)
    Ev0, V0 = eigsh(H, k=6, sigma=0.0, which='LM'); nu = int(np.argmax(V0[0, :] ** 2)); Ev = float(Ev0[nu]); w0 = float(V0[0, nu] ** 2)
    sig = Ev - 4.025 * AD; demi = 3.975 * AD; k = 40
    while True:
        E, V = eigsh(H, k=k, sigma=sig, which='LM')
        if np.max(np.abs(E - sig)) > demi + 0.5 * AD or k >= 600:
            break
        k *= 2
    c2 = V[0, :] ** 2
    return np.concatenate(([Ev], E)), np.concatenate(([w0], c2)), k


for N in (COTES if CREUX else range(CMIN, CMAX + 1, PAS)):
    t0 = time.time()
    if CREUX:
        E, c2, kk = niveaux_creux(N, g)
        nu = 0; Ev = float(E[0]); w0 = float(c2[0]); E = E[1:]; c2 = c2[1:]
    else:
        H = boite(N, g); E, V = eigh(H); c2 = V[0, :] ** 2; del V
        nu = int(np.argmax(c2)); Ev = float(E[nu]); w0 = float(c2[nu])
    lo, hi = Ev - 8.0 * AD, Ev - 0.05 * AD
    m = (E > lo) & (E < hi)
    off = E[m] - Ev; y = c2[m] / np.exp(np.interp(off, OFFS, LOGRHO))          # largeur d'energie sans w0
    ntous = int(m.sum())
    if ntous:
        ym = y[y > 1e-3 * y.max()]
        S0 = float(y.sum()) / (7.95 * AD); S1 = S0 / w0
        part = float(y.sum() ** 2 / np.sum(y ** 2)); rapp = float(y.min() / np.median(y))
        print('%-5d %-5d %.8f  %+.6f  %-6d %-12d %-27.4f %-21.4f %-17.3f %.3e' % (N, N * N, w0, Ev, ntous, len(ym), S1, S0, part, rapp), flush=True)
    else:
        print('%-5d %-5d %.8f  %+.6f  0 niveau dans la fenetre' % (N, N * N, w0, Ev), flush=True)
