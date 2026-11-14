# Hors chaine, classe 3, plume machine 1. CONCEPTION DU GEL : la CHAINE SEULE (aucune diagonalisation
# 2D) a des points candidats, pour savoir lesquels seraient lisibles. usage : <moteur_v17.py>
import sys, importlib.util, math
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
from fractions import Fraction as F
CAND = [(F(19, 10), F(1)), (F(21, 10), F(1)), (F(37, 20), F(1)), (F(43, 20), F(1)),
        (F(39, 20), F(1, 2)), (F(39, 20), F(3, 2)), (F(39, 20), F(2)), (F(39, 20), F(3)),
        (F(41, 20), F(1, 2)), (F(41, 20), F(3, 2)), (F(41, 20), F(2)), (F(41, 20), F(3)),
        (F(39, 20), F(1)), (F(41, 20), F(1)),
        (F(39, 20), F(2, 3)), (F(41, 20), F(2, 3)), (F(49, 25), F(1)), (F(51, 25), F(1))]
print("N_MAX_EB =", M.N_MAX_EB)
for w2, fac in CAND:
    g = M.g_du_point(w2) * float(fac); s = 0.70 * M.s_ff(w2, g); n1, n2 = M.appariement(s, w2)
    sites = M.barriere(n1, n2, w2, g, True)
    m2b = sites[-1][0] if sites else 0; bM = max(8, m2b); r_c = math.ceil(n1) + 2 * (m2b + bM) + 2
    lis = []
    for b in range(max(0, int(n2) - 1), int(n2) + 3):
        for a in range(max(0, int(n1) - 3), int(n1) + 5):
            st = M.barriere(float(a), float(b), w2, g, True)
            if not st:
                lis.append((a, b, None)); continue
            gc = M.gamma_chaine(float(a), float(b), w2, g, st, eta_facteur=0.0625, M_facteur=4)["Gamma_c"]
            lis.append((a, b, gc))
    ok = [x for x in lis if x[2] is not None and 1.33e-12 < x[2] < 1e-3]
    vide = sum(1 for x in lis if x[2] is None)
    mod = [x for x in lis if x[0] == int(n1) and x[1] == int(n2)][0]
    print("w2=%-6s x%-4s g=%.4e graine=(%.2f, %.2f) card=%d Lambda=%.2f r_c=%d N=%d | modal (%d,%d) Gamma_chaine=%s | %d/%d etats entre 1.33e-12 et 1e-3, %d a barriere vide" % (
        w2, fac, g, n1, n2, len(sites), M.Lambda_action(sites) if sites else 0.0, r_c, r_c + 20, mod[0], mod[1],
        ("%.2e" % mod[2]) if mod[2] is not None else "vide", len(ok), len(lis), vide))
