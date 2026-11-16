# -*- coding: ascii -*-
"""Lecture de l'emulation : trajectoires en k de la lecture 2D (nuit bis) et de la chaine en boite, etat 0."""
import sys, json, math
D = json.load(open(sys.argv[1]))
ORDRE = ["39_20", "197_100", "99_50", "101_50", "203_100", "41_20"]
CFG = ["F1G20", "F1G30", "F2G20", "F3G20", "F1GT"]
KS = [str(k) for k in range(-5, 13)]
tous = {v: [] for v in ("o1", "o2", "o2b")}
for nom in ORDRE:
    p = D["points"][nom]; G = p["G_run"]
    print("=== %s etat %s  G_run %.4e  chaine longue / G_run : %.4f (eta 1/4) %.4f (eta 1/16)  m_bord %d" % (
        p["w2"], tuple(p["etat"]), G, p["longue"]["gamma_025"] / G, p["longue"]["gamma_00625"] / G, p["longue"]["m_bord"]))
    for cfg in CFG:
        c = p["cfg"][cfg]
        print("  %s (N %d, r_c %d)  m_max %d" % (cfg, c["N"], c["r_c"], c["traj"]["3"]["m_max"]))
        print("    k   : " + " ".join("%6s" % k for k in KS))
        print("    2D  : " + " ".join("%6.3f" % (c["traj"][k]["g2D"] / G) if c["traj"][k]["g2D"] else "   -- " for k in KS))
        for v in ("o2b", "o2", "o1"):
            print("    %-4s: " % v + " ".join("%6.3f" % (c["traj"][k][v] / G) for k in KS))
        for v in ("o2b", "o2", "o1"):
            r = [c["traj"][k][v] / c["traj"][k]["g2D"] for k in KS if c["traj"][k]["g2D"]]
            tous[v] += [(nom, cfg, k, c["traj"][k][v] / c["traj"][k]["g2D"]) for k in KS if c["traj"][k]["g2D"]]
            print("    %-4s/2D : " % v + " ".join("%6.3f" % x for x in r))
print()
for v in ("o2b", "o2", "o1"):
    for nomplage, plage in (("k -5..12", range(-5, 13)), ("k -5..4", range(-5, 5)), ("k -5..-1", range(-5, 0)), ("k 0..3", range(0, 4)), ("k 5..12", range(5, 13))):
        xs = sorted(x[3] for x in tous[v] if int(x[2]) in plage)
        n = len(xs)
        print("%-4s %-9s n=%3d  min %.3f  q10 %.3f  med %.3f  q90 %.3f  max %.3f" % (v, nomplage, n, xs[0], xs[n // 10], xs[n // 2], xs[(9 * n) // 10], xs[-1]))
