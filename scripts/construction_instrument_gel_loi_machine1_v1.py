# -*- coding: ascii -*-
"""CONSTRUCTION DE L'INSTRUMENT du gel "loi de la largeur, ordre 3", seconde partie -- machine 1, v1, 2026-11-15.
Aucun calcul. Ecrit, dans le dossier de sortie : la TABLE GELEE des points (les douze cellules tirees et les deux ancres),
la table du pre-vol (points DEJA JOUES), et trois scripts DERIVES PAR REMPLACEMENTS de scripts certifies, jamais edites :
  sonde_dense_gel_loi_machine1_v1.py     de  sonde_ordre2_machine1_v1.py              (24315c52b234319c, delta 98)
  sonde_lecteur_gel_loi_machine1_v1.py   de  sonde_qualification_EB_ter_machine1_v1.py (b5616dcf858e8801, gel ter)
  lecture_lecteur_gel_loi_machine1_v1.py de  lecture_qualification_EB_ter_machine1_v1.py (gel ter)
Chaque remplacement doit trouver son texte UNE fois dans la source, sinon la construction s'arrete. Les canons sont
enchaines : table -> sonde dense -> sonde du lecteur -> feuille du lecteur. Un diff unifie est ecrit pour chaque derive.
Usage : python3 -I construction_instrument_gel_loi_machine1_v1.py <sonde dense certifiee> <sonde du gel ter> <feuille du
        gel ter> <journal de mon tirage> <dossier de sortie>"""
import sys, os, re, json, difflib, hashlib, unicodedata
from fractions import Fraction as F
S_DENSE, S_LECTEUR, S_FEUILLE, TIRAGE, OUT = sys.argv[1:6]
os.makedirs(OUT, exist_ok=True)
def canon_txt(t):
    t = unicodedata.normalize("NFC", t).replace("\r\n", "\n").replace("\r", "\n"); return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def canon(chemin):
    return canon_txt(open(chemin, "rb").read().decode("utf-8"))
ATTENDUS = {S_DENSE: "24315c52b234319c", S_LECTEUR: "b5616dcf858e8801"}
for ch, c in ATTENDUS.items():
    assert canon(ch) == c, (ch, canon(ch))
CANON_FEUILLE_TER = canon(S_FEUILLE)

# --- 1. les tables ---
cel = []
for l in open(TIRAGE):
    m = re.match(r"\s+(N[1-5]|P[1-5]|BN|BP)\s+w2 = (\S+)\s+facteur (\S+)\s*$", l)
    if m:
        w2, fac = F(m.group(2)), F(m.group(3))
        cel.append({"id": m.group(1), "role": "juge", "creneau": re.sub(r"\d", "", m.group(1)), "w2": "%d/%d" % (w2.numerator, w2.denominator), "facteur": "%d/%d" % (fac.numerator, fac.denominator)})
assert [c["id"] for c in cel] == ["N1", "N2", "N3", "N4", "N5", "P1", "P2", "P3", "P4", "P5", "BN", "BP"], [c["id"] for c in cel]
ANCRES = [{"id": "A1", "role": "ancre", "creneau": None, "w2": "39/20", "facteur": "1/1"}, {"id": "A2", "role": "ancre", "creneau": None, "w2": "41/20", "facteur": "1/1"}]
def ecrire_json(nom, obj):
    ch = os.path.join(OUT, nom); open(ch, "w", encoding="ascii", newline="\n").write(json.dumps(obj, indent=1, sort_keys=True) + "\n"); return ch
T_GEL = ecrire_json("table_points_gel_loi_ordre3_v1.json", {"table": "gel loi de la largeur, ordre 3 : les douze cellules tirees et les deux ancres du depot", "graine": "200482",
                    "rang": 0, "prevol": False, "points": cel + ANCRES})
T_PRE = ecrire_json("table_points_prevol_gel_loi_ordre3_v1.json", {"table": "PRE-VOL : un point DEJA JOUE (C3 du delta 98) et les deux ancres ; ne juge rien", "graine": None,
                    "rang": None, "prevol": True, "points": [{"id": "C3", "role": "juge", "creneau": "P", "w2": "203/100", "facteur": "3/2"}] + ANCRES})
CANON_TABLE, CANON_TABLE_PREVOL = canon(T_GEL), canon(T_PRE)

def deriver(source, nom, remplacements):
    s = open(source, encoding="ascii").read(); t = s
    for i, (a, b) in enumerate(remplacements):
        assert t.count(a) == 1, "%s : remplacement %d, texte trouve %d fois : %r" % (nom, i + 1, t.count(a), a[:70])
        t = t.replace(a, b)
    t.encode("ascii"); ch = os.path.join(OUT, nom); open(ch, "w", encoding="ascii", newline="\n").write(t)
    d = list(difflib.unified_diff(s.split("\n"), t.split("\n"), os.path.basename(source), nom, lineterm="", n=1))
    open(os.path.join(OUT, nom[:-3] + ".diff"), "w", encoding="ascii", newline="\n").write("\n".join(d) + "\n")
    print("%-44s canon %s ; %2d remplacements ; diff : %d blocs, %d lignes retirees, %d ajoutees" % (nom, canon(ch), len(remplacements), sum(l.startswith("@@") for l in d),
          sum(l.startswith("-") and not l.startswith("---") for l in d), sum(l.startswith("+") and not l.startswith("+++") for l in d)))
    return ch

# --- 2. la sonde dense ---
R_DENSE = [
 ('"""SONDE DU GEL "LA CHAINE E-A AU SECOND ORDRE" -- machine 1, v1, 2026-11-14.\n',
  '"""SONDE DENSE DU GEL "LOI DE LA LARGEUR, ORDRE 3" -- machine 1, v1, 2026-11-15. Derivee par remplacements de\n'
  'sonde_ordre2_machine1_v1.py (24315c52b234319c), jamais editee : memes mesures, meme code ; SEULS CHANGENT les points,\n'
  'lus dans une TABLE GELEE (fichier a canon) au lieu d\'etre ecrits dans le script, et l\'en-tete de la sortie.\n'
  'Usage : python -I sonde_dense_gel_loi_machine1_v1.py <moteur_v17.py> <table des points.json> <sortie.json> [id ...] [--prevol]\n'
  'Sans --prevol la table doit etre au canon du gel ; avec --prevol elle ne doit PAS l\'etre (points deja joues) et la\n'
  'sortie porte "prevol": true. Le texte ci-dessous est celui de la sonde d\'origine.\n'
  'SONDE DU GEL "LA CHAINE E-A AU SECOND ORDRE" -- machine 1, v1, 2026-11-14.\n'),
 ('MOTEUR, SORTIE = sys.argv[1], sys.argv[2]\nDEMANDES = sys.argv[3:]\n',
  'MOTEUR, TABLE, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]\nDEMANDES = [a for a in sys.argv[4:] if a != "--prevol"]\nPREVOL = "--prevol" in sys.argv[4:]\n'
  'CANON_MOTEUR, CANON_TABLE = "82a0be882568fe0c", "%s"\n' % CANON_TABLE),
 ('''POINTS = [  # (id, role, w2, facteur sur g_du_point)
    ("C1", "juge", F(197, 100), F(2, 3)), ("C2", "juge", F(97, 50), F(3, 4)),
    ("C3", "juge", F(203, 100), F(3, 2)), ("C4", "juge", F(103, 50), F(4, 3)),
    ("M1", "juge", F(193, 100), F(1)), ("M2", "juge", F(48, 25), F(4, 3)),
    ("M3", "juge", F(207, 100), F(2, 3)), ("M4", "juge", F(21, 10), F(3, 4)),
    ("L1", "juge", F(189, 100), F(4, 3)), ("L2", "juge", F(47, 25), F(1)),
    ("L3", "juge", F(211, 100), F(3, 2)), ("L4", "juge", F(53, 25), F(2, 3)),
    ("A1", "ancre", F(39, 20), F(1)), ("A2", "ancre", F(41, 20), F(1)),
    ("W1", "temoin", F(107, 50), F(1)), ("W2", "temoin", F(209, 100), F(1, 2)),   # les temoins en dernier
]
''',
  'POINTS = [(str(p["id"]), str(p["role"]), F(str(p["w2"])), F(str(p["facteur"]))) for p in json.load(open(TABLE))["points"]]   # (id, role, w2, facteur)\n'),
 ('''def main():
    ids = [p[0] for p in POINTS]
''',
  '''def main():
    if canon_B(MOTEUR) != CANON_MOTEUR:
        raise SystemExit("REFUS : le moteur n'est pas au canon %s" % CANON_MOTEUR)
    if (canon_B(TABLE) == CANON_TABLE) == PREVOL:
        raise SystemExit("REFUS : sans --prevol la table doit etre au canon %s ; avec --prevol elle ne doit pas l'etre" % CANON_TABLE)
    ids = [p[0] for p in POINTS]
'''),
 ('    sortie = {"sonde": "sonde_ordre2_machine1_v1", "moteur_canon": canon_B(MOTEUR),\n',
  '    sortie = {"sonde": "sonde_dense_gel_loi_machine1_v1", "moteur_canon": canon_B(MOTEUR), "table_canon": canon_B(TABLE), "prevol": PREVOL,\n'),
]
P_DENSE = deriver(S_DENSE, "sonde_dense_gel_loi_machine1_v1.py", R_DENSE); CANON_DENSE_SONDE = canon(P_DENSE)

# --- 3. la sonde du lecteur ---
R_LECT = [
 ('"""SONDE DE LA QUALIFICATION E-B TER -- machine 1, v1, 2026-11-15. CLASSE 2. Elle MESURE et ne juge pas.\n',
  '"""SONDE DU LECTEUR DU GEL "LOI DE LA LARGEUR, ORDRE 3" -- machine 1, v1, 2026-11-15. Elle MESURE et ne juge pas.\n'
  'Derivee par remplacements de sonde_qualification_EB_ter_machine1_v1.py (b5616dcf858e8801), jamais editee : meme lecteur,\n'
  'memes absorbeurs, memes barreaux. SEULS CHANGENT : les points du mode "point", pris dans la TABLE GELEE et lus dans la\n'
  'SORTIE DENSE DU RUN, dont le canon est passe en argument par le pilote (les ancres et les temoins restent ceux du depot\n'
  'du delta 98, au canon en dur) ; et l\'en-tete de la sortie. Arguments, dans l\'ordre :\n'
  '  <moteur_v17.py> <sonde_ordre2.json (depot)> <tp_retenus.json> <table des points.json> <sortie dense.json>\n'
  '  <canon de la sortie dense> <dossier de sortie> <mode> [<id> ...] [--prevol]\n'
  'Le texte ci-dessous est celui de la sonde d\'origine (ses "douze points juges" sont ici ceux de la table).\n'
  'SONDE DE LA QUALIFICATION E-B TER -- machine 1, v1, 2026-11-15. CLASSE 2. Elle MESURE et ne juge pas.\n'),
 ('MOTEUR, DEPOT, RETENUS, DOSSIER, MODE = sys.argv[1:6]\nIDS = sys.argv[6:]\n',
  'MOTEUR, DEPOT, RETENUS, TABLE, DENSE, CANON_DENSE, DOSSIER, MODE = sys.argv[1:9]\nIDS = [a for a in sys.argv[9:] if a != "--prevol"]\nPREVOL = "--prevol" in sys.argv[9:]\n'
  'CANON_TABLE, CANON_SONDE_DENSE, CANON_SONDE_DEPOT, N_ETATS_DENSE = "%s", "%s", "24315c52b234319c", 14\n' % (CANON_TABLE, CANON_DENSE_SONDE)),
 ('JUGES = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4"]\n',
  'T_POINTS = {str(p["id"]): p for p in json.load(open(TABLE))["points"]}\nJUGES = [i for i, p in T_POINTS.items() if p["role"] == "juge"]\n'),
 ('''for chemin, attendu, quoi in ((MOTEUR, CANON_MOTEUR, "moteur"), (DEPOT, CANON_DEPOT, "depot du delta 98"), (RETENUS, CANON_RETENUS, "couplages retenus")):
    if canon_B(chemin) != attendu:
        raise SystemExit("REFUS : le canon du %s (%s) n'est pas %s" % (quoi, canon_B(chemin), attendu))
''',
  '''for chemin, attendu, quoi in ((MOTEUR, CANON_MOTEUR, "moteur"), (DEPOT, CANON_DEPOT, "depot du delta 98"), (RETENUS, CANON_RETENUS, "couplages retenus")):
    if canon_B(chemin) != attendu:
        raise SystemExit("REFUS : le canon du %s (%s) n'est pas %s" % (quoi, canon_B(chemin), attendu))
if (canon_B(TABLE) == CANON_TABLE) == PREVOL:
    raise SystemExit("REFUS : sans --prevol la table doit etre au canon %s ; avec --prevol elle ne doit pas l'etre" % CANON_TABLE)
'''),
 ('''def main():
    D = json.load(open(DEPOT)); P = {p["id"]: p for p in D["points"]}
    sortie = {"sonde": "sonde_qualification_EB_ter_machine1_v1", "sonde_canon": canon_B(os.path.abspath(__file__)),
''',
  '''def points_de_la_sortie_dense():
    """Les points du mode "point" : lus dans la sortie dense du run, apres controle du canon passe et de la forme."""
    if canon_B(DENSE) != CANON_DENSE:
        raise SystemExit("REFUS : la sortie dense (%s) n'est pas au canon passe par le pilote (%s)" % (canon_B(DENSE), CANON_DENSE))
    DD = json.load(open(DENSE))
    if DD.get("moteur_canon") != CANON_MOTEUR or DD.get("sonde_canon") not in ((CANON_SONDE_DENSE, CANON_SONDE_DEPOT) if PREVOL else (CANON_SONDE_DENSE,)):
        raise SystemExit("REFUS : la sortie dense ne porte pas les canons du moteur et de la sonde dense")
    if not PREVOL and (DD.get("table_canon") != CANON_TABLE or DD.get("prevol") is not False):
        raise SystemExit("REFUS : la sortie dense n'a pas ete produite sur la table du gel")
    PD = {p["id"]: p for p in DD["points"]}
    for i in IDS:
        if i not in PD:
            raise SystemExit("REFUS : le point %s manque a la sortie dense" % i)
        p, t = PD[i], T_POINTS[i]; w2 = F(str(p["w2"])); g_att = float(M.g_du_point(w2)) * float(F(str(p["facteur"])))
        if w2 != F(str(t["w2"])) or F(str(p["facteur"])) != F(str(t["facteur"])) or abs(p["g"] / g_att - 1.0) > 1e-12 or len(p["etats"]) != N_ETATS_DENSE or not p.get("faisable"):
            raise SystemExit("REFUS : forme de la sortie dense au point %s (w2, facteur, couplage, nombre d'etats, faisable)" % i)
    return PD

def main():
    D = json.load(open(DEPOT)); P = {p["id"]: p for p in D["points"]}
    sortie = {"sonde": "sonde_lecteur_gel_loi_machine1_v1", "sonde_canon": canon_B(os.path.abspath(__file__)),
              "table_canon": canon_B(TABLE), "dense_canon": (CANON_DENSE if MODE == "point" else None), "prevol": PREVOL,
'''),
 ('''        sortie["points"] = [mesurer_point(P[pid], "juges", ABSORBEURS, KS) for pid in IDS]
''',
  '''        PD = points_de_la_sortie_dense()
        sortie["points"] = [mesurer_point(PD[pid], "juges", ABSORBEURS, KS) for pid in IDS]
'''),
]
P_LECT = deriver(S_LECTEUR, "sonde_lecteur_gel_loi_machine1_v1.py", R_LECT); CANON_LECT_SONDE = canon(P_LECT)

# --- 4. la feuille du lecteur ---
R_FEUILLE = [
 ('# FEUILLE DE LECTURE DE LA QUALIFICATION E-B TER -- machine 1, v1, 2026-11-15. CLASSE 2.\n',
  '# FEUILLE DU LECTEUR DU GEL "LOI DE LA LARGEUR, ORDRE 3" -- machine 1, v1, 2026-11-15. Derivee par remplacements de\n'
  '# lecture_qualification_EB_ter_machine1_v1.py (%s), jamais editee : meme routine de plateau, memes statuts par etat,\n'
  '# meme etage de l\'instrument, meme selftest. SEULS CHANGENT, a l\'etape "verdict" : les points juges sont ceux de la TABLE\n'
  '# GELEE, lus dans la SORTIE DENSE DU RUN (canon passe par le pilote, forme controlee avant toute lecture) ; un point dont\n'
  '# l\'etat de rang 0 n\'est pas lu n\'arrete plus la lecture (son "etat_lu" vaut "NON LU") ; le verdict porte trois canons de plus.\n'
  '# Usage de l\'etape "verdict" : ... verdict <dossier> <sonde_ordre2.json (depot)> <table des points.json> <sortie dense.json>\n'
  '#   <canon de la sortie dense> [--prevol]      ; l\'etape "instrument" et --selftest sont inchanges.\n'
  '# Le texte ci-dessous est celui de la feuille d\'origine.\n'
  '# FEUILLE DE LECTURE DE LA QUALIFICATION E-B TER -- machine 1, v1, 2026-11-15. CLASSE 2.\n' % CANON_FEUILLE_TER),
 ('CANON_SONDE = "b5616dcf858e8801"\n',
  'CANON_SONDE = "%s"\nCANON_TABLE, CANON_SONDE_DENSE, CANON_SONDE_DEPOT, N_ETATS_DENSE = "%s", "%s", "24315c52b234319c", 14\n' % (CANON_LECT_SONDE, CANON_TABLE, CANON_DENSE_SONDE)),
 ('''    lu0 = [j for j in etats if j["rang"] == 0]
    if len(lu0) != 1:
        raise Refus("point %s : l'etat de rang 0 n'est pas parmi les etats juges" % pt["id"])
    return {"id": pt["id"], "etat_lu": lu0[0]["statut"], "etats": etats,
''',
  '''    lu0 = [j for j in etats if j["rang"] == 0]
    return {"id": pt["id"], "etat_lu": (lu0[0]["statut"] if len(lu0) == 1 else "NON LU"), "etats": etats,
'''),
 ('''            P = {p["id"]: p for p in depot["points"]}
            pts, vus = {}, []
            if inst == "TIENT":
                for f in sorted(glob.glob(os.path.join(dossier, "sonde_ter_point_*.json"))):
                    s = lire_json(f)
                    controler_entete(s, "point")
''',
  '''            f_table, f_dense, canon_dense = sys.argv[4], sys.argv[5], sys.argv[6]
            prevol = "--prevol" in sys.argv[7:]
            canon_table = canon_b(open(f_table, "rb").read())
            if (canon_table == CANON_TABLE) == prevol:
                raise Refus("sans --prevol la table doit etre au canon %s ; avec --prevol elle ne doit pas l'etre" % CANON_TABLE)
            if canon_b(open(f_dense, "rb").read()) != canon_dense:
                raise Refus("la sortie dense n'est pas au canon passe par le pilote (%s)" % canon_dense)
            table = {str(p["id"]): p for p in lire_json(f_table)["points"]}
            JUGES[:] = [i for i, p in table.items() if p["role"] == "juge"]
            dense = lire_json(f_dense)
            if dense.get("moteur_canon") != CANON_MOTEUR or dense.get("sonde_canon") not in ((CANON_SONDE_DENSE, CANON_SONDE_DEPOT) if prevol else (CANON_SONDE_DENSE,)):
                raise Refus("la sortie dense ne porte pas les canons du moteur et de la sonde dense")
            if not prevol and (dense.get("table_canon") != CANON_TABLE or dense.get("prevol") is not False or sorted(p["id"] for p in dense["points"]) != sorted(table)):
                raise Refus("la sortie dense n'a pas ete produite sur la table du gel, ou n'en porte pas tous les points et eux seuls")
            P = {p["id"]: p for p in dense["points"]}
            for i in JUGES:
                if i not in P or Fraction(str(P[i]["w2"])) != Fraction(str(table[i]["w2"])) or Fraction(str(P[i]["facteur"])) != Fraction(str(table[i]["facteur"])) \\
                        or len(P[i]["etats"]) != N_ETATS_DENSE or not P[i].get("faisable"):
                    raise Refus("forme de la sortie dense au point %s (present, w2, facteur, nombre d'etats, faisable)" % i)
            pts, vus = {}, []
            if inst == "TIENT":
                for f in sorted(glob.glob(os.path.join(dossier, "sonde_ter_point_*.json"))):
                    s = lire_json(f)
                    controler_entete(s, "point")
                    if s.get("dense_canon") != canon_dense or s.get("table_canon") != canon_table or s.get("prevol") is not prevol:
                        raise Refus("%s : canon de la sortie dense, canon de la table ou marque de pre-vol differents de ceux de cette lecture" % os.path.basename(f))
'''),
 ('''                       "n_juges": nj, "n_qualifies": nq, "points": pts, "fichiers": vus, "instrument": inst},
''',
  '''                       "n_juges": nj, "n_qualifies": nq, "points": pts, "fichiers": vus, "instrument": inst,
                       "table_canon": canon_table, "dense_canon": canon_dense, "prevol": prevol, "feuille_canon": canon_b(open(__file__, "rb").read())},
'''),
]
P_FEUILLE = deriver(S_FEUILLE, "lecture_lecteur_gel_loi_machine1_v1.py", R_FEUILLE)
json.dump({"table": CANON_TABLE, "table_prevol": CANON_TABLE_PREVOL, "sonde_dense": CANON_DENSE_SONDE, "sonde_lecteur": CANON_LECT_SONDE, "feuille_lecteur": canon(P_FEUILLE),
           "feuille_ter_source": CANON_FEUILLE_TER, "cellules": cel}, open(os.path.join(OUT, "canons_instrument_v1.json"), "w"), indent=1, sort_keys=True)
print("table du gel %s ; table du pre-vol %s" % (CANON_TABLE, CANON_TABLE_PREVOL))
