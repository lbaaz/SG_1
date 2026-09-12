#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
GESTE (2), SUITE -- LA CAUSE DE L'ECART DETERMINISTE ENTRE PLATEFORMES A 7|1.73
(classe 3, machine 1, 2026-09-12) -- diagnostic_pow_cas_durs_machine1_v1.py
=====================================================================================
Question ouverte de machine 2 (POUR_MACHINE1 43d6fbbb5477e33a, section 6) : pourquoi
l'ecart entre les deux machines s'annule-t-il au pas fin ? Mesure de m2 : les flots
different d'un nombre ENTIER d'ulp de x1 a tau_CAP (1, 2, 2, 0 ulp aux pas dt2, dt2/2,
dt2/4, dt2/8 -- lecture m1 de sa comparaison), deux rejeux au meme poste sont identiques
au bit : difference deterministe, pas un bruit.

HYPOTHESE MISE A L'EPREUVE (ecrite avant la mesure, avec ce qui la ferait tomber)
  H-POW  Les seules operations non IEEE-elementaires du flot sont les puissances :
         (K1) (a1 + a2) ** 6 dans base (numpy, taille 1) ; (K2) tau ** (-a-2) et
         tau ** (-a) dans f(tau) (float Python) ; (K3) tau ** (-a) sur le tableau tau
         pour x_m dans e (numpy). Deux libm de qualite (glibc, UCRT) rendent le double
         CORRECTEMENT ARRONDI (CR) sauf sur des CAS DURS rares, differents d'une libm a
         l'autre. Un cas dur de K1 perturbe base d'un ulp ; cette perturbation, dt fois
         plus petite que l'ulp de l'etat, ne bascule le dernier bit de x1/v1 que sur une
         fraction des appels ; le nombre net de basculements par flot est petit et
         entier -- 1, 2, 2, 0 sont de cette forme. K2 est negligeable : f pese ~1e-8 de
         base au bord (f/base ~ (1 + w2^2) tau^2 / ((a+2)(a+3))). K3 ne touche que
         x_m, donc e a 1e-16 relatif.
         FALSIFIEE si : (i) le jumeau bit-fidele du flot (validation ci-dessous) ne
         reproduit pas l'instrument au bit ; ou (ii) le jumeau a puissances CR ne
         reproduit ni l'instrument ici ni les valeurs de machine 2 ; ou (iii) aucun cas
         dur n'est trouve sur les flots ou les machines different.
  CE QUE CE SCRIPT MESURE, SUR CETTE PLATEFORME SEULEMENT
    1. reproduit les quatre flots de l'instrument (jouer_T2, meme code) ;
    2. valide un JUMEAU en float Python, meme ordre d'operations, avec la puissance de
       l'instrument (numpy) : doit egaler l'instrument AU BIT sur x1, x2 a chaque pas ;
    3. enumere, le long de chaque flot, TOUS les appels K1, K2, K3 et compte ceux dont le
       resultat libm/numpy n'est pas le double CR (reference : Decimal a 60 chiffres,
       arrondi au plus proche par Fraction -> float) ;
    4. rejoue le jumeau avec K1 CR seulement, puis K1+K2+K3 CR, et compare a
       l'instrument (m1) et aux e de machine 2 (rejeu1 ed09e29e91b6eb00) ;
    5. pour chaque cas dur K1, rejoue le jumeau avec CE SEUL appel corrige et mesure
       l'effet sur x1 + x2 a tau_CAP, en ulp de x1 (bascule ou absorbe).
  Rien n'est edite (PB-1) ; l'instrument est importe en lecture ; le moteur n'est pas
  appele par T-2 et n'est pas charge ici (declare).
USAGE
  python3 diagnostic_pow_cas_durs_machine1_v1.py --instrument <v8> --temoin <v11>
      --rejeu-m2 <rejeu1_convergence_dt_machine2_v1.json> --sortie <dossier>
"""
import argparse, hashlib, importlib.util, json, math, os, platform, sys, time, unicodedata
from decimal import Decimal, localcontext
from fractions import Fraction

CANON_INSTRUMENT = "4d8882a2223a5c74"
CANON_TEMOIN = "a2e7ef3e237c5acf"
CANON_REJEU_M2 = "ed09e29e91b6eb00"
P_CELLULE, W2_CELLULE, NIVEAUX = 7, 1.73, 4


def empreinte_B(chemin):
    b = open(chemin, "rb").read()
    t = unicodedata.normalize("NFC", b.decode("utf-8").replace("\r\n", "\n"))
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


class Log(object):
    def __init__(self):
        self.lignes = []

    def __call__(self, cle, msg):
        ligne = "[%s] %-12s %s" % (time.strftime("%H:%M:%SZ", time.gmtime()), cle, msg)
        self.lignes.append(ligne)
        print(ligne)


LOG = Log()


def pow_cr(x, y):
    """Double correctement arrondi de x ** y : Decimal a 60 chiffres (exact pour y
    entier ; exp/ln a 60 chiffres sinon -- un ecart de 1e-60 ne change le double
    qu'a 1e-44 pres d'une frontiere), puis Fraction -> float (arrondi au plus proche
    pair, division entiere de CPython)."""
    with localcontext() as ctx:
        ctx.prec = 60
        v = Decimal(x) ** Decimal(y)
    return float(Fraction(v))


def ulps_entre(u, v):
    """Ecart entre deux doubles en ulp de u (signe : v - u)."""
    if u == v:
        return 0.0
    return (v - u) / math.ulp(u)


def hexf(x):
    return float(x).hex()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--instrument", required=True)
    ap.add_argument("--temoin", required=True)
    ap.add_argument("--rejeu-m2", required=True)
    ap.add_argument("--sortie", required=True)
    a = ap.parse_args()
    t_debut = time.perf_counter()
    os.makedirs(a.sortie, exist_ok=True)
    for chemin, canon, nom in ((a.instrument, CANON_INSTRUMENT, "instrument v8"), (a.temoin, CANON_TEMOIN, "temoin v11"),
                               (a.rejeu_m2, CANON_REJEU_M2, "rejeu1 m2")):
        h = empreinte_B(chemin)
        if h != canon:
            sys.exit("ARRET PB-1 : %s ne repond pas au canon %s (lu %s)" % (nom, canon, h))
        LOG("CANON", "%s %s authentifie" % (nom, canon))
    spec = importlib.util.spec_from_file_location("banc_v8", a.instrument)
    banc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(banc)
    import numpy as np
    m2 = json.load(open(a.rejeu_m2))
    e_m2 = [fl["e"] for fl in m2["flots"]]
    LOG("IMPORT", "instrument %s importe en lecture ; moteur NON charge (T-2 ne l'appelle pas) ; e de m2 : %s"
        % (banc.VERSION, ["%r" % v for v in e_m2]))
    cpu = ""
    try:
        for ligne in open("/proc/cpuinfo"):
            if ligne.startswith("model name"):
                cpu = ligne.split(":", 1)[1].strip(); break
        flags = [l for l in open("/proc/cpuinfo") if l.startswith("flags")][0]
        cpu += " ; avx512f %s ; fma %s" % ("avx512f" in flags, " fma " in flags)
    except Exception:
        cpu = "(cpuinfo non lu)"
    LOG("PLATEFORME", "python %s ; numpy %s ; %s ; %s" % (sys.version.split()[0], np.__version__, platform.platform(), cpu))

    p, w2 = P_CELLULE, W2_CELLULE
    al = float(banc.alpha_de(p)); A = banc.A_de(p); g = banc.G_REF; W1 = banc.W1
    td, tc, dt2 = banc.tau_dom(w2), banc.tau_cap(w2), banc.dt2_de(w2)
    tau0 = banc.K_BASC * td
    y_state = p - 1                       # 6 : l'instrument ecrit (a1 + a2) ** (p - 1), p - 1 entier
    y_f1, y_f2 = -al - 2, -al             # les exposants EXACTS que f evalue (doubles)
    LOG("CELLULE", "p=%d w2=%.2f a=%r A=%r tau0=%r tau_CAP=%r dt2=%r ; exposants K1 %r, K2 %r et %r, K3 %r"
        % (p, w2, al, A, tau0, tc, dt2, y_state, y_f1, y_f2, -al))
    LOG("A_de", "A = 306.432 ** 0.2 par libm : %s ; CR : %s ; %s"
        % (hexf(A), hexf(pow_cr(float(banc.K_de(p) / Fraction(repr(g))), 1.0 / (p - 2))),
           "IDENTIQUES" if A == pow_cr(float(banc.K_de(p) / Fraction(repr(g))), 1.0 / (p - 2)) else "DIFFERENT"))

    # ---------- les puissances de reference de cette plateforme ----------------------
    def pow_numpy(x, y):                  # exactement ce que fait acc_t : tableau de taille 1 ** entier
        return float((np.array([x]) ** y)[0])

    def pow_py(x, y):
        return x ** y

    # ---------- le jumeau du flot, meme ordre d'operations que phase2_pu ------------
    def jumeau(dt, pow_state, pow_f, journal=None):
        """Retourne (t, x1, x2) listes de floats ; journal (optionnel) recoit chaque
        appel de puissance : (kind, i_pas, etage, x, y, resultat)."""
        delta = w2 * w2 - W1 * W1

        def f(tau):
            u = pow_f(tau, -al - 2); v = pow_f(tau, -al)
            if journal is not None:
                journal.append(("K2", i_pas[0], etage[0], tau, -al - 2, u))
                journal.append(("K2", i_pas[0], etage[0], tau, -al, v))
            return A * ((1 + w2 * w2) * al * (al + 1) * u + w2 * w2 * v)

        def acc_t(a1, a2, t):
            s = a1 + a2
            pw = pow_state(s, y_state)
            if journal is not None:
                journal.append(("K1", i_pas[0], etage[0], s, y_state, pw))
            base = g * pw
            Fz = f(0.0 - t)
            return -W1 * W1 * a1 + (base + Fz) / delta, -w2 * w2 * a2 - (base + Fz) / delta

        x1, x2, v1, v2 = banc.vers_composantes(*banc.xm_et_derivees(p, tau0), w2)
        t0 = -tau0
        T, X1, X2 = [t0], [x1], [x2]
        i_pas, etage = [0], [0]
        n = 0
        while True:
            n += 1; i_pas[0] = n
            t = t0 + n * dt
            tp = t0 + (n - 1) * dt
            etage[0] = 1
            k1v1, k1v2 = acc_t(x1, x2, tp); k1x1, k1x2 = v1, v2
            etage[0] = 2
            k2v1, k2v2 = acc_t(x1 + .5 * dt * k1x1, x2 + .5 * dt * k1x2, tp + .5 * dt)
            k2x1, k2x2 = v1 + .5 * dt * k1v1, v2 + .5 * dt * k1v2
            etage[0] = 3
            k3v1, k3v2 = acc_t(x1 + .5 * dt * k2x1, x2 + .5 * dt * k2x2, tp + .5 * dt)
            k3x1, k3x2 = v1 + .5 * dt * k2v1, v2 + .5 * dt * k2v2
            etage[0] = 4
            k4v1, k4v2 = acc_t(x1 + dt * k3x1, x2 + dt * k3x2, tp + dt)
            k4x1, k4x2 = v1 + dt * k3v1, v2 + dt * k3v2
            x1 = x1 + dt / 6 * (k1x1 + 2 * k2x1 + 2 * k3x1 + k4x1)
            x2 = x2 + dt / 6 * (k1x2 + 2 * k2x2 + 2 * k3x2 + k4x2)
            v1 = v1 + dt / 6 * (k1v1 + 2 * k2v1 + 2 * k3v1 + k4v1)
            v2 = v2 + dt / 6 * (k1v2 + 2 * k2v2 + 2 * k3v2 + k4v2)
            T.append(t); X1.append(x1); X2.append(x2)
            if 0.0 - t <= tc * (1.0 + 1e-12):
                break
        return T, X1, X2

    def erreur_e(T, X1, X2, mode):
        """e = max |x1 + x2 - x_m| / |x_m| avec x_m = A tau ** (-a), tau = -t.
        mode 'numpy' : EXACTEMENT l'expression de l'instrument (tableau tau ** (-a)) ;
        mode 'cr' : tau ** (-a) correctement arrondi, element par element."""
        tau = -np.array(T)
        if mode == "numpy":
            xm = A * tau ** (-al)
        else:
            xm = A * np.array([pow_cr(float(v), -al) for v in tau])
        x = np.array(X1) + np.array(X2)
        return float(np.max(np.abs(x - xm) / np.abs(xm)))

    resultats = {"flots": [], "plateforme": {"python": sys.version.split()[0], "numpy": np.__version__,
                                              "platform": platform.platform(), "cpu": cpu},
                 "hypothese": "H-POW", "pieces": {"instrument_v8_B": CANON_INSTRUMENT, "temoin_v11_B": CANON_TEMOIN,
                                                  "rejeu1_m2_B": CANON_REJEU_M2}}
    for k in range(NIVEAUX):
        dt = dt2 / 2 ** k
        nom = "dt2/%d" % (2 ** k) if k else "dt2"
        # 1. l'instrument
        etat = banc.vers_composantes(*banc.xm_et_derivees(p, tau0), w2)
        ph = banc.phase2_pu(w2, p, etat, -tau0, dt, forcage=banc.forcage_de(p, w2), tau_star=0.0, tau_fin=tc)
        tau_arr = -ph["t"]; xm_arr = A * tau_arr ** (-al)
        e_inst = float(np.max(np.abs((ph["x1"] + ph["x2"]) - xm_arr) / np.abs(xm_arr)))
        X1i, X2i = [float(v) for v in ph["x1"]], [float(v) for v in ph["x2"]]
        # 2. le jumeau, puissance numpy (celle de l'instrument), f en float Python
        jr = []
        T, X1, X2 = jumeau(dt, pow_numpy, pow_py, journal=jr)
        fidele = (len(X1) == len(X1i)) and all(u == v for u, v in zip(X1, X1i)) and all(u == v for u, v in zip(X2, X2i))
        if not fidele:
            i0 = next((i for i, (u, v) in enumerate(zip(X1, X1i)) if u != v), None)
            sys.exit("ARRET H-POW (i) : le jumeau n'est pas bit-fidele a l'instrument au pas %s (premier ecart a l'indice %s)" % (nom, i0))
        e_jum = erreur_e(T, X1, X2, "numpy")
        err_fin_m1 = float(abs((X1[-1] + X2[-1]) - float(xm_arr[-1])) / abs(float(xm_arr[-1])))
        err_fin_m2 = m2["flots"][k]["err_rel_fin"]
        # 3. l'enumeration des cas durs de cette plateforme
        cas = {"K1": [], "K2": [], "K3": []}
        n_appels = {"K1": 0, "K2": 0, "K3": 0}
        for (kind, i, et, x, y, res) in jr:
            n_appels[kind] += 1
            cr = pow_cr(x, y)
            if cr != res:
                cas[kind].append({"appel": n_appels[kind], "pas": i, "etage": et, "x": x, "x_hex": hexf(x), "y": y,
                                  "libm": res, "libm_hex": hexf(res), "cr": cr, "cr_hex": hexf(cr),
                                  "ulp_libm_moins_cr": -ulps_entre(res, cr)})
        n_numpy_vs_py = sum(1 for (kind, i, et, x, y, res) in jr if kind == "K1" and res != pow_py(x, y))
        pw_arr = tau_arr ** (-al)                     # le chemin tableau, celui de l'instrument
        for i in range(len(tau_arr)):
            n_appels["K3"] += 1
            tau_i = float(tau_arr[i]); res = float(pw_arr[i])
            cr = pow_cr(tau_i, -al)
            if cr != res:
                cas["K3"].append({"appel": i, "tau": tau_i, "tau_hex": hexf(tau_i), "numpy": res, "cr": cr,
                                  "ulp_numpy_moins_cr": -ulps_entre(res, cr)})
        # 4. les jumeaux CR
        T_c1, X1_c1, X2_c1 = jumeau(dt, pow_cr, pow_py)          # K1 CR seul
        T_c, X1_c, X2_c = jumeau(dt, pow_cr, pow_cr)             # K1 + K2 CR
        e_c1 = erreur_e(T_c1, X1_c1, X2_c1, "numpy")
        e_c = erreur_e(T_c, X1_c, X2_c, "cr")
        e_c_xmnumpy = erreur_e(T_c, X1_c, X2_c, "numpy")
        x_fin = X1[-1] + X2[-1]; ulp_x1 = math.ulp(X1[-1])
        def diverge(XA1, XA2, XB1, XB2):
            i0 = next((i for i in range(len(XA1)) if XA1[i] != XB1[i] or XA2[i] != XB2[i]), None)
            dx = (XB1[-1] + XB2[-1]) - x_fin
            return i0, dx / ulp_x1
        i0_c1, d_c1 = diverge(X1, X2, X1_c1, X2_c1)
        i0_c, d_c = diverge(X1, X2, X1_c, X2_c)
        # 5. chaque cas dur K1, corrige SEUL
        effets = []
        for cd in cas["K1"]:
            cible = cd["appel"]; compteur = [0]
            def pow_patch(x, y):
                compteur[0] += 1
                return pow_cr(x, y) if compteur[0] == cible else pow_numpy(x, y)
            Tp, X1p, X2p = jumeau(dt, pow_patch, pow_py)
            i0p, dp = diverge(X1, X2, X1p, X2p)
            effets.append({"appel": cible, "pas": cd["pas"], "etage": cd["etage"], "ulp_libm_moins_cr": cd["ulp_libm_moins_cr"],
                           "premier_pas_qui_differe": i0p, "delta_x_fin_en_ulp_x1": dp,
                           "effet": "ABSORBE" if dp == 0 else "BASCULE"})
        fl = {"pas": nom, "dt": dt, "n_pas": len(X1) - 1, "e_instrument": e_inst, "e_jumeau_numpy": e_jum,
              "e_jumeau_egal_instrument": e_jum == e_inst,
              "jumeau_bit_fidele": fidele, "e_m2": e_m2[k], "err_fin_m1": err_fin_m1, "err_fin_m2": err_fin_m2,
              "ecart_bord_m1_m2_en_ulp_x1": ((err_fin_m2 - err_fin_m1) * abs(float(xm_arr[-1]))) / ulp_x1,
              "x1_fin": X1[-1], "x2_fin": X2[-1], "x_fin": x_fin, "ulp_x1_fin": ulp_x1,
              "appels": n_appels, "K1_numpy_differe_de_python": n_numpy_vs_py,
              "cas_durs": {kk: len(v) for kk, v in cas.items()}, "cas_durs_detail": cas,
              "jumeau_K1_CR": {"e": e_c1, "premier_pas_qui_differe": i0_c1, "delta_x_fin_en_ulp_x1": d_c1,
                               "egal_m1": e_c1 == e_inst, "egal_m2": e_c1 == e_m2[k]},
              "jumeau_tout_CR": {"e_xm_CR": e_c, "e_xm_numpy": e_c_xmnumpy, "premier_pas_qui_differe": i0_c,
                                 "delta_x_fin_en_ulp_x1": d_c, "egal_m1": e_c == e_inst or e_c_xmnumpy == e_inst,
                                 "egal_m2": e_c == e_m2[k] or e_c_xmnumpy == e_m2[k]},
              "effet_de_chaque_cas_dur_K1": effets}
        resultats["flots"].append(fl)
        LOG("FLOT-%s" % nom, "n_pas=%d e_inst=%r e_jumeau=%r (egal %s) fidele=%s ; e_m2=%r ; ecart au bord m2-m1 = %+.3f ulp(x1) ; x1_fin=%s ulp=%.3e"
            % (fl["n_pas"], e_inst, e_jum, e_jum == e_inst, fidele, e_m2[k], fl["ecart_bord_m1_m2_en_ulp_x1"], hexf(X1[-1]), ulp_x1))
        LOG("APPELS-%s" % nom, "K1 %d (numpy != python sur %d) ; K2 %d ; K3 %d ; CAS DURS ici : K1 %d, K2 %d, K3 %d"
            % (n_appels["K1"], n_numpy_vs_py, n_appels["K2"], n_appels["K3"], len(cas["K1"]), len(cas["K2"]), len(cas["K3"])))
        for cd in cas["K1"]:
            LOG("K1-DUR-%s" % nom, "appel %d pas %d etage %d x=%s libm=%s cr=%s (libm - cr = %+.1f ulp)"
                % (cd["appel"], cd["pas"], cd["etage"], cd["x_hex"], cd["libm_hex"], cd["cr_hex"], cd["ulp_libm_moins_cr"]))
        for ef in effets:
            LOG("EFFET-%s" % nom, "cas dur K1 appel %d (pas %d) corrige seul : premier pas qui differe %s, x_fin deplace de %+.1f ulp(x1) -> %s"
                % (ef["appel"], ef["pas"], ef["premier_pas_qui_differe"], ef["delta_x_fin_en_ulp_x1"], ef["effet"]))
        LOG("JUMEAU-CR-%s" % nom, "K1 CR seul : e=%r (egal m1 %s, egal m2 %s, premier pas %s, x_fin %+.1f ulp) ; tout CR : e=%r / xm numpy %r (egal m1 %s, egal m2 %s, premier pas %s, x_fin %+.1f ulp)"
            % (e_c1, e_c1 == e_inst, e_c1 == e_m2[k], i0_c1, d_c1, e_c, e_c_xmnumpy,
               fl["jumeau_tout_CR"]["egal_m1"], fl["jumeau_tout_CR"]["egal_m2"], i0_c, d_c))

    # ---------- bilan H-POW -------------------------------------------------------
    F = resultats["flots"]
    tous_fideles = all(f["jumeau_bit_fidele"] for f in F)
    cr_egal_m2 = [f["jumeau_tout_CR"]["egal_m2"] or f["jumeau_K1_CR"]["egal_m2"] for f in F]
    cr_egal_m1 = [f["jumeau_tout_CR"]["egal_m1"] or f["jumeau_K1_CR"]["egal_m1"] for f in F]
    flots_differents = [i for i, f in enumerate(F) if f["e_m2"] != f["e_instrument"]]
    cas_sur_differents = [F[i]["cas_durs"]["K1"] for i in flots_differents]
    bascules = [sum(1 for ef in f["effet_de_chaque_cas_dur_K1"] if ef["effet"] == "BASCULE") for f in F]
    LOG("BILAN", "jumeau fidele aux 4 pas : %s ; CR egal m1 : %s ; CR egal m2 : %s ; cas durs K1 par flot : %s ; bascules : %s"
        % (tous_fideles, cr_egal_m1, cr_egal_m2, [f["cas_durs"]["K1"] for f in F], bascules))
    if not tous_fideles:
        verdict = "H-POW FALSIFIEE (i)"
    elif all(cr_egal_m2[i] for i in flots_differents) and all(cr_egal_m1[i] for i in range(NIVEAUX) if i not in flots_differents):
        verdict = "H-POW TENUE, CAUSE NOMMEE : le jumeau a puissances CR rend les valeurs de machine 2 aux pas ou les machines different et celles de machine 1 ailleurs -- cette plateforme (glibc/numpy) n'est pas CR sur les cas durs enumeres, l'autre l'est sur ce flot"
    elif all(cr_egal_m1):
        verdict = "H-POW TENUE, CAUSE DE L'AUTRE COTE : cette plateforme est CR sur tous les appels des quatre flots ; l'ecart vient de cas durs de l'autre libm, a enumerer par machine 2 avec ce script"
    elif any(c > 0 for c in cas_sur_differents):
        verdict = "H-POW PARTIELLE : des cas durs existent ici sur les flots qui different, mais le jumeau CR ne rend ni m1 ni m2 -- les deux libm ont des cas durs sur ces flots ; enumeration m2 requise"
    else:
        verdict = "H-POW FALSIFIEE (iii) : aucun cas dur ici sur les flots qui different, et le jumeau CR ne rend pas m2"
    resultats["verdict"] = verdict
    resultats["duree_s"] = time.perf_counter() - t_debut
    LOG("VERDICT", verdict)
    chemin_json = os.path.join(a.sortie, "diagnostic_pow_cas_durs_machine1_v1.json")
    banc.ecrire_ascii(chemin_json, banc.json_ascii(resultats))
    LOG("JSON", "%s ecrit, empreinte B %s" % (chemin_json, banc.empreinte_B(chemin_json)))
    LOG("FIN", "%.1f s" % (time.perf_counter() - t_debut))
    banc.ecrire_ascii(os.path.join(a.sortie, "diagnostic_pow_cas_durs_machine1_v1.log"), "\n".join(LOG.lignes) + "\n")


if __name__ == "__main__":
    main()
