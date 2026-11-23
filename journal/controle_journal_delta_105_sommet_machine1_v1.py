# -*- coding: ascii -*-
"""CONTROLE DU PROJET D'ACTE DU RUN DU GEL "SOMMET" -- machine 1, v1, 2026-11-23. Aucun calcul de physique, aucune 2D.
Relit l'acte ECRIT et le confronte a ses sources par un autre chemin que le script de construction :
  - les nombres par cellule sont recalcules depuis le verdict DU RUN de machine 2 (et non depuis le verdict rejoue par
    machine 1, d'ou la construction les tire) et depuis la table gelee : ln q = ln G3* (table) - ln plateau (run),
    bande = etendue (table) + etalement (run), jugement refait de la regle de la section 5 du gel ;
  - S1, la portee, les comptes par w2 et par kappa sont refaits des LIGNES de l'acte ;
  - les lectures non suivies, le poids, le temoin sont recomptes dans les 112 fichiers de lecture ;
  - chaque empreinte citee est recalculee sur le fichier (convention B) ; chaque mot rapporte de l'operateur est cherche
    dans la note de machine 2 qui le rapporte ; les heures et les durees sont relues dans le journal du pilote ;
  - ce que l'acte dit du delta 102 est cherche dans l'acte depose (464ba00a6905e3a5).
Puis CONTRE-EPREUVE : l'acte est altere en memoire (un nombre, une empreinte, un compte, un mot, une reserve retiree) ;
chaque alteration doit faire echouer un controle au moins. Les fichiers de machine 2 sont lus comme des donnees.
Usage : python3 -I -B controle_journal_delta_nn_sommet_machine1_v1.py <acte.md> <racine de travail de machine 1>"""
import sys, os, re, json, math, hashlib, unicodedata
from fractions import Fraction as F
ACTE, RACINE = sys.argv[1], sys.argv[2]
ch = lambda *p: os.path.join(RACINE, *p)
RUN = ch("recu_23m", "lot", "certif_gel_sommet_partie2_machine2", "run_sommet_2026-11-23")
FICH = {"table": ch("lot22k", "table_cellules_gel_sommet_v1.json"), "gel1": ch("lot22i", "gel_sommet_partie1_regle_tirage_pre_enregistrement_v1.md"),
        "gel2": ch("lot22k", "gel_sommet_partie2_instrument_enonce_pre_enregistrement_v1.md"), "commune": ch("lot22i", "eligibilite_candidates_sommet_v1.json"),
        "feuille": ch("lot22k", "feuille_gel_sommet_machine1_v1.py"), "pilote": ch("lot22k", "pilote_gel_sommet_machine1_v1.py"),
        "rejeu": ch("rejeu_23a", "verdict_sommet_rejoue_machine1.json"), "verdict": os.path.join(RUN, "verdict_sommet.json"),
        "garde": os.path.join(RUN, "garde_sommet.json"), "instrument": os.path.join(RUN, "verdict_ter_instrument.json"), "journal": os.path.join(RUN, "pilote_gel_sommet.log"),
        "note_R": ch("recu_23m", "lot", "POUR_MACHINE1_resultat_run_gel_sommet_machine2_v1.md"), "note_C": ch("recu_23l", "lot", "POUR_MACHINE1_certification_gel_sommet_partie2_machine2_v1.md"),
        "note_T": ch("recu_22k", "lot", "POUR_MACHINE1_tirage_graine_114565_gel_sommet_machine2_v1.md"), "note_Q": ch("recu_22h", "lot", "POUR_MACHINE1_Q_sommet_demolition_machine2_v1.md"),
        "note_Q2": ch("recu_22i", "lot", "POUR_MACHINE1_Q2_signe_machine2_v1.md"), "acte_102": ch("registre", "clone", "journal", "journal_delta_102_largeur_vide_v1.md"),
        "bloc_abs": ch("registre", "clone", "scripts", "chaine_adaptee_bloc_machine1_v1.py")}
MANIF = {"3ba4618d7976c6ea": ch("envoi_22i", "MANIFESTE_lot_machine1_2026-11-22_Q2_notee_et_gel_sommet_partie1_v1.txt"), "a2dc5cb2b9c3da0d": ch("envoi_22k", "MANIFESTE_lot_machine1_2026-11-22_gel_sommet_partie2_v1.txt"),
         "423ec0fd24240977": ch("envoi_22g", "MANIFESTE_lot_machine1_2026-11-22_pole_court_lu_et_qualification_du_sommet_v1.txt"), "074b131287ad2b6f": ch("envoi_22h", "MANIFESTE_lot_machine1_2026-11-22_Q_notee_et_Q2_attendus_v1.txt"),
         "c58c2b3f533c516b": ch("recu_22h", "lot", "MANIFEST_lot_machine2_Q_sommet_v1.txt"), "295b2b1549b076c2": ch("recu_22i", "lot", "MANIFEST_lot_machine2_Q2_signe_v1.txt"),
         "21e9bddfe5db83b2": ch("recu_22j", "lot", "MANIFEST_lot_machine2_certification_gel_sommet_partie1_v1.txt"), "3db782eea5023b31": ch("recu_22k", "lot", "MANIFEST_lot_machine2_tirage_graine_114565_gel_sommet_v1.txt"),
         "b7f328b916ba720d": ch("recu_23l", "lot", "MANIFEST_lot_machine2_certification_gel_sommet_partie2_v1.txt"), "735b9394013b02db": ch("recu_23m", "lot", "MANIFEST_lot_machine2_resultat_run_gel_sommet_v1.txt")}
def canon_B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
lire = lambda cle: open(FICH[cle], encoding="utf-8").read()
aplat = lambda s: " ".join(s.split())
# ---------------------------------------------------------------- les sources, lues une fois
T = json.load(open(FICH["table"])); A = json.load(open(FICH["verdict"])); TC = {c["id"]: c for c in T["cellules"]}; AC = {c["id"]: c for c in A["cellules"]}
IDS = [c["id"] for c in T["cellules"]]; KAPPAS = ["0.0363", "0.0530", "0.0800", "0.1300", "0.2000", "0.4000", "1.0000"]; KS = T["regle"]["barreaux"]; TOL = T["regle"]["tolerance"]
CANONS = {k: canon_B(v) for k, v in FICH.items()}; CANONS_MANIF = {k: canon_B(v) for k, v in MANIF.items()}
JOURNAL = lire("journal"); NOTES = {k: aplat(lire(k)) for k in ("note_R", "note_C", "note_T", "note_Q", "note_Q2")}; ACTE_102 = aplat(lire("acte_102")); GEL2 = aplat(lire("gel2"))
dec = lambda w: "%.5f" % float(F(w))
lnpl = {i: AC[i]["ln_Gamma_pl"] for i in IDS}; s_lu = {i: AC[i]["etalement_du_lecteur"] for i in IDS}
lnq = {i: TC[i]["ln_G3"] - lnpl[i] for i in IDS}; bande = {i: TC[i]["etendue"] + s_lu[i] for i in IDS}
def juge(i):
    if AC[i]["lecteur"]["statut"] != "QUALIFIE" or not AC[i]["temoin"]["tient"]: return "NON LUE"
    return "TIENT" if abs(lnq[i]) <= TOL - bande[i] else ("TOMBE" if abs(lnq[i]) > TOL + bande[i] else "NON JUGEABLE")
# les fichiers de lecture, recomptes
non_suivies = []; poids = []; jum_ns = 0; jum_max = 0.0; n_lect = 0
for i in IDS:
    f = json.load(open(os.path.join(RUN, "lect2D_%s_fantome.json" % i))); j = json.load(open(os.path.join(RUN, "lect2D_%s_jumeau.json" % i)))
    assert f["cellule"]["id"] == i == j["cellule"]["id"]
    for a in "ABCD":
        for k in KS:
            x = f["lecture"]["traj"][a][str(k)]; y = j["lecture"]["traj"][a][str(k)]; n_lect += 1
            (poids.append(x["poids_site"]) if x.get("suivi") else non_suivies.append("%s %s k = %+d" % (i, a, k)))
            jum_ns += not y.get("suivi"); jum_max = max(jum_max, abs(y["gamma"]) / math.exp(lnpl[i]) if y.get("gamma") is not None else 0.0)
plats = [k for k in KS if all(json.load(open(os.path.join(RUN, "lect2D_%s_fantome.json" % i)))["lecture"]["traj"]["A"][str(k)].get("suivi") and
         abs(math.log(json.load(open(os.path.join(RUN, "lect2D_%s_fantome.json" % i)))["lecture"]["traj"]["A"][str(k)]["gamma"]) - lnpl[i]) <= 0.005 for i in IDS)]
# ---------------------------------------------------------------- les controles
def section(texte, n):
    m = re.search(r"(?ms)^nn\.%d .*?(?=^nn\.%d |^-- FIN )" % (n, n + 1), texte); return m.group(0) if m else ""
def controles(texte):
    R = []; ok = lambda nom, cond, detail="": R.append((nom, bool(cond), detail))
    lignes = texte.split("\n"); plat = aplat(texte); S = {n: section(texte, n) for n in range(13)}; SP = {n: aplat(S[n]) for n in S}
    dans = lambda n, phrase: aplat(phrase) in SP[n]
    # --- A. forme
    ok("A1 ASCII", all(ord(c) < 128 for c in texte)); ok("A2 100 colonnes au plus", max(len(l) for l in lignes) <= 100); ok("A3 pas de signe pour cent", chr(37) not in texte)
    ok("A4 en-tete", lignes[0].startswith("DELTA nn -- ") and "VERDICT : S1 TENU." in lignes[:6] and "-- PROJET, VERSION 1" in lignes[:6] and "a contresigner par machine 2" in lignes[5])
    tetes = [l for l in lignes if re.match(r"nn\.\d+ ", l)]; ok("A5 treize sections dans l'ordre", [int(re.match(r"nn\.(\d+)", l).group(1)) for l in tetes] == list(range(13)), str(len(tetes)))
    ok("A6 ligne de fin", texte.endswith("\n-- FIN journal_delta_nn_sommet_v1 --\n")); ok("A7 aucun numero de delta pris", not re.search(r"DELTA \d|delta 10[4-9]", texte))
    # --- B. la table par cellule, contre le verdict DU RUN et la table gelee
    rangs = [l.split() for l in S[3].split("\n") if re.match(r"    [MP][PG][ab]\d ", l)]; L = {r[0]: r for r in rangs}
    ok("B1 56 lignes dans l'ordre de la table", [r[0] for r in rangs] == IDS, str(len(rangs))); w2s = []
    for r in rangs:
        if len(r) > 1 and r[1] not in w2s: w2s.append(r[1])
    if [r[0] for r in rangs] == IDS and all(len(r) == 10 for r in rangs):
        ok("B2 w2, kappa, g", all(L[i][1] == dec(TC[i]["w2"]) and L[i][2] == TC[i]["kappa"] and L[i][3] == TC[i]["g"] for i in IDS))
        ok("B3 plateau lu", all(L[i][4] == "%.5e" % math.exp(lnpl[i]) for i in IDS)); ok("B4 etalement du lecteur", all(L[i][5] == "%.4f" % s_lu[i] for i in IDS))
        ok("B5 etendue de la chaine", all(L[i][6] == "%.4f" % TC[i]["etendue"] for i in IDS)); ok("B6 bande", all(L[i][7] == "%.4f" % bande[i] for i in IDS))
        ok("B7 ln q", all(L[i][8] in ("%+.5f" % lnq[i], "%+.5f" % AC[i]["ln_q"]) and abs(lnq[i] - AC[i]["ln_q"]) < 1e-12 for i in IDS))
        ok("B8 jugement refait de la regle", all(L[i][9] == juge(i) == AC[i]["jugement"] for i in IDS))
        tenues = [i for i in IDS if L[i][9] == "TIENT"]; par_w2 = {}; par_k = {}
        for i in tenues: par_w2[L[i][1]] = par_w2.get(L[i][1], 0) + 1; par_k[L[i][2]] = par_k.get(L[i][2], 0) + 1
        issue = "TOMBE" if sum(L[i][9] == "TOMBE" for i in IDS) >= 2 else ("NON CONCLUANT" if sum(L[i][9] in ("TIENT", "TOMBE") for i in IDS) < 42 or min(par_w2.get(dec(w), 0) for w in set(c["w2"] for c in T["cellules"])) < 4
                 else ("TENU" if len(tenues) == 56 else "TENU SAUF UNE CELLULE"))
        ok("B9 S1 refait des lignes", issue == "TENU" == A["S1"]["issue"] and dans(3, "S1 : TENU. Tenues 56, tombees 0, non jugeables 0, non lues 0."))
        ok("B10 tenues par w2 et par kappa", dans(3, "Tenues par w2 (sur sept) : " + " ; ".join("%s %d" % (w, par_w2.get(w, 0)) for w in w2s) + ".") and
           dans(3, "Tenues par kappa (sur huit) : " + " ; ".join("%s %d" % (k, par_k.get(k, 0)) for k in KAPPAS) + "."))
        ok("B11 portee", dans(3, "Portee : " + " ".join(k for k in KAPPAS if par_k.get(k, 0) >= 4) + ".") and A["S1"]["portee_kappa"] == [k for k in KAPPAS if par_k.get(k, 0) >= 4])
    else:
        ok("B2-B11 table illisible", False)
    # --- C. temoins positifs, garde, instrument
    tem = [l.split() for l in S[2].split("\n") if re.match(r"    Q2?[a-f] ", l)]; AT = {t["id"]: t for t in A["temoins_positifs"]["points"]}
    ok("C1 neuf temoins a leur reference", len(tem) == 9 and all(r[0] == c["id"] and r[1] == c["w2"] and r[2] == c["g"] and r[3] == "%.5e" % math.exp(AT[c["id"]]["ln_Gamma_pl"]) and
       r[4] == "%.5e" % math.exp(c["ln_Gamma_pl_reference"]) and abs(AT[c["id"]]["ln_Gamma_pl"] - c["ln_Gamma_pl_reference"]) <= 0.001 and float(r[5]) == AT[c["id"]]["ln_Gamma_pl"] - c["ln_Gamma_pl_reference"]
       for r, c in zip(tem, T["temoins_positifs"])))
    hg = re.search(r"(\d\d:\d\d:\d\d) GARDE : TIENT", JOURNAL).group(1); premieres = re.findall(r"(\d\d:\d\d:\d\d)   lecture (?:MP|PP|MG|PG)", JOURNAL)
    G = json.load(open(FICH["garde"]))
    ok("C2 instrument et garde tiennent", A["instrument"] == "TIENT" == G["instrument"] and G["verdict"].startswith("TIENT") and G["etape"] == "temoins" and G["temoins_positifs"]["tenus"] == 9 == A["temoins_positifs"]["tenus"]
       and dans(2, "Etage A : l'instrument du lecteur TIENT") and dans(2, "Les neuf temoins positifs TIENNENT"))
    ok("C3 heure de la garde", dans(2, "jouee a %s, avant la premiere lecture de cellule" % hg) and JOURNAL.index("GARDE : TIENT") < JOURNAL.index("ETAGE B") and min(premieres) > hg, hg)
    # --- D. les nombres de tete et les lectures
    pire = max(IDS, key=lambda i: abs(lnq[i])); juste = min(IDS, key=lambda i: TOL - bande[i] - abs(lnq[i]))
    sous = sum(abs(lnq[i]) < TC[i]["etendue"] for i in IDS); sous_s = sum(abs(lnq[i]) < s_lu[i] for i in IDS)
    ok("D1 plus grand ecart", dans(0, "|ln q|, vaut %.5f au plus (%s), pour une tolerance de 0.01" % (abs(lnq[pire]), pire)))
    ok("D2 largeurs et couplages", dans(0, "a des largeurs de %.2e a %.2e et des couplages de %s a %s." % (math.exp(min(lnpl.values())), math.exp(max(lnpl.values())),
       min((TC[i]["g"] for i in IDS), key=float), max((TC[i]["g"] for i in IDS), key=float))))
    ok("D3 sous l'etendue", dans(0, "sous l'etendue de la chaine a %d cellules sur 56" % sous) and dans(5, "sous l'etendue de la chaine a %d cellules sur 56, et sous l'etalement du lecteur a %d." % (sous, sous_s)))
    ok("D4 plus grande bande et plus petite marge", dans(5, "la plus grande bande est %.4f, et la cellule la plus pres de sa limite (%s) garde %.4f entre |ln q| et T - b." % (max(bande.values()), juste, TOL - bande[juste] - abs(lnq[juste]))))
    ok("D5 lectures du fantome", dans(3, "Fantome : %d lectures suivies sur %d ; les %d non suivies (%s) sont hors des fenetres retenues" % (n_lect - len(non_suivies), n_lect, len(non_suivies), " ; ".join(non_suivies))))
    ok("D6 jumeau", dans(3, "Jumeau : %d non suivie sur %d ; sa plus grande largeur vaut %.1e du plateau au plus (seuil 1e-6)." % (jum_ns, n_lect, jum_max)) and jum_max <= 1e-6)
    ok("D7 poids et barreaux plats", dans(3, "Plus petit poids du site (0, 0) sur les lectures suivies du fantome : %.4f." % min(poids)) and dans(3, "plate a 0.005 pres aux barreaux k = %d a %d a toutes les cellules." % (plats[0], plats[-1]))
       and plats == list(range(plats[0], plats[-1] + 1)))
    ok("D8 les huit w2 et la graine", dans(0, "graine de l'operateur (114565) : huit w2 (%s), sept kappa chacun (%s)." % (", ".join(w2s), ", ".join(KAPPAS))) and str(T["graine"]) == "114565" == A["graine"])
    # --- E. le consigne (nn.6), refait
    lig6 = {l.split()[0]: l.split() for l in S[6].split("\n") if re.match(r"    \d\.\d{4}  [+-]", l)}; e_ok = len(lig6) == 7; signes = 0; etal_lu = []; etal_ch = []
    for k in KAPPAS:
        ids = [i for i in IDS if TC[i]["kappa"] == k]; v = sorted(lnq[i] for i in ids); ph = sorted(lnpl[i] - math.log(abs(float(F(TC[i]["w2"]) - 2))) for i in ids)
        pc = sorted(TC[i]["ln_G3"] - math.log(abs(float(F(TC[i]["w2"]) - 2))) for i in ids); signes += len(set(x > 0 for x in v)) == 1; etal_lu.append(ph[-1] - ph[0]); etal_ch.append(pc[-1] - pc[0])
        e_ok = e_ok and k in lig6 and lig6[k][1:] == ["%+.5f" % v[0], "%+.5f" % v[-1], "%+.5f" % (sum(v) / 8), "%d" % sum(x < 0 for x in v), "%.5e" % math.exp(ph[0]), "%.5e" % math.exp(ph[-1]),
                                                       "%.5f" % (ph[-1] - ph[0]), "%.5f" % (pc[-1] - pc[0])]
    ok("E1 table par kappa", e_ok); ok("E2 meme signe aux huit w2", dans(6, "il a le meme signe aux huit w2 a %d kappa sur sept" % signes))
    ok("E3 superposition", dans(6, "varie de %.5f au plus en logarithme entre les huit w2" % max(etal_lu)) and dans(6, "la chaine donne %.5f au plus" % max(etal_ch)))
    mir = []
    for k in KAPPAS:
        m_ = [i for i in IDS if TC[i]["kappa"] == k and TC[i]["w2"] == "199989/100000"][0]; p_ = [i for i in IDS if TC[i]["kappa"] == k and TC[i]["w2"] == "200011/100000"][0]
        mir.append((k, lnpl[m_] - lnpl[p_], TC[m_]["ln_G3"] - TC[p_]["ln_G3"]))
    ok("E4 paires miroirs", dans(6, " ; ".join("%s %+.5f (%+.5f)" % x for x in mir) + ".") and dans(6, "s'y accordent a %.5f pres" % max(abs(x[1] - x[2]) for x in mir)) and max(abs(x[1]) for x in mir) < 1e-4)
    o3 = sum(abs(TC[i]["ln_G3"] - lnpl[i]) < abs(TC[i]["ln_G1"] - lnpl[i]) for i in IDS); neg = sum(lnq[i] < 0 for i in IDS); sd = sum((lnq[i] > 0) == (float(F(TC[i]["w2"])) > 2) for i in IDS)
    ok("E5 ordres et signes", dans(6, "plus pres du plateau lu que le premier ordre a %d cellules sur 56" % o3) and dans(6, "a %d cellules, et du signe de delta a %d." % (neg, sd)))
    t0 = " ; ".join("%s %.4f" % (k, sum(math.exp(lnpl[i]) / (float(k) * abs(float(F(TC[i]["w2"]) - 2))) for i in IDS if TC[i]["kappa"] == k) / 8) for k in KAPPAS)
    g1 = {TC[i]["w2"]: float(TC[i]["g"]) for i in IDS if TC[i]["kappa"] == "1.0000"}; psx = (g1["199989/100000"] + g1["200011/100000"]) / 0.00022
    res = sorted(set("%.4f" % (math.exp(AT[c["id"]]["ln_Gamma_pl"]) / float(c["g"]) * psx) for c in T["temoins_positifs"] if c["w2"] == "2"))
    ok("E6 largeur rapportee au saut", dans(6, "moyenne par kappa : %s." % t0) and dans(6, "elle vaut %s (le saut" % " a ".join(res)))
    # --- F. les annonces
    bar = [i for i in IDS if TC[i]["kappa"] in ("0.0363", "0.0530")]
    ok("F1 A-6", dans(7, "A-6 (0.75) plus grand |ln q| sous 0.001 : oui (%.5f)." % abs(lnq[pire])) and abs(lnq[pire]) < 0.001)
    ok("F2 A-7 tombe", dans(7, "au moins sur seize : NON. Il l'est a %d : aux huit de kappa = 0.0530 et a %d des huit de kappa = 0.0363" % (sum(lnq[i] < 0 for i in bar), sum(lnq[i] < 0 for i in bar if TC[i]["kappa"] == "0.0363")))
       and sum(lnq[i] < 0 for i in bar) < 12 and all(lnq[i] < 0 for i in bar if TC[i]["kappa"] == "0.0530") and dans(7, "Huit annonces sur neuf sont du cote annonce ; A-7 tombe."))
    ok("F3 A-8 et A-9", dans(7, "oui (%d sur 7)." % sum(abs(x[1] - x[2]) <= 0.0001 for x in mir)) and dans(7, "sous 0.001 : oui (%.5f au plus)." % max(etal_lu)) and max(etal_lu) < 0.001)
    ok("F4 probabilites du gel", all(aplat(x) in GEL2 for x in ("A-1 (0.95)", "A-2 (0.97)", "A-3 (0.95)", "A-4 (0.70)", "TENU 0.80", "A-6 (0.75)", "A-7 (0.70)", "A-8 (0.65)", "A-9 (0.75)")) and
       all(x in SP[7] for x in ("A-1 (0.95)", "A-2 (0.97)", "A-3 (0.95)", "A-4 (0.70)", "A-5 S1 TENU (0.80)", "A-6 (0.75)", "A-7 (0.70)", "A-8 (0.65)", "A-9 (0.75)")))
    # --- G. le run, ses heures, ses durees, les mots rapportes
    l0 = JOURNAL.strip().split("\n"); deb, fin = l0[0][:19], l0[-1][:19]; dt = int(re.search(r"duree totale (\d+) s", l0[-1]).group(1)); codes = re.findall(r"code=(\d+) duree=(\d+) s", JOURNAL)
    np_ = int(re.search(r"(\d+) processus", l0[0]).group(1)); dc = [int(d) for d in re.findall(r"lecture (?:MP|PP|MG|PG)\w+ (?:jumeau|fantome)\s+code=0 duree=(\d+) s", JOURNAL)]
    dq = [int(d) for d in re.findall(r"lecture Q\w+ (?:jumeau|fantome)\s+code=0 duree=(\d+) s", JOURNAL)]; da = re.findall(r"lecteur (etage0|ancres|etage1)\s+code=0 duree=(\d+) s", JOURNAL)
    ok("G1 debut, fin, duree, appels", dans(1, "lance le %s et fini a %s (heure de BOCAL4) ; duree totale %d s ; %d appels, tous au code 0" % (deb, fin[11:], dt, len(codes))) and all(c == "0" for c, d in codes)
       and "PRE-VOL" not in l0[0] and "FIN DU PILOTE" in l0[-1])
    ok("G2 processus et durees", dans(1, "%d processus, drapeau -P, sans --prevol." % np_) and "drapeau -P" in l0[0] and len(dc) == 112 and len(dq) == 18 and
       dans(1, "etage A %s s, %s s et %s s (etage 0, ancres, etage 1, en parallele) ; les dix-huit lectures des temoins de %d a %d s ; les 112 lectures des cellules de %d a %d s, %d a la fois."
            % (dict(da)["etage0"], dict(da)["ancres"], dict(da)["etage1"], min(dq), max(dq), min(dc), max(dc), np_)))
    ok("G3 canons imprimes par le pilote", all(c in JOURNAL for c in ("ed4c3886b17fcdc3", "82a0be882568fe0c", "d5cc48f48e37af99", "83701094e6a2b965", "4238e2b262119f83", "47a84eae6052f006", "ac934e0caaa59c08")) and
       A["feuille_canon"] == CANONS["feuille"] and A["table_canon"] == CANONS["table"])
    mots = (("\"RUn\"", "note_R"), ("\"GO\"", "note_C"), ("\"Oui GO !\"", "note_Q"), ("\"oui ces 4 pts\"", "note_Q2"), ("\"graine 114565\"", "note_T"))
    ok("G4 mots de l'operateur rapportes par machine 2", all(m in SP[1] and m in NOTES[n] for m, n in mots), " ".join(m for m, n in mots if not (m in SP[1] and m in NOTES[n])))
    ok("G5 certification : juge, bancs, pre-vol", all(x in NOTES["note_C"] for x in ("sur 38 scenarios", "30 cas, 30 tenus", "12 cas, 12 tenus", "00:05:47 PRE-VOL", "duree totale 1120 s")) and
       dans(1, "a 38 scenarios sur 38") and dans(1, "(30 cas sur 30, 12 sur 12)") and dans(1, "son pre-vol finit a 00:05:47, le run part a %s" % deb[11:]) and "00:05:47" < deb[11:] and dans(1, "1120 s."))
    ok("G6 E19 et le tour non attendu", dans(1, "Machine 1 n'a lu en 2D le systeme a fantome ni le jumeau a aucune cellule ni a aucun w2 tire") and "Je n'ai lu aucune cellule avant la fin du pilote" in NOTES["note_R"] and
       dans(1, "le tour n'a pas ete attendu") and dans(1, "Machine 1 n'a pas vu ce message. A l'operateur de l'attester.") and "Je ne t'ai pas retire ce tour" in NOTES["note_R"])
    ok("G7 remarques R-1 a R-5 et ecarts E-1 a E-4", all(("R-%d" % n) in SP[9] and ("R-%d." % n) in NOTES["note_C"] for n in range(1, 6)) and all(("E-%d" % n) in SP[9] and ("E-%d " % n) in GEL2 for n in range(1, 5)))
    # --- H. le rejeu
    Bj = json.load(open(FICH["rejeu"])); BC = {c["id"]: c for c in Bj["cellules"]}
    ec = max(max(abs(BC[i][k] - AC[i][k]) for i in IDS) for k in ("ln_q", "ln_Gamma_pl", "bande", "etalement_du_lecteur"))
    ok("H1 rejeu : meme verdict, memes jugements", Bj["verdict"] == A["verdict"] == "S1 TENU" and Bj["S1"] == A["S1"] and all(BC[i]["jugement"] == AC[i]["jugement"] and BC[i]["lecteur"]["statut"] == AC[i]["lecteur"]["statut"] for i in IDS)
       and dans(4, "Verdict rejoue : S1 TENU (canon %s)" % CANONS["rejeu"]) and dans(4, "l'etalement : %.1e" % ec) and CANONS["rejeu"] != CANONS["verdict"])
    ok("H2 lot de resultat et juge de machine 2", dans(4, "(735b9394013b02db, 284 pieces, aucun ecart)") and sum(1 for l in open(MANIF["735b9394013b02db"]) if re.match(r"[0-9a-f]{16} [0-9a-f]{16} ", l)) == 284 and
       "rend le meme verdict, la meme portee" in NOTES["note_R"] and len([f for f in os.listdir(RUN) if f.startswith("lect2D_")]) == 130 and dans(4, "il n'y a qu'UNE mesure 2D"))
    # --- I. les empreintes
    attendus = {"1e5039cade55d13f": "gel1", "81a2febcfce49007": "gel2", "4238e2b262119f83": "table", "77ce2a6c7e867011": "commune", "ac934e0caaa59c08": "feuille", "ed4c3886b17fcdc3": "pilote", "49a40d9098b55361": "bloc_abs"}
    ok("I1 pieces du gel et du registre", all(CANONS[v] == k and k in S[12] for k, v in attendus.items()), " ".join(k for k, v in attendus.items() if CANONS[v] != k))
    ok("I2 pieces du run et notes", all(CANONS[k] in S[12] for k in ("note_C", "note_R", "journal", "instrument", "garde", "verdict", "rejeu")) and dans(2, "(verdict %s)" % CANONS["instrument"]) and
       dans(2, "Garde : TIENT (%s)" % CANONS["garde"]) and dans(3, "Verdict du run : S1 TENU (canon %s)" % CANONS["verdict"]) and ("CANON DU VERDICT : %s" % CANONS["verdict"]) in JOURNAL and A["instrument_canon"] == CANONS["instrument"])
    ok("I3 canons des dix lots refaits de leurs manifestes", all(CANONS_MANIF[k] == k and k in plat for k in MANIF), " ".join(k for k in MANIF if CANONS_MANIF[k] != k or k not in plat))
    cites = set(re.findall(r"\b[0-9a-f]{16}\b", texte)); connus = set(MANIF) | set(CANONS.values()) | {"d5cc48f48e37af99", "83701094e6a2b965", "47a84eae6052f006", "82a0be882568fe0c"}
    ok("I4 aucune empreinte citee sans source", cites <= connus, " ".join(sorted(cites - connus)))
    ok("I5 pieces deposees citees", canon_B(ch("registre", "clone", "scripts", "sonde_lecteur_gel_loi_machine1_v1.py")) == "d5cc48f48e37af99" and canon_B(ch("registre", "clone", "scripts", "lecture_lecteur_gel_loi_machine1_v1.py")) == "83701094e6a2b965"
       and canon_B(ch("registre", "clone", "scripts", "m17_chaine_v17.py")) == "82a0be882568fe0c" and A["pilote_machine2_canon"] == "47a84eae6052f006" and CANONS["acte_102"] == "464ba00a6905e3a5")
    # --- J. le delta 102 et les reserves
    ok("J1 ce que l'acte dit du delta 102", all(x in ACTE_102 for x in ("(delta = -0.018, -0.003, +0.005, +0.017)", "(3, 4, 5, 6 barreaux : ligne lisible ; 8, 12, 16 : ligne profonde)", "Ils s'ecartent de 0.0098 a 3 barreaux",
       "et 0.1262 a 16. La chaine predit ces ecarts")) and dans(6, "s'ecartaient de 0.0098 a trois barreaux jusqu'a 0.1262 a seize") and dans(0, "trois a seize barreaux de barriere, |delta| de 0.003 a 0.018, kappa au plus 0.0262")
       and "kappa_3 = 0.0262 est le kappa des cellules de trois barreaux du gel" in aplat(lire("gel1")))
    reserves = ((0, "il ne MESURE pas l'erreur de la chaine"), (0, "Il n'oppose pas les ordres de la chaine."), (0, "Cinquante-six cellules sont HUIT tirages"), (0, "ce gel et le delta 102 ne se recouvrent pas"),
                (0, "cet acte ne dit rien de la duree de vie du systeme ferme."), (5, "n'est donc pas resolu par ce gel"), (5, "et non cinquante-six largeurs independantes"), (6, "Rien n'en est juge, et cet acte n'en donne pas la cause."), (6, "Consigne, pas juge."),
                (8, "Cet acte ecrit moins, et autrement."), (8, "Les deux domaines ne se touchent pas"), (8, "Il N'ecrit PAS : que la chaine est exacte"), (8, "que l'ordre 3 fait mieux que le premier ordre"),
                (8, "quoi que ce soit de la duree de vie du systeme ferme"), (8, "quoi que ce soit de w2 = 2 exactement"), (8, "ni au-dela de kappa = 1"), (8, "\"cinquante-six cellules\" sans dire \"huit tirages\""),
                (10, "une erreur commune au lecteur et a la chaine ne se verrait pas"), (10, "calculee sur une seule machine (BOCAL4), une seule fois"), (10, "ils eprouvent la reproduction, pas l'exactitude"),
                (10, "Rien n'est dit du systeme ferme."), (10, "sont rapportes par elle"), (11, "Depot : a la decision de l'operateur, numero pris au depot."), (2, "pas qu'il lit juste"))
    ok("J2 les reserves sont ecrites", all(dans(n, p) for n, p in reserves), " | ".join(p for n, p in reserves if not dans(n, p)))
    ok("J3 la phrase permise par le gel", aplat("a cinquante-six cellules tirees au sort, en huit tirages, pour |delta| de 0.00007 a 0.00048 et kappa de 0.0363 a 1") in GEL2 and
       dans(8, "a cinquante-six cellules tirees au sort, en huit tirages, pour |delta| de 0.00007 a 0.00048 et kappa de 0.0363 a 1") and dans(8, "a 0.01 pres en logarithme, au-dela de sa propre etendue et de l'etalement du lecteur")
       and aplat("Avec le delta 102, la loi d'echelle de la largeur du vide est alors eprouvee des ailes au sommet") in GEL2 and min(abs(float(F(c["w2"]) - 2)) for c in T["cellules"]) > 0.000069 and max(abs(float(F(c["w2"]) - 2)) for c in T["cellules"]) < 0.000481)
    ok("J4 defauts de la plume dits", all(dans(9, p) for p in ("D-REL-29", "D-REL-30", "Son annonce A-7 (nn.7)", "Le tour de correction non attendu : nn.1.")) and
       dans(9, "(il vaut %.4f)" % min(AC[i]["lecteur"]["poids_min"] for i in IDS)))
    return R
texte = open(ACTE, encoding="ascii").read()
print("CONTROLE DU PROJET D'ACTE DU GEL SOMMET -- machine 1 -- acte %s (canon B %s)" % (os.path.basename(ACTE), canon_B(ACTE)))
print("sources : verdict du run %s ; table gelee %s ; verdict rejoue %s ; %d lectures du fantome et %d du jumeau recomptees" % (CANONS["verdict"], CANONS["table"], CANONS["rejeu"], n_lect, n_lect))
res = controles(texte); echecs = [r for r in res if not r[1]]
for nom, cond, detail in res: print("  %-5s %s%s" % ("ok" if cond else "ECHEC", nom, (" : " + detail) if (detail and not cond) else ""))
print("CONTROLES : %d ; tenus : %d ; echecs : %d" % (len(res), len(res) - len(echecs), len(echecs)))
# ---------------------------------------------------------------- contre-epreuve
ALT = [("un plateau de la table", "7.35185e-10", "7.35186e-10"), ("un ln q de la table", "-0.00024  TIENT\n    MPa3", "-0.00034  TIENT\n    MPa3"), ("un jugement", "+0.00000  TIENT", "+0.00000  TOMBE"),
       ("une etendue", "0.0021  0.0034   0.0055  +0.00000", "0.0021  0.0035   0.0055  +0.00000"), ("une bande", "0.0021  0.0034   0.0055  +0.00000", "0.0021  0.0034   0.0056  +0.00000"),
       ("un couplage", "3.91071e-05  7.35185e-10", "3.91072e-05  7.35185e-10"), ("une ligne de la table retiree", "    PGb7     2.00048  1.0000", "    PGb8     2.00048  1.0000"),
       ("le compte des tenues", "Tenues 56, tombees 0", "Tenues 55, tombees 1"), ("la portee", "Portee : 0.0363 0.0530", "Portee : 0.0530"), ("le plus grand ecart", "vaut 0.00025 au plus", "vaut 0.00015 au plus"),
       ("la cellule du plus grand ecart", "au plus\n  (PPb2)", "au plus\n  (PPa2)"), ("sous l'etendue", "a 56 cellules sur 56 : le", "a 46 cellules sur 56 : le"), ("la plus petite marge", "garde 0.0044", "garde 0.0054"),
       ("les lectures suivies", "2679 lectures suivies", "2688 lectures suivies"), ("une lecture non suivie", "MGa7 C k = -3 ; ", ""), ("le temoin", "4.8e-26", "4.8e-06"), ("le poids", "0.7181", "0.9181"),
       ("un temoin positif", "1.36078e-05  1.36078e-05", "1.36079e-05  1.36078e-05"), ("l'heure de la garde", "00:36:05", "00:46:05"), ("la duree", "2944 s", "2844 s"), ("le nombre d'appels", "136 appels", "130 appels"),
       ("les processus", "12 processus", "16 processus"), ("le mot de l'operateur", "\"RUn\"", "\"RUN, vas-y\""), ("le mot du pre-vol", "(\"GO\")", "(\"OK\")"), ("la graine", "(114565)", "(114566)"),
       ("le canon du verdict", "(canon 2c39171a593d95df)", "(canon 2c39171a593d95de)"), ("le canon du rejeu", "(canon ab4629fe72da3e92)", "(canon ab4629fe72da3e93)"), ("le canon d'un lot", "735b9394013b02db lot", "735b9394013b02dc lot"),
       ("le canon de la table", "    4238e2b262119f83 table", "    4238e2b262119f84 table"), ("l'ecart du rejeu", "3.7e-15", "3.7e-11"), ("le residu par kappa", "-0.00025  -0.00020  -0.00024", "-0.00025  -0.00020  +0.00024"),
       ("un Phi lu", "1.79582e-04", "1.79592e-04"), ("la superposition", "desaccord varie de 0.00032 au", "desaccord varie de 0.00002 au"), ("une paire miroir", "0.0800 +0.00008 (+0.00014)", "0.0800 +0.00014 (+0.00014)"),
       ("les ordres", "a 35 cellules sur 56", "a 53 cellules sur 56"), ("A-7 retournee", "au moins sur seize : NON. Il l'est a 10", "au moins sur seize : oui. Il l'est a 12"), ("le bilan des annonces", "Huit annonces sur neuf", "Neuf annonces sur neuf"),
       ("le delta 102", "jusqu'a 0.1262 a seize", "jusqu'a 0.0126 a seize"), ("une reserve retiree : huit tirages", "Cinquante-six\n  cellules sont HUIT tirages", "Cinquante-six\n  cellules sont lues"),
       ("une reserve retiree : la chaine exacte", "Il N'ecrit PAS : que la chaine est exacte", "Il ecrit : que la chaine est exacte"), ("une reserve retiree : le moteur commun", "une erreur commune au lecteur et a la chaine ne se", "rien de tel ne se"),
       ("un numero de delta pris", "DELTA nn -- LARGEUR", "DELTA 105 -- LARGEUR"), ("le fait de deroulement efface", "le tour n'a pas ete attendu", "le tour a ete joue"), ("le rapport a la resonance", "elle vaut 0.5333", "elle vaut 0.5433"),
       ("une ligne trop longue", "nn.11 SUITE", "nn.11 SUITE" + " " * 95), ("un defaut efface", "D-REL-30 : ", ""), ("une reserve retiree : sept valeurs de Phi", "et non cinquante-six largeurs", "soit cinquante-six largeurs")]
print("CONTRE-EPREUVE : %d alterations de l'acte, en memoire" % len(ALT)); manquees = 0
for nom, a, b in ALT:
    n = texte.count(a)
    if n != 1: print("  ANCRE %-45s : %d occurrences (attendu 1)" % (nom, n)); manquees += 1; continue
    try: e = [r[0] for r in controles(texte.replace(a, b)) if not r[1]]
    except Exception as x: e = ["exception %s" % type(x).__name__]
    print("  %-7s %-45s -> %s" % ("vue" if e else "MANQUEE", nom, ", ".join(x.split()[0] for x in e)[:60])); manquees += not e
print("CONTRE-EPREUVE : %d alterations ; vues : %d ; manquees ou sans ancre : %d" % (len(ALT), len(ALT) - manquees, manquees))
print("VERDICT DU CONTROLE : %s" % ("TIENT" if not echecs and not manquees else "NE TIENT PAS")); sys.exit(0 if not echecs and not manquees else 1)
