#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VERIFICATION DE L'ACTE R4/R5 **v4** ET DE LA PIECE DE DEPOT -- machine 2, v1, 12/09/2026.

FEUILLE NEUVE (celle de la v3 est manifestee au canon bdd00189e68b61dc ; l'editer
perimerait son ancre).

PORTEE, DITE D'ABORD :
  - la v4 ne differe de la v3 que par SIX hunks (feuille controle_hunks_v3_v4, rejouee
    de ma main, comptee PAR POSITION). Hors hunks, elle est mot pour mot la v3 certifiee
    66/71 -- qui etait elle-meme, hors ses dix hunks, la v2 certifiee 89/89. La chaine
    de certification tient donc par transitivite, et c'est ce qui est verifie ici.
  - les DEUX hunks de fond portent MES DEUX ERRATA : je les relis contre MES .json.
  - la PIECE DE DEPOT est un RENOMMAGE (nn -> 89) : deux caracteres pour deux, taille
    identique. Une taille identique ne prouve rien. Je reconstruis la substitution et
    compare AU BIT.
"""
import hashlib, json, os, re, unicodedata

RAC = r"D:\devs\bocal\BOCAL4"
V4D = os.path.join(RAC, "entrant_machine1_2026-09-12_acte_v4")
LOT = os.path.join(V4D, "lot")
DEP = os.path.join(V4D, "depot")
ACTE = os.path.join(LOT, "journal_delta_nn_R4R5_v4.md")
V3 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_v3", "lot",
                  "journal_delta_nn_R4R5_v3.md")
T = open(ACTE, encoding="utf-8").read()
TPLAT = re.sub(r"\s+", " ", T)
J = lambda p: json.load(open(os.path.join(RAC, p), encoding="utf-8"))
OK, MORD = [], []


def chk(sec, quoi, cond, detail=''):
    OK.append((sec, quoi, bool(cond)))
    if not cond:
        MORD.append((sec, quoi, detail))
    print('  [%s] %-6s %-49s %s' % ('OK  ' if cond else 'MORD', sec, quoi[:49], detail))


def cite(s):
    return re.sub(r"\s+", " ", s) in TPLAT


def emp(chemin):
    raw = open(chemin, 'rb').read()
    txt = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n')
    return hashlib.sha256(txt.encode('utf-8')).hexdigest()[:16], len(raw)


print("=" * 88)
print("ACTE R4/R5 v4 ET PIECE DE DEPOT -- verification machine 2")
print("=" * 88)

# =========================================================== 1. RECEPTION
print("\n[REC] LE LOT DE L'ACTE v4")
MAN = os.path.join(LOT, "MANIFEST_lot_machine1_R4R5_acte_v4.txt")
chk("REC", "le manifeste de l'acte v4 existe", os.path.exists(MAN))
MT = open(MAN, encoding="utf-8").read()
canon = emp(MAN)[0]
print("      CANON du lot acte : %s" % canon)
lignes = []
for l in MT.splitlines():
    c = l.split()
    if len(c) == 3 and len(c[0]) == 16 and c[1].isdigit():
        try:
            int(c[0], 16)
        except ValueError:
            continue
        lignes.append((c[0], int(c[1]), c[2]))
chk("REC", "22 pieces annoncees et extraites", len(lignes) == 22, "%d" % len(lignes))
sur_disque = sorted(f for f in os.listdir(LOT) if f != os.path.basename(MAN))
chk("REC", "aucun fichier hors manifeste",
    set(sur_disque) == {n for _, _, n in lignes},
    str(set(sur_disque) ^ {n for _, _, n in lignes}) or '')
chk("REC", "le manifeste ne porte pas sa propre empreinte", canon not in MT)
mauvaises = []
for B, o, nom in lignes:
    p = os.path.join(LOT, nom)
    if not os.path.exists(p):
        mauvaises.append((nom, "ABSENTE"))
        continue
    lu, oc = emp(p)
    if lu != B or oc != o:
        mauvaises.append((nom, "lu %s %do" % (lu, oc)))
chk("REC", "les 22 pieces a l'empreinte et a la taille", not mauvaises, str(mauvaises))

# les pieces inchangees, au bit contre le lot v3
V3L = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_v3", "lot")
neuves, inchangees = [], 0
for _, _, nom in lignes:
    ref = os.path.join(V3L, nom)
    if not os.path.exists(ref):
        neuves.append(nom)
        continue
    if open(os.path.join(LOT, nom), 'rb').read() == open(ref, 'rb').read():
        inchangees += 1
    else:
        mauvaises.append((nom, "DIFFERE du lot v3"))
chk("REC", "les pieces communes au lot v3 sont AU BIT", not mauvaises, str(mauvaises))
print("      inchangees : %d ; neuves : %s" % (inchangees, ", ".join(neuves)))
chk("REC", "v4 = d467a239c3555737, 34728 o (annonce)",
    emp(ACTE) == ("d467a239c3555737", 34728), str(emp(ACTE)))
chk("REC", "la v3 conservee au lot est celle que j'ai certifiee",
    open(os.path.join(LOT, "journal_delta_nn_R4R5_v3.md"), 'rb').read()
    == open(V3, 'rb').read())

# =========================================================== 2. LES HUNKS
print("\n[DIFF] SIX HUNKS, ET SIX SEULEMENT")
import difflib
A = open(V3, encoding="utf-8").read().splitlines()
B = T.splitlines()
sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
h = [o for o in sm.get_opcodes() if o[0] != 'equal']
chk("DIFF", "6 hunks, +17 / -7 (compte PAR POSITION)",
    len(h) == 6 and sum(j2 - j1 for t, i1, i2, j1, j2 in h) == 17
    and sum(i2 - i1 for t, i1, i2, j1, j2 in h) == 7,
    "%d hunks, +%d / -%d" % (len(h), sum(j2 - j1 for t, i1, i2, j1, j2 in h),
                             sum(i2 - i1 for t, i1, i2, j1, j2 in h)))
chk("DIFF", "hors hunks, la v4 est mot pour mot la v3 certifiee",
    all(A[i1:i2] == B[j1:j2] for t, i1, i2, j1, j2 in sm.get_opcodes() if t == 'equal'))
# et la chaine en amont : la v3 hors ses dix hunks etait la v2 certifiee 89/89
V2 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5_v2", "lot",
                  "journal_delta_nn_R4R5_v2.md")
A2 = open(V2, encoding="utf-8").read().splitlines()
sm2 = difflib.SequenceMatcher(None, A2, A, autojunk=False)
chk("DIFF", "et la v3 l'etait de la v2 : la chaine tient par transitivite",
    len([o for o in sm2.get_opcodes() if o[0] != 'equal']) == 10
    and all(A2[i1:i2] == A[j1:j2] for t, i1, i2, j1, j2 in sm2.get_opcodes() if t == 'equal'))

# ================================================= 3. H9 : MES DEUX ERRATA
print("\n[H9] LES DEUX ERRATA, RELUS CONTRE MES .json")
S3 = open(os.path.join(RAC, "P3_pc26", "p40", "controle_section3_machine2_v1.log"),
          encoding="utf-8").read()
six = re.findall(r"p=(\d+) s=([\d.]+) : P_env\s+([\d.]+) ; T =\s+(\d+) ->\s+([\d.]+) per",
                 S3)
chk("H9", "six colonnes dans mon log de mesure", len(six) == 6, "%d" % len(six))
sv = [float(x[1]) for x in six]
pe = [float(x[2]) for x in six]
pr = [float(x[4]) for x in six]

chk("H9", "erratum (a) : 'au moins 4 periodes par fenetre (4.2 a 5.5)'",
    cite("au moins 4 periodes par fenetre") and cite("(4.2 a 5.5)")
    and min(pr) == 4.2 and max(pr) == 5.5,
    "mesure : %.1f a %.1f" % (min(pr), max(pr)))
chk("H9", "la borne haute fautive '4 a 5' a disparu", "4 a 5 periodes" not in TPLAT)
chk("H9", "erratum (b) : les trois valeurs sont dites DERIVEES au seuil",
    cite("DERIVEE au seuil s*, 116.8 / 119.5 / 180.1 unites a p = 26 / 30 / 40"))
chk("H9", "le mot 'mesuree' ne s'applique plus a ces trois valeurs",
    "117 a 180" not in TPLAT and "unites, mesuree dans les enveloppes" not in TPLAT)
chk("H9", "ce qui est dit MESURE est bien la modulation",
    cite("ce qui est MESURE (six colonnes de m2 sous le seuil"))
chk("H9", "et la phrase se clot sur la regle",
    cite("une derivation n'est pas une mesure"))

chk("H9", "'s de 0.4249 a 0.4679' encadre mes six colonnes",
    abs(min(sv) - 0.4249) < 5e-5 and abs(max(sv) - 0.4679) < 5e-5 and cite("0.4249 a"),
    "mesure : %.6f a %.6f" % (min(sv), max(sv)))
chk("H9", "les six colonnes sont TOUTES sous le seuil",
    all(s < 0.472090 for s in sv), "max %.6f < s*(30) = 0.472090" % max(sv))
chk("H9", "'P_env de 210.5 a 2284.1' encadre mes six colonnes",
    abs(min(pe) - 210.5) < 0.05 and abs(max(pe) - 2284.1) < 0.05,
    "MESURE : %.1f a %.1f -- la borne BASSE est 189.7 (p=26, s=0.467870), "
    "pas 210.5 ; 210.5 est le premier de ma LISTE, qui n'est pas triee"
    % (min(pe), max(pe)))
chk("H9", "'profondeur a 0.1 pour cent du premier ordre complet'",
    cite("profondeur a 0.1 pour cent du") and
    J(r"P3_pc26\rederivation\run_profondeur_machine2_v1.json")["n_mordues"] == 0)

print("\n[H10] LA FORME")
# FAUX ECHEC du premier passage : j'avais fige la fenetre de la TABLE aux lignes de la
# v3 (289-299) decalees a la main de +10. Elle est en 294-304 dans la v4. Un perimetre
# s'extrait d'une STRUCTURE, jamais d'un decalage suppose : je localise la table par son
# en-tete et je prends son bloc contigu.
tete = next(i for i, l in enumerate(B) if l.strip().startswith("prediction")
            and "plume" in l and "gel" in l)
fin = tete
while fin + 1 < len(B) and B[fin + 1].strip():
    fin += 1
hors_table = [(i + 1, len(l)) for i, l in enumerate(B) if not (tete <= i <= fin)]
chk("H10", "la ligne de 120 caracteres est refluee",
    max(n for _, n in hors_table) <= 100,
    "table localisee l. %d-%d ; plus longue ligne hors table : %d car. (l. %d)"
    % (tete + 1, fin + 1, max(n for _, n in hors_table),
       max(hors_table, key=lambda x: x[1])[0]))
chk("H10", "aucun mot n'a change dans ce hunk",
    re.sub(r"\s+|\[H10\]", " ", " ".join(A[210:211])).split()
    == [w for w in re.sub(r"\s+|\[H10\]", " ", " ".join(B[214:216])).split()],
    "v3 : %d mots ; v4 : %d mots"
    % (len(" ".join(A[210:211]).split()),
       len([w for w in " ".join(B[214:216]).split() if w != "[H10]"])))

# ======================================== 4. LA PIECE DE DEPOT : nn -> 89
print("\n[DEPOT] LA PIECE DEPOSEE CONTRE L'ACTE CERTIFIE")
# TROIS FAUX ECHECS du premier passage, et ils venaient d'une convention que j'avais
# INVENTEE : j'attendais une substitution nn -> 89 DANS le corps. Ce n'est pas la
# convention des deux machines, et je l'ai moi-meme certifiee 7/7 ce matin sur le depot
# v2 : le NUMERO vit dans le NOM DE FICHIER et dans le manifeste, et la piece deposee est
# AU BIT l'acte certifie -- ce qui est la propriete forte, pas la faible.
# La regle 7 du 11/09 (une taille identique ne prouve rien apres un renommage) garde tout
# son sens : c'est pourquoi je compare l'empreinte, pas la taille.
PD = os.path.join(DEP, "journal_delta_89_R4R5_v4.md")
brut_acte = open(ACTE, 'rb').read()
brut_dep = open(PD, 'rb').read()
chk("DEPOT", "la piece deposee est AU BIT l'acte v4 certifie", brut_acte == brut_dep,
    "%d octets, %d differents" % (len(brut_dep),
                                  sum(1 for x, y in zip(brut_acte, brut_dep) if x != y)))
chk("DEPOT", "le numero 89 vit dans le NOM du fichier",
    os.path.basename(PD) == "journal_delta_89_R4R5_v4.md")
nn_corps = len(re.findall(r"nn\.\d+|delta_nn", brut_dep.decode('utf-8')))
nn_v2 = len(re.findall(r"nn\.\d+|delta_nn",
                       open(os.path.join(RAC, "entrant_machine1_2026-09-11_depot_89_v2",
                                         "lot", "journal_delta_89_R4R5_v2.md"),
                            encoding="utf-8").read()))
# et le compte attendu n'est pas un nombre ecrit a la main : c'est CELUI DE LA v2 deposee.
chk("DEPOT", "convention identique a celle du depot v2, deja verifiee 7/7",
    nn_corps == nn_v2,
    "le corps garde %d reperes 'nn' (v2 deposee : %d) -- CONSTAT, non defaut : "
    "l'acte s'annonce lui-meme 'numero nn au depot'" % (nn_corps, nn_v2))

print("\n[DEPOT] LE MANIFESTE DE DEPOT")
MD = os.path.join(DEP, "MANIFEST_DEPOT_delta89_machine1.txt")
MDT = open(MD, encoding="utf-8").read()
B_dep = hashlib.sha256(unicodedata.normalize('NFC', brut_dep.decode('utf-8'))
                       .replace('\r\n', '\n').encode()).hexdigest()[:16]
print("      empreinte de la piece deposee : %s (%d o)" % (B_dep, len(brut_dep)))
chk("DEPOT", "le manifeste de depot cite l'empreinte de la piece", B_dep in MDT, B_dep)
# FAUX ECHEC : mon controle interdisait la chaine "-10", or elle apparait dans "etait
# -11 et non -10", qui est l'ENONCE MEME de la correction. Ce qu'il faut verifier est que
# le compte QUI FAIT FOI est -11 et que tout "-10" restant est cite comme faux.
chk("DEPOT", "il porte le compte du diff v2->v3 CORRIGE (+55 / -11)",
    "+55/-11" in MDT.replace(" ", ""))
chk("DEPOT", "et tout '-10' restant y est cite comme le compte FAUX",
    all(re.search(r"(et non|au lieu de|etait)\s*-10\b", MDT[max(0, m.start() - 40):m.end()])
        for m in re.finditer(r"-10\b", MDT)),
    "%d occurrence(s) de -10" % len(re.findall(r"-10\b", MDT)))
chk("DEPOT", "il nomme D-CERT-4 et D-CERT-5", "D-CERT-4" in MDT and "D-CERT-5" in MDT)
chk("DEPOT", "il ne porte pas sa propre empreinte",
    hashlib.sha256(unicodedata.normalize('NFC', MDT).replace('\r\n', '\n').encode()
                   ).hexdigest()[:16] not in MDT)
chk("DEPOT", "il cite le canon de MA certification v3",
    "bdd00189e68b61dc" in MDT)

print("\n" + "=" * 88)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for s, q, d in MORD:
    print("   MORD  [%s] %s" % (s, q))
    print("         %s" % d)
print("=" * 88)
