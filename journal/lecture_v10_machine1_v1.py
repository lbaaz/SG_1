#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LECTURE DU GEL constante A v10 -- machine 1, v1, 29/09/2026 (v9 4144c0086a3a99e7 + la prediction (c) : c1 LIBRE
aux 18 points ; deux leviers : levier_a = delta'_91 / delta'_run pour (a), levier_b = delta'_base / delta'_run
pour (b) ; la MESURE de A rendue par degre). Deposee AVEC le gel, AVANT le run.

Joue, sur les series qu'un run de l'instrument v14 depose (repertoire en argument), ce que le
gel v8 (section 5bis) pre-enregistre :
  1. l'ORDRE MESURE q par point sur les trois niveaux dt_2b, dt_2b/2, dt_2b/4 (cles plan,
     G_dt, G_dt4 du JSON) et Richardson lnA_R = lnA(dt/4) + (lnA(dt/4) - lnA(dt/2)) / (2^q - 1),
     pour l'ajustement II (sans c1) ET pour M1/M2 ; q hors [3, 5] -> point NON LU ;
  2. les modeles par degre, ecrits avant : M1 (c1 fixe) a p = 4, 5 ; M2 (c1 fixe + mode libre a
     b = alpha + 3/2 et w derives) a p = 7, avec M2- (w/2) et M2+ (2w) en tests negatifs ;
     S(p) = max - min des six lnA_R d'un degre est la tolerance d'instrument, mesuree ici ;
  3. la PREDICTION (a) : obs_R lu sur l'ajustement II sans c1, contre pred(p) = biais_91(p) x
     levier, levier = delta'_91 / delta'_run ; TIENT au degre si obs_R/pred dans [0.8, 1.2] aux
     six points ET |obs_R - pred| <= 3 S(p) ;
  4. la PREDICTION (b) a p = 7 : les coefficients (a, c) de M2 apres Richardson, contre la base
     du 91 transportee par amplitude x levier^(b/2) et phase - w ln sqrt(levier) ; TIENT au
     point si amplitude a 20 pour cent et phase a 0.3 rad ; le compte des six est rendu.
Mode --base : sur un run a DEUX niveaux (le 91), ecrit la base (a, c, amplitude, phase) a p = 7
apres Richardson a q = 4 suppose ; c'est la piece que le gel v8 tape par construction.
Les coefficients c1, b, w viennent de la derivation b70fca94d72822ad (JSON en argument) ;
`ajuster_point_fixe`, `fenetre_de`, `_minimiser_1d`, `tau_cap`, `tau_dom` viennent de
l'instrument (chemin en argument). Deux verbes : chk (mord) et note (ne mord pas). Rien n'est
edite ; sorties ecrites avant le bilan.
Usage : lecture_v10_machine1_v1.py <run_dir> <instrument.py> <derivation.json> <sortie.json> [--base | --predictions <base.json> <levier_a> <levier_b>]
"""
import hashlib, importlib.util, json, math, os, sys, unicodedata
from fractions import Fraction
import numpy as np

RUN, INSTR, DERIV, SORTIE = sys.argv[1:5]
MODE = sys.argv[5] if len(sys.argv) > 5 else '--lecture'
BASE = sys.argv[6] if len(sys.argv) > 6 else None
LEVIER = float(eval(sys.argv[7])) if len(sys.argv) > 7 else None          # levier_a : (a)
LEVIER_B = float(eval(sys.argv[8])) if len(sys.argv) > 8 else LEVIER   # levier_b : (b)
DEGRES, W2S, CS = (4, 5, 7), ("1.73", "2.27", "2.80"), ("1.05", "1.20")
G, K = 0.05, {4: 120.0, 5: 3640 / 81, 7: 9576 / 625}
lignes, bilan, out_j = [], {"chk": 0, "mord": []}, {}


def out(s=""):
    print(s); lignes.append(s)


def chk(nom, cond, detail=""):
    bilan["chk"] += 1
    if not cond:
        bilan["mord"].append(nom)
    out("  [chk %s] %s%s" % ("PASSE" if cond else "MORD ", nom, (" -- " + detail) if detail else ""))
    return bool(cond)


def note(nom, detail):
    out("  [note] %s -- %s" % (nom, detail))


def B(ch):
    t = open(ch, encoding="utf-8", newline="").read()
    return hashlib.sha256(unicodedata.normalize("NFC", t.replace("\r\n", "\n")).encode()).hexdigest()[:16]


out("LECTURE v8 -- machine 1 -- mode %s -- run %s" % (MODE, RUN))
out("python %s ; numpy %s" % (sys.version.split()[0], np.__version__))
chk("derivation du second ordre a son empreinte", B(DERIV) == "b70fca94d72822ad", B(DERIV))
note("instrument", "%s %s" % (os.path.basename(INSTR), B(INSTR)))
spec = importlib.util.spec_from_file_location("banc", INSTR)
banc = importlib.util.module_from_spec(spec); spec.loader.exec_module(banc)
der = json.load(open(DERIV, encoding="utf-8"))
run = json.load(open(os.path.join(RUN, "resultats_alpha.json"), encoding="utf-8"))
note("run", "resultats_alpha.json convention B %s ; verdict %s" % (B(os.path.join(RUN, "resultats_alpha.json")), run.get("verdict", "?")[:60]))
MODES = {p: (float(Fraction(4, p - 2) + Fraction(3, 2)), der["C3"][str(p)]["im_complexe"]) for p in DEGRES}
NIVEAUX = [("plan", "dt2_k2", 1), ("G_dt", "dt2s2_k2", 2)] + ([("G_dt4", "dt2s4_k2", 4)] if "G_dt4" in run else [])
if MODE == "--base":
    note("niveaux de pas", "%d niveau(x) ; q SUPPOSE = 4 (mode base, declare)" % len(NIVEAUX))
else:
    chk("trois niveaux de pas presents (dt, dt/2, dt/4)", len(NIVEAUX) == 3, "%d niveau(x) ; q %s" % (len(NIVEAUX), "MESURE" if len(NIVEAUX) == 3 else "SUPPOSE"))


def lire_serie(nom):
    m = np.loadtxt(os.path.join(RUN, nom), comments="#")
    return m[:, 0], m[:, 1] + m[:, 2]


def ajuster(tt, yy, alpha, c1, td, lo, hi, mode):
    def systeme(ts):
        tau = ts - tt
        u = yy + alpha * np.log(tau) - c1 * tau ** 2
        if mode is None:
            return u, None
        b, w = mode
        s = tau / td
        return u, np.column_stack([np.ones_like(s), s ** b * np.cos(w * np.log(s)), s ** b * np.sin(w * np.log(s))])

    def SS(ts):
        u, X = systeme(ts)
        if X is None:
            return float(((u - u.mean()) ** 2).sum())
        return float(((u - X @ np.linalg.lstsq(X, u, rcond=None)[0]) ** 2).sum())

    ts, ss = banc._minimiser_1d(SS, lo, hi)
    u, X = systeme(ts)
    if X is None:
        return {"lnA": float(u.mean()), "t_star": ts, "SS": ss, "cond": 1.0, "rang": 1, "a": 0.0, "c": 0.0}
    coef, _, rang, _ = np.linalg.lstsq(X, u, rcond=None)
    return {"lnA": float(coef[0]), "t_star": ts, "SS": ss, "cond": float(np.linalg.cond(X / np.linalg.norm(X, axis=0))),
            "rang": int(rang), "a": float(coef[1]), "c": float(coef[2])}


def richardson(v1, v2, v4):
    """v1 a dt, v2 a dt/2, v4 a dt/4 (None si absent) : ordre mesure et extrapolation."""
    if v4 is None:
        return 4.0, v2 + (v2 - v1) / 15.0, "q suppose"
    d1, d2 = v1 - v2, v2 - v4
    if d2 == 0 or d1 / d2 <= 0:
        return float("nan"), float("nan"), "q non mesurable"
    q = math.log2(d1 / d2)
    return q, v4 + (v4 - v2) / (2 ** q - 1), "q mesure"


out(); out("1. AJUSTEMENTS PAR POINT ET PAR NIVEAU")
R = {}
for p in DEGRES:
    alpha, (b, w) = float(Fraction(4, p - 2)), MODES[p]
    for w2 in W2S:
        c1 = der["C2"]["%d|%s" % (p, w2)]["c1_float"]
        tc, td = banc.tau_cap(float(w2)), banc.tau_dom(float(w2))
        for c in CS:
            cle = "%d|%s|%s" % (p, w2, c)
            R[cle] = {}
            for cell, suff, fac in NIVEAUX:
                ent = run[cell][cle]
                nom = "alpha_serie_p%d_w%s_c%s_%s.txt" % (p, w2, c, suff)
                if ent.get("serie_fichier") != nom or not os.path.exists(os.path.join(RUN, nom)):
                    note("NON LU %s %s" % (cle, cell), "serie absente ou renommee : %s" % ent.get("serie_fichier"))
                    continue
                t, x = lire_serie(nom)
                ref = banc.ajuster_point_fixe(t, x, float(w2), p, ent["dt2"])
                chk("C0 %s %s : lnA_II rejoue = JSON a 1e-12" % (cle, cell), abs(ref["lnA_II"] - ent["ajustement"]["lnA_II"]) <= 1e-12,
                    "%.2e" % abs(ref["lnA_II"] - ent["ajustement"]["lnA_II"]))
                ok = np.isfinite(x) & (x != 0)
                t, y = t[ok], np.log(np.abs(x[ok]))
                fen = banc.fenetre_de(t, ref["t_star"], tc, td, 1e-6 * ent["dt2"])
                tt, yy = t[fen], y[fen]
                lo, hi = float(tt[-1]) * (1 + 1e-12) + 1e-12 * tc, float(t[-1]) + 2 * td
                R[cle][cell] = {"lnA_II": ref["lnA_II"],
                                "M1": ajuster(tt, yy, alpha, c1, td, lo, hi, None),
                                "M2": ajuster(tt, yy, alpha, c1, td, lo, hi, (b, w)),
                                "M2-": ajuster(tt, yy, alpha, c1, td, lo, hi, (b, w / 2)),
                                "M2+": ajuster(tt, yy, alpha, c1, td, lo, hi, (b, 2 * w))}
                chk("C0c %s %s : M2 de rang 3" % (cle, cell), R[cle][cell]["M2"]["rang"] == 3, "cond %.2f" % R[cle][cell]["M2"]["cond"])

out(); out("2. ORDRE MESURE ET RICHARDSON, PAR POINT ; S(p) PAR MODELE")
S, LR, Q = {}, {}, {}
for p in DEGRES:
    lnAK = math.log(K[p] / G) / (p - 2)
    for mod in ("II", "M1", "M2", "M2-", "M2+"):
        vals = []
        for w2 in W2S:
            for c in CS:
                cle = "%d|%s|%s" % (p, w2, c)
                if not all(cell in R[cle] for cell, _, _ in NIVEAUX):
                    continue
                g_ = lambda cell: R[cle][cell]["lnA_II"] if mod == "II" else R[cle][cell][mod]["lnA"]
                v1, v2 = g_("plan"), g_("G_dt")
                v4 = g_("G_dt4") if len(NIVEAUX) == 3 else None
                q, lr, etat = richardson(v1, v2, v4)
                if mod == "II":
                    Q[cle] = q
                    if math.isnan(q) or not (3.0 <= q <= 5.0) and etat == "q mesure":
                        note("NON LU %s (II)" % cle, "q = %s hors [3, 5]" % ("%.3f" % q if not math.isnan(q) else "nan"))
                        LR.setdefault(mod, {})[cle] = float("nan"); continue
                LR.setdefault(mod, {})[cle] = lr
                vals.append(lr)
                if mod == "II":
                    note("%s II" % cle, "lnA dt %.10f dt/2 %.10f%s ; q %s ; lnA_R %.10f ; obs_R %+.4e" % (
                        v1, v2, (" dt/4 %.10f" % v4) if v4 is not None else "", ("%.3f" % q) if not math.isnan(q) else "nan", lr, lr - lnAK))
        S.setdefault(str(p), {})[mod] = (max(vals) - min(vals)) if len(vals) >= 2 else float("nan")
    out("   p = %d : S_II %.3e  S_M1 %.3e  S_M2 %.3e  S_M2- %.3e  S_M2+ %.3e" % (p, S[str(p)]["II"], S[str(p)]["M1"], S[str(p)]["M2"], S[str(p)]["M2-"], S[str(p)]["M2+"]))
chk("p = 7 : M2 gagne sur M1 d'un facteur >= 3 sur S", S["7"]["M2"] <= S["7"]["M1"] / 3, "%.3e / %.3e" % (S["7"]["M2"], S["7"]["M1"]))
chk("p = 7 : les frequences fausses ne gagnent pas (S > S_M1/3)", S["7"]["M2-"] > S["7"]["M1"] / 3 and S["7"]["M2+"] > S["7"]["M1"] / 3, "%.3e %.3e" % (S["7"]["M2-"], S["7"]["M2+"]))
out_j["S"], out_j["q"], out_j["lnA_R"] = S, Q, LR

# --- (a, c) de M2 apres Richardson, p = 7
out(); out("3. MODES LIBRES A p = 7 : (a, c) DE M2 APRES RICHARDSON")
AC = {}
for w2 in W2S:
    for c in CS:
        cle = "7|%s|%s" % (w2, c)
        if not all(cell in R[cle] for cell, _, _ in NIVEAUX):
            continue
        comp = {}
        for coef in ("a", "c"):
            v1, v2 = R[cle]["plan"]["M2"][coef], R[cle]["G_dt"]["M2"][coef]
            v4 = R[cle]["G_dt4"]["M2"][coef] if len(NIVEAUX) == 3 else None
            q, vr, etat = richardson(v1, v2, v4)
            if etat == "q mesure" and not (2.0 <= q <= 6.0):
                comp = None; note("NON LU %s (b)" % cle, "q(%s) = %.3f hors [2, 6]" % (coef, q)); break
            comp[coef] = vr if not math.isnan(vr) else float("nan")
        if comp is None:
            continue
        amp, ph = math.hypot(comp["a"], comp["c"]), math.atan2(comp["c"], comp["a"])
        AC[cle] = {"a": comp["a"], "c": comp["c"], "amplitude": amp, "phase": ph,
                   "amp_dt": math.hypot(R[cle]["plan"]["M2"]["a"], R[cle]["plan"]["M2"]["c"]),
                   "amp_dt2": math.hypot(R[cle]["G_dt"]["M2"]["a"], R[cle]["G_dt"]["M2"]["c"])}
        note(cle, "a %+.6e c %+.6e | amplitude %.6e phase %+.4f rad | amp dt %.3e dt/2 %.3e" % (comp["a"], comp["c"], amp, ph, AC[cle]["amp_dt"], AC[cle]["amp_dt2"]))
out_j["modes_p7"] = AC

if MODE == "--predictions" and BASE and LEVIER:
    out(); out("4. PREDICTION (a) -- BIAIS DU PREMIER ORDRE x LEVIER %.4f, SUR L'AJUSTEMENT II" % LEVIER)
    ver = {}
    for p in DEGRES:
        lnAK = math.log(K[p] / G) / (p - 2)
        ratios, ecarts = [], []
        for w2 in W2S:
            pred = der["C4"]["%d|%s" % (p, w2)]["0.0"]["biais_lnA"] * LEVIER   # R-v8-4 : re-derive, par (p, w2)
            for c in CS:
                cle = "%d|%s|%s" % (p, w2, c)
                lr = LR["II"].get(cle, float("nan"))
                if math.isnan(lr):
                    continue
                obs = lr - lnAK
                ratios.append(obs / pred); ecarts.append(abs(obs - pred))
                note("%s" % cle, "obs_R %+.4e pred %+.4e obs/pred %.4f" % (obs, pred, obs / pred))
        tient = len(ratios) == 6 and all(0.8 <= r_ <= 1.2 for r_ in ratios) and all(e_ <= 3 * S[str(p)]["II"] for e_ in ecarts)
        ver[p] = "TIENT" if tient else ("NON LU" if len(ratios) < 6 else "NON")
        chk("(a) p = %d : obs_R/pred dans [0.8, 1.2] aux six ET |obs_R - pred| <= 3 S(p)" % p, tient,
            "%s ; ratios %s ; 3S %.2e" % (ver[p], " ".join("%.3f" % r_ for r_ in ratios), 3 * S[str(p)]["II"]))
    out_j["prediction_a"] = ver
    out(); out("5. PREDICTION (b) -- TRANSPORT DES MODES LIBRES A p = 7 (base %s)" % os.path.basename(BASE))
    base = json.load(open(BASE, encoding="utf-8"))["modes_p7"]
    b7, w7 = MODES[7]
    fa, dph = LEVIER_B ** (b7 / 2), -w7 * math.log(math.sqrt(LEVIER_B))
    tenus = 0
    for cle in sorted(AC):
        if cle not in base:
            continue
        amp_att, ph_att = base[cle]["amplitude"] * fa, base[cle]["phase"] + dph
        ph_att = (ph_att + math.pi) % (2 * math.pi) - math.pi
        dph_obs = (AC[cle]["phase"] - ph_att + math.pi) % (2 * math.pi) - math.pi
        ok = abs(AC[cle]["amplitude"] / amp_att - 1) <= 0.20 and abs(dph_obs) <= 0.3
        tenus += ok
        chk("(b) %s : amplitude a 20 pour cent et phase a 0.3 rad de la base transportee" % cle, ok,
            "amp %.3e attendu %.3e (%.3f) ; phase %+.3f attendu %+.3f (%+.3f rad)" % (AC[cle]["amplitude"], amp_att, AC[cle]["amplitude"] / amp_att, AC[cle]["phase"], ph_att, dph_obs))
    out("   (b) : %d des six points tiennent" % tenus)
    out_j["prediction_b"] = {"tenus": tenus, "facteur_amplitude": fa, "decalage_phase": dph, "levier_b": LEVIER_B}
    out(); out("6. PREDICTION (c) -- LE TERME tau^2 AJUSTE LIBREMENT VAUT c1 DERIVE (18 points, 10 pour cent)")
    C = {}
    for p in DEGRES:
        for w2 in W2S:
            c1d = der["C2"]["%d|%s" % (p, w2)]["c1_float"]
            for c in CS:
                cle = "%d|%s|%s" % (p, w2, c)
                cells = [run[cell].get(cle, {}).get("ajustement_c1_libre") for cell, _, _ in NIVEAUX]
                if len(cells) < 3 or any(not isinstance(x, dict) or x.get("statut") != "AJUSTE" for x in cells):
                    note("NON JOUE %s (c)" % cle, "ajustement_c1_libre absent ou non ajuste (instrument sans (c) ?)")
                    C[cle] = {"etat": "NON JOUE"}; continue
                v1, v2, v4 = (x["c1_fit"] for x in cells)
                q, cr, etat = richardson(v1, v2, v4)
                if etat == "q mesure" and not (3.0 <= q <= 5.0) or math.isnan(cr):
                    note("NON LU %s (c)" % cle, "q(c1) = %s hors [3, 5]" % ("%.3f" % q if not math.isnan(q) else "nan"))
                    C[cle] = {"etat": "NON LU", "q": q}; continue
                r_ = cr / c1d
                ok = 0.9 <= r_ <= 1.1
                C[cle] = {"etat": "TIENT" if ok else "NON", "c1_R": cr, "c1_derive": c1d, "rapport": r_, "q": q, "err_dt4": cells[2]["c1_err"]}
                chk("(c) %s : c1_R / c1_derive dans [0.9, 1.1]" % cle, ok, "c1_R %.6f c1_der %.6f rapport %.4f (q %.3f ; err-type dt/4 %.2e)" % (cr, c1d, r_, q, cells[2]["c1_err"]))
    n_t = sum(1 for v in C.values() if v["etat"] == "TIENT"); n_j = sum(1 for v in C.values() if v["etat"] in ("TIENT", "NON"))
    out("   (c) : %d des %d points lus tiennent (%d non joues ou non lus)" % (n_t, n_j, 18 - n_j))
    out_j["prediction_c"] = {"tenus": n_t, "lus": n_j, "points": C}
    out(); out("7. LA MESURE DE A, PAR DEGRE (lnA_R sur M1/M2 ; delta_p = moyenne des ecarts a ln(K/g)/(p-2) ; S(p) = max - min)")
    MES = {}
    for p in DEGRES:
        lnAK = math.log(K[p] / G) / (p - 2)
        mod = "M2" if p == 7 else "M1"
        vals = [v for k, v in LR.get(mod, {}).items() if k.startswith("%d|" % p) and not math.isnan(v)]
        if len(vals) < 2:
            note("mesure p = %d" % p, "moins de deux points lus"); continue
        dp, Sp = sum(vals) / len(vals) - lnAK, max(vals) - min(vals)
        A_p = (K[p] / G) ** (1.0 / (p - 2)) * math.exp(dp)
        MES[p] = {"delta_p": dp, "S_p": Sp, "A_p": A_p, "n_points": len(vals), "A_theorique": (K[p] / G) ** (1.0 / (p - 2))}
        note("mesure p = %d" % p, "delta_p %+.3e ; S(p) %.3e ; A(p) = %.9f (theorique (K/g)^(1/(p-2)) = %.9f) ; %d points" % (dp, Sp, A_p, MES[p]["A_theorique"], len(vals)))
    out_j["mesure_A"] = {str(p): v for p, v in MES.items()}

out_j["bilan"] = {"chk": bilan["chk"], "mord": len(bilan["mord"]), "noms_mord": bilan["mord"]}
with open(SORTIE, "w", encoding="utf-8", newline="\n") as f:
    json.dump(out_j, f, sort_keys=True, indent=1)
out(); out("BILAN : %d controles, %d mordent%s" % (bilan["chk"], len(bilan["mord"]), (" : " + ", ".join(bilan["mord"][:6])) if bilan["mord"] else ""))
print("sortie %s convention B %s" % (os.path.basename(SORTIE), B(SORTIE)))
