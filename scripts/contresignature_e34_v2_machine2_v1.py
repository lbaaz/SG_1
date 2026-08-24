# -*- coding: ascii -*-
"""RE-COMPOSITION INDEPENDANTE DU BLOC E34_TEXTE_v2 -- machine 2.

Le delta 81 v2 (6e7fed3ca455b684) demande a machine 2 de re-executer la
MEME composition sur SES copies, puis de signer. Je ne rejoue pas
extraction_e33_e36_machine1_v2.py (E28) : je recompose avec mon propre
code, a partir des memes deux sources et des memes regles declarees.

REGLES DECLAREES PAR LE DELTA 81 v2, appliquees telles qu'ecrites :
  - source 1 : le bloc E34_TEXTE de l'acte 80 v2, l.55-62
  - source 2 : la forme machine 2, extraite PAR STRUCTURE de ma note
  - substitution : le segment "et le RESIDU ... r/(1-r))" remplace par
    les MOTS de la forme ; unicite du segment asseree
  - re-pliage : glouton, indent 2, largeur 72, coupure aux espaces
  - garde mot a mot : forme inseree == forme extraite

CE QUE CE LOG JOUE :
  1. custody des deux sources et du delta 81 v2
  2. les quatre verrous contresignes (ils ne doivent PAS avoir bouge)
  3. la re-composition, et son empreinte contre acd878ec74d6948b
  4. la garde mot a mot, et le test negatif (mutation d'un mot)
  5. le RACCORD : ce que la substitution laisse a la jointure

CE QUE CE LOG NE JOUE PAS :
  - il n'execute pas l'instrument de machine 1
  - il ne juge pas le fond de E33/E35/E36 : deja signes
  - il n'inscrit rien au gel ni au script

Sortie : contresignature_e34_v2_machine2_v1.log
"""
import hashlib
import os
import re
import unicodedata

B = os.path.dirname(os.path.abspath(__file__))
ACTE = os.path.join(B, "journal_delta_80_acte_M17_v2.md")
NOTE = os.path.join(B, "note_machine2_contresignature_E33_E36_v1.md")
D81 = os.path.join(B, "journal_delta_81_contresignature_E33_E36_v2.md")
LOG = os.path.join(B, "contresignature_e34_v2_machine2_v1.log")
OUT = []


def p(s=""):
    OUT.append(s)
    print(s, flush=True)


def cB(b):
    if isinstance(b, str):
        b = b.encode("ascii")
    return hashlib.sha256(unicodedata.normalize(
        "NFC", b.decode("utf-8")).encode("utf-8")).hexdigest()[:16]


def fich(c):
    b = open(c, "rb").read()
    return cB(b), len(b)


p("=" * 74)
p("RE-COMPOSITION INDEPENDANTE DU BLOC E34_TEXTE_v2 -- MACHINE 2")
p("=" * 74)
p("")
p("1. CUSTODY DES SOURCES")
for nom, c, att in (("acte 80 v2", ACTE, "a2b80c149d6a05bc"),
                    ("ma note v1", NOTE, "f9de93f16c5382ed"),
                    ("delta 81 v2", D81, "6e7fed3ca455b684")):
    e, o = fich(c)
    p("   %-12s %-46s %s %5d o  %s"
      % (nom, os.path.basename(c), e, o,
         "CONFORME" if e == att else "DIVERGENT (attendu %s)" % att))

acte = open(ACTE, encoding="ascii").read().split("\n")
note = open(NOTE, encoding="ascii").read().split("\n")
d81 = open(D81, encoding="ascii").read()

p("")
p("2. LES QUATRE VERROUS CONTRESIGNES -- ONT-ILS BOUGE ?")
VER = {"E33": ((45, 46), "076e110c6a0a53c7"),
       "E34_amendement": ((74, 76), "5b16b328a1e843fd"),
       "E35": ((85, 92), "febc6ef278392136"),
       "E36": ((104, 107), "6d808620ab1df171")}
tenus = 0
for nom, ((i0, i1), att) in VER.items():
    e = cB("\n".join(acte[i0 - 1:i1]))
    bon = e == att and att in d81
    tenus += bon
    p("   %-16s l.%-3d-%-3d %s  %s"
      % (nom, i0, i1, e, "TENU (et cite au 81 v2)" if bon else "BOUGE"))
p("   %d/%d verrous tenus" % (tenus, len(VER)))

p("")
p("3. LA RE-COMPOSITION")
V1 = "\n".join(acte[54:62])          # bloc E34_TEXTE, acte l.55-62
p("   bloc v1 de l'acte : l.55-62, %d o, empreinte %s" % (len(V1), cB(V1)))

# --- forme machine 2, extraite PAR STRUCTURE de ma note -------------------
i0 = next(i for i, l in enumerate(note)
          if l.strip().startswith('"... et le RESIDU estime par le ratio'))
i1 = next(i for i in range(i0, len(note))
          if note[i].rstrip().endswith('MEME paire."'))
forme_lignes = note[i0:i1 + 1]
p("   forme machine 2 : note l.%d-%d (span DERIVE, non lu du log m1)"
  % (i0 + 1, i1 + 1))
forme = " ".join(x.strip() for x in forme_lignes)
forme = forme.strip('"')
forme = re.sub(r"^\.\.\.\s*", "", forme)
mots_forme = forme.split()
p("   %d mots ; premiers : %s ..." % (len(mots_forme), " ".join(mots_forme[:6])))
p("   derniers : ... %s" % " ".join(mots_forme[-6:]))

# --- substitution par les MOTS -------------------------------------------
mots_v1 = V1.split()
seg = "et le RESIDU estime par le ratio mesure r (residu = pas x r/(1-r))".split()
occ = [k for k in range(len(mots_v1) - len(seg) + 1)
       if mots_v1[k:k + len(seg)] == seg]
p("   segment a substituer : %d mot(s) ; occurrences dans le bloc v1 : %d"
  % (len(seg), len(occ)))
assert len(occ) == 1, "unicite du segment NON tenue"
k = occ[0]
mots_v2 = mots_v1[:k] + mots_forme + mots_v1[k + len(seg):]
p("   mots : v1 %d -> v2 %d" % (len(mots_v1), len(mots_v2)))


def plier(mots, indent=2, largeur=72):
    """Glouton, coupure aux espaces, indent 2, largeur 72."""
    lignes, cour = [], ""
    for m in mots:
        cand = (cour + " " + m) if cour else m
        if len(cand) + indent <= largeur:
            cour = cand
        else:
            lignes.append(" " * indent + cour)
            cour = m
    if cour:
        lignes.append(" " * indent + cour)
    return "\n".join(lignes)


V2 = plier(mots_v2)
e2 = cB(V2)
p("")
p("   bloc compose : %d o, %d mots, empreinte %s" % (len(V2), len(mots_v2), e2))
p("   annonce par le delta 81 v2 : 668 o, 105 mots, acd878ec74d6948b")
p("   -> %s" % ("CONCORDE AU BIT" if e2 == "acd878ec74d6948b" and len(V2) == 668
                else "DIVERGE"))

p("")
p("4. GARDE MOT A MOT ET TEST NEGATIF")
p("   forme inseree == forme extraite : %s"
  % (mots_v2[k:k + len(mots_forme)] == mots_forme))
mut = list(mots_v2)
j = k + 3
mut[j] = mut[j].upper() if mut[j].islower() else mut[j] + "X"
p("   mutation d'UN mot de la forme (%r -> %r) -> empreinte %s : %s"
  % (mots_v2[j], mut[j], cB(plier(mut)),
     "MORD" if cB(plier(mut)) != e2 else "INERTE"))
p("   test negatif du pliage : largeur 71 au lieu de 72 -> %s"
  % ("MORD" if cB(plier(mots_v2, 2, 71)) != e2 else "INERTE"))

p("")
p("5. LE RACCORD -- CE QUE LA SUBSTITUTION LAISSE A LA JOINTURE")
jonction = " ".join(mots_v2[k + len(mots_forme) - 4:k + len(mots_forme) + 6])
p("   voisinage de la couture : ... %s ..." % jonction)
fin_forme = mots_forme[-1]
suite = mots_v2[k + len(mots_forme)] if k + len(mots_forme) < len(mots_v2) else ""
p("   dernier mot de la forme : %r ; premier mot qui suit : %r"
  % (fin_forme, suite))
p("   la forme se termine par un POINT : %s" % fin_forme.endswith("."))
p("   la suite reprend par un TIRET de continuation : %s" % (suite == "--"))
if fin_forme.endswith(".") and suite == "--":
    p("   -> RACCORD DEFECTUEUX : une phrase se ferme, puis une incise en")
    p("      tiret la continue comme si elle ne s'etait pas fermee. Dans le")
    p("      bloc v1 le tiret suivait une parenthese SANS point.")
    v1j = " ".join(mots_v1[k + len(seg) - 3:k + len(seg) + 4])
    p("      v1 a la meme place : ... %s ..." % v1j)

p("")
p("6. LES QUATRE AUTRES BLOCS SONT-ILS INCHANGES DANS LE 81 v2 ?")
for nom, ((i0v, i1v), att) in VER.items():
    p("   %-16s %s cite au 81 v2 : %s" % (nom, att, att in d81))
p("   le 81 v2 cite l'acte : %s ; ma note : %s"
  % ("a2b80c149d6a05bc" in d81, "f9de93f16c5382ed" in d81))
p("   emplacements de signature restants : %d"
  % d81.count("................"))

with open(LOG, "w", encoding="ascii", newline="\n") as fh:
    fh.write("\n".join(OUT) + "\n")
b = open(LOG, "rb").read()
print("")
print("LOG RELU DU DISQUE : %s  %s  %d o"
      % (os.path.basename(LOG), cB(b), len(b)))
