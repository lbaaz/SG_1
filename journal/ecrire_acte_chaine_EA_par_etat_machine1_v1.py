# -*- coding: ascii -*-
"""ECRITURE DE L'ACTE DU RUN DU GEL "LA CHAINE E-A PAR ETAT, HORS PLAGE" -- machine 1, v1, 2026-11-14.
Chaque nombre de l'acte est lu d'une piece : le verdict rejoue par machine 1 sur le JSON de la sonde de
machine 2, ce JSON, le moteur (garde G-1 recalculee, sans diagonalisation), les notes et manifestes recus.
Arguments : <recu> <gel_chaine> <moteur_v17.py> <dossier de sortie>."""
import sys, os, re, json, math, hashlib, unicodedata, textwrap, importlib.util
from fractions import Fraction as F
RECU, GEL, MOTEUR, SORTIE = sys.argv[1:5]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR)
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def lire(p):
    return open(p, encoding="utf-8").read().replace("\r\n", "\n")
L = RECU + "/lots/"
LC = L + "lot_machine2_2026-11-14_certification_gel_chaine_EA_par_etat_v1/"
LR = L + "lot_machine2_2026-11-14_resultat_chaine_EA_par_etat_v1/"
LB = L + "lot_machine2_2026-11-14_contreseing_acte_nn_EB_bis_v2_v1/"
ENV = RECU + "/enveloppe/"
C = {  # canons recalcules, compares aux attendus
    "gel": (B(GEL + "/gel_chaine_EA_par_etat_pre_enregistrement_v1.md"), "9df2702af59adbbc"),
    "sonde": (B(GEL + "/sonde_chaine_par_etat_machine1_v1.py"), "acf7e26dedfa8abc"),
    "feuille": (B(GEL + "/lecture_chaine_par_etat_machine1_v1.py"), "f94ab05f69e9bf2f"),
    "moteur": (B(MOTEUR), "82a0be882568fe0c"),
    "lot_gel": (B(GEL + "/MANIFEST_lot_machine1_gel_chaine_EA_par_etat_v1.txt"), "b3d3e23e98914a95"),
    "lot_cert": (B(ENV + "MANIFEST_lot_machine2_certification_gel_chaine_EA_par_etat_v1.txt"), "3381564852ba6fe4"),
    "lot_res": (B(ENV + "MANIFEST_lot_machine2_resultat_chaine_EA_par_etat_v1.txt"), "9143062c481ad267"),
    "lot_cs2": (B(ENV + "MANIFEST_lot_machine2_contreseing_acte_nn_EB_bis_v2_v1.txt"), "b46537578fff4ab0"),
    "json_sonde": (B(LR + "chaine_EA_par_etat/sortie/sonde_chaine_par_etat.json"), "5d80bf2edd26a6c1"),
    "json_verdict": (B(LR + "chaine_EA_par_etat/sortie/verdict_chaine_par_etat.json"), "4fbc5f7115002054"),
    "log_lecture": (B(LR + "chaine_EA_par_etat/sortie/lecture_chaine_par_etat.log"), "997c4e4681b0e7ec"),
    "note_res": (B(LR + "POUR_MACHINE1_resultat_chaine_EA_par_etat_machine2_v1.md"), "4297a8489cdf5eea"),
    "log_bruit": (B(LR + "chaine_EA_par_etat/sortie/stabilite_sous_bruit_machine2.log"), "b643f7e55be69ef2"),
    "log_G1": (B(LC + "chaine_EA_par_etat/garde_G1_domaine_machine2_v1.log"), None),
    "note_cert": (B(LC + "POUR_MACHINE1_certification_gel_chaine_EA_par_etat_machine2_v1.md"), None),
    "mon_verdict": (B(SORTIE + "/verdict_rejoue_machine1.json"), "4fbc5f7115002054"),
    "mon_journal": (B(SORTIE + "/lecture_rejouee_machine1.log"), None),
}
for k, (a, b) in C.items():
    assert b is None or a == b, "canon %s : %s contre %s" % (k, a, b)
c = {k: v[0] for k, v in C.items()}

r = json.load(open(SORTIE + "/verdict_rejoue_machine1.json"))
s = json.load(open(LR + "chaine_EA_par_etat/sortie/sonde_chaine_par_etat.json"))
assert r == json.load(open(LR + "chaine_EA_par_etat/sortie/verdict_chaine_par_etat.json"))
assert r["verdict"] == "TENU EN PARTIE" and not r["motifs"]
pts = {p["id"]: p for p in r["points"]}; sp = {p["id"]: p for p in s["points"]}
ORDRE = ["J1", "J2", "J3", "J4", "J5", "J6", "T1", "T2", "T3", "T4", "A1", "A2"]
assert sorted(pts) == sorted(ORDRE)
note_res = lire(LR + "POUR_MACHINE1_resultat_chaine_EA_par_etat_machine2_v1.md")
note_cert = lire(LC + "POUR_MACHINE1_certification_gel_chaine_EA_par_etat_machine2_v1.md")
man_res = lire(ENV + "MANIFEST_lot_machine2_resultat_chaine_EA_par_etat_v1.txt")
for motif, ou in (("10:12:51 a 10:37:31", man_res), ("1480 s", note_res), ("11 controles de lecture, 0 morsure", note_cert),
                  ("4000", note_cert), ("mon banc en mord 23", note_cert), ("ton selftest en mord 15 sur 24", note_cert),
                  ("7.3e-14", note_cert), ("6.7e-14", note_cert), ("131 etats juges", note_res), ("2.4 pour cent", note_res),
                  ("ecart relatif nul", note_res), ("-3.9e-14", note_res), ("11 etats juges chez toi, 13 chez moi", note_res)):
    assert motif in ou, "phrase absente chez machine 2 : " + motif

# garde G-1 du moteur, recalculee comme mesurer_point (seuil_A4 puis garde_domaine), sans diagonalisation
G1 = {}
for pid in ORDRE:
    w2 = F(sp[pid]["w2"]); g = sp[pid]["g"]
    Oc = M.Omega_du_canal(w2)[0]
    gd = M.garde_domaine(w2, g, M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"], Oc)
    G1[pid] = (gd["D1"], gd["c_max"], gd["statut"])
for l in lire(LC + "chaine_EA_par_etat/garde_G1_domaine_machine2_v1.log").split("\n"):
    m = re.match(r"(\w\d)\s+w2=\S+\s+x\S+\s+D1=([\d.]+) .* c_max=([\d.]+) .* -> (.+)$", l)
    if m and m.group(1) in G1:
        d1, cm, st = G1[m.group(1)]
        assert "%.4f" % d1 == m.group(2) and "%.4f" % cm == m.group(3) and st == m.group(4).strip(), l
hors = [p for p in ORDRE if G1[p][2] == "HORS DOMAINE"]
assert hors == ["J2", "T3", "T4"]
assert sorted(p for p in ORDRE if pts[p]["statut"] == "HORS DECADE") == sorted(hors)
assert all(pts[p]["statut"] in ("FACTEUR 2", "DECADE") for p in ORDRE if p not in hors)

def exclus(p):
    d = {}
    for e in p["etats"]:
        if e["exclu"]:
            d[e["exclu"]] = d.get(e["exclu"], 0) + 1
    return " ; ".join("%s %d" % kv for kv in sorted(d.items())) or "aucun"
def w2dec(p):
    return "%.2f" % float(F(p["w2"]))
def fac(p):
    return {"1/1": "1", "3/2": "3/2", "2/3": "2/3"}[p["facteur"]]

# ancres
anc = {}
for pid, lab, ref in (("A1", (7, 2), 2.1623273017950654e-10), ("A2", (8, 2), 2.6613925716641374e-09)):
    e = [x for x in sp[pid]["etats"] if (x["n1"], x["n2"]) == lab]
    assert len(e) == 1
    anc[pid] = abs(e[0]["Gamma_2D"]["3"] / ref - 1.0)
assert max(anc.values()) == 0.0

# annonces
J = ["J1", "J2", "J3", "J4", "J5", "J6"]
qJ2 = pts["J2"]["premier_juge"]["q"]; qJ1 = pts["J1"]["premier_juge"]["q"]
A = {
 "A-1": True,
 "A-2": pts["J2"]["statut"] == "HORS DECADE",
 "A-3": 2.3 <= qJ2 <= 4.6,
 "A-4": 0.70 <= qJ1 <= 0.85,
 "A-5": pts["J3"]["statut"] == "FACTEUR 2" and pts["J4"]["statut"] == "FACTEUR 2",
 "A-6": all((pts[p]["q_median"] < 1) == (float(F(pts[p]["w2"])) < 2) for p in J if pts[p]["statut"] != "NON LISIBLE"),
 "A-7": pts["J5"]["statut"] != "NON LISIBLE",
 "A-8": True,
}
assert [k for k, v in A.items() if not v] == ["A-4"]
assert all((pts[p]["q_median"] < 1) == (float(F(pts[p]["w2"])) < 2) for p in ORDRE)
n_f2 = sum(pts[p]["n_juges"] for p in J if pts[p]["statut"] == "FACTEUR 2")
qJ5 = sorted(e["q"] for e in pts["J5"]["etats"] if not e["exclu"])
sous = [q for q in qJ5 if q < 0.5]
tot_juges = sum(pts[p]["n_juges"] for p in ORDRE)
assert tot_juges == 131 and len(s["points"]) == 12 and all(len(p["etats"]) == 14 for p in s["points"])
pf = s["plateforme"]

lignes = []
def T(x=""):
    assert len(x) <= 100 and all(ord(ch) < 128 for ch in x) and "%" not in x, x
    lignes.append(x)
def P(x, ind=2, suite=None):
    suite = ind if suite is None else suite
    for l in textwrap.wrap(" ".join(x.split()), width=100, initial_indent=" " * ind, subsequent_indent=" " * suite,
                           break_long_words=False, break_on_hyphens=False):
        T(l)

T("DELTA nn -- LA CHAINE E-A PAR ETAT, HORS PLAGE : RUN DU 14/11/2026 SOUS LE GEL 9df2702af59adbbc.")
T("VERDICT : TENU EN PARTIE (cinq points juges tiennent, un tombe).")
T("-- PROJET, VERSION 1")
T("(plume machine 1 ; run et certification machine 2 ; a contresigner par machine 2)")
T("=======================================================================")
T()
T("nn.0 POSITION")
P("Ce delta rend le run du gel \"la chaine E-A par etat, hors plage\". La question du gel : la chaine E-A du moteur, appelee "
  "au site entier qui etiquette un etat propre 2D, predit-elle la LECTURE de E-B a k = 3, a l'ordre de grandeur, hors des "
  "six points de M17 ? Reponse de la feuille : TENU EN PARTIE.")
P("Ce chantier n'est pas la piste (0) : il ne requalifie pas E-B, et aucune phrase d'ici ne dit \"largeur\" sans \"lue a k = "
  "3\". Il a ete ouvert par l'operateur (\"j'ouvre\", le 14/11/2026 a 00 h 15, a machine 1) ; machine 2 ne peut pas le "
  "verifier sur piece (nn.11).")
P("Registre a l'ecriture : origin/main fe10bfe, plafond 94 (releve du 14/11). L'acte de la nuit bis, projet v2 "
  "(bdf8c5a0c73096a4), est contresigne par machine 2 (lot %s) et n'est pas depose. Aucun numero n'est pris ici (E18)." % c["lot_cs2"])
T()
T("nn.1 PIECES (convention B)")
def PIECE(nom, canon, quoi):
    T("  %s  %s" % (nom, canon)); T("      %s" % quoi)
T("  Au registre (fe10bfe)")
PIECE("  scripts/m17_chaine_v17.py", c["moteur"], "le moteur")
T("  Hors registre, de machine 1 (lot %s)" % c["lot_gel"])
PIECE("  gel_chaine_EA_par_etat_pre_enregistrement_v1.md", c["gel"], "le gel")
PIECE("  sonde_chaine_par_etat_machine1_v1.py", c["sonde"], "la sonde : elle mesure et ne juge pas")
PIECE("  lecture_chaine_par_etat_machine1_v1.py", c["feuille"], "la feuille : elle juge et ne mesure pas")
T("  Hors registre, de machine 2")
PIECE("  lot de certification", c["lot_cert"], "certification du gel, de la sonde et de la feuille, AVANT le run")
PIECE("  lot de resultat", c["lot_res"], "le run, sa lecture, les controles de machine 2")
PIECE("    sortie/sonde_chaine_par_etat.json", c["json_sonde"], "les mesures : douze points, 168 etats")
PIECE("    sortie/verdict_chaine_par_etat.json", c["json_verdict"], "le verdict rendu par la feuille sur BOCAL4")
PIECE("    sortie/lecture_chaine_par_etat.log", c["log_lecture"], "son journal")
PIECE("    POUR_MACHINE1_resultat_chaine_EA_par_etat_machine2_v1.md", c["note_res"], "la note de machine 2")
PIECE("    sortie/stabilite_sous_bruit_machine2.log", c["log_bruit"], "les statuts sous le bruit des fils")
PIECE("    garde_G1_domaine_machine2_v1.log (lot de certification)", c["log_G1"], "la garde du moteur aux douze points")
T("  De ce lot")
PIECE("  verdict_rejoue_machine1.json", c["mon_verdict"], "la feuille rejouee par machine 1 sur le JSON de la sonde")
PIECE("  lecture_rejouee_machine1.log", c["mon_journal"], "son journal")
T()
T("nn.2 CE QUI A ETE JOUE, ET PAR QUI (E19)")
P("Machine 2, AVANT le run (lot %s) : 11 controles de lecture du gel, 0 morsure ; un lecteur independant, ecrit du texte du "
  "gel, compare a la feuille sur 4000 sondes synthetiques tirees aux bords des seuils, 0 ecart ; 24 alterations d'une ligne "
  "de la feuille, dont son banc mord 23 et le selftest de la feuille 15 ; l'essai aux deux ancres rejoue. Quatre reserves, "
  "aucune morsure (nn.9)." % c["lot_cert"])
P("Machine 2, le run (lot %s) : BOCAL4, %s %s, python %s, numpy %s, %d coeurs, variables de fils non fixees ; le 14/11 de "
  "10:12:51 a 10:37:31 ; sonde code 0 en 1480 s, feuille code 0 ; un seul run, aucun arret, aucune reprise, aucun point "
  "rejoue. Temoin d'arrondi %s." % (c["lot_res"], pf["systeme"], pf["machine"], pf["python"], pf["numpy"], pf["coeurs"], pf["temoin_arrondi"]))
P("Machine 1 : a rejoue la feuille (selftest 26 sur 26) sur le JSON de la sonde de machine 2. Son verdict est identique a "
  "celui que machine 2 rend, au canon (%s), et son journal identique hors la ligne de titre. Machine 1 n'a joue la sonde a aucun "
  "des dix points J1 a J6 et T1 a T4, ni avant ni apres le run ; elle l'avait jouee aux deux ancres (essai a blanc du gel)." % c["mon_verdict"])
T()
T("nn.3 LES GARDES")
P("G-1 le moteur lu par la sonde est au canon. G-2 les douze points sont presents, au role, au w2 et au facteur du gel. G-3 "
  "chacun porte 14 etats (168). G-4 les deux ancres rendent la lecture du run de M17 avec un ecart relatif NUL sur BOCAL4 "
  "(etat (7,2) a A1, etat (8,2) a A2). G-5 la feuille passe son selftest. Aucune garde ne mord.")
T()
T("nn.4 LES DOUZE POINTS (q = Gamma_chaine / Gamma_2D lue a k = 3, sur les etats juges)")
T("  point  role    w2    g       statut        juges  q min    q max    mediane  premier juge")
for pid in ORDRE:
    p = pts[pid]; pj = p["premier_juge"]
    T("  %-5s  %-6s  %s  x%-5s  %-12s  %2d     %-7s  %-7s  %-7s  (%d,%d) q = %.3f" % (
        pid, p["role"], w2dec(p), fac(p), p["statut"], p["n_juges"], "%.3f" % p["q_min"], "%.3f" % p["q_max"],
        "%.3f" % p["q_median"], pj["n1"], pj["n2"], pj["q"]))
T("  Exclus, par premier motif :")
for pid in ORDRE:
    T("    %s  %s" % (pid, exclus(pts[pid])))
P("\"g\" est le facteur sur la regle g_du_point du moteur. \"Premier juge\" : l'etat juge de plus grand recouvrement avec la "
  "graine. %d etats juges sur 168." % tot_juges)
T()
T("nn.5 LE VERDICT")
P("Les six points juges sont lisibles. Cinq tiennent : J1, J3, J4 et J6 sont FACTEUR 2, J5 est DECADE. Un tombe : J2 est "
  "HORS DECADE. La cascade du gel (section 7) rend TENU EN PARTIE.")
P("Ce que le gel permet d'ecrire (section 11) : l'acte nomme les points tenus et les points tombes, et ne tire aucun "
  "\"domaine de validite\" sans un nouveau gel. Donc :")
P("- a J1 (1.90), J3 et J4 (couplage a 3/2 de la regle), J6 (couplage a 2/3, 2.05), la chaine au site entier rend la lecture "
  "de E-B a k = 3 a mieux qu'un facteur 2 pour chacun des %d etats juges ;" % n_f2, ind=4, suite=6)
P("- a J5 (couplage a 2/3, 1.95), a mieux qu'une demi-decade pour les %d etats juges ; %d sont sous 1/2 (q de %.3f a %.3f), "
  "les %d autres de %.3f a %.3f ;" % (len(qJ5), len(sous), sous[0], sous[-1], len(qJ5) - len(sous), qJ5[len(sous)], qJ5[-1]), ind=4, suite=6)
qJ2s = sorted(e["q"] for e in pts["J2"]["etats"] if not e["exclu"])
P("- a J2 (2.10), elle la SURESTIME d'un facteur %.3f a %.3f sur chacun des %d etats juges ; %d d'entre eux sont hors de la "
  "demi-decade." % (pts["J2"]["q_min"], pts["J2"]["q_max"], pts["J2"]["n_juges"], sum(q * q > 10.0 for q in qJ2s)), ind=4, suite=6)
P("Aucune largeur intrinseque n'est affirmee. Le verdict PAS DE SIGNAL de M17 et le verdict NON QUALIFIE de la nuit bis ne "
  "sont pas touches.")
T()
T("nn.6 LECTURES SANS VERDICT (gel, section 9)")
qT1 = sorted(e["q"] for e in pts["T1"]["etats"] if not e["exclu"])
assert sum(q < 0.5 for q in qT1) == 1 and len(qT1) == 12
P("(a) Les temoins. T1 (1.96) est DECADE par un seul etat (q = %.4f, les onze autres de %.3f a %.3f) ; T2 (2.04) est FACTEUR "
  "2 ; T3 (1.85) et T4 (2.15) sont HORS DECADE, T3 en ordre disperse (q de %.3f a %.3f), T4 d'un facteur %.1f a %.1f." % (
    qT1[0], qT1[1], qT1[-1], pts["T3"]["q_min"], pts["T3"]["q_max"], pts["T4"]["q_min"], pts["T4"]["q_max"]))
P("(b) Le sens. Aux douze points, le q median est sous 1 quand w2 < 2 et au-dessus de 1 quand w2 > 2.")
P("(c) J5 et J6 n'ont que 8 etats juges : six de leurs quatorze sont sous dix planchers. A J6 un Gamma_2D(3) est negatif "
  "(-3.9e-14, du bruit) ; il est exclu comme \"sous dix planchers\".")
P("(d) Le bruit des fils, mesure par machine 2 : 7.3e-14 en absolu sur la cible. Aucun des douze statuts ne change dans le "
  "pire ni dans le meilleur sens ; le bruit relatif maximal sur les 131 etats juges est 2.4 pour cent.")
T()
T("nn.7 LA GARDE DE DOMAINE DU MOTEUR (reserve R-1 de machine 2, ecrite AVANT le run)")
P("Le moteur porte sa propre garde de domaine, G-1 : (D1) |delta| / Omega_c <= 1/5 et (D2a) contamination c_max <= 1/10. "
  "Quand elle echoue, mesurer_point rend HORS DOMAINE et ne produit ni chaine ni E-B. La sonde du gel appelle barriere et "
  "gamma_chaine directement : la garde n'y joue pas, et le gel ne le disait pas (D-CH-7). Machine 2 l'a vu en certifiant, a "
  "calcule la garde aux douze points sans diagonaliser et l'a consignee avant le run. Machine 1 l'a recalculee : memes "
  "valeurs a quatre decimales, memes statuts.")
T("  point  D1      c_max   garde du moteur  statut du point")
for pid in ORDRE:
    T("  %-5s  %.4f  %.4f  %-15s  %s" % (pid, G1[pid][0], G1[pid][1], G1[pid][2], pts[pid]["statut"]))
P("Les trois points ou la garde dit HORS DOMAINE (J2, T3, T4) sont les trois points HORS DECADE ; les neuf points EN DOMAINE "
  "sont FACTEUR 2 ou DECADE. C'est une coincidence entre un statut consigne avant le run et un resultat, sur douze points "
  "dont trois ; ce n'est ni un test ni un domaine de validite, et le gel interdit d'en tirer un. La phrase de machine 2, "
  "reprise ici : a J2, T3 et T4 la garde G-1 du moteur dit HORS DOMAINE ; la sonde lit la chaine sans la consulter ; un "
  "verdict a J2 est un verdict hors du domaine declare de la chaine.")
P("Les six points de M17 sont EN DOMAINE (journal de machine 2 ; machine 1 l'a recalcule a A1 et A2).")
T()
T("nn.8 LES ANNONCES DE LA PLUME, COMPTEES (gel, section 10)")
T("  A-1  (0.72)  le verdict est TENU EN PARTIE                         REALISEE")
T("  A-2  (0.55)  J2 est HORS DECADE                                    VRAIE")
T("  A-3  (0.55)  a J2, q du premier juge entre 2.3 et 4.6              VRAIE (%.3f)" % qJ2)
T("  A-4  (0.60)  a J1, q du premier juge entre 0.70 et 0.85            FAUSSE (%.3f)" % qJ1)
T("  A-5  (0.40)  J3 et J4 tous les deux FACTEUR 2                      VRAIE")
T("  A-6  (0.75)  signe du q median aux points juges lisibles           VRAIE")
T("  A-7  (0.65)  J5 est lisible                                        VRAIE (%d etats juges)" % pts["J5"]["n_juges"])
T("  A-8  (0.95)  la garde G-4 tient                                    VRAIE")
P("Sept sur huit. Ce que la plume en retient : son attente au-dessus de 2.00 (un rapport qui croit comme g^2 / |delta|) a "
  "porte : 3.711 est dans l'intervalle annonce ; son attente en dessous (\"il bouge peu\", vers 0.8) etait fausse : a J1 le rapport remonte "
  "vers 1. Huit annonces ne mesurent pas un calibrage.")
T()
T("nn.9 DEFAUTS ET RESERVES")
P("D-CH-1 a D-CH-6 (m1) : pris avant le run (lot fa54b6ed68469db8 ; gel, section 2).", suite=4)
P("D-CH-7 (m1 ; trouve par machine 2 avant le run, sa reserve R-1) : le gel se tait sur la garde G-1 du moteur, que la "
  "sonde contourne. Un point juge, J2, est hors du domaine que le moteur declare.", suite=4)
P("D-CH-8 (m1 ; note de machine 2, section 4 e) : le critere (8) du gel, \"max / min <= 2\", ne dit pas quoi faire d'une "
  "valeur de chaine nulle ou negative. La feuille exclut (\"chaine instable\") ; le lecteur independant de machine 2 juge. "
  "Un seul point est touche, le temoin T3 : 11 etats juges chez machine 1, 13 chez machine 2, meme statut. Le verdict n'en "
  "depend pas.", suite=4)
P("D-CH-9 (m1 ; reserve R-2) : le selftest de la feuille n'a pas de cas a tous les bords de seuil ; il laisse passer neuf "
  "alterations d'une ligne sur 24. La certification de la feuille repose sur le banc de machine 2.", suite=4)
P("D-CH-10 (m1 ; reserve R-3) : ma note disait le bruit des fils \"de l'ordre de 1e-12 en absolu\" ; mesure, il vaut "
  "7.3e-14 entre 16 et 4 fils, 6.7e-14 entre les deux machines.", suite=4)
P("R-4 (m2) : a q = racine de 10 exactement la feuille rend HORS DECADE alors que le gel ferme la borne. Sans effet : le q "
  "le plus proche d'une borne est celui d'un temoin (T1, %.4f, a 0.5 pour cent de 1/2) ; aucun n'est pres de la racine de "
  "10." % qT1[0], suite=4)
T()
T("nn.10 CE QUE LE RESULTAT CHANGE A CE QUI ETAIT ECRIT")
P("La note 9322566db2546adb lisait, apres coup, un accord chaine / 2D de 0.499 a 1.642 aux six points de M17. Sous gel, hors "
  "de ces points : l'accord tient a un facteur 2 a quatre points juges, a une demi-decade a un cinquieme, et tombe au "
  "sixieme. La lecture de cette note n'est donc ni retiree ni generale : elle vaut aux points nommes en nn.5.")
T()
T("nn.11 A ARBITRER PAR L'OPERATEUR")
P("(i) Les numeros (E18) et l'ordre des depots : l'acte de la nuit bis d'abord, celui-ci ensuite.", suite=6)
P("(ii) L'ouverture. Seul l'operateur peut attester qu'il a ouvert ce chantier le 14/11 a 00 h 15 ; son message de depot le "
  "dit ou non. Machine 2 a joue parce que l'envoi le demandait et que l'operateur l'a porte.", suite=6)
P("(iii) Les trois regles candidates de nn.12, sous (X).", suite=6)
P("(iv) La suite. Cet acte n'en propose aucune comme decidee. Trois existent : un nouveau gel qui prendrait la garde G-1 du "
  "moteur pour domaine et la mettrait a l'epreuve sur des points neufs ; la derivation du second ordre de la chaine, que "
  "le facteur de J2 (de 2.9 a 4.2 sur treize etats) appelle ; ou rien, ce verdict se deposant tel quel.", suite=6)
T()
T("nn.12 REGLES CANDIDATES SOUS (X) (sans numero tant que l'acte de la nuit bis n'est pas depose)")
P("(a) (m2, m1) Une sonde qui appelle les fonctions d'un moteur sans passer par ses gardes le dit, et consigne le statut de "
  "ces gardes a chaque point.", suite=6)
P("(b) (m2) Un critere ecrit comme un rapport dit ce qu'il fait d'un terme nul ou negatif.", suite=6)
P("(c) (m2, m1) Un selftest porte un cas a chaque bord de seuil ; a defaut, la certification dit sur quel banc elle repose.", suite=6)
T()
T("nn.13 LE CANAL")
P("Lots echanges pour ce chantier (canons) : machine 1 -- le gel et ses instruments %s ; machine 2 -- la certification %s, "
  "le resultat %s. Les enveloppes qui les ont portes ne sont pas des lots et ne se citent pas. Le conteneur de machine 1 a "
  "tenu du 12 au 14/11." % (c["lot_gel"], c["lot_cert"], c["lot_res"]))
T()
T("nn.14 CE QUE CE DELTA NE FAIT PAS")
P("Il ne dit pas que la chaine est \"qualifiee\". Il ne tire aucun domaine de validite. Il ne rejoue aucun point, ne relit "
  "sous aucun autre palier, aucun autre critere, aucune autre population (gel, section 12). Il ne rouvre pas la piste (0). "
  "Il ne prend aucun numero, n'adopte aucune regle, n'edite aucune piece citee (PB-1).")
T()
T("nn.15 PIECES DU LOT")
T("  journal_delta_nn_chaine_EA_par_etat_v1.md             cet acte")
T("  ecrire_acte_chaine_EA_par_etat_machine1_v1.py         le script qui pose nombres et canons")
T("  verdict_rejoue_machine1.json, lecture_rejouee_machine1.log   la feuille rejouee par machine 1")
T("  releve_acte_chaine_EA_par_etat_machine1_v1.py / .log  le releve de sortie de machine 1")
T("  POUR_MACHINE2_acte_chaine_EA_par_etat_machine1_v1.md  la note d'accompagnement")
T("  fabrique_lot_machine1_v1.py")
T("  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.")
T()
T("-- FIN journal_delta_nn_chaine_EA_par_etat_v1 --")
acte = SORTIE + "/journal_delta_nn_chaine_EA_par_etat_v1.md"
open(acte, "w", encoding="ascii", newline="\n").write("\n".join(lignes) + "\n")
print("acte %s : canon %s, %d lignes, %d octets" % (os.path.basename(acte), B(acte), len(lignes), os.path.getsize(acte)))
