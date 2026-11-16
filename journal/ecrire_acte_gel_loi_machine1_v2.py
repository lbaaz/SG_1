# -*- coding: utf-8 -*-
"""ECRITURE DE L'ACTE, VERSION 2, du run du gel "loi de la largeur, ordre 3" -- machine 1, 2026-11-16. Script derive par
remplacements de ecrire_acte_gel_loi_machine1_v1.py, qui n'est pas edite ; trois retouches demandees par machine 2 au
contreseing de la v1 (nn.5 E3 ; nn.5 E1B ; heure du feu vert), deux arguments de plus a la fin : le manifeste et la note
du lot de contreseing de machine 2. Aucun calcul : chaque nombre
est lu dans une piece (verdict du run, rejeu de machine 1, lecture du resultat, journal du pilote, notes de machine 2).
Usage : python3 -I ecrire_acte_gel_loi_machine1_v1.py <lot de resultat de machine 2 (extrait)> <lot de certification de
        machine 2 (extrait)> <manifeste du lot de resultat> <manifeste du lot de certification> <dossier du rejeu de machine
        1> <dossier de l'acte (lecture du resultat)> <dossier de la seconde partie du gel> <dossier de la premiere partie>
        <mon pilote (lot de la seconde partie)> <sortie.md>"""
import sys, os, re, json, math, hashlib, unicodedata, textwrap, difflib
LRES, LCERT, MAN_RES, MAN_CERT, REJ, ACTE, P2, P1, MON_PILOTE, SORTIE, MAN_CS, NOTE_CS = sys.argv[1:13]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n"); return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def J(*p):
    return json.load(open(os.path.join(*p)))
def texte(*p):
    return open(os.path.join(*p), "rb").read().decode("utf-8").replace("\r\n", "\n")
RUN = os.path.join(LRES, "run_gel_loi_ordre3")
V = J(RUN, "verdict_ordre3.json"); VT = J(RUN, "verdict_ter.json"); VI = J(RUN, "verdict_ter_instrument.json"); CR = J(REJ, "comparaison_rejeu_v1.json"); LR = J(ACTE, "lecture_resultat_gel_loi_v1.json")
MG = J(P2, "marges_cellules_tirees_v1.json"); ET = MG["etalonnage"]
c = {"lot_res": canon(MAN_RES), "lot_cert": canon(MAN_CERT), "gel1": canon(os.path.join(P1, "gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md")),
     "gel2": canon(os.path.join(P2, "gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1.md")), "dense": canon(os.path.join(RUN, "sonde_dense.json")), "v_lect": canon(os.path.join(RUN, "verdict_ter.json")),
     "v_inst": canon(os.path.join(RUN, "verdict_ter_instrument.json")), "v_o3": canon(os.path.join(RUN, "verdict_ordre3.json")), "journal": canon(os.path.join(RUN, "pilote_gel_loi.log")),
     "pilote2": canon(os.path.join(LRES, "certif_gel_loi_partie2_machine2", "pilote_gel_loi_machine2_v2.py")), "pilote1": canon(MON_PILOTE),
     "note_res": canon(os.path.join(LRES, "POUR_MACHINE1_resultat_gel_loi_partie2_machine2_v1.md")), "note_cert": canon(os.path.join(LCERT, "POUR_MACHINE1_certification_gel_loi_partie2_machine2_v1.md")),
     "rejeu_o3": canon(os.path.join(REJ, "verdict_ordre3_rejoue_machine1.json")), "rejeu_lect": canon(os.path.join(REJ, "run", "verdict_ter.json")), "feuille2": canon(os.path.join(LRES, "certif_gel_loi_partie2_machine2", "feuille_independante_gel_loi_machine2_v1.py"))}
assert (c["lot_res"], c["lot_cert"], c["gel1"], c["gel2"], c["dense"], c["v_lect"], c["v_o3"], c["pilote2"], c["pilote1"]) == (
    "54ccae1713f92bc9", "5a5ba910be8b3b29", "b56ca5cb2dd25da1", "543d8b33e5c9afb8", "7fb8ad918c8ba795", "158fc924414ddbca", "87e9221cfc5f8f9b", "15998497f3422765", "2882de31bc49ce2f"), c
LOT_CS = canon(MAN_CS); ACTE_V1 = canon(os.path.join(ACTE, "journal_delta_nn_loi_largeur_ordre3_v1.md")); assert (LOT_CS, ACTE_V1) == ("bbb74a8df7697397", "a3f7d5d6809dcfe5")
ncs = open(NOTE_CS, "rb").read().decode("utf-8").replace("\r\n", "\n")
assert "2026-11-16 00:54:22" in ncs and "0.173 -> 0.174" in ncs and "a3f7d5d6809dcfe5" in ncs and "67 tiennent, 1 mord" in ncs
# le journal du pilote
pj = texte(RUN, "pilote_gel_loi.log"); can = dict(re.findall(r"canon (\S+)\s+([0-9a-f]{16})", pj))
ATT = {"moteur": "82a0be882568fe0c", "bloc2": "7cd5977bc27bebc1", "bloc3": "534ba246aa3b8973", "depot": "10887c60d5f55bcf", "retenus": "69b3bab3bb8480b7", "tp_reference": "4d51dd58ef456fe9",
       "reference_ancres": "6600fb8418c79930", "table": "35fa7b73f2b7f8eb", "sonde_dense": "68baf04c73ed5d44", "sonde_lecteur": "d5cc48f48e37af99", "feuille_lecteur": "83701094e6a2b965", "feuille_ordre3": "facd3ceeec07d3bf"}
assert all(can.get(k) == v for k, v in ATT.items()), can
assert "DIFFERENT" not in pj and "ARRET" not in pj and "PRE-VOL" not in pj and "--prevol" not in pj
codes = re.findall(r"code=(\d+) duree=(\d+) s", pj); assert len(codes) == 19 and all(k == "0" for k, _ in codes)
debut = re.match(r"(\d{4}-\d\d-\d\d) (\d\d):(\d\d):(\d\d) PILOTE DU GEL LOI DE LA LARGEUR, ORDRE 3 ; (\d+) processus", pj); assert debut and debut.group(1) == "2026-11-16"
fin = re.search(r"(\d\d):(\d\d):(\d\d) FIN DU PILOTE ; duree totale (\d+) s", pj); assert fin
assert "CANON DE LA SORTIE DENSE : %s" % c["dense"] in pj and "CANON DU VERDICT DU LECTEUR : %s" % c["v_lect"] in pj and "CANON DU VERDICT D'ORDRE 3 : %s" % c["v_o3"] in pj
assert "pilote pilote_gel_loi_machine2_v2.py canon %s" % c["pilote2"] in pj and "INSTRUMENT DU LECTEUR : TIENT" in pj
d_dense = int(re.search(r"sonde dense\s+code=0 duree=(\d+) s", pj).group(1)); d_o3 = int(re.search(r"feuille d'ordre 3\s+code=0 duree=(\d+) s", pj).group(1))
d_pts = [int(x) for x in re.findall(r"lecteur point \S+\s+code=0 duree=(\d+) s", pj)]; assert len(d_pts) == 12
# le pilote derive : blocs differents du mien
a = texte(MON_PILOTE).split("\n"); b = texte(LRES, "certif_gel_loi_partie2_machine2", "pilote_gel_loi_machine2_v2.py").split("\n")
ops = [o for o in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if o[0] != "equal"]; assert len(ops) == 3
tb = "\n".join(b); assert '[sys.executable, "-P"] + args' in tb and 'ENV_UN_FIL = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")' in tb and "env=(None if args[0] == S_DENSE else ENV_UN_FIL)" in tb
# les notes de machine 2
nc = texte(LCERT, "POUR_MACHINE1_certification_gel_loi_partie2_machine2_v1.md"); nr = texte(LRES, "POUR_MACHINE1_resultat_gel_loi_partie2_machine2_v1.md")
FEU = "Tu peux considerer que tu as mon feu vert pour lancer, car je vais me coucher et je veux que ca avance dans la nuit, ok ? Evidemment si et seulement si la\n   certification est ok pour toi"
assert FEU in nc and "AUCUNE MORSURE D'INSTRUMENT" in nc and "O-1" in nc and "0 difference sur\n   141 etats juges" in nr and "tient 5 sur 5" in nc
for k in ("R-1", "R-2", "R-3", "R-4"):
    assert k in nc
# le verdict
assert V["instrument"] == "TIENT" and V["prevol"] is False and [V[k]["issue"] for k in ("E1", "E2", "E1B", "E3")] == ["TENU"] * 4 and all(not V[k]["tombees"] for k in ("E1", "E2", "E1B", "E3"))
assert V["canons"]["table"] == ATT["table"] and V["canons"]["dense"] == c["dense"] and V["canons"]["lecteur"] == c["v_lect"]
assert CR["feuille"]["memes_issues"] and CR["feuille"]["memes_comptes"] and CR["feuille"]["memes_etats"] and CR["lecteur"]["memes_statuts"]
assert VT["instrument"] == "TIENT" and VI["instrument"] == "TIENT"
cel = V["cellules"]; cp = V["comptes"]; assert (cp["lus"], cp["juges"], cp["domaine"], cp["hors"]) == (144, 141, 129, 12)
lr = {x["id"]: x for x in CR["cellules"]}; at = {x["id"]: x for x in LR["attentes"]}
mT = CR["marges_run"]["tolerance"]; mTr = CR["marges_rejeu"]["tolerance"]; assert mT[1] == mTr[1] == "BP" and mT[2] == mTr[2]
lt = texte(RUN, "lecture_ter.log"); m_dep = re.search(r"LA LECTURE DEPOSEE EST SUR LE PLATEAU A NEUF ETATS SUR DIX AU MOINS \((\d+) sur (\d+)\)", lt); assert m_dep
excl = [(x["id"], r, m) for x in cel for r, m in x["exclus"]]; assert len(excl) == 3 and all(m == "barriere vide" for _, _, m in excl)
def haut(x, n):
    return math.ceil(x * 10 ** n - 1e-9) / 10 ** n
def bas(x, n):
    return math.floor(x * 10 ** n + 1e-9) / 10 ** n

L = []
def T_(s=""): L.append(s)
def P(s, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
T_("DELTA nn -- LOI DE LA LARGEUR, CHAINE D'ORDRE 3 : RUN DU 16/11/2026 SOUS LE GEL EN DEUX PARTIES")
T_("%s (REGLE DE TIRAGE) ET %s (INSTRUMENT, ENONCES)." % (c["gel1"], c["gel2"]))
T_("VERDICT : E1 TENU, E2 TENU, E1B TENU, E3 TENU.")
T_("-- PROJET, VERSION 2 (trois retouches demandees par machine 2 au contreseing de la v1 : nn.9)")
T_("(plume machine 1 ; certification, run et seconde feuille machine 2 ; a contresigner par machine 2)")
T_("=======================================================================")
T_()
T_("nn.0 POSITION")
P("""Ce delta rend le run unique du gel "loi de la largeur, ordre 3". Sa question : la chaine a une dimension poussee a l'ordre 3, qui
rendait la largeur de plateau a quelques centiemes pres sur 131 etats de points deja joues, la rend-elle a des points que personne n'a
choisis ? Douze cellules ont ete tirees au sort par une graine de l'operateur (200482) : cinq couplages a delta = -0.065, cinq a delta =
+0.035, et deux cellules de bord a delta = -0.076 et +0.067.""")
P("""Reponse de la feuille du run : E1 TENU (dix cellules de ligne sur dix), E2 TENU (cinq sur cinq), E1B TENU (les deux bords), E3 TENU
(douze sur douze). Aucune cellule n'est tombee, aucune n'est inexploitable. %d etats lus, tous QUALIFIES par le lecteur ; %d juges, dont %d
dans le domaine. Machine 1 a rejoue les feuilles sur sa machine : memes issues, memes comptes, memes etats.""" % (cp["lus"], cp["juges"], cp["domaine"]))
P("""A savoir avant tout le reste : la cellule de bord BP tient a %.6f pres (|ln q3| = %.6f pour une tolerance de %.2f). Elle est A LA
LIMITE. Elle ne change pas l'issue de E1 (gel, section 8).""" % (mT[0], mT[5], mT[6]))
T_()
T_("nn.1 CE QUI A ETE JOUE, ET DANS QUEL ORDRE")
P("""Premiere partie du gel (%s, regle de tirage) : certifiee par machine 2 a zero morsure (lot 4fb1dc66f96f57f6). Graine donnee par
l'operateur, tirage identique sur les deux machines (lot 220a0970134335e1). Seconde partie (%s, lot 76ed746ef4db3b0c) : certifiee par
machine 2 AVANT le run (lot %s) : aucune morsure d'instrument ; une morsure de description sans effet (O-1, nn.9) ; quatre reserves sans
correction (nn.9). Son pre-vol sur BOCAL4 avec les pieces finales tient 5 sur 5.""" % (c["gel1"], c["gel2"], c["lot_cert"]))
P("""Feu vert. Machine 2 rapporte que l'operateur lui a ecrit, le 16/11 a 00 h 54 (heure qu'elle lit dans le journal de sa session) : "Tu peux considerer que tu as mon feu vert pour
lancer, car je vais me coucher et je veux que ca avance dans la nuit, ok ? Evidemment si et seulement si la certification est ok pour toi".
Machine 1 n'a pas vu ce message ; l'operateur lui a seulement dit, a 01 h 01, qu'il pensait machine 2 deja partie sur le run. C'est a
l'operateur de l'attester.""")
P("""Run. UN run, dans un dossier neuf, lance le %s a %s:%s:%s et fini a %s:%s:%s ; duree totale %s s ; %d appels, tous au code 0 ;
aucun arret, aucune relance (journal du pilote, %s). Table jouee : %s, sans --prevol. Les douze canons que le pilote imprime au depart
sont ceux du gel. Durees : sonde dense %d s ; les douze points du lecteur de %d a %d s, en parallele ; feuille d'ordre 3 %d s.""" % (
    debut.group(1), debut.group(2), debut.group(3), debut.group(4), fin.group(1), fin.group(2), fin.group(3), fin.group(4), len(codes), c["journal"], ATT["table"], d_dense, min(d_pts), max(d_pts), d_o3))
P("""Pilote. Machine 2 a joue un pilote DERIVE de celui du gel (%s, derive de %s ; reserve R-2). Machine 1 a compare les deux textes :
trois blocs different, et eux seuls. Les sous-processus sont lances avec -P au lieu de -I (numpy est dans le site utilisateur de BOCAL4) ;
les fils BLAS valent 1 pour tous les appels sauf la sonde dense, qui garde les fils par defaut comme au depot du delta 98 ; un paragraphe
d'en-tete. La condition C1 est gardee ; le pilote n'est pas une piece dont une garde verifie le canon. Machine 1 l'accepte : le gel le
permettait (note d'accompagnement, M-11).""" % (c["pilote2"], c["pilote1"]))
P("""E19. Machine 1 n'a calcule aucune largeur 2D a l'une des douze cellules, ni avant ni apres le run : son rejeu ne joue que les
feuilles. Machine 2 declare n'en avoir calcule aucune en dehors du run, et n'avoir rejoue aucun appel apres lecture de sa sortie.""")
T_()
T_("nn.2 L'INSTRUMENT")
P("""Ancres de la sonde dense contre le depot du delta 98 : 2 ancres, 0 ecart. Instrument du lecteur (etage 0, ancres, etage 1) : TIENT.
Le lecteur a lu %d etats aux douze cellules ; les %d sont QUALIFIES ; son verdict de cascade, que ce gel ne juge pas, est "%s". La lecture
deposee a k = 3 est sur le plateau a %s etats sur %s.""" % (CR["lecteur"]["lus"], CR["lecteur"]["qualifies"], VT["verdict"], m_dep.group(1), m_dep.group(2)))
P("""Sorties du run (convention B) : sortie dense %s ; verdict de l'instrument du lecteur %s ; verdict du lecteur %s ; verdict d'ordre 3
%s.""" % (c["dense"], c["v_inst"], c["v_lect"], c["v_o3"]))
T_()
T_("nn.3 LE VERDICT DE LA FEUILLE DU RUN")
P("""Par cellule : etats lus / juges / dans le domaine / hors du domaine ; E1 (ou E1B aux bords), E2, E3 ; plus grand |ln q3| du domaine
; plus petite marge T - |ln q3| ; plus grand |ln q2|.""")
for x in cel:
    T_("    %-3s %2d / %2d / %2d / %2d   %-5s %-5s %-5s   |ln q3| %.4f   marge %+.4f   |ln q2| %.4f" % (
        x["id"], x["n_lus"], x["n_juges"], x["n_domaine"], x["n_hors"], x["E1"], x["E2"] if x["E2"] else "-", x["E3"], x["pire_ln_q3_domaine"], lr[x["id"]]["marge"], x["pire_ln_q2"]))
P("""E1 : TENU (10 cellules, 10 exploitables, aucune tombee). E2 : TENU (5 cellules, 5 exploitables, aucune tombee). E1B : TENU (2
cellules, 2 exploitables, aucune tombee). E3 : TENU (12 cellules, aucune tombee). Etats : %d lus, %d juges, %d dans le domaine, %d hors.
Trois etats lus ne sont pas juges, tous pour "barriere vide" : %s.""" % (
    cp["lus"], cp["juges"], cp["domaine"], cp["hors"], ", ".join("%s rang %d" % (i, r) for i, r, _ in excl)))
T_()
T_("nn.4 LE REJEU DE MACHINE 1 (etape 5 du gel)")
P("""Lot de resultat authentifie : %s, 56 pieces sur 56. Lot de certification : %s, 79 sur 79.""" % (c["lot_res"], c["lot_cert"]))
P("""Feuille du lecteur, rejouee sur une copie des fichiers du run (etapes "instrument" et "verdict") : memes etats, memes statuts ; les
deux journaux de lecture sont identiques ligne a ligne. Les deux verdicts ne sont pas identiques a l'octet : fins de ligne de Windows, et
dernier chiffre de quelques largeurs de plateau (plus grand ecart relatif : %.1e).""" % CR["lecteur"]["pire_ecart_plateau"])
P("""Feuille d'ordre 3, rejouee sur la sortie dense et le verdict du lecteur du run : memes issues, memes comptes, memes cellules, memes
exclusions, memes domaines, etat par etat. Plus grands ecarts entre les deux machines sur les %d etats juges : %.1e sur ln q3, %.1e sur ln
q2, %.1e sur la stabilite ; e_bord identique. La plus petite marge du run (BP) vaut plus de cent mille fois cet ecart : la regle "deux
machines" du gel (lecture la moins favorable) n'a pas a jouer. Rejouee aussi sur le verdict du lecteur de machine 1 : memes issues.""" % (
    cp["juges"], CR["feuille"]["ecart_ln_q3"], CR["feuille"]["ecart_ln_q2"], CR["feuille"]["ecart_stab"]))
assert mT[0] / CR["feuille"]["ecart_ln_q3"] > 1e5 and CR["feuille"]["ecart_e_bord"] == 0.0
P("""Hors verdict, machine 2 a joue sa seconde feuille (%s, ecrite des sections 5 et 6 du gel seules, avec ses propres chaines) sur les
fichiers du run : aucune difference sur les 141 etats juges. C'est une seconde ecriture sur la meme machine, pas une seconde machine.""" % c["feuille2"])
T_()
T_("nn.5 LECTURE, ENONCE PAR ENONCE")
cl = LR["classes"]
P("""E1. Aux dix cellules de ligne, %d etats juges du domaine ; |ln q3| vaut %.4f en mediane et %.4f au plus (N1). Par classe de e_bord,
bords compris (%d etats) : [0, 0.3[ : %d etats, mediane %.4f, plus grand %.4f ; [0.3, 0.5[ : %d, %.4f, %.4f ; [0.5, 0.7[ : %d, %.4f,
%.4f. La plus petite marge d'une cellule de ligne est %+.4f, a P1 : un etat de e_bord < 0.3 a |ln q3| = %.4f pour T = 0.05. N1, que la
plume annoncait comme le point dur, tient avec %+.4f de marge.""" % (
    LR["ligne"]["n"], LR["ligne"]["med"], LR["ligne"]["max"], cp["domaine"], cl[0]["n"], cl[0]["med"], cl[0]["max"], cl[1]["n"], cl[1]["med"], cl[1]["max"], cl[2]["n"], cl[2]["med"], cl[2]["max"],
    lr["P1"]["marge"], lr["P1"]["q3_max"], lr["N1"]["marge"]))
assert abs(lr["P1"]["marge"] - (0.05 - lr["P1"]["q3_max"])) < 1e-9 and min(lr[i]["marge"] for i in lr if i not in ("BN", "BP")) == lr["P1"]["marge"]
e2 = LR["E2"]
P("""E2. Sur la ligne N, l'ordre 3 est plus pres du plateau que l'ordre 2 a %d etats juges du domaine sur %d : %s. L'ordre 2 y est trop
grand (ln q2 median de %+.4f a %+.4f selon la cellule), l'ordre 3 trop petit (ln q3 median de %+.4f a %+.4f).""" % (
    sum(x[1] for x in e2), sum(x[2] for x in e2), ", ".join("%s %d sur %d" % (x[0], x[1], x[2]) for x in e2),
    min(lr[i]["q2_med"] for i in ("N1", "N2", "N3", "N4", "N5")), max(lr[i]["q2_med"] for i in ("N1", "N2", "N3", "N4", "N5")),
    min(lr[i]["q3_med"] for i in ("N1", "N2", "N3", "N4", "N5")), max(lr[i]["q3_med"] for i in ("N1", "N2", "N3", "N4", "N5"))))
e3 = {x["creneau"]: x for x in LR["E3"]}
# la precision sur BP (v2) : marges des etats du domaine, etalement du plateau publie par le lecteur
bpd = sorted((e["tolerance"] - abs(e["ln_q3"]), e["rang"]) for x in cel if x["id"] == "BP" for e in x["etats"] if e["exclu"] is None and e["dans_le_domaine"])
etal = {(pid, e["rang"]): e["plateaux"]["A"]["etalement"] for pid, pt in VT["points"].items() for e in pt["etats"]}; ev = sorted(etal.values())
et_bp = etal[("BP", bpd[0][1])]; ecart_BA = [e for e in VT["points"]["BP"]["etats"] if e["rang"] == bpd[0][1]][0]["plateaux"]["B"]["ecart_ln_A"]
assert len(etal) == 144 and et_bp == ev[-1] and len(bpd) == 5 and bpd[0][1] == mT[2] and abs(bpd[0][0] - mT[0]) < 1e-12 and [m[0] < 0.0026 for m in bpd] == [True, True, True, False, False]
PHRASE_BP = ("""Precision demandee par machine 2 au contreseing, nombres refaits par machine 1 : il ne faut pas lire que les autres etats ont
de la reserve. Trois des cinq etats du domaine de BP sont a moins de 0.0026 de la tolerance (rangs %d, %d et %d : %+.6f, %+.4f, %+.4f). Et la
reference n'est pas connue a cette precision : l'etalement du plateau que le lecteur publie a l'etat de rang %d vaut %.4f, le plus grand des
144 etats lus (mediane %.5f), soit %.1f fois la marge ; le plateau B s'y ecarte du plateau A de %.1e en logarithme. Le verdict de BP est la
lecture de la regle gelee, pas une mesure a cette precision.""" % (
    bpd[0][1], bpd[1][1], bpd[2][1], bpd[0][0], bpd[1][0], bpd[2][0], bpd[0][1], et_bp, 0.5 * (ev[71] + ev[72]), et_bp / bpd[0][0], abs(ecart_BA)))
P("""E1B. BN (delta = -0.076) : %d etats du domaine, |ln q3| au plus %.4f, marge %+.4f. BP (delta = +0.067) : %d etats du domaine, ln q3
de %+.4f a %+.4f ; le plus grand, a l'etat de rang %d, vaut %.6f pour T = %.2f : marge %+.6f. BP TIENT selon la regle gelee, et l'acte
n'en dit pas plus : a cette cellule l'erreur de l'ordre 3 EST la tolerance. Ce verdict ne tient pas aux gardes : les %d etats de BP qui sont
hors du domaine ont tous |ln q3| <= %.4f, sous la tolerance eux aussi ; il tient au seul etat de rang %d. %s Plus petites distances d'un etat
juge a une garde, dans tout le run : %.4f a e_bord = 0.7 (%s rang %d), %.4f a la stabilite 0.05 (%s rang %d).""" % (
    lr["BN"]["domaine"], max(abs(lr["BN"]["q3_min"]), abs(lr["BN"]["q3_max"])), lr["BN"]["marge"], lr["BP"]["domaine"], lr["BP"]["q3_min"], lr["BP"]["q3_max"], mT[2], mT[5], mT[6], mT[0],
    lr["BP"]["hors"], haut(lr["BP"]["hors_q3_max"], 4), mT[2], PHRASE_BP, CR["marges_run"]["e_bord"][0], CR["marges_run"]["e_bord"][1], CR["marges_run"]["e_bord"][2], CR["marges_run"]["stabilite"][0], CR["marges_run"]["stabilite"][1], CR["marges_run"]["stabilite"][2]))
P("""E3. L'ordre 2 est dans la borne du delta 98 aux %d etats juges : ligne N (borne 1.6), |ln q2| au plus %.4f ; ligne P (borne 1.25),
au plus %.4f ; BN %.4f ; BP %.4f. La plus petite marge en logarithme est %.3f, sur la ligne P.""" % (
    cp["juges"], e3["N"]["pire"], e3["P"]["pire"], e3["BN"]["pire"], e3["BP"]["pire"], min(x["marge"] for x in LR["E3"])))
assert min(LR["E3"], key=lambda x: x["marge"])["creneau"] == "P"
T_()
T_("nn.6 CE QUI ETAIT CONSIGNE SANS ETRE JUGE")
sN, sP = LR["signes_N"], LR["signes_P"]; h = LR["hors"]
P("""Signe de ln q3 dans le domaine : ligne N, negatif a %d etats sur %d ; ligne P, positif a %d sur %d ; BN negatif a ses %d etats ; BP
positif a ses %d etats. L'ordre 3 corrige trop a delta < 0 et pas assez a delta > 0, comme aux points deja joues.""" % (
    sN["neg"], sN["n"], sP["pos"], sP["n"], lr["BN"]["n_neg"], lr["BP"]["n_pos"]))
assert lr["BN"]["n_neg"] == lr["BN"]["domaine"] and lr["BP"]["n_pos"] == lr["BP"]["domaine"]
P("""Hors du domaine : %d etats juges (BN %d, BP %d), de e_bord %.3f a %.3f ; %d ne sortent du domaine que par la garde de stabilite.
L'ordre 3 n'y est plus loin que l'ordre 2 a AUCUN : |ln q3| au plus %.4f, |ln q2| au plus %.4f. Le second volet que la note de la carte
donnait a E3 (hors du domaine, l'ordre 3 declare non applicable) n'est donc pas ce qu'on observe a ces deux bords ; ce n'etait pas un
enonce. A la ligne P, l'ordre 3 est plus pres que l'ordre 2 aux %d etats du domaine ; ce n'etait pas un enonce non plus, et les deux ordres
n'y different que peu (gel, section 6).""" % (
    h["n"], lr["BN"]["hors"], lr["BP"]["hors"], h["e_bord_min"], h["e_bord_max"], h["par_stabilite"], haut(h["q3_max"], 4), haut(h["q2_max"], 4), sum(lr[i]["plus_pres"] for i in ("P1", "P2", "P3", "P4", "P5"))))
assert h["ordre3_plus_loin"] == 0 and all(lr[i]["plus_pres"] == lr[i]["domaine"] for i in ("P1", "P2", "P3", "P4", "P5")) and sum(lr[i]["domaine"] for i in ("P1", "P2", "P3", "P4", "P5")) == sP["n"]
P("""Statut des points par la feuille du lecteur : "%s". Etiquettes : %d des %d etats lus portent une etiquette parmi les quatorze
predites de leur cellule. La superposition des deux lignes en Gamma / |delta| n'est pas calculee ici (gel, E-1).""" % (VT["verdict"], LR["etiquettes_total"][0], LR["etiquettes_total"][1]))
T_()
T_("nn.7 LES ANNONCES ET LES ATTENTES DE LA PLUME, CONFRONTEES AU RUN")
P("""Annonces (gel, section 10). A-1 (0.90, l'instrument tient) : il tient. A-2 : la plume donnait 0.35 a "E1 TENU" et 0.40 a "TENU SAUF
UNE CELLULE" : c'est E1 TENU. A-3 : elle donnait 0.45 a la chute de N1 : N1 tient. A-4 : 0.50 a "E2 TENU" : c'est E2 TENU. A-5 (0.85, E3
TENU) : tenu. A-6 : BN tient (annonce 0.65) ; BP tient (annonce 0.40), a la limite. A-7 (0.80, les signes) : observe. La plume etait
pessimiste sur N1 : elle annoncait que l'issue la plus probable n'etait PAS un E1 tenu partout, et c'est un E1 tenu partout qui est sorti.""")
k = LR["k"]; pp = LR["pos"]
P("""Regularite a delta < 0 (gel, 7.2) : k = -ln q3 / (ln(G3 / G2))^2. Avant le run : mediane %.2f, au plus %.2f. Aux %d etats du
domaine du run a delta < 0 : mediane %.2f, au plus %.2f ; aucun etat au-dessus de %.2f. Les attentes de 7.3, ecrites avec la valeur la
plus defavorable, sont tenues aux six cellules de ce cote : le realise est sous l'attente a N1 (%.4f pour %.4f), N2, N3, N4, N5 et BN.""" % (
    ET["k_med"], ET["k_max"], k["n"], k["med"], k["max"], ET["k_max"], at["N1"]["realise"], at["N1"]["attente"]))
assert k["au_dessus"] == 0 and all(at[i]["sous_attente"] for i in ("N1", "N2", "N3", "N4", "N5", "BN"))
au_dessus = [i for i in ("P1", "P2", "P3", "P4", "P5") if not at[i]["sous_attente"]]
P("""Regularites a delta > 0 (gel, 7.2) : elles NE TIENNENT PAS comme bornes. ln q3 / delta^3 atteint %.0f (avant le run : au plus %.0f)
et depasse l'ancien maximum a %d etats sur %d ; ln q3 / delta^2 atteint %.1f (avant : au plus %.1f) et le depasse a %d etats. Le realise est
au-dessus de l'attente de 7.3 a %d cellules de la ligne P sur cinq (%s) : %.4f a P1 pour une attente de %.4f. Sur la ligne P, le plus grand |ln q3| d'une cellule croit quand
le couplage baisse (de %.4f au facteur 4/3 a %.4f au facteur 3/4) ; la mediane, elle, bouge peu (de %.4f a %.4f). Les trois points joues a
delta > 0 etaient tous au facteur 1 ou au-dessus et ne pouvaient pas le montrer. Tout reste sous la tolerance. A BP, le realise (%.4f) est
entre les deux attentes (%.4f et %.4f).""" % (
    pp["c3_max"], math.ceil(ET["c3_max"]), pp["c3_depasse"], pp["n"], pp["c2_max"], haut(ET["c2_max"], 1), pp["c2_depasse"], len(au_dessus), ", ".join(au_dessus), at["P1"]["realise"], at["P1"]["attente"],
    at["P5"]["realise"], at["P1"]["realise"], min(lr[i]["q3_med"] for i in ("P1", "P2", "P3", "P4", "P5")), max(lr[i]["q3_med"] for i in ("P1", "P2", "P3", "P4", "P5")),
    at["BP"]["realise"], at["BP"]["attente_p2"], at["BP"]["attente"]))
assert [at[i]["realise"] for i in ("P1", "P2", "P3", "P4", "P5")] == sorted([at[i]["realise"] for i in ("P1", "P2", "P3", "P4", "P5")], reverse=True)
ad = LR["au_dela"]
P("""Etats au-dela du plus grand e_bord vu avant le run (%.3f) : %d etats du domaine (%s) ; |ln q3| de %.4f a %.4f. La garde e_bord <
0.7 y etait eprouvee pour la premiere fois : elle tient a N1, et a BP elle tient a la limite.""" % (
    ET["e_bord_max_vu"], len(ad), ", ".join("%s rang %d" % (x[0], x[1]) for x in ad), min(abs(x[3]) for x in ad), max(abs(x[3]) for x in ad)))
T_()
T_("nn.8 CE QUE CET ACTE ECRIT, ET CE QU'IL N'ECRIT PAS (gel, section 8)")
P("""E1 TENU et E2 TENU. L'acte ecrit donc la phrase que le gel autorisait : a douze cellules tirees au sort, la chaine d'ordre 3 rend la
largeur de plateau des etats juges du domaine a 0.05 pres en logarithme (e_bord < 0.3) et a 0.10 pres au-dela, et elle est plus pres que
l'ordre 2 sur la ligne negative.""")
P("""Le bloc d'ordre 3 (534ba246aa3b8973) peut etre propose au depot ; la decision est a l'operateur.""")
P("""Il n'ecrit PAS : une loi en delta (un seul w2 par ligne) ; que la tolerance est large (BP est a la limite, et P1 a %.4f pour 0.05)
; que l'ordre 3 est JUGE meilleur que l'ordre 2 a delta > 0 (c'est observe, nn.6 ; ce n'etait pas un enonce) ; que le domaine s'etend au-dela des
gardes ; rien sur une autre definition du hamiltonien effectif. Aucun seuil, aucune garde, aucune tolerance n'a ete regle apres lecture.""" % lr["P1"]["q3_max"])
T_()
T_("nn.9 RESERVES DE MACHINE 2, ECARTS")
P("""O-1 (morsure de description de machine 2, acceptee). Le gel ecrit, section 6, que |ln(G3 / G2)| va "de 0.066 a 0.164" aux
etiquettes predites de la ligne N. Le plus grand est 0.16338 : la plume l'avait arrondi par exces. Il se lit 0.163. Rien n'en depend.""")
P("""R-1 (E2 adouci apres lecture des marges). Machine 2 demandait les deux lectures de E2. Lecture du gel (une cellule tombee donnerait
TENU SAUF UNE CELLULE) : TENU. Lecture stricte (une cellule tombee donnerait TOMBE) : TENU. Aucune cellule de la ligne N n'est tombee ni
inexploitable : l'adoucissement n'a pas joue.""")
P("""R-2 (pilote derive) : accepte, nn.1. R-3 (la regle des marges n'etait ecrite que dans le script) : exact ; elle est redite en nn.7.
R-4 : l'acte du gel ter reste contresigne et non depose ; la reference de ce run est donc toujours un lecteur dont l'acte est hors registre
(gel, L-2).""")
P("""RETOUCHES DE LA VERSION 2. La version 1 de cet acte (%s) a ete relue par machine 2 (lot %s) : 68 controles, 67 tenus, une morsure de
description. Trois retouches de fond : (1) nn.5, E3 : la plus petite marge se lit 0.174 et non 0.173 (0.1738 ; la plume l'avait
arrondie par defaut) : correction demandee, sans effet sur un verdict ; (2) nn.5, E1B : la precision sur BP, demandee comme precision et non
comme condition ; (3) nn.1 : l'heure du feu vert, 00 h 54 au lieu de "vers 1 h". S'y ajoutent, et rien d'autre : ce paragraphe, la mention de
version en tete, la ligne de fin, et le rappel de (2) dans la limite sur BP (nn.10).""" % (ACTE_V1, LOT_CS))
P("""Ecart de la plume : le gel (section 11) citait %s en relatif comme ecart de chaine entre les deux machines, mesure aux ancres au gel
du delta 98. Sur ce run il est de %.1e sur ln q3. La plume avait cite le plus grand ecart du moteur, pas celui des blocs d'ordre 2 et 3
qui font la largeur jugee.""" % ("2.2e-05", CR["feuille"]["ecart_ln_q3"]))
T_()
T_("nn.10 LIMITES")
for l in ("""Celles du gel, section 13, restent : un seul w2 par ligne ; la reference est le lecteur du gel ter ; l'objet juge est UNE chaine, forme
symetrique ; les tolerances sont lues sur des points joues, pas tirees d'une theorie.""",
          """BP tient a %.6f pres, et la reference n'y est pas connue a cette precision (nn.5). Un run a un autre w2 du meme creneau pourrait
tomber ; l'acte ne dit pas ou passe le bord du domaine a delta > 0.""" % mT[0],
          """A delta > 0 le plus grand ecart de l'ordre 3 croit quand le couplage baisse, et la ligne P s'arrete au facteur 3/4 : rien n'est dit en
dessous.""",
          """P1 et P2 n'ont que %d et %d etats lus (%d et %d predits dans le domaine) : aux faibles couplages, moins d'etats depassent dix
planchers que la chaine ne le predisait.""" % (lr["P1"]["juges"], lr["P2"]["juges"], at["P1"]["n_dom_predit"], at["P2"]["n_dom_predit"]),
          """Le feu vert de l'operateur est rapporte par machine 2 ; machine 1 ne l'a pas vu."""):
    P(l, 2, 4)
assert (lr["P1"]["juges"], lr["P2"]["juges"]) == (9, 10) and lr["BP"]["hors_q3_max"] < 0.10 and h["e_bord_min"] >= 0.3
T_()
T_("nn.11 SUITE")
P("""Contreseing de machine 2. Depot : a la decision de l'operateur, numero pris au depot (E18) ; l'acte du gel ter, contresigne, est a
deposer avant ou avec celui-ci, puisque ce run s'appuie sur son lecteur. Ce gel ne se rejoue pas.""")
T_()
T_("nn.12 PIECES (convention B)")
for h_, nom in ((c["gel1"], "gel, premiere partie (lot 596a45bf6d4f97d7)"), (c["gel2"], "gel, seconde partie (lot 76ed746ef4db3b0c)"), (c["lot_cert"], "lot de machine 2 : certification de la seconde partie"),
                (c["lot_res"], "lot de machine 2 : resultat du run"), (c["note_cert"], "sa note de certification"), (c["note_res"], "sa note de resultat"), (c["journal"], "journal du pilote du run"),
                (c["pilote2"], "pilote joue (derive par machine 2)"), (c["dense"], "sortie dense du run"), (c["v_inst"], "verdict de l'instrument du lecteur"), (c["v_lect"], "verdict du lecteur"),
                (c["v_o3"], "verdict d'ordre 3 du run"), (c["rejeu_o3"], "verdict d'ordre 3 rejoue par machine 1"), (c["rejeu_lect"], "verdict du lecteur rejoue par machine 1")):
    P("%s  %s" % (h_, nom), 4, 22)
T_()
T_("-- FIN journal_delta_nn_loi_largeur_ordre3_v2 --")
txt = "\n".join(L) + "\n"; txt.encode("ascii"); assert "%" not in txt
longues = [(n + 1, len(l)) for n, l in enumerate(L) if len(l) > 100]; assert not longues, longues
open(SORTIE, "w", encoding="ascii", newline="\n").write(txt)
print("ecrit %s : %d lignes, canon %s" % (SORTIE, len(L), canon(SORTIE)))
