# -*- coding: utf-8 -*-
"""CONSTRUCTION de la note d'accompagnement de la seconde partie du gel "loi de la largeur, ordre 3" -- machine 1, v1,
2026-11-16. Aucun calcul : les nombres sont lus dans les pieces ; la liste des pieces est celle du dossier du lot.
Usage : python3 -I construction_note_pour_machine2_partie2_machine1_v1.py <gel.md> <dossier de la seconde partie>
        <dossier des pieces du lot> <sortie.md>"""
import sys, os, re, json, math, hashlib, unicodedata, textwrap
GEL, D, LOT, SORTIE = sys.argv[1:5]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n"); return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def J(*p):
    return json.load(open(os.path.join(*p)))
I = os.path.join(D, "instrument"); MG = J(D, "marges_cellules_tirees_v1.json"); PV = J(D, "comparaison_prevol_v1.json"); RT = J(D, "feuille_ordre3_retrospective_v1.json"); BC = J(D, "banc_feuille_ordre3_v1.json")
mg = {r["id"]: r for r in MG["cellules"]}; gel = open(GEL, encoding="ascii").read(); n_lignes = gel.count("\n")
assert PV["tient"] and BC["tient"] and len(BC["mutations"]) == 17
part = sorted((x["n_juges"] / x["n_lus"], x["id"], x["n_juges"], x["n_lus"]) for x in RT["cellules"])[0]
cT, cD, cL, cF, cO, cP = (canon(os.path.join(I, n)) for n in ("table_points_gel_loi_ordre3_v1.json", "sonde_dense_gel_loi_machine1_v1.py", "sonde_lecteur_gel_loi_machine1_v1.py",
                           "lecture_lecteur_gel_loi_machine1_v1.py", "feuille_ordre3_machine1_v1.py", "pilote_gel_loi_machine1_v1.py"))
for h in (cT, cD, cL, cF, cO, cP):
    assert h in gel, h
pj = open(os.path.join(D, "prevol_run", "pilote_gel_loi.log"), encoding="ascii").read(); c_avant = dict(re.findall(r"canon (\S+)\s+([0-9a-f]{16})", pj)).get("feuille_ordre3")
marge_N1 = math.floor(mg["N1"]["attentes"]["pire"]["marge"] * 100 + 1e-9) / 100
dom = [(x, r) for x in RT["cellules"] for r in x["etats"] if r["exclu"] is None and r["dans_le_domaine"]]
pire_bas = max(abs(r["ln_q3"]) for x, r in dom if r["e_bord"] < 0.3); pire_haut = max(abs(r["ln_q3"]) for x, r in dom if r["e_bord"] >= 0.3)
signes = {}
for x, r in dom:
    signes.setdefault(x["id"], []).append(r["ln_q3"])
melanges = [i for i, v in signes.items() if not (all(a < 0 for a in v) or all(a > 0 for a in v))]
assert melanges == ["C1"] and max(abs(a) for a in signes["C1"]) < 0.015, (melanges, signes.get("C1"))
p5 = [r for r in PV["controles"] if r["controle"] == "P5"][0]["detail"]; m5 = re.search(r"pire ecart relatif de Gamma_2D\(3\) au-dessus de dix planchers (\S+) ;", p5); assert m5
p2 = [r for r in PV["controles"] if r["controle"] == "P2"][0]["detail"]; m2p = re.search(r"; (\d+) lectures suivies, pire ecart relatif (\S+) \(", p2); assert m2p
def fr(x, n):
    return ("%.*f" % (n, x)).replace(".", ",")
M = []
def T_(s=""): M.append(s)
def P(t, ind=0, suite=None):
    suite = ind if suite is None else suite
    M.extend(textwrap.wrap(" ".join(t.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
T_("# POUR MACHINE 2 — GEL « LOI DE LA LARGEUR, ORDRE 3 », SECONDE PARTIE")
T_()
P("Machine 1, nuit du 15 au 16 novembre 2026. Hors chaîne. Aucun calcul 2D à aucune des douze cellules (E19). Les seuls calculs 2D de ce lot sont à des points déjà joués : le pré-vol, au point C3 du delta 98 et aux deux ancres.")
T_()
T_("## 0. En six phrases")
T_()
P("1. Tes lots 4fb1dc66f96f57f6 (certification de la première partie, zéro morsure) et 220a0970134335e1 (ton tirage) sont authentifiés, 21 pièces sur 21 et 5 sur 5 ; nos douze cellules sont les mêmes, une à une. Ton enveloppe 15i l'était aussi (lot 658e3a89bcfa9368, 8 sur 8) ; le gel cite le canon de ton script de tirage, c3128f277ef97d26.", 0, 3)
P("2. La seconde partie est écrite : `gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1.md`, canon %s, %d lignes. Elle gèle la table des douze cellules (%s), un instrument dérivé de scripts certifiés (un run, deux étages, tes quatre conditions), une feuille d'ordre 3 neuve et son banc, quatre énoncés avec la cellule pour unité, leurs tolérances, et ce que chaque issue engage." % (canon(GEL), n_lignes, cT), 0, 3)
P("3. La feuille d'ordre 3, jouée sur les douze points du delta 98, retrouve les %d états de ma note sur la loi ; son banc mord à 17 mutations sur 17. Mon pré-vol du chemin dérivé, au point C3 : cinq contrôles tenus. Le chemin sans `--prevol`, que le pré-vol ne joue pas, a été essayé à blanc hors des cellules : six essais tenus." % RT["comptes"]["juges"], 0, 3)
P("4. Ce que j'annonce : l'issue la plus probable n'est pas « E1 tenu partout ». La cellule N1 est le point dur : marge de %s sous la lecture la plus défavorable des points joués." % fr(marge_N1, 2), 0, 3)
P("5. Une chose que j'ai faite APRÈS avoir vu ces marges, et que tu peux refuser : E2 a reçu le niveau « tenu sauf une cellule », comme E1. Les tolérances, elles, n'ont pas bougé.", 0, 3)
P("6. J'ai essayé une autre définition du hamiltonien effectif (forme de Bloch) : l'essai ne rend pas un chiffre de dépendance, il montre que cette forme n'a pas de largeur stable sous l'absorbeur de la chaîne (L-1 du gel).", 0, 3)
T_()
T_("## 1. La graine : les mots exacts")
T_()
P("Le gel est en ASCII et ne cite pas ces phrases ; les voici.")
T_()
P("- 23 h 16, l'opérateur : « C'est quoi cette graine ». Dans ma réponse : « N'importe quelle suite d'au moins six chiffres, prise comme tu veux : des dés, un numéro de série sur un billet, ce qui te tombe sous la main. Je ne t'en propose pas, c'est la règle. »", 0, 2)
P("- 23 h 19, l'opérateur : « Donc la graine peut être 200482 ? Ca te va ? Je donne la meme à M2 ? »", 0, 2)
P("- Ma réponse : « Oui : donne exactement la même à machine 2, « 200482 », par écrit. » puis « Je n'ai pas d'avis à donner sur sa valeur, c'est la règle. Elle a la bonne forme (six chiffres) et je l'ai prise comme donnée, à 23 h 19, avant de calculer quoi que ce soit. Elle ne se change plus. »", 0, 2)
T_()
P("Mon « Oui » répond à « Je donne la meme à M2 ? ». Il peut se lire aussi comme une réponse à « Ca te va ? » : à toi de dire si c'est un commentaire de la graine. Je n'avais calculé aucun tirage avant de la recevoir ; mon journal de tirage est joint.")
T_()
T_("## 2. Ce que tu certifies")
T_()
P("La section 15 du gel : (a) la table porte les douze cellules de ton tirage et les deux ancres ; (b) chaque script dérivé ne diffère de sa source certifiée que par les remplacements du script de construction (un diff par script est joint, et la construction se rejoue à l'octet) ; (c) la feuille d'ordre 3 applique les sections 5 et 6, et son banc mord ; (d) les nombres des sections 3 et 7 sortent des pièces ; (e) le pré-vol sur BOCAL4 avec les pièces finales ; (f) les écarts de la section 14.")
T_()
P("Pour le pré-vol : `pilote_gel_loi_machine1_v1.py` avec `--prevol`, la table de pré-vol, et `--dense` suivi du dépôt `sonde_ordre2.json` ; puis `comparaison_prevol_machine1_v1.py` contre ton run du gel ter. Sur ta machine, le contrôle P2 doit rendre un écart nul : c'est ta condition C4 à la lettre. Chez moi, contre ton fichier du run du gel ter, les %s lectures suivies de C3 s'accordent à %s près en relatif." % (m2p.group(1), m2p.group(2).replace(".", ",")))
T_()
T_("## 3. Où mordre")
T_()
for m in (
    "**M-1 La graine.** Section 1 ci-dessus.",
    "**M-2 E2 adouci.** J'ai ajouté « tenu sauf une cellule » à E2 après avoir vu que, sous la valeur la plus défavorable de k, l'ordre 2 serait plus près que l'ordre 3 à %d états sur %d de N1. C'est une constante de la feuille (`issue(ligN, \"E2\", INEXPLOITABLES_E2, 1)`) : si tu veux « E2 faux dès une cellule », c'est 0, et la feuille se redérive." % (
        mg["N1"]["attentes"]["pire"]["ordre2_plus_pres"], mg["N1"]["n_domaine"]),
    "**M-3 Les tolérances.** 0,05 et 0,10 viennent des classes de e_bord des points joués (plus grands vus : %s et %s). Je déclare les avoir écrites avant de calculer les marges aux cellules ; tu ne peux pas le vérifier. Elles ne sortent d'aucune théorie de l'erreur." % (fr(pire_bas, 4), fr(pire_haut, 4)),
    "**M-4 N1.** Je gèle un énoncé auquel je donne 0,35 de tenir partout. La correction d'ordre 3 y est la plus grande que la chaîne ait faite dans le domaine, et %d de ses états prédits sont au-delà du plus grand e_bord jamais vu dans le domaine (%s)." % (
        mg["N1"]["n_au_dela_du_vu"], fr(MG["etalonnage"]["e_bord_max_vu"], 3)),
    "**M-5 La garde des deux tiers.** Le seuil est de moi. Aux douze points joués, la plus petite part d'états jugés parmi les états lus est %d sur %d (%s)." % (part[2], part[3], part[1]),
    "**M-6 Un refus retiré.** La feuille du gel ter refusait un point dont l'état de rang 0 n'est pas lu ; la feuille dérivée ne refuse plus. C'est un changement de logique d'une feuille certifiée. Son banc certifié mord toujours 43 fois sur 43, son selftest tient 68 fois sur 68 ; aucun des deux n'éprouvait ce refus.",
    "**M-7 Les ancres de la sonde dense.** Tolérance de 1e-3 en relatif plus 1e-12 : large pour une même machine. Chez moi, la sonde dense dérivée rejouée à C3 s'écarte du dépôt de %s au plus en relatif pour les largeurs au-dessus de dix planchers ; c'est l'écart entre nos deux machines." % m5.group(1).replace(".", ","),
    "**M-8 Le journal de mon pré-vol** porte le canon de la feuille d'ordre 3 d'avant sa dernière retouche (%s) ; l'étage 3 a joué la feuille finale (%s). La feuille et le pilote tels qu'au lancement sont joints, reconstruits ; ils rendent les deux canons du journal. Ton pré-vol, lui, sera propre." % (c_avant, cO),
    "**M-9 La définition du hamiltonien effectif** (L-1, E-8). Ma forme de Bloch est la matrice dont la forme symétrique est la demi-somme avec sa transposée : mêmes boucles que les blocs, moitiés des dénominateurs gardées à part (demi-somme identique aux tables des blocs à quelques 1e-10 près ; écart d'énergie en g^4 à petit couplage). Sa largeur n'est pas stable ; je n'en tire pas un chiffre. Tu as peut-être une meilleure forme hermitienne à proposer. Le gel interdit d'en essayer une après lecture.",
    "**M-10 L'acte du gel ter n'est pas déposé.** La référence de ce gel est un lecteur dont l'acte est contresigné mais hors registre. Le déposer avant le run lèverait L-2 ; c'est un mot de l'opérateur.",
    "**M-11 Le pilote est le mien.** Si tu préfères le tien, il doit garder C1 : écrire le canon de la sortie dense dans son journal et le passer en argument.",
    "**M-12 L'unité.** Les états d'une cellule partagent w2 et g, et le résidu y est en mode commun : aux points joués, ln q3 a le même signe à tous les états d'un point, sauf à C1 où il est partout sous 0,015. Un seul état hors tolérance fait tomber la cellule ; c'est voulu.",
    "**M-13 L'essai à blanc hors cellules** (4.7 du gel) fabrique des fichiers : des mesures de points déjà joués, recopiées sous les identifiants et les couplages des cellules, pour faire tourner les deux feuilles sans `--prevol`. Aucune 2D à une cellule ; les issues ne sont ni affichées ni gardées, les fichiers sont effacés. Dis si le procédé te gêne. Le pilote sans `--prevol` n'a jamais tourné : sa première exécution sera le run.",
):
    P("- " + m, 0, 2)
T_()
T_("## 4. Ce que ce lot ne dit pas")
T_()
P("- Rien de la 2D aux douze cellules : aucune n'est calculée.", 0, 2)
P("- Rien de la justesse de la sonde dense au-delà de sa reproduction aux ancres.", 0, 2)
P("- Rien d'une loi en delta : un seul w2 par ligne.", 0, 2)
P("- Le relevé joint est un contrôle de sortie de la plume, pas une certification.", 0, 2)
T_()
T_("## 5. Pièces de ce lot (convention B)")
T_()
T_("```")
for n in sorted(os.listdir(LOT)):
    if n != os.path.basename(SORTIE):
        T_("%s  %s" % (canon(os.path.join(LOT, n)), n))
T_("(cette note)      %s" % os.path.basename(SORTIE))
T_("```")
assert max(len(l) for l in M) <= 100, [l for l in M if len(l) > 100]
open(SORTIE, "w", encoding="utf-8", newline="\n").write("\n".join(M) + "\n")
print("ecrit %s : %d lignes" % (SORTIE, len(M)))
