# -*- coding: ascii -*-
"""FEUILLE DE LECTURE DU GEL "LA CHAINE E-A AU SECOND ORDRE" -- machine 1, v1, 2026-11-14.
ELLE JUGE ET NE MESURE PAS : elle lit le JSON de la sonde et applique les sections 5 a 10 du gel.
Les neuf criteres d'etat du gel precedent sont repris (motif_exclusion de 0a760e3a244e547d), suivis de trois
criteres sur la chaine d'ordre 2. Tout le reste est neuf : les bandes de desaccord et leurs bornes, la marge de
bruit d'un plancher, la comparaison au pire etat, les energies, les gardes G-7 et G-8.
Le selftest ne construit AUCUN cas a partir de la table ATTENDUS : il porte sa propre copie de la section 4 du
gel (TEMOIN_SECTION_4) et ses propres references d'ancre (regle candidate nee du defaut D-G1-1).
Usage :
  python -P lecture_ordre2_machine1_v1.py --selftest
  python -P lecture_ordre2_machine1_v1.py <sonde.json> <verdict.json>
  python -P lecture_ordre2_machine1_v1.py --essai <sonde.json>     (essai a blanc, non opposable)
"""
import sys, json, math, copy

MOTEUR_CANON = "82a0be882568fe0c"
SONDE_CANON = "24315c52b234319c"
EN, HORS = "EN DOMAINE", "HORS DOMAINE"
PROCHE, MOYENNE, LOINTAINE = "proche", "moyenne", "lointaine"
BANDES = ((PROCHE, 1.25, "0.06"), (MOYENNE, 1.6, "0.10"), (LOINTAINE, 2.0, "0.12"))   # dans l'ordre de la cascade
ATTENDUS = {  # id : (role, w2, facteur, bande, garde du moteur, D1, c_max)  -- section 4 du gel
    "C1": ("juge", "197/100", "2/3", PROCHE, EN, 0.031915, 0.039186),
    "C2": ("juge", "97/50", "3/4", PROCHE, EN, 0.068182, 0.066595),
    "C3": ("juge", "203/100", "3/2", PROCHE, EN, 0.030000, 0.022594),
    "C4": ("juge", "103/50", "4/3", PROCHE, EN, 0.060000, 0.046008),
    "M1": ("juge", "193/100", "1/1", MOYENNE, EN, 0.081395, 0.059553),
    "M2": ("juge", "48/25", "4/3", MOYENNE, EN, 0.095238, 0.069702),
    "M3": ("juge", "207/100", "2/3", MOYENNE, EN, 0.070000, 0.090110),
    "M4": ("juge", "21/10", "3/4", MOYENNE, HORS, 0.100000, 0.130464),
    "L1": ("juge", "189/100", "4/3", LOINTAINE, HORS, 0.141026, 0.102322),
    "L2": ("juge", "47/25", "1/1", LOINTAINE, HORS, 0.157895, 0.114482),
    "L3": ("juge", "211/100", "3/2", LOINTAINE, EN, 0.110000, 0.086367),
    "L4": ("juge", "53/25", "2/3", LOINTAINE, HORS, 0.120000, 0.158143),
    "A1": ("ancre", "39/20", "1/1", None, EN, 0.055556, 0.040917),
    "A2": ("ancre", "41/20", "1/1", None, EN, 0.050000, 0.051012),
    "W1": ("temoin", "107/50", "1/1", None, HORS, 0.140000, 0.148692),
    "W2": ("temoin", "209/100", "1/2", None, HORS, 0.090000, 0.139955),
}
ANCRES = {  # id : (etiquette, Gamma_2D(3) lue par M17, Gamma d'ordre 2 de reference, dE d'ordre 2 de reference)
    "A1": ((7, 2), 2.1623273017950654e-10, 2.3236497766513317e-10, 0.002118984943055927),
    "A2": ((8, 2), 2.6613925716641374e-09, 2.794344791699548e-09, -0.0028201377357584354),
}
TOL_ANCRE = 1e-2              # G-4 : Gamma_2D(3) de l'etat d'ancre contre la lecture du run de M17
TOL_ANCRE_O2 = 1e-3           # G-8 : Gamma d'ordre 2 de l'etat d'ancre contre la reference de machine 1
TOL_ANCRE_DE = 1e-6           # G-8 : dE d'ordre 2 de l'etat d'ancre contre la reference, en relatif
TOL_GARDE = 5e-5              # G-6 : D1 et c_max du moteur contre la table du gel, donnee a six decimales
N_ETATS = 14
PLANCHER = 1.33e-13           # le plancher du jumeau de la nuit bis ; c'est la marge de bruit de la borne
DIX_PLANCHERS = 1.33e-12
SIGMA_J_MAX = 0.2
POIDS_SITE_MIN = 0.5
SUIVI_MIN = 0.9
STABILITE_CIBLE = 2.0         # max / min de Gamma_2D sur k = 2, 3, 4
ETALEMENT_CHAINE = 2.0        # max / min d'une chaine sur ses quatre eta, ordre 1 comme ordre 2
TOL_ENERGIE = 1e-2            # ecart relatif admis entre le decalage d'energie de la chaine d'ordre 2 et celui de la 2D
MIN_JUGES = 6                 # etats juges par point, sinon NON LISIBLE
MIN_LISIBLES_BANDE = 3        # points lisibles par bande (sur quatre), sinon la bande est NON LISIBLE
B_LOI = 2.87                  # loi post hoc de la note 022d32238a66df6b, pour une lecture declaree seulement

def motif_exclusion(e):
    """None si l'etat est juge, sinon le premier motif d'exclusion, dans l'ordre du gel (section 5)."""
    if not (e["J_ecart_type"] < SIGMA_J_MAX):
        return "J flou"
    if e["n1"] < 0 or e["n2"] < 0:
        return "etiquette hors domaine"
    if not (e["poids_site"] >= POIDS_SITE_MIN):
        return "site minoritaire"
    g3 = e["Gamma_2D"]["3"]
    if not (g3 > DIX_PLANCHERS):
        return "sous dix planchers"
    gs = [e["Gamma_2D"][k] for k in ("2", "3", "4")]
    if min(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:
        return "etat non suivi"
    if min(gs) <= 0 or max(gs) / min(gs) > STABILITE_CIBLE:
        return "cible instable"
    ch = e["chaine"]
    if ch.get("erreur"):
        return "chaine en erreur"
    if ch.get("vide") or not ch.get("definie"):
        return "barriere vide"
    cg = ch["gammas"]
    if min(cg) <= 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:
        return "chaine instable"
    c2 = e.get("chaine2") or {}
    if c2.get("erreur"):
        return "ordre 2 en erreur"
    if not c2.get("definie"):
        return "ordre 2 non defini"
    fg = c2["gammas_flux"]
    if min(fg) <= 0 or max(fg) / min(fg) > ETALEMENT_CHAINE:
        return "ordre 2 instable"
    return None

def dans_borne(g2, g3, borne):
    """La chaine d'ordre 2 rend la lecture 2D a un facteur 'borne' pres, a un plancher pres sur la lecture 2D."""
    return (g3 - PLANCHER) / borne <= g2 <= borne * (g3 + PLANCHER)

def palier_atteint(g2, g3):
    for (_, borne, _) in BANDES:
        if dans_borne(g2, g3, borne):
            return borne
    return None

def eval_fraction(t):
    a, b = t.split("/")
    return float(int(a)) / float(int(b))

def mediane(xs):
    xs = sorted(xs)
    return 0.5 * (xs[(len(xs) - 1) // 2] + xs[len(xs) // 2])

def lire_point(pt):
    pid = pt["id"]
    bande = ATTENDUS[pid][3] if pid in ATTENDUS else None
    borne = dict((b[0], b[1]) for b in BANDES).get(bande)
    out = {"id": pid, "role": pt["role"], "w2": pt["w2"], "facteur": pt["facteur"], "bande": bande, "borne": borne,
           "etats": [], "garde_moteur": (pt.get("garde_moteur") or {}).get("statut")}
    if not pt.get("faisable", False):
        out.update({"statut": "NON LISIBLE", "motif": "infaisable (N > N_max)", "n_juges": 0})
        return out
    delta = eval_fraction(pt["w2"]) - 2.0
    vus = {}
    for e in pt["etats"]:
        vus[(e["n1"], e["n2"])] = vus.get((e["n1"], e["n2"]), 0) + 1
    juges = []
    for e in pt["etats"]:
        m = motif_exclusion(e)
        if m is None and vus[(e["n1"], e["n2"])] > 1:
            m = "etiquette en double"
        ligne = {"rang": e["rang"], "n1": e["n1"], "n2": e["n2"], "Gamma_2D": e["Gamma_2D"]["3"], "exclu": m}
        if m is None:
            g3 = e["Gamma_2D"]["3"]; g1 = e["chaine"]["gammas"][2]; c2 = e["chaine2"]; g2 = c2["gammas_flux"][2]
            de_2d = e["E_re"] - e["E_libre"]; de_c2 = c2["dE"][2]
            ecart_e = abs(de_c2 - de_2d) / abs(de_2d) if de_2d != 0.0 else float("inf")
            pa = palier_atteint(g2, g3)
            ligne.update({"Gamma_chaine": g1, "Gamma_ordre2": g2, "q1": g1 / g3, "q2": g2 / g3,
                          "palier": pa, "dans_borne": (dans_borne(g2, g3, borne) if borne else None),
                          "dans_borne_nue": (bool(g3 / borne <= g2 <= borne * g3) if borne else None),
                          "dE_2D": de_2d, "dE_ordre2": de_c2, "ecart_energie": ecart_e,
                          "energie_tenue": bool(ecart_e <= TOL_ENERGIE),
                          "q2_sur_loi": (g2 / g3) / math.exp(B_LOI * delta * delta * c2["m_bord"]),
                          "flux_contre_im": abs(c2["gammas_im"][2] / g2 - 1.0)})
            juges.append(ligne)
        out["etats"].append(ligne)
    out["n_juges"] = len(juges)
    if len(juges) < MIN_JUGES:
        out.update({"statut": "NON LISIBLE", "motif": "moins de %d etats juges" % MIN_JUGES})
        return out
    q1s = [x["q1"] for x in juges]; q2s = [x["q2"] for x in juges]
    pire1 = max(abs(math.log(q)) for q in q1s); pire2 = max(abs(math.log(q)) for q in q2s)
    paliers = [x["palier"] for x in juges]
    out.update({"statut": ("LU" if borne is None else ("TENU" if all(x["dans_borne"] for x in juges) else "TOMBE")),
                "hors_borne": (None if borne is None else sum(1 for x in juges if not x["dans_borne"])),
                "statut_sans_marge": (None if borne is None else
                                      ("TENU" if all(x["dans_borne_nue"] for x in juges) else "TOMBE")),
                "gardes_par_la_marge": ([] if borne is None else
                                        [[x["n1"], x["n2"]] for x in juges if x["dans_borne"] and not x["dans_borne_nue"]]),
                "palier": (None if any(p is None for p in paliers) else max(paliers)),
                "q2_min": min(q2s), "q2_max": max(q2s), "q2_median": mediane(q2s),
                "q1_min": min(q1s), "q1_max": max(q1s), "q1_median": mediane(q1s),
                "pire_ordre1": pire1, "pire_ordre2": pire2, "comparaison": ("MIEUX" if pire2 < pire1 else "PAS MIEUX"),
                "ecart_energie_max": max(x["ecart_energie"] for x in juges),
                "energie": ("TENUE" if all(x["energie_tenue"] for x in juges) else "NON TENUE"),
                "q2_sur_loi_median": mediane([x["q2_sur_loi"] for x in juges]),
                "flux_contre_im_max": max(x["flux_contre_im"] for x in juges),
                "premier_juge": {k: juges[0][k] for k in ("rang", "n1", "n2", "q1", "q2")}})
    return out

def garde_ancres(pts):
    motifs = []
    for pid, ((n1, n2), ref, ref_o2, ref_de) in sorted(ANCRES.items()):
        p = pts.get(pid)
        if p is None or not p.get("faisable"):
            motifs.append("G-4 ancre %s absente" % pid); continue
        tr = [e for e in p["etats"] if (e["n1"], e["n2"]) == (n1, n2)]
        if len(tr) != 1:
            motifs.append("G-4 ancre %s : etat (%d,%d) vu %d fois" % (pid, n1, n2, len(tr))); continue
        ecart = abs(tr[0]["Gamma_2D"]["3"] / ref - 1.0)
        if ecart > TOL_ANCRE:
            motifs.append("G-4 ancre %s : ecart %.3e a la lecture du run" % (pid, ecart))
        c2 = tr[0].get("chaine2") or {}
        if not c2.get("definie") or c2.get("erreur"):
            motifs.append("G-8 ancre %s : chaine d'ordre 2 non definie" % pid); continue
        if abs(c2["gammas_flux"][2] / ref_o2 - 1.0) > TOL_ANCRE_O2:
            motifs.append("G-8 ancre %s : Gamma d'ordre 2 hors de la reference" % pid)
        if abs(c2["dE"][2] / ref_de - 1.0) > TOL_ANCRE_DE:
            motifs.append("G-8 ancre %s : dE d'ordre 2 hors de la reference" % pid)
    return motifs

def garde_du_moteur(pid, p):
    """G-6 : la garde G-1 du moteur, consignee par la sonde, est celle de la table du gel."""
    statut, d1, cmax = ATTENDUS[pid][4:7]
    gm = p.get("garde_moteur")
    if not isinstance(gm, dict):
        return ["G-6 point %s : garde du moteur non consignee" % pid]
    if gm.get("erreur"):
        return ["G-6 point %s : garde du moteur en erreur" % pid]
    if gm.get("statut") != statut:
        return ["G-6 point %s : garde du moteur %s, le gel attend %s" % (pid, gm.get("statut"), statut)]
    if gm.get("D1") is None or gm.get("c_max") is None or \
            abs(gm["D1"] - d1) > TOL_GARDE or abs(gm["c_max"] - cmax) > TOL_GARDE:
        return ["G-6 point %s : D1 ou c_max hors de la table du gel" % pid]
    return []

def gardes(s):
    motifs = []
    if s.get("moteur_canon") != MOTEUR_CANON:
        motifs.append("G-1 moteur hors canon")
    if s.get("sonde_canon") != SONDE_CANON:
        motifs.append("G-7 sonde hors canon")
    ids = [p["id"] for p in s.get("points", [])]
    pts = {p["id"]: p for p in s.get("points", [])}
    obligatoires = [k for k in ATTENDUS if ATTENDUS[k][0] != "temoin"]
    if len(ids) != len(set(ids)) or any(k not in ATTENDUS for k in ids) or any(k not in pts for k in obligatoires):
        motifs.append("G-2 points : attendu %s, temoins facultatifs" % " ".join(sorted(obligatoires)))
        return motifs
    for pid in sorted(pts):
        role, w2, fac = ATTENDUS[pid][0:3]
        p = pts[pid]
        if (p["role"], p["w2"], p["facteur"]) != (role, w2, fac):
            motifs.append("G-2 point %s : role, w2 ou facteur" % pid)
        if p.get("faisable") and len(p["etats"]) != N_ETATS:
            motifs.append("G-3 point %s : %d etats" % (pid, len(p["etats"])))
        if abs(p["g"] - p["g_regle"] * eval_fraction(fac)) > 1e-12 * p["g_regle"]:
            motifs.append("G-2 point %s : g n'est pas facteur x regle" % pid)
        motifs += garde_du_moteur(pid, p)
    motifs += garde_ancres(pts)
    return motifs

def lire_bandes(juges, cle):
    """Sections 6 et 7 : l'issue de chaque bande et le verdict, sur le statut 'cle' des points lisibles."""
    bandes = {}
    for (nom, borne, limite) in BANDES:
        pts = [x for x in juges if x["bande"] == nom]
        lis = [x for x in pts if x["statut"] != "NON LISIBLE"]
        tombes = sorted(x["id"] for x in lis if x[cle] == "TOMBE")
        if len(lis) < MIN_LISIBLES_BANDE:
            issue = "NON LISIBLE"
        else:
            issue = "TENUE" if not tombes else "NON TENUE"
        bandes[nom] = {"issue": issue, "borne": borne, "limite": limite, "lisibles": len(lis), "tombes": tombes}
    v = "L'ORDRE 2 TIENT"                     # la premiere bande qui n'est pas TENUE arrete la lecture
    for i in range(len(BANDES) - 1, -1, -1):
        if bandes[BANDES[i][0]]["issue"] != "TENUE":
            if i > 0:
                v = "L'ORDRE 2 TIENT JUSQU'A " + BANDES[i - 1][2]
            elif bandes[BANDES[0][0]]["issue"] == "NON LISIBLE":
                v = "NON LISIBLE"
            else:
                v = "L'ORDRE 2 NE TIENT PAS"
    return v, bandes

def cascade(s):
    motifs = gardes(s)
    lus = [lire_point(p) for p in s.get("points", []) if p.get("id") in ATTENDUS]
    if motifs:
        return {"verdict": "NON CONCLUANT D'INSTRUMENT", "motifs": motifs, "points": lus}
    par_id = {x["id"]: x for x in lus}
    juges = [par_id[k] for k in sorted(ATTENDUS) if ATTENDUS[k][0] == "juge"]
    v, bandes = lire_bandes(juges, "statut")
    v_nu, _ = lire_bandes(juges, "statut_sans_marge")        # lecture declaree, sans verdict (section 11)
    lis = [x for x in juges if x["statut"] != "NON LISIBLE"]
    pas_mieux = sorted(x["id"] for x in lis if x["comparaison"] != "MIEUX")
    sans_energie = sorted(x["id"] for x in lis if x["energie"] != "TENUE")
    comparaison = {"issue": ("NON LISIBLE" if not lis else
                             ("L'ORDRE 2 FAIT MIEUX PARTOUT" if not pas_mieux else "PAS PARTOUT")),
                   "lisibles": len(lis), "pas_mieux": pas_mieux}
    energie = {"issue": ("NON LISIBLE" if not lis else
                         ("L'ENERGIE TIENT" if not sans_energie else "L'ENERGIE NE TIENT PAS")),
               "lisibles": len(lis), "non_tenue": sans_energie}
    return {"verdict": v, "motifs": [], "points": lus, "bandes": bandes, "comparaison": comparaison,
            "energie": energie, "verdict_sans_marge": v_nu,
            "gardes_par_la_marge": [[x["id"]] + e for x in juges if x["statut"] != "NON LISIBLE"
                                    for e in x["gardes_par_la_marge"]]}

def afficher(r, titre):
    print(titre)
    for x in r["points"]:
        tete = "  %s %-6s w2=%-7s x%s %s" % (x["id"], x["role"], x["w2"], x["facteur"],
                                           ("bande %-9s borne %-4s" % (x["bande"], x["borne"])) if x["bande"]
                                           else "hors enonce              ")
        if x["statut"] == "NON LISIBLE":
            print("%s : NON LISIBLE (%s), %d etats juges" % (tete, x["motif"], x["n_juges"]))
        else:
            print("%s : %-5s %2d juges ; q2 %.3f %.3f %.3f ; q1 %.3f %.3f %.3f ; pire o2 %.3f, o1 %.3f : %-9s ; "
                  "energie %.2e %-9s ; palier %s ; q2/loi %.3f ; flux/im %.1e" % (
                      tete, x["statut"], x["n_juges"], x["q2_min"], x["q2_median"], x["q2_max"],
                      x["q1_min"], x["q1_median"], x["q1_max"], x["pire_ordre2"], x["pire_ordre1"], x["comparaison"],
                      x["ecart_energie_max"], x["energie"], x["palier"] if x["palier"] else "HORS",
                      x["q2_sur_loi_median"], x["flux_contre_im_max"]))
        ex = {}
        for e in x["etats"]:
            if e["exclu"]:
                ex[e["exclu"]] = ex.get(e["exclu"], 0) + 1
        if ex:
            print("      exclus : " + " ; ".join("%s %d" % kv for kv in sorted(ex.items())))
    for m in r["motifs"]:
        print("  MOTIF : " + m)
    if "bandes" in r:
        for (nom, borne, limite) in BANDES:
            b = r["bandes"][nom]
            print("  bande %-9s (|delta| <= %s, borne %s) : %-11s %d lisibles ; tombes : %s" % (
                nom, limite, borne, b["issue"], b["lisibles"], " ".join(b["tombes"]) or "aucun"))
        print("COMPARAISON au pire etat : %s (%d lisibles ; pas mieux : %s)" % (
            r["comparaison"]["issue"], r["comparaison"]["lisibles"], " ".join(r["comparaison"]["pas_mieux"]) or "aucun"))
        print("ENERGIES : %s (%d lisibles ; non tenue : %s)" % (
            r["energie"]["issue"], r["energie"]["lisibles"], " ".join(r["energie"]["non_tenue"]) or "aucun"))
        print("LECTURE SANS MARGE (declaree) : %s ; etats gardes par la marge d'un plancher : %s" % (
            r["verdict_sans_marge"], " ".join("%s(%d,%d)" % tuple(g) for g in r["gardes_par_la_marge"]) or "aucun"))
    print("VERDICT : " + r["verdict"])

# ---------------------------------------------------------------------------------------------- selftest
# Copie INDEPENDANTE de la section 4 du gel, tapee a part : aucun cas ne lit ATTENDUS ni ANCRES.
TEMOIN_SECTION_4 = (
    ("C1", "juge", "197/100", "2/3", "proche", 1.25, "EN DOMAINE", 0.031915, 0.039186),
    ("C2", "juge", "97/50", "3/4", "proche", 1.25, "EN DOMAINE", 0.068182, 0.066595),
    ("C3", "juge", "203/100", "3/2", "proche", 1.25, "EN DOMAINE", 0.030000, 0.022594),
    ("C4", "juge", "103/50", "4/3", "proche", 1.25, "EN DOMAINE", 0.060000, 0.046008),
    ("M1", "juge", "193/100", "1/1", "moyenne", 1.6, "EN DOMAINE", 0.081395, 0.059553),
    ("M2", "juge", "48/25", "4/3", "moyenne", 1.6, "EN DOMAINE", 0.095238, 0.069702),
    ("M3", "juge", "207/100", "2/3", "moyenne", 1.6, "EN DOMAINE", 0.070000, 0.090110),
    ("M4", "juge", "21/10", "3/4", "moyenne", 1.6, "HORS DOMAINE", 0.100000, 0.130464),
    ("L1", "juge", "189/100", "4/3", "lointaine", 2.0, "HORS DOMAINE", 0.141026, 0.102322),
    ("L2", "juge", "47/25", "1/1", "lointaine", 2.0, "HORS DOMAINE", 0.157895, 0.114482),
    ("L3", "juge", "211/100", "3/2", "lointaine", 2.0, "EN DOMAINE", 0.110000, 0.086367),
    ("L4", "juge", "53/25", "2/3", "lointaine", 2.0, "HORS DOMAINE", 0.120000, 0.158143),
    ("A1", "ancre", "39/20", "1/1", None, None, "EN DOMAINE", 0.055556, 0.040917),
    ("A2", "ancre", "41/20", "1/1", None, None, "EN DOMAINE", 0.050000, 0.051012),
    ("W1", "temoin", "107/50", "1/1", None, None, "HORS DOMAINE", 0.140000, 0.148692),
    ("W2", "temoin", "209/100", "1/2", None, None, "HORS DOMAINE", 0.090000, 0.139955),
)
TEMOIN_ANCRES = {"A1": (7, 2, 2.1623273017950654e-10, 2.3236497766513317e-10, 0.002118984943055927),
                 "A2": (8, 2, 2.6613925716641374e-09, 2.794344791699548e-09, -0.0028201377357584354)}
TEMOIN_CANONS = ("82a0be882568fe0c", "24315c52b234319c")
T4 = dict((t[0], t) for t in TEMOIN_SECTION_4)
T_VERDICT_BANDE = {"proche": "L'ORDRE 2 NE TIENT PAS", "moyenne": "L'ORDRE 2 TIENT JUSQU'A 0.06",
                   "lointaine": "L'ORDRE 2 TIENT JUSQU'A 0.10"}

def fr(t):
    a, b = t.split("/")
    return float(int(a)) / float(int(b))

def etat(pid, rang, n1, n2, g2d=1e-9, q2=1.05, q1=0.7, ecart_e=0.001, de=2.0e-3, **kw):
    el = -float(n1) + fr(T4[pid][2]) * n2
    e = {"rang": rang, "recouvrement": 0.03, "E_re": el + de, "E_libre": el, "J_moyen": float(n1 - 2 * n2),
         "J_ecart_type": 0.05, "n1_moyen": n1 + 0.1, "n2_moyen": n2 + 0.05, "n1": n1, "n2": n2, "poids_site": 0.9,
         "poids_Fock_max": 0.9, "Gamma_2D": {"2": g2d * 1.05, "3": g2d, "4": g2d * 0.97},
         "suivi": {"2": 0.999, "4": 0.999},
         "chaine": {"definie": True, "vide": False, "gammas": [g2d * q1 * f for f in (1.02, 1.01, 1.0, 0.99)],
                    "Lambda": 1.0, "card": 6, "erreur": None},
         "chaine2": {"definie": True, "m_bord": 8, "m_min": -2,
                     "gammas_flux": [g2d * q2 * f for f in (1.02, 1.01, 1.0, 0.99)],
                     "gammas_im": [g2d * q2 * f * 1.0001 for f in (1.02, 1.01, 1.0, 0.99)],
                     "dE": [de * (1.0 + ecart_e)] * 4, "Sigma2_0": 1e-4, "erreur": None}}
    for k, v in kw.items():
        if k.startswith("c2_"):
            e["chaine2"][k[3:]] = v
        elif k.startswith("c1_"):
            e["chaine"][k[3:]] = v
        else:
            e[k] = v
    return e

def point(pid, **kw):
    _, role, w2, fac, bande, borne, statut, d1, cmax = T4[pid]
    etats = [etat(pid, r, 5 + r, 2, **kw) for r in range(N_ETATS)]
    if pid in TEMOIN_ANCRES:
        n1, n2, ref, ref_o2, ref_de = TEMOIN_ANCRES[pid]
        etats[0] = etat(pid, 0, n1, n2, g2d=ref, q2=ref_o2 / ref, de=ref_de / 1.001)
        for r in range(1, N_ETATS):
            etats[r] = etat(pid, r, 20 + r, 2, **kw)
    return {"id": pid, "role": role, "w2": w2, "facteur": fac, "g_regle": 1e-3, "g": 1e-3 * fr(fac),
            "faisable": True, "etats": etats,
            "garde_moteur": {"Omega_c": 1.0, "D1": d1, "c_max": cmax, "site_c_max": 3, "statut": statut, "erreur": None}}

def jeu(modif=None):
    pts = dict((t[0], point(t[0])) for t in TEMOIN_SECTION_4)
    s = {"moteur_canon": TEMOIN_CANONS[0], "sonde_canon": TEMOIN_CANONS[1], "points": None}
    if modif:
        modif(pts, s)
    if s["points"] is None:
        s["points"] = [pts[t[0]] for t in TEMOIN_SECTION_4 if t[0] in pts]
    return s

def selftest():
    cas = []
    TIENT, J06, J10, NTP, NL, NC = ("L'ORDRE 2 TIENT", "L'ORDRE 2 TIENT JUSQU'A 0.06", "L'ORDRE 2 TIENT JUSQU'A 0.10",
                                    "L'ORDRE 2 NE TIENT PAS", "NON LISIBLE", "NON CONCLUANT D'INSTRUMENT")
    MIEUX, PASP, ETIENT, ENTP = ("L'ORDRE 2 FAIT MIEUX PARTOUT", "PAS PARTOUT", "L'ENERGIE TIENT",
                                 "L'ENERGIE NE TIENT PAS")
    def c(nom, attendu, modif=None, pt=None, bande=None, comp=None, ener=None, champ=None, nu=None):
        r = cascade(jeu(modif))
        ok = (r["verdict"] == attendu)
        if nu:
            ok = ok and r.get("verdict_sans_marge") == nu[0] and r.get("gardes_par_la_marge") == nu[1]
        if pt:
            ok = ok and [x for x in r["points"] if x["id"] == pt[0]][0]["statut"] == pt[1]
        if bande:
            ok = ok and r.get("bandes", {}).get(bande[0], {}).get("issue") == bande[1]
        if comp:
            ok = ok and r.get("comparaison", {}).get("issue") == comp
        if ener:
            ok = ok and r.get("energie", {}).get("issue") == ener
        if champ:
            x = [y for y in r["points"] if y["id"] == champ[0]][0]
            ok = ok and x.get(champ[1]) == champ[2]
        cas.append(ok)
        print("  %s  %-74s attendu %s ; rendu %s" % ("TIENT" if ok else "MORD ", nom, attendu, r["verdict"]))
    def sur(pid, rang, **kw):
        def f(pts, s):
            pts[pid]["etats"][rang] = etat(pid, rang, 5 + rang, 2, **kw)
        return f
    def tous(pid, **kw):
        def f(pts, s):
            pts[pid] = point(pid, **kw)
        return f
    def et(*fs):
        def f(pts, s):
            for g in fs:
                g(pts, s)
        return f
    # --- la base, et la borne de chaque point juge, des deux cotes (construites sur la copie de la section 4)
    c("S000 base : tout a q2 = 1.05, q1 = 0.7, energie a 1e-3", TIENT, pt=("C1", "TENU"), bande=("proche", "TENUE"),
      comp=MIEUX, ener=ETIENT, champ=("W1", "statut", "LU"))
    c("S001 base : une ancre est lue sans borne", TIENT, pt=("A1", "LU"), champ=("A1", "borne", None))
    c("S002 base : l'autre ancre aussi", TIENT, pt=("A2", "LU"), bande=("moyenne", "TENUE"))
    c("S003 base : le second temoin aussi", TIENT, pt=("W2", "LU"), bande=("lointaine", "TENUE"))
    k = 0
    for t in TEMOIN_SECTION_4:
        if t[1] != "juge":
            continue
        pid, bande, borne = t[0], t[4], t[5]
        k += 1
        c("S1%02d %s : un etat a q2 = borne x 1.01 : le point tombe" % (k, pid), T_VERDICT_BANDE[bande],
          sur(pid, 3, q2=borne * 1.01), pt=(pid, "TOMBE"), bande=(bande, "NON TENUE"), champ=(pid, "hors_borne", 1))
        c("S2%02d %s : un etat a q2 = borne x 0.99 : le point tient" % (k, pid), TIENT,
          sur(pid, 3, q2=borne * 0.99), pt=(pid, "TENU"), bande=(bande, "TENUE"), champ=(pid, "borne", borne))
        c("S3%02d %s : un etat a q2 = 1 / (borne x 1.01) : le point tombe" % (k, pid), T_VERDICT_BANDE[bande],
          sur(pid, 5, q2=1.0 / (borne * 1.01)), pt=(pid, "TOMBE"))
        c("S4%02d %s : un etat a q2 = 1 / (borne x 0.99) : le point tient" % (k, pid), TIENT,
          sur(pid, 5, q2=1.0 / (borne * 0.99)), pt=(pid, "TENU"))
    # --- la marge d'un plancher sur la lecture 2D (a 2e-12, un plancher vaut 6.65 pour cent)
    c("S501 marge : a Gamma_2D = 2e-12, q2 = 1.25 x 1.05 reste dans la borne", TIENT,
      sur("C2", 2, g2d=2e-12, q2=1.25 * 1.05))
    c("S502 marge : a Gamma_2D = 2e-12, q2 = 1.25 x 1.08 en sort", NTP, sur("C2", 2, g2d=2e-12, q2=1.25 * 1.08),
      pt=("C2", "TOMBE"))
    c("S503 marge : a Gamma_2D = 2e-12, q2 = 0.95 / 1.25 reste dans la borne", TIENT,
      sur("C2", 2, g2d=2e-12, q2=0.95 / 1.25))
    c("S504 marge : a Gamma_2D = 2e-12, q2 = 0.92 / 1.25 en sort", NTP, sur("C2", 2, g2d=2e-12, q2=0.92 / 1.25))
    c("S505 marge : a Gamma_2D = 1e-9 elle ne joue pas (q2 = 1.25 x 1.001 sort)", NTP, sur("C2", 2, q2=1.25 * 1.001))
    c("S506 sans marge : a la base, meme verdict et aucun etat garde", TIENT, nu=(TIENT, []))
    c("S507 sans marge : l'etat garde par le haut est nomme, la borne nue l'aurait sorti", TIENT,
      sur("C2", 2, g2d=2e-12, q2=1.25 * 1.05), nu=(NTP, [["C2", 7, 2]]))
    c("S508 sans marge : l'etat garde par le bas, en bande moyenne", TIENT,
      sur("M3", 4, g2d=2e-12, q2=0.95 / 1.6), nu=(J06, [["M3", 9, 2]]))
    c("S509 sans marge : un etat hors des deux bornes n'est pas dit garde", J10, sur("L4", 1, q2=2.5), nu=(J10, []))
    c("S510 sans marge : deux etats gardes en bande lointaine", TIENT,
      et(sur("L1", 0, g2d=2e-12, q2=2.0 * 1.05), sur("L3", 6, g2d=2e-12, q2=0.95 / 2.0)),
      nu=(J10, [["L1", 5, 2], ["L3", 11, 2]]))
    # --- la cascade des bandes
    c("S511 moyenne et lointaine tombees : tient jusqu'a 0.06", J06, et(sur("M2", 1, q2=1.7), sur("L3", 1, q2=2.5)),
      bande=("lointaine", "NON TENUE"))
    c("S512 proche tombee : ne tient pas, quoi que fassent les autres", NTP, et(sur("C4", 1, q2=1.3), sur("L3", 1, q2=2.5)))
    c("S513 palier atteint : q2 = 1.5 a un point de la bande lointaine", TIENT, sur("L1", 0, q2=1.5),
      champ=("L1", "palier", 1.6))
    c("S514 palier atteint : q2 = 1.9", TIENT, sur("L1", 0, q2=1.9), champ=("L1", "palier", 2.0))
    c("S515 palier atteint : q2 = 2.5, aucun", J10, sur("L1", 0, q2=2.5), champ=("L1", "palier", None))
    c("S516 palier atteint a la base : 1.25", TIENT, champ=("M3", "palier", 1.25))
    # --- lisibilite des points et des bandes
    def peu(ids, n=5):
        def f(pts, s):
            for pid in ids:
                pts[pid]["etats"] = [etat(pid, r, 5 + r, 2) for r in range(n)] + \
                                    [etat(pid, r, 5 + r, 2, g2d=1e-13) for r in range(n, N_ETATS)]
        return f
    c("S521 cinq etats juges en C1 : point NON LISIBLE, trois lisibles suffisent", TIENT, peu(["C1"]),
      pt=("C1", "NON LISIBLE"), bande=("proche", "TENUE"))
    c("S522 six etats juges en C1 : point lisible", TIENT, peu(["C1"], 6), pt=("C1", "TENU"))
    c("S523 deux points illisibles en bande proche : NON LISIBLE", NL, peu(["C1", "C3"]), bande=("proche", "NON LISIBLE"))
    c("S524 deux points illisibles en bande moyenne : tient jusqu'a 0.06", J06, peu(["M1", "M4"]),
      bande=("moyenne", "NON LISIBLE"))
    c("S525 deux points illisibles en bande lointaine : tient jusqu'a 0.10", J10, peu(["L2", "L4"]),
      bande=("lointaine", "NON LISIBLE"))
    def infaisable(pid):
        def f(pts, s):
            pts[pid]["faisable"] = False
        return f
    c("S526 point infaisable : NON LISIBLE au point", TIENT, infaisable("M3"), pt=("M3", "NON LISIBLE"))
    c("S527 un point illisible qui serait tombe ne pese pas", TIENT,
      lambda pts, s: pts["C2"].__setitem__("etats", [etat("C2", r, 5 + r, 2, g2d=1e-13, q2=9.0) for r in range(N_ETATS)]),
      pt=("C2", "NON LISIBLE"))
    # --- temoins et ancres ne pesent pas ; les temoins sont facultatifs
    c("S531 temoin W1 tout a q2 = 5 : ne pese pas", TIENT, tous("W1", q2=5.0), champ=("W1", "palier", None))
    c("S532 temoin W2 a l'energie fausse et pas mieux : ne pese pas", TIENT, tous("W2", q1=1.0, ecart_e=0.5),
      comp=MIEUX, ener=ETIENT)
    def sans(pid):
        def f(pts, s):
            del pts[pid]
        return f
    c("S533 temoin W2 absent : la lecture se fait", TIENT, sans("W2"))
    c("S534 les deux temoins absents", TIENT, et(sans("W1"), sans("W2")))
    c("S535 temoin W2 infaisable", TIENT, infaisable("W2"), pt=("W2", "NON LISIBLE"))
    def ancre_autres(pts, s):
        for e in pts["A1"]["etats"][1:]:
            e["chaine2"]["gammas_flux"] = [x * 50.0 for x in e["chaine2"]["gammas_flux"]]
    c("S536 les autres etats d'une ancre a q2 = 50 : ne pese pas", TIENT, ancre_autres, champ=("A1", "palier", None))
    # --- la comparaison au pire etat
    c("S541 M1 tout a q1 = 1.02 : pas mieux, le verdict n'est pas touche", TIENT, tous("M1", q1=1.02), comp=PASP,
      champ=("M1", "comparaison", "PAS MIEUX"))
    c("S542 egalite des pires ecarts : pas mieux (inegalite stricte)", TIENT, tous("M1", q1=1.05), comp=PASP)
    c("S543 un seul etat a q1 = 0.5, les autres a 1.0 : le pire etat decide, mieux", TIENT,
      et(tous("M1", q1=1.0), sur("M1", 4, q1=0.5)), comp=MIEUX)
    c("S544 un seul etat a q2 = 1.5 en M1 : pire ordre 2 au-dessus du pire ordre 1", TIENT, sur("M1", 4, q2=1.5),
      comp=PASP)
    c("S545 le pire etat vers le bas compte aussi : q2 = 0.68 contre q1 = 0.7", TIENT, sur("L1", 4, q2=0.68), comp=PASP)
    c("S546 un point illisible ne pese pas dans la comparaison", TIENT,
      lambda pts, s: pts["C1"].__setitem__("etats", [etat("C1", r, 5 + r, 2, g2d=1e-13, q1=1.0) for r in range(N_ETATS)]),
      comp=MIEUX)
    # --- les energies
    c("S551 un etat a 1.1 pour cent en L3 : l'energie ne tient pas, le verdict n'est pas touche", TIENT,
      sur("L3", 2, ecart_e=0.011), ener=ENTP, champ=("L3", "energie", "NON TENUE"))
    c("S552 un etat a 0.9 pour cent : tenue", TIENT, sur("L3", 2, ecart_e=0.009), ener=ETIENT)
    c("S553 un etat a moins 1.1 pour cent : non tenue", TIENT, sur("C1", 2, ecart_e=-0.011), ener=ENTP)
    c("S554 decalage 2D negatif : l'ecart se lit en valeur absolue", TIENT, tous("M2", de=-3.0e-3), ener=ETIENT)
    c("S555 decalage 2D nul : non tenue", TIENT, sur("M2", 2, de=0.0), ener=ENTP)
    def e_re(pts, s):
        pts["C3"]["etats"][1]["E_re"] += 1.0e-4          # le decalage 2D se lit sur E_re - E_libre
    c("S556 E_re deplace de 1e-4 sur un decalage de 2e-3 : non tenue", TIENT, e_re, ener=ENTP)
    def de_barreau(pts, s):
        pts["C3"]["etats"][1]["chaine2"]["dE"] = [9.0, 9.0, 2.0e-3 * 1.001, 9.0]   # lu au troisieme barreau
    c("S557 dE lu au troisieme barreau", TIENT, de_barreau, ener=ETIENT)
    c("S558 decalage 2D negatif et ecart de 1.1 pour cent : non tenue", TIENT, sur("M2", 2, de=-3.0e-3, ecart_e=0.011),
      ener=ENTP)
    # --- les exclusions : un etat a q2 = 100 en C2 ne pese pas s'il est exclu, pese s'il est juge
    def excl(n1=7, n2=2, **kw):
        def f(pts, s):
            pts["C2"]["etats"][2] = etat("C2", 2, n1, n2, q2=100.0, **kw)
        return f
    c("S601 J flou exclu (ecart-type 0.3)", TIENT, excl(J_ecart_type=0.3))
    c("S602 J flou au bord : 0.2 exactement exclu", TIENT, excl(J_ecart_type=0.2))
    c("S603 J net : 0.19 juge, le point tombe", NTP, excl(J_ecart_type=0.19))
    c("S604 etiquette n2 = -1 exclue", TIENT, excl(n1=7, n2=-1))
    c("S605 etiquette n1 = -1 exclue", TIENT, excl(n1=-1, n2=2))
    c("S606 site minoritaire exclu (0.49)", TIENT, excl(poids_site=0.49))
    c("S607 site au bord : 0.5 juge, le point tombe", NTP, excl(poids_site=0.5))
    c("S608 sous dix planchers exclu (1.2e-12)", TIENT, excl(g2d=1.2e-12))
    c("S609 dix planchers exactement (1.33e-12) exclu", TIENT,
      excl(Gamma_2D={"2": 1.33e-12, "3": 1.33e-12, "4": 1.33e-12}))
    c("S610 juste au-dessus (1.34e-12) juge, le point tombe", NTP, excl(g2d=1.34e-12))
    c("S611 etat non suivi exclu (0.85 a k = 4)", TIENT, excl(suivi={"2": 0.999, "4": 0.85}))
    c("S612 etat non suivi exclu (0.85 a k = 2)", TIENT, excl(suivi={"2": 0.85, "4": 0.999}))
    c("S613 suivi au bord : 0.9 juge, le point tombe", NTP, excl(suivi={"2": 0.9, "4": 0.9}))
    c("S614 cible instable exclue (rapport 2.1 par k = 2)", TIENT, excl(Gamma_2D={"2": 2.1e-9, "3": 1e-9, "4": 1e-9}))
    c("S615 cible instable par k = 4 seul", TIENT, excl(Gamma_2D={"2": 1e-9, "3": 1e-9, "4": 0.45e-9}))
    c("S616 cible au bord : rapport 2 exactement juge", NTP, excl(Gamma_2D={"2": 2e-9, "3": 1e-9, "4": 1e-9}))
    c("S617 cible a valeur nulle exclue", TIENT, excl(Gamma_2D={"2": 0.0, "3": 1e-9, "4": 1e-9}))
    c("S618 cible a valeur negative exclue", TIENT, excl(Gamma_2D={"2": 1e-9, "3": 1e-9, "4": -1e-9}))
    c("S619 barriere vide exclue", TIENT, excl(c1_vide=True))
    c("S620 chaine du moteur non definie exclue", TIENT, excl(c1_definie=False))
    c("S621 chaine du moteur en erreur exclue", TIENT, excl(c1_erreur="SystemExit: ARRET"))
    c("S622 chaine du moteur instable exclue", TIENT, excl(c1_gammas=[1e-9, 1e-9, 1e-9, 4e-10]))
    c("S623 chaine du moteur a valeur nulle exclue", TIENT, excl(c1_gammas=[1e-9, 1e-9, 1e-9, 0.0]))
    c("S624 chaine du moteur a valeur negative exclue", TIENT, excl(c1_gammas=[1e-9, -1e-9, 1e-9, 1e-9]))
    c("S625 ordre 2 en erreur exclu", TIENT, excl(c2_erreur="LinAlgError: x"))
    c("S626 ordre 2 non defini exclu", TIENT, excl(c2_definie=False))
    c("S627 ordre 2 instable exclu (dernier barreau)", TIENT, excl(c2_gammas_flux=[1e-7, 1e-7, 1e-7, 4e-8]))
    c("S628 ordre 2 instable par le premier barreau seul", TIENT, excl(c2_gammas_flux=[2.5e-7, 1e-7, 1e-7, 1e-7]))
    c("S629 ordre 2 a valeur nulle exclu", TIENT, excl(c2_gammas_flux=[1e-7, 1e-7, 1e-7, 0.0]))
    c("S630 ordre 2 a valeur negative exclu", TIENT, excl(c2_gammas_flux=[1e-7, -1e-7, 1e-7, 1e-7]))
    c("S631 ordre 2 au bord : etalement 2 exactement juge, le point tombe", NTP,
      excl(c2_gammas_flux=[2e-7, 1e-7, 1e-7, 1e-7]))
    def double(pts, s):
        pts["C2"]["etats"][2] = etat("C2", 2, 6, 2, q2=100.0)      # meme etiquette que le rang 1 : les deux exclus
    c("S632 etiquette en double : les deux exclus", TIENT, double)
    def chaine2_absente(pts, s):
        e = etat("C2", 2, 7, 2, q2=100.0); del e["chaine2"]
        pts["C2"]["etats"][2] = e
    c("S633 chaine d'ordre 2 non consignee : exclu", TIENT, chaine2_absente)
    # --- ce qui est lu : Gamma_flux et non -2 Im E, au troisieme barreau, contre k = 3
    def lecture_flux(pts, s):
        for e in pts["C4"]["etats"]:
            e["chaine2"]["gammas_im"] = [x * 100.0 for x in e["chaine2"]["gammas_im"]]
    c("S641 q2 se lit sur Gamma_flux, pas sur -2 Im E", TIENT, lecture_flux, pt=("C4", "TENU"))
    def lecture_barreau(pts, s):
        for e in pts["C4"]["etats"]:
            e["chaine2"]["gammas_flux"] = [1.9e-9, 1.9e-9, 1.0e-9, 1.0e-9]
            e["Gamma_2D"] = {"2": 1.9e-9, "3": 1.0e-9, "4": 1.0e-9}
            e["chaine"]["gammas"] = [1.0e-9, 1.0e-9, 0.7e-9, 0.7e-9]
    c("S642 q2 et q1 lus au troisieme barreau et a k = 3", TIENT, lecture_barreau, pt=("C4", "TENU"),
      champ=("C4", "comparaison", "MIEUX"))
    # --- les gardes
    def ancre(pid, champ, f):
        def g(pts, s):
            e = pts[pid]["etats"][0]
            if champ == "2D":
                e["Gamma_2D"]["3"] *= f
            elif champ == "flux":
                e["chaine2"]["gammas_flux"][2] *= f
            else:
                e["chaine2"]["dE"][2] *= f
        return g
    c("S701 G-4 : ancre a 2 pour cent", NC, ancre("A1", "2D", 1.02))
    c("S702 G-4 : ancre a 0.5 pour cent, tenue", TIENT, ancre("A1", "2D", 1.005))
    c("S703 G-4 : l'autre ancre a 1.5 pour cent", NC, ancre("A2", "2D", 0.985))
    c("S704 G-8 : ordre 2 de l'ancre a 0.2 pour cent", NC, ancre("A1", "flux", 1.002))
    c("S705 G-8 : ordre 2 de l'ancre a 0.05 pour cent, tenue", TIENT, ancre("A1", "flux", 1.0005))
    c("S706 G-8 : ordre 2 de l'autre ancre a 0.2 pour cent", NC, ancre("A2", "flux", 0.998))
    c("S707 G-8 : dE de l'ancre a 1e-5", NC, ancre("A2", "dE", 1.00001))
    c("S708 G-8 : dE de l'ancre a 1e-7, tenue", TIENT, ancre("A2", "dE", 1.0000001))
    c("S709 G-8 : dE de l'autre ancre a 1e-5", NC, ancre("A1", "dE", 0.99999))
    def ancre_abs(pts, s):
        pts["A2"]["etats"][0]["n1"] = 9
    c("S710 G-4 : etat d'ancre absent", NC, ancre_abs)
    def ancre_c2(pts, s):
        pts["A1"]["etats"][0]["chaine2"]["definie"] = False
    c("S711 G-8 : ordre 2 non defini a l'etat d'ancre", NC, ancre_c2)
    def ancre_double(pts, s):
        pts["A2"]["etats"][1]["n1"] = 8          # l'etiquette de l'etat d'ancre portee par deux etats
    c("S730 G-4 : etat d'ancre vu deux fois", NC, ancre_double)
    def canon(cle):
        def f(pts, s):
            s[cle] = "0000000000000000"
        return f
    c("S712 G-1 : moteur hors canon", NC, canon("moteur_canon"))
    c("S713 G-7 : sonde hors canon", NC, canon("sonde_canon"))
    c("S714 G-2 : un point juge manque", NC, sans("L2"))
    c("S715 G-2 : une ancre manque", NC, sans("A1"))
    def inconnu(pts, s):
        p = copy.deepcopy(pts["C1"]); p["id"] = "Z9"
        s["points"] = [pts[t[0]] for t in TEMOIN_SECTION_4] + [p]
    c("S716 G-2 : un point inconnu en plus", NC, inconnu)
    def doublon(pts, s):
        s["points"] = [pts[t[0]] for t in TEMOIN_SECTION_4] + [copy.deepcopy(pts["W1"])]
    c("S717 G-2 : un point en double", NC, doublon)
    def champ_pt(pid, cle, v):
        def f(pts, s):
            pts[pid][cle] = v
        return f
    c("S718 G-2 : g n'est pas facteur x regle", NC, champ_pt("M4", "g", 1e-3))
    c("S719 G-2 : w2 d'un point change", NC, champ_pt("C1", "w2", "49/25"))
    c("S720 G-2 : facteur d'un temoin change", NC, champ_pt("W2", "facteur", "2/3"))
    c("S721 G-2 : role d'un point change", NC, champ_pt("L4", "role", "temoin"))
    def treize(pts, s):
        pts["C1"]["etats"] = pts["C1"]["etats"][:13]
    c("S722 G-3 : treize etats a un point", NC, treize)
    def gm(pid, cle, v):
        def f(pts, s):
            pts[pid]["garde_moteur"][cle] = v
        return f
    c("S723 G-6 : la garde du moteur dit HORS a un point EN", NC, gm("C2", "statut", "HORS DOMAINE"))
    c("S724 G-6 : la garde du moteur dit EN a un point HORS", NC, gm("L4", "statut", "EN DOMAINE"))
    c("S725 G-6 : c_max a 1e-4 de la table", NC, gm("M3", "c_max", T4["M3"][8] + 1e-4))
    c("S726 G-6 : D1 a 1e-4 de la table", NC, gm("L1", "D1", T4["L1"][7] - 1e-4))
    c("S727 G-6 : c_max a 4e-5 de la table, tenue", TIENT, gm("M3", "c_max", T4["M3"][8] - 4e-5))
    c("S728 G-6 : garde du moteur en erreur", NC, gm("W1", "erreur", "AssertionError: A4"))
    def sans_garde(pts, s):
        del pts["A1"]["garde_moteur"]
    c("S729 G-6 : garde du moteur non consignee a une ancre", NC, sans_garde)
    print("SELFTEST : %d cas, %d tenus" % (len(cas), sum(cas)))
    return all(cas)

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--selftest":
        raise SystemExit(0 if selftest() else 1)
    if len(sys.argv) == 3 and sys.argv[1] == "--essai":
        s = json.load(open(sys.argv[2], encoding="ascii"))
        pts = {p["id"]: p for p in s["points"]}
        print("ESSAI A BLANC, NON OPPOSABLE : points presents %s" % " ".join(sorted(pts)))
        print("  moteur au canon : %s ; sonde au canon : %s" % (s.get("moteur_canon") == MOTEUR_CANON,
                                                               s.get("sonde_canon") == SONDE_CANON))
        m = garde_ancres(pts)
        print("  gardes G-4 et G-8 aux ancres : %s" % ("TENUES" if not m else " ; ".join(m)))
        m6 = [x for pid in sorted(pts) if pid in ATTENDUS for x in garde_du_moteur(pid, pts[pid])]
        print("  garde G-6 aux points presents : %s" % ("TENUE" if not m6 else " ; ".join(m6)))
        afficher({"points": [lire_point(p) for p in s["points"]], "motifs": [], "verdict": "AUCUN (essai)"},
                 "lecture des points presents :")
        return
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    if not selftest():
        raise SystemExit("selftest en echec : la feuille ne lit pas")
    s = json.load(open(sys.argv[1], encoding="ascii"))
    r = cascade(s)
    afficher(r, "LECTURE DU GEL, sonde %s :" % sys.argv[1])
    json.dump(r, open(sys.argv[2], "w", encoding="ascii"), indent=1, sort_keys=True)

if __name__ == "__main__":
    main()
