# -*- coding: ascii -*-
# FEUILLE DE LECTURE DE LA QUALIFICATION E-B -- machine 1, v2
# v2 = v1 (b3ac958a1a2b915b) + l'echelle du gel bis (bornes de fenetre, un
# cas de G-Q7) + deux refus a l'entree (gel de la sortie ; g de la sonde
# contre g de la table, observation O-2 de m2). Aucun seuil ne change.
# gel E-B bis v1 dcda1611adf5f8fd. CLASSE 2. Elle JUGE et ne mesure pas : aucune
# decomposition, aucun moteur. Routine de plateau (3.11, rationnels exacts),
# accords (3.12), statuts (6), cascade (9), T-etats (7), selftest G-Q7.
import sys, os, json, math, hashlib, unicodedata, argparse
from fractions import Fraction

CANON_GEL = "dcda1611adf5f8fd"
K_MIN, K_MAX = -2, 12                      # echelle du gel bis, 3.6
TAU = Fraction(1, 20)
TAU_F = 0.05
PLANCHER = 1e-12
SEUIL = 0.90
TOL_ANCRAGE = 1e-3
E_RUN_GEL = "3.7027"
POINTS = ["39_20", "197_100", "99_50", "101_50", "203_100", "41_20"]
GAUCHE, DROITE = POINTS[:3], POINTS[3:]
REQUIS = ["F1G20", "F1G30", "F2G20", "F3G20", "F1GT"]


def dire(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    if dire.f:
        dire.f.write(s + "\n")


dire.f = None


def canon_b(octets):
    t = unicodedata.normalize("NFC", octets.decode("utf-8"))
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


def serie(traj, t=0):
    """{k: gamma LISIBLE ou None} pour l'etat t d'une trajectoire (3.10)."""
    out = {}
    for ks, rec in traj.items():
        e = rec["etats"][t]
        g = e.get("gamma") if e.get("suivi") else None
        out[int(ks)] = g if (g is not None and g > PLANCHER) else None
    return out


def plateau(ser):
    """3.11 : fenetre de cinq valeurs lisibles a k consecutifs ; PLATEAU si
    Fraction(max) <= (1 + 1/20) Fraction(min), en rationnels exacts."""
    best = None
    for k0 in range(K_MIN, K_MAX - 3):
        v = [ser.get(k) for k in range(k0, k0 + 5)]
        if any(x is None for x in v):
            continue
        mx, mn = Fraction(max(v)), Fraction(min(v))
        ok = mx <= (1 + TAU) * mn
        cand = (not ok, mx / mn, k0)
        if best is None or cand < best[0]:
            best = (cand, v, ok)
    if best is None:
        return {"statut": "AUCUNE FENETRE"}
    (_, rapport, k0), v, ok = best
    return {"statut": "PLATEAU" if ok else "PAS DE PLATEAU", "k0": k0,
            "etalement": float(rapport) - 1.0,
            "Gamma_pl": math.exp(sum(math.log(x) for x in v) / 5.0)}


def accord(a, b, tau=TAU_F):
    return abs(math.log(a / b)) <= tau


def accord_tp(gamma_pl, gamma_ref, u_ref):
    """5.1 : |ln(Gamma_pl / Gamma_ref)| <= tau + u_ref. Rend (ecart, tient)."""
    e = abs(math.log(gamma_pl / gamma_ref))
    return e, e <= TAU_F + u_ref


def selection_gel(balayage):
    """5.1 : parmi les g_j a Gamma_ref dans [1e-11, 1e-7] et u_ref <= 0.01,
    les deux dont ln(Gamma_ref) est le plus proche de ln(1e-10) et ln(1e-8)."""
    c = [r for r in balayage if 1e-11 <= r["Gamma_ref"] <= 1e-7
         and r["u_ref"] <= 0.01]
    if not c:
        return []
    return sorted(set(min(c, key=lambda r: (abs(math.log(
        r["Gamma_ref"] / x)), r["j"]))["j"] for x in (1e-10, 1e-8)))


def selftest():
    """G-Q7. Rend (ok, lignes)."""
    eta = {k: 0.05 * 2.0 ** (-k) for k in range(K_MIN, K_MAX + 1)}
    T = []

    def t(nom, obtenu, attendu):
        T.append((nom, obtenu == attendu, obtenu, attendu))
    t("gamma = c eta", plateau({k: 3e-7 * eta[k] for k in eta})["statut"],
      "PAS DE PLATEAU")
    t("constante", plateau({k: 2e-10 for k in eta})["statut"], "PLATEAU")
    s = {k: (2e-10 if 2 <= k <= 6 else 2e-10 * eta[k] / eta[2] if k > 6
             else 2e-10 * (1.0 + 0.2 * (2 - k))) for k in eta}
    p = plateau(s)
    t("plateau de cinq puis chute lineaire", (p["statut"], p.get("k0")),
      ("PLATEAU", 2))
    f = {k: (2e-10 if k <= -1 else 2e-10 * eta[k] / eta[-1]) for k in eta}
    p = plateau(f)
    t("plateau au bord fort (k = -5 a -1) puis chute",
      (p["statut"], p.get("k0")), ("PLATEAU", -5))
    q = {k: None for k in eta}
    q.update({0: 1e-9, 1: 1e-9, 2: 1e-9, 3: 1e-9})
    t("quatre valeurs lisibles", plateau(q)["statut"], "AUCUNE FENETRE")
    b = {k: None for k in eta}
    b.update({0: 20.0, 1: 20.25, 2: 20.5, 3: 20.75, 4: 21.0})
    t("borne exacte (20.0 .. 21.0)", plateau(b)["statut"], "PLATEAU")
    b[4] = math.nextafter(21.0, math.inf)
    t("borne + 1 ulp", plateau(b)["statut"], "PAS DE PLATEAU")
    t("accord a tau - 1e-6", accord(math.exp(TAU_F - 1e-6), 1.0), True)
    t("accord a tau + 1e-6", accord(math.exp(TAU_F + 1e-6), 1.0), False)
    t("accord au TP a tau + u - 1e-6",
      accord_tp(math.exp(TAU_F + 0.01 - 1e-6), 1.0, 0.01)[1], True)
    t("accord au TP a tau + u + 1e-6",
      accord_tp(math.exp(TAU_F + 0.01 + 1e-6), 1.0, 0.01)[1], False)
    bal = [{"j": j, "Gamma_ref": 10.0 ** (-13 + j), "u_ref": 0.001}
           for j in range(9)]
    bal[5]["u_ref"] = 0.02
    t("selection du gel sur une table", selection_gel(bal), [3, 4])
    t("plancher : 1e-12 non lisible", serie({"0": {"etats": [
        {"suivi": True, "gamma": 1e-12}]}})[0], None)
    t("non suivi non lisible", serie({"0": {"etats": [
        {"suivi": False, "gamma": 1e-9}]}})[0], None)
    return all(x[1] for x in T), T


def juger_etage1(s1, ref):
    motifs, det = [], {}
    okst, T = selftest()
    for nom, ok, obt, att in T:
        dire("  G-Q7 %-38s %s" % (nom, "OK" if ok else
                                  "MORD (obtenu %s, attendu %s)" % (obt, att)))
    dire("G-Q7 selftest : %d tenus sur %d" % (sum(x[1] for x in T), len(T)))
    if not okst:
        motifs.append("G-Q7")
    if not all(s1["GQ3"].values()) or len(s1["GQ3"]) != 6:
        motifs.append("G-Q3")
    pl = [abs(v) for d in s1["GQ5"].values() for v in d.values()]
    dire("G-Q5 plancher : %d valeurs (attendu 30), max |Gamma(H+)| = %.3e,"
         " seuil %g" % (len(pl), max(pl) if pl else float("nan"), PLANCHER))
    if len(pl) != 30 or max(pl) > PLANCHER:
        motifs.append("G-Q5")
    if not s1.get("GQ10"):
        motifs.append("G-Q10")
    # --- TP -----------------------------------------------------------------
    table = {r["j"]: r for r in ref.get("balayage", [])}
    jr = sorted(r["j"] for r in ref.get("retenus", []))
    js = sorted(v["j"] for v in s1["TP"].values())
    det["TP"] = {}
    jg = selection_gel(ref.get("balayage", []))
    dire("TP selection : sonde %s ; reference %s ; rejouee par la regle du"
         " gel sur la table %s" % (js, jr, jg))
    if not js or js != jr or js != jg:
        motifs.append("TP non concluant (retenus sonde %s, reference %s,"
                      " regle du gel %s)" % (js, jr, jg))
    for cle, v in sorted(s1["TP"].items()):
        r = table.get(v["j"])
        if r is None:
            motifs.append("TP : j = %d absent de la table" % v["j"])
            continue
        tient = True
        det["TP"][cle] = {"Gamma_ref": r["Gamma_ref"], "u_ref": r["u_ref"]}
        for cfg in ("F1G20", "F1G30"):
            p = plateau(serie(v["traj"][cfg]))
            e, ok = (accord_tp(p["Gamma_pl"], r["Gamma_ref"], r["u_ref"])
                     if p["statut"] == "PLATEAU" else (None, False))
            tient = tient and ok
            det["TP"][cle][cfg] = dict(p, ecart_ln=e, tient=ok)
            dire("TP %s g = %.5f %s : %s%s ; Gamma_ref %.4e u_ref %.1e ;"
                 " |ln| = %s contre %.4f : %s" % (
                     cle, v["g"], cfg, p["statut"],
                     " Gamma_pl %.4e etalement %.4f k0 %d" % (
                         p["Gamma_pl"], p["etalement"], p["k0"])
                     if "k0" in p else "", r["Gamma_ref"], r["u_ref"],
                     "%.4f" % e if e is not None else "-",
                     TAU_F + r["u_ref"], "TIENT" if ok else "NE TIENT PAS"))
        if not tient:
            motifs.append("TP ne tient pas a %s" % cle)
    # --- TN -----------------------------------------------------------------
    tn = "NON JOUE"
    for t in range(len(s1["TN"]["candidats"])):
        p = plateau(serie(s1["TN"]["traj"], t))
        dire("TN candidat %d %s : %s%s" % (
            t, s1["TN"]["candidats"][t], p["statut"],
            " (etalement %.3f)" % p["etalement"] if "k0" in p else ""))
        if p["statut"] != "AUCUNE FENETRE":
            tn = p["statut"]
            break
    det["TN"] = tn
    if tn == "PLATEAU":
        motifs.append("TN rend PLATEAU : le critere ne mord pas")
    dire("TN : %s" % tn)
    return ("TIENT" if not motifs else "NE TIENT PAS"), motifs, det


def juger_point(pt):
    P, ech, nl = {}, [], []
    for cfg in REQUIS:
        c = pt["cfg"][cfg]
        if cfg != "F1G20" and c["identite"] < SEUIL:
            P[cfg] = {"statut": "IDENTITE NON ETABLIE",
                      "identite": c["identite"]}
            nl.append(cfg)
            continue
        P[cfg] = plateau(serie(c["traj"]))
        if P[cfg]["statut"] == "AUCUNE FENETRE":
            nl.append(cfg)
        elif P[cfg]["statut"] == "PAS DE PLATEAU":
            ech.append("pas de plateau a %s (meilleur etalement %.4f)"
                       % (cfg, P[cfg]["etalement"]))
    base = P["F1G20"]
    for cfg, ep in (("F1G30", "b"), ("F2G20", "c"), ("F3G20", "c"),
                    ("F1GT", "d")):
        if base["statut"] == "PLATEAU" and P[cfg]["statut"] == "PLATEAU":
            e = abs(math.log(P[cfg]["Gamma_pl"] / base["Gamma_pl"]))
            P[cfg]["ecart_ln_F1G20"] = e
            if e > TAU_F:
                ech.append("(%s) accord %s / F1G20 : |ln| = %.4f" % (ep, cfg, e))
    st = "NON QUALIFIE" if ech else ("NON LISIBLE" if nl else "QUALIFIE")
    e5 = None
    if base["statut"] == "PLATEAU":
        e5 = accord(pt["G_run"], base["Gamma_pl"])
    return {"statut": st, "echecs": ech, "non_lisibles": nl, "plateaux": P,
            "M17_sur_plateau": e5}


def juger_etats(pt):
    c = pt["cfg"]["F1G20"]["traj"]
    r3 = c["3"]
    sc = complex(r3["somme_c_re"], r3["somme_c_im"])
    out = {"somme_c_ecart": abs(sc - 1.0), "kappa": r3["kappa"],
           "c_abs": [abs(complex(a, b)) for a, b in zip(r3["c_re"],
                                                        r3["c_im"])],
           "poids_total": r3["poids_total"]}
    if out["somme_c_ecart"] > 1e-6:
        out["lecture"] = "DECOMPOSITION MAL CONDITIONNEE"
        return out
    pl = [plateau(serie(c, t)) for t in range(len(r3["etats"]))]
    g = [p["Gamma_pl"] for p in pl if p["statut"] == "PLATEAU"]
    out.update({"statuts": [p["statut"] for p in pl], "Gamma_pl": [
        p.get("Gamma_pl") if p["statut"] == "PLATEAU" else None for p in pl],
        "n_plateaux": len(g)})
    out["S_w"] = math.log(max(g) / min(g)) if len(g) >= 3 else None
    return out


def cascade(v1, s2, pts):
    if v1.get("etage1") != "TIENT":
        return "NON CONCLUANT D'INSTRUMENT"
    if s2 is None:
        return "ETAGE 2 NON JOUE"
    if not s2.get("GQ10") or any(
            abs(x["rapport"] - 1.0) > TOL_ANCRAGE for x in s2["GQ4"].values()
            if x["rapport"] is not None):
        return "NON CONCLUANT D'INSTRUMENT"
    nq = sum(1 for p in pts.values() if p["statut"] == "QUALIFIE")
    nn = sum(1 for p in pts.values() if p["statut"] == "NON QUALIFIE")
    if nq == 6:
        return "ESTIMATEUR QUALIFIE"
    if nq >= 1:
        return "QUALIFIE PAR POINT"
    return "NON QUALIFIE" if nn >= 1 else "NON LISIBLE"


def juger_etage2(v1, s2):
    pts = {n: juger_point(s2["points"][n]) for n in POINTS}
    verdict = cascade(v1, s2, pts)
    for n in POINTS:
        p = pts[n]
        dire("point %-8s %-13s plateaux : %s" % (n, p["statut"], " ".join(
            "%s:%s" % (c, ("%.3e/%.3f" % (q["Gamma_pl"], q["etalement"]))
                       if q["statut"] == "PLATEAU" else q["statut"])
            for c, q in p["plateaux"].items())))
        for e in p["echecs"]:
            dire("      echec : %s" % e)
        if p["non_lisibles"]:
            dire("      non lisibles : %s" % p["non_lisibles"])
        dire("      (e) M17 a lu %s" % {True: "sur le plateau", False:
             "HORS plateau", None: "- (pas de plateau a F1G20)"}[
                 p["M17_sur_plateau"]])
    # --- T-etats ------------------------------------------------------------
    G = [s2["points"][n]["G_run"] for n in POINTS]
    e_run = math.log(max(G) / min(G))
    et = {n: juger_etats(s2["points"][n]) for n in POINTS}
    sw = sorted(e["S_w"] for e in et.values() if e.get("S_w") is not None)
    med = (None if not sw else sw[len(sw) // 2] if len(sw) % 2 else
           0.5 * (sw[len(sw) // 2 - 1] + sw[len(sw) // 2]))
    lect = (None if med is None else "FLUCTUATION D'ETAT DOMINANTE"
            if med >= e_run else "STRUCTURE DE GRILLE DOMINANTE")
    dire("T-etats : E_run = %.4f (gel : %s, %s) ; S_w lus %d sur 6 : %s ;"
         " mediane %s -> %s" % (e_run, E_RUN_GEL, "concorde" if "%.4f" % e_run
                                == E_RUN_GEL else "DIFFERE", len(sw),
                                ["%.3f" % x for x in sw],
                                "%.3f" % med if med is not None else "-", lect))
    # --- annonces de la plume (gel 11) --------------------------------------
    q = {n: pts[n]["statut"] == "QUALIFIE" for n in POINTS}
    kap = {n: et[n]["kappa"][0] for n in POINTS}
    ann = {"A-1": verdict, "A-2 (2.02 non qualifie)": not q["101_50"],
           "A-3 (droite >= gauche)": sum(q[n] for n in DROITE) >= sum(
               q[n] for n in GAUCHE),
           "A-4 (fluctuation d'etat dominante)": (
               None if lect is None else lect.startswith("FLUCT")),
           "A-5 (kappa gauche > droite)": min(kap[n] for n in GAUCHE) > max(
               kap[n] for n in DROITE)}
    for k in sorted(ann):
        dire("annonce %s : %s" % (k, ann[k]))
    return verdict, {"points": pts, "T_etats": et, "E_run": e_run,
                     "mediane_S_w": med, "lecture_T_etats": lect,
                     "annonces": ann}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--etage", type=int, choices=[1, 2])
    ap.add_argument("--sortie")
    ap.add_argument("--reference")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        ok, T = selftest()
        for nom, o, obt, att in T:
            print("  %-40s %s" % (nom, "OK" if o else "MORD %s / %s" % (obt, att)))
        print("selftest G-Q7 : %d tenus sur %d" % (sum(x[1] for x in T), len(T)))
        sys.exit(0 if ok else 1)
    dire.f = open(os.path.join(a.sortie, "lecture_etage%d.log" % a.etage), "w")
    dire("=" * 74)
    dire("FEUILLE DE LECTURE E-B v2 -- gel %s -- etage %d" % (CANON_GEL, a.etage))
    dire("=" * 74)
    f1 = os.path.join(a.sortie, "sonde_etage1.json")
    fv = os.path.join(a.sortie, "verdict_etage1.json")
    if a.etage == 1:
        s1 = json.load(open(f1))
        ref = json.load(open(a.reference))
        if s1.get("gel") != CANON_GEL:
            dire("LECTURE REFUSEE : la sortie de la sonde porte le gel %s,"
                 " cette feuille juge le gel %s" % (s1.get("gel"), CANON_GEL))
            sys.exit(2)
        gt = {r["j"]: r["g"] for r in ref["balayage"]}
        for cle in sorted(s1["TP"]):
            if gt.get(s1["TP"][cle]["j"]) != s1["TP"][cle]["g"]:
                dire("LECTURE REFUSEE (O-2) : a %s le g de la sonde (%r) n'est"
                     " pas celui de la table (%r)" % (
                         cle, s1["TP"][cle]["g"], gt.get(s1["TP"][cle]["j"])))
                sys.exit(2)
        if s1.get("prevol"):
            dire("PRE-VOL : geometrie reduite, verdict NON OPPOSABLE")
        v, motifs, det = juger_etage1(s1, ref)
        out = {"etage1": v, "motifs": motifs, "detail": det,
               "prevol": bool(s1.get("prevol")),
               "canon_sonde_etage1": canon_b(open(f1, "rb").read()),
               "canon_reference": canon_b(open(a.reference, "rb").read())}
        json.dump(out, open(fv, "w"), indent=1, sort_keys=True)
        dire("VERDICT DE L'ETAGE 1 : %s %s" % (v, motifs))
    else:
        v1 = json.load(open(fv))
        f2 = os.path.join(a.sortie, "sonde_etage2.json")
        s2 = json.load(open(f2)) if os.path.exists(f2) else None
        if s2 is not None and s2.get("gel") != CANON_GEL:
            dire("LECTURE REFUSEE : la sortie de l'etage 2 porte le gel %s,"
                 " cette feuille juge le gel %s" % (s2.get("gel"), CANON_GEL))
            sys.exit(2)
        if s2 is None or v1.get("etage1") != "TIENT":
            verdict, det = cascade(v1, s2, {}), {}
        else:
            verdict, det = juger_etage2(v1, s2)
        json.dump({"verdict": verdict, "detail": det,
                   "prevol": bool(v1.get("prevol"))},
                  open(os.path.join(a.sortie, "verdict_qualification_EB.json"),
                       "w"), indent=1, sort_keys=True)
        dire("VERDICT : %s%s" % (verdict, " (PRE-VOL, NON OPPOSABLE)"
                                 if v1.get("prevol") else ""))
    dire("feuille %s canon %s (relue du disque)" % (
        os.path.basename(__file__), canon_b(open(__file__, "rb").read())))
    dire("CE QUE CE LOG NE JOUE PAS : aucune decomposition, aucune mesure.")


if __name__ == "__main__":
    main()
