# Rejeu par machine 1 des agregats de machine 2 sur ses fichiers niveau par niveau (lot dce7431e7a8b4a8c).
# Hors chaine, classe 3. Ne rejoue AUCUNE boite : relit les niveaux (ecart au vide, y lecture 1, y lecture 2, fiable).
# Arguments : <sortie.json> <fichier.jsonl> ...
import sys, json, math
import numpy as np
sortie = sys.argv[1]; fichiers = sys.argv[2:]
LARGEUR = 8.0 - 0.05
boites = {}
for f in fichiers:
    for l in open(f, encoding="utf-8"):
        l = l.strip()
        if not l: continue
        b = json.loads(l)
        assert b["cote"] not in boites, b["cote"]
        boites[b["cote"]] = b
print("boites lues : %d ; cles d'une boite : %s" % (len(boites), sorted(k for k in next(iter(boites.values())) if k != "niveaux")))
TRANCHES = [("200", 190, 209), ("300", 297, 302), ("400", 397, 402)]
rng = np.random.default_rng(20261117)
def part(y): return y.sum() ** 2 / (y ** 2).sum()
res = {}
for nom, a, b in TRANCHES:
    cs = [c for c in sorted(boites) if a <= c <= b]
    ns = []; sommes = []; parts = []; invp = []; nonf = 0; ecart12 = []; offs = []
    for c in cs:
        B = boites[c]; N = B["niveaux"]
        y1 = np.array([x["y1"] for x in N]); y2 = np.array([x["y2"] for x in N])
        off = np.array([x["off"] for x in N])
        assert len(N) == B["n"]
        nonf += sum(1 for x in N if not x["fiable"])
        for u, v in zip(y1, y2):
            if max(u, v) > 0: ecart12.append(abs(u - v) / max(u, v))
        ns.append(len(N)); sommes.append(y1.sum() / LARGEUR); parts.append(part(y1)); invp.append(1.0 / part(y1)); offs.append((off.min(), off.max()))
    ns = np.array(ns); R = np.mean(invp) / np.mean(3.0 / (ns + 2.0))
    # tirages : Porter-Thomas (khi-deux a un degre) et exponentielle, aux memes n
    T = 20000; Rpt = np.empty(T); Rex = np.empty(T)
    for t in range(T):
        ip = []; ie = []
        for n in ns:
            y = rng.chisquare(1, n); ip.append(1.0 / part(y))
            y = rng.exponential(1.0, n); ie.append(1.0 / part(y))
        Rpt[t] = np.mean(ip) / np.mean(3.0 / (ns + 2.0)); Rex[t] = np.mean(ie) / np.mean(3.0 / (ns + 2.0))
    res[nom] = {"cotes": cs, "n": ns.tolist(), "n_moyen": float(ns.mean()), "somme_moyenne": float(np.mean(sommes)), "somme_ecart_type": float(np.std(sommes, ddof=1)),
                "sommes": [float(x) for x in sommes], "participations": [float(x) for x in parts], "participation_moyenne": float(np.mean(parts)),
                "R": float(R), "R_PT": [float(Rpt.mean()), float(Rpt.std())], "R_exp": [float(Rex.mean()), float(Rex.std())],
                "non_fiables": nonf, "niveaux": int(ns.sum()), "ecart_lectures_max": float(max(ecart12)), "ecart_lectures_mediane": float(np.median(ecart12)),
                "off_min": float(min(o[0] for o in offs)), "off_max": float(max(o[1] for o in offs))}
    r = res[nom]
    print("tranche %s : %d boites (%d a %d) ; niveaux %d, par boite %.2f ; non fiables %d ; somme/largeur %.3f (ecart type %.3f) ; participation %.2f (min %.2f max %.2f)"
          % (nom, len(cs), cs[0], cs[-1], r["niveaux"], r["n_moyen"], nonf, r["somme_moyenne"], r["somme_ecart_type"], r["participation_moyenne"], min(parts), max(parts)))
    print("   R = %.3f ; Porter-Thomas aux memes n : %.3f +- %.3f ; exponentielle : %.3f +- %.3f ; ecart entre les deux lectures de y : mediane %.1e, max %.1e ; ecarts au vide de %.2f a %.2f"
          % (R, r["R_PT"][0], r["R_PT"][1], r["R_exp"][0], r["R_exp"][1], r["ecart_lectures_mediane"], r["ecart_lectures_max"], r["off_min"], r["off_max"]))
json.dump(res, open(sortie, "w"), indent=1, sort_keys=True)
