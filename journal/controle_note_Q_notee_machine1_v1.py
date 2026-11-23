# -*- coding: ascii -*-
"""Controle de la note POUR_MACHINE2_Q_notee_et_Q2_attendus_machine1_v1.md, en trois familles : (A) forme ; (B) chiffres
contre les journaux : chaque nombre decimal de la note doit se retrouver, a son arrondi, dans un journal ou une piece citee,
et les chiffres qui portent la note sont attaches a LEUR ligne de journal ; (C) citations et empreintes. Puis contre-epreuve :
chaque alteration doit faire tomber au moins un controle, depuis une note sans aucun controle tombe.

usage : python3 -I controle_note_Q_notee_machine1_v1.py <la note> <journal de notation de Q> <journal des points Q2>
            <journal de l'esquisse (lot 423ec0fd24240977)> <la note de machine 2> <manifeste du lot de machine 2>
            <manifeste de mon lot 423ec0fd24240977> <clone du registre> <tete du clone>
Tout est lu comme des donnees ; rien n'est execute.
"""
import hashlib, math, os, re, sys, unicodedata

(NOTE, J_Q, J_Q2, J_ESQ, SA_NOTE, SON_MAN, MON_MAN, CLONE, TETE) = sys.argv[1:10]
NB = r"(?<![A-Za-z0-9_.])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?(?![A-Za-z0-9_])"
HEX = r"\b[0-9a-f]{16}\b"
# seuils, probabilites et constantes posees par la plume ou citees telles quelles : pas des resultats
SEUILS = {"0.85", "0.75", "0.9", "0.7", "0.002", "0.01", "0.0005", "+0.0007", "+0.0017", "+0.0016", "+0.0026", "0.0262", "0.67", "3.9", "8e-05",
          "1e-4", "2.0001", "1.9999", "0.005", "6e-05", "4e-05", "3e-04", "1.5e-04", "6e-5", "4e-5", "3e-4", "1.5e-4"}


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


J = {n: lit(ch).decode("utf-8") for n, ch in (("Q", J_Q), ("Q2", J_Q2), ("esquisse", J_ESQ))}
SA = lit(SA_NOTE).decode("utf-8")
VALEURS = set()
for t in J.values():
    VALEURS.update(float(x) for x in nombres(t))
DEPOSES = {"feuille": os.path.join(CLONE, "scripts", "lecture_lecteur_gel_loi_machine1_v1.py"), "moteur": os.path.join(CLONE, "scripts", "m17_chaine_v17.py"),
           "bloc2": os.path.join(CLONE, "scripts", "chaine_ordre2_bloc_machine1_v1.py"), "bloc3": os.path.join(CLONE, "scripts", "ordre3_bloc_machine1_v1.py"),
           "bloc_adapte": os.path.join(CLONE, "scripts", "chaine_adaptee_bloc_machine1_v1.py")}
CANONS = {n: canon_b(lit(ch)) for n, ch in DEPOSES.items()}
CANONS["son_manifeste"] = canon_b(lit(SON_MAN)); CANONS["mon_manifeste"] = canon_b(lit(MON_MAN))
CONNUS = set(CANONS.values())
for ch in (SON_MAN, MON_MAN):
    CONNUS.update(re.findall(HEX, lit(ch).decode("utf-8")))


def lg(journal, motif):
    for l in J[journal].splitlines():
        if re.search(motif, l):
            return l
    raise RuntimeError("ligne absente du journal %s : %s" % (journal, motif))


def controle(note):
    mord, n = [], [0]
    plat = " ".join(note.split())

    def c(cond, texte):
        n[0] += 1
        if not cond:
            mord.append(texte)

    def dans(fragment, texte):
        if fragment.endswith("\n"):
            c(fragment in note, texte + " : ligne de table absente de la note : " + fragment.strip())
        else:
            c(" ".join(fragment.split()) in plat, texte + " : absent de la note : " + " ".join(fragment.split()))

    # (A) forme
    c(all(b < 128 for b in note.encode("utf-8")), "A1 la note n'est pas en ASCII")
    c("\r" not in note, "A2 fin de ligne CR")
    c("\x25" not in note, "A3 signe pour-cent")
    c("\t" not in note, "A4 tabulation")
    c(note.endswith("\n") and not note.endswith("\n\n"), "A5 fin de fichier")
    c(all(len(l) <= 104 for l in note.split("\n")), "A6 ligne de plus de 104 colonnes")
    for k in range(7):
        c(len(re.findall(r"(?m)^## %d\. " % k, note)) == 1, "A7 section %d absente ou double" % k)
    for k in range(1, 9):
        c(len(re.findall(r"(?m)^%d\. [A-Z]" % k, note)) == 1, "A8 ligne %d de la section 0 absente ou double" % k)
    for q in ("Q2-1", "Q2-2", "Q2-3", "Q2-4"):
        c(len(re.findall(r"(?m)^  %s  " % q, note)) == 1, "A9 attendu %s absent ou double" % q)
    for q in ("Q2-a", "Q2-b", "Q2-c", "Q2-d"):
        c(len(re.findall(r"(?m)^    %s " % q, note)) == 1, "A10 point %s : une ligne de table attendue" % q)
    c("CE QUI ME DONNERAIT TORT" in note and "CE QUE CHAQUE ISSUE ENGAGE" in note and "DECLARATION, avant toute lecture" in note, "A11 clause de tort, issues ou declaration absentes")
    c(note.count("D-REL-29") >= 3, "A12 le defaut D-REL-29 n'est pas dit trois fois")
    # (B1) chaque nombre decimal a un appui
    for tok in nombres(note):
        if tok in SEUILS:
            n[0] += 1
            continue
        v, k = float(tok), chiffres(tok)
        c(any(abs(arrondi(x, k) - v) <= 1e-12 * max(1.0, abs(v)) for x in VALEURS), "B1 nombre sans appui dans les journaux : " + tok)
    # (B2) les chiffres qui portent la note
    c(lg("Q", r"^=== BILAN").strip() == "=== BILAN : Q-1 TENU ; Q-2 TENU ; Q-3 TENU ; Q-4 TENU ; Q-5 TENU ; tort NON REALISE", "B2 bilan de Q au journal")
    for pid, nom in (("Qa", "Q-a"), ("Qc", "Q-c"), ("Qd", "Q-d"), ("Qe", "Q-e"), ("Qf", "Q-f")):
        bloc = J["Q"].split("=== %s " % pid)[1].split("===")[0]
        st = re.search(r"statut (\S+ ?\S*) ; echecs", J["Q"].split("=== %s " % pid)[1]).group(1)
        k0 = {a: re.search(r"(?m)^    %s : PLATEAU  k0 = ([-+]\d)" % a, bloc).group(1) for a in "ABCD"}
        m = re.search(r"(?m)^    A : PLATEAU  k0 = \S+  etalement \S+  Gamma_pl = (\S+)  ln\(Gamma_pl / G3\*\) = (\S+)", bloc)
        ex = max(float(x) for x in re.findall(r"\|ln\(X / A\)\| = (\S+)", bloc))
        dans("    %s    %s  %s %s %s %s    %s    %s            %.4f\n" % (nom, st, k0["A"], k0["B"], k0["C"], k0["D"], m.group(1), m.group(2), ex), "B2 table de Q, %s" % nom)
    m = re.search(r"plus grand (\S+)\)", lg("Q", r"^Q-2 "))
    dans("Q-2  TENU, plus grand ecart %s." % m.group(1), "B2 Q-2")
    m = re.search(r"rapportee au plateau : (\S+)\)", lg("Q", r"^Q-3 "))
    dans("jumeau a %s du plateau au plus" % m.group(1), "B2 Q-3")
    c("19 sur 20 (il en faut 16) : TENU ; hors liste : [('Qd', 'C', 3)]" in lg("Q", r"^Q-4 "), "B2 Q-4 au journal")
    dans("Q-4  TENU, 19 sur 20 ; hors liste : Q-d sous C, k0 = +3.", "B2 Q-4")
    m = re.search(r"= (\S+) \(<= 0\.005\) : TENU", lg("Q", r"^Q-5 "))
    dans("Q-5  TENU, %s." % m.group(1), "B2 Q-5")
    c(lg("Q", r"^lectures suivies").strip() == "lectures suivies : 477 sur 480", "B2 lectures suivies au journal")
    dans("Lectures suivies : 477 sur 480.", "B2 lectures suivies")
    c("[-3, -2, -1, 0, 1, 2, 3, 4]" in lg("Q", r"^barreaux plats"), "B2 barreaux plats au journal")
    for q in ("Q2-a", "Q2-b", "Q2-c", "Q2-d"):
        f = lg("Q2", r"^%s " % q).split()
        mb = f[5].rstrip("*")
        dans("    %s   %s   %s  %s  %s   %s  %s  %s\n" % (q, f[1], {"6.0e-05": "6e-05  ", "4.0e-05": "4e-05  ", "3.0e-04": "3e-04  ", "1.5e-04": "1.5e-04"}[f[2]], mb, f[6], f[7], f[9], f[11]), "B2 table de Q2, %s" % q)
        idc = q.replace("-", ""); gj = {"6.0e-05": "6e-5", "4.0e-05": "4e-5", "3.0e-04": "3e-4", "1.5e-04": "1.5e-4"}[f[2]]
        for signe in ("-1", "1"):
            c(("%s %s %s %s %s %s %s ABCD" % (idc, f[1], gj, mb, f[7], signe, f[6])) in note, "B2 ligne de travail %s signe %s" % (q, signe))
    r1 = re.search(r"= (\S+) ", lg("Q2", r"^ln\[G3\*\(Q2-c\)")).group(1); r2 = re.search(r"= (\S+) ", lg("Q2", r"^ln\[G3\*\(Q2-d\)")).group(1)
    dans("ln[G3*(Q2-c) / G3*(Q-e)] = %s et ln[G3*(Q2-d) / G3*(Q-f)] = %s." % (r1, r2), "B2 rapports de signe de la chaine")
    for r, (bas, haut) in ((r1, ("+0.0007", "+0.0017")), (r2, ("+0.0016", "+0.0026"))):
        c(abs(float(bas) - (float(r) - 0.0005)) <= 5.1e-05 and abs(float(haut) - (float(r) + 0.0005)) <= 5.1e-05, "B2 fenetre de Q2-4 : [%s, %s] n'est pas %s a 0.0005 pres" % (bas, haut, r))
    dans("[+0.0007, +0.0017]", "B2 fenetre 1 de Q2-4"); dans("[+0.0016, +0.0026]", "B2 fenetre 2 de Q2-4")
    man = [l for l in J["Q2"].splitlines() if re.match(r"^Q2-[abcd] +r_c", l)]
    c(len(man) == 4 and all("  QUALIFIE (mandataire)  " in l and "k = -3 a 4" in l for l in man), "B2 mandataire aux quatre points")
    dans("poids du site 0 de %.3f au moins" % min(float(re.search(r"poids >= (\S+)", l).group(1)) for l in man), "B2 poids du mandataire")
    m = re.search(r"plus grande (\S+) ;", lg("esquisse", r"^etendue d'ordre 3"))
    dans("etendue de chaine de %s au plus" % m.group(1), "B2 etendue de la chaine a l'esquisse")
    # (C) citations et empreintes
    for h in sorted(set(re.findall(HEX, note))):
        c(h in CONNUS, "C1 empreinte inconnue : " + h)
    dans("Lot %s authentifie : 38 pieces sur 38" % CANONS["son_manifeste"], "C2 canon du lot de machine 2")
    c(len(re.findall(r"(?m)^[0-9a-f]{16} [0-9a-f]{16} +\d+ +\d+ +\S", lit(SON_MAN).decode("utf-8"))) == 38, "C2 le manifeste de machine 2 ne porte pas 38 pieces")
    dans("mon lot %s et sa note" % CANONS["mon_manifeste"], "C3 canon de mon lot precedent")
    dans("feuille deposee (%s)" % CANONS["feuille"], "C3 canon de la feuille")
    dans("bloc depose %s" % CANONS["bloc_adapte"], "C3 canon du bloc adapte")
    dans("tete %s" % TETE[:7], "C4 tete du registre")
    dans('"Machine2 a hate de faire le calcul supp"', "C5 le mot de l'operateur")
    for cite in ("Q2-a   w2 = 20001/10000   g = 6e-05", "Q2-b   w2 = 20001/10000   g = 4e-05", "Q2-c   w2 = 19999/10000   g = 3e-04", "Q2-d   w2 = 19999/10000   g = 1.5e-04"):
        c(cite in SA, "C6 le point n'est pas celui que machine 2 demande : " + cite)
    c("Je proposerais 0.01" in SA and "T passe a 0.01" in note, "C6 T = 0.01")
    return n[0], mord


ALTERATIONS = [
    ("une cible de Q2", lambda s: s.replace("4.94622e-08", "4.94722e-08")),
    ("un eta0 de Q2", lambda s: s.replace("1.55762e-04", "1.55772e-04", 1)),
    ("un r_c de Q2", lambda s: s.replace("    Q2-b   20001/10000   4e-05    2  22 ", "    Q2-b   20001/10000   4e-05    2  20 ")),
    ("une ligne de travail", lambda s: s.replace("Q2c 19999/10000 3e-4 0 1.16909e-03 -1 18 ABCD", "Q2c 19999/10000 3e-4 0 1.16909e-03 -1 20 ABCD")),
    ("un rapport de signe", lambda s: s.replace("+0.00121", "+0.00131")),
    ("une fenetre de Q2-4", lambda s: s.replace("[+0.0007, +0.0017]", "[+0.0002, +0.0022]")),
    ("un plateau de Q", lambda s: s.replace("1.20926e-05", "1.20936e-05")),
    ("le compte de Q-4", lambda s: s.replace("19 sur 20 ; hors liste", "20 sur 20 ; hors liste")),
    ("un signe pour-cent", lambda s: s.replace("a 0.005 pres aux barreaux", "a 0.5 \x25 pres aux barreaux")),
    ("une fin de ligne CR", lambda s: s.replace("\n## 3.", "\r\n## 3.")),
    ("une ligne trop large", lambda s: s.replace("## 4. MES ATTENDUS", "## 4. MES ATTENDUS" + " x" * 45)),
    ("une empreinte", lambda s: s.replace("c58c2b3f533c516b", "c58c2b3f533c516a", 1)),
    ("le mot de l'operateur", lambda s: s.replace("Machine2 a hate de faire", "Machine 2 a hate de faire")),
    ("un attendu en moins", lambda s: s.replace("  Q2-3  le temoin", "  Q2-trois  le temoin")),
    ("un caractere non ASCII", lambda s: s.replace("MEMES COMPTES", "M" + chr(202) + "MES COMPTES", 1)),
    ("la declaration en moins", lambda s: s.replace("DECLARATION, avant toute lecture", "Avant toute lecture")),
]

note = lit(NOTE).decode("utf-8")
print("note : %d octets, %d lignes, canon B %s" % (len(note.encode("utf-8")), note.count("\n"), canon_b(lit(NOTE))))
print("journaux lus : %d ; canons recalcules : %d ; empreintes connues : %d" % (len(J), len(CANONS), len(CONNUS)))
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
        print("SANS EFFET  %-28s l'alteration ne change pas la note" % nom); muettes += 1
        continue
    n2, m2 = controle(alt)
    if not m2:
        muettes += 1
    print("%-5s %-28s %d morsure(s) : %s" % ("MORD" if m2 else "MUET", nom, len(m2), (m2[0][:96] if m2 else "")))
print("alterations : %d ; mordues : %d ; muettes : %d" % (len(ALTERATIONS), len(ALTERATIONS) - muettes, muettes))
print("VERDICT : %s" % ("NOTE CONFORME, CONTROLE MORDANT" if (not mord and muettes == 0) else "A REPRENDRE"))
sys.exit(0 if (not mord and muettes == 0) else 1)
