# -*- coding: ascii -*-
"""PILOTE DU RUN du gel "loi de la largeur, ordre 3" -- machine 1, v1, 2026-11-15. UN RUN, DEUX ETAGES. Il ne mesure ni ne
juge : il enchaine les scripts de l'instrument, tient le journal (heures, codes de sortie, canons) et passe au second
etage le canon de la sortie dense qu'il vient d'ecrire dans son journal.
  etage 1   sonde dense aux points de la table (les douze cellules et les deux ancres)        -> sonde_dense.json
  etage 2a  sonde du lecteur : etage0, ancres, etage1 (points regles du depot) ; feuille du lecteur, etape "instrument"
  etage 2b  si et seulement si l'instrument TIENT : sonde du lecteur en mode point, un appel par point juge (ils sont
            independants), avec le canon de la sortie dense ; feuille du lecteur, etape "verdict" -> verdict_ter.json
  etage 3   feuille d'ordre 3 (chaines a une dimension aux etiquettes lues ; ancres de la sonde dense) -> verdict_ordre3.json
Chaque appel est joue UNE fois ; le dossier du run doit etre neuf. Un code de sortie non nul arrete le pilote.
Usage : python -I pilote_gel_loi_machine1_v1.py <dossier des scripts de l'instrument> <moteur_v17.py> <bloc ordre 2>
        <bloc ordre 3> <sonde_ordre2.json (depot)> <tp_retenus.json> <tp_reference.json> <reference des ancres.json>
        <table des points.json> <dossier du run (neuf)> <nombre de processus> [--prevol [--dense <sortie dense deja jouee>]]
--prevol : la table n'est PAS celle du gel (points deja joues) ; rien n'est juge. Avec --dense, l'etage 1 n'est pas joue :
la sortie dense passee (le depot du delta 98, par exemple) en tient lieu ; cette option n'existe qu'en pre-vol."""
import sys, os, json, time, hashlib, unicodedata, subprocess
a = sys.argv[1:]
PREVOL = "--prevol" in a
DENSE_FOURNIE = a[a.index("--dense") + 1] if "--dense" in a else None
a = [x for i, x in enumerate(a) if x not in ("--prevol", "--dense") and not (i > 0 and a[i - 1] == "--dense")]
SCRIPTS, MOTEUR, BLOC2, BLOC3, DEPOT, RETENUS, TP_REF, ANC_REF, TABLE, RUN, NPROC = a[0:11]
NPROC = int(NPROC)
CANONS = {"moteur": "82a0be882568fe0c", "bloc2": "7cd5977bc27bebc1", "bloc3": "534ba246aa3b8973", "depot": "10887c60d5f55bcf",
          "retenus": "69b3bab3bb8480b7", "tp_reference": "4d51dd58ef456fe9", "reference_ancres": "6600fb8418c79930",
          "table": "35fa7b73f2b7f8eb", "sonde_dense": "68baf04c73ed5d44", "sonde_lecteur": "d5cc48f48e37af99",
          "feuille_lecteur": "83701094e6a2b965", "feuille_ordre3": "582d17c67f460ff6"}
S_DENSE = os.path.join(SCRIPTS, "sonde_dense_gel_loi_machine1_v1.py")
S_LECT = os.path.join(SCRIPTS, "sonde_lecteur_gel_loi_machine1_v1.py")
F_LECT = os.path.join(SCRIPTS, "lecture_lecteur_gel_loi_machine1_v1.py")
F_O3 = os.path.join(SCRIPTS, "feuille_ordre3_machine1_v1.py")

def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

if DENSE_FOURNIE and not PREVOL:
    raise SystemExit("REFUS : --dense n'existe qu'en pre-vol")
os.makedirs(RUN, exist_ok=False)
JOURNAL = open(os.path.join(RUN, "pilote_gel_loi.log"), "w")

def dire(s):
    s = time.strftime("%Y-%m-%d %H:%M:%S ") + s
    print(s, flush=True); JOURNAL.write(s + "\n"); JOURNAL.flush()

def arret(s):
    dire("ARRET DU PILOTE : " + s); sys.exit(2)

dire("PILOTE DU GEL LOI DE LA LARGEUR, ORDRE 3%s ; %d processus ; python %s" % (" -- PRE-VOL, RIEN N'EST JUGE" if PREVOL else "", NPROC, sys.version.split()[0]))
dire("pilote %s canon %s" % (os.path.basename(__file__), canon_B(os.path.abspath(__file__))))
for nom, chemin in (("moteur", MOTEUR), ("bloc2", BLOC2), ("bloc3", BLOC3), ("depot", DEPOT), ("retenus", RETENUS), ("tp_reference", TP_REF),
                    ("reference_ancres", ANC_REF), ("table", TABLE), ("sonde_dense", S_DENSE), ("sonde_lecteur", S_LECT), ("feuille_lecteur", F_LECT),
                    ("feuille_ordre3", F_O3)):
    c = canon_B(chemin)
    dire("  canon %-17s %s %s" % (nom, c, "" if c == CANONS[nom] else ("(table de pre-vol)" if nom == "table" and PREVOL else "DIFFERENT DE " + CANONS[nom])))
    if nom == "table":
        if (c == CANONS[nom]) == PREVOL:
            arret("sans --prevol la table doit etre au canon du gel ; avec --prevol elle ne doit pas l'etre")
    elif c != CANONS[nom]:
        arret("canon de %s" % nom)
JUGES = [str(p["id"]) for p in json.load(open(TABLE))["points"] if p["role"] == "juge"]
PV = ["--prevol"] if PREVOL else []

def lancer(nom, args, console):
    return (nom, time.time(), subprocess.Popen([sys.executable, "-I"] + args, stdout=open(os.path.join(RUN, console), "w"), stderr=subprocess.STDOUT))

def attendre(taches):
    for nom, t0, p in taches:
        code = p.wait()
        dire("  %-28s code=%d duree=%.0f s" % (nom, code, time.time() - t0))
        if code != 0:
            arret("%s a rendu le code %d" % (nom, code))

def par_lots(appels):
    """appels : liste de (nom, args, console) ; au plus NPROC a la fois, dans l'ordre."""
    en_cours, file = [], list(appels)
    while file or en_cours:
        while file and len(en_cours) < NPROC:
            en_cours.append(lancer(*file.pop(0)))
        time.sleep(0.5)
        for t in list(en_cours):
            if t[2].poll() is not None:
                en_cours.remove(t); attendre([t])

T0 = time.time()
# --- etage 1 : la sonde dense ---
DENSE = os.path.join(RUN, "sonde_dense.json")
if DENSE_FOURNIE:
    dire("ETAGE 1 NON JOUE (pre-vol) : la sortie dense passee en tient lieu : %s" % DENSE_FOURNIE)
    DENSE = DENSE_FOURNIE
else:
    dire("ETAGE 1 : sonde dense, %d points juges et les ancres" % len(JUGES))
    attendre([lancer("sonde dense", [S_DENSE, MOTEUR, TABLE, DENSE] + PV, "console_dense.log")])
CANON_DENSE = canon_B(DENSE)
dire("CANON DE LA SORTIE DENSE : %s (passe au second etage)" % CANON_DENSE)
# --- etage 2a : l'instrument du lecteur ---
dire("ETAGE 2a : sonde du lecteur, etage0, ancres, etage1")
commun = [S_LECT, MOTEUR, DEPOT, RETENUS, TABLE, DENSE, CANON_DENSE, RUN]
par_lots([("lecteur %s" % m, commun + [m] + PV, "console_%s.log" % m) for m in ("etage0", "ancres", "etage1")])
attendre([lancer("feuille du lecteur, instrument", [F_LECT, "instrument", RUN, DEPOT, TP_REF, ANC_REF], "lecture_ter_instrument.console.log")])
inst = json.load(open(os.path.join(RUN, "verdict_ter_instrument.json"))).get("instrument")
dire("INSTRUMENT DU LECTEUR : %s" % inst)
if inst != "TIENT":
    dire("L'INSTRUMENT NE TIENT PAS : le mode point n'est pas joue ; rien n'est juge ; duree totale %.0f s" % (time.time() - T0)); sys.exit(0)
# --- etage 2b : les points ---
dire("ETAGE 2b : sonde du lecteur en mode point, %d points : %s" % (len(JUGES), " ".join(JUGES)))
par_lots([("lecteur point %s" % i, commun + ["point", i] + PV, "console_point_%s.log" % i) for i in JUGES])
attendre([lancer("feuille du lecteur, verdict", [F_LECT, "verdict", RUN, DEPOT, TABLE, DENSE, CANON_DENSE] + PV, "lecture_ter.console.log")])
VERDICT = os.path.join(RUN, "verdict_ter.json"); CANON_VERDICT = canon_B(VERDICT)
dire("CANON DU VERDICT DU LECTEUR : %s" % CANON_VERDICT)
# --- etage 3 : la feuille d'ordre 3 ---
dire("ETAGE 3 : feuille d'ordre 3")
attendre([lancer("feuille d'ordre 3", [F_O3, MOTEUR, BLOC2, BLOC3, TABLE, DEPOT, DENSE, CANON_DENSE, VERDICT, CANON_VERDICT, os.path.join(RUN, "verdict_ordre3.json")] + PV,
                 "feuille_ordre3.log")])
for l in open(os.path.join(RUN, "feuille_ordre3.log")).read().split("\n"):
    if l.strip():
        dire("    " + l)
dire("CANON DU VERDICT D'ORDRE 3 : %s" % canon_B(os.path.join(RUN, "verdict_ordre3.json")))
dire("FIN DU PILOTE ; duree totale %.0f s" % (time.time() - T0))
