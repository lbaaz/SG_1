#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
GESTE (2), SUITE -- LES NEUF CELLULES T-2 (paire du gel dt2, dt2/2) : cas durs et basculements par cellule
Derive du v2 (e13e590d384da058) : memes jumeau, meme reference CR, meme comptage ; boucle sur les 9 cellules du reglage prime.
 -- LA CAUSE DE L'ECART DETERMINISTE ENTRE PLATEFORMES A 7|1.73
(classe 3, machine 1, 2026-09-12) -- diagnostic_pow_cas_durs_machine1_v2.py
=====================================================================================
v2 = v1 (a808e7a8635b0ced, non editee) + trois changements, apres la lecture m2
19427c98dd9e6ecf : (1) la garde du JSON compare accepte l'un OU l'autre canon (JSON du
geste m1 c8d86e5e5b4fd745 ; rejeu1 m2 ed09e29e91b6eb00) et NOMME lequel elle a recu
(D-G2-1 : la prose de la note eb056e4e844f29a3, section 7, contredisait la garde de la
v1) ; (2) les etiquettes et le verdict sont SYMETRIQUES -- 'ce poste' contre 'le JSON
recu' -- et le cas degenere (JSON recu = ce poste au bit) est nomme (D-G2-2 : la v1
imprimait un verdict a texte fixe, cote m1) ; (3) la ligne PLATEFORME porte un TEMOIN
D'ARRONDI executable : (1765.6704444885254) ** 6 par le tableau numpy et par le pow de
Python, en hexadecimal -- ...9c5 est le noyau SIMD, ...9c6 le double correctement
arrondi -- parce que c'est le noyau qui decide, pas le nom du CPU, de l'OS ni de la version.
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
  python3 diagnostic_pow_cas_durs_machine1_v2.py --instrument <v8> --temoin <v11>
      --rejeu <JSON du geste m1 c8d86e5e OU rejeu1 m2 ed09e29e> --sortie <dossier>
"""
import argparse, hashlib, importlib.util, json, math, os, platform, sys, time, unicodedata
from decimal import Decimal, localcontext
from fractions import Fraction

CANON_INSTRUMENT = "4d8882a2223a5c74"
CANON_TEMOIN = "a2e7ef3e237c5acf"
CANONS_REJEU = {"c8d86e5e5b4fd745": "JSON du geste, machine 1 (lot 2b155abffbe4f6ff)",
                "ed09e29e91b6eb00": "rejeu1, machine 2 (lot eb7fb1cefbf2cec4)"}
TEMOIN_X = 1765.6704444885254            # 0x1.b96ae89000000p+10, l'entree de l'appel 2827 (pas 707) a dt2/2
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
    ap.add_argument("--instrument", required=True); ap.add_argument("--temoin", required=True); ap.add_argument("--sortie", required=True)
    a = ap.parse_args(); os.makedirs(a.sortie, exist_ok=True); t_debut = time.perf_counter()
    for chemin, canon, nom in ((a.instrument, CANON_INSTRUMENT, "instrument v8"), (a.temoin, CANON_TEMOIN, "temoin v11")):
        h = empreinte_B(chemin)
        if h != canon: sys.exit("ARRET PB-1 : %s ne repond pas au canon %s (lu %s)" % (nom, canon, h))
    spec = importlib.util.spec_from_file_location("banc_v8", a.instrument); banc = importlib.util.module_from_spec(spec); spec.loader.exec_module(banc)
    import numpy as np
    temoin_np = float((np.array([TEMOIN_X]) ** 6)[0]).hex()
    LOG("PLATEFORME", "python %s ; numpy %s ; %s ; NPY_DISABLE_CPU_FEATURES=%r ; TEMOIN tableau %s (%s)" % (sys.version.split()[0], np.__version__, platform.platform(), os.environ.get("NPY_DISABLE_CPU_FEATURES", ""), temoin_np, "noyau SIMD" if temoin_np.endswith("9c5p+64") else "CR"))
    W1 = banc.W1; g = banc.G_REF
    def pow_numpy(x, y): return float((np.array([x]) ** y)[0])
    def pow_py(x, y): return x ** y
    res = {"cellules": {}, "temoin_arrondi": temoin_np}
    for p in (4, 5, 7):
        for w2 in (1.73, 2.27, 2.80):
            al = float(banc.alpha_de(p)); A = banc.A_de(p); td, tc, dt2 = banc.tau_dom(w2), banc.tau_cap(w2), banc.dt2_de(w2); tau0 = banc.K_BASC * td; y_state = p - 1
            def jumeau(dt, pow_state, journal=None):
                delta = w2 * w2 - W1 * W1
                def f(tau):
                    u = pow_py(tau, -al - 2); v = pow_py(tau, -al)
                    return A * ((1 + w2 * w2) * al * (al + 1) * u + w2 * w2 * v)
                def acc_t(a1, a2, t):
                    s = a1 + a2; pw = pow_state(s, y_state)
                    if journal is not None: journal.append((i_pas[0], etage[0], s, pw))
                    base = g * pw; Fz = f(0.0 - t)
                    return -W1 * W1 * a1 + (base + Fz) / delta, -w2 * w2 * a2 - (base + Fz) / delta
                x1, x2, v1, v2 = banc.vers_composantes(*banc.xm_et_derivees(p, tau0), w2); t0 = -tau0
                X1, X2 = [x1], [x2]; i_pas, etage = [0], [0]; n = 0
                while True:
                    n += 1; i_pas[0] = n; t = t0 + n * dt; tp = t0 + (n - 1) * dt
                    etage[0] = 1; k1v1, k1v2 = acc_t(x1, x2, tp); k1x1, k1x2 = v1, v2
                    etage[0] = 2; k2v1, k2v2 = acc_t(x1 + .5 * dt * k1x1, x2 + .5 * dt * k1x2, tp + .5 * dt); k2x1, k2x2 = v1 + .5 * dt * k1v1, v2 + .5 * dt * k1v2
                    etage[0] = 3; k3v1, k3v2 = acc_t(x1 + .5 * dt * k2x1, x2 + .5 * dt * k2x2, tp + .5 * dt); k3x1, k3x2 = v1 + .5 * dt * k2v1, v2 + .5 * dt * k2v2
                    etage[0] = 4; k4v1, k4v2 = acc_t(x1 + dt * k3x1, x2 + dt * k3x2, tp + dt); k4x1, k4x2 = v1 + dt * k3v1, v2 + dt * k3v2
                    x1 = x1 + dt / 6 * (k1x1 + 2 * k2x1 + 2 * k3x1 + k4x1); x2 = x2 + dt / 6 * (k1x2 + 2 * k2x2 + 2 * k3x2 + k4x2)
                    v1 = v1 + dt / 6 * (k1v1 + 2 * k2v1 + 2 * k3v1 + k4v1); v2 = v2 + dt / 6 * (k1v2 + 2 * k2v2 + 2 * k3v2 + k4v2)
                    X1.append(x1); X2.append(x2)
                    if 0.0 - t <= tc * (1.0 + 1e-12): break
                return X1, X2
            cle = "%d|%.2f" % (p, w2); resc = {}
            for k, nom in ((0, "dt2"), (1, "dt2/2")):
                dt = dt2 / 2 ** k
                etat = banc.vers_composantes(*banc.xm_et_derivees(p, tau0), w2)
                ph = banc.phase2_pu(w2, p, etat, -tau0, dt, forcage=banc.forcage_de(p, w2), tau_star=0.0, tau_fin=tc)
                X1i, X2i = [float(v) for v in ph["x1"]], [float(v) for v in ph["x2"]]
                jr = []; X1, X2 = jumeau(dt, pow_numpy, jr)
                fidele = len(X1) == len(X1i) and all(u == v for u, v in zip(X1, X1i)) and all(u == v for u, v in zip(X2, X2i))
                durs = [(i, (ip, et, s, pw)) for i, (ip, et, s, pw) in enumerate(jr, 1) if pow_cr(s, y_state) != pw]
                X1c, X2c = jumeau(dt, pow_cr)
                x_fin = X1[-1] + X2[-1]; ulp_x1 = math.ulp(X1[-1]); dx_cr = ((X1c[-1] + X2c[-1]) - x_fin) / ulp_x1
                basc = 0; details = []
                for (cible, (ip, et, s, pw)) in durs:
                    compteur = [0]
                    def pow_patch(x, y):
                        compteur[0] += 1
                        return pow_cr(x, y) if compteur[0] == cible else pow_numpy(x, y)
                    X1p, X2p = jumeau(dt, pow_patch); dp = ((X1p[-1] + X2p[-1]) - x_fin) / ulp_x1
                    if dp != 0: basc += 1; details.append({"appel": cible, "pas": ip, "etage": et, "x_hex": hexf(s), "delta_x_fin_ulp": dp})
                resc[nom] = {"n_pas": len(X1) - 1, "appels_K1": len(jr), "cas_durs_K1": len(durs), "bascules": basc, "bascules_detail": details,
                             "jumeau_bit_fidele": fidele, "x_fin_CR_moins_noyau_ulp": dx_cr}
                LOG("CELL-%s-%s" % (cle, nom), "fidele=%s appels K1=%d cas durs=%d (%.2f pour cent) bascules seules=%d ; tout CR : x_fin %+.1f ulp(x1)%s" % (fidele, len(jr), len(durs), 100.0 * len(durs) / len(jr), basc, dx_cr, "" if dx_cr == 0 else "  <-- LA CELLULE DIFFERE ENTRE NOYAU ET CR"))
            res["cellules"][cle] = resc
    res["duree_s"] = time.perf_counter() - t_debut
    banc.ecrire_ascii(os.path.join(a.sortie, "diagnostic_cellules_T2_machine1_v1.json"), banc.json_ascii(res))
    LOG("FIN", "%.1f s" % res["duree_s"])
    banc.ecrire_ascii(os.path.join(a.sortie, "diagnostic_cellules_T2_machine1_v1.log"), "\n".join(LOG.lignes) + "\n")

if __name__ == "__main__":
    main()
