# Hors chaine, classe 3, plume machine 1. PROPOSITION NON GELEE : largeurs de la chaine E-A du moteur
# v17 (gamma_chaine, eta_facteur 1/16, M_facteur 4) aux occupations entieres, a des points (w2, g)
# qu'aucune machine n'a diagonalises en 2D. usage : <moteur_v17.py> <num/den> [<num/den> ...]
import sys, importlib.util
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
from fractions import Fraction
for a in sys.argv[2:]:
    w2 = Fraction(a); g = M.g_du_point(w2); s = 0.70 * M.s_ff(w2, g); n1r, n2r = M.appariement(s, w2)
    print("POINT w2=%s g=%.6e s(f=0.70)=%.6f graine=(%.3f, %.3f)" % (w2, g, s, n1r, n2r))
    print(" n1 n2  Gamma_chaine   etalement sur eta/4..eta/32")
    for n2 in (1, 2, 3):
        for n1 in range(5, 11):
            sites = M.barriere(float(n1), float(n2), w2, g, True)
            gs = [M.gamma_chaine(float(n1), float(n2), w2, g, sites, eta_facteur=ef, M_facteur=4)["Gamma_c"]
                  for ef in (0.25, 0.125, 0.0625, 0.03125)]
            pos = [x for x in gs if x > 0]
            print(" %2d %2d  %.4e     %s" % (n1, n2, gs[2], ("%.3f" % (max(pos) / min(pos))) if len(pos) == 4 else "non lu"))
