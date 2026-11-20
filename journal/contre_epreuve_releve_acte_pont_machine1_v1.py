# -*- coding: ascii -*-
"""CONTRE-EPREUVE du releve de l'acte du run du gel "pont" -- machine 1, v1, 2026-11-18. Une alteration a la fois sur une
COPIE de l'acte ; le releve doit mordre. Code de sortie 0 si toutes les alterations sont mordues.
Usage : python3 -I -B ce_script <releve.py> <acte.md> <dossier du run de machine 2> <gel partie 2.md>
                                <liste des manifestes.json> <liste des pieces.json>"""
import sys, subprocess, tempfile
RELEVE, ACTE = sys.argv[1], sys.argv[2]; RESTE = sys.argv[3:7]
T0 = open(ACTE, encoding="ascii").read()
ALT = [("une lettre accentuee", "nn.0 POSITION", "nn.0 POSITION " + chr(233)), ("une ligne trop longue", "nn.0 POSITION", "nn.0 POSITION " + "x" * 100),
       ("un signe pour cent", "a 5 pour cent pres", "a 5 % pres"), ("la ligne de verdict", "VERDICT : (S) TENUE", "VERDICT : (S) TOMBEE"),
       ("le pire ln R3 de MG3", "-0.0502 a x = 8", "-0.0492 a x = 8"), ("un ln R3 de la table", "-0.0608  -0.0745", "-0.0608  -0.0755"),
       ("un ln R2 de la table", "+0.0187  +0.0165", "+0.0197  +0.0165"), ("une moyenne de groupe", "0.9339   1.0269", "0.9439   1.0269"),
       ("un verdict de cellule", "PG5      TIENT   +0.0180", "PG5      TOMBE   +0.0180"), ("la question Q1", "S = 0.9945 +- 0.0082", "S = 0.9955 +- 0.0082"),
       ("la question Q3", "1.0107              0.9946", "1.0207              0.9946"), ("une issue dans les annonces", "0.85 TOMBE  0.80 TOMBE  0.50 TOMBE", "0.85 tient  0.80 TOMBE  0.50 TOMBE"),
       ("une annonce", "0.88 tient  0.85 tient  0.75 tient", "0.98 tient  0.85 tient  0.75 tient"), ("le canon du lot du run", "9b980dffc71552d5", "9b980dffc71552d6"),
       ("le canon d'une piece", "65e760f718e040ac  verdict.json", "65e760f718e040ad  verdict.json"), ("la duree du run", "11185 s", "11195 s"),
       ("l'heure de reception du feu vert", "a 00 h 11 a son horloge", "a 00 h 12 a son horloge"), ("une citation du gel", "a 5 pour cent la ou elle tombe", "a 3 pour cent la ou elle tombe"),
       ("le nombre de calculs", "48 calculs", "46 calculs"), ("un compte reduit", "0.486               0.434", "0.496               0.434")]
mordues = 0
for nom, a, b in ALT:
    assert T0.count(a) >= 1, a
    with tempfile.TemporaryDirectory() as tmp:
        open(tmp + "/acte.md", "w", encoding="utf-8", newline="\n").write(T0.replace(a, b, 1))
        r = subprocess.run([sys.executable, "-I", "-B", RELEVE, tmp + "/acte.md"] + RESTE, capture_output=True, text=True)
        qui = [l.split()[0] for l in r.stdout.split("\n") if ": MORD" in l]; ok = r.returncode == 1 and bool(qui); mordues += ok
        print("%-36s : %s %s" % (nom, "MORDUE par" if ok else "NON MORDUE", " ".join(qui)))
print("CONTRE-EPREUVE DE L'ACTE : %d alterations, %d mordues" % (len(ALT), mordues)); sys.exit(0 if mordues == len(ALT) else 1)
