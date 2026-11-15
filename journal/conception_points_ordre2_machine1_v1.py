# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1, 2026-11-14. CONCEPTION DU GEL "CHAINE D'ORDRE 2" : la garde du moteur, la
# chaine du moteur et la chaine d'ordre 2 (bloc), SEULES, sur une grille de points candidats. AUCUNE diagonalisation 2D.
# La largeur 2D n'est pas connue : elle est PREDITE par la loi post hoc de la note 022d32238a66df6b,
# ln(q2) = 2.87 delta^2 m_bord, pour compter les etats lisibles et situer les rapports attendus.
# usage : python3 -I conception_points_ordre2_machine1_v1.py <moteur_v17.py> <bloc.py>
import sys, importlib.util, math
from fractions import Fraction as F
import numpy as np
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(sys.argv[2], encoding="ascii").read(), "bloc", "exec"))
W2S = [F(n, 100) for n in list(range(186, 200)) + list(range(201, 215))]
FACS = [F(1, 2), F(2, 3), F(3, 4), F(1), F(4, 3), F(3, 2)]
B_LOI = 2.87
print("N_MAX_EB = %d ; fraction 0.70 ; loi post hoc ln(q2) = %.2f delta^2 m_bord" % (M.N_MAX_EB, B_LOI))
print("w2      fac  g          graine         card N   | D1     c_max  garde        | lis/32 | m_bord min-max | q2 predit : min med max | q1 predit : min med max | G2D predit min, modal")
for fac in FACS:
    for w2 in W2S:
        g = M.g_du_point(w2) * float(fac); s = 0.70 * M.s_ff(w2, g); n1, n2 = M.appariement(s, w2)
        d = float(w2) - 2.0
        sites = M.barriere(n1, n2, w2, g, True)
        m2b = sites[-1][0] if sites else 0; bM = max(8, m2b); r_c = math.ceil(n1) + 2 * (m2b + bM) + 2
        Oc = M.Omega_du_canal(w2)[0]
        try:
            gd = M.garde_domaine(w2, g, M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"], Oc)
            garde = "%.4f %.4f %-12s" % (gd["D1"], gd["c_max"], gd["statut"])
        except BaseException as x:
            garde = "ERREUR %s" % (str(x)[:30])
        L = []
        for b in range(max(0, int(n2) - 1), int(n2) + 3):
            for a in range(max(0, int(n1) - 3), int(n1) + 5):
                try:
                    st = M.barriere(float(a), float(b), w2, g, True)
                    if not st: continue
                    g1 = M.gamma_chaine(float(a), float(b), w2, g, st, eta_facteur=0.0625, M_facteur=4)["Gamma_c"]
                    tb = tables_ordre2(float(a), float(b), w2, g, st); r = gamma_chaine_ordre2(tb, 0.0625)
                    q2p = math.exp(B_LOI * d * d * st[-1][0]); g2d = r["Gamma_flux"] / q2p
                    L.append((a, b, st[-1][0], g1, r["Gamma_flux"], q2p, g2d))
                except BaseException as x:
                    pass
        ok = [x for x in L if 1.33e-12 < x[6] < 1e-3]
        mod = [x for x in L if x[0] == int(n1) and x[1] == int(n2)]
        if ok:
            q2 = sorted(x[5] for x in ok); q1 = sorted(x[3] / x[6] for x in ok)
            txt = "%2d/32  | %2d-%2d | %.3f %.3f %.3f | %6.3f %6.3f %6.3f | %.1e %s" % (len(ok), min(x[2] for x in ok), max(x[2] for x in ok),
                q2[0], float(np.median(q2)), q2[-1], q1[0], float(np.median(q1)), q1[-1], min(x[6] for x in ok), ("%.1e" % mod[0][6]) if mod else "-")
        else:
            txt = " 0/32"
        print("%-7s %-4s %.4e (%5.2f,%4.2f) %3d %3d | %s | %s" % (w2, fac, g, n1, n2, len(sites), r_c + 20, garde, txt), flush=True)
    print()
