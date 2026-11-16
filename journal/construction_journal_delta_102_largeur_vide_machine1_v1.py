# -*- coding: ascii -*-
"""CONSTRUCTION DE L'ACTE DU GEL "LARGEUR DU VIDE" (projet, a contresigner) -- machine 1, v1, 2026-11-16.
Chaque nombre est lu dans une piece : le verdict rejoue, la lecture du resultat, la reception, les journaux du run, les
notes de machine 2 (par motif), les manifestes. Aucun nombre n'est tape a la main.
Usage : python3 -I -B construction_journal_delta_nn_largeur_vide_machine1_v1.py <dossier de ce lot> <lot m2 16i extrait>
        <lot m2 16h extrait> <lot m2 16g extrait> <lot m2 16f extrait> <lot gel partie 2> <lot gel partie 1>
        <lot de reception partie 1> <lot du rectificatif> <sortie.md>"""
import sys, os, re, json, glob, hashlib, unicodedata, textwrap
R16I, M2I, M2H, M2G, M2F, GEL2, GEL1, REC1, RECT, SORTIE = sys.argv[1:11]; RRES = R16I
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def lot(d):
    m = glob.glob(os.path.join(d, "MANIF*")); assert len(m) == 1, (d, m)
    return B(m[0]), sum(1 for l in open(m[0], encoding="utf-8").read().splitlines() if re.match(r"^[0-9a-f]{16} ", l))
def lire(p, enc="utf-8"):
    return open(p, encoding=enc).read()
def un(motif, texte, n=1):
    m = re.search(motif, texte, re.S); assert m, motif
    return m.group(1) if n == 1 else m.groups()

LR = json.load(open(os.path.join(R16I, "lecture_resultat_vide_v1.json"))); RR = json.load(open(os.path.join(R16I, "reception_resultat_vide_v1.json")))
V = json.load(open(os.path.join(R16I, "verdict_vide_rejoue_machine1.json")))
RUN = os.path.join(M2I, "run_gel_vide_machine2", "run_1"); V2 = json.load(open(os.path.join(RUN, "verdict_vide.json")))
auth = lire(os.path.join(R16I, "authentifie_lot_m2_resultat_run_machine1_v1.log")); assert "AUTHENTIFICATION : TIENT" in auth
canon_res, n_res = un(r"canon du lot ([0-9a-f]{16})", auth), int(un(r"au bon canon : (\d+)", auth)); assert lot(M2I) == (canon_res, n_res)
note2 = lire(os.path.join(M2I, "POUR_MACHINE1_resultat_run_gel_vide_machine2_v1.md")); noteH = lire(os.path.join(M2H, "POUR_MACHINE1_certification_gel_vide_partie2_machine2_v1.md"))
pil = lire(os.path.join(RUN, "pilote_gel_vide.log")); lanc = lire(os.path.join(M2I, "run_gel_vide_machine2", "lanceur_run_1.log"))
cmp2 = lire(os.path.join(M2I, "resultats_run_vide_machine2", "compare_feuilles_run_1_machine2_v1.log")); ana2 = lire(os.path.join(M2I, "resultats_run_vide_machine2", "analyse_run_vide_machine2_v1.log"))
aut2 = lire(os.path.join(M2I, "livraison_16i_rectificatif_gel_vide_partie2", "authentifie_rectificatif_m1_machine2_v1.log"))
C = LR["cellules"]; LIS, PRO, ENS, SG = LR["lisible"], LR["profonde"], LR["ensemble"], LR["signes"]; AN, PA, CP = RR["annonces"], RR["annonces_gelees"], RR["comparaison"]
G1 = os.path.join(GEL1, "gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md"); G2 = os.path.join(GEL2, "gel_largeur_vide_partie2_instrument_enonces_pre_enregistrement_v1.md")
TABLE = os.path.join(GEL2, "table_cellules_gel_vide_v1.json"); T = json.load(open(TABLE)); gel2 = lire(G2, "ascii")
c_g1, c_g2, c_table = B(G1), B(G2), B(TABLE); assert (c_g1, c_g2, c_table) == ("b57c9ccdd3946261", "eebd979f18d8db48", "b71206e5daf6c741")
assert V["verdict"] == V2["verdict"] == "V1 TENU ; VP TENU" and CP["issue"] == "VERDICTS IDENTIQUES" and not CP["dont_issues_jugements_statuts"]
assert V["feuille_canon"] == B(os.path.join(GEL2, "feuille_vide_machine1_v1.py")) and V["table_canon"] == c_table
# -- le run, lu dans le journal du pilote et du lanceur
debut, fin = pil.splitlines()[0][:19], [l for l in pil.splitlines() if "FIN DU PILOTE" in l][0][:19]
duree = int(un(r"FIN DU PILOTE ; duree totale (\d+) s", pil)); assert duree == int(un(r"code 0 apres (\d+) s", lanc))
appels = re.findall(r"code=(\d+) duree=(\d+) s", pil); assert all(c == "0" for c, _ in appels)
dA = {k: int(un(r"lecteur %s +code=0 duree=(\d+) s" % k, pil)) for k in ("etage0", "ancres", "etage1")}
dB = [int(x) for x in re.findall(r"sonde_vide \w+ +code=0 duree=(\d+) s", pil)]; assert len(dB) == 28
canons_pil = dict(re.findall(r"canon (\w+) +([0-9a-f]{16})", pil.split("ETAGE A")[0])); c_pilote = un(r"pilote pilote_gel_vide_machine1_v1.py canon ([0-9a-f]{16})", pil)
assert c_pilote == B(os.path.join(GEL2, "pilote_gel_vide_machine1_v1.py")) and canons_pil["table"] == c_table and canons_pil["sonde_vide"] == B(os.path.join(GEL2, "sonde_vide_machine1_v1.py"))
assert canons_pil["feuille_vide"] == V["feuille_canon"] and "--prevol" not in pil.splitlines()[0] and V["prevol"] is False
procs, drapeau = un(r"PILOTE DU GEL LARGEUR DU VIDE ; (\d+) processus ; python [0-9.]+ ; drapeau (-\w)", pil, 2)
c_verdict_run = un(r"CANON DU VERDICT : ([0-9a-f]{16})", pil); assert c_verdict_run == B(os.path.join(RUN, "verdict_vide.json"))
c_inst = un(r"INSTRUMENT DU LECTEUR : TIENT ; canon de son verdict ([0-9a-f]{16})", pil); assert c_inst == B(os.path.join(RUN, "verdict_ter_instrument.json"))
# -- ce que machine 2 rapporte, par motif
fv_heure, fv_texte = un(r"Le 16/11 a (\d\d:\d\d) \(heure de BOCAL4\), l'operateur a ecrit : \"([^\"]+)\"", note2, 2)
m2_feuille = un(r"Ma feuille \(([0-9a-f]{16}), ecrite de ton texte\)", note2); m2_ecart_pred = un(r"ecart max entre les deux ln q sur 28 cellules : ([0-9.e-]+) ", ana2)
assert "identiques : True" in cmp2.splitlines()[0] and "28 sur 28" in cmp2 and "DESACCORDS : []" in cmp2
m2_rect_canon = un(r"CANON du manifeste \(calcule, non annonce\) : ([0-9a-f]{16})", aut2); assert "console rejouee == log de m1 : True" in aut2
m2_mut, m2_mut_tot = un(r"(\d+) sur (\d+) attrapees", noteH, 2); m2_synth = un(r"sur (5 100) dossiers synthetiques", noteH)
m2_table, m2_table_ecart = un(r"ecrit une table de canon ([0-9a-f]{16}),", noteH), un(r"plus grand ecart ([0-9.e-]+) ;", noteH)
m2_prevol = un(r"14 h 30 a 14 h 46, (1 001) s", noteH)
et = lire(os.path.join(M2H, "certif_gel_vide_partie2_machine2", "etalement_lecteur_joues_machine2_v1.log"))
s_j_med, s_j_max, s_j_n = un(r"mediane ([0-9.]+) ; q25", et), un(r"max ([0-9.]+)\s*$", et.split("\n")[1]), un(r"etats lus \(quatre trajectoires\) : (\d+)", et)
graine = T["graine"]; rect_note = os.path.join(RECT, "rectificatif_gel_vide_partie2_C1_C2_machine1_v1.md"); c_rect = B(rect_note); l_rect = lot(RECT)
assert m2_rect_canon == l_rect[0]
l_g1, l_g2, l_rec1, l_f, l_g, l_h = lot(GEL1), lot(GEL2), lot(REC1), lot(M2F), lot(M2G), lot(M2H)
c_recep, c_essai = B(os.path.join(RRES, "reception_resultat_gel_vide_machine1_v1.py")), B(os.path.join(RRES, "essai_reception_resultat_machine1_v1.py"))
essai = lire(os.path.join(RRES, "essai_reception_resultat_machine1_v1.log")); n_essai = un(r"ESSAI DE LA RECEPTION : (\d+) cas tenus sur \1", essai)
c_bloc = B(os.path.join(GEL1, "chaine_adaptee_bloc_machine1_v1.py")); assert c_bloc in gel2 and "1.33e-12" in gel2
VC = json.load(open(os.path.join(RECT, "verifie_C1_C2_v1.json"))); VC1, VC2 = VC["C1"], VC["C2"]
cel = {x["id"]: x for x in C}; ORDRE = ("MG", "MP", "PP", "PG")
def F(x, n=4):
    return ("%%.%df" % n) % x
def S_(x, n=4):
    return ("%%+.%df" % n) % x

L = []
def T_(s=""): L.append(s)
def P(s, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))

T_("DELTA nn -- LARGEUR DU VIDE, CHAINE D'ORDRE 3 SOUS ABSORBEUR ADAPTE : RUN DU 16/11/2026 SOUS LE GEL")
T_("EN DEUX PARTIES %s (REGLE DE TIRAGE) ET %s (INSTRUMENT, ENONCES)." % (c_g1, c_g2))
T_("VERDICT : V1 %s, VP %s." % (V["V1"]["issue"], V["VP"]["issue"]))
T_("-- PROJET, VERSION 1")
T_("(plume machine 1 ; certification, run et seconde feuille machine 2 ; a contresigner par machine 2)")
T_("=======================================================================")
T_()
T_("nn.0 POSITION")
P("""Ce delta rend le run unique du gel "largeur du vide". Sa question : la largeur de l'etat que porte le site (0, 0), jamais lue
en 2D avant ce run, est-elle celle que predit une chaine a une dimension, l'ordre 3 des blocs deposes sous un absorbeur de chaine
adapte au saut, a des cellules que personne n'a choisies ? Vingt-huit cellules ont ete tirees par une graine de l'operateur (%s) :
quatre w2 (delta = %s, %s, %s, %s), sept profondeurs de barriere chacun (3, 4, 5, 6 barreaux : ligne lisible ; 8, 12, 16 : ligne
profonde). Les predictions etaient gelees dans une table (%s) avant toute lecture.""" % (
    graine, S_(cel["MG3"]["delta"], 3), S_(cel["MP3"]["delta"], 3), S_(cel["PP3"]["delta"], 3), S_(cel["PG3"]["delta"], 3), c_table))
P("""Reponse de la feuille du run : V1 %s (%d cellules lisibles sur %d tiennent), VP %s (%d profondes sur %d). Aucune cellule
n'est tombee, aucune n'est non jugeable, aucune n'est non lue : les %d cellules sont QUALIFIEES par le lecteur et leur temoin tient.
Machine 1 a rejoue la feuille sur les fichiers du run : meme verdict, champ par champ.""" % (
    V["V1"]["issue"], LIS["jugements"]["TIENT"], LIS["cellules"], V["VP"]["issue"], PRO["jugements"]["TIENT"], PRO["cellules"], LIS["qualifiees"] + PRO["qualifiees"]))
P("""A savoir avant tout le reste. (1) L'ecart de la chaine au plateau lu, |ln q|, vaut %s au plus aux cellules lisibles (%s) et %s au
plus aux profondes (%s), pour des tolerances de %s et %s, sur %s decades de largeur (de %.1e a %.1e). (2) Cet ecart est sous
l'etendue de la chaine a %d cellules sur %d : le gel est tenu a ses tolerances, et il ne MESURE pas l'erreur de la chaine en dessous de
ce que son absorbeur laisse indetermine. (3) La largeur jugee est celle d'un etat sous absorbeur ; cet acte ne dit rien de la duree de
vie du systeme ferme.""" % (F(LIS["abs_ln_q_max"], 5), LIS["abs_ln_q_max_cellule"], F(PRO["abs_ln_q_max"], 5), PRO["abs_ln_q_max_cellule"], F(cel["MG3"]["T"], 2),
                             F(cel["MG8"]["T"], 2), F(ENS["decades"], 1), LIS["Gamma_pl_max"], PRO["Gamma_pl_min"], ENS["sous_l_etendue"], len(C)))
T_()
T_("nn.1 CE QUI A ETE JOUE, ET DANS QUEL ORDRE")
P("""Ouverture. L'operateur a ecrit a machine 1 "on gele et on avance !" (16/11/2026, 12 h 19) : declaration de machine 1, que
machine 2 dit ne pas pouvoir attester. A l'operateur de l'attester.""")
P("""Premiere partie du gel (%s, regle de tirage et d'eligibilite, lot %s) : certifiee par machine 2 sans morsure (lot %s, %d
pieces). Graine donnee par l'operateur a machine 1 ("la graine %s", 13 h 34) ; tirage identique sur les deux machines (lot %s).
Seconde partie (%s, lot %s) : certifiee par machine 2 AVANT le run (lot %s, %d pieces) aux cinq points demandes ; aucune correction
d'un nombre ou d'une regle ; deux corrections de TEXTE (C-1, C-2 : nn.9). Sa feuille, ecrite du texte seul, rend les memes verdicts que
celle du gel sur %s dossiers synthetiques ; son pre-vol sur BOCAL4 tient (%s s).""" % (
    c_g1, l_g1[0], l_f[0], l_f[1], graine, l_g[0], c_g2, l_g2[0], l_h[0], l_h[1], m2_synth, m2_prevol))
P("""Rectificatif. Machine 1 a ecrit les deux corrections de texte AVANT le run (%s, lot %s) ; la seconde partie n'a pas de version
2, la table et l'instrument n'ont pas change. Machine 2 dit l'avoir authentifie avant de lancer (canon du manifeste recalcule par elle :
%s ; son rejeu du script de verification rend la console de machine 1).""" % (c_rect, l_rect[0], m2_rect_canon))
P("""Feu vert. Machine 2 rapporte que l'operateur lui a ecrit, le 16/11 a %s (heure de BOCAL4) : "%s". Elle le lit comme le feu
vert ecrit, conditionnel, et dit avoir d'abord authentifie le rectificatif et verifie sa machine. Machine 1 n'a pas vu ce message ;
l'operateur lui a ecrit a 19 h 18 : "M2 vient de lancer le run." C'est a l'operateur de l'attester.""" % (fv_heure.replace(":", " h "), fv_texte))
P("""Run. UN run, dans un dossier neuf, lance le %s a %s et fini a %s (heure de BOCAL4) ; duree totale %d s ; %d appels, tous au
code 0 ; aucun arret, aucune relance (journal du pilote, %s). Pilote joue : celui du gel, tel quel (%s), %s processus, drapeau %s,
lance par un lanceur de machine 2 (%s) qui recalcule %d canons et ne modifie aucune piece. Table jouee : %s, sans --prevol. Les
canons que le pilote imprime au depart sont ceux du gel. Durees : etage A %d s, %d s et %d s (etage 0, ancres, etage 1, en parallele) ;
les 28 cellules de %d a %d s chacune, %s a la fois.""" % (
    debut[:10], debut[11:], fin[11:], duree, len(appels), B(os.path.join(RUN, "pilote_gel_vide.log")), c_pilote, procs, drapeau,
    B(os.path.join(M2I, "run_gel_vide_machine2", "lance_run_vide_machine2_v1.py")), len(re.findall(r"canon .+ [0-9a-f]{16} ok", lanc)), c_table, dA["etage0"], dA["ancres"], dA["etage1"], min(dB), max(dB), procs))
P("""E19. Machine 1 n'a lu en 2D le systeme a fantome a aucune cellule, ni l'etat (0, 0) a aucun w2, ni avant ni apres le run : son
rejeu ne joue que la feuille. Machine 2 declare n'avoir lu, avant la fin du pilote, que le journal de demarrage de son lanceur, et
n'avoir rejoue aucun appel.""")
T_()
T_("nn.2 L'INSTRUMENT")
P("""Instrument du lecteur (etage 0, ancres, etage 1, pieces deposees, tolerances inchangees) : %s ; canon de son verdict %s.
Machine 2 le dit egal, champ pour champ, a celui de son pre-vol.""" % (V["instrument"], c_inst))
P("""Lecteur. %d cellules sur %d QUALIFIEES ; les quatre absorbeurs en PLATEAU partout (%d plateaux sur %d) ; %d lectures du fantome
sur %d suivies ; poids du site (0, 0) au moins %s ; residu au plus %.1e ; aucun decalage repris. L'etalement du plateau sous A vaut %s
au plus ; le plus grand ecart entre absorbeurs %s (%s). L'etalement du lecteur s, le plus grand des deux, va de %s a %s, mediane %s.
Machine 2 l'avait mesure aux %s etats deja lus du delta 100 : mediane %s, au plus %s.""" % (
    LIS["qualifiees"] + PRO["qualifiees"], len(C), ENS["plateaux"], 4 * len(C), LR["brut"]["suivies_fantome"], LR["brut"]["lectures_fantome"], F(ENS["poids_min"], 3),
    LR["brut"]["residu_max_fantome"], F(ENS["etalement_A_max"]), F(ENS["ecart_absorbeurs_max"]), ENS["s_max_cellule"], F(ENS["s_min"]), F(ENS["s_max"]), F(ENS["s_mediane"]),
    s_j_n, s_j_med, s_j_max))
P("""Temoin. Le jumeau sans fantome, a la geometrie de chaque cellule : %d lectures sur %d suivies ; il tient aux %d cellules ; sa
plus grande largeur vaut au plus %.1e du plateau, pour un seuil de %.0e.""" % (
    LR["brut"]["suivies_jumeau"], LR["brut"]["lectures_jumeau"], LIS["temoins_tenus"] + PRO["temoins_tenus"], ENS["temoin_rapport_max"], V["reglage"]["temoin_max"]))
P("""Sous le plancher. %d cellules sur %d ont un plateau sous 1.33e-12 (les %d profondes, et %s) : la qualification en cours de run
y est la seule garde (gel, G-8).""" % (ENS["sous_le_plancher"], len(C), len(PRO["sous_le_plancher"]), " ".join(LIS["sous_le_plancher"])))
P("""Sorties du run (convention B) : verdict de l'instrument %s ; verdict de la feuille %s ; les 28 fichiers de cellule portent
les canons que le journal du pilote imprime.""" % (c_inst, c_verdict_run))
T_()
T_("nn.3 LE VERDICT DE LA FEUILLE DU RUN")
P("""ln q = ln G3* (table gelee) - ln Gamma_pl : positif quand la chaine depasse la lecture. Bande b = etendue de la chaine sur ses
dix-huit variantes + etalement s du lecteur. TIENT si |ln q| <= T - b ; marge = T - b - |ln q|.""")
T_("    cellule  w2         m   ln Gamma_pl  s       etendue  bande b  ln q      T     marge   jugement")
for x in C:
    T_("    %-7s  %-9s  %-2d  %s     %s  %s   %s   %s  %s  %s  %s" % (x["id"], x["w2"], x["m"], S_(x["ln_Gamma_pl"]), F(x["s"]), F(x["etendue"]), F(x["bande"]),
                                                                           S_(x["ln_q"], 5), F(x["T"], 2), F(x["marge"]), x["jugement"]))
P("""V1 (%d cellules lisibles) : %s ; %d TIENT, %d TOMBE, %d NON JUGEABLE, %d NON LUE ; quatre tenues a chaque creneau. VP (%d
cellules profondes, hors de V1) : %s ; %d TIENT, %d TOMBE, %d NON JUGEABLE, %d NON LUE. Le run est complet.""" % (
    LIS["cellules"], V["V1"]["issue"], LIS["jugements"]["TIENT"], LIS["jugements"]["TOMBE"], LIS["jugements"]["NON JUGEABLE"], LIS["jugements"]["NON LUE"],
    PRO["cellules"], V["VP"]["issue"], PRO["jugements"]["TIENT"], PRO["jugements"]["TOMBE"], PRO["jugements"]["NON JUGEABLE"], PRO["jugements"]["NON LUE"]))
assert all(v == 4 for v in LIS["tenues_par_creneau"].values())
P("""Le lecteur, par cellule : barreau de depart du plateau sous A, B, C, D ; etalement du plateau sous A ; ecarts |ln| de B, C, D a
A ; rapport de la plus grande largeur du jumeau au plateau. Statut QUALIFIE et quatre PLATEAUX partout.""")
T_("    cellule  k0 (A B C D)   etalement A  ecart B   ecart C   ecart D   jumeau / plateau")
for x in C:
    T_("    %-7s  %-13s  %.1e      %.1e   %.1e   %.1e   %.1e" % (x["id"], " ".join("%2d" % x["k0"][a] for a in "ABCD"), x["etalement_A"], x["ecarts_ln_A"]["B"],
                                                                 x["ecarts_ln_A"]["C"], x["ecarts_ln_A"]["D"], x["temoin_rapport"]))
T_()
T_("nn.4 LE REJEU DE MACHINE 1 (etape 5 du gel)")
P("""Lot de resultat authentifie : %s, %d pieces sur %d. La piece de reception (%s) et son essai (%s, %s cas tenus sur %s) ont ete
ecrits PENDANT le run, avant tout resultat ; machine 1 en a donne les canons a l'operateur avant de recevoir le lot : declaration de
machine 1, a l'operateur de l'attester. Elle fixait d'avance comment compter les annonces (nn.9).""" % (canon_res, n_res, n_res, c_recep, c_essai, n_essai, n_essai))
P("""Feuille du gel (%s), rejouee par machine 1 sur les fichiers du run : %s. %d champs compares, dont %d nombres ; aucun champ
d'issue, de jugement ou de statut ne differe, ni aucun autre champ discret ; plus grand ecart d'un nombre : %.1e. La regle "deux
machines" du gel (lecture la moins favorable) n'a pas a jouer.""" % (V["feuille_canon"], CP["issue"], CP["champs"], CP["nombres_compares"], CP["plus_grand_ecart"]))
P("""Hors verdict, machine 2 a joue sa propre feuille (%s) sur les memes fichiers : meme verdict, memes jugements a 28 cellules sur
28. Elle note que ce zero est moins fort qu'il n'en a l'air, les deux feuilles appelant la meme routine deposee du lecteur. Et elle a
recalcule ln q avec SES predictions de chaine : ecart de %s au plus a celui de la feuille. C'est ce dernier controle qui garde le
chemin du fantome de la sonde, lequel n'avait jamais tourne avant le run (le pre-vol ne le lit pas, G-6) : ses 28 largeurs retrouvent
des chaines calculees de deux cotes.""" % (m2_feuille, m2_ecart_pred))
T_()
T_("nn.5 LECTURE, ENONCE PAR ENONCE")
P("""V1. Aux %d cellules lisibles (3 a 6 barreaux, |delta| de %s a %s, plateaux de %.1e a %.1e) : |ln q| vaut %s en mediane et %s au
plus (%s) pour T = %s ; la plus petite marge est %s (%s). La bande va de %s a %s : l'etendue de la chaine y entre pour %s a %s,
le lecteur pour %s a %s.""" % (
    LIS["cellules"], F(min(abs(x["delta"]) for x in C), 3), F(max(abs(x["delta"]) for x in C), 3), LIS["Gamma_pl_min"], LIS["Gamma_pl_max"], F(LIS["abs_ln_q_mediane"], 5),
    F(LIS["abs_ln_q_max"], 5), LIS["abs_ln_q_max_cellule"], F(cel["MG3"]["T"], 2), F(LIS["marge_min"]), LIS["marge_min_cellule"], F(LIS["bande_min"]), F(LIS["bande_max"]),
    F(LIS["etendue_min"]), F(LIS["etendue_max"]), F(LIS["s_min"]), F(LIS["s_max"])))
P("""VP. Aux %d cellules profondes (8, 12 et 16 barreaux, plateaux de %.1e a %.1e) : |ln q| vaut %s en mediane et %s au plus (%s) pour
T = %s ; la plus petite marge est %s (%s). Des cellules ont ete jugees jusqu'a 16 barreaux, aux quatre creneaux. Toute cette ligne est
sous 1.33e-12 : ce que VP dit, il le dit d'une reference que rien d'autre que sa stabilite sous quatre absorbeurs ne garde.""" % (
    PRO["cellules"], PRO["Gamma_pl_min"], PRO["Gamma_pl_max"], F(PRO["abs_ln_q_mediane"], 5), F(PRO["abs_ln_q_max"], 5), PRO["abs_ln_q_max_cellule"], F(cel["MG8"]["T"], 2),
    F(PRO["marge_min"]), PRO["marge_min_cellule"]))
P("""Ce que ces nombres ne permettent pas. |ln q| est sous l'etendue de la chaine a %d cellules sur %d, sous la bande a %d, et sous
l'etalement du lecteur a %d. Le gel tient donc avec une marge large, mais la taille de l'ecart (quelques dix-milliemes) est en dessous
de ce que la chaine et le lecteur determinent chacun : elle n'est pas une mesure de l'erreur de la chaine.""" % (
    ENS["sous_l_etendue"], len(C), ENS["sous_la_bande"], ENS["sous_s"]))
T_()
T_("nn.6 CE QUI ETAIT CONSIGNE SANS ETRE JUGE")
P("""Les autres predictions de la table, a la meme lecture : ln q de l'ordre 2, du premier ordre, de la loi d'echelle |delta|
Phi*(kappa), de la forme fermee (avec la definition de M0 du rectificatif) ; et ln(Gamma_pl / |delta|).""")
T_("    cellule  ordre 3    ordre 2   ordre 1   loi d'echelle  forme fermee  ln(Gamma_pl/|delta|)")
for x in C:
    T_("    %-7s  %s   %s   %s   %s        %s       %s" % (x["id"], S_(x["ln_q"], 5), S_(x["ln_q_ordre2"]), S_(x["ln_q_ordre1"]), S_(x["ln_q_loi"]), S_(x["ln_q_forme"]),
                                                          S_(x["ln_Gamma_pl_sur_delta"])))
P("""Ordres. Ligne lisible : l'ordre 2 est a %s au plus du plateau (%s), le premier ordre a %s (%s), la loi d'echelle a %s (%s), la
forme fermee a %s (%s) ; l'ordre 3 est plus pres que l'ordre 2 a %d cellules sur %d, que le premier ordre a %d, que la loi d'echelle a
%d. Ligne profonde : %s (%s), %s (%s), %s (%s), %s (%s) ; plus pres a %d, %d et %d cellules sur %d. Le gel disait (section 1) que V1 ne
separe pas les ordres, et que les corrections a la loi d'echelle ne seraient eprouvees que sur la ligne profonde du creneau MG si elle
etait lue. Elle l'a ete : a MG12 et MG16 l'ordre 3 est a %s et %s du plateau, le premier ordre a %s et %s, la loi d'echelle a %s et %s,
pour des bandes de %s et %s. Ce sont des nombres consignes : aucun enonce du gel ne portait sur eux.""" % (
    F(LIS["ordre2_abs_max"]), LIS["ordre2_abs_max_cellule"], F(LIS["ordre1_abs_max"]), LIS["ordre1_abs_max_cellule"], F(LIS["loi_abs_max"]), LIS["loi_abs_max_cellule"],
    F(LIS["forme_abs_max"]), LIS["forme_abs_max_cellule"], LIS["ordre3_plus_pres_que_ordre2"], LIS["cellules"], LIS["ordre3_plus_pres_que_ordre1"], LIS["ordre3_plus_pres_que_loi"],
    F(PRO["ordre2_abs_max"]), PRO["ordre2_abs_max_cellule"], F(PRO["ordre1_abs_max"]), PRO["ordre1_abs_max_cellule"], F(PRO["loi_abs_max"]), PRO["loi_abs_max_cellule"],
    F(PRO["forme_abs_max"]), PRO["forme_abs_max_cellule"], PRO["ordre3_plus_pres_que_ordre2"], PRO["ordre3_plus_pres_que_ordre1"], PRO["ordre3_plus_pres_que_loi"], PRO["cellules"],
    S_(cel["MG12"]["ln_q"]), S_(cel["MG16"]["ln_q"]), S_(cel["MG12"]["ln_q_ordre1"]), S_(cel["MG16"]["ln_q_ordre1"]), S_(cel["MG12"]["ln_q_loi"]), S_(cel["MG16"]["ln_q_loi"]),
    F(cel["MG12"]["bande"]), F(cel["MG16"]["bande"])))
k = V["consigne"]; assert k["ordre3_plus_pres_que_ordre1"] == LIS["ordre3_plus_pres_que_ordre1"] + PRO["ordre3_plus_pres_que_ordre1"]
SU = LR["superposition"]
P("""Superposition. A profondeur egale les quatre creneaux ont le meme kappa (a %.0e pres) : la loi d'echelle les superposerait en
ln(Gamma_pl / |delta|). Ils s'ecartent de %s a 3 barreaux, %s a 6, %s a 8, %s a 12 et %s a 16. La chaine predit ces ecarts (%s, %s,
%s, %s, %s) : une fois sa correction retiree il reste %s, %s, %s, %s et %s.""" % (
    max(SU[m]["kappa_etendue_relative"] for m in SU), F(SU["3"]["etendue"]), F(SU["6"]["etendue"]), F(SU["8"]["etendue"]), F(SU["12"]["etendue"]), F(SU["16"]["etendue"]),
    F(SU["3"]["etendue_des_r3"]), F(SU["6"]["etendue_des_r3"]), F(SU["8"]["etendue_des_r3"]), F(SU["12"]["etendue_des_r3"]), F(SU["16"]["etendue_des_r3"]),
    F(SU["3"]["etendue_apres_la_chaine"]), F(SU["6"]["etendue_apres_la_chaine"]), F(SU["8"]["etendue_apres_la_chaine"]), F(SU["12"]["etendue_apres_la_chaine"]),
    F(SU["16"]["etendue_apres_la_chaine"])))
PC = SG["par_creneau"]; D = SG["lisibles_ou_a_et_b_different"]; Cc = SG["lisibles_ou_a_et_b_coincident"]
P("""Signe de ln q. Positif a %d cellules sur %d, negatif a %d ; mediane %s. Par creneau : MG %d sur %d, MP %d sur %d, PP %d sur %d,
PG %d sur %d. A delta < 0 il est positif a %d cellules sur %d, a delta > 0 a %d sur %d : il ne suit pas le signe de delta (il en a le
signe a %d cellules sur %d). Il a le signe de la lecture (b) a %d. Aux %d cellules lisibles ou les lectures (a) et (b) different, il
a le signe de (b) a %d (%s) et celui de (a) a %d (%s) ; aux %d ou elles coincident, le signe commun a %d.""" % (
    SG["positifs"], len(C), SG["negatifs"], S_(ENS["ln_q_mediane"], 5), PC["MG"]["positifs"], PC["MG"]["cellules"], PC["MP"]["positifs"], PC["MP"]["cellules"],
    PC["PP"]["positifs"], PC["PP"]["cellules"], PC["PG"]["positifs"], PC["PG"]["cellules"], SG["delta_negatif"]["positifs"], SG["delta_negatif"]["cellules"],
    SG["delta_positif"]["positifs"], SG["delta_positif"]["cellules"], SG["du_signe_de_delta"], len(C), SG["du_signe_de_la_lecture_b"], len(D["cellules"]),
    len(D["du_signe_de_b"]), " ".join(D["du_signe_de_b"]), len(D["du_signe_de_a"]), " ".join(D["du_signe_de_a"]), len(Cc["cellules"]), len(Cc["du_signe_commun"])))
assert k["ln_q_du_signe_de_delta"] == SG["du_signe_de_delta"] and k["ln_q_du_signe_de_la_sous_correction"] == SG["du_signe_de_la_lecture_b"]
MG = SG["MG_lisibles"]
P("""Ces signes ne departagent rien : la taille est sous l'etendue de la chaine a toutes les cellules. Aux quatre cellules
lisibles de MG, les seules ou le rectificatif attendait que le signe puisse se lire, ln q vaut %s, %s, %s et %s pour des etendues de
%s, %s, %s et %s ; la lecture (b) y attendait de %s a %s pour la part manquee mediane des etats joues. Machine 2 note qu'un petit
decalage positif commun aux deux signes de delta decrirait aussi ces 28 nombres, et que personne ne l'avait ecrit avant le run. L'acte
ne retient ni l'un ni l'autre : le gel ne departage pas (a) de (b).""" % (
    S_(MG[0]["ln_q"], 5), S_(MG[1]["ln_q"], 5), S_(MG[2]["ln_q"], 5), S_(MG[3]["ln_q"], 5), F(MG[0]["etendue"]), F(MG[1]["etendue"]), F(MG[2]["etendue"]), F(MG[3]["etendue"]),
    F(MG[0]["attente_b_mediane"]), F(MG[3]["attente_b_mediane"])))
assert all(x["ln_q"] < x["etendue"] for x in MG) and [x["id"] for x in MG] == ["MG3", "MG4", "MG5", "MG6"]
T_()
T_("nn.7 LES ANNONCES DE LA PLUME, CONFRONTEES AU RUN (gel, section 10)")
a3 = AN["A-3"]; a6 = AN["A-6"]; a7 = AN["A-7"]
assert AN["A-1"]["realise"] is True and AN["A-2"]["realise"] is True and a3["realise"] == {"seize": True, "douze_au_moins": True} and a6["realise"] is True
assert AN["A-4"]["realise"] == "TENU" and AN["A-5"]["realise"] == "TENU" and a7["realise"] == "positif" and not a7["au_dela_de_la_bande"]
P("""A-1 (%s, l'instrument tient) : il tient. A-2 (%s, le temoin tient aux 28 cellules) : il tient aux %d. A-3 (%s pour seize
cellules lisibles qualifiees, %s pour douze au moins) : %d sur 16. A-4 : la plume donnait %s a "V1 TENU", %s a "NON CONCLUANT", %s a
"TOMBE" : c'est V1 TENU. A-5 : %s a "VP TENU", %s a "NON LUE ou NON CONCLUANT", %s a "TOMBE" : c'est VP TENU. A-6 (%s, plus grand |ln
q| lisible sous %s) : %s, a %s. A-7 : la plume donnait %s a "negatif a trois cellules lisibles de MG au moins" et %s a "positif a
trois au moins" : il est positif aux %d ; aucune ne sort de sa bande, et l'annonce, vraie dans sa lettre, ne tranche rien (nn.6).""" % (
    F(PA["A-1"], 2), F(PA["A-2"], 2), AN["A-2"]["temoins_tenus"], F(PA["A-3"]["seize"], 2), F(PA["A-3"]["douze_au_moins"], 2), a3["qualifiees"],
    F(PA["A-4"]["TENU"], 2), F(PA["A-4"]["NON CONCLUANT"], 2), F(PA["A-4"]["TOMBE"], 2), F(PA["A-5"]["TENU"], 2), F(PA["A-5"]["NON LUE ou NON CONCLUANT"], 2),
    F(PA["A-5"]["TOMBE"], 2), F(PA["A-6"]["probabilite"], 2), F(PA["A-6"]["seuil"], 2), F(a6["plus_grand"], 5), a6["cellule"], F(PA["A-7"]["negatif"], 2),
    F(PA["A-7"]["positif"], 2), len(a7["positives"])))
P("""La plume etait pessimiste, pour la seconde fois de suite apres le gel "ordre 3". Elle ecrivait que l'issue qu'elle craignait
le plus etait le NON CONCLUANT, "une tolerance de 0.02 contre une bande que le lecteur peut elargir" : aucune cellule n'est non
jugeable ; la plus grande bande lisible vaut %s et le lecteur n'y met que %s au plus. Elle n'avait pas la mesure de l'etalement du
lecteur aux etats deja lus quand elle a gele ses annonces (rectificatif, section 4) ; ce n'est pas une excuse : la mesure etait a sa
portee.""" % (F(LIS["bande_max"]), F(LIS["s_max"])))
T_()
T_("nn.8 CE QUE CET ACTE ECRIT, ET CE QU'IL N'ECRIT PAS (gel, section 8)")
P("""V1 TENU. L'acte ecrit la phrase que le gel autorisait : a seize cellules tirees au sort, de 3 a 6 barreaux et pour |delta|
de %s a %s, la chaine d'ordre 3 sous absorbeur adapte rend la largeur de l'etat porte par (0, 0) a %s pres en logarithme, au-dela de
sa propre etendue et de l'etalement du lecteur.""" % (F(min(abs(x["delta"]) for x in C), 3), F(max(abs(x["delta"]) for x in C), 3), F(cel["MG3"]["T"], 2)))
P("""VP TENU. La chaine tient aussi a 8, 12 et 16 barreaux, a %s pres, aux douze cellules profondes, toutes qualifiees par le
lecteur ; des cellules ont ete jugees jusqu'a 16 barreaux.""" % F(cel["MG8"]["T"], 2))
P("""Le bloc de l'absorbeur adapte (%s) peut etre propose au depot ; la decision est a l'operateur.""" % c_bloc)
P("""Il n'ecrit PAS : que la chaine est exacte, ni qu'elle l'est a un millieme (l'ecart lu est sous son etendue : nn.5) ; que
l'ordre 3 est JUGE meilleur que le premier ordre ou que la loi d'echelle (c'est consigne aux cellules profondes de MG, nn.6 ; ce
n'etait pas un enonce) ; la loi d'echelle comme resultat juge pour le vide (sa superposition est consignee, avec ses ecarts) ; laquelle
des lectures (a) et (b) vaut au vide ; rien des cellules non tirees, des |delta| hors de %s a %s, des centiemes exclus ; rien de la
duree de vie du systeme ferme : la largeur est celle d'un etat sous absorbeur, stable sous les variations jouees, et rien d'autre.
Aucun seuil, aucune garde, aucune tolerance n'a ete regle apres lecture ; ce gel ne se rejoue pas.""" % (
    F(min(abs(x["delta"]) for x in C), 3), F(max(abs(x["delta"]) for x in C), 3)))
T_()
T_("nn.9 CORRECTIONS DE MACHINE 2, DEFAUTS DE LA PLUME, ECARTS")
P("""C-1 (correction de texte de machine 2 ; D-VIDE-7). La seconde partie ne disait pas comment M0 est pris dans la forme fermee.
Il l'est avec kappa a la cellule (rectificatif, section 1) ; avec la definition de la note sur la loi d'echelle la forme fermee
differerait de %s au pire (a %s). La loi s'ecrit en kappa, le saut sur le desaccord, pas en g / |delta|. Sans effet sur un verdict : la
forme fermee est consignee.""" % (F(VC1["ecart_max_avec_la_definition_de_la_note"], 2), VC1["cellule"]), 2, 4)
P("""C-2 (correction de texte de machine 2 ; D-VIDE-8). La seconde partie disait qu'a %d des %d etats joues la chaine rend une
correction trop petite ; c'est a %d (rectificatif, section 2). Sans effet.""" % (VC2["part_positive"], VC2["etats"], VC2["entre_0_et_1"]), 2, 4)
P("""A-7. Machine 2 precisait que les lectures (a) et (b) different a MG et a MP ; le rectificatif ajoutait que seule MG pouvait
les departager par la taille. Le run ne les departage a aucune (nn.6).""", 2, 4)
P("""D-VIDE-1 a D-VIDE-5 sont declares dans la note sur le vide ; D-VIDE-6 dans le lot de reception %s.""" % l_rec1[0], 2, 4)
P("""Les ecarts E-1 a E-7 de la seconde partie restent tels qu'ecrits (section 14).""", 2, 4)
P("""Conventions de comptage des annonces, fixees par machine 1 seule pendant le run (piece de reception) : A-2 comptee
indeterminee si une cellule n'est pas qualifiee et qu'aucun temoin juge n'echoue ; un run incomplet compte dans la case "instrument"
de A-4 et A-5 ; A-7 "ni l'un ni l'autre" au reste des probabilites. Aucune n'a joue.""", 2, 4)
P("""Reserves de machine 2 a sa certification, sans correction : le script de predictions de machine 1 ne refait la table gelee "au
canon" que sur la plateforme de machine 1 (sur BOCAL4 : canon %s, a %s au plus) ; son test par mutations attrape %s fautes greffees sur
%s, les deux manquees etant des egalites de bord (strict contre large).""" % (m2_table, m2_table_ecart, m2_mut, m2_mut_tot), 2, 4)
P("""Ce que machine 2 dit ne pas avoir fait : verifier que deux executions de l'etage B rendent les memes octets (par regle il
n'y a qu'un run) ; relire la sonde ligne a ligne apres le run.""", 2, 4)
T_()
T_("nn.10 LIMITES")
P("""Celles du gel, section 13, restent (L-1 a L-9) : l'objet juge est UNE chaine sous UN absorbeur de chaine ; la reference est
une largeur sous absorbeur, qualifiee par sa stabilite sous quatre absorbeurs ; quatre w2, un seul par creneau ; un seul modele, un
seul etat ; la tolerance ne sort pas d'une theorie de l'erreur.""", 2, 4)
P("""Sous 1.33e-12 (%d cellules sur %d) aucune seconde mesure 2D n'existe : une erreur commune aux quatre absorbeurs echapperait
au lecteur. Ce qui appuie ces lectures est indirect : le jumeau, et le fait que la chaine, calculee avant et par deux machines, les
retrouve.""" % (ENS["sous_le_plancher"], len(C)), 2, 4)
P("""La 2D des cellules a ete calculee sur une seule machine (BOCAL4), une seule fois. Machine 1 n'en a rejoue aucune.""", 2, 4)
P("""Le chemin du fantome de la sonde a tourne pour la premiere fois dans ce run (nn.4).""", 2, 4)
P("""La chaine et la 2D partagent le moteur (%s) : les memes elements de matrice font le hamiltonien de la boite et les sauts de la
chaine. L'accord eprouve la reduction a une dimension et les absorbeurs, pas le moteur.""" % canons_pil["moteur"], 2, 4)
P("""L'accord a quelques dix-milliemes n'est pas resolu : il est sous l'etendue de la chaine partout (nn.5).""", 2, 4)
P("""Le feu vert de l'operateur est rapporte par machine 2 ; machine 1 ne l'a pas vu. L'ouverture, la graine et l'anteriorite de
la piece de reception sont des declarations de machine 1.""", 2, 4)
T_()
T_("nn.11 SUITE")
P("""Contreseing de machine 2. Depot : a la decision de l'operateur, numero pris au depot. Ce run s'appuie sur des pieces qui ne
sont pas au registre : les deux parties du gel et leurs lots (table gelee, sonde, feuille, pilote, bloc de l'absorbeur adapte), le
rectificatif, les notes sur la loi d'echelle et sur le vide. Ce gel ne se rejoue pas.""")
T_()
T_("nn.12 PIECES (convention B)")
for c, quoi in ((c_g1, "gel, premiere partie (lot %s)" % l_g1[0]), (c_g2, "gel, seconde partie (lot %s)" % l_g2[0]), (c_table, "table gelee des 28 cellules"),
                (c_bloc, "bloc de l'absorbeur adapte"), (c_rect, "rectificatif C-1, C-2 (lot %s)" % l_rect[0]),
                (l_f[0], "lot de machine 2 : certification de la premiere partie"), (l_g[0], "lot de machine 2 : son tirage"),
                (l_h[0], "lot de machine 2 : certification de la seconde partie"), (canon_res, "lot de machine 2 : resultat du run"),
                (B(os.path.join(M2H, "POUR_MACHINE1_certification_gel_vide_partie2_machine2_v1.md")), "sa note de certification de la seconde partie"),
                (B(os.path.join(M2I, "POUR_MACHINE1_resultat_run_gel_vide_machine2_v1.md")), "sa note de resultat"),
                (c_pilote, "pilote joue (celui du gel)"), (B(os.path.join(M2I, "run_gel_vide_machine2", "lance_run_vide_machine2_v1.py")), "lanceur de machine 2"),
                (B(os.path.join(RUN, "pilote_gel_vide.log")), "journal du pilote du run"), (c_inst, "verdict de l'instrument du lecteur"),
                (c_verdict_run, "verdict de la feuille du run"), (B(os.path.join(R16I, "verdict_vide_rejoue_machine1.json")), "verdict rejoue par machine 1"),
                (B(os.path.join(M2I, "resultats_run_vide_machine2", "verdict_vide_feuille_machine2.json")), "verdict de la seconde feuille de machine 2"),
                (c_recep, "piece de reception de machine 1 (ecrite pendant le run)"), (c_essai, "son essai"),
                (B(os.path.join(R16I, "reception_resultat_vide_v1.json")), "reception : comparaison des verdicts et annonces"),
                (B(os.path.join(R16I, "lecture_resultat_vide_machine1_v1.py")), "lecture du resultat pour l'acte (script)"),
                (B(os.path.join(R16I, "lecture_resultat_vide_v1.json")), "lecture du resultat pour l'acte (nombres)")):
    T_("    %s %s" % (c, quoi))
T_()
T_("-- FIN %s --" % os.path.basename(SORTIE)[:-3])
texte = "\n".join(L) + "\n"; texte.encode("ascii"); assert "%" not in texte, [l for l in L if "%" in l]
assert max(len(l) for l in L) <= 100, [(len(l), l) for l in L if len(l) > 100]
open(SORTIE, "w", encoding="ascii", newline="\n").write(texte)
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(SORTIE), len(L), B(SORTIE)))
