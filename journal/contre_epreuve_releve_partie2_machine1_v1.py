# -*- coding: ascii -*-
"""CONTRE-EPREUVE DU RELEVE de la seconde partie : une copie du gel alteree en six endroits (un nombre a la fois) est passee
au releve ; chaque controle vise doit mordre. Usage : python3 -I contre_epreuve_releve_partie2_machine1_v1.py <gel.md>
<releve.py> <dossier de travail> <arguments du releve apres le gel ...>"""
import sys, os, subprocess
GEL, RELEVE, TRAVAIL = sys.argv[1:4]; RESTE = sys.argv[4:]
os.makedirs(TRAVAIL, exist_ok=True); T = open(GEL, encoding="ascii").read()
MUT = [("R03", "N = 68   predits 11 / 11 /  0", "N = 68   predits 11 / 10 /  0"), ("R04", "attente 0.0866  marge 1.15", "attente 0.0866  marge 1.25"),
       ("R05", "13 etats   mediane 0.0385   plus grand 0.0604", "13 etats   mediane 0.0385   plus grand 0.0504"), ("R02", "35fa7b73f2b7f8eb", "35fa7b73f2b7f8ec"),
       ("R10", "A-2 E1 : TENU 0.35", "A-2 E1 : TENU 0.45"), ("R06", "T = 0.05 si e_bord < 0.3 et T = 0.10 sinon", "T = 0.05 si e_bord < 0.3 et T = 0.12 sinon")]
vises = []
for cible, a, b in MUT:
    assert T.count(a) >= 1, a
    T = T.replace(a, b); vises.append(cible)
ch = os.path.join(TRAVAIL, "gel_mute.md"); open(ch, "w", encoding="ascii", newline="\n").write(T)
r = subprocess.run([sys.executable, "-I", "-B", RELEVE, ch] + RESTE, capture_output=True, text=True)
mordus = [l.split()[0] for l in r.stdout.split("\n") if " MORD " in l]
print(r.stdout.strip().split("\n")[-1])
print("vises : %s ; mordus : %s ; tous les vises mordent : %s ; code du releve %d" % (sorted(set(vises)), mordus, all(v in mordus for v in vises), r.returncode))
sys.exit(0 if all(v in mordus for v in vises) and r.returncode == 1 else 1)
