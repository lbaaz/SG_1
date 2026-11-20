# -*- coding: utf-8 -*-
"""Écrit la v2 de la note du pont depuis les sorties des scripts (aucun nombre tapé à la main).
Usage : python3 -I -B construction_note_pont_machine1_v2.py <dossier des sorties du pont> <sortie.md>"""
import sys, os, json, math, statistics
import numpy as np
D, SORTIE = sys.argv[1:3]
def J(nom): return json.load(open(os.path.join(D, nom)))
S = J("pont_semiclassique_v1.json"); DG = J("pont_degres_v1.json"); LO = J("pont_lisse_ordres_v1.json"); SA = J("pont_sauts_regard_v1.json")
SAC = [J(n) for n in ("pont_2d_sacrifie_v1.json", "pont_2d_sacrifie_m3_v1.json", "pont_2d_sacrifie_m4_v1.json", "pont_2d_sacrifie_m5_v1.json")]
F1 = J("pont_2d_force_m3_v1.json"); F = {3: J("pont_2d_force_m3_v2.json"), 4: J("pont_2d_force_m4_v2.json"), 5: J("pont_2d_force_m5_v2.json")}
GC = J("pont_2d_grand_controle64_v1.json"); GR = {3: J("pont_2d_grand_m3_v1.json"), 4: J("pont_2d_grand_m4_v1.json"), 5: J("pont_2d_grand_m5_v1.json")}; G200 = J("pont_2d_grand_m3_cote200_v1.json")
L = []; W = L.append
def f(x, n=3): return ("%%.%df" % n) % x
def s(x, n=4): return ("%%+.%df" % n) % x
A2_MIN, A2_MAX = -0.05, 0.03        # attendu du regard 2D, tel qu'écrit dans pont_2d_sacrifie_machine1_v1.py avant le calcul
A3_MIN, A3_MAX = 0.85, 1.15         # attendu de la statistique repondérée, tel qu'écrit dans pont_2d_force_machine1_v2.py avant de lancer
A1 = 0.03                           # attendu des degrés, tel qu'écrit dans pont_degres_machine1_v1.py
for nom, motif in (("pont_2d_sacrifie_machine1_v1.py", "-0.05 <= ln( V^2 T / Gamma ) <= +0.03"), ("pont_2d_force_machine1_v2.py", "entre 0.85 et 1.15"), ("pont_degres_machine1_v1.py", "<= 0.03")):
    assert motif in open(os.path.join(D, nom), encoding="ascii").read(), (nom, motif)

W("# Le pont entre la largeur sous absorbeur et le système fermé — note d'exploration, v2")
W("")
W("Machine 1, 2026-11-16 (soir). **Hors chaîne, classe 3.** Aucun run de machine 2, aucun gel, machine 2 non consultée. Cette v2 remplace la v1 (qui reste au projet) : elle corrige un signe et ajoute quatre regards (autres degrés, boîte 2D fermée, règle de somme, grandes boîtes). Ouvertures de l'opérateur : « On peut avancer sur la recherche là ? » (21 h 39), puis « Ouvre ! on cherche ! » (21 h 55).")
W("")
W("## 0. Défaut de la v1, déclaré")
W("")
tous = [x for c in S["cellules"] for x in c["croisements"]]; lr = [x["ln_R_T"] for x in tous]
W("Le tableau de la v1 donnait ln(V²T/Γ) de +%s à +%s. Le signe est faux : V²T est SOUS Γ, de %s à %s en logarithme. Cause : le script de construction changeait le signe du champ lu. Le texte de la v1 ne dépendait pas du signe ; le tableau ci-dessous est le bon." % (f(min(abs(v) for v in lr), 4), f(max(abs(v) for v in lr), 4), s(min(lr)), s(max(lr))))
W("")
W("## 1. Chaîne fermée : Γ = V² · T")
W("")
W("La chaîne fermée (coupée au site N, sans absorbeur) est réelle symétrique : aucune largeur. Quand on fait défiler la condition de bord au bout de la chaîne, le vide subit un croisement évité de demi-écart V avec un niveau du dehors. T est le temps classique d'aller et retour entre la sortie de la barrière et le bout de la chaîne, T(E) = 2 ∫ dm / √(4 t(m)² − (E − m δ)²), calculé sur les sauts du moteur sans rien lire du spectre. Sur %d croisements (les 16 cellules lisibles du gel « largeur du vide », premier ordre, coupures N de %d à %d) :" % (len(tous), min(x["N"] for x in tous), max(x["N"] for x in tous)))
W("")
W("| barreaux | Γ sous absorbeur (de … à) | V (de … à) | 2π / (T·|δ|) | ln(V²T / Γ) (de … à) |")
W("|---|---|---|---|---|")
par_m = {}
for c in S["cellules"]:
    par_m.setdefault(c["m_bord"], []).extend((c, x) for x in c["croisements"])
for m in sorted(par_m):
    X = par_m[m]; G = [math.exp(c["ln_G_absorbeur_ordre1"]) for c, _ in X]; V = [x["V"] for _, x in X]; dt = [x["D_T"] / abs(c["delta"]) for c, x in X]; l = [x["ln_R_T"] for _, x in X]
    W("| %d | %.1e … %.1e | %.1e … %.1e | %s … %s | %s … %s |" % (m, min(G), max(G), min(V), max(V), f(min(dt)), f(max(dt)), s(min(l)), s(max(l))))
W("")
lv = [x["ln_R_voisins"] for x in tous]
W("Rappel de la v1 : l'attendu écrit AVANT le premier calcul (règle d'or avec l'espacement des niveaux voisins) est tombé, de %s à %s en logarithme ; la lecture par le temps classique est venue APRÈS avoir vu les nombres." % (s(min(lv), 3), s(max(lv), 3)))
W("")
W("**Épreuve hors échantillon : d'autres degrés.** Attendu écrit avant de lancer : %s. Point w2 = %s, couplage fixé par la même règle à chaque degré, premier ordre." % (DG["attendu"], DG["w2"]))
W("")
W("| degré p | barreaux | croisements retenus | 2π / (T·|δ|) | ln(V²T / Γ) (de … à) | étendue de l'absorbeur (de … à) |")
W("|---|---|---|---|---|---|")
bons = [x for x in DG["cas"] if 0.4 <= min(x["poids"]) and max(x["poids"]) <= 0.6]; faux = [x for x in DG["cas"] if x not in bons]
cles = sorted(set((x["p"], x["m_voulu"]) for x in DG["cas"])); tenus = 0
for p, m in cles:
    X = [x for x in bons if (x["p"], x["m_voulu"]) == (p, m)]
    if not X:
        W("| %d | %d | 0 | — | — | — |" % (p, m)); continue
    l = [x["ln_V2T_sur_G"] for x in X]; dt = [x["D_T_sur_delta"] for x in X]; e = [x["etendue"] for x in X]; tenus += sum(1 for v in l if abs(v) <= A1)
    W("| %d | %d | %d | %s … %s | %s … %s | %s … %s |" % (p, m, len(X), f(min(dt), 2), f(max(dt), 2), s(min(l)), s(max(l)), f(min(e), 4), f(max(e), 4)))
W("")
fx = sorted(set((x["p"], x["m_voulu"], x["N"]) for x in faux)); vfaux = [x["V"] for x in faux]; vbon9 = [x["V"] for x in bons if (x["p"], x["m_voulu"]) == (9, 6)]
W("Sur %d croisements rendus, %d sont retenus, dont %d respectent l'attendu. Écartés : %d faux croisements, tous au degré %s, %s barreaux (coupures %s) : les deux états n'y portent pas chacun la moitié du vide, et le demi-écart rendu (%.1e) n'a rien d'un couplage sous barrière ; le seul croisement lisible de cette case donne V = %.1e, au bord de la double précision. Défaut du chercheur de croisement, qui n'avait pas de garde ; le filtre appliqué ici (chacun des deux poids entre 0.4 et 0.6) est venu après lecture. Au degré 3 l'étendue de l'absorbeur dépasse l'écart mesuré : l'épreuve y est faible." % (
    len(DG["cas"]), len(bons), tenus, len(faux), ", ".join(sorted(set(str(a[0]) for a in fx))), ", ".join(sorted(set(str(a[1]) for a in fx))), ", ".join(str(a[2]) for a in fx), max(vfaux), min(vbon9)))
W("")
W("**Antériorité.** Lire une largeur dans les croisements évités d'un spectre réel, en faisant varier un paramètre de boîte, est la méthode de stabilisation de la chimie quantique (Hazi et Taylor, Phys. Rev. A 1, 1109, 1970) ; la relation Γ = 2π V² × densité de niveaux, avec une densité T/2π pour un seul canal, en est la forme élémentaire. Rien de neuf dans le principe. Ce qui est à nous : le nombre, sur le vide fantôme, avec un T classique fini quelle que soit la longueur de la chaîne. Que la largeur soit portée par plusieurs états quasi discrets voisins, et non par un seul croisement, est aussi relevé dans cette littérature (Kaprálová-Žďánská, arXiv:2004.06372, résumé seul lu) : c'est ce que la section 3 retrouve en 2D. Références relevées par une recherche rapide ce soir, non lues en entier ; la note d'antériorité n'en dit rien encore.")
W("")
W("## 2. Boîte 2D fermée, au point sacrifié")
W("")
g_ = {b["m_bord"]: (b["g"], b["Gamma_chaine_ordre3"]) for b in SAC}
W("Point w2 = %s. C'est un centième, exclu de tout tirage ; il est **sacrifié** pour tout gel futur sur le système fermé, puisque machine 1 y a lu la 2D. Cellules : %s. Boîte carrée en quanta (N × N), paroi dure, potentiel u sur le dernier site de l'échelle du vide pour faire défiler le bord ; diagonalisation complète. Γ : plateau de la chaîne d'ordre 3 sous absorbeur adapté." % (
    SAC[0]["w2"], " ; ".join("%d barreaux, g = %s, Γ = %.4e" % (m, g_[m][0], g_[m][1]) for m in sorted(g_))))
W("")
W("Attendu écrit AVANT de regarder : %s ≤ ln(V²T/Γ) ≤ %s dans la boîte 2D, comme dans la chaîne." % (s(A2_MIN, 2), s(A2_MAX, 2)))
W("")
W("| barreaux | côté N | site de coupure M | V trouvé (2D) | V attendu √(Γ/T) | ln(V²T/Γ) 2D | chaîne fermée ordre 1 | chaîne fermée ordre 3 | attendu |")
W("|---|---|---|---|---|---|---|---|---|")
lignes = []
for b in SAC:
    for x in b["boites"]:
        G = b["Gamma_chaine_ordre3"]; lg = lambda cle: (math.log(x[cle][0]["V"] ** 2 * x["T"] / G) if x[cle] else None); l2, l1, l3 = lg("boite_2d"), lg("chaine_ordre1"), lg("chaine_ordre3")
        lignes.append((b["m_bord"], x["N"], x["M"], x["boite_2d"][0]["V"], x["V_attendu"], l2, l1, l3, A2_MIN <= l2 <= A2_MAX))
for a in sorted(lignes):
    W("| %d | %d | %d | %.3e | %.3e | %s | %s | %s | %s |" % (a[0], a[1], a[2], a[3], a[4], s(a[5]), s(a[6]) if a[6] is not None else "pas de croisement trouvé", s(a[7]) if a[7] is not None else "pas de croisement trouvé", "tient" if a[8] else "**faussé**"))
W("")
nt = sum(1 for a in lignes if a[8]); pires = max(lignes, key=lambda a: abs(a[5])); chv = [abs(v) for a in lignes for v in (a[6], a[7]) if v is not None]; chmax = max(chv); manq = sum(1 for a in lignes for v in (a[6], a[7]) if v is None)
W("**L'attendu est faussé dans %d boîtes sur %d.** Il tient dans %d boîtes (%s) ; dans les autres, V est trop petit, jusqu'à un facteur %.1f, soit %.0f sur V² (côté %d, %d barreaux). L'en-tête des deux scripts de la règle de somme dit « 4 boîtes sur 7 » : erreur de décompte de la plume, le compte est celui du tableau. Les chaînes fermées coupées au même site restent à %s près en logarithme (%d lectures ; %d sans croisement trouvé par le balayage). La boîte 2D fermée n'est donc pas la chaîne fermée dès que la boîte grandit." % (
    len(lignes) - nt, len(lignes), nt, " ; ".join("côté %d à %d barreaux" % (a[1], a[0]) for a in sorted(lignes) if a[8]), math.exp(-pires[5] / 2.0), math.exp(-pires[5]), pires[1], pires[0], f(chmax, 3), len(chv), manq))
W("")
W("## 3. Où est passée la force ?")
W("")
W("Deux lectures : le couplage est PERDU (la largeur sous absorbeur ne dirait alors rien de la boîte fermée), ou il est PARTAGÉ entre plusieurs niveaux du dehors. Dans la boîte fermée nue, chaque niveau k du dehors porte un poids c_k² sur l'état (0, 0), et son couplage au vide est V_k² = c_k² (E_k − E_vide)² / poids du vide (premier ordre, loin du croisement). Sous absorbeur la même grandeur est lisse : Γ(E)/2π = (E − E_vide)² ρ(E), ρ étant la densité locale de (0, 0) dans la chaîne d'ordre 3.")
W("")
tot1 = sum(F1["moyennes"]["2d"]) / sum(F1["lisse"]); r1 = [F1["moyennes"]["2d"][i] / F1["lisse"][i] for i in range(len(F1["lisse"]))]
W("**Première passe (somme brute par fenêtre, %d barreaux, côtés %d à %d).** Rapport d'ensemble %s, mais par fenêtre de %s à %s : Γ(E) perd près d'une décade par |δ|, si bien que la somme est dominée par un ou deux niveaux. Défaut déclaré de cette passe : la densité lisse sortait avec le mauvais signe (résolvante prise à l'envers), corrigé avant relecture, les rapports n'en dépendant pas en valeur absolue ; et elle était prise à énergie absolue égale au lieu d'écart au vide égal (effet de l'ordre du centième de |δ|), corrigé dans la seconde passe." % (3, F1["boites"][0]["N"], F1["boites"][-1]["N"], f(abs(tot1)), f(min(abs(v) for v in r1)), f(max(abs(v) for v in r1))))
W("")
W("**Seconde passe (statistique repondérée).** Chaque niveau k porte une largeur d'énergie y_k = c_k² / (poids du vide × ρ(E_k)), comptée en |δ|. Si la force est partagée et non perdue, la somme des y_k sur une fenêtre vaut la largeur de la fenêtre, quel que soit le nombre de niveaux. Fenêtre : de %s à %s |δ| du vide, du côté opposé à δ (aucun état localisé sous la barrière n'y tombe)." % (f(F[3]["bornes"][0], 2), f(F[3]["bornes"][-1], 0)))
W("")
W("Attendu écrit AVANT de lancer : somme / largeur entre " + f(A3_MIN, 2) + " et " + f(A3_MAX, 2) + " pour la boîte 2D, à 3 barreaux pour les côtés 46 à 64, à 4 et à 5 barreaux pour les côtés 21 à 45 ; même bande pour la chaîne d'ordre 3 ; et le nombre de niveaux 2D par boîte croît avec le côté alors que celui de la chaîne ne croît pas. Les côtés 21 à 45 à 3 barreaux étaient déjà lus : ils ne comptent pas comme épreuve.")
W("")
W("| échantillon | boîtes | 2D : somme / largeur | chaîne ordre 3 | chaîne ordre 1 | niveaux par boîte, 2D | chaîne ordre 3 | participation 2D | épreuve |")
W("|---|---|---|---|---|---|---|---|---|")
ech = [(3, "N <= 45", "3 barreaux, côtés 21 à 45", "déjà lu"), (3, "N >= 46", "3 barreaux, côtés 46 à 64", None), (4, "toutes", "4 barreaux, côtés 21 à 45", None), (5, "toutes", "5 barreaux, côtés 21 à 45", None)]; ep = []
for m, cle, nom, deja in ech:
    b = F[m]["bilans"][cle]; d2, c3, c1 = b["boite 2D"], b["chaine ordre 3"], b["chaine ordre 1"]; ok = A3_MIN <= d2["moyenne"] <= A3_MAX
    if not deja:
        ep.append((d2["moyenne"], d2["erreur_type"], ok, c3["moyenne"]))
    W("| %s | %d | %s ± %s | %s ± %s | %s ± %s | %s | %s | %s | %s |" % (nom, d2["boites"], f(d2["moyenne"]), f(d2["erreur_type"]), f(c3["moyenne"]), f(c3["erreur_type"]), f(c1["moyenne"]), f(c1["erreur_type"]), f(d2["niveaux_par_boite"], 2), f(c3["niveaux_par_boite"], 2), f(d2["participation"], 2), deja or ("tient" if ok else "**faussé**")))
W("")
pw = sum(1.0 / e[1] ** 2 for e in ep); mp_ = sum(e[0] / e[1] ** 2 for e in ep) / pw
W("L'attendu tient aux %d épreuves sur %d. Moyenne pondérée des trois : %s ± %s. La barre d'erreur est l'écart type entre boîtes divisé par la racine de leur nombre ; elle suppose des boîtes indépendantes, ce qu'elles ne sont pas tout à fait (deux côtés consécutifs partagent le même site de coupure : pour les chaînes, qui ne dépendent que de ce site, la barre est sous-estimée d'un facteur racine de 2)." % (sum(1 for e in ep if e[2]), len(ep), f(mp_), f(1.0 / math.sqrt(pw))))
W("")
W("**La statistique voit-elle quelque chose ? Contrôle par l'ordre 1.** Sans bruit (deux chaînes sous absorbeur, à écart au vide égal), la densité lisse de l'ordre 1 rapportée à celle de l'ordre 3 vaut :")
W("")
W("| écart au vide, en |δ| | " + " | ".join(f(x, 2) for x in LO["points"][0]["x"]) + " |")
W("|---|" + "---|" * len(LO["points"][0]["x"]))
for pt in LO["points"]:
    W("| g = %s | " % pt["g"] + " | ".join(f(v) for v in pt["rho1_sur_rho3"]) + " |")
W("")
contre1 = {}
for m in (3, 4, 5):
    pt = [p for p in LO["points"] if float(p["g"]) == float(F[m]["g"])][0]; tots = []
    for b in F[m]["boites"]:
        tots.append(sum(x[2] / float(np.interp(x[0], pt["x"], pt["rho1_sur_rho3"])) for x in b["niveaux_2d"]) / (F[m]["bornes"][-1] - F[m]["bornes"][0]))
    contre1[m] = (sum(tots) / len(tots), statistics.pstdev(tots) / math.sqrt(len(tots)))
moy1 = [1.0 / (len(pt["x"]) - 1) * sum(0.5 * (pt["rho1_sur_rho3"][i] + pt["rho1_sur_rho3"][i + 1]) * (pt["x"][i + 1] - pt["x"][i]) for i in range(len(pt["x"]) - 1)) * (len(pt["x"]) - 1) / (pt["x"][-1] - pt["x"][0]) for pt in LO["points"]]
W("Les deux ordres s'accordent au vide (c'est là que le gel les a jugés) et s'écartent en s'en éloignant : en moyenne sur la fenêtre, l'ordre 1 vaut %s à %s de l'ordre 3. La chaîne FERMÉE d'ordre 1 lit %s (voir le tableau) : la statistique voit donc une différence réelle de cet ordre. Rapportée au lisse d'ordre 1, la boîte 2D donnerait %s. **La boîte 2D fermée se range avec l'ordre 3**, y compris loin de l'énergie du vide, où aucun gel n'a rien jugé." % (
    f(min(moy1), 2), f(max(moy1), 2), ", ".join(f(F[m]["bilans"]["toutes"]["chaine ordre 1"]["moyenne"]) for m in (3, 4, 5)), ", ".join("%s ± %s (%d barreaux)" % (f(contre1[m][0]), f(contre1[m][1]), m) for m in (3, 4, 5))))
W("")
W("**Le dehors se peuple quand la boîte grandit** (3 barreaux, côtés 21 à 64) :")
W("")
W("| côtés | boîtes | 2D : somme / largeur | niveaux 2D par boîte | niveaux de la chaîne | participation 2D | plus petite part y | part médiane |")
W("|---|---|---|---|---|---|---|---|")
B = F[3]["boites"]; LARG = F[3]["bornes"][-1] - F[3]["bornes"][0]
for a, b in ((21, 27), (28, 34), (35, 41), (42, 48), (49, 56), (57, 64)):
    bs = [x for x in B if a <= x["N"] <= b]; s2 = [sum(v[2] for v in x["niveaux_2d"]) / LARG for x in bs]; n2 = [len(x["niveaux_2d"]) for x in bs]; n3 = [len(x["niveaux_ch3"]) for x in bs]
    pa = [sum(v[2] for v in x["niveaux_2d"]) ** 2 / sum(v[2] ** 2 for v in x["niveaux_2d"]) for x in bs if x["niveaux_2d"]]; ys = sorted(v[2] for x in bs for v in x["niveaux_2d"])
    W("| %d à %d | %d | %s | %s | %s | %s | %.2g | %.2g |" % (a, b, len(bs), f(sum(s2) / len(s2), 2), f(sum(n2) / len(n2), 2), f(sum(n3) / len(n3), 2), f(sum(pa) / len(pa), 2), ys[0], ys[len(ys) // 2]))
W("")
Ns = [x["N"] for x in B]; c2 = np.polyfit(Ns, [len(x["niveaux_2d"]) for x in B], 1); c3 = np.polyfit(Ns, [len(x["niveaux_ch3"]) for x in B], 1)
seuil = {float(p["g"]): p["seuils"]["0.50"] for p in SA["points"]}; debut = {}
for m in (3, 4, 5):
    debut[m] = min(x["N"] for x in F[m]["boites"] if len(x["niveaux_2d"]) >= 3)
ty = sorted(v[2] for x in B for v in x["niveaux_2d"]); tr = [(21, 27), (57, 64)]; nn = [sum(len(x["niveaux_2d"]) for x in B if a <= x["N"] <= b) / float(sum(1 for x in B if a <= x["N"] <= b)) for a, b in tr]
sl = [sum(sum(v[2] for v in x["niveaux_2d"]) / LARG for x in B if a <= x["N"] <= b) / float(sum(1 for x in B if a <= x["N"] <= b)) for a, b in ((21, 27), (28, 34), (35, 41), (42, 48), (49, 56), (57, 64))]
W("Droite ajustée du nombre de niveaux selon le côté : pente %s par quantum en 2D, %s pour la chaîne. La somme reste entre %s et %s pendant que le nombre de niveaux par boîte est multiplié par %s : la force se partage. Le partage est très inégal (la plus petite part vaut %.1e fois la médiane), ce qui explique qu'un croisement pris au hasard puisse être très étroit, comme au côté 41 de la section 2." % (
    s(float(c2[0]), 3), s(float(c3[0]), 3), f(min(sl), 2), f(max(sl), 2), f(nn[1] / nn[0], 1), ty[0] / ty[len(ty) // 2]))
W("")
W("Où cela commence : un troisième niveau apparaît dans la fenêtre au côté %s (3, 4, 5 barreaux). Les sauts de l'échelle atteignent 0.5 — la moitié du désaccord d'une unité qui sépare l'échelle du vide de ses voisines — au site %s, soit au côté %s. Le dehors cesse d'être une échelle unique à peu près là où les échelles voisines s'ouvrent ; lecture cohérente, non éprouvée autrement." % (
    ", ".join(str(debut[m]) for m in (3, 4, 5)), ", ".join(str(seuil[float(F[m]["g"])]) for m in (3, 4, 5)), ", ".join(str(2 * seuil[float(F[m]["g"])] + 1) for m in (3, 4, 5))))
W("")
W("## 4. Boîtes plus grandes : le dehors continue-t-il de se peupler ?")
W("")
W("La conjecture de la section 5 repose sur la poursuite de cette croissance. Au-delà du côté 64 la diagonalisation complète est trop lourde : décalage-inversion creuse autour de la fenêtre, chaque boîte résolue deux fois (décalages à 2 et à 5 |δ| sous le vide), un niveau n'étant compté fiable que si ses deux lectures de y s'accordent à 2 pour cent près. Contrôle : aux côtés %s la méthode creuse rend ce que rend la diagonalisation complète (%s)." % (
    " et ".join(str(b["N"]) for b in sorted(GC["boites"], key=lambda b: b["N"])),
    " ; ".join("côté %d : %d niveaux et somme %s contre %d et %s" % (b["N"], b["n"], f(b["somme_sur_largeur"]), len(d["niveaux_2d"]), f(sum(v[2] for v in d["niveaux_2d"]) / LARG)) for b in sorted(GC["boites"], key=lambda b: b["N"]) for d in F[3]["boites"] if d["N"] == b["N"])))
W("")
W("| barreaux | côté | états | niveaux dans la fenêtre | non fiables | somme / largeur | participation | plus petite part y |")
W("|---|---|---|---|---|---|---|---|")
tg = [(m, b) for m in (3, 4, 5) for b in GR[m]["boites"]] + [(3, b) for b in G200["boites"]]
for m, b in sorted(tg, key=lambda a: (a[0], a[1]["N"])):
    W("| %d | %d | %d | %d | %d | %s | %s | %.2g |" % (m, b["N"], b["N"] ** 2, b["n"], b["non_fiables"], f(b["somme_sur_largeur"]), f(b["participation"], 2), min(v[1] for v in b["niveaux"])))
W("")
def moy(l): return sum(l) / float(len(l))
def sel(m, cotes, cle, src=None): return [b[cle] for b in (src or GR[m])["boites"] if b["N"] in cotes]
p5764 = moy([sum(v[2] for v in x["niveaux_2d"]) ** 2 / sum(v[2] ** 2 for v in x["niveaux_2d"]) for x in B if 57 <= x["N"] <= 64])
src1 = open(os.path.join(D, "pont_2d_grand_machine1_v1.py"), encoding="ascii").read(); src2 = open(os.path.join(D, "attendu_grand_m4_m5_cote200_machine1_v1.txt"), encoding="ascii").read()
for motif, src in (("entre 9 et 15 niveaux", src1), ("entre 0.85 et 1.15", src1), ("superieure a celle des cotes 57 a 64", src1), ("entre 8 et 12 niveaux", src2), ("entre 7 et 12 niveaux", src2), ("entre 0.85 et 1.15", src2), ("entre 12 et 19 niveaux", src2), ("entre 0.7 et 1.3", src2)):
    assert motif in src, motif
att = [("3 barreaux, côtés 150 et 151 : entre 9 et 15 niveaux (droite prolongée ; 6 ou moins aurait fait tomber la conjecture)", moy(sel(3, (150, 151), "n")), 9, 15, 1),
       ("3 barreaux, côtés 72 à 151 : somme / largeur moyenne entre 0.85 et 1.15", moy([b["somme_sur_largeur"] for b in GR[3]["boites"] if b["N"] >= 72]), 0.85, 1.15, 3),
       ("3 barreaux, côtés 128 à 151 : participation au-dessus de celle des côtés 57 à 64 (%s)" % f(p5764, 2), moy([b["participation"] for b in GR[3]["boites"] if b["N"] >= 128]), p5764, float("inf"), 2),
       ("4 barreaux, côtés 150 et 151 : entre 8 et 12 niveaux", moy(sel(4, (150, 151), "n")), 8, 12, 1),
       ("5 barreaux, côtés 150 et 151 : entre 7 et 12 niveaux", moy(sel(5, (150, 151), "n")), 7, 12, 1),
       ("4 barreaux, six boîtes : somme / largeur moyenne entre 0.85 et 1.15", moy([b["somme_sur_largeur"] for b in GR[4]["boites"]]), 0.85, 1.15, 3),
       ("5 barreaux, six boîtes : somme / largeur moyenne entre 0.85 et 1.15", moy([b["somme_sur_largeur"] for b in GR[5]["boites"]]), 0.85, 1.15, 3),
       ("4 barreaux : aucun niveau non fiable", float(sum(b["non_fiables"] for b in GR[4]["boites"])), 0, 0, 0),
       ("3 barreaux, côtés 200 et 201 : entre 12 et 19 niveaux", moy([b["n"] for b in G200["boites"]]), 12, 19, 1),
       ("3 barreaux, côtés 200 et 201 : somme / largeur moyenne entre 0.7 et 1.3", moy([b["somme_sur_largeur"] for b in G200["boites"]]), 0.7, 1.3, 3)]
W("Attendus écrits AVANT chaque lancement (en-tête de pont_2d_grand_machine1_v1.py, puis attendu_grand_m4_m5_cote200_machine1_v1.txt), et ce qui est sorti :")
W("")
W("| attendu | lu | verdict |")
W("|---|---|---|")
na = 0
for txt, v, lo, hi, nd in att:
    ok = lo <= v <= hi; na += 1 if ok else 0; W("| %s | %s | %s |" % (txt, f(v, nd), "tient" if ok else "**faussé**"))
W("")
tousN = [(x["N"], len(x["niveaux_2d"])) for x in B] + [(b["N"], b["n"]) for b in GR[3]["boites"]] + [(b["N"], b["n"]) for b in G200["boites"]]; cg = np.polyfit([a[0] for a in tousN], [a[1] for a in tousN], 1)
pc = [(c, moy([b["participation"] for b in list(GR[3]["boites"]) + list(G200["boites"]) if b["N"] in c])) for c in ((96, 97), (128, 129), (150, 151), (200, 201))]
W("Les %d attendus tiennent sur %d. À 3 barreaux, la droite ajustée sur tous les côtés de 21 à 201 a une pente de %s niveau par quantum : le compte croît toujours, un peu moins vite que sur les seuls côtés 21 à 64. Le compte dépend peu de la profondeur (%s niveaux en moyenne aux côtés 150 et 151, à 3, 4, 5 barreaux). **La participation croît moins nettement que le compte** : %s contre %s aux côtés 57 à 64 ; entre 150 et 200 elle ne monte plus de façon lisible, sur deux boîtes seulement. Le nombre de niveaux qui portent vraiment la force pourrait donc croître moins vite que le nombre de niveaux présents — point ouvert." % (
    na, len(att), s(float(cg[0]), 3), ", ".join(f(moy(sel(m, (150, 151), "n")), 1) for m in (3, 4, 5)), ", ".join("%s aux côtés %d et %d" % (f(v, 2), c[0], c[1]) for c, v in pc), f(p5764, 2)))
W("")
W("## 5. Lecture (pas un résultat jugé)")
W("")
b0 = SAC[0]["boites"][0]; GT = SAC[0]["Gamma_chaine_ordre3"] * b0["T"]
W("- La largeur sous absorbeur n'est pas un artefact de l'absorbeur : c'est la force de couplage du vide au dehors dans le spectre réel de la boîte fermée. En chaîne elle se lit sur un croisement (V²T) ; en 2D elle ne se lit que sur la somme.")
W("- La chaîne fermée ne vaut comme modèle de la boîte fermée que pour les petites boîtes : au croisement, l'attendu tient aux sites de coupure " + ", ".join("%d (%d barreaux)" % (a[2], a[0]) for a in sorted(lignes) if a[8]) + " et tombe aux sites " + ", ".join("%d (%d barreaux)" % (a[2], a[0]) for a in sorted(lignes) if not a[8]) + " ; les sauts atteignent 0.5 aux sites %s selon la profondeur. Au-delà, ses propres corrections d'ordre 2 sortent du domaine perturbatif (le décalage diagonal atteint l'unité vers le site %d à 3 barreaux), et le dehors 2D est une mer, pas une échelle. Sous absorbeur cela ne pèse pas, le gel l'a jugé : le flux est absorbé avant (lecture)." % (", ".join(str(seuil[float(F[m]["g"])]) for m in (3, 4, 5)), min(int(m) for m, v in [p for p in SA["points"] if float(p["g"]) == float(F[3]["g"])][0]["S"].items() if v >= 1.0)))
W("- En chaîne, le temps de retour T est fini quelle que soit la longueur : le nombre de niveaux du dehors par unité d'énergie ne croît pas, le système fermé ne se désintègre jamais, il bat aux conditions de bord accordées. En 2D ce nombre croît avec la boîte, jusqu'au côté " + str(max(b["N"] for b in G200["boites"])) + " où le calcul s'arrête (section 4). **Conjecture, non éprouvée au-delà** : s'il croît sans borne, chaque croisement s'affaiblit, ils se multiplient, et le grand bocal 2D tend vers une vraie désintégration au taux Γ — ce que la réduction à une chaîne ne peut pas montrer.")
W("- Ordre de grandeur, pour ne pas surlire : avec n niveaux se partageant la force, la part des bords « accordés » croît comme √(n Γ T). À 3 barreaux Γ T = %.1e : il faudrait de l'ordre de %.0e niveaux pour que le vide soit mêlé à coup sûr. Dans toute boîte calculable, le vide fermé reste stable hors accidents." % (GT, 1.0 / GT))
W("- Prudence sur la littérature : « le système tronqué ne se désintègre pas » et « il se désintègre sous absorbeur » ne se contredisent pas ; en 2D s'y ajoute que la réponse du système tronqué dépend de la taille de la troncature d'une façon que l'image à un canal ne contient pas.")
W("")
W("## 6. Limites")
W("")
W("- Un seul désaccord en 2D fermée (le point sacrifié), trois profondeurs, côtés jusqu'à 64 en diagonalisation complète et jusqu'à " + str(max(b["N"] for b in G200["boites"])) + " en creux ; boîte carrée en quanta, paroi dure : une autre forme de boîte est une autre condition à l'infini.")
W("- V_k est une formule de premier ordre ; les niveaux à moins de " + f(F[3]["bornes"][0], 2) + " |δ| du vide sont hors fenêtre. Les barres d'erreur supposent des boîtes indépendantes.")
W("- Le lisse Γ(E) loin de l'énergie du vide vient de la chaîne d'ordre 3, que le gel n'a jugée qu'à l'énergie du vide. L'accord de la somme 2D avec lui est un fait d'exploration, pas un énoncé gelé.")
W("- La repondération est venue après lecture de la première passe à 3 barreaux ; les épreuves sont les trois échantillons marqués « tient ». La bande d'attente (" + f(A3_MIN, 2) + " à " + f(A3_MAX, 2) + ") est du même ordre que le bruit de deux des trois : épreuve faible prise une à une, plus nette ensemble.")
cmin = min(v[1] * b["poids_vide"] / (v[0] * abs(float(__import__("fractions").Fraction(F[m]["w2"])) - 2.0)) ** 2 for m in (3, 4, 5) for b in F[m]["boites"] for v in b["niveaux_2d"])
W("- Double précision : le plus petit poids c_k² lu en diagonalisation complète vaut %.0e, soit une composante de %.0e, au bord de ce qu'un vecteur propre rend ; les plus petites parts y sont donc incertaines. Les sommes n'en dépendent pas (elles sont portées par les grandes parts), et dans les grandes boîtes les deux lectures indépendantes de chaque niveau s'accordent. Rien n'a été recalculé en précision étendue. Degré 9, 6 barreaux : illisible." % (cmin, math.sqrt(cmin)))
W("- Rien n'est gelé, rien n'est rejoué par machine 2. La croissance du nombre de niveaux au-delà du côté " + str(max(b["N"] for b in G200["boites"])) + " est une extrapolation, et rien ne dit que la participation suive le compte.")
W("")
W("## 7. Pièces (conteneur de machine 1, non livrées en lot)")
W("")
W("pont_ferme_absorbeur_machine1_v1.py, pont_semiclassique_machine1_v1.py (chaîne, v1 de la note) ; pont_degres_machine1_v1.py (degrés) ; pont_2d_sacrifie_machine1_v1.py (boîte 2D, croisement) ; pont_2d_force_machine1_v1.py puis _v2.py (règle de somme, brute puis repondérée) ; pont_lisse_ordres_machine1_v1.py (ordre 1 contre ordre 3, sans bruit) ; pont_sauts_regard_machine1_v1.py (sauts de l'échelle) ; pont_2d_grand_machine1_v1.py et attendu_grand_m4_m5_cote200_machine1_v1.txt (boîtes jusqu'au côté 201) ; leurs journaux et leurs JSON ; ce script. Moteur et blocs : ceux du registre (delta 102), non modifiés.")
open(SORTIE, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print("écrit :", SORTIE, len(L), "lignes")
