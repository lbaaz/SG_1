# -*- coding: ascii -*-
"""CONTROLE DE LA NOTE D'ENVOI (Q2 notee, apres-coup, premiere partie du gel) CONTRE LES JOURNAUX -- machine 1, v1,
2026-11-22. Aucun calcul de physique. Trois familles :
  F1  les deux tables (section 1 contre le journal de notation de Q2 ; section 2 contre le journal des ordres) ;
  F2  les nombres de la prose, contre les journaux et la table d'eligibilite ;
  F3  les empreintes, les numeros de lot, la liste des pieces.
Puis la CONTRE-EPREUVE : la note est alteree, une alteration a la fois ; chacune doit faire echouer un controle.
Usage : python3 -I -B controle_note_Q2_gel_machine1_v1.py <note.md> <dossier du lot> <manifeste de machine 2>"""
import sys, os, re, json, math, hashlib, unicodedata
NOTE, LOT, MANIF2 = sys.argv[1:4]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
ch = lambda nom: os.path.join(LOT, nom)
JQ2 = open(ch("note_Q2_machine1_v1.log")).read(); JO = open(ch("ordres_aux_points_lus_machine1_v1.log")).read()
D = json.load(open(ch("eligibilite_sommet_v1.json"))); GEL = ch("gel_sommet_partie1_regle_tirage_pre_enregistrement_v1.md")
cells = [(c["w2"], x) for s in ("MP", "PP", "MG", "PG") for c in D["creneaux"][s]["candidats"] for x in c["cellules"]]
COMPTE = [0]
def controler(texte):
    ech = []; lignes = [l.split() for l in texte.split("\n")]; plat = " ".join(texte.split())
    def exige(cond, quoi):
        COMPTE[0] += 1
        if not cond: ech.append(quoi)
    def dans(fragment): exige(" ".join(fragment.split()) in plat, "absent : " + " ".join(fragment.split())[:80])
    exige(all(len(l) <= 104 for l in texte.split("\n")), "ligne de plus de 104 colonnes"); exige(all(ord(c) < 128 for c in texte), "non ASCII"); exige(chr(37) not in texte, "signe pour cent")
    # F1, section 1
    blocs = re.split(r"^=== ", JQ2, flags=re.M)[1:]
    for b in blocs[:4]:
        pid = b.split()[0]; nom = "Q2-" + pid[-1]
        statut = re.search(r"statut (\S+)", b).group(1); mA = re.search(r"A : PLATEAU\s+k0 = (\S+)\s+etalement \S+\s+Gamma_pl = (\S+)\s+ln\(Gamma_pl / G3\*\) = (\S+)", b)
        poids = re.search(r"fenetre de A >= (\S+)", b).group(1)
        exige([nom, statut, mA.group(1), mA.group(2), mA.group(3), poids] in lignes, "F1 : ligne de %s (section 1)" % nom)
    exige(len(blocs) >= 4 and "BILAN : Q2-1 TENU ; Q2-2 TENU ; Q2-3 TENU ; Q2-4 TENU ; tort NON REALISE" in JQ2, "F1 : le journal ne rend pas ce bilan")
    # F1, section 2
    t1 = {}; t2 = {}
    for l in JO.split("\n"):
        c = l.split()
        if len(c) == 12 and re.match(r"Q2?[a-f]$", c[0]): t1[c[0]] = c
        if len(c) == 11 and re.match(r"Q2?[a-f]$", c[0]): t2[c[0]] = c
    exige(sorted(t1) == sorted(t2) == ["Q2a", "Q2b", "Q2c", "Q2d", "Qe", "Qf"], "F1 : le journal des ordres ne porte pas les six points")
    for pid in t1:
        nom = ("Q2-" if pid.startswith("Q2") else "Q-") + pid[-1]; a = t1[pid]; b = t2[pid]
        exige([nom, a[2], a[7], a[9], a[11], b[1], b[2], "a", b[4]] in lignes, "F1 : ligne de %s (section 2)" % nom)
    # F2
    ec = [abs(float(re.search(r"ln\(Gamma_pl / G3\*\) = (\S+)", b).group(1))) for b in blocs[:4]]
    dans("Q2-2 TENU, plus grand ecart %.5f pour 0.002" % max(ec)); dans("jumeau a %s du plateau au plus" % re.search(r"rapportee au plateau : (\S+)\)", JQ2).group(1))
    m = re.search(r"Q2-4 .*? = (\S+) dans \[\+0.0007, \+0.0017\] : oui ; .*? = (\S+) dans \[\+0.0016, \+0.0026\] : oui -> TENU", JQ2)
    exige(m is not None, "F2 : Q2-4 n'est pas TENU dans le journal")
    if m: dans("Q2-4 TENU : %s dans [+0.0007, +0.0017] et %s dans [+0.0016, +0.0026]" % (m.group(1), m.group(2)))
    dans("(point, absorbeur B, C, D) : %s." % re.search(r"absorbeur B, C, D\) : (\S+)", JQ2).group(1)); dans("Lectures suivies : %s sur %s." % re.search(r"lectures suivies : (\d+) sur (\d+)", JQ2).groups())
    dans("barreaux k = -3 a 4, aux quatre points"); exige("communs aux quatre points : [-3, -2, -1, 0, 1, 2, 3, 4]" in JQ2, "F2 : les barreaux plats du journal")
    dans("est deja a %.5f et %.5f sous le tien" % (-float(t1["Q2a"][11]), -float(t1["Q2b"][11]))); dans("le lecteur est a %.5f et %.5f au-dessus de lui" % (float(t1["Q2a"][7]), float(t1["Q2b"][7])))
    dans("n'y ajoutent que %.5f et %.5f en moyenne" % (-float(t2["Q2a"][1]), -float(t2["Q2b"][1])))
    e3 = sorted(float(t2[p][9]) for p in t2); dans("(%.4f a %.4f a ces points)" % (e3[0], e3[-1]))
    tous = [x for (w, x) in cells]; n = len(tous); nw = len(set(w for (w, x) in cells))
    dans("%d w2 candidats, %d cellules, toutes eligibles" % (nw, n)); dans("%d cellules eligibles sur %d ; etendue de %.4f au plus" % (sum(x["eligible"] for x in tous), n, max(x["etendue"] for x in tous)))
    dans("l'ordre 3 a %.5f au plus du premier ordre" % max(abs(x["ln_G3"] - x["ln_G1"]) for x in tous))
    et = max(max(x["ln_Phi"] for x in tous if x["kappa"] == k) - min(x["ln_Phi"] for x in tous if x["kappa"] == k) for k in set(x["kappa"] for x in tous)); dans("stable a %.4f pres" % et)
    from fractions import Fraction as F
    phi = {(F(w), x["kappa"]): x["ln_Phi"] for (w, x) in cells}; sg = sorted(phi[(w, k)] - phi[(4 - w, k)] for (w, k) in phi if w < 2); dans("entre %+.5f et %+.5f" % (sg[0], sg[-1]))
    G = sorted(math.exp(x["ln_G3"]) for x in tous); dans("a %d cellules la largeur predite depasse ton plus grand plateau qualifie (Q-d), jusqu'a %.2f fois" % (sum(v > 1.08861e-04 for v in G), G[-1] / 1.08861e-04))
    dans("15, 15, 25 et 25 par creneau, 80 en tout, au lieu de 18"); exige([len(D["creneaux"][s]["candidats"]) for s in ("MP", "PP", "MG", "PG")] == [15, 15, 25, 25], "F2 : tailles des creneaux")
    dans("apres avoir vu 112 des 560 cellules"); dans("112 cellules sur 560 etaient deja calculees"); exige(all(x["m_bord"] == x["cible"] for x in tous), "F2 : m_bord = la cible partout")
    # F3
    dans("gel_sommet_partie1_regle_tirage_pre_enregistrement_v1.md (%s)" % canon_B(GEL)); lot2 = canon_B(MANIF2); dans("Lot %s authentifie : 30 pieces sur 30" % lot2)
    exige(lot2 == "295b2b1549b076c2", "F3 : le canon du manifeste de machine 2"); dans("(83701094e6a2b965)"); dans("423ec0fd24240977 et 074b131287ad2b6f"); dans("en tete 055be58")
    for nom in re.findall(r"^    (\S+\.(?:py|log))\b", texte, re.M):
        exige(os.path.isfile(ch(nom)) or nom in ("controle_note_Q2_gel_machine1_v1.log", "fabrique_envoi_22i_machine1_v1.py"), "F3 : piece citee absente du lot : %s" % nom)
    gel = open(GEL).read(); exige(len(re.findall(r"^    [0-9a-f]{16}  \S+", gel, re.M)) + 1 == 19, "F3 : la section 14 de la piece ne porte pas dix-neuf pieces")
    exige("k = 50 (w2 = 3999/2000 et 4001/2000" in " ".join(gel.split()), "F3 : la piece ne retire pas k = 50")
    return ech
texte = open(NOTE, encoding="ascii").read(); ech = controler(texte)
print("note : %s (canon B %s)" % (os.path.basename(NOTE), canon_B(NOTE)))
print("CONTROLE : %d controles, %d echec(s)" % (COMPTE[0], len(ech)))
for e in ech: print("   ECHEC : %s" % e)
ALT = [("un plateau de Q2", "4.94717e-08    +0.00019", "4.94718e-08    +0.00019"), ("un ecart de Q2", "2.05518e-09    +0.00034", "2.05518e-09    +0.00035"), ("un poids", "0.9209", "0.9219"),
       ("un k0", "Q2-b   QUALIFIE  -2", "Q2-b   QUALIFIE  -1"), ("le temoin", "8.46e-36", "8.46e-35"), ("le signe", "+0.00212 dans", "+0.00213 dans"), ("une ligne des ordres", "+0.00030    +0.00033    -0.00033", "+0.00030    +0.00033    -0.00034"),
       ("une moyenne par variante", "-0.00008  -0.00030 a -0.00004", "-0.00009  -0.00030 a -0.00004"), ("la prose des ordres", "0.00020 et 0.00033", "0.00020 et 0.00034"), ("l'etendue", "etendue de 0.0037", "etendue de 0.0038"),
       ("le compte des cellules", "560 cellules eligibles sur 560", "574 cellules eligibles sur 574"), ("l'empreinte de la piece", canon_B(GEL), canon_B(GEL)[:-1] + ("0" if canon_B(GEL)[-1] != "0" else "1")),
       ("le lot de machine 2", "Lot 295b2b1549b076c2", "Lot 295b2b1549b076c3"), ("le depassement", "jusqu'a 2.33 fois", "jusqu'a 2.38 fois"), ("les lectures suivies", "384 sur 384", "383 sur 384"),
       ("le compte de l'esquisse", "apres avoir vu 112", "apres avoir vu 126")]
vues = 0
for (quoi, a, b) in ALT:
    assert texte.count(a) >= 1, "alteration sans prise : %s" % quoi
    e2 = controler(texte.replace(a, b, 1)); vues += bool(e2)
    print("   alteration : %-28s -> %s" % (quoi, ("vue (%d echec(s))" % len(e2)) if e2 else "NON VUE"))
print("CONTRE-EPREUVE : %d alterations vues sur %d" % (vues, len(ALT)))
ok = (not ech) and vues == len(ALT)
print("VERDICT DU CONTROLE : %s" % ("TIENT" if ok else "NE TIENT PAS")); sys.exit(0 if ok else 1)
