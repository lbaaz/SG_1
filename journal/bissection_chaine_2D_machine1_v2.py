# Hors chaine, classe 3, plume machine 1. Bissection de l'ecart Gamma_c (chaine E-A) / Gamma_LS (E-B)
# aux points M17 f070 : H complet (ancre : doit rendre le Gamma_LS du run) contre H "resonant seul"
# (diagonale libre + sauts +-(2,1) uniquement), meme graine, meme absorbeur, meme selection d'etat.
# usage : <moteur_v17.py> <num> <den> [variantes]
import sys, importlib.util, time, math
import numpy as np
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
from fractions import Fraction
w2 = Fraction(int(sys.argv[2]), int(sys.argv[3]))
variantes = sys.argv[4].split(",") if len(sys.argv) > 4 else ["complet", "resonant"]
N, r_c, P = 60, 40, M.P
g = M.g_du_point(w2); s = 0.70 * M.s_ff(w2, g)
eta = abs(float(w2) - 2.0) * 0.125
n1, n2 = M.appariement(s, w2)
print("w2=%s g=%.6e s=%.6f n1=%.3f n2=%.3f eta=%.6e N=%d r_c=%d" % (w2, g, s, n1, n2, eta, N, r_c), flush=True)

def H_filtre(garder):
    idx = M.indexation(N); dim = N * N
    H = np.zeros((dim, dim), dtype=complex)
    for (a, b), i in idx.items():
        H[i, i] = -float(M.W1) * a + float(w2) * b
    moitie = [(k, l) for k in range(-P, P + 1) for l in range(-P, P + 1)
              if abs(k) + abs(l) <= P and (k + l) % 2 == P % 2 and ((k, l) > (0, 0))]
    for (a, b), i in idx.items():
        for (k, l) in sorted(moitie):
            if not garder(k, l):
                continue
            a2, b2 = a + k, b + l
            if 0 <= a2 < N and 0 <= b2 < N:
                V = (g / P) * M.X_saut_reel(P, k, l, float(a), float(b), w2)
                if V:
                    j = idx[(a2, b2)]; H[j, i] += V; H[i, j] += V
    for (a, b), i in idx.items():
        if max(a, b) > r_c:
            H[i, i] += -1j * eta * (max(a, b) - r_c) ** 2
    return H

FILTRES = {
    "complet": lambda k, l: True,
    "resonant": lambda k, l: (k, l) == (2, 1),
    "sans_resonant": lambda k, l: (k, l) != (2, 1),
    "resonant_plus_voisins": lambda k, l: (k, l) in ((2, 1), (1, 0), (0, 1)),
}
psi = M.graine_coherente(N, s, w2)
_idx = M.indexation(N)
Jv = np.zeros(N * N); Bv = np.zeros(N * N)
for (a, b), i in _idx.items():
    Jv[i] = a - 2 * b; Bv[i] = b
for nom in variantes:
    t0 = time.time()
    H = H_filtre(FILTRES[nom])
    val, vec = np.linalg.eig(H)
    recs = np.abs(vec.conj().T @ psi) ** 2
    ordre = np.lexsort((val.real, -recs)); nu = ordre[0]
    tri = np.argsort(-recs)[:6]
    print("%-22s Gamma=%.4e  E_re=%.6f  recouvrement=%.4f  poids_total=%.4f  (%.0f s)" % (
        nom, -2.0 * val[nu].imag, val[nu].real, recs[nu], recs.sum(), time.time() - t0), flush=True)
    print("   six premiers (recouvrement, Gamma) : " + "  ".join(
        "(%.3f, %.2e)" % (recs[i], -2.0 * val[i].imag) for i in tri), flush=True)
    print("   Gamma pondere (tous etats) = %.4e" % float(np.sum(recs * (-2.0 * val.imag)) / recs.sum()), flush=True)
    for i in np.argsort(-recs)[:12]:
        w = np.abs(vec[:, i]) ** 2; w = w / w.sum()
        Jm = float(w @ Jv); Js = math.sqrt(max(float(w @ Jv ** 2) - Jm * Jm, 0.0))
        print("     rec=%.4f  Gamma=%.3e  E=%.5f  J=%+.3f (ecart-type %.3f)  <n2>=%.2f" % (
            recs[i], -2.0 * val[i].imag, val[i].real, Jm, Js, float(w @ Bv)), flush=True)
