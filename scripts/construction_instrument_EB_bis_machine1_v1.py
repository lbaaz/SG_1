# -*- coding: ascii -*-
# CONSTRUCTION DE L'INSTRUMENT DU GEL BIS (PB-1 : les pieces certifiees et
# deposees ne sont pas editees). Sonde v3 = v2, feuille v2 = v1, banc v3 = v2,
# chacune + des remplacements a ANCRE UNIQUE. Le canon du gel bis est LU du
# fichier du gel, jamais tape. Un ancre absent ou double arrete tout.
# Arguments : <dossier scripts/ du registre> <gel bis> <sortie> <journal>
import sys, os, hashlib, unicodedata

SCR, GEL, SORTIE, JOURNAL = sys.argv[1:5]
F = open(JOURNAL, "w", encoding="ascii", newline="\n")


def dire(s):
    print(s)
    F.write(s + "\n")


def cB(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8"))
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


G = cB(GEL)
V2 = "cde0cd11a763f26d"

SONDE = [
("S0", '''# SONDE DE QUALIFICATION E-B -- machine 1, v2 -- gel E-B v2 cde0cd11a763f26d
# v2 = v1 (214ea376cbf540a4) + D-1 (identite de reprise) + D-2 (porte).''',
       '''# SONDE DE QUALIFICATION E-B -- machine 1, v3 -- gel E-B bis v1 @GEL@
# v3 = v2 (facc7536ba4637cb) + l'echelle du gel bis (k = -5 a 12) et ses
# comptes. v2 = v1 (214ea376cbf540a4) + D-1 (identite de reprise) + D-2 (porte).'''),
("S1", '''CANON_GEL = "cde0cd11a763f26d"''', '''CANON_GEL = "@GEL@"'''),
("S2", '''K_ECH = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 2, 1, 0, -1, -2]   # ordre declare''',
       '''K_ECH = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 2, 1, 0, -1, -2, -3, -4, -5]   # ordre declare (gel bis, 3.6)'''),
("S3", '''        att = {"TP": 60, "TN": 15, "plancher": 30}
        att["TP"] = 30 * len(res["TP"])''',
       '''        n = len(K_ECH)
        att = {"TP": 4 * n, "TN": n, "plancher": 30}
        att["TP"] = 2 * n * len(res["TP"])'''),
("S4", '''        att = {"F1": 180, "formes": 180, "translation": 90, "ouverture": 6}''',
       '''        n = len(K_ECH)
        att = {"F1": 12 * n, "formes": 12 * n, "translation": 6 * n,
               "ouverture": 6}'''),
("S5", '''    dire("SONDE DE QUALIFICATION E-B v2 -- gel %s -- etage %d%s%s" % (''',
       '''    dire("SONDE DE QUALIFICATION E-B v3 -- gel %s -- etage %d%s%s" % ('''),
]

LECTURE = [
("L0", '''# FEUILLE DE LECTURE DE LA QUALIFICATION E-B -- machine 1, v1
# gel E-B v2 cde0cd11a763f26d. CLASSE 2.''',
       '''# FEUILLE DE LECTURE DE LA QUALIFICATION E-B -- machine 1, v2
# v2 = v1 (b3ac958a1a2b915b) + l'echelle du gel bis (bornes de fenetre, un
# cas de G-Q7) + deux refus a l'entree (gel de la sortie ; g de la sonde
# contre g de la table, observation O-2 de m2). Aucun seuil ne change.
# gel E-B bis v1 @GEL@. CLASSE 2.'''),
("L1", '''CANON_GEL = "cde0cd11a763f26d"''', '''CANON_GEL = "@GEL@"
K_MIN, K_MAX = -5, 12                      # echelle du gel bis, 3.6'''),
("L2", '''    for k0 in range(-2, 9):''', '''    for k0 in range(K_MIN, K_MAX - 3):'''),
("L3", '''    eta = {k: 0.05 * 2.0 ** (-k) for k in range(-2, 13)}''',
       '''    eta = {k: 0.05 * 2.0 ** (-k) for k in range(K_MIN, K_MAX + 1)}'''),
("L4", '''    t("plateau de cinq puis chute lineaire", (p["statut"], p.get("k0")),
      ("PLATEAU", 2))''',
       '''    t("plateau de cinq puis chute lineaire", (p["statut"], p.get("k0")),
      ("PLATEAU", 2))
    f = {k: (2e-10 if k <= -1 else 2e-10 * eta[k] / eta[-1]) for k in eta}
    p = plateau(f)
    t("plateau au bord fort (k = -5 a -1) puis chute",
      (p["statut"], p.get("k0")), ("PLATEAU", -5))'''),
("L5", '''    dire("FEUILLE DE LECTURE E-B v1 -- gel %s -- etage %d" % (CANON_GEL, a.etage))''',
       '''    dire("FEUILLE DE LECTURE E-B v2 -- gel %s -- etage %d" % (CANON_GEL, a.etage))'''),
("L6", '''        ref = json.load(open(a.reference))
        if s1.get("prevol"):''',
       '''        ref = json.load(open(a.reference))
        if s1.get("gel") != CANON_GEL:
            dire("LECTURE REFUSEE : la sortie de la sonde porte le gel %s,"
                 " cette feuille juge le gel %s" % (s1.get("gel"), CANON_GEL))
            sys.exit(2)
        gt = {r["j"]: r["g"] for r in ref["balayage"]}
        for cle in sorted(s1["TP"]):
            if gt.get(s1["TP"][cle]["j"]) != s1["TP"][cle]["g"]:
                dire("LECTURE REFUSEE (O-2) : a %s le g de la sonde (%r) n'est"
                     " pas celui de la table (%r)" % (
                         cle, s1["TP"][cle]["g"], gt.get(s1["TP"][cle]["j"])))
                sys.exit(2)
        if s1.get("prevol"):'''),
("L7", '''        s2 = json.load(open(f2)) if os.path.exists(f2) else None
''',
       '''        s2 = json.load(open(f2)) if os.path.exists(f2) else None
        if s2 is not None and s2.get("gel") != CANON_GEL:
            dire("LECTURE REFUSEE : la sortie de l'etage 2 porte le gel %s,"
                 " cette feuille juge le gel %s" % (s2.get("gel"), CANON_GEL))
            sys.exit(2)
'''),
]

BANC = [
("K0", '''# BANC QUI TUE DE LA QUALIFICATION E-B -- machine 1, v2 -- gel E-B v2
# v2 = v1 (666e69f11bc1f72c) + D-3 (-P), temoins de D-1 et D-2, O-3.
# cde0cd11a763f26d, section 10.''',
       '''# BANC QUI TUE DE LA QUALIFICATION E-B -- machine 1, v3 -- gel E-B bis v1
# v3 = v2 (4e46744fe4e8a8be) + l'echelle du gel bis dans les series
# synthetiques. v2 = v1 (666e69f11bc1f72c) + D-3 (-P), temoins de D-1 et
# D-2, O-3.
# @GEL@, section 10.'''),
("K1", '''for f in fonctions]} for k in range(-2, 13)}''', '''for f in fonctions]} for k in range(-5, 13)}'''),
]

PIECES = [
    ("sonde_qualification_EB_machine1_v2.py", "facc7536ba4637cb", "sonde_qualification_EB_machine1_v3.py", SONDE),
    ("lecture_qualification_EB_machine1_v1.py", "b3ac958a1a2b915b", "lecture_qualification_EB_machine1_v2.py", LECTURE),
    ("banc_qui_tue_qualification_EB_machine1_v2.py", "4e46744fe4e8a8be", "banc_qui_tue_qualification_EB_machine1_v3.py", BANC),
]
dire("gel bis v1 : canon %s (lu du fichier %s)" % (G, os.path.basename(GEL)))
for src, att, dst, hunks in PIECES:
    assert cB(os.path.join(SCR, src)) == att, (src, cB(os.path.join(SCR, src)))
    t = open(os.path.join(SCR, src), encoding="ascii").read()
    for h, vieux, neuf in hunks:
        assert t.count(vieux) == 1, "%s %s : ancre trouve %d fois" % (dst, h, t.count(vieux))
        t = t.replace(vieux, neuf.replace("@GEL@", G))
        dire("  %-3s %s : %3d -> %3d caracteres ; ancre %r" % (h, dst.split("_")[0], len(vieux), len(neuf), vieux.split("\n")[0][:48]))
    assert V2 not in t and "@GEL@" not in t and t.count(G) >= 1, dst      # plus aucune trace du canon du gel v2
    compile(t, dst, "exec")
    open(os.path.join(SORTIE, dst), "w", encoding="ascii", newline="\n").write(t)
    dire("ecrit : %s, canon %s, %d o (depuis %s %s, %d remplacements)" % (dst, cB(os.path.join(SORTIE, dst)), len(t), src, att, len(hunks)))
dire("-- FIN construction_instrument_EB_bis_machine1_v1 --")
