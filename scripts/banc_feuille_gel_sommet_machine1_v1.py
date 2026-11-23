# -*- coding: ascii -*-
"""BANC DE LA FEUILLE DU GEL "SOMMET" -- machine 1, v1, 2026-11-22. Aucune mesure : des dossiers de run SYNTHETIQUES pour la
table gelee (des plateaux poses a la main autour de la prediction : ils ne disent RIEN des cellules), une chose changee a
la fois, et l'effet attendu ECRIT AVANT dans la liste CAS. La feuille est jouee telle quelle, en sous-processus.
Dossier de base : instrument TIENT ; neuf temoins positifs a leur reference ; 56 cellules avec ln q = +0.0005, etalement
du lecteur 0.001 (C / A), jumeau a 1e-20 du plateau, toutes lectures suivies.
Usage : python3 -I -B banc_feuille_gel_sommet_machine1_v1.py <feuille du gel> <feuille deposee du lecteur> <table gelee> <dossier de travail (neuf)>"""
import sys, os, json, math, copy, shutil, subprocess
FEUILLE, FEUILLE_LECTEUR, TABLE, TRAVAIL = sys.argv[1:5]
T = json.load(open(TABLE)); R = T["regle"]; KS = R["barreaux"]; ABSORBEURS = R["absorbeurs_du_lecteur"]
CEL = {c["id"]: c for c in T["cellules"]}; TEM = {c["id"]: c for c in T["temoins_positifs"]}
os.makedirs(TRAVAIL, exist_ok=False)

def fichiers(c, ln_gamma_A, m):
    """Les deux fichiers d'un point, au format du pilote de machine 2. m : les modifications de ce point."""
    gA = math.exp(ln_gamma_A); ecarts = {"A": 0.0, "B": 1e-4, "C": m.get("C_ecart", 1e-3), "D": -5e-4}
    def entete(signe):
        return {"pilote": "lecteur_2D_pilote_machine2_v1", "pilote_canon": m.get("pilote_canon", R["pilote_machine2_canon"]), "moteur_canon": R["moteur_canon"],
                "source_bloc_canon": R["source_bloc_canon"], "bloc_sha256_16": R["bloc_sha256_16"], "synthetique": True,
                "cellule": {"id": c["id"], "w2": c["w2"], "m": c["m"], "g": m.get("g", c["g"]), "r_c": c["r_c"], "eta0": m.get("eta0", float(c["eta0"])), "P": 5, "W1": 1.0},
                "reglage": {"ks": KS, "absorbeurs": ABSORBEURS, "iter_min": 2, "iter_max": 12, "tol_residu": 1e-11, "poids_min": 0.5},
                "lecture": {"signe": signe, "site": [0, 0], "E_depart": 0.0, "traj": {},
                            "absorbeurs": {a: {"forme": f, "bord": c["r_c"] + dr + (m.get("bord", 0) if a == "A" else 0), "couches": L, "N": c["r_c"] + dr + L} for a, f, dr, L in ABSORBEURS}}}
    fan = entete(-1); jum = entete(+1)
    for a in "ABCD":
        fan["lecture"]["traj"][a] = {}; jum["lecture"]["traj"][a] = {}
        for k in KS:
            g = gA * math.exp(ecarts[a])
            if a == "A" and m.get("A_etal") and k % 2 == 0: g *= 1.0 + m["A_etal"]
            if a == "B" and m.get("B_sans_plateau"): g *= 1.0 + 0.1 * (k % 2)
            suivi = not (a == "A" and k in m.get("A_non_suivis", []))
            fan["lecture"]["traj"][a][str(k)] = {"gamma": g if suivi else None, "suivi": suivi, "poids_site": 0.95, "residu": 1e-12, "iterations": 3}
            jum["lecture"]["traj"][a][str(k)] = {"gamma": gA * 1e-20, "suivi": True, "poids_site": 0.999, "residu": 1e-12, "iterations": 3}
    if "jumeau_max" in m: jum["lecture"]["traj"]["C"]["-3"]["gamma"] = gA * m["jumeau_max"]
    if m.get("jumeau_non_suivi"): jum["lecture"]["traj"]["D"]["8"]["suivi"] = False
    return fan, jum

def dossier(nom, mods, instrument="TIENT", cellules=True):
    d = os.path.join(TRAVAIL, nom); os.makedirs(d)
    if instrument is not None:
        json.dump({"instrument": instrument, "synthetique": True}, open(os.path.join(d, "verdict_ter_instrument.json"), "w"))
    points = [(c, c["ln_Gamma_pl_reference"] + mods.get(c["id"], {}).get("ecart_reference", 0.0)) for c in T["temoins_positifs"]]
    if cellules:
        points += [(c, c["ln_G3"] - mods.get(c["id"], {}).get("lnq", 0.0005)) for c in T["cellules"]]
    for c, lg in points:
        m = mods.get(c["id"], {})
        if m.get("absent"): continue
        fan, jum = fichiers(c, lg, m)
        json.dump(fan, open(os.path.join(d, "lect2D_%s_fantome.json" % c["id"]), "w")); json.dump(jum, open(os.path.join(d, "lect2D_%s_jumeau.json" % c["id"]), "w"))
    return d

def jouer(d, table=TABLE, temoins=False):
    s = os.path.join(d, "sortie_banc.json")
    p = subprocess.run([sys.executable, "-I", "-B", FEUILLE, FEUILLE_LECTEUR, table, d, s] + (["--temoins"] if temoins else []), capture_output=True, text=True)
    return p.returncode, (json.load(open(s)) if os.path.exists(s) else None), p.stdout

ids = list(CEL); w2s = sorted(set(c["w2"] for c in T["cellules"]), key=lambda z: eval(z))
quinze = [i for w in w2s for i in [c["id"] for c in T["cellules"] if c["w2"] == w][:2]][:15]
NJ = {"lnq": 0.008}                                          # entre T - b et T + b pour toute etendue de la table : NON JUGEABLE
k7_cinq = [c["id"] for c in T["cellules"] if c["kappa"] == "1.0000"][:5]
S1 = lambda issue, **comptes: {"verdict": "S1 " + issue, "S1.issue": issue, **{"S1.comptes." + k: v for k, v in comptes.items()}}
# (nom, ce qui est change, modifications, options, ATTENDU) -- l'attendu est ecrit ici, avant tout passage
CAS = [
 ("b01", "rien : le dossier de base", {}, {}, dict(S1("TENU", TIENT=56, TOMBE=0, **{"NON JUGEABLE": 0, "NON LUE": 0}), **{"portee": 7, "miroirs": 7, "plus_grand_ln_q": 0.0005})),
 ("b02", "une cellule tombe (ln q = +0.02)", {"MPa3": {"lnq": 0.02}}, {}, dict(S1("TENU SAUF UNE CELLULE", TIENT=55, TOMBE=1), **{"tombees": ["MPa3"]})),
 ("b03", "deux cellules tombent", {"MPa3": {"lnq": 0.02}, "PGb7": {"lnq": 0.02}}, {}, S1("TOMBE", TIENT=54, TOMBE=2)),
 ("b04", "une cellule tombe de l'autre cote (ln q = -0.02)", {"MGa1": {"lnq": -0.02}}, {}, dict(S1("TENU SAUF UNE CELLULE", TIENT=55, TOMBE=1), **{"tombees": ["MGa1"]})),
 ("b05", "une cellule non jugeable (ln q = 0.008)", {"MPa1": NJ}, {}, S1("TENU", TIENT=55, TOMBE=0, **{"NON JUGEABLE": 1})),
 ("b06", "quinze cellules non jugeables : 41 jugees", {i: NJ for i in quinze}, {}, S1("NON CONCLUANT", TIENT=41, **{"NON JUGEABLE": 15})),
 ("b07", "un w2 n'a que trois cellules tenues", {i: NJ for i in ["MPa1", "MPa2", "MPa3", "MPa4"]}, {}, S1("NON CONCLUANT", TIENT=52, **{"NON JUGEABLE": 4})),
 ("b08", "desaccord de l'absorbeur C (0.06) a une cellule", {"PPa5": {"C_ecart": 0.06}}, {}, dict(S1("TENU", TIENT=55, **{"NON LUE": 1}), **{"statut:PPa5": "NON QUALIFIE"})),
 ("b09", "pas de plateau sous B a une cellule", {"PPb2": {"B_sans_plateau": True}}, {}, dict(S1("TENU", TIENT=55, **{"NON LUE": 1}), **{"statut:PPb2": "NON QUALIFIE"})),
 ("b10", "A sans cinq barreaux lisibles consecutifs (k = 1 et 6 non suivis)", {"MGb4": {"A_non_suivis": [1, 6]}}, {}, dict(S1("TENU", TIENT=55, **{"NON LUE": 1}), **{"statut:MGb4": "NON LISIBLE"})),
 ("b11", "une lecture non suivie sous A hors de toute gene (k = 8)", {"MGb4": {"A_non_suivis": [8]}}, {}, dict(S1("TENU", TIENT=56), **{"statut:MGb4": "QUALIFIE"})),
 ("b12", "jumeau trop large (1e-5 du plateau)", {"PGa6": {"jumeau_max": 1e-5}}, {}, S1("TENU", TIENT=55, **{"NON LUE": 1})),
 ("b13", "une lecture du jumeau non suivie", {"PGa6": {"jumeau_non_suivi": True}}, {}, S1("TENU", TIENT=55, **{"NON LUE": 1})),
 ("b14", "l'instrument ne tient pas", {}, {"instrument": "NE TIENT PAS"}, {"verdict": "L'INSTRUMENT NE TIENT PAS : RIEN N'EST JUGE", "S1": None}),
 ("b15", "le verdict de l'instrument est absent", {}, {"instrument": None}, {"verdict": "L'INSTRUMENT NE TIENT PAS : RIEN N'EST JUGE", "S1": None}),
 ("b16", "un temoin positif a 0.002 de sa reference", {"Q2b": {"ecart_reference": 0.002}}, {}, {"verdict": "LES TEMOINS POSITIFS DU SOMMET NE TIENNENT PAS : RIEN N'EST JUGE", "S1": None, "temoins.tenus": 8}),
 ("b17", "un temoin positif non qualifie", {"Qd": {"C_ecart": 0.06}}, {}, {"verdict": "LES TEMOINS POSITIFS DU SOMMET NE TIENNENT PAS : RIEN N'EST JUGE", "S1": None, "temoins.tenus": 8}),
 ("b18", "un temoin positif a 0.0009 de sa reference (sous le seuil)", {"Qa": {"ecart_reference": 0.0009}}, {}, dict(S1("TENU", TIENT=56), **{"temoins.tenus": 9})),
 ("b19", "les fichiers d'une cellule manquent", {"MGa2": {"absent": True}}, {}, {"verdict": "RUN INCOMPLET : RIEN N'EST JUGE", "S1": None, "incomplet": 1}),
 ("b20", "un fichier porte un autre canon de pilote", {"MGa2": {"pilote_canon": "0000000000000000"}}, {}, {"verdict": "RUN INCOMPLET : RIEN N'EST JUGE", "S1": None, "incomplet": 1}),
 ("b21", "un fichier porte un autre couplage", {"MGa2": {"g": "1.65975e-04"}}, {}, {"verdict": "RUN INCOMPLET : RIEN N'EST JUGE", "S1": None, "incomplet": 1}),
 ("b22", "un fichier porte un autre eta0", {"MGa2": {"eta0": 6.47329e-04}}, {}, {"verdict": "RUN INCOMPLET : RIEN N'EST JUGE", "S1": None, "incomplet": 1}),
 ("b23", "un fichier porte un autre bord d'absorbeur", {"MGa2": {"bord": 1}}, {}, {"verdict": "RUN INCOMPLET : RIEN N'EST JUGE", "S1": None, "incomplet": 1}),
 ("b24", "une autre table (un couplage change)", {}, {"autre_table": True}, {"code": 2, "sortie": None}),
 ("b25", "etalement du plateau sous A de 0.008 : la bande depasse T", {"PPa1": {"A_etal": 0.008}}, {}, S1("TENU", TIENT=55, **{"NON JUGEABLE": 1})),
 ("b26", "cinq cellules de kappa = 1 non lues : la portee perd ce kappa", {i: {"jumeau_max": 1e-5} for i in k7_cinq}, {}, dict(S1("TENU", TIENT=51, **{"NON LUE": 5}), **{"portee": 6, "portee_sans": "1.0000"})),
 ("b27", "etape de garde, avant toute cellule", {}, {"temoins": True, "cellules": False}, {"verdict": "TIENT : les cellules peuvent etre lues", "code": 0}),
 ("b28", "etape de garde, alors que des cellules sont deja lues", {}, {"temoins": True}, {"code": 3}),
 ("b29", "etape de garde, l'instrument ne tient pas", {}, {"temoins": True, "cellules": False, "instrument": "NE TIENT PAS"}, {"verdict": "L'INSTRUMENT NE TIENT PAS : aucune cellule ne doit etre lue"}),
 ("b30", "etape de garde, un temoin positif hors de sa reference", {"Qc": {"ecart_reference": -0.002}}, {"temoins": True, "cellules": False}, {"verdict": "LES TEMOINS POSITIFS NE TIENNENT PAS : aucune cellule ne doit etre lue"}),
]
tenus = 0
for (nom, quoi, mods, opt, att) in CAS:
    d = dossier(nom, mods, instrument=opt.get("instrument", "TIENT"), cellules=opt.get("cellules", True)); table = TABLE
    if opt.get("autre_table"):
        t2 = copy.deepcopy(T); t2["cellules"][0]["g"] = "3.91072e-05"; table = os.path.join(d, "autre_table.json"); json.dump(t2, open(table, "w"), indent=1, sort_keys=True)
    code, out, console = jouer(d, table, temoins=opt.get("temoins", False)); vu = {}
    for cle, v in att.items():
        if cle == "code": vu[cle] = code
        elif cle == "sortie": vu[cle] = out
        elif out is None: vu[cle] = "(pas de sortie)"
        elif cle == "verdict": vu[cle] = out.get("verdict")
        elif cle == "S1": vu[cle] = out.get("S1")
        elif cle == "S1.issue": vu[cle] = out["S1"]["issue"]
        elif cle.startswith("S1.comptes."): vu[cle] = out["S1"]["comptes"][cle[11:]]
        elif cle == "tombees": vu[cle] = out["S1"]["tombees"]
        elif cle == "portee": vu[cle] = len(out["S1"]["portee_kappa"])
        elif cle == "portee_sans": vu[cle] = v if v not in out["S1"]["portee_kappa"] else "(present)"
        elif cle == "miroirs": vu[cle] = len(out["consigne"]["paires_miroirs"])
        elif cle == "plus_grand_ln_q": vu[cle] = round(out["consigne"]["plus_grand_ln_q"], 6)
        elif cle.startswith("statut:"): vu[cle] = [r for r in out["cellules"] if r["id"] == cle[7:]][0]["lecteur"]["statut"]
        elif cle == "temoins.tenus": vu[cle] = out["temoins_positifs"]["tenus"]
        elif cle == "incomplet": vu[cle] = len(out["incomplet"])
    ok = all(vu[c] == att[c] for c in att); tenus += ok
    print("%s  %-68s : %s" % (nom, quoi, "TIENT" if ok else "NE TIENT PAS"))
    print("       attendu %s" % json.dumps(att, sort_keys=True))
    if not ok: print("       vu      %s" % json.dumps(vu, sort_keys=True, default=str))
print("BANC DE LA FEUILLE : %d cas, %d tenus" % (len(CAS), tenus))
shutil.rmtree(TRAVAIL)
sys.exit(0 if tenus == len(CAS) else 1)
