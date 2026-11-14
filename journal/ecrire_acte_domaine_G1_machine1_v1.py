# -*- coding: ascii -*-
"""ECRITURE DE L'ACTE DU RUN DU GEL "LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT" -- machine 1, v1, 2026-11-14.
Chaque nombre de l'acte est lu d'une piece : le verdict rejoue par machine 1 sur le JSON de la sonde de machine 2,
ce JSON, la feuille (sa table), les notes, journaux et manifestes recus, le clone du registre.
Arguments : <recu> <dossier du gel> <clone du registre> <dossier de sortie> <verdict du run precedent (json)>."""
import sys, os, re, json, math, hashlib, unicodedata, textwrap, subprocess, importlib.util
from fractions import Fraction as F
RECU, GEL, CLONE, SORTIE, PREC = sys.argv[1:6]

def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def lire(p):
    return open(p, encoding="utf-8").read().replace("\r\n", "\n")
def plat(t):
    return " ".join(t.split())
LC = RECU + "/lots/certification_gel_domaine_G1_chaine_EA/"
LR = RECU + "/lots/resultat_domaine_G1_chaine_EA/"
SO = LR + "domaine_G1/sortie/"
ENV = RECU + "/enveloppe/"
C = {  # canons recalcules, compares aux attendus
    "gel": (B(GEL + "/gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md"), "b59651f99e60707a"),
    "sonde": (B(GEL + "/sonde_domaine_G1_machine1_v1.py"), "940a21b1d562bb49"),
    "feuille": (B(GEL + "/lecture_domaine_G1_machine1_v1.py"), "0a760e3a244e547d"),
    "lot_gel": (B(GEL + "/MANIFEST_lot_machine1_gel_domaine_G1_chaine_EA_v1.txt"), "1aafb301d7d0ebb3"),
    "moteur": (B(CLONE + "/scripts/m17_chaine_v17.py"), "82a0be882568fe0c"),
    "acte96": (B(CLONE + "/journal/journal_delta_96_chaine_EA_par_etat_v1.md"), "aed8677322e20e0d"),
    "acte95": (B(CLONE + "/journal/journal_delta_95_qualification_EB_bis_v2.md"), "bdf8c5a0c73096a4"),
    "gel96": (B(CLONE + "/gels/gel_chaine_EA_par_etat_pre_enregistrement_v1.md"), "9df2702af59adbbc"),
    "lot_cert": (B(ENV + "MANIFEST_lot_machine2_certification_gel_domaine_G1_chaine_EA_v1.txt"), "d92a200ac348f0a3"),
    "lot_res": (B(ENV + "MANIFEST_lot_machine2_resultat_domaine_G1_chaine_EA_v1.txt"), "86a677dc0ff8ba9d"),
    "json_sonde": (B(SO + "sonde_domaine_G1.json"), "d51a9c6ce98b0452"),
    "json_verdict": (B(SO + "verdict_domaine_G1.json"), "955c4ee53bc2e5d5"),
    "log_lecture": (B(SO + "lecture_domaine_G1.log"), "1ee031ea89823525"),
    "log_bruit": (B(SO + "stabilite_sous_bruit_machine2.log"), "464b1e04a3fabd25"),
    "log_cascade": (B(SO + "stabilite_cascade_machine2.log"), "840acb8d6032e566"),
    "log_indep": (B(SO + "relecture_independante_machine2.log"), "240d94da00442ee0"),
    "log_ancres": (B(SO + "compare_run_essai_ancres_machine2.log"), "d6759636a140b472"),
    "note_res": (B(LR + "POUR_MACHINE1_resultat_domaine_G1_machine2_v1.md"), "7d4558a5322b2b00"),
    "note_cert": (B(LC + "POUR_MACHINE1_certification_gel_domaine_G1_machine2_v1.md"), None),
    "log_banc": (B(LC + "domaine_G1/banc_feuille_domaine_G1_machine2_v1.log"), "3f93d8747fd6a4ca"),
    "log_garde": (B(LC + "domaine_G1/garde_et_boites_machine2_v1.log"), "bfe10d4347e93202"),
    "mon_verdict": (B(SORTIE + "/verdict_rejoue_machine1.json"), "955c4ee53bc2e5d5"),
    "mon_journal": (B(SORTIE + "/lecture_rejouee_machine1.log"), None),
    "verdict_prec": (B(PREC), "4fbc5f7115002054"),
}
for k, (a, b) in C.items():
    assert b is None or a == b, "canon %s : %s contre %s" % (k, a, b)
c = {k: v[0] for k, v in C.items()}

# le registre
def git(*a):
    return subprocess.run(["git", "-C", CLONE] + list(a), check=True, capture_output=True, text=True).stdout.strip()
assert git("rev-parse", "--short", "HEAD") == "04053e0"
d95, d96 = git("log", "-1", "--format=%ad", "--date=format:%H:%M", "3c26420"), git("log", "-1", "--format=%ad", "--date=format:%H:%M", "04053e0")
assert git("log", "-1", "--format=%ad", "--date=format:%Y-%m-%d", "04053e0") == "2026-11-14" and (d95, d96) == ("14:12", "14:13")
assert git("log", "-1", "--format=%s", "04053e0").startswith("delta 96 --") and git("log", "-1", "--format=%s", "3c26420").startswith("delta 95 --")
assert "numbered 29 to 31, join the twenty-eight awaiting review" in git("log", "-1", "--format=%s", "04053e0")
for f in ("scripts/sonde_chaine_par_etat_machine1_v1.py", "scripts/lecture_chaine_par_etat_machine1_v1.py"):
    assert os.path.isfile(CLONE + "/" + f)

# la feuille (sa table) et les JSON
spec = importlib.util.spec_from_file_location("feuille", GEL + "/lecture_domaine_G1_machine1_v1.py")
Fe = importlib.util.module_from_spec(spec); spec.loader.exec_module(Fe)
r = json.load(open(SORTIE + "/verdict_rejoue_machine1.json"))
s = json.load(open(SO + "sonde_domaine_G1.json"))
assert r == json.load(open(SO + "verdict_domaine_G1.json"))
assert r["verdict"] == "LA GARDE NE TIENT PAS" and not r["motifs"] and r["rivale"] == "NON TENUE"
assert (r["a_EN_tombes"], r["b_HORS_tenus"], r["EN_lisibles"], r["HORS_lisibles"]) == (3, 3, 6, 6)
assert r["paires"] == {"P1": "HETEROGENE", "P2": "HOMOGENE", "P3": "HOMOGENE", "P4": "HOMOGENE", "P5": "HOMOGENE"}
pts = {p["id"]: p for p in r["points"]}; sp = {p["id"]: p for p in s["points"]}
ORDRE = ["E1", "E2", "E3", "E4", "E5", "E6", "H1", "H2", "H3", "H4", "H5", "H6", "A1", "A2"]
assert sorted(pts) == sorted(ORDRE) and len(s["points"]) == 14 and all(len(p["etats"]) == 14 for p in s["points"])
assert s["sonde_canon"] == c["sonde"] and s["moteur_canon"] == c["moteur"]
EN_ = [k for k in ORDRE if k[0] == "E"]; HO_ = [k for k in ORDRE if k[0] == "H"]
assert [k for k in EN_ if pts[k]["classe"] == "TOMBE"] == ["E2", "E3", "E4"]
assert [k for k in HO_ if pts[k]["classe"] == "TENU"] == ["H4", "H5", "H6"]
assert [pts[k]["statut"] for k in ORDRE] == ["DECADE", "HORS DECADE", "HORS DECADE", "HORS DECADE", "FACTEUR 2", "FACTEUR 2",
                                            "HORS DECADE", "HORS DECADE", "HORS DECADE", "DECADE", "FACTEUR 2", "FACTEUR 2",
                                            "FACTEUR 2", "FACTEUR 2"]
def qs(pid):
    return sorted(e["q"] for e in pts[pid]["etats"] if not e["exclu"])
R10 = math.sqrt(10.0)
def hors_dd(pid):
    return sum(q * q > 10.0 or q * q < 0.1 for q in qs(pid))
tot_juges = sum(pts[p]["n_juges"] for p in ORDRE)
assert tot_juges == 154
assert (hors_dd("E2"), hors_dd("E3"), hors_dd("E4"), hors_dd("H1"), hors_dd("H2"), hors_dd("H3")) == (6, 3, 12, 1, 9, 14)
assert all(hors_dd(p) == 0 for p in ("E1", "E5", "E6", "H4", "H5", "H6", "A1", "A2"))
sup2_E1 = sum(q > 2 for q in qs("E1")); sous_H4 = sum(q < 0.5 for q in qs("H4"))
assert (sup2_E1, sous_H4, pts["H5"]["n_juges"]) == (12, 2, 6)
m_E2, m_E3, m_E4 = qs("E2")[-1] / R10 - 1, qs("E3")[-1] / R10 - 1, qs("E4")[0] / R10 - 1
# l'etat de H1
h1 = [e for e in pts["H1"]["etats"] if not e["exclu"] and e["q"] * e["q"] > 10.0]
assert len(h1) == 1 and (h1[0]["rang"], h1[0]["n1"], h1[0]["n2"]) == (1, 11, 2)
BRUIT = 7.32e-14
h1_marge, h1_bruit = h1[0]["q"] / R10 - 1, BRUIT / h1[0]["Gamma_2D"]
assert "%.2f" % (100 * h1_marge) == "0.21" and "%.1f" % (100 * h1_bruit) == "1.4" and "%.2e" % h1[0]["Gamma_2D"] == "5.24e-12"
# gardes : ancres et G-6
anc = {}
for pid, (lab, ref) in Fe.ANCRES.items():
    e = [x for x in sp[pid]["etats"] if (x["n1"], x["n2"]) == lab]
    assert len(e) == 1
    anc[pid] = abs(e[0]["Gamma_2D"]["3"] / ref - 1.0)
assert max(anc.values()) == 0.0
ec_g6 = max(max(abs(sp[k]["garde_moteur"]["D1"] - Fe.ATTENDUS[k][4]), abs(sp[k]["garde_moteur"]["c_max"] - Fe.ATTENDUS[k][5])) for k in ORDRE)
assert ec_g6 < 5e-7 and all(sp[k]["garde_moteur"]["statut"] == Fe.ATTENDUS[k][3] and not sp[k]["garde_moteur"]["erreur"] for k in ORDRE)
# les notes et journaux de machine 2
note_res, note_cert = lire(LR + "POUR_MACHINE1_resultat_domaine_G1_machine2_v1.md"), lire(LC + "POUR_MACHINE1_certification_gel_domaine_G1_machine2_v1.md")
nr, nc = plat(note_res), plat(note_cert)
for motif, ou in (("18:59:46 a 19:50:14", nr), ("sonde code 0 en 3028 s", nr), ("JOUE SUR BATTERIE", nr), ("70 pour cent en decharge", nr),
                  ("2516 MHz pour un maximum de 3801", nr), ("de 1.5 a 1.6 fois", nr), ("28 etats, ecart 0", nr), ("7.32e-14", nr),
                  ("il N'A PAS ete mesure aux boites de N = 72 et 74", nr), ("0.21 pour cent AU-DESSUS", nr),
                  ("1.4 pour cent a cet etat", nr), ("5.5 pour cent, a E6 rang 8", nr), ("Neuf sur treize", nr),
                  ("11 controles de lecture rendent 0 morsure", nc), ("4000 sondes synthetiques", nc), ("3^12 = 531441", nc),
                  ("(0 violation)", nc), ("identique au bit a 16 fils (defaut) et a 1 fil", nc),
                  ("survivent a ton selftest : 9", nc), ("survivent a mon banc : 1 (15)", nc), ("R-1 Le selftest de la feuille ne tient pas la table du gel", nc),
                  ("delta 95 et l'acte de la chaine comme delta 96, au registre 04053e0", nc), ("28 etats, ils sont, au bit", nc)):
    assert motif in ou, "phrase absente chez machine 2 : " + motif
assert "VERDICT INCHANGE ; RIVALE PEUT CHANGER" in lire(SO + "stabilite_cascade_machine2.log")
assert "154 etats juges ; bruit relatif maximal de la cible 5.47e-02 (('E6', 8), Gamma_2D(3) = 1.337e-12)" in lire(SO + "stabilite_sous_bruit_machine2.log")
assert "ECARTS : 0" in lire(SO + "relecture_independante_machine2.log")
journal_m2, journal_m1 = lire(SO + "lecture_domaine_G1.log").split("\n"), lire(SORTIE + "/lecture_rejouee_machine1.log").split("\n")
diff_j = [i for i, (a, b) in enumerate(zip(journal_m2, journal_m1)) if a != b]
assert len(journal_m2) == len(journal_m1) and len(diff_j) == 1 and journal_m1[diff_j[0]].startswith("LECTURE DU GEL, sonde")
gel = plat(lire(GEL + "/gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md"))
assert "Au registre (fe10bfe)" in gel and "son acte, contresigne par machine 2 (lot 3ae869c8c037dc21)" in gel
assert "tiendrait a 70 chances sur 100" in gel

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
med = {k: pts[k]["q_median"] for k in ORDRE}

# annonces
A = {
 "A-1": r["verdict"] == "LA GARDE NE TIENT PAS",
 "A-2": pts["E3"]["statut"] == "HORS DECADE", "A-3": pts["E4"]["statut"] == "HORS DECADE", "A-4": pts["E2"]["statut"] == "HORS DECADE",
 "A-5": pts["E1"]["statut"] == "DECADE", "A-6": pts["H1"]["classe"] == "TENU", "A-7": pts["H6"]["classe"] == "TENU",
 "A-8": r["rivale"] == "TENUE", "A-9": 3.0 <= med["E3"] <= 4.5,
 "A-10": pts["E5"]["classe"] == "TENU" and pts["E6"]["classe"] == "TENU",
 "A-11": pts["H4"]["statut"] == "HORS DECADE" or pts["H5"]["statut"] == "HORS DECADE",
 "A-12": all((med[p] < 1) == (float(F(pts[p]["w2"])) < 2) for p in EN_ + HO_),
 "A-13": True,
}
assert [k for k, v in A.items() if not v] == ["A-6", "A-8", "A-9", "A-11"]
assert all((med[p] < 1) == (float(F(pts[p]["w2"])) < 2) for p in ORDRE)
PAIRES = Fe.PAIRES
assert all((abs(math.log(med[b])) > abs(math.log(med[a]))) for a, b in PAIRES.values())    # le petit facteur est plus loin de 1
assert all(float(F(pts[a]["facteur"])) > float(F(pts[b]["facteur"])) for a, b in PAIRES.values())
pf = s["plateforme"]
# le run precedent (delta 96), pour les lectures de nn.6
prec = {x["id"]: x["q_median"] for x in json.load(open(PREC))["points"]}
assert tuple("%.3f" % prec[k] for k in ("J2", "J4", "A2", "J6")) == ("3.735", "1.418", "1.505", "1.503")
r_205, r_210 = prec["J6"] / prec["J4"], med["H2"] / med["E3"]      # rapport des medians, facteur 2/3 sur facteur 3/2
assert ("%.2f" % r_205, "%.2f" % r_210) == ("1.06", "1.77")

lignes = []
def T(x=""):
    assert len(x) <= 100 and all(ord(ch) < 128 for ch in x) and "%" not in x, x
    lignes.append(x)
def P(x, ind=2, suite=None):
    suite = ind if suite is None else suite
    x = " ".join(x.split())
    for sig in (";", ":", "?"):                      # pas de ligne qui commence par un signe double
        x = x.replace(" " + sig, "\x00" + sig)
    for l in textwrap.wrap(x, width=100, initial_indent=" " * ind, subsequent_indent=" " * suite,
                           break_long_words=False, break_on_hyphens=False):
        T(l.replace("\x00", " "))

T("DELTA nn -- LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT : RUN DU 14/11/2026 SOUS LE GEL")
T("b59651f99e60707a.")
T("VERDICT : LA GARDE NE TIENT PAS (a = 3, b = 3). RIVALE : NON TENUE, A UN ETAT PRES.")
T("-- PROJET, VERSION 1")
T("(plume machine 1 ; run et certification machine 2 ; a contresigner par machine 2)")
T("=======================================================================")
T()
T("nn.0 POSITION")
P("Ce delta rend le run du gel \"la garde G-1 du moteur et la chaine E-A par etat\". Sa question : la garde de "
  "domaine G-1 du moteur, calculee avant toute diagonalisation, dit-elle ou la chaine E-A au site entier rend la LECTURE de "
  "E-B a k = 3 a une demi-decade pres ? Reponse de la feuille : LA GARDE NE TIENT PAS. Trois points que la garde dit EN "
  "DOMAINE tombent, trois points qu'elle dit HORS DOMAINE tiennent.")
P("Ce chantier n'est pas la piste (0) : il ne requalifie pas E-B, et aucune phrase d'ici ne dit \"largeur\" sans \"lue a k = "
  "3\". Il a ete ouvert par l'operateur (\"Ouvre !\", le 14/11/2026 a 14 h 57, a machine 1) ; machine 2 ne peut pas le "
  "verifier sur piece (nn.11).")
P("Registre a l'ecriture : origin/main 04053e0, plafond 96 (releve du 14/11 au soir). Les deltas 95 et 96 y sont depuis le "
  "14/11 a %s et %s. Aucun numero n'est pris ici (E18)." % (d95.replace(":", " h "), d96.replace(":", " h ")))
T()
T("nn.1 PIECES (convention B)")
def PIECE(nom, canon, quoi):
    T("  %s  %s" % (nom, canon)); T("  %s    %s" % (" " * (len(nom) - len(nom.lstrip())), quoi))
T("  Au registre (04053e0)")
PIECE("  scripts/m17_chaine_v17.py", c["moteur"], "le moteur ; sa garde G-1 est garde_domaine")
PIECE("  gels/gel_chaine_EA_par_etat_pre_enregistrement_v1.md", c["gel96"], "le gel precedent")
PIECE("  journal/journal_delta_96_chaine_EA_par_etat_v1.md", c["acte96"], "son acte : la coincidence que ce gel eprouve")
T("  Hors registre, de machine 1 (lot %s)" % c["lot_gel"])
PIECE("  gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md", c["gel"], "le gel")
PIECE("  sonde_domaine_G1_machine1_v1.py", c["sonde"], "la sonde : elle mesure et ne juge pas")
PIECE("  lecture_domaine_G1_machine1_v1.py", c["feuille"], "la feuille : elle juge et ne mesure pas")
T("  Hors registre, de machine 2")
PIECE("  lot de certification", c["lot_cert"], "certification du gel, de la sonde et de la feuille, AVANT le run")
PIECE("    POUR_MACHINE1_certification_gel_domaine_G1_machine2_v1.md", c["note_cert"], "la note : 0 morsure, quatre reserves")
PIECE("    domaine_G1/garde_et_boites_machine2_v1.log", c["log_garde"], "la garde et la boite recalculees aux quatorze points")
PIECE("    domaine_G1/banc_feuille_domaine_G1_machine2_v1.log", c["log_banc"], "le banc de la feuille")
PIECE("  lot de resultat", c["lot_res"], "le run, sa lecture, les controles de machine 2")
PIECE("    domaine_G1/sortie/sonde_domaine_G1.json", c["json_sonde"], "les mesures : quatorze points, 196 etats")
PIECE("    domaine_G1/sortie/verdict_domaine_G1.json", c["json_verdict"], "le verdict rendu par la feuille sur BOCAL4")
PIECE("    domaine_G1/sortie/lecture_domaine_G1.log", c["log_lecture"], "son journal")
PIECE("    POUR_MACHINE1_resultat_domaine_G1_machine2_v1.md", c["note_res"], "la note de machine 2")
PIECE("    domaine_G1/sortie/stabilite_sous_bruit_machine2.log", c["log_bruit"], "les statuts sous le bruit des fils")
PIECE("    domaine_G1/sortie/stabilite_cascade_machine2.log", c["log_cascade"], "le verdict et la rivale sous ce bruit")
PIECE("    domaine_G1/sortie/relecture_independante_machine2.log", c["log_indep"], "son lecteur independant, 0 ecart")
PIECE("    domaine_G1/sortie/compare_run_essai_ancres_machine2.log", c["log_ancres"], "les ancres du run contre son essai")
T("  De ce lot")
PIECE("  verdict_rejoue_machine1.json", c["mon_verdict"], "la feuille rejouee par machine 1 sur le JSON de la sonde")
PIECE("  lecture_rejouee_machine1.log", c["mon_journal"], "son journal")
T()
T("nn.2 CE QUI A ETE JOUE, ET PAR QUI (E19)")
P("Machine 2, AVANT le run (lot %s) : 11 controles de lecture du gel, 0 morsure ; la garde du moteur et la boite recalculees "
  "aux quatorze points, egales a la table du gel a six decimales, et la garde identique au bit a 16 fils et a 1 fil ; un "
  "lecteur independant, ecrit du texte du gel, compare a la feuille sur 4000 sondes synthetiques tirees aux bords des "
  "seuils, 0 ecart ; la cascade enumeree sur les 531441 vecteurs de classes des douze points : quand la garde separe, la "
  "rivale n'est jamais tenue ; 59 alterations d'une ligne de la feuille, dont 9 survivent au selftest de la feuille et une "
  "seule a son banc (equivalente en pratique) ; l'essai aux deux ancres rejoue, 28 etats au bit. Quatre reserves, aucune "
  "morsure (nn.9)." % c["lot_cert"])
P("Machine 2, le run (lot %s) : BOCAL4, %s %s, python %s, numpy %s, %d coeurs, variables de fils non fixees ; le 14/11 de "
  "18:59:46 a 19:50:14 ; sonde code 0 en 3028 s, feuille code 0 ; un seul run, aucun arret, aucune reprise, aucun point "
  "rejoue. Temoin d'arrondi %s. Le run a ete joue sur batterie (70 pour cent en decharge a 19:45, processeur a 2516 MHz "
  "pour un maximum de 3801) : chaque point dure de 1.5 a 1.6 fois un point de meme boite du run precedent, d'ou 3028 s "
  "contre l'ordre de 2000 s que le gel annoncait. Les nombres n'en dependent pas : les deux ancres rendent, au bit, les "
  "valeurs de l'essai de la certification." % (c["lot_res"], pf["systeme"], pf["machine"], pf["python"], pf["numpy"], pf["coeurs"], pf["temoin_arrondi"]))
P("Machine 1 : a rejoue la feuille (selftest 74 sur 74) sur le JSON de la sonde de machine 2. Son verdict est identique a "
  "celui que machine 2 rend, au canon (%s), et son journal identique hors la ligne de titre. Machine 1 n'a joue la sonde a "
  "aucun des douze points E1 a E6 et H1 a H6, ni avant ni apres le run ; elle l'avait jouee aux deux ancres (essai a blanc "
  "du gel)." % c["mon_verdict"])
T()
T("nn.3 LES GARDES")
P("G-1 le moteur lu par la sonde est au canon. G-2 les quatorze points sont presents, au role, au w2 et au facteur du gel. "
  "G-3 chacun porte 14 etats (196). G-4 les deux ancres rendent la lecture du run de M17 avec un ecart relatif NUL sur "
  "BOCAL4 (etat (7,2) a A1, etat (8,2) a A2). G-5 la feuille passe son selftest. G-6 a chacun des quatorze points la garde "
  "du moteur consignee par la sonde est sans erreur, au statut de la table du gel, et ses D1 et c_max sont ceux de la table "
  "a moins de 5e-7 pres (tolerance du gel : 5e-5). Aucune garde ne mord.")
T()
T("nn.4 LES QUATORZE POINTS (q = Gamma_chaine / Gamma_2D lue a k = 3, sur les etats juges)")
T("  pt  garde  w2    g     statut       classe   juges  q min  q max  med.   premier juge")
for pid in ORDRE:
    p = pts[pid]; pj = p["premier_juge"]
    T("  %-3s %-5s  %s  x%-3s  %-11s  %-7s  %2d     %.3f  %.3f  %.3f  (%d,%d) q = %.3f" % (
        pid, {"EN DOMAINE": "EN", "HORS DOMAINE": "HORS"}[Fe.ATTENDUS[pid][3]], w2dec(p), fac(p), p["statut"],
        p["classe"] if pid[0] != "A" else "(ancre)", p["n_juges"], p["q_min"], p["q_max"], p["q_median"], pj["n1"], pj["n2"], pj["q"]))
T("  Exclus, par premier motif :")
for pid in ORDRE:
    T("    %s  %s" % (pid, exclus(pts[pid])))
P("\"garde\" : EN pour EN DOMAINE, HORS pour HORS DOMAINE, statut de la garde G-1 du moteur consigne par la sonde. \"g\" est "
  "le facteur sur la regle g_du_point du moteur. \"Premier juge\" : l'etat juge de plus grand recouvrement avec la graine. "
  "Les deux ancres sont hors cascade. %d etats juges sur 196." % tot_juges)
T()
T("nn.5 LE VERDICT")
P("Les six points juges EN DOMAINE et les six points juges HORS DOMAINE sont lisibles. a = 3 : E2, E3 et E4, EN DOMAINE, "
  "sont TOMBES. b = 3 : H4, H5 et H6, HORS DOMAINE, sont TENUS. La cascade du gel (section 7) rend LA GARDE NE TIENT PAS.")
P("Ce que le gel fait ecrire (section 12) : la coincidence de l'acte %s etait une coincidence ; la garde G-1 n'est pas le "
  "domaine de validite de la chaine par etat ; l'acte nomme les points. Les voici." % c["acte96"])
P("- EN DOMAINE et TOMBES. E2 (2.09, facteur 1) : la chaine surestime la lecture d'un facteur %.3f a %.3f sur ses %d etats "
  "juges, dont %d hors de la demi-decade ; le plus grand q depasse la borne de %.1f pour cent. E3 (2.10, facteur 3/2) : "
  "de %.3f a %.3f, %d etats sur %d hors de la demi-decade, le plus grand la depassant de %.1f pour cent. E4 (2.12, facteur "
  "3/2) : de %.3f a %.3f, les %d etats juges hors de la demi-decade, le plus petit la depassant de %.1f pour cent." % (
      pts["E2"]["q_min"], pts["E2"]["q_max"], pts["E2"]["n_juges"], hors_dd("E2"), 100 * m_E2,
      pts["E3"]["q_min"], pts["E3"]["q_max"], hors_dd("E3"), pts["E3"]["n_juges"], 100 * m_E3,
      pts["E4"]["q_min"], pts["E4"]["q_max"], pts["E4"]["n_juges"], 100 * m_E4), ind=4, suite=6)
P("- EN DOMAINE et TENUS. E1 (2.08, facteur 1) est DECADE : q de %.3f a %.3f, %d etats juges sur %d au-dessus de 2. E5 "
  "(1.91, facteur 1) et E6 (1.90, facteur 3/2) sont FACTEUR 2." % (pts["E1"]["q_min"], pts["E1"]["q_max"], sup2_E1, pts["E1"]["n_juges"]),
  ind=4, suite=6)
P("- HORS DOMAINE et TENUS. H4 (1.91, facteur 2/3) est DECADE : q de %.3f a %.3f, %d etats juges sur %d sous 1/2. H5 (1.90, "
  "facteur 2/3) est FACTEUR 2 avec %d etats juges, le minimum du gel. H6 (1.89, facteur 1) est FACTEUR 2." % (
      pts["H4"]["q_min"], pts["H4"]["q_max"], sous_H4, pts["H4"]["n_juges"], pts["H5"]["n_juges"]), ind=4, suite=6)
P("- HORS DOMAINE et TOMBES. H2 (2.10, facteur 2/3) et H3 (2.12, facteur 1) : tous leurs etats juges sont hors de la "
  "demi-decade (%d et %d). H1 (2.08, facteur 2/3) tombe par un seul etat (nn.6)." % (hors_dd("H2"), hors_dd("H3")), ind=4, suite=6)
P("Aucune largeur intrinseque n'est affirmee. Les verdicts PAS DE SIGNAL de M17, NON QUALIFIE du delta 95 et TENU EN PARTIE "
  "du delta 96 ne sont pas touches.")
T()
T("nn.6 LA RIVALE, ET CE QUI LA TIENT")
P("La rivale du gel (section 8) : au-dessus de 2.00, a w2 fixe, la classe d'un point ne depend pas du facteur. Elle se lit "
  "sur P1, P2, P3. P2 (E3, H2) et P3 (E4, H3) sont HOMOGENES : leurs deux points tombent. P1 (E1, H1) est HETEROGENE : E1 "
  "tient, H1 tombe. La feuille rend RIVALE NON TENUE.")
P("Cette issue tient a UN etat, et machine 2 l'a montre (sa lecture sous le bruit des fils, sans verdict). H1 tombe par un "
  "seul de ses %d etats juges : rang 1, etiquette (%d,%d), Gamma_2D(3) = %.2e, q = %.4f, a %.2f pour cent au-dessus de la "
  "borne de la demi-decade (%.4f). Le bruit des fils sur la cible, %.2e en absolu, vaut %.1f pour cent de cette lecture ; "
  "il a ete mesure aux boites des ancres (N = 60 et 61) et pas a celle de H1 (N = 74), le gel interdisant de rejouer un "
  "point. Si cet etat passait sous la borne, H1 serait DECADE, P1 HOMOGENE, et la rivale TENUE." % (
      pts["H1"]["n_juges"], h1[0]["n1"], h1[0]["n2"], h1[0]["Gamma_2D"], h1[0]["q"], 100 * h1_marge, R10, BRUIT, 100 * h1_bruit))
P("Le verdict sur la garde, lui, ne depend pas de ce bruit : machine 2 enumere tous les cas et n'en trouve qu'un, LA GARDE NE "
  "TIENT PAS ; aucun etat de E2, E3 ou E4 n'est incertain.")
P("Ce que l'acte en fait. Il applique la section 12 du gel : la lecture (iii) de sa section 2, \"le desaccord seul compte\", "
  "est retiree comme enonce general. Il dit que cette issue tient a un etat dans le bruit. Et il rend la lecture declaree "
  "des q medians par paire (gel, section 10), qui ne depend pas de cet etat :")
T("    paire  w2    point EN DOMAINE        point HORS DOMAINE      lecture de la paire")
for nom in sorted(PAIRES):
    a, b = PAIRES[nom]
    T("    %s     %s  %s facteur %-3s  %.3f    %s facteur %-3s  %.3f    %s" % (
        nom, w2dec(pts[a]), a, fac(pts[a]), med[a], b, fac(pts[b]), med[b], r["paires"][nom]))
P("Dans les cinq paires, le point au plus petit facteur a le q median le plus loin de 1. A 2.10 le run precedent avait lu "
  "%.3f a facteur 1 (J2) : ce w2 porte donc trois facteurs, %.3f (3/2), %.3f (1) et %.3f (2/3). A 2.05 il avait lu %.3f "
  "(3/2), %.3f (1) et %.3f (2/3). Entre les facteurs 2/3 et 3/2, le rapport des q medians vaut %.2f a 2.05 et %.2f a 2.10. "
  "Ces lectures decrivent ; elles ne rejouent aucun seuil et ne tirent aucune frontiere." % (
      prec["J2"], med["E3"], prec["J2"], med["H2"], prec["J4"], prec["A2"], prec["J6"], r_205, r_210))
T()
T("nn.7 LECTURES SANS VERDICT (gel, section 10)")
P("(a) De part et d'autre de 2.00. Au-dessous, les cinq points juges (E5, E6, H4, H5, H6) sont TENUS, que la garde les dise "
  "EN DOMAINE ou HORS DOMAINE. Au-dessus, des sept points juges un seul est TENU, E1, et il est DECADE. Aucune frontiere en "
  "w2 n'en est tiree (gel, section 12).")
P("(b) Le sens. Aux quatorze points, le q median est sous 1 quand w2 < 2 et au-dessus de 1 quand w2 > 2.")
P("(c) Les exclus. A facteur 2/3 le motif \"sous dix planchers\" ecarte de 5 a 7 etats sur 14 (H1 6, H2 5, H4 7, H5 7) ; H5 "
  "n'a que 6 etats juges : un de moins et le point etait NON LISIBLE, sans effet sur le verdict.")
P("(d) Le bruit des fils, lu par machine 2 : les statuts de onze points juges sur douze et des deux ancres ne changent ni "
  "dans le pire ni dans le meilleur sens ; le douzieme est H1 (nn.6). Le bruit relatif maximal sur les 154 etats juges est "
  "5.5 pour cent, a E6 rang 8, sans effet sur une classe.")
P("(e) Les ancres rendent les lectures du run precedent : q de %.3f a %.3f a A1, de %.3f a %.3f a A2." % (
    pts["A1"]["q_min"], pts["A1"]["q_max"], pts["A2"]["q_min"], pts["A2"]["q_max"]))
T()
T("nn.8 LES ANNONCES DE LA PLUME, COMPTEES (gel, section 11)")
for nom, pr, quoi, res in (
        ("A-1", "0.74", "le verdict est LA GARDE NE TIENT PAS", "REALISEE"),
        ("A-2", "0.75", "E3 est HORS DECADE", "VRAIE"),
        ("A-3", "0.85", "E4 est HORS DECADE", "VRAIE"),
        ("A-4", "0.55", "E2 est HORS DECADE", "VRAIE"),
        ("A-5", "0.75", "E1 est DECADE", "VRAIE"),
        ("A-6", "0.70", "H1 est TENU", "FAUSSE (HORS DECADE, par un etat)"),
        ("A-7", "0.75", "H6 est TENU", "VRAIE"),
        ("A-8", "0.40", "la rivale est TENUE", "FAUSSE (NON TENUE, par un etat)"),
        ("A-9", "0.60", "a E3, le q median entre 3.0 et 4.5", "FAUSSE (%.3f)" % med["E3"]),
        ("A-10", "0.80", "E5 et E6 tous les deux TENUS", "VRAIE"),
        ("A-11", "0.50", "H4 ou H5, l'un au moins, HORS DECADE", "FAUSSE (DECADE et FACTEUR 2)"),
        ("A-12", "0.85", "signe du q median aux points juges lisibles", "VRAIE"),
        ("A-13", "0.95", "la garde G-4 tient ; (0.97) la garde G-6 tient", "VRAIES")):
    assert (res.startswith("FAUSSE")) == (not A[nom]), nom
    T("  %-5s (%s)  %-48s %s" % (nom, pr, quoi, res))
P("Neuf sur treize, comme machine 2 les compte. Ce que la plume en retient. Elle attendait que la garde tombe, et par E3 et "
  "E4 : c'est arrive. Mais la lecture qu'elle lui opposait etait trop simple : elle donnait 0.60 a un q median de E3 dans "
  "l'intervalle de J2 (de 3.0 a 4.5) et il vaut %.3f ; elle donnait une chance sur deux a la chute d'un point a facteur "
  "2/3 au-dessous de 2.00, et les deux tiennent. Treize annonces ne mesurent pas un calibrage." % med["E3"])
T()
T("nn.9 DEFAUTS ET RESERVES")
P("D-G1-1 (m1 ; reserve R-1 de machine 2) : le selftest de la feuille construit ses cas depuis la table qu'il devrait "
  "eprouver ; une faute dans cette table (un c_max, un statut, la reference d'une ancre) le passe. Neuf des 59 alterations "
  "de machine 2 le montrent. La certification de la feuille repose sur le banc de machine 2 et sur son controle de la "
  "table contre le texte du gel.", suite=4)
P("D-G1-2 (m1 ; reserve R-3 de machine 2) : le gel cite le registre a fe10bfe et dit \"hors registre\" les actes de la nuit "
  "bis et de la chaine. Ils etaient deposes depuis le 14/11 a %s et %s (deltas 95 et 96, 04053e0), avant l'ouverture de ce "
  "chantier. La plume n'a pas releve la tete du registre avant d'ecrire. Le gel est scelle (PB-1) ; cet acte cite les noms "
  "deposes." % (d95.replace(":", " h "), d96.replace(":", " h ")), suite=4)
P("D-G1-3 (m1 ; declare au gel, section 2) : la plume a conseille ce gel a l'operateur en lui annoncant que la garde "
  "tiendrait a 70 chances sur 100, avant d'avoir calcule la garde sur une grille, ce qui ne demandait aucun run. Le calcul "
  "fait, elle a annonce l'inverse (0.74 qu'elle ne tienne pas) et l'a ecrit a l'operateur avant de finir le gel.", suite=4)
P("D-G1-4 (m1 ; reserve R-2 de machine 2) : la regle \"un seul etat juge hors de la demi-decade fait tomber le point\" ne "
  "porte aucune marge au bruit de l'instrument. Voulue pour le verdict sur la garde, ou elle n'a rien coute, elle passe a "
  "la rivale, dont l'issue tient a un etat a 0.21 pour cent de la borne (nn.6).", suite=4)
P("R-4 (m2) : l'ouverture n'est pas verifiable sur piece par machine 2 (nn.11).", suite=4)
T()
T("nn.10 CE QUE LE RESULTAT CHANGE A CE QUI ETAIT ECRIT")
P("Delta 96, section nn.7 : les trois points ou la garde disait HORS DOMAINE etaient les trois points HORS DECADE, et l'acte "
  "ecrivait \"coincidence\". Mise a l'epreuve sur douze points neufs, elle ne se reproduit pas : six points sur douze "
  "contredisent la garde, trois dans chaque sens. La phrase du delta 96, \"un verdict a J2 est un verdict hors du domaine "
  "declare de la chaine\", reste vraie de la garde du moteur ; mais cette garde ne dit pas ou la chaine par etat rend la "
  "lecture de E-B.")
P("Gel b59651f99e60707a, section 2 (iii) : \"si le desaccord seul compte\" est retire comme enonce general (nn.6).")
P("Le defaut D-CH-7 du delta 96 (une sonde qui contourne la garde sans le dire) reste un defaut de forme, et la sonde de ce "
  "gel le corrige ; il n'etait pas la cause de la chute de J2.")
T()
T("nn.11 A ARBITRER PAR L'OPERATEUR")
P("(i) Le numero (E18) et le depot.", suite=6)
P("(ii) L'ouverture. Seul l'operateur peut attester qu'il a ouvert ce chantier le 14/11 a 14 h 57 ; son message de depot le "
  "dit ou non. Machine 2 a joue parce que l'envoi le demandait et que l'operateur l'a porte.", suite=6)
P("(iii) Les trois regles candidates de nn.12, sous (X).", suite=6)
P("(iv) La suite. Cet acte n'en propose aucune comme decidee. Trois existent : deriver le residuel de la chaine, que les "
  "lectures de nn.6 decrivent sans l'expliquer (il change de sens a 2.00, croit avec le desaccord et depend du facteur) ; "
  "un nouveau gel sur un autre domaine declare, ecrit avant tout run ; ou rien, ce verdict se deposant tel quel.", suite=6)
T()
T("nn.12 REGLES CANDIDATES SOUS (X) (numerotees au depot ; trente et une attendent deja la revue)")
P("(a) (m2, m1) Un selftest ne construit pas ses cas depuis la table qu'il doit eprouver ; a defaut, la certification dit "
  "quel controle tient cette table.", suite=6)
P("(b) (m2, m1) Un critere qui fait tomber un point ou une issue sur un seul etat dit sa marge au bruit de l'instrument, et "
  "la lecture sous ce bruit se rend avec le verdict.", suite=6)
P("(c) (m1) Avant d'ecrire un gel, la plume releve la tete du registre ; avant d'en conseiller un, elle calcule ce qui se "
  "calcule sans run.", suite=6)
T()
T("nn.13 LE CANAL")
P("Lots echanges pour ce chantier (canons) : machine 1 -- le gel et ses instruments %s ; machine 2 -- la certification %s, "
  "le resultat %s. Les enveloppes qui les ont portes ne sont pas des lots et ne se citent pas." % (c["lot_gel"], c["lot_cert"], c["lot_res"]))
T()
T("nn.14 CE QUE CE DELTA NE FAIT PAS")
P("Il ne tire aucun domaine de validite et aucune frontiere en w2. Il ne dit pas que la chaine est \"qualifiee\", ni "
  "qu'elle est disqualifiee : elle tient aux points nommes et tombe aux points nommes. Il ne rejoue aucun point, ne relit "
  "sous aucun autre palier, aucun autre critere, aucune autre paire, aucune autre population (gel, section 13). Il ne "
  "rouvre pas la piste (0). Il ne prend aucun numero, n'adopte aucune regle, n'edite aucune piece citee (PB-1).")
T()
T("nn.15 PIECES DU LOT")
T("  journal_delta_nn_domaine_G1_chaine_EA_v1.md           cet acte")
T("  ecrire_acte_domaine_G1_machine1_v1.py                 le script qui pose nombres et canons")
T("  verdict_rejoue_machine1.json, lecture_rejouee_machine1.log   la feuille rejouee par machine 1")
T("  releve_acte_domaine_G1_machine1_v1.py / .log          le releve de sortie de machine 1")
T("  contre_epreuve_releve_machine1_v1.py / .log           ce releve, sur des copies alterees de l'acte")
T("  POUR_MACHINE2_acte_domaine_G1_machine1_v1.md          la note d'accompagnement")
T("  fabrique_lot_machine1_v2.py")
T("  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.")
T()
T("-- FIN journal_delta_nn_domaine_G1_chaine_EA_v1 --")
acte = SORTIE + "/journal_delta_nn_domaine_G1_chaine_EA_v1.md"
open(acte, "w", encoding="ascii", newline="\n").write("\n".join(lignes) + "\n")
print("acte %s : canon %s, %d lignes, %d octets" % (os.path.basename(acte), B(acte), len(lignes), os.path.getsize(acte)))
