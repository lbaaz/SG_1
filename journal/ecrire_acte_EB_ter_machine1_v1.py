# -*- coding: ascii -*-
"""ECRITURE DE L'ACTE DU RUN DU GEL "QUALIFICATION E-B TER" -- machine 1, v1, 2026-11-15.
Chaque nombre de l'acte est lu d'une piece ou recalcule ici : les quinze sorties de la sonde jouee par machine 2
(recalcul des fenetres et des statuts par un code a part, compare a la feuille rejouee par machine 1 et au verdict de
BOCAL4), le depot du delta 98 et son verdict, les notes, journaux et manifestes recus, le gel, le clone du registre,
le rejeu de machine 1.
Arguments : <recu> <dossier du gel> <manifeste du lot du gel> <note hors chaine> <manifeste du lot de la note>
            <clone du registre> <dossier de sortie (le lot de l'acte)>."""
import sys, os, re, json, math, hashlib, unicodedata, textwrap, subprocess, statistics
from fractions import Fraction as Fr
RECU, GEL, MANIF_GEL, NOTE, MANIF_NOTE, CLONE, SORTIE = sys.argv[1:8]
NOM = "journal_delta_nn_qualification_EB_ter_v1"

def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def lire(p):
    return open(p, encoding="utf-8").read().replace("\r\n", "\n")
def plat(t):
    return " ".join(t.split())
def manifeste(p):
    out = {}
    for l in lire(p).splitlines():
        m = re.match(r"^([0-9a-f]{16})\s+[0-9a-f]{16}\s+\d+\s+\d+\s+(\S+)$", l)
        if m: out[m.group(2)] = m.group(1)
    return out

ENV = RECU + "/env/"
LR, LC = RECU + "/lot_resultat_EB_ter/", RECU + "/lot_certification_gel_EB_ter/"
LJ, LL = RECU + "/lot_rejeu_absorbeurs_longs_hors_chaine/", RECU + "/lot_lecteur_creux_hors_chaine/"
RUN = LR + "run_EB_ter/"
MR, MC = manifeste(ENV + "MANIFEST_lot_machine2_resultat_EB_ter_v1.txt"), manifeste(ENV + "MANIFEST_lot_machine2_certification_gel_EB_ter_v1.txt")
assert len(MR) == 43 and len(MC) == 28
for man, racine in ((MR, LR), (MC, LC)):
    for f, c in man.items():
        assert B(racine + f) == c, "piece hors canon : %s" % f
JUGES = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4"]
C = {  # canons recalcules, compares aux attendus
    "gel": (B(GEL + "/qualification_EB_ter_pre_enregistrement_v1.md"), "432319b9feb34b82"),
    "sonde": (B(GEL + "/sonde_qualification_EB_ter_machine1_v1.py"), "b5616dcf858e8801"),
    "bloc": (B(GEL + "/lecteur_plateau_bloc_machine1_v1.py"), "9b0f95f3e10e9b0d"),
    "feuille": (B(GEL + "/lecture_qualification_EB_ter_machine1_v1.py"), "b2d6d7cfaf30f1cf"),
    "banc": (B(GEL + "/banc_feuille_ter_machine1_v1.py"), "6b63a9de25107ae4"),
    "ref": (B(GEL + "/reference_ancres_ter_machine1_v1.json"), "6600fb8418c79930"),
    "lot_gel": (B(MANIF_GEL), "42110a3d1eabdaa0"),
    "note": (B(NOTE), "42c822811167b826"),
    "lot_note": (B(MANIF_NOTE), "4103eae43f989877"),
    "moteur": (B(CLONE + "/scripts/m17_chaine_v17.py"), "82a0be882568fe0c"),
    "depot": (B(CLONE + "/journal/sonde_ordre2.json"), "10887c60d5f55bcf"),
    "verdict98": (B(CLONE + "/journal/verdict_ordre2.json"), "4195583a970eaf70"),
    "retenus": (B(CLONE + "/journal/tp_retenus_machine2_v1.json"), "69b3bab3bb8480b7"),
    "tp_ref": (B(CLONE + "/journal/tp_reference_machine2_v1.json"), "4d51dd58ef456fe9"),
    "gel_bis": (B(CLONE + "/gels/qualification_EB_bis_pre_enregistrement_v1.md"), "dcda1611adf5f8fd"),
    "acte95": (B(CLONE + "/journal/journal_delta_95_qualification_EB_bis_v2.md"), "bdf8c5a0c73096a4"),
    "acte98": (B(CLONE + "/journal/journal_delta_98_ordre2_chaine_EA_v1.md"), "c2f3e5c9102dc1a7"),
    "lot_cert": (B(ENV + "MANIFEST_lot_machine2_certification_gel_EB_ter_v1.txt"), "d2f50caa808cfb1c"),
    "lot_res": (B(ENV + "MANIFEST_lot_machine2_resultat_EB_ter_v1.txt"), "1f057651c8f69eb6"),
    "lot_rejeu": (B(ENV + "MANIFEST_lot_machine2_rejeu_absorbeurs_longs_hors_chaine_v1.txt"), "29073aa2ac4decac"),
    "lot_lecteur": (B(ENV + "MANIFEST_lot_machine2_lecteur_creux_hors_chaine_v1.txt"), "c8164e6d80ee0b60"),
    "note_cert": (B(LC + "POUR_MACHINE1_certification_gel_EB_ter_machine2_v1.md"), MC["POUR_MACHINE1_certification_gel_EB_ter_machine2_v1.md"]),
    "log_ctl": (B(LC + "certif_EB_ter/controles/controles_gel_ter_machine2_v1.log"), "b27821bf0385581f"),
    "log_conf": (B(LC + "certif_EB_ter/controles/confrontation_feuilles_ter_machine2_v1.log"), "5fe3d3105e0cfe4e"),
    "log_bancs": (B(LC + "certif_EB_ter/controles/banc_sorties_ter_machine2_v1.log"), "5a05122ff1ea19f2"),
    "log_bloc": (B(LC + "certif_EB_ter/controles/bloc_et_lecteur_ter_machine2_v1.log"), "26c50a82f9d07061"),
    "prevol": (B(LC + "certif_EB_ter/prevol/verdict_ter_instrument.json"), "8e7b362aa86f20d6"),
    "note_res": (B(LR + "POUR_MACHINE1_resultat_EB_ter_machine2_v1.md"), "789b4e51dc9f9ceb"),
    "pilote": (B(RUN + "pilote_EB_ter.log"), "5d261985d0dce458"),
    "j_etage0": (B(RUN + "sonde_ter_etage0.json"), "cfd3020e5a0d8a77"),
    "j_ancres": (B(RUN + "sonde_ter_ancres.json"), "e51e8b56d2317130"),
    "j_etage1": (B(RUN + "sonde_ter_etage1.json"), "f88a21eff655f6e8"),
    "log_instr": (B(RUN + "lecture_ter_instrument.log"), "a5cb7f6b8d14ffc5"),
    "v_instr": (B(RUN + "verdict_ter_instrument.json"), "3e9d22bcb044f75a"),
    "log_lect": (B(RUN + "lecture_ter.log"), "4db341d830781530"),
    "v_ter": (B(RUN + "verdict_ter.json"), "2cd1f84efa02f2ab"),
    "log_indep": (B(LR + "certif_EB_ter/controles/relecture_independante_EB_ter_machine2_v1.log"), "e0ce06dd37a91061"),
    "note_lecteur": (B(LL + "POUR_MACHINE1_lecteur_creux_machine2_v1.md"), None),
    "note_rejeu": (B(LJ + "POUR_MACHINE1_rejeu_absorbeurs_longs_machine2_v1.md"), None),
    "mon_log": (B(SORTIE + "/lecture_ter_rejouee_machine1.log"), "4db341d830781530"),
    "mon_log_instr": (B(SORTIE + "/lecture_ter_instrument_rejouee_machine1.log"), "a5cb7f6b8d14ffc5"),
    "mon_v": (B(SORTIE + "/verdict_ter_rejoue_machine1.json"), None),
    "mon_v_instr": (B(SORTIE + "/verdict_ter_instrument_rejoue_machine1.json"), None),
    "mon_rejeu_L3": (B(SORTIE + "/sonde_ter_point_L3_rejeu_machine1.json"), None),
    "mon_cmp": (B(SORTIE + "/comparaison_rejeu_machine1_v1.log"), None),
}
for k, (a, b) in C.items():
    assert b is None or a == b, "canon %s : %s contre %s" % (k, a, b)
c = {k: v[0] for k, v in C.items()}
cp = {i: B(RUN + "sonde_ter_point_%s.json" % i) for i in JUGES}
for i in JUGES:
    assert cp[i] == MR["run_EB_ter/sonde_ter_point_%s.json" % i]

# ---------------------------------------------------------------- le registre
def git(*a):
    return subprocess.run(["git", "-C", CLONE] + list(a), check=True, capture_output=True, text=True).stdout.strip()
assert git("rev-parse", "--short", "HEAD") == "8d54bf9" and git("rev-parse", "--short", "origin/main") == "8d54bf9"
sujet = git("log", "-1", "--format=%s")
assert sujet.startswith("delta 98 --") and "no new candidate rule, thirty-four await review (X)" in sujet
assert git("status", "--porcelain") == "", "le clone du registre n'est pas propre"

# ---------------------------------------------------------------- textes cites
gel = plat(lire(GEL + "/qualification_EB_ter_pre_enregistrement_v1.md"))
acte98 = plat(lire(CLONE + "/journal/journal_delta_98_ordre2_chaine_EA_v1.md"))
ncert = plat(lire(LC + "POUR_MACHINE1_certification_gel_EB_ter_machine2_v1.md"))
nres = plat(lire(LR + "POUR_MACHINE1_resultat_EB_ter_machine2_v1.md"))
nlect = plat(lire(LL + "POUR_MACHINE1_lecteur_creux_machine2_v1.md"))
nrej = plat(lire(LJ + "POUR_MACHINE1_rejeu_absorbeurs_longs_machine2_v1.md"))
envoi = plat(lire(ENV + "ENVOI_machine2_2026-11-15d.txt"))
CIT = {  # citations : (texte, source) ; chacune doit etre dans sa source, mot pour mot
    "question": ("La largeur Gamma_LS que la manche M17 a lue est-elle une largeur SORTANTE INTRINSEQUE -- independante de la force, de la forme, "
                 "de la longueur et de la position de l'absorbeur -- ou depend-elle de la facon d'absorber ?", gel),
    "sens": ("largeur sortante stable sous les variations jouees", gel),
    "phrase": ("aux douze points et aux etats juges QUALIFIES, la largeur lue sous absorbeur long est une largeur sortante stable sous les "
               "variations jouees de force, de forme, de longueur et de position, a tau pres", gel),
    "reclassement": ("toute phrase portant un Gamma depuis juillet est reclassee", gel),
    "dernier": ("DERNIER ESSAI", gel),
    "garde_fou": ("L'operateur peut lever ce garde-fou ; les machines, non", gel),
    "suite": ("une suite demanderait un autre gel et une autre decision de l'operateur", gel),
    "tn": ("se divise par deux a chaque barreau (a 0.002 pres sur le rapport)", gel),
    "rejouer": ("elle peut ensuite rejouer, et compare alors a 1e-6 en relatif sur les lectures suivies", gel),
    "e4": ("a E4, la lecture deposee s'ecarte du plateau de plus de tau a la majorite des etats", gel),
    "statut98": ("La lecture de E-B garde son statut : elle n'est pas qualifiee.", acte98),
    "message": ("tu peux certifier et jouer si c'est ok ?", ncert),
}
for k, (t, src) in CIT.items():
    assert t in src, "citation absente de sa source : %s" % k
assert CIT["message"][0] in envoi and CIT["message"][0] in ncert
cit = {k: v[0] for k, v in CIT.items()}
for t in ('"ouvre" (15/11/2026, 08 h 38)', '"go" (15/11/2026, 10 h 28)'):
    assert t in gel
# faits lus dans les notes de machine 2 (au canon) : chacun doit y etre
for t, src in (("CERTIFIE, 0 morsure", ncert), ("six observations", ncert), ("12 sur 13 tiennent", ncert), ("38 cas sur 38", ncert),
               ("38 etats reels de ton reglage, 20000 etats synthetiques aux bords des seuils, 2657206 cas de cascade", ncert),
               ("ecart 0 sur 12 assemblages", ncert), ("ecart relatif au pire 2.0e-10", ncert), ("192 lectures (16 trajectoires, douze barreaux)", ncert),
               ("py -3.11 -P", ncert), ("un echec de factorisation SIMULE", ncert), ("0.0044 au plus, soit 0.0022 en relatif", ncert),
               ("Deux de mes controles ont mordu au premier jet par ma faute", ncert), ("c'est le rang du depot, non recalcule", ncert),
               ("je l'ai ecrite apres avoir lu la tienne", ncert), ("Selftest 68 sur 68 et banc 43 sur 43 rejoues chez moi", ncert),
               ("scelle a 13 h 42 min 03 s", nres), ("Mon lecteur n'a pas lu les douze points", nres), ("0 ecart", nres), ("sur secteur", nres),
               ("0.3 % a 9 %", nlect), ("leurs largeurs different d'un facteur 22 a 30", nlect),
               ("30 cellules sur 30 sont les tiennes", nrej), ("60 cellules sur 60", nrej)):
    assert t in src, "fait absent de la note de machine 2 : %s" % t

# ---------------------------------------------------------------- le pilote
pil = lire(RUN + "pilote_EB_ter.log")
def heure(motif):
    m = re.search(r"2026-11-15 (\d\d):(\d\d):(\d\d) " + motif, pil); assert m, motif
    return tuple(int(x) for x in m.groups())
h_debut, h_instr, h_fin = heure("DEBUT DU PILOTE"), heure("VERDICT DE L INSTRUMENT : TIENT"), heure("FIN DU PILOTE")
fins = re.findall(r"FIN  (.+?)\s+code=(\d+)(?: duree=(\d+) s)?", pil)
assert len(fins) == 17 and all(x[1] == "0" for x in fins), fins
dur = {x[0]: int(x[2]) for x in fins if x[2]}
assert [dur[k] for k in ("etage0", "ancres", "etage1")] == [14, 362, 396]
dpts = {i: dur["point_" + i] for i in JUGES}
m = re.search(r"DUREE TOTALE DU RUN : (\d+) s", pil); duree_run = int(m.group(1)); assert duree_run == 4377
n_canons_pilote = len(re.findall(r"^\S+ \S+ canon .* OK$", pil, re.M)); assert n_canons_pilote == 10 == len(re.findall(r"^\S+ \S+ canon ", pil, re.M))
assert "batterie (BatteryStatus WMI, 2 = secteur, 1 = batterie, vide = pas de batterie) : '2'" in pil
def hms(t):
    return "%d h %02d min %02d s" % t
assert hms(h_debut) == "13 h 42 min 11 s" and hms(h_fin) == "14 h 55 min 08 s"

# ---------------------------------------------------------------- le depot, les sorties du run, le recalcul
DEP = json.load(open(CLONE + "/journal/sonde_ordre2.json")); PD = {p["id"]: p for p in DEP["points"]}
KS = list(range(-3, 9)); TAU = 0.05; PLANCHER10 = 1.33e-12
S = {}
for i in JUGES:
    s = json.load(open(RUN + "sonde_ter_point_%s.json" % i))
    assert s["sonde_canon"] == c["sonde"] and s["mode"] == "point" and s["ids"] == [i] and s["depot_canon"] == c["depot"] and s["moteur_canon"] == c["moteur"]
    assert s["reglage"]["ks"] == KS and s["reglage"]["absorbeurs"] == [["A", "F2", 0, 80], ["B", "F2", 0, 100], ["C", "F1", 0, 100], ["D", "F2", 10, 80]]
    assert s["plateforme"]["python"] == "3.11.9" and s["plateforme"]["numpy"] == "2.2.6" and s["plateforme"]["scipy"] == "1.15.3" and s["plateforme"]["systeme"] == "Windows"
    assert s["plateforme"]["coeurs"] == 16 and s["plateforme"]["levier"] is None and s["plateforme"]["fils"]["OPENBLAS_NUM_THREADS"] == "1"
    S[i] = s["points"][0]; S[i]["_duree"] = s["duree_s"]
def fenetres(traj):
    """Toutes les fenetres de cinq valeurs lisibles : (k0, max / min en rationnel exact, moyenne geometrique)."""
    out = []
    for k0 in range(-3, 5):
        r = [traj[str(k)] for k in range(k0, k0 + 5)]
        if all(x["suivi"] and x["gamma"] is not None and math.isfinite(x["gamma"]) and x["gamma"] > 0 for x in r):
            v = [x["gamma"] for x in r]; fr = [Fr(x) for x in v]
            out.append((k0, max(fr) / min(fr), math.exp(sum(math.log(x) for x in v) / 5.0)))
    return out
def meilleure(traj):
    f = fenetres(traj)
    if not f: return None
    k0, rap, gm = min(f, key=lambda t: (t[1], t[0]))
    return {"k0": k0, "etal": float(rap - 1), "plateau": rap <= Fr(21, 20), "Gpl": gm}
E = []   # un enregistrement par etat juge
depot_total = 0; sous_plancher = 0
for i in JUGES:
    p = PD[i]; depot_total += len(p["etats"])
    attendus = [e for e in p["etats"] if (e.get("Gamma_2D") or {}).get("3") is not None and e["Gamma_2D"]["3"] > PLANCHER10]
    sous_plancher += len(p["etats"]) - len(attendus)
    assert [e["rang"] for e in attendus] == [e["rang"] for e in S[i]["etats"]], i
    for e, d in zip(S[i]["etats"], attendus):
        assert (e["n1"], e["n2"]) == (int(d["n1"]), int(d["n2"])) and e["E_depart"] == d["E_re"] and e["G_dep"]["3"] == d["Gamma_2D"]["3"]
        m4 = {x: meilleure(e["traj"][x]) for x in "ABCD"}
        echecs = []; illisibles = [x for x in "ABCD" if m4[x] is None]
        for x in "ABCD":
            if m4[x] is not None and not m4[x]["plateau"]: echecs.append("plateau " + x)
        acc = {}
        if m4["A"] is not None and m4["A"]["plateau"]:
            for x in "BCD":
                if m4[x] is not None and m4[x]["plateau"]:
                    acc[x] = abs(math.log(m4[x]["Gpl"] / m4["A"]["Gpl"]))
                    assert abs(acc[x] - TAU) > 1e-6
                    if acc[x] > TAU: echecs.append("accord " + x)
        statut = "NON QUALIFIE" if echecs else ("NON LISIBLE" if illisibles else "QUALIFIE")
        G3 = d["Gamma_2D"]["3"]; ecart = None; sur = None
        if m4["A"] is not None and m4["A"]["plateau"]:
            ecart = math.log(G3 / m4["A"]["Gpl"]); assert abs(abs(ecart) - TAU) > 1e-6; sur = abs(ecart) <= TAU
        E.append({"id": i, "rang": e["rang"], "site": (e["n1"], e["n2"]), "G3": G3, "m": m4, "acc": acc, "statut": statut, "echecs": echecs,
                  "ecart": ecart, "sur": sur, "traj": e["traj"]})
# comparaison a la feuille rejouee par machine 1 et au verdict de BOCAL4
VM = json.load(open(SORTIE + "/verdict_ter_rejoue_machine1.json")); V2 = json.load(open(RUN + "verdict_ter.json"))
def feuilles(d, p=""):
    if isinstance(d, dict):
        for k, v in d.items(): yield from feuilles(v, p + "/" + str(k))
    elif isinstance(d, list):
        for k, v in enumerate(d): yield from feuilles(v, p + "/" + str(k))
    else: yield p, d
FM, F2 = dict(feuilles(VM)), dict(feuilles(V2)); assert set(FM) == set(F2)
ecart_gpl = 0.0; ecart_ln = 0.0; n_flott = 0   # flottants differents : Gamma_pl (en relatif), ecarts logarithmiques (en absolu)
def flottants(FA, FB):
    global ecart_gpl, ecart_ln, n_flott
    for k in FA:
        a, b = FA[k], FB[k]
        if isinstance(a, float) and isinstance(b, float):
            if a != b:
                n_flott += 1; nom = k.split("/")[-1]
                if nom == "Gamma_pl": ecart_gpl = max(ecart_gpl, abs(a - b) / abs(b))
                else:
                    assert nom.startswith("ecart_ln"), k; ecart_ln = max(ecart_ln, abs(a - b))
        else:
            assert a == b, (k, a, b)
flottants(FM, F2)
for V in (VM, V2):
    assert V["verdict"] == "ESTIMATEUR QUALIFIE" and V["instrument"] == "TIENT" and V["n_juges"] == 137
    for r in E:
        ev = [x for x in V["points"][r["id"]]["etats"] if x["rang"] == r["rang"]][0]
        assert ev["statut"] == r["statut"] and (ev["n1"], ev["n2"]) == r["site"]
        for x in "ABCD":
            assert ev["plateaux"][x]["k0"] == r["m"][x]["k0"] and (ev["plateaux"][x]["statut"] == "PLATEAU") == r["m"][x]["plateau"]
            assert abs(ev["plateaux"][x]["Gamma_pl"] / r["m"][x]["Gpl"] - 1) < 1e-12 and abs(ev["plateaux"][x]["etalement"] - r["m"][x]["etal"]) < 1e-12
        assert ev["lu_sur_le_plateau"] == r["sur"] and abs(ev["ecart_ln_depot"] - abs(r["ecart"])) < 1e-12
NJ = len(E); NQ = sum(r["statut"] == "QUALIFIE" for r in E); NNQ = sum(r["statut"] == "NON QUALIFIE" for r in E); NNL = sum(r["statut"] == "NON LISIBLE" for r in E)
NPA = sum(r["m"]["A"] is not None and r["m"]["A"]["plateau"] for r in E); NSUR = sum(bool(r["sur"]) for r in E)
SEUIL = -((-9 * NJ) // 10)
assert (NJ, NQ, NNQ, NNL, NPA, NSUR, SEUIL) == (137, 136, 1, 0, 137, 130, 124)
assert V2["n_qualifies"] == NQ and V2["n_lus_sur_le_plateau"] == NSUR and V2["n_plateau_A"] == NPA
assert V2["issue_depot"] == "LA LECTURE DEPOSEE EST SUR LE PLATEAU A NEUF ETATS SUR DIX AU MOINS"
assert depot_total == 168 and sous_plancher == 31
lus = {i: [r for r in E if r["id"] == i and r["rang"] == 0][0] for i in JUGES}
assert all(lus[i]["statut"] == "QUALIFIE" for i in JUGES)
rang1 = {i: [r for r in E if r["id"] == i and r["rang"] == 1] for i in JUGES}
r1_juges = [i for i in JUGES if rang1[i]]; r1_non = [i for i in JUGES if not rang1[i]]
assert all(rang1[i][0]["statut"] == "QUALIFIE" for i in r1_juges) and len(r1_juges) == 10 and r1_non == ["M3", "M4"]
rec = {}; larg = {}
for i in JUGES:
    d0 = [e for e in PD[i]["etats"] if e["rang"] == 0][0]; d1 = [e for e in PD[i]["etats"] if e["rang"] == 1][0]
    assert d0["recouvrement"] >= d1["recouvrement"] > 0
    rec[i] = d0["recouvrement"] / d1["recouvrement"]; larg[i] = d1["Gamma_2D"]["3"] / d0["Gamma_2D"]["3"]
fact_larg = {i: max(larg[i], 1.0 / larg[i]) for i in JUGES}
sans_plateau = {x: sum(not (r["m"][x] is not None and r["m"][x]["plateau"]) for r in E) for x in "ABCD"}
assert sans_plateau == {"A": 0, "B": 0, "C": 0, "D": 0}
med = statistics.median
ET = {x: [r["m"][x]["etal"] for r in E] for x in "ABCD"}; AC = {x: [r["acc"][x] for r in E] for x in "BCD"}
EC = [abs(r["ecart"]) for r in E]
def arg(liste_cle):
    r = max(E, key=liste_cle); return r
pire_et = {x: max(E, key=lambda r: r["m"][x]["etal"]) for x in "ABCD"}
pire_ac = {x: max(E, key=lambda r: r["acc"][x]) for x in "BCD"}
hors_e = [r for r in E if not r["sur"]]; assert len(hors_e) == 7 and all(r["statut"] == "QUALIFIE" for r in hors_e)
N_DEP_LEVE = sum(r["statut"] == "QUALIFIE" and r["sur"] for r in E); assert N_DEP_LEVE == 129
nq = [r for r in E if r["statut"] != "QUALIFIE"]; assert len(nq) == 1
NQ1 = nq[0]; assert (NQ1["id"], NQ1["rang"], NQ1["site"], NQ1["echecs"]) == ("L3", 5, (7, 2), ["accord C"])
fC = fenetres(NQ1["traj"]["C"]); platC = [f for f in fC if f[1] <= Fr(21, 20)]; assert len(platC) == 2
fC_ret = min(fC, key=lambda t: (t[1], t[0])); fC_aut = [f for f in platC if f[0] != fC_ret[0]][0]
assert fC_ret[0] == NQ1["m"]["C"]["k0"] == -1 and fC_aut[0] == 4
acc_aut = abs(math.log(fC_aut[2] / NQ1["m"]["A"]["Gpl"])); assert acc_aut < TAU
hors_L3 = [r for r in E if r["id"] != "L3"]; assert len(hors_L3) == 123
hL3_et = {x: max(hors_L3, key=lambda r: r["m"][x]["etal"]) for x in "ABCD"}
hL3_ac = {x: max(hors_L3, key=lambda r: r["acc"][x]) for x in "BCD"}
L3e = [r for r in E if r["id"] == "L3"]
plus_petite_marge = max(((r["m"][x]["etal"], r, x) for r in E for x in "ABCD"), key=lambda t: t[0])
ac2 = sorted((r["acc"]["C"] for r in E), reverse=True)[1]
sg = [r["ecart"] for r in E]
gpl_q = [r["m"]["A"]["Gpl"] for r in E if r["statut"] == "QUALIFIE"]
# lectures
LECT = {"n": 0, "suivies": 0, "it": {}, "poids": 1.0, "res": 0.0, "repris": 0}
for i in JUGES:
    for e in S[i]["etats"]:
        for x in "ABCD":
            assert sorted(e["traj"][x], key=int) == [str(k) for k in KS]
            for k in KS:
                r = e["traj"][x][str(k)]; LECT["n"] += 1; LECT["suivies"] += bool(r["suivi"]); LECT["it"][r["iterations"]] = LECT["it"].get(r["iterations"], 0) + 1
                LECT["poids"] = min(LECT["poids"], r["poids_site"]); LECT["repris"] += bool(r["decalage_repris"])
                LECT["res"] = max(LECT["res"], r["residu"] / max(1.0, abs(complex(r["E_re"], -r["gamma_im"] / 2.0))))
assert LECT["n"] == LECT["suivies"] == 6576 and LECT["repris"] == 0 and sorted(LECT["it"]) == [2, 3, 4]
cumul = sum(S[i]["_duree"] for i in JUGES)

# ---------------------------------------------------------------- l'instrument
VI = json.load(open(SORTIE + "/verdict_ter_instrument_rejoue_machine1.json")); VI2 = json.load(open(RUN + "verdict_ter_instrument.json"))
for v in (VI, VI2):
    assert v["instrument"] == "TIENT" and v["etage0"]["tient"] and v["etage0"]["lectures"] == 84 and not v["etage0"]["hors"]
    assert v["ancres"]["tient"] and v["ancres"]["lectures"] == 192 and v["etage1"]["tient"]
e0_abs, e0_rel, anc = VI["etage0"]["pire_ecart_absolu"], VI["etage0"]["pire_ecart_relatif_au_dessus_de_mille_planchers"], VI["ancres"]["pire_ecart_ln"]
PV = json.load(open(LC + "certif_EB_ter/prevol/verdict_ter_instrument.json"))
assert PV["instrument"] == "TIENT" and abs(PV["etage0"]["pire_ecart_absolu"] / e0_abs - 1) < 1e-3 and PV["ancres"]["pire_ecart_ln"] == anc
FI, FI2 = dict(feuilles(VI)), dict(feuilles(VI2)); assert set(FI) == set(FI2)
flottants(FI, FI2)
assert ecart_gpl < 1e-13 and ecart_ln < 1e-13
TPd = VI["etage1"]["detail"]["TP"]; TNd = VI["etage1"]["detail"]["TN"]
tp_ln = {j: max(TPd[j][x]["ecart_ln"] for x in "ABCD") for j in ("j06", "j08")}
assert all(TPd[j][x]["statut"] == "PLATEAU" for j in TPd for x in "ABCD") and all(TNd[a][x]["statut"] == "PAS DE PLATEAU" for a in TNd for x in "ABCD")
tn_et = [TNd[a][x]["etalement"] for a in TNd for x in "ABCD"]
J1 = json.load(open(RUN + "sonde_ter_etage1.json")); J0 = json.load(open(RUN + "sonde_ter_etage0.json")); JA = json.load(open(RUN + "sonde_ter_ancres.json"))
tn3 = [t["traj"][x]["3"]["gamma"] for t in J1["temoin_negatif"] for x in "ABCD"]
tn_abs = max(abs(t["traj"][x][str(k)]["gamma"] / t["traj"][x][str(k + 1)]["gamma"] - 2.0) for t in J1["temoin_negatif"] for x in "ABCD" for k in range(-3, 8))
n_instr = 0; rep_instr = 0
for q in (J0, JA):
    for p in q["points"]:
        for e in p["etats"]:
            for tr in e["traj"].values():
                for r in tr.values(): n_instr += 1; rep_instr += bool(r["decalage_repris"]); assert r["suivi"]
for grp in ("temoin", "temoin_negatif"):
    for t in J1[grp]:
        for tr in t["traj"].values():
            for r in tr.values(): n_instr += 1; rep_instr += bool(r["decalage_repris"]); assert r["suivi"]
assert n_instr == 468 and rep_instr == 0
logi = lire(SORTIE + "/lecture_ter_instrument_rejouee_machine1.log")
bornes_tp = re.findall(r"TP j0([68]) g = \S+ A : .*contre ([0-9.]+) : TIENT", logi); assert len(bornes_tp) == 2
borne_tp = {"j0" + a: float(b) for a, b in bornes_tp}
assert "selftest : 68 tenus sur 68" in logi and "selftest : 68 tenus sur 68" in lire(SORTIE + "/lecture_ter_rejouee_machine1.log")

# ---------------------------------------------------------------- le delta 98
V98 = json.load(open(CLONE + "/journal/verdict_ordre2.json")); P98 = {p["id"]: p for p in V98["points"]}
j98 = [(i, e["rang"]) for i in JUGES for e in P98[i]["etats"] if e["exclu"] is None]; assert len(j98) == 132
Ed = {(r["id"], r["rang"]): r for r in E}; assert all(k in Ed for k in j98)
n98_q = sum(Ed[k]["statut"] == "QUALIFIE" for k in j98); n98_sur = sum(Ed[k]["statut"] == "QUALIFIE" and Ed[k]["sur"] for k in j98)

# ---------------------------------------------------------------- le rejeu de machine 1
RJ = json.load(open(SORTIE + "/comparaison_rejeu_machine1_v1.json"))
assert RJ["tient"] and not RJ["hors"] and not RJ["statuts_differents"] and RJ["non_suivies"] == 0 and RJ["tolerance"] == 1e-6
assert RJ["rejeu_L3"]["etats"] == 14 and RJ["rejeu_L3"]["lectures"] == 672
n_part = sum(len(r["rangs"]) for r in RJ["rejeu_partiel"]); l_part = sum(r["lectures"] for r in RJ["rejeu_partiel"])
assert sorted(r["id"] for r in RJ["rejeu_partiel"]) == sorted(i for i in JUGES if i != "L3") and l_part == 48 * n_part
for r in RJ["rejeu_partiel"]:
    assert 0 in r["rangs"] and set(r["rangs"]) == {0} | {x["rang"] for x in hors_e if x["id"] == r["id"]}
assert RJ["lectures"] == 672 + l_part and RJ["n_etats"] == 14 + n_part and len(RJ["points"]) == 12
pf1 = RJ["rejeu_L3"]["plateforme"]; assert (pf1["python"], pf1["numpy"], pf1["scipy"], pf1["systeme"]) == ("3.13.18", "2.5.3", "1.18.1", "Linux")
assert "COMPARAISON : TIENT" in lire(SORTIE + "/comparaison_rejeu_machine1_v1.log")

# ---------------------------------------------------------------- les annonces
neg = ["C1", "C2", "M1", "M2", "L1", "L2"]; assert all(Fr(PD[i]["w2"]) < 2 for i in neg) and all(Fr(PD[i]["w2"]) > 2 for i in JUGES if i not in neg)
a5 = max(max(r["m"]["A"]["etal"], r["m"]["B"]["etal"]) for r in E if r["id"] in neg)
nnq_pt = {i: sum(r["statut"] != "QUALIFIE" for r in E if r["id"] == i) for i in JUGES}
A = {"A-3": all(lus[i]["statut"] == "QUALIFIE" for i in JUGES if i != "L3"), "A-4": nnq_pt["L3"] == max(nnq_pt.values()),
     "A-5": a5 <= 0.02, "A-6": max(AC["B"]) <= 0.02, "A-7": VI["instrument"] == "TIENT", "A-8": sans_plateau["C"] == max(sans_plateau.values()),
     "A-9": 0.01 <= med(EC) <= 0.04, "A-10": NNL <= 3}
assert all(A.values())
sec11 = gel[gel.index("## 11."):gel.index("## 12.")]; sec11 = sec11[sec11.index("s'il n'y en a aucun.") + 20:sec11.index("Ces probabilites sont ecrites")]
mor = re.split(r"\s(A-\d+)\s", " " + sec11); PA = {}
for k, t in zip(mor[1::2], mor[2::2]):
    pr = re.findall(r": (0\.\d\d)\.", t)
    if k not in ("A-1", "A-2"):
        assert len(pr) == 1, (k, t); PA[k] = float(pr[0])
assert PA == {"A-3": 0.80, "A-4": 0.55, "A-5": 0.80, "A-6": 0.60, "A-7": 0.96, "A-8": 0.70, "A-9": 0.75, "A-10": 0.80}, PA
assert "ESTIMATEUR QUALIFIE : 0.46 ; QUALIFIE A L'ETAT LU : 0.08 ; QUALIFIE PAR POINT : 0.40 ; NON QUALIFIE : 0.01 ; NON LISIBLE : 0.01 ; NON CONCLUANT D'INSTRUMENT : 0.04." in gel
assert "SUR LE PLATEAU a tous les etats : 0.02 ; A NEUF ETATS SUR DIX AU MOINS : 0.23 ; PAS PARTOUT : 0.75." in gel
somme_pa = sum(PA.values())
m = re.search(r"etalement de la meilleure fenetre sous A : mediane [0-9.]+, plus grand ([0-9.]+) ; etalement de la meilleure fenetre sous B : mediane [0-9.]+, plus grand ([0-9.]+) ; "
              r"etalement de la meilleure fenetre sous C : mediane [0-9.]+, plus grand ([0-9.]+) ; etalement de la meilleure fenetre sous D : mediane [0-9.]+, plus grand ([0-9.]+) ;", gel)
regl = [m.group(k) for k in (1, 2, 3, 4)]; assert regl == ["0.0409", "0.0442", "0.0657", "0.0410"]
assert "de 7.1 h de calcul cumule" in gel and "E4, g = 1.2e-2" in gel

# ================================================================ le texte
L = []
def P(texte, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(plat(texte), width=100, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
def T(ligne=""):
    L.append(ligne)
def f4(x): return "%.4f" % x
def sg4(x): return "%+.4f" % x
def e2(x):
    s = "%.2e" % x; return s
def e1(x): return "%.1e" % x
def sup(x):
    """Le plus petit nombre a deux chiffres significatifs qui n'est pas sous x : pour les "au plus"."""
    if x == 0: return "0"
    e = math.floor(math.log10(x)); m = math.ceil(x / 10.0 ** e * 10 - 1e-9) / 10.0
    if m >= 10: m, e = 1.0, e + 1
    s = "%.1fe%+03d" % (m, e); assert float(s) >= x * (1 - 1e-12) and float(s) <= x * 1.12, (s, x)
    return s
def frac(s): return "1" if s == "1/1" else s
def delta(i):
    d = Fr(PD[i]["w2"]) - 2; return "%+.2f" % float(d)

T("DELTA nn -- QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS), TER : RUN DU 15/11/2026 SOUS LE GEL")
T("%s. VERDICT : ESTIMATEUR QUALIFIE. ISSUE SEPAREE : LA LECTURE DEPOSEE EST SUR LE" % c["gel"])
T("PLATEAU A NEUF ETATS SUR DIX AU MOINS. -- PROJET, VERSION 1")
T("(plume machine 1 ; run et certification machine 2 ; a contresigner par machine 2)")
T("=" * 71)
T()
T("nn.0 POSITION")
P("""Ce delta rend le run du gel "qualification E-B ter", troisieme gel de la piste (0). Sa question est celle du gel bis : "%s", posee aux
largeurs que la sonde du delta 98 a lues a la facon de M17 (k = 3, F1, 20 couches) aux douze points juges de ce delta, etat par etat, sous des
absorbeurs de 80 et 100 couches.""" % cit["question"])
P("""Reponse de la feuille : ESTIMATEUR QUALIFIE. L'etat lu est QUALIFIE aux douze points ; %d etats juges sur %d le sont, pour un seuil de %d.
Issue separee : LA LECTURE DEPOSEE EST SUR LE PLATEAU A NEUF ETATS SUR DIX AU MOINS (%d sur %d) ; a l'etat lu elle l'est a onze points sur
douze.""" % (NQ, NJ, SEUIL, NSUR, NJ))
P("""QUALIFIE veut dire "%s", et rien d'autre : rien sur l'unitarite, ni sur les extensions auto-adjointes, ni sur la dynamique du systeme
ferme. Le verdict de la nuit bis (delta 95, NON QUALIFIE) reste ce qu'il est, sous son gel : ce run joue d'autres absorbeurs, par un autre
instrument, sur d'autres points.""" % cit["sens"])
P("""Le gel bis ecrivait "%s" et "%s". L'operateur a leve ce garde-fou en deux temps, selon machine 1 : "ouvre" (15/11/2026, 08 h 38), pour un
calcul hors chaine, puis "go" (15/11/2026, 10 h 28), pour ce gel. Machine 2 ne peut pas le verifier sur piece (nn.11).""" % (cit["dernier"], cit["garde_fou"]))
P("""Registre a l'ecriture : origin/main 8d54bf9, plafond 98. Aucun numero n'est pris ici (E18).""")
T()
T("nn.1 PIECES (convention B)")
def piece(ind, nom, canon, glose):
    T(" " * ind + "%s  %s" % (nom, canon)); P(glose, ind + 4)
T("  Au registre (8d54bf9)")
piece(4, "scripts/m17_chaine_v17.py", c["moteur"], "le moteur ; il n'est pas modifie")
piece(4, "journal/sonde_ordre2.json", c["depot"], "la sortie deposee de la sonde du delta 98 : les douze points, leurs etats, les largeurs deposees")
piece(4, "journal/verdict_ordre2.json", c["verdict98"], "le verdict du delta 98 : ses 132 etats juges")
piece(4, "journal/journal_delta_98_ordre2_chaine_EA_v1.md", c["acte98"], "l'acte 98")
piece(4, "gels/qualification_EB_bis_pre_enregistrement_v1.md", c["gel_bis"], "le gel bis")
piece(4, "journal/journal_delta_95_qualification_EB_bis_v2.md", c["acte95"], "l'acte 95 : NON QUALIFIE, et le reclassement")
piece(4, "journal/tp_retenus_machine2_v1.json", c["retenus"], "les couplages retenus du temoin positif")
piece(4, "journal/tp_reference_machine2_v1.json", c["tp_ref"], "la table de reference du temoin positif")
T("  Hors registre, de machine 1")
piece(4, "lot du gel", c["lot_gel"], "le gel et ses instruments, 55 pieces")
piece(6, "qualification_EB_ter_pre_enregistrement_v1.md", c["gel"], "le gel")
piece(6, "sonde_qualification_EB_ter_machine1_v1.py", c["sonde"], "la sonde : elle mesure et ne juge pas")
piece(6, "lecteur_plateau_bloc_machine1_v1.py", c["bloc"], "le bloc du lecteur creux, insere tel quel dans la sonde")
piece(6, "lecture_qualification_EB_ter_machine1_v1.py", c["feuille"], "la feuille : elle juge et ne mesure pas")
piece(6, "banc_feuille_ter_machine1_v1.py", c["banc"], "le banc qui tue de la feuille")
piece(6, "reference_ancres_ter_machine1_v1.json", c["ref"], "la reference des ancres : la sonde sur le conteneur de machine 1")
piece(4, "lot de la note hors chaine", c["lot_note"], "34 pieces")
piece(6, "note_machine1_piste0_reprise_absorbeur_long_2026-11-15_v1.md", c["note"], "la note hors chaine, apres coup, d'une seule plume, sur laquelle l'operateur a dit \"go\"")
T("  Hors registre, de machine 2")
piece(4, "lot de certification", c["lot_cert"], "certification du gel, de la sonde, du bloc, de la feuille, du banc et de la reference des ancres, AVANT le run ; 28 pieces")
piece(6, "POUR_MACHINE1_certification_gel_EB_ter_machine2_v1.md", c["note_cert"], "la note : CERTIFIE, 0 morsure, six observations")
piece(6, "certif_EB_ter/controles/controles_gel_ter_machine2_v1.log", c["log_ctl"], "ses 13 controles de lecture du gel")
piece(6, "certif_EB_ter/controles/confrontation_feuilles_ter_machine2_v1.log", c["log_conf"], "sa feuille independante contre celle de machine 1, trois terrains")
piece(6, "certif_EB_ter/controles/banc_sorties_ter_machine2_v1.log", c["log_bancs"], "son banc de sorties : les etapes \"instrument\" et \"verdict\" de la feuille, 38 cas")
piece(6, "certif_EB_ter/controles/bloc_et_lecteur_ter_machine2_v1.log", c["log_bloc"], "le bloc controle, et son lecteur a elle contre le bloc")
piece(6, "certif_EB_ter/prevol/verdict_ter_instrument.json", c["prevol"], "son pre-vol des trois modes d'instrument")
piece(4, "lot de resultat", c["lot_res"], "le run, sa lecture, la relecture de machine 2 ; 43 pieces")
piece(6, "POUR_MACHINE1_resultat_EB_ter_machine2_v1.md", c["note_res"], "la note de machine 2")
piece(6, "run_EB_ter/pilote_EB_ter.log", c["pilote"], "le journal du pilote : heures et codes de sortie")
piece(6, "run_EB_ter/sonde_ter_etage0.json", c["j_etage0"], "l'etage 0")
piece(6, "run_EB_ter/sonde_ter_ancres.json", c["j_ancres"], "les ancres reglees")
piece(6, "run_EB_ter/sonde_ter_etage1.json", c["j_etage1"], "les temoins")
T("      run_EB_ter/sonde_ter_point_<id>.json, les douze sorties de la sonde aux points juges :")
for k in range(0, 12, 4):
    T("          " + "  ".join("%s %s" % (i, cp[i]) for i in JUGES[k:k + 4]))
piece(6, "run_EB_ter/lecture_ter_instrument.log", c["log_instr"], "le journal de la feuille, etape \"instrument\"")
piece(6, "run_EB_ter/verdict_ter_instrument.json", c["v_instr"], "le verdict de l'instrument rendu sur BOCAL4")
piece(6, "run_EB_ter/lecture_ter.log", c["log_lect"], "le journal de la feuille, etape \"verdict\"")
piece(6, "run_EB_ter/verdict_ter.json", c["v_ter"], "le verdict rendu sur BOCAL4 : les 137 etats, leurs fenetres, leurs Gamma_pl")
piece(6, "certif_EB_ter/controles/relecture_independante_EB_ter_machine2_v1.log", c["log_indep"], "sa feuille independante sur le run : 0 ecart")
piece(4, "lot \"lecteur creux\", hors chaine", c["lot_lecteur"], "le lecteur de machine 2, non certifie, et un fait sur l'ancrage (nn.9, R-TER-2)")
piece(4, "lot \"rejeu sous absorbeurs longs\", hors chaine", c["lot_rejeu"], "son rejeu de la note de machine 1 aux six points de M17")
T("  De ce lot")
piece(4, "lecture_ter_rejouee_machine1.log", c["mon_log"], "la feuille rejouee par machine 1 sur les sorties de BOCAL4, etape \"verdict\" : le meme canon")
piece(4, "verdict_ter_rejoue_machine1.json", c["mon_v"], "son verdict ; il differe de celui de BOCAL4 par des flottants (nn.2)")
piece(4, "lecture_ter_instrument_rejouee_machine1.log", c["mon_log_instr"], "la meme, etape \"instrument\" : le meme canon")
piece(4, "verdict_ter_instrument_rejoue_machine1.json", c["mon_v_instr"], "son verdict de l'instrument")
piece(4, "sonde_ter_point_L3_rejeu_machine1.json", c["mon_rejeu_L3"], "la sonde certifiee rejouee a L3 sur le conteneur de machine 1")
piece(4, "comparaison_rejeu_machine1_v1.log", c["mon_cmp"], "le rejeu de machine 1 contre le run")
T()
T("nn.2 CE QUI A ETE JOUE, ET PAR QUI (E19)")
P("""Machine 1, avant le lot de resultat : aucun calcul 2D sous absorbeur long a aucun des douze points. Ce qu'elle avait vu, et que le gel
dit (section 4, limite L-1) : les six points de M17, par la note hors chaine ; puis huit points deja joues des deltas 96, 97 et 98 (A1, A2, J1,
J2, J3, J5, E4, H1), en deux temps, son premier jeu d'absorbeurs (60 et 80 couches) s'etant montre trop court ; les etages 0 et 1 et les
ancres, sur son conteneur.""")
P("""Machine 2 : la certification d'abord (0 morsure, six observations ; ses 13 controles de lecture du gel, dont 12 tiennent, le treizieme
etant son observation O-1 ; le pre-vol des trois modes d'instrument, que le gel permettait), lot scelle a 13 h 42 min 03 s. Puis UN run, par
un pilote qui verifie %d canons et refuse de jouer si le dossier de sortie existe : debut a %s, fin a %s, %d secondes ; les dix-sept appels a
code 0 ; aucun appel interrompu, relance ou rejoue. Etape 1 : etage0 (%d s), ancres (%d s), etage1 (%d s), trois processus ; la feuille, etape
"instrument" : TIENT. Etape 3 : la sonde en mode point, les douze points lances ensemble, un processus par point, de %d s (%s) a %d s ; la
feuille, etape "verdict". BOCAL4, Windows AMD64, 16 coeurs, python 3.11.9, numpy 2.2.6, scipy 1.15.3, un fil par processus, sur secteur.""" % (
    n_canons_pilote, hms(h_debut), hms(h_fin), duree_run, dur["etage0"], dur["ancres"], dur["etage1"], min(dpts.values()),
    min(dpts, key=dpts.get), max(dpts.values())))
P("""Un ecart a la lettre de l'invocation, dit par machine 2 (son observation O-2) : la sonde a ete lancee par "py -3.11 -P" et non par
"python -I", qui ne voit ni numpy ni scipy sur BOCAL4, et sans le levier X86_V4, propre au conteneur de machine 1. Chaque sortie consigne sa
plateforme.""")
P("""Machine 1, apres avoir recu et authentifie le lot de resultat (quatre lots, 43, 28, 11 et 14 pieces, toutes au canon) :""")
P("""(a) sa feuille, rejouee sur les quinze sorties de BOCAL4 : les deux journaux sont ceux de BOCAL4 a l'octet pres (canons %s et %s) ; memes
statuts, memes fenetres, memes comptes. Les deux verdicts JSON different de ceux de BOCAL4 par %d flottants sur %d : des Gamma_pl, de %s
au plus en relatif, et des ecarts logarithmiques, de %s au plus en absolu ; la moyenne geometrique et le logarithme ne s'arrondissent pas de
meme d'une plateforme a l'autre. Les plateaux, eux, sont juges en rationnels exacts.""" % (c["mon_log"], c["mon_log_instr"], n_flott,
    sum(isinstance(v, float) for v in list(FM.values()) + list(FI.values())), sup(ecart_gpl), sup(ecart_ln)), 4, 8)
P("""(b) un rejeu, que le gel permet apres authentification ("%s") : la sonde certifiee, telle quelle, au point L3 (%d etats, %d lectures) ; et
le texte de la sonde execute jusqu'a sa fonction principale, la liste des etats restreinte, pour %d etats des onze autres points : l'etat lu de
chacun, et les etats ou la consigne (e) ne tient pas (%d lectures). Sur les %d lectures, toutes suivies des deux cotes : memes statuts, plus
grand ecart relatif de largeur %s, pour une tolerance de 1e-6 ; %s. Conteneur Linux, python
3.13.18, numpy 2.5.3, scipy 1.18.1.""" % (cit["rejouer"], RJ["rejeu_L3"]["etats"], RJ["rejeu_L3"]["lectures"], n_part, l_part, RJ["lectures"], sup(RJ["pire"]),
    "meme nombre d'iterations a chaque lecture" if RJ["iterations_differentes"] == 0 else "%d lectures n'ont pas le meme nombre d'iterations" % RJ["iterations_differentes"]), 4, 8)
P("""Le lecteur de machine 2, qui est un autre algorithme, n'a PAS lu les douze points (nn.9, R-TER-1).""")
T()
T("nn.3 L'INSTRUMENT ET LES GARDES")
P("""L'instrument TIENT dans le run, aux chiffres du pre-vol de machine 2 et de l'essai de machine 1. Selftest de la feuille : 68 sur 68, sur
BOCAL4 et chez machine 1.""")
P("""Etage 0 (le lecteur contre la sonde dense deposee : deux ancres, 14 etats, k = 2, 3, 4, F1 a 20 couches) : 84 lectures sur 84 dans la
tolerance ; plus grand ecart absolu %s, plus grand ecart relatif au-dessus de mille planchers %s.""" % (e2(e0_abs), e1(e0_rel)))
P("""Ancres reglees : 192 lectures sur 192, memes statuts de suivi ; plus grand |ln| a la reference de machine 1 : %s, pour une tolerance de
1e-6. Deux plateformes rendent la meme largeur a l'arrondi pres.""" % e1(anc))
P("""Temoin positif : PLATEAU aux huit (couplage, absorbeur) ; |ln(Gamma_pl / Gamma_ref)| vaut au plus %s a j = 6 et %s a j = 8, pour des
bornes de %s et %s.""" % (f4(tp_ln["j06"]), f4(tp_ln["j08"]), f4(borne_tp["j06"]), f4(borne_tp["j08"])))
P("""Temoin negatif : PAS DE PLATEAU aux huit (ancre, absorbeur). L'etalement de sa meilleure fenetre va de %.2f a %.2f, la ou une largeur
proportionnelle a eta donne 15 ; ses largeurs vont de %s a %s a k = 3.""" % (min(tn_et), max(tn_et), e1(min(tn3)), e1(max(tn3))))
P("""Gardes du gel : aucune ne mord. G-T1 : la sonde verifie ses trois canons a chaque appel, le pilote en verifie dix. G-T2, G-T3 : chaque
sortie porte le canon de la sonde (%s) et le reglage du gel ; la feuille les controle. G-T4 : a chaque point, les etats lus sont ceux que la
regle du gel tire du depot, chacun sous quatre absorbeurs et douze barreaux ; les douze points sont lus une fois. G-T5 : 84, 192, 96 et 96
lectures a l'instrument, %d a l'etage 2. G-T6 : selftest 68 sur 68 a chaque lecture ; le banc, 43 alterations mordues sur 43, rejoue a
l'identique par machine 2. G-T7 : plateforme consignee. G-T8 : machine 2 retrouve la matrice du moteur dans l'assemblage du bloc, ecart 0 sur
12 assemblages.""" % (c["sonde"], LECT["n"]))
P("""Les %d lectures de l'etage 2 sont toutes suivies : %d en deux iterations, %d en trois, %d en quatre ; poids au site au moins %.3f pour un
seuil de 0.5 ; residu rapporte a max(1, |lambda|) au plus %s pour un critere de 1e-11. La garde de singularite du bloc ne s'est declenchee a
aucune des %d lectures du run.""" % (LECT["n"], LECT["it"][2], LECT["it"][3], LECT["it"][4], math.floor(LECT["poids"] * 1000) / 1000.0, sup(LECT["res"]), LECT["n"] + n_instr))
T()
T("nn.4 LES DOUZE POINTS")
P("""Par point : les etats juges (ceux du depot au-dessus de dix planchers), ceux qui sont QUALIFIES, ceux ou la lecture deposee est sur le
plateau (consigne (e)) ; puis, pour l'etat lu (rang 0), son statut, sa largeur de plateau sous A et ln(G_dep / Gamma_pl(A)).""")
T("    id  w2       fact  delta  g         r_c  juges  QUAL  (e)  etat lu   Gamma_pl(A)  ln(G_dep/pl)")
for i in JUGES:
    rr = [r for r in E if r["id"] == i]; r0 = lus[i]
    T("    %-2s  %-7s  %-4s  %s  %s  %3d  %5d  %4d  %3d  %-8s  %s    %s" % (i, PD[i]["w2"], frac(PD[i]["facteur"]), delta(i), e2(PD[i]["g"]), PD[i]["r_c"], len(rr),
      sum(r["statut"] == "QUALIFIE" for r in rr), sum(bool(r["sur"]) for r in rr), r0["statut"], "%.3e" % r0["m"]["A"]["Gpl"], sg4(r0["ecart"])))
P("""Par point : le plus grand etalement de la meilleure fenetre sous chaque absorbeur (max / min - 1 sur cinq barreaux, soit un facteur 16
en eta ; seuil 0.05), le plus grand ecart a A (|ln|, seuil 0.05), et la consigne (e), |ln(G_dep / Gamma_pl(A))|.""")
T("    id   etalement, plus grand sous       ecart a A, plus grand     consigne (e)")
T("         A       B       C       D        B       C       D         mediane  plus grand")
for i in JUGES:
    rr = [r for r in E if r["id"] == i]
    T("    %-2s   %s  %s  %s  %s   %s  %s  %s    %s   %s" % ((i,) + tuple(f4(max(r["m"][x]["etal"] for r in rr)) for x in "ABCD") + tuple(f4(max(r["acc"][x] for r in rr)) for x in "BCD")
      + (f4(med([abs(r["ecart"]) for r in rr])), f4(max(abs(r["ecart"]) for r in rr)))))
P("""Aux douze points : %d etats au depot, %d juges, %d sous dix planchers. Par absorbeur : PLATEAU a %d etats sur %d sous A, sous B, sous C et
sous D ; accord a A manque a 0 etat pour B, 1 pour C, 0 pour D.""" % (depot_total, NJ, sous_plancher, NPA, NJ))
T()
T("nn.5 LE VERDICT")
P("""La cascade (gel, section 8) : l'instrument tient ; les douze points sont presents ; l'etat lu est QUALIFIE aux douze points ; %d etats
juges sur %d sont QUALIFIES, soit plus des neuf dixiemes (seuil %d) : ESTIMATEUR QUALIFIE. Aucun etat n'est NON LISIBLE.""" % (NQ, NJ, SEUIL))
P("""Etalement de la meilleure fenetre, mediane et plus grand, sur les %d etats : %s et %s sous A, %s et %s sous B, %s et %s sous C, %s et %s
sous D, pour un seuil de 0.05. Ecart a A, |ln|, mediane et plus grand : %s et %s pour B, %s et %s pour C, %s et %s pour D. Les plateaux des
douze points sont plus plats que ceux des points de reglage, dont les plus grands etalements etaient %s, %s, %s et %s.""" % (
    (NJ,) + tuple(v for x in "ABCD" for v in (f4(med(ET[x])), f4(max(ET[x])))) + tuple(v for x in "BCD" for v in (f4(med(AC[x])), f4(max(AC[x])))) + tuple(regl)))
P("""Ce que le gel autorise a ecrire (section 9), et rien de plus : "%s". Le reclassement du delta 95 ("%s") est leve pour ces %d etats, et
seulement pour eux, avec pour valeur Gamma_pl(A) : ces valeurs, de %s a %s, sont au verdict (verdict_ter.json). Pour une largeur DEPOSEE, il
n'est leve que si, de plus, la consigne (e) tient a cet etat : %d etats (nn.7).""" % (cit["phrase"], cit["reclassement"], NQ, e1(min(gpl_q)), e1(max(gpl_q)), N_DEP_LEVE))
T()
T("nn.6 L'ETAT NON QUALIFIE, ET LE POINT L3")
P("""Un seul etat n'est pas QUALIFIE : L3, rang %d, etiquette (%d, %d), G_dep %s. Il a un PLATEAU sous les quatre absorbeurs ; il echoue a
l'epreuve (c) : |ln(Gamma_pl(C) / Gamma_pl(A))| = %s pour tau = 0.05. B et D s'accordent a A a %s et %s.""" % (
    NQ1["rang"], NQ1["site"][0], NQ1["site"][1], e2(NQ1["G3"]), f4(NQ1["acc"]["C"]), f4(NQ1["acc"]["B"]), f4(NQ1["acc"]["D"])))
P("""Ce que ses douze barreaux montrent, sans rien rejuger : sous C (F1, 100 couches), deux fenetres ont un PLATEAU. Celle que la regle
retient, la plus plate, est du cote fort (k0 = %d, etalement %s, valeur %s) ; l'autre (k0 = %d, etalement %s, valeur %s) est a %s de A. C'est
le cas que la limite L-11 du gel decrivait, vu une fois au reglage. La regle n'est pas changee apres lecture : cet etat reste NON QUALIFIE, et
sa largeur reste reclassee.""" % (fC_ret[0], f4(float(fC_ret[1] - 1)), "%.3e" % fC_ret[2], fC_aut[0], f4(float(fC_aut[1] - 1)), "%.3e" % fC_aut[2], f4(acc_aut)))
P("""L3 (w2 = 211/100, facteur 3/2, g = %s) est le point juge de plus fort couplage, celui que la limite L-10 nommait. Les plus grands
etalements du run y sont, sous les quatre absorbeurs : %s, %s, %s et %s ; aux onze autres points, sur %d etats, ils sont %s, %s, %s et %s (tous
a L4). La plus petite marge du run est a L3, rang %d, sous %s : etalement %s pour un seuil de 0.05. Apres le %s de L3 rang 5, le plus grand
ecart de C a A est %s. Les treize autres etats de L3 sont QUALIFIES, son etat lu compris.""" % (
    e2(PD["L3"]["g"]), f4(max(r["m"]["A"]["etal"] for r in L3e)), f4(max(r["m"]["B"]["etal"] for r in L3e)), f4(max(r["m"]["C"]["etal"] for r in L3e)),
    f4(max(r["m"]["D"]["etal"] for r in L3e)), len(hors_L3), f4(hL3_et["A"]["m"]["A"]["etal"]), f4(hL3_et["B"]["m"]["B"]["etal"]), f4(hL3_et["C"]["m"]["C"]["etal"]),
    f4(hL3_et["D"]["m"]["D"]["etal"]), plus_petite_marge[1]["rang"], plus_petite_marge[2], f4(plus_petite_marge[0]), f4(NQ1["acc"]["C"]), f4(ac2)))
assert all(hL3_et[x]["id"] == "L4" for x in "ABCD") and plus_petite_marge[1]["id"] == "L3" and PD["L3"]["g"] == max(PD[i]["g"] for i in JUGES)
T()
T("nn.7 LA LECTURE DEPOSEE (consigne (e))")
P("""La lecture deposee est celle de la sonde dense du delta 98, a la facon de M17 : k = 3, F1, 20 couches. Sur les %d etats, qui ont tous un
PLATEAU sous A, |ln(G_dep / Gamma_pl(A))| a pour mediane %s et pour plus grande valeur %s. Elle depasse tau a %d etats : %s. Tous les %d sont
QUALIFIES : leur largeur est Gamma_pl(A), pas la lecture deposee.""" % (NJ, f4(med(EC)), f4(max(EC)), len(hors_e),
    ", ".join("%s rang %d (%s)" % (r["id"], r["rang"], f4(abs(r["ecart"]))) for r in hors_e), len(hors_e)))
P("""A l'etat lu, ln(G_dep / Gamma_pl(A)) vaut : %s. La lecture deposee de l'etat lu est sur le plateau a onze points ; a L4 elle est
au-dessus de son plateau de %d pour cent.""" % (", ".join("%s %s" % (i, sg4(lus[i]["ecart"])) for i in JUGES), round((math.exp(lus["L4"]["ecart"]) - 1) * 100)))
assert sum(bool(lus[i]["sur"]) for i in JUGES) == 11 and not lus["L4"]["sur"]
P("""Aucun signe ne domine : la lecture deposee est au-dessus du plateau a %d etats, au-dessous a %d ; la mediane de ln(G_dep / Gamma_pl(A))
est %s.""" % (sum(x > 0 for x in sg), sum(x < 0 for x in sg), sg4(med(sg))))
P("""Ce que cela dit de la lecture a la facon de M17, aux douze points et pas ailleurs : elle est a tau pres la largeur du plateau a %d etats
sur %d, et a un facteur %.2f pres partout.""" % (NSUR, NJ, math.ceil(math.exp(max(EC)) * 100) / 100.0))
T()
T("nn.8 LES ANNONCES DE LA PLUME, COMPTEES (gel, section 11)")
P("""Elles ont ete ecrites apres le reglage et avant tout calcul aux douze points.""")
P("""A-1 : la plume donnait 0.46 a ESTIMATEUR QUALIFIE, 0.08 a QUALIFIE A L'ETAT LU, 0.40 a QUALIFIE PAR POINT, 0.01 a NON QUALIFIE, 0.01 a
NON LISIBLE, 0.04 a NON CONCLUANT D'INSTRUMENT. L'issue qu'elle disait la plus probable est sortie.""")
P("""A-2 : elle donnait 0.02 a SUR LE PLATEAU a tous les etats, 0.23 a A NEUF ETATS SUR DIX AU MOINS, 0.75 a PAS PARTOUT. L'issue sortie est
celle a 0.23 : la plume s'est trompee de cote. Sa raison ("%s") ne s'est pas etendue aux points juges : a L3, la lecture deposee est sur le
plateau a %d etats sur %d.""" % (cit["e4"], sum(bool(r["sur"]) for r in L3e), len(L3e)))
def ann(k, texte, note=""):
    T("    %-4s (%.2f) %-53s %s%s" % (k, PA[k], texte, "VRAIE" if A[k] else "FAUSSE", ("  (" + note + ")") if note else ""))
ann("A-3", "l'etat lu est QUALIFIE aux onze points autres que L3")
ann("A-4", "L3 compte le plus d'etats non QUALIFIES", "1 ; 0 ailleurs")
ann("A-5", "delta negatif : aucun etalement sous A ni B > 0.02", "%s au plus" % f4(a5))
ann("A-6", "|ln(Gamma_pl(B) / Gamma_pl(A))| <= 0.02 partout", "%s au plus" % f4(max(AC["B"])))
ann("A-7", "l'instrument tient (annonce non aveugle)")
ann("A-8", "C a le plus d'etats sans PLATEAU, zero partout admis", "zero partout")
ann("A-9", "la mediane de la consigne (e) est entre 0.01 et 0.04", f4(med(EC)))
ann("A-10", "trois etats au plus sont NON LISIBLES", "%d" % NNL)
P("""Les huit annonces a deux issues sont vraies, pour une somme de probabilites de %.2f. A-8 n'est vraie que par sa clause "zero partout" et
n'apprend rien ; A-7 n'etait pas aveugle. La plume a ete pessimiste : son reglage s'appuyait sur E4 (g = 1.2e-2), ou trois etats sur
quatorze echouaient ; aucun des douze points juges n'en perd plus d'un. Elle n'en tire aucune phrase de calibrage : ces annonces ne sont pas
independantes.""" % somme_pa)
assert "E4 11/14" in gel and max(nnq_pt.values()) == 1
assert "l'estimation pour BOCAL4 est grossiere" in plat(lire(GEL + "/POUR_MACHINE2_gel_EB_ter_machine1_v1.md"))
T()
T("nn.9 DEFAUTS ET RESERVES")
P("""D-TER-1 (m1 ; observation O-1 de machine 2) : le gel (section 4, (iii)) dit du temoin negatif que sa largeur "%s". L'ecart du rapport a 2
est de %s au plus dans le run, soit %s en relatif : le chiffre du gel n'est juste qu'en relatif, et il ne le dit pas. Aucun seuil n'en
depend.""" % (cit["tn"], f4(tn_abs), f4(tn_abs / 2)), 2, 4)
P("""D-TER-2 (m1 ; O-2) : l'invocation ecrite par la plume, python -I avec le levier X86_V4, etait celle de son conteneur. Machine 2 a joue
autrement et l'a dit (nn.2) ; les ancres du run sont a %s de la reference de machine 1.""" % e1(anc), 2, 4)
P("""D-TER-3 (m1 ; O-3) : le selftest et le banc de la feuille n'executent ni son etape "instrument" ni son etape "verdict". La plume ne
les avait eprouvees que par des essais a part (les sorties de son conteneur, des sorties synthetiques), et l'avait dit a machine 2. Ce qui
tient ces etapes : le banc de sorties de machine 2 (38 cas sur 38, reponses declarees avant le passage) et sa feuille independante (0 ecart sur
le run).""", 2, 4)
P("""D-TER-4 (m1 ; O-4) : la garde de singularite du bloc n'a jamais ete declenchee par une matrice reellement singuliere, ni au reglage ni au
run. Machine 2 l'a eprouvee sur un echec de factorisation simule.""", 2, 4)
P("""D-TER-5 (m1) : le cout. Le gel annoncait de l'ordre de 7.1 h de calcul cumule pour l'etage 2 ; les douze processus de BOCAL4 en ont pris
%.1f (%d s), pour %d minutes d'horloge. L'estimation venait de deux coeurs partages ; la note d'accompagnement du gel la disait grossiere.""" % (
    cumul / 3600.0, round(cumul), round(((h_fin[0] * 3600 + h_fin[1] * 60 + h_fin[2]) - (h_instr[0] * 3600 + h_instr[1] * 60 + h_instr[2])) / 60.0)), 2, 4)
P("""D-TER-6 (m1) : le prix du reglage. Pour ecrire ce gel, la plume a vu sous absorbeur long les six points de M17 puis huit points des
deltas 96, 97 et 98, apres avoir ecrit le matin meme a machine 2 de ne rien calculer a ces derniers. Ces quatorze points ne peuvent plus etre
juges a l'aveugle. Le gel le dit (L-1) ; la note d'accompagnement du gel le dit a machine 2.""", 2, 4)
P("""R-TER-1 (m2, note du resultat) : son lecteur, independant du bloc, n'a pas lu les douze points, le gel ne se rejouant pas apres lecture.
Aux douze points, la MESURE n'a donc qu'un lecteur, celui de machine 1, joue sur deux plateformes. Le lecteur de machine 2 le retrouve aux
ancres et au temoin positif (192 lectures, ecart relatif au pire 2.0e-10), pas ailleurs. Le JUGEMENT, lui, a deux feuilles.""", 2, 4)
P("""R-TER-2 (m2, certification) : "l'etat lu" est le rang 0 du depot du delta 98, non recalcule. Machine 2 a montre hors chaine (lot %s)
qu'aux six points de M17 la regle du moteur departage l'etat lu du suivant par une marge de recouvrement de 0.3 a 9 pour cent, pour des
largeurs qui different d'un facteur 22 a 30. Ce gel juge chaque etat par son etiquette : la qualification d'un etat ne depend pas de ce choix
; le rang qu'on appelle "etat lu", si. Il en va de meme ici : au depot, le rapport des recouvrements des rangs 0 et 1 va de %.3f (%s) a
%.3f (%s) aux douze points, pour des largeurs deposees qui different d'un facteur %.1f a %.0f. L'etat de rang 1 est juge a dix points sur
douze et y est QUALIFIE ; a M3 et M4 il est sous dix planchers. L'enonce fort de cet acte est donc celui des %d etats sur %d, pas celui de
"l'etat lu".""" % (c["lot_lecteur"], min(rec.values()), min(rec, key=rec.get), max(rec.values()), max(rec, key=rec.get),
    math.floor(min(fact_larg.values()) * 10) / 10.0, math.ceil(max(fact_larg.values())), NQ, NJ), 2, 4)
P("""R-TER-3 (m2 ; O-5) : sa feuille a ete ecrite apres lecture de celle de machine 1. Elle en est independante par structure et par ses
terrains (38 etats reels, 20000 synthetiques, 2657206 cas de cascade : 0 desaccord), pas par ignorance.""", 2, 4)
P("""R-TER-4 (m2 ; O-6) : les ouvertures ne sont pas attestees a machine 2 (nn.11).""", 2, 4)
P("""Restent a dire, du gel : L-1 (apres coup : les longueurs, la forme de reference et l'echelle ont ete choisies apres la nuit bis et apres
quatorze points deja joues) ; L-7 (machine 1 connaissait les largeurs deposees aux douze points : la consigne (e) n'etait pas aveugle a G_dep)
; L-9 (C n'isole pas la forme : F1 y est jouee a 100 couches contre F2 a 80).""", 2, 4)
P("""De machine 2, declare par elle : deux de ses controles ont mordu a ses premiers jets, par sa faute, sans toucher au gel.""", 2, 4)
T()
T("nn.10 CE QUE LE RESULTAT CHANGE A CE QUI ETAIT ECRIT")
P("""Delta 95 (nuit bis). Son verdict, NON QUALIFIE, n'est pas touche : il porte sur l'etat lu des six points de M17 sous des absorbeurs de
20 et 30 couches. Son reclassement est leve pour %d etats de douze points du delta 98, a la valeur Gamma_pl(A), et pour leur largeur deposee a
%d d'entre eux. Il reste entier partout ailleurs : aucun Gamma de M17 ni d'aucune manche depuis juillet n'est requalifie par cet acte, leurs
points n'etant pas parmi les douze.""" % (NQ, N_DEP_LEVE))
P("""Note %s (hors chaine, apres coup, une plume). Elle disait qu'aux six points de M17 l'etat lu a un plateau des que l'absorbeur est long,
et que la nuit bis ne l'avait pas vu parce que ses absorbeurs faisaient 20 et 30 couches. Sur douze points que la plume n'avait pas vus sous
absorbeur long, sous un gel certifie avant le run, cette lecture tient. Les six points de M17 eux-memes restent hors chaine ; machine 2 a
rejoue la note par son propre lecteur (lot %s, hors chaine) et en retrouve les tableaux.""" % (c["note"], c["lot_rejeu"]))
P("""Delta 98. Il comparait la chaine E-A d'ordre 2 a la lecture de E-B a k = 3, et ecrivait : "%s" De ses %d etats juges, %d sont QUALIFIES
ici, et la lecture deposee est sur le plateau a %d d'entre eux. Son verdict et ses rapports ne sont pas touches ; cet acte n'en recalcule aucun
contre Gamma_pl(A), et il ne dit pas que la chaine est qualifiee : ce gel ne lit pas la chaine.""" % (cit["statut98"], len(j98), n98_q, n98_sur))
P("""Deltas 96 et 97, et le verdict PAS DE SIGNAL de M17 : non touches.""")
P("""Gel bis, "%s" : leve par l'operateur pour ce gel. Ce gel-ci se ferme a son tour : il ne se rejoue pas apres lecture, et "%s".""" % (cit["dernier"], cit["suite"]))
T()
T("nn.11 A ARBITRER PAR L'OPERATEUR")
P("""(i) Le numero (E18) et le depot.""")
P("""(ii) Les ouvertures. Machine 1 declare que l'operateur lui a ecrit "ouvre" (15/11/2026, 08 h 38) puis "go" (15/11/2026, 10 h 28), ce qui
levait le garde-fou du gel bis. Machine 2 ne peut pas le verifier ; le message qui l'a fait jouer est celui de l'operateur : "%s". Seul
l'operateur peut attester le reste ; son message de depot le dit ou non.""" % cit["message"], 2, 6)
P("""(iii) La suite. Cet acte n'en propose aucune comme decidee. Il en existe : faire lire les douze points par le lecteur de machine 2, pour
que la mesure ait deux lecteurs, ce qui est une decision de l'operateur sous un autre nom que ce gel ; relire la chaine d'ordre 2 du delta 98
contre Gamma_pl(A), sous un gel ; porter la question a d'autres fractions que 0.70 ou a un autre canal ; reprendre les points de M17, qui ne
peuvent plus etre juges a l'aveugle ; ou rien, ce verdict se deposant tel quel.""", 2, 6)
P("""(iv) Les regles. Cet acte n'en propose aucune (nn.12).""", 2, 6)
T()
T("nn.12 REGLES CANDIDATES SOUS (X)")
P("""Aucune regle nouvelle ; trente-quatre attendent la revue. Pour cette revue, un fait de ce chantier : le banc de sorties de machine 2
joue les etapes de la feuille que le selftest et le banc de machine 1 ne jouaient pas (D-TER-3). C'est une pratique de la machine qui
certifie, pas une regle proposee ici.""")
T()
T("nn.13 LE CANAL")
P("""Lots echanges pour ce chantier (canons) : machine 1 -- la note hors chaine %s, le gel et ses instruments %s ; machine 2 -- son lecteur
creux %s et son rejeu de la note %s, hors chaine et non certifies, la certification %s, le resultat %s. Les deux lots hors chaine de machine 2
ne sont parvenus a machine 1 qu'avec le resultat : le gel a ete ecrit sans eux. Les enveloppes qui ont porte ces lots ne sont pas des lots et
ne se citent pas.""" % (c["lot_note"], c["lot_gel"], c["lot_lecteur"], c["lot_rejeu"], c["lot_cert"], c["lot_res"]))
T()
T("nn.14 CE QUE CE DELTA NE FAIT PAS")
P("""Il ne dit rien hors des douze points, de la fraction 0.70, du canal (2,1) de x^5, ni des etats sous dix planchers du depot. Il ne
requalifie aucune largeur de M17 ni d'une manche anterieure. Il ne dit rien de l'unitarite, des extensions auto-adjointes ni de la dynamique
du systeme ferme. Il ne dit pas que la chaine est qualifiee. Il ne reecrit aucun verdict depose : celui de la nuit bis reste NON QUALIFIE sous
son gel. Il ne rejuge rien sous un autre seuil, un autre absorbeur, une autre echelle ou une autre regle de fenetre : l'etat L3 rang 5 reste
NON QUALIFIE. Il ne prend aucun numero, n'adopte aucune regle, n'edite aucune piece citee (PB-1).""")
T()
T("nn.15 PIECES DU LOT")
for a, b in (("%s.md" % NOM, "cet acte"),
             ("ecrire_acte_EB_ter_machine1_v1.py", "le script qui pose nombres et canons"),
             ("lecture_ter_rejouee_machine1.log, verdict_ter_rejoue_machine1.json", ""),
             ("lecture_ter_instrument_rejouee_machine1.log,", ""),
             ("verdict_ter_instrument_rejoue_machine1.json", "la feuille rejouee par machine 1"),
             ("rejeu_partiel_machine1_v1.py, comparaison_rejeu_machine1_v1.py / .log / .json", ""),
             ("sonde_ter_point_L3_rejeu_machine1.json, rejeu_partiel_<id>.json (onze)", "le rejeu de machine 1"),
             ("console_point_L3_rejeu_machine1.log, console_rejeu_partiel_machine1.log", "ses journaux"),
             ("releve_acte_EB_ter_machine1_v1.py / .log", "le releve de sortie de machine 1"),
             ("contre_epreuve_releve_acte_EB_ter_machine1_v1.py / .log", "ce releve, sur des copies alterees"),
             ("POUR_MACHINE2_acte_EB_ter_machine1_v1.md", "la note d'accompagnement"),
             ("fabrique_lot_machine1_v2.py", "")):
    T("  " + a)
    if b: T("      " + b)
P("""Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.""")
T()
T("-- FIN %s --" % NOM)

texte = "\n".join(L) + "\n"
texte.encode("ascii")
assert "%" not in texte, "un signe pour cent"
longues = [(n + 1, len(l), l) for n, l in enumerate(L) if len(l) > 100]; assert not longues, longues
assert not any(l != l.rstrip() for l in L)
open(os.path.join(SORTIE, NOM + ".md"), "w", encoding="ascii", newline="\n").write(texte)
print("ecrit %s.md : %d lignes, canon %s" % (NOM, len(L), B(os.path.join(SORTIE, NOM + ".md"))))
