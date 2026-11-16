# -*- coding: ascii -*-
"""SUPERPOSITION Gamma / |delta| CONTRE Phi(kappa) -- machine 1, v1, 2026-11-16. Hors chaine, classe 3, APRES COUP.
Aucun calcul 2D : les largeurs de plateau sont LUES dans les pieces deposees (delta 99 pour les douze points du
delta 98, delta 100 pour les douze cellules tirees). Pour chaque etat juge et qualifie :
  kappa = t_0 / |delta| (saut du site de depart au w2 et au g de l'etat, element du moteur) ;
  Phi(kappa ; n1, n2) : fonction d'echelle de la limite delta -> 0 (phi_echelle_machine1_v1.py), SANS parametre ;
  r = ln( Gamma_pl / (|delta| Phi) ) : ce que la loi d'echelle seule laisse.
VARIANTE, essayee APRES avoir vu r (declaree comme telle) : la variable d'echelle prise sur le saut lointain plutot
que sur le saut du site de depart, kappa* = kappa (X_c(w2) / X_c(2)) (tau_0(2) / tau_0(w2)), soit lambda = g X_c(w2) /
(P |delta|) ; r* = ln( Gamma_pl / (|delta| Phi(kappa*)) ).
Usage : python3 -I superposition_machine1_v1.py <moteur> <phi_echelle.py> <verdict_ordre3 du delta 100>
        <ordre3_par_etat du delta 98> <etape1_etalon> <sortie.json>"""
import sys, math, json, importlib.util, statistics
from fractions import Fraction as F
MOTEUR, PHI, V100, O98, ETALON, SORTIE = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("phi_echelle", PHI); PH = importlib.util.module_from_spec(spec); spec.loader.exec_module(PH)
M = PH.charger(MOTEUR)
E_MAX, STAB_MAX = 0.7, 0.05

def kappa_de(n1, n2, w2, g):
    return abs((g / M.P) * M.X_saut_reel(M.P, M.CANAL[0], M.CANAL[1], float(n1), float(n2), w2)) / abs(float(w2) - 2.0)

etats = []
# --- delta 100 : douze cellules tirees ---
v = json.load(open(V100))
ecart_kappa = 0.0
for c in v["cellules"]:
    w2 = F(c["w2"]); d = float(w2) - 2.0
    for e in c["etats"]:
        if e["exclu"] is not None:
            continue
        k = kappa_de(e["n1"], e["n2"], w2, c["g"]); ecart_kappa = max(ecart_kappa, abs(k / e["kappa"] - 1.0))
        etats.append({"source": "delta100", "id": c["id"], "facteur": c["facteur"], "w2": c["w2"], "delta": d, "g": c["g"], "rang": e["rang"],
                      "n1": e["n1"], "n2": e["n2"], "kappa": k, "m_bord": e["m_bord"], "e_bord": e["e_bord"], "stab3": e["stab3"],
                      "domaine": bool(e["dans_le_domaine"]), "Gamma_pl": e["Gamma_pl"], "G2": e["G2"], "G3": e["G3"]})
n100 = len(etats)
# --- delta 98 : douze points, largeurs de plateau du gel ter ---
o = json.load(open(O98)); et = json.load(open(ETALON))
pl = {(x["id"], x["rang"]): x for x in et["etats"]}
for pid in sorted(o["points"]):
    p = o["points"][pid]; w2 = F(p["w2"]); d = float(w2) - 2.0
    for e in p["etats"]:
        x = pl[(pid, e["rang"])]
        if x["statut"] != "QUALIFIE":
            continue
        G3 = e["G_c3"]; var = [e["variantes"][kk] for kk in ("ef_double", "ef_demi", "recul_4")]
        stab = max(abs(math.log(y / G3)) for y in var) if G3 > 0.0 and all(y > 0.0 for y in var) else None
        eb = [b for b in e["barriere"] if b["m"] == e["m_bord"]][0]
        e_bord = abs(eb["e"])
        etats.append({"source": "delta98", "id": pid, "facteur": None, "w2": p["w2"], "delta": d, "g": p["g"], "rang": e["rang"],
                      "n1": e["n1"], "n2": e["n2"], "kappa": kappa_de(e["n1"], e["n2"], w2, p["g"]), "m_bord": e["m_bord"], "e_bord": e_bord, "stab3": stab,
                      "domaine": bool(G3 > 0.0 and e_bord < E_MAX and stab is not None and stab <= STAB_MAX), "Gamma_pl": x["G_pl"], "G2": e["G_c2"], "G3": G3})
n98 = len(etats) - n100
print("etats juges et qualifies : delta 100 %d, delta 98 %d ; dans le domaine : %d et %d" % (
    n100, n98, sum(1 for e in etats if e["source"] == "delta100" and e["domaine"]), sum(1 for e in etats if e["source"] == "delta98" and e["domaine"])))
print("controle : kappa recalcule contre le kappa de la feuille du delta 100, plus grand ecart relatif %.1e" % ecart_kappa)

# --- Phi a chaque etat ---
XC2 = M.coeff_homogene_X_s(F(2))
pire_arith, pire_stab, vides = 0.0, 0.0, 0
for e in etats:
    f = PH.phi_fc(e["kappa"], e["n1"], e["n2"])
    if f is None:
        e["ln_Phi"] = None; vides += 1; continue
    g = PH.phi_eig(e["kappa"], e["n1"], e["n2"])
    e["ln_Phi"] = f["ln_Phi"]; e["m_bord_limite"] = f["m_bord"]; e["Z"] = f["Z"]
    if g["Phi_flux"] > 1e-18:
        pire_arith = max(pire_arith, abs(f["ln_Phi"] - math.log(g["Phi_flux"])))
    var = [PH.phi_fc(e["kappa"], e["n1"], e["n2"], ef=2 * PH.EF)["ln_Phi"], PH.phi_fc(e["kappa"], e["n1"], e["n2"], ef=PH.EF / 2)["ln_Phi"],
           PH.phi_fc(e["kappa"], e["n1"], e["n2"], recul=4)["ln_Phi"]]
    e["stab_Phi"] = max(abs(x - f["ln_Phi"]) for x in var); pire_stab = max(pire_stab, e["stab_Phi"])
    e["ln_G_sur_delta"] = math.log(e["Gamma_pl"] / abs(e["delta"]))
    e["r"] = e["ln_G_sur_delta"] - e["ln_Phi"]
    e["r_sur_delta"] = e["r"] / e["delta"]
    e["r_chaine3"] = math.log(e["G3"] / abs(e["delta"])) - e["ln_Phi"] if e["G3"] > 0.0 else None
    w2e = F(e["w2"])
    e["rho"] = (M.coeff_homogene_X_s(w2e) / XC2) * (PH.tau(e["n1"], e["n2"], 0) / PH.tau(e["n1"], e["n2"], 0, w2e))
    fs = PH.phi_fc(e["kappa"] * e["rho"], e["n1"], e["n2"])
    e["ln_Phi_etoile"] = fs["ln_Phi"] if fs is not None else None
    e["r_etoile"] = (e["ln_G_sur_delta"] - fs["ln_Phi"]) if fs is not None else None
print("etats sans barriere a la limite (Phi non defini) : %d" % vides)
print("controle : fraction continue contre diagonalisation (flux), plus grand ecart sur ln Phi : %.1e" % pire_arith)
print("stabilite de Phi sous l'absorbeur de la chaine (double, moitie, recule de 4), plus grand ecart sur ln Phi : %.3f" % pire_stab)

D = [e for e in etats if e["domaine"] and e["ln_Phi"] is not None]
H = [e for e in etats if not e["domaine"] and e["ln_Phi"] is not None]
def med(x):
    return statistics.median(x)
ln10 = math.log(10.0)
print()
print("DANS LE DOMAINE : %d etats" % len(D))
lo, hi = min(e["ln_G_sur_delta"] for e in D), max(e["ln_G_sur_delta"] for e in D)
print("  Gamma_pl / |delta| va de %.3e a %.3e : %.2f decades" % (math.exp(lo), math.exp(hi), (hi - lo) / ln10))
print("  kappa va de %.4f a %.4f ; |delta| de %.3f a %.3f" % (min(e["kappa"] for e in D), max(e["kappa"] for e in D), min(abs(e["delta"]) for e in D), max(abs(e["delta"]) for e in D)))
ar = [abs(e["r"]) for e in D]
print("  |r| = |ln(Gamma_pl / (|delta| Phi))| : mediane %.3f, plus grand %.3f (facteur %.2f) ; stabilite de Phi mediane %.4f, pire %.4f" % (
    med(ar), max(ar), math.exp(max(ar)), med([e["stab_Phi"] for e in D]), max(e["stab_Phi"] for e in D)))
neg = [e for e in D if e["delta"] < 0]; pos = [e for e in D if e["delta"] > 0]
print("  signe de r : delta < 0, r > 0 a %d etats sur %d ; delta > 0, r < 0 a %d etats sur %d" % (
    sum(1 for e in neg if e["r"] > 0), len(neg), sum(1 for e in pos if e["r"] < 0), len(pos)))
# correlation entre ln(Gamma/|delta|) et ln Phi
xs = [e["ln_Phi"] for e in D]; ys = [e["ln_G_sur_delta"] for e in D]
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
sxx = sum((x - mx) ** 2 for x in xs); sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys)); syy = sum((y - my) ** 2 for y in ys)
pente = sxy / sxx
print("  droite ln(Gamma_pl / |delta|) = a + b ln Phi : b = %.4f, a = %+.3f, correlation %.6f, ecart-type restant %.3f" % (
    pente, my - pente * mx, sxy / math.sqrt(sxx * syy), math.sqrt(sum((y - my - pente * (x - mx)) ** 2 for x, y in zip(xs, ys)) / len(xs))))
print()
print("  par cellule ou point (domaine) :   delta    etats   kappa min ; max     m_bord    r : min ; mediane ; max        r / delta : min ; mediane ; max")
par = {}
for e in D:
    par.setdefault((e["source"], e["id"]), []).append(e)
resume = []
for cle in sorted(par, key=lambda c: (par[c][0]["delta"], c)):
    L = par[cle]; r = sorted(e["r"] for e in L); rd = sorted(e["r_sur_delta"] for e in L)
    print("  %-8s %-3s %-4s  %+.3f   %3d    %.4f ; %.4f   %2d-%2d    %+.3f ; %+.3f ; %+.3f      %+7.2f ; %+7.2f ; %+7.2f" % (
        cle[0], cle[1], L[0]["facteur"] or "", L[0]["delta"], len(L), min(e["kappa"] for e in L), max(e["kappa"] for e in L), min(e["m_bord"] for e in L), max(e["m_bord"] for e in L),
        r[0], med(r), r[-1], rd[0], med(rd), rd[-1]))
    resume.append({"source": cle[0], "id": cle[1], "facteur": L[0]["facteur"], "delta": L[0]["delta"], "etats": len(L), "r": [r[0], med(r), r[-1]], "r_sur_delta": [rd[0], med(rd), rd[-1]]})
print()
print("VARIANTE (variable prise sur le saut lointain, essayee apres avoir vu r) :")
ars = [abs(e["r_etoile"]) for e in D]
print("  |r*| : mediane %.3f, plus grand %.3f (facteur %.2f) ; kappa* / kappa - 1 va de %+.4f a %+.4f" % (
    med(ars), max(ars), math.exp(max(ars)), min(e["rho"] for e in D) - 1.0, max(e["rho"] for e in D) - 1.0))
print("  signe de r* : delta < 0, r* > 0 a %d etats sur %d ; delta > 0, r* < 0 a %d etats sur %d" % (
    sum(1 for e in neg if e["r_etoile"] > 0), len(neg), sum(1 for e in pos if e["r_etoile"] < 0), len(pos)))
et_k = {"neg": [], "pos": []}; et_l = {"neg": [], "pos": []}
print("  par cellule ou point :            delta    etats   r : etendue (max - min)    r* : min ; mediane ; max       r* : etendue")
for cle in sorted(par, key=lambda c: (par[c][0]["delta"], c)):
    L = par[cle]; r = sorted(e["r"] for e in L); rs_ = sorted(e["r_etoile"] for e in L)
    cote = "neg" if L[0]["delta"] < 0 else "pos"; et_k[cote].append(r[-1] - r[0]); et_l[cote].append(rs_[-1] - rs_[0])
    print("  %-8s %-3s %-4s  %+.3f   %3d        %.3f                 %+.3f ; %+.3f ; %+.3f         %.3f" % (
        cle[0], cle[1], L[0]["facteur"] or "", L[0]["delta"], len(L), r[-1] - r[0], rs_[0], med(rs_), rs_[-1], rs_[-1] - rs_[0]))
    for x in resume:
        if x["source"] == cle[0] and x["id"] == cle[1]:
            x["r_etoile"] = [rs_[0], med(rs_), rs_[-1]]
print("  etendue de r dans une cellule, mediane sur les cellules : delta < 0 : %.3f (kappa) contre %.3f (kappa*) ; delta > 0 : %.3f contre %.3f" % (
    med(et_k["neg"]), med(et_l["neg"]), med(et_k["pos"]), med(et_l["pos"])))
variante = {"r_abs_mediane": med(ars), "r_abs_max": max(ars), "etendue_mediane": {"neg_kappa": med(et_k["neg"]), "neg_etoile": med(et_l["neg"]), "pos_kappa": med(et_k["pos"]), "pos_etoile": med(et_l["pos"])}}
print()
print("HORS DU DOMAINE : %d etats ; |r| mediane %.3f, plus grand %.3f" % (len(H), med([abs(e["r"]) for e in H]) if H else float("nan"), max([abs(e["r"]) for e in H]) if H else float("nan")))
json.dump({"etats": etats, "resume": resume, "controles": {"ecart_kappa": ecart_kappa, "pire_arith": pire_arith, "pire_stab_Phi": pire_stab, "vides": vides},
           "domaine": {"n": len(D), "decades": (hi - lo) / ln10, "r_abs_mediane": med(ar), "r_abs_max": max(ar), "pente": pente,
                       "signes": [sum(1 for e in neg if e["r"] > 0), len(neg), sum(1 for e in pos if e["r"] < 0), len(pos)]},
           "variante": variante}, open(SORTIE, "w"), indent=1, sort_keys=True)
