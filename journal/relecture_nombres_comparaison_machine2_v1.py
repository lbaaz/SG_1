#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RELECTURE MECANIQUE DES NOMBRES DE MA NOTE -- machine 2, v1, 12/09/2026."""
import hashlib, os, re, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
N = open(os.path.join(ICI, "POUR_MACHINE1_comparaison_a_trois_machine2_v1.md"),
         encoding="utf-8").read()
NP = re.sub(r"\s+", " ", N)
OK, MORD = [], []


def chk(q, c, d=''):
    OK.append(bool(c))
    if not c:
        MORD.append((q, d))
    print("  [%s] %-56s %s" % ("OK  " if c else "MORD", q[:56], d))


def dit(s):
    return re.sub(r"\s+", " ", s) in NP


C = open(os.path.join(ICI, "comparaison_a_trois_machine2_v1.log"),
         encoding="utf-8", errors="replace").read()
E = open(os.path.join(ICI, "erratum_seul_point_machine2_v1.log"),
         encoding="utf-8", errors="replace").read()

print("=" * 84)
print("RELECTURE DES NOMBRES DE MA NOTE (comparaison a trois)")
print("=" * 84)

print("\n[1] LES COMPTES DE LA COMPARAISON")
for lib, motif, cite in (
        ("856 feuilles communes", r"communes aux trois : 856", "856"),
        ("82 exposees", r"^      82 feuilles", "82"),
        ("77 == libm", r"== son LIBM   : 77 / 82", "77 / 82"),
        ("0 == noyau", r"== son NOYAU  : 0 / 82", "0 / 82"),
        ("5 ni l'un ni l'autre", r"ni l'un ni l'autre     : 5 / 82", "5 / 82"),
        ("774 non exposees", r"non exposees : 774", "774"),
        ("14 divergences residuelles", r"differe quand meme : 14", "14")):
    chk("au log : %s" % lib, re.search(motif, C, re.M) is not None)
    chk("  et cite dans ma note : %s" % cite, dit(cite))

print("\n[2] LES NEUF RATIOS, DES TROIS COTES")
lignes = re.findall(r"^      (\d\|[\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+(\S+)", C, re.M)
chk("les neuf cellules sont au log", len(lignes) == 9, "%d" % len(lignes))
chk("les neuf rendent 'LIBM'", all(x[4] == "LIBM" for x in lignes))
for cel, noy, lib, moi, _ in lignes:
    chk("%s : les trois valeurs citees" % cel,
        dit(noy) and dit(lib) and dit(moi))
chk("mon poste egale le libm aux neuf", all(x[2] == x[3] for x in lignes))

print("\n[3] LE CHAMP DE FORCES, LES TROIS EMPREINTES")
for h in ("0491b83e6893dbbf", "f150f2685187b9d2", "f7f8be507eb5e9cb"):
    chk("citee : %s" % h, h in C and dit(h))
chk("les trois sont distinctes",
    len({"0491b83e6893dbbf", "f150f2685187b9d2", "f7f8be507eb5e9cb"}) == 3)

print("\n[4] L'ERRATUM")
chk("le log de l'erratum MORD, et c'est voulu", "1 mordent" in E and dit("il DOIT mordre"))
chk("3 cellules different, dont 2 LUES",
    "3 cellules different, dont 2 LUES" in E and dit("Trois cellules sur neuf different"))
for cel, ec in (("4|1.73", "-2.30"), ("4|2.80", "+4.66"), ("7|1.73", "+10.96")):
    chk("%s : ecart %s cite" % (cel, ec), dit("%s (%s %%)" % ("`" + cel + "`", ec)))
chk("parmi les NON LUES, 7|1.73 est la seule qui differe",
    "7|1.73 est bien la seule qui differe" in E and dit("le seul point **NON LU** qui differe"))
chk("R_ELLE est classe NOYAU aux trois", E.count("classe NOYAU") >= 3
    and dit("classe NOYAU"))
chk("la ligne fautive du chk est citee telle quelle",
    dit("'c est le SEUL point non bit-reproductible de la campagne')  # jamais teste"))

print("\n[5] LES CANONS")


def emp(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8'))
                          .replace('\r\n', '\n').encode()).hexdigest()[:16]


L = os.path.join(RAC, "entrant_machine1_2026-09-12_reponse_globale", "lot")
chk("canon de son lot = ca5456d3b11df0be",
    emp(os.path.join(L, "MANIFEST_lot_machine1_reponse_globale_v1.txt"))
    == "ca5456d3b11df0be" and dit("ca5456d3b11df0be"))
env = r"C:\Users\bazil\Downloads\files (55).zip"
if os.path.exists(env):
    b = hashlib.sha256(open(env, 'rb').read()).hexdigest()[:16]
    chk("enveloppe 0664f712878e2f87", b == "0664f712878e2f87" and dit(b), b)
chk("la feuille de derivation est bien dans ce repertoire",
    os.path.exists(os.path.join(ICI, "derivation_fenetre_delta_machine2_v1.py"))
    and dit("sont pieces de ce\nlot"))

print("\n" + "=" * 84)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s  %s" % (q, d))
print("=" * 84)
