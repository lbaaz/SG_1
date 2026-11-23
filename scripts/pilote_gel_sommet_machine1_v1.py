# -*- coding: ascii -*-
"""PILOTE DU RUN du gel "sommet" -- machine 1, v1, 2026-11-22. UN RUN. Il ne mesure ni ne juge : il enchaine les scripts,
tient le journal (heures, codes de sortie, canons) et s'arrete au premier code de sortie non nul.
Derive de pilote_gel_vide_machine1_v1.py (registre) : meme etage A, memes lots de processus, meme journal.
  etage A   l'instrument du lecteur, par les PIECES DEPOSEES, inchangees : sonde_lecteur_gel_loi_machine1_v1.py en modes
            etage0, ancres, etage1 (sur la table deposee du gel "ordre 3") ; lecture_lecteur_gel_loi_machine1_v1.py, etape
            "instrument" -> verdict_ter_instrument.json
  etage A'  si et seulement si l'instrument TIENT : les neuf TEMOINS POSITIFS DU SOMMET (points sacrifies de Q et de Q2),
            par le pilote de lecture de machine 2 (lecteur_2D_pilote_machine2_v1.py, au canon), le jumeau puis le fantome
  garde     la feuille du gel, etape --temoins -> garde_sommet.json ; si elle ne rend pas TIENT, AUCUNE cellule n'est lue
  etage B   les 56 cellules de la table gelee, par le meme pilote de machine 2 : le jumeau sans fantome puis le fantome,
            quatre absorbeurs, douze barreaux -> lect2D_<id>_jumeau.json et lect2D_<id>_fantome.json
  etage C   la feuille du gel -> verdict_sommet.json
Chaque appel est joue UNE fois ; le dossier du run doit etre neuf. Tous les appels ont un fil BLAS et le drapeau -B.
Usage : python -I pilote_gel_sommet_machine1_v1.py <feuille_gel_sommet_machine1_v1.py> <dossier des scripts deposes>
        <lecteur_2D_pilote_machine2_v1.py> <moteur_v17.py> <sonde_ordre2.json (depot)> <tp_retenus.json> <tp_reference.json>
        <reference des ancres.json> <table deposee du gel ordre 3.json> <table gelee des cellules.json>
        <dossier du run (neuf)> <nombre de processus> [--prevol] [--drapeau <-I ou -P>]
--prevol : etage A, etage A' et garde seulement ; AUCUNE cellule n'est lue ; rien n'est juge.
--drapeau : le drapeau d'isolement passe a python pour chaque appel (-I par defaut ; -P la ou numpy est au site utilisateur)."""
import sys, os, json, time, hashlib, unicodedata, subprocess
a = sys.argv[1:]
PREVOL = "--prevol" in a
DRAPEAU = a[a.index("--drapeau") + 1] if "--drapeau" in a else "-I"
a = [x for i, x in enumerate(a) if x not in ("--prevol", "--drapeau") and not (i > 0 and a[i - 1] == "--drapeau")]
F_SOMMET, DEPOSES, PILOTE_M2, MOTEUR, DEPOT, RETENUS, TP_REF, ANC_REF, TABLE_LOI, TABLE, RUN, NPROC = a[0:12]
NPROC = int(NPROC)
if DRAPEAU not in ("-I", "-P"):
    raise SystemExit("REFUS : --drapeau vaut -I ou -P")
CANONS = {"moteur": "82a0be882568fe0c", "depot": "10887c60d5f55bcf", "retenus": "69b3bab3bb8480b7", "tp_reference": "4d51dd58ef456fe9",
          "reference_ancres": "6600fb8418c79930", "table_ordre3": "35fa7b73f2b7f8eb", "sonde_lecteur": "d5cc48f48e37af99",
          "feuille_lecteur": "83701094e6a2b965", "table": "4238e2b262119f83", "pilote_machine2": "47a84eae6052f006", "feuille_sommet": "ac934e0caaa59c08"}
S_LECT = os.path.join(DEPOSES, "sonde_lecteur_gel_loi_machine1_v1.py")
F_LECT = os.path.join(DEPOSES, "lecture_lecteur_gel_loi_machine1_v1.py")

def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

os.makedirs(RUN, exist_ok=False)
JOURNAL = open(os.path.join(RUN, "pilote_gel_sommet.log"), "w")

def dire(s):
    s = time.strftime("%Y-%m-%d %H:%M:%S ") + s
    print(s, flush=True); JOURNAL.write(s + "\n"); JOURNAL.flush()

def arret(s):
    dire("ARRET DU PILOTE : " + s); sys.exit(2)

dire("PILOTE DU GEL SOMMET%s ; %d processus ; python %s ; drapeau %s" % (" -- PRE-VOL, AUCUNE CELLULE N'EST LUE" if PREVOL else "", NPROC, sys.version.split()[0], DRAPEAU))
dire("pilote %s canon %s" % (os.path.basename(__file__), canon_B(os.path.abspath(__file__))))
for nom, chemin in (("moteur", MOTEUR), ("depot", DEPOT), ("retenus", RETENUS), ("tp_reference", TP_REF), ("reference_ancres", ANC_REF), ("table_ordre3", TABLE_LOI),
                    ("sonde_lecteur", S_LECT), ("feuille_lecteur", F_LECT), ("table", TABLE), ("pilote_machine2", PILOTE_M2), ("feuille_sommet", F_SOMMET)):
    c = canon_B(chemin)
    dire("  canon %-17s %s %s" % (nom, c, "" if c == CANONS[nom] else "DIFFERENT DE " + CANONS[nom]))
    if c != CANONS[nom]:
        arret("canon de %s" % nom)
T = json.load(open(TABLE))
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

def lectures(points):
    """Les appels au pilote de machine 2 : par point, le jumeau (signe 1) puis le fantome (signe -1)."""
    out = []
    for c in points:
        for signe, qui in (("1", "jumeau"), ("-1", "fantome")):
            out.append(("lecture %s %s" % (c["id"], qui), [PILOTE_M2, MOTEUR, S_LECT, RUN, str(c["id"]), str(c["w2"]), str(c["g"]), str(c["m"]), str(c["eta0"]), signe,
                                                          "--rc", str(c["r_c"]), "--abs", "ABCD"], "console_%s_%s.log" % (c["id"], qui)))
    return out

T0 = time.time()
# --- etage A : l'instrument du lecteur, pieces deposees ---
dire("ETAGE A : sonde deposee du lecteur, etage0, ancres, etage1 ; puis feuille deposee, etape instrument")
commun = [S_LECT, MOTEUR, DEPOT, RETENUS, TABLE_LOI, DEPOT, "sans-objet", RUN]      # la sortie dense n'est lue qu'en mode point, qui n'est pas joue
par_lots([("lecteur %s" % m, commun + [m], "console_%s.log" % m) for m in ("etage0", "ancres", "etage1")])
attendre([lancer("feuille du lecteur, instrument", [F_LECT, "instrument", RUN, DEPOT, TP_REF, ANC_REF], "lecture_ter_instrument.console.log")])
inst = json.load(open(os.path.join(RUN, "verdict_ter_instrument.json"))).get("instrument")
dire("INSTRUMENT DU LECTEUR : %s ; canon de son verdict %s" % (inst, canon_B(os.path.join(RUN, "verdict_ter_instrument.json"))))
if inst != "TIENT":
    dire("L'INSTRUMENT NE TIENT PAS : aucun temoin positif, aucune cellule n'est lue ; rien n'est juge ; duree totale %.0f s" % (time.time() - T0)); sys.exit(0)
# --- etage A' : les temoins positifs du sommet ---
dire("ETAGE A' : temoins positifs du sommet, %d points : %s" % (len(T["temoins_positifs"]), " ".join(c["id"] for c in T["temoins_positifs"])))
par_lots(lectures(T["temoins_positifs"]))
# --- garde : la feuille, etape --temoins ---
GARDE = os.path.join(RUN, "garde_sommet.json")
attendre([lancer("feuille du gel, etape de garde", [F_SOMMET, F_LECT, TABLE, RUN, GARDE, "--temoins"], "feuille_gel_sommet_garde.log")])
for l in open(os.path.join(RUN, "feuille_gel_sommet_garde.log")).read().split("\n"):
    if l.strip():
        dire("    " + l)
garde = json.load(open(GARDE)).get("verdict", "")
dire("GARDE : %s ; canon %s" % (garde, canon_B(GARDE)))
if not garde.startswith("TIENT"):
    dire("LA GARDE NE TIENT PAS : aucune cellule n'est lue ; rien n'est juge ; duree totale %.0f s" % (time.time() - T0)); sys.exit(0)
if PREVOL:
    dire("PRE-VOL : la garde tient ; aucune cellule n'est lue ; rien n'est juge ; duree totale %.0f s" % (time.time() - T0)); sys.exit(0)
# --- etage B : les cellules ---
dire("ETAGE B : %d cellules : %s" % (len(T["cellules"]), " ".join(c["id"] for c in T["cellules"])))
par_lots(lectures(T["cellules"]))
for c in T["cellules"]:
    dire("  canons lect2D_%-5s jumeau %s fantome %s" % (c["id"], canon_B(os.path.join(RUN, "lect2D_%s_jumeau.json" % c["id"])), canon_B(os.path.join(RUN, "lect2D_%s_fantome.json" % c["id"]))))
# --- etage C : la feuille ---
dire("ETAGE C : feuille du gel")
VERDICT = os.path.join(RUN, "verdict_sommet.json")
attendre([lancer("feuille du gel", [F_SOMMET, F_LECT, TABLE, RUN, VERDICT], "feuille_gel_sommet.log")])
for l in open(os.path.join(RUN, "feuille_gel_sommet.log")).read().split("\n"):
    if l.strip():
        dire("    " + l)
dire("CANON DU VERDICT : %s" % canon_B(VERDICT))
dire("FIN DU PILOTE ; duree totale %.0f s" % (time.time() - T0))
