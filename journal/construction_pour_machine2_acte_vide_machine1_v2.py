# -*- coding: ascii -*-
"""CONSTRUCTION DE LA NOTE D'ACCOMPAGNEMENT DE LA VERSION 2 DE L'ACTE DU GEL "LARGEUR DU VIDE" -- machine 1, v2, 2026-11-16.
Chaque nombre est lu dans les pieces.
Usage : python3 -I -B construction_pour_machine2_acte_vide_machine1_v2.py <dossier de ce lot> <lot de l'acte v1> <sortie.md>"""
import sys, os, re, json, difflib, hashlib, unicodedata, textwrap
D, V1, SORTIE = sys.argv[1:4]
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
A2 = os.path.join(D, "journal_delta_nn_largeur_vide_v2.md"); A1 = os.path.join(V1, "journal_delta_nn_largeur_vide_v1.md")
a1 = open(A1, encoding="ascii").read().splitlines(); a2 = open(A2, encoding="ascii").read().splitlines()
auth = open(os.path.join(D, "authentifie_lot_m2_contreseing_acte_machine1_v1.log"), encoding="ascii").read(); assert "AUTHENTIFICATION : TIENT" in auth
canon_j, n_j = re.search(r"canon du lot ([0-9a-f]{16})", auth).group(1), int(re.search(r"au bon canon : (\d+)", auth).group(1))
LR = json.load(open(os.path.join(V1, "lecture_resultat_vide_v1.json"))); RR = json.load(open(os.path.join(V1, "reception_resultat_vide_v1.json")))
V = json.load(open(os.path.join(V1, "verdict_vide_rejoue_machine1.json"))); MG = LR["signes"]["MG_lisibles"]
feuilles, listes = [0], []
def va(o):
    if isinstance(o, dict):
        for k in o: va(o[k])
    elif isinstance(o, list):
        if o and all(isinstance(x, dict) and "id" in x for x in o):
            for x in o: va(x)
        else:
            listes.append(len(o))
    else:
        feuilles[0] += 1
va(V); assert feuilles[0] + len(listes) == RR["comparaison"]["champs"] and not any(listes)
# ce qui change, compte par le diff des deux textes
sm = difflib.SequenceMatcher(None, a1, a2, autojunk=False); blocs = [op for op in sm.get_opcodes() if op[0] != "equal"]
def section(i):
    s = [l for l in a2[:i + 1] if re.match(r"^nn\.\d+ ", l)]
    return s[-1].split()[0] if s else "en-tete"
ou = []
for tag, i1, i2, j1, j2 in blocs:
    ou.append("%s (lignes %d a %d de la v2%s)" % (section(max(j1, j2 - 1)), j1 + 1, max(j2, j1 + 1), "" if j2 > j1 else ", retrait"))
tab = lambda L: [l for l in L if re.match(r"^    (MG|MP|PP|PG)\d+ ", l)]; assert tab(a1) == tab(a2) and len(tab(a2)) == 84
rho = [-x["ln_q"] / x["r3"] for x in MG]; f = [x["part"] for x in MG]; assert all(abs(fi - r / (1 + r)) < 1e-12 for fi, r in zip(f, rho))
L = []
def T_(s=""): L.append(s)
def P(s, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
T_('ACTE DU GEL "LARGEUR DU VIDE" -- VERSION 2 -- machine 1 pour machine 2, 2026-11-16')
T_()
T_("0. CE QUE CE LOT EST")
P("""Ton lot de contreseing (%s) est authentifie, %d pieces sur %d. Tu contresignes le contenu de la version 1 sans condition ; je
retiens tes cinq precisions. La version 2 est journal_delta_nn_largeur_vide_v2.md (%s). Ses %d lignes de tableau et sa ligne de verdict
sont celles de la version 1 : le script de construction le controle. Rien n'est depose.""" % (canon_j, n_j, n_j, B(A2), len(tab(a2))))
T_()
T_("1. CE QUI CHANGE (ton releve mordra la ou une phrase a change de forme)")
P("""Le diff des deux textes compte %d blocs changes, dans cet ordre :""" % len(blocs))
for x in ou:
    T_("    " + x)
P("""Soit : l'en-tete ; P-2 en nn.2 ("aux durees pres") ; P-3 puis P-1 en nn.4 ; P-4 en nn.6 (une phrase ajoutee apres la superposition)
; P-5 en nn.7 (ta phrase, plus une phrase de moi sur V1 : dis si elle va) ; le paragraphe des retouches en nn.9 ; P-1 en nn.10 ; la
premiere phrase de nn.11 ; trois lignes de nn.12 ; la ligne de fin.""")
T_()
T_("2. TES ECARTS APPARENTS")
P("""Les 1576 champs. Ma comparaison compte pour un champ chaque feuille de l'arbre du verdict, ET chaque liste qui n'est pas une
liste d'objets a identifiant : %d feuilles (les tiennes) et %d listes, toutes vides (les echecs et les non lisibles de chaque cellule,
les cellules tombees des deux enonces, la liste des fichiers incomplets). %d + %d = %d. La version 2 le dit.""" % (
    feuilles[0], len(listes), feuilles[0], len(listes), RR["comparaison"]["champs"]), 2, 4)
P("""Les parts de mon point (c). Ce n'est pas une troncature : ce sont deux grandeurs. Tu calcules rho = |ln q / r3| : %.4f, %.4f, %.4f,
%.4f. J'ecrivais la part manquee f de la lecture (b), f = rho / (1 + rho) : %.4f, %.4f, %.4f, %.4f, arrondies a trois decimales. Ma
phrase melait les deux ("ln q vaut une part de r3" et "part manquee") : faute de redaction de ma note d'accompagnement, sans effet sur
l'acte, qui ne porte pas cette lecture. Et tu as raison : elle ne tient pas a PP non plus.""" % tuple(rho + f), 2, 4)
P("""La superposition a 12 barreaux : rien a ajouter, la colonne est bien l'etendue des r3 de la chaine.""", 2, 4)
T_()
T_("3. CE QUE JE N'AI PAS FAIT")
P("""Je n'ai rejoue ni ton releve ni sa contre-epreuve : j'en ai lu les journaux, et l'acte cite leurs comptes. Aucune 2D. Le depot
est a l'operateur ; l'acte dit de quelles pieces hors registre il depend.""")
T_()
T_("4. PIECES DE CE LOT (convention B)")
for fch in sorted(os.listdir(D)):
    if fch.startswith("MANIFESTE") or fch == os.path.basename(SORTIE) or fch == os.path.basename(__file__):
        continue
    T_("    %s  %s" % (B(os.path.join(D, fch)), fch))
T_("    (ce script)       %s" % os.path.basename(__file__))
T_()
texte = "\n".join(L) + "\n"; texte.encode("ascii"); assert "%" not in texte and max(len(l) for l in L) <= 100, [l for l in L if len(l) > 100 or "%" in l]
open(SORTIE, "w", encoding="ascii", newline="\n").write(texte)
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(SORTIE), len(L), B(SORTIE)))
