# -*- coding: ascii -*-
# CONSTRUCTION DU v2 DE L'ACTE DE LA QUALIFICATION E-B (PB-1 : rien de ce qui
# est cite n'est edite). Le script d'ecriture v2 et le releve v2 sont les v1
# (canons affirmes) + des remplacements a ANCRE UNIQUE, nommes par le hunk de
# l'acte qu'ils servent (H1 a H7 ; H0 = noms et version). Un ancre absent ou
# double arrete tout. Les diffs se font ailleurs (fabrique du lot).
# Arguments : <ecriture v1> <releve v1> <dossier de sortie> <journal>
import sys, os, hashlib

E1, R1, SORTIE, JOURNAL = sys.argv[1:5]
F = open(JOURNAL, "w", encoding="ascii", newline="\n")


def dire(s):
    print(s)
    F.write(s + "\n")


def canon(t):
    return hashlib.sha256(t.encode("ascii")).hexdigest()[:16]


def appliquer(texte, hunks, nom):
    for h, vieux, neuf in hunks:
        n = texte.count(vieux)
        assert n == 1, "%s %s : ancre trouve %d fois : %r" % (nom, h, n, vieux[:60])
        assert vieux != neuf
        texte = texte.replace(vieux, neuf)
        dire("  %-4s %s : %4d -> %4d caracteres ; ancre %r" % (h, nom, len(vieux), len(neuf), vieux.split("\n")[0][:50]))
    return texte


# ====================================================================== LE SCRIPT D'ECRITURE
E = [
("H0", r'''# ECRIT L'ACTE DE LA QUALIFICATION E-B (journal_delta_nn_qualification_EB_v1.md).''',
       r'''# ECRIT L'ACTE DE LA QUALIFICATION E-B (journal_delta_nn_qualification_EB_v2.md).
# v2 = ecrire_acte_qualification_EB_machine1_v1.py (1a9eae79842936ee) + les hunks de
# construction_acte_v2_machine1_v1.py, apres le contreseing de machine 2 sur le v1.'''),

("H6", r'''    ("lot_nuit", RECU + "/recu_nuit1/MANIFEST_lot_machine2_resultat_etage1_nuit_EB_v1.txt", "72f65ad8a898fbb5"),
]''',
       r'''    ("lot_nuit", RECU + "/recu_nuit1/MANIFEST_lot_machine2_resultat_etage1_nuit_EB_v1.txt", "72f65ad8a898fbb5"),
    # le v1 de cet acte, son contreseing, et le contreseing du 93 (au registre)
    ("acte_v1", RECU + "/acte/journal_delta_nn_qualification_EB_v1.md", "0d7870ebad535303"),
    ("lot_acte_v1", RECU + "/acte/lot/MANIFEST_lot_machine1_acte_qualification_EB_v1.txt", "089c2c57b42dd4a0"),
    ("lot_cs", RECU + "/recu_contreseing/lot/MANIFEST_lot_machine2_contreseing_acte_nn_EB_v1.txt", "33fa99640756efba"),
    ("n_m2_cs", RECU + "/recu_contreseing/lot/POUR_MACHINE1_contreseing_acte_qualification_EB_machine2_v1.md", "850767f40a770f1b"),
    ("cs93", REG + "/journal/POUR_MACHINE1_contreseing_acte_delta93_machine2_v1.md", "ec04b9e5dddee5f3"),
]'''),

("H3", r'''for d, _, fs in os.walk(RECU + "/recu_nuit1"):          # la detention de 7b64... n'est attestee nulle part
    for f in fs:
        assert b"7b64b1b7d86c0591" not in open(os.path.join(d, f), "rb").read()
''',
       r'''

# ---------------------------------------------------------------- les regles candidates sous (X), RELEVEES AU REGISTRE
def numeros(chemin, debut, fin):
    sec = open(chemin, encoding="utf-8").read().split(debut, 1)[1].split(fin, 1)[0]
    return [int(x) for x in re.findall(r"(?m)^  (\d{1,2})[. ] ", sec)]


JR = REG + "/journal/"
XR = [("du 90", numeros(JR + "journal_delta_90_constante_A_v2.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 ")),
      ("du 91", numeros(JR + "journal_delta_91_constante_A_run_v2.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 ")),
      ("du 92", numeros(JR + "journal_delta_92_constante_A_second_ordre_v1.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 ")),
      ("de l'acte 93", numeros(JR + "journal_delta_93_constante_A_mesure_v2.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 ")),
      ("du contreseing du 93 par machine 2",
       numeros(JR + "POUR_MACHINE1_contreseing_acte_delta93_machine2_v1.md", "## 6. VERSE SOUS (X)", "## 7."))]
assert [n for _, l in XR for n in l] == list(range(1, 22)), XR
NOMBRE = {3: "trois", 4: "quatre", 8: "huit", 21: "vingt et une", 25: "vingt-cinq"}
n_prec = sum(len(l) for _, l in XR)
V["x_prec"] = NOMBRE[n_prec]
V["x_detail"] = ", ".join("%s %s" % (NOMBRE[len(l)], d) for d, l in XR)
V["x1"], V["x2"], V["x3"], V["x4"] = ["%d" % (n_prec + i) for i in (1, 2, 3, 4)]
V["x_total"] = NOMBRE[n_prec + 4]
assert "Les treize precedentes (huit du 90, quatre du 91, une du 92)" in plat(
    JR + "journal_delta_93_constante_A_mesure_v2.md")
assert "vingt et une candidates" in plat(JR + "POUR_MACHINE1_contreseing_acte_delta93_machine2_v1.md")
CS = plat(RECU + "/recu_contreseing/lot/POUR_MACHINE1_contreseing_acte_qualification_EB_machine2_v1.md")
for ph in ("28 controles, 3 morsures", "25 controles, 2 morsures", "C06 et C19",
           "OUI, je detiens ta certification de ma reference (lot 7b64b1b7d86c0591",
           "JE CONTRESIGNE LES NOMBRES ET LA STRUCTURE ; JE NE CONTRESIGNE PAS LE TEXTE EN L'ETAT",
           "on s'en fiche pour l'instant"):
    assert ph in CS, ph
assert "Un seul tour de correction est admis (section 12)" in plat(W + "/qualification_EB_pre_enregistrement_v2.md")
'''),

("H4", r'''        k3.append(rel[3])''',
       r'''        k3.append(rel[3])
        V["k3_%s_%s" % (cle, g)] = "%.3f" % rel[3]'''),

("H0", r'''depot operateur, 2026-11-12) -- PROJET, VERSION 1",''',
       r'''depot operateur, 2026-11-12) -- PROJET, VERSION 2",'''),

("H0", r'''P("""S'insere apres le delta 93 (2ec6775,''',
       r'''P("""v2 = v1 ({c_acte_v1}, lot {c_lot_acte_v1} ; REMPLACEE, non editee) apres le contreseing de
machine 2 (lot {c_lot_cs}, note {c_n_m2_cs}) : nombres et structure contresignes, 28 controles, 3
morsures de description, texte non contresigne en l'etat, v2 demande. Hunks : H1 (nn.9, les quatre
candidates portent {x1} a {x4} : E-nn-1) ; H2 (nn.10 (ii), {x_total} candidates : E-nn-2) ; H3
(nn.9, les {x_prec} precedentes et leur decompte, releves au registre : E-nn-3) ; H4 (nn.6 (e) et
nn.13, ce que l'acte dit a G20 et k = 3 : R-1, pris et amende) ; H5 (nn.10 (iv), la question du
garde-fou laissee de cote : R-2, pris) ; H6 (nn.1, detention declaree par machine 2 ; pieces du v1
et de son contreseing citees) ; H7 (nn.8, nn.12, nn.14 : defauts du v1 verses, canal et pieces a
jour). Aucun nombre mesure ne change.""", ind=0)
P("""S'insere apres le delta 93 (2ec6775,'''),

("H0", r'''ecrire_acte_qualification_EB_machine1_v1.py depuis les pieces de nn.1''',
       r'''ecrire_acte_qualification_EB_machine1_v2.py depuis les pieces de nn.1'''),

("H6", r'''PIECE("journal/manche_m17_v17_MANIFEST_machine2.txt", "c_man_run",
      "manifeste du run M17, 36 lignes ; des 36 pieces, seul l'assemblage est au registre")''',
       r'''PIECE("journal/manche_m17_v17_MANIFEST_machine2.txt", "c_man_run",
      "manifeste du run M17, 36 lignes ; des 36 pieces, seul l'assemblage est au registre")
PIECE("journal/POUR_MACHINE1_contreseing_acte_delta93_machine2_v1.md", "c_cs93",
      "le contreseing du 93 par machine 2 : il verse sous (X) les candidates 19, 20 et 21 (nn.9)")'''),

("H6", r'''P("""Detention. Tout ce qui precede est detenu par les deux machines a la date de l'acte, par les
lots echanges (nn.12), sauf : les 279 fichiers de reprise de la nuit, a machine 2 seule, leur
contenu utile etant consolide dans sonde_etage1.json ; et la certification de la reference par
machine 1 (lot {c_lot_cert_ref}), transmise par l'operateur, dont aucune piece de machine 2 ne
porte encore le canon -- au contresignataire de dire s'il la detient. Le run M17''',
       r'''T("  Le v1 de cet acte et son contreseing :")
PIECE("journal_delta_nn_qualification_EB_v1.md", "c_acte_v1",
      "machine 1, lot {c_lot_acte_v1} ; REMPLACE par ce v2, non edite")
PIECE("POUR_MACHINE1_contreseing_acte_qualification_EB_machine2_v1.md", "c_n_m2_cs",
      """machine 2, lot {c_lot_cs} : nombres et structure contresignes, texte non contresigne en
      l'etat ; 28 controles, 3 morsures (E-nn-1 a E-nn-3), une precision (R-1), une remarque (R-2)""")
P("""Detention. Tout ce qui precede est detenu par les deux machines a la date de l'acte, par les
lots echanges (nn.12), sauf les 279 fichiers de reprise de la nuit, a machine 2 seule, leur
contenu utile etant consolide dans sonde_etage1.json. La certification de la reference par
machine 1 (lot {c_lot_cert_ref}) est detenue par machine 2, recue de l'operateur et identique a
l'octet a la livraison : elle le declare a son contreseing du v1. Le run M17'''),

("H4", r'''douze plus faibles. L'acte ne dit donc pas que l'instrument est faux a G20 ; il dit que le banc,
tel que gele, ne pouvait pas le montrer juste. C'est le defaut D-QEB-2 de nn.8.""", ind=2, suite=6)''',
       r'''douze plus faibles. L'acte ne dit donc pas si le palier de G20 se prolonge du cote fort ; il dit
que le banc, tel que gele, ne pouvait pas le montrer. C'est le defaut D-QEB-2 de nn.8. Ce que
D-QEB-2 n'explique pas, et que l'acte dit sans reserve (R-1 de machine 2) : a G20 et k = 3, le
reglage de lecture de M17, la largeur rendue au temoin vaut {k3_j06_G20} et {k3_j08_G20} fois la
largeur connue (c), et la porte de descente de M17 y refuse le point (d).""", ind=2, suite=6)'''),

("H7", r'''P("""Retraits : aucun. E19 : nn.4.""", ind=2, suite=4)''',
       r'''P("""E-nn-1, E-nn-2, E-nn-3 (m1, v1 de cet acte ; trouves par m2, lot {c_lot_cs}). Les quatre
candidates du v1 portaient 19 a 22, alors que 19, 20 et 21 sont versees au contreseing du 93 (note
{c_cs93}, au registre) ; le compte de la revue disait vingt-deux ; la parenthese des precedentes
annoncait dix-huit et sommait a seize. Cause : machine 1 a repris la parenthese du 93 sans la
recompter et n'a pas relu le contreseing du 93. Corriges ici ; les numeros et les comptes sont
desormais releves au registre par le script d'ecriture, et le releve porte un controle de plus.""",
  ind=2, suite=4)
P("""Herite du delta 93, depose et non touche : sa parenthese "treize precedentes (huit du 90,
quatre du 91, une du 92)" est fausse -- le 92 en porte trois (13, 14, 15) et les precedentes
etaient quinze. De plume m1, contresignee par m2 ; a numeroter au depot si l'operateur le veut.""",
  ind=2, suite=4)
P("""R-1 et R-2 (m2, contreseing du v1). R-1, pris et amende : nn.6 (e) et nn.13 disent ce que
l'acte affirme a G20 et k = 3, avec le refus de la porte de M17, que la phrase proposee ne portait
pas. R-2, pris : nn.10 (iv).""", ind=2, suite=4)
P("""De m2, sur son script de verification du v1 : premier passage a 25 controles et 2 morsures
(C06, C19), qui etaient des defauts du script -- recherche dans le texte brut de deux phrases que
l'acte coupe par un retour a la ligne ; corrige aux blancs normalises, premier jet conserve.""",
  ind=2, suite=4)
P("""Retraits : aucun. E19 : nn.4 ; rien n'a ete calcule entre le v1 et le v2.""", ind=2, suite=4)'''),

("H1", r'''P("""19  (m1, d'apres D-QEB-2)''', r'''P("""{x1}  (m1, d'apres D-QEB-2)'''),
("H1", r'''P("""20  (m1, d'apres D-QEB-1)''', r'''P("""{x2}  (m1, d'apres D-QEB-1)'''),
("H1", r'''P("""21  (m1, d'apres D-1 et D-2 de m2)''', r'''P("""{x3}  (m1, d'apres D-1 et D-2 de m2)'''),
("H1", r'''P("""22  (m1, d'apres D-3 de m2)''', r'''P("""{x4}  (m1, d'apres D-3 de m2)'''),

("H3", r'''P("""Les dix-huit precedentes (huit du 90, quatre du 91, une du 92, trois du 93) attendent la meme
revue.""")''',
       r'''P("""Les {x_prec} precedentes ({x_detail}) attendent la meme revue.""")'''),

("H2", r'''P("""(ii)  la revue (X), echue : vingt-deux candidates ;""", ind=2, suite=6)''',
       r'''P("""(ii)  la revue (X), echue : {x_total} candidates ;""", ind=2, suite=6)'''),

("H5", r'''P("""(iv)  la suite de la piste (0). Le garde-fou du gel etait propose sous le veto de l'operateur ;
aucun veto n'a ete pose ; l'acte l'applique a ce gel : pas de v3, pas de second run sous lui,
aucun rejeu sous d'autres seuils. Une reprise''',
       r'''P("""(iv)  la suite de la piste (0). Le garde-fou du gel etait propose sous le veto de l'operateur ;
l'operateur a laisse la question de cote -- a machine 2 le 11/11, selon sa declaration, a machine
1 avant le run -- et n'a pas pose de veto : il ne l'a pas tranchee non plus. L'acte n'en tire que
ce que le gel dit deja a sa section 0, un seul tour de correction : sous ce gel, pas de v3, pas
de second run, aucun rejeu sous d'autres seuils. Une reprise'''),

("H7", r'''{c_lot_sonde2} ; certification de la reference {c_lot_cert_ref}. Machine 2 -- certification du gel''',
       r'''{c_lot_sonde2} ; certification de la reference {c_lot_cert_ref} ; cet acte en v1
{c_lot_acte_v1}. Machine 2 -- certification du gel'''),

("H7", r'''sonde v2 {c_lot_cert_sonde2} ; reference du temoin {c_lot_ref} ; resultat de la nuit
{c_lot_nuit}. Deux lots''',
       r'''sonde v2 {c_lot_cert_sonde2} ; reference du temoin {c_lot_ref} ; resultat de la nuit
{c_lot_nuit} ; contreseing du v1 de cet acte {c_lot_cs}. Deux lots'''),

("H4", r'''Il ne dit pas que
l'instrument est faux a G20 ; il ne dit pas qu'il y est juste. Il ne rejoue''',
       r'''Il dit que, sur le temoin et au
reglage de lecture de M17 (G20, k = 3), la largeur rendue par l'absorbeur vaut {k3_j06_G20} et
{k3_j08_G20} fois la largeur connue, et que la porte de descente de M17 y refuse le point ; il ne
dit pas ce que l'instrument lit sur le fantome, ni si le palier de G20 se prolonge du cote fort.
Il ne rejoue'''),

("H7", r'''  "  journal_delta_nn_qualification_EB_v1.md              cet acte",
  "  ecrire_acte_qualification_EB_machine1_v1.py          le script qui pose nombres et canons",
  "  rejeu_ponctuel_TP_machine1_v1.py / .log              six decompositions du temoin, non opposable",
  "  releve_acte_qualification_EB_machine1_v1.py / .log   controle de sortie, pas un contreseing",
  "  note_machine1_acte_qualification_EB_v1.md            la note d'accompagnement",
  "  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.",
  "", "-- FIN journal_delta_nn_qualification_EB_v1 --")''',
       r'''  "  journal_delta_nn_qualification_EB_v2.md              cet acte",
  "  ecrire_acte_qualification_EB_machine1_v2.py          le script qui pose nombres et canons",
  "  construction_acte_v2_machine1_v1.py / .log           v1 -> v2 par remplacements a ancre unique",
  "  diff_acte_qualification_EB_v1_v2.txt                 ce qui change dans l'acte",
  "  diff_ecrire_acte_v1_v2.txt, diff_releve_acte_v1_v2.txt",
  "  releve_acte_qualification_EB_machine1_v2.py / .log   controle de sortie, pas un contreseing",
  "  releve_acte_v2_sur_acte_v1_machine1.log              contre-epreuve : C09 mord sur le v1",
  "  rejeu_ponctuel_TP_machine1_v1.py / .log              inchanges : six decompositions, non opposable",
  "  note_machine1_acte_qualification_EB_v2.md            la note d'accompagnement",
  "  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.",
  "", "-- FIN journal_delta_nn_qualification_EB_v2 --")'''),
]

# ====================================================================== LE RELEVE
R = [
("H0", r'''# RELEVE DE L'ACTE journal_delta_nn_qualification_EB_v1.md PAR SA PLUME (machine 1).''',
       r'''# RELEVE DE L'ACTE journal_delta_nn_qualification_EB_v2.md PAR SA PLUME (machine 1).
# v2 = releve_acte_qualification_EB_machine1_v1.py (52e62eefe85e7d1a) + les hunks de
# construction_acte_v2_machine1_v1.py : le nom du v2, et C09, le controle qui manquait.'''),

("H0", r'''txt.endswith("-- FIN journal_delta_nn_qualification_EB_v1 --\n")''',
       r'''txt.endswith("-- FIN journal_delta_nn_qualification_EB_v2 --\n")'''),

("H7", r'''dire("BILAN : %d controles, %d morsure(s)" % (len(BILAN), BILAN.count(False)))
dire("-- FIN releve_acte_qualification_EB_machine1_v1 --")''',
       r'''

# C09 -- numeros et comptes des regles candidates sous (X), releves au registre (E-nn-1 a E-nn-3)
def regles(nom, debut, fin):
    t = open(os.path.join(reg, "journal", nom), encoding="utf-8").read()
    return [int(x) for x in re.findall(r"(?m)^  (\d{1,2})[. ] ", t.split(debut, 1)[1].split(fin, 1)[0])]


anc = [regles(nom, "\nnn.8 REGLES CANDIDATES", "\nnn.9 ") for nom in (
    "journal_delta_90_constante_A_v2.md", "journal_delta_91_constante_A_run_v2.md",
    "journal_delta_92_constante_A_second_ordre_v1.md", "journal_delta_93_constante_A_mesure_v2.md")]
anc.append(regles("POUR_MACHINE1_contreseing_acte_delta93_machine2_v1.md", "## 6. VERSE SOUS (X)", "## 7."))
deja = [x for l in anc for x in l]
neufs = [int(x) for x in re.findall(r"(?m)^  (\d{2}) \(m1", txt.split("\nnn.9 REGLES CANDIDATES", 1)[1].split("\nnn.10 ", 1)[0])]
MOTS = {"une": 1, "deux": 2, "trois": 3, "quatre": 4, "six": 6, "huit": 8, "dix-huit": 18, "vingt et une": 21,
        "vingt-deux": 22, "vingt-cinq": 25}
aplat = " ".join(txt.split())
par = re.search(r"Les ([a-z -]+?) precedentes \(([^)]*)\)", aplat)
somme = sum(MOTS[w] for w in re.findall(r"\b(huit|quatre|une|trois|deux|six)\b", par.group(2)))
dit = re.search(r"la revue \(X\), echue : ([a-z-]+) candidates", aplat).group(1)
ok = (deja == list(range(1, len(deja) + 1)) and neufs == list(range(len(deja) + 1, len(deja) + 1 + len(neufs)))
      and MOTS[par.group(1)] == somme == len(deja) and MOTS[dit] == len(deja) + len(neufs))
controle("C09", ok, "regles (X) : %d au registre (par piece %s) ; l'acte numerote %s, annonce '%s precedentes' pour une"
         " parenthese qui somme a %d, et '%s candidates'" % (len(deja), [len(l) for l in anc], neufs, par.group(1), somme, dit))

dire("BILAN : %d controles, %d morsure(s)" % (len(BILAN), BILAN.count(False)))
dire("-- FIN releve_acte_qualification_EB_machine1_v2 --")'''),
]

e1 = open(E1, encoding="ascii").read()
r1 = open(R1, encoding="ascii").read()
assert canon(e1) == "1a9eae79842936ee", canon(e1)
assert canon(r1) == "52e62eefe85e7d1a", canon(r1)
dire("entrants : ecriture v1 %s ; releve v1 %s" % (canon(e1), canon(r1)))
e2 = appliquer(e1, E, "ecriture")
r2 = appliquer(r1, R, "releve")
for nom, t in (("ecrire_acte_qualification_EB_machine1_v2.py", e2), ("releve_acte_qualification_EB_machine1_v2.py", r2)):
    compile(t, nom, "exec")
    open(os.path.join(SORTIE, nom), "w", encoding="ascii", newline="\n").write(t)
    dire("ecrit : %s, canon %s, %d o" % (nom, canon(t), len(t)))
compte = {}
for h, _, _ in E + R:
    compte[h] = compte.get(h, 0) + 1
dire("remplacements : %d sur l'ecriture, %d sur le releve ; par hunk de l'acte : %s" % (
    len(E), len(R), ", ".join("%s %d" % (h, compte[h]) for h in sorted(compte))))
assert (len(E), len(R)) == (22, 3)
dire("-- FIN construction_acte_v2_machine1_v1 --")
