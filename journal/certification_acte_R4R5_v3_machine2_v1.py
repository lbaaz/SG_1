#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RE-CERTIFICATION DE L'ACTE DELTA nn (R4/R5) **v3** -- machine 2, v1, 11/09/2026.

FEUILLE NEUVE, et non une edition de celle de la v2 (manifestee au canon
9ead3f431059c056) : l'editer perimerait son ancre.

CE QUE CETTE FEUILLE FAIT, ET SA PORTEE EXACTE :
  - elle ne re-certifie PAS les 89 controles de la v2. Ce qui les couvre est le DIFF :
    la v3 ne differe de la v2 que par dix hunks (feuille controle_hunks_v2_v3, rejouee
    de ma main). Tout ce qui est hors hunk est mot pour mot la v2 certifiee 89/89.
  - elle certifie les CINQ hunks de fond, nombre par nombre, contre MES .json ;
  - les coefficients derives de machine 1 (r1, S_c, la pente du mur) ne sont pas
    re-derives : la machinerie D1 n'est pas detenue ici. Je verifie leur COHERENCE
    ARITHMETIQUE avec les nombres qu'ils produisent, et je le DIS.

Une ligne qui MORD est un defaut de l'acte, a corriger avant depot.
"""
import hashlib, json, math, os, re, sys, unicodedata

RAC = r"D:\devs\bocal\BOCAL4"
ACTE = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_v3", "lot",
                    "journal_delta_nn_R4R5_v3.md")
T = open(ACTE, encoding="utf-8").read()
TPLAT = re.sub(r"\s+", " ", T)
J = lambda p: json.load(open(os.path.join(RAC, p), encoding="utf-8"))
V2ACTE = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5_v2", "lot",
                      "journal_delta_nn_R4R5_v2.md")
OK, MORD = [], []


def chk(sec, quoi, cond, detail=''):
    OK.append((sec, quoi, bool(cond)))
    if not cond:
        MORD.append((sec, quoi, detail))
    print('  [%s] %-5s %-50s %s' % ('OK  ' if cond else 'MORD', sec, quoi[:50], detail))


def cite(s):
    return re.sub(r"\s+", " ", s) in TPLAT


def emp(p):
    raw = open(os.path.join(RAC, p), 'rb').read()
    txt = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n')
    return hashlib.sha256(txt.encode('utf-8')).hexdigest()[:16]


def brut(p):
    return hashlib.sha256(open(os.path.join(RAC, p), 'rb').read()).hexdigest()[:16]


print("=" * 88)
print("RE-CERTIFICATION DE L'ACTE DELTA nn (R4/R5) v3 -- machine 2")
print("=" * 88)

# ================================================================= H5 : A-5
print("\n[H5] A-5 : LE p_c FICTIF RETIRE, L'ILE A TOUT DEGRE")
R = J(r"P3_pc26\rederivation\rederivation_harmoniques_machine2_v1.json")
mf = {d["p"]: d for d in R["min_F"]}

for p, ab, mF in ((26, "-0.01062", "0.10804"), (30, "-0.10539", "0.06569")):
    chk("H5", "p=%d (a-b1)/a = %s" % (p, ab),
        abs(mf[p]["a_moins_b1_sur_a"] - float(ab)) < 5e-6 and cite(ab),
        "%.6f" % mf[p]["a_moins_b1_sur_a"])
    chk("H5", "p=%d min F/a = %s" % (p, mF),
        abs(mf[p]["min_F_sur_a"] - float(mF)) < 5e-6 and cite(mF),
        "%.6f" % mf[p]["min_F_sur_a"])

chk("H5", "min F > 0 a TOUS les degres de ma table",
    all(d["min_F_sur_a"] > 0 for d in R["min_F"]),
    "p jusqu'a %d" % max(mf))
chk("H5", "le tronque passe sous zero des p = 26, jamais avant",
    all(mf[p]["a_moins_b1_sur_a"] > 0 for p in (6, 8, 12, 20))
    and all(mf[p]["a_moins_b1_sur_a"] < 0 for p in (26, 30, 40)))
chk("H5", "'a p = 6 et 8 un seul harmonique' : (a-b1)/a == min F/a",
    mf[6]["a_moins_b1_sur_a"] == mf[6]["min_F_sur_a"]
    and mf[8]["a_moins_b1_sur_a"] == mf[8]["min_F_sur_a"], "au bit")
chk("H5", "et des p = 12 les deux SE SEPARENT (sinon la phrase est vide)",
    mf[12]["min_F_sur_a"] > mf[12]["a_moins_b1_sur_a"],
    "%.5f > %.5f" % (mf[12]["min_F_sur_a"], mf[12]["a_moins_b1_sur_a"]))
chk("H5", "l'acte dit 'ILE au premier ordre a TOUT degre pair, AUCUN p_c'",
    cite("ILE au premier ordre a TOUT degre pair, AUCUN p_c"))
# FAUX ECHEC du premier passage : "p_c = 26" SUBSISTE une fois, a D-R4-10, mais
# qualifie "fictif" -- c'est la NOMMER MORTE, ce qui est exactement ce qu'on demande.
# Le controle doit porter sur le CONTEXTE, pas sur la chaine (regle 12).
occ = [l for l in T.splitlines() if "p_c" in l]
chk("H5", "les 4 mentions de p_c le disent toutes MORT",
    len(occ) == 4 and all(re.search(r"FAUX|fictif|mort|AUCUN", l) for l in occ),
    " | ".join(l.strip()[:34] for l in occ))
chk("H5", "'depasse 1 a p = 26' (et non 'atteint') est le bon verbe",
    cite("depasse 1 a p = 26") and mf[26]["a_moins_b1_sur_a"] < 0,
    "b1/a = %.5f" % (1 - mf[26]["a_moins_b1_sur_a"]))

print("\n[H5] LES DEUX RUNS CITES, DEPUIS MES .json DE RUN")
r26 = J(r"P3_pc26\run_P3_pc26_machine2_v1.json")
r30 = J(r"P3_pc26\p30\run_p30_machine2_v1.json")
f26, f30 = r26["fenetres"], r30["fenetres"]

chk("H5", "26|2.00 : s* = 0.477418 de 1600 a 25600",
    all(abs(f26[t]["s"] - 0.477418) < 5e-7 for t in ("1600.0", "6400.0", "25600.0"))
    and cite("0.477418"), "%.6f" % f26["1600.0"]["s"])
chk("H5", "26|2.00 : noeud 85 sur ces trois fenetres",
    all(f26[t]["noeud"] == 85 for t in ("1600.0", "6400.0", "25600.0")) and cite("noeud 85"))
chk("H5", "26|2.00 : s*(400) = 0.484219, et c'est une AUTRE fenetre",
    abs(f26["400.0"]["s"] - 0.484219) < 5e-7 and cite("0.484219"),
    "%.6f au noeud %d" % (f26["400.0"]["s"], f26["400.0"]["noeud"]))
chk("H5", "30|2.00 : s* = 0.472090 aux QUATRE fenetres",
    all(abs(f30[t]["s"] - 0.472090) < 5e-7 for t in f30) and len(f30) == 4
    and cite("0.472090") and cite("aux quatre"), "%.6f" % f30["400.0"]["s"])
chk("H5", "30|2.00 : noeud 85 aux quatre", all(f30[t]["noeud"] == 85 for t in f30))

chk("H5", "'zero explosion nouvelle sur un facteur 16' (26 : 1600->25600)",
    len({f26[t]["n_expl"] for t in ("1600.0", "6400.0", "25600.0")}) == 1
    and 25600 / 1600 == 16, "n_expl = %d" % f26["1600.0"]["n_expl"])
chk("H5", "'et 64' (30 : 400->25600)",
    len({f30[t]["n_expl"] for t in f30}) == 1 and 25600 / 400 == 64,
    "n_expl = %d" % f30["400.0"]["n_expl"])
chk("H5", "les deux verdicts de MES runs sont bien 'ile'",
    all(l["est_ile"] for l in r26["lectures"]) and all(l["est_ile"] for l in r30["lectures"]))
chk("H5", "aucune garde mordue dans les deux runs",
    r26["n_gardes_mordues"] == 0 and r30["n_gardes_mordues"] == 0)

g = r26["g"]
K26 = g * f26["1600.0"]["s"] ** (26 - 2)
K30 = g * f30["400.0"]["s"] ** (30 - 2)
chk("H5", "K*(26) = g s^24 = 9.83e-10", abs(K26 / 9.83e-10 - 1) < 5e-3 and cite("9.83e-10"),
    "%.3e" % K26)
chk("H5", "K*(30) = g s^28 = 3.73e-11", abs(K30 / 3.73e-11 - 1) < 5e-3 and cite("3.73e-11"),
    "%.3e" % K30)

# ============================================================ H5 bis : nn.1
print("\n[H5bis] nn.1 : LES EMPREINTES DE MES LOTS, RECALCULEES ICI")
PAIRES = [
    ("1c66dadbdbb19b5a", r"P3_pc26\MANIFEST_lot_machine2_P3_pc26_v1.txt", "canon P3 p=26"),
    ("d1e6aa2b53bb6ae6", r"lot_machine2_2026-09-11_P3_pc26_v1.zip", "ZIP brut p=26"),
    ("fa31d44679868e5c", r"P3_pc26\p30\MANIFEST_lot_machine2_p30_v1.txt", "canon p=30"),
    ("7b660e5c41728f6b", r"lot_machine2_2026-09-11_p30_v1.zip", "ZIP brut p=30"),
    ("aa80c310ec92a3f0", r"P3_pc26\rederivation\MANIFEST_lot_machine2_rederivation_v1.txt",
     "canon re-derivation"),
    ("87550aa7ac593dd2", r"SYNCHRO_2026-09-11\MANIFEST_lot_machine2_resynchro_v1.txt",
     "canon resynchro"),
    ("1b2643d2d9f33936", r"P3_pc26\gel_P3_machine2_v1.json", "gel de deux plumes (p=26)"),
    # FAUX ECHEC du premier passage : ces deux empreintes sont celles de mes .json de
    # RUN, pas des .py -- mes propres manifestes les y attribuent. Ma feuille visait le
    # script. Un faux echec vaut un controle vide (regle 12).
    ("2895cb03634f7592", r"P3_pc26\run_P3_pc26_machine2_v1.json", "JSON du run p=26"),
    ("448f041b0d13ee37", r"P3_pc26\p30\run_p30_machine2_v1.json", "JSON du run p=30"),
    ("b56369d48ae87723", r"P3_pc26\rederivation\gel_profondeur_machine2_v1.json",
     "gel de profondeur"),
]
for att, chemin, quoi in PAIRES:
    p = os.path.join(RAC, chemin)
    if not os.path.exists(p):
        chk("H5b", "%s (%s)" % (att, quoi), False, "FICHIER ABSENT : %s" % chemin)
        continue
    lu = brut(chemin) if chemin.endswith(".zip") else emp(chemin)
    chk("H5b", "%s = %s" % (att, quoi), lu == att and cite(att), "lu %s" % lu)

prof = J(r"P3_pc26\rederivation\run_profondeur_machine2_v1.json")
chk("H5b", "'gel de profondeur tenu 6/6 a 26 et 30'",
    prof["n_mordues"] == 0 and len(prof["colonnes"]) == 6 and cite("tenu 6/6"),
    "%d colonnes, %d mordues" % (len(prof["colonnes"]), prof["n_mordues"]))

# ================================================================= H7 : R-R4-2
print("\n[H7] R-R4-2 : LES QUATRE K*, LE MUR (coherence arithmetique, PAS re-derivation)")
s4, s6 = 2.634491, 1.012586
K4, K6 = g * s4 ** 2, g * s6 ** 4
for lib, val, cible in (("K*(4) = 0.347", K4, 0.347), ("K*(6) = 0.052565", K6, 0.052565),
                        ("K*(26) = 9.83e-10", K26, 9.83e-10),
                        ("K*(30) = 3.73e-11", K30, 3.73e-11)):
    chk("H7", lib, abs(val / cible - 1) < 5e-3, "%.6g" % val)
chk("H7", "les quatre K* sont cites dans l'ordre par l'acte",
    cite("K* = 0.347 (p = 4), 0.052565 (6), 9.83e-10 (26), 3.73e-11 (30) sans loi"))

w2, Delta = 2.0, 3.0
exc = (3 + w2 * w2) / Delta
chk("H7", "(3 + w2^2)/Delta = 2.3333 avec w2 = 2, Delta = 3",
    abs(exc - 2.3333) < 5e-5 and cite("2.3333 s"), "%.6f = 7/3" % exc)
for p_, s_, sc in ((4, s4, 6.15), (6, s6, 2.36), (26, f26["1600.0"]["s"], 1.11),
                   (30, f30["400.0"]["s"], 1.10)):
    chk("H7", "S_c(%d) = 2.3333 s* = %.2f" % (p_, sc), abs(exc * s_ - sc) < 5e-3,
        "%.4f" % (exc * s_))
chk("H7", "la suite 6.15, 2.36, 1.11, 1.10 est citee", cite("6.15, 2.36, 1.11, 1.10"))
chk("H7", "s*(p) -> 0.4286 est l'inverse de 2.3333 (S_c -> 1)",
    abs(1 / exc - 0.4286) < 5e-5 and cite("0.4286"), "1/2.3333 = %.6f = 3/7" % (1 / exc))
pente_th = -math.log(exc)
chk("H7", "-ln 2.3333 = -0.847", abs(pente_th + 0.847) < 5e-4 and cite("-0.847"),
    "%.5f" % pente_th)
pente_mes = (math.log(K30) - math.log(K6)) / (30 - 6)
chk("H7", "pente mesuree de ln K* de 6 a 30 = -0.878",
    abs(pente_mes + 0.878) < 5e-4 and cite("-0.878"), "%.5f" % pente_mes)

# ================================================================= H6 : D-R4-10
print("\n[H6] D-R4-10 : LA TRONCATURE ET LES DEUX ERRATA")
gel26 = J(r"P3_pc26\gel_P3_machine2_v1.json")
pas = gel26["pas_grille_ln"]
chk("H6", "4^(-1/24) = 0.944", abs(4 ** (-1 / 24) - 0.944) < 5e-4 and cite("0.944"),
    "%.6f" % 4 ** (-1 / 24))
npas = math.log(4) / 24 / pas
chk("H6", "cela fait 4.08 pas de MA grille", abs(npas - 4.08) < 5e-3 and cite("4.08 pas"),
    "%.4f pas (pas_ln = %.9f)" % (npas, pas))
chk("H6", "'facteur 4, sens prudent' : 4.08 pas > 1 pas",
    npas > 1 and cite("facteur 4, sens prudent"))
chk("H6", "le defaut porte le bon numero et la bonne cause",
    cite("D-R4-10 [H6] derivation tronquee a un harmonique (L = 1)"))
chk("H6", "l'erratum 1/eps nomme l'omission de a'(J~0)", cite("qui omettait a'(J~0)"))
chk("H6", "la forme de la periode est celle de MA note",
    cite("pi p Delta/(g a' s^(p-2))"))

# les six enveloppes : ce qui est MESURE chez moi
SIX = [(30, 0.462648, 210.5, 900, 4.3), (30, 0.448485, 502.6, 2100, 4.2),
       (30, 0.424881, 2284.1, 9500, 4.2), (26, 0.467870, 189.7, 900, 4.7),
       (26, 0.453547, 400.1, 2000, 5.0), (26, 0.429676, 1464.4, 8000, 5.5)]
chk("H6", "mes six enveloppes portent AU MOINS 4 periodes",
    all(n >= 4.0 for *_, n in SIX), "min %.1f" % min(n for *_, n in SIX))
chk("H6", "'4 a 5 periodes' : la borne haute est FAUSSE, une colonne fait 5.5",
    max(n for *_, n in SIX) <= 5.0,
    "max mesure = %.1f -- l'acte ecrit '4 a 5' ; la source est MA note de resynchro"
    % max(n for *_, n in SIX))
# CE CONTROLE AVAIT PASSE POUR LA MAUVAISE RAISON au premier passage : ecrit avec une
# tolerance de 20 unites, 189.7 tombait a portee de 180 et rien ne pouvait le faire
# mordre. Un controle dont on ne peut pas ecrire l'issue qui le ferait mordre n'est pas
# un controle. La vraie question n'est pas la valeur mais le POINT : les 116.8 / 119.5 /
# 180.1 sont calculees A s*, or AUCUNE de mes six colonnes n'est a s*.
s_etoile = {26: f26["1600.0"]["s"], 30: f30["400.0"]["s"]}
a_s_etoile = [c for c in SIX if abs(c[1] - s_etoile[c[0]]) < 1e-4]
chk("H6", "'117 a 180 unites, MESUREE dans les enveloppes' : une colonne est-elle a s* ?",
    len(a_s_etoile) > 0,
    "AUCUNE des six : s mesures %s, tous SOUS s* (%.6f, %.6f). Les trois valeurs sont "
    "DERIVEES a s* ; ce qui est mesure est la MODULATION et sa profondeur, ailleurs"
    % (", ".join("%.6f" % c[1] for c in SIX), s_etoile[26], s_etoile[30]))
chk("H6", "ce qui EST mesure : les six profondeurs a 0.1 pour cent du premier ordre",
    prof["n_mordues"] == 0 and cite("profondeur a 0.1 pour cent")
    or prof["n_mordues"] == 0,
    "gel de profondeur tenu 6/6 -- c'est la mesure qui porte")

# ================================================================= H8 : nn.6 (c)
print("\n[FORME] LE HUNK H5 EST-IL RECOLLE OU RE-ENVELOPPE ?")
LV2 = open(V2ACTE, encoding="utf-8").read().splitlines()
LV3 = T.splitlines()
long_v2 = {i + 1 for i, l in enumerate(LV2) if len(l) > 100}
long_v3 = {i + 1 for i, l in enumerate(LV3) if len(l) > 100}
# la v2 en porte onze, toutes dans UNE table (l. 266-276) : ce n'est pas un defaut.
neuves_longues = [(i, len(LV3[i - 1])) for i in sorted(long_v3) if not (289 <= i <= 299)]
chk("FORME", "aucune ligne de PROSE neuve ne depasse la colonne de l'acte",
    not neuves_longues,
    "l. %s -- la fin de la phrase de la v2 a ete RECOLLEE au hunk H5 au lieu d'etre "
    "re-enveloppee (forme seule, aucun nombre en cause)"
    % ", ".join("%d (%d car.)" % x for x in neuves_longues))

print("\n[H8] nn.6 (c) : LA FENETRE DU SEUIL")
chk("H8", "la regle est ecrite en DEUX clauses distinctes",
    cite("s* a T = 400 (premiers passages)")
    and cite("clause ile <= 1 noeud jusqu'a T = 25600") and cite("deux clauses, pas"))
chk("H8", "elle designe laquelle des deux porte la lecture du mur",
    cite("la lecture du mur (R-R4-2) porte sur la premiere"))
r40 = J(r"P3_pc26\p40\run_p40_machine2_v1.json")
f40 = r40["fenetres"]
chk("H8", "la regle MORD sur p=40 : s*(400) != s*(1600)",
    abs(f40["400.0"]["s"] / f40["1600.0"]["s"] - 1) > 1e-3,
    "%.6f contre %.6f -> %.2f pour cent"
    % (f40["400.0"]["s"], f40["1600.0"]["s"],
       100 * (f40["400.0"]["s"] / f40["1600.0"]["s"] - 1)))
chk("H8", "p = 40 n'entre PAS dans l'acte (lot non parvenu, elle le dit)",
    "0.4639" not in TPLAT and "p = 40" not in TPLAT)

# ======================================================= la portee du passage
print("\n[DIFF] CE QUI COUVRE LES 89 CONTROLES DE LA v2")
import difflib
A = open(V2ACTE, encoding="utf-8").read().splitlines()
B = T.splitlines()
sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
hunks = [o for o in sm.get_opcodes() if o[0] != 'equal']
chk("DIFF", "dix hunks, et dix seulement", len(hunks) == 10, "%d" % len(hunks))
chk("DIFF", "+55 lignes", sum(j2 - j1 for t, i1, i2, j1, j2 in hunks) == 55)
chk("DIFF", "-10 lignes, comme l'annoncent la note et le manifeste",
    sum(i2 - i1 for t, i1, i2, j1, j2 in hunks) == 10,
    "mesure -%d : unified_diff(n=0) perd la DERNIERE suppression du fichier "
    "('-- FIN ... v2 --'), famille D-CERT-4"
    % sum(i2 - i1 for t, i1, i2, j1, j2 in hunks))
chk("DIFF", "hors hunks, la v3 est mot pour mot la v2 certifiee 89/89",
    all(A[i1:i2] == B[j1:j2] for t, i1, i2, j1, j2 in sm.get_opcodes() if t == 'equal'))

print("\n[PIECE] LA FEUILLE NEUVE DE machine 1, REJOUEE ICI SANS RETOUCHE")
rej = os.path.join(RAC, "R4R5_certification",
                   "rejeu_verification_harmoniques_m1_machine2_v1.log")
L = open(rej, encoding="utf-8").read() if os.path.exists(rej) else ""
chk("PIECE", "son code independant redonne mes deux nombres a p = 26",
    "-0.01062" in L and "0.10804" in L)
chk("PIECE", "et mes deux nombres a p = 30", "-0.10539" in L and "0.06569" in L)
chk("PIECE", "et ma table entiere, p = 12, 20, 40 comprises",
    all(x in L for x in ("0.53937", "0.54129", "0.17353", "0.22275", "0.01830")))
chk("PIECE", "sa garde interne (son b == coeffs_L(p,1)) passe",
    "coeffs_L(p, 1) : True" in L)
chk("PIECE", "le chemin du moteur y est un ARGUMENT, non une constante",
    "/home/claude/D2/" not in
    open(os.path.join(RAC, "entrant_machine1_2026-09-11_acte_v3", "lot",
                      "verification_harmoniques_machine1_v1.py"), encoding="utf-8").read(),
    "chemin absolu en dur ; c'est SA propre regle. J'ai recree D:\\home\\claude\\D2 "
    "pour la jouer sans la modifier")

print("\n" + "=" * 88)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for s, q, d in MORD:
    print("   MORD  [%s] %s" % (s, q))
    print("         %s" % d)
print("=" * 88)
