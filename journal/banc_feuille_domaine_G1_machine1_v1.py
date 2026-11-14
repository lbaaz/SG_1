# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1. BANC DU SELFTEST de la feuille : chaque alteration d'une ligne doit
# faire mordre le selftest. Reprend les vingt-quatre alterations du banc de machine 2 (lot 3381564852ba6fe4),
# adaptees, et en ajoute pour la cascade, la garde G-6 et la rivale. usage : <feuille.py>
import sys, io, contextlib
SRC = open(sys.argv[1], encoding="ascii").read()
ALT = [
 ("M01", 'SIGMA_J_MAX = 0.2', 'SIGMA_J_MAX = 0.25'),
 ("M02", 'POIDS_SITE_MIN = 0.5', 'POIDS_SITE_MIN = 0.45'),
 ("M03", 'DIX_PLANCHERS = 1.33e-12', 'DIX_PLANCHERS = 1.0e-12'),
 ("M04", 'SUIVI_MIN = 0.9', 'SUIVI_MIN = 0.8'),
 ("M05", 'STABILITE_CIBLE = 2.0', 'STABILITE_CIBLE = 2.5'),
 ("M06", 'ETALEMENT_CHAINE = 2.0', 'ETALEMENT_CHAINE = 3.0'),
 ("M07", 'MIN_JUGES = 6', 'MIN_JUGES = 5'),
 ("M07b", 'MIN_JUGES = 6', 'MIN_JUGES = 7'),
 ("M08", 'MIN_EN_LISIBLES = 4', 'MIN_EN_LISIBLES = 3'),
 ("M08b", 'MIN_HORS_LISIBLES = 4', 'MIN_HORS_LISIBLES = 3'),
 ("M08c", 'MIN_EN_LISIBLES = 4', 'MIN_EN_LISIBLES = 5'),
 ("M08d", 'MIN_HORS_LISIBLES = 4', 'MIN_HORS_LISIBLES = 5'),
 ("M09", 'TOL_ANCRE = 1e-2', 'TOL_ANCRE = 2e-2'),
 ("M10", 'if 0.5 <= q <= 2.0:', 'if 0.5 < q <= 2.0:'),
 ("M10b", 'if 0.5 <= q <= 2.0:', 'if 0.5 <= q < 2.0:'),
 ("M11", 'if q * q >= 0.1 and q * q <= 10.0:', 'if q * q > 0.1 and q * q <= 10.0:'),
 ("M12", 'q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"]', 'q = e["chaine"]["gammas"][1] / e["Gamma_2D"]["3"]'),
 ("M13", 'q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"]', 'q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["2"]'),
 ("M14", 'vus[(e["n1"], e["n2"])] > 1', 'vus[(e["n1"], e["n2"])] > 2'),
 ("M15", 'if len(en_l) < MIN_EN_LISIBLES or', 'if len(en_l) <= MIN_EN_LISIBLES or'),
 ("M15b", 'or len(hors_l) < MIN_HORS_LISIBLES:', 'or len(hors_l) <= MIN_HORS_LISIBLES:'),
 ("M16", '"DECADE": "TENU"', '"DECADE": "TOMBE"'),
 ("M18", 'pire = max(juges, key=lambda x: ORDRE_PALIER[x["palier"]])', 'pire = min(juges, key=lambda x: ORDRE_PALIER[x["palier"]])'),
 ("M19", 'if min(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:', 'if max(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:'),
 ("M20", 'gs = [e["Gamma_2D"][k] for k in ("2", "3", "4")]', 'gs = [e["Gamma_2D"][k] for k in ("3", "4")]'),
 ("M20b", 'gs = [e["Gamma_2D"][k] for k in ("2", "3", "4")]', 'gs = [e["Gamma_2D"][k] for k in ("2", "3")]'),
 ("M21", 'if e["n1"] < 0 or e["n2"] < 0:', 'if e["n1"] < 0:'),
 ("M21b", 'if e["n1"] < 0 or e["n2"] < 0:', 'if e["n2"] < 0:'),
 ("M22", '        motifs += garde_ancres(pts)\n    return motifs', '        pass\n    return motifs'),
 ("M23", 'if not (g3 > DIX_PLANCHERS):', 'if not (g3 >= DIX_PLANCHERS):'),
 ("M24", 'if min(cg) <= 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:', 'if min(cg) <= 0 or max(cg[1:]) / min(cg[1:]) > ETALEMENT_CHAINE:'),
 ("M24b", 'if min(cg) <= 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:', 'if min(cg) <= 0 or max(cg[:3]) / min(cg[:3]) > ETALEMENT_CHAINE:'),
 ("N01", '    elif a == 0 and b == 0:', '    elif a == 0:'),
 ("N02", '    elif a == 0:\n        v = "LA GARDE SUFFIT"', '    elif b == 0:\n        v = "LA GARDE SUFFIT"'),
 ("N03", 'a = sum(1 for x in en_l if x["classe"] == "TOMBE")', 'a = sum(1 for x in en_l if x["classe"] == "TENU")'),
 ("N03b", 'b = sum(1 for x in hors_l if x["classe"] == "TENU")', 'b = sum(1 for x in hors_l if x["classe"] == "TOMBE")'),
 ("N04", '            motifs += garde_du_moteur(pid, p)', '            pass'),
 ("N05", 'TOL_GARDE = 5e-5', 'TOL_GARDE = 5e-4'),
 ("N05b", 'TOL_GARDE = 5e-5', 'TOL_GARDE = 5e-6'),
 ("N06", 'PAIRES_RIVALE = ("P1", "P2", "P3")', 'PAIRES_RIVALE = ("P1", "P2", "P3", "P4", "P5")'),
 ("N06b", 'PAIRES_RIVALE = ("P1", "P2", "P3")', 'PAIRES_RIVALE = ("P1", "P2")'),
 ("N07", 'MIN_PAIRES_RIVALE = 2', 'MIN_PAIRES_RIVALE = 1'),
 ("N07b", 'MIN_PAIRES_RIVALE = 2', 'MIN_PAIRES_RIVALE = 3'),
 ("N08", 'out[nom] = "HOMOGENE" if ca == cb else "HETEROGENE"', 'out[nom] = "HOMOGENE" if ca != cb else "HETEROGENE"'),
 ("N09", 'rivale = "TENUE" if all(x == "HOMOGENE" for x in lisibles) else "NON TENUE"', 'rivale = "TENUE" if any(x == "HOMOGENE" for x in lisibles) else "NON TENUE"'),
 ("N10", 'if not (e["J_ecart_type"] < SIGMA_J_MAX):', 'if not (e["J_ecart_type"] <= SIGMA_J_MAX):'),
 ("N11", 'if not (e["poids_site"] >= POIDS_SITE_MIN):', 'if not (e["poids_site"] > POIDS_SITE_MIN):'),
 ("N12", 'if min(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:', 'if min(e["suivi"]["2"], e["suivi"]["4"]) <= SUIVI_MIN:'),
 ("N13", 'if min(gs) <= 0 or max(gs) / min(gs) > STABILITE_CIBLE:', 'if min(gs) < 0 or max(gs) / max(min(gs), 1e-300) > STABILITE_CIBLE and False:'),
 ("N14", 'if min(cg) <= 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:', 'if max(cg) / min(cg) > ETALEMENT_CHAINE:'),
 ("N15", '    if gm.get("statut") != statut:', '    if False:'),
 ("N16", '    if gm.get("erreur"):', '    if False:'),
 ("N17", 'en = [par_id[k] for k in ATTENDUS if ATTENDUS[k][0] == "juge" and ATTENDUS[k][3] == EN]', 'en = [par_id[k] for k in ATTENDUS if ATTENDUS[k][3] == EN]'),
 ("N18", '    if ch.get("erreur"):', '    if False:'),
 ("N19", '    if ch.get("vide") or not ch.get("definie"):', '    if ch.get("vide"):'),
 ("N20", '    if ch.get("vide") or not ch.get("definie"):', '    if not ch.get("definie"):'),
 ("N21", 'if q * q >= 0.1 and q * q <= 10.0:', 'if q * q >= 0.1 and q * q <= 10.1:'),
 ("N22", 'if q * q >= 0.1 and q * q <= 10.0:', 'if q * q >= 0.1005 and q * q <= 10.0:'),
 ("N23", '            if p.get("faisable") and len(p["etats"]) != N_ETATS:', '            if False:'),
 ("N24", '            if (p["role"], p["w2"], p["facteur"]) != (role, w2, fac):', '            if False:'),
]
def joue(src):
    ns = {"__name__": "feuille_alteree"}
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(src, "feuille_alteree", "exec"), ns)
            return bool(ns["selftest"]())
    except BaseException as x:
        return "exception %s" % type(x).__name__
assert joue(SRC) is True, "la feuille intacte ne passe pas son selftest"
mord = 0
for nom, a, b in ALT:
    assert SRC.count(a) == 1, (nom, SRC.count(a))
    r = joue(SRC.replace(a, b))
    m = (r is not True); mord += m
    print("  %-5s %-8s %s  ->  %s" % (nom, "MORD" if m else "survit", a.replace("\n", " / ")[:60], b.replace("\n", " / ")[:60]))
print("BANC : %d alterations, %d mordues, %d survivantes" % (len(ALT), mord, len(ALT) - mord))
