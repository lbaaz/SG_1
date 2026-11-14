# Hors chaine, classe 3, plume machine 1, non contresigne.
# La chaine E-A du moteur v17 avec, en diagonale, le decalage du second ordre Sigma2 du moteur
# (e_m = m*delta + Sigma2_m - Sigma2_0), confrontee aux largeurs 2D lues dans les journaux
# comparaison_par_etat_machine1_v1_{A,B}.log.  usage : <moteur> <journal> [<journal> ...]
import sys, importlib.util, math, re
import numpy as np
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
from fractions import Fraction
def chaine2(n1, n2, w2, g, ef=0.0625, Mf=4, sigma=True):
    d = float(w2) - 2.0
    sites = M.barriere(n1, n2, w2, g, True)
    m2 = sites[-1][0] if sites else 8
    bM = max(8, m2); Mm = (m2 + bM) * Mf; debut = m2 + bM // 2
    S0 = M.Sigma2_site(n1, n2, w2, g)[0] if sigma else 0.0
    H = np.zeros((Mm + 1, Mm + 1), dtype=complex)
    for m in range(Mm + 1):
        Sm = M.Sigma2_site(n1 + 2 * m, n2 + m, w2, g)[0] if sigma else 0.0
        H[m, m] = m * d + (Sm - S0)
        if m > debut:
            H[m, m] += -1j * abs(d) * ef * (m - debut) ** 2
        if m < Mm:
            t = M.t_site(m, n1, n2, w2, g); H[m, m + 1] = t; H[m + 1, m] = t
    val, vec = np.linalg.eig(H)
    nu = int(np.argmax(np.abs(vec[0, :]) ** 2))
    return -2.0 * val[nu].imag
tous = []
for jl in sys.argv[2:]:
    w2 = None
    for l in open(jl, encoding="utf-8"):
        m = re.match(r"POINT w2=(\d+)/(\d+) ", l)
        if m:
            w2 = Fraction(int(m.group(1)), int(m.group(2))); g = M.g_du_point(w2); lig = []; continue
        m = re.match(r"\s*(\d+)\s+0\.\d+\s+(\d+)\s+(\d+)\s+\d+\s+[\d.]+\s+([\d.e+-]+)\s+([\d.e+-]+)", l)
        if m and w2 is not None:
            r, n1, n2, g2, gc1 = int(m.group(1)), int(m.group(2)), int(m.group(3)), float(m.group(4)), float(m.group(5))
            if g2 > 1.33e-12:
                c2 = chaine2(float(n1), float(n2), w2, g)
                c1 = chaine2(float(n1), float(n2), w2, g, sigma=False)
                lig.append((r, n1, n2, g2, gc1, c1, c2))
        if l.startswith("BILAN") and w2 is not None:
            q1 = [x[4] / x[3] for x in lig]; q2 = [x[6] / x[3] for x in lig]
            lent = [x for x in lig if x[3] < 1e-7]
            q2l = [x[6] / x[3] for x in lent]
            e0 = lig[0]
            print("w2=%.2f  etats=%d  1er ordre : %.3f a %.3f   avec Sigma2 : %.3f a %.3f   (Gamma<1e-7, %d etats : %.3f a %.3f)   etat lu (%d,%d) : %.3f -> %.3f   controle rejeu 1er ordre %.3f" % (
                float(w2), len(lig), min(q1), max(q1), min(q2), max(q2), len(lent), min(q2l), max(q2l),
                e0[1], e0[2], e0[4] / e0[3], e0[6] / e0[3], max(abs(x[5] / x[4] - 1) for x in lig)), flush=True)
            tous += [(float(w2),) + x for x in lig]; w2 = None
q = [x[7] / x[4] for x in tous]; ql = [x[7] / x[4] for x in tous if x[4] < 1e-7]
print("ENSEMBLE : %d etats-points ; avec Sigma2 chaine/2D de %.3f a %.3f ; pour Gamma_2D < 1e-7 (%d) de %.3f a %.3f ; Gamma_2D de %.2e a %.2e" % (
    len(q), min(q), max(q), len(ql), min(ql), max(ql), min(x[4] for x in tous), max(x[4] for x in tous)))
