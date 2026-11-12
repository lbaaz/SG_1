# -*- coding: ascii -*-
# FUMEE A TAILLE REELLE (non opposable) : un point, G-Q3 puis G-Q4 a k = 3.
import sys, time, json, importlib.util
import numpy as np
spec = importlib.util.spec_from_file_location("sonde_qeb", sys.argv[1])
S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
M = S.charger_moteur(sys.argv[2])
nom = sys.argv[4]
p = S.parametres(sys.argv[3], False)[nom]
forme, r_c, N, L = S.geometrie("F1G20", p["r0"], False)
t0 = time.time(); s = S.Systeme(M, N, p["w2"], p["g"], -1); t1 = time.time()
eta = p["eta0"] * 2.0 ** (-3)
w = S.absorbeur("F1", r_c, N, L)
ref = M.H_2D(N, p["w2"], p["g"], -1, "x5", eta, r_c)[0]
np.fill_diagonal(s.H, s.d0 + (-1j * eta) * w)
print("point %s N = %d dim %d ; construction H %.1f s ; G-Q3 identite : %s" % (nom, N, N * N, t1 - t0, bool(np.array_equal(s.H, ref))))
del ref
psi = S.cible(M, ("graine",), N, p["s"], p["w2"])
t2 = time.time(); vals, vecs = s.decomposer(eta, w); t3 = time.time()
idx, x = S.choisir_graine(psi, 10, extras=True)(vals, vecs)
g3 = float(-2.0 * vals[idx[0]].imag)
print("decomposition %.1f s ; gamma(k = 3) = %.10e ; G_run = %.10e ; rapport - 1 = %.3e ; au bit %s" % (t3 - t2, g3, p["G_run"], g3 / p["G_run"] - 1.0, g3 == p["G_run"]))
print("recouvrement %.6f ; poids_total %.4f ; |somme_c - 1| = %.2e ; kappa[0] = %.6f ; kappa des dix : %s" % (x["recouvrements"][0], x["poids_total"], abs(complex(x["somme_c_re"], x["somme_c_im"]) - 1.0), x["kappa"][0], ["%.3f" % k for k in x["kappa"]]))
print("gamma des dix etats : %s" % ["%.2e" % float(-2.0 * vals[j].imag) for j in idx])
print("recouvrements des dix : %s" % ["%.4f" % r for r in x["recouvrements"]])
