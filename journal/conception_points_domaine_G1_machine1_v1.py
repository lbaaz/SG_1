# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1. CONCEPTION DU GEL "DOMAINE G-1" : la garde G-1 du moteur et la
# CHAINE SEULE (aucune diagonalisation 2D) sur une grille de points candidats.
# usage : python3 -I conception_points_domaine_G1_machine1_v1.py <moteur_v17.py>
import sys, importlib.util, math
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
W2S = [F(n, 100) for n in (186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198,
                           202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214)]
FACS = [F(1, 2), F(2, 3), F(1), F(3, 2), F(2), F(3)]
print("N_MAX_EB = %d ; bornes G-1 : D1 <= %s, c_max <= %s ; fraction 0.70" % (M.N_MAX_EB, M.BORNE_D1, M.BORNE_D2A))
print("w2     fac  g          graine          card r_c N   | D1     c_max  site garde        | modal    Gamma_ch   lisibles vides")
for fac in FACS:
    for w2 in W2S:
        g = M.g_du_point(w2) * float(fac); s = 0.70 * M.s_ff(w2, g); n1, n2 = M.appariement(s, w2)
        sites = M.barriere(n1, n2, w2, g, True)
        m2b = sites[-1][0] if sites else 0; bM = max(8, m2b); r_c = math.ceil(n1) + 2 * (m2b + bM) + 2
        Oc = M.Omega_du_canal(w2)[0]
        try:
            gd = M.garde_domaine(w2, g, M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"], Oc)
            garde = "%.4f %.4f %-4s %-12s" % (gd["D1"], gd["c_max"], gd["site_c_max"], gd["statut"])
        except BaseException as x:
            garde = "ERREUR %s" % (str(x)[:40])
        lis = []
        for b in range(max(0, int(n2) - 1), int(n2) + 3):
            for a in range(max(0, int(n1) - 3), int(n1) + 5):
                try:
                    st = M.barriere(float(a), float(b), w2, g, True)
                    if not st:
                        lis.append((a, b, None)); continue
                    gc = M.gamma_chaine(float(a), float(b), w2, g, st, eta_facteur=0.0625, M_facteur=4)["Gamma_c"]
                    lis.append((a, b, gc))
                except BaseException as x:
                    lis.append((a, b, "arret"))
        ok = [x for x in lis if isinstance(x[2], float) and 1.33e-12 < x[2] < 1e-3]
        vide = sum(1 for x in lis if x[2] is None)
        mod = [x for x in lis if x[0] == int(n1) and x[1] == int(n2)][0]
        print("%-6s %-4s %.4e (%5.2f,%5.2f) %3d %3d %3d | %s | (%2d,%d) %-10s %2d/%d %2d" % (
            w2, fac, g, n1, n2, len(sites), r_c, r_c + 20, garde, mod[0], mod[1],
            ("%.2e" % mod[2]) if isinstance(mod[2], float) else str(mod[2]), len(ok), len(lis), vide), flush=True)
    print()
