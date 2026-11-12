# -*- coding: ascii -*-
# BANC QUI TUE DE LA QUALIFICATION E-B -- machine 1, v1 -- gel E-B v2
# cde0cd11a763f26d, section 10. Six mutations ; chacune doit faire tomber ce
# qu'elle vise ; le banc affirme sa branche et compte : mordues == attendues.
# M-1, M-2, M-3 : mutations de DONNEES sur une sortie de sonde synthetique,
#   jugee par la feuille de lecture reelle.
# M-6 : le suivi de la sonde reelle, sur le moteur reel a geometrie reduite,
#   puis sa consequence a la lecture.
# M-4, M-5 : la sonde reelle, en pre-vol, avec --mutation.
import sys, os, json, copy, shutil, subprocess, argparse, importlib.util
import numpy as np

POINTS = ["39_20", "197_100", "99_50", "101_50", "203_100", "41_20"]
CFGS = ["F1G20", "F2G20", "F3G20", "F1G30", "F1GT"]
ETA0 = 0.05


def charger(chemin, nom):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def ile(G):
    def f(k):
        if 0 <= k <= 8:
            return G
        return G * (1.0 + 0.3 * (-k)) if k < 0 else G * 2.0 ** (8 - k)
    return f


def lineaire(c):
    return lambda k: c * ETA0 * 2.0 ** (-k)


def traj(fonctions):
    return {str(k): {"k": k, "eta": ETA0 * 2.0 ** (-k), "saute": False,
                     "etats": [{"suivi": True, "ov": 0.99, "E_re": 1.0,
                                "E_im": -0.5 * f(k), "gamma": f(k)}
                               for f in fonctions]} for k in range(-2, 13)}


def synthetique():
    s1 = {"etage": 1, "prevol": False, "GQ10": True,
          "GQ3": {n: True for n in POINTS},
          "GQ5": {n: {c: 1e-14 for c in CFGS} for n in POINTS},
          "TP": {"j08": {"j": 8, "g": 0.1, "traj": {
              "F1G20": traj([ile(6.4e-9)]), "F1G30": traj([ile(6.4e-9)])}}},
          "TN": {"candidats": [[50, 25], [55, 27], [45, 22]],
                 "traj": traj([lineaire(100.0)] * 3)}}
    ref = {"retenus": [{"j": 8, "g": 0.1}], "balayage": [
        {"j": 8, "g": 0.1, "Gamma_ref": 6.4e-9, "u_ref": 0.001}]}
    s2 = {"etage": 2, "GQ10": True, "GQ4": {}, "points": {}}
    for i, n in enumerate(POINTS):
        G = 1e-10 * (i + 1)
        s2["GQ4"][n] = {"gamma": G, "reference": G, "rapport": 1.0,
                        "au_bit": True}
        cfg = {c: {"identite": 0.99, "traj": traj([ile(G)])} for c in CFGS}
        cfg["F1G20"]["traj"] = traj([ile(G * 10.0 ** (0.5 * t))
                                     for t in range(10)])
        cfg["F1G20"]["traj"]["3"].update({
            "somme_c_re": 1.0, "somme_c_im": 0.0, "poids_total": 0.9,
            "c_re": [0.03] * 10, "c_im": [0.0] * 10,
            "kappa": [2.0 if i < 3 else 1.0] * 10})
        s2["points"][n] = {"G_run": G, "cfg": cfg}
    return s1, ref, s2


def muter_gamma(tr, f):
    for ks, rec in tr.items():
        for e in rec["etats"]:
            if e.get("suivi"):
                e["gamma"] = f(int(ks), e["gamma"])


def main():
    ap = argparse.ArgumentParser()
    for x in ("lecture", "sonde", "moteur", "run", "manifeste", "prevol",
              "retenus", "sortie"):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()
    os.makedirs(a.sortie, exist_ok=True)
    L = charger(a.lecture, "lecture_qeb")
    L.dire.f = open(os.devnull, "w")
    sortie_std = sys.stdout
    R = []

    def muet(f, *args):
        sys.stdout = open(os.devnull, "w")
        try:
            return f(*args)
        finally:
            sys.stdout = sortie_std

    def affirmer(nom, vise, obtenu, attendu):
        ok = obtenu == attendu
        R.append(ok)
        print("%-4s %-52s %s" % (nom, vise, "MORD" if ok else
                                 "NE MORD PAS : obtenu %r, attendu %r"
                                 % (obtenu, attendu)), flush=True)

    def juger(s1, ref, s2):
        v, motifs, _ = muet(L.juger_etage1, s1, ref)
        v1 = {"etage1": v}
        if v != "TIENT":
            return L.cascade(v1, s2, {}), {}, v
        verdict, det = muet(L.juger_etage2, v1, s2)
        return verdict, det["points"], v

    # --- temoins du banc : la base saine ------------------------------------
    s1, ref, s2 = synthetique()
    v, pts, e1 = juger(s1, ref, s2)
    base = (e1 == "TIENT" and v == "ESTIMATEUR QUALIFIE")
    print("BASE synthetique : etage 1 %s, verdict %s : %s" % (
        e1, v, "saine" if base else "MALSAINE"))
    # --- M-1 ------------------------------------------------------------------
    s1, ref, s2 = synthetique()
    for n in POINTS:
        for c in CFGS:
            muter_gamma(s2["points"][n]["cfg"][c]["traj"],
                        lambda k, g: 3e-7 * ETA0 * 2.0 ** (-k))
    v, pts, _ = juger(s1, ref, s2)
    affirmer("M-1", "gamma = c eta -> six NON QUALIFIES, NON QUALIFIE",
             (v, sorted(set(p["statut"] for p in pts.values()))),
             ("NON QUALIFIE", ["NON QUALIFIE"]))
    # --- M-2 ------------------------------------------------------------------
    s1, ref, s2 = synthetique()
    muter_gamma(s2["points"]["39_20"]["cfg"]["F1G30"]["traj"],
                lambda k, g: 1.06 * g)
    v, pts, _ = juger(s1, ref, s2)
    affirmer("M-2", "Gamma_pl(G30) x 1.06 -> (b) echoue a ce point",
             (v, pts["39_20"]["statut"], any(
                 e.startswith("(b)") for e in pts["39_20"]["echecs"]),
              sum(p["statut"] == "QUALIFIE" for p in pts.values())),
             ("QUALIFIE PAR POINT", "NON QUALIFIE", True, 5))
    # --- M-3 ------------------------------------------------------------------
    s1, ref, s2 = synthetique()
    ref["balayage"][0]["Gamma_ref"] *= 1.07
    v, pts, e1 = juger(s1, ref, s2)
    affirmer("M-3", "reference du TP x 1.07 -> NON CONCLUANT D'INSTRUMENT",
             (e1, v), ("NE TIENT PAS", "NON CONCLUANT D'INSTRUMENT"))
    # --- M-6 : suivi de la sonde reelle, vecteur remplace --------------------
    S = charger(a.sonde, "sonde_qeb")
    S.dire.f = open(os.devnull, "w")
    M = muet(S.charger_moteur, a.moteur)
    P = S.parametres(a.run, True)["39_20"]
    forme, r_c, N, Lg = S.geometrie("F1G20", P["r0"], True)
    rep = os.path.join(a.sortie, "M6")
    shutil.rmtree(rep, ignore_errors=True)
    sysm = S.Systeme(M, N, P["w2"], P["g"], -1)
    psi = S.cible(M, ("graine",), N, P["s"], P["w2"])
    w = S.absorbeur(forme, r_c, N, Lg)
    S.trajectoire(sysm, w, P["eta0"], rep, "M6", S.choisir_graine(psi, 1),
                  ks=[3])
    faux = np.cos(np.arange(N * N) * 0.7310585786300049) + 0j
    faux /= np.sqrt(np.sum(np.abs(faux) * np.abs(faux)))
    np.save(os.path.join(rep, "k_+03.npy"), np.array([faux]))
    recs, _ = S.trajectoire(sysm, w, P["eta0"], rep, "M6",
                            S.choisir_graine(psi, 1), ks=[3, 4, 5])
    e4, e5 = recs[4]["etats"][0], recs[5]["etats"][0]
    s1, ref, s2 = synthetique()
    for ks, rec in s2["points"]["197_100"]["cfg"]["F2G20"]["traj"].items():
        if ks != "3":
            rec["etats"][0] = {"suivi": False, "ov": None}
    v, pts, _ = juger(s1, ref, s2)
    affirmer("M-6", "vecteur remplace -> SUIVI PERDU, configuration NON LISIBLE",
             (e4["suivi"], e4["ov"] is not None and e4["ov"] < 0.90,
              e5["suivi"], recs[5].get("saute"), v, pts["197_100"]["statut"],
              pts["197_100"]["non_lisibles"]),
             (False, True, False, True, "QUALIFIE PAR POINT", "NON LISIBLE",
              ["F2G20"]))
    # --- M-4, M-5 : la sonde reelle en pre-vol, avec mutation ----------------
    commun = [sys.executable, "-I", a.sonde, "--moteur", a.moteur, "--run",
              a.run, "--manifeste", a.manifeste, "--prevol"]

    def lancer(nom, extra):
        d = os.path.join(a.sortie, nom)
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d)
        for f in ("sonde_etage1.json", "verdict_etage1.json"):
            if os.path.exists(os.path.join(a.prevol, f)):
                shutil.copy(os.path.join(a.prevol, f), d)
        r = subprocess.run(commun + ["--sortie", d] + extra,
                           capture_output=True, text=True)
        return r.returncode, [l for l in r.stdout.splitlines()
                              if l.startswith("ARRET")]
    code, arr = lancer("M4", ["--etage", "2", "--mutation", "M-4",
                              "--verdict1", os.path.join(
                                  a.prevol, "verdict_etage1.json"),
                              "--ancrage-ref", os.path.join(
                                  a.prevol, "ancrage_prevol.json")])
    affirmer("M-4", "ancrage sur le deuxieme recouvrement -> G-Q4 mord",
             (code, bool(arr) and arr[0].startswith("ARRET G-Q4")), (3, True))
    code, arr = lancer("M5", ["--etage", "1", "--mutation", "M-5",
                              "--retenus", a.retenus])
    affirmer("M-5", "un element de W_F1 deplace -> G-Q3 mord",
             (code, bool(arr) and arr[0].startswith("ARRET G-Q3")), (3, True))
    # --- temoin de porte : un etage 1 qui ne tient pas ferme l'etage 2 ------
    reel = os.path.join(a.prevol, "verdict_etage1_reel.json")
    porte = None
    if os.path.exists(reel):
        code, arr = lancer("PORTE", ["--etage", "2", "--verdict1", reel])
        porte = (code == 2 and bool(arr) and "etage 2 refuse" in arr[0])
        print("PORTE verdict d'etage 1 %s -> etage 2 refuse (code %d) : %s" % (
            json.load(open(reel))["etage1"], code, "TIENT" if porte
            else "NE TIENT PAS"))
        base = base and porte
    else:
        print("PORTE : NON JOUEE (pas de verdict reel en pre-vol)")
    print("banc qui tue : %d mordues == 6 attendues ; base %s : %s" % (
        sum(R), "saine" if base else "MALSAINE",
        "PASSE" if (sum(R) == 6 and len(R) == 6 and base) else "ECHOUE"))
    sys.exit(0 if (sum(R) == 6 and len(R) == 6 and base) else 1)


if __name__ == "__main__":
    main()
