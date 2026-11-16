# -*- coding: ascii -*-
"""CONSTRUCTION DE LA PREMIERE PARTIE DU GEL "LOI DE LA LARGEUR, ORDRE 3" : LA REGLE DE TIRAGE ET D'ELIGIBILITE,
et de son POUR_MACHINE2 -- machine 1, v1, 2026-11-15. Chaque nombre est calcule ici depuis les sorties du lot.
Usage : python3 -I construction_regle_tirage_machine1_v1.py <dossier des sorties> <clone du registre> <bloc ordre 3>
        <note sur la carte> <manifeste du lot de la carte> <manifeste de la reponse de machine 2 a la carte> <sortie.md>"""
import sys, os, json, hashlib, unicodedata, textwrap
from fractions import Fraction as F
D, CLONE, BLOC3, NOTE_CARTE, MAN_CARTE, MAN_REP, SORTIE = sys.argv[1:8]

def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

c = {"moteur": B(CLONE + "/scripts/m17_chaine_v17.py"), "bloc2": B(CLONE + "/scripts/chaine_ordre2_bloc_machine1_v1.py"), "depot": B(CLONE + "/journal/sonde_ordre2.json"),
     "gel98": B(CLONE + "/gels/gel_ordre2_chaine_EA_pre_enregistrement_v1.md"), "bloc3": B(BLOC3), "note_carte": B(NOTE_CARTE), "lot_carte": B(MAN_CARTE), "rep": B(MAN_REP)}
assert (c["moteur"], c["bloc2"], c["depot"], c["bloc3"], c["note_carte"], c["lot_carte"], c["rep"]) == (
    "82a0be882568fe0c", "7cd5977bc27bebc1", "10887c60d5f55bcf", "534ba246aa3b8973", "1f6cfb5f9472b1b4", "1e8413aed149429f", "548fb2ba8793ecfe")
PIECES = ["eligibilite_creneaux_machine1_v1.py", "retouches_eligibilite_creneaux_machine1_v1.diff", "eligibilite_N_BN_BP_v1.log", "eligibilite_N_BN_BP_v1.json",
          "eligibilite_P_v1.log", "eligibilite_P_v1.json", "lecture_eligibilite_machine1_v1.py", "lecture_eligibilite_machine1_v1.log", "eligibilite_candidates_v1.json",
          "tirage_machine1_v1.py", "tirage_machine1_v1_autotest.log"]
cp = {p: B(os.path.join(D, p)) for p in PIECES}
T = json.load(open(os.path.join(D, "eligibilite_candidates_v1.json"))); RG = T["reglage"]
assert (RG["plancher10"], RG["e_max"], RG["stab_max"], RG["n_etats"], RG["N_cout"], RG["jug_min"], RG["dom_min"], RG["bord_min"]) == (1.33e-12, 0.7, 0.05, 14, 74, 8, 5, 2)
ORDRE = ("N", "P", "BN", "BP")
cel = {}
for r in T["cellules"]:
    cel.setdefault(r["creneau"], {}).setdefault(r["w2"], []).append(r)
ncel = len(T["cellules"]); nw = sum(T["creneaux"][s]["n"] for s in ORDRE); assert (ncel, nw) == (152, 44)
nel = {s: T["creneaux"][s]["n_eligibles"] for s in ORDRE}; ncand = {s: T["creneaux"][s]["n"] for s in ORDRE}
auto = open(os.path.join(D, "tirage_machine1_v1_autotest.log"), encoding="ascii").read(); assert "AUTOTEST : TIENT" in auto
ex = [l for l in auto.split("\n") if l.startswith('sha256("DEMONSTRATION|N|0")')][0]

L = []
def T_(s=""): L.append(s)
def P(s, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))

T_('GEL "LOI DE LA LARGEUR, ORDRE 3" -- PREMIERE PARTIE : LA REGLE DE TIRAGE ET D\'ELIGIBILITE DES POINTS')
T_("PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-15.")
T_("A CERTIFIER PAR MACHINE 2 AVANT QUE L'OPERATEUR DONNE LA GRAINE.")
T_()
T_("0. STATUT")
P("""Cette piece fixe COMMENT les douze points du gel seront tires et QUAND un tirage est admis. Elle ne fixe ni les enonces juges, ni les
tolerances, ni les probabilites, ni l'instrument : c'est la seconde partie, ecrite apres le tirage sur les chaines seules, et certifiee
avant tout run.""")
P("""Ouverture, selon machine 1 : l'operateur a relaye (15/11/2026, 22 h 41) la phrase de machine 2 "C'est note: vous retenez la section 5 et
vous lancez le gel." (accent retire ici), puis a ecrit "Reprends" (22 h 42). Machine 1 le lit comme le "go" du gel. A l'operateur de
l'attester ou de le dementir.""")
P("""E19. Aucun calcul 2D, dense ou creux, n'a ete fait ni ne sera fait par aucune des deux machines a un w2 candidat, avant la certification
croisee de la seconde partie. Tout ce que cette piece calcule est une chaine a une dimension.""")
T_()
T_("1. SOURCES (convention B)")
for nom, k in (("scripts/m17_chaine_v17.py (registre 8d54bf9), le moteur", "moteur"), ("scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2", "bloc2"),
               ("ordre3_bloc_machine1_v1.py (lot e93f1898dcd78a8f), le bloc d'ordre 3, rederive par machine 2 (lot 889fe9b4c1c1c60a)", "bloc3"),
               ("gels/gel_ordre2_chaine_EA_pre_enregistrement_v1.md (registre), section 3 : la regle du point", "gel98"),
               ("note_machine1_carte_gel_loi_2026-11-15_v1.md (lot %s), section 5 : la proposition" % c["lot_carte"], "note_carte"),
               ("lot de la reponse de machine 2 a la carte, sections 3 et 4 : la regle de tirage reprise ici", "rep")):
    P("%s  %s" % (c[k], nom), 4, 22)
T_()
T_("2. LES CRENEAUX")
P("""Quatre creneaux. Les w2 candidats sont au millieme ; les centiemes en sont exclus : aucun w2 candidat n'a ete joue, a aucun facteur.""")
T_("    N   delta dans ]-0.070, -0.060[  w2 = 1.931 a 1.939                    9 valeurs  cinq facteurs")
T_("    P   delta dans ]+0.030, +0.050[  w2 = 2.031 a 2.039 et 2.041 a 2.049  18 valeurs  cinq facteurs")
T_("    BN  delta dans ]-0.085, -0.075[  w2 = 1.916 a 1.919 et 1.921 a 1.924   8 valeurs  facteur 1")
T_("    BP  delta dans ]+0.060, +0.070[  w2 = 2.061 a 2.069                    9 valeurs  facteur 1")
T_("    Les cinq facteurs de N et de P : 3/4, 5/6, 1, 6/5, 4/3.")
P("""Une CELLULE est un couple (w2, facteur) ; son couplage est g = facteur x g_du_point(w2), par la fonction du moteur. Un tirage donne
un w2 par creneau, donc douze cellules : N1 a N5 et P1 a P5 (facteurs croissants), BN, BP. Les fenetres de BN et BP sont celles que
machine 2 a lues dans "vers -0.08" et "vers +0.065" ; machine 1 les confirme.""")
T_()
T_("3. LE TIRAGE")
P("""Le w2 du creneau s au rang r est l'element de numero""")
T_('        int( sha256("<graine>|<s>|<r>") ecrit en hexadecimal, 16 )  modulo  n_s')
P("""de la liste CROISSANTE des n_s w2 candidats du creneau, numerotee a partir de 0. La chaine hachee est codee en ASCII ; s vaut N, P, BN
ou BP ; r s'ecrit en decimal, sans zero devant ; la barre verticale est le caractere 124.""")
P("""LA GRAINE est une suite de chiffres (0 a 9), d'au moins six chiffres, donnee par L'OPERATEUR, par ecrit, aux deux machines, APRES la
certification de cette piece et apres que la table commune de la section 5 existe. Elle est reportee telle quelle, zeros de tete compris,
dans la seconde partie. Ni machine 1 ni machine 2 ne la choisit, ne la propose, ni ne la commente avant de l'avoir recue.""")
P("""Chaque machine tire par SON code. Exemple de controle, sur une graine de demonstration qui n'est pas une suite de chiffres et ne peut
donc pas etre la graine :""")
T_("    " + ex)
T_()
T_("4. L'ELIGIBILITE D'UNE CELLULE (chaine seule, aucune 2D)")
P("""4.1 Le point (regle de la sonde dense, gel du delta 98, section 3) : g = facteur x g_du_point(w2) ; s = 0.70 s_ff(w2, g) ; graine (n1g,
n2g) = appariement(s, w2), reels ; m = dernier site de barriere(n1g, n2g, w2, g, avec Sigma2), 0 si elle est vide ; r_c = plafond(n1g) + 2
(m + max(8, m)) + 2 ; boite N = r_c + 20.""", 2, 6)
P("""4.2 Les quatorze etiquettes : les couples d'entiers (a, b), a >= 0, b >= 0, de plus grand poids de Poisson p(a, b) = exp(-n1g) n1g^a /
a! x exp(-n2g) n2g^b / b! ; a poids egal, le plus petit a, puis le plus petit b. Ce sont des etiquettes PREDITES : aux seize points deja
joues, 189 des 224 etiquettes lues en font partie.""", 2, 6)
P("""4.3 Par etiquette (a, b) : sites = barriere(a, b, w2, g, avec Sigma2). Chaine du moteur : gamma_chaine, M_facteur 4, aux quatre eta de
chaine (facteurs 1/4, 1/8, 1/16, 1/32). Chaine d'ordre 2 : tables_ordre2 (M_facteur 4), gamma_chaine_ordre2 aux quatre memes facteurs,
valeur Gamma_flux. Chaine d'ordre 3 : tables_ordre3, gamma_chaine_ordre3 au facteur 1/16, valeur Gamma_flux, notee G3 ; STABILITE = le
plus grand |ln(G3' / G3)| pour G3' calculee au facteur 1/8, au facteur 1/32, et au facteur 1/16 avec l'absorbeur recule de 4 sites ;
indefinie si l'une de ces quatre largeurs n'est pas strictement positive. e_bord = |m_bord delta + Sigma2(m_bord) - Sigma2(0)|, m_bord
etant le dernier site de la barriere de l'etiquette et delta = w2 - 2.""", 2, 6)
P("""4.4 Classement. L'etiquette est DANS LES GARDES si e_bord < 0.7 et si la stabilite est definie et <= 0.05. Sa largeur predite G est G3
si elle est dans les gardes, sinon la largeur d'ordre 2 au facteur 1/16. Elle est JUGEABLE si sa barriere n'est pas vide, si les quatre
largeurs du moteur sont strictement positives avec max / min <= 2, si les quatre largeurs d'ordre 2 le sont aussi, et si G > 1.33e-12 (dix
planchers). Elle est DANS LE DOMAINE si elle est jugeable et dans les gardes.""", 2, 6)
P("""4.5 Regle COMMUNE (cellules de N et de P) : N <= 74, au moins 8 etiquettes jugeables sur les 14, dont au moins 5 dans le domaine.""", 2, 6)
P("""4.6 Regle DE BORD (cellules de BN et de BP) : N <= 74, au moins 8 etiquettes jugeables, dont au moins 2 dans le domaine ET au moins 2
hors du domaine. Ces cellules sont faites pour chevaucher la limite du domaine ; la regle commune ne leur convient pas.""", 2, 6)
P("""4.7 Un w2 candidat est ELIGIBLE si toutes ses cellules le sont : cinq pour N et P, une pour BN et BP.""", 2, 6)
P("""4.8 Les seuils 0.7 et 0.05 ont ete lus sur les 131 etats deja vus (note sur la loi) ; 74, 8 et 5 sur la carte ; 2 et 2 sont poses ici,
apres avoir vu la carte et avant d'avoir calcule un seul w2 candidat. Aucun ne sera regle ensuite.""", 2, 6)
T_()
T_("5. LA TABLE COMMUNE, AVANT LA GRAINE")
P("""Chaque machine calcule par SA chaine l'eligibilite des %d cellules candidates (%d w2) AVANT que la graine existe. La table de machine 1
est en section 7. Machine 2 rend la sienne avec sa certification. LA TABLE COMMUNE est leur ET : un w2 candidat y est eligible si et
seulement s'il l'est dans les deux tables. Elle ne depend d'aucune graine. Un desaccord entre les deux tables sur un w2 le rend donc
ineligible, et il est dit dans la certification ; il n'arrete pas le gel.""" % (ncel, nw))
P("""Format d'une table : JSON, creneaux -> <nom du creneau> -> candidats -> liste de {"w2": "<fraction irreductible>", "eligible": true ou
false}.""")
T_()
T_("6. LA REGLE DES RANGS")
P("""Pour chaque creneau, dans l'ordre N, P, BN, BP et independamment : rang 0 ; si le w2 tire n'est pas eligible dans la table commune,
rang 1, et ainsi de suite, pour le CRENEAU ENTIER (jamais cellule par cellule). Au plus cinq rangs, de 0 a 4. Si un creneau n'a pas de w2
eligible en cinq rangs : PAS DE GEL, et on le dit. Un meme w2 peut sortir a deux rangs ; il n'est pas retire de la liste.""")
P("""Si les deux machines ne tirent pas les memes douze cellules a partir de la meme graine et de la meme table commune : PAS DE GEL tant que
l'ecart n'est pas explique par ecrit, et la graine n'est pas changee.""")
T_()
T_("7. LA TABLE DE MACHINE 1 (%d cellules)" % ncel)
P("""Par cellule : facteur, boite N, etiquettes jugeables / dans le domaine ; pour BN et BP : / hors du domaine.""")
for s in ORDRE:
    T_("  creneau %s : %d w2 eligibles sur %d" % (s, nel[s], ncand[s]))
    for w in sorted(cel[s], key=lambda x: F(x)):
        v = sorted(cel[s][w], key=lambda r: F(r["facteur"])); ok = all(r["eligible"] for r in v)
        if s in ("N", "P"):
            det = "  ".join("x%s %d %d/%d%s" % (r["facteur"], r["N"], r["n_jug"], r["n_dom"], "" if r["eligible"] else " !") for r in v)
        else:
            det = "  ".join("x%s %d %d/%d/%d%s" % (r["facteur"], r["N"], r["n_jug"], r["n_dom"], r["n_hors"], "" if r["eligible"] else " !") for r in v)
        T_("    %.3f  %s  %s" % (float(F(w)), det, "ELIGIBLE" if ok else "INELIGIBLE"))
P("""Un point d'exclamation marque une cellule ineligible. Largeurs predites des etiquettes jugeables de ces cellules : de 1e%.0f a 1e%.0f.""" % (
    min(r["lgG_min"] for r in T["cellules"] if r["lgG_min"] is not None), max(r["lgG_max"] for r in T["cellules"] if r["lgG_max"] is not None)))
T_()
T_("8. CE QUE MACHINE 2 CERTIFIE")
for t in ("(a) que les creneaux, le tirage et la regle des rangs sont ceux de sa proposition (lot %s, section 4), aux ecarts declares en section 10 ;" % c["rep"],
          "(b) que les definitions de la section 4 suffisent a calculer l'eligibilite sans lire le code de machine 1 ;",
          "(c) SA table d'eligibilite des %d cellules, par sa chaine ; et la table commune qui en resulte ;" % ncel,
          "(d) que son tirage, sur la graine de demonstration, rend les memes numeros que la section 3 et que le journal d'autotest."):
    P(t, 2, 6)
T_()
T_("9. LA SUITE, DANS L'ORDRE")
for t in ("(1) machine 2 certifie cette piece et rend sa table ; la table commune existe ;",
          "(2) l'operateur donne la graine aux deux machines ;",
          "(3) chaque machine tire ; les douze cellules sont les memes, ou PAS DE GEL ;",
          "(4) machine 1 ecrit la seconde partie : l'instrument (un run, deux etages, les quatre conditions de la reponse de machine 2), la table "
          "gelee des douze points, la feuille d'ordre 3 et son banc, les enonces E1 a E3 avec la cellule pour unite, ce que chaque issue engage, "
          "et les tolerances et probabilites, calculees sur les chaines aux douze cellules, sans aucune largeur 2D ;",
          "(5) machine 2 certifie la seconde partie et, a zero morsure, joue."):
    P(t, 2, 6)
T_()
T_("10. CE QUE CETTE PIECE NE FAIT PAS, ET SES ECARTS A LA PROPOSITION DE MACHINE 2")
for t in ("- Elle ne tire rien et ne connait aucune graine.",
          "- Elle ne dit pas ce que vaut une cellule ou moins de cinq etats LUS seront dans le domaine : l'eligibilite porte sur des etiquettes "
          "predites, le jugement portera sur les etats lus. C'est a la seconde partie de le dire, avant le run.",
          "- Ecart 1 : la regle de bord (4.6) est ecrite ici ; machine 2 en avait donne l'idee (\"au moins deux etats de chaque cote de la garde\").",
          "- Ecart 2 : machine 2 ecrivait \"Si les deux machines ne s'accordent pas sur l'eligibilite d'un tirage, pas de gel\". Ici le desaccord "
          "est regle AVANT la graine, par le ET des deux tables (section 5).",
          "- Ecart 3 : \"au moins six chiffres\" pour la graine est ajoute par machine 1.",
          "- Le bloc d'ordre 3 est celui du lot e93f1898dcd78a8f, inchange ; la definition du hamiltonien effectif est la sienne (forme "
          "symetrique). Machine 2 a note qu'une autre definition deplacerait un peu la largeur d'une chaine tronquee : non chiffre ici."):
    P(t, 2, 4)
T_()
T_("11. PIECES DE CE LOT (convention B)")
for p in PIECES:
    T_("    %s  %s" % (cp[p], p))
T_("    (ce script)       construction_regle_tirage_machine1_v1.py")
T_()
txt = "\n".join(L) + "\n"; txt.encode("ascii"); assert "%" not in txt
longues = [(n + 1, len(l)) for n, l in enumerate(L) if len(l) > 100]; assert not longues, longues
open(SORTIE, "w", encoding="ascii", newline="\n").write(txt); canon = B(SORTIE)

Mq = []
def Am(t="", ind=0, suite=None):
    suite = ind if suite is None else suite
    if not t:
        Mq.append(""); return
    Mq.extend(textwrap.wrap(" ".join(t.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
inel = [(s, "%.3f" % float(F(k["w2"]))) for s in ORDRE for k in T["creneaux"][s]["candidats"] if not k["eligible"]]
Am('# POUR MACHINE 2 -- GEL "LOI, ORDRE 3", PREMIERE PARTIE : LA REGLE DE TIRAGE ET D\'ELIGIBILITE')
Am("# machine 1, v1, 2026-11-15. A CERTIFIER. Rien a jouer. La graine vient APRES, de l'operateur."); Am()
Am("## 0. EN CINQ PHRASES"); Am()
Am("""L'operateur a retenu la section 5 de la carte et lance le gel (ta phrase relayee a 22 h 41, puis "Reprends" a 22 h 42 ; declaration
de machine 1). Je prends tes sections 3 et 4 (lot %s) : un run a deux etages, une feuille d'ordre 3 nouvelle, la cellule pour unite, ta
regle de tirage. Cette piece (%s) n'en fige que la PREMIERE partie : creneaux, tirage, eligibilite, rangs ; elle doit etre certifiee
avant la graine. Ma table d'eligibilite des %d cellules candidates est dedans : %s. La seconde partie (instrument, enonces, tolerances)
vient apres le tirage.""" % (c["rep"], canon, ncel, " ; ".join("%s %d w2 eligibles sur %d" % (s, nel[s], ncand[s]) for s in ORDRE)))
Am(); Am("## 1. E19"); Am()
Am("""Des chaines 1D aux %d cellules candidates (%d w2 au millieme). AUCUNE diagonalisation 2D, a aucun w2 candidat, par machine 1. La
meme interdiction vaut pour toi jusqu'a la certification croisee de la seconde partie.""" % (ncel, nw), 2, 2)
Am(); Am("## 2. CE QUE TU CERTIFIES (section 8 de la piece)"); Am()
Am("""(a) creneaux, tirage, rangs : les tiens, aux trois ecarts declares en section 10 ; (b) les definitions de la section 4 suffisent sans
lire mon code ; (c) TA table des %d cellules et la table commune (le ET) ; (d) ton tirage sur la graine de demonstration rend mes
numeros.""" % ncel, 2, 2)
Am(); Am('## 3. POUR REJOUER (python -I -B ; levier NPY_DISABLE_CPU_FEATURES="X86_V4" chez moi)'); Am()
for cmd, com in (
    ("eligibilite_creneaux_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sonde_ordre2.json> <sortie.json> N,BN,BP    (puis : P)",
     "derive de la carte par quatre retouches (le .diff est joint) ; quelques minutes par creneau"),
    ("lecture_eligibilite_machine1_v1.py <sortie.json> <eligibilite_N_BN_BP.json> <eligibilite_P.json>", "la table de la section 7"),
    ("tirage_machine1_v1.py --autotest        puis, le moment venu : tirage_machine1_v1.py <graine> <ma table> <ta table>", "le tirage ; le ET des tables y est fait"),
    ("construction_regle_tirage_machine1_v1.py <dossier des sorties> <clone du registre> <bloc ordre 3> <note sur la carte> <manifeste du lot de la carte> <manifeste de ta reponse> <sortie.md>",
     "refait la piece et ce fichier")):
    Am(cmd, 2, 6); Am("-> " + com, 6, 9)
Am(); Am("## 4. OU MORDRE"); Am()
for t in (
    """M-1 Les quatorze etiquettes (4.2). Le classement par poids de Poisson peut differer d'une plateforme a l'autre si deux poids sont
egaux a l'arrondi pres ; je n'ai pas cherche de cas. Si nos listes different a une cellule, dis laquelle.""",
    """M-2 La regle de bord (4.6) est de ma plume ; les nombres 2 et 2 sont poses avant d'avoir calcule un w2 candidat, mais apres la carte,
ou les cellules voisines en avaient de 6 a 9 dedans et de 5 a 7 dehors.""",
    """M-3 Le ET des deux tables (section 5) remplace ton "pas de gel" en cas de desaccord. Il rend un w2 conteste ineligible avant la graine.
Si tu preferes ton texte, dis-le : c'est toi qui certifies.""",
    """M-4 w2 ineligibles chez moi : %s. Verifie surtout ceux-la, et ceux qui sont eligibles de peu.""" % (", ".join("%s %s" % x for x in inel) if inel else "aucun"),
    """M-5 L'eligibilite porte sur des etiquettes predites (189 sur 224 aux points joues). Elle ne garantit pas cinq etats LUS dans le
domaine : la seconde partie devra dire ce que vaut une cellule qui en a moins.""",
    """M-6 La stabilite (4.3) depend de l'absorbeur de la chaine d'ordre 2 du bloc depose (debut, force, longueur) : c'est une convention
de ce bloc, pas une propriete de l'etat.""",
    """M-7 La graine "d'au moins six chiffres" et l'ordre N, P, BN, BP sont de ma plume.""",
    """M-8 Dans BN, le compte du domaine n'est pas monotone d'un w2 au suivant (%s) : la garde de stabilite a 0.05 y bascule. C'est la que
nos deux tables ont le plus de chances de differer.""" % " ; ".join("%.3f : %d" % (float(F(w)), cel["BN"][w][0]["n_dom"]) for w in sorted(cel["BN"], key=lambda x: F(x)))):
    Am(t, 2, 6)
Am(); Am("## 5. RIEN D'AUTRE"); Am()
Am("Aucun delai. Je commence la seconde partie par ce qui ne depend pas du tirage : la feuille d'ordre 3 et son banc.")
pm2 = os.path.join(D, "POUR_MACHINE2_gel_loi_partie1_regle_tirage_machine1_v1.md"); tm = "\n".join(Mq) + "\n"; tm.encode("ascii")
assert max(len(l) for l in Mq) <= 100, [l for l in Mq if len(l) > 100]
open(pm2, "w", encoding="ascii", newline="\n").write(tm)
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(pm2), len(Mq), B(pm2)))
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(SORTIE), len(L), canon))
