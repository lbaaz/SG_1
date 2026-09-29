#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CAUSE PROPOSEE POUR 7|1.73|1.20 -- LA PROJECTION DU MODE LIBRE SUR L'AJUSTEMENT II. machine 1, 29/09/2026.

La prediction (a) se lit sur l'ajustement II (sans c1, sans mode). A p = 7 le mode libre est grand et
il n'est pas dans la forme de II : II le PROJETTE sur lnA, comme il projette c1 tau^2. Le biais lu
sur II est donc biais_c1 + biais_mode, et biais_mode depend de l'amplitude ET de la phase du mode
au point. Hypothese : obs_R/pred(a) = 1 + biais_mode / biais_c1, calculable point par point depuis
les (a, c) que M2 a AJUSTES au run (cles a_mode, c_mode de ajustement_corrige, niveau dt/4).
MESURE : pour chaque point de p = 7, une serie synthetique x = A tau^-alpha exp(c1 tau^2 + s^b (a cos
+ c sin)) posee sur la grille dt_2b de l'instrument (fenetre tau_CAP' .. 1.5 tau_dom'), ajustee par
ajuster_point_fixe (II) ; le biais total, le biais c1 seul (mode nul), et le rapport, contre le
ratio OBSERVE de la lecture. Test negatif : mode a phase + pi -> rapport different. Chemins en
arguments : <instrument v15> <resultats_alpha.json du run> <derivation.json> <predictions.json>.
"""
import importlib.util, json, math, sys
import numpy as np
from fractions import Fraction as F

INSTR, RUN, DER, PRED = sys.argv[1:5]
spec = importlib.util.spec_from_file_location("banc", INSTR); banc = importlib.util.module_from_spec(spec); spec.loader.exec_module(banc)
run, der, pred = (json.load(open(f, encoding="utf-8")) for f in (RUN, DER, PRED))
p, alpha = 7, 0.8
b, w = 2.3, der["C3"]["7"]["im_complexe"]
M = banc.M_PAS
lnAK = math.log((9576 / 625) / 0.05) / 5


def serie(w2f, c1, a_, c_, dec=0.0):
    tc, td = banc.tau_cap(w2f), banc.tau_dom(w2f)
    dt = tc / M
    n = int(math.ceil((1.5 * td - tc) / dt)) + 1
    taus = tc + (dec + np.arange(n)) * dt
    tt = (1.0 - taus)[::-1]
    A = banc.A_de(p)
    s = taus / td
    mode = s ** b * (a_ * np.cos(w * np.log(s)) + c_ * np.sin(w * np.log(s)))
    xx = A * taus ** (-alpha) * np.exp(c1 * taus ** 2 + mode)
    return tt, xx[::-1], dt, A


print("point          a_mode        c_mode        biais_II total  biais_c1 seul  rapport predit  ratio observe (a)")
res = {}
for w2 in ("1.73", "2.27", "2.80"):
    c1 = der["C2"]["7|%s" % w2]["c1_float"]
    for c in ("1.05", "1.20"):
        cle = "7|%s|%s" % (w2, c)
        aj = run["G_dt4"][cle]["ajustement_corrige"]
        a_, c_ = aj["a_mode"], aj["c_mode"]
        tt, xx, dt, A = serie(float(w2), c1, a_, c_)
        tot = banc.ajuster_point_fixe(tt, xx, float(w2), p, dt)["lnA_II"] - math.log(A)
        tt0, xx0, _, _ = serie(float(w2), c1, 0.0, 0.0)
        seul = banc.ajuster_point_fixe(tt0, xx0, float(w2), p, dt)["lnA_II"] - math.log(A)
        ttn, xxn, _, _ = serie(float(w2), c1, -a_, -c_)
        neg = banc.ajuster_point_fixe(ttn, xxn, float(w2), p, dt)["lnA_II"] - math.log(A)
        lr = pred["lnA_R"]["II"][cle]
        obs = (lr - lnAK) / (der["C4"]["7|%s" % w2]["0.0"]["biais_lnA"] * 441 / 324)
        res[cle] = {"a": a_, "c": c_, "biais_total": tot, "biais_c1": seul, "rapport_predit": tot / seul, "ratio_observe": obs, "rapport_phase_pi": neg / seul}
        print("%-13s %+.4e   %+.4e   %+.4e      %+.4e     %.3f           %.3f   (phase+pi : %.3f)" % (cle, a_, c_, tot, seul, tot / seul, obs, neg / seul))
ok = all(abs(v["rapport_predit"] - v["ratio_observe"]) <= 0.05 for v in res.values())
print("\n[chk %s] la projection du mode sur II reproduit les six ratios observes de (a) a 0.05 pres" % ("PASSE" if ok else "MORD "))
print("[chk %s] test negatif : la phase + pi ne les reproduit pas" % ("PASSE" if not all(abs(v["rapport_phase_pi"] - v["ratio_observe"]) <= 0.05 for v in res.values()) else "MORD "))
json.dump(res, open("cause_7_1p73_1p20_machine1_v1.json", "w"), indent=1)
