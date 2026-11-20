# -*- coding: ascii -*-
"""CONSTRUCTION de la seconde partie du gel "pont" -- machine 1, v1, 2026-11-17.
Chaque nombre du texte est lu dans une piece ; aucun n'est tape. ASCII, lignes de 100 colonnes au plus, sans signe
"pour cent" (sauf la mention du format "%.5e").
Usage : python3 -I -B ce_script <dossier partie2> <dossier qualif> <dossier certif_m2> <clone du registre>
                                <lot de certification de machine 2> <liste des pieces.json>
                                <regards_complements_v1.json de la premiere partie> <sortie.md>"""
import sys, os, json, math, re, hashlib, unicodedata, textwrap, subprocess
P2, QU, CE, CLONE, LOT_M2, LISTE, REGARDS, SORTIE = [a.rstrip("/") for a in sys.argv[1:9]]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
L = []
def par(texte, retrait="  ", suite=None):
    L.extend(textwrap.wrap(" ".join(texte.split()), width=100, initial_indent=retrait, subsequent_indent=retrait if suite is None else suite,
                           break_long_words=False, break_on_hyphens=False))
def brut(*lignes): L.extend(lignes)
def titre(t): brut("", t)
def sci(v, n=1): return ("%." + str(n) + "e") % v

CH = json.load(open(P2 + "/chaine_cellules_pont_v1.json")); X = CH["ecarts"]; C = CH["cellules"]
BQ = json.load(open(QU + "/bilan_qualification_pont_v1.json"))
R1 = json.load(open(CE + "/controle_details_R1_v1.json")); LT = json.load(open(CE + "/lecture_certification_m2_v1.json"))
REP = json.load(open(QU + "/repetition_verdict_v1.json")); CI = json.load(open(P2 + "/controles_instruments_pont_v1.json"))
RG = json.load(open(REGARDS))["E"]
durees = [float(re.search(r"\((\d+) s\)\s*$", open("%s/densite_2d_SA%d_%s_v1.log" % (QU, m, a)).read().strip().split("\n")[-1]).group(1))
          for m in (4, 5) for a in "ABCD"]
pics = [float(x) for f in os.listdir(QU) if f.startswith("boite") and f.endswith(".log")
        for x in re.findall(r"pic de memoire (\d+) Mo", open(QU + "/" + f).read())]
tir = open(P2 + "/tirage_pont_graine_456823_machine1_v1.log", encoding="ascii").read()
GRAINE = re.search(r"^graine : (\d+)$", tir, re.M).group(1)
rang = {s: re.search(r"^creneau %s rang (\d+) : numero (\d+) sur (\d+) -> w2 = (\S+) \((\S+)\) : ELIGIBLE, retenu$" % s, tir, re.M).groups() for s in ("MG", "PG")}
cel = re.findall(r"^  (\S+)\s+w2 = (\S+)\s+m = (\d) g = (\S+)$", tir, re.M)
assert [c[0] for c in cel] == ["MG3", "MG4", "MG5", "PG3", "PG4", "PG5"] and re.search(r"^TIRAGE : 6 cellules$", tir, re.M)
for nom, w2, m, g in cel: assert (C[nom]["w2"], str(C[nom]["m"]), C[nom]["g"]) == (w2, m, g)
NOMS = [c[0] for c in cel]
def h16(s, r): return hashlib.sha256(("%s|%s|%d" % (GRAINE, s, r)).encode("ascii")).hexdigest()
for s in ("MG", "PG"): assert int(h16(s, int(rang[s][0])), 16) % int(rang[s][2]) == int(rang[s][1])
assert LT["canon_commune_fichier"] == LT["canon_mon_sous_ensemble"] and LT["serialisation_identique"]["tel quel"]
COMMUNE = LT["canon_commune_fichier"]
tete = subprocess.run(["git", "-C", CLONE, "rev-parse", "--short=7", "HEAD"], capture_output=True, text=True).stdout.strip()
blocs = ["m17_chaine_v17.py", "chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py",
         "sonde_lecteur_gel_loi_machine1_v1.py"]
cb = {b: canon(CLONE + "/scripts/" + b) for b in blocs}
man_m2 = [f for f in os.listdir(os.path.dirname(LOT_M2)) if f.startswith("MANIFEST_")]; assert len(man_m2) == 1
CAN_M2 = canon(os.path.dirname(LOT_M2) + "/" + man_m2[0]); NOTE_M2 = canon(LOT_M2 + "/POUR_MACHINE1_certification_gel_pont_partie1_machine2_v1.md")
pieces = json.load(open(LISTE)); cp = {os.path.basename(p): canon(p) for p in pieces}; assert len(cp) == len(pieces)
def c_(nom): return cp[nom]

brut('GEL "PONT" -- SECONDE PARTIE : L\'INSTRUMENT, LES ENONCES, LES TOLERANCES',
     "pre-enregistrement, machine 1, 2026-11-17, version 1. Classe A. ASCII, lignes de 100 colonnes.")
titre("0. STATUT")
par("""Cette piece est la seconde partie du gel "pont". La premiere (canon 735ce41be200c5cd) a fixe le tirage et l'eligibilite ;
machine 2 l'a certifiee (lot %s) ; l'operateur a donne la graine. Cette piece fixe, AVANT toute 2D aux cellules tirees : les six
cellules, ce que la chaine seule y predit, les deux sondes et les trois feuilles, les enonces et leurs tolerances, ce que vaut une
cellule illisible, ce que chaque issue engage, et les annonces de la plume.""" % CAN_M2)
par("""RIEN N'EST JOUE. Aucune 2D du systeme a fantome, de quelque sorte, n'a ete calculee par machine 1 a w2 = %s ni a w2 = %s. Tout
ce qui est calcule et lu ici en 2D l'est au point sacrifie w2 = 101/50, qui n'est pas candidat ; un essai du code, a l'aveugle, a un
autre w2 non candidat, est dit en section 6. Le run n'a lieu qu'apres la certification
de cette piece par machine 2 et le feu vert ECRIT de l'operateur (E19). Machine 2 joue, une fois.""" % (rang["MG"][3], rang["PG"][3]))
par("Cette piece ne juge rien et ne depose rien.")

titre("1. SOURCES (convention B)")
brut("    735ce41be200c5cd  gel_pont_partie1_regle_tirage_pre_enregistrement_v1.md (lot de machine 1",
     "                      55612644fc4ca279)",
     "    %s  lot de machine 2 : certification de la premiere partie ; sa note :" % CAN_M2,
     "    %s  POUR_MACHINE1_certification_gel_pont_partie1_machine2_v1.md" % NOTE_M2,
     "    %s  table_commune_pont_v1.json : la table commune, la meme des deux cotes" % COMMUNE,
     "    dce7431e7a8b4a8c  lot de machine 2 : 32 boites fermees au point sacrifie, 3 barreaux")
par("Registre public lbaaz/SG_1, tete %s (delta 102). Blocs deposes, executes tels quels :" % tete)
for b, quoi in zip(blocs, ("le moteur", "tables d'ordre 2", "tables d'ordre 3", "absorbeur adapte de la chaine", 'le bloc "LECTEUR CREUX"')):
    brut("    %s  scripts/%s (%s)" % (cb[b], b, quoi))

titre("2. LA GRAINE ET LE TIRAGE")
par("""L'operateur a donne la graine a machine 1 le 17/11/2026 a 09 h 56, apres lui avoir remis la certification de machine 2 : %s. Elle
ne se change plus ; aucune machine ne la choisit ni ne la commente.""" % GRAINE)
par("""Tirage de machine 1 sur la table commune (%s), par tirage_pont_machine1_v1.py (69b8e585f57e0c1e), regle de la section 3 de la
premiere partie :""" % COMMUNE)
for s in ("MG", "PG"):
    r, num, n, w2, dec = rang[s]
    brut('    creneau %s, rang %s : sha256("%s|%s|%s") = %s... ; modulo %s = %s' % (s, r, GRAINE, s, r, h16(s, int(r))[:16], n, num),
         "                        -> w2 = %s (%s), ELIGIBLE, retenu" % (w2, dec))
par("LES SIX CELLULES :")
for nom, w2, m, g in cel: brut("    %-4s w2 = %-10s m = %s  g = %s" % (nom, w2, m, g))
par("Machine 2 tire de son cote, par son script. Si ses six cellules ne sont pas celles-ci : PAS DE GEL.")

titre("3. RECTIFICATION DE LA PREMIERE PARTIE (reserve R1 de machine 2)")
B = R1["B"]; assert B["decisions_iii_qui_changent"] == 0; em = B["ecart_relatif_max_par_profondeur"]; ch = B["cellules_dont_l_etendue_change_de_plus_de_5e-5"]
par("""Machine 2 a certifie la premiere partie avec une reserve de redaction, R1 : le 4.4 dit "Gamma = -2 Im(E)" sans dire que la valeur
propre lue en double precision ne suffit pas a 4 et 5 barreaux. La reserve est fondee, et la faute est de la plume : le gel du vide
portait la phrase, la premiere partie de ce gel l'a laissee tomber. Le 4.4 se lit AINSI : la largeur d'une variante est lue sans
perte, par le flux 2 somme_m W_m |psi_m|^2 / somme_m |psi_m|^2 tant que Gamma / |delta| > 1e-15, en precision arbitraire en dessous ;
c'est ce que fait le bloc depose, et ce qu'a fait le script de la premiere partie.""")
par("""Controle de machine 1 sur ses 48 matrices : -2 Im(E) en double precision s'ecarte de la lecture du bloc de %s au plus a 3
barreaux, %s a 4, %s a 5 ; l'etendue au vide change de plus de 5e-5 dans %d cellules (%d a 4 barreaux, %d a 5) ; %s decision de la
condition (iii) ne change (plus grande etendue ainsi lue : %.4f, pour un seuil de 0.02). La piece de la premiere partie n'est pas
retouchee.""" % (sci(em["3"]), sci(em["4"]), sci(em["5"]), ch["3"] + ch["4"] + ch["5"], ch["4"], ch["5"], "aucune",
                
                 B["plus_grande_etendue_en_double"]))
A_ = R1["A"]; pg = max(A_["plus_grand_ecart_absolu"].values())
par("""Pris aussi de sa note, sans changement de la regle. Sur les 48 cellules, seule la condition (v), a l'ecart x = 8, ecarte des
cellules ; les seuils (i) a (iv) n'en lient aucune et ne sont pas eprouves par cette table. La table commune est citee par son canon
%s (format de la section 5), non par le JSON complet de machine 1 (d03c9ca093ea5bfc), que machine 2 dit ne pas reproduire a l'octet
sur BOCAL4 (decisions identiques, flottants a 9e-7 pres). Controle de machine 1 : la chaine de machine 2, ecrite depuis le texte,
rend les %d cellules avec %d desaccord de couplage ecrit, %d d'eligibilite, et un plus grand ecart de %s sur les grandeurs comparees
(e_bord, etendues, logarithmes des largeurs et des densites, pas).""" % (COMMUNE, A_["cellules"], A_["desaccords"]["g"],
                                                                         A_["desaccords"]["eligible"], sci(pg)))

titre("4. LA TABLE GELEE DES SIX CELLULES (chaine seule, aucune 2D)")
par("""Par chaine_cellules_pont_machine1_v1.py et le bloc chaine_pont_bloc_machine1_v1.py, qui redonnent la table de la premiere partie
aux six cellules avec un ecart de %g. G3* : plateau de la largeur au vide (ordre 3). Les deux etendues sont celles des dix-huit
variantes de l'absorbeur adapte. Le pas est ln rho_2 - ln rho_3.""" % CI["table_ecart_max"])
brut("    cellule  m_bord  e_bord   r_c   G3*          etendue   etendue du    |pas| au",
     "                                                 au vide   lisse, au     plus",
     "                                                           plus")
for nom in NOMS:
    c = C[nom]
    brut("    %-7s  %d       %.4f   %d    %s   %.4f    %.4f        %.4f" % (nom, c["m_bord"], c["e_bord"], c["r_c"], sci(math.exp(c["ln_G3"]), 4),
         c["etendue_vide"], max(c["etendue_rho3"]), max(abs(v) for v in c["pas_2_3"])))
par("ln (rho_3 |delta|), le lisse d'ordre 3 du site 0 aux douze ecarts x (en |delta|, du cote oppose au desaccord) :")
brut("    x      " + "  ".join("%-7s" % n for n in NOMS))
for i, x in enumerate(X):
    brut("    %-5s  " % ("%g" % x) + "  ".join("%7.2f" % (C[n]["ln_rho3"][i] + math.log(abs(C[n]["delta"]))) for n in NOMS))
par("Le pas de l'ordre 2 a l'ordre 3, aux memes ecarts :")
brut("    x      " + "  ".join("%-7s" % n for n in NOMS))
for i, x in enumerate(X):
    brut("    %-5s  " % ("%g" % x) + "  ".join("%+7.4f" % C[n]["pas_2_3"][i] for n in NOMS))
par("""Ces nombres sont ceux du poste de machine 1. Machine 2 les recalcule sur BOCAL4 par le meme script ; c'est SON fichier que ses
feuilles lisent au run. A la premiere partie, nos deux chaines s'accordaient a %s pres sur les logarithmes des densites.""" % sci(A_["plus_grand_ecart_absolu"]["ln_rho3"]))

titre("5. L'INSTRUMENT")
par("Deux sondes, qui calculent en 2D et ne lisent pas la chaine ; trois feuilles, qui ne calculent aucune 2D. Aucun tirage aleatoire.")
par("""5.1 SONDE DE DENSITE (sonde_densite_2d_pont_machine1_v1.py, %s). Pour une cellule et un absorbeur : hamiltonien, absorbeurs et
lecture du vide du bloc "LECTEUR CREUX" depose ; geometrie du lecteur, r_c = 2 (m + max(8, m)) + 2 ; absorbeurs A (F2, bord r_c, 80
couches), B (F2, r_c, 100), C (F1, r_c, 100), D (F2, r_c + 10, 80) ; boite = bord + couches. Douze barreaux, eta_k = |delta| 2^(-k),
k = -3 a 8. A chaque barreau : l'etat-vide est lu (E_v, largeur, poids w0 du site (0, 0)) ; puis, a chacun des douze ecarts x, (A -
E) y = e_(0,0) avec A = H0 + diag - i eta W et E = E_v - x delta, et rho = (eta / pi) somme_j W_j |y_j|^2. Derivee de la sonde de
l'exploration du 17/11 (95a91f49bb5db12e) ; elle la redonne avec un ecart de %g au point sacrifie (absorbeur %s, k = %d).""" %
    (c_("sonde_densite_2d_pont_machine1_v1.py"), CI["regression_ecart_max"], CI["regression_absorbeur"], CI["regression_k"]),
    retrait="  ", suite="      ")
par("""5.2 FEUILLE DE DENSITE (lecture_densite_2d_pont_machine1_v1.py, %s). Par absorbeur et par ecart, la routine de PLATEAU deposee du
lecteur : parmi les fenetres de cinq barreaux consecutifs, celle de plus petit rapport max / min ; PLATEAU si ce rapport est <= 1.05 ;
valeur = moyenne geometrique des cinq. rho_2D(x) = exponentielle de la mediane des quatre ln rho. L'ecart est LISIBLE si les quatre
absorbeurs ont un plateau et si l'etendue de leurs quatre ln rho est <= 0.02. w0 : mediane sur les absorbeurs de la mediane sur les
barreaux. Elle rend ln R3(x) = ln rho_2D(x) - ln w0 - ln rho_3(x), et ln R2 de meme avec le lisse d'ordre 2.""" % c_("lecture_densite_2d_pont_machine1_v1.py"),
    retrait="  ", suite="      ")
par("""5.3 SONDE DE BOITE FERMEE (sonde_boite_fermee_pont_machine1_v1.py, %s). Ecrite par machine 1 sans recopier celle de machine 2.
Boite N x N sans absorbeur, H = H0 + diag du meme bloc. Niveau-vide : iteration inverse a decalage 0 depuis le site (0, 0) ; E_v et w0
= poids du site (0, 0). Fenetre : 0.05 < x < 8, x = (E_v - E) / delta. DEUX lectures par decalage-inversion (eigsh de scipy,
factorisation creuse d'ordre COLAMD, vecteur de depart fixe), decalages E_v - 2.5 delta et E_v - 5.5 delta ; le nombre de niveaux
demandes double, de 24 a 768, tant que les niveaux trouves ne debordent pas la fenetre des deux cotes. Poids c^2 du site (0, 0) d'un
niveau, lu PAR PARTITION : le vecteur est coupe en dedans I (sites max(a, b) <= r_c) et dehors O ; le dedans est recalcule depuis le
dehors, (H_II - E) psi_I = - H_IO psi_O, resolution dense dans l'ordre naturel des sites ; c^2 = psi_I(0,0)^2 / (|psi_I|^2 +
|psi_O|^2). Le composant BRUT du vecteur d'ARPACK est consigne a cote. Un niveau est FIABLE si ses deux lectures par partition
s'accordent a 2 pour cent.""" % c_("sonde_boite_fermee_pont_machine1_v1.py"), retrait="  ", suite="      ")
par("""5.4 FEUILLE DES BOITES (lecture_boites_pont_machine1_v1.py, %s). PART d'un niveau, en |delta| : y = c^2 / (w0 rho_3(x) |delta|),
rho_3(x) etant le lisse d'ordre 3 calcule directement a l'ecart du niveau (bloc chaine_pont_bloc_machine1_v1.py, %s). SOMME d'une
boite : S = (somme des y) / 7.95, 7.95 etant la largeur de la fenetre en |delta|. COMPTE : n, le nombre de niveaux de la fenetre. Le
compte d'une boite est VALIDE si son niveau-vide est suivi (poids du site (0, 0) >= 0.5, residu <= 1e-9) et si ses deux lectures
debordent la fenetre et trouvent les memes niveaux (energies a 1e-9 pres). Une
boite est LISIBLE si son compte est valide et si ses niveaux non fiables portent au plus 5 pour cent de la somme des y.""" %
    (c_("lecture_boites_pont_machine1_v1.py"), c_("chaine_pont_bloc_machine1_v1.py")), retrait="  ", suite="      ")
par("""5.5 FEUILLE DE VERDICT (verdict_pont_machine1_v1.py, %s). Applique la section 7 aux sorties des deux feuilles. Ses constantes sont
celles de la section 7 ; en cas de desaccord entre ce texte et la feuille, c'est ce TEXTE qui fait foi.""" % c_("verdict_pont_machine1_v1.py"),
    retrait="  ", suite="      ")
par("""5.6 CE QUI EST JOUE, par cellule : la sonde de densite aux quatre absorbeurs, douze barreaux chacun ; la sonde de boite fermee
a VINGT cotes, groupe UN = 180 a 189, groupe DEUX = 291 a 300, chaque cote une fois. Puis les feuilles. Les cotes peuvent etre
repartis entre plusieurs processus ; une boite interrompue se rejoue telle quelle ; rien d'autre ne se rejoue.""", retrait="  ", suite="      ")

titre("6. QUALIFICATION DE L'INSTRUMENT AU POINT SACRIFIE (w2 = 101/50, hors chaine)")
par("""Attendus ecrits avant les sorties : attendu_qualification_instruments_pont_machine1_v1.txt (%s ; son heure ecrite est fausse,
rectificatif %s : le fichier est date de 10 h 05, la premiere sortie de 10 h 11) et attendu_groupe_UN_point_sacrifie_machine1_v1.txt
(%s). Juges par bilan_qualification_pont_machine1_v1.py.""" % (c_("attendu_qualification_instruments_pont_machine1_v1.txt"),
    c_("rectificatif_heure_attendu_qualification_machine1_v1.txt"), c_("attendu_groupe_UN_point_sacrifie_machine1_v1.txt")))
par("DENSITE. ln R3 et ln R2 aux douze ecarts, aux trois profondeurs (3 barreaux : sorties de l'exploration du 17/11, remises au format) :")
brut("    x      3 barreaux         4 barreaux         5 barreaux",
     "           ln R3    ln R2     ln R3    ln R2     ln R3    ln R2")
for i, x in enumerate(X):
    brut("    %-5s  " % ("%g" % x) + "   ".join("%+.4f  %+.4f" % (BQ["SA%d" % m]["ln_R3"][i], BQ["SA%d" % m]["ln_R2"][i]) for m in (3, 4, 5)))
s3, s4, s5 = BQ["SA3"], BQ["SA4"], BQ["SA5"]
par("""Lisibles : %d, %d et %d ecarts sur 12. Plus grand |ln R3| : %.4f, %.4f, %.4f. Plus grande etendue entre absorbeurs : %.4f, %.4f,
%.4f. A1 (4 barreaux lisibles partout) : %s. A2 (5 barreaux lisibles partout) : %s. A3 (|ln R3| <= 0.02 partout a 4 et 5 barreaux) :
%s, a 5 barreaux et x = 8. A4 (R3 decroit avec x) : %s : a 8 |delta| le residu de l'ordre 3 CHANGE DE SIGNE avec la profondeur (%+.4f,
%+.4f, %+.4f) et grandit a 5 barreaux. L'ordre 3 est plus pres de la 2D que l'ordre 2 a chaque ecart x >= 5 aux trois profondeurs ; a
x = 4 et 3 barreaux il ne l'est que de %.4f.""" % (s3["ecarts_lisibles"], s4["ecarts_lisibles"], s5["ecarts_lisibles"], s3["ln_R3_max_abs"],
    s4["ln_R3_max_abs"], s5["ln_R3_max_abs"], s3["etendue_absorbeurs_max"], s4["etendue_absorbeurs_max"], s5["etendue_absorbeurs_max"],
    "TIENT" if BQ["A1"]["tient"] else "TOMBE", "TIENT" if BQ["A2"]["tient"] else "TOMBE", "TIENT" if BQ["A3"]["tient"] else "TOMBE",
    "TIENT" if BQ["A4"]["tient"] else "TOMBE", s3["ln_R3"][-1], s4["ln_R3"][-1], s5["ln_R3"][-1], s3["marge_x4"]))
vd = [BQ["SA%d" % m]["vide_ln_chaine3_sur_2d"] for m in (3, 4, 5)]
par("""Au vide, a cote : ln (chaine d'ordre 3 / 2D) vaut de %+.5f a %+.5f aux absorbeurs A, B, D, et de %+.5f a %+.5f a l'absorbeur C.""" %
    (min(v[a] for v in vd for a in "ABD"), max(v[a] for v in vd for a in "ABD"), min(v["C"] for v in vd), max(v["C"] for v in vd)))
b1, b2, b3, b4, ac = BQ["B1"], BQ["B2"], BQ["B3"], BQ["B4"], BQ["accords"]
par("""BOITE FERMEE, contre les niveaux publies par machine 2 (%d boites : cotes 190, 200, 209 et 300 a 3 barreaux, 300 a 4 et a 5
barreaux). B1 (memes niveaux) : %s ; meme compte partout, ecarts au vide egaux a %s |delta| pres. B2 (ma lecture brute contre ses
niveaux fiables, a 2 pour cent) : %s, plus grand ecart %.4f. B3 (partition contre brut a 1e-3 pres a 3 barreaux) : %s, de peu : %s au
cote %d, sur %d boites ; mediane %s. B4 (au niveau que machine 2 dit non fiable, 5 barreaux, cote 300, x = %.3f : mes deux lectures
par partition d'accord a 1e-3) : %s ; elles s'accordent a %s pres, quand mes deux lectures brutes different de %.4f.""" % (b1["boites"],
    "TIENT" if b1["tient"] else "TOMBE", sci(b1["ecart_x_max"]), "TIENT" if b2["tient"] else "TOMBE", b2["ecart_max_brut_contre_ses_fiables"],
    "TIENT" if b3["tient"] else "TOMBE", sci(b3["max"]), b3["cote_du_max"], b3["boites"], sci(b3["mediane"]), b4["x"],
    "TIENT" if b4["tient"] else "TOMBE", sci(b4["partition_a_b"]), b4["brut_a_b"]))
par("""Au cote 300, les deux lectures par partition s'accordent a %s, %s et %s pres a 3, 4 et 5 barreaux ; les deux lectures brutes a
%s, %.4f et %.4f. Sur toutes les boites jouees, la lecture par partition refaite au rayon r_c + 6 s'ecarte de %s au plus.""" %
    (sci(ac["3"]["partition_a_b_max"]), sci(ac["4"]["partition_a_b_max"]), sci(ac["5"]["partition_a_b_max"]), sci(ac["3"]["brut_a_b_max"]),
     ac["4"]["brut_a_b_max"], ac["5"]["brut_a_b_max"], sci(BQ["rayon_max_toutes_boites"])))
par("""ECART A MON ATTENDU, DECLARE. L'attendu disait : "Si B3 ou B4 tombe, la lecture du gel sera la lecture brute a deux decalages".
B3 est tombe, de peu. Je ne suis PAS cette clause : elle etait mal concue. B3 compare la partition au brut, et ce que les pieces
montrent est que c'est le brut qui flotte (jusqu'a %.4f entre mes deux lectures brutes, et %.1f pour cent entre celles de machine 2 au
meme niveau), pas la partition. La lecture du gel est la lecture PAR PARTITION. Machine 2 peut le refuser.""" %
    (ac["5"]["brut_a_b_max"], 100.0 * abs(b4["y_m2"][0]["y2"] / b4["y_m2"][0]["y1"] - 1.0)))
u = BQ["UN"]; c3 = BQ["cote_300"]
par("""GROUPE UN au point sacrifie, 3 barreaux, dix boites des cotes 180 a 189. U1 (n moyen de 8 a 11, lu sur le compte des niveaux
libres) : %s : n moyen %.1f (de %d a %d). Le compte ne suit PAS l'escalier des niveaux libres ; il suit le cote. U2 (moyenne de S dans
[0.90, 1.15]) : %s : %.4f +- %.4f. U3 (ecart-type de S de 0.08 a 0.20) : %s : %.4f. U4 (tous les niveaux fiables) : %s. Compte reduit n /
(cote x 7.95 x |delta|) : %.3f ; au cote 300, une boite par profondeur : n = %d, %d, %d, soit %.3f ; S = %.4f, %.4f, %.4f.""" %
    ("TIENT" if BQ["U1"]["tient"] else "TOMBE", u["n_moyen"], u["n_min"], u["n_max"], "TIENT" if BQ["U2"]["tient"] else "TOMBE", u["S_moyenne"],
     u["S_erreur"], "TIENT" if BQ["U3"]["tient"] else "TOMBE", u["S_ecart_type"], "TIENT" if BQ["U4"]["tient"] else "TOMBE", u["compte_reduit"],
     c3["3"]["n"], c3["4"]["n"], c3["5"]["n"], c3["3"]["compte_reduit"], c3["3"]["S"], c3["4"]["S"], c3["5"]["S"]))
ea = open(QU + "/essai_aveugle_delta_negatif_machine1_v1.log", encoding="ascii").read()
m_ea = re.search(r"^w2 d'essai : (\S+) \(delta = (\S+), non candidat\), 3 barreaux", ea, re.M)
assert m_ea and "ESSAI A L'AVEUGLE : le chemin delta < 0 s'execute." in ea and " : NON" not in ea and ea.count("code de sortie 0") == 2
par("""ESSAI A L'AVEUGLE DU CHEMIN delta < 0. Aucune 2D hors du vide n'a ete regardee a delta < 0, a aucun w2 ; c'est voulu, et cela
laissait les deux sondes jamais executees de ce cote. Elles l'ont ete une fois, a w2 = %s (delta = %s, non candidat), 3 barreaux : la
densite a un absorbeur et un barreau, une boite de cote 60, dans un dossier temporaire detruit ensuite. Seuls les deux codes de sortie
et %d booleens de forme ont ete lus (desaccord negatif, vide suivi, densites finies et positives, fenetre debordee, memes niveaux aux
deux lectures, ecarts dans la fenetre, poids positifs, niveaux fiables) : tous vrais. Aucun nombre de ces sorties n'a ete imprime ni
garde (essai_aveugle_delta_negatif_machine1_v1.py et son journal).""" % (m_ea.group(1), m_ea.group(2), ea.count(" : oui")))
rs = REP["cellules"]["SA3"]
par("""REPETITION de la feuille de verdict sur ces pieces (ce n'est pas un verdict ; le groupe DEUX n'y a qu'une boite) : a 3 barreaux,
(L) %s, pire ln R3 %+.4f ; (S) %s, %.4f +- %.4f ; (C) %s, comptes reduits %.3f et %.3f, rapport %.3f. A 4 et 5 barreaux : (L) %s et %s.""" %
    (rs["L"]["verdict"], rs["L"]["pire_ln_R3"], rs["S"]["verdict"], rs["S"]["moyenne"], rs["S"]["erreur"], rs["C"]["verdict"],
     rs["C"]["compte_reduit"]["UN"], rs["C"]["compte_reduit"]["DEUX"], rs["C"]["rapport"], REP["cellules"]["SA4"]["L"]["verdict"],
     REP["cellules"]["SA5"]["L"]["verdict"]))
par("""Cout sur le poste de machine 1 (2 coeurs, trois calculs de front) : densite, de %.0f a %.0f s par absorbeur a 4 et 5 barreaux ;
boite fermee, %.0f s en moyenne aux cotes 180 a 189, de %.0f a %.0f s au cote 300, pic de memoire %.1f Go.""" % (min(durees), max(durees),
    u["secondes_par_boite"], min(ac[m]["secondes"] for m in "345"), max(ac[m]["secondes"] for m in "345"), max(pics) / 1000.0))

titre("7. LES ENONCES (la cellule pour unite)")
par("""(L) LE LISSE. Une cellule est LISIBLE pour (L) si au moins 10 de ses 12 ecarts le sont (5.2). Elle TIENT si, a chaque ecart
lisible, |ln R3(x)| <= 0.05 : la chaine d'ordre 3 rend la densite 2D du site (0, 0) sous absorbeur a 5 pour cent pres, de 0.05 a 8
|delta| de l'energie du vide.""", retrait="  ", suite="      ")
par("""(L2) L'ORDRE. Une cellule lisible pour (L) TIENT si, a chaque ecart lisible x >= 5, |ln R3| < |ln R2| : l'ordre 3 est plus pres
de la 2D que l'ordre 2.""", retrait="  ", suite="      ")
par("""(S) LA SOMME. Une cellule est LISIBLE pour (S) si chacun de ses deux groupes compte au moins 8 boites lisibles (5.4). Elle TIENT
si la moyenne de S sur toutes ses boites lisibles est dans [0.85, 1.15] ET si la moyenne de S de chaque groupe est dans [0.80,
1.20] : la force que l'absorbeur lit comme une densite est la somme des poids que les niveaux de la boite fermee portent, et elle ne
depend pas du cote.""", retrait="  ", suite="      ")
par("""(C) LE COMPTE. Une cellule est LISIBLE pour (C) si chacun de ses deux groupes compte au moins 8 boites de compte valide. Elle
TIENT si, dans chaque groupe, le COMPTE REDUIT (moyenne de n) / (moyenne des cotes x 7.95 x |delta|) est dans [0.33, 0.55] ET si le
rapport de la moyenne de n du groupe DEUX a celle du groupe UN est dans [1.25, 1.85] : le nombre de niveaux qui portent la force
croit avec le cote, comme le cote fois |delta|.""", retrait="  ", suite="      ")
par("""UNE FAMILLE est TENUE si aucune cellule lisible ne tombe et si au moins quatre cellules sont lisibles, dont une au moins par
creneau ; TOMBEE si une cellule lisible tombe ; NON JUGEE sinon. Le verdict est rendu par famille, et par creneau a cote.""")

titre("8. CE QUE VAUT CE QUI NE SE LIT PAS")
par("""Une cellule illisible pour une famille ne compte ni pour ni contre elle. Un ecart illisible n'est pas juge. Une boite dont le
compte n'est pas valide sort de (S) et de (C) ; une boite dont les niveaux non fiables portent plus de 5 pour cent de la somme sort de
(S) et reste dans (C). Aucune boite n'est remplacee par une autre : les vingt cotes sont fixes. Si la barriere d'une cellule ne finit
pas au site m, les sondes refusent : la cellule est illisible pour les quatre familles. Aucune tolerance, aucun cote, aucun absorbeur
ni aucune definition ne change apres lecture du run.""")

titre("9. QUESTIONS POSEES A COTE, SANS JUGEMENT")
par("""(Q1) L'EXCES. Au point sacrifie la somme vaut %.3f +- %.3f sur les 32 boites de machine 2 (cotes 190 a 402) et %.4f +- %.4f sur
les dix boites des cotes 180 a 189. La feuille rend la moyenne de S toutes boites lisibles confondues et son erreur ; l'exces "se
retrouve" si elle depasse 1 de plus de deux erreurs.""" % (RG["somme"], RG["erreur"], u["S_moyenne"], u["S_erreur"]), retrait="  ", suite="      ")
par("""(Q2) LES PARTS SONT-ELLES EGALES. Par groupe, le rapport de la moyenne de 1 / participation a celle de 3 / (n + 2) : 1 pour des
parts tirees d'une loi de Porter-Thomas, moins si elles sont plus egales.""", retrait="  ", suite="      ")
par("""(Q3) LE PONT SANS LA CHAINE. La somme relue avec la densite 2D : chaque y divise par R3 a l'ecart du niveau, ln R3 interpole
lineairement en x entre les ecarts lisibles. Si (L) tombe dans une cellule, c'est cette somme qui dit si la boite fermee et
l'absorbeur s'accordent ; elle n'est pas jugee.""", retrait="  ", suite="      ")
par("""(Q4) LE VIDE. Le plateau de la largeur du vide par absorbeur, contre G3*. C'est la grandeur du gel du vide (delta 102), a deux
w2 qu'il n'a pas joues.""", retrait="  ", suite="      ")

titre("10. CE QUE CHAQUE ISSUE ENGAGE")
par("""(L), (S) et (C) TENUES : le pont tient, aux tolerances dites, sur six cellules neuves ; ce que l'absorbeur lit est la force du
vide repartie sur les niveaux de la boite fermee, dont le nombre croit avec la boite. Cela ne dit rien de la boite infinie, qui reste
une extrapolation, ni de la resonance exacte.""")
par("""(L) TOMBEE, (S) TENUE : la chaine d'ordre 3 ne rend pas la densite hors du vide a 5 pour cent la ou elle tombe ; le pont entre
boite fermee et absorbeur n'est pas atteint, et (Q3) dit ce qu'il vaut sans la chaine.""")
par("""(S) TOMBEE : la densite lue sous absorbeur n'est pas, aux tolerances dites, la force portee par les niveaux de la boite fermee
a ces cotes. La lecture "la largeur sous absorbeur est le taux de fuite du systeme ferme" n'a alors plus d'appui ici ; les resultats
des deltas 100 et 102 restent des resultats sur le systeme sous absorbeur.""")
par("""(C) TOMBEE : le nombre de niveaux ne croit pas comme le cote fois |delta| ; la lecture de machine 1 est fausse la ou elle
tombe, et (S) se lit seule.""")
par("(L2) TOMBEE : l'ordre 3 n'ameliore pas l'ordre 2 hors du vide la ou elle tombe ; (L) se lit seule.")
par("Une famille NON JUGEE n'engage rien. Un creneau qui tient et l'autre qui tombe se disent tels quels.")

titre("11. LES ANNONCES DE LA PLUME (ecrites avant le run)")
par("Probabilite que la cellule tienne, selon moi :")
PR = {"L": (0.85, 0.80, 0.50, 0.95, 0.95, 0.90), "L2": (0.85, 0.85, 0.85, 0.95, 0.95, 0.95), "S": (0.88, 0.85, 0.75, 0.93, 0.90, 0.85),
      "C": (0.75, 0.75, 0.75, 0.90, 0.90, 0.90)}
brut("    famille  " + "  ".join("%-4s" % n for n in NOMS) + "   la famille TENUE")
for fam, tot in (("L", 0.40), ("L2", 0.70), ("S", 0.50), ("C", 0.65)):
    brut("    %-7s  " % ("(%s)" % fam) + "  ".join("%.2f" % p for p in PR[fam]) + "   %.2f" % tot)
par("""Les quatre familles tenues : 0.2. L'issue que je crois la plus probable n'est PAS "tout tient" : c'est (L) qui tombe a MG5, aux
plus grands ecarts, le reste tenant.""")
par("""Pourquoi MG5. Au point sacrifie le residu de l'ordre 3 a 8 |delta| vaut %+.4f a 5 barreaux pour un pas de l'ordre 2 a l'ordre 3
de %.4f ; a MG5 ce pas vaut %.4f. Si le residu suit le pas, il arrive a la tolerance ; s'il suit son carre, il la depasse.""" %
    (s5["ln_R3"][-1], abs(C["SA5"]["pas_2_3"][-1]), abs(C["MG5"]["pas_2_3"][-1])))
par("""PG est presque le point sacrifie (delta = %+.3f contre %+.3f) : ce creneau eprouve la reproductibilite et les profondeurs 4
et 5 en boite fermee, guere plus. L'epreuve a l'aveugle est MG : aucune 2D hors du vide et aucune boite fermee n'ont ete regardees a
delta < 0, a aucun w2.""" % (C["PG3"]["delta"], C["SA3"]["delta"]))
par("""Paris sur les questions : (Q1) la moyenne de S toutes boites confondues est dans [0.99, 1.05], probabilite 0.7 ; l'exces se
retrouve, 0.4. (Q2) le rapport est entre 0.8 et 1.1 dans chaque groupe, 0.7. Une cellule au moins illisible pour (L), 0.15.""")

titre("12. CE QUE MACHINE 2 CERTIFIE")
par("(a) que son tirage, avec la graine %s sur la table commune, rend les six cellules de la section 2 ;" % GRAINE, retrait="  ", suite="      ")
par("""(b) que les sections 5 et 7 suffisent a ecrire les feuilles sans lire celles de machine 1, et que les trois feuilles de
machine 1 font ce que ces sections disent ;""", retrait="  ", suite="      ")
par("""(c) que les deux sondes tournent sur BOCAL4 au point sacrifie et y redonnent les pieces de la section 6 : la densite d'un
absorbeur a 5 barreaux, une boite du groupe UN a 3 barreaux et la boite de cote 300 a 5 barreaux (memes niveaux, memes poids par
partition) ; et ce qu'un run complet y coute ;""", retrait="  ", suite="      ")
par("""(d) la lecture par partition : qu'elle l'accepte comme lecture du gel, ou qu'elle la refuse, et alors pourquoi ; et mon ecart
a ma propre clause (section 6) ;""", retrait="  ", suite="      ")
par("(e) SA table de la section 4, recalculee sur BOCAL4 ;", retrait="  ", suite="      ")
par("""(f) qu'aucune 2D du systeme a fantome n'a ete jouee par elle a w2 = %s ni a w2 = %s depuis sa certification de la premiere
partie.""" % (rang["MG"][3], rang["PG"][3]), retrait="  ", suite="      ")

titre("13. LE RUN, ET LA SUITE")
par("""(1) machine 2 certifie cette piece ; (2) l'operateur donne le feu vert par ecrit ; (3) machine 2 joue une fois, aux six cellules
: 24 sorties de densite, 120 boites ; (4) elle passe ses sorties par les trois feuilles et rend le tout dans un lot, journaux compris
; (5) machine 1 rejoue les trois feuilles sur les sorties de machine 2 ; (6) machine 1 ecrit l'acte, machine 2 contresigne,
l'operateur depose.""")

titre("14. LIMITES, ET ECARTS DECLARES")
for t in (
    """Les tolerances sont de la plume de machine 1 : 0.05 pour (L), [0.85, 1.15] et [0.80, 1.20] pour (S), [0.33, 0.55] et [1.25, 1.85]
    pour (C). Elles sont posees APRES la calibration au point sacrifie et AVANT toute 2D aux cellules tirees.""",
    """Ecart de redaction, declare : ma premiere tolerance pour (L) etait max(0.02, la moitie du pas de l'ordre 2 a l'ordre 3). La
    calibration a 5 barreaux l'aurait fait tomber au point sacrifie (%.4f a x = 8). Je l'ai remplacee par 0.05 partout, la tolerance du
    gel de l'ordre 3 dans son domaine. C'est un desserrement, fait apres avoir vu le point sacrifie et avant d'avoir vu une cellule.""" % s5["ln_R3"][-1],
    """(L2) ne juge que x >= 5 : a x = 4 et 3 barreaux, au point sacrifie, l'ordre 3 ne devance l'ordre 2 que de %.4f.""" % s3["marge_x4"],
    """(C) n'est plus lu sur le compte des niveaux libres : mon attendu U1 est tombe. Le compte reduit n'est calibre qu'a un seul
    |delta| (0.02) ; qu'il vaille pour |delta| = 0.015 et pour l'autre signe est une prediction, pas un acquis.""",
    """La lecture par partition est neuve ; elle n'a jamais ete certifiee. Elle redonne les parts de machine 2 la ou ses deux lectures
    s'accordent.""",
    """(S) est lue avec le lisse de la chaine. Si (L) tombe dans une cellule, (S) y perd son sens et (Q3) la remplace, sans jugement.""",
    """Deux groupes de cotes seulement : la croissance du compte est jugee sur deux points. Cote 300 au plus.""",
    """Le chemin delta < 0 des deux sondes n'a ete execute qu'une fois, a l'aveugle, a un w2 non candidat et sur une petite boite :
    cela dit que le code s'y execute, pas qu'une boite de cote 300 ou une densite a 5 barreaux s'y lisent.""",
    """Le moteur et les blocs sont les memes pour la chaine et pour la 2D, et pour les deux machines : l'accord eprouve la reduction a
    une dimension, les absorbeurs et la boite fermee, pas le moteur. Une seule definition du hamiltonien effectif.""",
    """Rien n'est dit de la duree de vie du systeme ferme, de la boite infinie, de la resonance exacte, ni des w2 non tires."""):
    par("- " + t, retrait="  ", suite="    ")

titre("15. PIECES DE CE LOT (convention B)")
for p in pieces: brut("    %s  %s" % (cp[os.path.basename(p)], os.path.basename(p)))
brut("    (ce script)       construction_gel_pont_partie2_machine1_v1.py")
brut("", "-- FIN gel_pont_partie2_instrument_enonces_pre_enregistrement_v1 --")
txt = "\n".join(l.rstrip() for l in L) + "\n"
txt.encode("ascii")
long_ = [l for l in L if len(l) > 100]; assert not long_, long_
assert "%" not in txt.replace('"%.5e"', ""), [l for l in L if "%" in l]
open(SORTIE, "w", encoding="ascii", newline="\n").write(txt)
print("ecrit : %s ; %d lignes ; canon %s" % (SORTIE, len(L), canon(SORTIE)))
