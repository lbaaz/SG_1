# -*- coding: ascii -*-
"""FEUILLE DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16. CLASSE 2. Elle JUGE ; elle ne mesure rien et ne calcule
aucune chaine : les predictions sont dans la table gelee.
Par cellule, sur le fichier sonde_vide_<id>.json du dossier du run :
  LECTEUR  : juger_etat de la feuille DEPOSEE du lecteur (lecture_lecteur_gel_loi_machine1_v1.py, canon controle, importee
             telle quelle) : plateau sous chacun des quatre absorbeurs (cinq barreaux consecutifs a 5 pour cent), accords
             B / A, C / A, D / A a 0.05 pres en logarithme -> QUALIFIE, NON QUALIFIE ou NON LISIBLE.
             Gamma_pl : le plateau sous A. ETALEMENT DU LECTEUR s = max( ln(1 + etalement du plateau sous A),
             plus grand |ln(plateau X / plateau A)|, X = B, C, D ).
  TEMOIN   : le jumeau sans fantome a la meme cellule. Il TIENT si ses 48 lectures sont suivies et si sa plus grande
             largeur est <= 1e-6 Gamma_pl.
  CELLULE LUE : QUALIFIE et temoin tenu.
  JUGEMENT d'une cellule lue : ln q = ln(G3* / Gamma_pl) ; bande b = etendue de la chaine (table) + s ; T = tolerance de la
             ligne (table). TIENT si |ln q| <= T - b ; TOMBE si |ln q| > T + b ; NON JUGEABLE sinon.
ISSUES. V1 (seize cellules lisibles) : TOMBE si deux cellules ou plus tombent ; sinon NON CONCLUANT si moins de douze cellules
sont jugees (tenues ou tombees) ou si un creneau a moins de deux cellules tenues ; sinon TENU SAUF UNE CELLULE si une tombe ;
sinon TENU. VP (douze cellules profondes, hors de V1) : TOMBE si deux ou plus tombent ; sinon NON LUE si aucune n'est jugee ;
sinon NON CONCLUANT si moins de six sont jugees ; sinon TENU SAUF UNE CELLULE ou TENU.
Si l'instrument du lecteur ne TIENT pas (verdict_ter_instrument.json du dossier), ou si un fichier manque : rien n'est juge.
--prevol : la table n'est pas celle du gel et le fantome n'est pas lu ; la feuille ne rend que les nombres du jumeau.
Usage : python -I feuille_vide_machine1_v1.py <lecture_lecteur_gel_loi_machine1_v1.py> <table des cellules.json>
        <dossier du run> <sortie verdict.json> [--prevol]"""
import sys, os, json, math, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
FEUILLE_LECTEUR, TABLE, RUN, SORTIE = sys.argv[1:5]
PREVOL = "--prevol" in sys.argv[5:]
CANON_FEUILLE_LECTEUR, CANON_TABLE, CANON_SONDE = "83701094e6a2b965", "b71206e5daf6c741", "0f82986cca133330"
CANON_MOTEUR, CANON_SOURCE_BLOC = "82a0be882568fe0c", "d5cc48f48e37af99"
ABSORBEURS = [["A", "F2", 0, 80], ["B", "F2", 0, 100], ["C", "F1", 0, 100], ["D", "F2", 10, 80]]
KS = list(range(-3, 9)); ORDRE = ("MG", "MP", "PP", "PG")
TEMOIN_MAX = 1e-6; V1_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, VP_JUGEES_MIN = 12, 2, 6

def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

def arret(motif, code=2):
    print("FEUILLE REFUSEE : %s" % motif); sys.exit(code)

if canon_B(FEUILLE_LECTEUR) != CANON_FEUILLE_LECTEUR:
    arret("la feuille deposee du lecteur n'est pas au canon %s" % CANON_FEUILLE_LECTEUR)
if (canon_B(TABLE) == CANON_TABLE) == PREVOL:
    arret("sans --prevol la table doit etre au canon %s ; avec --prevol elle ne doit pas l'etre" % CANON_TABLE)
spec = importlib.util.spec_from_file_location("feuille_lecteur", FEUILLE_LECTEUR); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
assert L.KS == KS and L.ABS == ["A", "B", "C", "D"] and L.TAU_F == 0.05
T = json.load(open(TABLE)); CELLULES = T["cellules"]
if T["regle"]["absorbeurs_du_lecteur"] != ABSORBEURS or T["regle"]["barreaux"] != KS:
    arret("la table ne porte pas les absorbeurs et les barreaux de la regle")

def issue_ligne(cs, jugees_min, par_creneau, non_lue_possible):
    ten = [c for c in cs if c["jugement"] == "TIENT"]; tom = [c for c in cs if c["jugement"] == "TOMBE"]
    if len(tom) >= 2:
        return "TOMBE"
    if non_lue_possible and not (ten or tom):
        return "NON LUE"
    if len(ten) + len(tom) < jugees_min:
        return "NON CONCLUANT"
    if par_creneau and any(sum(1 for c in ten if c["creneau"] == s) < par_creneau for s in ORDRE):
        return "NON CONCLUANT"
    return "TENU SAUF UNE CELLULE" if tom else "TENU"

def lire_cellule(c):
    """Controle la forme du fichier de la cellule et rend ses mesures, ou leve ValueError."""
    chemin = os.path.join(RUN, "sonde_vide_%s.json" % c["id"])
    if not os.path.exists(chemin):
        raise ValueError("fichier absent")
    S = json.load(open(chemin))
    if S.get("sonde_canon") != CANON_SONDE or S.get("moteur_canon") != CANON_MOTEUR or S.get("source_bloc_canon") != CANON_SOURCE_BLOC:
        raise ValueError("canons de la sonde, du moteur ou du bloc du lecteur")
    if S.get("prevol") is not PREVOL or S.get("table_canon") != canon_B(TABLE):
        raise ValueError("le fichier n'a pas ete produit sur cette table, ou pas dans ce mode")
    x = S.get("cellule") or {}
    if (x.get("id"), x.get("w2"), x.get("m"), x.get("g"), x.get("r_c")) != (c["id"], c["w2"], c["m"], c["g"], c["r_c"]) or x.get("eta0") != c["eta0"]:
        raise ValueError("la cellule du fichier n'est pas celle de la table")
    if S.get("reglage", {}).get("ks") != KS or S.get("reglage", {}).get("absorbeurs") != ABSORBEURS:
        raise ValueError("barreaux ou absorbeurs")
    for nom in (("jumeau",) if PREVOL else ("jumeau", "fantome")):
        rec = S.get(nom)
        if not rec or rec.get("signe") != (+1 if nom == "jumeau" else -1) or rec.get("site") != [0, 0] or rec.get("E_depart") != 0.0:
            raise ValueError("%s : signe, site ou energie de depart" % nom)
        if sorted(rec["traj"]) != ["A", "B", "C", "D"] or any(sorted(int(k) for k in rec["traj"][a]) != KS for a in rec["traj"]):
            raise ValueError("%s : trajectoires incompletes" % nom)
        for a, forme, dr, couches in ABSORBEURS:
            g = rec["absorbeurs"][a]
            if (g["forme"], g["bord"], g["couches"], g["N"]) != (forme, c["r_c"] + dr, couches, c["r_c"] + dr + couches):
                raise ValueError("%s : geometrie de l'absorbeur %s" % (nom, a))
    if PREVOL and S.get("fantome") is not None:
        raise ValueError("un fichier de pre-vol porte une lecture du fantome")
    return S

def temoin(S):
    tr = S["jumeau"]["traj"]; lect = [tr[a][str(k)] for a in ("A", "B", "C", "D") for k in KS]
    suivis = sum(1 for r in lect if r.get("suivi"))
    gam = [r["gamma"] for r in lect if r.get("suivi") and r.get("gamma") is not None and math.isfinite(r["gamma"])]
    return {"lectures": len(lect), "suivies": suivis, "plus_grande_largeur": (max(gam) if gam else None)}

def main():
    out = {"feuille": "feuille_vide_machine1_v1", "feuille_canon": canon_B(os.path.abspath(__file__)), "table_canon": canon_B(TABLE), "prevol": PREVOL,
           "feuille_lecteur_canon": CANON_FEUILLE_LECTEUR, "sonde_canon": CANON_SONDE,
           "reglage": {"temoin_max": TEMOIN_MAX, "v1_jugees_min": V1_JUGEES_MIN, "v1_tenues_par_creneau_min": V1_TENUES_PAR_CRENEAU_MIN, "vp_jugees_min": VP_JUGEES_MIN,
                       "tau_plateau": 0.05, "tau_accord": 0.05}}
    print("=" * 100); print("FEUILLE DU GEL LARGEUR DU VIDE v1%s" % (" -- PRE-VOL, RIEN N'EST JUGE" if PREVOL else "")); print("=" * 100)
    f_inst = os.path.join(RUN, "verdict_ter_instrument.json")
    inst = json.load(open(f_inst)).get("instrument") if os.path.exists(f_inst) else "ABSENT"
    out["instrument"] = inst; out["instrument_canon"] = canon_B(f_inst) if os.path.exists(f_inst) else None
    print("INSTRUMENT DU LECTEUR (etage 0, ancres, etage 1 ; pieces deposees) : %s" % inst)
    cellules = []; incomplet = []
    for c in CELLULES:
        rec = {k: c[k] for k in ("id", "creneau", "ligne", "w2", "delta", "m", "g", "tolerance", "etendue", "ln_G3")}
        try:
            S = lire_cellule(c)
        except ValueError as e:
            incomplet.append("%s : %s" % (c["id"], e)); rec["forme"] = str(e); cellules.append(rec); continue
        rec["temoin"] = temoin(S)
        if not PREVOL:
            j = L.juger_etat(S["fantome"]["traj"], None); P = j["plateaux"]
            rec["lecteur"] = {"statut": j["statut"], "echecs": j["echecs"], "non_lisibles": j["non_lisibles"],
                              "plateaux": {a: {k: P[a].get(k) for k in ("statut", "k0", "etalement", "Gamma_pl", "ecart_ln_A")} for a in ("A", "B", "C", "D")},
                              "suivies": sum(1 for a in ("A", "B", "C", "D") for k in KS if S["fantome"]["traj"][a][str(k)].get("suivi")),
                              "poids_min": min([S["fantome"]["traj"][a][str(k)]["poids_site"] for a in ("A", "B", "C", "D") for k in KS
                                                if S["fantome"]["traj"][a][str(k)].get("poids_site") is not None] or [None])}
        cellules.append(rec)
    out["cellules"] = cellules; out["incomplet"] = incomplet
    if incomplet:
        print("RUN INCOMPLET : %d cellules sans fichier conforme" % len(incomplet))
        for x in incomplet:
            print("    " + x)
    if PREVOL:
        print("PRE-VOL : le fantome n'est pas lu. Temoin (jumeau) par cellule : lectures suivies, plus grande largeur")
        for r in cellules:
            if "temoin" in r:
                print("  %-6s w2 = %-9s m = %-2d : %d sur %d ; %s" % (r["id"], r["w2"], r["m"], r["temoin"]["suivies"], r["temoin"]["lectures"],
                      ("%.2e" % r["temoin"]["plus_grande_largeur"]) if r["temoin"]["plus_grande_largeur"] is not None else "aucune"))
        out["verdict"] = "PRE-VOL, RIEN N'EST JUGE"
        json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True); print("ecrit %s" % SORTIE); return
    if inst != "TIENT" or incomplet:
        out["verdict"] = "L'INSTRUMENT NE TIENT PAS : RIEN N'EST JUGE" if inst != "TIENT" else "RUN INCOMPLET : RIEN N'EST JUGE"
        print(out["verdict"]); json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True); print("ecrit %s" % SORTIE); return
    print("cellule  w2         m   lecteur        temoin     ln Gamma_pl  etal.s  etendue  bande b  ln q      T     jugement")
    for r in cellules:
        lec = r["lecteur"]; tm = r["temoin"]; r["jugement"] = "NON LUE"; r["motif"] = None
        if lec["statut"] != "QUALIFIE":
            r["motif"] = "lecteur : %s" % lec["statut"]
        else:
            A = lec["plateaux"]["A"]; gpl = A["Gamma_pl"]
            s = max([math.log(1.0 + A["etalement"])] + [lec["plateaux"][a]["ecart_ln_A"] for a in ("B", "C", "D")])
            r["ln_Gamma_pl"] = math.log(gpl); r["etalement_du_lecteur"] = s
            tm["rapport_au_plateau"] = (tm["plus_grande_largeur"] / gpl) if tm["plus_grande_largeur"] is not None else None
            tm["tient"] = bool(tm["suivies"] == tm["lectures"] and tm["rapport_au_plateau"] is not None and tm["rapport_au_plateau"] <= TEMOIN_MAX)
            if not tm["tient"]:
                r["motif"] = "temoin : %d lectures suivies sur %d, rapport au plateau %s" % (tm["suivies"], tm["lectures"], tm["rapport_au_plateau"])
            else:
                lnq = r["ln_G3"] - r["ln_Gamma_pl"]; b = r["etendue"] + s; Tt = r["tolerance"]
                r["ln_q"] = lnq; r["bande"] = b
                r["jugement"] = "TIENT" if abs(lnq) <= Tt - b else ("TOMBE" if abs(lnq) > Tt + b else "NON JUGEABLE")
                c = [x for x in CELLULES if x["id"] == r["id"]][0]
                r["consigne"] = {"signe_de_ln_q": (1 if lnq > 0 else -1), "signe_de_delta": (1 if r["delta"] > 0 else -1),
                                 "ln_q_ordre2": c["ln_G2"] - r["ln_Gamma_pl"], "ln_q_ordre1": c["ln_G1"] - r["ln_Gamma_pl"],
                                 "ln_q_loi_d_echelle": math.log(abs(r["delta"])) + c["ln_Phi_etoile"] - r["ln_Gamma_pl"],
                                 "ln_q_forme_fermee": c["ln_forme_fermee"] - r["ln_Gamma_pl"],
                                 "ln_Gamma_pl_sur_delta": r["ln_Gamma_pl"] - math.log(abs(r["delta"])),
                                 "attente_sous_correction_mediane": c["attente"]["sous_correction_mediane"], "attente_sous_correction_pire": c["attente"]["sous_correction_pire"]}
        print("%-7s  %-9s  %-2d  %-13s  %-9s  %-11s  %-6s  %.4f   %-7s  %-8s  %.2f  %s%s" % (
            r["id"], r["w2"], r["m"], lec["statut"], ("tenu" if tm.get("tient") else ("--" if "tient" not in tm else "NON TENU")),
            ("%+.4f" % r["ln_Gamma_pl"]) if "ln_Gamma_pl" in r else "--", ("%.4f" % r["etalement_du_lecteur"]) if "etalement_du_lecteur" in r else "--", r["etendue"],
            ("%.4f" % r["bande"]) if "bande" in r else "--", ("%+.4f" % r["ln_q"]) if "ln_q" in r else "--", r["tolerance"], r["jugement"],
            (" (%s)" % r["motif"]) if r["motif"] else ""))
    lis = [r for r in cellules if r["ligne"] == "lisible"]; pro = [r for r in cellules if r["ligne"] == "profonde"]
    compte = lambda cs: {k: sum(1 for r in cs if r["jugement"] == k) for k in ("TIENT", "TOMBE", "NON JUGEABLE", "NON LUE")}
    out["V1"] = {"issue": issue_ligne(lis, V1_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, False), "comptes": compte(lis), "cellules": len(lis),
                 "tombees": [r["id"] for r in lis if r["jugement"] == "TOMBE"]}
    out["VP"] = {"issue": issue_ligne(pro, VP_JUGEES_MIN, 0, True), "comptes": compte(pro), "cellules": len(pro),
                 "tombees": [r["id"] for r in pro if r["jugement"] == "TOMBE"]}
    lues = [r for r in cellules if "ln_q" in r]
    out["consigne"] = {"cellules_jugees_ou_non_jugeables": len(lues),
                       "ln_q_du_signe_de_delta": sum(1 for r in lues if r["consigne"]["signe_de_ln_q"] == r["consigne"]["signe_de_delta"]),
                       "ln_q_du_signe_de_la_sous_correction": sum(1 for r in lues if r["consigne"]["attente_sous_correction_mediane"] * r["ln_q"] > 0),
                       "ordre3_plus_pres_que_ordre1": sum(1 for r in lues if abs(r["ln_q"]) < abs(r["consigne"]["ln_q_ordre1"])),
                       "ordre3_plus_pres_que_la_loi_d_echelle": sum(1 for r in lues if abs(r["ln_q"]) < abs(r["consigne"]["ln_q_loi_d_echelle"])),
                       "plus_grand_ln_q_forme_fermee": max([abs(r["consigne"]["ln_q_forme_fermee"]) for r in lues] or [None])}
    for nom, quoi in (("V1", "ligne lisible, %d cellules" % len(lis)), ("VP", "ligne profonde, %d cellules, hors de V1" % len(pro))):
        v = out[nom]; print("%s (%s) : %s ; tenues %d, tombees %d %s, non jugeables %d, non lues %d" % (nom, quoi, v["issue"], v["comptes"]["TIENT"], v["comptes"]["TOMBE"],
              v["tombees"], v["comptes"]["NON JUGEABLE"], v["comptes"]["NON LUE"]))
    k = out["consigne"]
    print("consigne, sans jugement, sur %d cellules lues : ln q du signe de delta a %d ; du signe de la sous-correction a %d ; ordre 3 plus pres que l'ordre 1 a %d, que la loi d'echelle a %d ; plus grand |ln q| de la forme fermee %s" % (
        k["cellules_jugees_ou_non_jugeables"], k["ln_q_du_signe_de_delta"], k["ln_q_du_signe_de_la_sous_correction"], k["ordre3_plus_pres_que_ordre1"], k["ordre3_plus_pres_que_la_loi_d_echelle"],
        ("%.4f" % k["plus_grand_ln_q_forme_fermee"]) if k["plus_grand_ln_q_forme_fermee"] is not None else "--"))
    out["verdict"] = "V1 %s ; VP %s" % (out["V1"]["issue"], out["VP"]["issue"])
    print("VERDICT : %s" % out["verdict"])
    json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True); print("ecrit %s" % SORTIE)

main()
