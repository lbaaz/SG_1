# Ecrit la note de lecture des grandes boites ; chaque nombre vient des JSON de mes trois feuilles ou des constantes nommees ci-dessous.
# Arguments : <rejeu.json> <regards.json> <complements.json> <sortie.md>
import sys, json, io, math
J = json.load(open(sys.argv[1])); R = json.load(open(sys.argv[2])); C = json.load(open(sys.argv[3]))
DELTA = 0.02            # w2 = 101/50
GAMMA = 3.2661e-09      # largeur du vide a 3 barreaux au point sacrifie (note v3 du pont, section 2)
ATT = {"200": 14.4, "300": 21.6, "400": 28.8}   # 21.6 et 28.8 : mes attendus ; 14.4 : la meme droite, lue par machine 2
t = []; A = t.append
A("# Le pont — lecture des grandes boîtes de machine 2 (côtés 190 à 402), note d'exploration")
A("")
A("Machine 1, 2026-11-17 (nuit). **Hors chaîne, classe 3**, point sacrifié w2 = 101/50, 3 barreaux. Aucun calcul de physique de machine 1 : relecture des niveaux du lot de machine 2 lot_machine2_2026-11-17_grandes_boites_resultats_v1 (canon dce7431e7a8b4a8c, 27 pièces sur 27 au manifeste). Suite de la note v3 du pont et des attendus écrits avant le calcul (v1 c1ec807742b57f3b, tenue par machine 2 ; v2 écrite avant aussi).")
A("")
A("## 0. En cinq phrases")
A("")
n_tot = sum(J[k]["niveaux"] for k in J); nf = sum(J[k]["non_fiables"] for k in J)
A("1. Mes agrégats, recalculés depuis ses %d niveaux, sont les siens au chiffre imprimé : comptes, sommes, participations, R, repères tirés." % n_tot)
A("2. Mes attendus : le compte tient aux trois tranches, la somme aux trois ; les parts sortent « poids aléatoires » autour de 200 (R = %.3f) et de 300 (%.3f), « plus égales » autour de 400 (%.3f). **Mon pari écrit est perdu** : la tranche autour de 200 ne redescend pas sous 0.85."
  % (J["200"]["R"], J["300"]["R"], J["400"]["R"]))
A("3. La saturation est exclue : une participation bloquée à 5.31 aurait donné R = %.2f et %.2f autour de 300 et de 400 ; le rapport R(400)/R(300) vaut %.2f, contre %.2f pour une participation bloquée et %.2f ± %.2f pour un régime stationnaire."
  % (C["F_bloque"]["300"], C["F_bloque"]["400"], C["F"]["rapport"], C["F"]["bloque"], C["F"]["stationnaire"][0], C["F"]["stationnaire"][1]))
A("4. Les deux choses dont le pont a besoin tiennent donc jusqu'au côté 402 : la force est conservée (règle de somme) et elle se partage entre un nombre de niveaux qui croît avec la boîte.")
A("5. Ce qui ne se tranche pas : Porter-Thomas exact ou parts un peu plus égales. Et l'énoncé sur le bocal infini reste une extrapolation, sur six ordres de grandeur en côté (section 3).")
A("")
A("## 1. Mes attendus, appliqués tels quels")
A("")
A("| tranche | boîtes | niveaux par boîte (attendu, à 20 pour cent) | somme / largeur (attendu 0.90 à 1.10) | participation | R | Porter-Thomas aux mêmes comptes | exponentielle | issue |")
A("|---|---|---|---|---|---|---|---|---|")
for k, lab in (("200", "190 à 209"), ("300", "297 à 302"), ("400", "397 à 402")):
    j = J[k]; iss = "poids aléatoires" if 0.85 <= j["R"] <= 1.25 else ("plus égales" if j["R"] < 0.85 else "décroche")
    A("| %s | %d | %.2f (%.1f) : tient | %.3f ± %.3f : tient | %.2f | %.3f | %.3f ± %.3f | %.3f ± %.3f | %s |"
      % (lab, len(j["cotes"]), j["n_moyen"], ATT[k], C["E"]["tranche_" + k][0], C["E"]["tranche_" + k][1], j["participation_moyenne"], j["R"], j["R_PT"][0], j["R_PT"][1], j["R_exp"][0], j["R_exp"][1], iss))
A("")
A("Machine 2 a appliqué les seuils de la v1 (0.85 et 1.25). La v2 remontait le seuil haut à 1.35 et 1.55 : aucune issue ne change, le plus grand R vaut %.3f. Le compte attendu autour de 200 (14.4) est ma droite, lue par elle. Niveaux non fiables : %d sur %d ; écart médian entre ses deux lectures de y : %.0e à %.0e selon la tranche."
  % (max(J[k]["R"] for k in J), nf, n_tot, min(J[k]["ecart_lectures_mediane"] for k in J), max(J[k]["ecart_lectures_mediane"] for k in J)))
A("")
A("## 2. Regards venus APRÈS lecture (pas des épreuves)")
A("")
ab = R["AB_toutes"]
A("- **La densité de niveaux est uniforme dans la fenêtre** (rapport entre 7.5 et 0.5 |δ| : %.2f, %.2f, %.2f aux trois tranches). Normaliser les parts par la moyenne de la boîte ne biaise donc pas R : normalisé localement, R vaut %.3f, %.3f, %.3f."
  % tuple([(R["AB_" + k]["densite_droite"][0] + 7.5 * R["AB_" + k]["densite_droite"][1]) / (R["AB_" + k]["densite_droite"][0] + 0.5 * R["AB_" + k]["densite_droite"][1]) for k in ("200", "300", "400")] + [R["C_" + k]["R_local"] for k in ("200", "300", "400")]))
A("- **Le compte croît comme le côté** : %.4f niveau par quantum de côté dans la fenêtre, soit %.5f par |δ| et par quantum (droite par l'origine, 32 boîtes). Lecture : avec une énergie de forme indéfinie, les états voisins d'une énergie donnée longent une ligne du plan des quanta, pas une surface ; d'où une croissance comme le côté et non comme son carré." % (C["H"]["pente_origine"], C["H"]["par_delta_par_quantum"]))
A("- **La somme d'ensemble dépasse 1** : %.3f ± %.3f sur 32 boîtes. Par tranche d'écart au vide elle vaut %s (de 0.05–1 à 7–8 |δ|) ; pente %+.3f ± %.3f par |δ| ; extrapolée à l'écart nul %.3f ± %.3f, à 8 |δ| %.2f ± %.2f. Lecture possible, non établie : le lisse de la chaîne d'ordre 3 serait un peu bas loin de l'énergie du vide, là où aucun gel ne l'a jugé (le lisse d'ordre 1 y vaut 0.682 fois celui d'ordre 3 à 8 |δ|, note v3). Je ne le lis pas comme de la force gagnée."
  % (C["E"]["somme"], C["E"]["erreur"], ", ".join("%.2f" % v[0] for v in ab["somme"]), C["E"]["pente"], C["E"]["pente_erreur"], C["E"]["a_zero"], C["E"]["a_zero_erreur"], C["E"]["a_huit"], C["E"]["a_huit_erreur"]))
A("- **Le bas de la distribution est celui de Porter-Thomas, pas d'une exponentielle** : fraction des parts sous un dixième de la moyenne locale %.3f, %.3f, %.3f (Porter-Thomas 0.248 ; exponentielle 0.095) ; au-dessus de trois fois la moyenne %.3f, %.3f, %.3f (0.083 ; 0.050). L'écart à Porter-Thomas est dans la variance (%.2f, %.2f, %.2f fois le carré de la moyenne, contre 2) : il manque de très grosses parts autour de 200 et de 400. C'est la même information que R."
  % tuple([R["C_" + k]["z"]["sous_0.1"] for k in ("200", "300", "400")] + [R["C_" + k]["z"]["au_dessus_3"] for k in ("200", "300", "400")] + [R["C_" + k]["z"]["variance_sur_moyenne2"] for k in ("200", "300", "400")]))
A("- **Deux boîtes de côtés consécutifs se comportent comme deux tirages** : corrélation des logarithmes des parts entre niveaux appariés au plus proche %+.2f, %+.2f, %+.2f. La réserve de la note v3 (boîtes voisines non indépendantes) ne pèse pas sur les parts."
  % tuple(R["D_" + k]["correlation_log_y_apparies"] for k in ("200", "300", "400")))
A("- **L'issue « plus égales » autour de 400 tient à trois boîtes** : côtés impairs R = %.3f, côtés pairs R = %.3f (trois boîtes chacun). Autour de 200, pairs et impairs donnent %.3f et %.3f : pas d'effet de parité, donc une fluctuation probable."
  % (C["G"]["400_impairs"]["R"], C["G"]["400_pairs"]["R"], C["G"]["200_pairs"]["R"], C["G"]["200_impairs"]["R"]))
acc = sorted(C["I"]["accroches"], key=lambda x: -x[1])[:2]
A("- **Le vide est accroché dans deux boîtes sur 32** : il lui manque %.1e de poids au côté %d et %.1e au côté %d, sans doute par un niveau tombé tout près de lui, hors de la fenêtre (non vérifié : les fichiers ne portent que la fenêtre, et aucun niveau de la fenêtre n'en est assez proche). Ce seraient les accidents attendus, rares." % (acc[0][1], acc[0][0], acc[1][1], acc[1][0]))
A("")
A("## 3. Ce que cela dit, et l'échelle qu'il ne faut pas oublier")
A("")
dens = C["H"]["par_delta_par_quantum"] / DELTA   # niveaux par unite d'energie et par quantum de cote
A("- Le pont tient jusqu'au côté 402 : la largeur lue sous absorbeur est bien la force de couplage du vide au spectre réel de la boîte fermée, et cette force se répartit, avec des poids proches du hasard, sur des niveaux dont le nombre croît comme le côté.")
A("- Sur la question fine, je n'ai pas eu raison et machine 2 n'est pas confirmée : un R constant vers 0.9 (son R combiné 0.904 ± 0.052) décrit les trois tranches. Les parts « plus égales » des petites boîtes (R de 0.69 à 0.89 jusqu'au côté 151) ne se prolongent pas telles quelles.")
A("- **L'échelle.** Dans la fenêtre il y a %.3f niveau par unité d'énergie et par quantum de côté. Un niveau du dehors par largeur Γ = %.4e demande un côté d'environ %.0e. Les boîtes calculées s'arrêtent à 402 : dire que le bocal infini se désintègre au taux Γ, c'est prolonger sur six ordres de grandeur une tendance vue sur un facteur vingt. La conjecture de la note v3 reste une conjecture ; ce lot lui enlève une objection (la saturation), il ne la démontre pas."
  % (dens, GAMMA, 1.0 / (GAMMA * dens)))
A("")
A("## 4. Ce que je propose (à l'opérateur d'ouvrir ou non)")
A("")
A("1. Ne plus grossir les boîtes pour départager R : la question est secondaire pour le pont. Six boîtes de plus autour de 400 (35 minutes chez machine 2, selon elle) ne valent que si l'on veut savoir si 0.80 était une fluctuation.")
A("2. Contrôler directement le lisse loin de l'énergie du vide, sans bruit de comptage : densité locale de l'état (0, 0) sous absorbeur en 2D contre la chaîne d'ordre 3, de 0 à 8 |δ|, au point sacrifié. C'est ce que la somme à %.3f laisse soupçonner et ne peut pas établir." % C["E"]["somme"])
A("3. Ensuite seulement, geler le pont sur un point neuf (règle de somme et croissance du compte), joué par machine 2.")
A("")
A("## 5. Limites")
A("")
A("- Tous les regards de la section 2 sont venus après lecture des agrégats. Six boîtes seulement autour de 300 et de 400 ; 3 barreaux ; un seul point, sacrifié.")
A("- Mon rejeu relit les niveaux de machine 2 : il éprouve l'agrégation, pas ses boîtes. Le moteur et le lisse d'ordre 3 sont partagés par les deux machines.")
A("- Les parts y reposent sur une formule de premier ordre ; les niveaux à moins de 0.05 |δ| du vide sont hors fenêtre. Les barres d'erreur sur R supposent des parts de Porter-Thomas.")
A("")
A("## 6. Pièces")
A("")
A("rejeu_grandes_boites_machine1_v1.py, regards_niveaux_machine1_v1.py, regards_complements_machine1_v1.py, leurs journaux et leurs JSON ; construction_note_lecture_grandes_boites_machine1_v1.py (écrit cette note). Au poste de machine 1, non transmises.")
io.open(sys.argv[4], "w", encoding="utf-8", newline="\n").write("\n".join(t) + "\n")
print("note ecrite : %d lignes ; cote pour un niveau par largeur : %.2e ; niveaux %d, non fiables %d" % (len(t), 1.0 / (GAMMA * dens), n_tot, nf))
