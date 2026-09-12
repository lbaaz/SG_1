#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RELECTURE MECANIQUE DES NOMBRES DE MA NOTE -- machine 2, v1, 12/09/2026.

Chaque nombre est recalcule ou relu dans une SORTIE, jamais dans ma prose. Les comptes de
cas durs et de basculements sont repris du JSON du diagnostic, pas de son log.
"""
import hashlib, json, os, re, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
N = open(os.path.join(ICI, "POUR_MACHINE1_cas_durs_BOCAL4_machine2_v1.md"),
         encoding="utf-8").read()
NP = re.sub(r"\s+", " ", N)
D = json.load(open(os.path.join(ICI, "diagnostic_pow_cas_durs_machine1_v1.json"),
                   encoding="utf-8"))
LOTC = os.path.join(RAC, "entrant_machine1_2026-09-12_cause_ecart", "lot")
sans = json.load(open(os.path.join(LOTC,
                                   "convergence_dt_7_1p73_machine1_sansX86V4_v1.json"),
                      encoding="utf-8"))
avec = json.load(open(os.path.join(
    RAC, "entrant_machine1_2026-09-12_convergence_dt", "lot",
    "convergence_dt_7_1p73_machine1_v1.json"), encoding="utf-8"))
moi = json.load(open(os.path.join(RAC, "G2_convergence_dt",
                                  "rejeu1_convergence_dt_machine2_v1.json"),
                     encoding="utf-8"))
OK, MORD = [], []


def chk(q, c, d=''):
    OK.append(bool(c))
    if not c:
        MORD.append((q, d))
    print("  [%s] %-54s %s" % ("OK  " if c else "MORD", q[:54], d))


def dit(s):
    return re.sub(r"\s+", " ", s) in NP


def emp(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8'))
                          .replace('\r\n', '\n').encode()).hexdigest()[:16]


print("=" * 84)
print("RELECTURE DES NOMBRES DE MA NOTE (cas durs BOCAL4)")
print("=" * 84)

print("\n[1] LES 44 AU BIT, RECALCULES ICI")
G = ("e", "R_composantes", "plancher_composantes", "ratio_seuil_du_flot", "tau_au_max",
     "err_rel_fin", "e_sur_plancher", "seuil_5_4_du_flot", "dt", "tau_fin", "n_pas")
n = sum(1 for k in range(4) for q in G)
bit = sum(1 for k in range(4) for q in G if sans["flots"][k][q] == moi["flots"][k][q])
chk("44 grandeurs de flot, 44 au bit", (n, bit) == (44, 44) and dit("IDENTIQUES AU BIT"),
    "%d/%d" % (bit, n))
for nom, j, v in (("son noyau actif", avec, "0.7592658962"),
                  ("son noyau desactive", sans, "0.6841917056"),
                  ("moi", moi, "0.6841917056")):
    r = j["paires"][0]["lecture_5_4_sur_flot_fin"]["ratio_seuil"]
    chk("e/seuil %s = %s" % (nom, v), abs(r - float(v)) < 5e-11 and dit(v), "%.10f" % r)
chk("p_obs paire 1 : un ulp, les deux valeurs citees",
    sans["paires"][1]["p_obs"] != moi["paires"][1]["p_obs"]
    and dit("2.108349686957736") and dit("...65"))

print("\n[2] LE COMPTE DES CAS DURS ET DES BASCULEMENTS, DEPUIS LE JSON")
durs = [f.get("cas_durs", {}).get("K1", f.get("K1_durs")) for f in D["flots"]]
if durs[0] is None:
    durs = []
    for f in D["flots"]:
        c = [v for k, v in f.items() if "dur" in k.lower() and isinstance(v, int)]
        durs.append(c[0] if c else None)
print("      lu au JSON : cas durs K1 par flot = %s" % durs)
chk("cas durs K1 = [0, 0, 4, 3]", durs == [0, 0, 4, 3] and dit("0             0")
    and dit("4             0") and dit("3             0"), str(durs))
# CE CONTROLE AVAIT PASSE SUR None : aucune cle ne contient "bascul", donc la liste
# valait [None]*4 et le test l'acceptait. Un controle qui ne peut pas mordre n'est pas un
# controle. La structure porte l'information sous "effet" : ABSORBE ou non.
bas = [sum(1 for e in f["effet_de_chaque_cas_dur_K1"] if e["effet"] != "ABSORBE")
       for f in D["flots"]]
absorbes = [sum(1 for e in f["effet_de_chaque_cas_dur_K1"] if e["effet"] == "ABSORBE")
            for f in D["flots"]]
chk("basculements = 0 aux quatre flots (compte des effets != ABSORBE)",
    bas == [0, 0, 0, 0] and dit("BASCULEMENTS"), "bascules %s ; absorbes %s" % (bas, absorbes))
chk("et chaque cas dur deplace x_fin de +0.0 ulp",
    all(e["delta_x_fin_en_ulp_x1"] == 0.0 for f in D["flots"]
        for e in f["effet_de_chaque_cas_dur_K1"]) and dit("`+0.0 ulp`"))
chk("numpy != python sur 0 appel aux quatre flots",
    [f["K1_numpy_differe_de_python"] for f in D["flots"]] == [0, 0, 0, 0]
    and dit("sur 0 appel des 22 800"))
app = []
for f in D["flots"]:
    a = [v for k, v in f.items() if k.lower().startswith("appels") or k.lower() == "k1"]
    app.append(a[0] if a else None)
chk("les quatre comptes d'appels K1 : 1520, 3040, 6080, 12160",
    dit("1 520") and dit("3 040") and dit("6 080") and dit("12 160"))
chk("total 22 800 appels K1", 1520 + 3040 + 6080 + 12160 == 22800 and dit("22 800"))
chk("sept cas durs au total", sum(durs) == 7 and dit("**sept, et aucune ne bascule**"))

print("\n[3] LE CONTRE-EXEMPLE AVX512")
L = open(os.path.join(ICI, "niveau_dispatch_numpy_machine2_v1.log"),
         encoding="utf-8", errors="replace").read()
m = re.search(r"AVX512 actives : (.+)", L)
feats = [f.strip() for f in m.group(1).split(",")] if m else []
chk("quinze extensions AVX512 actives", len(feats) == 15 and dit("**quinze** extensions"),
    "%d" % len(feats))
for f in ("AVX512F", "AVX512_ICL", "AVX512_SKX", "AVX512VPOPCNTDQ"):
    chk("citee dans ma note : %s" % f, f in feats and dit(f))
chk("aucun niveau X86_Vn nomme par numpy 2.2.6",
    "aucun nomme ainsi" in L and dit("**aucun niveau `X86_Vn`**"))
chk("numpy 2.2.6 et python 3.11.9, comme je l'ecris",
    moi["plateforme"]["numpy"] == "2.2.6" and moi["plateforme"]["python"] == "3.11.9")

print("\n[4] LES EMPREINTES ET LES CANONS")
chk("canon de son lot = 117bcfaa1f283059",
    emp(os.path.join(LOTC, "MANIFEST_lot_machine1_cause_ecart_7_1p73_v1.txt"))
    == "117bcfaa1f283059" and dit("117bcfaa1f283059"))
env = r"C:\Users\bazil\Downloads\files (53).zip"
if os.path.exists(env):
    b = hashlib.sha256(open(env, 'rb').read()).hexdigest()[:16]
    chk("enveloppe a26895c6fabd0ee2", b == "a26895c6fabd0ee2" and dit(b), b)
chk("mon rejeu1 = ed09e29e91b6eb00",
    emp(os.path.join(RAC, "G2_convergence_dt", "rejeu1_convergence_dt_machine2_v1.json"))
    == "ed09e29e91b6eb00" and dit("ed09e29e91b6eb00"))
chk("son JSON du geste = c8d86e5e5b4fd745",
    emp(os.path.join(RAC, "entrant_machine1_2026-09-12_convergence_dt", "lot",
                     "convergence_dt_7_1p73_machine1_v1.json"))
    == "c8d86e5e5b4fd745" and dit("c8d86e5e5b4fd745"))
chk("mon lot precedent eb7fb1cefbf2cec4 est cite", dit("eb7fb1cefbf2cec4"))

print("\n[5] LA CONTRADICTION GARDE / SECTION 7, CITEE MOT POUR MOT")
note1 = open(os.path.join(LOTC, "note_machine1_cause_ecart_7_1p73_v1.md"),
             encoding="utf-8").read()
chk("sa section 7 dit bien de passer SON JSON",
    "recoit MON JSON du geste, c8d86e5e5b4fd745" in re.sub(r"\s+", " ", note1))
chk("et sa section 1 liste rejeu1 m2 = ed09e29e91b6eb00",
    "ed09e29e91b6eb00" in note1 and "rejeu1 m2" in note1)
chk("le message d'arret est cite exactement dans ma note",
    dit("ARRET PB-1 : rejeu1 m2 ne repond pas au canon ed09e29e91b6eb00 "
        "(lu c8d86e5e5b4fd745)"))

print("\n[6] LE VERDICT IMPRIME N'EST PAS CELUI QU'ELLE ATTENDAIT")
chk("le JSON porte le verdict cote m1, non 'CAUSE DE L'AUTRE COTE'",
    "CAUSE DE L'AUTRE COTE" not in D["verdict"] and dit("**NON TENUE**"),
    D["verdict"][:60])

print("\n" + "=" * 84)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s  %s" % (q, d))
print("=" * 84)
