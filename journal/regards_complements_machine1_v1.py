# Complements de machine 1 aux regards sur les niveaux des grandes boites (lot dce7431e7a8b4a8c). Hors chaine, classe 3, APRES lecture.
# (E) somme d'ensemble et pente de la somme avec l'ecart au vide, erreur par reechantillonnage des boites ; (F) critere de tendance de mes attendus v2 ;
# (G) cotes pairs contre impairs ; (H) densite de niveaux selon le cote ; (I) boites ou le vide est accroche.  Arguments : <sortie.json> <fichier.jsonl> ...
import sys, json, math
import numpy as np
sortie = sys.argv[1]; boites = {}
for f in sys.argv[2:]:
    for l in open(f, encoding="utf-8"):
        if l.strip():
            b = json.loads(l); boites[b["cote"]] = b
TR = {"200": (190, 209), "300": (297, 302), "400": (397, 402)}
L = 7.95; rng = np.random.default_rng(171117); out = {}
def niv(c):
    N = boites[c]["niveaux"]; return -np.array([x["off"] for x in N]), np.array([x["y1"] for x in N])
cs = sorted(boites)
# (E)
som = np.array([niv(c)[1].sum() / L for c in cs])
def pente(sel):
    X = []; Y = []
    for c in sel:
        o, y = niv(c)
        for a in range(8):
            lo = 0.05 if a == 0 else a; m = (o >= lo) & (o < a + 1); X.append((lo + a + 1) / 2); Y.append(y[m].sum() / (a + 1 - lo))
    return np.polyfit(X, Y, 1)
p = pente(cs); B = []; M = []
for t in range(4000):
    s = rng.choice(cs, len(cs)); q = pente(s); B.append(q); M.append(np.mean([niv(c)[1].sum() / L for c in s]))
B = np.array(B)
print("(E) 32 boites : somme / largeur moyenne %.3f +- %.3f (reechantillonnage %.3f) ; pente de la somme avec l'ecart au vide %+.4f +- %.4f par |delta| ; valeur extrapolee a l'ecart nul %.3f +- %.3f, a 8 |delta| %.3f +- %.3f"
      % (som.mean(), som.std(ddof=1) / math.sqrt(len(cs)), np.std(M), p[0], B[:, 0].std(), p[1], B[:, 1].std(), p[1] + 8 * p[0], (B[:, 1] + 8 * B[:, 0]).std()))
out["E"] = {"a_huit": float(p[1] + 8 * p[0]), "a_huit_erreur": float((B[:, 1] + 8 * B[:, 0]).std()), "somme": float(som.mean()), "erreur": float(som.std(ddof=1) / math.sqrt(len(cs))), "pente": float(p[0]), "pente_erreur": float(B[:, 0].std()), "a_zero": float(p[1]), "a_zero_erreur": float(B[:, 1].std())}
for nom, (a, b) in TR.items():
    s = np.array([niv(c)[1].sum() / L for c in cs if a <= c <= b]); print("     tranche %s : %.3f +- %.3f" % (nom, s.mean(), s.std(ddof=1) / math.sqrt(len(s))))
    out["E"]["tranche_" + nom] = [float(s.mean()), float(s.std(ddof=1) / math.sqrt(len(s)))]
# (F)
def R(sel):
    ns = np.array([len(niv(c)[0]) for c in sel]); ip = [(niv(c)[1] ** 2).sum() / niv(c)[1].sum() ** 2 for c in sel]
    return np.mean(ip) / np.mean(3.0 / (ns + 2.0)), ns
R3, n3 = R([c for c in cs if 297 <= c <= 302]); R4, n4 = R([c for c in cs if 397 <= c <= 402]); R2, n2 = R([c for c in cs if 190 <= c <= 209])
sim = []
for t in range(20000):
    a = np.mean([1 / ((y := rng.chisquare(1, n)).sum() ** 2 / (y ** 2).sum()) for n in n3]) / np.mean(3.0 / (n3 + 2.0))
    b = np.mean([1 / ((y := rng.chisquare(1, n)).sum() ** 2 / (y ** 2).sum()) for n in n4]) / np.mean(3.0 / (n4 + 2.0))
    sim.append(b / a)
sim = np.array(sim); bloque = (np.mean(n4 + 2.0) / np.mean(n3 + 2.0))
print("(F) critere de tendance : R(400) / R(300) = %.3f ; regime stationnaire de Porter-Thomas : %.3f +- %.3f (ecart %+.1f ecart type) ; participation bloquee : %.2f (ecart %+.1f)"
      % (R4 / R3, sim.mean(), sim.std(), (R4 / R3 - sim.mean()) / sim.std(), bloque, (R4 / R3 - bloque) / sim.std()))
for nom, Rr, nn in (("300", R3, n3), ("400", R4, n4)):
    rb = np.mean(nn + 2.0) / (3 * 5.31)
    print("     tranche %s : R = %.3f ; une participation bloquee a 5.31 aux memes comptes donnerait %.2f" % (nom, Rr, rb))
    out.setdefault("F_bloque", {})[nom] = float(rb)
out["F"] = {"rapport": float(R4 / R3), "stationnaire": [float(sim.mean()), float(sim.std())], "bloque": float(bloque)}
out["G"] = {}
# (G)
for nom, (a, b) in TR.items():
    for par, lab in ((0, "pairs"), (1, "impairs")):
        sel = [c for c in cs if a <= c <= b and c % 2 == par]; Rr, nn = R(sel)
        P = [niv(c)[1].sum() ** 2 / (niv(c)[1] ** 2).sum() for c in sel]
        out["G"][nom + "_" + lab] = {"boites": len(sel), "niveaux": float(nn.mean()), "participation": float(np.mean(P)), "R": float(Rr)}
        print("(G) tranche %s, cotes %-7s : %2d boites, niveaux %.2f, participation %.2f, R %.3f, somme %.3f" % (nom, lab, len(sel), nn.mean(), np.mean(P), Rr, np.mean([niv(c)[1].sum() / L for c in sel])))
# (H)
x = np.array(cs, float); n = np.array([len(niv(c)[0]) for c in cs], float)
q = np.polyfit(x, n, 1); q0 = (x * n).sum() / (x * x).sum()
print("(H) niveaux dans la fenetre selon le cote, 32 boites : droite %.2f + %.4f x cote ; droite par l'origine : %.4f x cote ; niveaux par |delta| et par quantum de cote : %.5f"
      % (q[1], q[0], q0, q0 / L))
print("     participation moyenne / compte moyen : 200 : %.3f ; 300 : %.3f ; 400 : %.3f (Porter-Thomas a ces comptes : %.3f, %.3f, %.3f ; parts egales : 1)"
      % tuple([np.mean([niv(c)[1].sum() ** 2 / (niv(c)[1] ** 2).sum() for c in cs if a <= c <= b]) / np.mean([len(niv(c)[0]) for c in cs if a <= c <= b]) for a, b in TR.values()]
              + [float(np.mean([np.mean([ (y := rng.chisquare(1, k)).sum() ** 2 / (y ** 2).sum() for _ in range(3000)]) for k in nn]) / nn.mean()) for nn in (n2, n3, n4)]))
out["H"] = {"pente_origine": float(q0), "par_delta_par_quantum": float(q0 / L), "droite": [float(q[1]), float(q[0])]}
# (I)
w = np.array([boites[c]["w0"] for c in cs]); med = np.median(w)
acc = [(c, float(med - boites[c]["w0"])) for c in cs if med - boites[c]["w0"] > 2e-6]
print("(I) poids du vide : mediane %.8f ; boites ou il manque plus de 2e-06 : %s" % (med, ["%d (%.1e)" % a for a in acc]))
out["I"] = {"mediane": float(med), "accroches": acc}
json.dump(out, open(sortie, "w"), indent=1, sort_keys=True)
