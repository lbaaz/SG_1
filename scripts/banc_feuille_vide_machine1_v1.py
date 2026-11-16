# -*- coding: ascii -*-
"""BANC DE LA FEUILLE DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16. Il doit MORDRE.
Fabrique des dossiers de run SYNTHETIQUES pour la table gelee (aucune mesure : des plateaux poses a la main autour de la
prediction de chaque cellule ; ils ne disent rien des cellules), joue la feuille dessus, et compare a l'effet ECRIT AVANT.
Une seule chose change a la fois par rapport au cas de base. Chaque cas dit ce qu'il attend ; le banc compte les cas tenus.
Usage : python3 -I -B banc_feuille_vide_machine1_v1.py <feuille_vide.py> <lecture_lecteur_gel_loi (deposee)> <table des cellules.json>
        <sonde_vide.py> <sonde_lecteur_gel_loi (deposee)> <moteur> <dossier de travail (neuf)>"""
import sys, os, json, math, copy, shutil, subprocess, hashlib, unicodedata
FEUILLE, F_LECT, TABLE, S_VIDE, S_LECT, MOTEUR, TRAVAIL = sys.argv[1:8]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
T = json.load(open(TABLE)); CELLULES = T["cellules"]; KS = list(range(-3, 9))
ABSORBEURS = [["A", "F2", 0, 80], ["B", "F2", 0, 100], ["C", "F1", 0, 100], ["D", "F2", 10, 80]]
ENTETE = {"sonde": "sonde_vide_machine1_v1", "sonde_canon": canon_B(S_VIDE), "table_canon": canon_B(TABLE), "prevol": False, "moteur_canon": canon_B(MOTEUR),
          "source_bloc_canon": canon_B(S_LECT), "reglage": {"ks": KS, "absorbeurs": ABSORBEURS}}
BASE = {"ln_q": 0.002, "ecarts": {"B": 0.001, "C": -0.001, "D": 0.002}, "ondulation_A": 0.0, "derive_A": False, "non_suivi": None,
        "jumeau": 1e-60, "jumeau_non_suivi": False}
os.makedirs(TRAVAIL, exist_ok=False)

def lecture(g, suivi=True):
    return {"gamma": g, "gamma_im": g, "E_re": 0.0, "poids_site": 0.999, "residu": 1e-13, "iterations": 2, "suivi": suivi, "decalage_repris": False}

def fichier(c, r, entete):
    """r : reglage de la cellule. Le plateau sous A vaut exp(ln_G3 - ln_q) ; B, C, D en sont a exp(ecart)."""
    gpl = math.exp(c["ln_G3"] - r["ln_q"])
    def traj(nom):
        base = gpl * (math.exp(r["ecarts"][nom]) if nom != "A" else 1.0); t = {}
        for i, k in enumerate(KS):
            g = base
            if nom == "A" and r["ondulation_A"]:
                g = base * (1.0 + r["ondulation_A"] * (i % 2))            # un barreau sur deux plus haut : etalement = ondulation
            if nom == "A" and r["derive_A"]:
                g = base * math.exp(0.05 * i)                             # derive : aucun plateau
            t[str(k)] = lecture(g, suivi=(r["non_suivi"] != nom))
        return t
    geo = {a: {"forme": f, "bord": c["r_c"] + dr, "couches": L, "N": c["r_c"] + dr + L} for a, f, dr, L in ABSORBEURS}
    jum = {a: {str(k): lecture(r["jumeau"] if r["jumeau"] < 1.0 else gpl * (r["jumeau"] - 1.0)) for k in KS} for a in "ABCD"}
    if r["jumeau_non_suivi"]:
        jum["C"]["2"]["suivi"] = False
    S = dict(copy.deepcopy(entete), cellule={"id": c["id"], "w2": c["w2"], "m": c["m"], "g": c["g"], "r_c": c["r_c"], "eta0": c["eta0"]},
             jumeau={"signe": 1, "site": [0, 0], "E_depart": 0.0, "traj": jum, "absorbeurs": geo},
             fantome={"signe": -1, "site": [0, 0], "E_depart": 0.0, "traj": {a: traj(a) for a in "ABCD"}, "absorbeurs": geo})
    return S

def jouer(nom, par_cellule=None, instrument="TIENT", absents=(), entetes=None, retouche=None, table=TABLE):
    d = os.path.join(TRAVAIL, nom); os.makedirs(d)
    json.dump({"instrument": instrument}, open(os.path.join(d, "verdict_ter_instrument.json"), "w"))
    for c in CELLULES:
        if c["id"] in absents:
            continue
        r = dict(BASE); r.update((par_cellule or {}).get(c["id"], {}))
        S = fichier(c, r, dict(ENTETE, **((entetes or {}).get(c["id"], {}))))
        if retouche and c["id"] in retouche:
            retouche[c["id"]](S)
        json.dump(S, open(os.path.join(d, "sonde_vide_%s.json" % c["id"]), "w"))
    p = subprocess.run([sys.executable, "-I", "-B", FEUILLE, F_LECT, table, d, os.path.join(d, "verdict_vide.json")], capture_output=True, text=True)
    V = json.load(open(os.path.join(d, "verdict_vide.json"))) if os.path.exists(os.path.join(d, "verdict_vide.json")) else None
    return p.returncode, V

def cel(V, i):
    return [x for x in V["cellules"] if x["id"] == i][0]

LIS = [c["id"] for c in CELLULES if c["ligne"] == "lisible"]; PRO = [c["id"] for c in CELLULES if c["ligne"] == "profonde"]
assert len(LIS) == 16 and len(PRO) == 12
CAS = []
def cas(nom, attendu, test, **kw):
    code, V = jouer(nom, **kw)
    try:
        ok = bool(test(code, V))
    except Exception as e:
        ok = False; attendu += " [exception : %r]" % (e,)
    CAS.append((nom, ok)); print("  %-4s %s : %s" % ("TENU" if ok else "RATE", nom, attendu), flush=True)

v1 = lambda V: V["V1"]["issue"]; vp = lambda V: V["VP"]["issue"]
cas("b00_base", "toutes les cellules tiennent : V1 TENU (16), VP TENU (12)",
    lambda c, V: c == 0 and v1(V) == "TENU" and vp(V) == "TENU" and V["V1"]["comptes"]["TIENT"] == 16 and V["VP"]["comptes"]["TIENT"] == 12)
cas("b01_une_tombe", "MG4 a ln q = +0.05 : MG4 TOMBE, V1 TENU SAUF UNE CELLULE, VP inchange",
    lambda c, V: cel(V, "MG4")["jugement"] == "TOMBE" and v1(V) == "TENU SAUF UNE CELLULE" and V["V1"]["tombees"] == ["MG4"] and vp(V) == "TENU", par_cellule={"MG4": {"ln_q": 0.05}})
cas("b02_signe", "MG4 a ln q = -0.05 : TOMBE aussi (valeur absolue)",
    lambda c, V: cel(V, "MG4")["jugement"] == "TOMBE" and cel(V, "MG4")["ln_q"] < 0, par_cellule={"MG4": {"ln_q": -0.05}})
cas("b03_deux_tombent", "MG4 et PP5 a ln q = 0.05 : V1 TOMBE",
    lambda c, V: v1(V) == "TOMBE" and sorted(V["V1"]["tombees"]) == ["MG4", "PP5"], par_cellule={"MG4": {"ln_q": 0.05}, "PP5": {"ln_q": 0.05}})
cas("b04_non_jugeable", "MP3 a ln q = 0.02, sur la tolerance : NON JUGEABLE ; V1 reste TENU (15 tenues)",
    lambda c, V: cel(V, "MP3")["jugement"] == "NON JUGEABLE" and v1(V) == "TENU" and V["V1"]["comptes"]["TIENT"] == 15, par_cellule={"MP3": {"ln_q": 0.02}})
cas("b05_trop_de_non_jugeables", "cinq cellules lisibles a ln q = 0.02 (une ou deux par creneau) : 11 jugees, V1 NON CONCLUANT",
    lambda c, V: v1(V) == "NON CONCLUANT" and V["V1"]["comptes"]["NON JUGEABLE"] == 5,
    par_cellule={i: {"ln_q": 0.02} for i in ("MG3", "MP3", "PP3", "PG3", "MG4")})
cas("b06_creneau_vide", "PG3, PG4, PG5 a ln q = 0.02 : 13 jugees mais une seule tenue au creneau PG : V1 NON CONCLUANT",
    lambda c, V: v1(V) == "NON CONCLUANT" and V["V1"]["comptes"]["TIENT"] == 13, par_cellule={i: {"ln_q": 0.02} for i in ("PG3", "PG4", "PG5")})
cas("b07_desaccord_C", "PP4 : plateau sous C a 0.08 de A : NON QUALIFIE, cellule NON LUE ; V1 TENU (15)",
    lambda c, V: cel(V, "PP4")["lecteur"]["statut"] == "NON QUALIFIE" and cel(V, "PP4")["jugement"] == "NON LUE" and v1(V) == "TENU",
    par_cellule={"PP4": {"ecarts": {"B": 0.001, "C": 0.08, "D": 0.002}}})
cas("b08_pas_de_plateau", "PP4 : derive sous A, aucun plateau : NON QUALIFIE, NON LUE",
    lambda c, V: cel(V, "PP4")["lecteur"]["statut"] == "NON QUALIFIE" and cel(V, "PP4")["jugement"] == "NON LUE", par_cellule={"PP4": {"derive_A": True}})
cas("b09_non_suivi", "PP4 : aucune lecture suivie sous B : NON LISIBLE, NON LUE",
    lambda c, V: cel(V, "PP4")["lecteur"]["statut"] == "NON LISIBLE" and cel(V, "PP4")["jugement"] == "NON LUE", par_cellule={"PP4": {"non_suivi": "B"}})
cas("b10_temoin_trop_large", "PP4 : le jumeau a une largeur de 1e-3 du plateau : temoin non tenu, NON LUE",
    lambda c, V: cel(V, "PP4")["temoin"]["tient"] is False and cel(V, "PP4")["jugement"] == "NON LUE" and "temoin" in cel(V, "PP4")["motif"], par_cellule={"PP4": {"jumeau": 1.001}})
cas("b11_temoin_non_suivi", "PP4 : une lecture du jumeau non suivie : temoin non tenu, NON LUE",
    lambda c, V: cel(V, "PP4")["temoin"]["tient"] is False and cel(V, "PP4")["temoin"]["suivies"] == 47 and cel(V, "PP4")["jugement"] == "NON LUE", par_cellule={"PP4": {"jumeau_non_suivi": True}})
cas("b12_instrument", "l'instrument ne tient pas : rien n'est juge, aucune issue",
    lambda c, V: c == 0 and V["verdict"].startswith("L'INSTRUMENT NE TIENT PAS") and "V1" not in V, instrument="NE TIENT PAS")
cas("b13_fichier_absent", "le fichier de MG8 manque : RUN INCOMPLET, rien n'est juge",
    lambda c, V: V["verdict"].startswith("RUN INCOMPLET") and "V1" not in V and len(V["incomplet"]) == 1, absents=("MG8",))
cas("b14_canon_de_sonde", "le fichier de MG3 porte un autre canon de sonde : RUN INCOMPLET",
    lambda c, V: V["verdict"].startswith("RUN INCOMPLET") and "MG3" in V["incomplet"][0], entetes={"MG3": {"sonde_canon": "0" * 16}})
cas("b15_couplage", "le fichier de MG3 porte un autre couplage : RUN INCOMPLET",
    lambda c, V: V["verdict"].startswith("RUN INCOMPLET") and "MG3" in V["incomplet"][0], retouche={"MG3": lambda S: S["cellule"].update(g="4.31697e-03")})
cas("b16_fichier_de_prevol", "le fichier de MG3 est marque pre-vol : RUN INCOMPLET",
    lambda c, V: V["verdict"].startswith("RUN INCOMPLET"), entetes={"MG3": {"prevol": True}})
cas("b17_geometrie", "le fichier de MG3 porte une autre boite pour B : RUN INCOMPLET",
    lambda c, V: V["verdict"].startswith("RUN INCOMPLET") and "geometrie" in V["incomplet"][0], retouche={"MG3": lambda S: S["fantome"]["absorbeurs"]["B"].update(N=125)})
cas("b18_profondes_tombent", "MG12 et PG16 a ln q = 0.09 : VP TOMBE, V1 inchange (TENU)",
    lambda c, V: vp(V) == "TOMBE" and v1(V) == "TENU", par_cellule={"MG12": {"ln_q": 0.09}, "PG16": {"ln_q": 0.09}})
cas("b19_profondes_non_lues", "aucune cellule profonde n'a de plateau : VP NON LUE, V1 TENU",
    lambda c, V: vp(V) == "NON LUE" and v1(V) == "TENU" and V["VP"]["comptes"]["NON LUE"] == 12, par_cellule={i: {"derive_A": True} for i in PRO})
cas("b20_profondes_peu_lues", "sept cellules profondes sans plateau : cinq jugees, VP NON CONCLUANT",
    lambda c, V: vp(V) == "NON CONCLUANT" and V["VP"]["comptes"]["TIENT"] == 5, par_cellule={i: {"derive_A": True} for i in PRO[:7]})
cas("b21_tolerance_par_ligne", "ln q = 0.03 a MG3 (lisible, T = 0.02) et a MG8 (profonde, T = 0.05) : MG3 TOMBE, MG8 TIENT",
    lambda c, V: cel(V, "MG3")["jugement"] == "TOMBE" and cel(V, "MG8")["jugement"] == "TIENT", par_cellule={"MG3": {"ln_q": 0.03}, "MG8": {"ln_q": 0.03}})
cas("b22_bande_absorbeurs", "MG3 a ln q = 0.012 : TIENT avec des absorbeurs a 0.002 pres, NON JUGEABLE s'ils different de 0.015 (la bande porte l'etalement du lecteur)",
    lambda c, V: cel(V, "MG3")["jugement"] == "TIENT" and cel(V, "MG4")["jugement"] == "NON JUGEABLE" and abs(cel(V, "MG4")["etalement_du_lecteur"] - 0.015) < 1e-9,
    par_cellule={"MG3": {"ln_q": 0.012}, "MG4": {"ln_q": 0.012, "ecarts": {"B": 0.001, "C": -0.001, "D": 0.015}}})
cas("b23_bande_plateau", "MG3 : plateau sous A ondulant de 3 pour cent : QUALIFIE, mais la bande depasse la tolerance : NON JUGEABLE",
    lambda c, V: cel(V, "MG3")["lecteur"]["statut"] == "QUALIFIE" and cel(V, "MG3")["jugement"] == "NON JUGEABLE" and cel(V, "MG3")["bande"] > 0.02,
    par_cellule={"MG3": {"ondulation_A": 0.03}})
cas("b24_bande_chaine", "MG3 (etendue %.4f) et PG6 (etendue %.4f) a ln q = 0.0125 : la plus petite etendue TIENT, la plus grande est NON JUGEABLE" % (
    cel({"cellules": CELLULES}, "MG3")["etendue"], cel({"cellules": CELLULES}, "PG6")["etendue"]),
    lambda c, V: cel(V, "MG3")["jugement"] == "TIENT" and cel(V, "PG6")["jugement"] == "NON JUGEABLE", par_cellule={"MG3": {"ln_q": 0.0125}, "PG6": {"ln_q": 0.0125}})
autre = os.path.join(TRAVAIL, "autre_table.json"); TT = copy.deepcopy(T); TT["graine"] = "000000"; json.dump(TT, open(autre, "w"), indent=1, sort_keys=True)
cas("b25_autre_table", "une table qui n'est pas au canon du gel, sans --prevol : la feuille refuse (code 2), aucun verdict",
    lambda c, V: c == 2 and V is None, table=autre)
n = sum(1 for _, ok in CAS if ok)
print("BANC : %d cas tenus sur %d : %s" % (n, len(CAS), "IL MORD COMME ATTENDU" if n == len(CAS) else "DES CAS RATES : " + " ".join(x for x, ok in CAS if not ok)))
shutil.rmtree(TRAVAIL)
sys.exit(0 if n == len(CAS) else 1)
