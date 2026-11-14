# -*- coding: ascii -*-
"""La garde de domaine G-1 du moteur (D1, D2a) EXACTEMENT comme mesurer_point la calcule (seuil_A4 puis garde_domaine), aux 12 points
du gel, sans diagonalisation. Usage : python -P ce_script <moteur>"""
import sys, importlib.util
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1]); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
POINTS = [("J1","19/10","1"),("J2","21/10","1"),("J3","39/20","3/2"),("J4","41/20","3/2"),("J5","39/20","2/3"),("J6","41/20","2/3"),
          ("T1","49/25","1"),("T2","51/25","1"),("T3","37/20","1"),("T4","43/20","1"),("A1","39/20","1"),("A2","41/20","1")]
# et les six points de M17 (connus), pour situer l'echelle
POINTS += [("M17-1.95","39/20","1"),("M17-1.97","197/100","1"),("M17-1.98","99/50","1"),("M17-2.02","101/50","1"),("M17-2.03","203/100","1"),("M17-2.05","41/20","1")]
for pid, w, f in POINTS:
    w2 = F(w); g = float(M.g_du_point(w2)) * float(F(f))
    Oc = M.Omega_du_canal(w2)[0]
    try:
        seuil = M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)
        gd = M.garde_domaine(w2, g, seuil["S_det"], Oc)
        print("%-9s w2=%-7s x%-3s D1=%.4f (<=0.2) c_max=%.4f site %s (<=0.1) -> %s" % (pid, w, f, gd["D1"], gd["c_max"], gd["site_c_max"], gd["statut"]))
    except AssertionError as e:
        print("%-9s w2=%-7s x%-3s seuil_A4 ARRET (assert) : %s" % (pid, w, f, str(e)[:100]))
    except Exception as e:
        print("%-9s w2=%-7s x%-3s ERREUR %s: %s" % (pid, w, f, type(e).__name__, str(e)[:100]))
