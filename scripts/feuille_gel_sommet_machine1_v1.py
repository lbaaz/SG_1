# -*- coding: ascii -*-
"""FEUILLE DU GEL "SOMMET" -- machine 1, v1, 2026-11-22. CLASSE 2. Elle JUGE ; elle ne mesure rien et ne calcule aucune
chaine : les predictions sont dans la table gelee. Derivee de feuille_vide_machine1_v1.py (registre, ac39a24def6c7420) :
memes regles de lecteur, de temoin, de bande et de jugement ; ce qui change : les fichiers lus sont ceux du pilote de
machine 2 (lect2D_<id>_fantome.json et lect2D_<id>_jumeau.json), les TEMOINS POSITIFS DU SOMMET, et l'enonce unique S1.
INSTRUMENT (etage A) : verdict_ter_instrument.json du dossier du run doit porter "instrument" = "TIENT".
TEMOINS POSITIFS DU SOMMET (etage A') : les neuf points sacrifies de Q et de Q2, relus dans le run. Chacun TIENT si le
  lecteur y est QUALIFIE, si son jumeau tient, et si |ln(Gamma_pl / plateau de reference de la table)| <= 0.001.
  Les temoins positifs TIENNENT si les neuf tiennent.
Par CELLULE (etage B), sur ses deux fichiers :
  LECTEUR  : juger_etat de la feuille DEPOSEE du lecteur (canon controle, importee telle quelle) : un plateau sous chacun
             des quatre absorbeurs (cinq barreaux lisibles consecutifs, plus grande valeur <= 1.05 fois la plus petite),
             accords B / A, C / A, D / A a 0.05 pres en logarithme -> QUALIFIE, NON QUALIFIE ou NON LISIBLE.
             Gamma_pl : le plateau sous A. ETALEMENT DU LECTEUR s = max( ln(1 + etalement du plateau sous A),
             plus grand |ln(plateau X / plateau A)|, X = B, C, D ).
  TEMOIN   : le jumeau sans fantome a la meme cellule. Il TIENT si ses 48 lectures sont suivies et si sa plus grande
             largeur est <= 1e-6 Gamma_pl.
  CELLULE LUE : QUALIFIE et temoin tenu. Sinon NON LUE, avec son motif.
  JUGEMENT d'une cellule lue : ln q = ln(G3* / Gamma_pl) ; bande b = etendue de la chaine (table) + s ; T = 0.01 (table).
             TIENT si |ln q| <= T - b ; TOMBE si |ln q| > T + b ; NON JUGEABLE sinon.
ENONCE S1 (cinquante-six cellules, huit w2) : TOMBE si deux cellules ou plus tombent ; sinon NON CONCLUANT si moins de 42
cellules sont jugees (tenues ou tombees) ou si un w2 a moins de quatre cellules tenues sur sept ; sinon TENU SAUF UNE
CELLULE si une tombe ; sinon TENU. PORTEE : les kappa ou quatre cellules au moins sur huit tiennent.
Si l'instrument ne TIENT pas, si les temoins positifs ne TIENNENT pas, ou si un fichier manque ou n'est pas conforme :
rien n'est juge.
--temoins : l'etape de garde, jouee AVANT toute lecture de cellule : instrument et temoins positifs seulement ; elle
            refuse un dossier ou une cellule est deja lue. C'est aussi tout ce que joue un pre-vol.
Usage : python -I feuille_gel_sommet_machine1_v1.py <lecture_lecteur_gel_loi_machine1_v1.py> <table gelee.json>
        <dossier du run> <sortie.json> [--temoins]"""
import sys, os, json, math, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
FEUILLE_LECTEUR, TABLE, RUN, SORTIE = sys.argv[1:5]
ETAPE_TEMOINS = "--temoins" in sys.argv[5:]
CANON_FEUILLE_LECTEUR, CANON_TABLE = "83701094e6a2b965", "4238e2b262119f83"
CANON_PILOTE_M2, CANON_MOTEUR, CANON_SOURCE_BLOC, BLOC16 = "47a84eae6052f006", "82a0be882568fe0c", "d5cc48f48e37af99", "5b835ce079ce2cf4"
ABSORBEURS = [["A", "F2", 0, 80], ["B", "F2", 0, 100], ["C", "F1", 0, 100], ["D", "F2", 10, 80]]
KS = list(range(-3, 9)); ORDRE = ("MP", "PP", "MG", "PG"); NOMS_ABS = ("A", "B", "C", "D")
TOLERANCE, TEMOIN_MAX, TOL_TEMOIN_POSITIF = 0.01, 1e-6, 1e-3
S1_JUGEES_MIN, S1_TENUES_PAR_W2_MIN, PORTEE_TENUES_PAR_KAPPA_MIN = 42, 4, 4
PLAT = 0.005

def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

def arret(motif, code=2):
    print("FEUILLE REFUSEE : %s" % motif); sys.exit(code)

if canon_B(FEUILLE_LECTEUR) != CANON_FEUILLE_LECTEUR:
    arret("la feuille deposee du lecteur n'est pas au canon %s" % CANON_FEUILLE_LECTEUR)
if canon_B(TABLE) != CANON_TABLE:
    arret("la table n'est pas la table gelee, canon %s" % CANON_TABLE)
spec = importlib.util.spec_from_file_location("feuille_lecteur", FEUILLE_LECTEUR); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
assert L.KS == KS and L.ABS == list(NOMS_ABS) and L.TAU_F == 0.05
T = json.load(open(TABLE)); CELLULES = T["cellules"]; TEMOINS = T["temoins_positifs"]; R = T["regle"]
if (R["absorbeurs_du_lecteur"], R["barreaux"], R["tolerance"], R["temoin_max"], R["tolerance_temoin_positif"], R["s1_jugees_min"], R["s1_tenues_par_w2_min"],
    R["portee_tenues_par_kappa_min"], R["pilote_machine2_canon"], R["moteur_canon"], R["source_bloc_canon"], R["bloc_sha256_16"]) != (
        ABSORBEURS, KS, TOLERANCE, TEMOIN_MAX, TOL_TEMOIN_POSITIF, S1_JUGEES_MIN, S1_TENUES_PAR_W2_MIN, PORTEE_TENUES_PAR_KAPPA_MIN, CANON_PILOTE_M2, CANON_MOTEUR,
        CANON_SOURCE_BLOC, BLOC16):
    arret("la regle de la table n'est pas celle de la feuille")
assert len(CELLULES) == 56 and len(TEMOINS) == 9 and len(set(c["id"] for c in CELLULES + TEMOINS)) == 65

def lire_fichier(c, nom):
    """Controle la forme du fichier lect2D_<id>_<nom>.json (nom : fantome ou jumeau) et rend sa lecture, ou leve ValueError."""
    chemin = os.path.join(RUN, "lect2D_%s_%s.json" % (c["id"], nom))
    if not os.path.exists(chemin):
        raise ValueError("%s : fichier absent" % nom)
    S = json.load(open(chemin))
    if (S.get("pilote_canon"), S.get("moteur_canon"), S.get("source_bloc_canon"), S.get("bloc_sha256_16")) != (CANON_PILOTE_M2, CANON_MOTEUR, CANON_SOURCE_BLOC, BLOC16):
        raise ValueError("%s : canons du pilote, du moteur ou du bloc du lecteur" % nom)
    x = S.get("cellule") or {}
    if (x.get("id"), x.get("w2"), x.get("m"), x.get("g"), x.get("r_c")) != (c["id"], c["w2"], c["m"], c["g"], c["r_c"]) or x.get("eta0") != float(c["eta0"]):
        raise ValueError("%s : la cellule du fichier n'est pas celle de la table" % nom)
    if S.get("reglage", {}).get("ks") != KS or S.get("reglage", {}).get("absorbeurs") != ABSORBEURS:
        raise ValueError("%s : barreaux ou absorbeurs" % nom)
    rec = S.get("lecture") or {}
    if rec.get("signe") != (+1 if nom == "jumeau" else -1) or rec.get("site") != [0, 0] or rec.get("E_depart") != 0.0:
        raise ValueError("%s : signe, site ou energie de depart" % nom)
    if sorted(rec.get("traj", {})) != list(NOMS_ABS) or any(sorted(int(k) for k in rec["traj"][a]) != KS for a in rec["traj"]):
        raise ValueError("%s : trajectoires incompletes" % nom)
    for a, forme, dr, couches in ABSORBEURS:
        g = rec["absorbeurs"][a]
        if (g["forme"], g["bord"], g["couches"], g["N"]) != (forme, c["r_c"] + dr, couches, c["r_c"] + dr + couches):
            raise ValueError("%s : geometrie de l'absorbeur %s" % (nom, a))
    return rec

def temoin(jum):
    lect = [jum["traj"][a][str(k)] for a in NOMS_ABS for k in KS]
    gam = [r["gamma"] for r in lect if r.get("suivi") and r.get("gamma") is not None and math.isfinite(r["gamma"])]
    return {"lectures": len(lect), "suivies": sum(1 for r in lect if r.get("suivi")), "plus_grande_largeur": (max(gam) if gam else None)}

def lire_point(c):
    """Lecteur et temoin d'un point (cellule ou temoin positif). Rend le dictionnaire du point, ou leve ValueError."""
    fan = lire_fichier(c, "fantome"); jum = lire_fichier(c, "jumeau")
    j = L.juger_etat(fan["traj"], None); P = j["plateaux"]
    rec = {"temoin": temoin(jum), "lu": False, "motif": None,
           "lecteur": {"statut": j["statut"], "echecs": j["echecs"], "non_lisibles": j["non_lisibles"],
                       "plateaux": {a: {k: P[a].get(k) for k in ("statut", "k0", "etalement", "Gamma_pl", "ecart_ln_A")} for a in NOMS_ABS},
                       "suivies": sum(1 for a in NOMS_ABS for k in KS if fan["traj"][a][str(k)].get("suivi")),
                       "poids_min": min([fan["traj"][a][str(k)]["poids_site"] for a in NOMS_ABS for k in KS if fan["traj"][a][str(k)].get("poids_site") is not None] or [None])}}
    tm = rec["temoin"]
    if j["statut"] != "QUALIFIE":
        rec["motif"] = "lecteur : %s" % j["statut"]; return rec
    A = P["A"]; gpl = A["Gamma_pl"]
    rec["ln_Gamma_pl"] = math.log(gpl)
    rec["etalement_du_lecteur"] = max([math.log(1.0 + A["etalement"])] + [P[a]["ecart_ln_A"] for a in ("B", "C", "D")])
    rec["barreaux_plats_sous_A"] = [k for k in KS if fan["traj"]["A"][str(k)].get("suivi") and fan["traj"]["A"][str(k)].get("gamma") and
                                    abs(math.log(fan["traj"]["A"][str(k)]["gamma"] / gpl)) <= PLAT]
    tm["rapport_au_plateau"] = (tm["plus_grande_largeur"] / gpl) if tm["plus_grande_largeur"] is not None else None
    tm["tient"] = bool(tm["suivies"] == tm["lectures"] and tm["rapport_au_plateau"] is not None and tm["rapport_au_plateau"] <= TEMOIN_MAX)
    if not tm["tient"]:
        rec["motif"] = "temoin : %d lectures suivies sur %d, rapport au plateau %s" % (tm["suivies"], tm["lectures"], tm["rapport_au_plateau"]); return rec
    rec["lu"] = True
    return rec

def issue_S1(cs):
    ten = [c for c in cs if c["jugement"] == "TIENT"]; tom = [c for c in cs if c["jugement"] == "TOMBE"]
    if len(tom) >= 2:
        return "TOMBE"
    if len(ten) + len(tom) < S1_JUGEES_MIN:
        return "NON CONCLUANT"
    if any(sum(1 for c in ten if c["w2"] == w) < S1_TENUES_PAR_W2_MIN for w in sorted(set(c["w2"] for c in cs))):
        return "NON CONCLUANT"
    return "TENU SAUF UNE CELLULE" if tom else "TENU"

def main():
    out = {"feuille": "feuille_gel_sommet_machine1_v1", "feuille_canon": canon_B(os.path.abspath(__file__)), "table_canon": canon_B(TABLE), "etape": "temoins" if ETAPE_TEMOINS else "verdict",
           "feuille_lecteur_canon": CANON_FEUILLE_LECTEUR, "pilote_machine2_canon": CANON_PILOTE_M2, "graine": T["graine"],
           "reglage": {"tolerance": TOLERANCE, "temoin_max": TEMOIN_MAX, "tolerance_temoin_positif": TOL_TEMOIN_POSITIF, "s1_jugees_min": S1_JUGEES_MIN,
                       "s1_tenues_par_w2_min": S1_TENUES_PAR_W2_MIN, "portee_tenues_par_kappa_min": PORTEE_TENUES_PAR_KAPPA_MIN, "tau_plateau": 0.05, "tau_accord": 0.05, "plat": PLAT}}
    print("=" * 100); print("FEUILLE DU GEL SOMMET v1%s" % (" -- ETAPE DE GARDE (instrument et temoins positifs), RIEN N'EST JUGE" if ETAPE_TEMOINS else "")); print("=" * 100)
    def ecrire(verdict):
        out["verdict"] = verdict; print("VERDICT : %s" % verdict if not ETAPE_TEMOINS else "GARDE : %s" % verdict)
        json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True); print("ecrit %s" % SORTIE)
    # --- etage A : l'instrument du lecteur
    f_inst = os.path.join(RUN, "verdict_ter_instrument.json")
    inst = json.load(open(f_inst)).get("instrument") if os.path.exists(f_inst) else "ABSENT"
    out["instrument"] = inst; out["instrument_canon"] = canon_B(f_inst) if os.path.exists(f_inst) else None
    print("INSTRUMENT DU LECTEUR (etage 0, ancres, etage 1 ; pieces deposees) : %s" % inst)
    # --- etage A' : les temoins positifs du sommet
    print("TEMOINS POSITIFS DU SOMMET (les neuf points sacrifies de Q et de Q2, relus dans le run)")
    print("temoin  w2           m  lecteur        jumeau     plateau lu   reference    ln(lu / reference)  ln(lu / G3*)  tient")
    tps = []; tp_ok = True
    for c in TEMOINS:
        r = {"id": c["id"], "w2": c["w2"], "m": c["m"], "g": c["g"]}
        try:
            r.update(lire_point(c))
        except ValueError as e:
            r["forme"] = str(e); r["tient"] = False; tp_ok = False; tps.append(r)
            print("%-6s  %-11s  %d  FICHIER NON CONFORME : %s" % (c["id"], c["w2"], c["m"], e)); continue
        if r["lu"]:
            r["ecart_reference"] = r["ln_Gamma_pl"] - c["ln_Gamma_pl_reference"]; r["ln_q"] = c["ln_G3"] - r["ln_Gamma_pl"]
            r["tient"] = abs(r["ecart_reference"]) <= TOL_TEMOIN_POSITIF
        else:
            r["tient"] = False
        tp_ok = tp_ok and r["tient"]; tps.append(r)
        print("%-6s  %-11s  %d  %-13s  %-9s  %-11s  %.5e  %-18s  %-12s  %s%s" % (c["id"], c["w2"], c["m"], r["lecteur"]["statut"],
              ("tenu" if r["temoin"].get("tient") else ("--" if "tient" not in r["temoin"] else "NON TENU")), ("%.5e" % math.exp(r["ln_Gamma_pl"])) if "ln_Gamma_pl" in r else "--",
              math.exp(c["ln_Gamma_pl_reference"]), ("%+.2e" % r["ecart_reference"]) if "ecart_reference" in r else "--", ("%+.5f" % -r["ln_q"]) if "ln_q" in r else "--",
              "oui" if r["tient"] else "NON", (" (%s)" % r["motif"]) if r.get("motif") else ""))
    out["temoins_positifs"] = {"issue": "TIENNENT" if tp_ok else "NE TIENNENT PAS", "tenus": sum(1 for r in tps if r["tient"]), "sur": len(tps), "points": tps}
    print("TEMOINS POSITIFS : %s (%d sur %d)" % (out["temoins_positifs"]["issue"], out["temoins_positifs"]["tenus"], len(tps)))
    deja = [c["id"] for c in CELLULES if any(os.path.exists(os.path.join(RUN, "lect2D_%s_%s.json" % (c["id"], n))) for n in ("fantome", "jumeau"))]
    if ETAPE_TEMOINS:
        if deja:
            out["cellules_deja_lues"] = deja
            ecrire("REFUS : %d cellules ont deja un fichier dans ce dossier ; l'etape de garde se joue AVANT toute lecture de cellule" % len(deja)); sys.exit(3)
        ecrire("TIENT : les cellules peuvent etre lues" if (inst == "TIENT" and tp_ok) else
               ("L'INSTRUMENT NE TIENT PAS : aucune cellule ne doit etre lue" if inst != "TIENT" else "LES TEMOINS POSITIFS NE TIENNENT PAS : aucune cellule ne doit etre lue"))
        return
    if inst != "TIENT" or not tp_ok:
        ecrire("L'INSTRUMENT NE TIENT PAS : RIEN N'EST JUGE" if inst != "TIENT" else "LES TEMOINS POSITIFS DU SOMMET NE TIENNENT PAS : RIEN N'EST JUGE"); return
    # --- etage B : les cellules
    cellules = []; incomplet = []
    for c in CELLULES:
        r = {k: c[k] for k in ("id", "creneau", "rang", "numero_kappa", "w2", "delta", "kappa", "m", "g", "tolerance", "etendue", "ln_G3")}
        try:
            r.update(lire_point(c))
        except ValueError as e:
            incomplet.append("%s : %s" % (c["id"], e)); r["forme"] = str(e)
        cellules.append(r)
    out["cellules"] = cellules; out["incomplet"] = incomplet
    if incomplet:
        print("RUN INCOMPLET : %d cellules sans fichiers conformes" % len(incomplet))
        for x in incomplet:
            print("    " + x)
        ecrire("RUN INCOMPLET : RIEN N'EST JUGE"); return
    print("cellule  w2              kappa   lecteur        temoin     ln Gamma_pl  etal.s  etendue  bande b  ln q      T     jugement")
    par_id = {c["id"]: c for c in CELLULES}
    for r in cellules:
        c = par_id[r["id"]]; r["jugement"] = "NON LUE"
        if r["lu"]:
            lnq = r["ln_G3"] - r["ln_Gamma_pl"]; b = r["etendue"] + r["etalement_du_lecteur"]; Tt = r["tolerance"]
            r["ln_q"] = lnq; r["bande"] = b
            r["jugement"] = "TIENT" if abs(lnq) <= Tt - b else ("TOMBE" if abs(lnq) > Tt + b else "NON JUGEABLE")
            r["consigne"] = {"signe_de_ln_q": (1 if lnq > 0 else -1), "signe_de_delta": (1 if r["delta"] > 0 else -1),
                             "ln_q_ordre2": c["ln_G2"] - r["ln_Gamma_pl"], "ln_q_ordre1": c["ln_G1"] - r["ln_Gamma_pl"],
                             "ln_Phi_lu": r["ln_Gamma_pl"] - math.log(abs(r["delta"])), "ln_Phi_chaine": c["ln_Phi"],
                             "ln_Gamma_pl_sur_t0": r["ln_Gamma_pl"] - math.log(abs(r["delta"])) - math.log(float(F(r["kappa"]))),
                             "barreaux_plats_sous_A": r["barreaux_plats_sous_A"]}
        lec = r["lecteur"]; tm = r["temoin"]
        print("%-7s  %-14s  %s  %-13s  %-9s  %-11s  %-6s  %.4f   %-7s  %-8s  %.2f  %s%s" % (
            r["id"], r["w2"], r["kappa"], lec["statut"], ("tenu" if tm.get("tient") else ("--" if "tient" not in tm else "NON TENU")),
            ("%+.4f" % r["ln_Gamma_pl"]) if "ln_Gamma_pl" in r else "--", ("%.4f" % r["etalement_du_lecteur"]) if "etalement_du_lecteur" in r else "--", r["etendue"],
            ("%.4f" % r["bande"]) if "bande" in r else "--", ("%+.5f" % r["ln_q"]) if "ln_q" in r else "--", r["tolerance"], r["jugement"], (" (%s)" % r["motif"]) if r["motif"] else ""))
    compte = lambda cs: {k: sum(1 for r in cs if r["jugement"] == k) for k in ("TIENT", "TOMBE", "NON JUGEABLE", "NON LUE")}
    kappas = sorted(set(r["kappa"] for r in cellules), key=float); w2s = sorted(set(r["w2"] for r in cellules), key=lambda z: float(F(z)))
    par_kappa = {k: compte([r for r in cellules if r["kappa"] == k]) for k in kappas}; par_w2 = {w: compte([r for r in cellules if r["w2"] == w]) for w in w2s}
    out["S1"] = {"issue": issue_S1(cellules), "comptes": compte(cellules), "cellules": len(cellules), "tombees": [r["id"] for r in cellules if r["jugement"] == "TOMBE"],
                 "par_kappa": par_kappa, "par_w2": par_w2, "portee_kappa": [k for k in kappas if par_kappa[k]["TIENT"] >= PORTEE_TENUES_PAR_KAPPA_MIN]}
    lues = [r for r in cellules if "ln_q" in r]
    echelle = {}
    for k in kappas:
        v = [r["consigne"]["ln_Phi_lu"] for r in lues if r["kappa"] == k]; vc = [r["consigne"]["ln_Phi_chaine"] for r in lues if r["kappa"] == k]
        echelle[k] = {"cellules": len(v), "etalement_lu": (max(v) - min(v)) if v else None, "etalement_chaine": (max(vc) - min(vc)) if vc else None}
    miroirs = []
    for rm in lues:
        for rp in lues:
            if rm["delta"] < 0 < rp["delta"] and rm["kappa"] == rp["kappa"] and F(rm["w2"]) + F(rp["w2"]) == 4:
                miroirs.append({"kappa": rm["kappa"], "moins": rm["id"], "plus": rp["id"], "ln_rapport_lu": rm["consigne"]["ln_Phi_lu"] - rp["consigne"]["ln_Phi_lu"],
                                "ln_rapport_chaine": rm["consigne"]["ln_Phi_chaine"] - rp["consigne"]["ln_Phi_chaine"]})
    out["consigne"] = {"cellules_jugees_ou_non_jugeables": len(lues), "plus_grand_ln_q": max([abs(r["ln_q"]) for r in lues] or [None]),
                       "ln_q_negatif": sum(1 for r in lues if r["ln_q"] < 0), "ln_q_du_signe_de_delta": sum(1 for r in lues if r["consigne"]["signe_de_ln_q"] == r["consigne"]["signe_de_delta"]),
                       "ordre3_plus_pres_que_ordre1": sum(1 for r in lues if abs(r["ln_q"]) < abs(r["consigne"]["ln_q_ordre1"])),
                       "loi_d_echelle": echelle, "paires_miroirs": miroirs}
    v = out["S1"]
    print("S1 (%d cellules, %d w2) : %s ; tenues %d, tombees %d %s, non jugeables %d, non lues %d" % (len(cellules), len(w2s), v["issue"], v["comptes"]["TIENT"], v["comptes"]["TOMBE"],
          v["tombees"], v["comptes"]["NON JUGEABLE"], v["comptes"]["NON LUE"]))
    print("  tenues par w2 (sur 7) : %s" % " ; ".join("%s %d" % (w, par_w2[w]["TIENT"]) for w in w2s))
    print("  tenues par kappa (sur 8) : %s ; PORTEE : %s" % (" ; ".join("%s %d" % (k, par_kappa[k]["TIENT"]) for k in kappas), " ".join(v["portee_kappa"]) or "aucun kappa"))
    k = out["consigne"]
    print("consigne, sans jugement, sur %d cellules lues : plus grand |ln q| %s ; ln q negatif (lecteur au-dessus de la chaine) a %d ; ln q du signe de delta a %d ; ordre 3 plus pres que l'ordre 1 a %d" % (
        k["cellules_jugees_ou_non_jugeables"], ("%.5f" % k["plus_grand_ln_q"]) if k["plus_grand_ln_q"] is not None else "--", k["ln_q_negatif"], k["ln_q_du_signe_de_delta"], k["ordre3_plus_pres_que_ordre1"]))
    print("  loi d'echelle, etalement de ln(Gamma_pl / |delta|) a kappa egal, lu (chaine) : %s" % " ; ".join("%s %s (%s)" % (kk, ("%.5f" % e["etalement_lu"]) if e["etalement_lu"] is not None else "--",
          ("%.5f" % e["etalement_chaine"]) if e["etalement_chaine"] is not None else "--") for kk, e in echelle.items()))
    print("  signe de delta, paires de w2 miroirs lues, ln[Phi(delta < 0) / Phi(delta > 0)] lu (chaine) : %s" % (" ; ".join("%s %+.5f (%+.5f)" % (m_["kappa"], m_["ln_rapport_lu"], m_["ln_rapport_chaine"]) for m_ in miroirs) or "aucune paire"))
    ecrire("S1 %s" % v["issue"])

main()
