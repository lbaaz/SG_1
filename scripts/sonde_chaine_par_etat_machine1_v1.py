# -*- coding: ascii -*-
"""SONDE DU GEL "LA CHAINE E-A PAR ETAT, HORS PLAGE" -- machine 1, v1, 2026-11-14.
ELLE MESURE ET NE JUGE PAS : aucun rapport chaine / 2D n'est affiche, aucun seuil du gel n'est applique.
Usage : python -P sonde_chaine_par_etat_machine1_v1.py <moteur_v17.py> <sortie.json> [id ...]
Sans id : les douze points du gel. Avec id : ces points seulement (essai a blanc ; machine 1 ne joue que A1 A2).
Par point : boite du moteur (regle de executer_EB, L = 20), H_2D du moteur a eta_k = eta0 2^(-k), k = 2, 3, 4 ;
a k = 3 les 14 etats de plus grand recouvrement avec la graine coherente (fraction 0.70), etiquetes par
J = n1 - 2 n2 et <n2> ; chacun est suivi a k = 2 et k = 4 par recouvrement ; la chaine du moteur
(barriere, gamma_chaine) est evaluee au site entier (n1, n2) de l'etiquette, a quatre eta de chaine.
Une seule decomposition est tenue en memoire a la fois."""
import sys, os, math, json, time, hashlib, unicodedata, importlib.util, platform
from fractions import Fraction as F
import numpy as np

MOTEUR, SORTIE = sys.argv[1], sys.argv[2]
DEMANDES = sys.argv[3:]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR)
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

POINTS = [  # (id, role, w2, facteur sur g_du_point)
    ("J1", "juge", F(19, 10), F(1)), ("J2", "juge", F(21, 10), F(1)),
    ("J3", "juge", F(39, 20), F(3, 2)), ("J4", "juge", F(41, 20), F(3, 2)),
    ("J5", "juge", F(39, 20), F(2, 3)), ("J6", "juge", F(41, 20), F(2, 3)),
    ("T1", "temoin", F(49, 25), F(1)), ("T2", "temoin", F(51, 25), F(1)),
    ("T3", "temoin", F(37, 20), F(1)), ("T4", "temoin", F(43, 20), F(1)),
    ("A1", "ancre", F(39, 20), F(1)), ("A2", "ancre", F(41, 20), F(1)),
]
FRACTION, L_BOITE, N_ETATS = 0.70, 20, 14
KS = (2, 3, 4)
EF_CHAINE = (0.25, 0.125, 0.0625, 0.03125)

def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

def mesurer(pid, role, w2, fac):
    t0 = time.time()
    g_regle = float(M.g_du_point(w2)); g = g_regle * float(fac)
    s = FRACTION * M.s_ff(w2, g)
    n1_0, n2_0 = M.appariement(s, w2)
    sites0 = M.barriere(n1_0, n2_0, w2, g, True)
    m2b = sites0[-1][0] if sites0 else 0
    b_M = max(8, m2b)
    r_c = int(math.ceil(n1_0)) + 2 * (m2b + b_M) + 2
    N = r_c + L_BOITE
    eta0 = abs(float(w2) - 2.0 * float(M.W1))
    pt = {"id": pid, "role": role, "w2": "%d/%d" % (w2.numerator, w2.denominator),
          "facteur": "%d/%d" % (fac.numerator, fac.denominator), "g_regle": g_regle, "g": g, "s": s,
          "graine": [n1_0, n2_0], "card_barriere_graine": len(sites0), "r_c": r_c, "N": N, "eta0": eta0,
          "faisable": bool(N <= M.N_MAX_EB), "etats": []}
    if not pt["faisable"]:
        return pt
    psi = M.graine_coherente(N, s, w2)

    def decomposer(k):
        H, idx = M.H_2D(N, w2, g, -1, "x5", eta0 * 2.0 ** (-k), r_c)
        val, vec = np.linalg.eig(H)
        del H
        return val, vec, idx

    val3, vec3, idx = decomposer(3)
    Jv = np.zeros(N * N); Av = np.zeros(N * N); Bv = np.zeros(N * N)
    for (a, b), i in idx.items():
        Jv[i] = a - 2 * b; Av[i] = a; Bv[i] = b
    recs = np.abs(vec3.conj().T @ psi) ** 2
    ordre = np.lexsort((val3.real, -recs))[:N_ETATS]
    V3 = vec3[:, ordre].copy(); E3 = val3[ordre].copy(); R3 = recs[ordre].copy()
    del vec3, val3
    n3 = np.sum(np.abs(V3) ** 2, axis=0)
    suivis = {}
    for k in (2, 4):
        valk, veck, _ = decomposer(k)
        ov = np.abs(veck.conj().T @ V3) ** 2 / (np.sum(np.abs(veck) ** 2, axis=0)[:, None] * n3[None, :])
        j = np.argmax(ov, axis=0)
        suivis[k] = ([float(-2.0 * valk[jj].imag) for jj in j], [float(ov[jj, c]) for c, jj in enumerate(j)])
        del veck, valk, ov
    for rang in range(N_ETATS):
        v = V3[:, rang]; w = np.abs(v) ** 2; w = w / w.sum()
        Jm = float(w @ Jv); Js = math.sqrt(max(float(w @ Jv ** 2) - Jm * Jm, 0.0))
        a_m = float(w @ Av); b_m = float(w @ Bv)
        kk = int(round(b_m)); J = int(round(Jm)); n1 = J + 2 * kk
        dans = (0 <= n1 < N and 0 <= kk < N)
        e = {"rang": rang, "recouvrement": float(R3[rang]), "E_re": float(E3[rang].real),
             "J_moyen": Jm, "J_ecart_type": Js, "n1_moyen": a_m, "n2_moyen": b_m,
             "n1": n1, "n2": kk, "poids_site": float(w[idx[(n1, kk)]]) if dans else 0.0,
             "poids_Fock_max": float(w.max()),
             "Gamma_2D": {"2": suivis[2][0][rang], "3": float(-2.0 * E3[rang].imag), "4": suivis[4][0][rang]},
             "suivi": {"2": suivis[2][1][rang], "4": suivis[4][1][rang]}}
        ch = {"definie": False, "vide": None, "gammas": None, "Lambda": None, "card": None, "erreur": None}
        if dans:
            try:
                sites = M.barriere(float(n1), float(kk), w2, g, True)
                ch["vide"] = (len(sites) == 0); ch["card"] = len(sites)
                if sites:
                    ch["gammas"] = [float(M.gamma_chaine(float(n1), float(kk), w2, g, sites, eta_facteur=ef,
                                                         M_facteur=4)["Gamma_c"]) for ef in EF_CHAINE]
                    ch["Lambda"] = float(M.Lambda_action(sites)); ch["definie"] = True
            except BaseException as x:          # un arret du moteur (garde de domaine) se consigne, ne se rattrape pas
                ch["erreur"] = "%s: %s" % (type(x).__name__, str(x)[:200])
        e["chaine"] = ch
        pt["etats"].append(e)
    pt["duree_s"] = round(time.time() - t0, 1)
    return pt

def main():
    ids = [p[0] for p in POINTS]
    for d in DEMANDES:
        if d not in ids:
            raise SystemExit("id inconnu : %s" % d)
    a_jouer = [p for p in POINTS if (not DEMANDES or p[0] in DEMANDES)]
    sortie = {"sonde": "sonde_chaine_par_etat_machine1_v1", "moteur_canon": canon_B(MOTEUR),
              "sonde_canon": canon_B(os.path.abspath(__file__)),
              "reglage": {"fraction": FRACTION, "L_boite": L_BOITE, "n_etats": N_ETATS, "ks": list(KS),
                          "ef_chaine": list(EF_CHAINE), "potentiel": "x5", "signe_fantome": -1, "P": int(M.P)},
              "plateforme": {"systeme": platform.system(), "machine": platform.machine(),
                             "python": platform.python_version(), "numpy": np.__version__,
                             "coeurs": os.cpu_count(),
                             "fils": {v: os.environ.get(v) for v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                             "levier": os.environ.get("NPY_DISABLE_CPU_FEATURES"),
                             "temoin_arrondi": float((np.array([1765.6704444885254]) ** 6)[0]).hex()},
              "points_demandes": [p[0] for p in a_jouer], "points": []}
    for (pid, role, w2, fac) in a_jouer:
        pt = mesurer(pid, role, w2, fac)
        sortie["points"].append(pt)
        print("%s %-6s w2=%s x%s g=%.6e graine=(%.3f, %.3f) r_c=%d N=%d : %s, %d etats, %s s" % (
            pid, role, pt["w2"], pt["facteur"], pt["g"], pt["graine"][0], pt["graine"][1], pt["r_c"], pt["N"],
            "joue" if pt["faisable"] else "INFAISABLE (N > N_max)", len(pt["etats"]), pt.get("duree_s")), flush=True)
        json.dump(sortie, open(SORTIE, "w", encoding="ascii"), indent=1, sort_keys=True)
    print("FIN : %d points, sortie %s" % (len(sortie["points"]), SORTIE), flush=True)

if __name__ == "__main__":
    main()
