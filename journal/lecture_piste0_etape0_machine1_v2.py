# -*- coding: ascii -*-
# Lecture a zero run des artefacts M17 -- piste (0), etape 0 -- machine 1 -- v2 = v1 + 7 remplacements (D-P0-1..3, B)
# CLASSE 3. Arguments : <dossier des points> <manifeste m2> <lecture
# pre-declaree> <sortie json>. Ne charge aucun moteur, n'ecrit que la sortie.
import sys, os, json, math, hashlib, unicodedata, itertools
from fractions import Fraction


def canon_b(octets):
    t = unicodedata.normalize("NFC", octets.decode("utf-8"))
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


def rangs(v):
    ordre = sorted(range(len(v)), key=lambda i: v[i])
    r = [0] * len(v)
    for k, i in enumerate(ordre):
        r[i] = k + 1
    assert len(set(v)) == len(v), "ex aequo : rang non defini"
    return r


def spearman(a, b):
    ra, rb = rangs(a), rangs(b)
    n = len(a)
    d2 = sum((x - y) ** 2 for x, y in zip(ra, rb))
    return Fraction(n * (n * n - 1) - 6 * d2, n * (n * n - 1)), ra, rb


def p_exact(n, rho):
    base = list(range(1, n + 1))
    tot = fav = 0
    for perm in itertools.permutations(base):
        d2 = sum((x - y) ** 2 for x, y in zip(base, perm))
        tot += 1
        if Fraction(n * (n * n - 1) - 6 * d2, n * (n * n - 1)) >= rho:
            fav += 1
    return Fraction(fav, tot)


def main():
    dossier, manifeste, predecl, sortie = sys.argv[1:5]
    print("=" * 74)
    print("PISTE (0) ETAPE 0 -- LECTURE A ZERO RUN DES ARTEFACTS M17 -- CLASSE 3")
    print("=" * 74)
    print("lecture pre-declaree : %s  canon %s" % (
        os.path.basename(predecl), canon_b(open(predecl, "rb").read())))
    lignes = open(manifeste, "rb").read()
    print("manifeste m2         : %s  canon %s" % (
        os.path.basename(manifeste), canon_b(lignes)))

    # 1. AUTHENTIFICATION DU LOT CONTRE LE MANIFESTE AU REGISTRE
    att = {}
    for l in lignes.decode("utf-8").splitlines():
        ch = l.split()
        if len(ch) == 3 and len(ch[0]) == 16:
            att[ch[1]] = (ch[0], int(ch[2]))
    ok = ko = absents = 0
    for nom, (emp, taille) in sorted(att.items()):
        p = os.path.join(dossier, nom)
        if not os.path.exists(p):
            absents += 1
            print("  ABSENT %s" % nom)
            continue
        b = open(p, "rb").read()
        if canon_b(b) == emp and len(b) == taille:
            ok += 1
        else:
            ko += 1
            print("  DIFFERE %s : canon %s contre %s, %d contre %d o" % (
                nom, canon_b(b), emp, len(b), taille))
    surnum = sorted(set(os.listdir(dossier)) - set(att))
    print("\n1. AUTHENTIFICATION : %d au canon et a la taille + %d differents"
          " + %d absents == %d lignes du manifeste ; surnumeraires %s" % (
              ok, ko, absents, len(att), surnum))
    if ko or absents or surnum:
        print("ARRET : lot non authentifie, aucune lecture.")
        sys.exit(1)

    # 2. EXTRACTION DES SIX POINTS f070
    noms = sorted(n for n in att if n.endswith("_f070.json"))
    pts, ecartes = {}, []
    for nom in noms:
        d = json.load(open(os.path.join(dossier, nom)))
        eb = d.get("EB", {})
        if not eb.get("faisable") or eb.get("critere_absorbeur", {}).get(
                "L_retenu") is None:
            ecartes.append(nom)
            continue
        w = float(Fraction(d["w2"]))
        L = eb["critere_absorbeur"]["L_retenu"]
        essai = [e for e in eb["critere_absorbeur"]["essais"]
                 if e["L"] == L and e["accepte"]]
        assert len(essai) == 1, nom
        H = eb["Gamma_LS"]["H"]
        op = eb["operatif_4_6"]
        pts[w] = {
            "fichier": nom, "statut": d.get("statut"),
            "G": H["Gamma_LS"], "R": op["Richardson"], "r": op["r"],
            "res": op["residu_declare"],
            "p1": essai[0]["pas"][0], "p2": essai[0]["pas"][1],
            "p3": essai[0]["pas"][2],
            "m": eb["temoin_montante"]["ecart"],
            "t": eb["stationnarites"]["translation_p"],
            "n": eb["stationnarites"]["N_plus_p"],
            "rec": H["recouvrement"], "W": H["poids_total"],
            "Gp": H["Gamma_pondere"], "q": H["Gamma_pondere"] / H["Gamma_LS"],
            "nres": H["n_resonances"], "c": H["poids_cumule"] / H["poids_total"],
            "Hp": eb["Gamma_LS"]["Hplus"]["Gamma_LS"],
            "L": L, "N": eb["N"], "r_c": eb["r_c"], "eta": eb["eta"],
            "g": d["g"], "Lam": d["EA"]["Lambda_c"],
            "essais": eb["critere_absorbeur"]["essais"],
            "motifs_arret": d.get("motifs_arret"),
        }
    print("\n2. COMPTE : %d f070 lus + %d ecartes == %d attendus %s" % (
        len(pts), len(ecartes), 6,
        "OK" if len(pts) + len(ecartes) == 6 and not ecartes else "ECART"))
    ws = sorted(pts)

    def ligne(cle, fmt):
        return "  %-5s " % cle + " ".join(fmt % pts[w][cle] for w in ws)

    print("\n3. TABLE (colonnes : w2 = %s)" % ", ".join("%.2f" % w for w in ws))
    for cle, fmt in [("g", "%11.4e"), ("eta", "%11.4f"), ("r_c", "%11d"),
                     ("L", "%11d"), ("N", "%11d"), ("Lam", "%11.5f"),
                     ("G", "%11.4e"), ("R", "%11.4e"), ("r", "%11.4f"),
                     ("res", "%11.4e"), ("p1", "%11.4e"), ("p2", "%11.4e"),
                     ("p3", "%11.4e"), ("m", "%11.4e"), ("t", "%11.4e"),
                     ("n", "%11.4e"), ("rec", "%11.4e"), ("W", "%11.4f"),
                     ("Gp", "%11.4e"), ("q", "%11.4e"), ("nres", "%11d"),
                     ("c", "%11.6f"), ("Hp", "%11.3e")]:
        print(ligne(cle, fmt))
    for w in ws:
        print("  essais %.2f : %s" % (w, [(e["L"], e["accepte"],
              ["%.3e" % x for x in e["pas"]]) for e in pts[w]["essais"]]))

    res = {"points": {("%.2f" % w): pts[w] for w in ws}}

    # L-1
    B = {w: max([pts[w]["t"], pts[w]["n"], pts[w]["p3"]]
                + ([abs(pts[w]["res"])] if pts[w]["res"] == pts[w]["res"]
                   else [])) for w in ws}
    print("\n    points SANS residu (r hors de ]0, 1[), B sur trois termes :"
          " %s" % ["%.2f" % w for w in ws if pts[w]["res"] != pts[w]["res"]])
    E = math.log(max(pts[w]["G"] for w in ws) / min(pts[w]["G"] for w in ws))
    l1 = max(B.values()) < 0.05 and E > math.log(10.0)
    print("\nL-1 budget B = max(t, n, p3, |res|) : %s" % " ".join(
        "%.2f:%.4f" % (w, B[w]) for w in ws))
    print("    max B = %.4f (< 0.05 : %s) ; E = ln(max G / min G) = %.4f"
          " soit x%.1f (> ln 10 : %s) -> L-1 %s" % (
              max(B.values()), max(B.values()) < 0.05, E, math.exp(E),
              E > math.log(10.0), "TIENT" if l1 else "NE TIENT PAS"))
    res["L1"] = {"B": {("%.2f" % w): B[w] for w in ws}, "E": E, "tient": l1}

    # L-2 / L-3
    O = [1.95, 1.97, 1.98, 2.03]
    T = [2.02, 2.05]
    grp = {"A": ["p1", "p2", "p3", "m", "t", "n", "absres", "L"],
           "I": ["rec", "W", "q", "nres", "c"]}
    for w in ws:
        pts[w]["absres"] = abs(pts[w]["res"])
    hors = {("%.2f" % j): {"A": [], "I": []} for j in T}
    non_lisibles = []
    print("\nL-2 / L-3 regle HORS PLAGE (reference O = %s)" % O)
    for g_, cles in sorted(grp.items()):
        for cle in cles:
            vo = [pts[w][cle] for w in O]
            lo, hi = min(vo), max(vo)
            wd = hi - lo
            for j in T:
                x = pts[j][cle]
                if x != x:
                    non_lisibles.append(("%.2f" % j, cle))
                    print("  [%s] %-6s O=[%.4e, %.4e]  %.2f : NON LISIBLE"
                          " (valeur non finie), ni dans ni hors la plage"
                          % (g_, cle, lo, hi, j))
                    continue
                if wd == 0:
                    h = (x != lo)
                    note = " (plage nulle)"
                else:
                    h = (x > hi + wd) or (x < lo - wd)
                    note = ""
                if h:
                    hors["%.2f" % j][g_].append(cle)
                print("  [%s] %-6s O=[%.4e, %.4e]  %.2f : %.4e  %s%s" % (
                    g_, cle, lo, hi, j, x,
                    "HORS PLAGE" if h else "dans la plage", note))
    for j in T:
        k = "%.2f" % j
        print("  bilan %s : groupe A hors plage %s ; groupe I hors plage %s"
              % (k, hors[k]["A"], hors[k]["I"]))
    l2 = len(hors["2.05"]["I"]) >= 1
    l3 = len(hors["2.05"]["A"]) == 0
    print("  L-2 (au moins un I hors plage a 2.05) : %s" % (
        "TIENT" if l2 else "NE TIENT PAS"))
    print("  L-3 (aucun A hors plage a 2.05)       : %s" % (
        "TIENT" if l3 else "NE TIENT PAS"))
    print("  non lisibles (D-P0-1) : %s" % non_lisibles)
    res["L2_L3"] = {"hors": hors, "L2": l2, "L3": l3,
                    "non_lisibles": non_lisibles}

    # L-4
    G = [pts[w]["G"] for w in ws]
    Gp = [pts[w]["Gp"] for w in ws]
    R = [pts[w]["R"] for w in ws]
    mL = [-pts[w]["Lam"] for w in ws]
    rc = Fraction(29, 35)
    r_ggp, ra, rb = spearman(G, Gp)
    wR = [w for w in ws if pts[w]["R"] == pts[w]["R"]]
    r_gr, _, _ = spearman([pts[w]["G"] for w in wR],
                          [pts[w]["R"] for w in wR])
    r_p6, rg6, rl6 = spearman(G, mL)
    r_p6p, rgp6, _ = spearman(Gp, mL)
    print("\nL-4 rangs G  : %s" % ra)
    print("    rangs Gp : %s" % rb)
    print("    rho(G, Gp) = %s (%.4f) contre 29/35 : %s ; p_exact = %s" % (
        r_ggp, float(r_ggp), "TIENT" if r_ggp >= rc else "NE TIENT PAS",
        p_exact(6, r_ggp)))
    print("    rho(G, R)  = %s sur %d points ou R existe + %d sans R"
          " == %d (D-P0-2)" % (r_gr, len(wR), len(ws) - len(wR), len(ws)))
    print("    temoin : P6 (i) rejoue rho(G, -Lam) = %s (assemblage : 1/35)"
          % r_p6)
    print("    EXPLORATOIRE, SANS VERDICT : rho(Gp, -Lam) = %s (%.4f),"
          " p_exact = %s ; rangs Gp %s, rangs -Lam %s" % (
              r_p6p, float(r_p6p), p_exact(6, r_p6p), rgp6, rl6))
    res["L4"] = {"rho_G_Gp": str(r_ggp), "tient": bool(r_ggp >= rc),
                 "rho_G_R": str(r_gr), "rho_G_Lam": str(r_p6),
                 "rho_Gp_Lam": str(r_p6p)}

    # L-5
    sg = {w: ((1 if pts[w]["R"] > pts[w]["G"] else -1)
              if 0.0 < pts[w]["r"] < 1.0 else 0) for w in ws}
    l5 = (0 not in sg.values()) and len(set(sg.values())) == 1
    print("    (0 = NON DEFINI : r hors de ]0, 1[, Richardson absent --"
          " D-P0-3) ; definis %d + non definis %d == %d" % (
              sum(1 for v in sg.values() if v), sum(1 for v in sg.values()
              if not v), len(ws)))
    print("\nL-5 signe(R - G) = signe du dernier pas (eta/4 -> eta/8) : %s"
          % " ".join("%.2f:%+d" % (w, sg[w]) for w in ws))
    print("    (R - G)/G : %s" % " ".join("%.2f:%+.4e" % (
        w, (pts[w]["R"] - pts[w]["G"]) / pts[w]["G"]) for w in ws))
    print("    L-5 (meme signe aux six) : %s" % ("TIENT" if l5 else
                                                 "NE TIENT PAS"))
    res["L5"] = {"signes": {("%.2f" % w): sg[w] for w in ws}, "tient": l5}

    # CONSIGNES : jumeau, f050, P8
    print("\nCONSIGNES")
    print("  G / |Hp| : %s" % " ".join("%.2f:%.1e" % (
        w, pts[w]["G"] / abs(pts[w]["Hp"])) for w in ws))
    autres = {}
    for nom in sorted(att):
        if nom.startswith("pt_") and not nom.endswith("_f070.json"):
            d = json.load(open(os.path.join(dossier, nom)))
            eb = d.get("EB", {})
            autres[nom] = {"statut": d.get("statut"),
                           "motifs": d.get("motifs_arret"),
                           "EB_cles": sorted(eb.keys()),
                           "essais": eb.get("critere_absorbeur", {}).get(
                               "essais"),
                           "N_derive": eb.get("N_derive")}
    cpt = {}
    for nom, a in autres.items():
        cpt[a["statut"]] = cpt.get(a["statut"], 0) + 1
    print("  hors f070 : %d fichiers, statuts %s" % (len(autres), cpt))
    for nom, a in autres.items():
        if a["statut"] not in ("EN DOMAINE",) or "P8" in nom:
            print("   %-28s %-16s %s" % (nom, a["statut"], a["motifs"]))
            if a["essais"]:
                print("      essais : %s" % [(e["L"], e["accepte"],
                      ["%.3e" % x for x in e["pas"]]) for e in a["essais"]])
            if a["N_derive"]:
                print("      N_derive = %s" % a["N_derive"])
    res["autres"] = autres
    json.dump(res, open(sortie, "w"), indent=1, sort_keys=True)
    print("\nsortie : %s" % os.path.basename(sortie))


main()
