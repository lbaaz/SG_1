# -*- coding: ascii -*-
"""CONSTRUCTION DE LA PREMIERE PARTIE DU GEL "LARGEUR DU VIDE" : LA REGLE DE TIRAGE ET D'ELIGIBILITE,
et de son POUR_MACHINE2 -- machine 1, v1, 2026-11-16. Chaque nombre est calcule ici depuis les sorties du lot.
Usage : python3 -I -B construction_regle_tirage_vide_machine1_v1.py <dossier des sorties> <clone du registre>
        <dossier du lot de la note sur le vide> <dossier du lot de la note sur la loi d'echelle> <sortie.md>"""
import sys, os, json, math, hashlib, unicodedata, textwrap
from fractions import Fraction as F
D, CLONE, LOT_VIDE, LOT_ECH, SORTIE = sys.argv[1:6]
NOTE_VIDE = os.path.join(LOT_VIDE, "note_machine1_vide_etape_sans_run_2026-11-16_v1.md"); MAN_VIDE = os.path.join(LOT_VIDE, "MANIFESTE_lot_machine1_2026-11-16_vide_etape_sans_run_v1.txt")
NOTE_ECH = os.path.join(LOT_ECH, "note_machine1_loi_echelle_2026-11-16_v1.md"); MAN_ECH = os.path.join(LOT_ECH, "MANIFESTE_lot_machine1_2026-11-16_loi_echelle_etape0_v1.txt")

def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

c = {"moteur": B(CLONE + "/scripts/m17_chaine_v17.py"), "bloc2": B(CLONE + "/scripts/chaine_ordre2_bloc_machine1_v1.py"),
     "bloc3": B(CLONE + "/scripts/ordre3_bloc_machine1_v1.py"), "lecteur": B(CLONE + "/scripts/sonde_lecteur_gel_loi_machine1_v1.py"),
     "tirage": B(CLONE + "/scripts/tirage_machine1_v1.py"), "gel_p1": B(CLONE + "/gels/gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md"),
     "note_vide": B(NOTE_VIDE), "lot_vide": B(MAN_VIDE), "note_ech": B(NOTE_ECH), "lot_ech": B(MAN_ECH)}
assert (c["moteur"], c["bloc2"], c["bloc3"], c["lecteur"], c["tirage"], c["gel_p1"]) == (
    "82a0be882568fe0c", "7cd5977bc27bebc1", "534ba246aa3b8973", "d5cc48f48e37af99", "0f608f8ade6ff378", "b56ca5cb2dd25da1"), c
assert (c["note_vide"], c["lot_vide"], c["note_ech"], c["lot_ech"]) == ("15641e09a351d56d", "c5d8fd0313217569", "8548cc16fb746f56", "408b8a595cad0040"), c
PIECES = ["chaine_adaptee_bloc_machine1_v1.py", "eligibilite_vide_machine1_v1.py", "eligibilite_vide_MG_MP_v1.log", "eligibilite_vide_MG_MP_v1.json",
          "eligibilite_vide_PP_PG_v1.log", "eligibilite_vide_PP_PG_v1.json", "eligibilite_vide_MG_MP_sans_levier_v1.log", "eligibilite_vide_MG_MP_sans_levier_v1.json",
          "eligibilite_vide_PP_PG_sans_levier_v1.log", "eligibilite_vide_PP_PG_sans_levier_v1.json", "lecture_eligibilite_vide_machine1_v1.py",
          "lecture_eligibilite_vide_machine1_v1.log", "eligibilite_candidates_vide_v1.json", "controle_bloc_adapte_machine1_v1.log", "controle_bloc_adapte_v1.json",
          "absorbeur_adapte_v1.json", "tirage_vide_machine1_v1.py", "tirage_vide_machine1_v1_autotest.log", "tirage_vide_machine1_v1_demonstration.log", "faisabilite_profondeur_jumeau_machine1_v1.py",
          "faisabilite_profondeur_jumeau_machine1_v1.log", "faisabilite_profondeur_jumeau_v1.json", "balayage_virginite_machine1_v1.py",
          "balayage_virginite_registre_v1.log", "balayage_virginite_registre_v1.json", "balayage_virginite_poste_v1.log", "balayage_virginite_poste_v1.json"]
cp = {p: B(os.path.join(D, p)) for p in PIECES}
assert cp["absorbeur_adapte_v1.json"] == "75e7e0259b1be1d4"
J = lambda nom: json.load(open(os.path.join(D, nom)))
T = J("eligibilite_candidates_vide_v1.json"); RG = T["regle"]; RS = T["resume"]; AU = T["autre_reglage"]
ORDRE = ("MG", "MP", "PP", "PG"); LIS = [int(x) for x in RG["lisibles"]]; PRO = [int(x) for x in RG["profondes"]]; TOUS = LIS + PRO
assert (LIS, PRO, RG["seuil_etendue"], RG["garde_e_bord"], RG["M_facteur"], len(RG["variantes"]), RG["seuil_flux"], RG["chiffres"]) == ([3, 4, 5, 6], [8, 12, 16], 0.02, 0.7, 4, 18, 1e-15, 100)
cand = {s: T["creneaux"][s]["candidats"] for s in ORDRE}
n_w2 = sum(len(cand[s]) for s in ORDRE); n_cel = sum(len(x["cellules"]) for s in ORDRE for x in cand[s]); assert (n_w2, n_cel) == (T["comptes"]["w2"], T["comptes"]["cellules"]) == (36, 252)
n_el = {s: sum(x["eligible"] for x in cand[s]) for s in ORDRE}
n_pro = {s: sum(y["eligible"] for x in cand[s] for y in x["cellules"] if not y["lisible"]) for s in ORDRE}
n_pro_tot = {s: sum(1 for x in cand[s] for y in x["cellules"] if not y["lisible"]) for s in ORDRE}
inel = [(s, "%.3f" % float(F(x["w2"]))) for s in ORDRE for x in cand[s] if not x["eligible"]]
non_ret = [(s, "%.3f" % float(F(x["w2"])), y["m"]) for s in ORDRE for x in cand[s] for y in x["cellules"] if not y["lisible"] and not y["eligible"]]
et_max = max(RS[str(m)]["etendue_max"] for m in TOUS); et_max_lis = max(RS[str(m)]["etendue_max"] for m in LIS)
poids_min = min(RS[str(m)]["poids_min"] for m in TOUS)
bornes = {s: (min(F(x["w2"]) for x in cand[s]), max(F(x["w2"]) for x in cand[s])) for s in ORDRE}
auto = open(os.path.join(D, "tirage_vide_machine1_v1_autotest.log"), encoding="ascii").read(); assert "AUTOTEST : TIENT" in auto
ex = [l for l in auto.split("\n") if l.startswith('sha256("DEMONSTRATION|MG|0")')][0]
CB = J("controle_bloc_adapte_v1.json"); assert CB["tient"]
FA = J("faisabilite_profondeur_jumeau_v1.json")["cas"]; assert [x["m_bord_du_vide"] for x in FA] == PRO and all(x["suivies"] == x["lectures"] for x in FA)
JV = lambda nom: json.load(open(os.path.join(LOT_VIDE, nom)))
TV = JV("temoin_lecteur_vide_v1.json")["cas"]
assert B(os.path.join(LOT_VIDE, "absorbeur_adapte_v1.json")) == cp["absorbeur_adapte_v1.json"]
vu_36 = max(b["ordres"]["3"]["etendue"] for b in JV("absorbeur_adapte_v1.json")["B"] if 3 <= b["m_cible"] <= 6)
vu_prof = max(q["etendue"] for q in JV("carte_adaptee_v1.json")["points"] if (q["n1"], q["n2"]) == (0, 0) and q["m_cible"] in (8, 12, 16) and abs(q["delta"]) <= 0.02 and not q["instable_adapte"])
vu = max(vu_36, vu_prof); assert vu < 0.5 * RG["seuil_etendue"]
EJ = JV("controle_joues_absorbeur_v1.json")["etats"]
def med(v):
    v = sorted(v); n = len(v); return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])
joues_d = abs(med([e["etoile_moins_depose"] for e in EJ])); joues_q = med([abs(e["ln_q3_depose"]) for e in EJ])
prof_ln = min(q["ln_Phi_lecteur"] for q in JV("procede_lecteur_profond_v1.json")["points"])
BR, BP_ = J("balayage_virginite_registre_v1.json"), J("balayage_virginite_poste_v1.json")
assert not BR["traces"] and not BR["etiquettes_00"] and not BR["deltas"] and not BP_["traces"] and not BP_["par_construction"] and BP_["hors"] == ["gel_vide"]
assert BR["json_non_lus"] == 0 and BP_["json_non_lus"] == 0
assert all(("/lot/" in q or "/lot2/" in q or "/sorties/" in q) for q in BP_["deltas"])
par_piece = {}
for q, ws in BP_["deltas"].items():
    par_piece.setdefault(os.path.basename(q), set()).update(ws)
deja = sorted(set(w for ws in par_piece.values() for w in ws))
groupes = {}
for nom, ws in par_piece.items():
    groupes.setdefault(" et ".join(sorted(ws)), []).append(nom)
assert all(("/lot/" in p or "/lot2/" in p or "/sorties/" in p) for p in BP_["etiquettes_00"])
tete = os.popen("git -C %s rev-parse --short HEAD" % CLONE).read().strip(); assert tete == "dee73bd", tete
n_suivis = int(os.popen("git -C %s ls-files | wc -l" % CLONE).read()); assert n_suivis == BR["lus"], (n_suivis, BR["lus"])

L = []
def T_(s=""): L.append(s)
def P(s, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
def e1(x): return "%.1e" % x

T_('GEL "LARGEUR DU VIDE" -- PREMIERE PARTIE : LA REGLE DE TIRAGE ET D\'ELIGIBILITE DES CELLULES')
T_("PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-16.")
T_("A CERTIFIER PAR MACHINE 2 AVANT QUE L'OPERATEUR DONNE LA GRAINE.")
T_()
T_("0. STATUT")
P("""Cette piece fixe COMMENT les cellules du gel seront tirees et QUAND un tirage est admis. Elle ne fixe ni les enonces juges, ni les
tolerances, ni les probabilites, ni l'instrument : c'est la seconde partie, ecrite apres le tirage sur les chaines seules, et certifiee
avant tout run.""")
P("""L'objet du gel : la largeur de l'etat que porte le site (0, 0) du systeme a fantome, "le vide", lue en 2D par le lecteur creux, et ce
que la chaine a une dimension en predit.""")
P("""Ouverture, selon machine 1 : a la fin de la note sur le vide (%s, hors chaine, classe 3), machine 1 a propose ce gel ; l'operateur a
ecrit "on gele et on avance !" (16/11/2026, 12 h 19). A l'operateur de l'attester ou de le dementir.""" % c["note_vide"])
P("""E19. Selon ses pieces (section 9), machine 1 n'a fait aucun calcul 2D du systeme a fantome, dense ou creux, a un w2 candidat, et
n'a lu aucune largeur 2D de l'etat porte par (0, 0) du systeme a fantome a AUCUN w2, candidat ou non. Aucune des deux machines ne fera
l'un avant la certification croisee de la seconde partie, ni l'autre avant le run. Machine 2 dit ce qu'il en est pour elle (section 10,
d). Tout ce que cette piece calcule est une chaine a une dimension, sauf la section 8, qui lit le JUMEAU SANS FANTOME (signe +1) a un w2
qui n'est pas candidat.""")
T_()
T_("1. SOURCES (convention B)")
for canon, quoi in ((c["moteur"], "scripts/m17_chaine_v17.py (registre %s), le moteur" % tete),
                    (c["bloc2"], "scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2"),
                    (c["bloc3"], "scripts/ordre3_bloc_machine1_v1.py (registre), le bloc d'ordre 3"),
                    (c["lecteur"], "scripts/sonde_lecteur_gel_loi_machine1_v1.py (registre), le lecteur creux ; lu ici au jumeau seulement"),
                    (c["gel_p1"], "gels/gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md (registre) : la regle de tirage dont celle-ci reprend la forme"),
                    (c["tirage"], "scripts/tirage_machine1_v1.py (registre), le tirage dont celui de ce lot derive"),
                    (c["note_vide"], "note_machine1_vide_etape_sans_run_2026-11-16_v1.md (lot %s), sections 3, 6 et 7 : l'absorbeur adapte et la proposition" % c["lot_vide"]),
                    (c["note_ech"], "note_machine1_loi_echelle_2026-11-16_v1.md (lot %s) : la loi d'echelle et la regle de barriere a la limite" % c["lot_ech"])):
    P(canon + " " + quoi, 4, 22)
P("""Les deux derniers lots sont HORS REGISTRE et machine 1 etait seule a les detenir : ils voyagent avec ce lot, dans la meme enveloppe.""")
T_()
T_("2. LES CRENEAUX ET LES CELLULES")
P("""Quatre creneaux, neuf w2 candidats chacun. Les w2 candidats sont au millieme ; les centiemes en sont exclus, et |w2 - 2| < 0.02.""")
noms = {"MG": "delta < 0, grand", "MP": "delta < 0, petit", "PP": "delta > 0, petit", "PG": "delta > 0, grand"}
for s in ORDRE:
    a, b = bornes[s]
    T_("    %-2s  %-17s delta de %+.3f a %+.3f   w2 = %.3f a %.3f   %d valeurs" % (s, noms[s], float(a) - 2, float(b) - 2, float(a), float(b), len(cand[s])))
P("""Sept PROFONDEURS de barriere m, chacune avec son rapport kappa_m, constante de ce gel :""")
T_("    LISIBLES   " + "   ".join("m = %d : %s" % (m, RG["kappa"][str(m)]) for m in LIS))
T_("    PROFONDES  " + "   ".join("m = %d : %s" % (m, RG["kappa"][str(m)]) for m in PRO))
P("""Une CELLULE est un couple (w2, m). Son couplage est""")
T_("        g = kappa_m x |w2 - 2| x P / X(w2) ,")
T_("        X(w2) = X_saut_reel(P, 2, 1, 0, 0, w2) du moteur, P = 5,")
P("""calcule en double precision puis ARRONDI a six chiffres significatifs (le format "%.5e" de Python) : le couplage de la cellule EST le
nombre decimal ainsi ecrit. kappa est le rapport du saut au pied de l'echelle, t_0 = g X(w2) / P, au desaccord |w2 - 2|. Les kappa_m
sont, a trois chiffres, le milieu geometrique de l'intervalle de kappa ou la barriere de l'etat (0, 0), a la limite du desaccord nul,
finit au site m (note sur la loi d'echelle) ; ce gel fige les decimales, pas la derivation.""")
P("""Un tirage donne un w2 par creneau, donc seize cellules lisibles et au plus douze cellules profondes, nommees par le creneau et la
profondeur : MG3, MG4, MG5, MG6, MG8, MG12, MG16, et de meme pour MP, PP, PG.""")
T_()
T_("3. LE TIRAGE")
P("""Le w2 du creneau s au rang r est l'element de numero""")
T_('        int( sha256("<graine>|<s>|<r>") ecrit en hexadecimal, 16 )  modulo  n_s')
P("""de la liste CROISSANTE des n_s w2 candidats du creneau, numerotee a partir de 0. La chaine hachee est codee en ASCII ; s vaut MG, MP,
PP ou PG ; r s'ecrit en decimal, sans zero devant ; la barre verticale est le caractere 124.""")
P("""LA GRAINE est une suite de chiffres (0 a 9), d'au moins six chiffres, donnee par L'OPERATEUR, par ecrit, aux deux machines, APRES la
certification de cette piece et apres que la table commune de la section 5 existe. Elle est reportee telle quelle, zeros de tete compris,
dans la seconde partie. Ni machine 1 ni machine 2 ne la choisit, ne la propose, ni ne la commente avant de l'avoir recue.""")
P("""Chaque machine tire par SON code. Exemple de controle, sur une graine de demonstration qui n'est pas une suite de chiffres et ne peut
donc pas etre la graine :""")
T_("    " + ex)
T_()
T_("4. L'ELIGIBILITE D'UNE CELLULE (chaine seule, aucune 2D)")
P("""4.1 La barriere : sites = barriere(0, 0, w2, g, avec Sigma2) du moteur ; m_bord = son dernier site ; e_bord = |m_bord delta +
Sigma2(m_bord) - Sigma2(0)|, avec delta = w2 - 2.""", 2, 6)
P("""4.2 Les tables : tables_ordre2(0, 0, w2, g, sites, M_facteur %d) puis tables_ordre3, des blocs deposes. Par site m de l'echelle :
le decalage S_m, le saut du premier ordre t_m (de m a m + 1), le saut au second voisin U_m, et a l'ordre 3 la correction T3_m du saut
et les sauts W3_m (de m a m + 3) et W5_m (de m a m + 5).""" % RG["M_facteur"], 2, 6)
P("""4.3 La chaine d'ordre 3 sous ABSORBEUR ADAPTE, variante (a, c, L). debut = m_bord + c. Les sites vont du premier site des tables
(m_min) au site debut + L. Matrice symetrique complexe : sur la diagonale, m delta + S_m - S_0 - i W_m ; hors diagonale, t_m + T3_m
entre m et m + 1, U_m entre m et m + 2, W3_m entre m et m + 3, W5_m entre m et m + 5. L'absorbeur :""", 2, 6)
T_("        W_m = a |t_m| ((m - debut) / L)^2   pour debut < m <= debut + L ,   0 ailleurs.")
P("""Dix-huit variantes : a = 1, 2, 4 ; c = 6, 8, 10 ; L = 16, 24. Seuls l'absorbeur et la longueur different de la chaine d'ordre 3
du bloc depose.""", 6)
P("""4.4 La largeur d'une variante : Gamma = -2 Im(E), E etant la valeur propre de cette matrice dont le vecteur propre, norme, porte
le plus grand poids sur le site 0. C'est une propriete de la matrice : chaque machine la calcule par sa methode. La double precision ne
la rend pas sous environ 1e-16 |delta| ; machine 1 la lit par le flux tant que Gamma / |delta| > %s et, en dessous, reprend la valeur
propre en precision arbitraire (%d chiffres) sur la meme matrice.""" % ("%.0e" % RG["seuil_flux"], RG["chiffres"]), 2, 6)
P("""4.5 Le PLATEAU G3* est l'exponentielle de la mediane des dix-huit ln Gamma (la moyenne des deux valeurs centrales) ; l'ETENDUE est
le plus grand moins le plus petit des dix-huit ln Gamma. Elle est indefinie si l'une des largeurs n'est pas strictement positive.""", 2, 6)
P("""4.6 La cellule (w2, m) est ELIGIBLE si : (i) m_bord = m ; (ii) e_bord < %s ; (iii) l'etendue est definie et <= %s.""" % (RG["garde_e_bord"], RG["seuil_etendue"]), 2, 6)
P("""4.7 Un w2 candidat est ELIGIBLE si ses quatre cellules LISIBLES le sont. Une cellule PROFONDE est RETENUE si elle est eligible ;
elle ne decide pas de l'eligibilite du w2. Une cellule profonde non retenue n'est pas jouee, et c'est dit.""", 2, 6)
P("""4.8 D'ou viennent les nombres. %s est la garde du domaine du gel "ordre 3" depose. Le seuil %s et la condition (i) sont poses ici,
APRES la note sur le vide, qui a vu des etendues de %.4f au plus a ses points de 3 a 16 barreaux, et AVANT d'avoir calcule une seule
cellule sous cette regle. Les deux notes de ce jour avaient deja calcule, en chaine seule et a d'autres couplages que ceux des cellules,
%d w2 qui sont des candidats : %s (section 9). Les profondeurs, les kappa_m et les dix-huit variantes viennent de la note sur le vide.
Aucun de ces nombres ne sera regle ensuite.""" % (RG["garde_e_bord"], RG["seuil_etendue"], vu, len(deja), ", ".join(deja)), 2, 6)
T_()
T_("5. LA TABLE COMMUNE, AVANT LA GRAINE")
P("""Chaque machine calcule par SA chaine l'eligibilite des %d cellules candidates (%d w2) AVANT que la graine existe. La table de
machine 1 est en section 7. Machine 2 rend la sienne avec sa certification. LA TABLE COMMUNE est leur ET : un w2 candidat y est eligible
si et seulement s'il l'est dans les deux tables ET si les couplages ecrits de ses sept cellules sont les memes dans les deux ; une
cellule profonde y est retenue si et seulement si elle l'est dans les deux. Elle ne depend d'aucune graine. Un desaccord entre les deux
tables est dit dans la certification ; il n'arrete pas le gel.""" % (n_cel, n_w2))
P("""Format d'une table : JSON, creneaux -> <nom du creneau> -> candidats -> liste de {"w2": "<fraction irreductible>", "eligible": true
ou false, "cellules": liste de {"m": <entier>, "g": "<le decimal a six chiffres>", "eligible": true ou false}}.""")
T_()
T_("6. LA REGLE DES RANGS")
P("""Pour chaque creneau, dans l'ordre MG, MP, PP, PG et independamment : rang 0 ; si le w2 tire n'est pas eligible dans la table
commune, rang 1, et ainsi de suite, pour le CRENEAU ENTIER (jamais cellule par cellule). Au plus cinq rangs, de 0 a 4. Si un creneau n'a
pas de w2 eligible en cinq rangs : PAS DE GEL, et on le dit. Un meme w2 peut sortir a deux rangs ; il n'est pas retire de la liste.""")
P("""Si les deux machines ne tirent pas les memes cellules, avec les memes couplages ecrits, a partir de la meme graine et de la meme
table commune : PAS DE GEL tant que l'ecart n'est pas explique par ecrit, et la graine n'est pas changee.""")
T_()
T_("7. LA TABLE DE MACHINE 1 (%d cellules)" % n_cel)
P("""Par cellule : l'etendue de la chaine d'ordre 3 sous l'absorbeur adapte. Les couplages ecrits sont dans la table JSON
(eligibilite_candidates_vide_v1.json, %s).""" % cp["eligibilite_candidates_vide_v1.json"])
for s in ORDRE:
    T_("  creneau %s : %d w2 eligibles sur %d ; cellules profondes retenues : %d sur %d" % (s, n_el[s], len(cand[s]), n_pro[s], n_pro_tot[s]))
    for x in cand[s]:
        T_("    %.3f  %s  %s" % (float(F(x["w2"])), "  ".join("m%d %s%s" % (y["m"], ("%.4f" % y["etendue"]) if y.get("etendue") is not None else "----", "" if y["eligible"] else " !") for y in x["cellules"]),
                               "ELIGIBLE" if x["eligible"] else "INELIGIBLE"))
P("""Un point d'exclamation marquerait une cellule ineligible : %s. Par profondeur, sur les %d w2 :""" % ("il n'y en a aucune" if not (inel or non_ret) else "%d w2 ineligibles, %d cellules profondes non retenues" % (len(inel), len(non_ret)), n_w2))
T_("    m    barreaux   etendue   e_bord   plus grande   plateau predit G3*   methode")
T_("         trouves    max       max      boite         de ... a ...         de machine 1")
for m in TOUS:
    r = RS[str(m)]; assert r["m_bord"] == [m]
    T_("    %-4d %-10s %-9s %-8s %-13d %-20s %s" % (m, "%d" % r["m_bord"][0], "%.4f" % r["etendue_max"], "%.3f" % r["e_bord_max"], r["N_max"], "%s a %s" % (e1(r["G_min"]), e1(r["G_max"])),
                                                  {"fl": "flux", "mp": "precision arbitraire"}["/".join(r["methodes"])]))
P("""La plus grande etendue est %.4f (%.4f aux cellules lisibles) pour un seuil de %s : l'eligibilite ne trie rien ici, et le tirage est
donc uniforme sur les candidats. Le plus petit poids du site 0 dans l'etat lu est %.4f. La plus grande boite du lecteur serait N = r_c +
100, avec r_c = 2 (m_bord + max(8, m_bord)) + 2, la regle du depot sans graine. Le meme calcul sous l'autre reglage de numpy de machine 1
(sans le levier NPY_DISABLE_CPU_FEATURES) : %d eligibilite changee, %d couplage ecrit change, plus grand ecart sur ln G3 %s.""" % (
    et_max, et_max_lis, RG["seuil_etendue"], poids_min, AU["eligibilites_changees"], AU["couplages_changes"], ("%.1e" % AU["ecart_ln_G3_max"]) if AU["ecart_ln_G3_max"] else "0"))
P("""Controle du bloc de l'absorbeur adapte contre la piece de la note sur le vide, a w2 = 99/50 et 101/50 qui ne sont pas candidats :
%d comparaisons, plus grand ecart %s.""" % (CB["comparaisons"], e1(CB["pire_ecart"])))
T_()
T_("8. FAISABILITE DE LA LIGNE PROFONDE (jumeau sans fantome, w2 non candidat)")
P("""Le lecteur depose, lu tel quel, au JUMEAU H+ (signe +1 : aucune echelle resonante, la largeur n'y est fabriquee que par l'absorbeur),
a w2 = 101/50, a la geometrie qu'aurait une cellule profonde ; absorbeurs A et B (la plus grande boite), barreaux k = -3, 3, 8.""")
T_("    m    g            r_c   boites N     lectures   duree   memoire   plus grande largeur")
T_("                                         suivies            max       du jumeau")
for x in FA:
    Ns = sorted(v["N"] for v in x["absorbeurs"].values())
    T_("    %-4d %-12s %-5d %-12s %-10s %-7s %-9s %s" % (x["m_bord_du_vide"], "%.5e" % x["g"], x["r_c"], "%d et %d" % (Ns[0], Ns[-1]), "%d sur %d" % (x["suivies"], x["lectures"]),
                                                       "%.0f s" % x["duree_totale_s"], "%.0f Mo" % x["memoire_max_Mo"], e1(x["plus_grande_largeur"])))
P("""A la geometrie de cellules de %s barreaux, la note sur le vide avait mesure, au jumeau aussi, de %.0f a %.0f s pour les %d lectures
d'une cellule (boites de %d a %d au plus), et une largeur du jumeau de %s au plus. La largeur fabriquee par l'absorbeur seul est donc
tres en dessous des plateaux predits de la section 7, la ou elle a ete mesuree. Ce que cette section NE montre PAS : que le lecteur lit juste, en 2D, sur le systeme a fantome, a
ces profondeurs. C'est au run de le dire, par sa qualification ; la seconde partie tiendra la ligne profonde hors des enonces qui font
tomber le gel.""" % (", ".join("%d" % x["m_bord_du_vide"] for x in TV), min(x["duree_totale_s"] for x in TV), max(x["duree_totale_s"] for x in TV), TV[0]["lectures"], min(x["Nmax"] for x in TV), max(x["Nmax"] for x in TV), e1(max(x["plus_grande_largeur"] for x in TV))))
T_()
T_("9. VIRGINITE")
P("""Balayage de machine 1, par recherche de texte : la fraction irreductible de chaque w2 candidat ; son ecriture au millieme apres
"w2" ; dans les fichiers JSON, une etiquette d'etat (0, 0), et une cle "delta" qui designe un w2 candidat.""")
P("""Au registre (%s, %d fichiers suivis, tous lus) : aucune trace d'un w2 candidat ; %d fichiers JSON, aucun ne porte l'etiquette
(0, 0) ni une telle cle.""" % (tete, BR["lus"], BR["json_lus"]), 4)
P("""Sur le poste de machine 1, hors du dossier de ce gel dont les pieces portent les candidats par construction (%d fichiers lus) :
aucune fraction ni ecriture apres "w2" d'un w2 candidat ; %d fichiers JSON portent l'etiquette (0, 0) et %d portent une cle "delta" qui
designe un w2 candidat (%s), tous des deux etapes sans run de ce jour (lots %s et %s, et leurs brouillons) : ce sont des chaines a une
dimension.""" % (BP_["lus"], len(BP_["etiquettes_00"]), len(BP_["deltas"]), " ; ".join("%s dans %s" % (k, ", ".join(sorted(v))) for k, v in sorted(groupes.items())),
                 c["lot_ech"], c["lot_vide"]), 4)
P("""Les seules 2D que machine 1 ait jouees pour preparer ce gel sont celles du jumeau sans fantome, a w2 = 101/50 et 199/100, qui ne
sont pas candidats. Ce balayage ne voit que le poste de machine 1, et une recherche de texte n'est pas une preuve d'absence : machine 2
tient les archives des runs et fait le sien.""")
T_()
T_("10. CE QUE MACHINE 2 CERTIFIE")
for t in ("""(a) que les definitions des sections 2 et 4, avec les blocs deposes, suffisent a calculer l'eligibilite sans lire le code de
machine 1 ;""",
          """(b) SA table d'eligibilite des %d cellules, par sa chaine ; et la table commune qui en resulte ;""" % n_cel,
          """(c) que son tirage, sur la graine de demonstration, rend les memes numeros que la section 3 et que le journal d'autotest ;""",
          """(d) SON balayage de ses archives : aucun calcul 2D du systeme a fantome a un w2 candidat, et aucune largeur 2D de l'etat
porte par (0, 0) du systeme a fantome, a aucun w2 ;""",
          """(e) que BOCAL4 peut jouer des boites jusqu'a N = %d (section 8), ou jusqu'ou il le peut.""" % max(RS[str(m)]["N_max"] for m in TOUS)):
    P(t, 2, 6)
T_()
T_("11. LA SUITE, DANS L'ORDRE")
for t in ("""(1) machine 2 certifie cette piece et rend sa table ; la table commune existe ;""",
          """(2) l'operateur donne la graine aux deux machines ;""",
          """(3) chaque machine tire ; les cellules sont les memes, ou PAS DE GEL ;""",
          """(4) machine 1 ecrit la seconde partie : l'instrument (la sonde du lecteur derivee du depot, sans etage dense, qui lit le site
(0, 0) aux cellules tirees ; sa feuille ; le bloc de ce lot comme predicteur ; les temoins : le jumeau sans fantome a la geometrie de
chaque cellule, les ancres et le temoin positif du depot), la table gelee des cellules avec leurs predictions calculees sur les chaines
seules, les enonces et leurs tolerances, ce que chaque issue engage, ce que vaut une cellule que le lecteur ne qualifie pas, et les
annonces de la plume ;""",
          """(5) machine 2 certifie la seconde partie ; l'operateur donne le feu vert par ecrit ; machine 2 joue, une fois."""):
    P(t, 2, 6)
T_()
T_("12. CE QUE CETTE PIECE NE FAIT PAS, ET SES ECARTS A LA REGLE DU GEL PRECEDENT")
for t in ("""Elle ne tire rien et ne connait aucune graine.""",
          """Elle ne donne aucune tolerance, et ne dit pas ce que vaut une cellule que le lecteur ne qualifie pas : c'est a la seconde
partie de le dire, avant le run.""",
          """Ecart 1 : un seul etat par cellule, celui que porte (0, 0), au lieu de quatorze etiquettes ; pas d'etage dense, donc ni
"jugeable" ni "dix planchers".""",
          """Ecart 2 : la cellule est un couple (w2, profondeur) dont le couplage vient d'une formule arrondie, au lieu de facteur x
g_du_point(w2) ; la table commune compare aussi les couplages ecrits.""",
          """Ecart 3 : les cellules profondes ne decident pas de l'eligibilite d'un w2.""",
          """Ecart 4 : la stabilite est l'etendue sous dix-huit variantes de l'absorbeur adapte, au lieu de trois variantes de l'absorbeur
du bloc depose. L'absorbeur adapte est une regle de ce jour, d'une seule plume ; son bloc est dans ce lot et se certifie avec lui. Son
etendue mesure la stabilite de la chaine sous ces variantes, pas l'erreur de la chaine.""",
          """Les bornes des creneaux, les profondeurs et l'ordre MG, MP, PP, PG sont de la plume de machine 1.""",
          """La definition du hamiltonien effectif est celle des blocs deposes (forme symetrique) ; aucune autre n'est essayee."""):
    P("- " + t, 2, 4)
T_()
T_("13. PIECES DE CE LOT (convention B)")
for p in PIECES:
    T_("    %s  %s" % (cp[p], p))
T_("    (ce script)       construction_regle_tirage_vide_machine1_v1.py")
T_()
texte = "\n".join(L) + "\n"; texte.encode("ascii")
assert max(len(l) for l in L) <= 100, [l for l in L if len(l) > 100]
open(SORTIE, "w", encoding="ascii", newline="\n").write(texte)
canon = B(SORTIE)

# --- le POUR_MACHINE2 ---
Mq = []
def Am(t="", ind=0, suite=None):
    if not t:
        Mq.append(""); return
    suite = ind if suite is None else suite
    Mq.extend(textwrap.wrap(" ".join(t.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
Am('# POUR MACHINE 2 -- GEL "LARGEUR DU VIDE", PREMIERE PARTIE : LA REGLE DE TIRAGE ET D\'ELIGIBILITE')
Am("# machine 1, v1, 2026-11-16. A CERTIFIER. Rien a jouer. La graine vient APRES, de l'operateur.")
Am(); Am("## 0. EN SIX PHRASES"); Am()
Am("""L'operateur a ouvert ce matin deux etapes hors chaine, sans run et sans toi (la loi d'echelle, puis le vide), et vient de lancer le
gel qui en sort ("on gele et on avance !", 12 h 19 ; declaration de machine 1). L'objet : la largeur de l'etat que porte le site (0, 0),
jamais lue en 2D selon mes pieces, predite par la chaine d'ordre 3 sous un absorbeur de chaine nouveau, adapte au saut. Cette piece (%s) n'en fige que la
PREMIERE partie : creneaux, cellules, tirage, eligibilite, rangs ; elle doit etre certifiee avant la graine. Ma table des %d cellules
candidates est dedans : %s. La seconde partie (sonde derivee sans etage dense, feuille, enonces, tolerances) vient apres le tirage. Tu
n'avais aucune des pieces de ces deux etapes : leurs deux lots (%s et %s) sont dans l'enveloppe.""" % (
    canon, n_cel, " ; ".join("%s %d w2 eligibles sur %d" % (s, n_el[s], len(cand[s])) for s in ORDRE), c["lot_ech"], c["lot_vide"]))
assert cp["eligibilite_vide_MG_MP_v1.json"] == cp["eligibilite_vide_MG_MP_sans_levier_v1.json"] and cp["eligibilite_vide_PP_PG_v1.json"] == cp["eligibilite_vide_PP_PG_sans_levier_v1.json"]
Am(); Am("## 1. E19"); Am()
Am("""Des chaines 1D aux %d cellules candidates (%d w2 au millieme). AUCUNE 2D du systeme a fantome a un w2 candidat par machine 1, et
aucune largeur 2D de l'etat (0, 0) du systeme a fantome a aucun w2. Les seules 2D : le jumeau sans fantome a w2 = 101/50 et 199/100, non
candidats. La meme interdiction vaut pour toi jusqu'au run ; elle est plus large que celle du gel precedent (section 0 de la piece).""" % (n_cel, n_w2), 2)
Am(); Am("## 2. CE QUE TU CERTIFIES (section 10 de la piece)"); Am()
Am("""(a) les definitions des sections 2 et 4 suffisent sans lire mon code ; (b) TA table des %d cellules et la table commune (le ET, qui
compare aussi les couplages ecrits) ; (c) ton tirage sur la graine de demonstration rend mes numeros ; (d) TON balayage de tes archives ;
(e) ce que BOCAL4 peut jouer comme boite, jusqu'a N = %d.""" % (n_cel, max(RS[str(m)]["N_max"] for m in TOUS)), 2)
Am(); Am("## 3. POUR REJOUER (python -I -B)"); Am()
Am("Le levier NPY_DISABLE_CPU_FEATURES=\"X86_V4\" ne change rien ici : les sorties avec et sans lui ont le meme canon (section 7 de la piece).", 2)
for cmd, com in (("eligibilite_vide_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> chaine_adaptee_bloc_machine1_v1.py <sortie.json> MG MP (puis : PP PG)",
                  "environ une minute et demie par paire de creneaux chez moi ; demande mpmath pour les cellules profondes"),
                 ("eligibilite_vide_machine1_v1.py <moteur> <bloc 2> <bloc 3> chaine_adaptee_bloc_machine1_v1.py <sortie.json> --controle absorbeur_adapte_v1.json",
                  "le bloc contre la piece de la note sur le vide, a deux w2 non candidats"),
                 ("lecture_eligibilite_vide_machine1_v1.py <sortie.json> <eligibilite MG MP.json> <eligibilite PP PG.json> [--autre <A'.json> <B'.json>]",
                  "la table de la section 7, au format du tirage"),
                 ("tirage_vide_machine1_v1.py --autotest ; tirage_vide_machine1_v1.py --demonstration <ma table> <ta table> ; puis, le moment venu : tirage_vide_machine1_v1.py <graine> <ma table> <ta table>",
                  "le tirage ; le ET des tables y est fait ; --demonstration lit les tables sous la graine de demonstration, qui n'est pas une suite de chiffres : ce n'est pas un tirage"),
                 ("faisabilite_profondeur_jumeau_machine1_v1.py <moteur> <sonde_lecteur_gel_loi_machine1_v1.py> <sortie.json>",
                  "le JUMEAU seulement, w2 = 101/50 ; environ une minute et demie ; c'est aussi ta mesure de cout pour (e)"),
                 ("balayage_virginite_machine1_v1.py <sortie.json> <dossier> [<dossier> ...] [--hors <sous-dossier>] [--connus <prefixe> ...]",
                  "mon balayage ; le tien porte sur tes archives, par ta methode"),
                 ("construction_regle_tirage_vide_machine1_v1.py <dossier des sorties> <clone du registre> <dossier du lot du vide> <dossier du lot de la loi d'echelle> <sortie.md>",
                  "refait la piece et ce fichier")):
    Am(cmd, 2, 6); Am("-> " + com, 6, 9)
Am(); Am("## 4. OU MORDRE"); Am()
for t in (
    """M-1 Le couplage d'une cellule (section 2) est le "%.5e" d'un produit en double precision ou entre X_saut_reel du moteur. Si un de tes
couplages ecrits differe d'un des miens, la regle rend le w2 ineligible : dis lequel.""",
    """M-2 La largeur (4.4) est une valeur propre ; sous 1e-15 |delta| je la reprends en precision arbitraire depuis le vecteur de la double
precision. L'etat est choisi en double precision par son poids sur le site 0 : il vaut %.4f au moins, il n'y a pas d'ambiguite. Ta
methode est la tienne ; les cellules de m = 8, 12 et 16 en dependent toutes.""" % poids_min,
    """M-3 Le seuil %s (4.6) est pose apres avoir vu %.4f au plus dans la note, dont des w2 candidats en chaine seule (4.8). Ma plus
grande etendue est %.4f : aucune cellule n'est pres du seuil, la regle ne trie rien chez moi. Elle garde contre ce que TA chaine verrait
et pas la mienne.""" % (RG["seuil_etendue"], vu, et_max),
    """M-4 L'absorbeur adapte et ses dix-huit variantes sont de ma plume et d'aujourd'hui. La note sur le vide (sections 3 et 4) dit
pourquoi l'absorbeur du bloc depose ne convient pas au vide (sa force suit le desaccord, pas le saut), et ce que l'adapte ne guerit PAS
(les termes d'ordre 3 apres la barriere, a des desaccords plus grands que ceux des creneaux). Lis-la avant de certifier le bloc.""",
    """M-5 La meme note retire, sous cinq defauts declares de ma plume, des phrases de la note sur la loi d'echelle. Et sa section 5 dit
une chose qui touche l'acte du delta 100 sans en changer un nombre : aux %d etats deja joues du domaine, l'absorbeur adapte deplace
l'ordre 3 de %.4f en mediane, pour un ecart median de la chaine a la 2D de %.4f. Rien n'est rejoue ni rejuge.""" % (len(EJ), joues_d, joues_q),
    """M-6 Les creneaux MP et PP (|delta| <= 0.009) sont pres de la limite d'echelle : la chaine y est presque au premier ordre, et le
gel y eprouve surtout Gamma = |delta| Phi(kappa). Je les garde pour couvrir une decade de |delta|. Le lecteur y a eta0 = |delta| petit ;
je n'ai pas de raison de croire que cela gene, et pas de preuve. Si tu en as une, dis-le avant la graine.""",
    """M-7 La ligne profonde predit des plateaux jusqu'a %s. Rien ne montre que le lecteur lit juste a ces profondeurs en 2D sur le
systeme a fantome ; au jumeau, a la meme geometrie, la largeur fabriquee par l'absorbeur est de %s au plus a m = 16, et la routine est
exacte sur une chaine jusqu'a exp(%.1f) (note sur le vide, 2.2). La seconde partie tiendra cette ligne hors des enonces letaux.""" % (
        e1(min(RS[str(m)]["G_min"] for m in PRO)), e1(FA[-1]["plus_grande_largeur"]), prof_ln),
    """M-8 La virginite (section 9) : mon balayage ne voit que mon poste. Les archives des runs sont chez toi.""",
    """M-9 r_c = 2 (m_bord + max(8, m_bord)) + 2 est la regle du depot sans sa graine ; je l'annonce ici pour le cout, elle sera figee
dans la seconde partie.""",
    """M-10 L'ouverture ("on gele et on avance !", 16/11, 12 h 19) et celles des deux etapes de ce matin (10 h 10, 11 h 03) sont des
declarations de machine 1 ; l'operateur les atteste ou non."""):
    Am(t, 2, 6)
Am(); Am("## 5. RIEN D'AUTRE"); Am()
Am("Aucun delai. Je commence la seconde partie par ce qui ne depend pas du tirage : la sonde derivee, sa feuille et son banc.")
pm2 = os.path.join(D, "POUR_MACHINE2_gel_vide_partie1_regle_tirage_machine1_v1.md"); tm = "\n".join(Mq) + "\n"; tm.encode("ascii")
assert max(len(l) for l in Mq) <= 100, [l for l in Mq if len(l) > 100]
open(pm2, "w", encoding="ascii", newline="\n").write(tm)
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(pm2), len(Mq), B(pm2)))
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(SORTIE), len(L), canon))
