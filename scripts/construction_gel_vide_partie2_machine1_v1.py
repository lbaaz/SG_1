# -*- coding: ascii -*-
"""CONSTRUCTION DE LA SECONDE PARTIE DU GEL "LARGEUR DU VIDE" : L'INSTRUMENT, LES ENONCES, LES TOLERANCES,
et de son POUR_MACHINE2 -- machine 1, v1, 2026-11-16. Chaque nombre est calcule ici depuis les pieces du lot.
Usage : python3 -I -B construction_gel_vide_partie2_machine1_v1.py <dossier de ce lot> <clone du registre> <dossier du lot de la
        premiere partie> <lot extrait de la certification de machine 2> <dossier du lot de reception de machine 1>
        <dossier du lot de la note sur le vide> <dossier du lot de la loi d'echelle> <sortie.md>"""
import sys, os, re, json, math, hashlib, unicodedata, textwrap
from fractions import Fraction as F
D, CLONE, P1, M2, REC, LOT_VIDE, LOT_ECH, SORTIE = sys.argv[1:9]
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
J = lambda nom: json.load(open(os.path.join(D, nom)))
lire = lambda nom: open(os.path.join(D, nom), encoding="ascii").read()
c = {"moteur": B(CLONE + "/scripts/m17_chaine_v17.py"), "bloc2": B(CLONE + "/scripts/chaine_ordre2_bloc_machine1_v1.py"), "bloc3": B(CLONE + "/scripts/ordre3_bloc_machine1_v1.py"),
     "sonde_lecteur": B(CLONE + "/scripts/sonde_lecteur_gel_loi_machine1_v1.py"), "feuille_lecteur": B(CLONE + "/scripts/lecture_lecteur_gel_loi_machine1_v1.py"),
     "depot": B(CLONE + "/journal/sonde_ordre2.json"), "retenus": B(CLONE + "/journal/tp_retenus_machine2_v1.json"), "tp_ref": B(CLONE + "/journal/tp_reference_machine2_v1.json"),
     "anc_ref": B(CLONE + "/journal/reference_ancres_ter_machine1_v1.json"), "table_loi": B(CLONE + "/journal/table_points_gel_loi_ordre3_v1.json"),
     "gel_p1": B(P1 + "/gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md"), "lot_p1": B(P1 + "/MANIFESTE_lot_machine1_2026-11-16_gel_vide_partie1_regle_tirage_v1.txt"),
     "bloc_adapte": B(P1 + "/chaine_adaptee_bloc_machine1_v1.py"), "tirage": B(P1 + "/tirage_vide_machine1_v1.py"), "table_m1": B(P1 + "/eligibilite_candidates_vide_v1.json"),
     "lot_m2": B(M2 + "/MANIFEST_lot_machine2_certification_gel_vide_partie1_v1.txt"), "table_m2": B(M2 + "/certif_gel_vide_partie1_machine2/table_machine2_vide_v1.json"),
     "lot_rec": B(REC + "/MANIFESTE_lot_machine1_2026-11-16_reception_certification_gel_vide_partie1_v1.txt"), "verif": B(REC + "/verifie_variantes_joues_v1.json"),
     "note_vide": B(LOT_VIDE + "/note_machine1_vide_etape_sans_run_2026-11-16_v1.md"), "lot_vide": B(LOT_VIDE + "/MANIFESTE_lot_machine1_2026-11-16_vide_etape_sans_run_v1.txt"),
     "lot_ech": B(LOT_ECH + "/MANIFESTE_lot_machine1_2026-11-16_loi_echelle_etape0_v1.txt")}
tete = os.popen("git -C %s rev-parse --short HEAD" % CLONE).read().strip()
assert (c["gel_p1"], c["lot_p1"], c["lot_m2"], c["lot_rec"], tete) == ("b57c9ccdd3946261", "879ea2e51c7d7f4f", "d4f95772710d545c", "53c604647e78afa4", "dee73bd"), c
PIECES = ["table_cellules_gel_vide_v1.json", "predictions_vide_machine1_v1.py", "predictions_vide_machine1_v1.log", "tirage_vide_graine_479579_machine1_v1.log",
          "sonde_vide_machine1_v1.py", "feuille_vide_machine1_v1.py", "pilote_gel_vide_machine1_v1.py", "banc_feuille_vide_machine1_v1.py", "banc_feuille_vide_machine1_v1.log",
          "banc_feuille_vide_machine1_v1_premier_passage_attente_fausse.log", "banc_feuille_vide_machine1_v1_retouche_b24.diff", "essai_refus_machine1_v1.py",
          "essai_refus_machine1_v1.log", "table_prevol_vide_machine1_v1.py", "table_cellules_prevol_vide_v1.json", "comparaison_prevol_vide_machine1_v1.py",
          "comparaison_prevol_vide_machine1_v1.log", "comparaison_prevol_vide_v1.json", "prevol_pilote_gel_vide.log", "prevol_verdict_ter_instrument.json",
          "prevol_sonde_vide_PV3.json", "prevol_sonde_vide_PV8.json", "prevol_verdict_vide.json"]
cp = {p: B(os.path.join(D, p)) for p in PIECES}
T = J("table_cellules_gel_vide_v1.json"); CEL = T["cellules"]; LIS = [x for x in CEL if x["ligne"] == "lisible"]; PRO = [x for x in CEL if x["ligne"] == "profonde"]
assert len(LIS) == 16 and len(PRO) == 12 and T["graine"] == "479579" and all(v == 0 for v in T["rangs"].values())
for nom, attendu in (("sonde_vide_machine1_v1.py", r'"d5cc48f48e37af99", "%s"'), ("feuille_vide_machine1_v1.py", r'"83701094e6a2b965", "%s"'), ("pilote_gel_vide_machine1_v1.py", r'"table": "%s"')):
    assert (attendu % cp["table_cellules_gel_vide_v1.json"]) in lire(nom), "le canon de la table n'est pas en dur dans %s" % nom
assert ('"%s"' % cp["sonde_vide_machine1_v1.py"]) in lire("feuille_vide_machine1_v1.py") and ('"sonde_vide": "%s"' % cp["sonde_vide_machine1_v1.py"]) in lire("pilote_gel_vide_machine1_v1.py")
assert ('"feuille_vide": "%s"' % cp["feuille_vide_machine1_v1.py"]) in lire("pilote_gel_vide_machine1_v1.py")
tir = lire("tirage_vide_graine_479579_machine1_v1.log"); assert "TIRAGE : 28 cellules (16 lisibles, 12 profondes)" in tir and "graine : 479579" in tir
banc = lire("banc_feuille_vide_machine1_v1.log"); nb = re.search(r"BANC : (\d+) cas tenus sur (\d+) : IL MORD COMME ATTENDU", banc); assert nb and nb.group(1) == nb.group(2)
banc1 = lire("banc_feuille_vide_machine1_v1_premier_passage_attente_fausse.log"); nb1 = re.search(r"BANC : (\d+) cas tenus sur (\d+) : DES CAS RATES : b24_bande_chaine", banc1); assert nb1
ref = lire("essai_refus_machine1_v1.log"); nr = re.search(r"ESSAIS DE REFUS : (\d+) tenus sur (\d+)", ref); assert nr and nr.group(1) == nr.group(2)
PV = J("comparaison_prevol_vide_v1.json"); assert PV["tient"]
journal_pv = lire("prevol_pilote_gel_vide.log"); assert ("pilote pilote_gel_vide_machine1_v1.py canon %s" % cp["pilote_gel_vide_machine1_v1.py"]) in journal_pv
assert ("canon sonde_vide        %s" % cp["sonde_vide_machine1_v1.py"]) in journal_pv and ("canon feuille_vide      %s" % cp["feuille_vide_machine1_v1.py"]) in journal_pv
VE = json.load(open(REC + "/verifie_variantes_joues_v1.json"))["etats"]
PLANCHER10 = float(re.search(r"^PLANCHER10 = ([0-9.e-]+)", open(CLONE + "/scripts/lecture_lecteur_gel_loi_machine1_v1.py", encoding="ascii").read(), re.M).group(1))
SOUS = [x for x in CEL if x["ligne"] == "lisible" and math.exp(x["ln_G3"]) < PLANCHER10]
assert all(math.exp(x["ln_G3"]) < PLANCHER10 for x in CEL if x["ligne"] == "profonde")
FM2 = [x for x in json.load(open(M2 + "/certif_gel_vide_partie1_machine2/faisabilite_profondeur_jumeau_machine2_v1.json"))["cas"] if x["m_bord_du_vide"] == 16][0]
par_lecture_m2 = sorted(v["duree_s"] / 3.0 for v in FM2["absorbeurs"].values())
delta_min_joue = min(abs(r["delta"]) for r in VE)
SUJ = {(e["source"], e["id"], e["rang"]): e for e in json.load(open(LOT_ECH + "/superposition_v1.json"))["etats"] if e["domaine"]}
assert B(LOT_ECH + "/superposition_v1.json") == T["canons"]["superposition"]
n_trop_petite = sum(1 for r in VE if -r["q_mediane"] / SUJ[(r["source"], r["id"], r["rang"])]["r"] > 0)
TOLL, TOLP = T["regle"]["tolerance"]["lisible"], T["regle"]["tolerance"]["profonde"]
e1 = lambda x: "%.1e" % x
G = lambda x: math.exp(x["ln_G3"])

L = []
def T_(s=""): L.append(s)
def P(s, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))

T_('GEL "LARGEUR DU VIDE" -- SECONDE PARTIE : L\'INSTRUMENT, LES ENONCES, LES TOLERANCES')
T_("PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-16.")
T_("A CERTIFIER PAR MACHINE 2 AVANT TOUTE LECTURE 2D DU FANTOME A L'UNE DES CELLULES.")
T_()
T_("0. STATUT")
P("""Cette piece complete la premiere partie (%s, lot %s), que machine 2 a certifiee telle quelle, sans morsure (lot %s). Elle fixe les
cellules tirees, l'instrument du run, les enonces juges, leurs tolerances, ce que chaque issue engage, et les annonces de la plume. Rien
n'est joue : l'etat que porte le site (0, 0) du systeme a fantome n'a ete lu en 2D a aucune cellule, par machine 1.""" % (c["gel_p1"], c["lot_p1"], c["lot_m2"]))
P("""Ouverture. L'operateur a ecrit "on gele et on avance !" (16/11/2026, 12 h 19) : declaration de machine 1, que machine 2 dit ne pas
pouvoir attester (lot %s).""" % c["lot_m2"])
P("""Graine. L'operateur a ecrit a machine 1 "la graine 479579" (16/11/2026, 13 h 34), apres avoir porte la certification de machine 2 et
apres que machine 1 a authentifie cette certification et ecrit la table commune (lot %s, remis a l'operateur avant la graine ; machine 1
ne sait pas s'il a ete porte a machine 2). Machine 1 n'avait calcule aucun tirage sur une graine faite de chiffres avant de la recevoir.
Elle avait rappele a l'operateur que la graine lui revenait ; elle n'en a propose ni commente aucune.""" % c["lot_rec"])
P("""Tirage. Par le script de machine 1 (%s), sur les deux tables d'eligibilite (%s et %s) : les quatre creneaux sortent au rang 0, 28
cellules. Machine 2 dit son tirage a la certification ; si ses cellules ou leurs couplages ecrits different, PAS DE GEL (premiere partie,
section 6).""" % (c["tirage"], c["table_m1"], c["table_m2"]))
P("""E19. Aucune des deux machines ne lit en 2D le systeme a fantome a l'une des cellules, ni l'etat (0, 0) du systeme a fantome a
aucun w2, avant la certification croisee de cette piece et le feu vert ecrit de l'operateur. Tout ce que cette piece calcule aux
cellules est une chaine a une dimension. Les calculs 2D qu'elle rapporte (pre-vol, section 4.5) sont l'instrument du lecteur a ses
points deja joues, et le JUMEAU SANS FANTOME a w2 = 101/50, qui n'est pas un candidat.""")
T_()
T_("1. QUESTION ET PERIMETRE")
P("""La largeur de l'etat que porte le site (0, 0), "le vide", n'a jamais ete lue en 2D. La note sur le vide (%s) dit qu'une chaine a
une dimension la predit, sous un absorbeur de chaine adapte au saut. Ce gel demande si c'est vrai, a des cellules que personne n'a
choisies.""" % c["note_vide"])
P("""Perimetre : quatre w2 (delta = %s), sept profondeurs de barriere. L'objet juge est la chaine d'ordre 3 des blocs deposes sous
l'absorbeur adapte (bloc %s), telle quelle : son plateau G3* sur dix-huit variantes. La reference est la largeur de plateau sous
l'absorbeur A, lue par le lecteur creux du delta 99.""" % (", ".join("%+.3f" % x for x in sorted(set(x["delta"] for x in CEL))), c["bloc_adapte"]))
P("""Ce que le gel SEPARE et ne separe pas. Aux seize cellules lisibles, l'ordre 3 differe de l'ordre 2 de %.4f au plus, du premier
ordre de %.4f au plus, et de la loi d'echelle |delta| Phi*(kappa) de %.4f au plus : sous une tolerance de %s, V1 n'oppose donc pas les
ordres entre eux. Il eprouve ceci : "le mecanisme de l'echelle et la chaine rendent la largeur du vide a %s pres". Les corrections a la
loi d'echelle ne sont eprouvees que sur la ligne profonde du creneau MG, si elle est lue : a MG12 et MG16 l'ordre 3 est a %.3f et %.3f
du premier ordre.""" % (max(abs(x["ln_G3"] - x["ln_G2"]) for x in LIS), max(abs(x["ln_G3"] - x["ln_G1"]) for x in LIS), max(abs(x["r3"]) for x in LIS), TOLL, TOLL,
                        [x["ln_G3"] - x["ln_G1"] for x in CEL if x["id"] == "MG12"][0], [x["ln_G3"] - x["ln_G1"] for x in CEL if x["id"] == "MG16"][0]))
T_()
T_("2. SOURCES (convention B)")
for canon, quoi in ((c["moteur"], "scripts/m17_chaine_v17.py (registre %s), le moteur" % tete),
                    (c["bloc2"], "scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2"),
                    (c["bloc3"], "scripts/ordre3_bloc_machine1_v1.py (registre), le bloc d'ordre 3"),
                    (c["sonde_lecteur"], "scripts/sonde_lecteur_gel_loi_machine1_v1.py (registre) : la sonde du lecteur, jouee telle quelle a l'etage A, et dont le bloc LECTEUR CREUX est execute par la sonde de ce gel"),
                    (c["feuille_lecteur"], "scripts/lecture_lecteur_gel_loi_machine1_v1.py (registre) : la feuille du lecteur, jouee telle quelle a l'etage A, et dont juger_etat est appele par la feuille de ce gel"),
                    (c["depot"], "journal/sonde_ordre2.json (registre), le depot du delta 98 : les ancres"),
                    (c["retenus"], "journal/tp_retenus_machine2_v1.json (registre) : couplages du temoin positif"),
                    (c["tp_ref"], "journal/tp_reference_machine2_v1.json (registre) : reference du temoin positif"),
                    (c["anc_ref"], "journal/reference_ancres_ter_machine1_v1.json (registre) : reference des ancres"),
                    (c["table_loi"], "journal/table_points_gel_loi_ordre3_v1.json (registre) : la table que la sonde deposee exige a l'etage A"),
                    (c["gel_p1"], "gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md (lot %s)" % c["lot_p1"]),
                    (c["bloc_adapte"], "chaine_adaptee_bloc_machine1_v1.py (meme lot) : le predicteur"),
                    (c["tirage"], "tirage_vide_machine1_v1.py (meme lot)"),
                    (c["lot_m2"], "lot de machine 2 : certification de la premiere partie, sa table (%s), ses cinq demandes R-1 a R-5" % c["table_m2"]),
                    (c["lot_rec"], "lot de machine 1 : reception, table commune, les dix-huit variantes aux etats joues (%s)" % c["verif"]),
                    (c["note_vide"], "note sur le vide (lot %s) ; la loi d'echelle : lot %s" % (c["lot_vide"], c["lot_ech"]))):
    P(canon + " " + quoi, 4, 22)
P("""Les lots de machine 1 et de machine 2 de ce jour ne sont pas au registre (%s) : les deux machines les detiennent.""" % tete)
T_()
T_("3. LES CELLULES")
P("""Table gelee : table_cellules_gel_vide_v1.json, canon %s. Elle porte la graine, les rangs, les 28 cellules, leurs predictions et leur
tolerance. La sonde, la feuille et le pilote portent son canon en dur. Par cellule : w2, delta, profondeur m, couplage ecrit, r_c, plus
grande boite du lecteur (r_c + 100), plateau predit G3* et etendue de la chaine sous ses dix-huit variantes, tolerance T.""" % cp["table_cellules_gel_vide_v1.json"])
T_("    cellule  w2          delta    m   g            r_c  boite  G3*       etendue  T")
for x in CEL:
    T_("    %-7s  %-10s  %+.3f   %-2d  %s  %-3d  %-5d  %s  %.4f   %.2f" % (
        x["id"], x["w2"], x["delta"], x["m"], x["g"], x["r_c"], x["N_max"], "%.2e" % G(x), x["etendue"], x["tolerance"]))
P("""Aux 28 cellules la barriere du moteur finit au site m, et G3* et l'etendue sont ceux de la table de la premiere partie, que machine
2 a retrouvee par sa methode (ecart de 1.3e-08 sur le logarithme du plateau, lot %s).""" % c["lot_m2"])
T_()
T_("4. L'INSTRUMENT : UN RUN, TROIS ETAGES")
T_("  4.1 Les pieces (convention B)")
for nom, quoi in (("table_cellules_gel_vide_v1.json", "la table gelee ; ecrite par predictions_vide_machine1_v1.py (%s)" % cp["predictions_vide_machine1_v1.py"]),
                  ("sonde_vide_machine1_v1.py", "NOUVELLE ; elle execute le bloc LECTEUR CREUX de la sonde deposee, lu dans son fichier"),
                  ("feuille_vide_machine1_v1.py", "NOUVELLE ; elle appelle juger_etat de la feuille deposee et juge les enonces"),
                  ("pilote_gel_vide_machine1_v1.py", "NOUVEAU ; il enchaine et tient le journal"),
                  ("table_cellules_prevol_vide_v1.json", "deux cellules a w2 = 101/50, non candidat : le pre-vol")):
    P("%s %s : %s" % (cp[nom], nom, quoi), 4, 22)
P("""Aucune piece deposee n'est editee ni derivee : la sonde et la feuille du lecteur sont jouees telles quelles a l'etage A, et leurs
routines sont executees depuis leurs fichiers, au canon controle, aux etages B et C.""")
T_("  4.2 Le deroulement du run (le pilote)")
P("""Etage A. L'instrument du lecteur, tel qu'au gel "ordre 3" : la sonde deposee en modes etage0, ancres et etage1 (les deux ancres du
depot, le temoin positif, le temoin negatif des ancres), puis la feuille deposee, etape "instrument". Si elle ne rend pas TIENT, le run
s'arrete : aucune cellule n'est lue.""", 4)
P("""Etage B. La sonde de ce gel, un appel par cellule : le jumeau sans fantome (signe +1) puis le fantome (signe -1), au site (0, 0),
depuis l'energie 0, sous les quatre absorbeurs du depot (A : F2, 80 couches ; B : F2, 100 ; C : F1, 100 ; D : F2, bord r_c + 10, 80), a
douze barreaux (k = -3 a 8, eta_k = eta0 2^(-k)), avec r_c = 2 (m + max(8, m)) + 2 et eta0 = |w2 - 2|. Aucun etage dense.""", 4)
P("""Etage C. La feuille de ce gel : section 5.""", 4)
T_("  4.3 Le banc de la feuille")
P("""Le banc fabrique des dossiers de run SYNTHETIQUES pour la table gelee (des plateaux poses a la main autour de la prediction : ils ne
disent rien des cellules), change une chose a la fois, avec l'effet attendu ecrit avant : %s cas, %s tenus. Ils couvrent : une cellule
qui tombe, deux, le signe, la cellule non jugeable, trop de non jugeables, un creneau sans deux cellules tenues, le desaccord d'un
absorbeur, l'absence de plateau, les lectures non suivies, le temoin trop large, le temoin non suivi, l'instrument, le fichier absent, le
canon de la sonde, le couplage, le fichier de pre-vol, la geometrie, la ligne profonde (qui tombe, non lue, peu lue), la tolerance par
ligne, les trois termes de la bande, une autre table.""" % (nb.group(2), nb.group(1)), 4)
P("""Defaut de ma plume, garde a cote : au premier passage %s cas sur %s tenaient. Le cas rate (b24) portait une attente fausse de ma
main (0.0105 pour un seuil de 0.0110) ; la feuille avait raison. L'attente est corrigee, le diff et le premier journal sont joints ; la
feuille n'a pas ete retouchee.""" % (nb1.group(1), nb1.group(2)), 4)
T_("  4.4 Les refus, sans aucune mesure")
P("""Le chemin sans --prevol sur la table du gel ne peut pas etre joue avant le feu vert : il lirait le fantome. Seuls ses refus le
sont (essai_refus_machine1_v1.py) : %s essais, %s tenus, aucun fichier ecrit. La sonde refuse la table du gel avec --prevol, toute autre
table sans --prevol, une cellule inconnue, un w2 candidat en pre-vol, un moteur qui n'est pas au canon ; la feuille et le pilote
refusent de meme. La lecture du fantome ne differe de celle du jumeau que par l'argument signe du bloc depose : elle n'a jamais ete
executee par la sonde de ce gel.""" % (nr.group(2), nr.group(1)), 4)
T_("  4.5 Le pre-vol de machine 1")
p3 = PV["P3"]
P("""Le pilote, avec --prevol, sur la table de pre-vol (deux cellules a w2 = 101/50, m = 3 et 8) : l'etage A entier, puis le jumeau
seul aux deux cellules, puis la feuille. Quatre controles (comparaison_prevol_vide_machine1_v1.py), tous tenus :""", 4)
P("""P1 l'instrument du lecteur, joue par le pilote avec les pieces deposees : %s.""" % PV["P1"]["instrument"], 6, 9)
P("""P2 a m = 8, le jumeau lu par la sonde de ce gel rend les largeurs de la piece de faisabilite de la premiere partie (meme w2, meme
couplage, meme geometrie) : %d lectures comparees, pire ecart relatif %s.""" % (PV["P2"]["lectures"], e1(PV["P2"]["pire_ecart_relatif"])), 6, 9)
P("""P3 lectures du jumeau suivies : %d sur %d a m = 3 (largeurs de %s a %s), %d sur %d a m = 8 (de %s a %s) ; le fantome n'est lu a
aucune ; les fichiers sont marques pre-vol.""" % (p3["PV3"]["suivies"], p3["PV3"]["lectures"], e1(p3["PV3"]["plus_petite_largeur"]), e1(p3["PV3"]["plus_grande_largeur"]),
                                                 p3["PV8"]["suivies"], p3["PV8"]["lectures"], e1(p3["PV8"]["plus_petite_largeur"]), e1(p3["PV8"]["plus_grande_largeur"])), 6, 9)
P("""P4 la feuille, en pre-vol : "%s", aucune issue rendue.""" % PV["P4"]["verdict"], 6, 9)
P("""Durees sur le conteneur de machine 1 (deux processus, un fil chacun) : %s ; total %.0f s. Ce que le pre-vol ne dit pas : rien du
fantome, et rien de BOCAL4.""" % (" ; ".join("%s %.0f s" % kv for kv in PV["P5"]["durees_s"].items()), PV["P5"]["total_s"]), 4)
T_()
T_("5. CELLULE LUE, BANDE, JUGEMENT (ce que fait la feuille)")
P("""LECTEUR. La feuille appelle juger_etat de la feuille deposee sur les quatre trajectoires du fantome : un plateau sous chacun des
quatre absorbeurs (cinq barreaux consecutifs, plus grande valeur <= 1.05 fois la plus petite), et les plateaux sous B, C et D a 0.05 pres
du plateau sous A, en logarithme. Statut : QUALIFIE, NON QUALIFIE ou NON LISIBLE, comme au gel ter. Gamma_pl est le plateau sous A.""")
P("""ETALEMENT DU LECTEUR, s : le plus grand de ln(1 + etalement du plateau sous A) et des trois |ln(plateau X / plateau A)|, X = B, C,
D. Ce sont des nombres que la feuille deposee calcule deja.""")
P("""TEMOIN. Le jumeau sans fantome a la meme cellule (demande R-4 de machine 2). Il TIENT si ses 48 lectures sont suivies et si sa
plus grande largeur vaut au plus 1e-6 Gamma_pl.""")
P("""CELLULE LUE : QUALIFIE et temoin tenu. Sinon NON LUE, avec son motif.""")
P("""JUGEMENT d'une cellule lue. ln q = ln(G3* / Gamma_pl). BANDE b = etendue de la chaine a la cellule (table) + s. La cellule TIENT si
|ln q| <= T - b ; elle TOMBE si |ln q| > T + b ; elle est NON JUGEABLE sinon (demande R-2 de machine 2, a laquelle la plume ajoute s).
Une cellule dont la bande atteint la tolerance ne peut donc pas tenir : elle tombe ou n'est pas jugeable.""")
T_()
T_("6. LES ENONCES ET LEURS ISSUES (la cellule est l'unite)")
P("""V1, ligne lisible, seize cellules, T = %s. TOMBE si deux cellules ou plus tombent ; sinon NON CONCLUANT si moins de douze cellules
sont jugees (tenues ou tombees), ou si un creneau a moins de deux cellules tenues ; sinon TENU SAUF UNE CELLULE si une tombe ; sinon
TENU.""" % TOLL)
P("""VP, ligne profonde, douze cellules, T = %s. Hors de V1 : quelle que soit son issue, celle de V1 ne change pas. TOMBE si deux
cellules ou plus tombent ; sinon NON LUE si aucune n'est jugee ; sinon NON CONCLUANT si moins de six sont jugees ; sinon TENU SAUF UNE
CELLULE ou TENU.""" % TOLP)
P("""Ce qui est consigne sans etre juge, par cellule lue : le signe de ln q et celui de delta ; ln q pour l'ordre 2, pour le premier
ordre, pour la loi d'echelle |delta| Phi*(kappa) et pour la forme fermee a trois termes ; ln(Gamma_pl / |delta|), pour lire la
superposition des creneaux a profondeur egale. Aucun enonce ne porte sur le signe du residu (demande R-5).""")
P("""La note sur le vide proposait un enonce V2 sur la forme fermee. Il n'est PAS pose : aux cellules lisibles la forme fermee est a
%.3f a %.3f du plateau predit, hors de toute tolerance utile ; elle est consignee (section 14, E-3).""" % (
    min(abs(x["ln_forme_fermee"] - x["ln_G3"]) for x in LIS), max(abs(x["ln_forme_fermee"] - x["ln_G3"]) for x in LIS)))
T_()
T_("7. LES TOLERANCES, ET CE QUE LA PLUME A VU AVANT DE LES ECRIRE")
P("""Aucune largeur 2D du vide n'existe. Les tolerances viennent de trois sources, toutes regardees avant d'ecrire.""")
T_("  7.1 Ce que la chaine peut")
P("""L'etendue de la chaine sous ses dix-huit variantes vaut de %.4f a %.4f aux cellules lisibles et %.4f au plus aux profondes. Ce
n'est pas l'erreur de la chaine : c'est ce que son absorbeur laisse indetermine.""" % (min(x["etendue"] for x in LIS), max(x["etendue"] for x in LIS), max(x["etendue"] for x in PRO)), 4)
T_("  7.2 Ce que la chaine a manque aux etats deja joues (apres coup ; lot %s)" % c["lot_rec"])
neg = [r for r in VE if r["delta"] < 0]; pos = [r for r in VE if r["delta"] > 0]
P("""Aux %d etats du domaine des deltas 98 et 100, sous l'absorbeur adapte, le residu ln(G3* / Gamma_pl) a le signe de delta partout
(constat de machine 2, retrouve par machine 1) ; a %d de ces etats la chaine rend une correction a la loi d'echelle trop petite. La part
manquee, (r - r de la chaine) / r, vaut %.3f en mediane, et de %.3f a %.3f selon la cellule (mediane par cellule).""" % (
    T["joues"]["etats"], n_trop_petite, T["joues"]["part_manquee_mediane"], T["joues"]["part_manquee_par_cellule_min"], T["joues"]["part_manquee_par_cellule_max"]), 4)
P("""DEUX LECTURES de ce constat, qui coincident aux etats joues et PAS au vide. (a) "Le residu a le signe de delta." (b) "La chaine
manque une part f de sa correction" : le residu vaut alors - f / (1 - f) r3, r3 etant ce que la chaine ajoute a la loi d'echelle. Aux
etats joues r a le signe oppose a delta et les deux lectures donnent le meme signe. Au vide, r3 est NEGATIF aux quatre cellules lisibles
de MG (delta < 0) : la lecture (a) y annonce un residu negatif, la lecture (b) un residu positif. La plume ne sait pas laquelle vaut pour
le vide ; le gel peut les departager a MG, si la bande le permet.""", 4)
T_("  7.3 Les chaines aux cellules, et ce qui tiendrait")
P("""Par cellule : ln(G3* / G2*) ; ln(G3* / G1*) ; r3 ; ecart de la forme fermee a G3* ; residu attendu sous la lecture (b), pour la
part manquee mediane puis pour la plus grande ; et T - etendue, le plus grand |ln q| qui tiendrait si le lecteur etait sans etalement.""", 4)
T_("    cellule  ln(G3*/G2*)  ln(G3*/G1*)  r3       ferme - G3*  residu (b) : median, pire   T - etendue")
for x in CEL:
    T_("    %-7s  %+.4f      %+.4f      %+.4f  %+.4f      %+.4f, %+.4f            %.4f" % (
        x["id"], x["ln_G3"] - x["ln_G2"], x["ln_G3"] - x["ln_G1"], x["r3"], x["ln_forme_fermee"] - x["ln_G3"], x["attente"]["sous_correction_mediane"],
        x["attente"]["sous_correction_pire"], x["tolerance"] - x["etendue"]))
P("""Lecture. Aux cellules lisibles le residu attendu sous (b) vaut %.4f au plus pour la part mediane et %.4f au plus pour la plus
grande (a MG6) ; machine 2 extrapolait "de l'ordre de 0.005, au plus 0.01". T - etendue y vaut de %.4f a %.4f : une cellule ne tient
que si le residu ET l'etalement du lecteur logent ensemble sous ce nombre. L'etalement du lecteur au vide n'est pas connu ; au
mandataire a une dimension de la note sur le vide (sa section 2.3) l'absorbeur du lecteur restait a moins d'un centieme de la chaine. Dans
l'hypothese d'un etalement de 0.01, les cellules du creneau PG ne tiendraient que sous %.4f a %.4f.""" % (
    max(abs(x["attente"]["sous_correction_mediane"]) for x in LIS), max(abs(x["attente"]["sous_correction_pire"]) for x in LIS),
    min(x["tolerance"] - x["etendue"] for x in LIS), max(x["tolerance"] - x["etendue"] for x in LIS),
    min(x["tolerance"] - x["etendue"] - 0.01 for x in LIS if x["creneau"] == "PG"), max(x["tolerance"] - x["etendue"] - 0.01 for x in LIS if x["creneau"] == "PG")), 4)
T_("  7.4 Les deux tolerances")
P("""T = %s sur la ligne lisible : c'est la demande R-1 de machine 2 ("au plus 0.02"), que la plume prend telle quelle. Elle vaut de %.1f
a %.1f fois l'etendue de la chaine et %.1f fois le plus grand residu attendu sous (b) ; la tolerance de E1 (0.05) en aurait valu %.1f
fois. T = %s sur la ligne profonde : la valeur de E1 pour e_bord < 0.3 ; les douze cellules profondes ont e_bord de %.3f a %.3f, et le
residu attendu sous (b) y monte a %.4f pour la plus grande part manquee.""" % (
    TOLL, TOLL / max(x["etendue"] for x in LIS), TOLL / min(x["etendue"] for x in LIS), TOLL / max(abs(x["attente"]["sous_correction_pire"]) for x in LIS),
    0.05 / max(abs(x["attente"]["sous_correction_pire"]) for x in LIS), TOLP, min(x["e_bord"] for x in PRO), max(x["e_bord"] for x in PRO),
    max(abs(x["attente"]["sous_correction_pire"]) for x in PRO)), 4)
P("""Ces deux valeurs, le facteur 1e-6 du temoin et les comptes des issues (douze, deux, six) ont ete ecrits dans la feuille AVANT le
banc et n'ont pas ete retouches ensuite. Declaration de la plume : machine 2 ne peut pas la verifier. Aucun ne sera regle apres
lecture.""", 4)
T_()
T_("8. CE QUE CHAQUE ISSUE ENGAGE")
for t in ("""L'INSTRUMENT NE TIENT PAS (etage A) : aucune cellule n'est lue, rien n'est juge ; l'acte le dit ; une suite demande un autre gel.""",
          """V1 TENU. L'acte peut ecrire : "a seize cellules tirees au sort, de 3 a 6 barreaux et pour |delta| de %.3f a %.3f, la chaine
d'ordre 3 sous absorbeur adapte rend la largeur de l'etat porte par (0, 0) a %s pres en logarithme, au-dela de sa propre etendue et de
l'etalement du lecteur". Il NE peut PAS ecrire que la chaine est exacte : son defaut connu (7.2) est seulement plus petit que la
tolerance (demande R-5). Il ne peut pas ecrire que l'ordre 3 fait mieux que le premier ordre : V1 ne les separe pas (section 1). Il ne
peut rien ecrire de la duree de vie du systeme ferme : la largeur est celle d'un etat sous absorbeur, stable sous les variations jouees,
et rien d'autre. Le bloc de l'absorbeur adapte peut alors etre propose au depot.""" % (min(abs(x["delta"]) for x in LIS), max(abs(x["delta"]) for x in LIS), TOLL),
          """V1 TENU SAUF UNE CELLULE. La meme phrase, la cellule nommee, avec son ln q, sa bande et son creneau.""",
          """V1 TOMBE. L'acte ecrit que la chaine ne rend pas la largeur du vide a cette tolerance, cellules nommees. La prediction de la note
sur le vide est alors declaree non confirmee. Aucune autre chaine, aucun autre absorbeur de chaine, aucune autre tolerance n'est essayee
sur ces cellules ; la loi d'echelle ne peut pas etre enoncee pour le vide.""",
          """V1 NON CONCLUANT. L'acte donne les comptes et dit lequel des deux a manque : le lecteur (cellules non lues) ou la resolution
(cellules non jugeables : la bande atteint la tolerance). Ce n'est pas une refutation, et ce n'est pas une confirmation. Pas de rejeu, pas
de nouveau seuil.""",
          """VP, quelle que soit son issue, ne change pas celle de V1. TENU : la chaine tient aussi a 8 barreaux et plus, la ou le lecteur
qualifie ; l'acte dit jusqu'a quelle profondeur des cellules ont ete jugees. TOMBE : la chaine ou le lecteur echoue en profondeur, et
l'acte ne dit pas lequel : sous %s la qualification en cours de run est la SEULE garde (demande R-3), aucune seconde mesure 2D
independante n'existe. NON LUE ou NON CONCLUANT : le lecteur ne lit pas la ligne profonde ; rien n'est dit de la chaine.""" % ("%.2e" % PLANCHER10),
          """Dans tous les cas : la table par cellule est publiee (statut du lecteur, plateaux et ecarts des quatre absorbeurs, temoin,
Gamma_pl, s, bande, ln q, jugement, et les grandeurs consignees), les cellules non lues avec leur motif."""):
    P(t, 2, 4)
T_()
T_("9. GARDES (chaque journal dit ce qu'il ne joue pas)")
for t in ("""G-1 canons en dur : moteur, sonde et feuille deposees du lecteur, depot, couplages et references du temoin et des ancres, table
deposee du gel "ordre 3", table gelee, sonde, feuille ; un ecart arrete.""",
          """G-2 la sonde lit le bloc du lecteur dans le fichier depose, au canon controle ; elle ne le recopie pas.""",
          """G-3 forme de chaque fichier de cellule, controlee par la feuille avant tout jugement : canons, mode, cellule egale a celle de la
table (w2, m, couplage ecrit, r_c, eta0), absorbeurs et boites, quatre trajectoires de douze barreaux pour le jumeau et pour le fantome,
signe, site, energie de depart. Un fichier manquant ou non conforme : RUN INCOMPLET, rien n'est juge.""",
          """G-4 instrument du lecteur : etage 0, ancres, etage 1, par les pieces deposees, tolerances inchangees.""",
          """G-5 temoin : le jumeau a la geometrie de chaque cellule (section 5).""",
          """G-6 pre-vol : avec --prevol la table du gel est refusee, un w2 candidat est refuse et le fantome n'est pas lu ; sans --prevol
toute autre table est refusee.""",
          """G-7 une seule execution : le pilote exige un dossier neuf et joue chaque appel une fois ; un code de sortie non nul l'arrete.""",
          """G-8 ce que l'accord des quatre absorbeurs eprouve : l'independance de la largeur a la boite (80 ou 100 couches, bord deplace de
dix) et a la forme de l'absorbeur (F1 ou F2). Il n'eprouve PAS l'exactitude de la largeur : une erreur commune aux quatre lui echappe.
Sous %s (dix planchers de la decomposition dense : aucun etat n'a ete lu en dessous), c'est pourtant la seule garde (demande R-3) ; cela
vaut pour %d cellules de la ligne lisible, dont le plateau predit est sous ce seuil (%s ; G3* de %s a %s), et pour toute la ligne
profonde.""" % ("%.2e" % PLANCHER10, len(SOUS), ", ".join(x["id"] for x in SOUS), e1(min(G(x) for x in SOUS)), e1(max(G(x) for x in SOUS)))):
    P(t, 2, 6)
T_()
T_("10. ANNONCES DE LA PLUME (ecrites apres les calculs de la section 7 ; aucune 2D du fantome)")
P("""Ce sont des jugements, pas des calculs. Probabilites :""")
for t in ("""A-1 (0.95) l'instrument du lecteur tient (etage A).""",
          """A-2 (0.95) le temoin tient aux 28 cellules.""",
          """A-3 (0.60) le lecteur qualifie les seize cellules lisibles ; (0.80) au moins douze.""",
          """A-4 V1 : TENU 0.50 ; TENU SAUF UNE CELLULE 0.05 ; TOMBE 0.08 ; NON CONCLUANT 0.32 ; le reste (0.05) est l'instrument.""",
          """A-5 VP : TENU 0.35 ; TENU SAUF UNE CELLULE 0.05 ; TOMBE 0.10 ; NON LUE ou NON CONCLUANT 0.45 ; le reste (0.05) est l'instrument.""",
          """A-6 (0.55) aux cellules lisibles lues, le plus grand |ln q| est sous 0.01.""",
          """A-7 le signe du residu a MG, aux cellules lisibles lues, d'apres le constat de machine 2 (section 7.2) : negatif, comme delta, a
trois cellules au moins : 0.40 ; positif, comme la lecture (b), a trois au moins : 0.40. La plume ne tranche pas."""):
    P(t, 2, 6)
P("""La plume annonce donc que V1 a une chance sur deux de tenir, et que l'issue qu'elle craint le plus n'est pas la chute mais le NON
CONCLUANT : une tolerance de %s contre une bande que le lecteur peut elargir. Elle le gele ainsi.""" % TOLL)
T_()
T_("11. DEROULEMENT, E19, ET CE QUI EST PERMIS")
P("""ORDRE. (1) Machine 2 dit son tirage et certifie cette piece, la table, la sonde, la feuille et son banc, le pilote ; un seul tour de
correction. (2) Feu vert ecrit de l'operateur. (3) Machine 2 joue le pilote UNE fois, dans un dossier neuf. (4) Lot de resultat : les
fichiers de l'etage A, les 28 fichiers de cellule, le verdict, les journaux, le journal du pilote. (5) Machine 1 authentifie et rejoue la
feuille. (6) Acte.""")
P("""PRE-VOL. Avant le feu vert, machine 2 peut jouer le pilote avec --prevol sur la table de pre-vol : l'etage A est a des points deja
joues, et le jumeau a un w2 non candidat. Son pilote peut deriver du mien s'il le faut ; --drapeau -P et un fil BLAS par appel y sont
deja.""")
P("""UNE SEULE EXECUTION. Un pilote arrete par une panne se relance ENTIER dans un dossier neuf, et l'acte le dit ; aucun appel n'est
rejoue apres lecture de sa sortie.""")
P("""DEUX MACHINES. Le verdict est celui de la feuille jouee par machine 2 dans le run. Machine 1 la rejoue sur les fichiers du lot : la
feuille ne calcule aucune chaine, les predictions sont dans la table ; les deux verdicts doivent etre les memes. S'ils different, l'acte
donne les deux et retient la lecture la MOINS favorable a l'enonce.""")
P("""E19. Aucune des deux machines ne lit le fantome a une cellule avant le feu vert ; machine 1 n'y lit rien en 2D avant d'avoir recu et
authentifie le lot de resultat. Ce gel ne se rejoue pas sous d'autres seuils, d'autres gardes, une autre chaine ou d'autres cellules
apres lecture.""")
T_()
T_("12. COUTS (a mesurer au pre-vol de machine 2, pas a promettre)")
P("""Etage A : %.0f s de calcul en trois appels sur le conteneur de machine 1 ; le run du gel "ordre 3" l'a joue sur BOCAL4. Etage B : par cellule, 48 lectures du
jumeau et 48 du fantome ; a m = 16, machine 2 a mesure sur BOCAL4 de %.1f s a %.1f s par lecture du jumeau (lot %s) ; sur machine 1, 48
lectures du jumeau ont pris %.0f s a m = 3 et %.0f s a m = 8. Etage C : quelques secondes.""" % (
    sum(v for k, v in PV["P5"]["durees_s"].items() if k.startswith("lecteur") or k.startswith("feuille du lecteur")), par_lecture_m2[0], par_lecture_m2[-1], c["lot_m2"],
                         p3["PV3"]["duree_s"], p3["PV8"]["duree_s"]))
T_()
T_("13. LIMITES DECLAREES")
for t in ("""L-1 L'objet juge est UNE chaine : les blocs deposes, forme symetrique, sous UN absorbeur de chaine, celui du bloc %s. Aucune
autre definition n'est essayee.""" % c["bloc_adapte"],
          """L-2 V1 ne separe pas l'ordre 3 des ordres inferieurs ni de la loi d'echelle (section 1).""",
          """L-3 La reference est une largeur sous absorbeur, qualifiee par sa stabilite sous quatre absorbeurs (G-8). Sous %s aucune
seconde mesure 2D n'existe. Le jumeau prouve un plancher, pas une exactitude.""" % ("%.2e" % PLANCHER10),
          """L-4 Aux etats juges des deltas 98 et 100 le lecteur n'a jamais lu le systeme a fantome a |delta| < %.3f, ni un etat de largeur
inferieure a %s : ce gel l'y envoie, en desaccord a toutes les cellules, en largeur a celles que nomme G-8. Qu'il y lise juste n'est appuye que
par des faits indirects (note sur le vide, section 2 ; faisabilite au jumeau par machine 2, a w2 = 3999/2000 et 4001/2000).""" % (delta_min_joue, "%.2e" % PLANCHER10),
          """L-5 Seules des cellules QUALIFIEES sont jugees. Une cellule que le lecteur ne qualifie pas peut etre une cellule ou la chaine
echoue : les comptes de V1 (douze, deux par creneau) bornent cet effet sans l'annuler.""",
          """L-6 La tolerance ne sort pas d'une theorie de l'erreur : elle vient de l'etendue de la chaine et d'une extrapolation depuis des
etats excites a |delta| >= 0.03, dont le sens meme est ambigu au vide (7.2).""",
          """L-7 Quatre w2, un seul par creneau : rien n'est dit de la dependance en delta a l'interieur d'un creneau.""",
          """L-8 Le creneau PP est sorti a w2 = 2.005, un des quatre w2 candidats que les notes de ce jour avaient deja calcules en chaine
seule (premiere partie, 4.8 et 9) ; et le creneau PG a w2 = 2.017, celui de la graine de demonstration. Aucune 2D n'y existe.""",
          """L-9 Un seul modele (x^5, W1 = 1, canal 2:1), un seul etat. Rien n'est dit de la dynamique du systeme ferme."""):
    P(t, 2, 6)
T_()
T_("14. ECARTS DECLARES, ET REPONSES AUX DEMANDES DE MACHINE 2")
for t in ("""E-1 La premiere partie annoncait (section 11) "la sonde du lecteur derivee du depot" et "sa feuille". Il n'y a pas de
derivation : la sonde et la feuille de ce gel sont nouvelles et executent les routines deposees depuis leurs fichiers ; l'etage A joue
les pieces deposees telles quelles.""",
          """E-2 Les ancres et le temoin positif que la premiere partie annoncait sont ceux de l'etage A, inchanges ; le temoin de chaque
cellule est le jumeau sans fantome, lu par la sonde de ce gel.""",
          """E-3 L'enonce V2 de la note sur le vide (forme fermee) n'est pas pose (section 6).""",
          """E-4 R-1 : T = %s, prise telle quelle. R-2 : la regle NON JUGEABLE est posee, et la bande porte en plus l'etalement du lecteur,
ajout de la plume. R-3 : G-8 et section 8. R-4 : le jumeau a chaque cellule, dans le run. R-5 : aucun enonce sur le signe ; il est
consigne, dit en section 8, et l'annonce A-7 en parle sans trancher. Machine 2 peut refuser A-7.""" % TOLL,
          """E-5 Le lot de reception de machine 1 (%s) disait que l'annonce donnerait "le signe attendu du residu et sa taille". Les chaines
aux cellules montrent que le signe attendu depend de la lecture (7.2) : l'annonce donne les deux.""" % c["lot_rec"],
          """E-6 Un cas du banc portait une attente fausse au premier passage (4.3).""",
          """E-7 Le pilote passe -B a python (aucun fichier de cache ecrit a cote des scripts deposes) : un premier pre-vol, lance sans ce
drapeau, a ete arrete au bout de moins d'une minute et relance ; rien n'en est garde."""):
    P(t, 2, 6)
T_()
T_("15. CE QUE MACHINE 2 CERTIFIE")
for t in ("""(a) que la table gelee porte les 28 cellules de SON tirage, avec les memes couplages ecrits ;""",
          """(b) que les predictions de la table (G3*, etendue) sont celles de sa table de la premiere partie, et que G2*, G1*, Phi* et la forme
fermee se recalculent ;""",
          """(c) que la sonde ne fait qu'executer le bloc depose a la geometrie de la section 4.2, et que la feuille applique les sections 5 et
6 ; que le banc mord ;""",
          """(d) que les nombres des sections 3 et 7 sortent des pieces ;""",
          """(e) le pre-vol sur BOCAL4 ;""",
          """(f) qu'elle accepte, ou refuse, les ecarts de la section 14, la bande (etendue + s), le facteur 1e-6 du temoin, les comptes des
issues, et l'annonce A-7."""):
    P(t, 2, 6)
T_()
T_("16. PIECES DE CE LOT (convention B)")
for p in PIECES:
    T_("    %s  %s" % (cp[p], p))
T_("    (ce script)       construction_gel_vide_partie2_machine1_v1.py")
T_()
T_("-- FIN gel_largeur_vide_partie2_instrument_enonces_pre_enregistrement_v1 --")
texte = "\n".join(L) + "\n"; texte.encode("ascii")
assert max(len(l) for l in L) <= 100, [l for l in L if len(l) > 100]
open(SORTIE, "w", encoding="ascii", newline="\n").write(texte)
canon = B(SORTIE)

Mq = []
def Am(t="", ind=0, suite=None):
    if not t:
        Mq.append(""); return
    suite = ind if suite is None else suite
    Mq.extend(textwrap.wrap(" ".join(t.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
Am('# POUR MACHINE 2 -- GEL "LARGEUR DU VIDE", SECONDE PARTIE : INSTRUMENT, ENONCES, TOLERANCES')
Am("# machine 1, v1, 2026-11-16. A CERTIFIER. Rien n'est joue. Le feu vert est a l'operateur.")
Am(); Am("## 0. EN SIX PHRASES"); Am()
Am("""L'operateur m'a donne la graine 479579 a 13 h 34 ; mon tirage : %s, rang 0 partout, 28 cellules. La piece (%s) gele ces cellules
avec leurs predictions (table %s), une sonde et une feuille nouvelles qui executent tes pieces deposees sans les deriver, et deux enonces
: V1 sur les seize cellules lisibles a T = %s, VP sur les douze profondes a T = %s, hors de V1. Tes cinq demandes y sont (section 14,
E-4). Le banc de la feuille mord a %s cas sur %s ; le pre-vol tient chez moi, au jumeau seulement. Une chose que tu n'as pas vue : au
vide, "le residu a le signe de delta" et "la chaine sous-corrige" ne disent plus la meme chose (7.2). J'annonce une chance sur deux pour
V1, et je crains le NON CONCLUANT plus que la chute.""" % (
    ", ".join("%s %s" % (s, [x["w2"] for x in CEL if x["creneau"] == s][0]) for s in ("MG", "MP", "PP", "PG")), canon, cp["table_cellules_gel_vide_v1.json"], TOLL, TOLP,
    nb.group(1), nb.group(2)))
Am(); Am("## 1. E19"); Am()
Am("""Aux cellules : des chaines 1D seulement. En 2D : l'etage A (points deja joues) et le jumeau a w2 = 101/50. La sonde de ce gel n'a
JAMAIS execute la lecture du fantome : elle ne differe de celle du jumeau que par l'argument signe du bloc depose. Tu ne la joues pas non
plus avant le feu vert.""", 2)
Am(); Am("## 2. CE QUE TU CERTIFIES (section 15 de la piece)"); Am()
Am("""(a) TON tirage rend mes 28 cellules et leurs couplages ; (b) les predictions de la table ; (c) la sonde, la feuille, le banc ; (d) les
nombres des sections 3 et 7 ; (e) le pre-vol sur BOCAL4 ; (f) ce que tu acceptes ou refuses : la bande, le facteur 1e-6, les comptes des
issues, A-7, les ecarts.""", 2)
Am(); Am("## 3. POUR REJOUER (python -I -B)"); Am()
for cmd, com in (("predictions_vide_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> chaine_adaptee_bloc_machine1_v1.py tirage_vide_machine1_v1.py 479579 <ma table> <ta table> forme_phi_v1.json superposition_v1.json verifie_variantes_joues_v1.json <sortie.json>",
                  "refait la table gelee, au canon ; une quarantaine de secondes ; chaines seules"),
                 ("banc_feuille_vide_machine1_v1.py feuille_vide_machine1_v1.py <feuille deposee du lecteur> table_cellules_gel_vide_v1.json sonde_vide_machine1_v1.py <sonde deposee du lecteur> <moteur> <dossier neuf>",
                  "le banc ; dossiers synthetiques, aucune mesure"),
                 ("essai_refus_machine1_v1.py <dossier de l'instrument> <scripts deposes> <moteur> <depot> <tp_retenus> <tp_reference> <reference des ancres> <table deposee du gel ordre 3> <table du gel> <table de pre-vol> <dossier neuf>",
                  "les refus ; aucune mesure"),
                 ("pilote_gel_vide_machine1_v1.py <dossier de l'instrument> <scripts deposes> <moteur> <depot> <tp_retenus> <tp_reference> <reference des ancres> <table deposee du gel ordre 3> table_cellules_prevol_vide_v1.json <dossier neuf> <processus> --prevol [--drapeau -P]",
                  "le pre-vol ; puis comparaison_prevol_vide_machine1_v1.py <dossier du pre-vol> <faisabilite_profondeur_jumeau_v1.json> <sortie.json>"),
                 ("pilote_gel_vide_machine1_v1.py <les memes> table_cellules_gel_vide_v1.json <dossier neuf> <processus> [--drapeau -P]",
                  "LE RUN : apres ta certification et le feu vert ecrit, une fois"),
                 ("construction_gel_vide_partie2_machine1_v1.py <dossier de ce lot> <clone du registre> <lot de la premiere partie> <ton lot extrait> <mon lot de reception> <lot de la note sur le vide> <lot de la loi d'echelle> <sortie.md>",
                  "refait la piece et ce fichier")):
    Am(cmd, 2, 6); Am("-> " + com, 6, 9)
Am(); Am("## 4. OU MORDRE"); Am()
for t in (
    """M-1 La bande b = etendue + s (section 5). Tu demandais l'etendue ; j'ajoute l'etalement du lecteur, defini par le plus grand de deux
nombres que ta feuille deposee calcule. C'est plus severe pour "tient" et plus indulgent pour "tombe". Si tu veux l'etendue seule, ou une
autre definition de s, dis-le : ce sont trois lignes de la feuille.""",
    """M-2 Le temoin : le facteur 1e-6 et l'exigence des 48 lectures suivies sont de ma plume. Au pre-vol (w2 = 101/50), la plus grande
largeur du jumeau est a plus de %d decades sous le plus petit plateau predit a la meme profondeur (m = 3 et 8) ; le facteur ne devrait
donc rien trier. S'il trie, c'est une information.""" % min(math.floor(math.log10(min(G(x) for x in CEL if x["m"] == mm) / p3["PV%d" % mm]["plus_grande_largeur"])) for mm in (3, 8)),
    """M-3 Les comptes des issues (douze cellules jugees sur seize, deux tenues par creneau, six sur douze en profondeur ; deux chutes
font tomber) sont de ma plume, poses avant le banc.""",
    """M-4 V1 ne separe pas les ordres (section 1) : a T = 0.02, le premier ordre passerait aussi aux cellules lisibles. Je le dis dans
la piece plutot que de poser un enonce d'ordre que la bande ne pourrait pas juger. Si tu en vois un jugeable, dis-le.""",
    """M-5 Les deux lectures du residu (7.2). A MG, r3 est negatif alors que delta l'est aussi : ta phrase "le residu a le signe de delta"
et ta phrase "la chaine sous-corrige" s'y contredisent. Ton extrapolation ("0.005, au plus 0.01") tient en taille sous les deux ; je n'ai
pas su choisir le signe. Verifie r3 aux quatre cellules de MG : c'est le nombre dont tout cela depend.""",
    """M-6 La sonde n'est pas derivee par remplacements : elle lit le bloc entre ses deux marqueurs dans ton exemplaire de la sonde
deposee et l'execute. Le controle porte sur le canon du fichier entier ; l'empreinte du bloc lu est consignee dans chaque sortie.""",
    """M-7 L'etage A passe a la sonde deposee la table deposee du gel "ordre 3" et, a la place de la sortie dense qu'elle ne lit pas dans
ces trois modes, le chemin du depot et le mot "sans-objet". Verifie que ta sonde deposee ne lit rien d'autre en modes etage0, ancres,
etage1.""",
    """M-8 L-8 : PP est sorti a 2.005, que nos deux machines avaient deja calcule en chaine seule (a d'autres couplages) ; PG a 2.017, le
w2 de la demonstration. Le tirage est ce qu'il est ; je le dis.""",
    """M-9 Mes probabilites (section 10) sont des jugements. A-4 dit 0.32 pour NON CONCLUANT : c'est le prix de ta tolerance et de ma
bande ensemble. Je le prefere a un test qui ne peut pas echouer."""):
    Am(t, 2, 6)
Am(); Am("## 5. RIEN D'AUTRE"); Am()
Am("Aucun delai. Le feu vert est a l'operateur, apres ta certification.")
pm2 = os.path.join(D, "POUR_MACHINE2_gel_vide_partie2_machine1_v1.md"); tm = "\n".join(Mq) + "\n"; tm.encode("ascii")
assert max(len(l) for l in Mq) <= 100, [l for l in Mq if len(l) > 100]
open(pm2, "w", encoding="ascii", newline="\n").write(tm)
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(pm2), len(Mq), B(pm2)))
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(SORTIE), len(L), canon))
