# -*- coding: ascii -*-
"""L'emulation classe-t-elle PLATEAU / PAS DE PLATEAU comme la lecture 2D de la nuit bis ? (30 couples point, configuration)
Critere du gel bis : cinq k consecutifs, max / min <= 21/20, meilleure fenetre. Description apres coup.
Usage : python3 -I plateaux_emulation_machine1_v1.py <emulation.json>"""
import sys, json, math
D = json.load(open(sys.argv[1]))
ORDRE = ["39_20", "197_100", "99_50", "101_50", "203_100", "41_20"]
CFG = ["F1G20", "F1G30", "F2G20", "F3G20", "F1GT"]
def plateau(vals):
    best = None; tous = []
    for k0 in range(-5, 9):
        f = [vals[k] for k in range(k0, k0 + 5)]
        e = max(f) / min(f) - 1.0
        if e <= 0.05: tous.append(k0)
        if best is None or e < best[0]:
            best = (e, k0, math.exp(sum(math.log(x) for x in f) / 5.0))
    return best[0], best[1], best[2], tous
acc = {v: [0, 0, 0, 0] for v in ("o2b", "o2", "o1")}      # PL/PL, --/--, 2D PL emu --, 2D -- emu PL
for nom in ORDRE:
    p = D["points"][nom]; G = p["G_run"]
    for cfg in CFG:
        tr = p["cfg"][cfg]["traj"]
        b = plateau({k: tr[str(k)]["g2D"] / G for k in range(-5, 13)})
        s = "%-8s %-6s 2D : %s etal %.4f k0 %+d val %.4f fen %-16s" % (p["w2"], cfg, "PL" if b[0] <= 0.05 else "--", b[0], b[1], b[2], b[3])
        for v in ("o2b", "o2"):
            e = plateau({k: tr[str(k)][v] / G for k in range(-5, 13)})
            s += " | %s : %s etal %.4f k0 %+d val %.4f fen %-14s" % (v, "PL" if e[0] <= 0.05 else "--", e[0], e[1], e[2], e[3])
            i = (0 if e[0] <= 0.05 else 2) if b[0] <= 0.05 else (3 if e[0] <= 0.05 else 1)
            acc[v][i] += 1
        e = plateau({k: tr[str(k)]["o1"] / G for k in range(-5, 13)}); i = (0 if e[0] <= 0.05 else 2) if b[0] <= 0.05 else (3 if e[0] <= 0.05 else 1); acc["o1"][i] += 1
        print(s)
for v in acc:
    a = acc[v]; print("%s : accord %d sur 30 (PL/PL %d, --/-- %d) ; 2D PL et emulation -- : %d ; 2D -- et emulation PL : %d" % (v, a[0] + a[1], a[0], a[1], a[2], a[3]))
