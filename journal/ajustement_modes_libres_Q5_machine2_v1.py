"""ajustement_modes_libres_Q5_machine2_v1.py -- machine 2, 2026-09-13 (soir).

Joue la lecture pre-declaree lecture_predeclaree_Q5_modes_libres_machine2_v1.md
(convention B fc6ca127f8eabc8b, figee 20:59) TELLE QU'ECRITE : C0, C0b, C0c,
modeles M1 / M2 / M2- / M2+, Richardson q = 4, S_M(p), regles Q5-a/b/c.
Series du run 91 (out_run_delta91/alpha_v13, 54 series du plan, G_dt, G_k).
Code de l'instrument v13 IMPORTE (ajuster_point_fixe, fenetre_de, _minimiser_1d).
Deux verbes : chk (peut mordre), note (ne peut pas). Sorties avant bilan.
Classe C, detenteur machine 2. Non opposable.
"""
import hashlib
import importlib.util
import json
import math
import os
import sys
import unicodedata
from fractions import Fraction

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
LECTURE, LECTURE_B = os.path.join(ICI, "lecture_predeclaree_Q5_modes_libres_machine2_v1.md"), "fc6ca127f8eabc8b"
INSTRUMENT, INSTRUMENT_B = os.path.join(ICI, "banc_qualification_machine1_v13.py"), "1ac295648490a86c"
DERIV, DERIV_B = os.path.join(ICI, "derivation_second_ordre_machine2_v1.json"), "b70fca94d72822ad"
RUN = os.path.join(ICI, "out_run_delta91", "alpha_v13")
LOG = os.path.join(ICI, "ajustement_modes_libres_Q5_machine2_v1.log")
SORTIE = os.path.join(ICI, "ajustement_modes_libres_Q5_machine2_v1.json")
DEGRES, W2S, CS = (4, 5, 7), ("1.73", "2.27", "2.80"), ("1.05", "1.20")
CELLULES = (("plan", "dt2_k2"), ("G_dt", "dt2s2_k2"), ("G_k", "dt2_k4"))
lignes, bilan = [], {"chk": 0, "mord": []}


def out(s=""):
    print(s)
    lignes.append(s)


def chk(nom, cond, detail=""):
    bilan["chk"] += 1
    if not cond:
        bilan["mord"].append(nom)
    out("  [chk %s] %s%s" % ("PASSE" if cond else "MORD ", nom, (" -- " + detail) if detail else ""))
    return cond


def note(nom, detail):
    out("  [note] %s -- %s" % (nom, detail))


def B(ch):
    t = open(ch, encoding="utf-8", newline="").read()
    return hashlib.sha256(unicodedata.normalize("NFC", t.replace("\r\n", "\n")).encode()).hexdigest()[:16]


out("Q5 -- AJUSTEMENT DES MODES LIBRES SUR LES SERIES DU 91 -- machine 2 -- lecture %s" % LECTURE_B)
out("python %s ; numpy %s" % (sys.version.split()[0], np.__version__))
chk("lecture Q5 a son empreinte", B(LECTURE) == LECTURE_B, B(LECTURE))
chk("instrument v13 a son empreinte", B(INSTRUMENT) == INSTRUMENT_B, B(INSTRUMENT))
chk("derivation v1 a son empreinte", B(DERIV) == DERIV_B, B(DERIV))
spec = importlib.util.spec_from_file_location("banc_v13", INSTRUMENT)
banc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(banc)
der = json.load(open(DERIV, encoding="utf-8"))
run = json.load(open(os.path.join(RUN, "resultats_alpha.json"), encoding="utf-8"))
note("run", "resultats_alpha.json convention B %s" % B(os.path.join(RUN, "resultats_alpha.json")))

MODES = {p: (float(Fraction(4, p - 2) + Fraction(3, 2)), der["C3"][str(p)]["im_complexe"]) for p in DEGRES}
for p in DEGRES:
    chk("p=%d : b = alpha + 3/2 = Re beta de la derivation" % p,
        abs(MODES[p][0] - der["C3"][str(p)]["re_complexe"]) < 1e-12, "b %.6f w %.6f" % MODES[p])


def lire_serie(nom):
    m = np.loadtxt(os.path.join(RUN, nom), comments="#")
    return m[:, 0], m[:, 1] + m[:, 2]


def ajuster(tt, yy, alpha, c1, tc, td, lo, hi, mode):
    """mode None -> M1 ; (b, w) -> M2. Rend lnA, t*, SS, cond."""
    def systeme(ts):
        tau = ts - tt
        u = yy + alpha * np.log(tau) - c1 * tau ** 2
        if mode is None:
            return u, None
        b, w = mode
        s = tau / td
        X = np.column_stack([np.ones_like(s), s ** b * np.cos(w * np.log(s)), s ** b * np.sin(w * np.log(s))])
        return u, X

    def SS(ts):
        u, X = systeme(ts)
        if X is None:
            return float(((u - u.mean()) ** 2).sum())
        coef = np.linalg.lstsq(X, u, rcond=None)[0]
        return float(((u - X @ coef) ** 2).sum())

    ts, ss = banc._minimiser_1d(SS, lo, hi)
    u, X = systeme(ts)
    if X is None:
        return {"lnA": float(u.mean()), "t_star": ts, "SS": ss, "cond": 1.0, "rang": 1, "amp": 0.0}
    Xn = X / np.linalg.norm(X, axis=0)
    coef, _, rang, _ = np.linalg.lstsq(X, u, rcond=None)
    return {"lnA": float(coef[0]), "t_star": ts, "SS": ss, "cond": float(np.linalg.cond(Xn)), "rang": int(rang),
            "amp": float(math.hypot(coef[1], coef[2]))}


MODELES = ("M1", "M2", "M2-", "M2+")
res = {}
out()
out("1. C0 / C0b -- LECTURE DES SERIES ET CONCORDANCE AVEC L'INSTRUMENT ; AJUSTEMENTS")
for p in DEGRES:
    alpha = float(Fraction(4, p - 2))
    b, w = MODES[p]
    for w2 in W2S:
        c1 = der["C2"]["%d|%s" % (p, w2)]["c1_float"]
        tc, td = banc.tau_cap(float(w2)), banc.tau_dom(float(w2))
        for c in CS:
            cle = "%d|%s|%s" % (p, w2, c)
            res[cle] = {}
            for cell, suff in CELLULES:
                ent = run[cell][cle]
                nom = "alpha_serie_p%d_w%s_c%s_%s.txt" % (p, w2, c, suff)
                chk("C0 %s %s : fichier de serie = celui du JSON" % (cle, cell), ent["serie_fichier"] == nom, ent["serie_fichier"])
                t, x = lire_serie(nom)
                dt = ent["dt2"]
                ref = banc.ajuster_point_fixe(t, x, float(w2), p, dt)
                e0 = abs(ref["lnA_II"] - ent["ajustement"]["lnA_II"])
                chk("C0 %s %s : lnA_II rejoue = JSON a 1e-13" % (cle, cell), e0 <= 1e-13, "%.2e" % e0)
                ok = np.isfinite(x) & (x != 0)
                t, y = t[ok], np.log(np.abs(x[ok]))
                fen = banc.fenetre_de(t, ref["t_star"], tc, td, 1e-6 * dt)
                tt, yy = t[fen], y[fen]
                lo, hi = float(tt[-1]) * (1 + 1e-12) + 1e-12 * tc, float(t[-1]) + 2 * td
                m0 = ajuster(tt, yy, alpha, 0.0, tc, td, lo, hi, None)
                e0b = abs(m0["lnA"] - ref["lnA_II"])
                chk("C0b %s %s : M1 a c1 = 0 = ajustement II a 1e-12" % (cle, cell), e0b <= 1e-12, "%.2e" % e0b)
                r = {"M1": ajuster(tt, yy, alpha, c1, tc, td, lo, hi, None),
                     "M2": ajuster(tt, yy, alpha, c1, tc, td, lo, hi, (b, w)),
                     "M2-": ajuster(tt, yy, alpha, c1, tc, td, lo, hi, (b, w / 2)),
                     "M2+": ajuster(tt, yy, alpha, c1, tc, td, lo, hi, (b, 2 * w))}
                for mo in ("M2", "M2-", "M2+"):
                    chk("C0c %s %s %s : rang 3" % (cle, cell, mo), r[mo]["rang"] == 3, "rang %d cond %.3g" % (r[mo]["rang"], r[mo]["cond"]))
                res[cle][cell] = {"n_points": int(len(tt)), "lnA_II_instrument": ref["lnA_II"], **{
                    mo: {k: r[mo][k] for k in ("lnA", "t_star", "SS", "cond", "amp")} for mo in MODELES}}

out()
out("2. RICHARDSON (q = 4 suppose) ET DISPERSION ENTRE LES SIX POINTS")
S, synth = {}, {}
for p in DEGRES:
    lnAK = math.log(float(banc.K_de(p)) / banc.G_REF) / (p - 2)
    S[p] = {}
    for mo in MODELES:
        vals = []
        for w2 in W2S:
            for c in CS:
                cle = "%d|%s|%s" % (p, w2, c)
                a1, a2 = res[cle]["plan"][mo]["lnA"], res[cle]["G_dt"][mo]["lnA"]
                lR = a2 + (a2 - a1) / 15
                res[cle].setdefault("R", {})[mo] = lR - lnAK
                vals.append(lR - lnAK)
        S[p][mo] = max(vals) - min(vals)
        conds = [res["%d|%s|%s" % (p, w2, c)]["plan"][mo]["cond"] for w2 in W2S for c in CS]
        note("p=%d %-3s" % (p, mo), "S = %.4e ; lnA_R - ln(K/g)/(p-2) aux six : %s ; cond max %.3g"
             % (S[p][mo], " ".join("%+.3e" % v for v in vals), max(conds)))
    for mo in ("M2", "M2-", "M2+"):
        note("p=%d %s / M1" % (p, mo), "S rapport %.4f ; SS moyen rapport %.4f" % (
            S[p][mo] / S[p]["M1"],
            np.mean([res["%d|%s|%s" % (p, w2, c)]["plan"][mo]["SS"] / res["%d|%s|%s" % (p, w2, c)]["plan"]["M1"]["SS"]
                     for w2 in W2S for c in CS])))

out()
out("3. REGLE DE LECTURE (ecrite avant, section 3)")
q5a = S[7]["M2"] <= S[7]["M1"] / 3
q5b = S[7]["M2-"] > S[7]["M1"] / 3 and S[7]["M2+"] > S[7]["M1"] / 3
q5c = {p: S[p]["M2"] <= 2 * S[p]["M1"] for p in (4, 5)}
note("Q5-a", "S_M2(7) = %.4e <= S_M1(7)/3 = %.4e : %s" % (S[7]["M2"], S[7]["M1"] / 3, q5a))
note("Q5-b", "S_M2-(7) = %.4e , S_M2+(7) = %.4e > %.4e : %s" % (S[7]["M2-"], S[7]["M2+"], S[7]["M1"] / 3, q5b))
for p in (4, 5):
    note("Q5-c p=%d" % p, "S_M2 = %.4e <= 2 S_M1 = %.4e : %s" % (S[p]["M2"], 2 * S[p]["M1"], q5c[p]))
if not q5a:
    verdict = "(i) NE TIENT PAS -> voie (ii)"
elif not q5b:
    verdict = "(i) NON SPECIFIQUE"
else:
    verdict = "(i) TIENT A p = 7"
if q5a and not all(q5c.values()):
    verdict += " ; Q5-c echoue -> (i) restreint a p = 7"
note("VERDICT DE LECTURE", verdict)

sortie = {"S": {str(p): S[p] for p in DEGRES}, "points": res, "Q5": {"a": q5a, "b": q5b, "c": {str(k): v for k, v in q5c.items()}},
          "verdict": verdict, "ancres": {"lecture": LECTURE_B, "instrument": INSTRUMENT_B, "derivation": DERIV_B},
          "portee": "a posteriori, non opposable ; q = 4 suppose ; six points par degre ; BOCAL4"}
with open(SORTIE, "w", encoding="utf-8", newline="\n") as f:
    json.dump(sortie, f, sort_keys=True, ensure_ascii=True, indent=1)
out()
out("SORTIE %s convention B %s" % (os.path.basename(SORTIE), B(SORTIE)))
out("BILAN : %d controles, %d mordent %s" % (bilan["chk"], len(bilan["mord"]), bilan["mord"][:10]))
with open(LOG, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lignes) + "\n")
print("log convention B %s ; script convention B %s" % (B(LOG), B(os.path.abspath(__file__))))
