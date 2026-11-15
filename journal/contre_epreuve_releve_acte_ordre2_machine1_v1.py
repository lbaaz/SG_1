# -*- coding: ascii -*-
"""CONTRE-EPREUVE DU RELEVE DE L'ACTE DU GEL "LA CHAINE E-A AU SECOND ORDRE" -- machine 1, v1, 2026-11-15.
Le releve doit mordre sur chaque copie de l'acte ou un seul nombre, un seul canon ou un seul mot a ete change.
Arguments : <releve.py> <acte.md> <les six autres arguments du releve>."""
import sys, os, subprocess, tempfile
releve, acte, reste = sys.argv[1], sys.argv[2], sys.argv[3:]
T = open(acte, encoding="ascii").read()
ALT = [
 ("canon du gel dans le titre", "SOUS LE GEL 41153158190cf7f1.", "SOUS LE GEL 41153158190cf7f2."),
 ("tete du registre", "79e77d2, plafond 97", "79e77d3, plafond 97"),
 ("canon du JSON de la sonde", "sonde_ordre2.json  10887c60d5f55bcf", "sonde_ordre2.json  10887c60d5f55bce"),
 ("canon d'un lot en nn.13", "machine 2 -- la certification 59a583a640112891", "machine 2 -- la certification 59a583a640112892"),
 ("canon du verdict en nn.2", "le meme canon 4195583a970eaf70", "le meme canon 4195583a970eaf71"),
 ("regles en attente", "trente-quatre attendent", "trente-cinq attendent"),
 ("compte des etats juges en nn.0", "132 etats juges. Les deux", "133 etats juges. Les deux"),
 ("verdict du titre", "VERDICT : L'ORDRE 2 TIENT. COMPARAISON", "VERDICT : L'ORDRE 2 TIENT JUSQU'A 0.10. COMPARAISON"),
 ("q2 d'une ligne du tableau", "1.044  1.099  1.136", "1.044  1.099  1.137"),
 ("statut d'une ligne du tableau", "1.508  1.579  1.679   2       TENU", "1.508  1.579  1.679   2       TOMBE"),
 ("etats juges d'une ligne", "moyenne    1.6      9     1.356", "moyenne    1.6     10     1.356"),
 ("pire ecart d'une ligne", "0.810   1.052   1.350    0.273    0.300", "0.810   1.052   1.350    0.273    0.301"),
 ("energie d'une ligne", "4.60e-03", "4.61e-03"),
 ("comparaison d'une ligne", "0.273    0.300   MIEUX      ", "0.273    0.300   PAS MIEUX  "),
 ("exclus par motif", "36 exclus (31 sous dix planchers", "36 exclus (30 sous dix planchers"),
 ("plus grand q2 d'une bande", "1.136 pour une borne de", "1.137 pour une borne de"),
 ("etendue de q1", "de q1 = 0.415", "de q1 = 0.416"),
 ("comparaison mince", "L1 (0.203 contre", "L1 (0.204 contre"),
 ("energie d'une bande", "0.0025 a la moyenne", "0.0026 a la moyenne"),
 ("loi apres coup", "0.889\n  (L2)", "0.899\n  (L2)"),
 ("temoin W1", "sept sont\n  au-dela de 1.6", "six sont\n  au-dela de 1.6"),
 ("paliers", "1.25 a huit points juges", "1.25 a neuf points juges"),
 ("garde G-8", "a 8e-11 pres pour Gamma_flux", "a 8e-12 pres pour Gamma_flux"),
 ("statuts de la garde du moteur", "DOMAINE a M4, L1, L2, L4, W1, W2.", "DOMAINE a M4, L1, L4, W1, W2."),
 ("duree du run", "0 h 41, 4524", "0 h 41, 4525"),
 ("batterie", "a 62 a la fin", "a 72 a la fin"),
 ("duree d'un point", "A2 157", "A2 156"),
 ("controles du bloc", "17\n  controles, 0 morsure)", "18\n  controles, 0 morsure)"),
 ("controle d'energie de machine 2", "4.59e-06", "4.69e-06"),
 ("banc de machine 2", "laisse passer 22 des 115", "laisse passer 21 des 115"),
 ("multiple du bruit", "(5.12e-13)", "(5.22e-13)"),
 ("boites sans mesure du bruit", "(C1, M3, L4)", "(C1, M4, L4)"),
 ("probabilite d'une annonce", "A-4  (0.60) la bande LOINTAINE", "A-4  (0.70) la bande LOINTAINE"),
 ("verite d'une annonce", "entre 0.93 et 1.15  FAUSSE (L2 : 0.889)", "entre 0.93 et 1.15  VRAIE  (L2 : 0.889)"),
 ("somme des probabilites", "est 15.2 pour 18 vraies", "est 15.3 pour 18 vraies"),
 ("chiffre de la note", "7.00 pour 6.987", "7.00 pour 6.977"),
 ("marge contre bruit", "vaut 1.7 fois le bruit", "vaut 1.8 fois le bruit"),
 ("heure de l'ouverture", "a 22 h 04, a\n  machine 1", "a 22 h 05, a\n  machine 1"),
 ("W2", "W2 a coute 1346 secondes", "W2 a coute 1347 secondes"),
 ("second canal", "le plus petit q2 y est 1.171", "le plus petit q2 y est 1.172"),
 ("le dementi de D-O2-1", "son plus grand q2, 1.679, est au-dela", "son plus grand q2, 1.669, est au-dela"),
 ("W1 dans les suites", "va jusqu'a 2.047", "va jusqu'a 2.057"),
 ("forme", "Aucune ne mord.", "Aucune ne mord a 100 %."),
]
mord = 0
with tempfile.TemporaryDirectory() as tmp:
    for nom, a, b in ALT:
        assert T.count(a) == 1, (nom, T.count(a))
        p = os.path.join(tmp, "acte.md"); open(p, "w", encoding="ascii", newline="\n").write(T.replace(a, b))
        r = subprocess.run([sys.executable, "-I", releve, p] + reste, capture_output=True, text=True)
        m = (r.returncode != 0); mord += m
        qui = [l.split()[1] for l in r.stdout.split("\n") if l.startswith("  MORD")]
        print("  %-7s %-34s %s" % ("MORD" if m else "survit", nom, " ".join(qui) or r.stderr.strip().split("\n")[-1][:70]))
    r = subprocess.run([sys.executable, "-I", releve, acte] + reste, capture_output=True, text=True)
    print("  l'acte intact : %s" % r.stdout.strip().split("\n")[-1])
print("CONTRE-EPREUVE : %d copies alterees, %d mordues" % (len(ALT), mord))
