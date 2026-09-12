#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CONTROLE DE RECEPTION DU LOT machine 1 -- ACTE R4/R5 **v3** -- machine 2, v1, 11/09/2026.

FEUILLE NEUVE. Elle ne certifie RIEN du contenu de l'acte : elle etablit seulement
(a) que le lot recu est complet et conforme a son manifeste, (b) que les pieces dites
INCHANGEES le sont AU BIT contre celles que je detiens deja des lots v1 et v2, et
(c) quelles pieces sont NEUVES -- donc a verifier au fond.

Regles appliquees :
  - le canon est l'empreinte du MANIFESTE, jamais celle du ZIP brut (regle du 11/09) ;
  - un manifeste ne porte JAMAIS sa propre empreinte : je verifie qu'il ne s'y liste pas ;
  - une taille identique ne prouve rien -- seule l'empreinte tranche ;
  - le compte se mesure APRES le dernier ajout ;
  - je dis ce que je ne peux PAS verifier, a la portee exacte.
"""
import hashlib, os, sys, unicodedata

RAC = r"D:\devs\bocal\BOCAL4"
ICI = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_v3")
LOT = os.path.join(ICI, "lot")
MAN = os.path.join(LOT, "MANIFEST_lot_machine1_R4R5_acte_v3.txt")
V1 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5", "lot")
V2 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5_v2", "lot")

OK, MORD = [], []


def chk(quoi, cond, detail=''):
    OK.append(bool(cond))
    if not cond:
        MORD.append((quoi, detail))
    print('  [%s] %-52s %s' % ('OK  ' if cond else 'MORD', quoi[:52], detail))


def emp(chemin):
    """(B, brut, octets) : B = sha256 du texte NFC + LF ; brut = sha256 des octets."""
    raw = open(chemin, 'rb').read()
    brut = hashlib.sha256(raw).hexdigest()[:16]
    txt = unicodedata.normalize('NFC', raw.decode('utf-8'))
    txt = txt.replace('\r\n', '\n').replace('\r', '\n')
    B = hashlib.sha256(txt.encode('utf-8')).hexdigest()[:16]
    return B, brut, len(raw)


print("=" * 84)
print("RECEPTION DU LOT machine 1 -- ACTE R4/R5 v3")
print("=" * 84)

# ------------------------------------------------------------------ le canon
print("\n[1] LE CANON (empreinte du MANIFESTE, pas du ZIP)")
B_man, brut_man, o_man = emp(MAN)
print("      CANON (B)  = %s   %d octets" % (B_man, o_man))
print("      manifeste brut = %s" % brut_man)
ZIP = os.path.join(ICI, "lot_machine1_2026-09-11_R4R5_acte_v3.zip")
brut_zip = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()[:16]
print("      ZIP brut (indicatif, ne fait PAS canon) = %s" % brut_zip)
ENV = r"C:\Users\bazil\Downloads\files (49).zip"
if os.path.exists(ENV):
    print("      enveloppe recue brut = %s"
          % hashlib.sha256(open(ENV, 'rb').read()).hexdigest()[:16])

T = open(MAN, encoding="utf-8").read()
chk("le manifeste ne porte pas sa propre empreinte", B_man not in T and brut_man not in T)

# --------------------------------------------------------------- les 21 lignes
print("\n[2] LES PIECES DU MANIFESTE, EMPREINTE ET TAILLE")
lignes = []
for l in T.splitlines():
    ch = l.split()
    if len(ch) == 3 and len(ch[0]) == 16 and ch[1].isdigit():
        try:
            int(ch[0], 16)
        except ValueError:
            continue
        lignes.append((ch[0], int(ch[1]), ch[2]))
chk("21 lignes de pieces extraites de la STRUCTURE", len(lignes) == 21, "%d" % len(lignes))
chk("le manifeste annonce 21 pieces", "pieces : 21" in T)

sur_disque = sorted(f for f in os.listdir(LOT)
                    if f != "MANIFEST_lot_machine1_R4R5_acte_v3.txt")
chk("21 fichiers au lot hors manifeste", len(sur_disque) == 21, "%d" % len(sur_disque))
chk("aucun fichier hors manifeste",
    set(sur_disque) == set(n for _, _, n in lignes),
    str(set(sur_disque) ^ set(n for _, _, n in lignes)) if
    set(sur_disque) != set(n for _, _, n in lignes) else '')

emps = {}
for B_att, o_att, nom in lignes:
    p = os.path.join(LOT, nom)
    if not os.path.exists(p):
        chk(nom, False, "ABSENTE")
        continue
    B, brut, o = emp(p)
    emps[nom] = (B, brut, o)
    chk(nom, B == B_att and o == o_att,
        "lu B=%s %do / attendu %s %do" % (B, o, B_att, o_att)
        if (B != B_att or o != o_att) else "")

print("\n[3] LA CONVENTION B == brut (tout ASCII / LF)")
for nom, (B, brut, o) in sorted(emps.items()):
    raw = open(os.path.join(LOT, nom), 'rb').read()
    pur = (B == brut) and (b'\r' not in raw) and all(c < 128 for c in raw)
    if not pur:
        chk("ASCII/LF : %s" % nom, False,
            "B=%s brut=%s CR=%d non-ASCII=%d"
            % (B, brut, raw.count(b'\r'), sum(1 for c in raw if c >= 128)))
chk("B == brut pour les 21 pieces",
    all(emps[n][0] == emps[n][1] for n in emps), "")

# ------------------------------------------------- ce que je detiens deja
print("\n[4] LES PIECES DITES INCHANGEES, AU BIT CONTRE MES COPIES")
neuves, inchangees = [], []
for nom in sorted(emps):
    ref = None
    for base in (V2, V1):
        c = os.path.join(base, nom)
        if os.path.exists(c):
            ref = c
            break
    if ref is None:
        neuves.append(nom)
        continue
    a = open(os.path.join(LOT, nom), 'rb').read()
    b = open(ref, 'rb').read()
    inchangees.append(nom)
    chk("au bit : %s" % nom, a == b,
        "" if a == b else "DIFFERE de %s" % os.path.basename(os.path.dirname(ref)))
print("      inchangees confrontees : %d" % len(inchangees))
print("      NEUVES (a verifier au fond) : %s" % (", ".join(neuves) or "aucune"))

print("\n[5] LES DEUX ANCRES CITEES PAR LE MANIFESTE")
B_v2 = emps.get("journal_delta_nn_R4R5_v2.md", ('', '', 0))[0]
B_v1 = emps.get("journal_delta_nn_R4R5_v1.md", ('', '', 0))[0]
chk("v2 du lot == ce07e533176441a5 (annoncee)", B_v2 == "ce07e533176441a5", B_v2)
chk("v2 du lot == la v2 que j'ai CERTIFIEE 89/89",
    open(os.path.join(LOT, "journal_delta_nn_R4R5_v2.md"), 'rb').read()
    == open(os.path.join(V2, "journal_delta_nn_R4R5_v2.md"), 'rb').read())
chk("v1 du lot == 86d6ee29d27938ff (annoncee)", B_v1 == "86d6ee29d27938ff", B_v1)
B_v3 = emps.get("journal_delta_nn_R4R5_v3.md", ('', '', 0))[0]
chk("v3 == eaaacadd99fb468d (annoncee dans la note)", B_v3 == "eaaacadd99fb468d", B_v3)
chk("v3 fait 34028 octets", emps["journal_delta_nn_R4R5_v3.md"][2] == 34028)

print("\n[6] LA NOTE DE COUVERTURE, HORS LOT ET DANS LE LOT")
a = open(os.path.join(ICI, "POUR_MACHINE2_v3_acte_R4R5_machine1_v1.md"), 'rb').read()
b = open(os.path.join(LOT, "POUR_MACHINE2_v3_acte_R4R5_machine1_v1.md"), 'rb').read()
chk("note hors lot == note du lot, au bit", a == b)
c = open(os.path.join(ICI, "journal_delta_nn_R4R5_v3.md"), 'rb').read()
d = open(os.path.join(LOT, "journal_delta_nn_R4R5_v3.md"), 'rb').read()
chk("journal v3 hors lot == journal v3 du lot, au bit", c == d)

print("\n" + "=" * 84)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s  %s" % (q, d))
print("CANON DU LOT RECU : %s" % B_man)
print("=" * 84)
sys.exit(1 if MORD else 0)
