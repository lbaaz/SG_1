# -*- coding: ascii -*-
"""Lecture corrigee (apres coup, description) : Gamma_2D(k, cfg) / Gamma_emul(k, cfg), etat 0, six points de M17.
Si la chaine en boite rend la dependance a l'absorbeur, ce rapport est constant en k et en configuration.
Critere de plateau du gel bis repris comme REGLE DE DESCRIPTION : cinq k consecutifs, max / min <= 21/20.
Usage : python3 -I lecture_corrigee_machine1_v1.py <emulation.json> [variante]"""
import sys, json, math
D = json.load(open(sys.argv[1])); VAR = sys.argv[2] if len(sys.argv) > 2 else "o2b"
ORDRE = ["39_20", "197_100", "99_50", "101_50", "203_100", "41_20"]
CFG = ["F1G20", "F1G30", "F2G20", "F3G20", "F1GT"]
KS = list(range(-5, 13))
INTR = {"39_20": 1.0709, "197_100": 1.0236, "99_50": 1.0107, "101_50": 1.0188, "203_100": 1.0228, "41_20": 1.0409}  # chaine sans boite / G_run

def plateau(vals):          # vals : {k: valeur} ; rend (meilleur etalement, k0, moyenne geometrique, liste des k0 a plateau)
    best = None; tous = []
    for k0 in range(-5, 9):
        f = [vals[k] for k in range(k0, k0 + 5)]
        e = max(f) / min(f) - 1.0
        if e <= 0.05:
            tous.append(k0)
        if best is None or e < best[0]:
            best = (e, k0, math.exp(sum(math.log(x) for x in f) / 5.0))
    return best[0], best[1], best[2], tous

nb = {"brut": {c: 0 for c in CFG}, "corr": {c: 0 for c in CFG}}
print("variante", VAR)
for nom in ORDRE:
    p = D["points"][nom]; G = p["G_run"]
    print("=== %s" % p["w2"])
    lignes = []
    for cfg in CFG:
        tr = p["cfg"][cfg]["traj"]
        brut = {k: tr[str(k)]["g2D"] / G for k in KS}
        corr = {k: tr[str(k)]["g2D"] / tr[str(k)][VAR] for k in KS}          # 2D / emulation
        eb, kb, gb, tb = plateau(brut); ec, kc, gc, tc = plateau(corr)
        nb["brut"][cfg] += eb <= 0.05; nb["corr"][cfg] += ec <= 0.05
        print("  %-6s brut : %s etal %.4f k0 %+d val %.4f | 2D/emul : %s etal %.4f k0 %+d val %.4f fenetres %s" % (
            cfg, "PL" if eb <= 0.05 else "--", eb, kb, gb, "PL" if ec <= 0.05 else "--", ec, kc, gc, tc))
        print("         2D/emul, k=-5..4 : " + " ".join("%.3f" % corr[k] for k in range(-5, 5)))
        lignes.append((cfg, ec, gc, corr))
    # accord entre configurations sur k = -1..2 (zone ou G20 et G30 coincident et avant les bosses)
    for (ka, kb_) in ((-2, 2), (-1, 2), (0, 2), (0, 3)):
        v = [l[3][k] for l in lignes for k in range(ka, kb_ + 1)]
        print("  toutes configurations, k = %+d..%+d : 2D/emul de %.4f a %.4f, etalement %.4f, moyenne geo %.4f ; brut : etalement %.4f" % (
            ka, kb_, min(v), max(v), max(v) / min(v) - 1.0, math.exp(sum(math.log(x) for x in v) / len(v)),
            max(p["cfg"][c]["traj"][str(k)]["g2D"] for c in CFG for k in range(ka, kb_ + 1)) / min(p["cfg"][c]["traj"][str(k)]["g2D"] for c in CFG for k in range(ka, kb_ + 1)) - 1.0))
print()
print("PLATEAUX (cinq k consecutifs a 0.05) sur six points : brut", nb["brut"], "; 2D/emul", nb["corr"])
