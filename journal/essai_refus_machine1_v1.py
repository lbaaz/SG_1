# -*- coding: ascii -*-
"""ESSAIS DE REFUS DE L'INSTRUMENT DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16. AUCUNE MESURE : chaque essai doit
s'arreter AVANT toute lecture, et ne rien ecrire. Le chemin sans --prevol sur la table du gel ne peut pas etre joue avant
le feu vert (il lirait le fantome) : seuls ses refus le sont.
Usage : python3 -I -B essai_refus_machine1_v1.py <dossier de l'instrument> <dossier des scripts deposes> <moteur> <depot>
        <tp_retenus> <tp_reference> <reference des ancres> <table deposee du gel ordre 3> <table du gel> <table de pre-vol> <dossier de travail (neuf)>"""
import sys, os, json, copy, glob, shutil, subprocess
INSTR, DEPOSES, MOTEUR, DEPOT, RETENUS, TP_REF, ANC_REF, TABLE_LOI, TABLE, TABLE_PV, TRAVAIL = sys.argv[1:12]
os.makedirs(TRAVAIL, exist_ok=False)
S_VIDE = os.path.join(INSTR, "sonde_vide_machine1_v1.py"); F_VIDE = os.path.join(INSTR, "feuille_vide_machine1_v1.py"); PILOTE = os.path.join(INSTR, "pilote_gel_vide_machine1_v1.py")
S_LECT = os.path.join(DEPOSES, "sonde_lecteur_gel_loi_machine1_v1.py"); F_LECT = os.path.join(DEPOSES, "lecture_lecteur_gel_loi_machine1_v1.py")
candidate = os.path.join(TRAVAIL, "table_prevol_avec_candidat.json")
T = json.load(open(TABLE_PV)); T2 = copy.deepcopy(T); T2["cellules"][0].update(w2="401/200", delta=0.005, eta0=abs(float(401) / 200 - 2.0)); json.dump(T2, open(candidate, "w"), indent=1, sort_keys=True)
def jouer(args):
    p = subprocess.run([sys.executable, "-I", "-B"] + args, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip().split("\n")[-1]
def sortie(nom):
    d = os.path.join(TRAVAIL, nom); os.makedirs(d); return d
pilote_args = lambda table, run: [PILOTE, INSTR, DEPOSES, MOTEUR, DEPOT, RETENUS, TP_REF, ANC_REF, TABLE_LOI, table, run, "1"]
ESSAIS = [
 ("S1 sonde_vide, table du gel avec --prevol", lambda d: jouer([S_VIDE, MOTEUR, S_LECT, TABLE, d, "MG3", "--prevol"]), "REFUS"),
 ("S2 sonde_vide, table de pre-vol sans --prevol", lambda d: jouer([S_VIDE, MOTEUR, S_LECT, TABLE_PV, d, "PV3"]), "REFUS"),
 ("S3 sonde_vide, cellule inconnue", lambda d: jouer([S_VIDE, MOTEUR, S_LECT, TABLE_PV, d, "MG3", "--prevol"]), "REFUS"),
 ("S4 sonde_vide, pre-vol a un w2 candidat", lambda d: jouer([S_VIDE, MOTEUR, S_LECT, candidate, d, "PV3", "--prevol"]), "REFUS"),
 ("S5 sonde_vide, moteur qui n'est pas au canon", lambda d: jouer([S_VIDE, S_LECT, S_LECT, TABLE, d, "MG3"]), "REFUS"),
 ("S6 feuille_vide, table du gel avec --prevol", lambda d: jouer([F_VIDE, F_LECT, TABLE, d, os.path.join(d, "v.json"), "--prevol"]), "FEUILLE REFUSEE"),
 ("S7 feuille_vide, table de pre-vol sans --prevol", lambda d: jouer([F_VIDE, F_LECT, TABLE_PV, d, os.path.join(d, "v.json")]), "FEUILLE REFUSEE"),
 ("S8 pilote, table du gel avec --prevol", lambda d: jouer(pilote_args(TABLE, os.path.join(d, "run")) + ["--prevol"]), "ARRET DU PILOTE"),
 ("S9 pilote, table de pre-vol sans --prevol", lambda d: jouer(pilote_args(TABLE_PV, os.path.join(d, "run"))), "ARRET DU PILOTE"),
]
tenus = 0
for i, (nom, f, attendu) in enumerate(ESSAIS):
    d = sortie("s%d" % (i + 1)); code, derniere = f(d)
    ecrits = [x for x in glob.glob(os.path.join(d, "**", "*.json"), recursive=True)]
    ok = code != 0 and attendu in derniere and not ecrits
    tenus += ok
    print("  %-4s %s : code %d ; fichiers json ecrits : %d ; %s" % ("TENU" if ok else "RATE", nom, code, len(ecrits), derniere[:150]))
print("ESSAIS DE REFUS : %d tenus sur %d" % (tenus, len(ESSAIS)))
shutil.rmtree(TRAVAIL)
sys.exit(0 if tenus == len(ESSAIS) else 1)
