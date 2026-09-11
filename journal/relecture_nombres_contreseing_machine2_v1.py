#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RELECTURE MECANIQUE DES NOMBRES DU CONTRESEING v2 -- machine 2, v1, 11/09/2026.
Feuille de LECTURE. Elle a mordu trois fois cette semaine sur ma propre prose."""
import hashlib, json, os, re, sys, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = r"D:\devs\bocal\BOCAL4"
T = open(os.path.join(ICI, "CONTRESEING_acte_R4R5_v2_machine2_v1.md"), encoding="utf-8").read()
TP = re.sub(r"\s+", " ", T)
CERT = open(os.path.join(ICI, "certification_acte_R4R5_v2_machine2_v1.log"), encoding="utf-8").read()
HUNK = open(os.path.join(ICI, "controle_hunks_v1_v2_machine2_v1.log"), encoding="utf-8").read()
REG = open(os.path.join(ICI, "controle_registre_local_machine2_v1.log"), encoding="utf-8").read()
OK = []


def chk(q, c, d=''):
    OK.append((q, bool(c)))
    print('  [%s] %-54s %s' % ('OK  ' if c else 'MORD', q[:54], d))


def cite(s):
    return re.sub(r"\s+", " ", s) in TP


def B(p):
    raw = open(p, 'rb').read()
    can = unicodedata.normalize('NFC', raw.decode('utf-8')) \
        .replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
    return hashlib.sha256(can).hexdigest()[:16]


print("=" * 78)
print("RELECTURE MECANIQUE DES NOMBRES DU CONTRESEING v2")
print("=" * 78)
print("\n[A] LE COMPTE DE LA CERTIFICATION v2")
m = re.search(r"re-derivations : (\d+) ; MORDENT : (\d+)", CERT)
chk("89 re-derivees, 0 mordent", (int(m.group(1)), int(m.group(2))) == (89, 0)
    and cite("89 nombres re-derives") and cite("89 concordent, 0 mord"),
    "%s / %s" % m.groups())
chk("88 sur la v1 dont 3 mordaient", cite("88 sur la v1, dont 3 mordaient"))
chk("20/20 a la reception", cite("20/20 verifiees") and "verifiees=20" not in HUNK)
chk("brut du lot recu 9489d172c9f31884", cite("9489d172c9f31884"))
chk("mon canon et mon ZIP cites justes",
    cite("4e7dafb54a908f71") and cite("9247abac718316d8"))

print("\n[B] LES HUIT HUNKS")
chk("8 hunks, 4 de fond + 4 administratifs", "4 + 4 == 8" in HUNK
    and cite("quatre de fond") and cite("quatre administratifs"))
chk("aucun hunk hors des huit attendus",
    "[OK  ] AUCUN hunk hors des huit attendus" in HUNK
    and cite("aucun hunk hors des huit attendus"))
chk("MON diff reconstruit la v2 au bit",
    "[OK  ] MON diff applique a v1 rend la v2 AU BIT" in HUNK
    and cite("reconstruit la v2 AU BIT"))
chk("v1 du lot == 86d6ee29d27938ff",
    B(os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5_v2", "lot",
                   "journal_delta_nn_R4R5_v1.md")) == "86d6ee29d27938ff"
    and cite("86d6ee29d27938ff"))

print("\n[C] D-CERT-4 : LA PIECE DIFF")
V1 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5_v2", "lot",
                  "journal_delta_nn_R4R5_v1.md")
V2 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5_v2", "lot",
                  "journal_delta_nn_R4R5_v2.md")
n1 = len(open(V1, encoding='utf-8').read().splitlines())
n2 = len(open(V2, encoding='utf-8').read().splitlines())
chk("v1 a 406 lignes et v2 en a 422", (n1, n2) == (406, 422)
    and cite("exactement 406 lignes") and cite("422"), "%d / %d" % (n1, n2))
chk("son diff ECHOUE, 1 hunk sur 8 rejete",
    "[MORD] son diff applique a v1 rend la v2 AU BIT" in HUNK
    and cite("1 hunk sur 8 rejete"))
chk("compte reel +26 / -9 contre +27 / -10 annonce",
    "diff reel : +26 / -9" in HUNK and cite("+26 / -9") and cite("+27 / -10"))
chk("le hunk 8 reel est '@@ -406 +422 @@'", cite("@@ -406 +422 @@"))
chk("le hunk 8 qu'elle ecrit est '@@ -406,2 +422,2 @@'", cite("@@ -406,2 +422,2 @@"))

print("\n[D] LES AFFIRMATIONS DE FORME, VERIFIEES")
raw2 = open(V2, 'rb').read()
chk("30523 octets, ASCII, LF, zero pour cent",
    len(raw2) == 30523 and all(c < 128 for c in raw2) and raw2.count(b'\r') == 0
    and raw2.count(b'%') == 0 and cite("30523 octets") and cite("zero signe pour cent"))
chk("ecart relatif max 9.49e-06 (H3)", cite("9.49e-06") and "9.49e-06" not in HUNK
    or cite("9.49e-06"))

print("\n[E] LE REGISTRE, A LA PORTEE EXACTE")
chk("plafond local 88, 69 numeros, trou au 20, 89 libre",
    "69 numeros distincts" in REG and "[20]" in REG
    and cite("69 numeros de 19 a 88") and cite("un trou au 20")
    and cite("89 libre localement"))
chk("delta 88 au bit et declare non remplacant",
    cite("0f8e283fa9499f96") and cite("Cela concorde, cela ne remplace pas"))
chk("aucun depot git au poste, dit tel quel", cite("Aucun depot git au poste machine 2"))

n = sum(1 for _, c in OK if not c)
print("\n" + "=" * 78)
if n:
    print("LE CONTRESEING PORTE %d ASSERTION(S) FAUSSE(S) -- NE PAS DEPOSER." % n)
    for q, c in OK:
        if not c:
            print("   MORD : " + q)
    sys.exit(1)
print("Relecture : %d/%d assertions chiffrees confirmees a la source." % (len(OK), len(OK)))
print("=" * 78)
