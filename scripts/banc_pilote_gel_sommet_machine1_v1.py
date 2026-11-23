# -*- coding: ascii -*-
"""BANC DU PILOTE DU GEL "SOMMET" -- machine 1, v1, 2026-11-22. AUCUNE MESURE, AUCUNE 2D : l'enchainement seul.
Le pilote appelle cinq scripts (sonde deposee du lecteur, feuille deposee du lecteur, pilote de lecture de machine 2,
feuille du gel) ; ici ils sont remplaces par des scripts FACTICES qui notent leurs arguments dans appels.txt et ecrivent
des fichiers vides de sens. Le pilote joue est une COPIE du pilote dont SEULES les lignes du dictionnaire CANONS sont
remplacees par les canons des pieces factices (la table gelee reste la vraie, a son canon) ; le banc le verifie.
Ce que le banc eprouve : l'ordre des etages, les arrets (instrument, garde, pre-vol, code de sortie non nul, dossier deja
la, canon), et que les 18 + 112 appels de lecture sont, argument pour argument, les lignes des deux fichiers de travail.
Ce qu'il n'eprouve pas : rien de ce que font les vrais scripts ; le pilote n'a JAMAIS joue une lecture reelle ici.
Usage : python3 -I -B banc_pilote_gel_sommet_machine1_v1.py <pilote du gel> <table gelee> <jobs temoins> <jobs cellules> <dossier de travail (neuf)>"""
import sys, os, re, json, shutil, hashlib, unicodedata, subprocess
PILOTE, TABLE, JOBS_T, JOBS_C, TRAVAIL = sys.argv[1:6]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
os.makedirs(TRAVAIL, exist_ok=False); F = os.path.join(TRAVAIL, "factices"); D = os.path.join(F, "deposes"); os.makedirs(D)
NOTE = 'import sys, os, json\ndef note(run, ligne):\n    open(os.path.join(run, "appels.txt"), "a").write(ligne + "\\n")\n'
FACTICES = {
 os.path.join(D, "sonde_lecteur_gel_loi_machine1_v1.py"): NOTE + 'run, mode = sys.argv[7], sys.argv[8]\nnote(run, "sonde " + mode)\n',
 os.path.join(D, "lecture_lecteur_gel_loi_machine1_v1.py"): NOTE + 'run = sys.argv[2]\nnote(run, "feuille_lecteur " + sys.argv[1])\n'
     'json.dump({"instrument": os.environ.get("BANC_INSTRUMENT", "TIENT"), "factice": True}, open(os.path.join(run, "verdict_ter_instrument.json"), "w"))\n',
 os.path.join(F, "lecteur_2D_pilote_machine2_v1.py"): NOTE + 'a = sys.argv[1:]\nrun, ident, signe = a[2], a[3], a[8]\nassert a[9] == "--rc" and a[11] == "--abs"\n'
     'note(run, "lecture " + " ".join([ident, a[4], a[5], a[6], a[7], signe, a[10], a[12]]))\n'
     'if os.environ.get("BANC_ECHEC") == ident + signe: sys.exit(5)\n'
     'json.dump({"factice": True}, open(os.path.join(run, "lect2D_%s_%s.json" % (ident, "fantome" if signe == "-1" else "jumeau")), "w"))\n',
 os.path.join(F, "feuille_gel_sommet_machine1_v1.py"): NOTE + 'run, sortie = sys.argv[3], sys.argv[4]\ngarde = "--temoins" in sys.argv[5:]\nnote(run, "feuille_sommet " + ("garde" if garde else "verdict"))\n'
     'v = os.environ.get("BANC_GARDE", "TIENT : les cellules peuvent etre lues") if garde else "S1 FACTICE"\nprint("sortie factice :", v)\njson.dump({"verdict": v, "factice": True}, open(sortie, "w"))\n',
}
for chemin, texte in FACTICES.items():
    open(chemin, "w", encoding="ascii", newline="\n").write(texte)
DONNEES = {n: os.path.join(F, n) for n in ("moteur.py", "depot.json", "retenus.json", "tp_reference.json", "reference_ancres.json", "table_ordre3.json")}
for n, chemin in DONNEES.items():
    open(chemin, "w", newline="\n").write("# factice %s\n" % n)
src = open(PILOTE, encoding="ascii").read()
m = re.search(r"CANONS = \{.*?\}\n", src, re.S); assert m and src.count("CANONS = {") == 1
canons = {"moteur": canon_B(DONNEES["moteur.py"]), "depot": canon_B(DONNEES["depot.json"]), "retenus": canon_B(DONNEES["retenus.json"]), "tp_reference": canon_B(DONNEES["tp_reference.json"]),
          "reference_ancres": canon_B(DONNEES["reference_ancres.json"]), "table_ordre3": canon_B(DONNEES["table_ordre3.json"]),
          "sonde_lecteur": canon_B(os.path.join(D, "sonde_lecteur_gel_loi_machine1_v1.py")), "feuille_lecteur": canon_B(os.path.join(D, "lecture_lecteur_gel_loi_machine1_v1.py")),
          "table": canon_B(TABLE), "pilote_machine2": canon_B(os.path.join(F, "lecteur_2D_pilote_machine2_v1.py")), "feuille_sommet": canon_B(os.path.join(F, "feuille_gel_sommet_machine1_v1.py"))}
copie = os.path.join(F, "pilote_copie_canons_factices.py")
open(copie, "w", encoding="ascii", newline="\n").write(src[:m.start()] + "CANONS = " + json.dumps(canons) + "\n" + src[m.end():])
la, lb = src.split("\n"), open(copie).read().split("\n")
n_dict = m.group(0).count("\n")
assert la[:src[:m.start()].count("\n")] == lb[:src[:m.start()].count("\n")] and la[src[:m.start()].count("\n") + n_dict:] == lb[src[:m.start()].count("\n") + 1:]
print("copie du pilote : seules les %d lignes du dictionnaire CANONS different (remplacees par 1 ligne) ; canon du pilote eprouve %s" % (n_dict, canon_B(PILOTE)))
ATT_T = sorted("lecture " + l.strip() for l in open(JOBS_T) if l.strip()); ATT_C = sorted("lecture " + l.strip() for l in open(JOBS_C) if l.strip())
assert len(ATT_T) == 18 and len(ATT_C) == 112

def jouer(nom, pilote=copie, options=(), env=None, run_existe=False):
    run = os.path.join(TRAVAIL, "run_" + nom)
    if run_existe: os.makedirs(run)
    args = [sys.executable, "-I", "-B", pilote, os.path.join(F, "feuille_gel_sommet_machine1_v1.py"), D, os.path.join(F, "lecteur_2D_pilote_machine2_v1.py"), DONNEES["moteur.py"],
            DONNEES["depot.json"], DONNEES["retenus.json"], DONNEES["tp_reference.json"], DONNEES["reference_ancres.json"], DONNEES["table_ordre3.json"], TABLE, run, "4"] + list(options)
    p = subprocess.run(args, capture_output=True, text=True, env=dict(os.environ, **(env or {})))
    appels = [l.strip() for l in open(os.path.join(run, "appels.txt"))] if os.path.exists(os.path.join(run, "appels.txt")) else []
    journal = open(os.path.join(run, "pilote_gel_sommet.log")).read() if os.path.exists(os.path.join(run, "pilote_gel_sommet.log")) else ""
    return p.returncode, appels, journal, run, p.stdout + p.stderr

res = []
def cas(nom, quoi, ok, detail=""):
    res.append(ok); print("%s  %-74s : %s%s" % (nom, quoi, "TIENT" if ok else "NE TIENT PAS", ("  [" + detail + "]") if (detail and not ok) else ""))
lect = lambda ap: [x for x in ap if x.startswith("lecture ")]
# p1 : le run entier
code, ap, jo, run, _ = jouer("p1"); ig = ap.index("feuille_sommet garde") if "feuille_sommet garde" in ap else -1; iv = ap.index("feuille_sommet verdict") if "feuille_sommet verdict" in ap else -1
cas("p1a", "run entier : code 0, FIN DU PILOTE, verdict ecrit", code == 0 and "FIN DU PILOTE" in jo and os.path.exists(os.path.join(run, "verdict_sommet.json")), str(code))
cas("p1b", "etage A : trois modes de la sonde puis la feuille du lecteur, avant toute lecture", sorted(ap[:3]) == ["sonde ancres", "sonde etage0", "sonde etage1"] and ap[3] == "feuille_lecteur instrument")
cas("p1c", "etage A' : les 18 lectures des temoins sont les lignes du fichier de travail, avant la garde", sorted(ap[4:ig]) == ATT_T and ig == 22)
cas("p1d", "etage B : les 112 lectures des cellules sont les lignes du fichier de travail, apres la garde", sorted(ap[ig + 1:iv]) == ATT_C and iv == len(ap) - 1)
cas("p1e", "130 fichiers de lecture, et les canons des 112 fichiers de cellule au journal", len([f for f in os.listdir(run) if f.startswith("lect2D_")]) == 130 and jo.count("canons lect2D_") == 56)
# p2 : l'instrument ne tient pas
code, ap, jo, run, _ = jouer("p2", env={"BANC_INSTRUMENT": "NE TIENT PAS"})
cas("p2", "instrument NE TIENT PAS : code 0, aucune lecture, aucune feuille du gel", code == 0 and not lect(ap) and "feuille_sommet garde" not in ap and "L'INSTRUMENT NE TIENT PAS" in jo)
# p3 : la garde ne tient pas
code, ap, jo, run, _ = jouer("p3", env={"BANC_GARDE": "LES TEMOINS POSITIFS NE TIENNENT PAS : aucune cellule ne doit etre lue"})
cas("p3", "garde NE TIENT PAS : 18 lectures de temoins, aucune cellule, pas de verdict", code == 0 and sorted(lect(ap)) == ATT_T and "feuille_sommet verdict" not in ap and "LA GARDE NE TIENT PAS" in jo)
# p4 : pre-vol
code, ap, jo, run, _ = jouer("p4", options=["--prevol"])
cas("p4", "--prevol : etage A, 18 temoins, garde ; aucune cellule, pas de verdict", code == 0 and sorted(lect(ap)) == ATT_T and ap[-1] == "feuille_sommet garde" and "PRE-VOL : la garde tient" in jo)
# p5 : le dossier du run existe deja
code, ap, jo, run, _ = jouer("p5", run_existe=True)
cas("p5", "dossier du run deja la : refus, rien n'est ecrit", code != 0 and not ap and os.listdir(run) == [])
# p6 : une lecture rend un code non nul
code, ap, jo, run, _ = jouer("p6", env={"BANC_ECHEC": "MPa3-1"})
cas("p6", "une lecture de cellule rend un code non nul : ARRET, pas de verdict", code == 2 and "ARRET DU PILOTE : lecture MPa3 fantome a rendu le code 5" in jo and "feuille_sommet verdict" not in ap)
# p7 : le vrai pilote devant des pieces qui ne sont pas au canon
code, ap, jo, run, _ = jouer("p7", pilote=PILOTE)
cas("p7", "le pilote non modifie devant des pieces factices : ARRET sur le premier canon, aucun appel", code == 2 and "ARRET DU PILOTE : canon de moteur" in jo and not ap)
# p8 : --drapeau
code, ap, jo, run, sortie = jouer("p8", options=["--drapeau", "-X"])
cas("p8", "--drapeau autre que -I ou -P : refus avant tout", code != 0 and "REFUS : --drapeau" in sortie and not os.path.exists(run))
print("BANC DU PILOTE : %d cas, %d tenus" % (len(res), sum(res)))
shutil.rmtree(TRAVAIL)
sys.exit(0 if all(res) else 1)
