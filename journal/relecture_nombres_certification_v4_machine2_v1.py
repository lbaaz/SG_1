#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RELECTURE MECANIQUE DES NOMBRES DE MA NOTE v4 -- machine 2, v1, 12/09/2026.

Regle 2 : elle vaut pour TOUT texte qui sort, note comprise. Et la regle neuve du jour :
un intervalle ne se lit pas sur une liste, il se calcule -- y compris les MIENS. Chaque
borne citee dans ma note est donc recalculee par min/max sur la structure, jamais reprise
de ma prose.

La tolerance de chaque controle est celle du CHIFFRE ECRIT, pas plus fine (regle 17).
"""
import hashlib, json, os, re, unicodedata

RAC = r"D:\devs\bocal\BOCAL4"
ICI = os.path.join(RAC, "R4R5_certification")
NOTE = open(os.path.join(ICI, "CERTIFICATION_acte_R4R5_v4_machine2_v1.md"),
            encoding="utf-8").read()
NPLAT = re.sub(r"\s+", " ", NOTE)
OK, MORD = [], []


def chk(quoi, cond, detail=''):
    OK.append(bool(cond))
    if not cond:
        MORD.append((quoi, detail))
    print('  [%s] %-54s %s' % ('OK  ' if cond else 'MORD', quoi[:54], detail))


def dit(s):
    return re.sub(r"\s+", " ", s) in NPLAT


def emp(p):
    raw = open(os.path.join(RAC, p), 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8'))
                          .replace('\r\n', '\n').encode()).hexdigest()[:16], len(raw)


print("=" * 84)
print("RELECTURE DES NOMBRES DE MA NOTE v4")
print("=" * 84)

print("\n[1] LES COMPTEURS, CONTRE MES LOGS")
L = open(os.path.join(ICI, "certification_acte_R4R5_v4_et_depot_machine2_v1.log"),
         encoding="utf-8").read()
m = re.search(r"BILAN : (\d+) controles, (\d+) mordent", L)
n, mo = int(m.group(1)), int(m.group(2))
chk("33 controles, 32 tenus, 1 mord",
    (n, mo) == (33, 1) and dit("**33 controles, 32 tenus, 1 mord.**"),
    "%d / %d tenus / %d mord" % (n, n - mo, mo))
H = open(os.path.join(ICI, "controle_hunks_v3_v4_machine2_v1.log"), encoding="utf-8").read()
chk("6 hunks, +17 / -7, et -6 par prefixe",
    "6 hunks, +17 / -7" in H and "-6" in H and dit("6 hunks, +17 / -7")
    and dit("il rend **-6**"))
E = open(os.path.join(ICI, "controle_cause_du_moins_dix_machine2_v1.log"),
         encoding="utf-8").read()
chk("l'erratum : 10 par prefixe, 11 par position",
    "par PREFIXE    : 10" in E and "par POSITION   : 11" in E
    and dit("suppressions comptees par PREFIXE  : 10")
    and dit("suppressions comptees par POSITION : 11"))

print("\n[2] LES SIX COLONNES : TOUTE BORNE EST CALCULEE, JAMAIS LUE")
S3 = open(os.path.join(RAC, "P3_pc26", "p40", "controle_section3_machine2_v1.log"),
          encoding="utf-8").read()
six = re.findall(r"p=(\d+) s=([\d.]+) : P_env\s+([\d.]+) ; T =\s+(\d+) ->\s+([\d.]+) per",
                 S3)
chk("six colonnes", len(six) == 6, "%d" % len(six))
sv = [float(x[1]) for x in six]
pe = [float(x[2]) for x in six]
pr = [float(x[4]) for x in six]
chk("borne basse de P_env = min(mesures) = 189.7",
    abs(min(pe) - 189.7) < 0.05 and dit("La borne basse est `189.7`"), "%.1f" % min(pe))
chk("borne haute de P_env = max(mesures) = 2284.1",
    abs(max(pe) - 2284.1) < 0.05 and dit("189.7 a 2284.1"), "%.1f" % max(pe))
chk("210.5 est bien le PREMIER de ma liste, pas le minimum",
    pe[0] == 210.5 and min(pe) != 210.5 and dit("**`210.5` est le PREMIER de ma liste"))
chk("2284.1 est le troisieme ET le maximum (ma note le dit)",
    pe[2] == max(pe) and dit("elle est le troisieme de la liste"))
chk("periodes : min 4.2, max 5.5",
    (min(pr), max(pr)) == (4.2, 5.5) and dit("mon minimum est 4.2 et mon\nmaximum 5.5"))
chk("s : 0.424881 a 0.467870, cites",
    abs(min(sv) - 0.424881) < 5e-7 and abs(max(sv) - 0.467870) < 5e-7
    and dit("`0.424881` a `0.467870`"))
chk("les six sont sous s*(30) = 0.472090",
    max(sv) < 0.472090 and dit("sous `s*(30) = 0.472090`"))
chk("le tableau des six lignes de ma note est celui du log",
    all(dit("%.6f" % s) for s in sv) and all(dit("%.1f" % p) for p in pe)
    and all(dit("%.1f" % r) for r in pr))
chk("la ligne marquee 'borne basse' est bien celle de 189.7",
    re.search(r"26\s+0\.467870\s+189\.7\s+4\.7\s+<-- la borne basse", NOTE) is not None)

print("\n[3] LES EMPREINTES ET LES TAILLES")
V4 = os.path.join("entrant_machine1_2026-09-12_acte_v4")
for att, chemin in (
        ("d467a239c3555737", os.path.join(V4, "lot", "journal_delta_nn_R4R5_v4.md")),
        ("7b4918f7837511dd", os.path.join(V4, "lot",
                                          "MANIFEST_lot_machine1_R4R5_acte_v4.txt"))):
    lu, o = emp(chemin)
    chk("%s = %s" % (att, os.path.basename(chemin)), lu == att and dit(att), "lu %s" % lu)
lu, o = emp(os.path.join(V4, "lot", "journal_delta_nn_R4R5_v4.md"))
chk("34728 octets", o == 34728 and dit("34728 o"), "%d" % o)
env = r"C:\Users\bazil\Downloads\files (50).zip"
if os.path.exists(env):
    b = hashlib.sha256(open(env, 'rb').read()).hexdigest()[:16]
    chk("enveloppe e44aa27c81335eb1", b == "e44aa27c81335eb1" and dit("e44aa27c81335eb1"), b)

print("\n[4] LES COMPTES DE PIECES ET LE DEPOT")
LOG = L
chk("22 pieces, 20 au bit, 2 neuves",
    "22 pieces annoncees et extraites" in LOG and "inchangees : 20" in LOG
    and dit("22 pieces") and dit("20 sont AU BIT") and dit("2 neuves"))
acte = open(os.path.join(RAC, V4, "lot", "journal_delta_nn_R4R5_v4.md"), 'rb').read()
dep = open(os.path.join(RAC, V4, "depot", "journal_delta_89_R4R5_v4.md"), 'rb').read()
chk("la piece de depot : 34728 octets, ZERO different",
    acte == dep and len(dep) == 34728 and dit("34728 octets, ZERO different"))
nn = len(re.findall(r"nn\.\d+|delta_nn", dep.decode('utf-8')))
nn2 = len(re.findall(r"nn\.\d+|delta_nn",
                     open(os.path.join(RAC, "entrant_machine1_2026-09-11_depot_89_v2",
                                       "lot", "journal_delta_89_R4R5_v2.md"),
                          encoding="utf-8").read()))
chk("18 reperes 'nn', et c'est le compte de la v2 deposee",
    nn == nn2 == 18 and dit("garde **18** reperes"), "%d et %d" % (nn, nn2))
chk("plus longue ligne hors table = 97 caracteres",
    "plus longue ligne hors table : 97 car." in LOG and dit("97 caracteres"))
chk("table localisee l. 294-304", "l. 294-304" in LOG and dit("l. 294-304"))
chk("23 mots contre 23 dans H10", "23 mots ; v4 : 23 mots" in LOG and dit("23 mots contre 23"))

print("\n" + "=" * 84)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s  %s" % (q, d))
print("=" * 84)
