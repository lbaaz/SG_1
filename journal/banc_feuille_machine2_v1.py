# -*- coding: ascii -*-
"""BANC DE MACHINE 2 pour la feuille de lecture de machine 1 (lecture_chaine_par_etat_machine1_v1.py), gel 9df2702af59adbbc.
Deux parties, toutes deux sur des sondes SYNTHETIQUES (aucune mesure) :
  A. LECTEUR INDEPENDANT. Ecrit par machine 2 a partir du TEXTE du gel (sections 5, 6, 7, 8), sans copier la feuille ; compare a la
     feuille sur N sondes tirees au hasard, aux bords exacts des seuils (egalites, 0.4999, 2.0, 1.33e-12 ...) : verdict, statut
     de chaque point, nombre d'etats juges, motif de chaque etat.
  B. MUTATIONS. Vingt-quatre alterations d'une ligne de la feuille ; pour chacune : le selftest de machine 1 mord-il ? mon banc A mord-il ?
Usage : python -P banc_feuille_machine2_v1.py <feuille.py> [N_sondes]       (graine fixe)."""
import importlib.util
import math
import os
import random
import subprocess
import sys
import tempfile

FEUILLE = os.path.abspath(sys.argv[1])
NSONDES = int(sys.argv[2]) if len(sys.argv) > 2 else 3000


def charger(chemin, nom):
    sp = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


# ------------------------------------------------------------------ A. le lecteur independant (texte du gel)
POINTS = {"J1": ("juge", "19/10", "1/1"), "J2": ("juge", "21/10", "1/1"), "J3": ("juge", "39/20", "3/2"), "J4": ("juge", "41/20", "3/2"),
          "J5": ("juge", "39/20", "2/3"), "J6": ("juge", "41/20", "2/3"), "T1": ("temoin", "49/25", "1/1"), "T2": ("temoin", "51/25", "1/1"),
          "T3": ("temoin", "37/20", "1/1"), "T4": ("temoin", "43/20", "1/1"), "A1": ("ancre", "39/20", "1/1"), "A2": ("ancre", "41/20", "1/1")}
CANON = "82a0be882568fe0c"
REFS = {"A1": (7, 2, 2.1623273017950654e-10), "A2": (8, 2, 2.6613925716641374e-09)}


def motif(e):
    """Sections 5 (1) a (8) du gel, dans l'ordre. None = juge."""
    if not e["J_ecart_type"] < 0.2:
        return "(1)"
    if e["n1"] < 0 or e["n2"] < 0:
        return "(2)"
    if not e["poids_site"] >= 0.5:
        return "(3)"
    if not e["Gamma_2D"]["3"] > 1.33e-12:
        return "(4)"
    if e["suivi"]["2"] < 0.9 or e["suivi"]["4"] < 0.9:
        return "(5)"
    g = [e["Gamma_2D"][k] for k in ("2", "3", "4")]
    if not (max(g) / min(g) <= 2.0):
        return "(6)"
    c = e["chaine"]
    if c["erreur"] is not None or c["vide"] or not c["definie"]:
        return "(7)"
    if not (max(c["gammas"]) / min(c["gammas"]) <= 2.0):
        return "(8)"
    return None


def lecteur(s):
    # section 8 : gardes
    mot = []
    if s["moteur_canon"] != CANON:
        mot.append("G1")
    pts = {p["id"]: p for p in s["points"]}
    if len(s["points"]) != 12 or set(pts) != set(POINTS):
        mot.append("G2")
    else:
        for pid, (r, w, f) in POINTS.items():
            p = pts[pid]
            if (p["role"], p["w2"], p["facteur"]) != (r, w, f):
                mot.append("G2")
            a, b = f.split("/")
            if abs(p["g"] - p["g_regle"] * int(a) / int(b)) > 1e-12 * p["g_regle"]:
                mot.append("G2g")
            if p["faisable"] and len(p["etats"]) != 14:
                mot.append("G3")
        for pid, (n1, n2, ref) in REFS.items():
            p = pts[pid]
            tr = [e for e in p["etats"] if e["n1"] == n1 and e["n2"] == n2]
            if not p["faisable"] or len(tr) != 1 or abs(tr[0]["Gamma_2D"]["3"] / ref - 1) > 1e-2:
                mot.append("G4" + pid)
    res = {}
    for pid, p in pts.items():
        if not p["faisable"]:
            res[pid] = ("NL", 0, [])
            continue
        cnt = {}
        for e in p["etats"]:
            cnt[(e["n1"], e["n2"])] = cnt.get((e["n1"], e["n2"]), 0) + 1
        ms, qs = [], []
        for e in p["etats"]:
            m = motif(e)
            if m is None and cnt[(e["n1"], e["n2"])] >= 2:
                m = "(9)"
            ms.append(m)
            if m is None:
                qs.append(e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"])
        if len(qs) < 6:
            res[pid] = ("NL", len(qs), ms)
        elif all(0.5 <= q <= 2.0 for q in qs):
            res[pid] = ("F2", len(qs), ms)
        elif all(10 ** -0.5 <= q <= 10 ** 0.5 for q in qs):
            res[pid] = ("DEC", len(qs), ms)
        else:
            res[pid] = ("HD", len(qs), ms)
    if mot:
        return "NCI", res
    jug = [res[p][0] for p in POINTS if POINTS[p][0] == "juge"]
    lis = [x for x in jug if x != "NL"]
    if len(lis) < 4:
        return "NL", res
    tenus = [x for x in lis if x in ("F2", "DEC")]
    if len(tenus) == len(lis):
        return "TENU", res
    return ("PARTIE" if tenus else "NON TENU"), res


TRAD = {"ORDRE DE GRANDEUR TENU HORS PLAGE": "TENU", "TENU EN PARTIE": "PARTIE", "NON TENU": "NON TENU",
        "NON LISIBLE": "NL", "NON CONCLUANT D'INSTRUMENT": "NCI"}
TRADP = {"FACTEUR 2": "F2", "DECADE": "DEC", "HORS DECADE": "HD", "NON LISIBLE": "NL"}


# ------------------------------------------------------------------ sondes synthetiques
def etat_alea(R, rang, n1, n2, ref=None):
    """Un etat dont chaque champ est tire AUX BORDS des seuils du gel, avec probabilite 0.82 d'etre sain."""
    sain = R.random() < 0.80
    noms = ["sig", "ps", "g3", "sv2", "sv4", "f2", "f4", "q", "etal"]
    mauvais = set() if sain else set(R.sample(noms, R.choice([1, 1, 2])))
    pick = lambda nom, sainv, bords: R.choice(bords) if nom in mauvais else sainv
    sig = pick("sig", R.uniform(0.01, 0.15), [0.19999999, 0.2, 0.25, 0.5])
    ps = pick("ps", R.uniform(0.6, 1.0), [0.49999999, 0.5, 0.3])
    g3 = ref if ref is not None else pick("g3", 10 ** R.uniform(-10, -6), [1.33e-12, 1.3300001e-12, 1.0e-12, 1.4e-12])
    sv2 = pick("sv2", R.uniform(0.95, 0.9999), [0.9, 0.89999, 0.5])
    sv4 = pick("sv4", R.uniform(0.95, 0.9999), [0.9, 0.89999, 0.5])
    f2 = pick("f2", R.uniform(0.7, 1.4), [2.0, 2.0000001, 0.5, 0.49999, 1.0])
    f4 = pick("f4", R.uniform(0.7, 1.4), [2.0, 2.0000001, 0.5, 0.49999, 1.0])
    q = pick("q", 10 ** R.uniform(-0.25, 0.25), [0.5, 0.49999, 2.0, 2.0000001, 0.316227, 0.316228, 0.3162, 0.3163, 3.162277, 3.162278, 3.1622, 3.1624, 4.0, 0.2])
    etal = pick("etal", R.uniform(1.0, 1.3), [2.0, 2.0000001, 1.9999, 3.0])
    ch = {"definie": True, "vide": False, "gammas": None, "Lambda": 1.0, "card": 5, "erreur": None}
    if not sain and R.random() < 0.12:
        ch["vide"] = True
        ch["definie"] = False
    if not sain and R.random() < 0.08:
        ch["erreur"] = "SystemExit: x"
        ch["definie"] = False
    # gammas : [1/4, 1/8, 1/16, 1/32] ; la valeur lue (indice 2) = q x Gamma_2D(3) ; l'etalement max/min = etal
    lu = q * g3
    ch["gammas"] = [lu * etal, lu * (1.0 + 0.5 * (etal - 1.0)), lu, lu]       # la valeur lue (indice 2) differe de l'indice 1
    e = {"rang": rang, "recouvrement": 0.03, "E_re": 0.0, "J_moyen": 0.0, "J_ecart_type": sig, "n1_moyen": n1, "n2_moyen": n2,
         "n1": n1, "n2": n2, "poids_site": ps, "poids_Fock_max": ps,
         "Gamma_2D": {"2": g3 * f2, "3": g3, "4": g3 * f4}, "suivi": {"2": sv2, "4": sv4}, "chaine": ch}
    if not sain and R.random() < 0.10:
        if R.random() < 0.5:
            e["n1"] = -1
        else:
            e["n2"] = -1
    return e


def sonde_alea(R):
    pts = []
    pas_sain = R.random() < 0.25          # une sonde sur quatre porte un defaut de garde
    for pid, (r, w, f) in POINTS.items():
        a, b = f.split("/")
        g_regle = 10 ** R.uniform(-3, -2)
        etats = []
        dup = R.random() < 0.25
        for rang in range(14):
            n1 = 5 + rang // (2 if dup else 1)
            etats.append(etat_alea(R, rang, n1, 2))      # dup : les rangs 2j et 2j+1 portent la meme etiquette
        if R.random() < 0.20:                              # un point a 4..7 etats juges seulement (bord de MIN_JUGES = 6)
            for rang in R.sample(range(14), 14 - R.choice([4, 5, 6, 7])):
                etats[rang]["Gamma_2D"] = {"2": 1e-13, "3": 1e-13, "4": 1e-13}
        if pid in REFS:
            (n1, n2, ref) = REFS[pid]
            for rang in range(1, 14):                      # aucun autre etat ne porte l'etiquette de l'ancre (G-4 : une seule fois)
                etats[rang]["n1"], etats[rang]["n2"] = 20 + rang, 2
            etats[0] = etat_alea(R, 0, n1, n2, ref=ref * (1.0 + R.choice([0.0, 0.0, 0.004, 0.0099999, -0.0099999, 0.0100001, 0.03])))
            etats[0]["poids_site"] = 0.9
        p = {"id": pid, "role": r, "w2": w, "facteur": f, "g_regle": g_regle, "g": g_regle * int(a) / int(b), "faisable": True, "etats": etats}
        if R.random() < 0.04:
            p["faisable"] = False
        pts.append(p)
    s = {"moteur_canon": CANON, "points": pts}
    if pas_sain:
        c = R.choice(["moteur", "manque", "g", "nombre", "role", "ancre_absent", "n_etats"])
        if c == "moteur":
            s["moteur_canon"] = "0000000000000000"
        elif c == "manque":
            s["points"] = [p for p in pts if p["id"] != R.choice(["T1", "T3", "J2", "A1"])]
        elif c == "g":
            pts[R.randrange(12)]["g"] *= 1.001
        elif c == "role":
            pts[R.randrange(12)]["role"] = "juge" if R.random() < 0.5 else "temoin"
        elif c == "ancre_absent":
            pts[10]["etats"][0]["n1"] = 99
        elif c == "n_etats":
            pts[R.randrange(12)]["etats"] = pts[R.randrange(12)]["etats"][:13]
    # des points entiers sains pour que la cascade ne soit pas toujours NON LISIBLE
    return s


def comparer(F, nsondes, graine=20261114):
    R = random.Random(graine)
    n_ecarts, repart, exemples = 0, {}, []
    for i in range(nsondes):
        s = sonde_alea(R)
        mien, rm = lecteur(s)
        try:
            r = F.cascade(s)
            sien = TRAD[r["verdict"]]
            sp = {x["id"]: (TRADP.get(x["statut"]), x["n_juges"]) for x in r["points"]}
        except Exception as ex:
            sien, sp = "EXC:" + type(ex).__name__, {}
        repart[mien] = repart.get(mien, 0) + 1
        ok = (mien == sien)
        if ok and mien != "NCI":
            for pid, (st, nj, ms) in rm.items():
                if sp.get(pid) != (st, nj):
                    ok = False
                    break
        if not ok:
            n_ecarts += 1
            if len(exemples) < 4:
                exemples.append((i, mien, sien))
    return n_ecarts, repart, exemples


def main():
    F = charger(FEUILLE, "feuille_m1")
    print("A. LECTEUR INDEPENDANT (gel 9df2702af59adbbc, sections 5 a 8) CONTRE LA FEUILLE %s" % os.path.basename(FEUILLE))
    ne, rep, ex = comparer(F, NSONDES)
    print("   %d sondes synthetiques aux bords des seuils ; verdicts du lecteur independant : %s" % (NSONDES, dict(sorted(rep.items()))))
    print("   ecarts feuille / lecteur : %d%s" % (ne, "" if ne == 0 else "  exemples " + str(ex)))
    q_edge = math.sqrt(10.0)
    print("   BORD EXACT, hors tirage : q = sqrt(10) = %r ; feuille : %s ; le gel (section 6) ferme la borne : [10^(-1/2), 10^(1/2)]"
          % (q_edge, F.palier(q_edge)))
    qm = 1.0 / q_edge
    print("   BORD EXACT : q = 1/sqrt(10) = %r ; feuille : %s" % (qm, F.palier(qm)))
    # B. mutations
    src = open(FEUILLE, encoding="ascii").read()
    MUT = [
        ("SIGMA_J_MAX = 0.2", "SIGMA_J_MAX = 0.25"), ("POIDS_SITE_MIN = 0.5", "POIDS_SITE_MIN = 0.45"),
        ("DIX_PLANCHERS = 1.33e-12", "DIX_PLANCHERS = 1.0e-12"), ("SUIVI_MIN = 0.9", "SUIVI_MIN = 0.8"),
        ("STABILITE_CIBLE = 2.0", "STABILITE_CIBLE = 2.5"), ("ETALEMENT_CHAINE = 2.0", "ETALEMENT_CHAINE = 3.0"),
        ("MIN_JUGES = 6", "MIN_JUGES = 5"), ("MIN_POINTS_LISIBLES = 4", "MIN_POINTS_LISIBLES = 3"), ("TOL_ANCRE = 1e-2", "TOL_ANCRE = 2e-2"),
        ("if 0.5 <= q <= 2.0:", "if 0.5 < q <= 2.0:"), ("if q * q >= 0.1 and q * q <= 10.0:", "if q * q > 0.1 and q * q <= 10.0:"),
        ('q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"]', 'q = e["chaine"]["gammas"][1] / e["Gamma_2D"]["3"]'),
        ('q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"]', 'q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["2"]'),
        ('vus[(e["n1"], e["n2"])] > 1', 'vus[(e["n1"], e["n2"])] > 2'),
        ("if len(lisibles) < MIN_POINTS_LISIBLES:", "if len(lisibles) <= MIN_POINTS_LISIBLES:"),
        ('if x["statut"] in ("FACTEUR 2", "DECADE")]', 'if x["statut"] in ("FACTEUR 2",)]'),
        ('juges = [x for x in lus if x["role"] == "juge"]', 'juges = [x for x in lus if x["role"] in ("juge", "temoin")]'),
        ('pire = max(juges, key=lambda x: ORDRE_PALIER[x["palier"]])', 'pire = min(juges, key=lambda x: ORDRE_PALIER[x["palier"]])'),
        ('if min(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:', 'if max(e["suivi"]["2"], e["suivi"]["4"]) < SUIVI_MIN:'),
        ('gs = [e["Gamma_2D"][k] for k in ("2", "3", "4")]', 'gs = [e["Gamma_2D"][k] for k in ("3", "4")]'),
        ('if e["n1"] < 0 or e["n2"] < 0:', 'if e["n1"] < 0:'),
        ("motifs += garde_ancres(pts)", "pass"),
        ('if not (g3 > DIX_PLANCHERS):', 'if not (g3 >= DIX_PLANCHERS):'),
        ('if min(cg) <= 0 or max(cg) / min(cg) > ETALEMENT_CHAINE:', 'if min(cg) <= 0 or max(cg[1:]) / min(cg[1:]) > ETALEMENT_CHAINE:'),
    ]
    print("B. MUTATIONS DE LA FEUILLE : %d alterations d'une ligne ; le selftest de machine 1 mord-il ? mon banc A mord-il ?" % len(MUT))
    surv_selftest, surv_banc, surv_deux = [], [], []
    for i, (a, b) in enumerate(MUT, 1):
        if src.count(a) < 1:
            print("   M%02d  MOTIF ABSENT : %s" % (i, a))
            continue
        t = src.replace(a, b, 1)
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "feuille_mutee.py")
            open(p, "w", encoding="ascii", newline="\n").write(t)
            rc = subprocess.run([sys.executable, "-P", p, "--selftest"], capture_output=True, text=True).returncode
            mord_self = (rc != 0)
            Fm = charger(p, "feuille_mutee_%d" % i)
            ne2, _, _ = comparer(Fm, 1200)
            mord_banc = ne2 > 0
        print("   M%02d  selftest m1 : %-8s  banc m2 : %-8s  %s  ->  %s" % (i, "MORD" if mord_self else "survit", "MORD" if mord_banc else "survit",
              a[:58].strip(), b[:50].strip()))
        if not mord_self:
            surv_selftest.append(i)
        if not mord_banc:
            surv_banc.append(i)
        if not mord_self and not mord_banc:
            surv_deux.append(i)
    print("   BILAN : survivent au selftest de machine 1 : %s ; survivent a mon banc : %s ; survivent aux deux : %s" % (surv_selftest, surv_banc, surv_deux))


if __name__ == "__main__":
    main()
