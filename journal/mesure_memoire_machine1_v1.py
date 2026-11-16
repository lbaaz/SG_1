# -*- coding: ascii -*-
"""Pic de memoire et duree d'UNE lecture a la plus grande boite du gel (N = 154), au point de reglage H1 (r_c = 54),
etat de rang 0, absorbeur B (F2, 100 couches), k = 3. Usage : <moteur.py> <bloc.py> <sonde_domaine_G1.json>"""
import sys, json, time, resource, importlib.util
from fractions import Fraction as F
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sl
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(sys.argv[2]).read(), sys.argv[2], "exec"))
p = [q for q in json.load(open(sys.argv[3]))["points"] if q["id"] == "H1"][0]
num, den = p["w2"].split("/"); w2 = F(int(num), int(den)); r_c = p["r_c"]; N = r_c + 100
t0 = time.time(); H0, dg = assembler(w2, p["g"], N); H0 = H0.tocsc(); t1 = time.time()
e = [x for x in p["etats"] if x["rang"] == 0][0]
r, x = lire_etat(H0, dg, table_W(N, "F2", r_c, 100), p["eta0"] / 8.0, N, (int(e["n1"]), int(e["n2"])), e["E_re"])
t2 = time.time()
print("N = %d ; assemblage %.1f s ; une lecture %.1f s ; suivi %s ; pic de memoire : %d Mo" % (
    N, t1 - t0, t2 - t1, r["suivi"], resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024))
