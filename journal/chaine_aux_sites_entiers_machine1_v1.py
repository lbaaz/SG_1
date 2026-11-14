# Hors chaine, classe 3, plume machine 1. La chaine E-A du moteur v17 (gamma_chaine, barriere),
# evaluee aux occupations ENTIERES des etats propres 2D lus par bissection_chaine_2D_v2.
# usage : <moteur_v17.py> <num> <den> "n1,n2,Gamma2D;n1,n2,Gamma2D;..."
import sys, importlib.util, math
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
from fractions import Fraction
w2 = Fraction(int(sys.argv[2]), int(sys.argv[3]))
g = M.g_du_point(w2); s = 0.70 * M.s_ff(w2, g)
def chaine(n1, n2):
    sites = M.barriere(n1, n2, w2, g, True)
    out = []
    for ef in (0.25, 0.125, 0.0625, 0.03125):
        out.append(M.gamma_chaine(n1, n2, w2, g, sites, eta_facteur=ef, M_facteur=4)["Gamma_c"])
    return out, (M.Lambda_action(sites) if sites else 0.0), len(sites)
n1r, n2r = M.appariement(s, w2)
gs, lam, card = chaine(n1r, n2r)
print("w2=%s  graine reelle (%.3f, %.3f) : Gamma_c aux quatre eta = %s  Lambda=%.3f card=%d" % (
    w2, n1r, n2r, " ".join("%.3e" % x for x in gs), lam, card))
print(" n1 n2  ntot  Gamma_2D     Gamma_chaine(eta/16)  etalement_eta  chaine/2D   Lambda  card")
for bloc in sys.argv[4].split(";"):
    a, b, g2 = bloc.split(","); a, b, g2 = int(a), int(b), float(g2)
    gs, lam, card = chaine(float(a), float(b))
    pos = [x for x in gs if x > 0]
    et = (max(pos) / min(pos)) if len(pos) == 4 else float("nan")
    print(" %2d %2d  %3d   %.3e    %.3e            %.3f        %7.3f    %6.3f  %d" % (
        a, b, a + b, g2, gs[2], et, gs[2] / g2, lam, card))
