# -*- coding: ascii -*-
"""Construit le rectificatif d'avant run a la seconde partie du gel "pont". Les nombres sont lus dans la lecture de la
certification de machine 2 par machine 1. ASCII, lignes de 100 colonnes au plus, sans signe pour cent.
Usage : python3 -I -B ce_script <lecture_certification_m2_partie2_v1.json> <gel partie 2.md> <manifeste du lot de machine 2>
                                <sortie.md>"""
import sys, json, hashlib, unicodedata, textwrap
LECT, GEL, MAN, SORTIE = sys.argv[1:5]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
J = json.load(open(LECT)); T = J["sortie_tronquee"]; D = J["densite_SA5_A"]; B = J["boites"]
g = " ".join(open(GEL, encoding="ascii").read().split())
assert "une boite interrompue se rejoue telle quelle ; rien d'autre ne se rejoue." in g and T["code_de_sortie"] == 0
L = []
def par(t, r="  ", s=None): L.extend(textwrap.wrap(" ".join(t.split()), width=100, initial_indent=r, subsequent_indent=r if s is None else s,
                                                   break_long_words=False, break_on_hyphens=False))
L += ['RECTIFICATIF D\'AVANT RUN A LA SECONDE PARTIE DU GEL "PONT"', "machine 1, 2026-11-17, version 1. ASCII, lignes de 100 colonnes au plus.", "", "0. STATUT"]
par("""Ecrit apres la certification de la seconde partie (canon %s) par machine 2 (lot %s), AVANT le feu vert de l'operateur et avant
toute 2D aux six cellules tirees. Il ne change aucun enonce, aucune tolerance, aucun cote, aucun absorbeur, aucune feuille. La piece
de la seconde partie n'est pas retouchee. Il ne demande pas de reponse : machine 2 dit dans sa note de run si elle le prend.""" % (canon(GEL), canon(MAN)))
L += ["", "1. UNE SORTIE DE DENSITE INTERROMPUE"]
par("""Le fait est de machine 2 (sa note, 2.5) : la sonde de densite reecrit son fichier apres chaque barreau, et ma feuille de densite
accepte sans erreur une sortie interrompue. Verifie de mon cote : sur les sorties du point sacrifie a la profondeur 5, reduites a %d
barreaux d'absorbeur sur 12, ma feuille rend le code de sortie %d et %d ecarts lisibles ; la lecture bouge de %.1e. La faute est de ma plume.""" %
    (T["barreaux_gardes"], T["code_de_sortie"], T["ecarts_lisibles"], T["ln_R3_ecart_max_a_la_lecture_complete"]))
par("""De plus le 5.6 dit : "une boite interrompue se rejoue telle quelle ; rien d'autre ne se rejoue". A la lettre, une sortie de
densite interrompue ne pourrait pas etre rejouee. Ce n'etait pas voulu.""")
par("""LA REGLE. Une sortie de la sonde de densite est COMPLETE si elle porte les douze barreaux k = -3 a 8, chacun suivi ou dit non
suivi. Une sortie incomplete n'est pas une sortie du run : son calcul se rejoue tel quel, par la meme commande, comme une boite
interrompue. Une sortie complete ne se rejoue jamais. Les feuilles ne lisent que des sorties completes ; ma feuille n'est pas
modifiee : la completude se controle avant elle, par machine 2 au run comme elle l'annonce, par machine 1 au rejeu.""")
L += ["", "2. LES RESERVES DE MACHINE 2, PRISES (aucune ne change une decision)"]
for t in ("R1 : la part y prend la PREMIERE lecture par partition (c2_a). Un niveau est fiable si |c2_a - c2_b| <= 0.02 c2_a.",
          "R2 : la feuille de verdict rend la famille ; le verdict par creneau se lit sur ses lignes par cellule.",
          """R3 : (Q1) porte sur les boites lisibles des cellules lisibles pour (S) ; (Q2) sur les boites lisibles de chaque groupe, toutes
          cellules melees. Rien n'y est juge.""",
          """R4 : "barreaux" designe les douze barreaux d'absorbeur (k) dans les sections 5.1 et 5.2, et la profondeur de la chaine (3, 4,
          5) partout ailleurs.""",
          "R5 : (L2) sans aucun ecart lisible x >= 5 est ILLISIBLE, comme la feuille le rend.",
          "R6 : le mode repetition de la feuille de verdict n'est pas un verdict ; a six cellules la regle est celle du texte.",
          "R7 : une boite sans niveau dans la fenetre n'est pas lisible pour (S) ; son compte, s'il est valide, vaut 0 dans (C).",
          """R8 : le controle R11 de mon releve compare au caractere pres ; sur BOCAL4 un nombre sur 91 y differe au dernier bit (question
          Q3, non jugee), les verdicts sont identiques. Au rejeu je comparerai les nombres a 1e-12 pres.""",
          """Egalites aux bornes : comme les feuilles (<= 1.05, <= 0.02, <= 0.05, bornes des intervalles incluses). A rapport egal, la
          fenetre de plateau de plus petit k."""):
    par("- " + t, r="  ", s="    ")
L += ["", "3. CE QUE JE RETIENS DE SA CERTIFICATION, POUR L'ACTE"]
par("""Mes deux sondes rejouees sur BOCAL4 au point sacrifie redonnent mes pieces : la densite a %s pres sur ln rho (absorbeur A,
profondeur 5, les %d barreaux d'absorbeur) ; quatre boites aux memes niveaux, poids par partition a %.1e pres au plus, quand le poids BRUT differe d'une
machine a l'autre jusqu'a %.3f. La lecture par partition est acceptee par machine 2, qui l'a refaite depuis le texte avec d'autres
decalages et d'autres coupures. Elle dit, et c'est juste : rien n'a ete verifie en precision etendue ; la partition est jugee sur sa
stabilite et sur deux ecritures, pas sur une valeur de reference exacte. Cette limite ira dans l'acte.""" %
    ("%.1e" % D["ln_rho_ecart_max"], D["barreaux"], max(max(b["c2_a"], b["c2_b"]) for b in B.values()), max(b["brut_a"] for b in B.values())))
L += ["", "-- FIN rectificatif_gel_pont_partie2_avant_run_machine1_v1 --"]
txt = "\n".join(l.rstrip() for l in L) + "\n"; txt.encode("ascii"); assert all(len(l) <= 100 for l in L) and "%" not in txt
open(SORTIE, "w", encoding="ascii", newline="\n").write(txt); print("ecrit : %s ; %d lignes ; canon %s" % (SORTIE, len(L), canon(SORTIE)))
