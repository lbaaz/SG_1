# -*- coding: ascii -*-
"""ECRITURE DE L'ACTE DU RUN DU GEL "LA CHAINE E-A AU SECOND ORDRE" -- machine 1, v1, 2026-11-15.
Chaque nombre de l'acte est lu d'une piece : le verdict rejoue par machine 1 sur le JSON de la sonde de machine 2,
ce JSON, la feuille (sa table), les notes, journaux et manifestes recus, le clone du registre.
Arguments : <recu> <dossier du gel> <manifeste du lot du gel> <note hors chaine> <clone du registre> <dossier de sortie>."""
import sys, os, re, json, math, hashlib, unicodedata, textwrap, subprocess, importlib.util
RECU, GEL, MANIF_GEL, NOTE, CLONE, SORTIE = sys.argv[1:7]

def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def lire(p):
    return open(p, encoding="utf-8").read().replace("\r\n", "\n")
def plat(t):
    return " ".join(t.split())
LC = RECU + "/lots/certification/"
LR = RECU + "/lots/resultat/"
SO = LR + "ordre2/sortie/"
ENV = RECU + "/enveloppe/"
C = {  # canons recalcules, compares aux attendus
    "gel": (B(GEL + "/gel_ordre2_chaine_EA_pre_enregistrement_v1.md"), "41153158190cf7f1"),
    "sonde": (B(GEL + "/sonde_ordre2_machine1_v1.py"), "24315c52b234319c"),
    "bloc": (B(GEL + "/chaine_ordre2_bloc_machine1_v1.py"), "7cd5977bc27bebc1"),
    "feuille": (B(GEL + "/lecture_ordre2_machine1_v1.py"), "0dc8241c680eb1ff"),
    "lot_gel": (B(MANIF_GEL), "3bc363266957de56"),
    "note": (B(NOTE), "022d32238a66df6b"),
    "moteur": (B(CLONE + "/scripts/m17_chaine_v17.py"), "82a0be882568fe0c"),
    "acte97": (B(CLONE + "/journal/journal_delta_97_domaine_G1_chaine_EA_v1.md"), "e718d2db619af9b1"),
    "gel97": (B(CLONE + "/gels/gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md"), "b59651f99e60707a"),
    "lot_cert": (B(ENV + "MANIFEST_lot_machine2_certification_gel_ordre2_chaine_EA_v1.txt"), "59a583a640112891"),
    "lot_res": (B(ENV + "MANIFEST_lot_machine2_resultat_ordre2_chaine_EA_v1.txt"), "6dfdfe8fd0b8eaad"),
    "note_cert": (B(LC + "POUR_MACHINE1_certification_gel_ordre2_machine2_v1.md"), "e25286235e5474f5"),
    "log_ctl": (B(LC + "ordre2/controles_gel_ordre2_machine2_v1.log"), "830b16e74f339795"),
    "log_bloc": (B(LC + "ordre2/bloc_independant_machine2_v1.log"), "2adf855b5aba5f50"),
    "log_garde": (B(LC + "ordre2/garde_et_boites_machine2_v1.log"), "9dd0fc58e38936e9"),
    "log_banc": (B(LC + "ordre2/banc_feuille_ordre2_machine2_v1.log"), "04e47095995210c4"),
    "log_essais": (B(LC + "ordre2/compare_essais_16fils_machine1.log"), "33585399bf8c0d9b"),
    "note_res": (B(LR + "POUR_MACHINE1_resultat_ordre2_machine2_v1.md"), "e10c02883d9b20a9"),
    "console": (B(SO + "console_ordre2.log"), "3e0fceb4dec89ba7"),
    "log_sonde": (B(SO + "sonde_ordre2.log"), "a68ab28afb75e54e"),
    "json_sonde": (B(SO + "sonde_ordre2.json"), "10887c60d5f55bcf"),
    "json_verdict": (B(SO + "verdict_ordre2.json"), "4195583a970eaf70"),
    "log_lecture": (B(SO + "lecture_ordre2.log"), "c8a03a393d95cebf"),
    "log_indep": (B(SO + "relecture_independante_machine2.log"), "81d9151e2595f712"),
    "log_ancres": (B(SO + "compare_run_essai_ancres_machine2.log"), "64c3a19b08afb862"),
    "log_cascade": (B(SO + "stabilite_cascade_machine2.log"), "172c031d05d5f56a"),
    "log_sens": (B(SO + "sensibilite_bruit_machine2.log"), "a48503026fecbb7d"),
    "log_defaut": (B(SO + "stabilite_cascade_machine2_v1_defaut.log"), "0db441d7922f03b2"),
    "log_etat": (B(SO + "etat_machine_machine2.log"), "4d6ca2940b76beff"),
    "mon_verdict": (B(SORTIE + "/verdict_rejoue_machine1.json"), "4195583a970eaf70"),
    "mon_journal": (B(SORTIE + "/lecture_rejouee_machine1.log"), None),
}
for k, (a, b) in C.items():
    assert b is None or a == b, "canon %s : %s contre %s" % (k, a, b)
c = {k: v[0] for k, v in C.items()}

# ---------------------------------------------------------------- le registre
def git(*a):
    return subprocess.run(["git", "-C", CLONE] + list(a), check=True, capture_output=True, text=True).stdout.strip()
assert git("rev-parse", "--short", "HEAD") == "79e77d2" and git("rev-parse", "--short", "origin/main") == "79e77d2"
assert git("log", "-1", "--format=%s").startswith("delta 97 --")
assert "three candidate rules, numbered 32 to 34, join the thirty-one awaiting review (X)" in git("log", "-1", "--format=%s")
acte97 = lire(CLONE + "/journal/journal_delta_97_domaine_G1_chaine_EA_v1.md")
assert all(x in acte97 for x in ("deriver le residuel", "  (a) (m2, m1)", "  (b) (m2, m1)", "  (c) (m1)", "trente et une attendent"))

# ---------------------------------------------------------------- le verdict, le JSON, la feuille
r = json.load(open(SORTIE + "/verdict_rejoue_machine1.json", encoding="ascii"))
assert r == json.load(open(SO + "verdict_ordre2.json", encoding="utf-8")), "le verdict rejoue n'est pas celui de machine 2"
s = json.load(open(SO + "sonde_ordre2.json", encoding="utf-8"))
spec = importlib.util.spec_from_file_location("feuille", GEL + "/lecture_ordre2_machine1_v1.py")
Fe = importlib.util.module_from_spec(spec); spec.loader.exec_module(Fe)
assert Fe.cascade(s) == r and Fe.gardes(s) == [] and r["motifs"] == []
ORDRE = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4", "A1", "A2", "W1", "W2"]
assert [p["id"] for p in s["points"]] == ORDRE and s["points_demandes"] == ORDRE
assert s["sonde_canon"] == c["sonde"] and s["moteur_canon"] == c["moteur"]
pf = s["plateforme"]
assert (pf["systeme"], pf["machine"], pf["python"], pf["numpy"], pf["coeurs"]) == ("Windows", "AMD64", "3.11.9", "2.2.6", 16)
R = {p["id"]: p for p in r["points"]}; S = {p["id"]: p for p in s["points"]}
JUG = [k for k in ORDRE if Fe.ATTENDUS[k][0] == "juge"]
assert len(JUG) == 12 and all(len(S[k]["etats"]) == 14 and S[k]["faisable"] for k in ORDRE)
assert r["verdict"] == "L'ORDRE 2 TIENT" and r["verdict_sans_marge"] == "L'ORDRE 2 TIENT" and r["gardes_par_la_marge"] == []
assert all(r["bandes"][b] == {"issue": "TENUE", "borne": bo, "limite": li, "lisibles": 4, "tombes": []}
           for (b, bo, li) in Fe.BANDES)
assert r["comparaison"] == {"issue": "L'ORDRE 2 FAIT MIEUX PARTOUT", "lisibles": 12, "pas_mieux": []}
assert r["energie"] == {"issue": "L'ENERGIE TIENT", "lisibles": 12, "non_tenue": []}
assert all(R[k]["statut"] == "TENU" and R[k]["comparaison"] == "MIEUX" and R[k]["energie"] == "TENUE" for k in JUG)
assert R["A1"]["statut"] == "LU" and R["A2"]["statut"] == "LU" and R["W1"]["statut"] == "LU" and R["W2"]["statut"] == "NON LISIBLE"
ej = [(k, e) for k in JUG for e in R[k]["etats"] if e["exclu"] is None]
n_juges = len(ej); n_etats = sum(len(R[k]["etats"]) for k in JUG)
excl = {}
for k in JUG:
    for e in R[k]["etats"]:
        if e["exclu"]:
            excl[e["exclu"]] = excl.get(e["exclu"], 0) + 1
assert (n_juges, n_etats) == (132, 168) and excl == {"sous dix planchers": 31, "J flou": 4, "barriere vide": 1}
q2s = [e["q2"] for _, e in ej]; q1s = [e["q1"] for _, e in ej]
f3 = lambda x: "%.3f" % x
def par_bande(b, cle, f):
    return f(e[cle] for k, e in ej if R[k]["bande"] == b)
exw2 = {}
for e in R["W2"]["etats"]:
    if e["exclu"]:
        exw2[e["exclu"]] = exw2.get(e["exclu"], 0) + 1
assert R["W2"]["n_juges"] == 3 and exw2 == {"sous dix planchers": 11}
w1 = [e["q2"] for e in R["W1"]["etats"] if e["exclu"] is None]
assert len(w1) == 11 and sum(1 for x in w1 if x > 1.6) == 7 and sum(1 for x in w1 if x > 2.0) == 2 and R["W1"]["palier"] is None
l4_hors16 = sorted(e["q2"] for e in R["L4"]["etats"] if e["exclu"] is None and e["q2"] > 1.6)
assert len(l4_hors16) == 3 and sum(1 for x in q2s if x > 1.6) == 3 and R["L4"]["palier"] == 2.0

# ---------------------------------------------------------------- les gardes, recalculees
g4, g8f, g8e = {}, {}, {}
for pid, ((n1, n2), ref, ref_o2, ref_de) in Fe.ANCRES.items():
    e = [x for x in S[pid]["etats"] if (x["n1"], x["n2"]) == (n1, n2)]
    assert len(e) == 1
    g4[pid] = abs(e[0]["Gamma_2D"]["3"] / ref - 1.0)
    g8f[pid] = abs(e[0]["chaine2"]["gammas_flux"][2] / ref_o2 - 1.0); g8e[pid] = abs(e[0]["chaine2"]["dE"][2] / ref_de - 1.0)
assert max(g4.values()) == 0.0 and max(g8f.values()) < 1e-9 and max(g8e.values()) < 1e-10
g6 = max(max(abs(S[k]["garde_moteur"]["D1"] - Fe.ATTENDUS[k][5]), abs(S[k]["garde_moteur"]["c_max"] - Fe.ATTENDUS[k][6])) for k in ORDRE)
assert g6 < 1e-6 and all(S[k]["garde_moteur"]["statut"] == Fe.ATTENDUS[k][4] for k in ORDRE)
hors_dom = [k for k in ORDRE if S[k]["garde_moteur"]["statut"] == "HORS DOMAINE"]
assert hors_dom == ["M4", "L1", "L2", "L4", "W1", "W2"]

# ---------------------------------------------------------------- le run, lu dans les journaux de machine 2
cons = lire(SO + "console_ordre2.log")
assert "2026-11-14 23:26:01 LANCEMENT DE LA SONDE aux seize points (W2 en dernier)" in cons
assert "2026-11-15 00:41:24 FIN DE LA SONDE code=0 duree=4524 s" in cons and "2026-11-15 00:41:25 FIN DE LA FEUILLE code=0" in cons
etat = lire(SO + "etat_machine_machine2.log")
assert all(x in etat for x in ("BatteryStatus 1 (1 = en decharge", "EstimatedChargeRemaining 62 pour cent", "CurrentClockSpeed 2516 MHz ; MaxClockSpeed 3801 MHz", "batterie en decharge a 100 pour cent"))
durees = {k: S[k]["duree_s"] for k in ORDRE}
ent = lambda x: int(math.floor(x + 0.5))
ls = lire(SO + "sonde_ordre2.log")
for k in ORDRE:
    assert re.search(r"^%s .* N=%d .* joue, 14 etats, %.1f s$" % (k, S[k]["N"], durees[k]), ls, re.M), k
assert abs(sum(durees.values()) - 4524) < 6 and S["W2"]["N"] == 89 and ent(durees["W2"]) == 1346
ll = lire(SO + "lecture_ordre2.log")
assert "SELFTEST : 160 cas, 160 tenus" in ll and "VERDICT : L'ORDRE 2 TIENT" in ll
ml = lire(SORTIE + "/lecture_rejouee_machine1.log")
assert "SELFTEST : 160 cas, 160 tenus" in ml and ml.rstrip().endswith("VERDICT : L'ORDRE 2 TIENT")
ind = lire(SO + "relecture_independante_machine2.log")
assert "ECARTS ENTRE MON LECTEUR ET LA FEUILLE : 0 []" in ind
anc = lire(SO + "compare_run_essai_ancres_machine2.log")
assert "BILAN : 28 etats, 0 etiquettes differentes ; ecart absolu max de Gamma_2D (k = 2, 3, 4) 0.00e+00" in anc and "chaine : ecart relatif max 0.00e+00" in anc
casc = lire(SO + "stabilite_cascade_machine2.log")
assert casc.count("-> INCHANGE") == 12 and "VERDICT INCHANGE" in casc and 'verdicts possibles sous le bruit : ["L\'ORDRE 2 TIENT"]' in casc
assert re.search(r"^L4 .* 1 etat\(s\) incertain\(s\) -> INCHANGE$", casc, re.M) and casc.count(" 0 etat(s) incertain(s)") == 11
sens = lire(SO + "sensibilite_bruit_machine2.log")
assert "bruit de base 7.32e-14 sur Gamma_2D(3)" in sens
for n in range(1, 8):
    assert re.search(r"^x%d +\(bruit .*VERDICT INCHANGE *$" % n, sens, re.M), n
assert re.search(r"^x7 +\(bruit 5\.12e-13\)", sens, re.M) and re.search(r"^x8 +\(bruit 5\.86e-13\) .*NE TIENT PAS.*TIENT JUSQU'A 0\.10.*VERDICT PEUT CHANGER *$", sens, re.M)
dfo = lire(SO + "stabilite_cascade_machine2_v1_defaut.log")
assert "VERDICT PEUT CHANGER" in dfo

# ---------------------------------------------------------------- la certification, lue dans ses journaux
ctl = lire(LC + "ordre2/controles_gel_ordre2_machine2_v1.log")
assert "BILAN : 22 controles, 0 mordent []" in ctl and "3^12 = 531441 vecteurs" in ctl and "['RELEVE : 24 controles, 24 tenus']" in ctl
assert "BANC, famille T (la table) : 131 alterations, 131 mordues, 0 survivantes" in ctl and "SELFTEST : 160 cas, 160 tenus" in ctl
bl = lire(LC + "ordre2/bloc_independant_machine2_v1.log")
assert "BILAN : 17 controles, 0 mordent []" in bl
assert "plus grand ecart relatif : t 0.00e+00 ; Sigma2 5.22e-13 ; u 4.60e-13" in bl and "122 etats" in bl and "36 sauts" in bl
assert "ecart relatif : t 0.00e+00 ; Sigma2 1.18e-14 ; u 5.16e-15" in bl and "LOWDIN SUR LE H_2D EXACT DU MOTEUR" in bl
assert "ecart relatif max : Gamma_flux 6.97e-09 ; dE 1.95e-11" in bl
assert "erreur / |dE| de la chaine d'ordre 2 : 7.50e-05, 1.84e-05, 4.59e-06 ; ordre 1 : 4.37e-02 ; Sigma2 seul : 4.40e-04 ; u seul : 4.40e-02" in bl
assert "'Sigma2 seul' est aussi bon que lui" in bl and "q1 de 0.375 a 6.987" in bl
assert "dans un facteur 1.5 a l'ordre 2 : 242 sur 243 (la note : 241)" in bl
assert "(gel 2.3236497766513317e-10, ecart 8.28e-12)" in bl
bc = lire(LC + "ordre2/banc_feuille_ordre2_machine2_v1.log")
mb = re.search(r"BILAN : 115 alterations ; motifs absents \[\] ; survivent au selftest de machine 1 : \[([0-9, ]+)\] ; survivent a mon banc : \[45, 69, 109\]", bc)
assert mb and len(mb.group(1).split(",")) == 22 and "4000 sondes synthetiques" in bc
nc = plat(lire(LC + "POUR_MACHINE1_certification_gel_ordre2_machine2_v1.md"))
assert all(x in nc for x in ("CERTIFIE, 0 morsure, avec des reserves", "R-1 Ton selftest laisse passer", "R-2 -2 Im E de la chaine DU MOTEUR",
                             "il differe de 0.2 a 0.3 pour cent aux etats juges", "R-3 La marge d'un plancher (1.33e-13) vaut 1.7 fois le bruit",
                             "7.7e-14 entre 16 et 1 fil", "R-4 Section 2 : deux chiffres", "R-5 L'ouverture", "R-6 Ce que je ne verifie pas",
                             "ecrit du texte du gel", "Six de mes controles ont mordu au premier ou au deuxieme jet, tous par ma faute"))
nr = plat(lire(LR + "POUR_MACHINE1_resultat_ordre2_machine2_v1.md"))
assert all(x in nr for x in ("JOUE SUR BATTERIE", "un seul run, aucun arret, aucune reprise, aucun point rejoue", "Le bruit a ete mesure a N = 60 et 61",
                             "il N'A PAS ete mesure aux boites de N = 73 et 74", "UN DEFAUT DE MON OUTIL, PAS DU RESULTAT", "je le note comme ma morsure",
                             "Dix-huit sur vingt annonces jugees vraies"))
es = lire(LC + "ordre2/compare_essais_16fils_machine1.log")
assert "ecart absolu max de Gamma_2D (k = 2, 3, 4) 6.72e-14" in es

# ---------------------------------------------------------------- les annonces, comptees sur le verdict
gel = lire(GEL + "/gel_ordre2_chaine_EA_pre_enregistrement_v1.md")
assert "A-1  le verdict : L'ORDRE 2 TIENT 0.45 ; TIENT JUSQU'A 0.10 0.27" in gel
lis = [R[k] for k in JUG]
AN = [
    ("A-2", 0.85, "la bande PROCHE est TENUE", r["bandes"]["proche"]["issue"] == "TENUE", ""),
    ("A-3", 0.80, "la bande MOYENNE est TENUE", r["bandes"]["moyenne"]["issue"] == "TENUE", ""),
    ("A-4", 0.60, "la bande LOINTAINE est TENUE", r["bandes"]["lointaine"]["issue"] == "TENUE", ""),
    ("A-5", 0.70, "L2 est TENU", R["L2"]["statut"] == "TENU", "plus petit q2 %s" % f3(R["L2"]["q2_min"])),
    ("A-6", 0.80, "L4 est TENU", R["L4"]["statut"] == "TENU", ""),
    ("A-6", 0.65, "son plus grand q2 est entre 1.5 et 1.9", 1.5 <= R["L4"]["q2_max"] <= 1.9, f3(R["L4"]["q2_max"])),
    ("A-7", 0.80, "M4 est TENU", R["M4"]["statut"] == "TENU", ""),
    ("A-7", 0.65, "son plus grand q2 est entre 1.35 et 1.55", 1.35 <= R["M4"]["q2_max"] <= 1.55, f3(R["M4"]["q2_max"])),
    ("A-8", 0.85, "L'ORDRE 2 FAIT MIEUX PARTOUT", r["comparaison"]["issue"] == "L'ORDRE 2 FAIT MIEUX PARTOUT", ""),
    ("A-9", 0.90, "L'ENERGIE TIENT", r["energie"]["issue"] == "L'ENERGIE TIENT", ""),
    ("A-9", 0.70, "le plus grand ecart d'energie est < 0.006", max(p["ecart_energie_max"] for p in lis) < 0.006,
     "%.4f, a L1" % max(p["ecart_energie_max"] for p in lis)),
    ("A-10", 0.70, "a chaque point le plus petit q2 est >= 0.95", all(p["q2_min"] >= 0.95 for p in lis),
     "le plus petit : %s, a C1" % f3(min(p["q2_min"] for p in lis))),
    ("A-11", 0.60, "la mediane de q2 / loi est entre 0.93 et 1.15", all(0.93 <= p["q2_sur_loi_median"] <= 1.15 for p in lis),
     "L2 : %s" % f3(R["L2"]["q2_sur_loi_median"])),
    ("A-12", 0.75, "W1 a un etat juge hors de 1.6", any(not (1 / 1.6 <= x <= 1.6) for x in w1), "sept sur onze"),
    ("A-12", 0.70, "tous ses etats juges sont sous 2.5", all(x < 2.5 for x in w1), "le plus grand : %s" % f3(max(w1))),
    ("A-13", 0.65, "W2 est joue et lisible", R["W2"]["statut"] != "NON LISIBLE", "joue, 3 etats juges"),
    ("A-14", 0.65, "-2 Im E et Gamma_flux a moins de 0.05", all(p["flux_contre_im_max"] < 0.05 for p in lis),
     "le plus grand : %.3f, a L4" % max(p["flux_contre_im_max"] for p in lis)),
    ("A-15", 0.95, "la garde G-4 tient", not any(m.startswith("G-4") for m in r["motifs"]), ""),
    ("A-15", 0.93, "la garde G-8 tient", not any(m.startswith("G-8") for m in r["motifs"]), ""),
    ("A-15", 0.97, "la garde G-6 tient", not any(m.startswith("G-6") for m in r["motifs"]), ""),
]
n_vraies = sum(1 for a in AN if a[3]); fausses = sorted(set(a[0] for a in AN if not a[3]))
assert (len(AN), n_vraies, fausses) == (20, 18, ["A-11", "A-13"])
attendu = sum(a[1] for a in AN)
assert min(p["q2_min"] for p in lis) == R["C1"]["q2_min"] and max(p["ecart_energie_max"] for p in lis) == R["L1"]["ecart_energie_max"]
assert max(p["flux_contre_im_max"] for p in lis) == R["L4"]["flux_contre_im_max"]
loi = {k: R[k]["q2_sur_loi_median"] for k in JUG}
assert min(loi, key=loi.get) == "L2" and f3(max(loi.values())) == f3(loi["M4"]) == f3(loi["L3"]) == "1.037"
ecart_pires = {k: R[k]["pire_ordre1"] - R[k]["pire_ordre2"] for k in JUG}
serres = sorted(JUG, key=lambda k: ecart_pires[k])[:3]
assert serres == ["L2", "L1", "C3"]
bords = [min((k for k in JUG if R[k]["bande"] == b), key=lambda k: R[k]["borne"] / R[k]["q2_max"]) for (b, _, _) in Fe.BANDES]
assert bords == ["C2", "M4", "L4"]

# ---------------------------------------------------------------- mise en page
L = []
def P(texte, ind=2, suite=None):
    t = plat(texte).replace(" ;", "\x00;").replace(" :", "\x00:").replace(" ?", "\x00?")
    for l in textwrap.wrap(t, width=100, initial_indent=" " * ind, subsequent_indent=" " * (ind if suite is None else suite),
                           break_long_words=False, break_on_hyphens=False):
        L.append(l.replace("\x00", " "))
def T(*lignes):
    L.extend(lignes)
def piece(nom, canon, quoi, ind=4):
    L.append("%s%s  %s" % (" " * ind, nom, canon)); P(quoi, ind + 4)
fac = lambda k: Fe.ATTENDUS[k][2].replace("/1", "")
dlt = lambda k: "%+.2f" % (Fe.eval_fraction(Fe.ATTENDUS[k][1]) - 2.0)

T("DELTA nn -- LA CHAINE E-A AU SECOND ORDRE : RUN DES 14 ET 15/11/2026 SOUS LE GEL 41153158190cf7f1.",
  "VERDICT : L'ORDRE 2 TIENT. COMPARAISON : L'ORDRE 2 FAIT MIEUX PARTOUT. ENERGIES : L'ENERGIE TIENT.",
  "-- PROJET, VERSION 1",
  "(plume machine 1 ; run et certification machine 2 ; a contresigner par machine 2)",
  "=======================================================================", "")
T("nn.0 POSITION")
P("""Ce delta rend le run du gel "la chaine E-A au second ordre". Sa question : completee par son second ordre (le
deplacement Sigma2 de chaque site, un saut au second voisin) et par ses sites bas, la chaine E-A rend-elle la LECTURE de
E-B a k = 3, sur douze points jamais joues, dans des bornes ecrites d'avance : 1.25 jusqu'a |delta| = 0.06, 1.6 jusqu'a
0.10, 2 jusqu'a 0.12 ? Reponse de la feuille : L'ORDRE 2 TIENT. Les trois bandes sont TENUES ; aucun des douze points ne
tombe ; %d etats juges. Les deux issues propres du gel sont L'ORDRE 2 FAIT MIEUX PARTOUT et L'ENERGIE TIENT.""" % n_juges)
P("""Ce chantier n'est pas la piste (0) : il ne requalifie pas E-B, et aucune phrase d'ici ne dit "largeur" sans "lue a
k = 3". Il a ete ouvert par l'operateur ("ok go", le 14/11/2026 a 22 h 04, a machine 1) ; machine 2 ne peut pas le
verifier sur piece (nn.11).""")
P("""Registre a l'ecriture : origin/main 79e77d2, plafond 97 (releve du 15/11 au matin). Aucun numero n'est pris ici
(E18).""")
T("", "nn.1 PIECES (convention B)", "  Au registre (79e77d2)")
piece("scripts/m17_chaine_v17.py", c["moteur"], "le moteur ; il n'est pas modifie")
piece("gels/gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md", c["gel97"], "le gel precedent")
piece("journal/journal_delta_97_domaine_G1_chaine_EA_v1.md", c["acte97"],
      "son acte : la suite \"deriver le residuel de la chaine\" et les trois regles candidates (a), (b), (c)")
T("  Hors registre, de machine 1 (lot %s)" % c["lot_gel"])
piece("gel_ordre2_chaine_EA_pre_enregistrement_v1.md", c["gel"], "le gel")
piece("sonde_ordre2_machine1_v1.py", c["sonde"], "la sonde : elle mesure et ne juge pas")
piece("chaine_ordre2_bloc_machine1_v1.py", c["bloc"], "le bloc de la chaine d'ordre 2, insere tel quel dans la sonde")
piece("lecture_ordre2_machine1_v1.py", c["feuille"], "la feuille : elle juge et ne mesure pas")
piece("note_machine1_residuel_chaine_EA_second_ordre_2026-11-14_v1.md", c["note"],
      "la note hors chaine, apres coup, que ce gel met a l'epreuve ; non certifiee")
T("  Hors registre, de machine 2", "    lot de certification  %s" % c["lot_cert"])
P("certification du gel, de la sonde, de la feuille et du bloc, AVANT le run", 8)
piece("POUR_MACHINE1_certification_gel_ordre2_machine2_v1.md", c["note_cert"], "la note : 0 morsure, six reserves", 6)
piece("ordre2/controles_gel_ordre2_machine2_v1.log", c["log_ctl"], "ses 22 controles de lecture", 6)
piece("ordre2/bloc_independant_machine2_v1.log", c["log_bloc"], "le bloc recalcule a part, 17 controles", 6)
piece("ordre2/garde_et_boites_machine2_v1.log", c["log_garde"], "la garde et la boite recalculees aux seize points", 6)
piece("ordre2/banc_feuille_ordre2_machine2_v1.log", c["log_banc"], "le banc de la feuille et son lecteur independant", 6)
piece("ordre2/compare_essais_16fils_machine1.log", c["log_essais"], "son essai aux ancres contre celui de machine 1", 6)
T("    lot de resultat  %s" % c["lot_res"])
P("le run, sa lecture, les controles de machine 2", 8)
piece("ordre2/sortie/sonde_ordre2.json", c["json_sonde"], "les mesures : seize points, 224 etats", 6)
piece("ordre2/sortie/verdict_ordre2.json", c["json_verdict"], "le verdict rendu par la feuille sur BOCAL4", 6)
piece("ordre2/sortie/lecture_ordre2.log", c["log_lecture"], "son journal", 6)
piece("ordre2/sortie/console_ordre2.log", c["console"], "le journal du pilote : heures et codes de retour", 6)
piece("ordre2/sortie/sonde_ordre2.log", c["log_sonde"], "le journal de la sonde : boites et durees", 6)
piece("POUR_MACHINE1_resultat_ordre2_machine2_v1.md", c["note_res"], "la note de machine 2", 6)
piece("ordre2/sortie/relecture_independante_machine2.log", c["log_indep"], "son lecteur independant, 0 ecart", 6)
piece("ordre2/sortie/compare_run_essai_ancres_machine2.log", c["log_ancres"], "les ancres du run contre son essai", 6)
piece("ordre2/sortie/stabilite_cascade_machine2.log", c["log_cascade"], "le verdict sous le bruit des fils", 6)
piece("ordre2/sortie/sensibilite_bruit_machine2.log", c["log_sens"], "le meme, a des multiples de ce bruit", 6)
piece("ordre2/sortie/stabilite_cascade_machine2_v1_defaut.log", c["log_defaut"], "le defaut de bord de son premier outil", 6)
piece("ordre2/sortie/etat_machine_machine2.log", c["log_etat"], "la batterie et l'horloge du processeur a la fin du run", 6)
T("  De ce lot")
piece("verdict_rejoue_machine1.json", c["mon_verdict"], "la feuille rejouee par machine 1 sur le JSON de machine 2 : le meme canon")
piece("lecture_rejouee_machine1.log", c["mon_journal"], "son journal")
assert sum(len(S[k]["etats"]) for k in ORDRE) == 224

T("", "nn.2 CE QUI A ETE JOUE, ET PAR QUI (E19)")
P("""Machine 1, avant le lot de resultat : aucune decomposition 2D aux quatorze points neufs ; la garde du moteur et les
deux chaines, seules ; la sonde aux deux ancres, points connus. Apres : la feuille, rejouee sur le JSON de machine 2, et
rien d'autre. Machine 1 n'a joue la sonde a aucun point juge ni temoin.""")
P("""Machine 2 : la certification d'abord (22 controles, 0 morsure ; le bloc recalcule a part, 17 controles, 0 morsure),
puis UN run, par un pilote qui verifie les quatre canons : sonde lancee le 14/11 a 23 h 26, finie le 15/11 a 0 h 41, 4524
secondes, code 0 ; les seize points dans l'ordre du gel, W2 en dernier, 14 etats chacun ; aucun arret, aucune reprise,
aucun point rejoue ; puis la feuille (selftest 160 sur 160, code 0). BOCAL4, Windows AMD64, python 3.11.9, numpy 2.2.6,
16 coeurs, variables de fils non fixees.""")
P("""Le run a ete joue SUR BATTERIE, et cette fois c'est sur une piece : batterie a 100 pour cent au lancement, a 62 a
la fin, processeur a 2516 MHz pour un maximum de 3801 (journal de l'etat de la machine). Le gel annoncait de l'ordre de
3100 secondes pour quinze points et 1500 pour W2 ; le run en a pris %d et %d. Durees par point, en secondes : %s.""" % (
    ent(sum(durees[k] for k in ORDRE if k != "W2")), ent(durees["W2"]), ", ".join("%s %d" % (k, ent(durees[k])) for k in ORDRE)))
P("""Rejeu de machine 1 : le verdict rejoue est, objet JSON pour objet JSON, celui que machine 2 a rendu ; les deux
fichiers ont le meme canon %s. Le lecteur independant de machine 2, ecrit du texte du gel, lit la meme chose a chaque
point (0 ecart). Aux deux ancres, le run rend au bit les valeurs de l'essai de sa certification (28 etats, chaines
comprises).""" % c["json_verdict"])

T("", "nn.3 LES GARDES")
P("""Aucune ne mord. G-1 et G-7 : le moteur et la sonde lus au JSON sont aux canons %s et %s. G-2, G-3 : les seize
points sont presents, chacun avec son role, son w2, son facteur, g = facteur x regle, et 14 etats. G-4 : les etats (7,2)
de A1 et (8,2) de A2 rendent la lecture du run de M17 au bit (ecart relatif 0, tolerance 1e-2). G-5 : selftest 160 sur
160, sur BOCAL4 et chez machine 1. G-6 : la garde du moteur consignee porte aux seize points le statut de la table, et
ses D1 et c_max en different de moins de 1e-6 (tolerance 5e-5) ; elle dit HORS DOMAINE a %s. G-8 : aux deux memes etats,
la chaine d'ordre 2 de BOCAL4 rend les references de machine 1 a %.0e pres pour Gamma_flux (tolerance 1e-3) et a
%.0e pres pour dE (tolerance 1e-6).""" % (c["moteur"], c["sonde"], ", ".join(hors_dom), max(g8f.values()), max(g8e.values())))

T("", "nn.4 LES SEIZE POINTS (q = Gamma de chaine / Gamma_2D lue a k = 3, sur les etats juges)")
P("L'ordre 2 : q2 lu a Gamma_flux. Le palier est la plus petite des bornes 1.25, 1.6, 2 qui contient tous les etats juges.")
T("    id  w2       fact  delta  bande      borne  juges   q2 min    med    max   palier  statut")
for k in ORDRE:
    p = R[k]; role = Fe.ATTENDUS[k][0]
    bande = p["bande"] if p["bande"] else ("ancre" if role == "ancre" else "temoin")
    borne = ("%-5s" % ("%g" % p["borne"])) if p["borne"] else "-    "
    if p["statut"] == "NON LISIBLE":
        T("    %s  %-7s  %-4s  %s  %-9s  %s  %3d     NON LISIBLE (moins de 6 etats juges)" % (k, Fe.ATTENDUS[k][1], fac(k), dlt(k), bande, borne, p["n_juges"]))
    else:
        T("    %s  %-7s  %-4s  %s  %-9s  %s  %3d     %s  %s  %s   %-6s  %s" % (
            k, Fe.ATTENDUS[k][1], fac(k), dlt(k), bande, borne, p["n_juges"], f3(p["q2_min"]), f3(p["q2_median"]), f3(p["q2_max"]),
            ("%g" % p["palier"]) if p["palier"] else "aucun", p["statut"]))
P("""La chaine du moteur (q1, lu a -2 Im E), les deux pires ecarts (le plus grand |ln q| d'un etat juge) et le plus grand
ecart d'energie :""")
T("    id   q1 min     med     max   pire o2  pire o1  comparaison   ecart d'energie  energie")
for k in ORDRE:
    p = R[k]
    if p["statut"] == "NON LISIBLE":
        continue
    T("    %s  %7s %7s %7s    %.3f    %.3f   %-11s   %.2e         %s" % (
        k, f3(p["q1_min"]), f3(p["q1_median"]), f3(p["q1_max"]), p["pire_ordre2"], p["pire_ordre1"], p["comparaison"],
        p["ecart_energie_max"], p["energie"]))
P("""Aux douze points juges : %d etats, %d juges, %d exclus (%d sous dix planchers, %d a J flou, %d a barriere vide). A
W2 : 3 etats juges, 11 exclus sous dix planchers.""" % (n_etats, n_juges, n_etats - n_juges, excl["sous dix planchers"], excl["J flou"], excl["barriere vide"]))

T("", "nn.5 LE VERDICT")
P("""Chaque bande a ses quatre points lisibles et aucun ne tombe : PROCHE, MOYENNE et LOINTAINE sont TENUES, et la
cascade rend L'ORDRE 2 TIENT. Plus grand q2 par bande : %s pour une borne de 1.25, %s pour 1.6, %s pour 2 ; ils sont a
C2, M4 et L4. L'ecart est d'un seul cote : le plus petit q2 des %d etats
juges est %s (a C1), le plus grand %s (a L4).""" % (
    f3(par_bande("proche", "q2", max)), f3(par_bande("moyenne", "q2", max)), f3(par_bande("lointaine", "q2", max)),
    n_juges, f3(min(q2s)), f3(max(q2s))))
assert (par_bande("proche", "q2", max), par_bande("moyenne", "q2", max), par_bande("lointaine", "q2", max)) == (R["C2"]["q2_max"], R["M4"]["q2_max"], R["L4"]["q2_max"])
P("""La lecture SANS MARGE (gel, section 11) rend le meme verdict : aucun etat n'est garde par la marge d'un plancher,
la borne nue les contient tous.""")
P("""Ce que le gel autorise a ecrire (section 13), et rien de plus : sur douze points neufs, aux facteurs de 2/3 a 3/2,
la chaine completee par son second ordre et ses sites bas a rendu la lecture de E-B a k = 3 a un facteur 1.25 pres pour
|delta| <= 0.06, 1.6 pres jusqu'a 0.10, 2 pres jusqu'a 0.12. C'est un domaine, borne par bande, de cette chaine-la
contre cette lecture-la.""")

T("", "nn.6 LA COMPARAISON ET LES ENERGIES")
P("""Comparaison au pire etat : les douze points sont MIEUX. La chaine du moteur va, sur les memes %d etats, de q1 = %s
a q1 = %s ; l'ordre 2 de %s a %s. Les trois points ou l'ecart entre les deux pires est le plus mince : L2 (%.3f pour
l'ordre 2 contre %.3f), L1 (%.3f contre %.3f), C3 (%.3f contre %.3f). q1 reste lu a -2 Im E, le moteur n'etant pas
modifie ; machine 2 mesure que cette valeur differe de 0.2 a 0.3 pour cent d'une machine a l'autre aux etats juges (sa
reserve R-2) : l'ecart de L2, %.3f en logarithme, est une dizaine de fois plus large.""" % (
    n_juges, f3(min(q1s)), f3(max(q1s)), f3(min(q2s)), f3(max(q2s)),
    R["L2"]["pire_ordre2"], R["L2"]["pire_ordre1"], R["L1"]["pire_ordre2"], R["L1"]["pire_ordre1"], R["C3"]["pire_ordre2"], R["C3"]["pire_ordre1"],
    ecart_pires["L2"]))
assert 8 <= ecart_pires["L2"] / 0.003 <= 12
P("""Ce que le gel autorise a ecrire : le second ordre est ce qui manquait a la chaine du moteur, aux points lus.""")
P("""Energies : les douze points sont tenus. Plus grand ecart relatif entre le decalage d'energie de la chaine d'ordre 2
et celui de l'etat 2D : %.4f a la bande proche, %.4f a la moyenne, %.4f a la lointaine (a L1), pour une tolerance de
0.01. Ce que le gel autorise a ecrire : la chaine d'ordre 2 rend aussi le decalage d'energie des etats, a un pour cent
pres, ce que les largeurs ne controlent pas.""" % (par_bande("proche", "ecart_energie", max), par_bande("moyenne", "ecart_energie", max), par_bande("lointaine", "ecart_energie", max)))
P("""Ce que ce controle tient, et ce qu'il ne tient pas (certification de machine 2, bloc recalcule a part) : contre
l'energie exacte du H_2D sans absorbeur, a g, g/2 et g/4, l'erreur relative de la chaine d'ordre 2 est divisee par quatre
a chaque moitie de g (7.50e-05, 1.84e-05, 4.59e-06 a l'etat d'ancre de A1) ; a g, l'ordre 1 est a 4.37e-02, "u seul" a
4.40e-02, "Sigma2 seul" a 4.40e-04. L'energie tient donc Sigma2 ; elle ne tient pas le saut au second voisin, qui n'y entre qu'a l'ordre suivant.
Ce saut est tenu autrement : machine 2 le retrouve a 5e-13 pres par une somme sur les 36 sauts de x^5, et a 5e-15 pres
en le lisant sur la matrice H_2D du moteur, sans enumerer aucun saut.""")

T("", "nn.7 LECTURES SANS VERDICT (gel, section 11)")
pal = {v: sorted(k for k in JUG if R[k]["palier"] == v) for v in (1.25, 1.6, 2.0)}
assert pal[1.25] == ["C1", "C2", "C3", "C4", "L1", "M1", "M2", "M3"] and pal[1.6] == ["L2", "L3", "M4"] and pal[2.0] == ["L4"]
NOMBRE = {8: "huit"}
P("""Le palier atteint est en nn.4 : 1.25 a %s points juges, les quatre de la bande proche, M1, M2, M3 et L1 ; 1.6 a
M4, L2 et L3 ; 2 a L4.""" % NOMBRE[len(pal[1.25])])
P("""La loi apres coup de la note, ln(q2) = 2.87 delta^2 m_bord : la mediane de q2 / loi va de %s (L2) a %s (M4 et L3).
Elle surestime au point le plus bas, 1.88.""" % (f3(loi["L2"]), f3(loi["M4"])))
P("""L'arithmetique : le plus grand ecart relatif entre -2 Im E et Gamma_flux de la chaine d'ordre 2, a un point juge,
est %.3f (L4).""" % R["L4"]["flux_contre_im_max"])
P("""Les ancres, points connus : q2 de %s a %s a A1, de %s a %s a A2.""" % (f3(R["A1"]["q2_min"]), f3(R["A1"]["q2_max"]), f3(R["A2"]["q2_min"]), f3(R["A2"]["q2_max"])))
P("""Le temoin W1 (2.14, facteur 1, hors enonce) : %d etats juges, q2 de %s a %s ; sept sont au-dela de 1.6, deux au-dela
de 2 ; aucun palier. Il est MIEUX (%.3f contre %.3f) et tenu en energie (%.4f).""" % (
    R["W1"]["n_juges"], f3(R["W1"]["q2_min"]), f3(R["W1"]["q2_max"]), R["W1"]["pire_ordre2"], R["W1"]["pire_ordre1"], R["W1"]["ecart_energie_max"]))
P("""Le temoin W2 (2.09, facteur 1/2, hors enonce) a ete joue, boite de 89, %d secondes sur batterie, et il est NON
LISIBLE : 3 etats juges sur 14, les 11 autres sous dix planchers. L'acte n'en lit rien ; rien n'est appris au facteur
1/2.""" % ent(durees["W2"]))
P("""Le bruit des fils (machine 2, sa reserve R-3 ; bruit de la cible 7.32e-14 en absolu sur Gamma_2D(3)) : au bruit
mesure, aucun statut de point ne change et un seul verdict est possible. Un etat de L4 peut entrer ou sortir des etats
juges ; le point est TENU dans les deux cas. Le verdict est inchange jusqu'a sept fois ce bruit (5.12e-13) ; a partir de
huit fois (5.86e-13), NE TIENT PAS, TIENT JUSQU'A 0.10 et TIENT sont tous possibles. Ce bruit a ete mesure aux boites de
60 et 61 ; il ne l'a pas ete a celles de 73 et 74 (C1, M3, L4), le gel interdisant de rejouer un point.""")

T("", "nn.8 LES ANNONCES DE LA PLUME, COMPTEES (gel, section 12)")
P("""A-1 : la plume donnait 0.45 a L'ORDRE 2 TIENT, 0.27 a TIENT JUSQU'A 0.10, 0.10 a TIENT JUSQU'A 0.06, 0.08 a NE
TIENT PAS, 0.04 a NON LISIBLE, 0.06 a NON CONCLUANT D'INSTRUMENT. L'issue qu'elle disait la plus probable est sortie.""")
for (nom, pr, quoi, vrai, detail) in AN:
    T(("    %-4s (%.2f) %-46s %s%s" % (nom, pr, quoi, "VRAIE " if vrai else "FAUSSE", (" (%s)" % detail) if detail else "")).rstrip())
P("""%d annonces jugees sur 20 sont vraies ; les deux fausses sont A-11 (la loi apres coup, a L2) et A-13 (W2 n'est pas
lisible). La condition de A-5 et les deux sous-annonces de A-13 ne sont pas jugees. La somme des probabilites annoncees
est %.1f pour %d vraies : ces annonces ne sont pas independantes, presque toutes tiennent a la meme question, et la plume
n'en tire aucune phrase de calibrage.""" % (n_vraies, attendu, n_vraies))

T("", "nn.9 DEFAUTS ET RESERVES")
P("""D-O2-1 (m1) : la plume a ecrit a l'operateur, avant de calculer la grille, 0.85 pour "un facteur 1.6 jusqu'a |delta|
= 0.12". Le gel le dit (section 2 (iii)). Le run le dement : le palier de L4 est 2, son plus grand q2, %s, est au-dela
de 1.6. C'est le defaut D-G1-3 du delta 97, refait le meme jour.""" % f3(R["L4"]["q2_max"]), 2, 4)
P("""D-O2-2 (m1 ; reserve R-1 de machine 2) : le selftest de la feuille laisse passer 22 des 115 alterations d'une ligne
que machine 2 lui oppose ; son banc en mord 20, les deux dernieres etant equivalentes. La table est tenue (131 alterations
sur 131), ce que la regle candidate (a) demandait ; le reste ne l'est qu'en partie : les tolerances de G-8, des bords
d'inegalite, des lectures declarees. Ce sont des trous du selftest, pas des defauts de la feuille : le lecteur
independant de machine 2 et la feuille s'accordent sur 4000 sondes synthetiques, et sur le run.""", 2, 4)
P("""D-O2-3 (m1) : W2 a coute %d secondes sur batterie pour 3 etats juges. La plume avait estime sa lisibilite sur les 32
sites voisins de la graine, pas sur les 14 etats que la sonde retient ; elle annoncait 0.65 (A-13).""" % ent(durees["W2"]), 2, 4)
P("""D-O2-4 (m1 ; reserve R-4 de machine 2) : deux chiffres de la note different de ceux que machine 2 recalcule : 7.00
pour 6.987 (repris par le gel, section 2 (i)), et 241 etats sur 243 dans un facteur 1.5 pour 242. Ils viennent de
l'arrondi de -2 Im E aux plus petites largeurs ; rien ne s'y appuie.""", 2, 4)
P("""D-O2-5 (m1) : la note ecrit que les energies "preferent la somme des deux termes a chacun pris seul". Le controle de
machine 2 (nn.6) montre que l'energie tient Sigma2 et non le saut au second voisin. La phrase de la note est trop forte.""", 2, 4)
P("""R-2 (m2) : -2 Im E de la chaine du moteur s'arrondit d'une machine a l'autre, Gamma_flux non (1e-9). Le choix de
Gamma_flux pour q2 tient ; q1 reste a -2 Im E (nn.6).""", 2, 4)
P("""R-3 (m2) : la marge d'un plancher vaut 1.7 fois le bruit qu'elle mesure sur Gamma_2D(3) ; le verdict, lui, tient
jusqu'a sept fois ce bruit (nn.7).""", 2, 4)
P("""R-5 (m2) : l'ouverture n'est pas verifiable sur piece par machine 2 (nn.11).""", 2, 4)
P("""R-6 (m2) : elle ne verifie ni le rattachement des deux termes a la litterature, ni la note d'anteriorite, ni les
choix de la plume (bandes, bornes, points, comparaison au pire etat, tolerance d'energie) : ils sont ecrits d'avance, pas
valides.""", 2, 4)
P("""De machine 2, declares par elle : six de ses controles ont mordu a ses premiers jets, par sa faute, sans toucher au
gel ; son premier outil de lecture sous le bruit avait un defaut de bord, qu'elle a corrige par une version derivee, la
premiere restant jointe.""", 2, 4)

T("", "nn.10 CE QUE LE RESULTAT CHANGE A CE QUI ETAIT ECRIT")
P("""Note %s : elle etait une lecture apres coup de 22 points connus. Sur douze points neufs, dans des bornes ecrites
avant le run, sa lecture tient ; l'acte en ecrit ce que nn.5 et nn.6 autorisent. Sa loi apres coup reste une
description : elle manque a L2. Deux de ses chiffres et une de ses phrases sont corriges (D-O2-4, D-O2-5).""" % c["note"])
P("""Delta 97, nn.11 (iv) : la suite "deriver le residuel de la chaine" est faite, et mise a l'epreuve. Ce que cet acte
decrivait sans l'expliquer, un rapport qui change de sens a 2.00, croit avec le desaccord et depend du facteur, est, aux
points lus, le second ordre de la chaine. Son verdict, LA GARDE NE TIENT PAS, n'est pas touche.""")
P("""Gel %s, section 2 (ii) : la plume supposait un second canal vers 1.85. A L2, le point le plus bas (1.88), aucun etat
n'est trop bas : le plus petit q2 y est %s. Rien n'est dit de 1.85.""" % (c["gel"], f3(R["L2"]["q2_min"])))
P("""La lecture de E-B garde son statut : elle n'est pas qualifiee. Deux calculs aux absorbeurs differents s'accordent
dans les bornes du gel a douze points ; cet acte n'en tire rien sur la lecture elle-meme. Les verdicts PAS DE SIGNAL de
M17, NON QUALIFIE de la nuit bis, TENU EN PARTIE et LA GARDE NE TIENT PAS ne sont pas touches.""")

T("", "nn.11 A ARBITRER PAR L'OPERATEUR")
P("(i) Le numero (E18) et le depot.", 2, 6)
P("""(ii) L'ouverture. Seul l'operateur peut attester qu'il a ouvert ce chantier le 14/11 a 22 h 04 ; son message de
depot le dit ou non. Machine 2 a joue parce que l'envoi le demandait et que l'operateur l'a porte.""", 2, 6)
P("""(iii) La suite. Cet acte n'en propose aucune comme decidee. Il en existe : porter l'ordre 2 dans le moteur, ce qui
demande une nouvelle version ; calculer l'ordre suivant, le residu etant d'un seul cote, croissant avec le desaccord, et
non explique ; eprouver le facteur 1/2, que W2 n'a pas rendu lisible, ou le desaccord au-dela de 0.12, ou W1 va jusqu'a
%s ; reprendre la piste (0) avec cette chaine pour second calcul ; ou rien, ce verdict se deposant tel quel.""" % f3(R["W1"]["q2_max"]), 2, 6)
P("""(iv) Les regles. Cet acte n'en propose aucune (nn.12).""", 2, 6)

T("", "nn.12 REGLES CANDIDATES SOUS (X)")
P("""Aucune regle nouvelle ; trente-quatre attendent la revue. Pour cette revue, ce que les trois regles candidates du
delta 97, appliquees ici sans etre adoptees, ont donne :""")
P("""(a) le selftest porte sa propre copie de la table : la table est tenue (131 sur 131), le reste du selftest ne l'est
pas (D-O2-2) ; ce qui tient la feuille, c'est le banc de la machine qui certifie.""", 2, 6)
P("""(b) la borne porte une marge d'un plancher et la lecture sans marge est rendue : ici la marge n'a garde aucun etat,
et machine 2 mesure que le verdict tient jusqu'a sept fois le bruit.""", 2, 6)
P("""(c) la tete du registre a ete relevee, et le gel n'a rien cite a tort hors registre ; mais la plume a encore
conseille un gel avec un chiffre avant de calculer (D-O2-1).""", 2, 6)
assert "trente et une attendent" in acte97    # 31 avant le delta 97, plus ses trois regles (a), (b), (c)

T("", "nn.13 LE CANAL")
P("""Lots echanges pour ce chantier (canons) : machine 1 -- le gel et ses instruments %s ; machine 2 -- la certification
%s, le resultat %s. Les enveloppes qui les ont portes ne sont pas des lots et ne se citent pas.""" % (c["lot_gel"], c["lot_cert"], c["lot_res"]))

T("", "nn.14 CE QUE CE DELTA NE FAIT PAS")
P("""Il n'affirme aucune largeur intrinseque et ne dit pas que la chaine est "qualifiee" : elle rend, dans des bornes
dites, une lecture qui ne l'est pas. Il ne dit rien hors des facteurs de 2/3 a 3/2, de la fraction 0.70, du canal 2:1 de
x^5 et de |delta| de 0.03 a 0.12. Il ne dit pas d'ou vient le residu. Il ne rejoue aucun point, ne relit sous aucune
autre borne, aucune autre bande, aucun autre critere, aucune autre population (gel, section 14). Il ne modifie pas le
moteur. Il ne rouvre pas la piste (0). Il ne prend aucun numero, n'adopte aucune regle, n'edite aucune piece citee
(PB-1).""")

T("", "nn.15 PIECES DU LOT",
  "  journal_delta_nn_ordre2_chaine_EA_v1.md               cet acte",
  "  ecrire_acte_ordre2_machine1_v1.py                     le script qui pose nombres et canons",
  "  verdict_rejoue_machine1.json, lecture_rejouee_machine1.log   la feuille rejouee par machine 1",
  "  releve_acte_ordre2_machine1_v1.py / .log              le releve de sortie de machine 1",
  "  contre_epreuve_releve_acte_ordre2_machine1_v1.py / .log   ce releve, sur des copies alterees",
  "  POUR_MACHINE2_acte_ordre2_machine1_v1.md              la note d'accompagnement",
  "  fabrique_lot_machine1_v2.py",
  "  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.",
  "", "-- FIN journal_delta_nn_ordre2_chaine_EA_v1 --")

txt = "\n".join(L) + "\n"
assert all(ord(ch) < 128 for ch in txt) and "%" not in txt, [ch for ch in txt if ord(ch) >= 128][:5]
longues = [(i + 1, len(l)) for i, l in enumerate(L) if len(l) > 100]
assert not longues, longues
debuts = [i + 1 for i, l in enumerate(L) if l.lstrip()[:1] in (";", ":", "?")]
assert not debuts, debuts
assert not [i + 1 for i, l in enumerate(L) if l != l.rstrip()]
dst = SORTIE + "/journal_delta_nn_ordre2_chaine_EA_v1.md"
open(dst, "w", encoding="ascii", newline="\n").write(txt)
print("acte ecrit : %s  canon %s  %d lignes" % (dst, B(dst), len(L)))
