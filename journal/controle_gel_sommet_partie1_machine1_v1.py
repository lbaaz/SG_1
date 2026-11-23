# -*- coding: ascii -*-
"""CONTROLE DE LA PREMIERE PARTIE DU GEL "SOMMET" CONTRE LES SORTIES DU LOT -- machine 1, v1, 2026-11-22.
Aucun calcul de chaine. Le texte de la piece est relu comme un texte, et chaque nombre qu'il porte est compare a ce que
les sorties du lot donnent, par un code qui n'est pas celui de la construction. Trois familles :
  F1  les tables : les 80 lignes de la section 7, les trois tables par kappa, la table des neuf points ;
  F2  la regle : listes, kappa, seuils, exemples de hachage refaits, et les trois nombres ecrits des 560 cellules
      recalcules (g et eta0 en arithmetique exacte sur X(w2) du moteur, r_c depuis m_bord) ;
  F3  les empreintes (sections 1, 7 et 14) et les nombres de la prose.
Puis la CONTRE-EPREUVE : le texte est altere de plusieurs facons, une a la fois ; chaque alteration doit faire echouer
au moins un controle.
Usage : python3 -I -B controle_gel_sommet_partie1_machine1_v1.py <piece.md> <dossier du lot> <clone du registre> <lot 22g> <lot 22h> <journal note Q>"""
import sys, os, re, json, math, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
PIECE, LOT, REG, L22G, L22H, JQ = sys.argv[1:7]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
MOTEUR = os.path.join(REG, "scripts", "m17_chaine_v17.py"); assert canon_B(MOTEUR) == "82a0be882568fe0c"
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
D = json.load(open(os.path.join(LOT, "eligibilite_sommet_v1.json"))); C = json.load(open(os.path.join(LOT, "eligibilite_candidates_sommet_v1.json")))
BR = json.load(open(os.path.join(LOT, "balayage_virginite_sommet_registre_v1.json"))); BP = json.load(open(os.path.join(LOT, "balayage_virginite_sommet_poste_v1.json")))
NOMS = ("MP", "PP", "MG", "PG"); KAP = ("0.0363", "0.0530", "0.0800", "0.1300", "0.2000", "0.4000", "1.0000"); CIB = (2, 1, 0, 0, 0, 0, 0)
cells = [(s, c["w2"], x) for s in NOMS for c in D["creneaux"][s]["candidats"] for x in c["cellules"]]
X_de = {}
def X(w2):
    if w2 not in X_de: X_de[w2] = M.X_saut_reel(M.P, 2, 1, 0.0, 0.0, w2)
    return X_de[w2]

COMPTE = [0]
def controler(texte):
    """Rend la liste des echecs (chaine vide = aucun)."""
    ech = []; lignes = texte.split("\n"); plat = " ".join(texte.split())
    def exige(cond, quoi):
        COMPTE[0] += 1
        if not cond: ech.append(quoi)
    def dans(fragment):
        exige(" ".join(fragment.split()) in plat, "absent de la prose : " + " ".join(fragment.split())[:90])
    # ---------- forme
    exige(all(len(l) <= 100 for l in lignes), "ligne de plus de 100 colonnes"); exige(all(ord(ch) < 128 for ch in texte), "non ASCII"); exige(chr(37) not in texte, "signe pour cent")
    # ---------- F1 : les 80 lignes
    rangs = [l for l in lignes if re.match(r"^    [12]\.\d{5}  ", l)]
    att = []
    for s in NOMS:
        for c in D["creneaux"][s]["candidats"]:
            w = F(c["w2"]); num = w.numerator * (100000 // w.denominator)
            att.append("    %d.%05d  %s  %s" % (num // 100000, num % 100000, " ".join("%.4f" % round(x["etendue"], 10) for x in c["cellules"]), "ELIGIBLE" if c["eligible"] else "INELIGIBLE"))
    exige(len(rangs) == 80, "F1 : %d lignes de w2 au lieu de 80" % len(rangs))
    for a, b in zip(rangs, att):
        exige(a == b, "F1 : ligne de w2 differente : %s" % a.strip()[:40])
    for s in NOMS:
        n = len(D["creneaux"][s]["candidats"]); dans("creneau %s : %d w2 eligibles sur %d" % (s, sum(c["eligible"] for c in D["creneaux"][s]["candidats"]), n))
    # ---------- F1 : les trois tables par kappa
    for i, k in enumerate(KAP):
        Lk = [x for (s, w, x) in cells if x["kappa"] == k]; g = sorted(float(x["g"]) for x in Lk); G = sorted(x["ln_G3"] for x in Lk); ph = sorted(x["ln_Phi"] for x in Lk)
        q = sorted(math.exp(x["ln_G3"]) / float(x["g"]) for x in Lk); ms = sorted(x["m_etoile"] for x in Lk)
        t1 = [k, str(CIB[i]), "/".join(sorted(set(str(x["m_bord"]) for x in Lk))), "/".join(sorted(set(str(x["r_c"]) for x in Lk))), str(max(x["r_c"] for x in Lk) + 100),
              "%.4f" % max(x["etendue"] for x in Lk), "%.3f" % max(x["e_bord"] for x in Lk), "%.4f" % min(x["poids_min"] for x in Lk), str(ms[0]), "a", str(ms[-1])]
        t2 = [k, "%.5e" % g[0], "a", "%.5e" % g[-1], "%.5e" % math.exp(G[0]), "a", "%.5e" % math.exp(G[-1]), "%.4e" % q[0], "a", "%.4e" % q[-1]]
        t3 = [k, "%.5e" % math.exp(ph[0]), "a", "%.5e" % math.exp(ph[-1]), "%.4f" % (ph[-1] - ph[0]), "%.5f" % max(abs(x["ln_G3"] - x["ln_G1"]) for x in Lk), "%.5f" % max(abs(x["ln_G3"] - x["ln_G2"]) for x in Lk)]
        trouve = [l.split() for l in lignes if l.startswith("    " + k + "   ")]
        exige(len(trouve) == 3, "F1 : %d lignes de table pour kappa = %s" % (len(trouve), k))
        for t in (t1, t2, t3):
            exige(t in trouve, "F1 : ligne de table par kappa absente ou differente : %s" % " ".join(t)[:60])
    # ---------- F1 : les neuf points
    def lus(journal):
        r = {}; pid = None
        for l in open(journal):
            m = re.match(r"=== (Q2?)([a-f])\s", l)
            if m: pid = m.group(1) + "-" + m.group(2)
            m = re.search(r"A : PLATEAU .*Gamma_pl = (\S+)\s+ln\(Gamma_pl / G3\*\) = (\S+)", l)
            if m and pid: r[pid] = (m.group(1), m.group(2))
        return r
    R = lus(JQ); R.update(lus(os.path.join(LOT, "note_Q2_machine1_v1.log")))
    PTS = {"Q-a": ("2", "2.5e-04", 0), "Q-c": ("2", "1e-03", 0), "Q-d": ("2", "2e-03", 0), "Q-e": ("20001/10000", "3e-04", 0), "Q-f": ("20001/10000", "1.5e-04", 0),
           "Q2-a": ("20001/10000", "6e-05", 1), "Q2-b": ("20001/10000", "4e-05", 2), "Q2-c": ("19999/10000", "3e-04", 0), "Q2-d": ("19999/10000", "1.5e-04", 0)}
    exige(sorted(R) == sorted(PTS), "F1 : les journaux de notation ne portent pas les neuf points")
    for nom, (w2t, gt, mb) in PTS.items():
        w = F(w2t); kap = "infini" if w == 2 else "%.4f" % (float(gt) * X(w) / (M.P * abs(float(w) - 2.0)))
        att9 = [nom, w2t, gt, kap, str(mb), R[nom][0], R[nom][1]]
        exige(att9 in [l.split() for l in lignes], "F1 : ligne du point %s absente ou differente" % nom)
    # ---------- F2 : la regle
    listes = {"MP": [F(2) - F(k, 100000) for k in range(20, 4, -1) if k != 10], "PP": [F(2) + F(k, 100000) for k in range(5, 21) if k != 10],
              "MG": [F(2) - F(k, 100000) for k in range(49, 24, -1)], "PG": [F(2) + F(k, 100000) for k in range(25, 50)]}
    for s in NOMS:
        exige([F(c["w2"]) for c in D["creneaux"][s]["candidats"]] == listes[s], "F2 : la liste du creneau %s n'est pas celle de la regle" % s)
        exige([c["w2"] for c in C["creneaux"][s]["candidats"]] == [c["w2"] for c in D["creneaux"][s]["candidats"]], "F2 : la table compacte n'a pas les memes w2 (%s)" % s)
    dans("MP delta < 0, petit k = 5 a 20, sauf 10 w2 = 1.99980 a 1.99995 15 valeurs"); dans("PP delta > 0, petit k = 5 a 20, sauf 10 w2 = 2.00005 a 2.00020 15 valeurs")
    dans("MG delta < 0, grand k = 25 a 49 w2 = 1.99951 a 1.99975 25 valeurs"); dans("PG delta > 0, grand k = 25 a 49 w2 = 2.00025 a 2.00049 25 valeurs")
    dans("DEUX BARREAUX 1 : 0.0363 UN BARREAU 2 : 0.0530"); dans("SANS BARRIERE 3 : 0.0800 4 : 0.1300 5 : 0.2000 6 : 0.4000 7 : 1.0000")
    dans("eta0 = max( |w2 - 2| , g x X(w2) / (P x kappa_3) ) , kappa_3 = 0.0262 ;"); dans("r_c = 2 (m_bord + max(8, m_bord)) + 2")
    dans("g = kappa x |w2 - 2| x P / X(w2)"); dans("(ii) e_bord < 0.7 ; (iii) l'etendue est definie et <= 0.005"); dans("M_facteur 5"); dans("Au plus dix rangs, de 0 a 9")
    dans("Dix-huit variantes : a = 1, 2, 4 ; c = 6, 8, 10 ; L = 16, 24"); dans("On s'arrete a DEUX w2 retenus")
    exige(D["regle"]["seuil_etendue"] == 0.005 and D["regle"]["garde_e_bord"] == 0.7 and D["regle"]["M_facteur"] == 5 and D["regle"]["kappa_3"] == "0.0262" and
          [tuple(v) for v in D["regle"]["kappas"]] == list(zip(KAP, CIB)) and len(D["regle"]["variantes"]) == 18, "F2 : la regle ecrite dans la table n'est pas celle du texte")
    for s in NOMS:
        for r in (0, 1):
            h = hashlib.sha256(("DEMONSTRATION|%s|%d" % (s, r)).encode("ascii")).hexdigest(); n = len(listes[s]); i = int(h, 16) % n
            dans("sha256(\"DEMONSTRATION|%s|%d\") = %s... ; modulo %d = %d -> w2 = %.5f" % (s, r, h[:16], n, i, float(sorted(listes[s])[i])))
    faux = 0
    for s in NOMS:
        for c, c2 in zip(D["creneaux"][s]["candidats"], C["creneaux"][s]["candidats"]):
            w = F(c["w2"]); d = abs(w - 2); Xw = F(X(w))
            for i, (x, y) in enumerate(zip(c["cellules"], c2["cellules"])):
                g_ex = F(KAP[i]) * d * 5 / Xw; ok = abs(F(x["g"]) / g_ex - 1) < F(6, 10 ** 6) and ("%.5e" % float(g_ex)) == x["g"]
                e_ex = max(d, F(x["g"]) * Xw / (5 * F("0.0262"))); ok = ok and ("%.5e" % float(e_ex)) == x["eta0"]
                ok = ok and x["r_c"] == 2 * (x["m_bord"] + max(8, x["m_bord"])) + 2 and x["m_bord"] == CIB[i] and x["kappa"] == KAP[i]
                ok = ok and x["eligible"] == (x["m_bord"] == CIB[i] and x["e_bord"] < 0.7 and x["etendue"] is not None and x["etendue"] <= 0.005)
                ok = ok and (y["kappa"], y["g"], y["eta0"], y["r_c"], y["eligible"]) == (x["kappa"], x["g"], x["eta0"], x["r_c"], x["eligible"])
                faux += not ok
            exige(c["eligible"] == all(x["eligible"] for x in c["cellules"]) == c2["eligible"], "F2 : eligibilite du w2 %s" % c["w2"])
    exige(faux == 0, "F2 : %d cellules dont les nombres ecrits ne sont pas ceux de la regle" % faux)
    # ---------- F3 : les empreintes
    for m in re.finditer(r"^    ([0-9a-f]{16}) +(\S+)", texte, re.M):
        canon, nom = m.group(1), m.group(2); cands = [os.path.join(LOT, nom), os.path.join(REG, nom), os.path.join(L22G, nom), os.path.join(L22H, nom)]
        ch = next((p for p in cands if os.path.isfile(p)), None)
        exige(ch is not None and canon_B(ch) == canon, "F3 : empreinte de %s" % nom)
    n_emp = len(re.findall(r"^    [0-9a-f]{16} +\S+", texte, re.M)); exige(n_emp == 10 + 18, "F3 : %d empreintes listees au lieu de 28" % n_emp)
    dans("(eligibilite_candidates_sommet_v1.json, %s)" % canon_B(os.path.join(LOT, "eligibilite_candidates_sommet_v1.json")))
    dans("(lot 423ec0fd24240977)"); dans("(lot 074b131287ad2b6f)"); dans("c58c2b3f533c516b et 295b2b1549b076c2"); dans("(83701094e6a2b965)"); dans("(registre 055be58)")
    # ---------- F3 : la prose
    tous = [x for (s, w, x) in cells]; nesq = sum(1 for v in BP["par_w2"].values() if v)
    dans("La plus grande etendue est %.4f pour un seuil de 0.005" % max(x["etendue"] for x in tous))
    dans("vide a %d cellules" % sum(x["barriere_vide"] for x in tous)); dans("la profondeur cible est %d." % sum(x["m_bord"] != x["cible"] for x in tous))
    dans("dans l'etat lu est %.4f" % min(x["poids_min"] for x in tous)); dans("l'emporte aux %d cellules" % sum(float(x["eta0"]) > abs(float(F(w)) - 2.0) for (s, w, x) in cells))
    r1 = sorted(float(x["eta0"]) / float(x["g"]) for x in tous); r2 = sorted(float(x["eta0"]) / abs(float(F(w)) - 2.0) for (s, w, x) in cells)
    dans("eta0 / g va de %.4f a %.4f, et eta0 / |w2 - 2| de %.3f a %.2f" % (r1[0], r1[-1], r2[0], r2[-1])); dans("N = r_c + 100 = %d" % (max(x["r_c"] for x in tous) + 100))
    dans("du premier ordre de %.5f au plus en logarithme, et de l'ordre 2 de %.5f au plus" % (max(abs(x["ln_G3"] - x["ln_G1"]) for x in tous), max(abs(x["ln_G3"] - x["ln_G2"]) for x in tous)))
    et = max(max(x["ln_Phi"] for x in tous if x["kappa"] == k) - min(x["ln_Phi"] for x in tous if x["kappa"] == k) for k in KAP); dans("Phi varie de %.4f au plus" % et)
    phi = {(F(w), x["kappa"]): x["ln_Phi"] for (s, w, x) in cells}; sg = sorted(phi[(w, k)] - phi[(4 - w, k)] for (w, k) in phi if w < 2)
    dans("(%d paires) : ln[Phi(delta < 0) / Phi(delta > 0)] va de %+.5f a %+.5f" % (len(sg), sg[0], sg[-1]))
    G = sorted(math.exp(x["ln_G3"]) for x in tous); gg = sorted(float(x["g"]) for x in tous)
    dans("a %d cellules la largeur predite depasse" % sum(v > 1.08861e-04 for v in G)); dans("jusqu'a %.2f fois, et les couplages vont jusqu'a %.5e" % (G[-1] / 1.08861e-04, gg[-1]))
    dans("a %d cellules elle est sous le plus petit plateau" % sum(v < 2.05518e-09 for v in G)); dans("jusqu'a %.3f fois" % (G[0] / 2.05518e-09))
    D2 = json.load(open(os.path.join(LOT, "eligibilite_sommet_avec_levier_v1.json")))
    ecart = max(abs(x["ln_G3"] - y["ln_G3"]) for s in NOMS for c, c2 in zip(D["creneaux"][s]["candidats"], D2["creneaux"][s]["candidats"]) for x, y in zip(c["cellules"], c2["cellules"]))
    memes = all((x["g"], x["eta0"], x["r_c"], x["eligible"]) == (y["g"], y["eta0"], y["r_c"], y["eligible"]) for s in NOMS for c, c2 in zip(D["creneaux"][s]["candidats"], D2["creneaux"][s]["candidats"])
                for x, y in zip(c["cellules"], c2["cellules"]))
    exige(memes, "F3 : les deux reglages de numpy ne rendent pas les memes nombres ecrits"); dans("0 eligibilite changee, 0 nombre ecrit change, plus grand ecart sur ln G3 %.1e" % ecart)
    dans("133 cellules dont %d sont des cellules candidates d'ici (%d w2 ; etendue de 0.0036 au plus), et AVANT d'avoir calcule les %d autres" % (7 * nesq, nesq, 560 - 7 * nesq))
    dans("l'eligibilite des 560 cellules candidates (80 w2)"); dans("7. LA TABLE DE MACHINE 1 (560 cellules)"); dans("SA table des 560 cellules")
    dans("son plateau est a %.5f au plus de la colonne G3*" % max(abs(float(v[1])) for v in R.values()))
    dans("(055be58, %d fichiers lus) : aucune trace d'un w2 candidat" % BR["lus"]); exige(not BR["touches"], "F3 : le registre porte un w2 candidat")
    dans("y sont dans %d fichiers" % len(set(os.path.basename(p) for v in BR["retires"].values() for p in v)))
    dans("(%d fichiers lus) : %d w2 candidats, dans un seul journal (%d copies), esquisse_gel_sommet_machine1_v1.log" % (BP["lus"], nesq, len(BP["touches"])))
    exige(BP["noms"] == ["esquisse_gel_sommet_machine1_v1.log"] and not BP["nom_2d"] and not BR["nom_2d"], "F3 : le balayage du poste ne dit pas ce que dit le texte")
    dans("(22/11/2026, 20 h 09)"); dans("+0.00121 et +0.00212 pour +0.00121 et +0.00211"); dans("0.306 (deux points), 0.153 (deux points), 0.0612 et 0.0408")
    return ech

texte = open(PIECE, encoding="ascii").read()
ech = controler(texte)
print("piece : %s (canon B %s)" % (os.path.basename(PIECE), canon_B(PIECE)))
print("CONTROLE : %d controles, %d echec(s)" % (COMPTE[0], len(ech)))
for e in ech: print("   ECHEC : %s" % e)
# ---------- contre-epreuve
ALTERATIONS = [("une etendue de la table des w2", "    1.99980  0.0034", "    1.99980  0.0035"), ("un ELIGIBLE", "0.0029  ELIGIBLE", "0.0029  INELIGIBLE"),
               ("un couplage de la table par kappa", "1.77800e-05 a", "1.77801e-05 a"), ("un plateau predit", "a 2.53553e-04", "a 2.53554e-04"),
               ("un Phi", "5.17263e-01 a", "5.17264e-01 a"), ("un poids du site 0", "0.9985    63 a 159", "0.9986    63 a 159"), ("un plateau lu", "4.94717e-08  +0.00019", "4.94718e-08  +0.00019"),
               ("un ecart d'un point lu", "2.05518e-09  +0.00034", "2.05518e-09  +0.00033"), ("le kappa d'un point lu", "6e-05    0.0612", "6e-05    0.0613"),
               ("un kappa du gel", "2 : 0.0530", "2 : 0.0540"), ("kappa_3", "kappa_3 = 0.0262 ;", "kappa_3 = 0.0263 ;"), ("le seuil d'etendue", "definie et <= 0.005", "definie et <= 0.006"),
               ("un exemple de hachage", "modulo 15 = 2 -> w2 = 1.99982", "modulo 15 = 3 -> w2 = 1.99983"), ("le prefixe d'un hachage", "e2635f39a4c07247", "e2635f39a4c07248"),
               ("une empreinte du registre", "    7cd5977bc27bebc1 ", "    7cd5977bc27bebc2 "), ("une empreinte du lot", "  tirage_sommet_machine1_v1.py", "  tirage_sommet_machine1_v1_autotest.log"),
               ("la plus grande etendue", "etendue est 0.0037", "etendue est 0.0036"), ("le compte des barrieres vides", "vide a 400 cellules", "vide a 410 cellules"),
               ("l'ecart des ordres", "premier ordre de 0.00034", "premier ordre de 0.00035"), ("le signe", "a +0.00051", "a +0.00052"), ("le compte du registre", "3553 fichiers", "3554 fichiers"),
               ("les bornes d'un creneau", "w2 = 2.00025 a 2.00049", "w2 = 2.00025 a 2.00050"), ("le nombre de rangs", "Au plus dix rangs, de 0 a 9", "Au plus cinq rangs, de 0 a 4"),
               ("l'heure de l'operateur", "20 h 09", "20 h 19"), ("le compte de l'esquisse", "dont 112 sont", "dont 126 sont")]
vues = 0
for (quoi, a, b) in ALTERATIONS:
    assert texte.count(a) >= 1, "alteration sans prise : %s" % quoi
    e2 = controler(texte.replace(a, b, 1))
    vues += bool(e2)
    print("   alteration : %-36s -> %s" % (quoi, ("vue (%d echec(s))" % len(e2)) if e2 else "NON VUE"))
print("CONTRE-EPREUVE : %d alterations vues sur %d" % (vues, len(ALTERATIONS)))
ok = (not ech) and vues == len(ALTERATIONS)
print("VERDICT DU CONTROLE : %s" % ("TIENT" if ok else "NE TIENT PAS"))
sys.exit(0 if ok else 1)
