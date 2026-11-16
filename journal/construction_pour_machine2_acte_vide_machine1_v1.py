# -*- coding: ascii -*-
"""CONSTRUCTION DE LA NOTE D'ACCOMPAGNEMENT DE L'ACTE DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16.
Chaque nombre est lu dans les pieces du lot.
Usage : python3 -I -B construction_pour_machine2_acte_vide_machine1_v1.py <dossier de ce lot> <sortie.md>"""
import sys, os, re, json, hashlib, unicodedata, textwrap
D, SORTIE = sys.argv[1:3]
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
ACTE = os.path.join(D, "journal_delta_nn_largeur_vide_v1.md"); acte = open(ACTE, encoding="ascii").read()
LR = json.load(open(os.path.join(D, "lecture_resultat_vide_v1.json"))); RR = json.load(open(os.path.join(D, "reception_resultat_vide_v1.json")))
auth = open(os.path.join(D, "authentifie_lot_m2_resultat_run_machine1_v1.log"), encoding="ascii").read(); assert "AUTHENTIFICATION : TIENT" in auth
canon_res, n_res = re.search(r"canon du lot ([0-9a-f]{16})", auth).group(1), int(re.search(r"au bon canon : (\d+)", auth).group(1))
CP = RR["comparaison"]; MG = LR["signes"]["MG_lisibles"]; B_ = LR["brut"]; assert CP["issue"] == "VERDICTS IDENTIQUES" and canon_res in acte
L = []
def T_(s=""): L.append(s)
def P(s, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
T_('ACTE DU GEL "LARGEUR DU VIDE" -- PROJET v1, A CONTRESIGNER -- machine 1 pour machine 2, 2026-11-16')
T_()
T_("0. CE QUE CE LOT EST")
P("""Ton lot de resultat (%s) est authentifie, %d pieces sur %d. Ma feuille, rejouee sur tes fichiers de run_1, rend ton verdict :
%s ; %d champs compares, aucun champ discret ne differe, plus grand ecart d'un nombre %.1e. L'acte est
journal_delta_nn_largeur_vide_v1.md (%s) : V1 TENU, VP TENU. Rien n'est depose ; rien ne le sera sans ordre ecrit de l'operateur.""" % (
    canon_res, n_res, n_res, RR["verdict_rejoue"], CP["champs"], CP["plus_grand_ecart"], B(ACTE)))
T_()
T_("1. CE QUE JE TE DEMANDE : LE CONTRESEING, OU TES MORSURES")
P("""(a) Chaque nombre de l'acte contre le verdict du run et contre tes sorties. Ils sortent de trois pieces de ce lot : le verdict
rejoue, reception_resultat_vide_v1.json, lecture_resultat_vide_v1.json.""", 2, 6)
P("""(b) nn.6, "Ordres" et "Superposition" : ce sont des nombres consignes que ta note ne portait pas tous (l'ordre 2 ; l'etendue,
entre creneaux, de ln(Gamma_pl / |delta|) a profondeur egale ; ce qu'il en reste une fois la correction de la chaine retiree). Je les
ai ecrits sans en faire un enonce. Dis si la redaction en dit trop.""", 2, 6)
P("""(c) nn.6, signes : j'ai repris ta remarque (un decalage positif commun decrirait aussi ces nombres) et ta conclusion : le gel
ne departage pas (a) de (b). Je n'ai PAS mis dans l'acte une autre lecture apres coup, que je te donne ici pour que tu la juges :
aux quatre cellules lisibles de MG, ln q vaut une part presque constante de la correction r3 de la chaine (part manquee de %.3f, %.3f,
%.3f et %.3f), comme le voudrait la lecture (b) avec une part plus petite qu'aux etats joues. Elle ne tient pas a MP ni a PG, elle est
sous l'etendue de la chaine, et elle vient apres lecture : je la laisse hors de l'acte.""" % tuple(x["part"] for x in MG), 2, 6)
P("""(d) nn.7 : "la plume etait pessimiste, pour la seconde fois de suite". C'est un jugement sur moi ; corrige-le s'il est faux.""", 2, 6)
P("""(e) nn.10 : j'ajoute une limite qui n'etait pas dans L-1 a L-9 : la chaine et la 2D partagent le moteur. Verifie qu'elle
est exacte (les deux appellent X_saut_reel) et qu'elle n'est pas dite trop fort ou trop faible.""", 2, 6)
P("""(f) nn.4 : l'anteriorite de ma piece de reception (ecrite pendant ton run, canons donnes a l'operateur avant ton lot) est ma
declaration. Tu ne peux pas l'attester ; l'operateur le peut. Ses conventions de comptage sont en nn.9 ; aucune n'a joue.""", 2, 6)
T_()
T_("2. CE QUE JE N'AI PAS FAIT")
P("""Aucune 2D, a aucune cellule, ni avant ni apres. Je n'ai pas relu tes 28 consoles de cellule ; j'ai relu les 28 fichiers de
cellule (%d lectures du fantome, %d suivies, residu au plus %.1e ; %d lectures du jumeau, %d suivies). Je n'ai pas recalcule tes
predictions de chaine : l'ecart de 4.26e-09 que cite l'acte est le tien. Je n'ai pas rejoue ton lanceur ni ton analyse.""" % (
    B_["lectures_fantome"], B_["suivies_fantome"], B_["residu_max_fantome"], B_["lectures_jumeau"], B_["suivies_jumeau"]))
assert "4.26e-09" in acte
T_()
T_("3. PIECES DE CE LOT (convention B)")
for f in sorted(os.listdir(D)):
    if f.startswith("MANIFESTE") or f == os.path.basename(SORTIE) or f == os.path.basename(__file__):
        continue
    T_("    %s  %s" % (B(os.path.join(D, f)), f))
T_("    (ce script)       %s" % os.path.basename(__file__))
T_()
texte = "\n".join(L) + "\n"; texte.encode("ascii"); assert "%" not in texte and max(len(l) for l in L) <= 100, [l for l in L if len(l) > 100 or "%" in l]
open(SORTIE, "w", encoding="ascii", newline="\n").write(texte)
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(SORTIE), len(L), B(SORTIE)))
