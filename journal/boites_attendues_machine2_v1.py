# -*- coding: ascii -*-
"""Calcule, SANS aucune diagonalisation, pour les 12 points du gel : g, s, graine, boite (r_c, N), faisabilite, et les gardes de
domaine G-1 du moteur (D1, D2a) que la sonde de machine 1 ne consulte pas. Usage : python -P ce_script <moteur>"""
import sys, math, importlib.util
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1]); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
POINTS = [("J1","19/10","1"),("J2","21/10","1"),("J3","39/20","3/2"),("J4","41/20","3/2"),("J5","39/20","2/3"),("J6","41/20","2/3"),
          ("T1","49/25","1"),("T2","51/25","1"),("T3","37/20","1"),("T4","43/20","1"),("A1","39/20","1"),("A2","41/20","1")]
print("BORNE_D1 = %s ; BORNE_D2A = %s ; N_MAX_EB = %d" % (M.BORNE_D1, M.BORNE_D2A, M.N_MAX_EB))
for pid, w, f in POINTS:
    w2, fac = F(w), F(f)
    greg = float(M.g_du_point(w2)); g = greg * float(fac)
    s = 0.70 * M.s_ff(w2, g)
    n1, n2 = M.appariement(s, w2)
    sites0 = M.barriere(n1, n2, w2, g, True)
    m2b = sites0[-1][0] if sites0 else 0
    r_c = int(math.ceil(n1)) + 2 * (m2b + max(8, m2b)) + 2
    N = r_c + 20
    Oc = M.Omega_du_canal(w2)[0]
    d_abs = abs(float(w2) - 2.0)
    D1 = d_abs / float(Oc)
    cmax = max([t / (2.0 * float(Oc)) for _, _, t in sites0], default=0.0)
    print("%s w2=%-5s x%-3s g_regle=%.4e g=%.4e s=%.5f graine=(%.3f,%.3f) card_b=%d r_c=%d N=%d faisable=%s | Omega_c=%.4f D1=%.4f (borne %.2f) %s ; c_max(graine)=%.4f (borne %.3f)"
          % (pid, w, f, greg, g, s, n1, n2, len(sites0), r_c, N, N <= M.N_MAX_EB, float(Oc), D1, float(M.BORNE_D1),
             "OK" if D1 <= float(M.BORNE_D1) else "HORS D1", cmax, float(M.BORNE_D2A)))
