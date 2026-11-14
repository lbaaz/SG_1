# -*- coding: ascii -*-
"""FEUILLE DE LECTURE DU GEL "LA CHAINE E-A PAR ETAT, HORS PLAGE" -- machine 1, v1, 2026-11-14.
ELLE JUGE ET NE MESURE PAS : elle lit le JSON de la sonde et applique les sections 6 a 9 du gel.
Usage :
  python -P lecture_chaine_par_etat_machine1_v1.py --selftest
  python -P lecture_chaine_par_etat_machine1_v1.py <sonde.json> <verdict.json>
  python -P lecture_chaine_par_etat_machine1_v1.py --essai <sonde.json>     (essai a blanc, non opposable)
"""
import sys, json, math

MOTEUR_CANON = "82a0be882568fe0c"
ATTENDUS = {  # id : (role, w2, facteur)  -- section 4 du gel
    "J1": ("juge", "19/10", "1/1"), "J2": ("juge", "21/10", "1/1"),
    "J3": ("juge", "39/20", "3/2"), "J4": ("juge", "41/20", "3/2"),
    "J5": ("juge", "39/20", "2/3"), "J6": ("juge", "41/20", "2/3"),
    "T1": ("temoin", "49/25", "1/1"), "T2": ("temoin", "51/25", "1/1"),
    "T3": ("temoin", "37/20", "1/1"), "T4": ("temoin", "43/20", "1/1"),
    "A1": ("ancre", "39/20", "1/1"), "A2": ("ancre", "41/20", "1/1"),
}
ANCRES = {"A1": ((7, 2), 2.1623273017950654e-10), "A2": ((8, 2), 2.6613925716641374e-09)}  # lecture du run M17
TOL_ANCRE = 1e-2
N_ETATS = 14
DIX_PLANCHERS = 1.33e-12      # dix fois le plancher du jumeau de la nuit bis (1.330e-13)
SIGMA_J_MAX = 0.2
POIDS_SITE_MIN = 0.5
SUIVI_MIN = 0.9
STABILITE_CIBLE = 2.0         # max / min de Gamma_2D sur k = 2, 3, 4
ETALEMENT_CHAINE = 2.0        # max / min de la chaine sur ses quatre eta (meme exigence que la cible)
MIN_JUGES = 6                 # etats juges par point, sinon NON LISIBLE
MIN_POINTS_LISIBLES = 4       # points juges lisibles, sinon NON LISIBLE

def motif_exclusion(e):
    """None si l'etat est juge, sinon le premier motif d'exclusion, dans l'ordre du gel (section 6)."""
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
    return None

def palier(q):
    if 0.5 <= q <= 2.0:
        return "FACTEUR 2"
    if q * q >= 0.1 and q * q <= 10.0:
        return "DECADE"
    return "HORS DECADE"

ORDRE_PALIER = {"FACTEUR 2": 0, "DECADE": 1, "HORS DECADE": 2}

def lire_point(pt):
    out = {"id": pt["id"], "role": pt["role"], "w2": pt["w2"], "facteur": pt["facteur"], "etats": []}
    if not pt.get("faisable", False):
        out.update({"statut": "NON LISIBLE", "motif": "infaisable (N > N_max)", "n_juges": 0})
        return out
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
            q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"]
            ligne.update({"Gamma_chaine": e["chaine"]["gammas"][2], "q": q, "palier": palier(q)})
            juges.append(ligne)
        out["etats"].append(ligne)
    out["n_juges"] = len(juges)
    if len(juges) < MIN_JUGES:
        out.update({"statut": "NON LISIBLE", "motif": "moins de %d etats juges" % MIN_JUGES})
        return out
    qs = sorted(x["q"] for x in juges)
    pire = max(juges, key=lambda x: ORDRE_PALIER[x["palier"]])
    out.update({"statut": pire["palier"], "q_min": qs[0], "q_max": qs[-1],
                "q_median": 0.5 * (qs[(len(qs) - 1) // 2] + qs[len(qs) // 2]),
                "premier_juge": {k: juges[0][k] for k in ("rang", "n1", "n2", "q", "palier")}})
    return out

def gardes(s):
    motifs = []
    if s.get("moteur_canon") != MOTEUR_CANON:
        motifs.append("G-1 moteur hors canon")
    pts = {p["id"]: p for p in s.get("points", [])}
    if sorted(pts) != sorted(ATTENDUS) or len(s.get("points", [])) != len(ATTENDUS):
        motifs.append("G-2 points : attendu %s" % " ".join(sorted(ATTENDUS)))
    else:
        for pid, (role, w2, fac) in ATTENDUS.items():
            p = pts[pid]
            if (p["role"], p["w2"], p["facteur"]) != (role, w2, fac):
                motifs.append("G-2 point %s : role, w2 ou facteur" % pid)
            if p.get("faisable") and len(p["etats"]) != N_ETATS:
                motifs.append("G-3 point %s : %d etats" % (pid, len(p["etats"])))
            if abs(p["g"] - p["g_regle"] * eval_fraction(fac)) > 1e-12 * p["g_regle"]:
                motifs.append("G-2 point %s : g n'est pas facteur x regle" % pid)
        motifs += garde_ancres(pts)
    return motifs

def eval_fraction(t):
    a, b = t.split("/")
    return float(int(a)) / float(int(b))

def garde_ancres(pts):
    motifs = []
    for pid, ((n1, n2), ref) in ANCRES.items():
        p = pts.get(pid)
        if p is None or not p.get("faisable"):
            motifs.append("G-4 ancre %s absente" % pid); continue
        tr = [e for e in p["etats"] if (e["n1"], e["n2"]) == (n1, n2)]
        if len(tr) != 1:
            motifs.append("G-4 ancre %s : etat (%d,%d) vu %d fois" % (pid, n1, n2, len(tr))); continue
        ecart = abs(tr[0]["Gamma_2D"]["3"] / ref - 1.0)
        if ecart > TOL_ANCRE:
            motifs.append("G-4 ancre %s : ecart %.3e a la lecture du run" % (pid, ecart))
    return motifs

def cascade(s):
    motifs = gardes(s)
    lus = [lire_point(p) for p in s.get("points", [])]
    if motifs:
        return {"verdict": "NON CONCLUANT D'INSTRUMENT", "motifs": motifs, "points": lus}
    juges = [x for x in lus if x["role"] == "juge"]
    lisibles = [x for x in juges if x["statut"] != "NON LISIBLE"]
    if len(lisibles) < MIN_POINTS_LISIBLES:
        v = "NON LISIBLE"
    else:
        tenus = [x for x in lisibles if x["statut"] in ("FACTEUR 2", "DECADE")]
        if len(tenus) == len(lisibles):
            v = "ORDRE DE GRANDEUR TENU HORS PLAGE"
        elif tenus:
            v = "TENU EN PARTIE"
        else:
            v = "NON TENU"
    return {"verdict": v, "motifs": [], "points": lus,
            "points_juges": {x["id"]: x["statut"] for x in juges}}

def afficher(r, titre):
    print(titre)
    for x in r["points"]:
        if x["statut"] == "NON LISIBLE":
            print("  %s %-6s w2=%s x%s : NON LISIBLE (%s), %d etats juges" % (
                x["id"], x["role"], x["w2"], x["facteur"], x["motif"], x["n_juges"]))
        else:
            print("  %s %-6s w2=%s x%s : %-11s  %d etats juges, q de %.3f a %.3f, mediane %.3f ; premier juge (%d,%d) q = %.3f" % (
                x["id"], x["role"], x["w2"], x["facteur"], x["statut"], x["n_juges"], x["q_min"], x["q_max"],
                x["q_median"], x["premier_juge"]["n1"], x["premier_juge"]["n2"], x["premier_juge"]["q"]))
        ex = {}
        for e in x["etats"]:
            if e["exclu"]:
                ex[e["exclu"]] = ex.get(e["exclu"], 0) + 1
        if ex:
            print("      exclus : " + " ; ".join("%s %d" % kv for kv in sorted(ex.items())))
    for m in r["motifs"]:
        print("  MOTIF : " + m)
    print("VERDICT : " + r["verdict"])

# ---------------------------------------------------------------------------------------------- selftest
def etat(rang, n1, n2, g2d, q, **kw):
    e = {"rang": rang, "recouvrement": 0.03, "E_re": 0.0, "J_moyen": float(n1 - 2 * n2), "J_ecart_type": 0.05,
         "n1_moyen": n1 + 0.1, "n2_moyen": n2 + 0.05, "n1": n1, "n2": n2, "poids_site": 0.9, "poids_Fock_max": 0.9,
         "Gamma_2D": {"2": g2d * 1.05, "3": g2d, "4": g2d * 0.97}, "suivi": {"2": 0.999, "4": 0.999},
         "chaine": {"definie": True, "vide": False, "gammas": [g2d * q * f for f in (1.02, 1.01, 1.0, 0.99)],
                    "Lambda": 1.0, "card": 6, "erreur": None}}
    for k, v in kw.items():
        if k in e["chaine"]:
            e["chaine"][k] = v
        else:
            e[k] = v
    return e

def point(pid, qs=None, etats=None):
    role, w2, fac = ATTENDUS[pid]
    if etats is None:
        qs = qs if qs is not None else [1.0] * N_ETATS
        etats = [etat(r, 5 + r, 2, 1e-9, qs[r]) for r in range(N_ETATS)]
    if pid in ANCRES:
        (n1, n2), ref = ANCRES[pid]
        etats = [etat(0, n1, n2, ref, 1.0)] + [etat(r, 20 + r, 2, 1e-9, 1.0) for r in range(1, N_ETATS)]
    return {"id": pid, "role": role, "w2": w2, "facteur": fac, "g_regle": 1e-3, "g": 1e-3 * eval_fraction(fac),
            "faisable": True, "etats": etats}

def jeu(modif=None):
    pts = {pid: point(pid) for pid in ATTENDUS}
    s = {"moteur_canon": MOTEUR_CANON, "points": None}
    if modif:
        modif(pts, s)
    s["points"] = s["points"] if s["points"] is not None else [pts[k] for k in ATTENDUS]
    return s

def selftest():
    cas = []
    def c(nom, attendu, modif=None, sonde=None, point_attendu=None):
        r = cascade(sonde if sonde is not None else jeu(modif))
        ok = (r["verdict"] == attendu)
        if point_attendu:
            pid, st = point_attendu
            ok = ok and [x for x in r["points"] if x["id"] == pid][0]["statut"] == st
        cas.append(ok); print("  %s  %-58s attendu %s ; rendu %s" % ("TIENT" if ok else "MORD ", nom, attendu, r["verdict"]))
    def qsur(pid, r, q):
        def f(pts, s):
            pts[pid]["etats"][r] = etat(r, 5 + r, 2, 1e-9, q)
        return f
    def tous(q, ids):
        def f(pts, s):
            for pid in ids:
                pts[pid] = point(pid, [q] * N_ETATS)
        return f
    J = ["J1", "J2", "J3", "J4", "J5", "J6"]
    c("S01 base saine, tous q = 1", "ORDRE DE GRANDEUR TENU HORS PLAGE", point_attendu=("J1", "FACTEUR 2"))
    c("S02 un etat a q = 2.5 en J2", "ORDRE DE GRANDEUR TENU HORS PLAGE", qsur("J2", 3, 2.5), point_attendu=("J2", "DECADE"))
    c("S03 un etat a q = 4 en J2", "TENU EN PARTIE", qsur("J2", 3, 4.0), point_attendu=("J2", "HORS DECADE"))
    c("S04 un etat a q = 0.3 en J1", "TENU EN PARTIE", qsur("J1", 0, 0.3), point_attendu=("J1", "HORS DECADE"))
    c("S05 les six juges hors decade", "NON TENU", tous(5.0, J))
    c("S06 bords : q = 2 et q = 0.5 restent FACTEUR 2", "ORDRE DE GRANDEUR TENU HORS PLAGE",
      lambda pts, s: (qsur("J3", 0, 2.0)(pts, s), qsur("J3", 1, 0.5)(pts, s)), point_attendu=("J3", "FACTEUR 2"))
    c("S07 q = 0.499 fait DECADE", "ORDRE DE GRANDEUR TENU HORS PLAGE", qsur("J3", 0, 0.499), point_attendu=("J3", "DECADE"))
    c("S08 q = 3.17 fait HORS DECADE, 3.16 fait DECADE", "TENU EN PARTIE",
      lambda pts, s: (qsur("J3", 0, 3.17)(pts, s), qsur("J4", 0, 3.16)(pts, s)), point_attendu=("J4", "DECADE"))
    def excl(champ, valeur, q=100.0):
        def f(pts, s):
            pts["J2"]["etats"][2] = etat(2, 7, 2, 1e-9, q, **{champ: valeur})
        return f
    c("S09 J flou exclu (q = 100 sans effet)", "ORDRE DE GRANDEUR TENU HORS PLAGE", excl("J_ecart_type", 0.3))
    c("S10 site minoritaire exclu", "ORDRE DE GRANDEUR TENU HORS PLAGE", excl("poids_site", 0.49))
    c("S11 sous dix planchers exclu", "ORDRE DE GRANDEUR TENU HORS PLAGE",
      excl("Gamma_2D", {"2": 1e-12, "3": 1e-12, "4": 1e-12}))
    c("S12 cible instable exclue", "ORDRE DE GRANDEUR TENU HORS PLAGE", excl("Gamma_2D", {"2": 2.1e-9, "3": 1e-9, "4": 1e-9}))
    c("S13 etat non suivi exclu", "ORDRE DE GRANDEUR TENU HORS PLAGE", excl("suivi", {"2": 0.5, "4": 0.999}))
    c("S14 barriere vide exclue", "ORDRE DE GRANDEUR TENU HORS PLAGE", excl("vide", True))
    c("S15 chaine instable exclue", "ORDRE DE GRANDEUR TENU HORS PLAGE", excl("gammas", [1e-7, 1e-7, 1e-7, 4e-8]))
    c("S16 chaine en erreur exclue", "ORDRE DE GRANDEUR TENU HORS PLAGE", excl("erreur", "SystemExit: ARRET"))
    def double(pts, s):
        pts["J2"]["etats"][2] = etat(2, 6, 2, 1e-9, 100.0)      # meme etiquette que le rang 1 : les deux sont exclus
    c("S17 etiquette en double : les deux exclus", "ORDRE DE GRANDEUR TENU HORS PLAGE", double)
    def peu(ids):
        def f(pts, s):
            for pid in ids:
                pts[pid]["etats"] = [etat(r, 5 + r, 2, 1e-9, 1.0) for r in range(5)] + \
                                    [etat(r, 5 + r, 2, 1e-13, 1.0) for r in range(5, N_ETATS)]
        return f
    c("S18 cinq etats juges en J5 : point NON LISIBLE, verdict tenu", "ORDRE DE GRANDEUR TENU HORS PLAGE",
      peu(["J5"]), point_attendu=("J5", "NON LISIBLE"))
    c("S19 trois points juges illisibles", "NON LISIBLE", peu(["J4", "J5", "J6"]))
    c("S20 un temoin hors decade ne pese pas", "ORDRE DE GRANDEUR TENU HORS PLAGE", tous(50.0, ["T1", "T2", "T3", "T4"]))
    def ancre(pts, s):
        pts["A1"]["etats"][0]["Gamma_2D"]["3"] *= 1.02
    c("S21 ancre a 2 pour cent", "NON CONCLUANT D'INSTRUMENT", ancre)
    def ancre_abs(pts, s):
        pts["A2"]["etats"][0]["n1"] = 9
    c("S22 etat d'ancre absent", "NON CONCLUANT D'INSTRUMENT", ancre_abs)
    def moteur(pts, s):
        s["moteur_canon"] = "0000000000000000"
    c("S23 moteur hors canon", "NON CONCLUANT D'INSTRUMENT", moteur)
    def manque(pts, s):
        s["points"] = [pts[k] for k in ATTENDUS if k != "T3"]
    c("S24 un point manque", "NON CONCLUANT D'INSTRUMENT", manque)
    def mauvais_g(pts, s):
        pts["J3"]["g"] = pts["J3"]["g_regle"]
    c("S25 g n'est pas facteur x regle", "NON CONCLUANT D'INSTRUMENT", mauvais_g)
    def infaisable(pts, s):
        pts["J6"]["faisable"] = False
    c("S26 point infaisable : NON LISIBLE au point", "ORDRE DE GRANDEUR TENU HORS PLAGE", infaisable,
      point_attendu=("J6", "NON LISIBLE"))
    print("SELFTEST : %d cas, %d tenus" % (len(cas), sum(cas)))
    return all(cas)

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--selftest":
        raise SystemExit(0 if selftest() else 1)
    if len(sys.argv) == 3 and sys.argv[1] == "--essai":
        s = json.load(open(sys.argv[2], encoding="ascii"))
        pts = {p["id"]: p for p in s["points"]}
        print("ESSAI A BLANC, NON OPPOSABLE : points presents %s" % " ".join(sorted(pts)))
        print("  moteur au canon : %s" % (s.get("moteur_canon") == MOTEUR_CANON))
        m = garde_ancres(pts)
        print("  garde des ancres : %s" % ("TENUE" if not m else " ; ".join(m)))
        afficher({"points": [lire_point(p) for p in s["points"]], "motifs": [], "verdict": "AUCUN (essai)"}, "lecture des points presents :")
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
