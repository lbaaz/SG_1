# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1, 2026-11-14. La chaine d'ordre 2 (bloc) aux deux etats d'ancre : valeurs de
# reference de la garde G-8 du gel. Aucune diagonalisation 2D. usage : <moteur_v17.py> <bloc.py>
import sys, math, importlib.util
from fractions import Fraction as F
import numpy as np
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(sys.argv[2], encoding="ascii").read(), "bloc", "exec"))
for pid, w2, n1, n2 in (("A1", F(39, 20), 7, 2), ("A2", F(41, 20), 8, 2)):
    g = float(M.g_du_point(w2)); sites = M.barriere(float(n1), float(n2), w2, g, True)
    tb = tables_ordre2(float(n1), float(n2), w2, g, sites, M_facteur=4)
    for ef in (0.25, 0.125, 0.0625, 0.03125):
        r = gamma_chaine_ordre2(tb, ef)
        print("%s (%d,%d) eta de chaine %-7s Gamma_flux = %r  -2 Im E = %r  dE = %r  m_bord = %d  m_min = %d" % (
            pid, n1, n2, ef, r["Gamma_flux"], r["Gamma_c2"], r["dE"], tb["m2_bord"], tb["m_min"]))
    print("%s E_libre = %r  Sigma2(0) = %r" % (pid, float(M.energie_libre(float(n1), float(n2), w2)), tb["S"][0]))
