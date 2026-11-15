# -*- coding: ascii -*-
"""RELEVE DE SORTIE DE L'ACTE DU GEL "LA CHAINE E-A AU SECOND ORDRE" -- machine 1, v1, 2026-11-15.
Chaque nombre et chaque canon de l'acte est relu a sa source par un autre chemin que le script qui l'a pose : la
lecture du JSON de la sonde est REFAITE ici, du texte du gel, sans la feuille ni le verdict.
Arguments : <acte.md> <recu> <dossier du gel> <manifeste du lot du gel> <note hors chaine> <clone du registre>
            <dossier des pieces de l'acte>."""
import sys, os, re, json, math, hashlib, unicodedata, subprocess, statistics
from collections import Counter
ACTE, RECU, GEL, MANIF_GEL, NOTE, CLONE, DOS = sys.argv[1:8]
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
lire = lambda p: open(p, encoding="utf-8").read().replace("\r\n", "\n")
T = lire(ACTE); L = T.split("\n"); plat = " ".join(T.split())
res = []
def ctl(nom, ok, detail=""):
    res.append(bool(ok)); print("  %s  %s%s" % ("TIENT" if ok else "MORD ", nom, (" : " + detail) if detail else ""))
def dans(*ph):
    return all(" ".join(p.split()) in plat for p in ph)
f3 = lambda x: "%.3f" % x
LC, LR = RECU + "/lots/certification/", RECU + "/lots/resultat/"
SO, ENV = LR + "ordre2/sortie/", RECU + "/enveloppe/"

# ---------------------------------------------------------------- R01 forme
ctl("R01 forme : ASCII, sans pour-cent, lignes de 100 au plus, sans blanc final, titre et ligne de fin",
    all(ord(ch) < 128 for ch in T) and "%" not in T and max(len(l) for l in L) <= 100 and all(l == l.rstrip() for l in L)
    and L[0].startswith("DELTA nn -- LA CHAINE E-A AU SECOND ORDRE") and L[2] == "-- PROJET, VERSION 1"
    and L[-2] == "-- FIN journal_delta_nn_ordre2_chaine_EA_v1 --" and L[-1] == "" and not re.search(r"delta 9[89]|DELTA 9", T))

# ---------------------------------------------------------------- R02 canons
sec1 = T[T.index("nn.1 PIECES"):T.index("nn.2 CE QUI A ETE JOUE")]
paires = re.findall(r"^ +(\S+)  ([0-9a-f]{16})$", sec1, re.M)
def chemin(nom):
    for base in (CLONE + "/", GEL + "/", LC, LR, DOS + "/"):
        if os.path.isfile(base + nom):
            return base + nom
    if nom.startswith("note_machine1_residuel"):
        return NOTE
    return None
faux = [(n, c) for n, c in paires if chemin(n) is None or B(chemin(n)) != c]
lots = dict(re.findall(r"lot de (certification|resultat)  ([0-9a-f]{16})", sec1))
lot_m1 = re.search(r"de machine 1 \(lot ([0-9a-f]{16})\)", sec1).group(1)
ok_lots = (lots.get("certification") == B(ENV + "MANIFEST_lot_machine2_certification_gel_ordre2_chaine_EA_v1.txt")
           and lots.get("resultat") == B(ENV + "MANIFEST_lot_machine2_resultat_ordre2_chaine_EA_v1.txt") and lot_m1 == B(MANIF_GEL))
ctl("R02 canons : %d pieces de nn.1 relues a leur fichier, trois lots a leur manifeste" % len(paires), len(paires) == 28 and not faux and ok_lots, str(faux))
connus = set(c for _, c in paires) | set(lots.values()) | {lot_m1}
tous = set(re.findall(r"(?<![0-9a-f.])[0-9a-f]{16}(?![0-9a-f-])", T))
ctl("R03 tout motif de 16 hexadecimaux de l'acte est un canon de nn.1", tous <= connus and len(tous) == len(connus), " ".join(sorted(tous ^ connus)))

# ---------------------------------------------------------------- R04 le registre
git = lambda *a: subprocess.run(["git", "-C", CLONE] + list(a), capture_output=True, text=True).stdout.strip()
sujet = git("log", "-1", "--format=%s")
ctl("R04 registre : tete 79e77d2 = origin/main, delta 97, regles 32 a 34 : trente-quatre attendent",
    git("rev-parse", "--short", "HEAD") == "79e77d2" == git("rev-parse", "--short", "origin/main") and sujet.startswith("delta 97 --")
    and "numbered 32 to 34, join the thirty-one awaiting review" in sujet and T.count("79e77d2") == 2
    and dans("plafond 97", "trente-quatre attendent la revue"))

# ---------------------------------------------------------------- la lecture, refaite du texte du gel
s = json.load(open(SO + "sonde_ordre2.json", encoding="utf-8"))
gel = lire(GEL + "/gel_ordre2_chaine_EA_pre_enregistrement_v1.md")
tab_gel = re.findall(r"^    ([A-Z]\d)  w2 = (\d+)/(\d+)\s+facteur (\S+)\s+delta ([+-]\d\.\d\d)\s+D1 (\d\.\d{6})  c_max (\d\.\d{6})  (EN DOMAINE|HORS DOMAINE)\s+N (\d+)$", gel, re.M)
assert len(tab_gel) == 16
G = {t[0]: t for t in tab_gel}
def borne_de(pid):
    if pid[0] not in "CML":
        return None
    a = abs(float(G[pid][4]))
    return 1.25 if a <= 0.06 else (1.6 if a <= 0.10 else 2.0)
PL = 1.33e-13
def motif(e, vus):
    g = [e["Gamma_2D"][k] for k in ("2", "3", "4")]; ch = e["chaine"]; c2 = e.get("chaine2") or {}
    if not e["J_ecart_type"] < 0.2: return "J flou"
    if e["n1"] < 0 or e["n2"] < 0: return "etiquette"
    if not e["poids_site"] >= 0.5: return "site"
    if not e["Gamma_2D"]["3"] > 10 * PL: return "sous dix planchers"
    if e["suivi"]["2"] < 0.9 or e["suivi"]["4"] < 0.9: return "suivi"
    if min(g) <= 0 or max(g) > 2 * min(g): return "cible"
    if ch.get("erreur") or ch.get("vide") or not ch.get("definie"): return "barriere vide"
    if min(ch["gammas"]) <= 0 or max(ch["gammas"]) > 2 * min(ch["gammas"]): return "chaine"
    if c2.get("erreur") or not c2.get("definie"): return "ordre 2"
    if min(c2["gammas_flux"]) <= 0 or max(c2["gammas_flux"]) > 2 * min(c2["gammas_flux"]): return "ordre 2 instable"
    if vus[(e["n1"], e["n2"])] > 1: return "double"
    return None
PT = {}
for p in s["points"]:
    pid = p["id"]; d = int(G[pid][1]) / int(G[pid][2]) - 2.0; vus = Counter((e["n1"], e["n2"]) for e in p["etats"])
    js, ex = [], Counter()
    for e in p["etats"]:
        m = motif(e, vus)
        if m:
            ex[m] += 1; continue
        g3 = e["Gamma_2D"]["3"]; g2 = e["chaine2"]["gammas_flux"][2]; g1 = e["chaine"]["gammas"][2]
        de = e["E_re"] - e["E_libre"]
        js.append({"q2": g2 / g3, "q1": g1 / g3, "ee": abs(e["chaine2"]["dE"][2] - de) / abs(de), "g2": g2, "g3": g3,
                   "loi": (g2 / g3) / math.exp(2.87 * d * d * e["chaine2"]["m_bord"]), "fi": abs(e["chaine2"]["gammas_im"][2] / g2 - 1.0)})
    b = borne_de(pid)
    dedans = lambda x, bo, marge: (x["g3"] - marge) / bo <= x["g2"] <= bo * (x["g3"] + marge)
    PT[pid] = {"n": len(js), "ex": ex, "js": js, "borne": b, "lisible": len(js) >= 6, "N": p["N"], "duree": p["duree_s"],
               "tenu": (b is not None and all(dedans(x, b, PL) for x in js)), "tenu_nu": (b is not None and all(dedans(x, b, 0.0) for x in js)),
               "palier": next((bo for bo in (1.25, 1.6, 2.0) if all(dedans(x, bo, PL) for x in js)), None)}
ORDRE = [t[0] for t in tab_gel]; JUG = [k for k in ORDRE if k[0] in "CML"]
mq = lambda k, c, f: f(x[c] for x in PT[k]["js"])
pire = lambda k, c: max(abs(math.log(x[c])) for x in PT[k]["js"])

# ---------------------------------------------------------------- R05, R06 les deux tableaux de nn.4
sec4 = T[T.index("nn.4 LES SEIZE POINTS"):T.index("nn.5 LE VERDICT")]
t1 = re.findall(r"^    ([A-Z]\d)  (\d+/\d+)\s+(\S+)\s+([+-]\d\.\d\d)  (\S+)\s+(\S+)\s+(\d+)     (\d\.\d{3})  (\d\.\d{3})  (\d\.\d{3})   (\S+)\s+(\S+)$", sec4, re.M)
ok = len(t1) == 15 and [x[0] for x in t1] == [k for k in ORDRE if k != "W2"]
for (pid, w2, fac, d, bande, borne, n, a, m, b, pal, st) in t1:
    p = PT[pid]; g = G[pid]
    ok = ok and w2 == "%s/%s" % (g[1], g[2]) and fac == g[3] and d == g[4] and int(n) == p["n"]
    ok = ok and (a, m, b) == (f3(mq(pid, "q2", min)), f3(mq(pid, "q2", statistics.median)), f3(mq(pid, "q2", max)))
    ok = ok and borne == ("%g" % p["borne"] if p["borne"] else "-") and pal == ("%g" % p["palier"] if p["palier"] else "aucun")
    ok = ok and st == (("TENU" if p["tenu"] else "TOMBE") if p["borne"] else "LU")
    ok = ok and bande == ({1.25: "proche", 1.6: "moyenne", 2.0: "lointaine"}.get(p["borne"]) or {"A": "ancre", "W": "temoin"}[pid[0]])
lw2 = re.search(r"^    W2  209/100  1/2   \+0\.09  temoin     -        3     NON LISIBLE \(moins de 6 etats juges\)$", sec4, re.M)
ctl("R05 nn.4, premier tableau : quinze lignes relues (etats juges, q2, palier, statut), W2 NON LISIBLE", ok and lw2 and not PT["W2"]["lisible"] and PT["W2"]["n"] == 3)
t2 = re.findall(r"^    ([A-Z]\d)\s+(\d+\.\d{3})\s+(\d+\.\d{3})\s+(\d+\.\d{3})    (\d\.\d{3})    (\d\.\d{3})   (\S+(?: \S+)?)\s+(\d\.\d\de-\d\d)\s+(\S+(?: \S+)?)$", sec4, re.M)
ok = len(t2) == 15
for (pid, a, m, b, p2, p1, comp, ee, en) in t2:
    ok = ok and (a, m, b) == (f3(mq(pid, "q1", min)), f3(mq(pid, "q1", statistics.median)), f3(mq(pid, "q1", max)))
    ok = ok and (p2, p1) == (f3(pire(pid, "q2")), f3(pire(pid, "q1"))) and comp == ("MIEUX" if pire(pid, "q2") < pire(pid, "q1") else "PAS MIEUX")
    ok = ok and ee == "%.2e" % mq(pid, "ee", max) and en == ("TENUE" if mq(pid, "ee", max) <= 0.01 else "NON TENUE")
ctl("R06 nn.4, second tableau : quinze lignes relues (q1, pires ecarts, comparaison, energie)", ok)
nj = sum(PT[k]["n"] for k in JUG); exj = sum((PT[k]["ex"] for k in JUG), Counter())
ctl("R07 nn.4 : %d etats juges aux douze points, exclus par motif ; W2" % nj,
    nj == 132 and dict(exj) == {"sous dix planchers": 31, "J flou": 4, "barriere vide": 1} and dict(PT["W2"]["ex"]) == {"sous dix planchers": 11}
    and dans("168 etats, 132 juges, 36 exclus (31 sous dix planchers, 4 a J flou, 1 a barriere vide)", "A W2 : 3 etats juges, 11 exclus sous dix planchers",
             "132 etats juges", "seize points, 224 etats") and sum(len(p["etats"]) for p in s["points"]) == 224
    and sorted(Counter(re.findall(r"(\d+) etats juges", T)).items()) == [("11", 1), ("132", 2), ("3", 4), ("6", 1)])

# ---------------------------------------------------------------- R08 le verdict, les bandes, les deux issues
par_bande = {bo: [k for k in JUG if PT[k]["borne"] == bo] for bo in (1.25, 1.6, 2.0)}
ok = all(len(v) == 4 and all(PT[k]["lisible"] and PT[k]["tenu"] and PT[k]["tenu_nu"] for k in v) for v in par_bande.values())
ok = ok and all(pire(k, "q2") < pire(k, "q1") and mq(k, "ee", max) <= 0.01 for k in JUG)
q2j = [x["q2"] for k in JUG for x in PT[k]["js"]]; q1j = [x["q1"] for k in JUG for x in PT[k]["js"]]
mx = {bo: max((mq(k, "q2", max), k) for k in v) for bo, v in par_bande.items()}
ok = ok and dans("VERDICT : L'ORDRE 2 TIENT. COMPARAISON : L'ORDRE 2 FAIT MIEUX PARTOUT. ENERGIES : L'ENERGIE TIENT.",
                 "PROCHE, MOYENNE et LOINTAINE sont TENUES", "La lecture SANS MARGE (gel, section 11) rend le meme verdict",
                 "Plus grand q2 par bande : %s pour une borne de 1.25, %s pour 1.6, %s pour 2 ; ils sont a %s, %s et %s" % (
                     f3(mx[1.25][0]), f3(mx[1.6][0]), f3(mx[2.0][0]), mx[1.25][1], mx[1.6][1], mx[2.0][1]),
                 "le plus petit q2 des 132 etats juges est %s (a C1), le plus grand %s (a L4)" % (f3(min(q2j)), f3(max(q2j))),
                 "de q1 = %s a q1 = %s ; l'ordre 2 de %s a %s" % (f3(min(q1j)), f3(max(q1j)), f3(min(q2j)), f3(max(q2j))))
ok = ok and min(q2j) == mq("C1", "q2", min) and max(q2j) == mq("L4", "q2", max)
ctl("R08 nn.5, nn.6 : les trois bandes TENUES avec et sans marge, MIEUX aux douze points, energie tenue aux douze ; les extremes", ok)
ser = sorted(JUG, key=lambda k: pire(k, "q1") - pire(k, "q2"))[:3]
ebande = {bo: max(mq(k, "ee", max) for k in v) for bo, v in par_bande.items()}
ctl("R09 nn.6 : les trois comparaisons les plus minces ; l'energie par bande",
    ser == ["L2", "L1", "C3"] and dans("L2 (%s pour l'ordre 2 contre %s), L1 (%s contre %s), C3 (%s contre %s)" % tuple(f3(pire(k, c)) for k in ser for c in ("q2", "q1")),
                                       "l'ecart de L2, %s en logarithme" % f3(pire("L2", "q1") - pire("L2", "q2")),
                                       "%.4f a la bande proche, %.4f a la moyenne, %.4f a la lointaine (a L1)" % (ebande[1.25], ebande[1.6], ebande[2.0]))
    and ebande[2.0] == mq("L1", "ee", max) and 8 < (pire("L2", "q1") - pire("L2", "q2")) / 0.003 < 12)

# ---------------------------------------------------------------- R10 les lectures sans verdict
loi = {k: statistics.median(x["loi"] for x in PT[k]["js"]) for k in JUG}
w1 = [x["q2"] for x in PT["W1"]["js"]]
ok = (min(loi, key=loi.get) == "L2" and sorted(loi, key=loi.get)[-2:] in (["M4", "L3"], ["L3", "M4"]) and f3(loi["M4"]) == f3(loi["L3"])
      and dans("va de %s (L2) a %s (M4 et L3)" % (f3(loi["L2"]), f3(loi["M4"])),
               "a un point juge, est %.3f (L4)" % max(mq(k, "fi", max) for k in JUG),
               "q2 de %s a %s a A1, de %s a %s a A2" % (f3(mq("A1", "q2", min)), f3(mq("A1", "q2", max)), f3(mq("A2", "q2", min)), f3(mq("A2", "q2", max))),
               "11 etats juges, q2 de %s a %s ; sept sont au-dela de 1.6, deux au-dela de 2 ; aucun palier" % (f3(min(w1)), f3(max(w1))),
               "Il est MIEUX (%s contre %s) et tenu en energie (%.4f)" % (f3(pire("W1", "q2")), f3(pire("W1", "q1")), mq("W1", "ee", max)),
               "1.25 a huit points juges, les quatre de la bande proche, M1, M2, M3 et L1 ; 1.6 a M4, L2 et L3 ; 2 a L4")
      and max(mq(k, "fi", max) for k in JUG) == mq("L4", "fi", max) and len(w1) == 11 and sum(x > 1.6 for x in w1) == 7 and sum(x > 2 for x in w1) == 2
      and PT["W1"]["palier"] is None and sorted(k for k in JUG if PT[k]["palier"] == 1.25) == ["C1", "C2", "C3", "C4", "L1", "M1", "M2", "M3"]
      and sorted(k for k in JUG if PT[k]["palier"] == 1.6) == ["L2", "L3", "M4"] and [k for k in JUG if PT[k]["palier"] == 2.0] == ["L4"])
ctl("R10 nn.7 : paliers, loi apres coup, arithmetique, ancres, temoin W1", ok)

# ---------------------------------------------------------------- R11 les gardes
anc = {"A1": ((7, 2), "2.1623273017950654e-10", "2.3236497766513317e-10", "0.002118984943055927"),
       "A2": ((8, 2), "2.6613925716641374e-09", "2.794344791699548e-09", "-0.0028201377357584354")}
g4 = g8f = g8e = 0.0
for pid, (lab, r2d, ro2, rde) in anc.items():
    assert r2d in gel and ro2 in gel and rde in gel
    e = [x for p in s["points"] if p["id"] == pid for x in p["etats"] if (x["n1"], x["n2"]) == lab]
    assert len(e) == 1
    g4 = max(g4, abs(e[0]["Gamma_2D"]["3"] / float(r2d) - 1)); g8f = max(g8f, abs(e[0]["chaine2"]["gammas_flux"][2] / float(ro2) - 1))
    g8e = max(g8e, abs(e[0]["chaine2"]["dE"][2] / float(rde) - 1))
S = {p["id"]: p for p in s["points"]}
g6 = max(max(abs(S[k]["garde_moteur"]["D1"] - float(G[k][5])), abs(S[k]["garde_moteur"]["c_max"] - float(G[k][6]))) for k in ORDRE)
hd = [k for k in ORDRE if S[k]["garde_moteur"]["statut"] == "HORS DOMAINE"]
ctl("R11 nn.3 : G-4 au bit, G-8 a %.0e et %.0e, G-6 sous 1e-6, statuts de la garde, canons du moteur et de la sonde au JSON" % (g8f, g8e),
    g4 == 0.0 and dans("a %.0e pres pour Gamma_flux (tolerance 1e-3) et a %.0e pres pour dE (tolerance 1e-6)" % (g8f, g8e),
                       "elle dit HORS DOMAINE a %s." % ", ".join(hd), "au bit (ecart relatif 0, tolerance 1e-2)")
    and g6 < 1e-6 and all(S[k]["garde_moteur"]["statut"] == G[k][7] for k in ORDRE) and [k for k in ORDRE if G[k][7] == "HORS DOMAINE"] == hd
    and s["moteur_canon"] == B(CLONE + "/scripts/m17_chaine_v17.py") and s["sonde_canon"] == B(GEL + "/sonde_ordre2_machine1_v1.py")
    and all(len(S[k]["etats"]) == 14 for k in ORDRE) and [p["id"] for p in s["points"]] == ORDRE)

# ---------------------------------------------------------------- R12 le run
cons = lire(SO + "console_ordre2.log"); etat = lire(SO + "etat_machine_machine2.log"); ls = lire(SO + "sonde_ordre2.log")
du = dict((m.group(1), float(m.group(2))) for m in re.finditer(r"^([A-Z]\d) .* joue, 14 etats, ([0-9.]+) s$", ls, re.M))
ent = lambda x: int(math.floor(x + 0.5))
pf = s["plateforme"]
ctl("R12 nn.2 : heures, duree, batterie, horloge, plateforme, durees par point",
    "2026-11-14 23:26:01 LANCEMENT DE LA SONDE" in cons and "2026-11-15 00:41:24 FIN DE LA SONDE code=0 duree=4524 s" in cons
    and "EstimatedChargeRemaining 62 pour cent" in etat and "CurrentClockSpeed 2516 MHz ; MaxClockSpeed 3801 MHz" in etat and "a 100 pour cent" in etat
    and len(du) == 16 and all(abs(du[k] - PT[k]["duree"]) < 0.06 for k in ORDRE)
    and dans("lancee le 14/11 a 23 h 26, finie le 15/11 a 0 h 41, 4524 secondes, code 0", "batterie a 100 pour cent au lancement, a 62 a la fin",
             "2516 MHz pour un maximum de 3801", "le run en a pris %d et %d" % (ent(sum(du[k] for k in ORDRE if k != "W2")), ent(du["W2"])),
             "Durees par point, en secondes : %s." % ", ".join("%s %d" % (k, ent(du[k])) for k in ORDRE),
             "BOCAL4, Windows AMD64, python 3.11.9, numpy 2.2.6, 16 coeurs", "boite de 89, %d secondes sur batterie" % ent(du["W2"]))
    and (pf["systeme"], pf["machine"], pf["python"], pf["numpy"], pf["coeurs"]) == ("Windows", "AMD64", "3.11.9", "2.2.6", 16) and PT["W2"]["N"] == 89
    and "de l'ordre de 3100 secondes" in gel and "de 1500 pour W2 seul" in gel)

# ---------------------------------------------------------------- R13 le rejeu et le lecteur independant
a = json.load(open(DOS + "/verdict_rejoue_machine1.json", encoding="ascii")); b = json.load(open(SO + "verdict_ordre2.json", encoding="utf-8"))
ctl("R13 nn.2 : verdict rejoue = verdict de machine 2, meme canon ; lecteur independant 0 ecart ; ancres au bit",
    a == b and B(DOS + "/verdict_rejoue_machine1.json") == B(SO + "verdict_ordre2.json") and a["verdict"] == "L'ORDRE 2 TIENT"
    and a["verdict_sans_marge"] == "L'ORDRE 2 TIENT" and a["gardes_par_la_marge"] == [] and a["motifs"] == []
    and "ECARTS ENTRE MON LECTEUR ET LA FEUILLE : 0 []" in lire(SO + "relecture_independante_machine2.log")
    and "BILAN : 28 etats, 0 etiquettes differentes ; ecart absolu max de Gamma_2D (k = 2, 3, 4) 0.00e+00" in lire(SO + "compare_run_essai_ancres_machine2.log")
    and "SELFTEST : 160 cas, 160 tenus" in lire(SO + "lecture_ordre2.log") and "SELFTEST : 160 cas, 160 tenus" in lire(DOS + "/lecture_rejouee_machine1.log"))

# ---------------------------------------------------------------- R14 la certification de machine 2
ctlg = lire(LC + "ordre2/controles_gel_ordre2_machine2_v1.log"); bl = lire(LC + "ordre2/bloc_independant_machine2_v1.log")
bc = lire(LC + "ordre2/banc_feuille_ordre2_machine2_v1.log")
mA = re.search(r"plus grand ecart relatif : t 0\.00e\+00 ; Sigma2 [0-9.e-]+ ; u ([0-9.e-]+)", bl); mB = re.search(r"5 etats, boite N = n1 \+ 24, .* ; ecart relatif : t 0\.00e\+00 ; Sigma2 [0-9.e-]+ ; u ([0-9.e-]+)", bl)
mE = re.search(r"A1 \(7,2\) w2=39/20 : .* erreur / \|dE\| de la chaine d'ordre 2 : ([0-9.e-]+), ([0-9.e-]+), ([0-9.e-]+) ; ordre 1 : ([0-9.e-]+) ; Sigma2 seul : ([0-9.e-]+) ; u seul : ([0-9.e-]+)", bl)
mb = re.search(r"survivent au selftest de machine 1 : \[([0-9, ]+)\] ; survivent a mon banc : \[([0-9, ]+)\]", bc)
sv1 = set(mb.group(1).replace(" ", "").split(",")); sv2 = set(mb.group(2).replace(" ", "").split(","))
ok = ("BILAN : 22 controles, 0 mordent []" in ctlg and "BILAN : 17 controles, 0 mordent []" in bl and "36 sauts" in bl
      and "%.0e" % float(mA.group(1)) == "5e-13" and "%.0e" % float(mB.group(1)) == "5e-15" and "LOWDIN SUR LE H_2D EXACT DU MOTEUR" in bl
      and mE.groups() == ("7.50e-05", "1.84e-05", "4.59e-06", "4.37e-02", "4.40e-04", "4.40e-02")
      and 3.9 < float(mE.group(1)) / float(mE.group(2)) < 4.2 and 3.9 < float(mE.group(2)) / float(mE.group(3)) < 4.2
      and "BILAN : 115 alterations" in bc and len(sv1) == 22 and len(sv1 - sv2) == 20 and len(sv1 & sv2) == 2 and "4000 sondes synthetiques" in bc
      and "famille T (la table) : 131 alterations, 131 mordues" in ctlg
      and dans("22 controles, 0 morsure ; le bloc recalcule a part, 17 controles, 0 morsure", "(7.50e-05, 1.84e-05, 4.59e-06 a l'etat d'ancre de A1)",
               "a g, l'ordre 1 est a 4.37e-02, \"u seul\" a 4.40e-02, \"Sigma2 seul\" a 4.40e-04", "a 5e-13 pres par une somme sur les 36 sauts de x^5, et a 5e-15 pres",
               "laisse passer 22 des 115 alterations", "son banc en mord 20, les deux dernieres etant equivalentes", "(131 alterations sur 131)",
               "s'accordent sur 4000 sondes synthetiques", "la note : 0 morsure, six reserves"))
ctl("R14 nn.2, nn.6, nn.9 : les nombres de la certification de machine 2, relus dans ses journaux", ok)

# ---------------------------------------------------------------- R15 le bruit des fils
sens = lire(SO + "sensibilite_bruit_machine2.log"); casc = lire(SO + "stabilite_cascade_machine2.log")
lg = dict((int(m.group(1)), (m.group(2), m.group(3), m.group(4))) for m in re.finditer(r"^x(\d+) +\(bruit ([0-9.e-]+)\) : verdicts possibles sous le bruit : (\[.*?\]) \(rendu : L'ORDRE 2 TIENT\) (VERDICT \S+(?: \S+)?)", sens, re.M))
ok = (all(lg[n][2] == "VERDICT INCHANGE" and lg[n][1] == '["L\'ORDRE 2 TIENT"]' for n in range(1, 8)) and lg[8][2] == "VERDICT PEUT CHANGER"
      and lg[7][0] == "5.12e-13" and lg[8][0] == "5.86e-13" and all(x in lg[8][1] for x in ("NE TIENT PAS", "TIENT JUSQU'A 0.10", "\"L'ORDRE 2 TIENT\""))
      and "TIENT JUSQU'A 0.06" not in lg[8][1] and "bruit de base 7.32e-14" in sens and casc.count("-> INCHANGE") == 12 and "VERDICT INCHANGE" in casc
      and re.search(r"^L4 .* 1 etat\(s\) incertain\(s\)", casc, re.M)
      and [PT[k]["N"] for k in ("A1", "A2", "C1", "M3", "L4")] == [60, 61, 73, 74, 74] and sorted(k for k in ORDRE if PT[k]["N"] in (73, 74)) == ["C1", "L4", "M3"]
      and dans("bruit de la cible 7.32e-14", "inchange jusqu'a sept fois ce bruit (5.12e-13) ; a partir de huit fois (5.86e-13), NE TIENT PAS, TIENT JUSQU'A 0.10 et TIENT sont tous possibles",
               "aux boites de 60 et 61 ; il ne l'a pas ete a celles de 73 et 74 (C1, M3, L4)", "Un etat de L4 peut entrer ou sortir des etats juges"))
ctl("R15 nn.7 : le verdict sous le bruit des fils, relu dans les deux journaux de machine 2", ok)

# ---------------------------------------------------------------- R16 les annonces
sec8 = T[T.index("nn.8 LES ANNONCES"):T.index("nn.9 DEFAUTS")]
an = re.findall(r"^    (A-\d+) +\((0\.\d\d)\) (.*?) +(VRAIE|FAUSSE)(?:  ?\((.*)\))?$", sec8, re.M)
sg = gel[gel.index("12. ANNONCES DE LA PLUME"):gel.index("13. CE QUE CHAQUE ISSUE ENGAGE")]
pg = {}
for m in re.finditer(r"^  (A-\d+) +(.*?)(?=^  A-\d+ |^  Une annonce)", sg, re.M | re.S):
    pg[m.group(1)] = re.findall(r"\((0\.\d\d)\)", m.group(2))
attendu = {"A-2": ["0.85"], "A-3": ["0.80"], "A-4": ["0.60"], "A-5": ["0.70"], "A-6": ["0.80", "0.65"], "A-7": ["0.80", "0.65"], "A-8": ["0.85"],
           "A-9": ["0.90", "0.70"], "A-10": ["0.70"], "A-11": ["0.60"], "A-12": ["0.75", "0.70"], "A-13": ["0.65"], "A-14": ["0.65"], "A-15": ["0.95", "0.93", "0.97"]}
ok = len(an) == 20
par = {}
for (nom, pr, quoi, v, det) in an:
    par.setdefault(nom, []).append(pr)
ok = ok and par == attendu and all(pg[k][:len(v)] == v for k, v in attendu.items() if k not in ("A-5", "A-13")) and pg["A-5"][0] == "0.70" and pg["A-13"][0] == "0.65"
vrai = [
    all(PT[k]["tenu"] for k in par_bande[1.25]), all(PT[k]["tenu"] for k in par_bande[1.6]), all(PT[k]["tenu"] for k in par_bande[2.0]),
    PT["L2"]["tenu"], PT["L4"]["tenu"], 1.5 <= mq("L4", "q2", max) <= 1.9, PT["M4"]["tenu"], 1.35 <= mq("M4", "q2", max) <= 1.55,
    all(pire(k, "q2") < pire(k, "q1") for k in JUG), all(mq(k, "ee", max) <= 0.01 for k in JUG), max(mq(k, "ee", max) for k in JUG) < 0.006,
    all(mq(k, "q2", min) >= 0.95 for k in JUG), all(0.93 <= loi[k] <= 1.15 for k in JUG), any(x > 1.6 for x in w1), all(x < 2.5 for x in w1),
    PT["W2"]["lisible"], all(mq(k, "fi", max) < 0.05 for k in JUG), g4 <= 1e-2, g8f <= 1e-3 and g8e <= 1e-6, g6 <= 5e-5]
ok = ok and [x[3] == "VRAIE" for x in an] == vrai and sum(vrai) == 18
som = sum(float(x[1]) for x in an)
ok = ok and dans("18 annonces jugees sur 20 sont vraies", "est %.1f pour 18 vraies" % som, "A-11 (la loi apres coup, a L2) et A-13 (W2 n'est pas lisible)",
                 "0.45 a L'ORDRE 2 TIENT, 0.27 a TIENT JUSQU'A 0.10, 0.10 a TIENT JUSQU'A 0.06, 0.08 a NE TIENT PAS, 0.04 a NON LISIBLE, 0.06 a NON CONCLUANT D'INSTRUMENT")
ok = ok and "A-1  le verdict : L'ORDRE 2 TIENT 0.45 ; TIENT JUSQU'A 0.10 0.27 ; TIENT JUSQU'A 0.06 0.10 ; NE" in gel
det = dict(((x[0], x[2]), x[4]) for x in an)
ok = ok and det[("A-6", "son plus grand q2 est entre 1.5 et 1.9")] == f3(mq("L4", "q2", max)) and det[("A-7", "son plus grand q2 est entre 1.35 et 1.55")] == f3(mq("M4", "q2", max))
ok = ok and det[("A-11", "la mediane de q2 / loi est entre 0.93 et 1.15")] == "L2 : %s" % f3(loi["L2"]) and det[("A-5", "L2 est TENU")] == "plus petit q2 %s" % f3(mq("L2", "q2", min))
ctl("R16 nn.8 : vingt annonces, leurs probabilites relues dans le gel, leur verite recalculee ; 18 vraies, somme %.1f" % som, ok)

# ---------------------------------------------------------------- R17 defauts, reserves, sources
nc = " ".join(lire(LC + "POUR_MACHINE1_certification_gel_ordre2_machine2_v1.md").split()); nr = " ".join(lire(LR + "POUR_MACHINE1_resultat_ordre2_machine2_v1.md").split())
nt = " ".join(lire(NOTE).split()); a97 = " ".join(lire(CLONE + "/journal/journal_delta_97_domaine_G1_chaine_EA_v1.md").split())
ok = ("q1 de 0.375 a 6.987" in bl and "242 sur 243 (la note : 241)" in bl and "[0.375 ; 7.00]" in gel and "241" in nt
      and "pr\u00e9f\u00e8rent donc la somme des deux termes \u00e0 chacun pris seul" in nt
      and "vaut 1.7 fois le bruit" in nc and "il differe de 0.2 a 0.3 pour cent aux etats juges" in nc and "Gamma_flux de l'ordre 2, lui, differe de 1e-9" in nc
      and "Six de mes controles ont mordu" in nc and "UN DEFAUT DE MON OUTIL, PAS DU RESULTAT" in nr and "JOUE SUR BATTERIE" in nr
      and "0.85" in gel and "D-G1-3" in a97 and "deriver le residuel de la chaine" in a97 and "depend du facteur" in a97
      and "a ce que la plume suppose" in gel and '"ok go" a machine 1 le 14/11/2026 a 22 h 04' in gel
      and dans("7.00 pour 6.987", "241 etats sur 243 dans un facteur 1.5 pour 242", "vaut 1.7 fois le bruit", "0.2 a 0.3 pour cent",
               "six de ses controles ont mordu a ses premiers jets", "le plus petit q2 y est %s" % f3(mq("L2", "q2", min)),
               "son plus grand q2, %s, est au-dela de 1.6" % f3(mq("L4", "q2", max)), "\"ok go\", le 14/11/2026 a 22 h 04",
               "ou W1 va jusqu'a %s" % f3(max(w1)), "W2 a coute %d secondes sur batterie pour 3 etats juges" % ent(du["W2"])))
ctl("R17 nn.9, nn.10, nn.11 : les defauts et les reserves, relus dans la note, le gel, l'acte du delta 97 et les notes de machine 2", ok)
m13 = re.search(r"machine 1 -- le gel et ses instruments\s+([0-9a-f]{16}) ; machine 2 -- la certification\s+([0-9a-f]{16}), le resultat\s+([0-9a-f]{16})\.", T)
ctl("R18 nn.13 : les trois lots du canal", bool(m13) and m13.groups() == (lot_m1, lots["certification"], lots["resultat"]))
print("RELEVE : %d controles, %d tenus" % (len(res), sum(res)))
sys.exit(0 if all(res) else 1)
