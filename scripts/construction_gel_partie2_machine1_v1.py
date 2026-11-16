# -*- coding: utf-8 -*-
"""CONSTRUCTION du texte du gel "loi de la largeur, ordre 3", SECONDE PARTIE -- machine 1, v1, 2026-11-16. Aucun calcul de
chaine ni de 2D : chaque nombre du texte est lu ici dans une piece (JSON ou journal) ; les annonces de la section 10 sont
des jugements de la plume, ecrits en dur ici et dits tels.
Usage : python3 -I construction_gel_partie2_machine1_v1.py <dossier de la seconde partie> <dossier de la premiere partie>
        <clone du registre> <dossier du gel ter> <dossier du lot de machine 2 (certification)> <dossier du lot de machine 2
        (tirage)> <manifeste du lot du gel ter> <manifeste du lot de resultat du gel ter> <journal de l'ecart entre machines
        (gel du delta 98)> <note de la carte.md> <note de machine 2 en reponse a la carte.md> <sortie.md>"""
import sys, os, re, json, math, hashlib, unicodedata, textwrap
from fractions import Fraction as F
D, D1, CLONE, DTER, M2CERT, M2TIR, MAN_TER, MAN_RES, J_ECART, N_CARTE, N_REP, SORTIE = sys.argv[1:13]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n"); return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def J(*p):
    return json.load(open(os.path.join(*p)))
I = os.path.join(D, "instrument")
C = J(I, "canons_instrument_v1.json"); MG = J(D, "marges_cellules_tirees_v1.json"); RT = J(D, "feuille_ordre3_retrospective_v1.json"); BC = J(D, "banc_feuille_ordre3_v1.json")
EB = J(D, "essai_a_blanc_hors_cellules_v1.json"); BL = J(D, "definition_bloch_v1.json"); AN = J(D, "ancres_retrospectif_v1.json"); EL = J(D1, "eligibilite_candidates_v1.json"); PV = J(D, "comparaison_prevol_v1.json"); DEP = J(CLONE, "journal", "sonde_ordre2.json")
c = {"moteur": canon(os.path.join(CLONE, "scripts", "m17_chaine_v17.py")), "bloc2": canon(os.path.join(CLONE, "scripts", "chaine_ordre2_bloc_machine1_v1.py")),
     "bloc3": canon(os.path.join(I, "ordre3_bloc_machine1_v1.py")), "depot": canon(os.path.join(CLONE, "journal", "sonde_ordre2.json")),
     "gel98": canon(os.path.join(CLONE, "gels", "gel_ordre2_chaine_EA_pre_enregistrement_v1.md")), "gel_ter": canon(os.path.join(DTER, "qualification_EB_ter_pre_enregistrement_v1.md")),
     "sonde98": canon(os.path.join(CLONE, "scripts", "sonde_ordre2_machine1_v1.py")), "sonde_ter": canon(os.path.join(DTER, "sonde_qualification_EB_ter_machine1_v1.py")),
     "feuille_ter": canon(os.path.join(DTER, "lecture_qualification_EB_ter_machine1_v1.py")), "banc_ter": canon(os.path.join(DTER, "banc_feuille_ter_machine1_v1.py")),
     "retenus": canon(os.path.join(CLONE, "journal", "tp_retenus_machine2_v1.json")), "tp_ref": canon(os.path.join(CLONE, "journal", "tp_reference_machine2_v1.json")),
     "anc_ref": canon(os.path.join(DTER, "reference_ancres_ter_machine1_v1.json")), "partie1": canon(os.path.join(D1, "gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md")),
     "table_m1": canon(os.path.join(D1, "eligibilite_candidates_v1.json")), "tirage_m1": canon(os.path.join(D1, "tirage_machine1_v1.py")),
     "tirage_m2": canon(os.path.join(M2CERT, "controle_carte_machine2", "tirage_gel_loi_machine2_v1.py")), "tirage_complet_m2": canon(os.path.join(M2CERT, "controle_carte_machine2", "tirage_complet_machine2_v1.py")),
     "table_m2": canon(os.path.join(M2CERT, "controle_carte_machine2", "eligibilite_machine2_v1.json")), "table_commune": canon(os.path.join(M2CERT, "controle_carte_machine2", "table_commune_machine2_v1.json")),
     "lot_cert": canon(os.path.join(M2CERT, "MANIFEST_lot_machine2_certification_gel_loi_partie1_v1.txt")), "lot_tir": canon(os.path.join(M2TIR, "MANIFEST_lot_machine2_tirage_graine_200482_v1.txt")),
     "table": canon(os.path.join(I, "table_points_gel_loi_ordre3_v1.json")), "table_prevol": canon(os.path.join(I, "table_points_prevol_gel_loi_ordre3_v1.json")),
     "sonde_dense": canon(os.path.join(I, "sonde_dense_gel_loi_machine1_v1.py")), "sonde_lecteur": canon(os.path.join(I, "sonde_lecteur_gel_loi_machine1_v1.py")),
     "feuille_lecteur": canon(os.path.join(I, "lecture_lecteur_gel_loi_machine1_v1.py")), "feuille_o3": canon(os.path.join(I, "feuille_ordre3_machine1_v1.py")),
     "pilote": canon(os.path.join(I, "pilote_gel_loi_machine1_v1.py")), "banc_o3": canon(os.path.join(D, "banc_feuille_ordre3_machine1_v1.py"))}
assert (c["moteur"], c["bloc2"], c["bloc3"], c["depot"], c["gel98"], c["partie1"], c["lot_cert"], c["lot_tir"], c["sonde98"], c["sonde_ter"]) == (
    "82a0be882568fe0c", "7cd5977bc27bebc1", "534ba246aa3b8973", "10887c60d5f55bcf", "41153158190cf7f1", "b56ca5cb2dd25da1", "4fb1dc66f96f57f6", "220a0970134335e1", "24315c52b234319c", "b5616dcf858e8801"), c
assert (c["table"], c["sonde_dense"], c["sonde_lecteur"], c["feuille_lecteur"]) == (C["table"], C["sonde_dense"], C["sonde_lecteur"], C["feuille_lecteur"]) and c["feuille_ter"] == C["feuille_ter_source"]
LOT_GEL_TER, LOT_RES_TER = canon(MAN_TER), canon(MAN_RES); assert (LOT_GEL_TER, LOT_RES_TER) == ("42110a3d1eabdaa0", "1f057651c8f69eb6")
assert "verdict_ter.json" in open(MAN_RES, encoding="utf-8").read() and "qualification_EB_ter_pre_enregistrement_v1.md" in open(MAN_TER, encoding="utf-8").read()
m_ec = re.search(r"plus grand ecart de chaine entre machines aux deux etats d'ancre : (\S+) ;", open(J_ECART, encoding="ascii").read()); assert m_ec; ECART_MACHINES = m_ec.group(1)
assert "189 étiquettes lues sur 224" in open(N_CARTE, encoding="utf-8").read()
assert "4377 s pour le gel ter" in open(N_REP, encoding="utf-8").read()
# les constantes de la feuille d'ordre 3, lues dans son texte
fo3 = open(os.path.join(I, "feuille_ordre3_machine1_v1.py"), encoding="ascii").read()
def cst(nom):
    m = re.search(r"\b%s = ([^;\n]+)" % nom, fo3); assert m, nom; return m.group(1).strip()
assert (cst("E_MAX"), cst("STAB_MAX"), cst("J_NET"), cst("E_BAS"), cst("T_BAS"), cst("T_HAUT")) == ("0.7", "0.05", "0.2", "0.3", "0.05", "0.10")
assert (cst("DOM_MIN"), cst("BORD_MIN"), cst("PART_JUGES"), cst("PART_E2"), cst("INEXPLOITABLES_E1"), cst("INEXPLOITABLES_E2"), cst("N_ETATS")) == ("5", "2", "F(2, 3)", "F(3, 4)", "2", "1", "14")
assert "TOL_ANCRE_REL, TOL_ANCRE_ABS, TOL_ANCRE_E = 1e-3, 1e-12, 1e-9" in fo3 and '"%s", "%s", "%s"' % (c["table"], c["sonde_dense"], c["feuille_lecteur"]) in fo3
assert 'issue(lig, "E1", INEXPLOITABLES_E1, 1)' in fo3 and 'issue(ligN, "E2", INEXPLOITABLES_E2, 1)' in fo3 and 'issue(brd, "E1", 0, 0)' in fo3
pil = open(os.path.join(I, "pilote_gel_loi_machine1_v1.py"), encoding="ascii").read()
for k in ("table", "sonde_dense", "sonde_lecteur", "feuille_lecteur"):
    assert '"%s"' % c[k] in pil, k
assert '"feuille_ordre3": "%s"' % c["feuille_o3"] in pil
# la table et les cellules
TB = J(I, "table_points_gel_loi_ordre3_v1.json"); cel = [p for p in TB["points"] if p["role"] == "juge"]; assert len(cel) == 12 and TB["graine"] == "200482" and TB["rang"] == 0
mg = {r["id"]: r for r in MG["cellules"]}; el = {(r["creneau"], F(r["w2"]), F(r["facteur"])): r for r in EL["cellules"]}; ET = MG["etalonnage"]
def e(p):
    return el[(p["creneau"], F(p["w2"]), F(p["facteur"]))]
assert all(e(p)["eligible"] for p in cel)
tir = open(os.path.join(D, "tirage_machine1_v1_graine_200482.log"), encoding="ascii").read(); assert "TIRAGE : douze cellules" in tir and tir.count("rang 0 :") == 4 and "rang 1" not in tir
tir2 = open(os.path.join(M2TIR, "controle_carte_machine2", "tirage_graine_200482_machine2_v1.log"), encoding="ascii").read()
for p in cel:
    assert re.search(r"%s\s+w2 = %s \(\S+\) facteur %s\s" % (p["id"], F(p["w2"]), F(p["facteur"])), tir2), p
# le retrospectif
rc = {x["id"]: x for x in RT["cellules"]}; dom = [(x, r) for x in RT["cellules"] for r in x["etats"] if r["exclu"] is None and r["dans_le_domaine"]]
assert RT["comptes"] == {"lus": 137, "juges": 131, "domaine": 56, "hors": 75}, RT["comptes"]
def med(v):
    v = sorted(v); n = len(v); return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])
def haut(x, n):                       # "au plus" : arrondi par exces
    return math.ceil(x * 10 ** n - 1e-9) / 10 ** n
def bas(x, n):                        # "au moins" : arrondi par defaut
    return math.floor(x * 10 ** n + 1e-9) / 10 ** n
cl = {}
for lo, hi in ((0.0, 0.3), (0.3, 0.5), (0.5, 0.7)):
    v = [abs(r["ln_q3"]) for x, r in dom if lo <= r["e_bord"] < hi]; cl[(lo, hi)] = (len(v), med(v), max(v))
assert [cl[k][0] for k in sorted(cl)] == [27, 16, 13]
pire_bas, pire_haut = cl[(0.0, 0.3)][2], max(cl[(0.3, 0.5)][2], cl[(0.5, 0.7)][2])
n_mieux = sum(1 for x, r in dom if r["ordre3_plus_pres"]); assert n_mieux == len(dom) == 56
sous07 = [r for x in RT["cellules"] for r in x["etats"] if r["exclu"] is None and r["e_bord"] < 0.7]; assert len(sous07) == 83 and all(r["ordre3_plus_pres"] for r in sous07)
n_sous07_hors = sum(1 for r in sous07 if not r["dans_le_domaine"]); assert n_sous07_hors == 27
anp = [r for r in AN["etats"] if r["plateau"]]; assert len(anp) == 4 and all(r["dans_le_domaine"] for r in anp)
a1 = [r["plateau"]["ln_q3"] for r in anp if r["id"] == "A1"]; a2 = [r["plateau"]["ln_q3"] for r in anp if r["id"] == "A2"]
assert BC["tient"] and len(BC["mutations"]) == 17 and all(m["tient"] for m in BC["mutations"])
assert PV["tient"] and len(PV["controles"]) == 5, PV
bl = open(os.path.join(D, "banc_feuille_lecteur_sur_derivee_v1.log"), encoding="ascii").read(); mb = re.search(r"BANC : (\d+) alterations, (\d+) mordues, 0 survivantes \[\], 0 cibles refusees \[\] ; base saine : True", bl); assert mb and mb.group(1) == mb.group(2) == "43"
st = open(os.path.join(D, "selftest_feuille_lecteur_derivee_v1.log"), encoding="ascii").read(); ms = re.search(r"selftest : (\d+) tenus sur (\d+)", st); assert ms and ms.group(1) == ms.group(2) == "68"
assert EB["tient"] and [x["essai"] for x in EB["essais"]] == ["S1", "S2", "S3", "S4", "S5", "S6"]
assert (EB["canons"]["feuille_ordre3_machine1_v1.py"], EB["canons"]["lecture_lecteur_gel_loi_machine1_v1.py"], EB["canons"]["sonde_dense_gel_loi_machine1_v1.py"], EB["canons"]["sonde_lecteur_gel_loi_machine1_v1.py"],
        EB["canons"]["table_points_gel_loi_ordre3_v1.json"], EB["canons"]["ordre3_bloc_machine1_v1.py"]) == (c["feuille_o3"], c["feuille_lecteur"], c["sonde_dense"], c["sonde_lecteur"], c["table"], c["bloc3"])
# l'essai de la forme de Bloch
bj = BL["joues"]; assert len(bj) == 56 and BL["C1"]["pire_ecart_tables"] < 1e-8 and abs(BL["C2"]["pentes"][0] - 4.0) < 0.05
bl_med = med([abs(r["ln_B_S"]) for r in bj]); bl_max = max(abs(r["ln_B_S"]) for r in bj); bl_pres = sum(1 for r in bj if abs(r["ln_q3_bloch"]) < abs(r["ln_q3"]))
bl_cel = max(max(abs(x["min"]), abs(x["max"])) for x in BL["cellules"]); BD = BL["D"]
# le pre-vol : durees lues dans le journal du pilote
pj = open(os.path.join(D, "prevol_run", "pilote_gel_loi.log"), encoding="ascii").read()
def duree(nom):
    m = re.search(r"%s\s+code=0 duree=(\d+) s" % re.escape(nom), pj); assert m, nom; return int(m.group(1))
du = {k: duree(k) for k in ("lecteur etage0", "lecteur ancres", "lecteur etage1", "lecteur point C3", "feuille d'ordre 3")}
mfin = re.search(r"FIN DU PILOTE ; duree totale (\d+) s", pj); assert mfin; du["total"] = int(mfin.group(1))
canons_pv = dict(re.findall(r"canon (\S+)\s+([0-9a-f]{16})", pj))
dC3 = [p for p in J(D, "prevol_dense_C3_machine1_v1.json")["points"] if p["id"] == "C3"][0]["duree_s"]
# couts : la sonde dense au depot (BOCAL4), par boite
dd = sorted((p["N"], p["duree_s"]) for p in DEP["points"] if p["N"] <= 74)
def cout_dense(N):                    # interpolation en loi de puissance entre les deux boites deposees qui encadrent N
    bas_ = [x for x in dd if x[0] <= N][-1]; haut_ = [x for x in dd if x[0] >= N][0]
    if bas_[0] == haut_[0]:
        return med([x[1] for x in dd if x[0] == N])
    return bas_[1] * (N / bas_[0]) ** (math.log(haut_[1] / bas_[1]) / math.log(haut_[0] / bas_[0]))
cout1 = sum(cout_dense(e(p)["N"]) for p in cel) + sum(p["duree_s"] for p in DEP["points"] if p["id"] in ("A1", "A2"))
n_pred = sum(e(p)["n_jug"] for p in cel)

L = []
def T_(s=""): L.append(s)
def P(s, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))

T_('GEL "LOI DE LA LARGEUR, ORDRE 3" -- SECONDE PARTIE : L\'INSTRUMENT, LES ENONCES, LES TOLERANCES')
T_("PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-16 (nuit du 15 au 16).")
T_("A CERTIFIER PAR MACHINE 2 AVANT TOUT CALCUL 2D A L'UNE DES DOUZE CELLULES.")
T_()
T_("0. STATUT")
P("""Cette piece complete la premiere partie (%s, lot 596a45bf6d4f97d7), que machine 2 a certifiee telle quelle, a zero morsure (lot %s). Elle
fixe les douze cellules tirees, l'instrument du run, les enonces juges, leurs tolerances, ce que chaque issue engage, et les annonces de la
plume. Rien n'est joue : aucune des douze cellules n'a ete calculee en 2D, par aucune des deux machines.""" % (c["partie1"], c["lot_cert"]))
P("""Ouverture. L'operateur a atteste a machine 1 (15/11/2026, 22 h 54) que son "Reprends" de 22 h 42 etait bien le "go" du gel. Machine 2
dit avoir recu de lui "OK go on gel", sans pouvoir le dater (lot %s, section 2).""" % c["lot_cert"])
P("""Graine. L'operateur a donne la graine 200482 a machine 1 par ecrit (15/11/2026, 23 h 19), apres la certification de la premiere partie ;
il l'a ecrite sous forme de question, machine 1 a repondu que sa valeur n'appelait pas d'avis de sa part et l'a prise comme donnee. Machine
1 n'avait calcule aucun tirage avant de la recevoir. Machine 2 rapporte l'avoir recue de l'operateur (lot %s). Les mots exacts sont dans la
note d'accompagnement.""" % c["lot_tir"])
P("""Tirage. Par le script de machine 1 (%s) et par ceux de machine 2 (%s et %s), sur le ET des deux tables d'eligibilite (%s et %s, identiques) :
les quatre creneaux sortent au rang 0 et les douze cellules des deux machines sont les memes, une a une (lot %s ; journal de machine 1
joint).""" % (c["tirage_m1"], c["tirage_m2"], c["tirage_complet_m2"], c["table_m1"], c["table_m2"], c["lot_tir"]))
P("""E19. Aucun calcul 2D, dense ou creux, a aucune des douze cellules, par aucune des deux machines, avant la certification croisee de cette
piece et le feu vert ecrit de l'operateur. Tout ce que cette piece calcule aux cellules est une chaine a une dimension. Les calculs 2D
qu'elle rapporte (pre-vol, section 4.6) sont a des points DEJA JOUES.""")
T_()
T_("1. QUESTION ET PERIMETRE")
P("""La note sur la loi de la largeur (lot e93f1898dcd78a8f) a lu, sur 131 etats de douze points deja joues, qu'une chaine a une dimension
poussee a l'ordre 3 rend la largeur de plateau a quelques centiemes pres DANS UN DOMAINE (e_bord < 0.7 et chaine d'ordre 3 stable), et
qu'elle s'egare au-dela. C'etait lu apres coup, sur des points choisis pour autre chose. Ce gel demande si cela tient a des points que
personne n'a choisis : douze cellules tirees au sort par une graine de l'operateur.""")
P("""Perimetre : un w2 par ligne (delta = -0.065 et +0.035), cinq couplages par ligne, et deux cellules de bord (delta = -0.076 et +0.067).
L'objet juge est la chaine du bloc d'ordre 3 de machine 1 (%s), telle quelle. La reference est la largeur de plateau sous l'absorbeur A,
lue par le lecteur creux du gel ter (%s).""" % (c["bloc3"], c["gel_ter"]))
T_()
T_("2. SOURCES (convention B)")
for k, nom in (("moteur", "scripts/m17_chaine_v17.py (registre 8d54bf9), le moteur"), ("bloc2", "scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2"),
               ("bloc3", "ordre3_bloc_machine1_v1.py (lot e93f1898dcd78a8f ; joint ici), le bloc d'ordre 3, rederive par machine 2 (lot 889fe9b4c1c1c60a)"),
               ("depot", "journal/sonde_ordre2.json (registre), le depot du delta 98 : ancres, et sortie dense du pre-vol"),
               ("gel98", "gels/gel_ordre2_chaine_EA_pre_enregistrement_v1.md (registre) : regle du point, bandes de l'ordre 2"),
               ("sonde98", "scripts/sonde_ordre2_machine1_v1.py (registre) : la sonde dense certifiee"),
               ("gel_ter", "qualification_EB_ter_pre_enregistrement_v1.md (lot %s) : le lecteur, ses epreuves, ses statuts" % LOT_GEL_TER),
               ("sonde_ter", "sonde_qualification_EB_ter_machine1_v1.py (meme lot) : la sonde du lecteur certifiee"),
               ("feuille_ter", "lecture_qualification_EB_ter_machine1_v1.py (meme lot) : la feuille du lecteur certifiee"),
               ("retenus", "journal/tp_retenus_machine2_v1.json (registre) : couplages du temoin"), ("tp_ref", "journal/tp_reference_machine2_v1.json (registre) : reference du temoin"),
               ("anc_ref", "reference_ancres_ter_machine1_v1.json (lot %s) : reference des ancres" % LOT_GEL_TER),
               ("partie1", "gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md (lot 596a45bf6d4f97d7)"),
               ("lot_cert", "lot de machine 2 : certification de la premiere partie, sa table, la table commune"), ("lot_tir", "lot de machine 2 : son tirage sur la graine 200482")):
    P("%s  %s" % (c[k], nom), 4, 22)
P("""2cd1f84efa02f2ab  verdict_ter.json du run du gel ter (lot %s de machine 2) : les largeurs de plateau des points deja joues.""" % LOT_RES_TER, 4, 22)
P("""L'acte du gel ter (751165a3eee613d9, lot 26b3912297b31713) est contresigne par machine 2 (lots e8ff4d600edf89ef et b42a63640f1c566a) et
N'EST PAS ENCORE DEPOSE : le clone de machine 1 est a 8d54bf9, et les enveloppes de machine 2 du 15/11 disent le registre a ce numero. La
reference de ce gel s'appuie donc sur un acte contresigne, pas sur un acte depose (section 13, L-2).""")
T_()
T_("3. LES DOUZE CELLULES")
P("""Table gelee : table_points_gel_loi_ordre3_v1.json, canon %s. Elle porte la graine, le rang, les douze cellules (role "juge") et les
deux ancres du depot, A1 (w2 = 39/20) et A2 (41/20), au facteur 1 (role "ancre"). Les scripts de l'instrument lisent les points dans cette
table et portent son canon en dur.""" % c["table"])
P("""Par cellule : w2, delta, facteur, couplage g = facteur x g_du_point(w2), boite N de la sonde dense ; puis, pour les quatorze etiquettes
PREDITES par la chaine (premiere partie, section 4) : etats jugeables / dans le domaine / hors du domaine.""")
for p in cel:
    r = e(p)
    T_("    %-3s w2 = %-9s delta %+.3f  x%-4s g = %.4e  N = %d   predits %2d / %2d / %2d" % (p["id"], p["w2"], float(F(p["w2"])) - 2.0, p["facteur"], r["g"], r["N"], r["n_jug"], r["n_dom"], r["n_hors"]))
P("""Ces comptes sont ceux des deux tables (machine 1 et machine 2, identiques). Ils portent sur des etiquettes predites : le jugement
portera sur les etats LUS (sections 5 et 6).""")
T_()
T_("4. L'INSTRUMENT : UN RUN, DEUX ETAGES")
T_("  4.1 Les pieces (convention B)")
for k, nom in (("table", "table_points_gel_loi_ordre3_v1.json : la table gelee"), ("sonde_dense", "sonde_dense_gel_loi_machine1_v1.py : derivee de la sonde dense certifiee (%s)" % c["sonde98"]),
               ("sonde_lecteur", "sonde_lecteur_gel_loi_machine1_v1.py : derivee de la sonde du gel ter (%s)" % c["sonde_ter"]),
               ("feuille_lecteur", "lecture_lecteur_gel_loi_machine1_v1.py : derivee de la feuille du gel ter (%s)" % c["feuille_ter"]),
               ("feuille_o3", "feuille_ordre3_machine1_v1.py : NOUVELLE ; elle juge les enonces"), ("pilote", "pilote_gel_loi_machine1_v1.py : NOUVEAU ; il enchaine et tient le journal"),
               ("table_prevol", "table_points_prevol_gel_loi_ordre3_v1.json : un point deja joue (C3) et les ancres")):
    P("%s  %s" % (c[k], nom), 4, 22)
P("""Les trois scripts derives le sont par remplacements de texte, chacun trouve une seule fois dans sa source ; aucun script certifie
n'est edite. Le script de construction et un diff unifie par script sont joints : la sonde dense differe de sa source par la lecture de la
table et l'en-tete de sa sortie ; la sonde du lecteur par l'origine des points du mode "point" (la sortie dense du run, au canon passe) et
l'en-tete ; la feuille du lecteur par la meme origine, le controle de forme, trois canons de plus dans le verdict, et un refus retire
(section 14, E-4).""")
T_("  4.2 Le deroulement du run (le pilote)")
P("""Etage 1. La sonde dense, aux quatorze points de la table : boite, trois decompositions denses (k = 2, 3, 4), les 14 etats de plus
grand recouvrement avec la graine coherente, leurs etiquettes, leur largeur deposee a k = 3. Meme code que la sonde du delta 98.""", 4)
P("""Etage 2a. La sonde du lecteur en modes etage0, ancres, etage1 (points regles du depot : inchanges) ; la feuille du lecteur, etape
"instrument". Si elle ne rend pas TIENT, le run s'arrete : rien n'est juge.""", 4)
P("""Etage 2b. La sonde du lecteur en mode point, un appel par cellule : chaque etat dont la largeur deposee a k = 3 depasse dix planchers
(1.33e-12) est lu sous les quatre absorbeurs, a douze barreaux. La feuille du lecteur, etape "verdict" : plateau sous A, accords B, C, D,
statut de chaque etat (gel ter, section 7).""", 4)
P("""Etage 3. La feuille d'ordre 3 : chaines a une dimension (moteur, ordre 2, ordre 3) a l'etiquette LUE de chaque etat ; jugement des
enonces de la section 6.""", 4)
T_("  4.3 Les quatre conditions de machine 2 (lot 548fb2ba8793ecfe, section 2)")
P("""C1. Le pilote ecrit le canon de la sortie dense dans son journal des qu'elle existe et le passe en argument a la sonde du lecteur, a
la feuille du lecteur et a la feuille d'ordre 3, qui le comparent au fichier qu'elles lisent. Il fait de meme du canon du verdict du lecteur
pour la feuille d'ordre 3. Les canons des scripts, du moteur, des blocs, du depot et de la table restent en dur.""", 4)
P("""C2. Forme de la sortie dense, controlee avant toute lecture : par la sonde du lecteur (canon du moteur et de la sonde dense, canon de
la table ; par point : w2 et facteur egaux a ceux de la table a l'egalite des fractions, couplage egal a facteur x g_du_point(w2) a 1e-12
pres en relatif, 14 etats, point faisable) ; par la feuille du lecteur (les memes, sauf le couplage : elle n'a pas de moteur ; et les
quatorze points de la table, eux seuls) ; par la feuille d'ordre 3 (tout cela, et les ancres : 4.4).""", 4)
P("""C3. Les points sont dans la table gelee, pas dans le texte des scripts.""", 4)
P("""C4. Pre-vol sur des points deja joues : section 4.6.""", 4)
T_("  4.4 Les ancres de la sonde dense")
P("""Ajout de machine 1. La sonde dense rejoue les deux ancres du depot. La feuille d'ordre 3 exige que leurs 14 etats portent les memes
etiquettes que dans le depot, que leur largeur deposee a k = 3 s'en ecarte d'au plus 1e-3 en relatif plus 1e-12, et leur energie d'au plus
1e-9. Sinon l'instrument ne tient pas et rien n'est juge. C'est un controle de reproduction de la sonde dense sur la machine du run, pas un
controle de justesse (L-10).""", 4)
T_("  4.5 Les deux feuilles et leurs bancs")
P("""Feuille du lecteur derivee : son selftest tient (%s cas sur %s) ; le banc certifie de la feuille du gel ter (%s), joue sur la feuille
derivee, mord a %s alterations sur %s.""" % (ms.group(1), ms.group(2), c["banc_ter"], mb.group(2), mb.group(1)), 4)
P("""Feuille d'ordre 3 : jouee sur les douze points juges du delta 98 (depot, et verdict du run du gel ter), elle retrouve les %d etats de
la note sur la loi, les memes, dont %d dans le domaine. Son banc (%s) part de trois points deja joues et change UNE chose a la fois, avec
l'effet attendu ecrit avant : %d mutations, %d mordent comme attendu. Elles couvrent : une largeur de plateau, toutes les largeurs d'un
point, un statut, l'instrument, une etiquette, le couplage, le nombre d'etats, le facteur de la table, la bande de l'ordre 2, le J, un canon,
la cellule inexploitable, l'etiquette double, une ancre, la part des etats juges, une ancre retiree, la table hors pre-vol.""" % (
    RT["comptes"]["juges"], RT["comptes"]["domaine"], c["banc_o3"], len(BC["mutations"]), sum(m["tient"] for m in BC["mutations"])), 4)
T_("  4.6 Le pre-vol de machine 1 (condition C4)")
P("""Sur la machine de machine 1, le pilote a joue le chemin derive en mode --prevol sur la table de pre-vol (le point C3 du delta 98,
deja joue, et les ancres), la sortie du depot tenant lieu de sortie dense. Cinq controles (comparaison_prevol_machine1_v1.py), tous tenus
:""", 4)
for r in PV["controles"]:
    P("%s  %s" % (r["controle"], r["detail"]), 6, 10)
P("""Durees sur le conteneur de machine 1 (deux coeurs) : etage0 %d s, ancres %d s, etage1 %d s, point C3 %d s, feuille d'ordre 3 %d s ;
total %d s. La sonde dense derivee a C3 : %.0f s.""" % (du["lecteur etage0"], du["lecteur ancres"], du["lecteur etage1"], du["lecteur point C3"], du["feuille d'ordre 3"], du["total"], dC3), 4)
m_pil = re.search(r"pilote pilote_gel_loi_machine1_v1.py canon ([0-9a-f]{16})", pj); assert m_pil
f_av = canon(os.path.join(D, "avant", "feuille_ordre3_machine1_v1_au_lancement_du_prevol.py")); p_av = canon(os.path.join(D, "avant", "pilote_gel_loi_machine1_v1_au_lancement_du_prevol.py"))
assert canons_pv.get("feuille_ordre3") == f_av != c["feuille_o3"] and m_pil.group(1) == p_av != c["pilote"]
P("""Ecart declare (E-7) : ce pre-vol a ete LANCE avant la derniere retouche de la feuille d'ordre 3 (le niveau TENU SAUF UNE CELLULE de E2 et
quatre lignes d'en-tete). Le journal du pilote porte donc les canons d'avant, de la feuille (%s) et du pilote (%s) ; l'etage 3 du pre-vol,
lui, a joue la feuille finale (%s), deja en place quand il a ete atteint. Les deux pieces telles qu'au lancement sont jointes,
reconstruites : elles rendent les deux canons du journal ; le diff de la retouche est joint. Le pilote final ne differe de celui du pre-vol
que par le canon de la feuille qu'il porte. Machine 2 refait le pre-vol avec les pieces finales (section 11).""" % (f_av, p_av, c["feuille_o3"]), 4)
P("""Ce que le pre-vol de machine 1 ne dit pas : "les memes octets que le lecteur certifie" au point (C4, a la lettre) ne se verifie que sur
la machine du run certifie ; machine 1 ne peut comparer qu'a 1e-6 pres. C'est a machine 2 de le faire sur BOCAL4, avec le meme script de
comparaison.""", 4)
T_("  4.7 Le chemin sans --prevol, essaye a blanc hors des cellules")
P("""Le run se joue SANS --prevol. Ses branches propres (table du gel, controles de provenance, creneaux N, P, BN, BP) ne peuvent pas etre
jouees pour de vrai avant le feu vert : ce serait calculer en 2D aux cellules. Machine 1 les a fait tourner sans aucune mesure 2D a une
cellule (essai_a_blanc_hors_cellules_machine1_v1.py), sur les pieces aux canons de 4.1. Six essais, tous tenus :""", 4)
for r in EB["essais"]:
    P("%s  %s" % (r["essai"], r["detail"]), 6, 10)
P("""Les fichiers dits fabriques recopient des mesures de points DEJA JOUES (depot du delta 98, run du gel ter) sous les identifiants, w2,
facteurs et couplages des cellules, avec les en-tetes que les scripts attendent. Ils ne disent rien des cellules ; les issues que la feuille
en tire n'ont aucun sens, ne sont pas affichees, et les fichiers sont effaces. Les seules chaines calculees aux cellules y sont a une
dimension. Le pilote, lui, n'a ete joue qu'avec --prevol.""", 4)
T_()
T_("5. ETATS JUGES, DOMAINE, CELLULE EXPLOITABLE")
P("""ETAT LU : un des 14 etats de la sonde dense que le lecteur a lus (largeur deposee a k = 3 au-dessus de dix planchers).""")
P("""ETAT JUGE : un etat lu qui est, dans cet ordre, QUALIFIE par la feuille du lecteur ; d'etiquette nette (ecart-type de J < 0.2) ;
d'etiquette unique parmi les 14 etats du point ; de barriere non vide ; de chaine du moteur stable et de chaine d'ordre 2 stable (quatre eta
de chaine, toutes les largeurs positives, plus grande / plus petite <= 2). Un etat exclu l'est avec son premier motif, publie.""")
P("""DANS LE DOMAINE : un etat juge tel que e_bord < 0.7 et que la stabilite de sa chaine d'ordre 3 soit definie et <= 0.05 (premiere partie,
4.3 et 4.4). HORS DU DOMAINE : un etat juge qui n'est pas dans le domaine.""")
P("""Grandeurs : G2 et G3 sont les largeurs des chaines d'ordre 2 et d'ordre 3 au facteur d'eta 1/16 ; Gamma_pl est la largeur de plateau
sous l'absorbeur A ; q2 = G2 / Gamma_pl, q3 = G3 / Gamma_pl.""")
P("""CELLULE EXPLOITABLE. Il faut d'abord qu'au moins les deux tiers de ses etats lus soient juges. Puis : pour une cellule de ligne (N1 a
N5, P1 a P5), au moins 5 etats juges dans le domaine ; pour une cellule de bord (BN, BP), au moins 2 dans le domaine et au moins 2 hors du
domaine. Une cellule INEXPLOITABLE n'entre ni dans E1, ni dans E2, ni dans E1B ; elle reste jugee par E3 ; ses nombres sont publies.""")
T_()
T_("6. LES ENONCES ET LEURS ISSUES (la cellule est l'unite)")
P("""E1, cellules de ligne. Une cellule exploitable TIENT si chacun de ses etats juges du domaine a |ln q3| <= T, avec T = 0.05 si e_bord
< 0.3 et T = 0.10 sinon ; elle TOMBE sinon. Un seul etat hors tolerance fait tomber la cellule.""")
P("""E2, cellules de la ligne N. Une cellule exploitable TIENT si |ln q3| < |ln q2| pour au moins les trois quarts (arrondis par exces) de
ses etats juges du domaine ; elle TOMBE sinon.""")
P("""E1B, cellules de bord. Comme E1, sur les etats juges du domaine de BN et de BP.""")
P("""E3, les douze cellules. Une cellule TIENT si chacun de ses etats juges, dans le domaine ou non, a 1/B <= q2 <= B, B etant la borne du
delta 98 : 1.25 pour |delta| <= 0.06, 1.6 jusqu'a 0.10. Les lignes N et les deux bords sont a B = 1.6 ; la ligne P a B = 1.25. Une cellule
sans etat juge est VIDE et ne tombe pas.""")
P("""ISSUES. Les chutes d'abord, ce sont des faits ; les cellules inexploitables ensuite.""")
P("""E1 (dix cellules) : TOMBE si deux cellules exploitables ou plus tombent ; sinon NON CONCLUANT si plus de deux cellules sont
inexploitables ; sinon TENU si aucune ne tombe, TENU SAUF UNE CELLULE si une seule tombe.""", 4)
P("""E2 (cinq cellules) : de meme, NON CONCLUANT si plus d'une cellule est inexploitable.""", 4)
P("""E1B (deux cellules) : TOMBE si une cellule exploitable tombe ; sinon NON CONCLUANT si l'une est inexploitable ; sinon TENU.""", 4)
P("""E3 (douze cellules) : TOMBE si une cellule tombe ; sinon TENU.""", 4)
P("""La ligne P ne juge pas l'ordre 3 contre l'ordre 2 : aux etiquettes predites de ses cinq cellules, |ln(G3 / G2)| vaut de %.3f a %.3f,
du niveau de la stabilite de la chaine. E1 y eprouve "la chaine marche a des points neufs", pas l'ordre 3. Seule la ligne N, par E2, oppose
les deux ordres (|ln(G3 / G2)| de %.3f a %.3f a ses etiquettes predites).""" % (
    bas(min(abs(mg[i]["d32_max"]) for i in ("P1", "P2", "P3", "P4", "P5")), 3), haut(max(abs(mg[i]["d32_min"]) for i in ("P1", "P2", "P3", "P4", "P5")), 3),
    bas(min(abs(mg[i]["d32_max"]) for i in ("N1", "N2", "N3", "N4", "N5")), 3), haut(max(abs(mg[i]["d32_min"]) for i in ("N1", "N2", "N3", "N4", "N5")), 3)))
P("""Ce qui est consigne sans etre juge : pour les etats hors du domaine, si l'ordre 3 est plus loin que l'ordre 2 ; le signe de ln q3 ; le
statut que la feuille du lecteur donne a chaque point.""")
T_()
T_("7. LES TOLERANCES, ET CE QUE LA PLUME A VU AVANT DE LES ECRIRE")
P("""Aucune largeur 2D n'existe aux douze cellules, pas meme la largeur deposee a k = 3 : dans le run unique elle nait a l'etage 1. Les
tolerances ne peuvent donc venir que de deux sources, et la plume a regarde les deux.""")
T_("  7.1 Les points deja joues")
P("""Les %d etats du domaine des douze points du delta 98 (feuille d'ordre 3 retrospective), par classe de e_bord : nombre, mediane et
plus grand |ln q3| :""" % len(dom), 4)
for (lo, hi) in sorted(cl):
    T_("      e_bord dans [%.1f, %.1f[   %2d etats   mediane %.4f   plus grand %.4f" % (lo, hi, cl[(lo, hi)][0], cl[(lo, hi)][1], cl[(lo, hi)][2]))
P("""D'ou T = 0.05 sous e_bord = 0.3 (plus grand vu : %.4f) et T = 0.10 au-dela (plus grand vu : %.4f). L'ordre 3 est plus pres que
l'ordre 2 a %d de ces %d etats. La tolerance ne descend nulle part sous la stabilite de la chaine, qui vaut au plus 0.05 dans le domaine par
definition.""" % (pire_bas, pire_haut, n_mieux, len(dom)), 4)
P("""Ces deux valeurs ont ete ecrites dans la feuille AVANT que la plume calcule les marges de 7.3 ; elles n'ont pas ete retouchees
ensuite. C'est une declaration de la plume : machine 2 ne peut pas la verifier.""", 4)
P("""Les deux ancres, deja jouees et absentes des 131 etats (leurs deux etats lus, plateau de la reference de machine 1) : a A1 (delta =
-0.05), ln q3 = %+.4f et %+.4f ; a A2 (delta = +0.05), ln q3 = %+.4f et %+.4f.""" % (a1[0], a1[1], a2[0], a2[1]), 4)
T_("  7.2 Deux regularites lues aux points deja joues (etats du domaine)")
P("""A delta < 0 (%d etats : A1, C1, C2, M1, M2), ln q3 est negatif a %d etats sur %d : l'ordre 3 corrige trop. Aux %d etats ou la
correction d'ordre 3 se lit (|ln(G3 / G2)| >= 0.05), k = -ln q3 / (ln(G3 / G2))^2 vaut de %.2f a %.2f, mediane %.2f.""" % (
    ET["n_neg"], sum(1 for x, r in dom if x["delta"] < 0 and r["ln_q3"] < 0) + sum(1 for v in a1 if v < 0), ET["n_neg"], ET["n_neg_k"], ET["k_min"], ET["k_max"], ET["k_med"]), 4)
P("""A delta > 0 (%d etats : A2, C3, C4), ln q3 est positif partout ; ln q3 / delta^2 vaut au plus %.1f (mediane %.1f), ln q3 / delta^3 au
plus %.0f (mediane %.0f). Trois points ne separent pas ces deux puissances.""" % (ET["n_pos"], haut(ET["c2_max"], 1), ET["c2_med"], math.ceil(ET["c3_max"]), ET["c3_med"]), 4)
T_("  7.3 Les chaines aux douze cellules (etiquettes predites), et les marges")
P("""Par cellule : nombre d'etats predits du domaine ; ceux a T = 0.05 ; e_bord extremes ; ln(G3 / G2) median ; puis l'attente du pire |ln
q3| par les regularites de 7.2 prises a leur valeur la plus defavorable (k = %.2f a delta < 0 ; la puissance 3 et son plus grand coefficient
a delta > 0), et la marge, T / attente.""" % ET["k_max"], 4)
for p in cel:
    r = mg[p["id"]]; a = r["attentes"]["pire"] if r["delta"] < 0 else r["attentes"]["p3_pire"]
    T_("    %-3s domaine %2d (%2d a 0.05)  e_bord %.3f a %.3f  ln(G3/G2) %+.4f  attente %.4f  marge %.2f" % (
        p["id"], r["n_domaine"], r["n_T_bas"], r["e_bord_min"], r["e_bord_max"], r["d32_med"], a["attente_pire"], a["marge"]))
P("""Lecture. La cellule N1 est le point dur : sa correction d'ordre 3 est la plus grande que la chaine ait faite dans le domaine (%.3f en
mediane, contre %.3f au plus aux points joues), et sa marge est de %.2f. Sous la valeur la plus defavorable de k, l'ordre 2 y serait plus
pres que l'ordre 3 a %d etats sur %d : E2 y tomberait. La cellule BP est sous la tolerance par une regularite (%.4f, puissance 2) et au-dessus
par l'autre (%.4f, puissance 3). Les neuf autres cellules de ligne ont une marge d'au moins %.2f.""" % (
    abs(mg["N1"]["d32_med"]), haut(max(abs(med([math.log(r["G3"] / r["G2"]) for r in x["etats"] if r["exclu"] is None and r["dans_le_domaine"]])) for x in RT["cellules"] if x["n_domaine"]), 3),
    bas(mg["N1"]["attentes"]["pire"]["marge"], 2), mg["N1"]["attentes"]["pire"]["ordre2_plus_pres"], mg["N1"]["n_domaine"], mg["BP"]["attentes"]["p2_pire"]["attente_pire"],
    mg["BP"]["attentes"]["p3_pire"]["attente_pire"],
    bas(min((mg[i]["attentes"]["pire"] if mg[i]["delta"] < 0 else mg[i]["attentes"]["p3_pire"])["marge"] for i in ("N2", "N3", "N4", "N5", "P1", "P2", "P3", "P4", "P5")), 2)), 4)
P("""Ce que la plume n'a pas vu : aux points joues, aucun etat du domaine n'a e_bord au-dessus de %.3f. Aux douze cellules, %d etats predits
du domaine sont au-dela (%d a N1, %d a BP) : la garde e_bord < 0.7 y est eprouvee pour la premiere fois.""" % (
    ET["e_bord_max_vu"], sum(r["n_au_dela_du_vu"] for r in MG["cellules"]), mg["N1"]["n_au_dela_du_vu"], mg["BP"]["n_au_dela_du_vu"]), 4)
P("""La plume n'a PAS desserre la tolerance au vu de ces marges. Elle a en revanche donne a E2 le niveau TENU SAUF UNE CELLULE apres les
avoir vues (section 14, E-2).""", 4)
T_()
T_("8. CE QUE CHAQUE ISSUE ENGAGE")
P("""L'INSTRUMENT NE TIENT PAS (feuille du lecteur, ou ancres de la sonde dense) : rien n'est juge ; l'acte le dit ; aucun rejeu sous
d'autres reglages ; une suite demande un autre gel.""")
P("""E1 TENU et E2 TENU. L'acte peut ecrire : "a douze cellules tirees au sort, la chaine d'ordre 3 rend la largeur de plateau des etats
juges du domaine a 0.05 pres en logarithme (e_bord < 0.3) et a 0.10 pres au-dela, et elle est plus pres que l'ordre 2 sur la ligne
negative". Il ne peut pas ecrire une loi en delta : un seul w2 par ligne. Le bloc d'ordre 3 peut alors etre propose au depot.""")
P("""E1 TENU SAUF UNE CELLULE, ou E2 TENU SAUF UNE CELLULE. La meme phrase, la cellule nommee. L'acte dit que la garde du domaine ne suffit
pas a cette cellule. Il ne redessine pas le domaine : aucune garde, aucun seuil n'est regle apres lecture ; un domaine plus etroit demande
un autre gel et d'autres points.""")
P("""E1 TOMBE. L'acte ecrit que la chaine d'ordre 3 ne rend pas la largeur a cette tolerance dans le domaine declare. La lecture de la note
sur la loi (%d etats du domaine, plus grand |ln q3| : %.4f) est alors declaree lue en echantillon, non confirmee hors echantillon. Le bloc d'ordre 3 n'est pas
propose au depot.""" % (len(dom), pire_haut))
P("""E2 TOMBE. L'acte ecrit qu'a des points neufs l'ordre 3 n'est pas plus pres que l'ordre 2 sur la ligne negative. L'ordre 3 n'est pas
propose comme correction de l'ordre 2.""")
P("""E3 TOMBE. Les bornes du delta 98 ne tiennent pas a des points neufs : l'acte le dit, cellule et etat nommes, et dit que l'acte du
delta 98 est borne a ses douze points.""")
P("""E1B. TENU : les deux fenetres de bord sont dans le domaine au facteur 1, a ces deux w2. TOMBE : le bord du domaine est plus pres que la
garde ne le dit, du cote nomme. Dans les deux cas c'est une observation du bord ; elle ne change pas l'issue de E1.""")
P("""NON CONCLUANT : l'acte le dit et donne les comptes ; pas de rejeu, pas de nouveau seuil.""")
P("""Dans tous les cas : la table par etat est publiee (etiquette, e_bord, stabilite, G2, G3, Gamma_pl, q2, q3, statut), les etats exclus
avec leur motif. Aucune autre definition du hamiltonien effectif, aucun autre absorbeur de chaine, aucune autre tolerance n'est essayee
apres lecture.""")
T_()
T_("9. GARDES (chaque journal dit ce qu'il ne joue pas)")
for g in ("G-1 canons en dur : moteur, blocs d'ordre 2 et 3, depot, couplages et references du temoin et des ancres, table, les quatre scripts ; un ecart arrete.",
          "G-2 la sortie dense et le verdict du lecteur sont lus au canon que le pilote vient d'ecrire dans son journal (C1).",
          "G-3 forme de la sortie dense (C2) ; provenance : sortie dense et verdict portent le canon de la table et des scripts qui les ont ecrits.",
          "G-4 ancres de la sonde dense contre le depot (4.4).",
          "G-5 instrument du lecteur : etage 0, ancres, etage 1, tels qu'au gel ter (sections 5 et 6 de ce gel-la), tolerances inchangees.",
          "G-6 pre-vol : un script lance avec --prevol refuse la table du gel ; sans --prevol il refuse toute autre table ; une sortie de pre-vol ne juge rien.",
          "G-7 une seule execution : le pilote exige un dossier neuf et joue chaque appel une fois ; un code de sortie non nul l'arrete."):
    P(g, 2, 6)
T_()
T_("10. ANNONCES DE LA PLUME (ecrites apres les calculs de la section 7 ; aucune 2D aux cellules)")
P("""Ce sont des jugements, pas des calculs : huit points deja joues ne font pas une loi d'erreur. Probabilites :""")
for a in ("A-1 (0.90) l'instrument tient (feuille du lecteur et ancres de la sonde dense).",
          "A-2 E1 : TENU 0.35 ; TENU SAUF UNE CELLULE 0.40 ; TOMBE 0.10 ; NON CONCLUANT 0.05 ; le reste (0.10) est l'instrument.",
          "A-3 la cellule qui tombe le plus probablement sous E1 est N1 : 0.45 qu'elle tombe, si elle est exploitable.",
          "A-4 E2 : TENU 0.50 ; TENU SAUF UNE CELLULE 0.30 (N1) ; TOMBE 0.05 ; NON CONCLUANT 0.05 ; le reste (0.10) est l'instrument.",
          "A-5 E3 TENU : 0.85.",
          "A-6 E1B : BN tient 0.65 ; BP tient 0.40.",
          "A-7 (0.80) a la ligne N, ln q3 est negatif pour au moins trois quarts des etats juges du domaine ; a la ligne P, positif pour au moins trois quarts."):
    P(a, 2, 6)
P("""La plume annonce donc que l'issue la plus probable n'est PAS un E1 tenu partout. Elle le gele ainsi.""")
T_()
T_("11. DEROULEMENT, E19, ET CE QUI EST PERMIS")
P("""ORDRE. (1) Machine 2 certifie cette piece, la table, les scripts derives et leurs diffs, la feuille d'ordre 3 et son banc, le pilote ;
un seul tour de correction. (2) Feu vert ecrit de l'operateur. (3) Machine 2 joue le pilote UNE fois, dans un dossier neuf. (4) Lot de
resultat : la sortie dense, les fichiers du lecteur, les deux verdicts du lecteur, le verdict d'ordre 3, les journaux, le journal du pilote.
(5) Machine 1 authentifie et rejoue les feuilles. (6) Acte.""")
P("""PRE-VOL. Avant le feu vert, machine 2 peut jouer le pilote avec --prevol sur la table de pre-vol, avec ou sans --dense : ce sont des
points deja joues. Avec --dense et le depot, le mode point doit lui rendre les mesures du fichier de C3 de son run du gel ter.""")
P("""UNE SEULE EXECUTION. Un pilote arrete par une panne se relance ENTIER dans un dossier neuf, et l'acte le dit ; aucun appel n'est rejoue
apres lecture de sa sortie.""")
P("""DEUX MACHINES. Le verdict est celui de la feuille d'ordre 3 jouee par machine 2 dans le run. Machine 1 la rejoue sur les fichiers du
lot. Les chaines different d'une machine a l'autre : %s en relatif au plus aux deux etats d'ancre (mesure de machine 1 au gel du delta
98). Un etat au ras d'une garde peut donc changer de cote. Si le verdict d'une cellule differe entre les deux machines, la lecture la MOINS favorable a l'enonce est retenue, et
l'acte donne les deux.""" % ECART_MACHINES)
P("""E19. Aucune des deux machines ne calcule en 2D a l'une des douze cellules avant le feu vert ; machine 1 n'y calcule rien en 2D avant
d'avoir recu et authentifie le lot de resultat.""")
P("""Ce gel ne se rejoue pas sous d'autres seuils, d'autres gardes, une autre chaine ou d'autres points apres lecture.""")
T_()
T_("12. COUTS (a mesurer au pre-vol de machine 2, pas a promettre)")
P("""Etage 1 : de l'ordre de %d s sur BOCAL4, par interpolation des durees du depot selon la boite (boites de %d a %d, plus les deux
ancres). Etages 2a et 2b : le run du gel ter a coute 4377 s pour 137 etats ; les tables predisent %d etats au-dessus de dix planchers aux
douze cellules. Etage 3 : de l'ordre de la minute.""" % (int(round(cout1, -2)), min(e(p)["N"] for p in cel), max(e(p)["N"] for p in cel), n_pred))
T_()
T_("13. LIMITES DECLAREES")
for l in ("""L-1 L'objet juge est UNE chaine : le bloc %s, forme symetrique (hermitienne). Essai fait, sur les chaines seules
(definition_bloch_machine1_v1.py) : la forme de Bloch, tronquee au meme ordre et mise sous le meme absorbeur. Les deux formes s'accordent
comme il se doit a petit couplage (l'ecart d'energie varie en g^%.2f, attendu 4), mais aux couplages du gel la forme de Bloch n'est pas une
chaine utilisable : a l'etat eprouve, ses deux moities du saut valent %.1f et %.1f fois la correction symetrique au dernier site de la
barriere et depassent le saut lui-meme a partir du site %d ; sa largeur varie d'un facteur %.1f avec la force de l'absorbeur (la forme
symetrique : %.3f). Aux %d etats du domaine des points joues, |ln(G_Bloch / G_sym)| vaut %.2f en mediane et jusqu'a %.1f ; la forme de Bloch
n'est plus pres du plateau qu'a %d etats. Cet essai ne chiffre donc PAS une dependance a la definition : il dit que la troncature n'a de
largeur stable que sous sa forme hermitienne. Aucune autre forme hermitienne n'a ete essayee.""" % (
    c["bloc3"], BL["C2"]["pentes"][0], BD["rapports_bord"][0], BD["rapports_bord"][1], BD["m_moitie_depasse_saut"], max(BD["G_bloch"]) / min(BD["G_bloch"]), max(BD["G_sym"]) / min(BD["G_sym"]),
    len(bj), bl_med, haut(bl_max, 1), bl_pres),
          """L-2 La reference est le lecteur du gel ter, dont l'acte est contresigne et non depose.""",
          """L-3 Seuls des etats QUALIFIES et d'etiquette nette sont juges. Un etat que le lecteur ne qualifie pas ou dont l'etiquette est floue
peut etre un etat ou la chaine echoue : la garde des deux tiers borne cet effet sans l'annuler.""",
          """L-4 L'eligibilite portait sur des etiquettes predites, justes a 189 sur 224 aux points joues (note de la carte) : une cellule peut
sortir inexploitable.""",
          """L-5 Etats au-dela du plus grand e_bord vu : 7.3.""",
          """L-6 La ligne P ne discrimine pas les deux ordres : section 6.""",
          """L-7 Les tolerances ne sortent pas d'une theorie de l'erreur : elles sont lues sur %d etats de huit points deja joues, et ne dependent de
la chaine que par e_bord.""" % (len(dom) + len(anp)),
          """L-8 Un w2 par ligne : rien n'est dit de la dependance en delta entre les lignes et les bords.""",
          """L-9 Etats au ras d'une garde : section 11, DEUX MACHINES.""",
          """L-10 Les ancres de la sonde dense eprouvent sa reproduction, pas sa justesse.""",
          """L-11 E3 applique la borne du delta 98 a la largeur de plateau, sans la marge d'un plancher que ce gel-la donnait a la lecture dense.""",
          """L-12 La stabilite est une convention : celle de l'absorbeur de la chaine et du bloc d'ordre 2 depose (premiere partie)."""):
    P(l, 2, 6)
T_()
T_("14. ECARTS DECLARES")
for l in ("""E-1 La note de la carte donnait a E3 deux volets : hors du domaine, l'ordre 2 reste dans les bandes du delta 98, et l'ordre 3 est
declare non applicable. Ici E3 porte sur tous les etats juges, dans le domaine ou non, et le second volet n'est pas un enonce : il est
consigne. La superposition des deux lignes en Gamma / |delta| a facteur egal, que la note voulait observer, n'est pas calculee par la
feuille : elle se lira dans la table par etat. Aux points joues l'ordre 3 est plus pres que l'ordre 2 aux
%d etats juges de e_bord < 0.7, dont les %d que la stabilite exclut du domaine.""" % (len(sous07), n_sous07_hors),
          """E-2 Machine 2 demandait ce qu'engage "E2 faux". La plume a donne a E2 les memes niveaux qu'a E1, dont TENU SAUF UNE CELLULE, APRES
avoir vu sur les chaines que N1 est a la limite. C'est un adoucissement fait en connaissance des marges ; machine 2 peut le refuser : c'est
une constante de la feuille.""",
          """E-3 C2 demandait l'egalite de (w2, g) a la table. La table porte w2 et le facteur ; le couplage est compare a facteur x g_du_point(w2)
a 1e-12 pres, par les scripts qui chargent le moteur.""",
          """E-4 La feuille du gel ter refusait de lire un point dont l'etat de rang 0 n'etait pas lu. La feuille derivee ne refuse plus : un seul
tel point aurait arrete toute la lecture, et ce gel ne se sert pas du statut du point.""",
          """E-5 La garde des deux tiers (section 5) et les ancres de la sonde dense (4.4) sont des ajouts de machine 1.""",
          """E-6 La premiere partie annoncait des tolerances "calculees sur les chaines aux douze cellules". Elles sont lues aux points deja joues
; ce qui est calcule aux douze cellules, ce sont les classes de e_bord, les attentes et les marges.""",
          """E-7 Le journal du pre-vol porte un canon anterieur de la feuille d'ordre 3 : 4.6.""",
          """E-8 La plume avait dit a l'operateur qu'elle chiffrerait la dependance a la definition du hamiltonien effectif en ecrivant ce gel.
Elle a essaye une autre definition ; l'essai ne rend pas un chiffre de dependance (L-1)."""):
    P(l, 2, 6)
T_()
T_("15. CE QUE MACHINE 2 CERTIFIE")
for l in ("(a) que la table gelee porte les douze cellules de SON tirage et les deux ancres ;",
          "(b) que chaque script derive ne differe de sa source certifiee que par les remplacements du script de construction ;",
          "(c) que la feuille d'ordre 3 applique les sections 5 et 6, et que son banc mord ;",
          "(d) que les nombres des sections 3 et 7 sortent des pieces ;",
          "(e) le pre-vol sur BOCAL4, avec les pieces finales ;",
          "(f) qu'elle accepte, ou refuse, les ecarts de la section 14."):
    P(l, 2, 6)
T_()
T_("-- FIN gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1 --")
txt = "\n".join(L) + "\n"; txt.encode("ascii"); assert "%" not in txt
longues = [(n + 1, len(l)) for n, l in enumerate(L) if len(l) > 100]; assert not longues, longues
assert not any(l != l.rstrip() for l in L)
open(SORTIE, "w", encoding="ascii", newline="\n").write(txt)
print("ecrit %s : %d lignes, canon %s" % (SORTIE, len(L), canon(SORTIE)))
