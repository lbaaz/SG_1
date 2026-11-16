# -*- coding: ascii -*-
"""RELEVE de la seconde partie du gel "loi de la largeur, ordre 3" : controle de sortie de la plume, pas une certification.
Les nombres du texte sont refaits ici depuis les pieces par un code qui n'est pas celui de la construction ni celui des
marges : le texte est RELU (expressions regulieres), les chaines brutes des cellules et la feuille retrospective sont
recomptees.
Usage : python3 -I releve_gel_partie2_machine1_v1.py <gel.md> <dossier de la seconde partie> <dossier de la premiere partie>
        <clone du registre> <dossier du gel ter> <lot de machine 2 (certification)> <lot de machine 2 (tirage)>
        <fichier des canons connus.json> <ordre3_par_etat_v1.json de la note sur la loi>     (code 0 si aucun controle ne mord)"""
import sys, os, re, json, math, hashlib, unicodedata, subprocess, tempfile
from fractions import Fraction as F
GEL, D, D1, CLONE, DTER, M2CERT, M2TIR, CONNUS, PAR_ETAT = sys.argv[1:10]
T = open(GEL, "rb").read().decode("utf-8"); LG = T.split("\n"); U = re.sub(r"\s+", " ", T); RES = []
I = os.path.join(D, "instrument")
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n"); return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def ctl(nom, ok, detail=""):
    RES.append((nom, bool(ok))); print("%-4s %s  %s" % (nom, "TIENT" if ok else "MORD ", detail))
def mediane(v):
    v = sorted(v); return 0.5 * (v[(len(v) - 1) // 2] + v[len(v) // 2])
# R01 forme
try:
    T.encode("ascii"); asc = True
except UnicodeEncodeError:
    asc = False
ctl("R01", asc and "%" not in T and max(len(l) for l in LG) <= 100 and T.endswith("-- FIN gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1 --\n") and "\r" not in T
    and not any(l != l.rstrip() for l in LG), "ASCII %s ; pour cent %d ; plus longue ligne %d ; ligne de FIN ; pas d'espace en fin de ligne" % (asc, T.count("%"), max(len(l) for l in LG)))
# R02 empreintes : chaque suite de 16 hex du texte est le canon d'une piece tenue (recalcule) ou d'un lot connu (fichier des canons connus, avec le manifeste)
connus = json.load(open(CONNUS)); vus = sorted(set(re.findall(r"\b[0-9a-f]{16}\b", T))); mauvais = []
for h in vus:
    if h not in connus:
        mauvais.append(h + " inconnu"); continue
    ch = connus[h]
    if not os.path.exists(ch) or canon(ch) != h:
        mauvais.append("%s : %s ne rend pas ce canon" % (h, ch))
ctl("R02", not mauvais, "%d empreintes distinctes dans le texte, toutes recalculees depuis un fichier tenu ; en defaut : %s" % (len(vus), mauvais))
# R03 la table des cellules, relue dans le texte, contre mon tirage, celui de machine 2, et les deux tables d'eligibilite
lig = [re.match(r"\s+(N[1-5]|P[1-5]|BN|BP)\s+w2 = (\S+)\s+delta ([+-]\d\.\d{3})\s+x(\S+)\s+g = (\S+)\s+N = (\d+)\s+predits\s+(\d+) /\s+(\d+) /\s+(\d+)\s*$", l) for l in LG]
lig = [m.groups() for m in lig if m]
def tirage(ch, motif):
    return [(m.group(1), F(m.group(2)), F(m.group(3))) for m in (re.match(motif, l) for l in open(ch)) if m]
t1 = tirage(os.path.join(D, "tirage_machine1_v1_graine_200482.log"), r"\s+(N[1-5]|P[1-5]|BN|BP)\s+w2 = (\S+)\s+facteur (\S+)\s*$")
t2 = tirage(os.path.join(M2TIR, "controle_carte_machine2", "tirage_graine_200482_machine2_v1.log"), r"\s+(N[1-5]|P[1-5]|BN|BP)\s+w2 = (\S+) \(\S+\) facteur (\S+)\s*$")
texte = [(a, F(b), F(c)) for a, b, c_, c, *_ in lig]
E1 = {(r["creneau"], F(r["w2"]), F(r["facteur"])): r for r in json.load(open(os.path.join(D1, "eligibilite_candidates_v1.json")))["cellules"]}
E2 = {(r["creneau"], F(r["w2"]), F(str(r["facteur"]))): r for r in json.load(open(os.path.join(M2CERT, "controle_carte_machine2", "eligibilite_machine2_v1.json")))["cellules"]}
ok3 = len(lig) == 12 and texte == t1 == t2
for (i, w, dl, f, g, N, nj, nd, nh) in lig:
    k = (re.sub(r"\d", "", i), F(w), F(f)); a, b = E1[k], E2[k]
    ok3 = ok3 and abs(float(dl) - (float(F(w)) - 2.0)) < 5e-4 and abs(float(g) / a["g"] - 1.0) < 1e-4 and (int(N), int(nj), int(nd), int(nh)) == (a["N"], a["n_jug"], a["n_dom"], a["n_hors"]) == (b["N"], b["n_jug"], b["n_dom"], b["n_hors"])
TB = json.load(open(os.path.join(I, "table_points_gel_loi_ordre3_v1.json")))
tab = [(p["id"], F(p["w2"]), F(p["facteur"])) for p in TB["points"] if p["role"] == "juge"]; anc = [(p["id"], p["w2"], p["facteur"]) for p in TB["points"] if p["role"] == "ancre"]
ctl("R03", ok3 and tab == t1 and anc == [("A1", "39/20", "1/1"), ("A2", "41/20", "1/1")] and TB["graine"] == "200482",
    "12 cellules relues dans le texte = mon tirage = celui de machine 2 = la table gelee ; boite et comptes = ma table = celle de machine 2 ; 2 ancres")
# R04 les marges de 7.3, relues dans le texte, contre un recalcul depuis les chaines brutes et la feuille retrospective
RT = json.load(open(os.path.join(D, "feuille_ordre3_retrospective_v1.json"))); AN = json.load(open(os.path.join(D, "ancres_retrospectif_v1.json")))
neg, pos = [], []
for x in RT["cellules"]:
    for r in x["etats"]:
        if r["exclu"] is None and r["dans_le_domaine"]:
            (neg if x["delta"] < 0 else pos).append((r["ln_q3"], math.log(r["G3"] / r["G2"]), x["delta"]))
for r in AN["etats"]:
    if r["plateau"] and r["dans_le_domaine"]:
        (neg if r["delta"] < 0 else pos).append((r["plateau"]["ln_q3"], r["ln_G3_G2"], r["delta"]))
kmax = max(-a / b ** 2 for a, b, _ in neg if abs(b) >= 0.05); c3max = max(a / d ** 3 for a, _, d in pos)
brut = json.load(open(os.path.join(D1, "eligibilite_N_BN_BP_v1.json")))["cellules"] + json.load(open(os.path.join(D1, "eligibilite_P_v1.json")))["cellules"]
m4 = [re.match(r"\s+(N[1-5]|P[1-5]|BN|BP)\s+domaine\s+(\d+) \(\s*(\d+) a 0\.05\)\s+e_bord (\S+) a (\S+)\s+ln\(G3/G2\) (\S+)\s+attente (\S+)\s+marge (\S+)\s*$", l) for l in LG]
m4 = {m.group(1): m.groups()[1:] for m in m4 if m}; ok4 = len(m4) == 12; pire4 = 0.0
for (i, w, f) in t1:
    cc = [x for x in brut if F(x["w2"]) == w and F(x["facteur"]) == f]; assert len(cc) == 1
    dm = []
    for s in cc[0]["etats"]:
        if s["rang_predit"] is None or s["rang_predit"] >= 14 or s["vide"]:
            continue
        dans = s["e_bord"] < 0.7 and s["stab3"] is not None and s["stab3"] <= 0.05
        if dans and s["stable1"] and s["stable2"] and s["G3"] > 1.33e-12:
            dm.append(s)
    d = float(w) - 2.0; tol = [0.05 if s["e_bord"] < 0.3 else 0.10 for s in dm]; d32 = [math.log(s["G3"] / s["G2"][2]) for s in dm]
    if d < 0:
        att = [kmax * x * x for x in d32]; attente = max(att); marge = min(t / a for t, a in zip(tol, att))
    else:
        attente = c3max * d ** 3; marge = min(tol) / attente
    n, nb, e0, e1, dmed, a_t, m_t = m4[i]
    vals = (int(n) == len(dm), int(nb) == sum(t == 0.05 for t in tol), abs(float(e0) - min(s["e_bord"] for s in dm)) < 6e-4, abs(float(e1) - max(s["e_bord"] for s in dm)) < 6e-4,
            abs(float(dmed) - mediane(d32)) < 6e-5, abs(float(a_t) - attente) < 6e-5, abs(float(m_t) - marge) < 6e-3)
    ok4 = ok4 and all(vals); pire4 = max(pire4, abs(float(a_t) - attente))
ctl("R04", ok4, "12 lignes de marges relues dans le texte ; recalcul independant (k le plus grand %.4f, coefficient de la puissance 3 le plus grand %.1f) : pire ecart sur l'attente %.1e" % (kmax, c3max, pire4))
# R05 la table par classe de 7.1 ; et la feuille retrospective contre le fichier par etat de la note sur la loi
m5 = [re.match(r"\s+e_bord dans \[(\S+), (\S+)\[\s+(\d+) etats\s+mediane (\S+)\s+plus grand (\S+)\s*$", l) for l in LG]; m5 = [m.groups() for m in m5 if m]; ok5 = len(m5) == 3
dom = [r for x in RT["cellules"] for r in x["etats"] if r["exclu"] is None and r["dans_le_domaine"]]
for lo, hi, n, md, mx in m5:
    v = [abs(r["ln_q3"]) for r in dom if float(lo) <= r["e_bord"] < float(hi)]
    ok5 = ok5 and int(n) == len(v) and abs(float(md) - mediane(v)) < 6e-5 and abs(float(mx) - max(v)) < 6e-5
note = PAR_ETAT; pire5 = None
if os.path.exists(note):
    O = {(i, s["rang"]): s for i, p in json.load(open(note))["points"].items() for s in p["etats"]}
    pire5 = max(abs(r["G3"] / O[(x["id"], r["rang"])]["G_c3"] - 1.0) for x in RT["cellules"] for r in x["etats"] if r["exclu"] is None)
ctl("R05", ok5 and len(dom) == 56 and pire5 is not None and pire5 < 1e-9, "3 classes relues, %d etats du domaine ; largeur d'ordre 3 de la feuille contre le fichier par etat de la note sur la loi : pire ecart relatif %s" % (
    len(dom), ("%.1e" % pire5) if pire5 is not None else "fichier absent"))
# R06 les constantes des sections 5 et 6 sont celles de la feuille
fo3 = open(os.path.join(I, "feuille_ordre3_machine1_v1.py"), encoding="ascii").read()
attendu = ["E_MAX = 0.7; STAB_MAX = 0.05; J_NET = 0.2; E_BAS = 0.3; T_BAS = 0.05; T_HAUT = 0.10", "DOM_MIN = 5; BORD_MIN = 2; PART_JUGES = F(2, 3); PART_E2 = F(3, 4); INEXPLOITABLES_E1 = 2; INEXPLOITABLES_E2 = 1; N_ETATS = 14",
           "BANDES = ((0.06, 1.25), (0.10, 1.6), (0.12, 2.0))", 'issue(lig, "E1", INEXPLOITABLES_E1, 1)', 'issue(ligN, "E2", INEXPLOITABLES_E2, 1)', 'issue(brd, "E1", 0, 0)', "EF = 0.0625"]
phrases = ["e_bord < 0.7 et que la stabilite de sa chaine d'ordre 3 soit definie et <= 0.05", "T = 0.05 si e_bord < 0.3 et T = 0.10 sinon", "au moins les deux tiers de ses etats lus soient juges",
           "au moins 5 etats juges dans le domaine", "au moins 2 dans le domaine et au moins 2 hors du domaine", "au moins les trois quarts (arrondis par exces)", "1.25 pour |delta| <= 0.06, 1.6 jusqu'a 0.10",
           "ecart-type de J < 0.2", "au facteur d'eta 1/16", "NON CONCLUANT si plus de deux cellules sont inexploitables", "NON CONCLUANT si plus d'une cellule est inexploitable"]
ctl("R06", all(a in fo3 for a in attendu) and all(p in U for p in phrases), "constantes de la feuille : %d sur %d ; phrases du texte qui les portent : %d sur %d" % (
    sum(a in fo3 for a in attendu), len(attendu), sum(p in U for p in phrases), len(phrases)))
# R07 les scripts derives se reconstruisent a l'octet depuis leurs sources certifiees
tmp = tempfile.mkdtemp(); r = subprocess.run([sys.executable, "-I", "-B", os.path.join(D, "construction_instrument_gel_loi_machine1_v1.py"), os.path.join(CLONE, "scripts", "sonde_ordre2_machine1_v1.py"),
     os.path.join(DTER, "sonde_qualification_EB_ter_machine1_v1.py"), os.path.join(DTER, "lecture_qualification_EB_ter_machine1_v1.py"), os.path.join(D, "tirage_machine1_v1_graine_200482.log"), tmp], capture_output=True, text=True)
noms = ["table_points_gel_loi_ordre3_v1.json", "table_points_prevol_gel_loi_ordre3_v1.json", "sonde_dense_gel_loi_machine1_v1.py", "sonde_lecteur_gel_loi_machine1_v1.py", "lecture_lecteur_gel_loi_machine1_v1.py",
        "sonde_dense_gel_loi_machine1_v1.diff", "sonde_lecteur_gel_loi_machine1_v1.diff", "lecture_lecteur_gel_loi_machine1_v1.diff"]
ident = r.returncode == 0 and all(open(os.path.join(tmp, n), "rb").read() == open(os.path.join(I, n), "rb").read() for n in noms)
ctl("R07", ident, "construction rejouee dans un dossier neuf (code %d) : %d fichiers identiques a l'octet a ceux de l'instrument" % (r.returncode, len(noms)))
# R08 les canons portes en dur par les scripts sont ceux des pieces
cn = {n: canon(os.path.join(I, n)) for n in os.listdir(I) if n.endswith((".py", ".json"))}
pil = open(os.path.join(I, "pilote_gel_loi_machine1_v1.py"), encoding="ascii").read(); sl = open(os.path.join(I, "sonde_lecteur_gel_loi_machine1_v1.py"), encoding="ascii").read()
fl = open(os.path.join(I, "lecture_lecteur_gel_loi_machine1_v1.py"), encoding="ascii").read(); sd = open(os.path.join(I, "sonde_dense_gel_loi_machine1_v1.py"), encoding="ascii").read()
tb, cd, cs, cf, co = (cn["table_points_gel_loi_ordre3_v1.json"], cn["sonde_dense_gel_loi_machine1_v1.py"], cn["sonde_lecteur_gel_loi_machine1_v1.py"], cn["lecture_lecteur_gel_loi_machine1_v1.py"],
                      cn["feuille_ordre3_machine1_v1.py"])
ok8 = ('CANON_MOTEUR, CANON_TABLE = "82a0be882568fe0c", "%s"' % tb in sd and 'CANON_TABLE, CANON_SONDE_DENSE, CANON_SONDE_DEPOT, N_ETATS_DENSE = "%s", "%s", "24315c52b234319c", 14' % (tb, cd) in sl
       and 'CANON_SONDE = "%s"' % cs in fl and 'CANON_TABLE, CANON_SONDE_DENSE, CANON_SONDE_DEPOT, N_ETATS_DENSE = "%s", "%s", "24315c52b234319c", 14' % (tb, cd) in fl
       and 'CANON_TABLE, CANON_SONDE_DENSE, CANON_FEUILLE_LECTEUR = "%s", "%s", "%s"' % (tb, cd, cf) in fo3
       and all('"%s": "%s"' % (k, v) in pil for k, v in (("table", tb), ("sonde_dense", cd), ("sonde_lecteur", cs), ("feuille_lecteur", cf), ("feuille_ordre3", co)))
       and cn["ordre3_bloc_machine1_v1.py"] == "534ba246aa3b8973" and all(h in T for h in (tb, cd, cs, cf, co, cn["pilote_gel_loi_machine1_v1.py"])))
ctl("R08", ok8, "canons en dur de la sonde dense, de la sonde du lecteur, des deux feuilles et du pilote = canons des pieces ; ils sont dans le texte")
# R09 bancs, selftest, pre-vol : relus dans leurs journaux
bo = open(os.path.join(D, "banc_feuille_ordre3_machine1_v1.log")).read(); bl = open(os.path.join(D, "banc_feuille_lecteur_sur_derivee_v1.log")).read(); st = open(os.path.join(D, "selftest_feuille_lecteur_derivee_v1.log")).read()
pv = open(os.path.join(D, "comparaison_prevol_machine1_v1.log")).read()
ok9 = ("BANC DE LA FEUILLE D'ORDRE 3 : 17 mutations, 17 mordent comme attendu : TIENT" in bo and bo.count(" MORD ") == 17 and "BANC : 43 alterations, 43 mordues, 0 survivantes" in bl and "selftest : 68 tenus sur 68" in st
       and "PRE-VOL : 5 controles, 5 tiennent" in pv and "17 mutations, 17 mordent" in U and "mord a 43 alterations sur 43" in U and "(68 cas sur 68)" in U)
ctl("R09", ok9, "banc de la feuille d'ordre 3 17 sur 17 ; banc certifie sur la feuille du lecteur derivee 43 sur 43 ; selftest 68 sur 68 ; pre-vol 5 sur 5 ; le texte dit ces nombres")
# R10 les annonces somment a un
a2 = re.search(r"A-2 E1 : TENU (\S+) ; TENU SAUF UNE CELLULE (\S+) ; TOMBE (\S+) ; NON CONCLUANT (\S+) ; le reste \((\S+)\)", U); a4 = re.search(r"A-4 E2 : TENU (\S+) ; TENU SAUF UNE CELLULE (\S+) \(N1\) ; TOMBE (\S+) ; NON CONCLUANT (\S+) ; le reste \((\S+)\)", U)
a1 = re.search(r"A-1 \((\S+)\) l'instrument tient", U)
ok10 = bool(a1 and a2 and a4) and abs(sum(float(x) for x in a2.groups()) - 1.0) < 1e-9 and abs(sum(float(x) for x in a4.groups()) - 1.0) < 1e-9 and abs(float(a2.group(5)) - (1.0 - float(a1.group(1)))) < 1e-9
ctl("R10", ok10, "annonces A-2 et A-4 : chacune somme a 1 ; leur reste est le complement de A-1")
# R11 l'essai a blanc hors cellules : relu dans son journal ; les pieces qu'il a eprouvees sont celles de l'instrument
eb = open(os.path.join(D, "essai_a_blanc_hors_cellules_machine1_v1.log")).read(); EBJ = json.load(open(os.path.join(D, "essai_a_blanc_hors_cellules_v1.json")))
ok11 = ("ESSAI A BLANC HORS CELLULES : 6 essais, 6 tiennent" in eb and eb.count(" TIENT ") == 6 and "Six essais, tous tenus" in U and all(EBJ["canons"][n_] == cn[n_] for n_ in EBJ["canons"])
        and all(re.sub(r"\s+", " ", x["detail"]) in U for x in EBJ["essais"]))
ctl("R11", ok11, "essai a blanc hors cellules : 6 sur 6 ; les %d pieces qu'il a eprouvees ont les canons de l'instrument ; ses six lignes sont dans le texte" % len(EBJ["canons"]))
n = sum(1 for _, o in RES if not o)
print("RELEVE : %d controles, %d mordent" % (len(RES), n)); sys.exit(0 if n == 0 else 1)
