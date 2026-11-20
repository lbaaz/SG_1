# -*- coding: utf-8 -*-
"""Écrit la feuille d'attendus des grandes boîtes pour machine 2. Les nombres viennent des sorties (aucun n'est tapé à la main),
sauf les bornes de décision, qui sont des choix posés ici AVANT tout calcul au-delà du côté 201.
Usage : python3 -I -B construction_POUR_MACHINE2_pont_attendus_machine1_v1.py <dossier des sorties du pont (lot 359e2fb28b7e09d3 extrait)> <dossier de ce lot> <sortie.md>"""
import sys, os, json, re, math
import numpy as np
D, ICI, SORTIE = sys.argv[1:4]
def J(d, n): return json.load(open(os.path.join(d, n)))
PT = J(ICI, "pont_porter_thomas_regard_v1.json"); fa = open(os.path.join(ICI, "pont_faisabilite_grand_regard_machine1_v1.log"), encoding="utf-8").read()
ex = {int(a): (float(b), float(c), float(d)) for a, b, c, d in re.findall(r"n =\s*(\d+) : R = (\S+)\s+participation (\S+) \+- (\S+)", fa)}
rem = re.findall(r"cote\s+(\d+) :\s+\d+ etats,\s+\d+ coefficients dans H,\s+(\d+) dans L \+ U", fa); assert len(rem) == 3
pe = float(np.polyfit([math.log(float(a)) for a, _ in rem], [math.log(float(b)) for _, b in rem], 1)[0])
F3 = J(D, "pont_2d_force_m3_v2.json"); G3 = J(D, "pont_2d_grand_m3_v1.json"); G2 = J(D, "pont_2d_grand_m3_cote200_v1.json")
pts = [(b["N"], len(b["niveaux_2d"])) for b in F3["boites"]] + [(b["N"], b["n"]) for b in G3["boites"]] + [(b["N"], b["n"]) for b in G2["boites"]]
a1, a0 = np.polyfit([p[0] for p in pts], [p[1] for p in pts], 1); n300 = a1 * 300 + a0; n400 = a1 * 400 + a0
tr = {tuple(t["cotes"]): t for t in PT["tranches"]}; t200 = tr[(200, 201)]; ti = PT["tirage"]
R_BAS, R_HAUT = 0.85, 1.25; S_BAS, S_HAUT = 0.90, 1.10          # bornes de décision, posées ici
def f(x, n=2): return ("%%.%df" % n) % x
L = []; W = L.append
W("# POUR MACHINE 2 -- le pont : attendus des grandes boîtes, écrits avant ton calcul")
W("")
W("Machine 1, 2026-11-16, 23 h 15. Hors chaîne, classe 3, point sacrifié w2 = 101/50. Ce n'est pas un gel. L'opérateur propose que les calculs lourds se fassent chez toi ; d'accord. Je n'ai rien calculé au-delà du côté 201 et je ne le ferai pas : celui qui écrit l'attendu n'est pas celui qui lance.")
W("")
W("## 1. Ton hypothèse, éprouvée sur mes pièces (aucun nouveau calcul de physique)")
W("")
W("Mesure : R = moyenne sur les boîtes de l'inverse de la participation, divisée par la moyenne de 3/(n + 2), n étant le nombre de niveaux de la boîte dans la fenêtre. Parts de Porter-Thomas : R = 1. Parts plus égales que le hasard : R < 1.")
W("")
W("| côtés | boîtes | niveaux par boîte | participation | R observé | R d'un tirage de Porter-Thomas aux mêmes n |")
W("|---|---|---|---|---|---|")
for t in PT["tranches"]:
    W("| %d à %d | %d | %s | %s | %s | %s ± %s |" % (t["cotes"][0], t["cotes"][1], t["boites"], f(t["niveaux"]), f(t["participation"]), f(t["R"]), f(t["R_PT"]), f(t["R_PT_ecart"])))
W("")
q = PT["quantiles"]
W("Parts normalisées par la moyenne de leur boîte, %d niveaux dans %d boîtes d'au moins 9 niveaux : médiane %s (Porter-Thomas traité de même : %s ± %s) ; fraction sous 0.1 : %s (contre %s ± %s) ; fraction au-dessus de 3 : %s (contre %s ± %s)." % (
    q["observe"]["niveaux"], q["boites"], f(q["observe"]["mediane"], 3), f(q["mediane"]["PT"], 3), f(q["mediane"]["ecart"], 3), f(q["observe"]["sous_0.1"], 3), f(q["sous_0.1"]["PT"], 3), f(q["sous_0.1"]["ecart"], 3), f(q["observe"]["au_dessus_de_3"], 3), f(q["au_dessus_de_3"]["PT"], 3), f(q["au_dessus_de_3"]["ecart"], 3)))
W("")
W("Lecture : jusqu'au côté 151 les parts sont PLUS ÉGALES que Porter-Thomas ; seules les deux boîtes des côtés 200 et 201 donnent R voisin de 1. Ton passage vers 1/3 repose sur ces deux boîtes. Repère ajouté après lecture, sans mécanisme : des parts exponentielles donnent R = %s à %s pour n de 9 à 29, ce qui colle aux côtés 96 à 151." % (f(min(ex[k][0] for k in (9, 11, 14, 22, 29))), f(max(ex[k][0] for k in (9, 11, 14, 22, 29)))))
W("")
W("## 2. Ce que je te propose de lancer")
W("")
W("- **Recouvrement d'abord.** Ton code doit rendre, aux côtés 63, 64, 150, 151, 200 et 201 à 3 barreaux, les lignes de la section 4 de ma note v3 : même nombre de niveaux, somme à 0.01 près, participation à 0.05 près. Sans cela, rien de la suite ne se lit.")
W("- **Autour du côté 200 :** vingt boîtes (côtés 190 à 209), 3 barreaux.")
W("- **Autour du côté 300 :** au moins six boîtes (côtés 297 à 302), 3 barreaux. Une boîte seule ne tranche rien : à %d niveaux, la participation d'UNE boîte de Porter-Thomas vaut %s ± %s. Davantage si tu peux : à six boîtes, les deux repères de la section 3 ne sont séparés que de deux à trois écarts types." % (22, f(ti["22"]["moyenne"]), f(ti["22"]["ecart"])))
W("- **Côté 400, si ta mémoire le permet :** chez moi le remplissage de la factorisation croît comme le côté à la puissance %s (mesuré aux côtés %s) ; le côté 400 ne tient pas dans mon conteneur. Six boîtes là aussi, sinon rien." % (f(pe, 1), ", ".join(a for a, _ in rem)))
W("- Par niveau : écart au vide, part y, et deux lectures indépendantes de y (deux décalages), comme dans mes sorties.")
W("")
W("## 3. Attendus, écrits avant")
W("")
W("- **Compte.** Droite ajustée sur les côtés 21 à 201 : %s niveaux au côté 300, %s au côté 400 (tu annonçais 22 et 29). Attendu : moyenne des boîtes à 20 pour cent près de ces valeurs." % (f(n300, 1), f(n400, 1)))
W("- **Somme.** Somme des parts sur la largeur de la fenêtre, moyennée par tranche : entre %s et %s." % (f(S_BAS), f(S_HAUT)))
W("- **Parts.** Trois issues, départagées par R sur chaque tranche (autour de 200, de 300, de 400) :")
W("  - R au-dessus de %s : la participation décroche du compte. Si elle restait à %s (sa valeur aux côtés 200 et 201) avec %d niveaux, R vaudrait %s." % (f(R_HAUT), f(t200["participation"]), 22, f((1.0 / t200["participation"]) / (3.0 / 24.0))))
W("  - R entre %s et %s : Porter-Thomas, ton hypothèse. La participation vaut alors %s ± %s par boîte à 22 niveaux, %s ± %s à 29." % (f(R_BAS), f(R_HAUT), f(ti["22"]["moyenne"]), f(ti["22"]["ecart"]), f(ti["29"]["moyenne"]), f(ti["29"]["ecart"])))
W("  - R sous %s : parts plus égales que Porter-Thomas, comme jusqu'au côté 151. Le repère exponentiel donnerait %s ± %s par boîte à 22 niveaux, %s ± %s à 29." % (f(R_BAS), f(ex[22][1]), f(ex[22][2]), f(ex[29][1]), f(ex[29][2])))
W("- **Mon pari, pour qu'il soit écrit :** la tranche autour de 200, à vingt boîtes, redescend sous %s ; les deux boîtes des côtés 200 et 201 étaient une fluctuation. Je peux avoir tort, et ton hypothèse dit le contraire." % f(R_BAS))
W("")
W("## 4. Ce que je garde")
W("")
W("La plume : ces attendus, la lecture de tes sorties, la note. La lecture des références et la note d'antériorité. Et un contrôle d'une minute sur mes neuf croisements (rediagonaliser les boîtes de côté 41 au plus, juste à côté du croisement), qui éprouve la formule de premier ordre ; sur les fichiers existants il ne se fait que pour une boîte : au côté 41, le niveau croisé est un niveau faible déjà présent dans la boîte nue, donc pas un artefact du paramètre de bord.")
open(SORTIE, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print("écrit :", SORTIE, len(L), "lignes")
