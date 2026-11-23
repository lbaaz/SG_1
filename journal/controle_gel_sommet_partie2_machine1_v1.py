# -*- coding: ascii -*-
"""CONTROLE DE LA SECONDE PARTIE DU GEL "SOMMET" CONTRE LES PIECES DU LOT -- machine 1, v1, 2026-11-22. Aucun calcul de
chaine ni de 2D. Le texte de la piece est relu comme un texte, par un code qui n'est pas celui de la construction.
  F1  les tables : les 56 lignes de cellules et les 9 lignes de temoins, contre la table gelee ; la table gelee contre le
      journal du tirage, la table commune et la table complete de machine 1 ;
  F2  la regle : tolerances et seuils du texte, de la table, de la feuille et du pilote (lus dans leur source) ; les
      comptes des bancs contre leurs journaux ; les fichiers de travail contre la table ;
  F3  les empreintes (sections 2, 4.1 et 16) et les nombres de la prose.
Puis la CONTRE-EPREUVE : le texte est altere, une alteration a la fois ; chacune doit faire echouer un controle.
Usage : python3 -I -B controle_gel_sommet_partie2_machine1_v1.py <piece.md> <dossier du lot> <clone du registre> <lot 22i de machine 1>
        <table commune.json> <pilote de lecture de machine 2.py>"""
import sys, os, re, json, math, hashlib, unicodedata
from fractions import Fraction as F
PIECE, LOT, REG, L22I, COMMUNE, PILOTE_M2 = sys.argv[1:7]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
ch = lambda nom: os.path.join(LOT, nom)
T = json.load(open(ch("table_cellules_gel_sommet_v1.json"))); C = T["cellules"]; TP = T["temoins_positifs"]; R = T["regle"]
FEU = open(ch("feuille_gel_sommet_machine1_v1.py")).read(); PIL = open(ch("pilote_gel_sommet_machine1_v1.py")).read()
COMPTE = [0]
def controler(texte):
    ech = []; lignes = [l.split() for l in texte.split("\n")]; plat = " ".join(texte.split())
    def exige(cond, quoi):
        COMPTE[0] += 1
        if not cond: ech.append(quoi)
    def dans(fragment): exige(" ".join(fragment.split()) in plat, "absent : " + " ".join(fragment.split())[:90])
    exige(all(len(l) <= 100 for l in texte.split("\n")), "ligne de plus de 100 colonnes"); exige(all(ord(c) < 128 for c in texte), "non ASCII"); exige(chr(37) not in texte, "signe pour cent")
    # ---------- F1
    for c in C:
        exige([c["id"], c["w2"], "%+.5f" % (float(F(c["w2"])) - 2.0), c["kappa"], str(c["m"]), c["g"], c["eta0"], str(c["r_c"]), "%.3e" % math.exp(c["ln_G3"]), "%.4f" % c["etendue"]] in lignes,
              "F1 : ligne de la cellule %s" % c["id"])
    exige(sum(1 for l in lignes if len(l) == 10 and re.match(r"(MP|PP|MG|PG)[ab][1-7]$", l[0])) == 56, "F1 : le texte ne porte pas 56 lignes de cellules")
    for t in TP:
        exige([t["id"], t["w2"], str(t["m"]), t["g"], t["eta0"], str(t["r_c"]), "%.5e" % math.exp(t["ln_Gamma_pl_reference"])] in lignes, "F1 : ligne du temoin %s" % t["id"])
    tir = [tuple(m.groups()) for m in re.finditer(r"^\s+(\S+)\s+w2 = (\S+)\s+kappa = (\S+)\s+g = (\S+)\s+eta0 = (\S+)\s+r_c = (\d+)", open(ch("tirage_sommet_graine_114565_machine1_v1.log")).read(), re.M)]
    exige(tir == [(c["id"], c["w2"], c["kappa"], c["g"], c["eta0"], str(c["r_c"])) for c in C], "F1 : la table gelee n'est pas le journal du tirage")
    com = {(F(c["w2"]), x["kappa"]): x for s in ("MP", "PP", "MG", "PG") for c in json.load(open(COMMUNE))["creneaux"][s]["candidats"] for x in c["cellules"]}
    full = {(F(c["w2"]), x["kappa"]): x for s in ("MP", "PP", "MG", "PG") for c in json.load(open(os.path.join(L22I, "eligibilite_sommet_v1.json")))["creneaux"][s]["candidats"] for x in c["cellules"]}
    mal = 0
    for c in C:
        a = com[(F(c["w2"]), c["kappa"])]; b = full[(F(c["w2"]), c["kappa"])]
        mal += not ((a["g"], a["eta0"], a["r_c"], a["eligible"]) == (c["g"], c["eta0"], c["r_c"], True) and (b["ln_G3"], b["etendue"], b["ln_G2"], b["ln_G1"], b["m_bord"]) == (c["ln_G3"], c["etendue"], c["ln_G2"], c["ln_G1"], c["m"])
                    and abs(c["delta"] - (float(F(c["w2"])) - 2.0)) < 1e-15 and c["tolerance"] == 0.01)
    exige(mal == 0, "F1 : %d cellules de la table gelee ne sont pas celles de la table commune et de la table complete" % mal)
    exige(canon_B(COMMUNE) == "77ce2a6c7e867011" and canon_B(os.path.join(L22I, "eligibilite_sommet_v1.json")) == "882f55d07d03dfff" and T["graine"] == "114565", "F1 : canons des tables, ou graine")
    # ---------- F2
    cst = lambda src, nom: re.search(r"^%s\s*=\s*(.+)$" % re.escape(nom), src, re.M).group(1).strip()
    exige(cst(FEU, "TOLERANCE, TEMOIN_MAX, TOL_TEMOIN_POSITIF") == "0.01, 1e-6, 1e-3" and cst(FEU, "S1_JUGEES_MIN, S1_TENUES_PAR_W2_MIN, PORTEE_TENUES_PAR_KAPPA_MIN") == "42, 4, 4", "F2 : constantes de la feuille")
    exige((R["tolerance"], R["temoin_max"], R["tolerance_temoin_positif"], R["s1_jugees_min"], R["s1_tenues_par_w2_min"], R["portee_tenues_par_kappa_min"]) == (0.01, 1e-6, 1e-3, 42, 4, 4), "F2 : regle de la table")
    exige('CANON_TABLE = "83701094e6a2b965", "%s"' % canon_B(ch("table_cellules_gel_sommet_v1.json")) in FEU and '"table": "%s"' % canon_B(ch("table_cellules_gel_sommet_v1.json")) in PIL, "F2 : canon de la table en dur")
    exige('"feuille_sommet": "%s"' % canon_B(ch("feuille_gel_sommet_machine1_v1.py")) in PIL and '"pilote_machine2": "%s"' % canon_B(PILOTE_M2) in PIL and R["pilote_machine2_canon"] == canon_B(PILOTE_M2), "F2 : canons de la feuille et du pilote de lecture")
    dans("S1, cinquante-six cellules, huit w2, T = 0.01. TOMBE si deux cellules ou plus tombent ; sinon NON CONCLUANT si moins de 42 cellules sont jugees")
    dans("ou si un w2 a moins de 4 cellules tenues sur sept"); dans("les kappa ou 4 cellules au moins sur huit tiennent"); dans("vaut au plus 1e-6 Gamma_pl")
    dans("|ln(Gamma_pl / plateau de reference)| <= 0.001"); dans("TIENT si |ln q| <= T - b ; elle TOMBE si |ln q| > T + b ; elle est NON JUGEABLE sinon")
    dans("plus grande valeur <= 1.05 fois la plus petite"); dans("a 0.05 pres du plateau sous A")
    mf = re.search(r"BANC DE LA FEUILLE : (\d+) cas, (\d+) tenus", open(ch("banc_feuille_gel_sommet_machine1_v1.log")).read()); mp = re.search(r"BANC DU PILOTE : (\d+) cas, (\d+) tenus", open(ch("banc_pilote_gel_sommet_machine1_v1.log")).read())
    exige(bool(mf and mp) and mf.group(1) == mf.group(2) and mp.group(1) == mp.group(2), "F2 : un banc ne tient pas")
    if mf and mp: dans("ecrit avant : %s cas, %s tenus au premier passage" % mf.groups()); dans("%s cas, %s tenus : le run entier" % mp.groups())
    gl = open(ch("garde_sur_les_sorties_de_Q_et_Q2_machine1_v1.log")).read(); exige("TEMOINS POSITIFS : TIENNENT (9 sur 9)" in gl and "L'INSTRUMENT NE TIENT PAS" in gl, "F2 : journal de la garde sur Q et Q2")
    jobs = [l.split() for l in open(ch("jobs_gel_sommet_v1.txt")) if l.strip()]; att = [[c["id"], c["w2"], c["g"], str(c["m"]), c["eta0"], s, str(c["r_c"]), "ABCD"] for c in C for s in ("1", "-1")]
    jobt = [l.split() for l in open(ch("jobs_temoins_sommet_v1.txt")) if l.strip()]; attt = [[c["id"], c["w2"], c["g"], str(c["m"]), c["eta0"], s, str(c["r_c"]), "ABCD"] for c in TP for s in ("1", "-1")]
    exige(jobs == att and jobt == attt, "F2 : les fichiers de travail ne sont pas la table")
    # ---------- F3 : empreintes
    n_emp = 0
    for m in re.finditer(r"^    ([0-9a-f]{16}) +(\S+)", texte, re.M):
        canon, nom = m.group(1), m.group(2); n_emp += 1
        if nom == "la": continue                                                       # "la table commune", controlee plus haut
        cands = [ch(nom), os.path.join(REG, nom), os.path.join(L22I, nom)] + ([PILOTE_M2] if nom == os.path.basename(PILOTE_M2) else [])
        chemin = next((p for p in cands if os.path.isfile(p)), None)
        exige(chemin is not None and canon_B(chemin) == canon, "F3 : empreinte de %s" % nom)
    exige(n_emp == 16 + 6 + 13, "F3 : %d empreintes listees au lieu de 35" % n_emp)
    dans("table_cellules_gel_sommet_v1.json, canon %s" % canon_B(ch("table_cellules_gel_sommet_v1.json"))); dans("predictions_sommet_machine1_v1.py (%s)" % canon_B(ch("predictions_sommet_machine1_v1.py")))
    dans("(1e5039cade55d13f, lot 3ba4618d7976c6ea)"); dans("(lot 21e9bddfe5db83b2)"); dans("(816ac4d298e82f16)"); dans("(5b835ce079ce2cf4)")
    exige(canon_B(os.path.join(L22I, "gel_sommet_partie1_regle_tirage_pre_enregistrement_v1.md")) == "1e5039cade55d13f" and R["bloc_sha256_16"] == "5b835ce079ce2cf4", "F3 : canon de la premiere partie ou du bloc")
    # ---------- F3 : prose
    G = sorted(math.exp(c["ln_G3"]) for c in C); et = sorted(c["etendue"] for c in C); gg = sorted((c["g"] for c in C), key=float)
    dans("du premier ordre de %.5f au plus en logarithme, et de l'ordre 2 de %.5f au plus" % (max(abs(c["ln_G3"] - c["ln_G1"]) for c in C), max(abs(c["ln_G3"] - c["ln_G2"]) for c in C)))
    dans("Couplages de %s a %s ; plateaux predits de %.3e a %.3e ; etendue de %.4f a %.4f." % (gg[0], gg[-1], G[0], G[-1], et[0], et[-1]))
    w2s = []
    for c in C:
        if c["w2"] not in w2s: w2s.append(c["w2"])
    dans("huit w2 (%s) et sept kappa (0.0363, 0.0530, 0.0800, 0.1300, 0.2000, 0.4000, 1.0000)" % ", ".join("%.5f" % float(F(w)) for w in w2s))
    dans("etendue de %.4f au plus aux 56 cellules" % et[-1]); dans("la bande est de %.4f au plus et une cellule tient jusqu'a |ln q| = %.4f : %d fois le pire ecart lu" % (et[-1] + 0.0018, 0.01 - et[-1] - 0.0018, int((0.01 - et[-1] - 0.0018) / 0.00034)))
    dans("La tolerance vaut %d fois le plus grand" % int(0.01 / 0.00034))
    haut = [c["id"] for c in C if math.exp(c["ln_G3"]) > 1.08861e-04]; bas = [c["id"] for c in C if math.exp(c["ln_G3"]) < 2.05518e-09]
    dans("Quatre cellules (%s) ont un plateau predit au-dessus" % ", ".join(haut)); dans("jusqu'a %.2f fois, a des couplages de plus de 2e-03 ; quatre (%s) sont sous" % (G[-1] / 1.08861e-04, ", ".join(bas)))
    dans("jusqu'a %.3f fois. Aucune borne" % (G[0] / 2.05518e-09)); exige(len(haut) == 4 and len(bas) == 4 and all(float(c["g"]) > 2e-3 for c in C if c["id"] in haut), "F3 : cellules hors de ce que le lecteur a qualifie")
    phi = {(F(c["w2"]), c["kappa"]): c["ln_Phi"] for c in C}; mir = [phi[(w, k)] - phi[(4 - w, k)] for (w, k) in sorted(phi, key=lambda z: float(z[1])) if w < 2 and (4 - w, k) in phi]
    dans("de kappa = 0.0363 a 1 : %s." % " ; ".join("%+.5f" % v for v in mir)); exige(len(mir) == 7, "F3 : sept paires miroirs")
    ek = [max(c["ln_Phi"] for c in C if c["kappa"] == k) - min(c["ln_Phi"] for c in C if c["kappa"] == k) for k in sorted(set(c["kappa"] for c in C), key=float)]
    dans("la chaine donne de %.5f a %.5f." % (min(ek), max(ek))); dans("ne varie que de %.5f au plus d'un w2 tire a l'autre" % max(ek))
    dm = sorted(abs(float(F(w)) - 2.0) for w in w2s); dans("pour |delta| de %.5f a %.5f et kappa de 0.0363 a 1" % (dm[0], dm[-1]))
    dans("\"graine 114565\" (22/11/2026, 23 h 21)"); dans("A-5 S1 : TENU 0.80 ; TENU SAUF UNE CELLULE 0.02 ; TOMBE 0.02 ; NON CONCLUANT 0.08 ; le reste (0.08)")
    dans("une paire de w2 MIROIRS, 1.99989 et 2.00011"); dans("130 lectures dans des boites de %d au plus" % max(c["boite"] for c in C + TP))
    return ech
texte = open(PIECE, encoding="ascii").read(); ech = controler(texte)
print("piece : %s (canon B %s)" % (os.path.basename(PIECE), canon_B(PIECE)))
print("CONTROLE : %d controles, %d echec(s)" % (COMPTE[0], len(ech)))
for e in ech: print("   ECHEC : %s" % e)
ALT = [("un couplage d'une cellule", "3.91071e-05  1.52405e-04", "3.91072e-05  1.52405e-04"), ("un eta0 d'une cellule", "4.71149e-03  1.83206e-02", "4.71149e-03  1.83207e-02"),
       ("un plateau predit", "22   7.352e-10", "22   7.353e-10"), ("une etendue", "2.483e-04  0.0030", "2.483e-04  0.0031"), ("le w2 d'une cellule", "MGa1     6249/3125", "MGa1     6249/3126"),
       ("une profondeur", "0.0530  1  5.70985e-05", "0.0530  2  5.70985e-05"), ("un plateau de reference", "22   2.05518e-09", "22   2.05519e-09"), ("le eta0 d'un temoin", "6e-5     2.33642e-04", "6e-5     2.33643e-04"),
       ("le seuil des cellules jugees", "si moins de 42 cellules", "si moins de 40 cellules"), ("le seuil par w2", "un w2 a moins de 4", "un w2 a moins de 3"),
       ("la tolerance des temoins positifs", "  0.001. Les temoins positifs TIENNENT", "  0.002. Les temoins positifs TIENNENT"), ("la regle de jugement", "TIENT si |ln q| <= T - b", "TIENT si |ln q| <= T + b"),
       ("le canon de la table", "canon 4238e2b262119f83", "canon 4238e2b262119f84"), ("le canon du pilote de lecture", "    47a84eae6052f006 lecteur_2D_pilote_machine2_v1.py (lots", "    47a84eae6052f007 lecteur_2D_pilote_machine2_v1.py (lots"),
       ("un canon du registre", "    10887c60d5f55bcf ", "    10887c60d5f55bce "), ("un canon du lot", "  feuille_gel_sommet_machine1_v1.py\n", "  pilote_gel_sommet_machine1_v1.py\n"),
       ("le compte du banc de la feuille", "30 cas, 30 tenus au premier passage", "31 cas, 31 tenus au premier passage"), ("le compte du banc du pilote", "12 cas, 12 tenus", "13 cas, 13 tenus"),
       ("l'ecart des ordres", "ordre de 0.00034 au plus", "ordre de 0.00035 au plus"), ("la bande attendue", "bande est de 0.0053", "bande est de 0.0054"), ("une valeur miroir", "+0.00014 ;", "+0.00015 ;"),
       ("la graine", "\"graine 114565\"", "\"graine 114566\""), ("une annonce", "TENU 0.80 ;", "TENU 0.85 ;"), ("les cellules hors plage", "(MGa7, MGb7, PGa7, PGb7)", "(MGa6, MGb7, PGa7, PGb7)"),
       ("la plage des desaccords", "de 0.00007 a 0.00048", "de 0.00005 a 0.00049")]
vues = 0
for (quoi, a, b) in ALT:
    assert texte.count(a) >= 1, "alteration sans prise : %s" % quoi
    e2 = controler(texte.replace(a, b, 1)); vues += bool(e2)
    print("   alteration : %-36s -> %s" % (quoi, ("vue (%d echec(s))" % len(e2)) if e2 else "NON VUE"))
print("CONTRE-EPREUVE : %d alterations vues sur %d" % (vues, len(ALT)))
ok = (not ech) and vues == len(ALT)
print("VERDICT DU CONTROLE : %s" % ("TIENT" if ok else "NE TIENT PAS")); sys.exit(0 if ok else 1)
