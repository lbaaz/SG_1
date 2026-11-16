# -*- coding: utf-8 -*-
"""CONSTRUCTION DE LA NOTE « LA LOI DE LA LARGEUR » -- machine 1, v1, 2026-11-15. Hors chaîne.
Chaque nombre de la note est calculé ici à partir des sorties des scripts du lot ; aucun n'est tapé à la main.
Usage : python3 -I construction_note_loi_machine1_v1.py <dossier du chantier> <clone du registre>
        <verdict_ter.json de BOCAL4> <acte ter (projet)> <manifeste du lot de résultat de machine 2> <sortie.md>"""
import sys, os, json, math, hashlib, unicodedata, statistics, textwrap
D, CLONE, VTER, ACTE, MANIF_RES, SORTIE = sys.argv[1:7]

def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def J(nom): return json.load(open(os.path.join(D, nom)))
med = statistics.median
def fr(x, n=3): return ("%.*f" % (n, x)).replace(".", ",")
def sg(x, n=3): return ("%+.*f" % (n, x)).replace(".", ",")
def ex(x, n=1): return ("%.*e" % (n, x)).replace(".", ",")
def pc(x, n=1): return fr(100 * x, n)
def pcl(x, n=1): return fr(100 * (math.exp(x) - 1), n)      # un ecart |ln q| dit en pour cent

c = {"moteur": B(CLONE + "/scripts/m17_chaine_v17.py"), "depot": B(CLONE + "/journal/sonde_ordre2.json"), "v98": B(CLONE + "/journal/verdict_ordre2.json"),
     "bloc2": B(CLONE + "/scripts/chaine_ordre2_bloc_machine1_v1.py"), "note14": B(CLONE + "/journal/note_machine1_residuel_chaine_EA_second_ordre_2026-11-14_v1.md"),
     "acte98": B(CLONE + "/journal/journal_delta_98_ordre2_chaine_EA_v1.md"), "vter": B(VTER), "acte_ter": B(ACTE), "lot_res": B(MANIF_RES)}
assert (c["moteur"], c["depot"], c["v98"], c["vter"], c["lot_res"]) == ("82a0be882568fe0c", "10887c60d5f55bcf", "4195583a970eaf70", "2cd1f84efa02f2ab", "1f057651c8f69eb6")
PIECES = ["etape1_etalon_machine1_v1.py", "etape1_etalon_machine1_v1.log", "etape1_etalon_v1.json", "ordre3_bloc_machine1_v1.py",
          "controle_algebre_ordre3_machine1_v1.py", "controle_algebre_ordre3_machine1_v1.log", "controle_algebre_ordre3_v1.json",
          "calcul_ordre3_machine1_v1.py", "calcul_ordre3_machine1_v1.log", "ordre3_par_etat_v1.json",
          "forme_fermee_machine1_v1.py", "forme_fermee_machine1_v1.log", "forme_fermee_v1.json", "structure_en_delta_machine1_v1.py", "structure_en_delta_machine1_v1.log", "structure_en_delta_v1.json"]
cp = {p: B(os.path.join(D, p)) for p in PIECES}

E = J("etape1_etalon_v1.json"); O = J("ordre3_par_etat_v1.json")["points"]; FFl = J("forme_fermee_v1.json")["etats"]; ST = J("structure_en_delta_v1.json")["series"]
AL = J("controle_algebre_ordre3_v1.json"); assert AL["tient"]
E1 = {(r["id"], r["rang"]): r for r in E["etats"]}; FF = {(r["id"], r["rang"]): r for r in FFl}
JUGES = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4"]
rows = []
for i in JUGES:
    for e in O[i]["etats"]:
        k = (i, e["rang"]); r = E1[k]; f = FF[k]
        assert abs(e["G_c2"] / r["G_c2"] - 1) < 1e-7 and e["ecart_c2_depot"] < 1e-7
        if r["statut"] != "QUALIFIE":
            continue
        v = e["variantes"]; d2D = e["E_re"] - e["E_libre"]
        rows.append({"id": i, "rang": e["rang"], "n1": e["n1"], "n2": e["n2"], "delta": r["delta"], "g": r["g"], "mb": f["m_bord"], "eb": f["e_bord"], "tb": f["t_bord"],
                     "kappa": f["t_0"] / abs(r["delta"]), "Gpl": r["G_pl"], "l1": math.log(r["q1p"]), "l2": math.log(r["q2p"]), "l3": math.log(e["G_c3"] / r["G_pl"]),
                     "stab": max(abs(math.log(v[x] / e["G_c3"])) for x in ("ef_double", "ef_demi", "recul_4")), "en2": abs((e["dE_c2"] - d2D) / d2D), "en3": abs((e["dE_c3"] - d2D) / d2D),
                     "w3t": e["W3_sur_t_max_barriere"], "w5t": e["W5_sur_t_max_barriere"], "lw5": abs(math.log(e["G_c3"] / v["sans_W5"])),
                     "pente": f["pente_c2"], "Lw": f["Lw"], "Lm": f["Lm"], "Lp": f["Lp"], "T3t": e["T3_sur_t_max_barriere"],
                     "rap": [2 * abs(b["t"]) / abs(b["e"]) for b in e["barriere"] if b["m"] in e["sites_barriere"]]})
N = len(rows); assert N == 131 and E["n_juges_98"] == 132 and E["n_qualifies"] == 131
assert sum((r["n1"], r["n2"]) == (6, 2) for r in rows) == 7 and all(r["l2"] > 0 for r in rows)
assert [(i_, e_["rang"]) for i_ in JUGES for e_ in O[i_]["etats"] if E1[(i_, e_["rang"])]["statut"] != "QUALIFIE"] == [("L3", 5)]
for i_ in JUGES:
    rs_ = [r for r in rows if r["id"] == i_]; assert statistics.median([r["en3"] for r in rs_]) < statistics.median([r["en2"] for r in rs_]), i_
    ms_ = statistics.median([r["stab"] for r in rs_]); assert (ms_ > 0.15) == (i_ in ("M4", "L1", "L2", "L3", "L4")) and (ms_ > 0.15 or ms_ < 0.10), (i_, ms_)
assert len(AL["V2"]) == 3 and AL["V1"]["g"] == [0.0002, 0.0004, 0.0008, 0.0016]
rbt = [r["eb"] / r["tb"] for r in rows]
CL = ((0.0, 0.3), (0.3, 0.5), (0.5, 0.7), (0.7, 1.0), (1.0, 2.0))
def classe(lo, hi, signe=0):
    return [r for r in rows if lo <= r["eb"] < hi and (signe == 0 or (r["delta"] > 0) == (signe > 0))]
assert sum(len(classe(*k)) for k in CL) == N
bas = classe(0.0, 0.3); sous07 = [r for r in rows if r["eb"] < 0.7]; sur07 = [r for r in rows if r["eb"] >= 0.7]
dom = [r for r in rows if r["eb"] < 0.7 and r["stab"] <= 0.05]
mieux = lambda rs: sum(abs(r["l3"]) < abs(r["l2"]) for r in rs)
def corr(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / math.sqrt(sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))
def droite(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y); b = sum((a - mx) * (q - my) for a, q in zip(x, y)) / sum((a - mx) ** 2 for a in x); a0 = my - b * mx
    res = [q - a0 - b * a for a, q in zip(x, y)]
    return a0, b, statistics.pstdev(res), max(abs(v) for v in res)
lnG = [math.log(r["Gpl"]) for r in rows]
wkb = droite([-2 * r["Lw"] for r in rows], lnG); mot = droite([-2 * r["Lm"] for r in rows], lnG); prod = droite([-2 * r["Lp"] for r in rows], lnG)
pm = droite([r["mb"] for r in rows], [r["pente"] for r in rows])
raps = sorted(x for r in rows for x in r["rap"])
def fit0(x, y):
    cc = sum(a * b for a, b in zip(x, y)) / sum(a * a for a in x); res = [b - cc * a for a, b in zip(x, y)]
    return cc, corr(x, y), statistics.pstdev(res)
f_eb = fit0([r["eb"] ** 2 / r["mb"] for r in rows], [r["l2"] for r in rows])
sig = {n: {"neg_bon": sum((r["l%d" % n] < 0) for r in rows if r["delta"] < 0), "neg": sum(r["delta"] < 0 for r in rows),
           "pos_bon": sum((r["l%d" % n] > 0) for r in rows if r["delta"] > 0), "pos": sum(r["delta"] > 0 for r in rows)} for n in (1, 2, 3)}
sigd = {"neg_bon": sum(r["l3"] < 0 for r in dom if r["delta"] < 0), "neg": sum(r["delta"] < 0 for r in dom), "pos_bon": sum(r["l3"] > 0 for r in dom if r["delta"] > 0), "pos": sum(r["delta"] > 0 for r in dom)}
pire3 = max(rows, key=lambda r: abs(r["l3"]))
etend_dep = med([math.log(p["q2"][2] / p["q2"][0]) for p in E["points"].values()]); etend_pl = med([math.log(p["q2p"][2] / p["q2p"][0]) for p in E["points"].values()])
# exemple de divergence : L4 rang 0
ex4 = [e for e in O["L4"]["etats"] if e["rang"] == 0][0]; b4 = [b for b in ex4["barriere"] if b["m"] == ex4["m_bord"]][0]
serieA = [s for s in ST if (s["n1"], s["n2"], s["kappa"]) == (6, 2, 0.30)][0]; serieB = [s for s in ST if (s["n1"], s["n2"], s["kappa"]) == (6, 2, 0.22)][0]
serieC = [s for s in ST if (s["n1"], s["n2"]) == (10, 3)][0]
def etendue_G1(s):
    v = [l["G1_sur_delta"] for l in s["lignes"] if not l["vide"]]; return max(v) / min(v) - 1
def b_neg(s, emax):
    v = [l["ln_32"] / l["delta"] ** 2 for l in s["lignes"] if not l["vide"] and l["delta"] < 0 and l["e_bord"] <= emax]; return min(v), max(v), len(v)

V = {"N": N, "bas": len(bas), "sous07": len(sous07), "sur07": len(sur07), "dom": len(dom)}
L = []
def T(s=""): L.append(s)
def P(s, ind=0, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=96, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))

T("# Note hors chaîne : la loi de la largeur — étalon, ordre 3, structure"); T()
P("""Plume : machine 1. Date : 15/11/2026, soir. Statut : exploration hors chaîne, non certifiée, non rejouée par machine 2, faite APRÈS COUP
sur des états déjà joués. Elle ne tranche rien, ne modifie aucune pièce citée et n'ouvre aucun gel. Ouverture, selon machine 1 :
l'opérateur a demandé la méthode (15/11/2026, 18 h 44), puis écrit « ouvre » (18 h 50).""")
T()
P("""Aucune largeur 2D n'est calculée ici. Ce qui est calculé : de l'arithmétique sur des pièces, des chaînes à une dimension (quelques
dizaines de sites) et un contrôle d'algèbre sur de petites matrices hermitiennes, sans absorbeur, où aucune largeur n'est lue (section
3.2). Les éléments de matrice sont ceux du moteur (%s), appelés tels quels. La chaîne d'ordre 2 est le bloc déposé (%s).""" % (c["moteur"], c["bloc2"]))
T()
P("""Référence : les largeurs de plateau Gamma_pl(A) que le run du gel « qualification E-B ter » a rendues (verdict de BOCAL4 %s, lot de
résultat %s). L'acte de ce run (projet v1, %s) attend le contreseing de machine 2 : cette référence n'est pas déposée. Si un nombre de ce
verdict bougeait, la note serait à refaire. Les états sont les %d que le delta 98 a jugés (sortie %s, verdict %s) ; %d sont QUALIFIÉS par
le run ter et sont seuls gardés (L3 rang 5 est écarté).""" % (c["vter"], c["lot_res"], c["acte_ter"], E["n_juges_98"], c["depot"], c["v98"], N))
T()
T("## 0. Verdict"); T()
P("""1. L'étalon. Contre la largeur de plateau, les trois bandes du delta 98 tiennent encore : aucun état hors borne sur %d, q2 de %s à %s
(contre la lecture déposée : %s à %s). Et le résidu devient presque une constante par point : l'étendue de ln q2 à l'intérieur d'un point
passe de %s à %s (médianes). La dispersion que le delta 98 voyait d'un état à l'autre était, pour l'essentiel, celle de la lecture déposée
(k = 3, F1, 20 couches), pas celle de la chaîne.""" % (N, fr(E["q2p_min"]), fr(E["q2p_max"]), fr(E["q2_min"]), fr(E["q2_max"]), fr(etend_dep), fr(etend_pl)), 0, 3)
P("""2. L'ordre 3 ferme le résidu là où le développement converge, et pas ailleurs. Trois termes d'ordre g^3, dérivés sans paramètre : une
correction du saut entre voisins, un saut au troisième voisin et un saut au cinquième. Soit e_bord le désaccord atteint au dernier barreau de la barrière. Pour
e_bord < 0,3 (%d états), l'écart médian à la largeur 2D vaut %s pour cent avec la chaîne du moteur, %s avec l'ordre 2, %s avec l'ordre 3.
Pour e_bord < 0,7 (%d états), l'ordre 3 fait mieux que l'ordre 2 à %d états sur %d. Au-delà (%d états), il fait pire à %d, jusqu'à un
facteur %s (%s rang %d), et la chaîne d'ordre 3 n'est plus stable sous son propre absorbeur.""" % (
    len(bas), pcl(med([abs(r["l1"]) for r in bas])), pcl(med([abs(r["l2"]) for r in bas])), pcl(med([abs(r["l3"]) for r in bas])),
    len(sous07), mieux(sous07), len(sous07), len(sur07), len(sur07) - mieux(sur07), fr(math.exp(abs(pire3["l3"])), 1), pire3["id"], pire3["rang"]), 0, 3)
P("""3. Contrôle indépendant : les énergies. Le décalage d'énergie de l'état, qui n'a servi à rien régler, est rendu à %s pour cent près
par l'ordre 2 et à %s pour cent près par l'ordre 3 (médianes ; pires états %s et %s pour cent). L'ordre 3 l'améliore aux douze points, y
compris là où sa largeur diverge.""" % (fr(100 * med([r["en2"] for r in rows]), 2), fr(100 * med([r["en3"] for r in rows]), 3),
    fr(100 * max(r["en2"] for r in rows), 2), fr(100 * max(r["en3"] for r in rows), 2)), 0, 3)
P("""4. La loi. La chaîne est un développement en puissances du désaccord delta, à rapport kappa = t_0 / |delta| fixé (saut du site de
départ rapporté au désaccord) : Gamma = |delta| × Phi(kappa ; état) × [1 + a delta + b delta^2 + …]. La chaîne seule le montre (section
4.1). Les largeurs 2D le montrent par la parité du résidu : après l'ordre 1 il change de signe avec delta, après l'ordre 2 il est du même
côté des deux côtés de 2,00, après l'ordre 3 il change de signe à nouveau (section 4.2). Ce qui décide de l'accord n'est pas delta seul :
c'est le saut atteint au bout de la barrière, soit e_bord / 2 (section 3.6).""", 0, 3)
P("""5. Ce que j'avais annoncé à l'opérateur et qui est faux. Ma réponse de méthode disait : « la pente vaut deux fois le nombre de barreaux, donc un entier pair ». La chaîne dit de %s
à %s, soit de %s à %s par barreau. La barrière est peu profonde (2 t / |e| vaut %s en médiane sur ses %d sites) : ni le produit perturbatif
ni le WKB discret n'y sont quantitatifs (écart-type %s en logarithme pour le WKB, pire état à un facteur %s). Il n'y a pas de formule fermée
courte : la loi est la chaîne. L'exposant 2/3 (« un calcul de coin de table, à ne pas citer ») n'est pas testé ; je le retire.""" % (
    fr(min(r["pente"] for r in rows), 1), fr(max(r["pente"] for r in rows), 1), fr(min(r["pente"] / r["mb"] for r in rows), 1), fr(max(r["pente"] / r["mb"] for r in rows), 1),
    fr(med(raps), 2), len(raps), fr(wkb[2], 2), fr(math.exp(wkb[3]), 0)), 0, 3)
P("""6. Cela vaut un gel, sur un énoncé plus étroit que celui que j'espérais : dans un domaine calculable avant tout run (e_bord sous un
seuil, chaîne d'ordre 3 stable sous son absorbeur), l'ordre 3 rend la largeur 2D qualifiée à quelques pour cent. Ici, ce domaine compte %d
états sur %d : écart médian %s pour cent, pire %s pour cent. Section 5.""" % (len(dom), N, pcl(med([abs(r["l3"]) for r in dom])), pcl(max(abs(r["l3"]) for r in dom))), 0, 3)
T()
T("## 1. Notations"); T()
P("""Échelle résonante de l'état (n1, n2) : sites m, (n1 + 2m, n2 + m). Saut t_m entre les sites m et m + 1. Désaccord du site
e_m = m delta + Sigma2(m) − Sigma2(0), delta = w2 − 2. Barrière : les sites où |e_m| > 2 |t_m| (règle du moteur) ; m_bord est le dernier,
e_bord = |e_m| à ce site. kappa = t_0 / |delta|. q_n = Gamma de la chaîne d'ordre n / Gamma_pl(A) ; ordre 1 : chaîne du moteur, telle que
déposée ; ordre 2 : bloc déposé (déplacements, saut au second voisin, sites bas) ; ordre 3 : bloc de cette note. « Écart » veut dire
|ln q| ; il est donné tel quel dans les tableaux, et converti en pour cent (exp − 1) dans le verdict.""")
T()
T("## 2. Étape 1 : l'étalon"); T()
P("""La comparaison du delta 98 est refaite avec Gamma_pl(A) au dénominateur. Rien n'est recalculé : la chaîne est celle du dépôt.""")
T()
T("| bande | borne | états | q2 contre la lecture déposée : min, médiane, max | q2 contre le plateau : min, médiane, max | hors borne |")
T("|---|---|---|---|---|---|")
for nom in ("proche", "moyenne", "lointaine"):
    b = E["bandes"][nom]
    T("| %s | %s | %d | %s ; %s ; %s | %s ; %s ; %s | %d |" % (nom, fr(b["borne"], 2), b["qualifies"], fr(b["q2"][0]), fr(b["q2"][1]), fr(b["q2"][2]),
      fr(b["q2p"][0]), fr(b["q2p"][1]), fr(b["q2p"][2]), b["hors_plateau"]))
T()
T("| point | delta | états | q2 déposé : min ; max | q2 plateau : min ; max |")
T("|---|---|---|---|---|")
for i in JUGES:
    p = E["points"][i]
    T("| %s | %s | %d | %s ; %s | %s ; %s |" % (i, sg(p["delta"], 2), p["etats"], fr(p["q2"][0]), fr(p["q2"][2]), fr(p["q2p"][0]), fr(p["q2p"][2])))
T()
P("""L'ajustement à un paramètre de la note du 14/11 (%s), ln q = c delta^2 m_bord, donne contre le plateau c = %s (corrélation %s,
écart-type restant %s) ; contre la lecture déposée, %s (%s ; %s). Un meilleur prédicteur du résidu de l'ordre 2 est e_bord^2 / m_bord :
c = %s, corrélation %s, écart-type restant %s. C'est un ajustement après coup, pas une dérivation.""" % (c["note14"],
    fr(E["ajust_q2p"]["c"], 2), fr(E["ajust_q2p"]["correlation"], 2), fr(E["ajust_q2p"]["ecart_type_restant"]),
    fr(E["ajust_q2"]["c"], 2), fr(E["ajust_q2"]["correlation"], 2), fr(E["ajust_q2"]["ecart_type_restant"]), fr(f_eb[0], 2), fr(f_eb[1], 2), fr(f_eb[2])))
T()
T("## 3. Étape 3 : l'ordre 3"); T()
T("### 3.1 Ce qui est ajouté"); T()
P("""Le hamiltonien effectif sur l'échelle, à l'ordre g^3, forme symétrique (formules de Löwdin ; A : les sites de l'échelle, B : le
reste) :""")
T()
T("    H3_mm' = −(1/2) Σ_{l∈B, m''∈A} [ V_ml V_lm'' V_m''m' / ((E_m' − E_l)(E_m'' − E_l))")
T("                                    + V_mm'' V_m''l V_lm' / ((E_m − E_l)(E_m'' − E_l)) ]")
T("             +(1/2) Σ_{l,l'∈B} V_ml V_ll' V_l'm' [ 1/((E_m − E_l)(E_m − E_l'))")
T("                                                   + 1/((E_m' − E_l)(E_m' − E_l')) ]")
T()
P("""La parité de x^5 ne laisse à cet ordre que des sauts à un nombre impair de barreaux : T3_m, correction du saut entre voisins ;
W3_m, saut au troisième voisin ; W5_m, saut au cinquième voisin (trois pas de cinq quanta, tous hors échelle). Les énergies sont les
énergies libres du moteur ; absorbeur, longueur et lecture de l'état sont ceux de la chaîne d'ordre 2. Rapportés au saut du premier ordre,
W3 et W5 valent au plus %s et %s dans les barrières des %d états ; retirer W5 déplace la largeur d'ordre 3 d'au plus %s (en |ln|) dans le
domaine de la section 3.6, et d'au plus %s hors de lui.""" % (fr(max(r["w3t"] for r in rows), 4), fr(max(r["w5t"] for r in rows), 4), N,
    fr(max(r["lw5"] for r in dom), 3), fr(max(r["lw5"] for r in rows if r not in dom), 3)))
T()
T("### 3.2 Contrôles d'algèbre (aucune largeur n'y est lue)"); T()
a1 = AL["V1"]["pentes"]
P("""- (V0) Les éléments de x^5 du moteur contre une matrice construite à part (opérateurs d'échelle), %d éléments : pire écart relatif
%s.""" % (AL["V0"]["elements"], ex(AL["V0"]["pire_ecart_relatif"])), 0, 2)
P("""- (V1) La formule, écrite à part en matrices denses, contre le hamiltonien effectif canonique exact d'une base tronquée hermitienne
(13 niveaux par mode, w2 = 2,11, échelle de (3, 1), quatre couplages de 2e-4 à 1,6e-3). Le reste sur le saut entre voisins décroît comme g^%s avec le terme d'ordre 3 et comme g^%s
sans lui (attendu : 5 et 3) ; sur le troisième voisin, g^%s et g^%s ; sur la diagonale et le second voisin, g^%s et g^%s (attendu : 4).
Au cinquième voisin, la base n'offre qu'un élément, qui tombe au plancher d'arrondi aux petits couplages : sans le terme le reste suit
g^%s, et au plus fort couplage le terme n'en laisse que la fraction %s. Au quatrième voisin, que la parité interdit à l'ordre 3, le reste
suit g^%s (attendu : 4).""" % (
    fr(a1["voisin_avec"], 2), fr(a1["voisin_sans"], 2), fr(a1["troisieme_avec"], 2), fr(a1["troisieme_sans"], 2), fr(a1["diag"], 2), fr(a1["second"], 2),
    fr(a1["cinquieme_sans"], 2), ex(AL["V1"]["cinquieme_rapport_g_max"]), fr(a1["quatrieme"], 2)), 0, 2)
v2 = AL["V2"]
P("""- (V2) Les tables du bloc (sommes sur les chemins, éléments du moteur) contre la formule dense, sur trois échelles : pire écart relatif
%s pour T3, %s pour W3, %s pour W5.""" % (ex(max(p["T3"] for p in v2.values())), ex(max(p["W3"] for p in v2.values())), ex(max(p["W5"] for p in v2.values()))), 0, 2)
T()
P("""La chaîne d'ordre 2 refaite ici redonne celle du dépôt à %s près au pire, d'une plateforme à l'autre.""" % ex(max(e["ecart_c2_depot"] for i in JUGES for e in O[i]["etats"])))
T()
T("### 3.3 Par classe de e_bord"); T()
T("| e_bord | delta | états | écart médian, ordre 1 | ordre 2 (pire) | ordre 3 (pire) | ordre 3 meilleur que 2 | stabilité de la chaîne d'ordre 3, médiane |")
T("|---|---|---|---|---|---|---|---|")
for lo, hi in CL:
    for s_, nom in ((-1, "< 0"), (1, "> 0"), (0, "tous")):
        rs = classe(lo, hi, s_)
        if not rs or (s_ != 0 and len(rs) == len(classe(lo, hi))):
            continue
        T("| %s à %s | %s | %d | %s | %s (%s) | %s (%s) | %d sur %d | %s |" % (fr(lo, 1), fr(hi, 1), nom, len(rs), fr(med([abs(r["l1"]) for r in rs])),
          fr(med([abs(r["l2"]) for r in rs])), fr(max(abs(r["l2"]) for r in rs)), fr(med([abs(r["l3"]) for r in rs])), fr(max(abs(r["l3"]) for r in rs)),
          mieux(rs), len(rs), fr(med([r["stab"] for r in rs])) if s_ == 0 else "—"))
T()
P("""« Stabilité » : le plus grand |ln| du rapport de la largeur d'ordre 3 à elle-même quand l'absorbeur de la chaîne est deux fois plus
fort, deux fois plus faible, ou reculé de quatre sites. Pour e_bord < 0,3 elle vaut %s en médiane (pire %s) : l'accord à %s pour cent de
cette classe est au niveau de ce que la chaîne sait d'elle-même.""" % (fr(med([r["stab"] for r in bas])), fr(max(r["stab"] for r in bas)), pcl(med([abs(r["l3"]) for r in bas]))))
T()
T("### 3.4 Par point"); T()
T("| point | delta | e_bord : min ; max | q2 médian | q3 : min ; médiane ; max | stabilité d'ordre 3, médiane |")
T("|---|---|---|---|---|---|")
for i in JUGES:
    rs = [r for r in rows if r["id"] == i]
    T("| %s | %s | %s ; %s | %s | %s ; %s ; %s | %s |" % (i, sg(rs[0]["delta"], 2), fr(min(r["eb"] for r in rs), 2), fr(max(r["eb"] for r in rs), 2), fr(math.exp(med([r["l2"] for r in rs]))),
      fr(math.exp(min(r["l3"] for r in rs))), fr(math.exp(med([r["l3"] for r in rs]))), fr(math.exp(max(r["l3"] for r in rs))), fr(med([r["stab"] for r in rs]))))
T()
P("""Aux quatre points lointains (|delta| de 0,11 à 0,12) et à M4, la largeur d'ordre 3 dépend de l'absorbeur de la chaîne : les q3 de ces
lignes sont ceux du réglage du delta 98 et n'ont pas de sens au-delà.""")
T()
T("### 3.5 Une étiquette suivie d'un point à l'autre"); T()
P("""L'état (6, 2) est jugé et qualifié à sept points. Rangé par kappa :""")
T()
T("| point | delta | kappa | m_bord | e_bord | Gamma_pl / |delta| | q1 | q2 | q3 |")
T("|---|---|---|---|---|---|---|---|---|")
for r in sorted([r for r in rows if (r["n1"], r["n2"]) == (6, 2)], key=lambda r: r["kappa"]):
    T("| %s | %s | %s | %d | %s | %s | %s | %s | %s |" % (r["id"], sg(r["delta"], 2), fr(r["kappa"], 4), r["mb"], fr(r["eb"]), ex(r["Gpl"] / abs(r["delta"]), 3),
      fr(math.exp(r["l1"])), fr(math.exp(r["l2"])), fr(math.exp(r["l3"]))))
T()
s62 = sorted([r for r in rows if (r["n1"], r["n2"]) == (6, 2)], key=lambda r: r["kappa"]); ad = [r["Gpl"] / abs(r["delta"]) for r in s62]
grp = [s62[0:2], s62[2:5], s62[5:7]]; assert all(max(r["kappa"] for r in g_) - min(r["kappa"] for r in g_) < 0.001 for g_ in grp)
fg = [max(r["Gpl"] / abs(r["delta"]) for r in g_) / min(r["Gpl"] / abs(r["delta"]) for r in g_) for g_ in grp]
P("""Les sept points forment trois groupes de kappa presque égal (%s ; %s ; %s), à des désaccords très différents. Dans chaque groupe,
Gamma_pl / |delta| tient dans un facteur %s, %s et %s ; d'un groupe à l'autre, la même quantité parcourt %s décades. C'est la forme
Gamma = |delta| × Phi(kappa) lue sur les largeurs 2D elles-mêmes ; l'écart à kappa égal est la correction en delta, que q1, q2 et q3
mesurent.""" % (fr(med([r["kappa"] for r in grp[0]]), 3), fr(med([r["kappa"] for r in grp[1]]), 3), fr(med([r["kappa"] for r in grp[2]]), 3),
    fr(fg[0], 1), fr(fg[1], 1), fr(fg[2], 1), fr(math.log10(max(ad) / min(ad)), 1)))
T()
T("### 3.6 Pourquoi la série casse"); T()
P("""Lecture, non démontrée. Le développement a pour petit paramètre, au site m, le saut t_m rapporté aux dénominateurs des états hors échelle, qui sont de
l'ordre de la fréquence de l'oscillateur (prise pour unité). Or la barrière finit, par définition, au dernier site où |e_m| > 2 t_m : au
bout de la barrière ce paramètre vaut à peu près e_bord / 2 (sur les %d états, e_bord / t_bord va de %s à %s). e_bord range donc les états
parce qu'il mesure le saut au dernier barreau. Il vaut à peu près m_bord × |delta| : il grandit avec le désaccord et avec la longueur de la
barrière, donc quand le couplage baisse.""" % (N, fr(min(rbt), 2), fr(max(rbt), 2)))
T()
P("""Exemple. À L4, état lu (11, 2), la barrière compte %d sites et finit à un désaccord de %s et un saut de %s. Les deux parts de la
correction T3 (chemins hors échelle, chemins repassant par l'échelle) y valent %s et %s fois le saut du premier ordre, et leur somme %s :
le terme d'ordre 3 y est la différence de deux grands nombres. À C1, la barrière finit à un désaccord de %s à %s.""" % (
    ex4["m_bord"], fr(abs(b4["e"]), 2), fr(abs(b4["t"]), 2), sg(b4["T3_BB_sur_t"], 1), sg(b4["T3_A_sur_t"], 1), sg(b4["T3_sur_t"], 2),
    fr(min(r["eb"] for r in rows if r["id"] == "C1"), 2), fr(max(r["eb"] for r in rows if r["id"] == "C1"), 2)))
T()
P("""Domaine calculable avant tout run, lu sur ces données : e_bord < 0,7 et stabilité de la chaîne d'ordre 3 au plus 0,05. Il compte %d
états (%s). L'écart de l'ordre 3 y vaut %s en médiane, %s au pire ; celui de l'ordre 2, %s et %s. L'ordre 3 y fait mieux à %d états sur
%d.""" % (len(dom), ", ".join("%s %d" % (i, sum(r["id"] == i for r in dom)) for i in JUGES if any(r["id"] == i for r in dom)),
    fr(med([abs(r["l3"]) for r in dom])), fr(max(abs(r["l3"]) for r in dom)), fr(med([abs(r["l2"]) for r in dom])), fr(max(abs(r["l2"]) for r in dom)), mieux(dom), len(dom)))
T()
T("## 4. Étape 2 : la structure"); T()
T("### 4.1 Un développement en delta à kappa fixé (chaîne seule)"); T()
P("""À étiquette et kappa fixés, on fait varier delta ; les w2 parcourus ne sont pas des points de la campagne et aucune largeur 2D n'y
est lue ni prédite. Raison attendue : le saut vaut kappa × delta × (un élément réduit) ; à kappa fixé, la chaîne du premier ordre est
delta fois une matrice qui ne dépend que de kappa et de l'état, et l'ordre n en g pèse delta^(n − 1) devant elle (à la dépendance en w2
des éléments de matrice près). Gamma_1 : sauts du premier ordre seuls, sites bas compris (ce n'est pas la chaîne du moteur) ; Gamma_2,
Gamma_3 : ordres 2 et 3 complets. État (6, 2), kappa = 0,30 :""")
T()
T("| delta | m_bord | e_bord | Gamma_1 / |delta| | ln(Gamma_2 / Gamma_1) / delta | ln(Gamma_3 / Gamma_2) / delta^2 |")
T("|---|---|---|---|---|---|")
for l in serieA["lignes"]:
    T("| %s | %d | %s | %s | %s | %s |" % (sg(l["delta"], 4), l["m_bord"], fr(l["e_bord"]), ex(l["G1_sur_delta"], 3), sg(l["ln_21"] / l["delta"], 2), sg(l["ln_32"] / l["delta"] ** 2, 1)))
T()
bA = b_neg(serieA, 0.25); bB = b_neg(serieB, 0.45)
def mbs(s_): return min(l["m_bord"] for l in s_["lignes"] if not l["vide"]), max(l["m_bord"] for l in s_["lignes"] if not l["vide"])
def a_lim(s_, d_): return [l["ln_21"] / l["delta"] for l in s_["lignes"] if not l["vide"] and abs(l["delta"] - d_) < 1e-12][0]
dabs = sorted(set(abs(l["delta"]) for l in serieA["lignes"])); assert all(l["ln_32"] < 0 for s_ in (serieA, serieB) for l in s_["lignes"])
assert all(l["e_bord"] > 0.4 for l in serieC["lignes"] if abs(l["delta"]) >= 0.025 - 1e-12)
P("""Gamma_1 / |delta| ne bouge que de %s pour cent quand |delta| varie d'un facteur %s et que delta change de signe (%d à %d barreaux ; à
kappa = 0,22, %d à %d barreaux : %s pour cent ; à (10, 3), kappa = 0,20, %d à %d barreaux : %s pour cent). La correction d'ordre 2 a un
terme dominant linéaire en delta, qui change de signe avec lui : ln(Gamma_2 / Gamma_1) / delta vaut %s à delta = −0,0125 et %s à +0,0125 ;
la dérive du reste de la colonne est sa courbure. Celle d'ordre 3 est proportionnelle à delta^2 tant que e_bord reste petit : côté
delta < 0, le coefficient va de %s à %s sur %d valeurs à kappa = 0,30, de %s à %s sur %d valeurs à kappa = 0,22. Côté delta > 0, où la barrière gagne un barreau, il est moins net : de %s à %s à kappa = 0,30.
Dans ces deux séries il est négatif des deux côtés : c'est le résidu d'un seul signe de l'ordre 2, celui que la note du 14/11 laissait sans cause. À (10, 3), où
e_bord dépasse 0,4 dès |delta| = 0,025, il n'y a plus de coefficient.""" % (
    pc(etendue_G1(serieA)), fr(dabs[-1] / dabs[0], 0), mbs(serieA)[0], mbs(serieA)[1], mbs(serieB)[0], mbs(serieB)[1], pc(etendue_G1(serieB)),
    mbs(serieC)[0], mbs(serieC)[1], pc(etendue_G1(serieC), 0), sg(a_lim(serieA, -0.0125), 2), sg(a_lim(serieA, 0.0125), 2),
    sg(bA[1], 2), sg(bA[0], 2), bA[2], sg(bB[1], 2), sg(bB[0], 2), bB[2],
    sg(max(l["ln_32"] / l["delta"] ** 2 for l in serieA["lignes"] if l["delta"] > 0), 1), sg(min(l["ln_32"] / l["delta"] ** 2 for l in serieA["lignes"] if l["delta"] > 0), 1)))
T()
T("### 4.2 La parité du résidu, sur les largeurs 2D"); T()
T("| résidu après | delta < 0 : ln q < 0 | delta > 0 : ln q > 0 | lecture |")
T("|---|---|---|---|")
T("| l'ordre 1 | %d sur %d | %d sur %d | change de signe avec delta, sauf %d états côté delta < 0 |" % (sig[1]["neg_bon"], sig[1]["neg"], sig[1]["pos_bon"], sig[1]["pos"], sig[1]["neg"] - sig[1]["neg_bon"]))
T("| l'ordre 2 | %d sur %d | %d sur %d | du même côté : q2 > 1 partout |" % (sig[2]["neg_bon"], sig[2]["neg"], sig[2]["pos_bon"], sig[2]["pos"]))
T("| l'ordre 3 | %d sur %d | %d sur %d | change de signe avec delta |" % (sig[3]["neg_bon"], sig[3]["neg"], sig[3]["pos_bon"], sig[3]["pos"]))
T()
P("""Dans le domaine de la section 3.6 : %d sur %d et %d sur %d après l'ordre 3. C'est la signature d'une série en puissances de delta ;
le terme suivant serait impair. Il n'est pas calculé.""" % (sigd["neg_bon"], sigd["neg"], sigd["pos_bon"], sigd["pos"]))
T()
T("### 4.3 Les pentes, et les formes fermées qui ne tiennent pas"); T()
P("""Pente d ln Gamma / d ln g de la chaîne d'ordre 2, à état et désaccord fixés (différence centrée à 2 pour cent) : de %s à %s,
médiane %s. Elle suit pente = %s m_bord + %s (écart-type %s), et non 2 m_bord. Une variation de 2 pour cent du couplage change la largeur
d'un facteur %s à %s.""" % (fr(min(r["pente"] for r in rows), 1), fr(max(r["pente"] for r in rows), 1), fr(med([r["pente"] for r in rows]), 1), fr(pm[1], 2), fr(pm[0], 1), fr(pm[2], 1),
    fr(1.02 ** min(r["pente"] for r in rows), 2), fr(1.02 ** max(r["pente"] for r in rows), 2)))
T()
P("""La raison : sur les %d sites de barrière des %d états, 2 t / |e| va de %s à %s (médiane %s, premier décile %s). La barrière est
partout peu profonde, ce qui tient au choix des points (fraction 0,70 du seuil, largeurs au-dessus de dix planchers). Dans ce régime :""" % (
    len(raps), N, fr(raps[0], 2), fr(raps[-1], 2), fr(med(raps), 2), fr(raps[len(raps) // 10], 2)))
T()
T("| forme fermée | ln Gamma_pl = a + b × (−2 action) : b | écart-type restant (ln) | pire état (ln) |")
T("|---|---|---|---|")
T("| WKB discret, somme des arccosh(|e_m| / 2 racine(t_{m−1} t_m)) | %s | %s | %s |" % (fr(wkb[1], 2), fr(wkb[2], 2), fr(wkb[3], 2)))
T("| action du moteur, somme des ln(|e_m| / 2 t_m) | %s | %s | %s |" % (fr(mot[1], 2), fr(mot[2], 2), fr(mot[3], 2)))
T("| produit perturbatif, somme des ln(|e_m| / t_{m−1}) | %s | %s | %s |" % (fr(prod[1], 2), fr(prod[2], 2), fr(prod[3], 2)))
T()
P("""Une loi exigerait b = 1 et un écart-type de quelques centièmes. Aucune de ces formes n'est la loi ; la chaîne, qui est le calcul
exact sur l'échelle, l'est.""")
T()
T("## 5. Ce qu'un gel jugerait (proposition ; rien n'est décidé)"); T()
P("""- A. Le domaine. À des points neufs, pour les états où e_bord est sous un seuil gelé et où la chaîne d'ordre 3 est stable sous son
absorbeur, l'ordre 3 rend la largeur de plateau dans une tolérance gelée, et fait mieux que l'ordre 2. Les deux gardes se calculent avant
tout run, sans 2D.""", 0, 2)
P("""- B. Le balayage en couplage. À w2 fixé et neuf, quelques couplages sur un facteur 1,3 à 1,5 : la chaîne y prédit une largeur qui
change de plusieurs décades. C'est l'épreuve la plus dure, et la plus lisible.""", 0, 2)
P("""- C. La parité. Dans le domaine, le signe du résidu de l'ordre 3 suit celui de delta.""", 0, 2)
P("""- D. Hors domaine. L'ordre 2 reste dans les bandes du delta 98 ; l'ordre 3 y est déclaré non applicable d'avance.""", 0, 2)
T()
P("""Instrument : la sonde et la feuille du gel E-B ter, inchangées, pour que chaque largeur arrive qualifiée dans le même run. Points :
jamais joués, tirés par une règle ou par machine 2. Bornes et probabilités : annoncées après que la chaîne a calculé les points tirés, pas
avant.""")
T()
T("## 6. Limites"); T()
for s in (
    "L-1. Après coup, sur %d états connus. L'ordre 3 est dérivé sans paramètre, mais les seuils 0,3, 0,7 et 0,05 sont lus sur ces données." % N,
    "L-2. Une plume. Le bloc d'ordre 3 n'a que mes trois contrôles ; machine 2 n'a rien rejoué.",
    "L-3. La référence (largeurs de plateau) n'est pas déposée ; elle tient à l'acte en contreseing.",
    "L-4. Hors du domaine, la largeur d'ordre 3 dépend de l'absorbeur de la chaîne : les q3 donnés n'y ont pas de sens. Je n'ai pas démêlé si "
    "cette instabilité est celle de la série ou un artefact d'une chaîne à sauts longs (les sauts au troisième et au cinquième voisin peuvent y introduire des "
    "solutions parasites).",
    "L-5. L'ordre 4 n'est pas calculé. « Développement en delta » est établi sur la chaîne aux ordres 2 et 3 seulement ; « la série diverge » "
    "au-delà de e_bord = 0,7 est une lecture de deux symptômes (accord perdu, chaîne instable), pas une démonstration.",
    "L-6. Domaine couvert : fraction 0,70, canal (2, 1) de x^5, |delta| de 0,03 à 0,12, facteurs 2/3 à 3/2. Rien au-delà.",
    "L-7. Défauts de ma plume, dans ma réponse de méthode à l'opérateur (sa demande est de 18 h 44). D-LOI-1 : « la pente vaut deux fois le "
    "nombre de barreaux, donc un entier pair » est faux (section 4.3) ; « Elle sera bonne sur la pente et moins sur le préfacteur » aussi : la "
    "formule fermée n'est bonne ni sur l'une ni sur l'autre. D-LOI-2 : « S'il efface le résidu, la chaîne d'ordre 3 est la loi au niveau de "
    "l'instrument » n'est vrai que dans le domaine ; et la note du 14/11 n'annonçait que « Le troisième ordre (correction du saut entre "
    "voisins) », en oubliant les sauts au troisième et au cinquième voisin, du même ordre. D-LOI-3 : ma première lecture de l'ordre 3, par point, concluait "
    "qu'il ne fermait rien ; c'est le classement par e_bord qui montre où il ferme. D-LOI-4 : ma première écriture du bloc d'ordre 3 "
    "oubliait le saut au cinquième voisin (son commentaire disait que la parité ne laissait que deux termes) ; je l'ai vu en relisant, avant "
    "tout envoi ; les nombres de cette note sont ceux du bloc complet."):
    P("- " + s, 0, 2)
T()
T("## 7. Pièces (convention B)"); T()
T("Au registre (8d54bf9) :"); T()
for nom, k in (("scripts/m17_chaine_v17.py", "moteur"), ("scripts/chaine_ordre2_bloc_machine1_v1.py", "bloc2"), ("journal/sonde_ordre2.json", "depot"),
               ("journal/verdict_ordre2.json", "v98"), ("journal/journal_delta_98_ordre2_chaine_EA_v1.md", "acte98"),
               ("journal/note_machine1_residuel_chaine_EA_second_ordre_2026-11-14_v1.md", "note14")):
    T("    %s  %s" % (c[k], nom))
T(); T("Hors registre :"); T()
T("    %s  run_EB_ter/verdict_ter.json (machine 2, lot %s)" % (c["vter"], c["lot_res"]))
T("    %s  journal_delta_nn_qualification_EB_ter_v1.md (machine 1, projet v1)" % c["acte_ter"])
T(); T("De ce lot :"); T()
for p in PIECES:
    T("    %s  %s" % (cp[p], p))
T("    (ce script)       construction_note_loi_machine1_v1.py")
T()
texte = "\n".join(L) + "\n"
longues = [(n + 1, len(l), l[:60]) for n, l in enumerate(L) if not l.startswith("|") and len(l) > 100]; assert not longues, longues
open(SORTIE, "w", encoding="utf-8", newline="\n").write(texte)
canon_note = B(SORTIE)
def fa(x, n=3): return "%.*f" % (n, x)
Mq = []
def A(t="", ind=0, suite=None):
    suite = ind if suite is None else suite
    if not t:
        Mq.append(""); return
    Mq.extend(textwrap.wrap(" ".join(t.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
n_mb = sum(1 for r in rows if FF[(r["id"], r["rang"])]["m_bord_plus"] != r["mb"] or FF[(r["id"], r["rang"])]["m_bord_moins"] != r["mb"])
hors = [r for r in rows if r not in dom]
A("# POUR MACHINE 2 -- NOTE HORS CHAINE : LA LOI DE LA LARGEUR (ETALON, ORDRE 3, STRUCTURE)")
A("# machine 1, v1, 2026-11-15. Rien a certifier, rien a contresigner, rien a jouer d'office."); A()
A("## 0. EN CINQ PHRASES"); A()
A("""L'operateur a ouvert ("ouvre", 15/11/2026, 18 h 50, declaration de machine 1) les etapes 1 a 3 de la recherche de la loi de la largeur,
hors chaine, sans aucune largeur 2D. (1) Contre les largeurs de plateau de TON run ter, la chaine d'ordre 2 tient ses bandes (0 etat hors
borne sur %d) et son residu devient presque une constante par point. (2) Un ordre 3 derive sans parametre (correction du saut entre voisins,
sauts au troisieme et au cinquieme voisin) ferme ce residu la ou le saut au bout de la barriere reste petit : pour e_bord < 0.7 il fait mieux que l'ordre 2
a %d etats sur %d ; au-dela, pire a %d etats sur %d, et la chaine d'ordre 3 n'est plus stable sous son absorbeur. (3) Les energies, qui
n'ont rien regle, passent de %s a %s pour cent d'ecart median. (4) Pas de formule fermee courte ; des annonces que j'ai faites a l'operateur
sont fausses et la note le dit (L-7). La note (note_machine1_loi_largeur_2026-11-15_v1.md, %s) fait foi pour chaque nombre ; elle est post
hoc, d'une plume, non opposable, et sa reference (ton verdict_ter.json, %s) n'est pas deposee.""" % (
    N, mieux(sous07), len(sous07), len(sur07) - mieux(sur07), len(sur07), fa(100 * med([r["en2"] for r in rows]), 2), fa(100 * med([r["en3"] for r in rows]), 3), canon_note, c["vter"]))
A(); A("## 1. CE QUE J'AI FAIT, ET OU (E19)"); A()
A("(a) De l'arithmetique sur pieces : sortie et verdict du delta 98 (au registre), verdict_ter.json de ton lot de resultat (%s)." % c["lot_res"], 2, 6)
A("""(b) Des chaines 1D (onze diagonales, quelques dizaines de sites) aux %d etats juges du delta 98 ; et, pour la section 4.1, aux
etiquettes (6, 2), (10, 3) et (5, 1) a w2 = 2 +/- 1/80, 1/40, 1/20, 3/40, 1/10, qui ne sont pas des points de la campagne : chaine
seule.""" % E["n_juges_98"], 2, 6)
A("(c) Un controle d'algebre sur des bases tronquees hermitiennes, sans absorbeur : aucune largeur n'y est lue.", 2, 6)
A("Aucune diagonalisation 2D de machine 1, nulle part.", 2, 2)
A(); A("## 2. CE QUI EST A TOI, SI L'OPERATEUR LE DEMANDE (aucune de ces lignes n'est une commande)"); A()
A("""(i) Rederiver par TON code le terme d'ordre 3 (formule en 3.1 de la note) et le confronter a mes tables T3 et W3 : c'est la seule
piece neuve, et elle n'a qu'une plume.""", 2, 6)
A("""(ii) NE RIEN calculer en 2D a un point neuf. La section 5 de la note propose un gel dont les points seraient tires par une regle ou
par toi ; un calcul avant certification croisee les brulerait (E19).""", 2, 6)
A("(iii) Dire si la proposition de la section 5 est jugeable telle quelle par la sonde et la feuille du gel ter, et ce qui y manque.", 2, 6)
A(); A('## 3. POUR REJOUER MES PIECES (python -I -B ; levier NPY_DISABLE_CPU_FEATURES="X86_V4" chez moi)'); A()
for cmd, com in (
    ("etape1_etalon_machine1_v1.py <sonde_ordre2.json> <verdict_ordre2.json> <verdict_ter.json> <sortie.json>", "arithmetique ; secondes"),
    ("controle_algebre_ordre3_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sortie.json>", "derniere ligne : CONTROLE D'ALGEBRE : TIENT"),
    ("calcul_ordre3_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sonde_ordre2.json> <verdict_ordre2.json> <sortie.json> C1 C2 C3 C4 M1 M2 M3 M4 L1 L2 L3 L4",
     "chaines d'ordre 2 et 3 aux 132 etats ; moins d'une minute sur deux coeurs"),
    ("forme_fermee_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sonde_ordre2.json> <verdict_ordre2.json> <sortie.json>", "actions, pentes ; secondes"),
    ("structure_en_delta_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sortie.json>", "section 4.1 ; chaine seule"),
    ("construction_note_loi_machine1_v1.py <dossier des sorties> <clone du registre> <verdict_ter.json> <acte ter, projet v1> <manifeste de ton lot de resultat> <sortie.md>",
     "refait la note et ce fichier ; chaque nombre y est calcule depuis les sorties")):
    A(cmd, 2, 6); A("-> " + com, 6, 9)
A("""Le bloc d'ordre 2 est scripts/chaine_ordre2_bloc_machine1_v1.py du registre ; le bloc d'ordre 3 est ordre3_bloc_machine1_v1.py de ce
lot. Les JSON de ce lot sont ceux de ma plateforme ; la chaine d'ordre 2 refaite ici redonne celle de ton depot a %s pres au pire.""" % (
    "%.1e" % max(e["ecart_c2_depot"] for i in JUGES for e in O[i]["etats"])), 2, 2)
A(); A("## 4. OU MORDRE"); A()
for t in (
    """M-1  La formule d'ordre 3. Les denominateurs sont les energies libres du moteur. (V1) ne la confronte qu'a UNE base tronquee, une
echelle, w2 = 2.11 ; l'effectif "exact" y est MA construction (projection sur les etats propres de plus grand poids sur l'echelle, puis
orthonormalisation symetrique). Si ce n'est pas celui que tu prendrais, la pente g^5 dit seulement que ma formule et ma construction
s'accordent. Le cinquieme voisin n'y a qu'UN element, au plancher d'arrondi aux petits couplages. Et ma premiere ecriture du bloc
oubliait ce saut (D-LOI-4, vu avant envoi) : cherche s'il manque encore un terme.""",
    """M-2  La chaine d'ordre 3. Onze diagonales (sauts a 1, 2, 3 et 5 barreaux), meme absorbeur que l'ordre 2 (debut, force, longueur), meme choix de l'etat. Hors du domaine
elle depend de son absorbeur : aux %d etats hors domaine, le doubler, le diviser par deux ou le reculer de quatre sites change la largeur
jusqu'a |ln| = %s (mediane %s). Je ne sais pas si c'est la serie ou un artefact des sauts longs.""" % (len(hors), fa(max(r["stab"] for r in hors), 2), fa(med([r["stab"] for r in hors]), 2)),
    """M-3  Les chemins qui bifurquent. Les seuils 0.3, 0.7 et 0.05 sont lus sur ces donnees. Le classement par e_bord vient APRES une
premiere lecture par point qui concluait "l'ordre 3 ne ferme rien" (D-LOI-3) : j'ai change de variable apres avoir vu.""",
    """M-4  La reference. Largeurs de plateau Gamma_pl(A) de ton verdict_ter.json, acte non contresigne ; %d etats = juges par le delta 98
ET qualifies par le run ter (L3 rang 5 ecarte).""" % N,
    """M-5  "Developpement en delta a kappa fixe". Trois series, chaine seule. Le coefficient de l'ordre 3 n'est constant que cote delta < 0
et a petit e_bord ; cote delta > 0 il derive ; a (10, 3) il n'y en a pas. La forme Gamma = |delta| Phi(kappa) lue sur les largeurs 2D ne
repose que sur l'etiquette (6, 2), sept points, trois groupes de kappa presque egal (facteurs %s, %s, %s a kappa egal).""" % (fa(fg[0], 1), fa(fg[1], 1), fa(fg[2], 1)),
    """M-6  La parite. Les comptes de signes incluent des etats dont |ln q3| est sous la stabilite de la chaine elle-meme (mediane %s pour
e_bord < 0.3). Dans le domaine : %d sur %d et %d sur %d.""" % (fa(med([r["stab"] for r in bas])), sigd["neg_bon"], sigd["neg"], sigd["pos_bon"], sigd["pos"]),
    """M-7  Les pentes. Difference centree a 2 pour cent ; le bord de barriere, donc le debut de l'absorbeur de la chaine, bouge entre les
deux evaluations a %d etats sur %d. La droite pente = %s m_bord + %s est descriptive.""" % (n_mb, N, fa(pm[1], 2), fa(pm[0], 1)),
    """M-8  Les energies. L'ordre 3 n'a pas de terme diagonal (parite de x^5) : le gain vient des sauts corriges. La comparaison est faite
contre E_re - E_libre de TA sonde du delta 98.""",
    """M-9  Les citations. La note cite ma reponse de methode a l'operateur (qui n'est pas une piece : c'est une declaration) et la note du
14/11 (au registre, %s), ligne "Le troisieme ordre (correction du saut entre voisins)".""" % c["note14"]):
    A(t, 2, 7)
A(); A("## 5. RIEN D'AUTRE"); A()
A("Aucune demande, aucun delai. L'acte du gel ter (enveloppe 15d) reste la seule piece de machine 1 en attente de ta plume.")
pm2 = os.path.join(D, "POUR_MACHINE2_note_loi_largeur_machine1_v1.md"); tm = "\n".join(Mq) + "\n"; tm.encode("ascii")
assert max(len(l) for l in Mq) <= 100, [l for l in Mq if len(l) > 100]
open(pm2, "w", encoding="ascii", newline="\n").write(tm); print("ecrit %s : %d lignes, canon %s" % (os.path.basename(pm2), len(Mq), B(pm2)))
json.dump({"comptes": V, "canons": c, "pieces": cp}, open(os.path.join(D, "valeurs_note_loi_machine1_v1.json"), "w"), indent=1, sort_keys=True)
print("écrit %s : %d lignes, canon %s" % (os.path.basename(SORTIE), len(L), B(SORTIE)))
