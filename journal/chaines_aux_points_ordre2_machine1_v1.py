# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1, 2026-11-14. Les deux chaines, SEULES, aux seize points du gel, sur les 32 sites
# voisins de la graine, par les fonctions de la sonde elle-meme : aucune exception ne doit etre levee. AUCUNE 2D.
# usage : python3 -I chaines_aux_points_ordre2_machine1_v1.py <moteur_v17.py> <sonde_ordre2.py>
import sys, importlib.util, math
src = open(sys.argv[2], encoding="ascii").read()
argv = sys.argv; sys.argv = [argv[2], argv[1], "inutile.json"]
S = {"__name__": "sonde_chargee", "__file__": argv[2]}
exec(compile(src, "sonde", "exec"), S); sys.argv = argv
M = S["M"]
print("id  w2      fac  sites  barriere vide  chaine du moteur  ordre 2  exceptions | Gamma_flux min, max | flux contre -2 Im E, max")
tot = [0, 0]
for (pid, role, w2, fac) in S["POINTS"]:
    g = float(M.g_du_point(w2)) * float(fac); s = S["FRACTION"] * M.s_ff(w2, g); n1, n2 = M.appariement(s, w2)
    n = vide = c1 = c2 = exc = 0; fl = []; ec = []
    for b in range(max(0, int(n2) - 1), int(n2) + 3):
        for a in range(max(0, int(n1) - 3), int(n1) + 5):
            n += 1
            try:
                st = M.barriere(float(a), float(b), w2, g, True)
                if not st:
                    vide += 1; continue
                [M.gamma_chaine(float(a), float(b), w2, g, st, eta_facteur=ef, M_facteur=4)["Gamma_c"] for ef in S["EF_CHAINE"]]; c1 += 1
                tb = S["tables_ordre2"](float(a), float(b), w2, g, st, M_facteur=4)
                rs = [S["gamma_chaine_ordre2"](tb, ef) for ef in S["EF_CHAINE"]]; c2 += 1
                fl.append(rs[2]["Gamma_flux"])
                if rs[2]["Gamma_flux"] > 1.33e-12: ec.append(abs(rs[2]["Gamma_c2"] / rs[2]["Gamma_flux"] - 1.0))
            except BaseException as x:
                exc += 1; print("   exception au site (%d,%d) : %s %s" % (a, b, type(x).__name__, str(x)[:80]))
    tot[0] += n; tot[1] += exc
    print("%s  %-7s %-4s %3d %6d %14d %12d %9d | %.1e %.1e | %.1e" % (pid, w2, fac, n, vide, c1, c2, exc, min(fl), max(fl), max(ec) if ec else 0.0), flush=True)
print("TOTAL : %d sites, %d exceptions" % tuple(tot))
