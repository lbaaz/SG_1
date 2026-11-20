# -*- coding: ascii -*-
"""CONSTRUCTION DE LA PREMIERE PARTIE DU GEL "PONT" : LA REGLE DE TIRAGE ET D'ELIGIBILITE -- machine 1, v1, 2026-11-17.
Chaque nombre est calcule ici depuis les sorties du lot ; les canons sont recalcules. Derive, pour la forme, de
construction_regle_tirage_vide_machine1_v1.py (registre).
Usage : python3 -I -B construction_regle_tirage_pont_machine1_v1.py <dossier des sorties> <clone du registre>
        <dossier de l'exploration du lisse> <dossier de la lecture des grandes boites> <dossier du lot de machine 2> <sortie.md>"""
import sys, os, re, json, math, hashlib, unicodedata, textwrap
from fractions import Fraction as F
D, CLONE, EXPLO, GB, LOT_M2, SORTIE = sys.argv[1:7]

def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def J(p): return json.load(open(p))

c = {"moteur": B(CLONE + "/scripts/m17_chaine_v17.py"), "bloc2": B(CLONE + "/scripts/chaine_ordre2_bloc_machine1_v1.py"),
     "bloc3": B(CLONE + "/scripts/ordre3_bloc_machine1_v1.py"), "adapte": B(CLONE + "/scripts/chaine_adaptee_bloc_machine1_v1.py"),
     "lecteur": B(CLONE + "/scripts/sonde_lecteur_gel_loi_machine1_v1.py"), "tirage": B(CLONE + "/scripts/tirage_vide_machine1_v1.py"),
     "elig": B(CLONE + "/scripts/eligibilite_vide_machine1_v1.py"),
     "gel_p1": B(CLONE + "/gels/gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md"),
     "acte102": B(CLONE + "/journal/journal_delta_102_largeur_vide_v2.md"),
     "note_lisse": B(EXPLO + "/note_machine1_pont_lisse_hors_vide_2026-11-17_v1.md"), "attendu": B(EXPLO + "/attendu_lisse_hors_vide_machine1_v1.txt"),
     "rectif": B(EXPLO + "/rectificatif_instrument_lisse_hors_vide_machine1_v1.txt"),
     "note_gb": B(GB + "/note_machine1_pont_lecture_grandes_boites_2026-11-17_v1.md"),
     "lot_m2": B(os.path.join(os.path.dirname(LOT_M2.rstrip("/")), "MANIFEST_lot_machine2_grandes_boites_resultats_v1.txt")),
     "note_m2": B(LOT_M2 + "/POUR_MACHINE1_grandes_boites_resultats_machine2_v1.md")}
assert (c["moteur"], c["bloc2"], c["bloc3"], c["adapte"], c["lecteur"], c["tirage"], c["elig"]) == (
    "82a0be882568fe0c", "7cd5977bc27bebc1", "534ba246aa3b8973", "49a40d9098b55361", "d5cc48f48e37af99", "cc1b2df637a9f3cd", "34eb68229983b1f2"), c
TETE = "2988237"
T = J(D + "/eligibilite_pont_MG_PG_v1.json"); TS = J(D + "/eligibilite_pont_MG_PG_sans_levier_v1.json"); R = T["regle"]
CT = J(D + "/controle_point_sacrifie_v1.json"); VR = J(D + "/balayage_virginite_pont_registre_v1.json"); VP = J(D + "/balayage_virginite_pont_poste_v1.json")
LL = J(EXPLO + "/lecture_lisse_hors_vide_v1.json"); CG = J(GB + "/regards_complements_v1.json"); RJ = J(GB + "/rejeu_grandes_boites_v1.json")
ORDRE = ("MG", "PG"); PROF = tuple(R["profondeurs"]); ECARTS = R["ecarts"]
assert PROF == (3, 4, 5) and len(ECARTS) == 12 and (R["seuil_etendue"], R["seuil_etendue_rho"], R["seuil_pas"], R["garde_e_bord"]) == (0.02, 0.03, 0.10, 0.7)
cands = {s: T["creneaux"][s]["candidats"] for s in ORDRE}
cells = [(s, cd, x) for s in ORDRE for cd in cands[s] for x in cd["cellules"]]
n_w2 = sum(len(cands[s]) for s in ORDRE); n_cel = len(cells); assert (n_w2, n_cel) == (16, 48)
# le meme calcul sans le levier
diff = max(abs(a["ln_G3"] - b["ln_G3"]) for (_, _, a), (_, _, b) in zip(cells, [(s, cd, x) for s in ORDRE for cd in TS["creneaux"][s]["candidats"] for x in cd["cellules"]]))
bascule = sum(a["eligible"] != b["eligible"] or a["g"] != b["g"] for (_, _, a), (_, _, b) in zip(cells, [(s, cd, x) for s in ORDRE for cd in TS["creneaux"][s]["candidats"] for x in cd["cellules"]]))
# motifs d'ineligibilite
def conds(x):
    return {"i": x["m_bord"] == x["m"], "ii": x["e_bord"] < 0.7, "iii": x["etendue"] is not None and x["etendue"] <= 0.02,
            "iv": x["etendue_rho_max"] is not None and x["etendue_rho_max"] <= 0.03, "v": x["pas_max"] is not None and x["pas_max"] <= 0.10}
for (_, _, x) in cells: assert x["eligible"] == all(conds(x).values())
echecs = {k: sum(1 for (_, _, x) in cells if not conds(x)[k]) for k in ("i", "ii", "iii", "iv", "v")}
echecs_v_MG = sum(1 for (s, _, x) in cells if s == "MG" and not conds(x)["v"])
el = {s: [cd for cd in cands[s] if cd["eligible"]] for s in ORDRE}
p_rien = {s: (1.0 - len(el[s]) / float(len(cands[s]))) ** 5 for s in ORDRE}

L = []
def A(s=""): L.append(s)
def P(texte, indent=2, suite=None):
    for l in textwrap.wrap(" ".join(texte.split()), width=100, initial_indent=" " * indent, subsequent_indent=" " * (indent if suite is None else suite),
                           break_long_words=False, break_on_hyphens=False): L.append(l)

A('GEL "PONT" -- PREMIERE PARTIE : LA REGLE DE TIRAGE ET D\'ELIGIBILITE DES CELLULES')
A("PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-17.")
A("A CERTIFIER PAR MACHINE 2 AVANT QUE L'OPERATEUR DONNE LA GRAINE.")
A()
A("0. STATUT")
P("""Cette piece fixe COMMENT les cellules du gel seront tirees et QUAND un tirage est admis. Elle ne fixe ni les enonces juges, ni les
tolerances, ni les probabilites, ni l'instrument : c'est la seconde partie, ecrite apres le tirage sur les chaines seules, et certifiee avant
tout run.""")
P("""L'objet du gel, "le pont" : la largeur que le lecteur lit sous absorbeur est-elle la force de couplage du vide (l'etat que porte le site
(0, 0) du systeme a fantome) au spectre REEL de la boite fermee ? Trois appuis ont ete vus, hors chaine, a un seul point, w2 = 101/50, qui est
sacrifie : (L) loin de l'energie du vide, la densite du vide dans le systeme 2D sous absorbeur est celle de la chaine d'ordre 3 ; (S) dans la
boite 2D fermee, les parts des niveaux se somment a la largeur de la fenetre ; (C) le nombre de niveaux qui portent cette force croit avec le
cote de la boite. Ce gel les eprouve a des points que personne n'a choisis ni joues.""")
P("""Ouverture, selon machine 1 : a la fin de la note du 17/11 (%s, hors chaine, classe 3), machine 1 a propose de geler le pont sur un point
neuf ; l'operateur a ecrit "Go rediger le gel." (17/11/2026, 00 h 56). A l'operateur de l'attester ou de le dementir.""" % c["note_lisse"])
P("""E19. Selon ses pieces (section 9), machine 1 n'a joue aucune 2D du systeme a fantome a un w2 candidat de ce gel : ni boite fermee, ni
densite sous absorbeur hors de l'energie du vide, ni largeur. Les 2D du pont qu'elle a jouees ou lues sont toutes a w2 = 101/50, un centieme :
des boites fermees jusqu'au cote 201 et des croisements (sa note v3 du pont, 16/11, dans un autre conteneur), les niveaux des boites de machine
2 jusqu'au cote 402 (lot %s), et des densites sous absorbeur de 0.05 a 8 |delta| du vide (note %s). Le gel "largeur du vide" a fait jouer le
lecteur creux, a l'energie du vide, a w2 = 1.982, 1.997, 2.005 et 2.017 (acte %s) : les deux qui tombent dans les creneaux de ce gel sont
retires des candidats. Aucune des deux machines ne jouera une 2D du systeme a fantome, de quelque sorte, a un w2 candidat avant la
certification croisee de la seconde partie et le feu vert ecrit de l'operateur. Machine 2 dit ce qu'il en est pour elle (section 10, d).
Tout ce que cette piece calcule est une chaine a une dimension.""" % (c["lot_m2"], c["note_lisse"], c["acte102"]))
A()
A("1. SOURCES (convention B)")
for canon, txt in ((c["moteur"], "scripts/m17_chaine_v17.py (registre %s), le moteur" % TETE),
                   (c["bloc2"], "scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2"),
                   (c["bloc3"], "scripts/ordre3_bloc_machine1_v1.py (registre), le bloc d'ordre 3"),
                   (c["adapte"], "scripts/chaine_adaptee_bloc_machine1_v1.py (registre), l'absorbeur adapte"),
                   (c["lecteur"], "scripts/sonde_lecteur_gel_loi_machine1_v1.py (registre), le lecteur creux ; non lu ici"),
                   (c["gel_p1"], "gels/gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md (registre) : la regle dont celle-ci reprend la forme, les kappa_m et le couplage ecrit"),
                   (c["elig"], "scripts/eligibilite_vide_machine1_v1.py (registre), dont l'eligibilite de ce lot derive"),
                   (c["tirage"], "scripts/tirage_vide_machine1_v1.py (registre), dont le tirage de ce lot derive"),
                   (c["acte102"], "journal/journal_delta_102_largeur_vide_v2.md (registre) : les w2 que le gel du vide a joues"),
                   (c["lot_m2"], "lot de machine 2 lot_machine2_2026-11-17_grandes_boites_resultats_v1, HORS REGISTRE : les boites fermees des cotes 190 a 402 au point sacrifie ; sa note : %s" % c["note_m2"]),
                   (c["note_gb"], "note_machine1_pont_lecture_grandes_boites_2026-11-17_v1.md, HORS REGISTRE : lecture de ces boites"),
                   (c["note_lisse"], "note_machine1_pont_lisse_hors_vide_2026-11-17_v1.md, HORS REGISTRE : la chaine d'ordre 3 contre la 2D ouverte, loin de l'energie du vide ; son attendu %s et son rectificatif %s" % (c["attendu"], c["rectif"]))):
    P("%s %s" % (canon, txt), indent=4, suite=22)
P("""Les deux notes de machine 1 et leurs pieces voyagent avec ce lot. La note v3 du pont et les attendus des grandes boites (lot
4e15e302d97e26b8, que la note du lot de machine 2 dit avoir authentifie) sont detenus par machine 2 et sont au projet de l'operateur ; ce
conteneur de machine 1 ne les detient pas en fichiers et leurs canons ne sont pas recalcules ici.""")
A()
A("2. LES CRENEAUX ET LES CELLULES")
P("""Deux creneaux, huit w2 candidats chacun. Les w2 candidats sont au millieme ; les centiemes en sont exclus ; 0.01 < |w2 - 2| < 0.02 ; et
les deux w2 que le gel du vide a joues (1.982 et 2.017) en sont retires.""")
for s, lab in (("MG", "delta < 0"), ("PG", "delta > 0")):
    P("%s, %s : w2 = %s" % (s, lab, ", ".join("%.3f" % float(F(cd["w2"])) for cd in cands[s])), indent=4, suite=24)
P("Trois PROFONDEURS de barriere m, chacune avec son rapport kappa_m, repris tels quels du gel du vide :")
P("m = 3 : %s ; m = 4 : %s ; m = 5 : %s" % (R["kappa"]["3"], R["kappa"]["4"], R["kappa"]["5"]), indent=4)
P("Une CELLULE est un couple (w2, m). Son couplage est")
A("        g = kappa_m x |w2 - 2| x P / X(w2) ,")
A("        X(w2) = X_saut_reel(P, 2, 1, 0, 0, w2) du moteur, P = 5,")
P("""calcule en double precision puis ARRONDI a six chiffres significatifs (le format "%.5e" de Python) : le couplage de la cellule EST le
nombre decimal ainsi ecrit. C'est la regle du gel du vide. Au point sacrifie, w2 = 101/50 et m = 3, elle rend le couplage de l'exploration,
""" + CT["cellule"]["g"] + """.""")
P("Un tirage donne un w2 par creneau, donc six cellules, nommees par le creneau et la profondeur : MG3, MG4, MG5, PG3, PG4, PG5.")
A()
A("3. LE TIRAGE")
P("Le w2 du creneau s au rang r est l'element de numero")
A('        int( sha256("<graine>|<s>|<r>") ecrit en hexadecimal, 16 )  modulo  n_s')
P("""de la liste CROISSANTE des n_s w2 candidats du creneau, numerotee a partir de 0. La chaine hachee est codee en ASCII ; s vaut MG ou PG ;
r s'ecrit en decimal, sans zero devant ; la barre verticale est le caractere 124. C'est le hachage des deux gels deposes.""")
P("""LA GRAINE est une suite de chiffres (0 a 9), d'au moins six chiffres, donnee par L'OPERATEUR, par ecrit, aux deux machines, APRES la
certification de cette piece et apres que la table commune de la section 5 existe. Elle est reportee telle quelle, zeros de tete compris, dans
la seconde partie. Ni machine 1 ni machine 2 ne la choisit, ne la propose, ni ne la commente avant de l'avoir recue.""")
P("""Chaque machine tire par SON code. Exemple de controle, sur une graine de demonstration qui n'est pas une suite de chiffres et ne peut
donc pas etre la graine :""")
demo = [l.rstrip("\n") for l in open(D + "/tirage_pont_machine1_v1_autotest.log") if l.startswith("sha256(")]
assert len(demo) == 4
for l in demo: A("    " + l)
A()
A("4. L'ELIGIBILITE D'UNE CELLULE (chaine seule, aucune 2D)")
P("""4.1 La barriere : sites = barriere(0, 0, w2, g, avec Sigma2) du moteur ; m_bord = son dernier site ; e_bord = |m_bord delta + Sigma2(m_bord)
- Sigma2(0)|, avec delta = w2 - 2.""", suite=6)
P("""4.2 Les tables : tables_ordre2(0, 0, w2, g, sites, M_facteur 4) puis tables_ordre3, des blocs deposes : par site m de l'echelle, le decalage
S_m, le saut t_m, le saut au second voisin U_m, et a l'ordre 3 la correction T3_m et les sauts W3_m et W5_m.""", suite=6)
P("""4.3 La chaine sous ABSORBEUR ADAPTE, variante (a, c, L), est la matrice du bloc depose (matrice_adaptee) : sur la diagonale, m delta + S_m
- S_0 - i W_m ; hors diagonale, t_m + T3_m entre m et m + 1, U_m entre m et m + 2, W3_m entre m et m + 3, W5_m entre m et m + 5 ; W_m = a |t_m|
((m - debut) / L)^2 pour debut < m <= debut + L, 0 ailleurs, debut = m_bord + c. Dix-huit variantes : a = 1, 2, 4 ; c = 6, 8, 10 ; L = 16, 24.
La chaine d'ORDRE 2 est la meme matrice avec T3, W3 et W5 nuls.""", suite=6)
P("""4.4 Au vide. Largeur d'une variante : Gamma = -2 Im(E), E etant la valeur propre de la matrice d'ordre 3 dont le vecteur propre, norme,
porte le plus grand poids sur le site 0 (a poids egal, la plus petite partie reelle). PLATEAU G3* : exponentielle de la mediane des dix-huit ln
Gamma (moyenne des deux valeurs centrales) ; ETENDUE : le plus grand moins le plus petit. C'est la regle du gel du vide.""", suite=6)
P("""4.5 Hors du vide. Douze ECARTS x, en unites de |delta| : %s. A l'ecart x, pour une variante et un ordre o (2 ou 3) : E_v est la partie
reelle de la valeur propre du 4.4 prise sur la matrice d'ordre o ; E = E_v - x delta, c'est-a-dire du cote OPPOSE au desaccord (sous le vide si
delta > 0, au-dessus si delta < 0) ; la DENSITE du site 0 est""" % ", ".join("%g" % x for x in ECARTS), suite=6)
A("          rho = -(1 / pi) Im [ (E - H)^(-1) ]_00 ,")
P("""H etant la matrice et l'indice 0 le site 0. C'est une propriete de la matrice : chaque machine la calcule par sa methode ; machine 1 la
lit par le flux, (1 / pi) somme_m W_m |y_m|^2 avec y = (E - H)^(-1) e_0, qui lui est egal. Le LISSE rho_o(x) est l'exponentielle de la mediane
des dix-huit ln rho ; son ETENDUE est le plus grand moins le plus petit des dix-huit ln rho. Le PAS de l'ordre 2 a l'ordre 3 est ln rho_2(x) -
ln rho_3(x).""", indent=6)
P("""4.6 La cellule (w2, m) est ELIGIBLE si : (i) m_bord = m ; (ii) e_bord < 0.7 ; (iii) les dix-huit largeurs au vide sont strictement
positives et leur etendue est <= 0.02 ; (iv) a chacun des douze ecarts, les dix-huit densites d'ordre 3 sont strictement positives et l'etendue
du lisse est <= 0.03 ; (v) a chacun des douze ecarts, le pas de l'ordre 2 a l'ordre 3 est, en valeur absolue, <= 0.10.""", suite=6)
P("4.7 Un w2 candidat est ELIGIBLE si ses trois cellules le sont.", suite=6)
P("""4.8 D'ou viennent les nombres. (i), (ii), (iii), les kappa_m et les dix-huit variantes sont ceux du gel du vide. Les douze ecarts sont
ceux de l'exploration du 17/11. Les seuils 0.03 et 0.10 sont poses ici, APRES cette exploration, qui a vu au point sacrifie (3 barreaux) une
etendue du lisse de %.4f au plus et un pas de %.4f au plus, et AVANT d'avoir calcule une seule cellule candidate sous cette regle. La condition
(v) borne le domaine a la region ou la serie de la chaine avance a petits pas loin de l'energie du vide ; ce n'est pas une mesure de l'erreur
de l'ordre 3. Aucun de ces nombres ne sera regle ensuite : ils ne l'ont pas ete quand la condition (v) a ecarte des cellules (section 7)."""
  % (CT["cellule"]["etendue_rho_max"], CT["cellule"]["pas_max"]), suite=6)
A()
A("5. LA TABLE COMMUNE, AVANT LA GRAINE")
P("""Chaque machine calcule par SA chaine l'eligibilite des %d cellules candidates (%d w2) AVANT que la graine existe. La table de machine 1
est en section 7. Machine 2 rend la sienne avec sa certification. LA TABLE COMMUNE est leur ET : un w2 candidat y est eligible si et seulement
s'il l'est dans les deux tables ET si les couplages ecrits de ses trois cellules sont les memes dans les deux. Elle ne depend d'aucune graine.
Un desaccord entre les deux tables est dit dans la certification ; il n'arrete pas le gel.""" % (n_cel, n_w2))
P("""Format d'une table : JSON, creneaux -> <nom du creneau> -> candidats -> liste de {"w2": "<fraction irreductible>", "eligible": true ou
false, "cellules": liste de {"m": <entier>, "g": "<le decimal a six chiffres>", "eligible": true ou false}}.""")
A()
A("6. LA REGLE DES RANGS")
P("""Pour chaque creneau, dans l'ordre MG puis PG et independamment : rang 0 ; si le w2 tire n'est pas eligible dans la table commune, rang
1, et ainsi de suite, pour le CRENEAU ENTIER (jamais cellule par cellule). Au plus cinq rangs, de 0 a 4. Si un creneau n'a pas de w2 eligible
en cinq rangs : PAS DE GEL, et on le dit. Un meme w2 peut sortir a deux rangs ; il n'est pas retire de la liste.""")
P("""Si les deux machines ne tirent pas les memes cellules, avec les memes couplages ecrits, a partir de la meme graine et de la meme table
commune : PAS DE GEL tant que l'ecart n'est pas explique par ecrit, et la graine n'est pas changee.""")
A()
A("7. LA TABLE DE MACHINE 1 (%d cellules)" % n_cel)
P("""Par cellule, dans l'ordre : l'etendue au vide, la plus grande etendue du lisse d'ordre 3 sur les douze ecarts, le plus grand pas de
l'ordre 2 a l'ordre 3 en valeur absolue ; un point d'exclamation marque une cellule ineligible. Les couplages ecrits sont dans la table JSON
(eligibilite_pont_MG_PG_v1.json, %s).""" % B(D + "/eligibilite_pont_MG_PG_v1.json"))
for s in ORDRE:
    A("  creneau %s : %d w2 eligibles sur %d" % (s, len(el[s]), len(cands[s])))
    for cd in cands[s]:
        A("  %.3f  %s  %s" % (float(F(cd["w2"])), "  ".join("m%d %.4f %.4f %.4f%s" % (x["m"], x["etendue"], x["etendue_rho_max"], x["pas_max"], "" if x["eligible"] else "!")
                                                         for x in cd["cellules"]), "ELIGIBLE" if cd["eligible"] else "INELIGIBLE"))
P("Par creneau et par profondeur, sur les huit w2 :")
A("    creneau  m   e_bord   etendue   etendue    pas      plateau predit G3*    rho_3 |delta| a huit")
A("                 max      au vide   du lisse   max      de ... a ...          |delta| : de ... a ...")
for s in ORDRE:
    for m in PROF:
        X = [x for (s2, _, x) in cells if s2 == s and x["m"] == m]
        A("    %-7s  %d   %.3f    %.4f    %.4f     %.4f   %.1e a %.1e    %.0e a %.0e" % (s, m, max(x["e_bord"] for x in X), max(x["etendue"] for x in X), max(x["etendue_rho_max"] for x in X),
          max(x["pas_max"] for x in X), math.exp(min(x["ln_G3"] for x in X)), math.exp(max(x["ln_G3"] for x in X)),
          math.exp(min(x["ln_rho3_8_delta"] for x in X)), math.exp(max(x["ln_rho3_8_delta"] for x in X))))
assert echecs["i"] == echecs["ii"] == echecs["iii"] == echecs["iv"] == 0 and echecs["v"] == echecs_v_MG
pas_de = {(s, int(round(abs(float(F(cd["w2"])) - 2.0) * 1000)), x["m"]): x["pas_max"] for (s, cd, x) in cells}
rapports = [pas_de[("MG", d, m)] / pas_de[("PG", d, m)] for (s, d, m) in pas_de if s == "MG" and ("PG", d, m) in pas_de]
assert len(rapports) == 21, len(rapports)
P("""Les conditions (i) a (iv) n'ecartent aucune cellule. La condition (v) en ecarte %d, toutes dans le creneau MG : a |delta| et a profondeur
egaux (%d paires), le plus grand pas de l'ordre 2 a l'ordre 3 est de %.1f a %.1f fois plus grand du cote delta < 0. Restent eligibles %d w2 sur %d dans MG (%s)
et %d sur %d dans PG. L'eligibilite trie donc ici, a la difference du gel du vide : le tirage n'est pas uniforme sur les candidats de MG, et le
domaine du gel, du cote delta < 0, s'arrete a |delta| = %.3f. La probabilite qu'un creneau n'ait aucun w2 eligible en cinq rangs vaut %.4f pour
MG et %.0f pour PG, sous la table de machine 1.""" % (echecs["v"], len(rapports), min(rapports), max(rapports), len(el["MG"]), len(cands["MG"]), ", ".join("%.3f" % float(F(cd["w2"])) for cd in el["MG"]),
   len(el["PG"]), len(cands["PG"]), max(abs(float(F(cd["w2"])) - 2.0) for cd in el["MG"]), p_rien["MG"], p_rien["PG"]))
P("""Le plus petit poids du site 0 dans l'etat lu est %.4f. La derniere colonne donne l'echelle des plus petits poids qu'une boite fermee
devra rendre a 8 |delta| du vide (un niveau y porte un poids de l'ordre de rho_3 fois sa part, elle-meme une fraction de |delta|). Le meme
calcul sous l'autre reglage de numpy de machine 1 (sans le levier NPY_DISABLE_CPU_FEATURES) : %d eligibilite ou couplage ecrit change, plus
grand ecart sur ln G3 %g.""" % (min(x["poids_min"] for (_, _, x) in cells), bascule, diff))
P("""Controle du script contre la piece de l'exploration, a w2 = 101/50 et 3 barreaux, qui n'est pas candidat : %d comparaisons, plus grand
ecart %g ; la cellule y est eligible.""" % (CT["comparaisons"], max(CT["pire_ecart"], CT["ecart_largeur"])))
assert CT["tient"] and CT["cellule"]["eligible"]
A()
A("8. FAISABILITE, ET CE QUE LA SECONDE PARTIE DEMANDERA")
durees = []
for a in "ABCDE":
    for l in open(EXPLO + "/lisse_2d_%s_v1.log" % a):
        m = re.search(r"^  k = .*\((\d+) s\)\s*$", l)
        if m: durees.append(int(m.group(1)) / 13.0)
note_m2 = open(LOT_M2 + "/POUR_MACHINE1_grandes_boites_resultats_machine2_v1.md", encoding="utf-8").read()
CIT = "36 a 67 s aux cotes 190-209 ; 158 a 228 s aux cotes 297-302 ; 515 a 734 s aux cotes 397-402"
assert CIT in note_m2 and "environ 1.6 Go par processus a 300" in note_m2
P("""Boites fermees. Au point sacrifie, a 3 barreaux, machine 2 a joue 32 boites des cotes 190 a 402 sur BOCAL4, chaque niveau lu deux fois ;
sa note (%s) donne : "%s", et "environ 1.6 Go par processus a 300". Sur %d niveaux, %d n'est pas fiable. A 4 et 5 barreaux, machine 1 n'a lu
des boites fermees que jusqu'au cote 151 (sa note v3 du pont). La seconde partie demandera des boites fermees de cote 300 AU PLUS, aux trois
profondeurs et aux deux signes de delta.""" % (c["note_m2"], CIT, sum(RJ[k]["niveaux"] for k in RJ), sum(RJ[k]["non_fiables"] for k in RJ)))
P("""Densite 2D sous absorbeur hors du vide. Sur le poste de machine 1, au point sacrifie : boites de 104 a 134 quanta de cote, de %.1f a
%.1f s par factorisation creuse, treize factorisations par barreau et par absorbeur. Les quatre absorbeurs du lecteur depose s'y accordent a
%.4f pres sous la routine de plateau deposee. La seconde partie demandera ce calcul aux six cellules, a la geometrie du lecteur (r_c = 2
(m_bord + max(8, m_bord)) + 2 ; boite = bord + couches), soit des boites de %d au plus pour 5 barreaux, et de %d si un absorbeur de 100 couches
au bord recule de 30 est ajoute.""" % (min(durees), max(durees), max(p["etendue_absorbeurs"] for p in LL["par_x"]), 2 * (5 + 8) + 2 + 100, 2 * (5 + 8) + 2 + 30 + 100))
P("""Ce que cette section NE montre PAS : qu'une boite fermee se lit a delta < 0 (rien n'y a ete joue en 2D, a aucun w2), ni que les poids
les plus petits de la table de la section 7 (5 barreaux, 8 |delta|) sortent fiables d'une boite de cote 300. La seconde partie dira ce que vaut
une cellule dont trop de niveaux ne sont pas fiables.""")
A()
A("9. VIRGINITE")
P("""Balayage de machine 1, par recherche de texte, des seize w2 candidats : leur fraction irreductible ; leur ecriture au millieme apres
"w2" ; dans les JSON, une cle "delta" qui les designe.""")
P("""Au registre (%s, %d fichiers lus) : %d fichiers portent un w2 candidat, sous %d noms. Ce sont les pieces de la premiere partie du gel du
vide (ses tables d'eligibilite des deux machines, ses tirages de demonstration, le texte du gel, sa certification, ses balayages) : des
chaines a une dimension et des listes. Aucun n'a le nom d'une sortie 2D (sonde, verdict, boite).""" % (TETE, VR["lus"], len(VR["touches"]), len(VR["noms"])), indent=4)
P("""Sur le poste de machine 1, hors des clones du registre et du dossier de ce gel (%d fichiers lus) : %d fichier porte un w2 candidat.
Ce conteneur n'est pas celui ou l'exploration du pont du 16/11 a ete jouee ; ce balayage ne le voit pas.""" % (VP["lus"], len(VP["touches"])), indent=4)
assert len(VR["nom_2d"]) == 0 and len(VP["touches"]) == 0
P("""Une recherche de texte n'est pas une preuve d'absence. Machine 2 tient les archives des runs et de ses propres explorations, et fait le
sien.""")
A()
A("10. CE QUE MACHINE 2 CERTIFIE")
for l in ("(a) que les definitions des sections 2 et 4, avec les blocs deposes, suffisent a calculer l'eligibilite sans lire le code de machine 1 ;",
          "(b) SA table d'eligibilite des %d cellules, par sa chaine, densites hors du vide comprises ; et la table commune qui en resulte ;" % n_cel,
          "(c) que son tirage, sur la graine de demonstration, rend les memes numeros que la section 3 et que le journal d'autotest ;",
          "(d) SON balayage de ses archives et de ses explorations : aucune boite fermee, aucune densite 2D hors de l'energie du vide et aucune largeur 2D du systeme a fantome a un w2 candidat de ce gel ;",
          "(e) ce que BOCAL4 peut jouer : des boites fermees jusqu'au cote 300, a 3, 4 et 5 barreaux, ou jusqu'ou il le peut."):
    P(l, suite=6)
A()
A("11. LA SUITE, DANS L'ORDRE")
for l in ("(1) machine 2 certifie cette piece et rend sa table ; la table commune existe ;",
          "(2) l'operateur donne la graine aux deux machines ;",
          "(3) chaque machine tire ; les cellules sont les memes, ou PAS DE GEL ;",
          """(4) machine 1 ecrit la seconde partie : l'instrument, la table gelee des six cellules avec ce que les chaines seules en predisent,
          les enonces et leurs tolerances, ce que chaque issue engage, ce que vaut une cellule illisible, et les annonces de la plume. Trois
          familles d'enonces, la cellule pour unite : (L) la densite 2D sous absorbeur aux douze ecarts, avec le hamiltonien et les absorbeurs du
          bloc depose du lecteur, contre le lisse d'ordre 3 ; (S) la somme des parts des niveaux de la boite fermee, sur la largeur de la fenetre ; (C) la croissance
          du nombre de niveaux de la fenetre avec le cote. L'instrument de la boite fermee sera ecrit par machine 1 et ne recopiera pas celui
          de machine 2, qui reste une seconde feuille independante ;""",
          "(5) machine 2 certifie la seconde partie ; l'operateur donne le feu vert par ecrit ; machine 2 joue, une fois."):
    P(l, suite=6)
P("""Une question sera posee a cote des enonces, sans faire tomber le gel : au point sacrifie la somme des parts vaut %.3f +- %.3f sur 32
boites, et ce n'est pas le lisse (la chaine d'ordre 3 y rend la densite 2D a %.4f pres en moyenne sur la fenetre). Le run dira, toutes cellules
confondues, si cet exces se retrouve.""" % (CG["E"]["somme"], CG["E"]["erreur"], abs(LL["moyenne_fenetre"] - 1.0)))
A()
A("12. CE QUE CETTE PIECE NE FAIT PAS, ET SES ECARTS A LA REGLE DU GEL PRECEDENT")
for l in ("- Elle ne tire rien et ne connait aucune graine.",
          "- Elle ne donne aucun enonce ni aucune tolerance : c'est a la seconde partie, avant le run.",
          """- Ecart 1 : deux creneaux au lieu de quatre. Les petits desaccords sont hors de portee des boites fermees : au point sacrifie le
          nombre de niveaux de la fenetre croit comme le cote, et la lecture de machine 1, non eprouvee ailleurs, est qu'il croit comme le cote
          fois |delta|.""",
          "- Ecart 2 : les deux w2 que le gel du vide a joues sont retires des candidats ; huit w2 par creneau au lieu de neuf.",
          "- Ecart 3 : trois profondeurs, toutes jugees ; pas de ligne profonde.",
          """- Ecart 4 : deux conditions d'eligibilite de plus, (iv) et (v), hors de l'energie du vide. Elles viennent d'une exploration a un
          seul point et a un seul signe de delta ; (v) ecarte trois w2 du creneau MG.""",
          """- Le creneau MG est joue a l'aveugle pour la 2D : aucune boite fermee et aucune densite hors du vide n'a ete regardee a delta < 0,
          a aucun w2. C'est voulu.""",
          "- Les bornes des creneaux, les profondeurs, les douze ecarts et les seuils 0.03 et 0.10 sont de la plume de machine 1.",
          "- La definition du hamiltonien effectif est celle des blocs deposes (forme symetrique) ; aucune autre n'est essayee."):
    P(l, suite=4)
A()
A("13. PIECES DE CE LOT (convention B)")
PIECES = ["eligibilite_pont_machine1_v1.py", "eligibilite_pont_MG_PG_v1.log", "eligibilite_pont_MG_PG_v1.json", "eligibilite_pont_MG_PG_sans_levier_v1.log",
          "eligibilite_pont_MG_PG_sans_levier_v1.json", "controle_point_sacrifie_machine1_v1.log", "controle_point_sacrifie_v1.json",
          "tirage_pont_machine1_v1.py", "tirage_pont_machine1_v1_autotest.log", "tirage_pont_machine1_v1_demonstration.log",
          "balayage_virginite_pont_machine1_v1.py", "balayage_virginite_pont_registre_v1.log", "balayage_virginite_pont_registre_v1.json",
          "balayage_virginite_pont_poste_v1.log", "balayage_virginite_pont_poste_v1.json"]
for p in PIECES: A("    %s  %s" % (B(os.path.join(D, p)), p))
A("  de l'exploration du 17/11, qui voyage avec ce lot :")
EXP = [(EXPLO, x) for x in ("note_machine1_pont_lisse_hors_vide_2026-11-17_v1.md", "attendu_lisse_hors_vide_machine1_v1.txt", "rectificatif_instrument_lisse_hors_vide_machine1_v1.txt",
        "lisse_chaine_machine1_v1.py", "lisse_chaine_machine1_v1.log", "lisse_chaine_v1.json", "lisse_2d_machine1_v1.py",
        "lisse_2d_A_v1.log", "lisse_2d_A_v1.json", "lisse_2d_A_bords_v1.log", "lisse_2d_A_bords_v1.json", "lisse_2d_B_v1.log", "lisse_2d_B_v1.json", "lisse_2d_B_bords_v1.log", "lisse_2d_B_bords_v1.json",
        "lisse_2d_C_v1.log", "lisse_2d_C_v1.json", "lisse_2d_C_bords_v1.log", "lisse_2d_C_bords_v1.json", "lisse_2d_D_v1.log", "lisse_2d_D_v1.json", "lisse_2d_D_bords_v1.log", "lisse_2d_D_bords_v1.json",
        "lisse_2d_E_v1.log", "lisse_2d_E_v1.json", "lecture_lisse_hors_vide_machine1_v1.py", "lecture_lisse_hors_vide_machine1_v1.log", "lecture_lisse_hors_vide_v1.json",
        "controle_absorbeur_recule_machine1_v1.py", "controle_absorbeur_recule_machine1_v1.log", "controle_absorbeur_recule_v1.json", "construction_note_lisse_hors_vide_machine1_v1.py")] + \
      [(GB, x) for x in ("note_machine1_pont_lecture_grandes_boites_2026-11-17_v1.md", "rejeu_grandes_boites_machine1_v1.py", "rejeu_grandes_boites_machine1_v1.log", "rejeu_grandes_boites_v1.json",
        "regards_niveaux_machine1_v1.py", "regards_niveaux_machine1_v1.log", "regards_niveaux_v1.json", "regards_complements_machine1_v1.py", "regards_complements_machine1_v1.log",
        "regards_complements_v1.json", "construction_note_lecture_grandes_boites_machine1_v1.py")]
for d, p in EXP: A("    %s  %s" % (B(os.path.join(d, p)), p))
A("    (ce script)       construction_regle_tirage_pont_machine1_v1.py")
A()
A("-- FIN gel_pont_partie1_regle_tirage_pre_enregistrement_v1 --")
txt = "\n".join(L) + "\n"
assert all(ord(ch) < 128 for ch in txt), [ch for ch in txt if ord(ch) >= 128][:5]
longues = [(i + 1, len(l)) for i, l in enumerate(L) if len(l) > 100]
if longues:
    for i, n in longues: print(n, repr(L[i - 1]))
assert not longues, longues
assert txt.count("%") == 1 and '"%.5e"' in txt          # le seul signe pour cent est celui du format du couplage, comme au gel du vide
open(SORTIE, "w", encoding="ascii", newline="\n").write(txt)
json.dump({"pieces": PIECES, "exploration": [[d, p] for d, p in EXP]}, open(os.path.join(D, "liste_pieces_lot_v1.json"), "w"), indent=1)
print("ecrit : %s ; %d lignes ; canon %s" % (SORTIE, len(L), B(SORTIE)))
