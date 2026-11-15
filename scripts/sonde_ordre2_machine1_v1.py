# -*- coding: ascii -*-
"""SONDE DU GEL "LA CHAINE E-A AU SECOND ORDRE" -- machine 1, v1, 2026-11-14.
ELLE MESURE ET NE JUGE PAS : aucun rapport chaine / 2D n'est affiche, aucun seuil du gel n'est applique.
Derivee par hunks de sonde_domaine_G1_machine1_v1.py (940a21b1d562bb49) : memes mesures 2D, meme chaine du moteur,
meme garde du moteur consignee et jamais appliquee ; autres points ;
EN PLUS, pour chaque etat, la CHAINE D'ORDRE 2 (bloc insere ci-dessous : deplacements Sigma2, saut au second voisin,
sites m < 0), a quatre eta de chaine, et l'energie libre du site de l'etiquette. Le moteur n'est pas modifie.
Usage : python -P sonde_ordre2_machine1_v1.py <moteur_v17.py> <sortie.json> [id ...]
Sans id : les seize points du gel. Avec id : ces points seulement (essai a blanc ; machine 1 ne joue que A1 A2).
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
    ("C1", "juge", F(197, 100), F(2, 3)), ("C2", "juge", F(97, 50), F(3, 4)),
    ("C3", "juge", F(203, 100), F(3, 2)), ("C4", "juge", F(103, 50), F(4, 3)),
    ("M1", "juge", F(193, 100), F(1)), ("M2", "juge", F(48, 25), F(4, 3)),
    ("M3", "juge", F(207, 100), F(2, 3)), ("M4", "juge", F(21, 10), F(3, 4)),
    ("L1", "juge", F(189, 100), F(4, 3)), ("L2", "juge", F(47, 25), F(1)),
    ("L3", "juge", F(211, 100), F(3, 2)), ("L4", "juge", F(53, 25), F(2, 3)),
    ("A1", "ancre", F(39, 20), F(1)), ("A2", "ancre", F(41, 20), F(1)),
    ("W1", "temoin", F(107, 50), F(1)), ("W2", "temoin", F(209, 100), F(1, 2)),   # les temoins en dernier
]
FRACTION, L_BOITE, N_ETATS = 0.70, 20, 14
KS = (2, 3, 4)
EF_CHAINE = (0.25, 0.125, 0.0625, 0.03125)

# --- CHAINE E-A AU SECOND ORDRE (bloc de machine 1, v1, 2026-11-14 ; insere tel quel dans la sonde) ---
# Hamiltonien effectif sur l'echelle resonante de l'etat (n1, n2), sites m : (n1 + CANAL[0] m, n2 + CANAL[1] m),
# a l'ordre g^2, forme symetrique, energies libres du moteur :
#   H_ab = E_a delta_ab + V_ab + (1/2) somme_q V_aq V_qb [ 1/(E_a - E_q) + 1/(E_b - E_q) ],  q hors echelle.
# La parite de x^P (P impair) ne laisse que le deplacement diagonal Sigma2(m) et le saut au second voisin u_m.
# Les sites m < 0 (jusqu'a epuisement de n1 ou de n2) sont gardes. Absorbeur, longueur et lecture de l'etat :
# ceux de gamma_chaine du moteur. Depend de M (le moteur), np et math, deja charges par la sonde.
SAUTS_HORS_ECHELLE = [(k, l) for k in range(-M.P, M.P + 1) for l in range(-M.P, M.P + 1)
                      if 0 < abs(k) + abs(l) <= M.P and (k + l) % 2 == M.P % 2
                      and (k, l) != (M.CANAL[0], M.CANAL[1]) and (k, l) != (-M.CANAL[0], -M.CANAL[1])]

def tables_ordre2(n1, n2, w2, g, sites, M_facteur=4):
    """Sauts t_m, deplacements Sigma2(m) et sauts au second voisin u_m, sites m_min..Mh."""
    w = float(w2); w1 = float(M.W1); c0, c1 = M.CANAL
    d = c1 * w - c0 * w1
    m2_bord = sites[-1][0]
    b_M = max(8, m2_bord)
    Mh = (m2_bord + b_M) * M_facteur
    m_min = -min(int(n1) // c0, int(n2) // c1)

    def V(k, l, a, b):
        if a < 0 or b < 0 or a + k < 0 or b + l < 0:
            return 0.0
        return (g / M.P) * M.X_saut_reel(M.P, k, l, float(a), float(b), w2)

    t, S, U = {}, {}, {}
    for m in range(m_min, Mh + 1):
        a, b = n1 + c0 * m, n2 + c1 * m
        t[m] = V(c0, c1, a, b); S[m] = 0.0; U[m] = 0.0
        for (k, l) in SAUTS_HORS_ECHELLE:
            v = V(k, l, a, b)
            if v == 0.0:
                continue
            ej = -w1 * k + w * l                    # energie libre de l'intermediaire, comptee du site m
            S[m] += v * v / (-ej)
            k2, l2 = 2 * c0 - k, 2 * c1 - l
            if abs(k2) + abs(l2) <= M.P and (k2, l2) != (c0, c1):
                U[m] += 0.5 * v * V(k2, l2, a + k, b + l) * (1.0 / (-ej) + 1.0 / (2.0 * d - ej))
    return {"d": d, "m2_bord": m2_bord, "b_M": b_M, "Mh": Mh, "m_min": m_min, "t": t, "S": S, "U": U}

def gamma_chaine_ordre2(tb, eta_facteur=1.0):
    """Largeur de l'etat de plus grand recouvrement avec le site 0, chaine d'ordre 2 complete.
    Rend Gamma_c2 = -2 Im E (la valeur lue), Gamma_flux = 2 <W> (meme quantite, autre arithmetique),
    dE = Re E + Sigma2(0) (decalage d'energie de l'etat, compte de l'energie libre du site 0)."""
    d, Mh, m_min = tb["d"], tb["Mh"], tb["m_min"]
    eta_c = abs(d) * eta_facteur
    debut_cap = tb["m2_bord"] + tb["b_M"] // 2
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + (tb["S"][m] - tb["S"][0])
        if m > debut_cap:
            Wd[i] = eta_c * (m - debut_cap) ** 2
            H[i, i] += -1j * Wd[i]
        if m < Mh:
            H[i, i + 1] = tb["t"][m]; H[i + 1, i] = tb["t"][m]
        if m + 2 <= Mh:
            H[i, i + 2] = tb["U"][m]; H[i + 2, i] = tb["U"][m]
    valeurs, vecteurs = np.linalg.eig(H)
    recs = np.abs(vecteurs[-m_min, :]) ** 2
    nu = np.lexsort((valeurs.real, -recs))[0]
    psi2 = np.abs(vecteurs[:, nu]) ** 2
    return {"Gamma_c2": float(-2.0 * valeurs[nu].imag), "Gamma_flux": float(2.0 * (Wd @ psi2) / psi2.sum()),
            "dE": float(valeurs[nu].real + tb["S"][0]), "recouvrement": float(recs[nu]), "M": Mh, "m_min": m_min}
# --- fin du bloc ---

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
    Oc = M.Omega_du_canal(w2)[0]            # garde G-1 du moteur : consignee, jamais appliquee
    gm = {"Omega_c": float(Oc), "D1": None, "c_max": None, "site_c_max": None, "statut": None, "erreur": None}
    try:
        gd = M.garde_domaine(w2, g, M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"], Oc)
        gm.update({"D1": float(gd["D1"]), "c_max": float(gd["c_max"]), "site_c_max": gd["site_c_max"],
                   "statut": gd["statut"]})
    except BaseException as x:
        gm["erreur"] = "%s: %s" % (type(x).__name__, str(x)[:200])
    pt["garde_moteur"] = gm
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
        e["E_libre"] = float(M.energie_libre(float(n1), float(kk), w2)) if dans else None
        c2 = {"definie": False, "m_bord": None, "m_min": None, "gammas_flux": None, "gammas_im": None, "dE": None,
              "Sigma2_0": None, "erreur": None}
        if dans and ch["definie"]:
            try:
                tb = tables_ordre2(float(n1), float(kk), w2, g, sites, M_facteur=4)
                rs = [gamma_chaine_ordre2(tb, ef) for ef in EF_CHAINE]
                c2.update({"definie": True, "m_bord": int(tb["m2_bord"]), "m_min": int(tb["m_min"]),
                           "gammas_flux": [r["Gamma_flux"] for r in rs], "gammas_im": [r["Gamma_c2"] for r in rs],
                           "dE": [r["dE"] for r in rs], "Sigma2_0": float(tb["S"][0])})
            except BaseException as x:          # se consigne, ne se rattrape pas
                c2["erreur"] = "%s: %s" % (type(x).__name__, str(x)[:200])
        e["chaine2"] = c2
        pt["etats"].append(e)
    pt["duree_s"] = round(time.time() - t0, 1)
    return pt

def main():
    ids = [p[0] for p in POINTS]
    for d in DEMANDES:
        if d not in ids:
            raise SystemExit("id inconnu : %s" % d)
    a_jouer = [p for p in POINTS if (not DEMANDES or p[0] in DEMANDES)]
    sortie = {"sonde": "sonde_ordre2_machine1_v1", "moteur_canon": canon_B(MOTEUR),
              "sonde_canon": canon_B(os.path.abspath(__file__)),
              "reglage": {"fraction": FRACTION, "L_boite": L_BOITE, "n_etats": N_ETATS, "ks": list(KS),
                          "ef_chaine": list(EF_CHAINE), "potentiel": "x5", "signe_fantome": -1, "P": int(M.P),
                          "ordre2": {"M_facteur": 4, "forme": "symetrique", "sites_bas": True,
                                     "sauts_hors_echelle": len(SAUTS_HORS_ECHELLE)}},
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
        print("%s %-6s w2=%s x%s g=%.6e graine=(%.3f, %.3f) r_c=%d N=%d garde du moteur %s : %s, %d etats, %s s" % (
            pid, role, pt["w2"], pt["facteur"], pt["g"], pt["graine"][0], pt["graine"][1], pt["r_c"], pt["N"],
            pt["garde_moteur"]["statut"] or "EN ERREUR",
            "joue" if pt["faisable"] else "INFAISABLE (N > N_max)", len(pt["etats"]), pt.get("duree_s")), flush=True)
        json.dump(sortie, open(SORTIE, "w", encoding="ascii"), indent=1, sort_keys=True)
    print("FIN : %d points, sortie %s" % (len(sortie["points"]), SORTIE), flush=True)

if __name__ == "__main__":
    main()
