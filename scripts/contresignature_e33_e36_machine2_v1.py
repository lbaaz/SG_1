# -*- coding: ascii -*-
"""CONTRESIGNATURE E33..E36 -- re-extraction INDEPENDANTE, machine 2.

Le delta 81 (brouillon 53b3485b3e66715e) demande a machine 2, AVANT de
signer, de re-extraire chaque bloc de SA copie de l'acte avec les memes
ancres et de comparer les empreintes.

CE QUE CE LOG JOUE :
  1. custody de l'acte source et du brouillon 81
  2. les spans DERIVES PAR STRUCTURE (regle 12), non lus du log de
     machine 1 -- chaque bloc va de son ancre d'ouverture (debut de ligne,
     colonne 0 relative a l'indentation de section) a la ligne qui precede
     l'ancre de fermeture suivante
  3. la comparaison des spans derives avec les spans DECLARES au delta 81
  4. les empreintes convention B des blocs, comparees aux cinq annoncees
  5. le defaut declare par machine 1 (4 lignes de fondement echouees)
  6. le test negatif : une mutation d'un caractere par bloc doit changer
     EXACTEMENT une empreinte

CE QUE CE LOG NE JOUE PAS :
  - il n'execute PAS extraction_e33_e36_machine1_v1.py : rejouer
    l'instrument de l'autre machine ne serait pas une re-derivation
    (E28 : l'accord obtenu dans la meme arithmetique ne prouve rien)
  - il ne juge pas le FOND des textes : c'est la note qui signe
  - il n'inscrit rien au gel ni au script

Sortie : contresignature_e33_e36_machine2_v1.log
"""
import hashlib
import os
import unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
ACTE = os.path.join(BASE, "journal_delta_80_acte_M17_v2.md")
D81 = os.path.join(BASE, "journal_delta_81_contresignature_E33_E36_v1.md")
LOG = os.path.join(BASE, "contresignature_e33_e36_machine2_v1.log")
OUT = []


def p(s=""):
    OUT.append(s)
    print(s, flush=True)


def convB_octets(b):
    return hashlib.sha256(unicodedata.normalize(
        "NFC", b.decode("utf-8")).encode("utf-8")).hexdigest()[:16]


def convB(chemin):
    b = open(chemin, "rb").read()
    return convB_octets(b), len(b)


p("=" * 74)
p("CONTRESIGNATURE E33..E36 -- RE-EXTRACTION INDEPENDANTE, MACHINE 2")
p("=" * 74)
p("")
p("1. CUSTODY")
ea, oa = convB(ACTE)
e8, o8 = convB(D81)
p("   acte source  journal_delta_80_acte_M17_v2.md  %s  %d o" % (ea, oa))
p("   attendu par le delta 81 : a2b80c149d6a05bc, 18049 o -> %s"
  % ("CONFORME" if ea == "a2b80c149d6a05bc" and oa == 18049 else "DIVERGENT"))
p("   brouillon 81 %s  %d o" % (e8, o8))

lignes = open(ACTE, encoding="ascii").read().split("\n")
d81 = open(D81, encoding="ascii").read()

# --- 2 : spans derives par STRUCTURE ---------------------------------------
p("")
p("2. SPANS DERIVES PAR STRUCTURE (regle 12), NON LUS DU LOG DE MACHINE 1")
p("   ancre d'ouverture : une ligne dont le contenu commence par le mot-cle")
p("   a l'indentation de section ; fermeture : la premiere ligne suivante")
p("   qui ouvre un autre mot-cle de meme rang.")

MOTS = ("TEXTE :", "TEXTE PROPOSE (", "AMENDEMENT AU TEXTE (", "FONDEMENT",
        "FONDEMENT MESURE", "EFFET SCRIPT", "Regle M15", "TABLE DE",
        "Les mesures des")


def ouvre(l, mot):
    return l.strip().startswith(mot)


def span(depart, mot, fins):
    """Rend (i0, i1) 1-indexes : de la ligne qui ouvre `mot` a la ligne
    qui precede la premiere ligne ouvrant l'un de `fins`."""
    i0 = None
    for i in range(depart, len(lignes)):
        if ouvre(lignes[i], mot):
            i0 = i
            break
    if i0 is None:
        return None
    for j in range(i0 + 1, len(lignes)):
        if any(ouvre(lignes[j], f) for f in fins):
            return (i0 + 1, j)
    return None


# chaque bloc : (nom, ligne de depart de recherche, mot d'ouverture, fins)
DEP = {}
for i, l in enumerate(lignes):
    s = l.strip()
    if s.startswith("80.2 E33"):
        DEP["E33"] = i
    elif s.startswith("80.3 E34"):
        DEP["E34"] = i
    elif s.startswith("80.4 E35"):
        DEP["E35"] = i
    elif s.startswith("80.5 E36"):
        DEP["E36"] = i
p("   ancres de section trouvees : %s"
  % ", ".join("%s l.%d" % (k, v + 1) for k, v in sorted(DEP.items())))

BLOCS = [
    ("E33", span(DEP["E33"], "TEXTE :", ("FONDEMENT",)), "076e110c6a0a53c7",
     114, "l.45-46"),
    ("E34_texte", span(DEP["E34"], "TEXTE :", ("FONDEMENT",)),
     "cbf046e533c2c94d", 477, "l.55-62"),
    ("E34_amendement", span(DEP["E34"], "AMENDEMENT AU TEXTE (",
                            ("Regle M15", "EFFET SCRIPT")),
     "5b16b328a1e843fd", 203, "l.74-76"),
    ("E35", span(DEP["E35"], "TEXTE PROPOSE (", ("FONDEMENT",)),
     "febc6ef278392136", 519, "l.85-92"),
    ("E36", span(DEP["E36"], "TEXTE :", ("FONDEMENT",)), "6d808620ab1df171",
     254, "l.104-107"),
]

p("")
p("3. LES CINQ BLOCS -- SPAN DERIVE, OCTETS, EMPREINTE")
p("   bloc              derive      declare     o     empreinte derivee"
  "  verdict")
sigs = {}
tous_ok = True
for nom, sp, att_e, att_o, att_span in BLOCS:
    if sp is None:
        p("   %-17s ANCRE INTROUVABLE" % nom)
        tous_ok = False
        continue
    i0, i1 = sp
    txt = "\n".join(lignes[i0 - 1:i1])
    b = txt.encode("ascii")
    e = convB_octets(b)
    d = "l.%d-%d" % (i0, i1)
    bon = (e == att_e) and (len(b) == att_o) and (d == att_span)
    tous_ok = tous_ok and bon
    sigs[nom] = (e, len(b), d)
    p("   %-17s %-11s %-11s %-5d %-17s %s"
      % (nom, d, att_span, len(b), e, "CONCORDE" if bon else "DIVERGE"))
p("")
p("   comptes : %d blocs extraits + %d introuvables == %d ancres"
  % (sum(1 for _, s, _, _, _ in BLOCS if s), sum(1 for _, s, _, _, _ in BLOCS
                                                 if not s), len(BLOCS)))
p("   les cinq empreintes de machine 1 sont-elles retrouvees ? %s"
  % ("OUI, les cinq" if tous_ok else "NON"))

# --- 4 : le defaut declare -------------------------------------------------
p("")
p("4. LE DEFAUT DECLARE PAR MACHINE 1 -- LES QUATRE LIGNES ECHOUEES")
sp = span(DEP["E34"], "Regle M15", ("EFFET SCRIPT",))
if sp:
    i0, i1 = sp
    b = "\n".join(lignes[i0 - 1:i1]).encode("ascii")
    e = convB_octets(b)
    p("   span derive : l.%d-%d, %d o, empreinte %s" % (i0, i1, len(b), e))
    p("   declare au log machine 1 : l.77-80, 266 o, 151063c2614891f9")
    p("   -> %s" % ("CONCORDE : le defaut existe et il est exactement decrit"
                    if (i0, i1) == (77, 80) and len(b) == 266
                    and e == "151063c2614891f9" else "DIVERGE"))
    p("   premiere ligne : %s" % lignes[i0 - 1].strip()[:60])
    p("   derniere ligne : %s" % lignes[i1 - 1].strip()[:60])
    p("   ces quatre lignes sont-elles DANS un bloc signe ? %s"
      % ("non -- aucun span de bloc ne les couvre"
         if all(not (s and s[0] <= i0 <= s[1]) for _, s, _, _, _ in BLOCS)
         else "OUI <-- elles seraient signees a tort"))
else:
    p("   ANCRE INTROUVABLE")

# --- 5 : test negatif ------------------------------------------------------
p("")
p("5. TEST NEGATIF -- une mutation d'un caractere change-t-elle EXACTEMENT")
p("   une empreinte ?")
for cible, sp, _, _, _ in BLOCS[:1] + BLOCS[2:3]:
    i0, i1 = sp
    mut = list(lignes)
    src = mut[i0 - 1]
    j = next(k for k, c in enumerate(src) if c.isalpha())
    mut[i0 - 1] = src[:j] + ("X" if src[j] != "X" else "Y") + src[j + 1:]
    chg = 0
    for nom, s2, _, _, _ in BLOCS:
        a = convB_octets("\n".join(lignes[s2[0] - 1:s2[1]]).encode("ascii"))
        bmut = convB_octets("\n".join(mut[s2[0] - 1:s2[1]]).encode("ascii"))
        chg += (a != bmut)
    p("   mutation dans %-17s -> %d/%d empreintes changees : %s"
      % (cible, chg, len(BLOCS), "MORD" if chg == 1 else "INERTE OU DIFFUSE"))

# --- 6 : les empreintes annoncees sont-elles dans le brouillon 81 ? --------
p("")
p("6. LES CINQ EMPREINTES SONT-ELLES CELLES QUE LE BROUILLON 81 AFFICHE ?")
for nom, _, att_e, _, _ in BLOCS:
    p("   %-17s %s present dans le delta 81 : %s"
      % (nom, att_e, att_e in d81))
p("   le delta 81 cite l'acte par son empreinte : %s"
  % ("a2b80c149d6a05bc" in d81))
p("   emplacements de signature vides (a remplir) : %d"
  % d81.count("empreinte = ................"))

with open(LOG, "w", encoding="ascii", newline="\n") as fh:
    fh.write("\n".join(OUT) + "\n")
b = open(LOG, "rb").read()
print("")
print("LOG RELU DU DISQUE : %s  %s  %d o"
      % (os.path.basename(LOG), convB_octets(b), len(b)))
