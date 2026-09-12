#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RELECTURE MECANIQUE DES NOMBRES DE MA REPONSE GLOBALE -- machine 2, v1, 12/09/2026.

Chaque nombre est relu dans une SORTIE ou recalcule, jamais dans ma prose. Les bornes et
les pourcentages viennent des logs qui les ont produits.
"""
import hashlib, json, os, re, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
N = open(os.path.join(ICI, "POUR_MACHINE1_reponse_globale_machine2_v1.md"),
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


def lire(f):
    return open(os.path.join(ICI, f), encoding="utf-8", errors="replace").read()


def emp(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8'))
                          .replace('\r\n', '\n').encode()).hexdigest()[:16]


print("=" * 88)
print("RELECTURE DES NOMBRES DE MA REPONSE GLOBALE")
print("=" * 88)

print("\n[1] LE TEMOIN ET LES TROIS ufuncs")
T = lire("temoin_arrondi_BOCAL4_machine2_v1.log")
chk("le temoin rend ...9c6 par le tableau ET par Python",
    T.count("0x1.a483018a169c6p+64") >= 3 and dit("0x1.a483018a169c6p+64"))
chk("son noyau est cite a ...9c5", dit("0x1.a483018a169c5p+64"))
tab = dict(re.findall(r"(x \*\* 6|exp|arctan2)\s+non CR :\s+\d+ / \d+\s+\(([\d.]+) pour cent\)", T))
chk("les trois pourcentages de ma table sont ceux du log",
    all(dit(v) for v in tab.values()), str(tab))
chk("et les trois sont sous 0.5 pour cent",
    all(float(v) < 0.5 for v in tab.values()))
for v in ("4.92", "4.56", "5.92"):
    chk("sa colonne avec noyau : %s citee" % v, dit(v))

print("\n[2] LES DEUX MODES DU v2")
A = lire("diagnostic_v2_contre_json_m1_machine2.log")
B = lire("diagnostic_v2_contre_mon_rejeu_machine2.log")
chk("contre SON JSON : verdict CAUSE CHEZ L'AUTRE",
    "CAUSE CHEZ L'AUTRE" in A and dit("CAUSE CHEZ L'AUTRE"))
chk("contre MON rejeu : verdict COMPARAISON DEGENEREE",
    "COMPARAISON DEGENEREE" in B and dit("COMPARAISON DEGENEREE"))
chk("le motif [F,F,F,T] est bien celui du log",
    "[False, False, False, True]" in A and dit("[F,F,F,T]"))
chk("et les flots differents sont [0, 1, 2]",
    "[0, 1, 2]" in A and dit("[0,1,2]"))
chk("le temoin est porte par la ligne PLATEFORME des deux runs",
    A.count("TEMOIN") >= 1 and B.count("TEMOIN") >= 1)

print("\n[3] LA TENAILLE")
L = lire("lecture_tenaille_apres_correction_machine2_v1.log")
m = re.search(r"BILAN : (\d+) controles, (\d+) mordent", L)
chk("12 controles, 0 mordent", (int(m.group(1)), int(m.group(2))) == (12, 0),
    m.group(0))
chk("INF = max(borne(R_MOI, True).values()) est cite tel quel",
    "INF = max(borne(R_MOI, True).values())" in L
    and dit("INF = max(borne(R_MOI, True).values())"))
for val in ("1.286644e-05", "1.427723e-05", "1.659726e-05"):
    chk("borne citee : %s" % val, val in L and dit(val))
chk("les quatre lignes de R_ELLE sont citees (42, 89, 100, 119)",
    all(("l.%d" % n) in L for n in (42, 89, 100, 119))
    and all(dit("l.%d" % n) for n in (42, 89, 100, 119)))
chk("la carte : m=2 kT=1 rend x1.0415", "x1.0415" in L and dit("x1.0415"))
chk("le plateau 1.26-1.46 dans b = 1.15-1.74", dit("1.26-1.46") and dit("1.15-1.74"))
chk("la fenetre vaut 4 pour cent et l'ecart 11 pour cent",
    dit("soit 4 %") and dit("11,0 %"))

print("\n[4] LA SURFACE")
S = lire("surface_exposition_registre_machine2_v1.log")
for lib, motif in (("34 .log deposes", r"\.log deposes au registre\s+: 34"),
                   ("1 nomme numpy", r"version de numpy\s+: 1"),
                   ("0 nomment python", r"version de python\s+: 0"),
                   ("0 nomment un dispatch", r"niveau de dispatch\s+: 0"),
                   ("91 scripts", r"scripts \.py deposes\s+: 91"),
                   ("27 de sa plume", r"de plume machine 1\s+: 27"),
                   ("49 sans plume", r"sans plume au nom\s+: 49"),
                   ("m1 3 chargent le moteur", r"LE MOTEUR : m1 3")):
    chk("au log : %s" % lib, re.search(motif, S) is not None)
for v in ("34", "91", "27", "49", "6.4e13", "1.41e-2", "5.9e7"):
    chk("cite dans ma note : %s" % v, dit(v))
chk("les trois versions du banc sont nommees",
    dit("banc_qualification_machine1_v1/v2/v3"))

print("\n[5] LES EMPREINTES ET LES CANONS")
LOTC = os.path.join(RAC, "entrant_machine1_2026-09-12_reponse_cas_durs", "lot")
chk("canon de son lot = 5ea2fa8d7457a125",
    emp(os.path.join(LOTC, "MANIFEST_lot_machine1_reponse_cas_durs_BOCAL4_v1.txt"))
    == "5ea2fa8d7457a125" and dit("5ea2fa8d7457a125"))
env = r"C:\Users\bazil\Downloads\files (54).zip"
if os.path.exists(env):
    b = hashlib.sha256(open(env, 'rb').read()).hexdigest()[:16]
    chk("enveloppe 4543b199330a4fb7", b == "4543b199330a4fb7" and dit(b), b)
for h, chemin in (
        ("d5ace962a3a6e413", os.path.join(RAC, "entrant_machine1_2026-09-09_constante_A_v5",
                                          "MANIFEST_lot_machine1_constante_A_v5.txt")),
        ("13d2973b0e143a20", os.path.join(
            RAC, "certification_constante_A_v5",
            "MANIFEST_lot_machine2_certification_constante_A_v5_v1.txt"))):
    chk("%s est AU POSTE, comme je l'ecris" % h,
        os.path.exists(chemin) and emp(chemin) == h and dit(h),
        "lu %s" % (emp(chemin) if os.path.exists(chemin) else "ABSENT"))
for h in ("a4c35a2ee691c9a7", "ca9b3bb13a20e7c3", "c8d86e5e", "ed09e29e"):
    chk("cite : %s" % h, dit(h))

print("\n[6] LA PAIRE INTERVERTIE DE SA SECTION 6, CITEE EXACTEMENT")
note = open(os.path.join(LOTC, "note_machine1_reponse_cas_durs_BOCAL4_v1.md"),
            encoding="utf-8").read()
plat = re.sub(r"\s+", " ", note)
chk("sa section 6 dit bien 'contre mon JSON c8d86e5e (attendu COMPARAISON DEGENEREE)'",
    "le v2 contre mon JSON c8d86e5e (attendu : \"COMPARAISON DEGENEREE\"" in plat)
chk("or contre SON json mon poste rend CAUSE CHEZ L'AUTRE",
    "CAUSE CHEZ L'AUTRE" in A and "COMPARAISON DEGENEREE" not in A)
chk("et contre MON rejeu il rend COMPARAISON DEGENEREE",
    "COMPARAISON DEGENEREE" in B)

print("\n" + "=" * 88)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s  %s" % (q, d))
print("=" * 88)
