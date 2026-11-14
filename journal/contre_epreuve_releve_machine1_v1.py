# -*- coding: ascii -*-
"""CONTRE-EPREUVE du releve de l'acte : le releve doit mordre sur une copie de l'acte dont un chiffre est change.
Arguments : <acte> <releve.py> <recu> <dossier du gel> <clone du registre> <verdict du run precedent (json)>."""
import subprocess, sys, os, shutil, tempfile
ACTE, RELEVE = sys.argv[1:3]; RESTE = sys.argv[3:7]
t = open(ACTE, encoding="ascii").read()
ALT = [("2.529  (8,2) q = 2.529", "2.539  (8,2) q = 2.529"), ("VERDICT : LA GARDE NE TIENT PAS (a = 3, b = 3)", "VERDICT : LA GARDE NE TIENT PAS (a = 2, b = 3)"),
       ("dont 6 hors de la", "dont 5 hors de la"), ("q = 3.1688", "q = 3.1680"), ("vaut 1.4 pour cent", "vaut 1.5 pour cent"),
       ("FAUSSE (2.867)", "FAUSSE (2.877)"), ("1.06 a 2.05 et 1.77 a 2.10", "1.07 a 2.05 et 1.77 a 2.10"), ("d51a9c6ce98b0452", "d51a9c6ce98b0453"),
       ("sonde code 0 en 3028 s", "sonde code 0 en 3020 s"), ("14 h 12 et 14 h 13. Aucun", "14 h 12 et 14 h 15. Aucun"),
       ("H2 facteur 2/3  5.065    HOMOGENE", "H2 facteur 2/3  5.065    HETEROGENE"), ("154 etats juges sur", "155 etats juges sur"),
       ("H5  HORS   1.90  x2/3  FACTEUR 2  ", "H5  HORS   1.90  x2/3  DECADE     "), ("5e-7 pres", "5e-9 pres"),
       ("E4  EN     2.12  x3/2  HORS DECADE  TOMBE    12", "E4  EN     2.12  x3/2  HORS DECADE  TOMBE    13"),
       ("A-11  (0.50)  H4 ou H5, l'un au moins, HORS DECADE             FAUSSE", "A-11  (0.50)  H4 ou H5, l'un au moins, HORS DECADE             VRAIE "),
       ("86a677dc0ff8ba9d\n", "86a677dc0ff8ba9e\n"), ("rang 1, etiquette (11,2)", "rang 2, etiquette (11,2)")]
d = tempfile.mkdtemp()
for f in ("verdict_rejoue_machine1.json", "lecture_rejouee_machine1.log"):
    shutil.copy(os.path.join(os.path.dirname(os.path.abspath(ACTE)), f), d)
mordus = joues = 0
for a, b in ALT:
    if t.count(a) != 1:
        print("  NON JOUEE (motif vu %d fois) : %s" % (t.count(a), a.strip())); continue
    open(d + "/acte.md", "w", encoding="ascii", newline="\n").write(t.replace(a, b))
    r = subprocess.run([sys.executable, "-I", RELEVE, d + "/acte.md"] + RESTE, capture_output=True, text=True)
    m = "RELEVE : 0 controle" not in r.stdout
    joues += 1; mordus += m
    print("  %s  %s  ->  %s" % ("MORD  " if m else "SURVIT", a.strip(), b.strip()))
shutil.rmtree(d)
print("CONTRE-EPREUVE : %d alterations jouees, %d mordues" % (joues, mordus))
