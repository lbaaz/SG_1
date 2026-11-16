# -*- coding: ascii -*-
"""PILOTE DU RUN du gel "largeur du vide" -- machine 1, v1, 2026-11-16. UN RUN. Il ne mesure ni ne juge : il enchaine les
scripts, tient le journal (heures, codes de sortie, canons) et s'arrete au premier code de sortie non nul.
  etage A  l'instrument du lecteur, par les PIECES DEPOSEES, inchangees : sonde_lecteur_gel_loi_machine1_v1.py en modes
           etage0, ancres, etage1 (sur la table deposee du gel "ordre 3") ; lecture_lecteur_gel_loi_machine1_v1.py, etape
           "instrument" -> verdict_ter_instrument.json
  etage B  si et seulement si l'instrument TIENT : sonde_vide, un appel par cellule de la table (ils sont independants) :
           le jumeau sans fantome puis le fantome, quatre absorbeurs, douze barreaux -> sonde_vide_<id>.json
  etage C  feuille_vide -> verdict_vide.json
Chaque appel est joue UNE fois ; le dossier du run doit etre neuf. Tous les appels ont un fil BLAS et le drapeau -B
(python n'ecrit aucun fichier de cache a cote des scripts).
Usage : python -I pilote_gel_vide_machine1_v1.py <dossier de sonde_vide et feuille_vide> <dossier des scripts deposes>
        <moteur_v17.py> <sonde_ordre2.json (depot)> <tp_retenus.json> <tp_reference.json> <reference des ancres.json>
        <table deposee du gel ordre 3.json> <table des cellules.json> <dossier du run (neuf)> <nombre de processus>
        [--prevol] [--drapeau <-I ou -P>]
--prevol : la table des cellules n'est PAS celle du gel ; le fantome n'est pas lu ; rien n'est juge.
--drapeau : le drapeau d'isolement passe a python pour chaque appel (-I par defaut ; -P la ou numpy est au site utilisateur)."""
import sys, os, json, time, hashlib, unicodedata, subprocess
a = sys.argv[1:]
PREVOL = "--prevol" in a
DRAPEAU = a[a.index("--drapeau") + 1] if "--drapeau" in a else "-I"
a = [x for i, x in enumerate(a) if x not in ("--prevol", "--drapeau") and not (i > 0 and a[i - 1] == "--drapeau")]
INSTRUMENT, DEPOSES, MOTEUR, DEPOT, RETENUS, TP_REF, ANC_REF, TABLE_LOI, TABLE, RUN, NPROC = a[0:11]
NPROC = int(NPROC)
if DRAPEAU not in ("-I", "-P"):
    raise SystemExit("REFUS : --drapeau vaut -I ou -P")
CANONS = {"moteur": "82a0be882568fe0c", "depot": "10887c60d5f55bcf", "retenus": "69b3bab3bb8480b7", "tp_reference": "4d51dd58ef456fe9",
          "reference_ancres": "6600fb8418c79930", "table_ordre3": "35fa7b73f2b7f8eb", "sonde_lecteur": "d5cc48f48e37af99",
          "feuille_lecteur": "83701094e6a2b965", "table": "b71206e5daf6c741", "sonde_vide": "0f82986cca133330", "feuille_vide": "ac39a24def6c7420"}
S_LECT = os.path.join(DEPOSES, "sonde_lecteur_gel_loi_machine1_v1.py")
F_LECT = os.path.join(DEPOSES, "lecture_lecteur_gel_loi_machine1_v1.py")
S_VIDE = os.path.join(INSTRUMENT, "sonde_vide_machine1_v1.py")
F_VIDE = os.path.join(INSTRUMENT, "feuille_vide_machine1_v1.py")

def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

os.makedirs(RUN, exist_ok=False)
JOURNAL = open(os.path.join(RUN, "pilote_gel_vide.log"), "w")

def dire(s):
    s = time.strftime("%Y-%m-%d %H:%M:%S ") + s
    print(s, flush=True); JOURNAL.write(s + "\n"); JOURNAL.flush()

def arret(s):
    dire("ARRET DU PILOTE : " + s); sys.exit(2)

dire("PILOTE DU GEL LARGEUR DU VIDE%s ; %d processus ; python %s ; drapeau %s" % (" -- PRE-VOL, RIEN N'EST JUGE" if PREVOL else "", NPROC, sys.version.split()[0], DRAPEAU))
dire("pilote %s canon %s" % (os.path.basename(__file__), canon_B(os.path.abspath(__file__))))
for nom, chemin in (("moteur", MOTEUR), ("depot", DEPOT), ("retenus", RETENUS), ("tp_reference", TP_REF), ("reference_ancres", ANC_REF), ("table_ordre3", TABLE_LOI),
                    ("sonde_lecteur", S_LECT), ("feuille_lecteur", F_LECT), ("table", TABLE), ("sonde_vide", S_VIDE), ("feuille_vide", F_VIDE)):
    c = canon_B(chemin)
    dire("  canon %-17s %s %s" % (nom, c, "" if c == CANONS[nom] else ("(table de pre-vol)" if nom == "table" and PREVOL else "DIFFERENT DE " + CANONS[nom])))
    if nom == "table":
        if (c == CANONS[nom]) == PREVOL:
            arret("sans --prevol la table doit etre au canon du gel ; avec --prevol elle ne doit pas l'etre")
    elif c != CANONS[nom]:
        arret("canon de %s" % nom)
CELLULES = [str(c["id"]) for c in json.load(open(TABLE))["cellules"]]
PV = ["--prevol"] if PREVOL else []
ENV_UN_FIL = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")

def lancer(nom, args, console):
    return (nom, time.time(), subprocess.Popen([sys.executable, DRAPEAU, "-B"] + args, stdout=open(os.path.join(RUN, console), "w"), stderr=subprocess.STDOUT, env=ENV_UN_FIL))

def attendre(taches):
    for nom, t0, p in taches:
        code = p.wait()
        dire("  %-34s code=%d duree=%.0f s" % (nom, code, time.time() - t0))
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
# --- etage A : l'instrument du lecteur, pieces deposees ---
dire("ETAGE A : sonde deposee du lecteur, etage0, ancres, etage1 ; puis feuille deposee, etape instrument")
commun = [S_LECT, MOTEUR, DEPOT, RETENUS, TABLE_LOI, DEPOT, "sans-objet", RUN]      # la sortie dense n'est lue qu'en mode point, qui n'est pas joue
par_lots([("lecteur %s" % m, commun + [m], "console_%s.log" % m) for m in ("etage0", "ancres", "etage1")])
attendre([lancer("feuille du lecteur, instrument", [F_LECT, "instrument", RUN, DEPOT, TP_REF, ANC_REF], "lecture_ter_instrument.console.log")])
inst = json.load(open(os.path.join(RUN, "verdict_ter_instrument.json"))).get("instrument")
dire("INSTRUMENT DU LECTEUR : %s ; canon de son verdict %s" % (inst, canon_B(os.path.join(RUN, "verdict_ter_instrument.json"))))
if inst != "TIENT":
    dire("L'INSTRUMENT NE TIENT PAS : aucune cellule n'est lue ; rien n'est juge ; duree totale %.0f s" % (time.time() - T0)); sys.exit(0)
# --- etage B : les cellules ---
dire("ETAGE B : sonde_vide, %d cellules : %s" % (len(CELLULES), " ".join(CELLULES)))
par_lots([("sonde_vide %s" % i, [S_VIDE, MOTEUR, S_LECT, TABLE, RUN, i] + PV, "console_vide_%s.log" % i) for i in CELLULES])
for i in CELLULES:
    dire("  canon sonde_vide_%-5s %s" % (i, canon_B(os.path.join(RUN, "sonde_vide_%s.json" % i))))
# --- etage C : la feuille ---
dire("ETAGE C : feuille_vide")
VERDICT = os.path.join(RUN, "verdict_vide.json")
attendre([lancer("feuille_vide", [F_VIDE, F_LECT, TABLE, RUN, VERDICT] + PV, "feuille_vide.log")])
for l in open(os.path.join(RUN, "feuille_vide.log")).read().split("\n"):
    if l.strip():
        dire("    " + l)
dire("CANON DU VERDICT : %s" % canon_B(VERDICT))
dire("FIN DU PILOTE ; duree totale %.0f s" % (time.time() - T0))
