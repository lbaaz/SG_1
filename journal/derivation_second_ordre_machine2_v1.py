"""derivation_second_ordre_machine2_v1.py -- machine 2, 2026-09-13.

Chantier du SECOND ORDRE de la constante A (engagement operateur "go 1").
Joue la lecture pre-declaree lecture_predeclaree_second_ordre_machine2_v1.md
(convention B 99080e4822bf0108, figee 2026-09-13T17:29 avant cette piece),
TELLE QU'ECRITE : C1..C4 (sections 1), I1/I2 (section 2), lecture a
posteriori non opposable sur le run 91 (section 3).

Deux verbes : chk (peut mordre) et note (ne peut pas). Les sorties (log,
JSON) s'ecrivent AVANT le bilan ; aucun assert ne tue l'assemblage.
Classe C, detenteur machine 2. Ce n'est pas un gel.
"""
import ast
import hashlib
import importlib.util
import inspect
import json
import math
import os
import sys
import unicodedata
from fractions import Fraction

import numpy as np
import sympy as sp

ICI = os.path.dirname(os.path.abspath(__file__))
LECTURE = os.path.join(ICI, "lecture_predeclaree_second_ordre_machine2_v1.md")
LECTURE_B = "99080e4822bf0108"
INSTRUMENT = os.path.join(ICI, "banc_qualification_machine1_v13.py")
INSTRUMENT_B = "1ac295648490a86c"
RUN91 = os.path.join(ICI, "out_run_delta91", "alpha_v13", "resultats_alpha.json")
LOG = os.path.join(ICI, "derivation_second_ordre_machine2_v1.log")
SORTIE = os.path.join(ICI, "derivation_second_ordre_machine2_v1.json")

DEGRES = (4, 5, 7)
W2S = ("1.73", "2.27", "2.80")
CS = ("1.05", "1.20")

lignes, bilan, sortie = [], {"chk": 0, "mord": 0, "noms_mord": []}, {}


def out(s=""):
    print(s)
    lignes.append(s)


def chk(nom, cond, detail=""):
    bilan["chk"] += 1
    if not cond:
        bilan["mord"] += 1
        bilan["noms_mord"].append(nom)
    out("  [chk %s] %s%s" % ("PASSE" if cond else "MORD ", nom, (" -- " + detail) if detail else ""))
    return cond


def note(nom, detail):
    out("  [note] %s -- %s" % (nom, detail))


def empreinte_B(chemin):
    t = open(chemin, encoding="utf-8", newline="").read()
    return hashlib.sha256(unicodedata.normalize("NFC", t.replace("\r\n", "\n")).encode()).hexdigest()[:16]


# ---------------------------------------------------------------------------
out("DERIVATION DU SECOND ORDRE -- machine 2 -- lecture %s" % LECTURE_B)
out("python %s ; numpy %s ; sympy %s" % (sys.version.split()[0], np.__version__, sp.__version__))
out()
out("0. ANCRES")
chk("lecture pre-declaree a son empreinte", empreinte_B(LECTURE) == LECTURE_B, empreinte_B(LECTURE))
chk("instrument v13 a son empreinte", empreinte_B(INSTRUMENT) == INSTRUMENT_B, empreinte_B(INSTRUMENT))
spec = importlib.util.spec_from_file_location("banc_v13", INSTRUMENT)
banc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(banc)
chk("reglage de l'instrument = 1/44100", banc.DELTA == Fraction(1, 44100), str(banc.DELTA))
DELTA = banc.DELTA
R_FEN = Fraction(1, 10)     # gel alpha v5 6 : tau_CAP = r tau_dom
M = banc.M_PAS
chk("M de l'instrument = 20", M == 20, str(M))

# ---------------------------------------------------------------------------
out()
out("1. C1 -- ELIMINATION DEPUIS LE TEXTE DE acc_pu")
src = inspect.getsource(banc.acc_pu)
arbre = ast.parse(src.replace("\n    ", "\n") if src.startswith("    ") else src)
retours = [n for n in ast.walk(arbre) if isinstance(n, ast.Return) and isinstance(n.value, ast.Tuple)]
chk("acc_pu porte UN retour-tuple (les deux accelerations)", len(retours) == 1, "%d" % len(retours))
e1_txt, e2_txt = (ast.unparse(e) for e in retours[0].value.elts)
note("acc 1 (texte)", e1_txt)
note("acc 2 (texte)", e2_txt)
assigns = [n for n in ast.walk(arbre) if isinstance(n, ast.Assign)]
base_txt = [ast.unparse(n.value) for n in assigns if ast.unparse(n.targets[0]) == "base"]
chk("acc_pu definit base une fois", len(base_txt) == 1, str(base_txt))
note("base (texte)", base_txt[0])

t, g, pp, w = sp.symbols("t g p w2", positive=True)
x1f, x2f = sp.Function("x1")(t), sp.Function("x2")(t)
Wd = w ** 2 - 1                                            # delta = w2^2 - W1^2, W1 = 1
Fsym = sp.Function("F")(t)                                 # F = base, fonction de t par x1 + x2
env = {"W1": sp.Integer(1), "w2": w, "delta": Wd, "a1": x1f, "a2": x2f}
env_d = dict(env, d1=Fsym, d2=Fsym, base=Fsym)
acc1 = sp.sympify(e1_txt.replace("d1", "base"), locals=env_d)
acc2 = sp.sympify(e2_txt.replace("d2", "base"), locals=env_d)
# x1'' = acc1(x1, F) ; derivee quatrieme par derivation de la relation
x1pp, x2pp = acc1, acc2
x1p4 = sp.diff(x1pp, t, 2).subs({sp.Derivative(x1f, (t, 2)): acc1, sp.Derivative(x2f, (t, 2)): acc2})
x2p4 = sp.diff(x2pp, t, 2).subs({sp.Derivative(x1f, (t, 2)): acc1, sp.Derivative(x2f, (t, 2)): acc2})
reste = sp.simplify((x1p4 + x2p4) + (1 + w ** 2) * (x1pp + x2pp) + w ** 2 * (x1f + x2f) - Fsym)
chk("C1 : x'''' + (1+w2^2) x'' + w2^2 x - F == 0 identiquement", reste == 0, "reste = %s" % reste)
# test negatif : un couplage mutile (2 base / delta sur la premiere) doit laisser un reste
acc1_mut = sp.sympify(e1_txt.replace("d1", "(2*base)"), locals=env_d)
x1p4m = sp.diff(acc1_mut, t, 2).subs({sp.Derivative(x1f, (t, 2)): acc1_mut, sp.Derivative(x2f, (t, 2)): acc2})
x2p4m = sp.diff(acc2, t, 2).subs({sp.Derivative(x1f, (t, 2)): acc1_mut, sp.Derivative(x2f, (t, 2)): acc2})
reste_m = sp.simplify((x1p4m + x2p4m) + (1 + w ** 2) * (acc1_mut + acc2) + w ** 2 * (x1f + x2f) - Fsym)
chk("C1 negatif : couplage mutile -> reste NON nul", reste_m != 0, "reste = %s" % reste_m)
chk("base = g (a1 + a2)^(p-1) au texte", sp.simplify(sp.sympify(base_txt[0], locals={"g": g, "a1": x1f, "a2": x2f, "p": pp})
                                                   - g * (x1f + x2f) ** (pp - 1)) == 0)

# ---------------------------------------------------------------------------
out()
out("2. C2 -- COEFFICIENT c1 EN EXACT, ET SUBSTITUTION")
tau, c1s, c2s = sp.symbols("tau c1 c2")


def alpha_q(p):
    return Fraction(4, p - 2)


def K_q(p):
    a = alpha_q(p)
    return a * (a + 1) * (a + 2) * (a + 3)


def P_q(a, m):
    """m (m-1) (m-2) (m-3) pour la puissance tau^m (derivee quatrieme)."""
    return m * (m - 1) * (m - 2) * (m - 3)


def residu_serie(p, w2v, c1v, c2v, ordre):
    """Residu de l'EDO en tau (d/dt = -d/dtau, derivees paires inchangees),
    x = tau^(-a) (1 + c1 tau^2 + c2 tau^4), A factorise, g A^(p-2) = K.
    Rend les coefficients de tau^0, tau^2, tau^4 de residu / tau^(-a-4)."""
    a = sp.Rational(alpha_q(p).numerator, alpha_q(p).denominator)
    K = a * (a + 1) * (a + 2) * (a + 3)
    u = 1 + c1v * tau ** 2 + c2v * tau ** 4
    x = tau ** (-a) * u
    lin = sp.diff(x, tau, 4) + (1 + w2v ** 2) * sp.diff(x, tau, 2) + w2v ** 2 * x
    nl = K * tau ** (-a * (p - 1)) * u ** (p - 1)            # g A^(p-1) = A K
    r = sp.expand(sp.simplify((lin - nl) * tau ** (a + 4)))
    return [sp.nsimplify(r.coeff(tau, k)) for k in range(0, ordre + 1, 2)]


resultats_c = {}
for p in DEGRES:
    a = alpha_q(p)
    K = K_q(p)
    P2 = P_q(a, 2 - a)
    c1_sur_1pw2 = a * (a + 1) / ((p - 1) * K - P2)
    for w2txt in W2S:
        w2v = sp.Rational(w2txt)
        c1v = sp.Rational(c1_sur_1pw2.numerator, c1_sur_1pw2.denominator) * (1 + w2v ** 2)
        co = residu_serie(p, w2v, c1v, 0, 2)
        ok = chk("C2 p=%d w2=%s : coeff tau^0 et tau^2 nuls en exact" % (p, w2txt), co[0] == 0 and co[1] == 0,
                 "tau^0 %s ; tau^2 %s" % (co[0], co[1]))
        co_m = residu_serie(p, w2v, c1v * sp.Rational(1001, 1000), 0, 2)
        chk("C2 negatif p=%d w2=%s : c1 x 1.001 -> tau^2 non nul" % (p, w2txt), co_m[1] != 0, "tau^2 %s" % co_m[1])
        # c2, pour memoire : il n'est lu qu'apres les modes libres (I1)
        c2v = sp.solve(residu_serie(p, w2v, c1v, c2s, 4)[2], c2s)
        resultats_c["%d|%s" % (p, w2txt)] = {"c1": str(c1v), "c1_float": float(c1v),
                                             "c2": [str(v) for v in c2v], "c2_float": [float(v) for v in c2v]}
    # grandeur sans w2 : c1 tau_dom'^2 = delta' a(a+1)/((p-1)K - P2)
    rel = DELTA * c1_sur_1pw2
    planch = DELTA / ((a + 2) * (a + 3))
    note("p=%d" % p, "alpha %s  K %s  P2 %s  c1/(1+w2^2) = %s  ; c1 tau_dom'^2 = %s = %.4e ; plancher v7 = %.4e ; "
         "rapport terme/plancher = %s = %.4f" % (a, K, P2, c1_sur_1pw2, rel, float(rel), float(planch),
                                                rel / planch, float(rel / planch)))
    resultats_c["%d" % p] = {"alpha": str(a), "K": str(K), "P2": str(P2), "c1_sur_1pw2": str(c1_sur_1pw2),
                             "c1_tau_dom2": str(rel), "plancher_v7": str(planch),
                             "terme_sur_plancher": str(rel / planch)}
sortie["C2"] = resultats_c

# ---------------------------------------------------------------------------
out()
out("3. C3 -- EXPOSANTS DES MODES LIBRES")
beta = sp.symbols("beta")
modes = {}
for p in DEGRES:
    a = sp.Rational(alpha_q(p).numerator, alpha_q(p).denominator)
    K = a * (a + 1) * (a + 2) * (a + 3)
    m = beta - a
    poly = sp.expand(m * (m - 1) * (m - 2) * (m - 3) - (p - 1) * K)
    chk("C3 p=%d : beta = -1 racine EXACTE (translation de t*)" % p, poly.subs(beta, -1) == 0,
        "poly(-1) = %s" % poly.subs(beta, -1))
    chk("C3 negatif p=%d : beta = -1 n'est pas racine si K est mutile" % p,
        sp.expand(m * (m - 1) * (m - 2) * (m - 3) - (p - 1) * K * sp.Rational(1001, 1000)).subs(beta, -1) != 0)
    racines = [complex(r) for r in sp.Poly(poly, beta).nroots(n=30)]
    note("p=%d racines" % p, " ; ".join("%.6f%+.6fi" % (r.real, r.imag) for r in racines))
    cplx = [r for r in racines if abs(r.imag) > 1e-12]
    re_c = cplx[0].real if cplx else None
    chk("C3 p=%d : Re(beta) complexe = alpha + 3/2" % p, cplx and all(abs(r.real - float(a + sp.Rational(3, 2))) < 1e-12
                                                               for r in cplx), "Re %s ; alpha+3/2 %s" % (re_c, a + sp.Rational(3, 2)))
    entre = cplx and 2 < re_c < 4
    note("I1 p=%d" % p, "modes libres complexes a Re beta = %.6f, %s tau^2 et tau^4 ; frequence en ln tau %.6f"
         % (re_c, "ENTRE" if entre else "HORS de", abs(cplx[0].imag)))
    modes[str(p)] = {"racines": [[r.real, r.imag] for r in racines], "re_complexe": re_c,
                     "im_complexe": abs(cplx[0].imag), "entre_tau2_et_tau4": bool(entre),
                     "residuel_exposant_en_delta": re_c / 2}
sortie["C3"] = modes

# ---------------------------------------------------------------------------
out()
out("4. C4 -- BIAIS DE L'AJUSTEMENT II DE L'INSTRUMENT SUR SERIE SYNTHETIQUE")


def serie_synth(p, w2f, c1v, decalage):
    """tau^(-a)(1 + c1 tau^2) A sur la grille dt_2b nominale, t* = 1 ; la serie
    finit a tau_CAP' (+ decalage x dt) ; t croissant."""
    tc, td = banc.tau_cap(w2f), banc.tau_dom(w2f)
    dt = tc / M
    n = int(math.ceil((1.5 * td - tc) / dt)) + 1
    taus = tc + (decalage + np.arange(n)) * dt
    tt = (1.0 - taus)[::-1]
    a, A = float(alpha_q(p)), banc.A_de(p)
    xx = A * taus ** (-a) * (1 + c1v * taus ** 2)
    return tt, xx[::-1], dt, A


biais = {}
for p in DEGRES:
    for w2txt in W2S:
        w2f = float(w2txt)
        c1v = resultats_c["%d|%s" % (p, w2txt)]["c1_float"]
        planch = float(DELTA / ((alpha_q(p) + 2) * (alpha_q(p) + 3)))
        cle = "%d|%s" % (p, w2txt)
        biais[cle] = {}
        for dec in (0.0, 0.5):
            res = {}
            for mult in (0.0, 1.0, 2.0):
                tt, xx, dt, A = serie_synth(p, w2f, mult * c1v, dec)
                aj = banc.ajuster_point_fixe(tt, xx, w2f, p, dt)
                res[mult] = (aj["statut"], aj.get("lnA_II", float("nan")) - math.log(A), aj.get("n_points"))
            st = all(r[0] == "POINT_FIXE" for r in res.values())
            chk("C4 %s dec %.1f : point fixe atteint aux trois series" % (cle, dec), st, str([r[0] for r in res.values()]))
            chk("C4a %s dec %.1f : c1 = 0 -> |biais| <= 1e-9" % (cle, dec), abs(res[0.0][1]) <= 1e-9, "%.3e" % res[0.0][1])
            b1, b2 = res[1.0][1], res[2.0][1]
            lin = abs(b2 / (2 * b1) - 1) if b1 != 0 else float("inf")
            chk("C4b %s dec %.1f : mutation 2 c1 -> biais x 2 a 1e-2" % (cle, dec), lin <= 1e-2, "b2/(2 b1) - 1 = %.3e" % lin)
            note("C4c %s dec %.1f" % (cle, dec), "biais lnA = %.6e ; /plancher v7 = %.4f ; /(c1 tau_dom'^2) = %.4f ; n_points %s"
                 % (b1, b1 / planch, b1 / float(DELTA * Fraction(resultats_c[str(p)]["c1_sur_1pw2"])), res[1.0][2]))
            biais[cle]["%.1f" % dec] = {"biais_lnA": b1, "sur_plancher": b1 / planch, "linearite": lin,
                                        "biais_c1_nul": res[0.0][1], "n_points": res[1.0][2]}
sortie["C4"] = biais

# ---------------------------------------------------------------------------
out()
out("5. LECTURE A POSTERIORI SUR LE RUN 91 -- NON OPPOSABLE (section 3 de la lecture)")
run = json.load(open(RUN91, encoding="utf-8"))
note("run 91 lu", "%s ; convention B %s" % (os.path.relpath(RUN91, ICI), empreinte_B(RUN91)))
lect = {}
etats = []
for p in DEGRES:
    disp = run["degres"][str(p)].get("dispersion_lnA")
    chk("run 91 p=%d : cle /degres/p/dispersion_lnA presente" % p, disp is not None, str(disp))
    for w2txt in W2S:
        for c in CS:
            cle = "%d|%s|%s" % (p, w2txt, c)
            aj = run["plan"].get(cle, {}).get("ajustement", {})
            gk = aj.get("gA_II_sur_K")
            if gk is None or disp is None:
                note("NON JOUE %s" % cle, "cle gA_II_sur_K absente")
                etats.append("NON_JOUE")
                continue
            obs = math.log(gk) / (p - 2)
            pred = biais["%d|%s" % (p, w2txt)]["0.0"]["biais_lnA"]
            ecart = obs - pred
            compat = abs(ecart) <= 3 * disp
            signe = (obs > 0) == (pred > 0)
            etats.append("COMPAT" if compat else ("SIGNE" if signe else "NON"))
            note(cle, "obs %.6e  pred %.6e  obs/pred %.4f  (obs-pred)/disp_91 %+.3f  -> %s"
                 % (obs, pred, obs / pred, ecart / disp, etats[-1]))
            lect[cle] = {"obs": obs, "pred": pred, "obs_sur_pred": obs / pred, "ecart_sur_disp": ecart / disp,
                         "etat": etats[-1]}
if "NON_JOUE" in etats:
    verdict_l = "NON JOUE (cle absente)"
elif all(e == "COMPAT" for e in etats):
    verdict_l = "COMPATIBLE"
elif all(e in ("COMPAT", "SIGNE") for e in etats) and all(
        (lect[k]["obs"] > 0) == (lect[k]["pred"] > 0) for k in lect):
    verdict_l = "DE SIGNE"
else:
    verdict_l = "NON"
note("LECTURE a posteriori (regle ecrite avant ouverture)", "%s ; comptes %s" % (
    verdict_l, {e: etats.count(e) for e in sorted(set(etats))}))
sortie["lecture_run91"] = {"verdict": verdict_l, "points": lect, "portee": "a posteriori, NON opposable (N-70)"}

# ---------------------------------------------------------------------------
out()
bilan["noms_mord"] = list(bilan["noms_mord"])
sortie["bilan"] = bilan
sortie["ancres"] = {"lecture": LECTURE_B, "instrument": INSTRUMENT_B}
with open(SORTIE, "w", encoding="utf-8", newline="\n") as f:
    json.dump(sortie, f, sort_keys=True, ensure_ascii=True, indent=1)
out("SORTIE %s ecrite, convention B %s" % (os.path.basename(SORTIE), empreinte_B(SORTIE)))
out("BILAN : %d controles, %d mordent%s" % (bilan["chk"], bilan["mord"],
                                           (" : " + ", ".join(bilan["noms_mord"])) if bilan["mord"] else ""))
with open(LOG, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lignes) + "\n")
print("log convention B %s" % empreinte_B(LOG))
