# Regards de machine 1 sur les niveaux des grandes boites de machine 2 (lot dce7431e7a8b4a8c). Hors chaine, classe 3.
# TOUT ce qui suit est venu APRES lecture des agregats : ce sont des regards, pas des epreuves.
# (A) regle de somme par tranche d'ecart au vide ; (B) densite de niveaux par tranche d'ecart ; (C) parts normalisees localement ;
# (D) dependance entre boites voisines.  Arguments : <sortie.json> <fichier.jsonl> ...
import sys, json, math
import numpy as np
sortie = sys.argv[1]; fichiers = sys.argv[2:]
boites = {}
for f in fichiers:
    for l in open(f, encoding="utf-8"):
        if l.strip():
            b = json.loads(l); boites[b["cote"]] = b
TR = {"200": (190, 209), "300": (297, 302), "400": (397, 402)}
BORDS = [0.05, 1, 2, 3, 4, 5, 6, 7, 8]
rng = np.random.default_rng(1117)
def niveaux(c):
    N = boites[c]["niveaux"]
    off = -np.array([x["off"] for x in N]); y = np.array([x["y1"] for x in N])
    o = np.argsort(off); return off[o], y[o]
out = {}
print("(A)(B) par tranche d'ecart au vide (en |delta|, du cote oppose a delta) : somme des y / largeur, et niveaux par unite d'ecart")
for nom, (a, b) in list(TR.items()) + [("toutes", (0, 10 ** 6))]:
    cs = [c for c in sorted(boites) if a <= c <= b]
    S = np.zeros((len(cs), len(BORDS) - 1)); C = np.zeros_like(S)
    for i, c in enumerate(cs):
        off, y = niveaux(c)
        for j in range(len(BORDS) - 1):
            m = (off >= BORDS[j]) & (off < BORDS[j + 1])
            S[i, j] = y[m].sum() / (BORDS[j + 1] - BORDS[j]); C[i, j] = m.sum() / (BORDS[j + 1] - BORDS[j])
    ligne_s = []; ligne_c = []
    for j in range(len(BORDS) - 1):
        ligne_s.append((S[:, j].mean(), S[:, j].std(ddof=1) / math.sqrt(len(cs)))); ligne_c.append((C[:, j].mean(), C[:, j].std(ddof=1) / math.sqrt(len(cs))))
    out["AB_" + nom] = {"bords": BORDS, "somme": ligne_s, "densite": ligne_c, "boites": len(cs)}
    print("  %-6s (%2d boites) somme  : %s" % (nom, len(cs), "  ".join("%.2f+-%.2f" % x for x in ligne_s)))
    print("  %-6s             niveaux: %s" % ("", "  ".join("%.2f+-%.2f" % x for x in ligne_c)))
    # pente de la densite et de la somme avec l'ecart (moindres carres sur les 8 tranches)
    x = np.array([(BORDS[j] + BORDS[j + 1]) / 2 for j in range(len(BORDS) - 1)])
    ps = np.polyfit(x, [v[0] for v in ligne_s], 1); pc = np.polyfit(x, [v[0] for v in ligne_c], 1)
    print("  %-6s             pente de la somme %.4f par |delta| ; densite : %.3f + %.3f x ecart ; rapport de densite entre 7.5 et 0.5 : %.2f"
          % ("", ps[0], pc[1], pc[0], (pc[1] + 7.5 * pc[0]) / (pc[1] + 0.5 * pc[0])))
    out["AB_" + nom]["pente_somme"] = float(ps[0]); out["AB_" + nom]["densite_droite"] = [float(pc[1]), float(pc[0])]

print("(C) parts normalisees LOCALEMENT : z = y x densite(ecart), densite = droite ajustee par tranche de cotes")
REP = {"Porter-Thomas": lambda n: rng.chisquare(1, n), "exponentielle": lambda n: rng.exponential(1.0, n)}
for nom, (a, b) in TR.items():
    cs = [c for c in sorted(boites) if a <= c <= b]; d0, d1 = out["AB_" + nom]["densite_droite"]
    Z = []; invp = []; ns = []; invp_brut = []
    for c in cs:
        off, y = niveaux(c); z = y * (d0 + d1 * off); Z.append(z)
        invp.append((z ** 2).sum() / z.sum() ** 2); invp_brut.append((y ** 2).sum() / y.sum() ** 2); ns.append(len(y))
    ns = np.array(ns); Zt = np.concatenate(Z)
    Rz = np.mean(invp) / np.mean(3.0 / (ns + 2.0)); Rb = np.mean(invp_brut) / np.mean(3.0 / (ns + 2.0))
    # reperes : memes n, memes ecarts, parts tirees puis MULTIPLIEES par l'espacement local 1/densite (ce que la regle de somme impose), lues des deux facons
    sim = {}
    for rep, tir in REP.items():
        rb = []; rz = []
        for t in range(4000):
            ib = []; iz = []
            for c in cs:
                off, y = niveaux(c); dens = d0 + d1 * off
                z = tir(len(off)); yy = z / dens
                ib.append((yy ** 2).sum() / yy.sum() ** 2); iz.append((z ** 2).sum() / z.sum() ** 2)
            rb.append(np.mean(ib) / np.mean(3.0 / (ns + 2.0))); rz.append(np.mean(iz) / np.mean(3.0 / (ns + 2.0)))
        sim[rep] = (float(np.mean(rb)), float(np.std(rb)), float(np.mean(rz)), float(np.std(rz)))
    q = {"moyenne": float(Zt.mean()), "variance_sur_moyenne2": float(Zt.var() / Zt.mean() ** 2), "mediane_sur_moyenne": float(np.median(Zt) / Zt.mean()),
         "sous_0.1": float((Zt / Zt.mean() < 0.1).mean()), "au_dessus_3": float((Zt / Zt.mean() > 3).mean())}
    out["C_" + nom] = {"R_brut": float(Rb), "R_local": float(Rz), "reperes": sim, "z": q, "niveaux": int(len(Zt))}
    print("  %s : R brut %.3f, R local %.3f ; z : moyenne %.3f, variance/moyenne^2 %.2f (PT 2, exp 1), mediane/moyenne %.3f (PT 0.455, exp 0.693), sous 0.1 : %.3f (0.248 ; 0.095), au-dessus de 3 : %.3f (0.083 ; 0.050)"
          % (nom, Rb, Rz, q["moyenne"], q["variance_sur_moyenne2"], q["mediane_sur_moyenne"], q["sous_0.1"], q["au_dessus_3"]))
    for rep, v in sim.items():
        print("       repere %-13s avec la densite non uniforme : R brut attendu %.3f +- %.3f ; R local attendu %.3f +- %.3f" % ((rep,) + v))

print("(D) boites voisines : sont-elles independantes ?")
for nom, (a, b) in TR.items():
    cs = [c for c in sorted(boites) if a <= c <= b]
    P = []; Sm = []
    for c in cs:
        off, y = niveaux(c); P.append(y.sum() ** 2 / (y ** 2).sum()); Sm.append(y.sum())
    P = np.array(P); Sm = np.array(Sm)
    def auto(v): v = v - v.mean(); return float((v[:-1] * v[1:]).sum() / (v ** 2).sum())
    # appariement : pour chaque niveau de la boite c, distance au plus proche niveau de la boite c+1, rapportee a l'espacement local ; meme chose a boite decalee de 2
    def proche(c1, c2):
        o1, y1 = niveaux(c1); o2, y2 = niveaux(c2); d = []; ry = []
        esp = (o1[-1] - o1[0]) / max(1, len(o1) - 1)
        for k, x in enumerate(o1):
            j = int(np.argmin(abs(o2 - x))); d.append(abs(o2[j] - x) / esp); ry.append((y1[k], y2[j]))
        return d, ry
    d1 = []; d2 = []; ry1 = []
    for c in cs:
        if c + 1 in boites and c + 1 <= b: d, ry = proche(c, c + 1); d1 += d; ry1 += ry
        if c + 2 in boites and c + 2 <= b: d, ry = proche(c, c + 2); d2 += d
    # repere : positions independantes uniformes -> distance au plus proche / espacement ~ exponentielle de moyenne 0.5
    ry1 = np.array(ry1); cor = float(np.corrcoef(np.log(ry1[:, 0] + 1e-30), np.log(ry1[:, 1] + 1e-30))[0, 1])
    out["D_" + nom] = {"auto_participation": auto(P), "auto_somme": auto(Sm), "distance_voisine_mediane": float(np.median(d1)), "distance_plus2_mediane": float(np.median(d2)) if d2 else None,
                       "correlation_log_y_apparies": cor}
    print("  %s : autocorrelation de rang 1 entre cotes consecutifs -- participation %+.2f, somme %+.2f (bruit attendu +-%.2f) ; distance au plus proche niveau de la boite voisine / espacement : mediane %.3f (cote +1), %s (cote +2) ; independance : 0.35 ; correlation des log y des niveaux apparies %+.2f"
          % (nom, auto(P), auto(Sm), 1 / math.sqrt(len(cs)), np.median(d1), ("%.3f" % np.median(d2)) if d2 else "-", cor))
json.dump(out, open(sortie, "w"), indent=1, sort_keys=True)
