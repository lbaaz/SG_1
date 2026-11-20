# -*- coding: ascii -*-
"""CONTRE-EPREUVE du releve de la seconde partie du gel "pont" -- machine 1, v1, 2026-11-17.
Une alteration a la fois, sur une COPIE du gel ou d'une piece ; le releve doit mordre. Rien n'est ecrit hors du
dossier temporaire. Code de sortie 0 si toutes les alterations sont mordues.
Usage : python3 -I -B ce_script <releve.py> <gel.md> <dossier du lot a plat> <clone du registre>
                                <dossier extrait du lot de machine 2> <manifeste du lot de machine 2> <table commune.json>"""
import sys, os, re, json, shutil, subprocess, tempfile
RELEVE, GEL, D, CLONE, LOT_M2, MAN_M2, COMMUNE = sys.argv[1:8]
T0 = open(GEL, encoding="ascii").read()
def texte(a, b, n=1, codage="ascii"):
    def f(tmp):
        assert T0.count(a) >= 1, a
        open(tmp + "/gel.md", "w", encoding=codage, newline="\n").write(T0.replace(a, b, n))
    return f
def piece(nom, a, b):
    def f(tmp):
        s = open(tmp + "/lot/" + nom, encoding="utf-8").read(); assert s.count(a) >= 1, (nom, a)
        open(tmp + "/lot/" + nom, "w", encoding="utf-8", newline="\n").write(s.replace(a, b, 1))
    return f
def retire(nom):
    return lambda tmp: os.remove(tmp + "/lot/" + nom)
c15 = re.search(r"^    ([0-9a-f]{16})  verdict_pont_machine1_v1.py$", T0, re.M).group(1)
ALT = [
 ("une lettre accentuee dans le texte", texte("0. STATUT", "0. STATUT " + chr(233), 1, "utf-8")),
 ("une ligne de plus de 100 colonnes", texte("0. STATUT", "0. STATUT " + "x" * 100)),
 ("un signe pour cent", texte("a 5 pour cent pres", "a 5 % pres")),
 ("un canon de la section 15", texte(c15 + "  verdict_pont", ("0" if c15[0] != "0" else "1") + c15[1:] + "  verdict_pont")),
 ("le canon du moteur", texte("82a0be882568fe0c", "82a0be882568fe0d")),
 ("le canon du lot de machine 2", texte("acfecb6da73f20ae  lot de machine 2", "acfecb6da73f20af  lot de machine 2")),
 ("la graine", texte("certification de machine 2 : 456823.", "certification de machine 2 : 456824.")),
 ("un hachage du tirage", texte("bab2ed478849ce6c", "bab2ed478849ce6d")),
 ("le couplage de MG4", texte("g = 2.77765e-03", "g = 2.77766e-03")),
 ("un nombre de la table de la chaine", texte("  -52.49", "  -52.48")),
 ("un pas de la table de la chaine", texte("-0.0869", "-0.0868", 2)),
 ("un ln R3 de la qualification", texte("+0.0225  +0.0631", "+0.0235  +0.0631")),
 ("la tolerance de (L)", texte("|ln R3(x)| <= 0.05", "|ln R3(x)| <= 0.06")),
 ("la tolerance de (S)", texte("[0.85, 1.15]", "[0.80, 1.15]")),
 ("la tolerance de (C)", texte("[0.33, 0.55]", "[0.30, 0.55]")),
 ("les cotes du groupe UN", texte("groupe UN = 180 a 189", "groupe UN = 170 a 189")),
 ("la moyenne du groupe UN", texte("0.9975 +- 0.0349", "0.9985 +- 0.0349")),
 ("la moyenne du groupe UN, seconde mention", texte("et 0.9975 +- 0.0349 sur", "et 0.9985 +- 0.0349 sur")),
 ("un nombre de la reserve R1", texte("4.6e-03 a 5", "4.7e-03 a 5")),
 ("une annonce incoherente", texte("0.95  0.95  0.90   0.40", "0.95  0.95  0.90   0.60")),
 ("la repetition du verdict", texte("rapport 1.397", "rapport 1.497")),
 ("la piece de la chaine", piece("chaine_cellules_pont_v1.json", '"e_bord": 0.0', '"e_bord": 0.1')),
 ("une constante de la feuille de verdict", piece("verdict_pont_machine1_v1.py", "TOL_L, MIN_ECARTS, X_L2 = 0.05, 10, 5.0", "TOL_L, MIN_ECARTS, X_L2 = 0.08, 10, 5.0")),
 ("une constante de la sonde de boite", piece("sonde_boite_fermee_pont_machine1_v1.py", "24, 768, 0.02, 1e-9, 6", "24, 768, 0.05, 1e-9, 6")),
 ("une lecture de densite", piece("lecture_densite_2d_SA5_v1.json", '"ln_R3": 0.02', '"ln_R3": 0.03')),
 ("une boite du groupe UN", piece("lecture_boites_repetition_v1.json", '"S": 1.1', '"S": 1.2')),
 ("le journal du tirage", piece("tirage_pont_graine_456823_machine1_v1.log", "g = 3.63872e-03", "g = 3.63873e-03")),
 ("une piece retiree", retire("bilan_qualification_pont_v1.json")),
]
mordues = 0
for nom, alt in ALT:
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copytree(D, tmp + "/lot"); shutil.copy(GEL, tmp + "/gel.md"); alt(tmp)
        r = subprocess.run([sys.executable, "-I", "-B", RELEVE, tmp + "/gel.md", tmp + "/lot", CLONE, LOT_M2, MAN_M2, COMMUNE], capture_output=True, text=True)
        qui = [l.split()[0] for l in r.stdout.split("\n") if ": MORD" in l]
        ok = r.returncode == 1 and bool(qui); mordues += ok
        print("%-45s : %s %s" % (nom, "MORDUE par" if ok else "NON MORDUE", " ".join(qui)))
print("CONTRE-EPREUVE : %d alterations, %d mordues" % (len(ALT), mordues))
sys.exit(0 if mordues == len(ALT) else 1)
