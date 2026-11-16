# -*- coding: ascii -*-
"""Lecture de l'exploration des absorbeurs longs (hors chaine, classe 3, apres coup) : plateaux et accords.
PLATEAU(tol) : cinq k consecutifs, max / min <= 1 + tol. On rend, par configuration : la plus longue suite de k
consecutifs tenant dans tol, sa moyenne geometrique rapportee a G_run (lecture de M17 a k = 3, F1, L = 20).
Usage : python3 -I lecture_exploration_machine1_v1.py <exploration.json> [<exploration.json> ...]"""
import sys, json, math
P = {}
for f in sys.argv[1:]:
    P.update(json.load(open(f))["points"])
ORDRE = [n for n in ["39_20", "197_100", "99_50", "101_50", "203_100", "41_20"] if n in P]
INTR = {"39_20": 1.0709, "197_100": 1.0236, "99_50": 1.0107, "101_50": 1.0188, "203_100": 1.0228, "41_20": 1.0409}
KS = list(range(-5, 15))
def plus_longue(vals, tol):
    best = (0, None, None)
    for i in range(len(KS)):
        for j in range(i, len(KS)):
            f = [vals[k] for k in KS[i:j + 1]]
            if max(f) / min(f) - 1.0 <= tol:
                if j - i + 1 > best[0]:
                    best = (j - i + 1, KS[i], math.exp(sum(math.log(x) for x in f) / len(f)))
            else:
                break
    return best
RETENUES = ["F2_r+0_L60", "F2_r+0_L80", "F1_r+0_L80", "F3_r+0_L60", "F1_r+10_L60"]
bilan = {}
for nom in ORDRE:
    p = P[nom]; G = p["G_run"]
    print("=== %s  (G_run %.4e)" % (p["w2"], G))
    for cle in sorted(p["cfg"], key=lambda c: (p["cfg"][c]["forme"], p["cfg"][c]["r_c"], p["cfg"][c]["L"])):
        c = p["cfg"][cle]; v = {k: c["traj"][str(k)]["gamma"] / G for k in KS}
        a = plus_longue(v, 0.05); b = plus_longue(v, 0.02); d = plus_longue(v, 0.005)
        print("  %-12s N %3d | a 5 %% : %2d barreaux des k=%+d, val %.4f | a 2 %% : %2d des k=%+d, val %.4f | a 0.5 %% : %2d des k=%+d, val %.4f" % (
            cle, c["N"], a[0], a[1], a[2], b[0], b[1], b[2], d[0], d[1], d[2]))
        if cle in RETENUES:
            bilan.setdefault(nom, {})[cle] = d
    vals = [bilan[nom][c][2] for c in RETENUES if c in bilan[nom] and bilan[nom][c][0] >= 5]
    if vals:
        m = math.exp(sum(math.log(x) for x in vals) / len(vals))
        print("  -> plateaux a 0.5 %% de cinq barreaux au moins : %d sur %d configurations retenues ; valeurs de %.4f a %.4f (etalement %.4f) ; moyenne %.4f" % (
            len(vals), len([c for c in RETENUES if c in bilan[nom]]), min(vals), max(vals), max(vals) / min(vals) - 1.0, m))
        print("  -> lecture de M17 / plateau : %.4f ; chaine d'ordre 2 sans boite / plateau : %.4f" % (1.0 / m, INTR[nom] / m))
