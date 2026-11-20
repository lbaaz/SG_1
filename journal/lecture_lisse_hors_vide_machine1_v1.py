# -*- coding: utf-8 -*-
# Lecture : R(x) = rho_2D(x) / (w0 rho_chaine(x)), au point sacrifie, 3 barreaux. Hors chaine, classe 3.
# Applique l'attendu (canon 5bb45d0c8081106f) et son rectificatif d'instrument (c0dc8b2732ba7065), ecrits avant.
# Usage : python3 -I lecture_lisse_hors_vide_machine1_v1.py <dossier des sorties> <sortie.json>
import sys, json, math
from fractions import Fraction
import numpy as np
D, SORTIE = sys.argv[1].rstrip("/"), sys.argv[2]
CH = json.load(open(D + "/lisse_chaine_v1.json")); X = CH["X"]
K_MIN, K_MAX, TAU = -3, 8, Fraction(1, 20)
def plateau(ser):                      # recopie de la routine deposee du lecteur (lecture_lecteur_gel_loi_machine1_v1.py, lignes 75 a 92)
    best = None
    for k0 in range(K_MIN, K_MAX - 3):
        v = [ser.get(k) for k in range(k0, k0 + 5)]
        if any(x is None for x in v): continue
        mx, mn = Fraction(max(v)), Fraction(min(v)); ok = mx <= (1 + TAU) * mn; cand = (not ok, mx / mn, k0)
        if best is None or cand < best[0]: best = (cand, v, ok)
    if best is None: return {"statut": "AUCUNE FENETRE"}
    (_, rapport, k0), v, ok = best
    return {"statut": "PLATEAU" if ok else "PAS DE PLATEAU", "k0": k0, "etalement": float(rapport) - 1.0, "val": math.exp(sum(math.log(x) for x in v) / 5.0)}
ABSN = ["A", "B", "C", "D"]; d2 = {}
for a in ABSN:
    d = {}
    for f in ("lisse_2d_%s_v1.json" % a, "lisse_2d_%s_bords_v1.json" % a): d.update(json.load(open("%s/%s" % (D, f)))["k"])
    d2[a] = {int(k): v for k, v in d.items()}
out = {"X": X, "par_x": [], "absorbeurs": {}}
# le vide : plateau de la largeur et poids, par absorbeur
print("LE VIDE, par absorbeur (routine de plateau deposee) :")
lnG3 = CH["ordres"]["3"]["ln_Gamma_vide"]; w0s = []
for a in ABSN:
    p = plateau({k: (v["gamma_vide"] if v["suivi"] else None) for k, v in d2[a].items()}); w = np.median([v["w0"] for v in d2[a].values() if v["suivi"]]); w0s.append(w)
    out["absorbeurs"][a] = {"plateau_vide": p, "w0": float(w)}
    print("  %s : %s, k0 = %d, etalement %.4f, Gamma %.5e ; ln(chaine ordre 3 / 2D) = %+.5f ; w0 = %.8f" % (a, p["statut"], p["k0"], p["etalement"], p["val"], lnG3 - math.log(p["val"]), w))
w0 = float(np.median(w0s)); out["w0"] = w0
# A0 tel qu'ecrit, puis la regle de remplacement
print("A0 TEL QU'ECRIT (k = 0 a 6, quatre absorbeurs) : etendue des ln rho_2D par ecart : %s"
      % "  ".join("%.3f" % (max(math.log(d2[a][k]["rho_flux"][i]) for a in ABSN for k in range(0, 7)) - min(math.log(d2[a][k]["rho_flux"][i]) for a in ABSN for k in range(0, 7))) for i in range(len(X))))
out["A0_tel_qu_ecrit"] = [max(math.log(d2[a][k]["rho_flux"][i]) for a in ABSN for k in range(0, 7)) - min(math.log(d2[a][k]["rho_flux"][i]) for a in ABSN for k in range(0, 7)) for i in range(len(X))]
print("REGLE DE REMPLACEMENT : plateau depose par absorbeur, mediane des quatre.")
print("   x     statuts  k0 (A B C D)   etalement max   etendue entre absorbeurs   ln rho_2D     R ordre 3   R ordre 2   R ordre 1   lisible")
R3 = []; lis = []
for i, x in enumerate(X):
    P = {a: plateau({k: (v["rho_flux"][i] if v["suivi"] else None) for k, v in d2[a].items()}) for a in ABSN}
    tous = all(P[a]["statut"] == "PLATEAU" for a in ABSN)
    lg = [math.log(P[a]["val"]) for a in ABSN]; med = float(np.median(lg)); et = max(lg) - min(lg)
    r = {o: math.exp(med - math.log(w0) - CH["ordres"][o]["ln_rho"][i]) for o in "321"}
    ok = tous and et <= 0.02; lis.append(ok); R3.append(r["3"])
    out["par_x"].append({"x": x, "plateaux": P, "ln_rho_2d": med, "etendue_absorbeurs": et, "R3": r["3"], "R2": r["2"], "R1": r["1"], "lisible": ok,
                         "etendue_chaine3": CH["ordres"]["3"]["etendue"][i]})
    print("  %5.2f  %s   %s   %.4f          %.4f                     %9.4f     %.4f      %.4f      %.4f      %s"
          % (x, "".join("P" if P[a]["statut"] == "PLATEAU" else "-" for a in ABSN), " ".join("%2d" % P[a]["k0"] for a in ABSN), max(P[a]["etalement"] for a in ABSN), et, med, r["3"], r["2"], r["1"], "oui" if ok else "NON"))
R3 = np.array(R3); xs = np.array(X)
moy = float(np.trapezoid(R3, xs) / (xs[-1] - xs[0])); pente = float(np.polyfit(xs, R3, 1)[0])
inc = max(max(p["etendue_absorbeurs"] for p in out["par_x"]), max(p["etendue_chaine3"] for p in out["par_x"]))
out["moyenne_fenetre"] = moy; out["pente"] = pente; out["R_max"] = float(R3.max()); out["R_min"] = float(R3.min()); out["incertitude_max"] = inc
print("R ordre 3 : de %.4f a %.4f sur la fenetre ; moyenne uniforme en x (trapezes) %.4f ; pente %+.5f par |delta| ; R(0.05) = %.4f ; R(8) = %.4f"
      % (R3.min(), R3.max(), moy, pente, R3[0], R3[-1]))
print("incertitude : etendue entre absorbeurs 2D au plus %.4f ; etendue entre les dix-huit variantes de la chaine au plus %.4f"
      % (max(p["etendue_absorbeurs"] for p in out["par_x"]), max(p["etendue_chaine3"] for p in out["par_x"])))
A1 = abs(R3[0] - 1) <= 0.01; A2 = (1.05 <= R3[-1] <= 1.25) and (1.01 <= moy <= 1.08) and all(np.diff(R3) > 0)
plat = all(abs(R3 - 1) <= 0.01)
issue = "(i)" if A2 else ("(ii)" if plat else "(iii)")
out["A0_remplace"] = bool(all(lis)); out["A1"] = bool(A1); out["A2"] = bool(A2); out["issue"] = issue
print("A0 (regle de remplacement) : %s ; A1 : %s ; A2 : %s ; ISSUE %s" % ("lisible a tous les ecarts" if all(lis) else "NON lisible a %s" % [x for x, l in zip(X, lis) if not l], "TIENT" if A1 else "NE TIENT PAS", "TIENT" if A2 else "NE TIENT PAS", issue))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True, default=float)
