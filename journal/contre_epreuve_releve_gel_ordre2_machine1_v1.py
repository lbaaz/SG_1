# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1, 2026-11-14. CONTRE-EPREUVE du releve du gel "chaine d'ordre 2" : le releve doit
# mordre sur chaque copie du gel ou un seul nombre, un seul canon ou un seul mot a ete change.
# usage : python3 -I contre_epreuve_releve_gel_ordre2_machine1_v1.py <releve.py> <gel.md> <les cinq autres arguments du releve>
import sys, os, subprocess, tempfile
releve, gel, reste = sys.argv[1], sys.argv[2], sys.argv[3:]
T = open(gel, encoding="ascii").read()
ALT = [
 ("canon du gel precedent en section 1", "pre_enregistrement_v1.md  b59651f99e60707a", "pre_enregistrement_v1.md  b59651f99e60707b"),
 ("canon de la sonde en G-7", "est au canon 24315c52b234319c", "est au canon 24315c52b234319d"),
 ("canon de la feuille", "lecture_ordre2_machine1_v1.py  ", "lecture_ordre2_machine1_v1.py  0"),
 ("tete du registre", "79e77d2 (delta 97)", "79e77d3 (delta 97)"),
 ("D1 de C1", "D1 0.031915", "D1 0.031916"),
 ("c_max de M4", "c_max 0.130464", "c_max 0.130465"),
 ("boite de W2", "HORS DOMAINE  N 89", "HORS DOMAINE  N 88"),
 ("facteur de C3", "C3  w2 = 203/100  facteur 3/2", "C3  w2 = 203/100  facteur 4/3"),
 ("desaccord de W2", "facteur 1/2   delta +0.09", "facteur 1/2   delta +0.08"),
 ("garde de L3", "c_max 0.086367  EN DOMAINE  ", "c_max 0.086367  HORS DOMAINE"),
 ("plus grand q2 de la note", "[0.998 ; 1.512]", "[0.998 ; 1.522]"),
 ("energie mediane de la note", "0.11 pour cent en", "0.12 pour cent en"),
 ("compte d'etats d'une classe", "(88 etats)", "(87 etats)"),
 ("mediane de H6", "0.958 contre", "0.968 contre"),
 ("loi a 2.10", "1.411 au plus", "1.421 au plus"),
 ("taille de la grille", "168 points candidats (journal", "169 points candidats (journal"),
 ("essai du bloc", "1.5e-06 en mediane", "1.6e-06 en mediane"),
 ("cas du selftest", "les 160 cas de la feuille", "les 161 cas de la feuille"),
 ("compte du banc", "la table, 131 alterations", "la table, 132 alterations"),
 ("reference d'ancre", "2.3236497766513317e-10", "2.3236497766513417e-10"),
 ("borne de la bande moyenne", "0.06 < |delta| <= 0.10    B = 1.6", "0.06 < |delta| <= 0.10    B = 1.7"),
 ("plancher", "p = 1.33e-13", "p = 1.34e-13"),
 ("duree", "de l'ordre de 3100 secondes", "de l'ordre de 4100 secondes"),
 ("annonce A-1", "L'ORDRE 2 TIENT 0.45", "L'ORDRE 2 TIENT 0.46"),
 ("champs de l'essai", "les 737", "les 738"),
 ("bruit de fils", "7.32e-14", "7.33e-14"),
 ("forme", "Rien ne se joue avant", "Rien ne se joue avant 100 % de"),
 ("tolerance de G-8", "Gamma_flux a 1e-3 pres", "Gamma_flux a 1e-2 pres"),
]
mord = 0
with tempfile.TemporaryDirectory() as tmp:
    for nom, a, b in ALT:
        assert T.count(a) == 1, (nom, T.count(a))
        p = os.path.join(tmp, "gel.md"); open(p, "w", encoding="ascii", newline="\n").write(T.replace(a, b))
        r = subprocess.run([sys.executable, "-I", releve, p] + reste, capture_output=True, text=True)
        m = (r.returncode != 0); mord += m
        qui = [l.split()[1] for l in r.stdout.split("\n") if l.startswith("  MORD")]
        print("  %-7s %-32s %s" % ("MORD" if m else "survit", nom, " ".join(qui) or r.stderr.strip().split("\n")[-1][:60]))
    r = subprocess.run([sys.executable, "-I", releve, gel] + reste, capture_output=True, text=True)
    print("  le gel intact : %s" % r.stdout.strip().split("\n")[-1])
print("CONTRE-EPREUVE : %d copies alterees, %d mordues" % (len(ALT), mord))
