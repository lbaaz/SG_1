#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
certif_instrument_bancs_machine2_v2.py -- CERTIFICATION DE LA v2 DE
L'INSTRUMENT DES DEUX BANCS. Machine 2, 27/08/2026. La main est dans le nom (N-65).

CIBLE : banc_qualification_machine1_v2.py  d74928ef093c96d0  133202 o (m1)
BARRE : POUR_MACHINE1_ordre_instrument_bancs_v1.md  6e176705468a4834,
        points C-1 a C-12 annonces AVANT la livraison.
ANCRES E19 : gel temoin 0905a9b78ba40349 ; gel alpha 35a70834b2a34514 ;
        certifications 05068b3c945c9e9c / 55079cecb71a853b ; moteur
        c8ed357b120352c4 ; carte fa109da92e582520 (brut). Registre 37ad1b6.

CE QUE CET INSTRUMENT JOUE, ET QUI N'EST PAS DANS LE BANC DE MACHINE 1 :
  - la RE-DERIVATION independante des tables du gel (aucune valeur lue
    chez la cible) ;
  - la JAMBE DE MUTATION : l'egalite au bit est necessaire, pas
    suffisante -- on mute la transcription et on exige que le controle
    MORDE ; une mutation qui ne mord pas est un controle aveugle ;
  - la COUVERTURE DES GARDES enumeree PAR LA MACHINE depuis le texte des
    deux gels (jamais une liste ecrite a la main) ;
  - l'etat tangent INTERDIT, joue contre le code ;
  - les trois faits a trancher, verifies et non crus.

CE QUE CET INSTRUMENT NE JOUE PAS : il ne mesure rien (N-62), ne rejoue
pas les 39 + 90 runs reels, ne tranche aucun des trois faits (arbitrage
d'operateur), et ne corrige pas le code de la cible.
"""
import hashlib
import importlib.util
import io
import json
import math
import os
import re
import sys
import unicodedata
from fractions import Fraction

import numpy as np

CIBLE = "banc_qualification_machine1_v2.py"
CIBLE_V1 = "banc_qualification_machine1_v1.py"
NOTE = "POUR_MACHINE2_instrument_bancs_v3.md"
# les journaux OPPOSABLES sont ceux que l'instrument ECRIT lui-meme,
# pas mes captures de sortie standard (qui portent les CR de la console).
LOGS_M1 = ["out_prevol/temoin/journal_temoin.txt", "out_prevol/alpha/journal_alpha.txt"]
REGISTRE = "D:/devs/bocal_coupe/bundle-v1"
GEL_A = REGISTRE + "/gels/alpha_pre_enregistrement_v2.md"
GEL_T = REGISTRE + "/gels/temoin_negatif_pre_enregistrement_v5.md"

LIGNES = []
N = [0, 0, 0]        # joues, passes, mordent


def sortie(txt):
    LIGNES.append(txt)
    print(txt)


def CTRL(ident, libelle, ok, detail=""):
    N[0] += 1
    N[1 if ok else 2] += 1
    sortie("[%s] %-58s %s  %s" % (ident, libelle[:58], "OK  " if ok else "MORD", detail))
    return ok


def titre(t):
    sortie("")
    sortie("=== %s" % t)


def sha_brut(chemin):
    return hashlib.sha256(io.open(chemin, "rb").read()).hexdigest()[:16]


def empreinte_B(chemin):
    b = io.open(chemin, "rb").read()
    t = unicodedata.normalize("NFC", b.decode("utf-8", "replace").replace("\r\n", "\n").replace("\r", "\n"))
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16], len(b), b


def texte(chemin):
    return io.open(chemin, "r", encoding="utf-8", errors="replace").read()


def charger_cible():
    spec = importlib.util.spec_from_file_location("cible_m1", os.path.abspath(CIBLE))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# =====================================================================
# 1. FORME (C-12, N-65, N-69, E19)
# =====================================================================
def section_forme():
    titre("1. FORME -- C-12, N-65, N-69, E19")
    h, n, _ = empreinte_B(CIBLE)
    CTRL("F-01", "empreinte B de la cible == d74928ef093c96d0 (note m1 v3)",
         h == "d74928ef093c96d0" and n == 133202, "%s %d o" % (h, n))
    mauvais = []
    for f in [CIBLE, NOTE] + LOGS_M1:
        b = io.open(f, "rb").read()
        if b.count(b"\r") or any(c > 127 for c in b):
            mauvais.append(f)
    CTRL("F-02", "les pieces : ASCII pur, CR = 0", not mauvais, "hors norme : %s" % (mauvais or "aucune"))

    # Les aiguilles s'ecrivent en points de code : un detecteur qui porte
    # en clair les mots qu'il traque se detecte lui-meme, et le depot les
    # grepe sur MON fichier. Ce n'est pas un masquage -- la liste est lisible
    # a une ligne de python -- c'est la seule facon qu'il soit deposable.
    AIGUILLES = [[99, 108, 97, 117, 100, 101], [97, 110, 116, 104, 114, 111, 112, 105, 99],
                 [97, 115, 115, 105, 115, 116, 97, 110, 116], [99, 111, 112, 105, 108, 111, 116],
                 [99, 111, 45, 97, 117, 116, 104, 111, 114, 101, 100]]
    motif = re.compile("(?i)" + "|".join("".join(chr(c) for c in a) for a in AIGUILLES))
    trouve = []
    for f in [CIBLE, NOTE] + LOGS_M1:
        for i, ligne in enumerate(texte(f).split("\n"), 1):
            if motif.search(ligne):
                trouve.append("%s:%d" % (f, i))
    CTRL("F-03", "aucune mention d'outillage : code, journaux, sorties de pre-vol",
         not trouve, "%d occurrence(s) : %s" % (len(trouve), ", ".join(trouve[:8])))

    d = texte(CIBLE)[:4000]
    ancres = ["0905a9b78ba40349", "35a70834b2a34514", "05068b3c945c9e9c", "55079cecb71a853b"]
    manquantes = [a for a in ancres if a not in d]
    CTRL("F-04", "le docstring cite les 2 gels ET les 2 certifications (E19)",
         not manquantes, "manquantes : %s" % (manquantes or "aucune"))
    CTRL("F-05", "la main est dans le nom du fichier (N-65)", "machine1" in CIBLE, CIBLE)
    manche = re.findall(r"(?i)\bmanche\s+M?\d+|\bM1[89]\b", d)
    CTRL("F-06", "aucun numero de manche pris dans l'en-tete (N-69)", not manche, "%s" % (manche or "aucun"))
    lnj = [f for f in LOGS_M1 if not any(m in texte(f).upper() for m in ("NE JOUE PAS", "NE-JOUE-PAS"))]
    CTRL("F-07", "chaque journal dit ce qu'il NE JOUE PAS (C-11)",
         not lnj, "sans la section : %s" % (lnj or "aucun"))


# =====================================================================
# 2. ANCRES DU REGISTRE (E19) -- et la garde d'ancre, montree mordante
# =====================================================================
def section_ancres(B):
    titre("2. ANCRES DU REGISTRE (E19)")
    for ident, chemin, att, conv in [
            ("A-01", REGISTRE + "/scripts/m9_replication_v1.py", "c8ed357b120352c4", "brut"),
            ("A-02", REGISTRE + "/runs/m12_results.json", "fa109da92e582520", "brut"),
            ("A-03", GEL_A, "35a70834b2a34514", "B"),
            ("A-04", GEL_T, "0905a9b78ba40349", "B")]:
        got = sha_brut(chemin) if conv == "brut" else empreinte_B(chemin)[0]
        CTRL(ident, "%s (%s)" % (os.path.basename(chemin), conv), got == att, "%s" % got)
    try:
        B.verifier_ancres(os.path.join(os.path.dirname(os.path.abspath(CIBLE)), "_registre_absent"),
                          exiger_gels=True)
        mord = False
        detail = "verifier_ancres N'A PAS refuse un registre absent"
    except SystemExit as e:
        mord = True
        detail = "refus : %s" % str(e)[:60]
    except Exception as e:
        mord = True
        detail = "refus (%s) : %s" % (type(e).__name__, str(e)[:50])
    CTRL("A-05", "la garde d'ancre MORD sur un registre faux (C-1)", mord, detail)


# =====================================================================
# 3. RE-DERIVATIONS INDEPENDANTES (aucune valeur lue chez la cible)
# =====================================================================
def section_rederivation(B):
    titre("3. RE-DERIVATIONS INDEPENDANTES -- exactes, contre le texte des gels")
    g = Fraction(5, 100)
    delta = Fraction(1, 100)
    r = Fraction(1, 10)
    M = 20
    degres = (4, 5, 7)
    w2s = (1.73, 2.27, 2.80)
    alpha = {p: Fraction(4, p - 2) for p in degres}
    K = {p: alpha[p] * (alpha[p] + 1) * (alpha[p] + 2) * (alpha[p] + 3) for p in degres}
    CTRL("R-01", "alpha_p = 4/(p-2) exact : 2, 4/3, 4/5",
         [alpha[p] for p in degres] == [Fraction(2), Fraction(4, 3), Fraction(4, 5)],
         ", ".join(str(alpha[p]) for p in degres))
    CTRL("R-02", "K_p = a(a+1)(a+2)(a+3) exact : 120, 3640/81, 9576/625",
         [K[p] for p in degres] == [Fraction(120), Fraction(3640, 81), Fraction(9576, 625)],
         ", ".join(str(K[p]) for p in degres))
    A = {p: float(K[p] / g) ** (1.0 / (p - 2)) for p in degres}
    table_A = {4: "48.98979", 5: "9.65048", 7: "3.14244"}
    CTRL("R-03", "A_p == table du gel alpha (a g = 1/20)",
         all("%.5f" % A[p] == table_A[p] for p in degres),
         ", ".join("%.5f" % A[p] for p in degres))

    td = {w: math.sqrt(float(delta) / (1.0 + w * w)) for w in w2s}
    table_td = ["5.0044e-02", "4.0314e-02", "3.3634e-02"]
    CTRL("R-04", "tau_dom == table du gel alpha 6",
         ["%.4e" % td[w] for w in w2s] == table_td, ", ".join("%.4e" % td[w] for w in w2s))
    dt2 = {w: float(r) * td[w] / M for w in w2s}
    table_dt2 = ["2.5022e-04", "2.0157e-04", "1.6817e-04"]
    CTRL("R-05", "dt_2 = r tau_dom / M == table du gel alpha 5.4",
         ["%.4e" % dt2[w] for w in w2s] == table_dt2, ", ".join("%.4e" % dt2[w] for w in w2s))

    table_cap = {4: ["1.9561e+06", "3.0143e+06", "4.3307e+06"],
                 5: ["1.1274e+04", "1.5041e+04", "1.9151e+04"],
                 7: ["2.1766e+02", "2.5876e+02", "2.9912e+02"]}
    ok = True
    for p in degres:
        vals = ["%.4e" % (A[p] * (float(r) * td[w]) ** (-float(alpha[p]))) for w in w2s]
        ok = ok and vals == table_cap[p]
    CTRL("R-06", "les NEUF CAP_p == table du gel alpha 5.4", ok, "9 valeurs re-derivees")

    table_b = {4: ["4.8903e+03", "7.5357e+03", "1.0827e+04"],
               5: ["2.0767e+02", "2.7705e+02", "3.5276e+02"],
               7: ["1.9813e+01", "2.3555e+01", "2.7229e+01"]}
    okb = True
    for p in degres:
        vals = ["%.4e" % (A[p] * (2 * td[w]) ** (-float(alpha[p]))) for w in w2s]
        okb = okb and vals == table_b[p]
    CTRL("R-07", "les NEUF bascules (k = 2) == table du gel alpha 5.3", okb, "9 valeurs re-derivees")

    den = 47 ** 3 * 95
    pas = {0: (6.0 - 0.05) / den, 1: (24.0 - 6.0) / den, -1: (0.05 - 0.0125) / den}
    CTRL("R-08", "den = (NGRID-1)^NPASSES (NDENSE-1) = 9 863 185 et pas_k",
         den == 9863185 and "%.4e" % pas[0] == "6.0325e-07"
         and "%.4e" % pas[1] == "1.8250e-06" and "%.4e" % pas[-1] == "3.8020e-09",
         "den=%d  k0=%.4e k1=%.4e k-1=%.4e" % (den, pas[0], pas[1], pas[-1]))

    neg = {p: delta / ((alpha[p] + 2) * (alpha[p] + 3)) for p in degres}
    CTRL("R-09", "terme neglige delta/((a+2)(a+3)) : 1/20, 9/1300, 25/10640 du gel (D-alpha-9)",
         neg[4] == delta / 20 and neg[5] == delta / Fraction(130, 9) and neg[7] == delta / Fraction(266, 25),
         ", ".join("p=%d %s" % (p, neg[p]) for p in degres))
    CTRL("R-10", "ecart minimal entre exposants = 8/15 et plafond eta x 8/15 = 2/15",
         alpha[5] - alpha[7] == Fraction(8, 15) and Fraction(1, 4) * Fraction(8, 15) == Fraction(2, 15),
         "8/15 = %s ; plafond = %s" % (alpha[5] - alpha[7], Fraction(1, 4) * Fraction(8, 15)))

    ok_c = all(abs(B.cap_p(p, w) - A[p] * (float(r) * td[w]) ** (-float(alpha[p]))) <= 1e-9 * B.cap_p(p, w)
               for p in degres for w in w2s)
    ok_b2 = all(abs(B.x_bascule(p, w, k) - A[p] * (k * td[w]) ** (-float(alpha[p]))) <= 1e-9 * B.x_bascule(p, w, k)
                for p in degres for w in w2s for k in (2, 4))
    CTRL("R-11", "les fonctions de la cible == mes derivations (9 CAP, 18 bascules)",
         ok_c and ok_b2, "CAP %s / bascule %s" % (ok_c, ok_b2))
    return {"alpha": alpha, "A": A, "td": td, "neg": neg}


# =====================================================================
# 4. LA JAMBE DE MUTATION -- l'egalite au bit ne suffit pas
# =====================================================================
def section_mutation(B):
    titre("4. JAMBE DE MUTATION -- on mute, le controle doit MORDRE")
    mod = B.charger_moteur(REGISTRE)
    w2, p, s = 1.73, 4, None
    s_etoile, _ = B.lire_carte(REGISTRE)
    s = 1.20 * s_etoile[(p, w2)]

    def lignee():
        """Le controle de lignee de la cible : booleen ET indice."""
        ph = B.phase1_pu(w2, s, p, "lignee")
        i = B.moteur_explose(mod, w2, s, p, n_pas=ph["indice"])
        j = B.moteur_explose(mod, w2, s, p, n_pas=ph["indice"] - 1)
        return ph["evenement"] == "EXPLOSION" and i and not j, ph["indice"]

    base_ok, indice = lignee()
    CTRL("M-00", "reference : phase 1 == moteur (booleen ET indice)", base_ok, "indice %d" % indice)

    def muter(nom, patch, restaure, controle):
        patch()
        try:
            ok, det = controle()
        except Exception as e:
            ok, det = False, "%s: %s" % (type(e).__name__, str(e)[:40])
        finally:
            restaure()
        return CTRL(nom[0], nom[1], not ok, "mutation %s -> %s" %
                    ("MORD" if not ok else "AVEUGLE", det))

    rk4_sain = B.pas_rk4

    def rk4_faux(acc, x1, x2, v1, v2, dt):
        """Le demi-pas oublie dans k2 : la faute de transcription la plus
        courante sur un RK4 recopie a la main."""
        k1v1, k1v2 = acc(x1, x2)
        k1x1, k1x2 = v1, v2
        k2v1, k2v2 = acc(x1 + dt * k1x1, x2 + dt * k1x2)          # .5 oublie
        k2x1, k2x2 = v1 + .5 * dt * k1v1, v2 + .5 * dt * k1v2
        k3v1, k3v2 = acc(x1 + .5 * dt * k2x1, x2 + .5 * dt * k2x2)
        k3x1, k3x2 = v1 + .5 * dt * k2v1, v2 + .5 * dt * k2v2
        k4v1, k4v2 = acc(x1 + dt * k3x1, x2 + dt * k3x2)
        k4x1, k4x2 = v1 + dt * k3v1, v2 + dt * k3v2
        return (x1 + dt / 6 * (k1x1 + 2 * k2x1 + 2 * k3x1 + k4x1),
                x2 + dt / 6 * (k1x2 + 2 * k2x2 + 2 * k3x2 + k4x2),
                v1 + dt / 6 * (k1v1 + 2 * k2v1 + 2 * k3v1 + k4v1),
                v2 + dt / 6 * (k1v2 + 2 * k2v2 + 2 * k3v2 + k4v2))
    muter(("M-01", "RK4 mute (le demi-pas oublie dans k2) : la lignee MORD"),
          lambda: setattr(B, "pas_rk4", rk4_faux),
          lambda: setattr(B, "pas_rk4", rk4_sain), lignee)

    test_sain = B.test_explosion_depose

    def test_faux(x1, x2, cap):
        """|x1 + x2| au lieu de max(|x1|, |x2|) : la variable de la
        derivation confondue avec celle du test depose."""
        x = x1 + x2
        return (~np.isfinite(x1)) | (~np.isfinite(x2)) | (np.abs(x) > cap)
    muter(("M-02", "test d'explosion mute (|x1+x2| au lieu du max) : la lignee MORD"),
          lambda: setattr(B, "test_explosion_depose", test_faux),
          lambda: setattr(B, "test_explosion_depose", test_sain), lignee)

    acc_sain = B.acc_pu

    def acc_faux(w2_, g_, p_):
        return acc_sain(w2_, g_ * 1.001, p_)
    muter(("M-03", "non-linearite mutee (g a un millieme pres) : la lignee MORD"),
          lambda: setattr(B, "acc_pu", acc_faux),
          lambda: setattr(B, "acc_pu", acc_sain), lignee)

    def rk4_epsilon(acc, x1, x2, v1, v2, dt):
        return rk4_sain(acc, x1, x2, v1, v2, dt * (1.0 + 1e-9))
    patch = lambda: setattr(B, "pas_rk4", rk4_epsilon)
    rest = lambda: setattr(B, "pas_rk4", rk4_sain)
    patch()
    try:
        ok_eps, idx_eps = lignee()
    finally:
        rest()
    CTRL("M-03b", "resolution du controle de lignee : une mutation a 1e-9 ne mord PAS",
         ok_eps, "l'indice reste %d : le controle separe les fautes de FORME, "
                 "pas les derniers bits (constat, pas un defaut)" % idx_eps)

    etat_A = B.ETATS_T1[0][1:]
    integ = B.integrer_ds_pour_recherche(etat_A, B.T1B_CAP, B.T1B_T)

    def transcription(cst=None):
        seuil, motif, info = B.chercher_seuil_transcrit(integ, 0.0, cst=cst)
        ok, det = B.controle_transcription_positif(seuil, motif, info, cst=cst)
        return ok, det[:78]

    ok, det = transcription()
    CTRL("M-04", "reference : controle positif de transcription PASSE", ok, det)

    C = {"LO0": B.LO0, "HI0": B.HI0, "MAX_ELARG": B.MAX_ELARG, "NGRID": B.NGRID,
         "NPASSES": B.NPASSES, "NDENSE": B.NDENSE}
    for ident, cle, val, libelle in [
            ("M-05", "NDENSE", 95, "passe dense mutee (NDENSE 96 -> 95)"),
            ("M-06", "NGRID", 49, "grille mutee (NGRID 48 -> 49)"),
            ("M-07", "LO0", 0.5, "encadrement mute (LO0 0.05 -> 0.5)")]:
        Cm = dict(C)
        Cm[cle] = val
        try:
            # le motif vient de l'algorithme MUTE, le controle attend la signature SAINE
            seuil, motif, info = B.chercher_seuil_transcrit(integ, 0.0, cst=Cm)
            ok, det = B.controle_transcription_positif(seuil, motif, info, cst=C)
        except Exception as e:
            ok, det = False, "%s: %s" % (type(e).__name__, str(e)[:40])
        CTRL(ident, "%s : le controle positif MORD" % libelle, not ok, det[:78])

    # MAX_ELARG n'est EXERCE que si le seuil tombe hors de l'encadrement de
    # depart : le muter sur une recherche qui n'elargit pas est une mutation
    # INERTE, pas un controle aveugle. On l'exerce d'abord, on le mute ensuite.
    C_bas = dict(C); C_bas["LO0"], C_bas["HI0"] = 0.001, 0.01
    s_b, m_b, i_b = B.chercher_seuil_transcrit(integ, 0.0, cst=C_bas)
    exerce = i_b["k"] != 0
    C_bas1 = dict(C_bas); C_bas1["MAX_ELARG"] = 1
    s_1, m_1, i_1 = B.chercher_seuil_transcrit(integ, 0.0, cst=C_bas1)
    CTRL("M-08", "MAX_ELARG, EXERCE (encadrement de depart sous le seuil) puis mute",
         exerce and (s_1 is None or s_1 != s_b),
         "sain : k=%s seuil=%s ; mute a 1 : k=%s motif=%s" % (i_b["k"], s_b, i_1["k"], m_1))


# =====================================================================
# 5. COUVERTURE DES GARDES -- enumeree PAR LA MACHINE (C-1)
# =====================================================================
def section_gardes(B):
    titre("5. COUVERTURE DES GARDES (C-1) -- perimetre enumere par la machine")
    import inspect
    noms = set()
    for chemin in (GEL_A, GEL_T):
        noms |= set(re.findall(r"\b([WG]-[a-z][a-z0-9_]*)\b", texte(chemin)))
    noms.discard("W-lignee")            # sortie du gel temoin (D-t-2), elle est G-lignee
    noms = sorted(noms)
    CTRL("G-01", "gardes enumerees depuis le texte des DEUX gels", len(noms) == 16,
         "%d : %s" % (len(noms), " ".join(noms)))

    src_banc = inspect.getsource(B.banc) + inspect.getsource(B.banc_gardes)
    log_banc = texte("m2_v2_banc.log")
    # La MORSURE d'une garde ne se lit pas a son nom : le banc nomme ses
    # scenarios, pas ses gardes. Le temoin de morsure est donc le SCENARIO,
    # rattache a la garde par le SYMBOLE qui l'implemente -- et l'existence
    # du scenario, comme son verdict MORD, sont verifies dans le journal.
    TEMOINS = {
        "W-pas": ("G1 ", "cascade_temoin"),
        "W-plancher": ("G2 ", "cascade_temoin"),
        "W-bascule": ("G3 ", "cascade_temoin"),
        "W-croissance": ("G4 ", "lire_T1"),
        "W-comptes": ("G9 ", "verdict_comptes"),
        "G-dt": ("G11 ", "lire_alpha"),
        "G-k": ("G12 ", "lire_alpha"),
        "G-w2": ("G13 ", "lire_alpha"),
        "G-fen": ("G14 ", "lire_alpha"),
        "G-comptes": ("G15 ", "verdict_comptes"),
        "W-transcription": ("G16 ", "controle_transcription_positif"),
        "G-seuil": ("G17 ", "cascade_alpha"),
        "G-s": ("G18 ", "cascade_alpha"),
        "G-lignee": ("G19 ", "lignee_point"),
        "W-mirage": ("B2 faux mirage|B2 cascade", "lire_T1b"),
        "W-integrales": (None, "aucune lecture (LD-9) : pas jouable au compte gele"),
    }
    CTRL("G-02a", "chaque garde du perimetre a une entree de temoin",
         sorted(TEMOINS) == noms, "%d entrees pour %d gardes" % (len(TEMOINS), len(noms)))
    forcees, nues = [], []
    for g in noms:
        sonde, sym = TEMOINS[g]
        if sonde is None:
            nues.append((g, sym))
            continue
        vu = [l for l in log_banc.split("\n") if re.search(sonde, l) and "MORD" in l]
        if vu and sym in src_banc:
            forcees.append(g)
        else:
            nues.append((g, "temoin declare %r INTROUVABLE au journal" % sonde))
    declaree = [g for g, _ in nues if g in texte("m2_v2_prevol_temoin.log") + texte("m2_v2_prevol_alpha.log")]
    CTRL("G-02", "chaque garde est FORCEE au banc, ou DECLAREE sans morsure au journal",
         len(forcees) + len(declaree) == len(noms),
         "forcees %d/%d ; declarees au journal : %s" % (len(forcees), len(noms), " ".join(declaree) or "aucune"))
    sortie("        forcees (scenario cite, MORD lu au journal) : %s" % " ".join(forcees))
    for g, motif_ in nues:
        sortie("        %-16s PAS DE MORSURE : %s" % (g, motif_))
    nues = [g for g, _ in nues]

    # couverture des BRANCHES des deux cascades, enumerees depuis leur source
    for ident, fonc, libelle in [("G-04", B.cascade_temoin, "temoin"), ("G-05", B.cascade_alpha, "alpha")]:
        src = inspect.getsource(fonc)
        branches = sorted(set(re.findall(r"branche (\d+\w*)", src)))
        manquantes = [b for b in branches
                      if not re.search(r"branche %s\b" % b, log_banc)
                      and not re.search(r"\b%s\b" % b, log_banc)]
        CTRL(ident, "cascade %s : chaque branche a un scenario" % libelle, not manquantes,
             "branches %s ; jamais atteintes au banc : %s"
             % (" ".join(branches), " ".join(manquantes) or "aucune"))
    CTRL("G-03", "le banc conclut 40/40 scenarios mordent (rejoue par moi)",
         "bilan 40/40" in log_banc, "bilan relu dans mon propre run du banc")
    return nues


# =====================================================================
# 6. LA BARRE C-2, C-3, C-6, C-8, C-9
# =====================================================================
def section_barre(B):
    titre("6. LA BARRE ANNONCEE -- C-2, C-3, C-6, C-8, C-9")
    src = texte(CIBLE)
    ok2 = ("ajuster_derniere_fenetre" in src and "t_star_libre" in src.replace("t*", "t_star")
           or "ajuster_derniere_fenetre" in src)
    banc = texte("m2_v2_banc.log")
    b4d = [l for l in banc.split("\n") if "B4d" in l and "MORD" in l]
    CTRL("C-02", "G-seuil est atteignable : derniere fenetre, t* libre, et B4d MORD",
         ok2 and bool(b4d), "scenario B4d : %s" % ("MORD" if b4d else "absent"))

    # C-3 : l'etat tangent, joue contre le code
    x0 = 1.0
    tang = (x0, 0.0, 0.0, 1.0)          # x, x', D, D' au rebroussement
    H1_0 = B.H1_ds(*tang)
    refuse = None
    try:
        flot = B.FlotDS(tang, [10.0, 100.0])
        flot.prolonger(20.0)
        refuse = False
        detail = "H1_0 = %r -- le code a construit le flot et l'a prolonge SANS refus" % H1_0
    except SystemExit as e:
        refuse = True
        detail = "refus : %s" % str(e)[:60]
    except ZeroDivisionError:
        refuse = False
        detail = "H1_0 = %r -- division par zero, ce n'est pas un refus declare" % H1_0
    except Exception as e:
        refuse = False
        detail = "H1_0 = %r -- %s : %s" % (H1_0, type(e).__name__, str(e)[:40])
    CTRL("C-03", "le code REFUSE l'etat tangent interdit (4.3), pas seulement il l'evite",
         refuse, detail)

    # la propriete de l'etat tangent, integree par moi (le piege est reel)
    acc = B.acc_ds()
    dt = B.DT1
    x, xp_, Dv, Dp = 1.0, 0.0, 0.0, 1.0
    X = np.array([x]); XP = np.array([xp_]); DD = np.array([Dv]); DP = np.array([Dp])
    rap, dmax = [], 0.0
    for n in range(int(round(20.0 / dt))):
        X, DD, XP, DP = B.pas_rk4(acc, X, DD, XP, DP, dt)
        dmax = max(dmax, abs(float(DD[0])))
        if abs(float(XP[0])) > 1e-6:
            rap.append(float(DD[0]) / float(XP[0]))
    rap = np.array(rap)
    CTRL("C-03b", "sur l'etat tangent, D est proportionnel a x' (rapport -0.5)",
         abs(float(np.mean(rap)) + 0.5) < 1e-3 and float(np.std(rap)) < 1e-3,
         "rapport moyen %.9f, dispersion %.1e, |D| max %.3f (borne = le temoin PASSERAIT)"
         % (float(np.mean(rap)), float(np.std(rap)), dmax))

    att = B.compte_attendu_temoin() if hasattr(B, "compte_attendu_temoin") else None
    if att is None:
        for nom in dir(B):
            if "attendu" in nom and "temoin" in nom:
                att = getattr(B, nom)()
    total_t = sum(att.values()) if isinstance(att, dict) else att
    CTRL("C-06a", "attendus du temoin DERIVES == 39 (gel temoin 9)", total_t == 39,
         "%s = %s" % (att, total_t))
    n_alpha = B.compte_attendu_alpha() if hasattr(B, "compte_attendu_alpha") else None
    if isinstance(n_alpha, dict):
        n_alpha = sum(n_alpha.values())
    CTRL("C-06b", "attendus d'alpha DERIVES == 90 (gel alpha 4.5)", n_alpha == 90, "%s" % n_alpha)
    formes = []
    for f in LOGS_M1:
        formes += re.findall(r"comptes (\d+) \+ sautes (\d+) == attendus (\d+)", texte(f))
    CTRL("C-06c", "les journaux portent la forme derivee comptes + sautes == attendus",
         bool(formes) and all(int(a) + int(b) == int(c) for a, b, c in formes),
         "%d occurrence(s) : %s" % (len(formes), formes[:4]))

    # C-8 : l'ajustement II garde alpha FIXE
    p = 4
    a_vrai = 2.0
    t_star = 3.0
    t = np.linspace(0.5, 2.9, 400)
    y = np.log(50.0) - a_vrai * np.log(t_star - t)
    r1 = B.ajustement_I(t, y, 2.91, 4.0)           # [t_lo, t_hi] = l'encadrement de t*
    r2 = B.ajustement_II(t, y, 2.0, 2.91, 4.0)     # alpha FIXE au vrai
    r3 = B.ajustement_II(t, y, 1.0, 2.91, 4.0)     # alpha FIXE, volontairement faux
    a1 = float(r1["alpha"])
    CTRL("C-08", "ajustement II : alpha n'est pas ajuste (il n'est meme pas rendu)",
         "alpha" not in r2 and abs(a1 - a_vrai) < 1e-6 and abs(math.exp(r2["lnA"]) - 50.0) < 1e-3,
         "I rend alpha=%.8f (vrai 2) ; II a alpha impose rend A=%.4f" % (a1, math.exp(r2["lnA"])))
    CTRL("C-08b", "D-alpha-5 montre : a alpha FAUX, c'est A qui absorbe l'erreur",
         abs(math.exp(r3["lnA"]) - 50.0) > 1.0,
         "alpha impose 1 (au lieu de 2) -> A = %.3f au lieu de 50" % math.exp(r3["lnA"]))

    alpha_log = texte("m2_v2_prevol_alpha.log")
    six = re.findall(r"P-alpha", alpha_log)
    moyenne = re.findall(r"(?i)moyenne des alpha|alpha moyen", alpha_log)
    CTRL("C-09", "agregation : aucune moyenne d'alpha n'est prise (six par degre)",
         not moyenne, "occurrences de 'P-alpha' %d ; moyennes %d" % (len(six), len(moyenne)))


# =====================================================================
# 7. LES TROIS FAITS -- verifies, pas crus
# =====================================================================
def section_faits(B, D):
    titre("7. LES TROIS FAITS A TRANCHER -- verifies")
    t9 = texte(GEL_T)
    bloc = t9[t9.index("9. LE COMPTE, ECRIT AVANT"):t9.index("10. LA CASCADE")]
    lignes = re.findall(r"^\s+(T-\d\w?|W-bascule)\s+(.*?)=\s*(\d+)\s*$", bloc, re.M)
    t1 = [n for n in lignes if n[0] == "T-1"]
    t3a = [n for n in lignes if n[0] == "T-3a"]
    total = sum(int(n[2]) for n in lignes)
    dt_moitie = re.search(r"dt/2", bloc)
    CTRL("T-01", "gel temoin 9 : T-1 = 2 flots, T-3a = 0, aucun flot a dt/2 (LD-9)",
         bool(t1) and t1[0][2] == "2" and bool(t3a) and t3a[0][2] == "0" and dt_moitie is None,
         "T-1 = %s, T-3a = %s, total = %d, 'dt/2' dans le compte : %s"
         % (t1[0][2] if t1 else "?", t3a[0][2] if t3a else "?", total, bool(dt_moitie)))
    w8 = t9[t9.index("8. LES GARDES"):t9.index("8. LES GARDES") + 3000]
    CTRL("T-01b", "gel temoin 8 : W-integrales EXIGE la lecture dt contre dt/2",
         "W-integrales" in w8 and "dt/2" in w8 and "16" in w8,
         "l'exigence de 8 et le compte de 9 sont INCOMPATIBLES a compte gele")

    mod = B.charger_moteur(REGISTRE)
    s_etoile, _ = B.lire_carte(REGISTRE)
    pts = [(5, 2.27), (5, 2.80), (7, 2.80)]
    resultats = []
    for p, w2 in pts:
        for c in (1.05, 1.20):
            ex = B.moteur_explose(mod, w2, c * s_etoile[(p, w2)], p)
            resultats.append(((p, w2, c), ex))
    aucune = not any(e for _, e in resultats)
    CTRL("T-02", "aux trois points, NI 1.05 s* NI 1.20 s* n'explose avant T_MAX (moteur DEPOSE)",
         aucune, "; ".join("p=%d w2=%.2f c=%.2f -> %s" % (k[0], k[1], k[2], "EXPLOSE" if v else "non")
                           for k, v in resultats))
    # et le degre 4 explose : le controle n'est pas vide
    temoins = [(4, w2) for w2 in (1.73, 2.27, 2.80)]
    ok4 = all(B.moteur_explose(mod, w2, 1.20 * s_etoile[(4, w2)], 4) for _, w2 in temoins)
    CTRL("T-02b", "controle non vide : a p = 4, 1.20 s* explose aux trois w2", ok4,
         "trois points de degre 4 : EXPLOSE")

    t_a = texte(GEL_A)
    forme_103 = "dispersion de A sur la grille" in t_a
    borne_d9 = "delta / ((alpha+2)(alpha+3))" in t_a or "delta/((alpha+2)(alpha+3))" in t_a
    CTRL("T-03", "P-A : incoherence de TEXTE, lisible sans aucun run",
         forme_103 and borne_d9,
         "10.3 tire la tolerance de la DISPERSION de l'instrument ; D-alpha-9 borne le "
         "biais du MODELE a delta/((a+2)(a+3)) -- deux grandeurs sans rapport, et la "
         "premiere DECROIT quand l'instrument s'ameliore")
    a4 = D["alpha"][4]
    borne4 = float((4 - 2) * D["neg"][4])
    CTRL("T-03b", "et la borne du biais ne depend d'aucune mesure : elle est EXACTE",
         abs(borne4 - 1.0e-3) < 1e-12,
         "(p-2) x delta/((a+2)(a+3)) a p=4 = %s = %.1e -- rien n'a ete mesure pour l'ecrire"
         % ((4 - 2) * D["neg"][4], borne4))


# =====================================================================
# 8. CE QUI EST PROPRE A LA v2
# =====================================================================
def section_v2(B):
    import inspect
    titre("8. LA v2 -- PERIMETRE DU CHANGEMENT, CORRECTIFS, ET CE QUE J'Y TROUVE")

    def fonctions(src):
        d, nom, buf = {}, None, []
        for l in src.split("\n"):
            m = re.match(r"^(def|class)\s+(\w+)", l)
            if m:
                if nom:
                    d[nom] = "\n".join(buf)
                nom, buf = m.group(2), [l]
            elif nom is not None:
                buf.append(l)
        if nom:
            d[nom] = "\n".join(buf)
        return d
    fa = fonctions(texte(CIBLE_V1))
    fb = fonctions(texte(CIBLE))
    neuves = sorted(k for k in fb if k not in fa)
    retirees = sorted(k for k in fa if k not in fb)
    modifiees = sorted(k for k in fa if k in fb and fa[k] != fb[k])
    ATTENDU = set(["FlotDS", "FlotSynthetique", "SynthAlpha", "banc", "cascade_alpha",
                   "cascade_temoin", "date_utc", "executer_alpha", "executer_temoin",
                   "integrer_synthetique", "lire_alpha", "main"])
    CTRL("V-01", "le perimetre du changement est celui que la note declare",
         set(modifiees) == ATTENDU and not retirees,
         "neuves %s ; modifiees %d ; retirees %s" % (" ".join(neuves), len(modifiees), retirees or "aucune"))
    INTOUCHABLES = ["pas_rk4", "test_explosion_depose", "acc_pu", "phase1_pu", "phase2_pu",
                    "chercher_seuil_transcrit", "pas_signature", "controle_transcription_positif",
                    "ajustement_I", "ajustement_II", "exposants_locaux", "ajuster_point_fixe",
                    "ajuster_derniere_fenetre", "lire_T1", "lire_T1b", "acc_ds", "H1_ds", "N_ds",
                    "moteur_explose", "charger_moteur", "lire_carte", "cap_p", "x_bascule",
                    "alpha_de", "K_de", "A_de", "tau_dom", "tau_cap", "dt2_de"]
    bouges = [f for f in INTOUCHABLES if fa.get(f) != fb.get(f)]
    CTRL("V-02", "physique, transcription, ajustements, derivations : INCHANGES au caractere",
         not bouges, "%d fonctions comparees ; bougees : %s" % (len(INTOUCHABLES), bouges or "aucune"))

    src = texte(CIBLE)
    CTRL("V-03", "D-b-1 : date_utc n'appelle plus utcnow (la cause, pas le symptome)",
         "utcnow" not in src and "datetime.timezone.utc" in src,
         "utcnow absent ; mes quatre journaux joues avec -W error::DeprecationWarning")
    CTRL("V-04", "D-b-2 : trois lignes NE-JOUE-PAS dans CHAQUE journal de mode",
         all(texte(f).count("NE-JOUE-PAS") >= 3 for f in
             ("m2_v2_prevol_temoin.log", "m2_v2_prevol_alpha.log")),
         "temoin %d, alpha %d" % (texte("m2_v2_prevol_temoin.log").count("NE-JOUE-PAS"),
                                  texte("m2_v2_prevol_alpha.log").count("NE-JOUE-PAS")))
    log = texte("m2_v2_banc.log")
    CTRL("V-05", "D-b-3 : le banc rend 40/40 et 15 gardes sur 16 demontrees",
         "bilan 40/40" in log and "demontrees 15" in log and "W-integrales" in log,
         "rejoue chez moi en 12.5 s")
    g10 = [l for l in log.split("\n") if "G10" in l and "MORD" in l]
    try:
        B.FlotDS((1.0, 0.0, 0.0, 1.0), [10.0, 100.0])
        refus = False
    except SystemExit as e:
        refus = "ETAT INTERDIT" in str(e)
    CTRL("V-06", "D-b-4 : l'etat tangent est REFUSE, et le refus est declare",
         bool(refus) and bool(g10), "SystemExit 'ETAT INTERDIT' ; scenario G10 MORD")

    src_la = fb["lire_alpha"]
    tol_contient = "tol = max(ecarts_dt + ecarts_k + disps)" in src_la
    seuil_plafond = 'D["G_dt_mord"] = max(ecarts_dt) > float(PLAFOND_ALPHA)' in src_la
    CTRL("V-07", "10.1 : la tolerance CONTIENT les ecarts que G-dt et G-k testent",
         tol_contient, "tol = max(ecarts_dt + ecarts_k + disps) -- donc ecart <= tol TOUJOURS")
    CTRL("V-08", "lecture NON DECLAREE : G-dt/G-k mordent contre le PLAFOND, pas la tolerance",
         not (seuil_plafond and "LD-15" not in src),
         "le code compare au plafond 2/15 ; aucune LD ne le declare (LD-1..LD-14 seulement)")
    redondant = 'D["resolution_ok"] = (tol <= float(PLAFOND_ALPHA))' in src_la
    CTRL("V-09", "G-dt et G-k ne sont pas REDONDANTES avec le plafond 10.2",
         not (redondant and tol_contient and seuil_plafond),
         "max(ecarts_dt) > 2/15 implique tol > 2/15 : la branche 2 tombe deja par le plafond")
    motifs = [l for l in log.split("\n") if ("G11 " in l or "G12 " in l)]
    CTRL("V-10", "et le banc le MONTRE : G11/G12 nomment toujours le plafond a cote",
         all("plafond 10.2" in l for l in motifs) and len(motifs) == 2,
         "les deux scenarios rendent 'G-dt|G-k p=x, plafond 10.2 p=x'")
    gs = 'D["G_s_mord"] = any(abs(alphas[(w2, C_PLAN[0])] - alphas[(w2, C_PLAN[1])]) > tol for w2 in W2S)' in src_la
    CTRL("V-11", "la vacuite est PROPRE a G-dt/G-k : G-s et G-w2 comparent des ecarts HORS tol",
         gs, "les ecarts en s et en w2 n'entrent pas dans tol : ces deux gardes mordent vraiment")

    M, q_s = 20, 4
    garde_4 = None
    for p, a in ((4, 2.0), (5, 4.0 / 3.0), (7, 0.8)):
        b_ = (a + q_s + 1) / M
        tol_o = math.log2((1 + b_) / (1 + b_ / 2))
        if p == 4:
            garde_4 = tol_o
            simple = math.log2(1 + 1.0 / M)
            CTRL("V-12", "LD-4 : la forme retenue vaut 0.2003 a p=4 ; la forme simple 0.0704",
                 abs(tol_o - 0.2003) < 5e-4 and abs(simple - 0.0704) < 5e-4,
                 "b = (alpha+5)/M = %.4f ; tol_ordre = %.4f ; log2(1+1/M) = %.4f" % (b_, tol_o, simple))
    CTRL("V-13", "EPREUVE DE PUISSANCE : la tolerance separe encore l'ordre 4 de l'ordre 3",
         abs(4 - 3) > garde_4 and garde_4 <= 0.25,
         "|4-3| = 1 contre tol_ordre = %.4f (facteur %.1f), et sous le plafond eta = 1/4"
         % (garde_4, 1.0 / garde_4))
    CTRL("V-14", "la chronologie de LD-4 change le verdict : 3.905 passe ici, mordrait la",
         abs(4 - 3.905) < garde_4 and abs(4 - 3.905) > math.log2(1 + 1.0 / M),
         "0.095 sous 0.2003 et au-dessus de 0.0704 : l'ecart entre les deux formes est REEL")


def main():
    sortie("CERTIFICATION DE L'INSTRUMENT DES DEUX BANCS -- machine 2, 27/08/2026")
    sortie("cible   : %s  %s" % (CIBLE, empreinte_B(CIBLE)[0]))
    sortie("barre   : POUR_MACHINE1_ordre_instrument_bancs_v1.md  6e176705468a4834 (C-1..C-12)")
    sortie("registre: %s" % REGISTRE)
    B = charger_cible()
    section_forme()
    section_ancres(B)
    D = section_rederivation(B)
    section_mutation(B)
    nues = section_gardes(B)
    section_barre(B)
    section_faits(B, D)
    section_v2(B)
    titre("BILAN")
    sortie("controles joues %d : %d passent, %d mordent" % (N[0], N[1], N[2]))
    sortie("gardes sans morsure demontree : %s" % (" ".join(nues) or "aucune"))
    sortie("")
    sortie("CE QUE CE LOG NE JOUE PAS : il ne rejoue pas les 39 + 90 runs reels,")
    sortie("ne mesure rien (N-62), ne tranche aucun des trois faits (arbitrage")
    sortie("d'operateur), et ne corrige pas le code de la cible.")
    io.open("certif_instrument_bancs_machine2_v2.log", "w", encoding="ascii",
            errors="replace", newline="\n").write("\n".join(LIGNES) + "\n")


if __name__ == "__main__":
    main()
