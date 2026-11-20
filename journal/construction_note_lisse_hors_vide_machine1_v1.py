# Ecrit la note ; chaque nombre vient des JSON nommes en argument.
# Arguments : <lecture.json> <chaine.json> <controle E.json> <regards des grandes boites.json> <complements des grandes boites.json> <sortie.md>
import sys, json, io, math
L = json.load(open(sys.argv[1])); CH = json.load(open(sys.argv[2])); CE = json.load(open(sys.argv[3])); RG = json.load(open(sys.argv[4])); CP = json.load(open(sys.argv[5]))
P = L["par_x"]; X = L["X"]
dec = (P[0]["ln_rho_2d"] - P[-1]["ln_rho_2d"]) / math.log(10)
p7 = [p for p in P if p["R3"] == L["R_min"]][0]
S, eS = CP["E"]["somme"], CP["E"]["erreur"]; Rm = L["moyenne_fenetre"]
ab = RG["AB_toutes"]; larg = [ab["bords"][i + 1] - ab["bords"][i] for i in range(8)]
def moy(idx):
    w = sum(larg[i] for i in idx); m = sum(ab["somme"][i][0] * larg[i] for i in idx) / w
    e = math.sqrt(sum((ab["somme"][i][1] * larg[i]) ** 2 for i in idx)) / w
    return m, e
m06, e06 = moy(range(6)); m68, e68 = moy((6, 7))
t = []; A = t.append
A("# Le pont — la chaîne d'ordre 3 loin de l'énergie du vide, contre la 2D sous absorbeur — note d'exploration")
A("")
A("Machine 1, 2026-11-17 (nuit). **Hors chaîne, classe 3**, point sacrifié w2 = 101/50, 3 barreaux, g = 5.53067e-03. Aucun run de machine 2, aucun gel. Ouverture de l'opérateur : « Go regarder la chaîne d'ordre 3 » (00 h 24). Attendu écrit avant le calcul (canon 5bb45d0c8081106f), rectificatif d'instrument écrit avant de calculer le rapport (c0dc8b2732ba7065). Suite de la note de lecture des grandes boîtes du même jour, dont elle corrige un soupçon.")
A("")
A("## 0. En cinq phrases")
A("")
A("1. **Mon soupçon est faux.** La chaîne d'ordre 3 rend la densité de l'état (0, 0) du système 2D ouvert à 1 pour cent près sur toute la fenêtre, de 0.05 à 8 |δ| du vide : le rapport R va de %.4f à %.4f, sur %.1f décades de densité." % (L["R_max"], L["R_min"], dec))
A("2. Attendu : A1 tient (R = %.4f au plus près du vide) ; A2 tombe (j'attendais R entre 1.05 et 1.25 à 8 |δ|, il vaut %.4f). À la lettre l'issue est (iii) : R décroît et passe sous 0.99 de %.4f à %g |δ|, moins que l'incertitude ; en substance c'est (ii), le lisse est bon."
  % (P[0]["R3"], P[-1]["R3"], 0.99 - L["R_min"], p7["x"]))
A("3. Ma spécification d'instrument (A0) ne tenait pas : aux barreaux 5 et 6 l'absorbeur réfléchit. Je l'ai remplacée, avant de calculer R, par la routine de plateau déposée du lecteur. Sous elle les quatre absorbeurs s'accordent à %.4f près, et un cinquième, reculé de 30 quanta, rend les mêmes densités à %.4f près."
  % (max(p["etendue_absorbeurs"] for p in P), CE["ecart_max"]))
A("4. Les ordres convergent aussi loin du vide : à 8 |δ| la chaîne d'ordre 1 est à %+.1f pour cent de la 2D, l'ordre 2 à %+.1f, l'ordre 3 à %+.1f."
  % (100 * (1 / P[-1]["R1"] - 1), 100 * (1 / P[-1]["R2"] - 1), 100 * (1 / P[-1]["R3"] - 1)))
A("5. L'excès de la somme des grandes boîtes (%.3f ± %.3f) ne vient donc pas du lisse. Rapporté à la 2D ouverte il vaut %.3f, à %.1f écarts types de 1 ; il est porté par les deux dernières tranches d'écart (6 à 8 |δ|). Il reste inexpliqué."
  % (S, eS, S / Rm, (S / Rm - 1) / (eS / Rm)))
A("")
A("## 1. Ce qui est calculé")
A("")
A("Densité locale de (0, 0) sous absorbeur à l'énergie E, lue par le flux : ρ = (η/π) Σ W |x|², x = (E − H + iηW)⁻¹ e₍₀,₀₎, E pris à écart égal du vide de chaque système.")
A("- **Chaîne** : blocs déposés d'ordre 2 et 3, dix-huit variantes de l'absorbeur adapté, médiane des logarithmes. Recoupements : largeur au vide %.4e (note v3 : 3.2661e-09) ; rapports ordre 1 sur ordre 3 du tableau de la note v3 retrouvés ; la forme directe −Im G₀₀/π, celle des grandes boîtes, égale la forme par flux à %.0e près."
  % (math.exp(CH["ordres"]["3"]["ln_Gamma_vide"]), max(CH["ordres"][o]["direct_contre_flux_max"] for o in "123")))
A("- **2D** : hamiltonien, absorbeurs A, B, C, D et lecture du vide du bloc « lecteur creux » déposé (canon contrôlé), boîtes de 104 à 124 quanta de côté, barreaux k = −3 à 8 ; seule la résolution à énergie fixée est neuve. Poids du vide w0 = %.8f. Au vide, le plateau 2D et la chaîne d'ordre 3 s'accordent à %.5f près en logarithme sous A, B et D."
  % (L["w0"], max(abs(CH["ordres"]["3"]["ln_Gamma_vide"] - math.log(L["absorbeurs"][a]["plateau_vide"]["val"])) for a in "ABD")))
A("- R(x) = ρ_2D(x) / (w0 ρ_chaîne(x)). La somme / largeur des grandes boîtes est, en moyenne, la moyenne de R sur la fenêtre multipliée par ce que la boîte fermée ajoute ou retire au système ouvert.")
A("")
A("## 2. Résultat")
A("")
A("| écart au vide (|δ|) | log₁₀ ρ 2D | R, ordre 3 | R, ordre 2 | R, ordre 1 | étendue entre absorbeurs 2D | étendue entre variantes de la chaîne |")
A("|---|---|---|---|---|---|---|")
for p in P:
    A("| %g | %.2f | %.4f | %.4f | %.4f | %.4f | %.4f |" % (p["x"], p["ln_rho_2d"] / math.log(10), p["R3"], p["R2"], p["R1"], p["etendue_absorbeurs"], p["etendue_chaine3"]))
A("")
A("Moyenne de R (ordre 3) sur la fenêtre, uniforme en écart : %.4f ; pente %+.4f par |δ|. L'écart à 1 (au plus %.4f) est du même ordre que ce que l'absorbeur de la chaîne laisse indéterminé (étendue des dix-huit variantes : jusqu'à %.4f) : la chaîne d'ordre 3 n'est pas distinguée de la 2D ouverte au-delà de cette étendue."
  % (Rm, L["pente"], max(abs(p["R3"] - 1) for p in P), max(p["etendue_chaine3"] for p in P)))
A("")
A("## 3. L'attendu, appliqué")
A("")
A("- **A0 tel qu'écrit (barreaux 0 à 6, quatre absorbeurs, étendue ≤ 0.02) : ne tient pas.** L'étendue va de %.2f à %.2f selon l'écart. Cause : aux barreaux faibles (5, 6 et au-delà) la densité oscille avec l'écart, signe de réflexion ; sous C (forme F1) le bord fort se dégrade aussi. Défaut de ma spécification, pas de la lecture : je n'avais pas repris la règle de plateau du lecteur." % (min(L["A0_tel_qu_ecrit"]), max(L["A0_tel_qu_ecrit"])))
A("- **Règle de remplacement, fixée avant R** : routine de plateau déposée (cinq barreaux consécutifs de plus petit rapport, plateau si le rapport est au plus 1.05), par absorbeur ; médiane des quatre ; lisible si les quatre rendent un plateau et s'accordent à 0.02. Lisible aux douze écarts.")
A("- **A1 : tient.** **A2 : ne tient pas.** **Issue : (iii) à la lettre, (ii) en substance.** Je m'étais donné 0.50 pour (i), 0.30 pour (ii), 0.20 pour (iii) : la moitié de ma mise était sur la mauvaise issue.")
A("- Contrôle venu après : un absorbeur de forme F2 dont le bord est reculé de 30 (boîte de %d) rend les densités de la médiane à %.4f près. La densité ouverte ne dépend pas de l'endroit où l'on absorbe, de 24 à 54 quanta." % (CE["N"], CE["ecart_max"]))
A("")
A("## 4. Ce que cela dit")
A("")
A("- La chaîne d'ordre 3 n'avait été jugée qu'à l'énergie du vide (gels des deltas 100 et 102). Ici, hors gel et sur un seul point, elle tient à 1 pour cent près jusqu'à 8 |δ| du vide, là où la densité a perdu plus de douze décades. Le lisse que les deux machines partagent pour les grandes boîtes est maintenant confronté à un objet 2D indépendant de la chaîne (même moteur).")
A("- **La somme des grandes boîtes.** Tranches d'écart de 0.05 à 6 |δ| : %.2f ± %.2f ; de 6 à 8 |δ| : %.2f ± %.2f (32 boîtes, erreurs indicatives). Or R y vaut 0.99. L'excès n'est donc ni le lisse ni, d'après les deux lectures indépendantes de machine 2, une erreur numérique sur les petites parts. Restent : une fluctuation (2 à 3 écarts types ; sept des huit échantillons de la note v3 étaient déjà au-dessus de 1, comme les trois tranches de machine 2), ou un effet propre à la boîte fermée que je ne sais pas nommer. Je ne tranche pas."
  % (m06, e06, m68, e68))
A("- La phrase de ma note de lecture des grandes boîtes, « le lisse de la chaîne d'ordre 3 serait un peu bas loin de l'énergie du vide », est retirée : c'est le contraire, de 1 pour cent au plus.")
A("")
A("## 5. Ce que je propose (à l'opérateur d'ouvrir ou non)")
A("")
A("1. Pour l'excès de la somme, la seule épreuve nette est le nombre : quatre-vingts boîtes neuves autour du côté 200 (environ une heure et quart chez machine 2 au rythme de ses journaux) ramènent l'erreur à 0.01. Attendu à écrire avant ; c'est elle qui lance.")
A("2. Le pont a maintenant ses trois appuis vérifiés au point sacrifié : la chaîne vaut la 2D ouverte dans toute la fenêtre, la force se retrouve dans la boîte fermée, elle se partage sur un nombre de niveaux qui croît. L'étape qui compte ensuite est de le geler sur un point neuf.")
A("")
A("## 6. Limites")
A("")
A("- Un seul point (sacrifié), une seule profondeur (3 barreaux), un seul côté du vide (opposé à δ). La chaîne et la 2D partagent le moteur : l'accord éprouve la réduction à une dimension et les absorbeurs, pas le moteur.")
A("- A0 a été remplacé en cours de route ; la règle de remplacement existait (elle est déposée) et a été fixée avant de rapprocher la 2D de la chaîne, mais après avoir vu les densités 2D.")
A("- Le contrôle par l'absorbeur reculé et la lecture par tranches de la somme sont venus après la lecture.")
A("")
A("## 7. Pièces (au poste de machine 1, non transmises)")
A("")
A("attendu_lisse_hors_vide_machine1_v1.txt, rectificatif_instrument_lisse_hors_vide_machine1_v1.txt ; lisse_chaine_machine1_v1.py, lisse_2d_machine1_v1.py, lecture_lisse_hors_vide_machine1_v1.py, controle_absorbeur_recule_machine1_v1.py, leurs journaux et leurs JSON ; construction_note_lisse_hors_vide_machine1_v1.py (écrit cette note). Registre lu à la tête 2988237 (delta 102), non écrit.")
io.open(sys.argv[6], "w", encoding="utf-8", newline="\n").write("\n".join(t) + "\n")
print("note ecrite : %d lignes ; decades %.2f ; somme rapportee %.3f, %.2f ecarts types ; tranches %.3f+-%.3f et %.3f+-%.3f" % (len(t), dec, S / Rm, (S / Rm - 1) / (eS / Rm), m06, e06, m68, e68))
