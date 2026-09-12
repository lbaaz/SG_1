#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RELECTURE MECANIQUE DES NOMBRES DE MA NOTE DE REJEU -- machine 2, v1, 12/09/2026.

Chaque nombre de la note est repris de MES sorties ou des SIENNES, jamais de ma prose.
Les pourcentages et les parts de plancher sont RECALCULES, pas relus. La tolerance de
chaque controle est celle du chiffre ecrit.
"""
import hashlib, json, os, re, sys, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
N = open(os.path.join(ICI, "POUR_MACHINE1_rejeu_convergence_dt_machine2_v1.md"),
         encoding="utf-8").read()
NP = re.sub(r"\s+", " ", N)
m1 = json.load(open(os.path.join(
    RAC, "entrant_machine1_2026-09-12_convergence_dt", "lot",
    "convergence_dt_7_1p73_machine1_v1.json"), encoding="utf-8"))
r1 = json.load(open(os.path.join(ICI, "rejeu1_convergence_dt_machine2_v1.json"),
                    encoding="utf-8"))
r2 = json.load(open(os.path.join(ICI, "rejeu2_convergence_dt_machine2_v1.json"),
                    encoding="utf-8"))
OK, MORD = [], []


def chk(q, c, d=''):
    OK.append(bool(c))
    if not c:
        MORD.append((q, d))
    print("  [%s] %-54s %s" % ("OK  " if c else "MORD", q[:54], d))


def dit(s):
    return re.sub(r"\s+", " ", s) in NP


print("=" * 84)
print("RELECTURE DES NOMBRES DE MA NOTE DE REJEU")
print("=" * 84)

print("\n[1] LES SEPT LECTURES, CONTRE MON JSON")
chk("n_pas 380/760/1520/3040",
    [f["n_pas"] for f in r1["flots"]] == [380, 760, 1520, 3040]
    and dit("380/760/1520/3040"))
chk("les quatre finissent sur TAU_FIN",
    len({f["tau_fin"] for f in r1["flots"]}) == 1
    and abs(r1["flots"][0]["tau_fin"] - r1["cellule"]["tau_CAP"]) < 1e-18)
R = r1["flots"][3]["R_composantes"]
chk("R = 59087466.259, a 1e-06 de 59087466.747",
    abs(R / 59087466.747 - 1) < 1e-6 and dit("59087466.259"), "%.3f" % R)
e0 = r1["flots"][0]["e"]
chk("e(dt2) = 1.048162e-06, a 0.42 % de la sienne",
    abs(e0 - 1.048162e-06) < 5e-13
    and abs(round(100 * abs(e0 / m1["flots"][0]["e"] - 1), 2) - 0.42) < 0.005
    and dit("1.048162e-06") and dit("0.42 %"),
    "%.6e ; ecart %.4f %%" % (e0, 100 * abs(e0 / m1["flots"][0]["e"] - 1)))
rs = r1["paires"][0]["lecture_5_4_sur_flot_fin"]["ratio_seuil"]
chk("e/seuil a la paire du gel = 0.6842", abs(rs - 0.6842) < 5e-5 and dit("0.6842"),
    "%.6f" % rs)
chk("et 0.7593 est exclu (c'est SON nombre, pas le mien)",
    abs(rs - 0.7593) > 0.05 and dit("0.7593 exclu"))
chk("e/plancher a dt2/4 et dt2/8 = 1.4116 et 1.2600",
    abs(r1["flots"][2]["e_sur_plancher"] - 1.4116) < 5e-5
    and abs(r1["flots"][3]["e_sur_plancher"] - 1.2600) < 5e-5
    and dit("1.4116 ; 1.2600"))
chk("p_obs raffines 2.1083 et 0.1640, sous 3.8280",
    abs(r1["paires"][1]["p_obs"] - 2.1083) < 5e-5
    and abs(r1["paires"][2]["p_obs"] - 0.1640) < 5e-5
    and max(r1["paires"][1]["p_obs"], r1["paires"][2]["p_obs"]) < 3.8280
    and dit("2.1083 ; 0.1640"))

print("\n[2] LA TABLE DU FAIT CENTRAL -- TOUT RECALCULE")
b0 = r1["flots"][0]["e_sur_plancher"]
attendus = [(79.890, 79.8903, 0.0), (4.993, 6.0869, 18.0),
            (0.312, 1.4116, 77.9), (0.020, 1.2600, 98.5)]
for k, (tr, em, pp) in enumerate(attendus):
    tronc = b0 / 16 ** k
    e_m = r1["flots"][k]["e_sur_plancher"]
    part = 100 * (1 - min(tronc, e_m) / e_m)
    chk("dt2/%-3d : troncature %.3f, e %.4f, plancher %.1f %%" % (2 ** k, tr, em, pp),
        abs(tronc - tr) < 5e-4 and abs(e_m - em) < 5e-5 and abs(part - pp) < 0.05
        and dit("%.3f plancher" % tr) and dit("%.1f %%" % pp),
        "calcule : %.3f / %.4f / %.1f %%" % (tronc, e_m, part))
ec = [abs(r1["flots"][k]["e"] / m1["flots"][k]["e"] - 1) for k in range(4)]
chk("les ecarts 4.16e-03, 9.89e-02, 3.60e-02, et 0 au dernier",
    abs(ec[0] - 4.16e-3) < 5e-6 and abs(ec[1] - 9.89e-2) < 5e-5
    and abs(ec[2] - 3.60e-2) < 5e-5 and ec[3] == 0.0
    and dit("4.16e-03") and dit("9.89e-02") and dit("3.60e-02"),
    "%.3e %.3e %.3e %.1e" % tuple(ec))
chk("'domine a 82 % par la TRONCATURE' a dt2/2 == 18.0 % plancher",
    abs((100 - 18.0) - 82) < 0.05 and dit("domine a 82 % par la TRONCATURE"))

print("\n[3] L'IDENTITE AU BIT A dt2/8, LES CINQ GRANDEURS")
for q in ("e", "R_composantes", "plancher_composantes", "ratio_seuil_du_flot",
          "tau_au_max"):
    chk("dt2/8 : %s identique au bit" % q, m1["flots"][3][q] == r1["flots"][3][q])
for v in ("1.6530853961382515e-08", "59087466.25901179", "0.00015638885675542218"):
    chk("cite en pleine precision : %s" % v, dit(v))

print("\n[4] LES DEUX PLATEFORMES, CITEES")
p1, p2 = m1.get("plateforme", {}), r1.get("plateforme", {})
chk("m1 : python 3.12.3, numpy 2.4.4, Linux",
    p1.get("python") == "3.12.3" and p1.get("numpy") == "2.4.4"
    and "Linux" in p1.get("platform", "") and dit("python 3.12.3 / numpy\n2.4.4"))
chk("m2 : python 3.11.9, numpy 2.2.6, Windows",
    p2.get("python") == "3.11.9" and p2.get("numpy") == "2.2.6"
    and "Windows" in p2.get("platform", "") and dit("python 3.11.9 / numpy\n2.2.6"))
chk("'trois versions differentes' : python, numpy, OS",
    p1.get("python") != p2.get("python") and p1.get("numpy") != p2.get("numpy")
    and p1.get("platform") != p2.get("platform") and dit("Trois versions differentes"))

print("\n[5] LE DETERMINISME, RECALCULE ICI")
tout = all(r1["flots"][k][q] == r2["flots"][k][q] for k in range(4)
           for q in ("e", "R_composantes", "plancher_composantes",
                     "ratio_seuil_du_flot", "tau_au_max", "err_rel_fin"))
tout &= all(r1["paires"][i]["p_obs"] == r2["paires"][i]["p_obs"] for i in range(3))
chk("deux rejeux : quatre flots x six grandeurs + trois p_obs, au bit",
    tout and dit("Les quatre flots, six grandeurs chacun, et\nles trois `p_obs` : identiques au bit"))

print("\n[6] LES EMPREINTES CITEES")


def emp(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8'))
                          .replace('\r\n', '\n').encode()).hexdigest()[:16]


LOT = os.path.join(RAC, "entrant_machine1_2026-09-12_convergence_dt", "lot")
chk("canon de son lot = 2b155abffbe4f6ff",
    emp(os.path.join(LOT, "MANIFEST_lot_machine1_convergence_dt_7_1p73_v1.txt"))
    == "2b155abffbe4f6ff" and dit("2b155abffbe4f6ff"))
env = r"C:\Users\bazil\Downloads\files (52).zip"
if os.path.exists(env):
    b = hashlib.sha256(open(env, 'rb').read()).hexdigest()[:16]
    chk("enveloppe e98c01d7116f7bb4", b == "e98c01d7116f7bb4" and dit(b), b)
for h in ("a4c35a2ee691c9a7", "c8ed357b120352c4", "d037d21"):
    chk("cite : %s" % h, dit(h))

print("\n[7] MES SORTIES SONT BIEN CELLES DE SON SCRIPT, INTOUCHEES")
a = open(os.path.join(ICI, "convergence_dt_7_1p73_machine1_v1.json"), 'rb').read()
b = open(os.path.join(ICI, "rejeu1_convergence_dt_machine2_v1.json"), 'rb').read()
chk("rejeu1_*.json == la sortie du script, au bit", a == b, "%d octets" % len(b))
a = open(os.path.join(ICI, "convergence_dt_7_1p73_machine1_v1.log"), 'rb').read()
b = open(os.path.join(ICI, "rejeu1_convergence_dt_machine2_v1.log"), 'rb').read()
chk("rejeu1_*.log == la sortie du script, au bit", a == b, "%d octets" % len(b))
a = open(os.path.join(ICI, "rejeu2", "convergence_dt_7_1p73_machine1_v1.json"), 'rb').read()
b = open(os.path.join(ICI, "rejeu2_convergence_dt_machine2_v1.json"), 'rb').read()
chk("rejeu2_*.json == la sortie du second run, au bit", a == b, "%d octets" % len(b))

print("\n" + "=" * 84)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s  %s" % (q, d))
print("=" * 84)
