# -*- coding: ascii -*-
"""CONTRE-EPREUVE DU RELEVE DE LA PREMIERE PARTIE DU GEL "PONT" -- machine 1, v1, 2026-11-17.
Le releve mord-il quand le texte ment ? Une alteration a la fois, sur une copie ; le texte du gel n'est pas touche.
Usage : python3 -I contre_epreuve_releve_gel_pont_partie1_machine1_v1.py <releve.py> <texte du gel> <dossier temporaire neuf>
        <dossier des sorties> <clone> <exploration du lisse> <lecture des grandes boites> <lot de machine 2>"""
import sys, os, subprocess
RELEVE, TEXTE, TMP = sys.argv[1:4]; RESTE = sys.argv[4:]
txt = open(TEXTE, encoding="ascii").read()
ALT = [("une etendue citee", "du lisse de 0.0106 au plus", "du lisse de 0.0107 au plus", "R08"),
       ("le pas cite", "un pas de 0.0450 au plus", "un pas de 0.0460 au plus", "R08"),
       ("un compte d'eligibles", "creneau MG : 5 w2 eligibles sur 8", "creneau MG : 6 w2 eligibles sur 8", "R05"),
       ("une cellule de la table", "m3 0.0014 0.0046 0.0690", "m3 0.0014 0.0046 0.0691", "R05"),
       ("un point d'exclamation retire", "m5 0.0027 0.0109 0.1021!", "m5 0.0027 0.0109 0.1021", "R05"),
       ("une eligibilite inversee", "0.0869  ELIGIBLE", "0.0869  INELIGIBLE", "R05"),
       ("le nombre de cellules ecartees", "La condition (v) en ecarte 6", "La condition (v) en ecarte 5", "R06"),
       ("la probabilite de PAS DE GEL", "vaut 0.0074", "vaut 0.0075", "R06"),
       ("un seuil", "est <= 0.03 ; (v)", "est <= 0.04 ; (v)", "R06"),
       ("un canon du registre", "82a0be882568fe0c", "82a0be882568fe0d", "R02"),
       ("un canon de piece", "733369d4b82e0b1b", "733369d4b82e0b1c", "R04"),
       ("un numero de demonstration", "modulo  8 =  5 -> w2 = 1.987", "modulo  8 =  4 -> w2 = 1.986", "R07"),
       ("un candidat ajoute", "w2 = 1.981, 1.983,", "w2 = 1.981, 1.982, 1.983,", "R07"),
       ("le compte des niveaux", "Sur 568 niveaux, 1 n'est pas fiable", "Sur 568 niveaux, 0 n'est pas fiable", "R08"),
       ("la somme citee", "vaut 1.043 +- 0.018", "vaut 1.034 +- 0.018", "R08"),
       ("le balayage", "15 fichiers portent un w2 candidat", "14 fichiers portent un w2 candidat", "R08"),
       ("une ligne du tableau par profondeur", "MG       5   0.094", "MG       5   0.095", "R09"),
       ("une citation de machine 2", "36 a 67 s aux cotes", "36 a 68 s aux cotes", "R10"),
       ("un signe pour cent de trop", "des deux gels deposes.", "des deux gels deposes, a 100 %.", "R01"),
       ("une ligne trop longue", "3. LE TIRAGE", "3. LE TIRAGE" + " " * 95 + ".", "R01"),
       ("une empreinte inconnue", "PONT\" -- PREMIERE PARTIE", "PONT\" 0123456789abcdef -- PREMIERE PARTIE", "R03")]
def jouer(chemin):
    r = subprocess.run([sys.executable, "-I", "-B", RELEVE, chemin] + RESTE, capture_output=True, text=True)
    der = [l for l in r.stdout.splitlines() if l.startswith("RELEVE :")]
    return r.returncode, (der[-1] if der else "pas de ligne RELEVE")
os.makedirs(TMP)
code, ligne = jouer(TEXTE); ok0 = code == 0
print("texte intact : code %d ; %s -> %s" % (code, ligne, "TIENT" if ok0 else "NE TIENT PAS"))
bons = 0
for nom, a, b, attendu in ALT:
    assert txt.count(a) == 1, (nom, txt.count(a))
    p = os.path.join(TMP, "copie.md"); open(p, "w", encoding="ascii", newline="\n").write(txt.replace(a, b))
    code, ligne = jouer(p); ok = code == 1 and ("'%s'" % attendu) in ligne; bons += ok
    print("%-36s : code %d ; attendu %s ; %s -> %s" % (nom, code, attendu, ligne.split("mordent : ")[-1], "MORD" if ok else "NE MORD PAS COMME ATTENDU"))
os.remove(os.path.join(TMP, "copie.md")); os.rmdir(TMP)
print("CONTRE-EPREUVE : %d alterations, %d mordent au controle attendu ; texte intact : %s" % (len(ALT), bons, "aucune morsure" if ok0 else "MORD"))
sys.exit(0 if (ok0 and bons == len(ALT)) else 1)
