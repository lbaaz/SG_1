# -*- coding: ascii -*-
"""RELEVE DE L'ACTE, VERSION 2 (derive par remplacements du releve de la v1, qui n'est pas edite : ligne de fin, et quatre
phrases de plus a refaire : la marge de E3, les deux phrases sur BP, l'heure du feu vert).
RELEVE DE L'ACTE du run du gel "loi de la largeur, ordre 3" : controle de sortie de la plume, pas une certification.
L'acte est RELU par expressions regulieres ; ses nombres sont refaits depuis le verdict d'ordre 3 du run, etat par etat, par
un code qui n'est ni la feuille, ni la lecture du resultat, ni l'ecriture de l'acte.
Usage : python3 -I releve_acte_gel_loi_machine1_v1.py <acte.md> <dossier du run (lot de machine 2)> <verdict d'ordre 3
        rejoue par machine 1> <canons connus.json> <marges gelees.json>      (code 0 si aucun controle ne mord)"""
import sys, os, re, json, math, hashlib, unicodedata
ACTE, RUN, REJEU, CONNUS, MARGES = sys.argv[1:6]
T = open(ACTE, "rb").read().decode("utf-8"); LG = T.split("\n"); U = re.sub(r"\s+", " ", T); RES = []
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n"); return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def ctl(nom, ok, detail=""):
    RES.append((nom, bool(ok))); print("%-4s %s  %s" % (nom, "TIENT" if ok else "MORD ", detail))
def mediane(v):
    v = sorted(v); return 0.5 * (v[(len(v) - 1) // 2] + v[len(v) // 2])
V = json.load(open(os.path.join(RUN, "verdict_ordre3.json"))); W = json.load(open(REJEU)); ET = json.load(open(MARGES))["etalonnage"]
# R01 forme
try:
    T.encode("ascii"); asc = True
except UnicodeEncodeError:
    asc = False
ctl("R01", asc and "%" not in T and max(len(l) for l in LG) <= 100 and T.endswith("-- FIN journal_delta_nn_loi_largeur_ordre3_v2 --\n") and not any(l != l.rstrip() for l in LG),
    "ASCII, sans pour cent, plus longue ligne %d, ligne de FIN" % max(len(l) for l in LG))
# R02 empreintes
connus = json.load(open(CONNUS)); vus = sorted(set(re.findall(r"\b[0-9a-f]{16}\b", T))); mauvais = [h for h in vus if h not in connus or not os.path.exists(connus[h]) or canon(connus[h]) != h]
ctl("R02", not mauvais, "%d empreintes distinctes, toutes recalculees depuis un fichier tenu ; en defaut : %s" % (len(vus), mauvais))
# R03 la table des cellules et les issues, refaites etat par etat depuis le verdict du run
def tol(e):
    return 0.05 if e["e_bord"] < 0.3 else 0.10
lignes = [re.match(r"\s+(N[1-5]|P[1-5]|BN|BP)\s+(\d+) /\s+(\d+) /\s+(\d+) /\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+\|ln q3\| (\S+)\s+marge (\S+)\s+\|ln q2\| (\S+)\s*$", l) for l in LG]
lignes = {m.group(1): m.groups()[1:] for m in lignes if m}; ok3 = len(lignes) == 12; verdicts = {}
for x in V["cellules"]:
    jug = [e for e in x["etats"] if e["exclu"] is None]; dom = [e for e in jug if e["e_bord"] < 0.7 and e["stab3"] is not None and e["stab3"] <= 0.05 and e["G3"] > 0]; hors = [e for e in jug if e not in dom]
    q3 = [abs(math.log(e["G3"] / e["Gamma_pl"])) for e in dom]; q2 = [abs(math.log(e["G2"] / e["Gamma_pl"])) for e in jug]; B = 1.25 if abs(x["delta"]) <= 0.06 + 1e-12 else 1.6
    e1 = "TIENT" if all(a <= tol(e) for a, e in zip(q3, dom)) else "TOMBE"; pres = sum(1 for e in dom if abs(math.log(e["G3"] / e["Gamma_pl"])) < abs(math.log(e["G2"] / e["Gamma_pl"])))
    e2 = ("TIENT" if 4 * pres >= 3 * len(dom) else "TOMBE") if x["creneau"] == "N" else "-"; e3 = "TIENT" if all(a <= math.log(B) for a in q2) else "TOMBE"
    assez = 3 * len(jug) >= 2 * len(x["etats"]); expl = assez and (len(dom) >= 5 if x["creneau"] in ("N", "P") else (len(dom) >= 2 and len(hors) >= 2))
    verdicts[x["id"]] = (e1, e2, e3, expl); marge = min(tol(e) - a for a, e in zip(q3, dom))
    n_l, n_j, n_d, n_h, t1, t2, t3, a3, mg_, a2 = lignes[x["id"]]
    ok3 = ok3 and (int(n_l), int(n_j), int(n_d), int(n_h)) == (len(x["etats"]), len(jug), len(dom), len(hors)) and (t1, t2, t3) == (e1, e2, e3) and expl \
        and abs(float(a3) - max(q3)) < 6e-5 and abs(float(mg_) - marge) < 6e-5 and abs(float(a2) - max(q2)) < 6e-5
tomb = lambda ids, k: [i for i in ids if verdicts[i][k] == "TOMBE"]
LN, LP = ["N1", "N2", "N3", "N4", "N5"], ["P1", "P2", "P3", "P4", "P5"]
iss = (not tomb(LN + LP, 0), not tomb(LN, 1), not tomb(["BN", "BP"], 0), not tomb(LN + LP + ["BN", "BP"], 2))
ctl("R03", ok3 and all(iss) and "VERDICT : E1 TENU, E2 TENU, E1B TENU, E3 TENU." in T and [V[k]["issue"] for k in ("E1", "E2", "E1B", "E3")] == ["TENU"] * 4,
    "12 lignes relues ; comptes, verdicts de cellule, plus grands ecarts et marges refaits etat par etat ; les quatre issues refaites : aucune cellule tombee, toutes exploitables")
# R04 le rejeu de machine 1 : memes verdicts de cellule, ecart maximal
dw = {x["id"]: x for x in W["cellules"]}; pire = 0.0; memes = [W[k]["issue"] for k in ("E1", "E2", "E1B", "E3")] == ["TENU"] * 4
for x in V["cellules"]:
    y = dw[x["id"]]; memes = memes and (x["E1"], x["E2"], x["E3"], x["n_juges"], x["n_domaine"]) == (y["E1"], y["E2"], y["E3"], y["n_juges"], y["n_domaine"])
    for a, b in zip(x["etats"], y["etats"]):
        if a["exclu"] is None:
            pire = max(pire, abs(a["ln_q3"] - b["ln_q3"]))
m4 = re.search(r"sur les 141 etats juges : (\S+) sur ln q3", U)
ctl("R04", memes and m4 and abs(float(m4.group(1)) / pire - 1.0) < 0.06, "rejeu de machine 1 : memes issues et memes cellules ; plus grand ecart sur ln q3 refait : %.1e (l'acte : %s)" % (pire, m4.group(1) if m4 else "-"))
# R05 les nombres de nn.0, nn.5, nn.6, nn.7
J = [(x, e) for x in V["cellules"] for e in x["etats"] if e["exclu"] is None]; D = [(x, e) for x, e in J if e["dans_le_domaine"]]; H = [(x, e) for x, e in J if not e["dans_le_domaine"]]
q3 = lambda e: math.log(e["G3"] / e["Gamma_pl"]); q2 = lambda e: math.log(e["G2"] / e["Gamma_pl"]); d32 = lambda e: math.log(e["G3"] / e["G2"])
bp = max((abs(q3(e)), e["rang"]) for x, e in D if x["id"] == "BP")
lig = [abs(q3(e)) for x, e in D if x["creneau"] in ("N", "P")]; neg = [(x, e) for x, e in D if x["delta"] < 0]; pos = [(x, e) for x, e in D if x["delta"] > 0]
ks = [-q3(e) / d32(e) ** 2 for x, e in neg if abs(d32(e)) >= 0.05]; c3 = [q3(e) / x["delta"] ** 3 for x, e in pos]; c2 = [q3(e) / x["delta"] ** 2 for x, e in pos]
VT = json.load(open(os.path.join(RUN, "verdict_ter.json"))); BPM = sorted(((0.05 if e["e_bord"] < 0.3 else 0.10) - abs(q3(e)), e["rang"]) for x, e in D if x["id"] == "BP")
ETA = [e["plateaux"]["A"]["etalement"] for pt in VT["points"].values() for e in pt["etats"]]; eb_ = [e for e in VT["points"]["BP"]["etats"] if e["rang"] == BPM[0][1]][0]
ETB = eb_["plateaux"]["A"]["etalement"]; EBA = eb_["plateaux"]["B"]["ecart_ln_A"]; assert len(ETA) == 144 and ETB == max(ETA) and len(BPM) == 5 and BPM[2][0] < 0.0026 <= BPM[3][0]
attendus = ["144 etats lus, tous QUALIFIES par le lecteur ; 141 juges, dont 129 dans le domaine", "|ln q3| = %.6f pour une tolerance de 0.10" % bp[0], "tient a %.6f pres" % (0.10 - bp[0]),
            "a l'etat de rang %d, vaut %.6f pour T = 0.10 : marge %+.6f" % (bp[1], bp[0], 0.10 - bp[0]),
            "%d etats juges du domaine ; |ln q3| vaut %.4f en mediane et %.4f au plus (N1)" % (len(lig), mediane(lig), max(lig)),
            "a %d etats juges du domaine sur %d" % (sum(abs(q3(e)) < abs(q2(e)) for x, e in D if x["creneau"] == "N"), sum(1 for x, e in D if x["creneau"] == "N")),
            "ligne N, negatif a %d etats sur %d ; ligne P, positif a %d sur %d" % (sum(q3(e) < 0 for x, e in D if x["creneau"] == "N"), sum(1 for x, e in D if x["creneau"] == "N"),
                                                                                  sum(q3(e) > 0 for x, e in D if x["creneau"] == "P"), sum(1 for x, e in D if x["creneau"] == "P")),
            "Hors du domaine : %d etats juges (BN %d, BP %d), de e_bord %.3f a %.3f" % (len(H), sum(x["id"] == "BN" for x, e in H), sum(x["id"] == "BP" for x, e in H), min(e["e_bord"] for x, e in H), max(e["e_bord"] for x, e in H)),
            "Aux %d etats du domaine du run a delta < 0 : mediane %.2f, au plus %.2f ; aucun etat au-dessus de %.2f" % (len(ks), mediane(ks), max(ks), ET["k_max"]),
            "ln q3 / delta^3 atteint %.0f (avant le run : au plus %d) et depasse l'ancien maximum a %d etats sur %d" % (max(c3), math.ceil(ET["c3_max"]), sum(v > ET["c3_max"] for v in c3), len(pos)),
            "atteint %.1f (avant : au plus %.1f) et le depasse a %d etats" % (max(c2), math.ceil(ET["c2_max"] * 10 - 1e-9) / 10, sum(v > ET["c2_max"] for v in c2)),
            "l'ordre 3 est plus pres que l'ordre 2 aux %d etats du domaine" % sum(abs(q3(e)) < abs(q2(e)) for x, e in D if x["creneau"] == "P"),
            "L'ordre 3 n'y est plus loin que l'ordre 2 a AUCUN",
            "La plus petite marge en logarithme est %.3f, sur la ligne P" % min(math.log(1.25 if abs(x["delta"]) <= 0.06 + 1e-12 else 1.6) - abs(q2(e)) for x, e in J),
            "Trois des cinq etats du domaine de BP sont a moins de 0.0026 de la tolerance (rangs %d, %d et %d : %+.6f, %+.4f, %+.4f)" % (BPM[0][1], BPM[1][1], BPM[2][1], BPM[0][0], BPM[1][0], BPM[2][0]),
            "a l'etat de rang %d vaut %.4f, le plus grand des 144 etats lus (mediane %.5f), soit %.1f fois la marge ; le plateau B s'y ecarte du plateau A de %.1e en logarithme" % (
                BPM[0][1], ETB, mediane(ETA), ETB / BPM[0][0], abs(EBA)),
            "le 16/11 a 00 h 54 (heure qu'elle lit dans le journal de sa session)", "PROJET, VERSION 2"]
assert max(ks) <= ET["k_max"] and not any(abs(q3(e)) > abs(q2(e)) for x, e in H)
manq = [a for a in attendus if a not in U]
ctl("R05", not manq, "%d phrases a nombres refaites depuis les etats du run et retrouvees dans l'acte ; absentes : %s" % (len(attendus), manq))
# R06 les classes de e_bord
m6 = re.search(r"\[0, 0\.3\[ : (\d+) etats, mediane (\S+), plus grand (\S+) ; \[0\.3, 0\.5\[ : (\d+), (\S+), (\S+) ; \[0\.5, 0\.7\[ : (\d+), (\S+), (\S+)\. ", U); ok6 = bool(m6)
if m6:
    g = m6.groups()
    for i, (lo, hi) in enumerate(((0.0, 0.3), (0.3, 0.5), (0.5, 0.7))):
        v = [abs(q3(e)) for x, e in D if lo <= e["e_bord"] < hi]; ok6 = ok6 and int(g[3 * i]) == len(v) and abs(float(g[3 * i + 1].rstrip(",")) - mediane(v)) < 6e-5 and abs(float(g[3 * i + 2].rstrip(".")) - max(v)) < 6e-5
ctl("R06", ok6, "trois classes de e_bord relues et refaites (129 etats)")
# R07 le journal du pilote
pj = open(os.path.join(RUN, "pilote_gel_loi.log"), "rb").read().decode().replace("\r\n", "\n")
ok7 = (len(re.findall(r"code=0 duree=", pj)) == 19 and "code=1" not in pj and "01:49:18 PILOTE DU GEL" in pj and "03:32:04 FIN DU PILOTE ; duree totale 6166 s" in pj
       and "lance le 2026-11-16 a 01:49:18 et fini a 03:32:04 ; duree totale 6166 s ; 19 appels, tous au code 0" in U and "canon table             35fa7b73f2b7f8eb" in pj and "prevol" not in pj.lower())
ctl("R07", ok7, "journal du pilote : heures, duree, 19 appels au code 0, table du gel, pas de pre-vol ; l'acte dit ces nombres")
n = sum(1 for _, o in RES if not o)
print("RELEVE DE L'ACTE (v2) : %d controles, %d mordent" % (len(RES), n)); sys.exit(0 if n == 0 else 1)
