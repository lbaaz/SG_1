# -*- coding: ascii -*-
"""Controle de la note POUR_MACHINE2_pole_court_lu_et_qualification_du_sommet_machine1_v1.md, en trois familles :
(A) forme ; (B) chiffres contre les journaux : chaque nombre decimal de la note doit se retrouver, a son arrondi, dans un
journal ou une piece citee, et les chiffres qui portent la note sont en plus attaches a LEUR ligne de journal ;
(C) citations et empreintes. Puis contre-epreuve : chaque alteration de la note doit faire tomber au moins un controle,
depuis une note sans aucun controle tombe.

usage : python3 -I controle_note_pole_court_lu_machine1_v1.py <la note> <journal de notation> <journal du controle>
            <journal d'apres coup> <journal du sommet> <journal de l'esquisse> <journal des fenetres>
            <manifeste du lot de machine 2> <clone du registre> <mon module de la 21h> <tete du clone>
Tout est lu comme des donnees ; rien n'est execute.
"""
import hashlib, math, os, re, sys, unicodedata

(NOTE, J_NOT, J_CTL, J_APR, J_SOM, J_ESQ, J_FEN, SON_MAN, CLONE, MODULE_21H, TETE) = sys.argv[1:12]
NB = r"(?<![A-Za-z0-9_.])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?(?![A-Za-z0-9_])"
HEX = r"\b[0-9a-f]{16}\b"
# seuils, probabilites et constantes posees par la plume ou citees telles quelles : pas des resultats
SEUILS = {"0.8", "0.75", "0.9", "0.6", "0.010", "0.005", "0.02", "0.05", "1.05", "0.5", "1e-6", "0.0544", "2.0001", "0.0539", "0.0549",
          "0.053", "0.056", "2.5e-04", "1e-03", "2e-03", "3e-04", "1.5e-04", "3e-03", "0.4", "0.08", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5",
          "4.0", "4.5", "5.0", "4.2", "2.3", "1.5e-03", "4.9e-03", "6.2", "6.3", "6.4", "6.1", "8.1", "8.2", "8.3", "8.4"}


def lit(ch):
    return open(ch, "rb").read()


def canon_b(data):
    t = unicodedata.normalize("NFC", data.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


def nombres(texte):
    texte = re.sub(HEX, " ", texte)
    return [x for x in re.findall(NB, texte) if "." in x or "e" in x.lower()]


def chiffres(tok):
    m = tok.lstrip("+-").lower().split("e")[0]
    return len(m.replace(".", "").lstrip("0")) or 1


def arrondi(v, k):
    if v == 0:
        return 0.0
    return round(v, k - 1 - int(math.floor(math.log10(abs(v)))))


GELS = [os.path.join(CLONE, "gels", "gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md"),
        os.path.join(CLONE, "gels", "gel_largeur_vide_partie2_instrument_enonces_pre_enregistrement_v1.md"),
        os.path.join(CLONE, "journal", "journal_delta_102_largeur_vide_v2.md")]
DEPOSES = {"moteur": os.path.join(CLONE, "scripts", "m17_chaine_v17.py"), "bloc2": os.path.join(CLONE, "scripts", "chaine_ordre2_bloc_machine1_v1.py"),
           "bloc3": os.path.join(CLONE, "scripts", "ordre3_bloc_machine1_v1.py"), "bloc_adapte": os.path.join(CLONE, "scripts", "chaine_adaptee_bloc_machine1_v1.py"),
           "sonde_lecteur": os.path.join(CLONE, "scripts", "sonde_lecteur_gel_loi_machine1_v1.py"),
           "feuille_lecteur": os.path.join(CLONE, "scripts", "lecture_lecteur_gel_loi_machine1_v1.py"),
           "sonde_vide": os.path.join(CLONE, "journal", "lot_b1919dc9468dc437__sonde_vide_machine1_v1.py"), "gel1": GELS[0], "gel2": GELS[1]}
J = {n: lit(ch).decode("utf-8") for n, ch in (("notation", J_NOT), ("controle", J_CTL), ("apres coup", J_APR), ("sommet", J_SOM), ("esquisse", J_ESQ), ("fenetres", J_FEN))}
CITES = {n: lit(ch).decode("utf-8") for n, ch in (("gel1", GELS[0]), ("gel2", GELS[1]), ("acte102", GELS[2]))}
VALEURS = set()
for t in list(J.values()) + list(CITES.values()):
    VALEURS.update(float(x) for x in nombres(t))
for t in J.values():                                   # les entiers des journaux aussi (d ln a / g^2, comptes)
    VALEURS.update(float(x) for x in re.findall(r"(?<![\w.])[-+]?\d+(?![\w.])", t))
CANONS = {n: canon_b(lit(ch)) for n, ch in DEPOSES.items()}
CANONS["son_manifeste"] = canon_b(lit(SON_MAN)); CANONS["module_21h"] = canon_b(lit(MODULE_21H))
CONNUS = set(CANONS.values())
CONNUS.update(re.findall(HEX, lit(SON_MAN).decode("utf-8")))
for t in CITES.values():
    CONNUS.update(re.findall(HEX, t))
DECLARES = {"6eae3f6860a46eef"}      # canon de ma note de la 22f : cite d'apres le SUIVI du 22/11 f au projet, NON recalcule ici


def lg(journal, motif):
    """Premiere ligne du journal qui contient le motif (expression reguliere)."""
    for l in J[journal].splitlines():
        if re.search(motif, l):
            return l
    raise RuntimeError("ligne absente du journal %s : %s" % (journal, motif))


def lgs(journal, motif):
    return [l for l in J[journal].splitlines() if re.search(motif, l)]


def controle(note):
    """Rend (nombre de controles, liste des morsures)."""
    mord, n = [], [0]

    def c(cond, texte):
        n[0] += 1
        if not cond:
            mord.append(texte)

    plat = " ".join(note.split())

    def dans(fragment, texte):
        # le fragment est cherche a la mise en ligne pres (blancs et retours a la ligne confondus) ;
        # un fragment qui finit par un retour a la ligne est une ligne de TABLE : il est cherche tel quel
        if fragment.endswith("\n"):
            c(fragment in note, texte + " : ligne de table absente de la note : " + fragment.strip())
        else:
            c(" ".join(fragment.split()) in plat, texte + " : absent de la note : " + " ".join(fragment.split()))

    # ---------------- (A) forme
    octets = note.encode("utf-8")
    c(all(b < 128 for b in octets), "A1 la note n'est pas en ASCII")
    c("\r" not in note, "A2 fin de ligne CR")
    c("\x25" not in note, "A3 signe pour-cent")
    c("\t" not in note, "A4 tabulation")
    c(note.endswith("\n") and not note.endswith("\n\n"), "A5 fin de fichier")
    c(all(len(l) <= 104 for l in note.split("\n")), "A6 ligne de plus de 104 colonnes")
    for k in range(12):
        c(len(re.findall(r"(?m)^## %d\. " % k, note)) == 1, "A7 section %d absente ou double" % k)
    for k in range(1, 13):
        c(len(re.findall(r"(?m)^%d\. [A-Z(]" % k, note)) == 1, "A8 ligne %d de la section 0 absente ou double" % k)
    for q in ("Q-1", "Q-2", "Q-3", "Q-4", "Q-5"):
        c(len(re.findall(r"(?m)^  %s  " % q, note)) == 1, "A9 attendu %s absent ou double" % q)
    for q in ("Q-a", "Q-c", "Q-d", "Q-e", "Q-f"):
        c(len(re.findall(r"(?m)^    %s " % q, note)) == 2, "A10 point %s : deux lignes de table attendues (6.2 et 8.1)" % q)
    c(note.count("D-REL-28") >= 3, "A11 le defaut D-REL-28 n'est pas dit en tete, en section 0 et en section 10")
    c("CE QUI ME DONNERAIT TORT" in note and "CE QUE CHAQUE ISSUE ENGAGE" in note, "A12 clause de tort ou issues absentes")
    for lettre in "abcdef":
        c(len(re.findall(r"(?m)^  \(%s\) " % lettre, note)) == 1, "A13 question (%s) absente ou double" % lettre)

    # ---------------- (B1) chaque nombre decimal de la note a un appui
    for tok in nombres(note):
        if tok in SEUILS:
            n[0] += 1
            continue
        v, k = float(tok), chiffres(tok)
        c(any(abs(arrondi(x, k) - v) <= 1e-12 * max(1.0, abs(v)) for x in VALEURS), "B1 nombre sans appui dans les journaux ni les pieces citees : " + tok)

    # ---------------- (B2) les chiffres qui portent la note, attaches a leur ligne
    m = re.search(r"plus petit (\S+) ; plus grand (\S+) ; hors fenetre : 0", lg("notation", r"=== 2\. S-1") and lg("notation", r"plus petit"))
    dans("de %s a %s, fenetre [0.0539, 0.0549]. TENU." % (m.group(1), m.group(2)), "B2 S-1")
    m = re.search(r"plus grand ecart : (\S+) ", lg("notation", r"^plus grand ecart : "))
    dans("plus grand ecart a ma table %s, limite 2.5e-04. TENU." % m.group(1), "B2 S-2")
    m = re.search(r"coupes paires \(12\) : de (\S+) a (\S+) ; coupes impaires \(12\) : de (\S+) a (\S+)", lg("notation", r"coupes paires \(12\)"))
    dans("coupes paires de %s a %s, coupes impaires de %s a %s." % m.groups(), "B2 S-3")
    m = re.search(r"plus grand etalement : (\S+) \(limite 0\.02\) ; TORT REALISE : NON", lg("notation", r"TORT REALISE"))
    c(m is not None, "B2 le journal de notation ne dit pas TORT REALISE : NON")
    if m:
        dans("plus grand etalement %s, limite 0.02. NON REALISE." % m.group(1), "B2 tort")
    c(lg("notation", r"^=== BILAN").strip() == "=== BILAN : S-1 TENU ; S-2 TENU ; S-3 TENU ; tort NON REALISE", "B2 bilan du journal de notation")
    m = re.search(r"pire \|somme des poids - 1\| : (\S+) ; pire residu : (\S+)", lg("notation", r"pire residu"))
    dans("pire |somme des poids - 1| :\n%s ; pire residu : %s." % m.groups(), "B2 controle R1")
    m = re.search(r"m = 0 a 30 : (\S+)", lg("controle", r"ecart relatif maximal"))
    dans("ecart\n    relatif %s au pire, de m = 0 a 30" % m.group(1), "B2 forme close")
    m = re.search(r"de (\S+) a (\S+) ; moyenne", lg("controle", r"absorbeur fort \(24 cas"))
    dans("24 cas forts de %s a %s" % m.groups(), "B2 chaine du premier ordre")
    tri = [re.search(r"Gamma / g (\S+) ; Re E / g (\S+) ; poids (\S+)", l).groups() for l in lgs("controle", r"plus grand ecart a machine 2 : Gamma")]
    c(len(tri) == 8, "B2 huit boites rejouees attendues au journal, lu %d" % len(tri))
    c(len(lgs("controle", r"^   a = \S+ m0 = \d : Gamma / g = ")) == 96, "B2 96 cas rejoues attendus au journal")
    if len(tri) == 8:
        pg, pr, pp = (max(float(t[i]) for t in tri) for i in range(3))
        dans("plus\n    grand ecart a tes nombres : %.1e sur Gamma / g, %.1e sur Re E / g, %.1e sur le poids." % (pg, pr, pp), "B2 rejeu")
        dans("plus grand ecart %.1e (section 2)" % max(pg, pr, pp), "B2 rejeu, section 0")
    m = re.search(r"plus grand \|2D - C1\| = (\S+) ; cas au-dessus de 2\.5e-04 : 0", lg("apres coup", r"48 cas forts"))
    dans("plus grand |2D - C1| = %s sur 48 cas" % m.group(1), "B2 C1 passe S-2")
    faibles = [l.split() for l in lgs("apres coup", r"^    (0\.5|1\.0)  \de-0\d ")]
    c(len(faibles) == 4 and all(l[4:] == ["12", "sur", "12"] for l in faibles), "B2 C1 plus pres que C2 aux 48 cas faibles")
    if len(faibles) == 4:
        dans("plus grand |2D - C1| = %s, plus grand |2D - C2| = %s." % (max((l[2] for l in faibles), key=float), max((l[3] for l in faibles), key=float)), "B2 absorbeur faible")
    sig = lgs("apres coup", r"coupes (paires|impaires) +: 2D - C1 : .* C2 - C1")
    c(len(sig) == 2 and "12 negatifs, 0 positifs ; C2 - C1 : 0 negatifs, 12 positifs" in sig[0] and "0 negatifs, 12 positifs ; C2 - C1 : 12 negatifs, 0 positifs" in sig[1], "B2 signes opposes a a = 0.5")
    r = [re.search(r"2D - C1 : de (\S+) a (\S+) ;", l).groups() for l in lgs("apres coup", r"^    a = \S+ : 2D - C1 : de")]
    dans("multiplie par %s a %s quand g double" % (min((x[0] for x in r), key=float), max((x[1] for x in r), key=float)), "B2 croissance en g")
    m = re.search(r"moyenne (\S+) ; reference", lg("apres coup", r"^    de \S+ a \S+ ; moyenne"))
    dans("moyenne des 48 cas forts %s aux deux couplages" % m.group(1), "B2 plateau")
    # le sommet
    m = re.search(r"tau_0 = X\(2\) / P = (\S+) ; forme close 1 / \(4 sqrt 6\) = (\S+)", lg("sommet", r"^tau_0 = "))
    dans("tau_0 = X(2) / P = %s (ma forme close : %s)" % m.groups(), "B2 tau_0")
    b = [re.search(r"le site (\d) entre dans la barriere pour \|d\| / g > (\S+), soit kappa < (\S+)", l).groups() for l in lgs("sommet", r"le site \d entre")]
    dans("le site 1 entre pour |d| / g > %s, soit kappa < %s ;   le site 2 : %s, %s ;" % (b[0][1], b[0][2], b[1][1], b[1][2]), "B2 barriere 1-2")
    dans("le site 3 : %s, %s ;   le site 4 : %s, %s." % (b[2][1], b[2][2], b[3][1], b[3][2]), "B2 barriere 3-4")
    for prof in (1, 2, 3):
        m = re.search(r"milieu geometrique (\S+) ; \|d\| / g = (\S+)", lg("sommet", r"profondeur %d : kappa de" % prof))
        dans("profondeur %d : milieu geometrique %s, |d| / g = %s" % (prof, m.group(1), m.group(2)), "B2 profondeur %d" % prof)
    sept = re.findall(r"m = \d+ : (\S+)", lg("sommet", r"^   m = 3 : "))
    dans("|d| / g = %s, %s, %s, %s, %s, %s et %s." % tuple(sept), "B2 les sept profondeurs du gel du vide")
    for q, w2t, gt in (("Q-a", "2     ", "2.5e-04"), ("Q-c", "2     ", "1e-03  "), ("Q-d", "2     ", "2e-03  "), ("Q-e", "2.0001", "3e-04  "), ("Q-f", "2.0001", "1.5e-04")):
        m = re.search(r"G3\* / g = (\S+)  G3\* = (\S+)  etendue (\S+)", lg("sommet", r"^    %s  w2 = \S+ +g = \S+  G3\* / g" % q))
        dans("    %s              %s   %s  %s    %s  %s\n" % (q, w2t, gt, m.group(1), m.group(2), m.group(3)), "B2 table 6.2, %s" % q)
        e = re.search(r"eta0 = (\S+)  eta0 / g = (\S+)  r_c = 18  QUALIFIE", lg("sommet", r"^    %s  w2 = \S+ +eta0 = " % q))
        c(e is not None, "B2 %s : pas de ligne QUALIFIE, r_c = 18, au resume du mandataire" % q)
        if e:
            c(len(re.findall(r"(?m)^    %s .*eta0 = %s$" % (q, re.escape(e.group(1))), note)) == 1, "B2 table 8.1, %s : eta0 = %s attendu" % (q, e.group(1)))
    g3 = [re.search(r"G3\* = (\S+)", lg("sommet", r"^    %s  w2 = \S+ +g = \S+  G3\* / g" % q)).group(1) for q in ("Q-a", "Q-c", "Q-d", "Q-e", "Q-f")]
    dans("%s, %s, %s, %s, %s. 0.75." % tuple(g3), "B2 les cinq cibles de Q-2")
    m = re.search(r"plus grand etalement a kappa fixe : (\S+) ; sur la grille : etendue d'ordre 3 max (\S+) ; \|ln\(G3 / G1\)\| max (\S+) ; \|ln\(G3 / G2\)\| max (\S+)", lg("sommet", r"plus grand etalement a kappa fixe"))
    dans("etendue d'ordre 3 de %s au plus ; |ln(G3 / G1)| de %s au plus ; |ln(G3 / G2)| de\n%s au plus. La loi d'echelle y tient a %s pres" % (m.group(2), m.group(3), m.group(4), m.group(1)), "B2 grille")
    m = re.search(r": (\d+) points ; plus grand ecart (\S+)", lg("sommet", r"controle de ma lecture par le flux"))
    dans("a %s pres, a %s points sur %s." % (m.group(2), m.group(1), m.group(1)), "B2 lecture par le flux contre le bloc")
    m = re.search(r"G1\* / g = (\S+) ; G1\* / t_0 = (\S+)", lg("sommet", r"a la resonance exacte"))
    dans("Gamma / t_0 = %s, soit %s g" % (m.group(2), m.group(1)), "B2 resonance")
    res = lgs("sommet", r"^    \S.*eta0 = \S+  eta0 / g = \S+  r_c = \d+  (QUALIFIE|NON QUALIFIE)  fenetres")
    c(len(res) == 19 and all("  QUALIFIE  " in l for l in res), "B2 19 points qualifies au resume du mandataire")
    dans("QUALIFIE a 19 points sur 19", "B2 mandataire")
    c(lg("sommet", r"^regle en absolu : ").startswith("regle en absolu : 19 points sur 19 qualifies par le mandataire ; non qualifies : aucun"), "B2 ligne de compte du mandataire")
    fen = {a: sorted(set(int(re.search(r"%s ([-+]\d)" % a, l.split("fenetres k0 :")[1]).group(1)) for l in res)) for a in "ABCD"}
    c(fen == {"A": [-1], "B": [-1, 0], "C": [0, 1, 2], "D": [-2, -1]}, "B2 fenetres du mandataire : %s" % fen)
    dans("Fenetres : A a\n    k0 = -1 partout ; B a -1 ou 0 ; C a 0, +1 ou +2 ; D a -2 ou -1.", "B2 fenetres du mandataire, texte")
    dans("Plus grand |ln(X / A)| : %.4f." % max(float(re.search(r"plus grand \|ln\(X / A\)\| (\S+)", l).group(1)) for l in res), "B2 accord des absorbeurs")
    dans("%.3f au moins" % min(float(re.search(r"poids >= (\S+)", l).group(1)) for l in res), "B2 poids")
    dans("(eta0 / g = %s a w2 = 2)" % re.search(r"eta0 / g = (\S+)", lg("sommet", r"^    Q-a  w2 = 2 +eta0")).group(1), "B2 eta0 / g")
    c("['Q-e  w2 = 2.0001', 'k=0.400-', 'k=0.400+', 'k=1.000-', 'k=1.000+']" in lg("sommet", r"^regle du depot"), "B2 regle du depot : points non qualifies")
    m = re.search(r"rapport (\S+) non", lg("sommet", r"Q-e +depot : \|w2 - 2\| +eta0/g = +\S+  D "))
    dans("rapport %s)" % m.group(1), "B2 regle du depot au point Q-e")
    # l'esquisse
    c(lg("esquisse", r"^cellules candidates").startswith("cellules candidates : 133 (19 w2 x 7 kappa) ; eligibles (m_bord = cible et etendue <= 0.02) : 133"), "B2 133 cellules eligibles")
    dans("133 cellules (19 w2, 7\nkappa), toutes eligibles", "B2 esquisse, compte")
    for kap, prof in (("0.0363", 2), ("0.0530", 1), ("0.0800", 0), ("0.1300", 0), ("0.2000", 0), ("0.4000", 0), ("1.0000", 0)):
        m = re.search(r"G3\* / \|d\| de (\S+) a (\S+) \(etalement \S+ en logarithme\) ; G3\* / g de (\S+) a (\S+)", lg("esquisse", r"^kappa = %s : 19 cellules" % kap))
        dans("    %s   %d           %s a %s    %s a %s\n" % (kap, prof, m.group(1), m.group(2), m.group(3), m.group(4)), "B2 table 6.4, kappa = %s" % kap)
    m = re.search(r"couplages : de (\S+) a (\S+) ; largeurs predites G3\* : de (\S+) a (\S+)", lg("esquisse", r"^couplages : "))
    dans("Couplages de %s a %s ; largeurs predites de %s a %s" % m.groups(), "B2 esquisse, couplages")
    m = re.search(r"plus grande (\S+) ; \|ln\(G3/G1\)\| : plus grand (\S+) ;", lg("esquisse", r"^etendue d'ordre 3"))
    dans("etendue de\n%s au plus ; |ln(G3 / G1)| de %s au plus." % m.groups(), "B2 esquisse, etendue")
    m = re.search(r": de (\d+) a (\d+) ; cellules ou m\* <= r_c / 2 .* : (\d+)", lg("esquisse", r"^m\* \("))
    dans("(m*) va de %s a\n%s" % (m.group(1), m.group(2)), "B2 m*")
    c(m.group(3) == "0", "B2 une cellule a son absorbeur au-dela de m*")
    m = re.search(r": (\d+) ; plus grand rapport : (\S+)", lg("esquisse", r"^cellules ou G3\* depasse"))
    dans("A %s cellules la largeur\npredite depasse 1.785e-05, jusqu'a %s fois" % m.groups(), "B2 largeurs au-dessus de la plage qualifiee")
    # les fenetres du delta 102
    cel = [l.split() for l in lgs("fenetres", r"^(MG3|MP3|PP3|PG3) ")]
    c(len(cel) == 4, "B2 quatre cellules de trois barreaux attendues")
    if len(cel) == 4:
        xs = [float(l[3]) for l in cel]; phis = [float(l[11]) for l in cel]
        dans("Gamma_pl / |d| va de %.4e a %.4e, pour |d| / g de %.3f a %.3f." % (min(phis), max(phis), min(xs), max(xs)), "B2 jonction")
        dans("eta0 / g de\n    %.3f a %.3f" % (min(xs), max(xs)), "B2 eta0 / g aux cellules de trois barreaux")
        dans("rien en deca de |d| / g = %.2f (cellule PG3" % min(xs), "B2 bord des ailes")
        f2 = {a: sorted(set(int(l[5 + i]) for l in cel)) for i, a in enumerate("ABCD")}
        c(f2 == {"A": [-2, -1], "B": [-1], "C": [1, 2], "D": [-2]}, "B2 fenetres du delta 102 : %s" % f2)
        dans("les fenetres retenues sont A a -2 ou -1, B a -1, C a +1 ou +2, D a -2.", "B2 fenetres du delta 102, texte")

    # ---------------- (C) citations et empreintes
    for h in sorted(set(re.findall(HEX, note))):
        c(h in CONNUS or h in DECLARES, "C1 empreinte inconnue : " + h)
    dans("Lot %s authentifie : 27 pieces sur 27" % CANONS["son_manifeste"], "C2 canon du lot de machine 2")
    c(len(re.findall(r"(?m)^[0-9a-f]{16} [0-9a-f]{16} +\d+ +\d+ +\S", lit(SON_MAN).decode("utf-8"))) == 27, "C2 le manifeste de machine 2 ne porte pas 27 pieces")
    for nom, texte in (("moteur", "Le moteur (%s)"), ("bloc2", "(%s, 534ba246aa3b8973"), ("bloc3", "7cd5977bc27bebc1, %s,"), ("bloc_adapte", "bloc\n    %s)"),
                       ("sonde_lecteur", "sonde deposee (%s)"), ("feuille_lecteur", "feuille deposee (%s)"), ("sonde_vide", "sonde du gel du vide (%s)"),
                       ("gel1", "partie 1 (%s)"), ("gel2", "partie 2 (%s)"), ("module_21h", "mon module de la 21h (%s)")):
        dans(texte % CANONS[nom], "C3 canon recalcule de %s" % nom)
    dans("tete %s" % TETE[:7], "C4 tete du registre")
    dans('"je dis oui on ouvre. Par contre tous les calculs\ncouteux, c\'est sur machine 2 ok ?"', "C5 le mot de l'operateur")
    for cite, source in (("0.0262, 0.0200, 0.0159, 0.0130", "gel1"), ("0.00928", "gel1"), ("0.00558", "gel1"), ("0.00382", "gel1"),
                         ("0.00068", "acte102"), ("0.00134", "acte102"), ("r_c = 2 (m + max(8, m)) + 2", "gel2"), ("eta_k = eta0 2^(-k)", "gel2")):
        c(cite.split(", ")[0] in CITES[source] and cite in note, "C6 citation absente de la piece %s ou de la note : %s" % (source, cite))
    c("m = 3 : 0.0262   m = 4 : 0.0200   m = 5 : 0.0159   m = 6 : 0.0130" in CITES["gel1"], "C6 les kappa lisibles du gel du vide")
    return n[0], mord


ALTERATIONS = [
    ("une borne de S-1", lambda s: s.replace("0.054191", "0.054192")),
    ("l'ecart du rejeu", lambda s: s.replace("1.9e-10", "1.8e-10")),
    ("une cible de Q-2", lambda s: s.replace("1.20924e-05", "1.20934e-05", 1)),
    ("un eta0 de la table 8.1", lambda s: s.replace("7.79100e-03", "7.79200e-03")),
    ("un bord de barriere", lambda s: s.replace("1.5713", "1.5813")),
    ("le compte des candidates", lambda s: s.replace("133 cellules (19 w2", "134 cellules (19 w2")),
    ("un signe pour-cent", lambda s: s.replace("a 0.0032 pres", "a 0.32 \x25 pres")),
    ("une fin de ligne CR", lambda s: s.replace("\n## 3.", "\r\n## 3.")),
    ("une ligne trop large", lambda s: s.replace("## 8. LA QUALIFICATION", "## 8. LA QUALIFICATION" + " x" * 45)),
    ("une empreinte", lambda s: s.replace("2d69195af996cc0f", "2d69195af996cc0e", 1)),
    ("le mot de l'operateur", lambda s: s.replace("je dis oui on ouvre", "je dis oui, on ouvre")),
    ("un attendu en moins", lambda s: s.replace("  Q-3  le temoin", "  Q-trois  le temoin")),
    ("une fenetre du mandataire", lambda s: s.replace("D a -2 ou -1.", "D a -3 ou -1.")),
    ("une section en moins", lambda s: s.replace("## 9. L'ESQUISSE", "## 9bis. L'ESQUISSE")),
    ("la largeur a la resonance", lambda s: s.replace("0.53331", "0.53341")),
    ("un caractere non ASCII", lambda s: s.replace("A JOUER CHEZ TOI", chr(192) + " JOUER CHEZ TOI", 1)),
    ("le compte du mandataire", lambda s: s.replace("QUALIFIE a 19 points sur 19", "QUALIFIE a 18 points sur 19")),
    ("l'accord des absorbeurs", lambda s: s.replace("Plus grand |ln(X / A)| : 0.0054", "Plus grand |ln(X / A)| : 0.0064")),
    ("une ligne de la table 6.4", lambda s: s.replace("5.1726e-01 a 5.1746e-01", "5.1726e-01 a 5.1756e-01")),
    ("la jonction avec le delta 102", lambda s: s.replace("1.6342e-07", "1.6352e-07")),
    ("un kappa du gel du vide", lambda s: s.replace("0.00928", "0.00938")),
    ("une question en moins", lambda s: s.replace("  (f) ce que je n'ai pas vu.", "  ce que je n'ai pas vu.")),
]

note = lit(NOTE).decode("utf-8")
print("note : %d octets, %d lignes, canon B %s" % (len(note.encode("utf-8")), note.count("\n"), canon_b(lit(NOTE))))
print("journaux lus : %d ; pieces citees lues : %d ; canons recalcules : %d ; empreintes connues : %d ; declarees sans recalcul : %d (%s)" % (
    len(J), len(CITES), len(CANONS), len(CONNUS), len(DECLARES), ", ".join(sorted(DECLARES))))
nc, mord = controle(note)
for x in mord:
    print("MORD " + x)
print("controles : %d ; morsures : %d" % (nc, len(mord)))
print()
print("CONTRE-EPREUVE : une alteration a la fois ; attendu : au moins une morsure a chacune")
muettes = 0
for nom, f in ALTERATIONS:
    alt = f(note)
    if alt == note:
        print("SANS EFFET  %-32s l'alteration ne change pas la note" % nom); muettes += 1
        continue
    n2, m2 = controle(alt)
    if not m2:
        muettes += 1
    print("%-5s %-32s %d morsure(s) : %s" % ("MORD" if m2 else "MUET", nom, len(m2), (m2[0][:92] if m2 else "")))
print("alterations : %d ; mordues : %d ; muettes : %d" % (len(ALTERATIONS), len(ALTERATIONS) - muettes, muettes))
print("VERDICT : %s" % ("NOTE CONFORME, CONTROLE MORDANT" if (not mord and muettes == 0) else "A REPRENDRE"))
sys.exit(0 if (not mord and muettes == 0) else 1)
