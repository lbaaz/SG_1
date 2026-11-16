# -*- coding: ascii -*-
"""CONSTRUCTION DU RECTIFICATIF DE TEXTE A LA SECONDE PARTIE DU GEL "LARGEUR DU VIDE" (C-1, C-2 de machine 2), ECRIT AVANT LE RUN --
machine 1, v1, 2026-11-16. Chaque nombre est lu dans les sorties du dossier.
Usage : python3 -I -B construction_rectificatif_gel_vide_partie2_machine1_v1.py <dossier des sorties> <lot extrait de machine 2> <gel partie 2.md> <table gelee.json> <sortie.md>"""
import sys, os, re, json, hashlib, unicodedata, textwrap
D, M2, GEL, TABLE, SORTIE = sys.argv[1:6]
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
au = open(os.path.join(D, "authentifie_lot_m2_certification_partie2_machine1_v1.log"), encoding="ascii").read(); assert "AUTHENTIFICATION : TIENT" in au
canon_lot = re.search(r"canon du lot ([0-9a-f]{16})", au).group(1); n_pieces = int(re.search(r"au bon canon : (\d+)", au).group(1))
assert canon_lot == B(os.path.join(M2, "MANIFEST_lot_machine2_certification_gel_vide_partie2_v1.txt")) and B(GEL) == "eebd979f18d8db48" and B(TABLE) == "b71206e5daf6c741"
V = json.load(open(os.path.join(D, "verifie_C1_C2_v1.json"))); C1, C2, A7 = V["C1"], V["C2"], V["A7"]
et = open(os.path.join(M2, "certif_gel_vide_partie2_machine2", "etalement_lecteur_joues_machine2_v1.log"), encoding="utf-8").read()
s_med, s_max = re.search(r"mediane ([0-9.]+) ; q25", et).group(1), re.search(r"max ([0-9.]+)\s*$", et.split("\n")[1]).group(1)
n_et = re.search(r"etats lus \(quatre trajectoires\) : (\d+)", et).group(1)
note = open(os.path.join(M2, "POUR_MACHINE1_certification_gel_vide_partie2_machine2_v1.md"), encoding="utf-8").read()
m2_C1 = re.search(r"different des tiens de ([0-9.]+) au pire", note).group(1); m2_ecart = re.search(r"plus grand ecart ([0-9.e-]+) ;", note).group(1)
m2_canon = re.search(r"ecrit une table de canon ([0-9a-f]{16}),", note).group(1); TJ = json.load(open(TABLE))["joues"]
assert abs(float(m2_C1) - C1["ecart_max_avec_la_definition_de_la_note"]) < 0.05 and len(C2["r_du_signe_de_delta"]) == 1 and len(C2["negative"]) == 1
assert C2["r_du_signe_de_delta"][0][:2] == C2["negative"][0][:2] and C2["etats"] == TJ["etats"] and C1["forme_refaite_depuis_M0_ecart_max"] == 0.0
PIECES = ["authentifie_lot_m2_certification_vide_machine1_v1.py", "authentifie_lot_m2_certification_partie2_machine1_v1.log", "verifie_C1_C2_machine1_v1.py",
          "verifie_C1_C2_machine1_v1.log", "verifie_C1_C2_v1.json"]
L = []
def T_(s=""): L.append(s)
def P(s, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
T_('RECTIFICATIF DE TEXTE A LA SECONDE PARTIE DU GEL "LARGEUR DU VIDE" -- ECRIT AVANT LE RUN')
T_("machine 1, v1, 2026-11-16. Rien a certifier, rien a jouer. Le feu vert est a l'operateur.")
T_()
T_("0. STATUT")
P("""La seconde partie (eebd979f18d8db48, lot b1919dc9468dc437) n'est PAS modifiee et n'a pas de version 2 : la table gelee
(b71206e5daf6c741), la sonde, la feuille et le pilote restent ceux que machine 2 a certifies (lot %s, %d pieces authentifiees). Cette
piece repond a son "seul tour de correction" : ses deux corrections de texte C-1 et C-2, retrouvees par machine 1 sur ses propres
donnees, sont ecrites ici AVANT le run. Elles ne touchent aucun enonce, aucune tolerance, aucune prediction jugee. L'acte les citera.""" % (canon_lot, n_pieces))
T_()
T_("1. C-1 : LA FORME FERMEE, DEFINITION DE M0 (section 7.3 de la seconde partie)")
P("""Le texte donnait l'ecart de la forme fermee a G3* sans dire comment M0 est pris aux cellules. A lire ainsi :""")
T_("        ln Gamma = ln|delta| - B M0 + c ln M0 + d ,   M0 = (2 lambda)^(-2/3) ,")
T_("        lambda = kappa X_c / (P tau_0) ,   kappa = g X(0, 0 ; w2) / (P |delta|) ,")
T_("        tau_0 = X(0, 0 ; 2) / P ,")
P("""ou kappa est le rapport du saut au desaccord A LA CELLULE (le saut au pied de l'echelle pris au w2 de la cellule), et ou X_c et
tau_0 sont pris a w2 = 2. C'est ce que calcule predictions_vide_machine1_v1.py et ce que porte la table (champ M0) : la forme fermee
s'en refait sans ecart.""")
P("""La note sur la loi d'echelle ecrivait lambda = g X_c / (P |delta|), qui prend le saut a w2 = 2. Aux cellules, les deux lambda sont
dans un rapport de %.4f a %.4f (c'est X(0, 0 ; w2) / X(0, 0 ; 2)), et la forme fermee ainsi calculee s'ecarterait de celle de la table de
%.2f au pire, en logarithme (a %s). Constat de machine 2 (%s), retrouve.""" % (C1["rapport_lambda_min"], C1["rapport_lambda_max"], C1["ecart_max_avec_la_definition_de_la_note"], C1["cellule"], m2_C1))
P("""D-VIDE-7, defaut de ma plume. La definition manquait au texte du gel. Et l'ecriture de la note sur la loi d'echelle en
puissance de |delta| / g ne vaut qu'a la limite w2 = 2 : a desaccord fini la variable de la loi est kappa, le saut sur le desaccord,
pas g / |delta|. Aucun verdict n'en depend : la forme fermee est consignee, pas jugee.""")
T_()
T_("2. C-2 : LA PART MANQUEE AUX ETATS JOUES (section 7.2 de la seconde partie)")
P("""Le texte disait : "a 184 de ces etats la chaine rend une correction a la loi d'echelle trop petite". A lire ainsi : sur %d etats,
la part manquee (r - r de la chaine) / r est positive a %d ; elle est entre 0 et 1 a %d : la chaine y rend une correction du bon signe et
trop petite. A %d etats (%s) elle depasse 1 : r y est presque nul et la chaine rend une correction de signe contraire. A %d etat (%s) elle
est negative : la chaine y corrige trop, et c'est le seul etat ou r a le signe de delta (r = %+.4f, delta = %+.3f) ; r a le signe oppose
a delta aux %d autres. La phrase de la section 7.2, "aux etats joues r a le signe oppose a delta", se lit donc : a %d etats sur %d. La
mediane de la part manquee (%.3f) et ses medianes par cellule (de %.3f a %.3f) ne changent pas.""" % (C2["etats"], C2["part_positive"], C2["entre_0_et_1"], len(C2["au_dessus_de_1"]),
                             ", ".join("%s rang %d, r = %+.4f" % (a, b, c) for a, b, c in C2["au_dessus_de_1"]), len(C2["negative"]),
                             ", ".join("%s rang %d, part %.2f" % (a, b, c) for a, b, c in C2["negative"]), C2["r_du_signe_de_delta"][0][2], C2["r_du_signe_de_delta"][0][3],
                             C2["r_oppose_a_delta"], C2["r_oppose_a_delta"], C2["etats"], TJ["part_manquee_mediane"], TJ["part_manquee_par_cellule_min"], TJ["part_manquee_par_cellule_max"]))
P("""D-VIDE-8, defaut de ma plume : j'avais pris le compte des parts positives pour celui des corrections trop petites.""")
T_()
T_("3. A-7 : OU LES DEUX LECTURES DU SIGNE DIFFERENT")
PC = A7["residu_b_par_creneau"]; assert A7["lectures_differentes"][:8] == ["MG3", "MG4", "MG5", "MG6", "MP3", "MP4", "MP5", "MP6"]
P("""La seconde partie disait que le gel peut departager les lectures (a) et (b) du residu "a MG". Machine 2 precise : elles different a
MG et a MP, huit cellules et non quatre. Retrouve, et par le signe seul la table gelee en donne %d (%s) contre %d ou elles coincident
(%s).""" % (len(A7["lectures_differentes"]), " ".join(A7["lectures_differentes"]), len(A7["lectures_de_meme_signe"]), " ".join(A7["lectures_de_meme_signe"])))
P("""Mais le signe ne se lit que si la taille depasse ce que la chaine laisse indetermine. Sous (b), le plus grand residu attendu
vaut, pour la part manquee mediane puis pour la plus grande : %.4f et %.4f a MG ; %.4f et %.4f a MP ; %.4f et %.4f a PP ; %.4f et %.4f a
PG. La plus petite etendue de la chaine y vaut %.4f, %.4f, %.4f et %.4f. A MP et a PP le residu de la lecture (b) est donc sous
l'etendue de la chaine a toutes les cellules : le signe n'y departage rien. Il ne peut departager qu'a MG, et encore : pour la part
mediane il y est de l'ordre de l'etendue.""" % (PC["MG"]["mediane"], PC["MG"]["pire"], PC["MP"]["mediane"], PC["MP"]["pire"], PC["PP"]["mediane"], PC["PP"]["pire"],
                                                  PC["PG"]["mediane"], PC["PG"]["pire"], PC["MG"]["etendue_min"], PC["MP"]["etendue_min"], PC["PP"]["etendue_min"], PC["PG"]["etendue_min"]))
assert PC["MP"]["pire"] < PC["MP"]["etendue_min"] and PC["PP"]["pire"] < PC["PP"]["etendue_min"] and PC["MG"]["pire"] > PC["MG"]["etendue_min"]
P("""L'annonce A-7 reste ecrite sur MG ; la feuille consigne deja les deux comptes sur toutes les cellules lues. Rien ne change. Ce
que je retiens pour l'acte : un compte de signes a MP ou a PP ne se lira pas comme un arbitrage entre (a) et (b).""")
T_()
T_("4. CE QUE JE NE CHANGE PAS")
P("""L'etalement du lecteur aux %s etats deja lus du delta 100, mesure par machine 2 : mediane %s, maximum %s. Je ne l'avais pas. Mes
annonces (section 10) ont ete ecrites sans lui, avec la crainte d'un etalement plus grand ; elles restent telles qu'elles sont gelees, et
c'est A-4 a 0.32 pour NON CONCLUANT qui sera compare a l'issue. Je ne les reecris pas apres avoir lu ce nombre.""" % (n_et, s_med, s_max))
P("""La table gelee est la piece livree : mon script de predictions ne la refait "au canon" que sur ma plateforme (sur celle de machine 2 il ecrit une table de canon %s, a %s au
plus de la table gelee). Accepte.""" % (m2_canon, m2_ecart))
T_()
T_("5. PIECES DE CE LOT (convention B)")
for p in PIECES:
    T_("    %s  %s" % (B(os.path.join(D, p)), p))
T_("    (ce script)       construction_rectificatif_gel_vide_partie2_machine1_v1.py")
T_()
texte = "\n".join(L) + "\n"; texte.encode("ascii"); assert max(len(l) for l in L) <= 100, [l for l in L if len(l) > 100]
open(SORTIE, "w", encoding="ascii", newline="\n").write(texte)
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(SORTIE), len(L), B(SORTIE)))
