# UNE decomposition a taille reelle ; N'IMPRIME QUE gamma de l'etat d'ancrage et son rapport a G_run.
import sys, os, time, importlib.util
sys.dont_write_bytecode = True
SONDE, MOTEUR, RUN = sys.argv[1:4]
spec = importlib.util.spec_from_file_location("sonde_qeb", SONDE)
S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
M = S.charger_moteur(MOTEUR)
p = S.parametres(RUN, False)["39_20"]
forme, r_c, N, L = S.geometrie("F1G20", p["r0"], False)
s = S.Systeme(M, N, p["w2"], p["g"], -1)
psi = S.cible(M, ("graine",), N, p["s"], p["w2"])
t0 = time.time()
vals, vecs = s.decomposer(p["eta0"] * 2.0 ** (-3), S.absorbeur(forme, r_c, N, L))
idx, x = S.choisir_graine(psi, 1)(vals, vecs)
g3 = float(-2.0 * vals[idx[0]].imag)
print("ANCRAGE point 39_20 N = %d : %.1f s ; gamma = %.10e ; G_run = %.10e ; rapport - 1 = %.3e ; au bit %s" % (
    N, time.time() - t0, g3, p["G_run"], g3 / p["G_run"] - 1.0, g3 == p["G_run"]))
