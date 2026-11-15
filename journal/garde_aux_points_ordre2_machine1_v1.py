# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1, 2026-11-14. Les seize points du gel "chaine d'ordre 2" : couplage, graine,
# garde G-1 du moteur (calculee comme mesurer_point la calcule, SANS diagonalisation 2D), barriere a la graine et boite
# attendue par la regle de executer_EB. usage : python3 -I garde_aux_points_ordre2_machine1_v1.py <moteur_v17.py>
import sys, math, importlib.util
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
POINTS = [("C1", F(197, 100), F(2, 3)), ("C2", F(97, 50), F(3, 4)), ("C3", F(203, 100), F(3, 2)), ("C4", F(103, 50), F(4, 3)),
          ("M1", F(193, 100), F(1)), ("M2", F(48, 25), F(4, 3)), ("M3", F(207, 100), F(2, 3)), ("M4", F(21, 10), F(3, 4)),
          ("L1", F(189, 100), F(4, 3)), ("L2", F(47, 25), F(1)), ("L3", F(211, 100), F(3, 2)), ("L4", F(53, 25), F(2, 3)),
          ("A1", F(39, 20), F(1)), ("A2", F(41, 20), F(1)), ("W1", F(107, 50), F(1)), ("W2", F(209, 100), F(1, 2))]
print("bornes G-1 du moteur : D1 <= %s, c_max <= %s ; fraction 0.70 ; N_MAX_EB = %d" % (M.BORNE_D1, M.BORNE_D2A, M.N_MAX_EB))
for pid, w2, fac in POINTS:
    g = M.g_du_point(w2) * float(fac); s = 0.70 * M.s_ff(w2, g); n1, n2 = M.appariement(s, w2)
    sites = M.barriere(n1, n2, w2, g, True)
    m2b = sites[-1][0] if sites else 0; r_c = int(math.ceil(n1)) + 2 * (m2b + max(8, m2b)) + 2
    Oc = M.Omega_du_canal(w2)[0]
    gd = M.garde_domaine(w2, g, M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"], Oc)
    print("%s w2=%-7s x%-3s delta=%+.2f g=%.6e Omega_c=%-5s D1=%.6f c_max=%.6f site=%s %-12s graine=(%.3f, %.3f) card=%d r_c=%d N=%d" % (
        pid, w2, fac, float(w2) - 2.0, g, Oc, gd["D1"], gd["c_max"], gd["site_c_max"], gd["statut"], n1, n2, len(sites), r_c, r_c + 20))
