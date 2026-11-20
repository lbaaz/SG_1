# -*- coding: utf-8 -*-
"""Écrit la note du pont depuis les deux JSON. Usage : python3 -I -B construction_note_pont_machine1_v1.py <pont_v1.json> <pont_semiclassique_v1.json> <sortie.md>"""
import sys, json, math, statistics
P1, P2, SORTIE = sys.argv[1:4]
A = json.load(open(P1)); S = json.load(open(P2)); L = []; W = L.append
par_m = {}
for c in S["cellules"]:
    par_m.setdefault(c["m_bord"], []).extend((c, x) for x in c["croisements"])
def f(x, n=3): return ("%%.%df" % n) % x
tous = [x for c in S["cellules"] for x in c["croisements"]]
W("# Le pont entre la largeur sous absorbeur et le système fermé — note d'exploration")
W("")
W("Machine 1, 2026-11-16 (soir). **Hors chaîne, classe 3.** Chaîne à une dimension seule : aucune 2D, aucun run, aucun gel, machine 2 non consultée. Ouverture : l'opérateur a écrit « On peut avancer sur la recherche là ? » (21 h 39) ; machine 1 a choisi la question.")
W("")
W("## La question")
W("")
W("Tous les actes répètent : « rien n'est dit de la durée de vie du système fermé ». La chaîne fermée (coupée au site N, sans absorbeur) est réelle symétrique : spectre discret, aucune largeur. Que devient Γ ?")
W("")
W("## Le résultat")
W("")
W("Dans la chaîne fermée, l'état du site 0 est couplé aux niveaux de la région d'après la barrière par un élément V, lu comme la demi-largeur du croisement évité quand on fait défiler la condition de bord au bout de la chaîne. Sur %d croisements (les 16 cellules lisibles du gel « largeur du vide », premier ordre, neuf coupures N de %d à %d) :" % (
    len(tous), min(x["N"] for x in tous), max(x["N"] for x in tous)))
W("")
W("**Γ = V² · T**, où T est le temps classique d'aller et retour entre la sortie de la barrière et le bout de la chaîne, T(E) = 2 ∫ dm / √(4 t(m)² − (E − m δ)²), calculé sur les sauts du moteur sans rien lire du spectre.")
W("")
W("| barreaux | Γ sous absorbeur (de … à) | V (de … à) | 2π / (T·|δ|) | ln(V²T / Γ) (de … à) |")
W("|---|---|---|---|---|")
for m in sorted(par_m):
    X = par_m[m]; G = [math.exp(c["ln_G_absorbeur_ordre1"]) for c, _ in X]; V = [x["V"] for _, x in X]; dt = [x["D_T"] / abs(c["delta"]) for c, x in X]; lr = [-x["ln_R_T"] for _, x in X]
    W("| %d | %.1e … %.1e | %.1e … %.1e | %s … %s | %s … %s |" % (m, min(G), max(G), min(V), max(V), f(min(dt)), f(max(dt)), ("%+.4f" % min(lr)), ("%+.4f" % max(lr))))
lrT = [abs(x["ln_R_T"]) for x in tous]
W("")
W("L'écart va de %s à %s en logarithme et diminue quand la barrière s'allonge, comme une relation semi-classique doit le faire. Il est le même aux quatre désaccords à profondeur égale, et il suit la coupure N." % (f(min(lrT), 4), f(max(lrT), 4)))
W("")
W("## Ce qui a été faussé en chemin")
W("")
lv = [x["ln_R_voisins"] for x in tous]; l5 = [x["ln_R_5"] for x in tous]; l7 = [x["ln_R_7"] for x in tous]
W("L'attendu écrit AVANT le calcul prenait pour espacement D la demi-distance aux deux niveaux voisins (règle d'or à spectre discret, Γ = 2πV²/D). Il tombe : 2πV²/D dépasse Γ de %s à %s en logarithme, et de plus en plus avec la profondeur. Les différences centrées à 5 et 7 points font pire (%s à %s ; %s à %s). La lecture par le temps classique est donc venue APRÈS avoir vu les nombres ; ce qui la soutient est qu'elle n'a aucun paramètre et qu'elle rend à la fois la profondeur, le désaccord et la coupure. Cause probable de l'échec des voisins, non éprouvée : près de l'énergie du vide le spectre mêle les niveaux de la région de fuite et les états localisés sous la barrière (une échelle de pas |δ|)." % (
    ("%+.3f" % min(lv)), ("%+.3f" % max(lv)), ("%+.3f" % min(l5)), ("%+.3f" % max(l5)), ("%+.3f" % min(l7)), ("%+.3f" % max(l7))))
W("")
W("## Ce que cela dit du système fermé (lecture, pas un résultat jugé)")
W("")
ex = [(c, x) for c in S["cellules"] for x in c["croisements"] if c["id"] == "MG3"][0]; c, x = ex; G = math.exp(c["ln_G_absorbeur_ordre1"]); Tc = 2 * math.pi / x["D_T"]; ad = abs(c["delta"])
W("- Le temps T est FINI parce que la fuite classique atteint l'infini en temps fini (l'explosion de la branche classique de la campagne). C'est aussi pourquoi le hamiltonien fermé n'est pas essentiellement auto-adjoint (fait connu, note d'antériorité, section 3) : il faut dire ce que devient ce qui arrive à l'infini.")
W("- Si rien ne revient (condition sortante, ce que fait l'absorbeur) : le vide se vide au taux Γ.")
W("- Si tout revient (condition réfléchissante, une extension auto-adjointe, une troncature) : le vide ne se désintègre pas. Il est mêlé aux états de fuite à hauteur de (V/écart)², et ne bat pleinement qu'aux conditions de bord accordées à V près.")
W("- Exemple, %s (N = %d) : Γ = %.2e, T = %.0f, V = %.2e, espacement des niveaux de fuite 2π/T = %s |δ|. Mélange pour un écart de |δ| : (V/|δ|)² = %.1e. Part des conditions de bord qui accordent : de l'ordre de 2V/(2π/T) = %.1e. Période du battement quand c'est accordé : π/V = %.1e." % (
    c["id"], x["N"], G, Tc, x["V"], f(x["D_T"] / ad), (x["V"] / ad) ** 2, 2 * x["V"] / x["D_T"], math.pi / x["V"]))
W("- « Métastable » et « ne se désintègre pas » ne se contredisent donc pas : ce sont deux conditions à l'infini pour le même nombre. C'est une réponse chiffrée, dans notre modèle, à ce que Maiezza et Nesti observent dans le leur (survie qui plafonne et oscille, irrégularités à certains couplages, deux régularisations qui ne convergent pas vers la même limite).")
W("")
W("## Limites")
W("")
de = lambda c, x, o: 2 * math.pi * x["V"] ** 2 / (math.exp(c["ln_G_absorbeur"][o]) * abs(c["delta"]))
d3 = sorted(de(c, x, "3") for c in A["cellules"] if c["id"] != "MG3" for x in c["croisements"] if x["ordre"] == 3)
d3mg = sorted((x["N"], de(c, x, "3")) for c in A["cellules"] if c["id"] == "MG3" for x in c["croisements"] if x["ordre"] == 3)
d1 = sorted(de(c, x, "1") for c in A["cellules"] for x in c["croisements"] if x["ordre"] == 1)
W("- Chaîne à une dimension, premier ordre. À l'ordre 3 la première passe donne un rapport 2πV²/(Γ|δ|) voisin (de %s à %s sur %d croisements hors MG3, contre %s à %s au premier ordre). À MG3 la chaîne d'ordre 3 se dégrade quand la coupure s'allonge (%s) : ses sites lointains sortent sans doute du domaine perturbatif (lecture non éprouvée). Le temps classique n'a pas été calculé à l'ordre 3." % (
    f(d3[0]), f(d3[-1]), len(d3), f(d1[0]), f(d1[-1]), ", ".join("N = %d : %s" % (n, f(v)) for n, v in sorted(set((n, round(v, 3)) for n, v in d3mg)))))
W("- Rien en deux dimensions : la 2D fermée a plus d'un canal vers l'infini, et une boîte n'a pas de paramètre de bord continu. C'est le test qui compte, et il demande un gel.")
W("- La relation est connue dans son principe (taux de fuite = couplage² × temps de retour) ; ce qui est à nous est le nombre, et le fait que T soit un temps de fuite classique fini, de la même nature que l'explosion en temps fini de la branche classique.")
W("- Lecture après coup pour le choix de T (voir plus haut). Une seule forme de chaîne ; aucune 2D ; aucun énoncé gelé.")
W("")
W("## Pièces (conteneur de machine 1, non livrées en lot)")
W("")
W("pont_ferme_absorbeur_machine1_v1.py / .log / pont_v1.json (première passe) ; pont_semiclassique_machine1_v1.py / .log / pont_semiclassique_v1.json (seconde passe) ; ce script.")
open(SORTIE, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n"); print("\n".join(L))
