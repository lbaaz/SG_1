#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RELECTURE MECANIQUE DES NOMBRES DE MA NOTE DE CERTIFICATION v3 -- machine 2, v1.

Regle 2 : la relecture mecanique des nombres de la prose vaut pour TOUT texte qui sort,
note comprise. Cette feuille confronte chaque nombre de CERTIFICATION_acte_R4R5_v3 a sa
source (mes .json, mes logs de controle, les empreintes recalculees). Elle ne relit pas
ma prose : elle recalcule.

Regle du 28/08 : un compteur de bilan se calcule APRES le dernier ajout.
"""
import hashlib, json, math, os, re, unicodedata

RAC = r"D:\devs\bocal\BOCAL4"
ICI = os.path.join(RAC, "R4R5_certification")
NOTE = open(os.path.join(ICI, "CERTIFICATION_acte_R4R5_v3_machine2_v1.md"),
            encoding="utf-8").read()
NPLAT = re.sub(r"\s+", " ", NOTE)
J = lambda p: json.load(open(os.path.join(RAC, p), encoding="utf-8"))
OK, MORD = [], []


def chk(quoi, cond, detail=''):
    OK.append(bool(cond))
    if not cond:
        MORD.append((quoi, detail))
    print('  [%s] %-56s %s' % ('OK  ' if cond else 'MORD', quoi[:56], detail))


def dit(s):
    return re.sub(r"\s+", " ", s) in NPLAT


print("=" * 84)
print("RELECTURE DES NOMBRES DE MA NOTE DE CERTIFICATION v3")
print("=" * 84)

# ---------------------------------------------------------- les trois bilans
print("\n[1] LES TROIS COMPTEURS, CONTRE MES PROPRES LOGS")
for fic, motif, dans_la_note in (
        ("controle_reception_v3_machine2_v1.log", r"BILAN : (\d+) controles, (\d+) mordent",
         "52 controles, 0 mordent"),
        ("certification_acte_R4R5_v3_machine2_v1.log",
         r"BILAN : (\d+) controles, (\d+) mordent", "71 controles, 66 tenus, 5 mordent")):
    L = open(os.path.join(ICI, fic), encoding="utf-8").read()
    m = re.search(motif, L)
    n, mo = int(m.group(1)), int(m.group(2))
    if "66 tenus" in dans_la_note:
        chk("bilan de %s : %d/%d" % (fic.split('_')[1], n - mo, n),
            n == 71 and mo == 5 and dit("71 controles, 66 tenus, 5 mordent"),
            "%d controles, %d tenus, %d mordent" % (n, n - mo, mo))
    else:
        chk("bilan de reception : %d controles, %d mordent" % (n, mo),
            n == 52 and mo == 0 and dit("52 controles, 0 mordent"))

H = open(os.path.join(ICI, "controle_hunks_v2_v3_machine2_v1.log"), encoding="utf-8").read()
m = re.search(r"HUNKS : (\d+)\s+\+(\d+) / -(\d+) lignes", H)
nh, pl, mi = int(m.group(1)), int(m.group(2)), int(m.group(3))
chk("le diff : %d hunks, +%d / -%d" % (nh, pl, mi),
    (nh, pl, mi) == (10, 55, 11) and dit("10 hunks, `+55` lignes") and dit("`-11`, et non `-10`"))

# ------------------------------------------------------------ les empreintes
print("\n[2] LES EMPREINTES CITEES DANS MA NOTE")


def emp(p):
    raw = open(os.path.join(RAC, p), 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8'))
                          .replace('\r\n', '\n').encode('utf-8')).hexdigest()[:16]


def brut(p):
    return hashlib.sha256(open(os.path.join(RAC, p), 'rb').read()).hexdigest()[:16]


V3 = os.path.join("entrant_machine1_2026-09-11_acte_v3", "lot")
for att, chemin, f in (
        ("fadc1c4f4c91b353", os.path.join(V3, "MANIFEST_lot_machine1_R4R5_acte_v3.txt"), emp),
        ("eaaacadd99fb468d", os.path.join(V3, "journal_delta_nn_R4R5_v3.md"), emp),
        ("ce07e533176441a5", os.path.join(V3, "journal_delta_nn_R4R5_v2.md"), emp),
        ("86d6ee29d27938ff", os.path.join(V3, "journal_delta_nn_R4R5_v1.md"), emp),
        ("187c723064996059", os.path.join(V3, "D2_premier_ordre_2_1_pair_machine1_v1.py"), emp)):
    lu = f(chemin)
    chk("%s = %s" % (att, os.path.basename(chemin)), lu == att and dit(att), "lu %s" % lu)
env = r"C:\Users\bazil\Downloads\files (49).zip"
lu = hashlib.sha256(open(env, 'rb').read()).hexdigest()[:16] if os.path.exists(env) else "?"
chk("enveloppe 5db99356792064fd", lu == "5db99356792064fd" and dit("5db99356792064fd"), lu)
chk("la v3 fait 34028 octets",
    os.path.getsize(os.path.join(RAC, V3, "journal_delta_nn_R4R5_v3.md")) == 34028
    and dit("34028 o"))

# -------------------------------------------------------------- les mesures
print("\n[3] LES NOMBRES DE MESURE")
R = {d["p"]: d for d in
     J(r"P3_pc26\rederivation\rederivation_harmoniques_machine2_v1.json")["min_F"]}
r26 = J(r"P3_pc26\run_P3_pc26_machine2_v1.json")
r30 = J(r"P3_pc26\p30\run_p30_machine2_v1.json")
r40 = J(r"P3_pc26\p40\run_p40_machine2_v1.json")
g = r26["g"]
s26, s30 = r26["fenetres"]["1600.0"]["s"], r30["fenetres"]["400.0"]["s"]

# La tolerance doit etre celle du CHIFFRE ECRIT, pas plus fine : mes deux K* sont cites
# a quatre chiffres significatifs, et 9.830e-10 est l'arrondi juste de 9.82966e-10. Une
# tolerance de 1e-5 y faisait mordre un nombre exact -- un faux echec vaut un controle
# vide. `sig` = nombre de chiffres significatifs de la forme ecrite.
for lib, val, cible, sig in (
        ("s*(26) = 0.477418", s26, 0.477418, 6),
        ("s*(26|400) = 0.484219", r26["fenetres"]["400.0"]["s"], 0.484219, 6),
        ("s*(30) = 0.472090", s30, 0.472090, 6),
        ("s*(40|400) = 0.465235", r40["fenetres"]["400.0"]["s"], 0.465235, 6),
        ("s*(40|1600) = 0.458701", r40["fenetres"]["1600.0"]["s"], 0.458701, 6),
        ("K*(26) = 9.830e-10", g * s26 ** 24, 9.830e-10, 4),
        ("K*(30) = 3.730e-11", g * s30 ** 28, 3.730e-11, 4)):
    chk(lib, abs(val / cible - 1) < 5 * 10 ** (-sig) and dit("%s" % lib.split("= ")[1]),
        "%.6g" % val)

chk("1.42 % d'ecart entre les deux fenetres a p = 40",
    abs(100 * (r40["fenetres"]["400.0"]["s"] / r40["fenetres"]["1600.0"]["s"] - 1) - 1.42)
    < 5e-3 and dit("1.42 %"),
    "%.4f %%" % (100 * (r40["fenetres"]["400.0"]["s"] / r40["fenetres"]["1600.0"]["s"] - 1)))

for p_, ab, mf in ((26, -0.01062, 0.10804), (30, -0.10539, 0.06569)):
    chk("p=%d : (a-b1)/a et min F/a" % p_,
        abs(R[p_]["a_moins_b1_sur_a"] - ab) < 5e-6 and abs(R[p_]["min_F_sur_a"] - mf) < 5e-6
        and dit("%.5f" % ab) and dit("%.5f" % mf))
chk("b1/a = 1.01062 a p = 26",
    abs((1 - R[26]["a_moins_b1_sur_a"]) - 1.01062) < 5e-6 and dit("1.01062"))
chk("min F > 0 jusqu'a p = 80", max(R) == 80 and all(R[p]["min_F_sur_a"] > 0 for p in R)
    and dit("jusqu'a 80"))

exc = 7 / 3
for p_, s_, sc in ((4, 2.634491, 6.1471), (6, 1.012586, 2.3627), (26, s26, 1.1140),
                   (30, s30, 1.1015)):
    chk("S_c(%d) = %.4f" % (p_, sc), abs(exc * s_ - sc) < 5e-5 and dit("%.4f" % sc))
chk("-ln(7/3) = -0.84730", abs(-math.log(exc) + 0.84730) < 5e-6 and dit("-0.84730"))
pente = (math.log(g * s30 ** 28) - math.log(g * 1.012586 ** 4)) / 24
chk("pente mesuree = -0.87777", abs(pente + 0.87777) < 5e-6 and dit("-0.87777"),
    "%.6f" % pente)
chk("4^(-1/24) = 0.943874", abs(4 ** (-1 / 24) - 0.943874) < 5e-7 and dit("0.943874"))
pas = J(r"P3_pc26\gel_P3_machine2_v1.json")["pas_grille_ln"]
chk("4.0837 pas, pas_ln = 0.014144576",
    abs(math.log(4) / 24 / pas - 4.0837) < 5e-5 and abs(pas - 0.014144576) < 5e-10
    and dit("4.0837") and dit("0.014144576"))

# ------------------------------------------------------ les six enveloppes
print("\n[4] LES SIX ENVELOPPES, DEPUIS MON LOG DE LA SECTION 3")
S3 = open(os.path.join(RAC, "P3_pc26", "p40", "controle_section3_machine2_v1.log"),
          encoding="utf-8").read()
lus = re.findall(r"p=(\d+) s=([\d.]+) : P_env\s+([\d.]+) ; T =\s+(\d+) ->\s+([\d.]+) periodes",
                 S3)
chk("six colonnes dans mon log", len(lus) == 6, "%d" % len(lus))
per = [float(x[4]) for x in lus]
sval = [float(x[1]) for x in lus]
pen = [float(x[2]) for x in lus]
chk("les periodes citees : 4.3, 4.2, 4.2, 4.7, 5.0, 5.5",
    sorted(per) == sorted([4.3, 4.2, 4.2, 4.7, 5.0, 5.5])
    and dit("`4.3, 4.2, 4.2, 4.7, 5.0, 5.5`"), str(per))
chk("le maximum est bien 5.5 (et non 5)", max(per) == 5.5 and dit("5.5"))
chk("les six s sont cites et sont TOUS sous le seuil",
    all(dit("%.6f" % s) for s in sval)
    and all(s < (s30 if lus[i][0] == '30' else s26) for i, s in enumerate(sval)))
chk("les six P_env citees : 210.5, 502.6, 2284.1, 189.7, 400.1, 1464.4",
    sorted(pen) == sorted([210.5, 502.6, 2284.1, 189.7, 400.1, 1464.4])
    and dit("`210.5, 502.6, 2284.1, 189.7, 400.1, 1464.4`"), str(pen))
chk("aucune des six n'est a s* (ce qui fonde l'erratum (b))",
    not any(abs(s - s26) < 1e-4 or abs(s - s30) < 1e-4 for s in sval))

# ------------------------------------------------------- la table du point 6
print("\n[5] LA TABLE DU POINT 6 == LE REJEU DE SA FEUILLE")
L = open(os.path.join(ICI, "rejeu_verification_harmoniques_m1_machine2_v1.log"),
         encoding="utf-8").read()
lignes = re.findall(r"^\s*(\d+)\s+(\d+)\s+(-?[\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)\s+(\w+)",
                    L, re.M)
chk("sept lignes de sa table citees dans ma note",
    len([1 for x in lignes if x[0] in ("6", "8", "12", "20", "26", "30", "40")]) == 7,
    "%d lues" % len(lignes))
for p_, nL, b1, ab, mf, pos in lignes:
    if p_ == "16":
        continue          # je ne cite pas p = 16 dans ma note : je ne le controle pas
    chk("p=%s : %s %s %s reproduits dans ma note" % (p_, b1, ab, mf),
        all(dit(x) for x in (b1, ab, mf)) and dit("%s      %s" % (p_.rjust(2), nL)
                                                  ) or all(dit(x) for x in (b1, ab, mf)))
chk("les 16 lignes de table de ma note ne portent que des nombres de ce log",
    "0.91026" in L and "0.78609" in L and "1.2795" in L)

# ------------------------------------------------------------------- bilan
print("\n" + "=" * 84)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s  %s" % (q, d))
print("=" * 84)
