# -*- coding: ascii -*-
"""La garde G-1 du moteur aux quatorze points du gel b59651f99e60707a, imprimee a TOUS LES CHIFFRES (repr), pour comparer deux nombres de fils BLAS :
la reserve R-3 de la note de machine 1 dit "la garde est de l'arithmetique sans BLAS". Usage : python -P garde_fils_machine2_v1.py <moteur> [etiquette]
(les variables de fils sont celles de l'environnement : lancer une fois sans, une fois avec OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1)."""
import importlib.util
import os
import sys
from fractions import Fraction as F

spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
POINTS = [("E1", "52/25", "1"), ("E2", "209/100", "1"), ("E3", "21/10", "3/2"), ("E4", "53/25", "3/2"), ("E5", "191/100", "1"), ("E6", "19/10", "3/2"),
          ("H1", "52/25", "2/3"), ("H2", "21/10", "2/3"), ("H3", "53/25", "1"), ("H4", "191/100", "2/3"), ("H5", "19/10", "2/3"), ("H6", "189/100", "1"),
          ("A1", "39/20", "1"), ("A2", "41/20", "1")]
print("fils : %s" % {k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")})
for pid, w, f in POINTS:
    w2 = F(w)
    g = float(M.g_du_point(w2)) * float(F(f))
    gd = M.garde_domaine(w2, g, M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"], M.Omega_du_canal(w2)[0])
    print("%s %s %s %r %r %s" % (pid, w, f, float(gd["D1"]), float(gd["c_max"]), gd["statut"]))
