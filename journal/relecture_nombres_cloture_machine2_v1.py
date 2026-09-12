#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RELECTURE MECANIQUE DES NOMBRES DE MA NOTE DE CLOTURE -- machine 2, v1, 12/09/2026."""
import hashlib, os, re, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
N = open(os.path.join(ICI, "POUR_MACHINE1_cloture_et_precision_machine2_v1.md"),
         encoding="utf-8").read()
NP = re.sub(r"\s+", " ", N)
L = open(os.path.join(ICI, "precision_de_la_borne_machine2_v1.log"),
         encoding="utf-8", errors="replace").read()
OK, MORD = [], []


def chk(q, c, d=''):
    OK.append(bool(c))
    if not c:
        MORD.append((q, d))
    print("  [%s] %-56s %s" % ("OK  " if c else "MORD", q[:56], d))


def dit(s):
    return re.sub(r"\s+", " ", s) in NP


print("=" * 84)
print("RELECTURE DES NOMBRES DE MA NOTE DE CLOTURE")
print("=" * 84)

print("\n[1] LES DEUX BORNES ET LEUR ECART")
for v in ("1.659725811e-05", "1.659260768e-05", "2.802e-04"):
    chk("au log ET cite : %s" % v, v in L and dit(v))
chk("les deux fenetres citees", "x1.0415" in L and "x1.0418" in L
    and dit("x1.0415") and dit("x1.0418"))
chk("la marge 4.15e-02 est celle du log",
    "4.153e-02" in L and dit("4.15e-02"))
chk("le meme point porte la borne des deux facons", "7|1.73" in L and dit("7|1.73"))
chk("l'ecart est bien deux ordres sous la marge",
    2.802e-04 < 4.153e-02 / 100 and dit("deux\nordres en dessous"))

print("\n[2] LE MORDANT EST VOULU")
chk("le log MORD une fois, et c'est la correction",
    "1 mordent" in L and dit("1 mord -- et il DOIT"))
chk("aucune cellule de la carte ne change de statut",
    "aucune cellule de la carte ne change de statut" in L
    and dit("aucun changement de statut"))

print("\n[3] LES CANONS CITES, VERIFIES AU POSTE")


def emp(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8'))
                          .replace('\r\n', '\n').encode()).hexdigest()[:16]


for h, chemin in (
        ("d5ace962a3a6e413", os.path.join(RAC, "entrant_machine1_2026-09-09_constante_A_v5",
                                          "MANIFEST_lot_machine1_constante_A_v5.txt")),
        ("13d2973b0e143a20", os.path.join(RAC, "certification_constante_A_v5",
                                          "MANIFEST_lot_machine2_certification_constante_A_v5_v1.txt")),
        ("a4c35a2ee691c9a7", os.path.join(RAC, "chaine_constante_A_pour_machine1",
                                          "MANIFEST_lot_machine2_chaine_constante_A_v1.txt")),
        ("7883311c6e363b02", os.path.join(RAC, "G4_trois",
                                          "MANIFEST_lot_machine2_comparaison_a_trois_v1.txt"))):
    chk("%s au poste et cite" % h,
        os.path.exists(chemin) and emp(chemin) == h and dit(h),
        "lu %s" % (emp(chemin) if os.path.exists(chemin) else "ABSENT"))
env = r"C:\Users\bazil\Downloads\files (56).zip"
if os.path.exists(env):
    b = hashlib.sha256(open(env, 'rb').read()).hexdigest()[:16]
    chk("enveloppe efd5f76bcdef0e20", b == "efd5f76bcdef0e20" and dit(b), b)

print("\n[4] SA PHRASE, CITEE EXACTEMENT")
note = open(os.path.join(RAC, "entrant_machine1_2026-09-12_cloture_geste2",
                         "note_machine1_cloture_geste2_v1.md"), encoding="utf-8").read()
plat = re.sub(r"\s+", " ", note)
chk("sa phrase est bien dans sa note",
    "les grandeurs de la borne, elles, viennent des JSON en pleine precision" in plat)
chk("et la moitie que je lui accorde aussi",
    "assez pour la classe, pas pour un bit" in plat
    and dit("assez pour la classe, pas pour un bit"))

print("\n" + "=" * 84)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s  %s" % (q, d))
print("=" * 84)
