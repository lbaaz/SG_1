# Hors chaine, classe 3, plume machine 1, non contresigne.
# A un point M17 (fraction 0.70) : H_2D du moteur v17 (certifie) diagonalise au reglage du run
# (N=60, r_c=40, eta=|delta|/8) ; les etats de plus grand recouvrement avec la graine coherente sont
# etiquetes par J = n1 - 2 n2 et k = <n2> ; la chaine E-A du moteur (gamma_chaine) est evaluee aux
# occupations ENTIERES (n1 = J + 2k, n2 = k) et comparee etat par etat.
# usage : <moteur_v17.py> <num> <den>
import sys, importlib.util, math, time
import numpy as np
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
from fractions import Fraction
w2 = Fraction(int(sys.argv[2]), int(sys.argv[3]))
N, r_c = 60, 40
g = M.g_du_point(w2); s = 0.70 * M.s_ff(w2, g)
eta = abs(float(w2) - 2.0) * 0.125
n1r, n2r = M.appariement(s, w2)
def chaine(n1, n2):
    sites = M.barriere(n1, n2, w2, g, True)
    gs = [M.gamma_chaine(n1, n2, w2, g, sites, eta_facteur=ef, M_facteur=4)["Gamma_c"]
          for ef in (0.25, 0.125, 0.0625, 0.03125)]
    return gs, (M.Lambda_action(sites) if sites else 0.0)
t0 = time.time()
H, idx = M.H_2D(N, w2, g, -1, "x5", eta, r_c)
val, vec = np.linalg.eig(H)
psi = M.graine_coherente(N, s, w2)
recs = np.abs(vec.conj().T @ psi) ** 2
Jv = np.zeros(N * N); Bv = np.zeros(N * N)
for (a, b), i in idx.items():
    Jv[i] = a - 2 * b; Bv[i] = b
gr, lr = chaine(n1r, n2r)
print("POINT w2=%s g=%.6e s=%.6f eta=%.4e graine=(%.3f, %.3f) ntot_moyen=%.3f  Gamma_c(graine reelle)=%.4e Lambda=%.3f  (%.0f s)" % (
    w2, g, s, eta, n1r, n2r, n1r + n2r, gr[2], lr, time.time() - t0), flush=True)
print("rang rec     n1 n2 ntot  sigma_J  Gamma_2D     Gamma_chaine  etal_eta  chaine/2D")
tri = np.argsort(-recs)[:14]
rap = []
for r, i in enumerate(tri):
    w = np.abs(vec[:, i]) ** 2; w = w / w.sum()
    Jm = float(w @ Jv); Js = math.sqrt(max(float(w @ Jv ** 2) - Jm * Jm, 0.0)); k = float(w @ Bv)
    J, kk = int(round(Jm)), int(round(k)); n1 = J + 2 * kk
    g2 = -2.0 * val[i].imag
    if n1 < 0 or kk < 0:
        print("%2d  %.4f  (J=%.2f k=%.2f hors lecture)" % (r, recs[i], Jm, k)); continue
    gs, lam = chaine(float(n1), float(kk))
    pos = [x for x in gs if x > 0]
    et = (max(pos) / min(pos)) if len(pos) == 4 else float("nan")
    q = gs[2] / g2 if g2 > 0 else float("nan")
    if g2 > 1.33e-12:
        rap.append(q)
    print("%2d  %.4f  %2d %2d  %3d   %.3f    %.3e    %.3e     %.3f     %.3f%s" % (
        r, recs[i], n1, kk, n1 + kk, Js, g2, gs[2], et, q, "" if g2 > 1.33e-12 else "  (sous 10 planchers)"), flush=True)
print("BILAN w2=%s : etat lu par E-B = rang 0 ; chaine/2D min %.3f max %.3f sur %d etats au-dessus de 10 planchers ; marge du rang 0 sur le rang 1 : %.4f" % (
    w2, min(rap), max(rap), len(rap), recs[tri[0]] / recs[tri[1]]), flush=True)
