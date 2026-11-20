# -*- coding: ascii -*-
"""CONSTRUCTION de l'acte du run du gel "pont" -- machine 1, v1, 2026-11-18. Chaque nombre est lu dans une piece.
ASCII, lignes de 100 colonnes au plus, sans signe pour cent.
Usage : python3 -I -B ce_script <sorties du rejeu de machine 1> <dossier du run de machine 2> <gel partie 2.md>
          <chaine_cellules de machine 1.json> <liste des manifestes.json> <liste des pieces.json> <sortie.md>"""
import sys, os, re, json, math, hashlib, unicodedata, textwrap
OUT, RUN, GEL, CHAINE, MANIFS, LISTE, SORTIE = [a.rstrip("/") for a in sys.argv[1:8]]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
L = []
def par(t, r="  ", s=None): L.extend(textwrap.wrap(" ".join(t.split()), width=100, initial_indent=r, subsequent_indent=r if s is None else s,
                                                   break_long_words=False, break_on_hyphens=False))
def brut(*l): L.extend(l)
def titre(t): brut("", t)
NOMS = ("MG3", "MG4", "MG5", "PG3", "PG4", "PG5")
V = json.load(open(OUT + "/verdict.json")); RJ = json.load(open(OUT + "/rejeu_feuilles_run_pont_v1.json")); CH = json.load(open(CHAINE)); X = CH["ecarts"]
LD = {n: json.load(open("%s/lecture_densite_2d_%s.json" % (OUT, n))) for n in NOMS}
LB = json.load(open(OUT + "/lecture_boites.json")); ET = json.load(open(RUN + "/etat_run.json"))
journal = open(RUN + "/run_pont_machine2.log", encoding="utf-8").read()
duree = int(re.search(r"\[\s*(\d+) s\] RUN TERMINE", journal).group(1)); feu = re.search(r"feu vert ecrit : (\S+) (\S+)", journal).groups()
assert len(ET) == 48 and all(v["etat"] == "fait" and v["relances"] == 0 for v in ET.values())
M = {k: canon(v) for k, v in json.load(open(MANIFS)).items()}                       # canons des lots, lus sur leurs manifestes
gel = open(GEL, encoding="ascii").read(); G2 = canon(GEL)
PR = {f: [float(v) for v in re.search(r"^    \(%s\)\s+((?:\d\.\d\d\s+){6})(\d\.\d\d)$" % f, gel, re.M).group(1).split()] for f in ("L", "L2", "S", "C")}
PF = {f: float(re.search(r"^    \(%s\)\s+((?:\d\.\d\d\s+){6})(\d\.\d\d)$" % f, gel, re.M).group(2)) for f in ("L", "L2", "S", "C")}
pieces = json.load(open(LISTE)); cp = [(canon(p), os.path.basename(p), q) for p, q in pieces]
C = V["cellules"]; F = V["familles"]; Q = V["questions"]
def vd(f): return {"TENUE": "TENUE", "TOMBEE": "TOMBEE", "NON JUGEE": "NON JUGEE"}[F[f]["verdict"]]
niv = sum(b["n"] for c in LB["cellules"] for b in c["boites"]); nfi = sum(b["n"] - b["fiables"] for c in LB["cellules"] for b in c["boites"])
nli = sum(b["lisible"] for c in LB["cellules"] for b in c["boites"])
Smin, Smax = min(C[n]["S"]["moyenne"] for n in NOMS), max(C[n]["S"]["moyenne"] for n in NOMS)
Rmin = min(v for n in NOMS for v in C[n]["C"]["compte_reduit"].values()); Rmax = max(v for n in NOMS for v in C[n]["C"]["compte_reduit"].values())
rapmin, rapmax = min(C[n]["C"]["rapport"] for n in NOMS), max(C[n]["C"]["rapport"] for n in NOMS)
pire = {n: C[n]["L"]["pire_ln_R3"] for n in NOMS}
dmg, dpg = CH["cellules"]["MG3"]["delta"], CH["cellules"]["PG3"]["delta"]

brut('DELTA nn -- LE PONT : CE QUE L\'ABSORBEUR LIT, ET LES NIVEAUX DE LA BOITE FERMEE. RUN DU 18/11/2026',
     "SOUS LE GEL EN DEUX PARTIES 735ce41be200c5cd (REGLE DE TIRAGE) ET %s (INSTRUMENT," % G2,
     "ENONCES), RECTIFICATIF D'AVANT RUN 9e25019f3b9bdf04.",
     "VERDICT : (S) %s, (C) %s, (L) %s, (L2) %s." % (vd("S"), vd("C"), vd("L"), vd("L2")),
     "(plume machine 1 ; certifications, run et seconde feuille machine 2)",
     "=" * 71)
titre("nn.0 POSITION")
par("""Ce delta rend le run unique du gel "pont". Sa question : ce que l'absorbeur lit comme une densite, et dont le delta 102 a tire
la largeur du vide, est-il la force que le vide porte reellement sur les niveaux de la boite FERMEE ? Six cellules ont ete tirees par
une graine de l'operateur (456823) : w2 = 397/200 (delta = %+.3f) et w2 = 2019/1000 (delta = %+.3f), chacun a 3, 4 et 5 barreaux de
chaine. Par cellule : la densite 2D du site (0, 0) sous quatre absorbeurs, a douze ecarts de l'energie du vide, et vingt boites
fermees de cotes 180 a 189 et 291 a 300.""" % (dmg, dpg))
par("""(S) et (C) sont TENUES aux six cellules : la somme des parts des niveaux de la boite fermee vaut de %.4f a %.4f par cellule, et
leur nombre croit avec le cote. (L) et (L2) sont TOMBEES aux trois cellules de desaccord negatif : a 8 |delta| du vide, la
chaine d'ordre 3 s'ecarte de la densite 2D de %.4f a %.4f en logarithme, et l'ordre 2 y est plus pres que l'ordre 3. Elles tiennent
aux trois cellules de desaccord positif.""" % (Smin, Smax, min(abs(pire[n]) for n in NOMS[:3]), max(abs(pire[n]) for n in NOMS[:3])))
q3mg = [C[n]["Q3_somme_avec_la_densite_2d"]["moyenne"] for n in NOMS[:3]]
par("""Ce que cela dit. A delta > 0, ou (L) tient, le pont entre l'absorbeur et la boite fermee tient aux tolerances du gel. A delta <
0, joue a l'aveugle, la somme tient avec le lisse de la chaine, mais ce lisse n'est pas, a 5 pour cent pres, la densite que lit
l'absorbeur loin du vide : par les enonces JUGES le pont n'y est pas atteint, comme le gel l'avait ecrit d'avance pour cette issue.
La somme relue avec la densite 2D elle-meme, (Q3), qui n'est pas jugee, y vaut de %.4f a %.4f. Cela ne dit rien de la boite infinie,
de la resonance exacte, ni de la duree de vie du systeme ferme.""" % (min(q3mg), max(q3mg)))

titre("nn.1 CE QUI A ETE JOUE, ET DANS QUEL ORDRE")
for t in (
    """17/11, 00 h 56 : l'operateur ouvre le gel ("Go rediger le gel."). Premiere partie, regle de tirage et d'eligibilite : canon
    735ce41be200c5cd, lot de machine 1 %s. Certifiee par machine 2 (lot %s), avec une reserve de redaction.""" % (M["m1_p1"], M["m2_certif_p1"]),
    """17/11, 09 h 56 : l'operateur donne la graine 456823 aux deux machines. Tirages identiques des deux cotes (lot de machine 2 %s) :
    les deux creneaux au rang 0, MG a w2 = 397/200, PG a w2 = 2019/1000.""" % M["m2_tirage"],
    """17/11 : seconde partie, instrument, enonces, tolerances : canon %s, lot de machine 1 %s. Certifiee par machine 2 sur ses six
    points, lecture par partition acceptee, huit reserves de redaction (lot %s).""" % (G2, M["m1_p2"], M["m2_certif_p2"]),
    """17/11 : rectificatif d'avant run de machine 1 (canon 9e25019f3b9bdf04, lot %s) : une sortie de densite incomplete se rejoue telle
    quelle, une sortie complete jamais ; les huit reserves prises. Machine 2 prend la regle.""" % M["m1_rectificatif"],
    """18/11 : feu vert ECRIT de l'operateur a machine 2. La date y est ; l'heure n'y est pas (nn.9). Machine 2 l'a recu a %s a son
    horloge.""" % feu[1].replace(":", " h "),
    """18/11 : le run, un seul appel du pilote de machine 2 sur BOCAL4 : %d calculs (par cellule quatre densites et quatre lots de
    boites), huit de front, %d s. Aucun calcul relance ; 24 sorties de densite completes sur 24 ; 120 boites sur 120. Puis les trois
    feuilles de machine 1 et celles de machine 2. Lot de machine 2 : %s.""" % (len(ET), duree, M["m2_resultats"]),
    """18/11 : machine 1 rejoue ses trois feuilles sur les sorties de machine 2 (nn.4) et ecrit cet acte."""):
    par("- " + t, r="  ", s="    ")
par("""Avant le run, aucune 2D du systeme a fantome n'a ete calculee aux deux w2 tires, par aucune machine (E19) ; une fois, a w2 =
197/100, machine 1 a execute ses deux sondes a l'aveugle, sans en lire aucun nombre (gel, section 6).""")

titre("nn.2 L'INSTRUMENT")
par("""Celui de la seconde partie du gel, certifie, non modifie : sonde de densite 2D a energie fixee, sonde de boite fermee (poids du
site (0, 0) lu par partition), feuille de densite, feuille des boites, feuille de verdict. Machine 2 a controle apres le run que les
84 pieces du lot de machine 1 utilisees etaient de canon identique au manifeste. La table de la chaine lue par les feuilles est
celle que machine 2 a recalculee sur BOCAL4 ; elle s'accorde a celle de machine 1 a %s pres.""" % ("%.1e" % RJ["table_chaine_ecart_max"]))

titre("nn.3 LE VERDICT DE LA FEUILLE DU RUN")
brut("    cellule  (L)     pire ln R3, a l'ecart x   part de la tolerance   (L2)")
for n in NOMS:
    c = C[n]
    brut("    %-7s  %-6s  %+.4f a x = %-12s %.2f                   %s" % (n, c["L"]["verdict"], c["L"]["pire_ln_R3"], "%g" % c["L"]["pire_ecart"], c["L"]["pire_part_de_tolerance"], c["L2"]["verdict"]))
brut("    cellule  (S)     moyenne de S       (C)     compte reduit, UN   DEUX    rapport des comptes")
for n in NOMS:
    c = C[n]
    brut("    %-7s  %-6s  %.4f +- %.4f   %-6s  %.3f               %.3f   %.3f" % (n, c["S"]["verdict"], c["S"]["moyenne"], c["S"]["erreur"], c["C"]["verdict"],
         c["C"]["compte_reduit"]["UN"], c["C"]["compte_reduit"]["DEUX"], c["C"]["rapport"]))
for f, nom in (("L", "le lisse"), ("L2", "l'ordre"), ("S", "la somme"), ("C", "le compte")):
    brut("    FAMILLE (%s), %s : %s ; cellules lisibles %d sur 6%s" % (f, nom, F[f]["verdict"], len(F[f]["lisibles"]), "" if not F[f]["tombees"] else " ; tombees : " + " ".join(F[f]["tombees"])))
par("""Par creneau, lu sur les lignes par cellule : MG (delta < 0), (L) et (L2) tombent aux trois cellules, (S) et (C) tiennent aux
trois ; PG (delta > 0), les quatre familles tiennent aux trois cellules. La feuille de machine 2, ecrite depuis le texte, rend les
memes 24 jugements.""")
par("""Tout est lisible : douze ecarts sur douze aux six cellules, plus grande etendue entre absorbeurs %.4f ; %d boites lisibles sur
120 ; %d niveaux, %s.""" % (max(LD[n]["etendue_absorbeurs_max"] for n in NOMS), nli, niv, "tous fiables" if nfi == 0 else "dont %d non fiables" % nfi))

titre("nn.4 LE REJEU DE MACHINE 1 (etape 5 du gel)")
cm = RJ["contre_machine2"]
par("""Par rejeu_feuilles_run_pont_machine1_v1.py, sur les fichiers du lot de machine 2. Completude, controlee avant les feuilles : 24
sorties de densite a douze barreaux d'absorbeur, 120 boites, les vingt cotes de chaque cellule une fois chacun, chaque fichier a la
cellule du tirage : %s. Mes trois feuilles rendent les verdicts de nn.3. Contre les sorties que machine 2 a rendues : %d nombres
compares, plus grand ecart %s, aucun desaccord de verdict ni de champ. Refaits avec MA table de la chaine au lieu de la sienne : les
memes 24 jugements et les memes quatre familles.""" % ("aucune faute" if not RJ["completude"]["fautes"] else "%d FAUTES" % len(RJ["completude"]["fautes"]), cm["nombres"], "%.1e" % cm["ecart_max"]))
par("""Mon rectificatif annoncait une comparaison a 1e-12 pres : elle n'est PAS tenue a ce seuil. Les ecarts au-dessus sont sur des
nombres derives et non juges (des parts y, recalculees avec la densite de la chaine sur chaque machine, et l'exces de (Q1) compte
en erreurs). L'annonce etait trop serree ; je le dis au lieu de changer le seuil.""")

titre("nn.5 LECTURE, ENONCE PAR ENONCE")
par("(L) ln R3 = ln [densite 2D / (w0 x lisse d'ordre 3)], aux douze ecarts x (en |delta|) ; tolerance 0.05 :")
brut("    x      " + "  ".join("%-7s" % n for n in NOMS))
for i, x in enumerate(X): brut("    %-5s  " % ("%g" % x) + "  ".join("%+7.4f" % LD[n]["par_x"][i]["ln_R3"] for n in NOMS))
for n in NOMS[:3]:
    r3 = [p["ln_R3"] for p in LD[n]["par_x"]]; assert all(v < 0 for v in r3[3:]) and all(r3[i + 1] < r3[i] for i in range(3, 11))
assert all(abs(LD["MG3"]["par_x"][i]["ln_R3"]) < abs(LD["MG4"]["par_x"][i]["ln_R3"]) < abs(LD["MG5"]["par_x"][i]["ln_R3"]) for i in range(6, 12))
par("""Hors tolerance : %s. Partout ailleurs, et a tous les ecarts des trois cellules PG, la tolerance est tenue. A delta < 0 le
residu est negatif aux trois profondeurs a partir de 1 |delta|, croit avec l'ecart, et avec la profondeur a partir de 3 |delta| ;
jusqu'a 4 |delta| il reste sous %.4f.""" %
    (" ; ".join("%s a x = %s" % (n, " et ".join("%g" % v for v in C[n]["L"]["ecarts_hors_tolerance"])) for n in NOMS if C[n]["L"]["ecarts_hors_tolerance"]),
     max(abs(LD[n]["par_x"][i]["ln_R3"]) for n in NOMS[:3] for i in range(8)) + 5e-5))
par("""MG3 tombe de tres peu : %.5f pour 0.05, a un seul ecart. C'est une chute a la lettre ; l'etendue entre absorbeurs y vaut %.4f,
soit %.0f fois l'ecart a la tolerance.""" % (abs(pire["MG3"]), LD["MG3"]["par_x"][-1]["etendue_absorbeurs"],
    LD["MG3"]["par_x"][-1]["etendue_absorbeurs"] / (abs(pire["MG3"]) - 0.05)))
par("(L2) ln R2, le meme rapport avec le lisse d'ordre 2 :")
brut("    x      " + "  ".join("%-7s" % n for n in NOMS))
for i, x in enumerate(X): brut("    %-5s  " % ("%g" % x) + "  ".join("%+7.4f" % LD[n]["par_x"][i]["ln_R2"] for n in NOMS))
assert all(C[n]["L2"]["ecarts_ou_l_ordre_2_est_plus_pres"] == [5.0, 6.0, 7.0, 8.0] for n in NOMS[:3]) and all(C[n]["L2"]["ecarts_ou_l_ordre_2_est_plus_pres"] == [] for n in NOMS[3:])
assert all(LD[n]["par_x"][i]["ln_R2"] > 0 > LD[n]["par_x"][i]["ln_R3"] for n in NOMS[:3] for i in range(8, 12))
par("""Aux trois cellules MG, l'ordre 2 est plus pres de la 2D que l'ordre 3 aux quatre ecarts juges (5, 6, 7, 8) ; aux trois cellules
PG, l'ordre 3 est plus pres aux quatre. A delta < 0 la 2D est entre l'ordre 2 et l'ordre 3, et plus pres de l'ordre 2 : l'ordre 3
corrige dans le bon sens et trop.""")
par("(S) moyenne de la somme des parts, par cellule et par groupe de cotes ; (C) nombre moyen de niveaux :")
brut("    cellule  S, vingt boites    S, UN    S, DEUX   ecart-type UN / DEUX   n, UN   n, DEUX")
for n in NOMS:
    c = C[n]
    brut("    %-7s  %.4f +- %.4f   %.4f   %.4f    %.3f / %.3f          %.2f   %.2f" % (n, c["S"]["moyenne"], c["S"]["erreur"], c["S"]["moyenne_par_groupe"]["UN"],
         c["S"]["moyenne_par_groupe"]["DEUX"], c["S"]["ecart_type_par_groupe"]["UN"], c["S"]["ecart_type_par_groupe"]["DEUX"], c["C"]["moyenne_par_groupe"]["UN"],
         c["C"]["moyenne_par_groupe"]["DEUX"]))
par("""La somme est dans [0.85, 1.15] aux six cellules et dans [0.80, 1.20] aux douze groupes ; la moyenne de groupe la plus loin de 1
vaut %.4f. Le compte reduit vaut de %.3f a %.3f, pour [0.33, 0.55] ; le rapport des comptes de %.3f a %.3f, pour [1.25, 1.85]. A
delta < 0, ou rien n'avait ete regarde, le compte reduit est celui de delta > 0 : le nombre de niveaux suit bien le cote fois |delta|.""" %
    (max((v for n in NOMS for v in C[n]["S"]["moyenne_par_groupe"].values()), key=lambda v: abs(v - 1.0)), Rmin, Rmax, rapmin, rapmax))

titre("nn.6 CE QUI ETAIT CONSIGNE SANS ETRE JUGE")
par("""(Q1) L'exces. Toutes boites confondues : S = %.4f +- %.4f sur %d boites, soit %+.2f erreur par rapport a 1. L'exces de 4 pour
cent vu au point sacrifie ne se retrouve pas.""" % (Q["Q1"]["moyenne"], Q["Q1"]["erreur"], Q["Q1"]["boites"], Q["Q1"]["exces_en_erreurs"]), r="  ", s="      ")
par("""(Q2) Les parts sont-elles egales. Rapport a la loi de Porter-Thomas : %.3f au groupe UN, %.3f au groupe DEUX (%d boites chacun).
Les parts sont un peu plus egales que cette loi ; aucune erreur n'est attachee a ces deux nombres.""" % (Q["Q2_UN"]["rapport"], Q["Q2_DEUX"]["rapport"], Q["Q2_UN"]["boites"]),
    r="  ", s="      ")
par("(Q3) Le pont sans la chaine : la somme relue avec la densite 2D, et (Q4) le vide, ln (G3* de la chaine / largeur 2D) :", r="  ", s="      ")
brut("    cellule  (Q3) S avec la 2D   (S) S avec la chaine   (Q4) absorbeurs A, B, D       absorbeur C")
for n in NOMS:
    q4 = C[n]["Q4_vide_ln_chaine3_sur_2d"]; abd = [q4[a] for a in "ABD"]
    brut("    %-7s  %.4f              %.4f                 %+.5f a %+.5f       %+.5f" % (n, C[n]["Q3_somme_avec_la_densite_2d"]["moyenne"], C[n]["S"]["moyenne"], min(abd), max(abd), q4["C"]))
par("""Aux trois cellules MG, ou (L) tombe, la somme relue avec la densite 2D vaut de %.4f a %.4f : la boite fermee et l'absorbeur
s'accordent sans passer par la chaine. Au vide meme, la chaine d'ordre 3 rend la largeur 2D a mieux que %.4f aux six cellules (hors
absorbeur C) : la chaine est juste a l'energie du vide et s'en ecarte en s'en eloignant.""" %
    (min(C[n]["Q3_somme_avec_la_densite_2d"]["moyenne"] for n in NOMS[:3]), max(C[n]["Q3_somme_avec_la_densite_2d"]["moyenne"] for n in NOMS[:3]),
     max(abs(C[n]["Q4_vide_ln_chaine3_sur_2d"][a]) for n in NOMS for a in "ABD") + 5e-5))
par("""REGARD APRES LECTURE, hors gel, non juge. A 8 |delta|, la place de la 2D entre l'ordre 2 (0) et l'ordre 3 (1), soit ln R2 / (ln
R2 - ln R3) : %s. A delta > 0 l'ordre 3 fait l'essentiel du chemin, ou reste en deca ; a delta < 0 il va de %.1f a %.1f fois trop
loin. Ce n'est pas explique.""" % ((" ; ".join("%s %.2f" % (n, LD[n]["par_x"][-1]["ln_R2"] / (LD[n]["par_x"][-1]["ln_R2"] - LD[n]["par_x"][-1]["ln_R3"])) for n in NOMS),) +
    (min((LD[n]["par_x"][-1]["ln_R2"] - LD[n]["par_x"][-1]["ln_R3"]) / LD[n]["par_x"][-1]["ln_R2"] for n in NOMS[:3]),
     max((LD[n]["par_x"][-1]["ln_R2"] - LD[n]["par_x"][-1]["ln_R3"]) / LD[n]["par_x"][-1]["ln_R2"] for n in NOMS[:3]))))

titre("nn.7 LES ANNONCES DE LA PLUME, CONFRONTEES AU RUN (gel, section 11)")
brut("    famille  " + "  ".join("%-10s" % n for n in NOMS) + " la famille")
for f in ("L", "L2", "S", "C"):
    brut("    %-7s  " % ("(%s)" % f) + "  ".join("%.2f %-5s" % (p, "tient" if C[n][f]["verdict"] == "TIENT" else "TOMBE") for p, n in zip(PR[f], NOMS)) + " %.2f %s" % (PF[f], F[f]["verdict"]))
rate = [(f, n, p) for f in ("L", "L2", "S", "C") for p, n in zip(PR[f], NOMS) if p != 0.5 and (p > 0.5) != (C[n][f]["verdict"] == "TIENT")]
assert all(n.startswith("MG") and f in ("L", "L2") for f, n, p in rate)
par("""Sur 24 annonces, %d vont contre le run : %s. Toutes sont a delta < 0, toutes sur la chaine. J'annoncais comme issue la plus
probable "(L) qui tombe a MG5, [...] le reste tenant" : MG5 tombe, mais MG3 et MG4 aussi, et (L2) avec elles. J'avais transporte a delta <
0 un residu calibre a delta > 0 ; a 8 |delta| il vaut %.4f, %.4f et %.4f en valeur absolue aux trois cellules MG, contre %.4f, %.4f et
%.4f aux trois cellules PG. Sur (S) et (C), mes annonces etaient plus prudentes que le run.""" %
    ((len(rate), ", ".join("(%s) %s annoncee a %.2f" % r for r in rate)) + tuple(abs(LD[n]["par_x"][-1]["ln_R3"]) for n in NOMS)))
par("""Paris. (Q1) moyenne dans [0.99, 1.05] : %s (%.4f). L'exces se retrouve (annonce a 0.4) : non. (Q2) rapport entre 0.8 et 1.1 dans
chaque groupe : %s (%.3f et %.3f). Une cellule au moins illisible pour (L) (annonce a 0.15) : aucune.""" %
    ("tenu, de peu" if 0.99 <= Q["Q1"]["moyenne"] <= 1.05 else "perdu", Q["Q1"]["moyenne"],
     "tenu" if all(0.8 <= Q[k]["rapport"] <= 1.1 for k in ("Q2_UN", "Q2_DEUX")) else "perdu, de peu", Q["Q2_UN"]["rapport"], Q["Q2_DEUX"]["rapport"]))

titre("nn.8 CE QUE CET ACTE ECRIT, ET CE QU'IL N'ECRIT PAS (gel, section 10)")
par("""Le gel prevoyait cette issue : "(L) TOMBEE, (S) TENUE : la chaine d'ordre 3 ne rend pas la densite hors du vide a 5 pour cent
la ou elle tombe ; le pont entre boite fermee et absorbeur n'est pas atteint, et (Q3) dit ce qu'il vaut sans la chaine." Et : "(L2)
TOMBEE : l'ordre 3 n'ameliore pas l'ordre 2 hors du vide la ou elle tombe".""")
par("""IL ECRIT : aux six cellules, la somme des poids que les niveaux de la boite fermee portent sur le site (0, 0), rapportee au
lisse d'ordre 3 de la chaine, vaut 1 aux tolerances du gel, aux deux groupes de cotes ; le nombre de ces niveaux croit comme le cote
fois |delta| ; cela vaut a delta < 0, joue a l'aveugle, comme a delta > 0. Aux trois cellules de delta > 0, ou (L) tient, c'est le
pont entre la boite fermee et l'absorbeur, aux tolerances dites. A delta < 0, la chaine d'ordre 3 ne rend pas la densite 2D a 5 pour
cent a 7 et 8 |delta| du vide et n'y ameliore pas l'ordre 2 : le pont n'y est pas atteint par les enonces juges.""")
par("""IL N'ECRIT PAS : que le pont tient a delta < 0 au titre d'un enonce juge (seule (Q3), non jugee, l'y montre, de %.4f a %.4f) ;
que la largeur sous absorbeur est le taux de fuite d'un systeme ferme infini (deux groupes de cotes, 300 au
plus) ; une loi en delta (un w2 par signe) ; que la chaine d'ordre 3 est fausse au vide (elle y tient, (Q4) et delta 102) ; pourquoi
l'ordre 3 corrige trop loin du vide a delta < 0 ; rien sur la resonance exacte ni sur des champs.""" % (min(q3mg), max(q3mg)))

tomb1 = []
for n in NOMS:
    pas = CH["cellules"][n]["pas_2_3"]
    if any(abs(p["ln_R3"]) > max(0.02, 0.5 * abs(pas[i])) for i, p in enumerate(LD[n]["par_x"])): tomb1.append(n)
assert tomb1 == F["L"]["tombees"]
phrase = "les cellules %s tombent, les memes" % " ".join(tomb1)
titre("nn.9 CORRECTIONS DE MACHINE 2, DEFAUTS DE LA PLUME, ECARTS")
for t in (
    """Reserve R1 de machine 2 sur la premiere partie : le 4.4 disait la largeur lue sur la valeur propre sans dire que la double
    precision n'y suffit pas a 4 et 5 barreaux. Faute de la plume, rectifiee en section 3 de la seconde partie ; aucune decision ne
    change.""",
    """Seconde partie, declares avant le run : une heure fausse dans mon attendu de qualification ; une clause de cet attendu que je
    n'ai pas suivie (la lecture brute des poids en cas de chute de B3), acceptee par machine 2 ; une lecture des poids neuve, par
    partition, acceptee par machine 2 et jamais verifiee en precision etendue ; un attendu tombe (U1) qui a change la lecture de (C).""",
    """Tolerance de (L), desserree pendant la redaction, apres la calibration au point sacrifie et avant toute cellule : de max(0.02,
    la moitie du pas de l'ordre 2 a l'ordre 3) a 0.05 partout. Avec la premiere, calculee ici sur le run : %s. Le desserrement n'a
    sauve aucune cellule tombee.""" % phrase,
    """Fait trouve par machine 2 a sa certification : ma feuille de densite accepte une sortie interrompue ; et mon 5.6 interdisait, a
    la lettre, de rejouer une densite coupee. Rectificatif d'avant run, pris par machine 2. Ni cette regle ni celle des cotes
    manquants n'ont servi : rien n'a ete coupe.""",
    """Le feu vert. L'operateur l'a ecrit avec sa date ; l'heure etait laissee a completer dans la formule que machine 1 lui avait
    proposee, et elle est partie telle quelle. Machine 2 a porte au journal son heure de reception (%s) : ce n'est pas une heure
    attestee par l'operateur. Le feu vert, lui, est ecrit et anterieur au run.""" % feu[1].replace(":", " h "),
    """Le seuil de 1e-12 annonce pour mon rejeu n'est pas tenu (nn.4).""",
    """De machine 2, dits par elle : une premiere passe de son script de comparaison repliait les boites de deux cellules de meme
    profondeur (gardee, non corrigee en place) ; la memoire du run n'a pas ete mesuree."""):
    par("- " + t, r="  ", s="    ")

titre("nn.10 LIMITES")
for t in (
    """Les tolerances sont de la plume. MG3 tombe pour %.5f de trop sur 0.05 : avec une tolerance a peine plus large elle tenait, et
    MG4, MG5 tombaient quand meme.""" % (abs(pire["MG3"]) - 0.05),
    """(S) est jugee avec le lisse de la chaine, que (L) montre faux de %.4f a %.4f en logarithme a 8 |delta| a delta < 0 ; la somme
    n'en bouge que de %.4f a %.4f, et (Q3) la donne sans la chaine. (Q3) n'est pas jugee.""" %
    (min(abs(pire[n]) for n in NOMS[:3]), max(abs(pire[n]) for n in NOMS[:3]),
     min(C[n]["Q3_somme_avec_la_densite_2d"]["moyenne"] - C[n]["S"]["moyenne"] for n in NOMS[:3]),
     max(C[n]["Q3_somme_avec_la_densite_2d"]["moyenne"] - C[n]["S"]["moyenne"] for n in NOMS[:3])),
    """La lecture par partition est jugee sur sa stabilite (decalage, rayon, forme de la coupure, deux ecritures, deux machines), pas
    sur une valeur de reference exacte.""",
    """Deux groupes de cotes, 300 au plus ; un w2 par signe du desaccord ; PG est presque le point sacrifie.""",
    """Le moteur et les blocs sont les memes pour la chaine et la 2D, et pour les deux machines. Une seule definition du hamiltonien
    effectif.""",
    """Les deux feuilles ont ete ecrites separement, mais lisent les memes sorties de sondes : les sondes de machine 1 n'ont pas de
    seconde ecriture complete (machine 2 a refait la partition et compare les matrices)."""):
    par("- " + t, r="  ", s="    ")

titre("nn.11 SUITE")
par("""Contreseing de machine 2 ; depot sur l'ordre de l'operateur (prochain numero libre au registre : 103). Rien n'est ouvert par cet
acte. Ce qu'il laisse sans reponse : pourquoi l'ordre 3 corrige trop loin du vide a delta < 0 alors qu'il est juste au vide.""")

titre("nn.12 PIECES (convention B)")
dernier = None
for c, n, q in cp:
    if q != dernier: brut("  %s :" % q); dernier = q
    brut("    %s  %s" % (c, n))
brut("", "-- FIN journal_delta_nn_pont_v1 --")
txt = "\n".join(l.rstrip() for l in L) + "\n"; txt.encode("ascii")
trop = [l for l in L if len(l) > 100]; assert not trop, trop
assert "%" not in txt
open(SORTIE, "w", encoding="ascii", newline="\n").write(txt); print("ecrit : %s ; %d lignes ; canon %s" % (SORTIE, len(L), canon(SORTIE)))
