# Hors chaine, classe 3, plume machine 1. Leve la morsure (i) de machine 2 (lot df01461fc9b2b099) :
# la note 9322566db2546adb dit "<n2> entier a 0.1 pres" alors que le script du lot 2b211d51 n'imprime
# que l'arrondi. Ici <n1>, <n2> et leurs ecarts a l'entier sont imprimes aux quatorze rangs.
# Meme reglage que comparaison_par_etat_machine1_v1.py. usage : <moteur_v17.py> <num> <den>
import sys, importlib.util, math
import numpy as np
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
from fractions import Fraction
w2 = Fraction(int(sys.argv[2]), int(sys.argv[3]))
N, r_c = 60, 40
g = M.g_du_point(w2); s = 0.70 * M.s_ff(w2, g); eta = abs(float(w2) - 2.0) * 0.125
H, idx = M.H_2D(N, w2, g, -1, "x5", eta, r_c)
val, vec = np.linalg.eig(H)
psi = M.graine_coherente(N, s, w2)
recs = np.abs(vec.conj().T @ psi) ** 2
Av = np.zeros(N * N); Bv = np.zeros(N * N)
for (a, b), i in idx.items():
    Av[i] = a; Bv[i] = b
print("POINT w2=%s" % w2, flush=True)
print("rang  <n1>     <n2>     ecart_n1  ecart_n2  sigma_n2  poids_Fock_max  Gamma_2D")
pire1 = pire2 = 0.0; pmin = 1.0
for r, i in enumerate(np.argsort(-recs)[:14]):
    w = np.abs(vec[:, i]) ** 2; w = w / w.sum()
    a = float(w @ Av); b = float(w @ Bv); sb = math.sqrt(max(float(w @ Bv ** 2) - b * b, 0.0))
    g2 = -2.0 * val[i].imag
    e1, e2 = a - round(a), b - round(b)
    if g2 > 1.33e-12:
        pire1 = max(pire1, abs(e1)); pire2 = max(pire2, abs(e2)); pmin = min(pmin, float(w.max()))
    print("%2d    %.4f  %.4f  %+.4f   %+.4f   %.4f    %.4f          %.3e%s" % (
        r, a, b, e1, e2, sb, float(w.max()), g2, "" if g2 > 1.33e-12 else "  (sous 10 planchers)"), flush=True)
print("BILAN w2=%s : sur les etats au-dessus de 10 planchers, pire |ecart <n1>| = %.4f, pire |ecart <n2>| = %.4f, plus petit poids sur un seul etat de Fock = %.4f" % (
    w2, pire1, pire2, pmin), flush=True)
