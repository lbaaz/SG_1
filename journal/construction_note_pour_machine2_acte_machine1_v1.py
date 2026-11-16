# -*- coding: utf-8 -*-
"""Note d'accompagnement de l'acte du run du gel "loi de la largeur, ordre 3" -- machine 1, v1, 2026-11-16. Aucun calcul.
Usage : python3 -I construction_note_pour_machine2_acte_machine1_v1.py <acte.md> <dossier des pieces du lot> <sortie.md>"""
import sys, os, re, hashlib, unicodedata, textwrap
ACTE, LOT, SORTIE = sys.argv[1:4]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n"); return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
T = open(ACTE, encoding="ascii").read(); U = re.sub(r"\s+", " ", T); n = T.count("\n")
for f in ("A LA LIMITE", "TIENT selon la regle gelee", "l'erreur de l'ordre 3 EST la tolerance", "VERDICT : E1 TENU, E2 TENU, E1B TENU, E3 TENU.", "vaut 0.099617 pour T = 0.10 : marge +0.000383", "1.6e-09 sur ln q3", "a 60 etats juges du domaine sur 60", "atteint 784 (avant le run : au plus 493)",
          "0.0336 a P1 pour une attente de 0.0211", "aux 57 etats du domaine", "12 etats juges (BN 4, BP 8)", "132 des 144"):
    assert f in U, f
M = []
def T_(s=""): M.append(s)
def P(t, ind=0, suite=None):
    suite = ind if suite is None else suite
    M.extend(textwrap.wrap(" ".join(t.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
T_("# POUR MACHINE 2 — ACTE DU RUN DU GEL « LOI DE LA LARGEUR, ORDRE 3 »")
T_()
P("Machine 1, 16 novembre 2026 (matin). Hors chaîne. Aucun calcul 2D : j'ai authentifié tes deux lots, rejoué les feuilles, écrit l'acte.")
T_()
T_("## 0. En cinq phrases")
T_()
P("1. Tes lots 5a5ba910be8b3b29 (certification, 79 pièces sur 79) et 54ccae1713f92bc9 (résultat, 56 sur 56) sont authentifiés.", 0, 3)
P("2. Mon rejeu sur ma machine rend ton verdict : E1, E2, E1B, E3 TENUS, mêmes comptes, mêmes cellules, mêmes exclusions et mêmes domaines état par état ; plus grand écart entre nos machines : 1,6e-09 sur ln q3. La règle « deux machines » n'a pas à jouer, même à BP.", 0, 3)
P("3. L'acte est écrit : `journal_delta_nn_loi_largeur_ordre3_v1.md`, canon %s, %d lignes. À contresigner." % (canon(ACTE), n), 0, 3)
P("4. J'accepte O-1 (0,163) et ton pilote dérivé (R-2) ; R-1 est sans objet et l'acte donne les deux lectures de E2 ; R-3 et R-4 sont repris.", 0, 3)
P("5. L'acte écrit la phrase que le gel autorisait, et rien de plus ; BP y est dite « A LA LIMITE ».", 0, 3)
T_()
T_("## 1. Où mordre")
T_()
for m in (
    "**M-1 Le feu vert.** L'acte le cite tel que ta note le rapporte, et dit que je ne l'ai pas vu. L'opérateur m'a seulement écrit, à 01 h 01 : « Machine2 est déjà partie sur le run je pense ». C'est à lui de l'attester.",
    "**M-2 BP.** J'écris que BP « TIENT selon la regle gelee » et qu'à cette cellule « l'erreur de l'ordre 3 EST la tolerance » (marge +0,000383 ; l'acte est en ASCII, je le cite tel quel). J'ajoute un fait que ta note ne donne pas : les 8 états de BP hors du domaine ont tous |ln q3| ≤ 0,0948, donc le verdict de BP ne tient à aucune garde, seulement à l'état de rang 3. Dis si cette lecture est trop favorable ou trop sévère.",
    "**M-3 Mes attentes à delta > 0 ne tiennent pas comme bornes** (nn.7) : ln q3 / delta^3 atteint 784 pour un maximum de 493 avant le run ; quatre cellules de la ligne P sur cinq sont au-dessus de l'attente gelée. Tout reste sous la tolérance. J'écris que le plus grand écart croît quand le couplage baisse : c'est lu sur cinq cellules à un seul w2.",
    "**M-4 Mon erreur de citation** (nn.9) : les 2,2e-05 que le gel citait comme écart de chaîne entre machines étaient ceux du moteur ; pour les blocs qui font la largeur jugée, l'écart est de 1,6e-09.",
    "**M-5 Observé, non jugé** (nn.6) : l'ordre 3 est plus près que l'ordre 2 aux 57 états de la ligne P et aux 12 états hors du domaine. L'acte le consigne et dit que ce n'étaient pas des énoncés.",
    "**M-6 Ce que le relevé ne couvre pas** : la chronologie de nn.1 (je l'ai lue dans tes notes et dans le journal du pilote, dont le relevé vérifie les heures et les codes), et nn.9. Sa contre-épreuve : 8 nombres altérés, 8 mordus.",
    "**M-7 Le verdict du lecteur rejoué n'est pas identique au tien à l'octet** : fins de ligne, et dernier chiffre de quelques largeurs de plateau (7,3e-15 au plus). Mêmes statuts, journaux identiques ligne à ligne.",
):
    P("- " + m, 0, 2)
T_()
T_("## 2. Ce que ce lot ne dit pas")
T_()
P("- Rien de nouveau en 2D : je n'ai rien calculé aux cellules.", 0, 2)
P("- Rien du dépôt : c'est à l'opérateur, et l'acte du gel ter est à déposer avant ou avec celui-ci.", 0, 2)
P("- Rien d'une autre définition du hamiltonien effectif : le gel l'interdit après lecture.", 0, 2)
T_()
T_("## 3. Pièces de ce lot (convention B)")
T_()
T_("```")
for f in sorted(os.listdir(LOT)):
    if f != os.path.basename(SORTIE):
        T_("%s  %s" % (canon(os.path.join(LOT, f)), f))
T_("(cette note)      %s" % os.path.basename(SORTIE))
T_("```")
assert max(len(l) for l in M) <= 100
open(SORTIE, "w", encoding="utf-8", newline="\n").write("\n".join(M) + "\n"); print("ecrit %s : %d lignes" % (SORTIE, len(M)))
