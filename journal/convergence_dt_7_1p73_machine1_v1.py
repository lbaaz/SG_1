#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
GESTE (2) -- CONVERGENCE EN dt DE e(dt2/2) A LA CELLULE 7|1.73 (classe 3, machine 1)
=====================================================================================
Bloc d'ouverture (SUIVI_campagne_2026-09-12, section 4) :
  ETAPE    convergence en dt en 7|1.73 : e(dt2/2) a dt, dt/2, dt/4 sur machine 1
           (le point ou les deux machines divergent, 0.759 contre 0.684)
  FICHIERS instrument v8 4d8882a2223a5c74 (le banc qui produit e(dt2/2)),
           temoin v11 a2e7ef3e237c5acf (gel du volet T : definition de e, cellule, dt),
           moteur c8ed357b120352c4 (chemin en argument, jamais une constante)
  LIVRABLE script, log, JSON de convergence, note de lecture, manifeste
  CLASSE   3 -- aucun verdict, aucune porte neuve ; la mesure precede toute
           lecture de la tenaille.

CE QUE CE SCRIPT FAIT, ET RIEN D'AUTRE
  1. authentifie par canon les trois pieces qu'il touche (instrument : convention B ;
     temoin : convention B ; moteur : sha256 brut complet, celui que l'instrument
     porte dans MOTEUR) -- ARRET si une empreinte ne repond pas ;
  2. importe l'instrument v8 EN LECTURE (PB-1 : rien n'est edite) et reutilise SES
     fonctions : alpha_de, A_de, tau_dom, tau_cap, dt2_de, forcage_de, xm_et_derivees,
     vers_composantes, phase2_pu, tol_ordre, lecture_5_4, K_BASC, R_CAP, M_PAS --
     le meme code que jouer_T2 (instrument l.1634-1719), au meme reglage prime ;
  3. charge le moteur par charger_moteur de l'instrument (custody transitive :
     empreinte, globales heritees, certifier_gel) -- T-2 n'appelle pas le moteur,
     mais le geste le nomme et l'instrument l'exige a la charge ;
  4. joue QUATRE flots de la solution manufacturee (temoin 5.3) a la cellule
     (p, w2) = (7, 1.73) : pas dt2, dt2/2, dt2/4, dt2/8, soit les trois PAIRES
     (dt, dt/2) du bloc : base dt2 (la paire du gel), base dt2/2, base dt2/4 ;
  5. consigne, par flot : e = max |x - x_m| / |x_m|, n_pas, evenement, tau de fin,
     R_composantes du flot, plancher_composantes = eps x R, e / plancher,
     tau et R au point du max ; par paire : p_obs = log2(e(dt)/e(dt/2)) et la
     lecture 5.4 (C_effectif, seuil, ratio_seuil, W-plancher, W-pas) SUR LE FLOT
     FIN de la paire, exactement comme l'instrument la fait sur la paire du gel ;
  6. ecrit le JSON et le log en ASCII pur ; les attentes sont imprimees AVANT
     la premiere integration, et le compte attendu des flots est declare avant.

LES ATTENTES, ECRITES AVANT (classe 3, non gelees, avec leur falsifieur)
  E-A  Signature du plancher : aux DEUX paires raffinees (base dt2/2 et base dt2/4),
       p_obs sort de [4 - tol_ordre(7), 4 + tol_ordre(7)] -- l'ordre RK4 n'est pas
       retrouve en raffinant. FALSIFIEE si l'une des deux paires raffinees rend un
       p_obs dans cette bande.
  E-B  Le rapport e(dt2/2) / plancher_composantes, a la paire du gel, tombe dans
       la fourchette des deux machines etendue de la part de plancher que le gel
       reconstruit (b = 1.15 a 1.74 plancher) : [6.09 - 1.74, 6.75 + 1.74] =
       [4.35, 8.49], ou 6.09 = 0.684 x C_eff(7) et 6.75 = 0.759 x C_eff(7),
       C_eff(7) = 8.8966. FALSIFIEE si la valeur d'aujourd'hui sort de [4.35, 8.49].
  E-C  Monotonie : e(dt2/8) >= e(dt2/4) x 2^(-(4 - tol_ordre(7))) n'est PAS une
       attente (le max d'un bruit peut descendre par chance) ; on consigne seulement
       le signe de p_obs a la derniere paire, sans attente.
  Lecture annoncee : si E-A tient, la valeur de e(dt2/2) a 7|1.73 est une grandeur
  de plancher (arrondi accumule dans la compensation x1 + x2), donc dependante de
  la plateforme (libm, contraction FMA) : l'ecart 0.759 / 0.684 est alors DERIVE
  du plancher que 5.4 ecarte deja, et les machines ne divergent sur rien de LU.
  Si E-A est falsifiee, l'ecart est INDECIDABLE par cette mesure.

USAGE
  python3 convergence_dt_7_1p73_machine1_v1.py --moteur <clone>/scripts/m9_replication_v1.py
      --instrument <lot>/banc_qualification_machine1_v8.py
      --temoin <lot>/temoin_negatif_pre_enregistrement_v11.md --sortie <dossier>
"""
import argparse, hashlib, importlib.util, json, math, os, platform, sys, time, unicodedata

CANON_INSTRUMENT = "4d8882a2223a5c74"     # banc_qualification_machine1_v8.py, convention B
CANON_TEMOIN = "a2e7ef3e237c5acf"         # temoin_negatif_pre_enregistrement_v11.md, convention B
P_CELLULE, W2_CELLULE = 7, 1.73
NIVEAUX = 4                               # dt2, dt2/2, dt2/4, dt2/8 -> trois paires (dt, dt/2)
RATIO_M1_28_08, RATIO_M2 = 0.759, 0.684   # e(dt2/2)/seuil a 7|1.73, les deux machines (SUIVI 28d, 09/09)
B_SUR_PLANCHER = (1.15, 1.74)             # part de plancher reconstruite par le gel (temoin 5.4, D-t-25)


def empreinte_B(chemin):
    b = open(chemin, "rb").read()
    t = b.decode("utf-8")
    crlf = "\r\n" in t
    t = unicodedata.normalize("NFC", t.replace("\r\n", "\n"))
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16], crlf, len(b)


def sha_brut(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


class Log(object):
    def __init__(self):
        self.lignes = []

    def __call__(self, cle, msg):
        ligne = "[%s] %-10s %s" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), cle, msg)
        self.lignes.append(ligne)
        print(ligne)


LOG = Log()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--moteur", required=True, help="chemin du moteur m9_replication_v1.py (argument, jamais une constante)")
    ap.add_argument("--instrument", required=True, help="banc_qualification_machine1_v8.py (certifie, lu seulement)")
    ap.add_argument("--temoin", required=True, help="temoin_negatif_pre_enregistrement_v11.md (gel du volet T)")
    ap.add_argument("--sortie", required=True)
    a = ap.parse_args()
    t_debut = time.perf_counter()
    os.makedirs(a.sortie, exist_ok=True)

    # ---- 1. authentification par canon, avant toute lecture ---------------------
    hi, crlf_i, oct_i = empreinte_B(a.instrument)
    if hi != CANON_INSTRUMENT:
        sys.exit("ARRET PB-1 : l'instrument ne repond pas au canon %s (lu %s)" % (CANON_INSTRUMENT, hi))
    ht, crlf_t, oct_t = empreinte_B(a.temoin)
    if ht != CANON_TEMOIN:
        sys.exit("ARRET PB-1 : le temoin ne repond pas au canon %s (lu %s)" % (CANON_TEMOIN, ht))
    LOG("CANON", "instrument v8 %s (%d o, CRLF %s) ; temoin v11 %s (%d o, CRLF %s) -- authentifies"
        % (hi, oct_i, crlf_i, ht, oct_t, crlf_t))

    spec = importlib.util.spec_from_file_location("banc_v8", a.instrument)
    banc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(banc)
    import numpy as np
    LOG("IMPORT", "instrument importe en lecture : VERSION=%s ; DELTA=%s ; R_CAP=%s ; M_PAS=%d ; K_BASC=%d"
        % (banc.VERSION, banc.DELTA, banc.R_CAP, banc.M_PAS, banc.K_BASC))

    hm = sha_brut(a.moteur)
    if hm != banc.MOTEUR[1]:
        sys.exit("ARRET PB-1 : le moteur ne repond pas a l'empreinte que l'instrument porte (%s / %s)" % (hm[:16], banc.MOTEUR[1][:16]))
    chemin_norm = a.moteur.replace("\\", "/")
    if not chemin_norm.endswith(banc.MOTEUR[0]):
        sys.exit("ARRET : charger_moteur exige la disposition <registre>/%s ; recu %s" % (banc.MOTEUR[0], a.moteur))
    registre = chemin_norm[: -len(banc.MOTEUR[0])].rstrip("/") or "."
    mod = banc.charger_moteur(registre)      # custody transitive (empreinte, globales, certifier_gel)
    LOG("MOTEUR", "%s sha256 brut %s -- charge par charger_moteur de l'instrument (registre %s) ; P=%d DT=%r"
        % (a.moteur, hm[:16], registre, mod.P, mod.DT))
    LOG("PLATEFORME", "python %s ; numpy %s ; %s ; %s"
        % (sys.version.split()[0], np.__version__, platform.platform(), platform.machine()))

    # ---- 2. le reglage de la cellule, aux formules de l'instrument ---------------
    p, w2 = P_CELLULE, W2_CELLULE
    al = float(banc.alpha_de(p)); A = banc.A_de(p)
    td, tc, dt2 = banc.tau_dom(w2), banc.tau_cap(w2), banc.dt2_de(w2)
    f = banc.forcage_de(p, w2)
    tau0 = banc.K_BASC * td
    tol = banc.tol_ordre(al)
    C_eff = 1.0 / (1.0 - 2.0 ** (-tol))
    eps = float(np.finfo(float).eps)
    n_attendu_base = int((banc.K_BASC / banc.R_CAP - 1) * banc.M_PAS)     # (k/r - 1) M = 380, DERIVE
    LOG("CELLULE", "p=%d w2=%.2f alpha=%s A=%r tau_dom=%r tau_CAP=%r dt2=%r tau0=k*tau_dom=%r"
        % (p, w2, banc.alpha_de(p), A, td, tc, dt2, tau0))
    LOG("REGLE-5.4", "tol_ordre(7)=%r C_eff(7)=%r eps=%r ; bande de lecture de p_obs [%.4f, %.4f]"
        % (tol, C_eff, eps, 4 - tol, 4 + tol))

    # ---- 3. les attentes, AVANT la premiere integration --------------------------
    bas = RATIO_M2 * C_eff - B_SUR_PLANCHER[1]
    haut = RATIO_M1_28_08 * C_eff + B_SUR_PLANCHER[1]
    LOG("ATTENTE", "compte attendu des flots : %d (dt2/2^k, k=0..%d), n_pas attendu 380 x 2^k ; chaque flot doit finir sur TAU_FIN"
        % (NIVEAUX, NIVEAUX - 1))
    LOG("ATTENTE", "E-A : aux deux paires raffinees (bases dt2/2 et dt2/4), p_obs HORS [%.4f, %.4f] ; falsifiee si l'une y entre"
        % (4 - tol, 4 + tol))
    LOG("ATTENTE", "E-B : e(dt2/2)/plancher a la paire du gel dans [%.2f, %.2f] (0.684 et 0.759 x C_eff, elargis de 1.74 plancher) ; falsifiee sinon"
        % (bas, haut))
    LOG("ATTENTE", "E-C : aucune attente sur le signe de p_obs a la derniere paire ; consigne seulement")

    # ---- 4. les quatre flots ------------------------------------------------------
    flots = []
    compte = {"joues": 0, "sautes": 0}
    for k in range(NIVEAUX):
        dt = dt2 / 2 ** k
        etat = banc.vers_composantes(*banc.xm_et_derivees(p, tau0), w2)
        ph = banc.phase2_pu(w2, p, etat, -tau0, dt, forcage=f, tau_star=0.0, tau_fin=tc)
        compte["joues"] += 1
        tau = -ph["t"]
        xm = A * tau ** (-al)
        x = ph["x1"] + ph["x2"]
        err_rel = np.abs(x - xm) / np.abs(xm)
        e = float(np.max(err_rel))
        i_max = int(np.argmax(err_rel))
        R_serie = (np.abs(ph["x1"]) + np.abs(ph["x2"])) / np.maximum(np.abs(x), 1e-300)
        R_comp = float(np.max(R_serie))
        plancher = eps * R_comp
        n = int(ph["n"])
        fl = {"k": k, "pas": "dt2/%d" % (2 ** k) if k else "dt2", "dt": dt, "n_pas": n,
              "n_pas_attendu": n_attendu_base * 2 ** k, "n_pas_conforme": n == n_attendu_base * 2 ** k,
              "evenement": ph["evenement"], "tau_fin": float(tau[-1]),
              "e": e, "R_composantes": R_comp, "plancher_composantes": plancher,
              "e_sur_plancher": e / plancher,
              "tau_au_max": float(tau[i_max]), "R_au_max": float(R_serie[i_max]),
              "indice_max": i_max, "err_rel_fin": float(err_rel[-1]),
              "seuil_5_4_du_flot": C_eff * plancher, "ratio_seuil_du_flot": e / (C_eff * plancher)}
        flots.append(fl)
        LOG("FLOT-%d" % k, "%s dt=%.6e n_pas=%d (attendu %d, %s) %s tau_fin=%.6e e=%.6e R=%.3f plancher=%.6e e/plancher=%.4f tau_max=%.4e (R la %.3f) err_fin=%.3e"
            % (fl["pas"], dt, n, fl["n_pas_attendu"], "conforme" if fl["n_pas_conforme"] else "NON CONFORME",
               ph["evenement"], fl["tau_fin"], e, R_comp, plancher, fl["e_sur_plancher"], fl["tau_au_max"], fl["R_au_max"], fl["err_rel_fin"]))
        if ph["evenement"] != "TAU_FIN":
            sys.exit("ARRET : le flot %s ne finit pas sur TAU_FIN (%s) -- mesure sans fenetre" % (fl["pas"], ph["evenement"]))

    # ---- 5. les trois paires (dt, dt/2), lues comme l'instrument lit la paire du gel
    paires = []
    for k in range(NIVEAUX - 1):
        g, fin = flots[k], flots[k + 1]
        p_obs = math.log2(g["e"] / fin["e"]) if fin["e"] > 0 else float("inf")
        lec = banc.lecture_5_4(fin["e"], p_obs, al, fin["plancher_composantes"])
        pr = {"base": g["pas"], "fin": fin["pas"], "e_base": g["e"], "e_fin": fin["e"], "p_obs": p_obs,
              "dans_bande_ordre": bool(abs(p_obs - 4) <= tol),
              "lecture_5_4_sur_flot_fin": {"C_effectif": lec["C_effectif"], "seuil": lec["seuil"],
                                           "ratio_seuil": lec["ratio_seuil"], "W_plancher": lec["W_plancher"],
                                           "W_pas": lec["W_pas"], "lu": bool(lec["lu"])},
              "paire_du_gel": k == 0}
        paires.append(pr)
        LOG("PAIRE-%d" % k, "(%s, %s) p_obs=%.4f %s ; 5.4 sur le flot fin : e/seuil=%.4f C_eff=%.4f W-plancher %s W-pas %s%s"
            % (g["pas"], fin["pas"], p_obs, "DANS la bande RK4" if pr["dans_bande_ordre"] else "HORS bande",
               lec["ratio_seuil"], lec["C_effectif"], lec["W_plancher"], lec["W_pas"], " [PAIRE DU GEL]" if k == 0 else ""))

    # ---- 6. les attentes, confrontees ------------------------------------------------
    EA = all(not pr["dans_bande_ordre"] for pr in paires[1:])
    ratio_gel = paires[0]["lecture_5_4_sur_flot_fin"]["ratio_seuil"]
    e_sur_pl_gel = flots[1]["e_sur_plancher"]
    EB = bas <= e_sur_pl_gel <= haut
    LOG("VERDICT-E-A", "%s : p_obs raffines = %s ; bande [%.4f, %.4f]"
        % ("TENUE" if EA else "FALSIFIEE", ["%.4f" % pr["p_obs"] for pr in paires[1:]], 4 - tol, 4 + tol))
    LOG("VERDICT-E-B", "%s : e(dt2/2)/plancher = %.4f dans [%.2f, %.2f] ; e/seuil (grandeur des deux machines) = %.4f contre 0.759 (m1 28/08) et 0.684 (m2)"
        % ("TENUE" if EB else "FALSIFIEE", e_sur_pl_gel, bas, haut, ratio_gel))
    LOG("E-C", "signe de p_obs a la derniere paire : %s (%.4f), consigne sans attente"
        % ("positif" if paires[-1]["p_obs"] > 0 else "negatif ou nul", paires[-1]["p_obs"]))
    LOG("COMPTE", "flots joues %d + sautes %d == attendus %d : %s"
        % (compte["joues"], compte["sautes"], NIVEAUX, "OK" if compte["joues"] + compte["sautes"] == NIVEAUX else "MORD"))
    lecture = ("ECART DERIVE du plancher (E-A tenue)" if EA else "ECART INDECIDABLE par cette mesure (E-A falsifiee)")
    LOG("LECTURE", lecture + " -- classe 3, aucun verdict de gel, la tenaille n'est pas lue ici")

    res = {"geste": "convergence en dt de e(dt2/2), cellule 7|1.73, machine 1", "classe": 3,
           "pieces": {"instrument_v8_B": hi, "temoin_v11_B": ht, "moteur_sha256_brut": hm,
                      "moteur_chemin": a.moteur, "registre": registre},
           "plateforme": {"python": sys.version.split()[0], "numpy": np.__version__, "platform": platform.platform(),
                          "machine": platform.machine()},
           "cellule": {"p": p, "w2": w2, "alpha": str(banc.alpha_de(p)), "A": A, "tau_dom": td, "tau_CAP": tc,
                       "dt2": dt2, "tau0": tau0, "tol_ordre": tol, "C_effectif": C_eff, "eps": eps,
                       "n_pas_attendu_base": n_attendu_base},
           "attentes": {"E-A": {"enonce": "p_obs hors [4-tol, 4+tol] aux deux paires raffinees", "verdict": "TENUE" if EA else "FALSIFIEE"},
                        "E-B": {"enonce": "e(dt2/2)/plancher dans [%.4f, %.4f]" % (bas, haut), "valeur": e_sur_pl_gel,
                                "verdict": "TENUE" if EB else "FALSIFIEE"},
                        "E-C": {"enonce": "aucune attente ; signe de p_obs a la derniere paire consigne", "p_obs": paires[-1]["p_obs"]}},
           "references_deux_machines": {"ratio_seuil_m1_28_08": RATIO_M1_28_08, "ratio_seuil_m2": RATIO_M2,
                                        "ratio_seuil_ici": ratio_gel},
           "flots": flots, "paires": paires, "compte": dict(compte, attendus=NIVEAUX),
           "lecture": lecture, "duree_s": time.perf_counter() - t_debut,
           "journal_instrument": list(banc.JRN.lignes)}
    chemin_json = os.path.join(a.sortie, "convergence_dt_7_1p73_machine1_v1.json")
    banc.ecrire_ascii(chemin_json, banc.json_ascii(res))
    LOG("JSON", "%s ecrit, empreinte B %s" % (chemin_json, banc.empreinte_B(chemin_json)))
    LOG("FIN", "%.1f s" % (time.perf_counter() - t_debut))
    banc.ecrire_ascii(os.path.join(a.sortie, "convergence_dt_7_1p73_machine1_v1.log"), "\n".join(LOG.lignes) + "\n")


if __name__ == "__main__":
    main()
