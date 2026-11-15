# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1, 2026-11-14. BANC DU SELFTEST de la feuille du gel "chaine d'ordre 2" :
# chaque alteration doit faire mordre le selftest. Deux familles :
#  (T) LA TABLE : chaque champ de chaque ligne de ATTENDUS, chaque valeur de ANCRES, de BANDES et des deux canons
#      (c'est la reserve R-1 de machine 2 sur le gel precedent : le selftest doit tenir la table du gel) ;
#  (C) LE CODE : constantes, comparaisons, lectures, cascade, gardes.
# usage : python3 -I banc_feuille_ordre2_machine1_v1.py <feuille.py>
import sys, io, re, contextlib
SRC = open(sys.argv[1], encoding="ascii").read()
ALT = []
# ---------------------------------------------------------------- (T) la table
lignes = [l for l in SRC.split("\n") if re.match(r'^    "[A-Z][0-9]": \("(juge|ancre|temoin)"', l)]
assert len(lignes) == 16, len(lignes)
AUTRE_ROLE = {"juge": "temoin", "ancre": "juge", "temoin": "juge"}
AUTRE_BANDE = {"PROCHE": "MOYENNE", "MOYENNE": "LOINTAINE", "LOINTAINE": "PROCHE", "None": "PROCHE"}
AUTRE_FAC = {"2/3": "3/4", "3/4": "2/3", "1/1": "3/2", "3/2": "1/1", "4/3": "3/2", "1/2": "2/3"}
for l in lignes:
    m = re.match(r'^    "(..)": \("(\w+)", "(\d+)/(\d+)", "(\d/\d)", (\w+), (EN|HORS), ([0-9.]+), ([0-9.]+)\),$', l)
    assert m, l
    pid, role, num, den, fac, bande, garde, d1, cmax = m.groups()
    def ligne(role=role, num=num, fac=fac, bande=bande, garde=garde, d1=d1, cmax=cmax):
        return '    "%s": ("%s", "%s/%s", "%s", %s, %s, %s, %s),' % (pid, role, num, den, fac, bande, garde, d1, cmax)
    assert ligne() == l, (ligne(), l)
    ALT += [("T-%s-role" % pid, l, ligne(role=AUTRE_ROLE[role])),
            ("T-%s-w2" % pid, l, ligne(num=str(int(num) + 1))),
            ("T-%s-facteur" % pid, l, ligne(fac=AUTRE_FAC[fac])),
            ("T-%s-bande" % pid, l, ligne(bande=AUTRE_BANDE[bande])),
            ("T-%s-garde" % pid, l, ligne(garde=("HORS" if garde == "EN" else "EN"))),
            ("T-%s-D1" % pid, l, ligne(d1="%.6f" % (float(d1) + 1e-3))),
            ("T-%s-c_max" % pid, l, ligne(cmax="%.6f" % (float(cmax) - 1e-3)))]
ALT += [
 ("T-ancre-A1-etiquette", '"A1": ((7, 2), 2.1623273017950654e-10', '"A1": ((7, 3), 2.1623273017950654e-10'),
 ("T-ancre-A2-etiquette", '"A2": ((8, 2), 2.6613925716641374e-09', '"A2": ((9, 2), 2.6613925716641374e-09'),
 ("T-ancre-A1-2D", '"A1": ((7, 2), 2.1623273017950654e-10', '"A1": ((7, 2), 2.2623273017950654e-10'),
 ("T-ancre-A2-2D", '"A2": ((8, 2), 2.6613925716641374e-09', '"A2": ((8, 2), 2.5613925716641374e-09'),
 ("T-ancre-A1-ordre2", '2.3236497766513317e-10, 0.002118984943055927),\n    "A2"', '2.3336497766513317e-10, 0.002118984943055927),\n    "A2"'),
 ("T-ancre-A2-ordre2", '2.794344791699548e-09, -0.0028201377357584354),\n}', '2.784344791699548e-09, -0.0028201377357584354),\n}'),
 ("T-ancre-A1-dE", '2.3236497766513317e-10, 0.002118984943055927),\n    "A2"', '2.3236497766513317e-10, 0.002119984943055927),\n    "A2"'),
 ("T-ancre-A2-dE", '2.794344791699548e-09, -0.0028201377357584354),\n}', '2.794344791699548e-09, -0.0028211377357584354),\n}'),
 ("T-bande-proche-borne", 'BANDES = ((PROCHE, 1.25, "0.06")', 'BANDES = ((PROCHE, 1.3, "0.06")'),
 ("T-bande-proche-borne-b", 'BANDES = ((PROCHE, 1.25, "0.06")', 'BANDES = ((PROCHE, 1.2, "0.06")'),
 ("T-bande-moyenne-borne", '(MOYENNE, 1.6, "0.10")', '(MOYENNE, 1.7, "0.10")'),
 ("T-bande-moyenne-borne-b", '(MOYENNE, 1.6, "0.10")', '(MOYENNE, 1.5, "0.10")'),
 ("T-bande-lointaine-borne", '(LOINTAINE, 2.0, "0.12"))', '(LOINTAINE, 2.1, "0.12"))'),
 ("T-bande-lointaine-borne-b", '(LOINTAINE, 2.0, "0.12"))', '(LOINTAINE, 1.9, "0.12"))'),
 ("T-bande-proche-limite", 'BANDES = ((PROCHE, 1.25, "0.06")', 'BANDES = ((PROCHE, 1.25, "0.07")'),
 ("T-bande-moyenne-limite", '(MOYENNE, 1.6, "0.10")', '(MOYENNE, 1.6, "0.11")'),
 ("T-bande-ordre", 'BANDES = ((PROCHE, 1.25, "0.06"), (MOYENNE, 1.6, "0.10"), (LOINTAINE, 2.0, "0.12"))',
                   'BANDES = ((MOYENNE, 1.6, "0.10"), (PROCHE, 1.25, "0.06"), (LOINTAINE, 2.0, "0.12"))'),
 ("T-canon-moteur", 'MOTEUR_CANON = "82a0be882568fe0c"', 'MOTEUR_CANON = "82a0be882568fe0d"'),
 ("T-canon-sonde", 'SONDE_CANON = "', 'SONDE_CANON = "0'),
]
# ---------------------------------------------------------------- (C) le code
ALT += [
 ("C01", 'SIGMA_J_MAX = 0.2', 'SIGMA_J_MAX = 0.25'),
 ("C02", 'POIDS_SITE_MIN = 0.5', 'POIDS_SITE_MIN = 0.45'),
 ("C03", 'DIX_PLANCHERS = 1.33e-12', 'DIX_PLANCHERS = 1.0e-12'),
 ("C04", 'SUIVI_MIN = 0.9', 'SUIVI_MIN = 0.8'),
 ("C05", 'STABILITE_CIBLE = 2.0 ', 'STABILITE_CIBLE = 2.5 '),
 ("C05b", 'STABILITE_CIBLE = 2.0 ', 'STABILITE_CIBLE = 1.9 '),
 ("C06", 'ETALEMENT_CHAINE = 2.0 ', 'ETALEMENT_CHAINE = 3.0 '),
 ("C06b", 'ETALEMENT_CHAINE = 2.0 ', 'ETALEMENT_CHAINE = 1.9 '),
 ("C07", 'MIN_JUGES = 6 ', 'MIN_JUGES = 5 '),
 ("C07b", 'MIN_JUGES = 6 ', 'MIN_JUGES = 7 '),
 ("C08", 'MIN_LISIBLES_BANDE = 3 ', 'MIN_LISIBLES_BANDE = 2 '),
 ("C08b", 'MIN_LISIBLES_BANDE = 3 ', 'MIN_LISIBLES_BANDE = 4 '),
 ("C09", 'TOL_ANCRE = 1e-2 ', 'TOL_ANCRE = 2e-2 '),
 ("C09b", 'TOL_ANCRE = 1e-2 ', 'TOL_ANCRE = 4e-3 '),
 ("C10", 'TOL_ANCRE_O2 = 1e-3 ', 'TOL_ANCRE_O2 = 3e-3 '),
 ("C10b", 'TOL_ANCRE_O2 = 1e-3 ', 'TOL_ANCRE_O2 = 3e-4 '),
 ("C11", 'TOL_ANCRE_DE = 1e-6 ', 'TOL_ANCRE_DE = 1e-4 '),
 ("C11b", 'TOL_ANCRE_DE = 1e-6 ', 'TOL_ANCRE_DE = 1e-8 '),
 ("C12", 'TOL_GARDE = 5e-5 ', 'TOL_GARDE = 5e-4 '),
 ("C12b", 'TOL_GARDE = 5e-5 ', 'TOL_GARDE = 5e-6 '),
 ("C13", 'PLANCHER = 1.33e-13 ', 'PLANCHER = 2.66e-13 '),
 ("C13b", 'PLANCHER = 1.33e-13 ', 'PLANCHER = 0.66e-13 '),
 ("C13c", 'PLANCHER = 1.33e-13 ', 'PLANCHER = 0.0 '),
 ("C14", 'TOL_ENERGIE = 1e-2 ', 'TOL_ENERGIE = 2e-2 '),
 ("C14b", 'TOL_ENERGIE = 1e-2 ', 'TOL_ENERGIE = 5e-3 '),
 ("C15", 'N_ETATS = 14', 'N_ETATS = 13'),
 ("C20", 'return (g3 - PLANCHER) / borne <= g2 <= borne * (g3 + PLANCHER)', 'return (g3 - PLANCHER) / borne <= g2'),
 ("C21", 'return (g3 - PLANCHER) / borne <= g2 <= borne * (g3 + PLANCHER)', 'return g2 <= borne * (g3 + PLANCHER)'),
 ("C22", 'return (g3 - PLANCHER) / borne <= g2 <= borne * (g3 + PLANCHER)', 'return (g3 - PLANCHER) / borne <= g2 <= borne * g3'),
 ("C23", 'return (g3 - PLANCHER) / borne <= g2 <= borne * (g3 + PLANCHER)', 'return g3 / borne <= g2 <= borne * (g3 + PLANCHER)'),
 ("C24", 'g2 = c2["gammas_flux"][2]', 'g2 = c2["gammas_flux"][1]'),
 ("C25", 'g2 = c2["gammas_flux"][2]', 'g2 = c2["gammas_im"][2]'),
 ("C26", 'g3 = e["Gamma_2D"]["3"]; g1 = e["chaine"]["gammas"][2]', 'g3 = e["Gamma_2D"]["2"]; g1 = e["chaine"]["gammas"][2]'),
 ("C27", 'g3 = e["Gamma_2D"]["3"]; g1 = e["chaine"]["gammas"][2]', 'g3 = e["Gamma_2D"]["3"]; g1 = e["chaine"]["gammas"][1]'),
 ("C28", 'de_2d = e["E_re"] - e["E_libre"]; de_c2 = c2["dE"][2]', 'de_2d = e["E_re"] - e["E_libre"]; de_c2 = c2["dE"][1]'),
 ("C29", 'de_2d = e["E_re"] - e["E_libre"]; de_c2 = c2["dE"][2]', 'de_2d = e["E_re"]; de_c2 = c2["dE"][2]'),
 ("C30", 'ecart_e = abs(de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else float("inf")', 'ecart_e = (de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else float("inf")'),
 ("C31", 'ecart_e = abs(de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else float("inf")', 'ecart_e = abs(de_c2 - de_2d) / de_2d if de_2d != 0.0 else float("inf")'),
 ("C32", 'ecart_e = abs(de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else float("inf")', 'ecart_e = abs(de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else 0.0'),
 ("C33", '"energie_tenue": bool(ecart_e <= TOL_ENERGIE)', '"energie_tenue": bool(ecart_e <= TOL_ENERGIE or True)'),
 ("C34", 'pire1 = max(abs(math.log(q)) for q in q1s); pire2 = max(abs(math.log(q)) for q in q2s)', 'pire1 = mediane([abs(math.log(q)) for q in q1s]); pire2 = max(abs(math.log(q)) for q in q2s)'),
 ("C35", 'pire1 = max(abs(math.log(q)) for q in q1s); pire2 = max(abs(math.log(q)) for q in q2s)', 'pire1 = max(abs(math.log(q)) for q in q1s); pire2 = mediane([abs(math.log(q)) for q in q2s])'),
 ("C36", 'pire1 = max(abs(math.log(q)) for q in q1s); pire2 = max(abs(math.log(q)) for q in q2s)', 'pire1 = max(abs(math.log(q)) for q in q1s); pire2 = max(math.log(q) for q in q2s)'),
 ("C37", '"comparaison": ("MIEUX" if pire2 < pire1 else "PAS MIEUX")', '"comparaison": ("MIEUX" if pire2 <= pire1 else "PAS MIEUX")'),
 ("C38", '("TENU" if all(x["dans_borne"] for x in juges) else "TOMBE")', '("TENU" if any(x["dans_borne"] for x in juges) else "TOMBE")'),
 ("C39", '"energie": ("TENUE" if all(x["energie_tenue"] for x in juges) else "NON TENUE")', '"energie": ("TENUE" if any(x["energie_tenue"] for x in juges) else "NON TENUE")'),
 ("C40", 'vus[(e["n1"], e["n2"])] > 1', 'vus[(e["n1"], e["n2"])] > 2'),
 ("C41", 'if len(juges) < MIN_JUGES:', 'if len(juges) <= MIN_JUGES:'),
 ("C42", '"palier": (None if any(p is None for p in paliers) else max(paliers))', '"palier": (None if any(p is None for p in paliers) else min(paliers))'),
 ("C50", 'if not (e["J_ecart_type"] < SIGMA_J_MAX):', 'if not (e["J_ecart_type"] <= SIGMA_J_MAX):'),
 ("C51", 'if e["n1"] < 0 or e["n2"] < 0:', 'if e["n1"] < 0:'),
 ("C51b", 'if e["n1"] < 0 or e["n2"] < 0:', 'if e["n2"] < 0:'),
 ("C52", 'if not (e["poids_site"] >= POIDS_SITE_MIN):', 'if not (e["poids_site"] > POIDS_SITE_MIN):'),
 ("C53", 'if not (g3 > DIX_PLANCHERS):', 'if not (g3 >= DIX_PLANCHERS):'),
 ("C54", 'if min(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:', 'if max(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:'),
 ("C54b", 'if min(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:', 'if min(e["suivi"]["2"], e["suivi"]["4"]) <= SUIVI_MIN:'),
 ("C55", 'gs = [e["Gamma_2D"][k] for k in ("2", "3", "4")]', 'gs = [e["Gamma_2D"][k] for k in ("3", "4")]'),
 ("C55b", 'gs = [e["Gamma_2D"][k] for k in ("2", "3", "4")]', 'gs = [e["Gamma_2D"][k] for k in ("2", "3")]'),
 ("C56", 'if min(gs) <= 0 or max(gs) / min(gs) > STABILITE_CIBLE:', 'if max(gs) / min(gs) > STABILITE_CIBLE:'),
 ("C56b", 'if min(gs) <= 0 or max(gs) / min(gs) > STABILITE_CIBLE:', 'if min(gs) <= 0 or max(gs) / min(gs) >= STABILITE_CIBLE:'),
 ("C57", '    if ch.get("erreur"):', '    if False:'),
 ("C58", '    if ch.get("vide") or not ch.get("definie"):', '    if ch.get("vide"):'),
 ("C58b", '    if ch.get("vide") or not ch.get("definie"):', '    if not ch.get("definie"):'),
 ("C59", 'if min(cg) <= 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:', 'if max(cg) / min(cg) > ETALEMENT_CHAINE:'),
 ("C59b", 'if min(cg) <= 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:', 'if min(cg) <= 0 or max(cg[:3]) / min(cg[:3]) > ETALEMENT_CHAINE:'),
 ("C60", '    if c2.get("erreur"):\n        return "ordre 2 en erreur"', '    if False:\n        return "ordre 2 en erreur"'),
 ("C61", '    if not c2.get("definie"):\n        return "ordre 2 non defini"', '    if False:\n        return "ordre 2 non defini"'),
 ("C62", 'if min(fg) <= 0 or max(fg) / min(fg) > ETALEMENT_CHAINE:', 'if max(fg) / min(fg) > ETALEMENT_CHAINE:'),
 ("C62b", 'if min(fg) <= 0 or max(fg) / min(fg) > ETALEMENT_CHAINE:', 'if min(fg) <= 0 or max(fg[1:]) / min(fg[1:]) > ETALEMENT_CHAINE:'),
 ("C62c", 'if min(fg) <= 0 or max(fg) / min(fg) > ETALEMENT_CHAINE:', 'if min(fg) <= 0 or max(fg[:3]) / min(fg[:3]) > ETALEMENT_CHAINE:'),
 ("C62d", 'if min(fg) <= 0 or max(fg) / min(fg) > ETALEMENT_CHAINE:', 'if min(fg) <= 0 or max(fg) / min(fg) >= ETALEMENT_CHAINE:'),
 ("C70", 'juges = [par_id[k] for k in sorted(ATTENDUS) if ATTENDUS[k][0] == "juge"]', 'juges = [par_id[k] for k in sorted(ATTENDUS) if k in par_id]'),
 ("C71", 'tombes = sorted(x["id"] for x in lis if x[cle] == "TOMBE")', 'tombes = sorted(x["id"] for x in lis if x[cle] == "TENU")'),
 ("C72", 'if len(lis) < MIN_LISIBLES_BANDE:', 'if len(lis) <= MIN_LISIBLES_BANDE:'),
 ("C73", 'issue = "TENUE" if not tombes else "NON TENUE"', 'issue = "TENUE" if len(tombes) < 2 else "NON TENUE"'),
 ("C74", '            if i > 0:\n                v = "L\'ORDRE 2 TIENT JUSQU\'A " + BANDES[i - 1][2]', '            if i > 0:\n                v = "L\'ORDRE 2 TIENT JUSQU\'A " + BANDES[i][2]'),
 ("C75", '    for i in range(len(BANDES) - 1, -1, -1):', '    for i in range(len(BANDES)):'),
 ("C76", '            elif bandes[BANDES[0][0]]["issue"] == "NON LISIBLE":\n                v = "NON LISIBLE"', '            elif False:\n                v = "NON LISIBLE"'),
 ("C77", 'pas_mieux = sorted(x["id"] for x in lis if x["comparaison"] != "MIEUX")', 'pas_mieux = sorted(x["id"] for x in lis if x["comparaison"] == "MIEUX")'),
 ("C78", 'sans_energie = sorted(x["id"] for x in lis if x["energie"] != "TENUE")', 'sans_energie = sorted(x["id"] for x in lis if x["energie"] == "TENUE")'),
 ("C79", '    lis = [x for x in juges if x["statut"] != "NON LISIBLE"]\n    pas_mieux', '    lis = [x for x in lus if x["statut"] != "NON LISIBLE"]\n    pas_mieux'),
 ("C100", '"dans_borne_nue": (bool(g3 / borne <= g2 <= borne * g3) if borne else None)', '"dans_borne_nue": (dans_borne(g2, g3, borne) if borne else None)'),
 ("C101", '"dans_borne_nue": (bool(g3 / borne <= g2 <= borne * g3) if borne else None)', '"dans_borne_nue": (bool(g3 / borne <= g2) if borne else None)'),
 ("C102", '"dans_borne_nue": (bool(g3 / borne <= g2 <= borne * g3) if borne else None)', '"dans_borne_nue": (bool(g2 <= borne * g3) if borne else None)'),
 ("C103", '("TENU" if all(x["dans_borne_nue"] for x in juges) else "TOMBE")),', '("TENU" if any(x["dans_borne_nue"] for x in juges) else "TOMBE")),'),
 ("C104", '[[x["n1"], x["n2"]] for x in juges if x["dans_borne"] and not x["dans_borne_nue"]]', '[[x["n1"], x["n2"]] for x in juges if not x["dans_borne_nue"]]'),
 ("C105", '    v_nu, _ = lire_bandes(juges, "statut_sans_marge")', '    v_nu, _ = lire_bandes(juges, "statut")'),
 ("C106", '    v, bandes = lire_bandes(juges, "statut")', '    v, bandes = lire_bandes(juges, "statut_sans_marge")'),
 ("C80", '    if s.get("moteur_canon") != MOTEUR_CANON:', '    if False:'),
 ("C81", '    if s.get("sonde_canon") != SONDE_CANON:', '    if False:'),
 ("C82", 'obligatoires = [k for k in ATTENDUS if ATTENDUS[k][0] != "temoin"]', 'obligatoires = [k for k in ATTENDUS]'),
 ("C82b", 'obligatoires = [k for k in ATTENDUS if ATTENDUS[k][0] != "temoin"]', 'obligatoires = [k for k in ATTENDUS if ATTENDUS[k][0] == "juge"]'),
 ("C83", 'if len(ids) != len(set(ids)) or any(k not in ATTENDUS for k in ids) or', 'if any(k not in ATTENDUS for k in ids) or'),
 ("C84", 'if len(ids) != len(set(ids)) or any(k not in ATTENDUS for k in ids) or', 'if len(ids) != len(set(ids)) or'),
 ("C85", '        if (p["role"], p["w2"], p["facteur"]) != (role, w2, fac):', '        if False:'),
 ("C86", '        if p.get("faisable") and len(p["etats"]) != N_ETATS:', '        if False:'),
 ("C87", '        if abs(p["g"] - p["g_regle"] * eval_fraction(fac)) > 1e-12 * p["g_regle"]:', '        if False:'),
 ("C88", '        motifs += garde_du_moteur(pid, p)', '        pass'),
 ("C89", '    motifs += garde_ancres(pts)\n    return motifs', '    return motifs'),
 ("C90", '    if gm.get("statut") != statut:', '    if False:'),
 ("C91", '    if gm.get("erreur"):', '    if False:'),
 ("C92", '    if not isinstance(gm, dict):', '    if False:'),
 ("C93", '        if ecart > TOL_ANCRE:', '        if False:'),
 ("C94", '        if abs(c2["gammas_flux"][2] / ref_o2 - 1.0) > TOL_ANCRE_O2:', '        if False:'),
 ("C95", '        if abs(c2["dE"][2] / ref_de - 1.0) > TOL_ANCRE_DE:', '        if False:'),
 ("C96", '        if abs(c2["gammas_flux"][2] / ref_o2 - 1.0) > TOL_ANCRE_O2:', '        if abs(c2["gammas_im"][2] / ref_o2 - 1.0) > TOL_ANCRE_O2:'),
 ("C97", '        if len(tr) != 1:', '        if len(tr) < 1:'),
 ("C98", '        if not c2.get("definie") or c2.get("erreur"):', '        if False:'),
 ("C99", '    if motifs:\n        return {"verdict": "NON CONCLUANT D\'INSTRUMENT"', '    if False:\n        return {"verdict": "NON CONCLUANT D\'INSTRUMENT"'),
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
mord = {"T": 0, "C": 0}; total = {"T": 0, "C": 0}; surv = []
for nom, a, b in ALT:
    assert SRC.count(a) == 1, (nom, SRC.count(a))
    assert a != b, nom
    r = joue(SRC.replace(a, b))
    m = (r is not True); fam = nom[0]; mord[fam] += m; total[fam] += 1
    if not m: surv.append(nom)
    print("  %-26s %-7s %s" % (nom, "MORD" if m else "survit", ("(%s)" % r) if isinstance(r, str) else ""))
print("BANC, famille T (la table) : %d alterations, %d mordues, %d survivantes" % (total["T"], mord["T"], total["T"] - mord["T"]))
print("BANC, famille C (le code)  : %d alterations, %d mordues, %d survivantes" % (total["C"], mord["C"], total["C"] - mord["C"]))
print("survivantes : %s" % (" ".join(surv) or "aucune"))
