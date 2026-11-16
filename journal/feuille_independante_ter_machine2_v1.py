# -*- coding: ascii -*-
"""MA FEUILLE de jugement du gel E-B ter (432319b9feb34b82), ecrite du TEXTE du gel (sections 3.7, 3.8, 3.9, 6, 7, 8) par machine 2, 2026-11-15.
HONNETETE SUR L'INDEPENDANCE : j'avais lu la feuille de machine 1 (b2d6d7cfaf30f1cf) avant de l'ecrire ; elle est donc independante par
structure (exposants, rationnels partout, cascade par table, pas de dictionnaire intermediaire) et par construction (je ne la copie pas), pas par
ignorance. Elle ne juge que : plateau, etat, point, cascade, issue de la consigne (e), tenue de l'etage 0, des ancres, du temoin.
Pure bibliotheque (aucun calcul 2D). Importee par confrontation_feuilles_ter_machine2_v1.py."""
import math
from fractions import Fraction

K_BAS, K_HAUT = -3, 8
TAU = 0.05
SEUIL_PLATEAU = Fraction(21, 20)                 # 1 + 1/20, gel 3.8
NEUF_DIXIEMES = Fraction(9, 10)
JUGES = ("C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4")
ABSORBEURS = ("A", "B", "C", "D")


def lisible(rec):
    """Gel 3.7 : suivie, finie et strictement positive ; pas de plancher."""
    if not rec or not rec.get("suivi"):
        return None
    g = rec.get("gamma")
    if g is None or not math.isfinite(g) or not g > 0.0:
        return None
    return g


def fenetres(traj):
    """Les huit fenetres de cinq valeurs lisibles a k consecutifs : [(rapport exact, k0, valeurs)]."""
    val = {k: lisible(traj.get(str(k))) for k in range(K_BAS, K_HAUT + 1)}
    out = []
    for k0 in range(K_BAS, K_HAUT - 3):
        v = [val[k] for k in range(k0, k0 + 5)]
        if None in v:
            continue
        out.append((Fraction(max(v)) / Fraction(min(v)), k0, v))
    return out


def plateau(traj):
    f = fenetres(traj)
    if not f:
        return {"statut": "AUCUNE FENETRE"}
    rap, k0, v = min(f, key=lambda t: (t[0], t[1]))
    return {"statut": "PLATEAU" if rap <= SEUIL_PLATEAU else "PAS DE PLATEAU", "k0": k0, "rapport": rap,
            "etalement": float(rap) - 1.0, "Gamma_pl": math.exp(math.fsum(math.log(x) for x in v) / 5.0)}


def accord(a, b, tau=TAU):
    return abs(math.log(a) - math.log(b)) <= tau


def juger_etat(trajs, g_dep):
    pl = {x: plateau(trajs[x]) for x in ABSORBEURS}
    echecs, sans_fenetre = [], []
    for x in ABSORBEURS:
        if pl[x]["statut"] == "AUCUNE FENETRE":
            sans_fenetre.append(x)
        elif pl[x]["statut"] == "PAS DE PLATEAU":
            echecs.append({"A": "a", "B": "b", "C": "c", "D": "d"}[x])
    if pl["A"]["statut"] == "PLATEAU":
        for x, ep in (("B", "b"), ("C", "c"), ("D", "d")):
            if pl[x]["statut"] == "PLATEAU" and not accord(pl[x]["Gamma_pl"], pl["A"]["Gamma_pl"]):
                echecs.append(ep + "-accord")
    if echecs:
        statut = "NON QUALIFIE"
    elif sans_fenetre:
        statut = "NON LISIBLE"
    else:
        statut = "QUALIFIE"
    lu = None
    if pl["A"]["statut"] == "PLATEAU" and g_dep is not None:
        lu = accord(g_dep, pl["A"]["Gamma_pl"])
    return {"statut": statut, "echecs": sorted(echecs), "sans_fenetre": sans_fenetre, "plateaux": pl, "lu": lu}


def cascade(instrument_tient, etats_lus, n_juges, n_qualifies):
    """etats_lus : {id: statut de l'etat de rang 0} (ids lus) ; n_juges, n_qualifies : totaux des points lus."""
    if not instrument_tient:
        return "NON CONCLUANT D'INSTRUMENT"
    if set(etats_lus) != set(JUGES):
        return "RUN INCOMPLET"
    nb_q = sum(1 for s in etats_lus.values() if s == "QUALIFIE")
    nb_n = sum(1 for s in etats_lus.values() if s == "NON QUALIFIE")
    if nb_q == 12:
        return "ESTIMATEUR QUALIFIE" if Fraction(n_qualifies, n_juges) >= NEUF_DIXIEMES else "QUALIFIE A L'ETAT LU"
    if nb_q >= 1:
        return "QUALIFIE PAR POINT"
    return "NON QUALIFIE" if nb_n >= 1 else "NON LISIBLE"


def issue_consigne(n_plateau_A, n_lus):
    if n_plateau_A == 0:
        return "NON LUE"
    if n_lus == n_plateau_A:
        return "LA LECTURE DEPOSEE EST SUR LE PLATEAU"
    if Fraction(n_lus, n_plateau_A) >= NEUF_DIXIEMES:
        return "LA LECTURE DEPOSEE EST SUR LE PLATEAU A NEUF ETATS SUR DIX AU MOINS"
    return "LA LECTURE DEPOSEE N'EST PAS PARTOUT SUR LE PLATEAU"


def tient_etage0(g_lu, suivi, g_dep):
    """Gel 4 : |Gamma_lue - G_dep| <= 1e-3 G_dep + 1e-12, et la lecture est suivie."""
    return bool(suivi) and g_lu is not None and abs(g_lu - g_dep) <= 1e-3 * g_dep + 1e-12


def tient_ancre(a, b):
    """Gel 5.2 : meme statut de suivi, et |ln(Gamma_m2 / Gamma_m1)| <= 1e-6 si suivie."""
    if bool(a.get("suivi")) != bool(b.get("suivi")):
        return False
    if not a.get("suivi"):
        return True
    return abs(math.log(a["gamma"]) - math.log(b["gamma"])) <= 1e-6


def tient_temoin_positif(traj, g_ref, u_ref):
    """Gel 6.1 : PLATEAU, et |ln(Gamma_pl / Gamma_ref)| <= tau + u_ref."""
    p = plateau(traj)
    if p["statut"] != "PLATEAU":
        return False
    return abs(math.log(p["Gamma_pl"]) - math.log(g_ref)) <= TAU + u_ref


def tient_temoin_negatif(traj):
    """Gel 6.2 : PAS DE PLATEAU (ni PLATEAU) ; une absence de fenetre n'est pas un plateau."""
    return plateau(traj)["statut"] != "PLATEAU"
