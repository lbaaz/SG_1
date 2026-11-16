# -*- coding: ascii -*-
"""CONTRE-EPREUVE DU RELEVE DE L'ACTE, VERSION 2 (derivee de celle de la v1 : quatre alterations de plus, sur les retouches).
Des copies de l'acte, UN nombre altere dans chacune ; le controle vise doit mordre.
Usage : python3 -I contre_epreuve_releve_acte_gel_loi_machine1_v1.py <acte.md> <releve.py> <dossier de travail> <arguments
du releve apres l'acte ...>"""
import sys, os, subprocess
ACTE, RELEVE, TRAVAIL = sys.argv[1:4]; RESTE = sys.argv[4:]
os.makedirs(TRAVAIL, exist_ok=True); T = open(ACTE, encoding="ascii").read()
MUT = [("R03", "    BP  13 / 13 /  5 /  8   TIENT", "    BP  13 / 13 /  6 /  7   TIENT"), ("R03", "|ln q3| 0.0740   marge +0.0260", "|ln q3| 0.0740   marge +0.0360"),
       ("R05", "vaut 0.099617 pour T = 0.10", "vaut 0.098617 pour T = 0.10"), ("R06", "[0.3, 0.5[ : 59, 0.0160, 0.0770", "[0.3, 0.5[ : 59, 0.0160, 0.0670"),
       ("R07", "totale 6166 s ; 19 appels", "totale 6166 s ; 18 appels"), ("R02", "87e9221cfc5f8f9b", "87e9221cfc5f8f9c"), ("R04", "1.6e-09 sur ln q3", "1.6e-07 sur ln q3"),
       ("R05", "negatif a 58 etats sur 60", "negatif a 60 etats sur 60"), ("R05", "marge en logarithme est 0.174", "marge en logarithme est 0.173"),
       ("R05", "soit 6.2 fois la marge", "soit 5.2 fois la marge"), ("R05", "+0.000383, +0.0024, +0.0025", "+0.000383, +0.0024, +0.0035"), ("R05", "le 16/11 a 00 h 54", "le 16/11 a 00 h 45")]
ok = True
for n, (cible, a, b) in enumerate(MUT):
    assert T.count(a) >= 1, a
    ch = os.path.join(TRAVAIL, "acte_mute_%d.md" % n); open(ch, "w", encoding="ascii", newline="\n").write(T.replace(a, b))
    r = subprocess.run([sys.executable, "-I", "-B", RELEVE, ch] + RESTE, capture_output=True, text=True); mordus = [l.split()[0] for l in r.stdout.split("\n") if " MORD " in l]
    bon = cible in mordus and r.returncode == 1; ok = ok and bon
    print("mutation %d (%s) : %-34s -> mordus %s : %s" % (n + 1, cible, a[:34], mordus, "comme attendu" if bon else "MUET"))
print("CONTRE-EPREUVE : %d mutations, %s" % (len(MUT), "toutes mordues sur le controle vise" if ok else "AU MOINS UNE MUETTE")); sys.exit(0 if ok else 1)
