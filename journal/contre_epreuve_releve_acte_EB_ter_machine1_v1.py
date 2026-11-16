# -*- coding: ascii -*-
"""CONTRE-EPREUVE DU RELEVE DE L'ACTE E-B TER -- machine 1, v1, 2026-11-15.
Le releve est rejoue sur l'acte intact (il ne doit rien mordre), puis sur des copies de l'acte dont UN chiffre, UN
mot ou UNE empreinte est change : a chaque copie, le controle vise doit mordre. Non opposable.
Une copie alteree peut depasser cent colonnes : R01 mord alors aussi, ce qui ne compte pas.
Usage : python3 -I contre_epreuve_releve_acte_EB_ter_machine1_v1.py <acte.md> <releve.py> <recu> <dossier du gel>
        <manifeste du lot du gel> <note hors chaine> <manifeste du lot de la note> <clone> <lot> <dossier de travail>"""
import sys, os, re, subprocess
ACTE, RELEVE = sys.argv[1:3]; ARGS = sys.argv[3:10]; TRAVAIL = sys.argv[10]
T = open(ACTE, encoding="ascii").read()
ALT = [  # (controle vise, contexte, ancien, nouveau) : le contexte est cherche a la coupure de ligne pres ; il porte l'ancien une fois
    ("R01", "AU MOINS. -- PROJET, VERSION 1", "VERSION 1", "VERSION 2"),
    ("R02", "scripts/m17_chaine_v17.py  82a0be882568fe0c", "82a0be882568fe0c", "82a0be882568fe0d"),
    ("R03", "sonde_qualification_EB_ter_machine1_v1.py  b5616dcf858e8801", "b5616dcf858e8801", "9b0f95f3e10e9b0d"),
    ("R03", "C1 73d4b1ea9cf5cc6d  C2", "73d4b1ea9cf5cc6d", "803f04c6ee0184e2"),
    ("R03", "lot de resultat  1f057651c8f69eb6", "1f057651c8f69eb6", "d2f50caa808cfb1c"),
    ("R04", "independante de la force, de la forme, de la longueur", "de la force, de la forme", "de la forme, de la force"),
    ("R04", "tu peux certifier et jouer si c'est ok ?", "ok", "bon"),
    ("R04", '"go" (15/11/2026, 10 h 28), pour ce gel', "10 h 28", "10 h 29"),
    ("R04", "variations jouees de force, de forme, de longueur et de position, a tau pres", "de forme, de longueur et", "de forme et"),
    ("R05", "14    14   14  QUALIFIE  1.792e-08", "1.792e-08", "1.793e-08"),
    ("R05", "le sont, pour un seuil de 124", "124", "125"),
    ("R05", "2.301e-12    +0.0686", "+0.0686", "+0.0687"),
    ("R05", "137 juges, 31 sous dix planchers", "31", "32"),
    ("R05", "L3  211/100  3/2   +0.11  1.07e-02   35     14    13   12", "14    13", "14    14"),
    ("R05", "(seuil 124) : ESTIMATEUR QUALIFIE. Aucun", "ESTIMATEUR QUALIFIE", "QUALIFIE A L'ETAT LU"),
    ("R06", "L3   0.0234  0.0204  0.0376  0.0416", "0.0416", "0.0417"),
    ("R06", "0.0025 et 0.0376 sous C", "0.0025", "0.0026"),
    ("R06", "0.0409, 0.0442, 0.0657 et 0.0410", "0.0657", "0.0667"),
    ("R06", "M4   0.0091  0.0038  0.0282  0.0099   0.0015  0.0121", "0.0121", "0.0131"),
    ("R07", "mediane 0.0193 et pour plus grande valeur 0.1023", "0.0193", "0.0194"),
    ("R07", "(0.1023), L4 rang 4", "rang 4", "rang 5"),
    ("R07", "au-dessus du plateau a 61 etats", "61", "62"),
    ("R07", "129 etats (nn.7)", "129", "130"),
    ("R07", "a un facteur 1.11 pres partout", "1.11", "1.10"),
    ("R07", "C1 +0.0076, C2 -0.0049", "-0.0049", "+0.0049"),
    ("R07", "plateau de 7 pour cent", "7", "6"),
    ("R08", "est a 0.0008 de A", "0.0008", "0.0018"),
    ("R08", "L3, rang 5, etiquette (7, 2)", "(7, 2)", "(7, 3)"),
    ("R08", "le plus grand ecart de C a A est 0.0174", "0.0174", "0.0184"),
    ("R08", "(k0 = -1, etalement", "-1", "-2"),
    ("R09", "6461 en deux iterations, 110 en trois", "110", "111"),
    ("R09", "poids au site au moins 0.656", "0.656", "0.657"),
    ("R09", "aucune des 7044 lectures du run", "7044", "7045"),
    ("R10", "plus grand ecart absolu 5.80e-13", "5.80e-13", "5.90e-13"),
    ("R10", "bornes de 0.0521 et 0.0502", "0.0521", "0.0512"),
    ("R10", "est de 0.0044 au plus dans le run", "0.0044", "0.0034"),
    ("R10", "1.4e-52 a 1.6e-39", "1.6e-39", "1.6e-38"),
    ("R11", "4377 secondes", "4377", "4378"),
    ("R11", "de 3772 s (M3) a 3981 s", "(M3)", "(M4)"),
    ("R11", "pour 66 minutes d'horloge", "66", "67"),
    ("R11", "ancres (362 s)", "362", "363"),
    ("R12", "    A-6  (0.60) ", "0.60", "0.65"),
    ("R12", "est entre 0.01 et 0.04  VRAIE", "VRAIE", "FAUSSE"),
    ("R12", "somme de probabilites de 5.96", "5.96", "5.86"),
    ("R12", "0.23 a A NEUF ETATS SUR DIX AU MOINS,", "0.23", "0.25"),
    ("R12", "ou trois etats sur quatorze echouaient", "trois", "deux"),
    ("R11", "de l'ordre de 7.1 h de calcul cumule", "7.1", "7.5"),
    ("R13", "(14 etats, 672 lectures)", "672", "673"),
    ("R13", "Sur les 1392 lectures", "1392", "1393"),
    ("R13", "scipy 1.18.1.", "1.18.1", "1.18.2"),
    ("R14", "132 etats juges, 131 sont", "131", "130"),
    ("R15", "dont 12 tiennent", "12", "13"),
    ("R15", "a 1.055 (M1)", "1.055", "1.065"),
    ("R15", "a M3 et M4 il est sous dix", "M4", "M2"),
    ("R15", "ecart relatif au pire 2.0e-10", "2.0e-10", "2.0e-11"),
    ("R15", "2657206 cas", "2657206", "2657207"),
    ("R16", "par 344 flottants sur 1828", "344", "345"),
    ("R17", "origin/main 8d54bf9, plafond 98", "98", "97"),
    ("R17", "trente-quatre attendent la revue", "trente-quatre", "trente-trois"),
    ("R18", "fabrique_lot_machine1_v2.py Perimetre", "v2", "v3"),
]
def alterer(a, ancien, nouveau):
    """Rend l'acte altere, ou None si le contexte n'est pas present une fois et une seule (a la coupure de ligne pres)."""
    motif = r"\s+".join(re.escape(m) for m in a.split())
    if a.startswith(" "): motif = re.escape(a[:len(a) - len(a.lstrip())]) + motif
    if a.endswith(" "): motif = motif + re.escape(" ")
    tr = list(re.finditer(motif, T))
    if len(tr) != 1 or a.count(ancien) != 1: return None
    brut = tr[0].group(0); mo = r"\s+".join(re.escape(m) for m in ancien.split())
    if len(re.findall(mo, brut)) != 1: return None
    return T[:tr[0].start()] + re.sub(mo, lambda _: nouveau, brut) + T[tr[0].end():]
def jouer(chemin):
    r = subprocess.run([sys.executable, "-I", "-B", RELEVE, chemin] + ARGS, capture_output=True, text=True)
    return r.returncode, re.findall(r"^(R\d\d)  MORD", r.stdout, re.M), r.stdout[-300:] + r.stderr[-300:]
os.makedirs(TRAVAIL, exist_ok=True)
code, mord, fin = jouer(ACTE)
print("acte intact : code %d (attendu 0), controles qui mordent %s" % (code, mord))
intact = (code == 0 and not mord)
ok = 0; rates = []
for n, (vise, a, ancien, nouveau) in enumerate(ALT, 1):
    alt = alterer(a, ancien, nouveau)
    if alt is None or alt == T:
        rates.append((n, vise, "contexte absent ou non unique")); print("C%02d  %s  NON JOUEE : contexte absent ou non unique : %r" % (n, vise, a[:50])); continue
    f = os.path.join(TRAVAIL, "C%02d.md" % n); open(f, "w", encoding="ascii", newline="\n").write(alt)
    code, mord, fin = jouer(f)
    bon = (code != 0 and vise in mord)
    ok += bon
    if not bon: rates.append((n, vise, mord))
    print("C%02d  %s  %s  mordent %s  [%s : %s -> %s]" % (n, vise, "MORDUE" if bon else "MANQUEE", mord, " ".join(a.split())[:44], ancien, nouveau))
print("CONTRE-EPREUVE : %d copies alterees, %d mordues au controle vise ; acte intact sans morsure : %s ; manquees : %s" % (len(ALT), ok, intact, rates))
sys.exit(0 if (intact and ok == len(ALT)) else 1)
