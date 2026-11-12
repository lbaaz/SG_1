# -*- coding: ascii -*-
"""REFERENCE du TEMOIN POSITIF (gel E-B v2, section 5.1) par ROTATION COMPLEXE -- machine 2, v1, 2026-11-11.

Le jumeau H+ du moteur (signe_fantome = +1, potentiel x^5), w2 = 39/20, p = 5, SANS absorbeur : la largeur
est celle de la resonance, lue sur la partie imaginaire d'une valeur propre de H(theta),
    H(theta) = somme_i w_i [cos(2 theta) n_i + (i/2) sin(2 theta) (a_i^2 + a_i^+2)]
               + (1/2)(w1 + w2)(cos(2 theta) - 1) + exp(5 i theta) (g/5) x^5 ,
x = l1 (a1 + a1^+) + l2 (a2 + a2^+), l_i = 1 / sqrt(2 Delta w_i), Delta = w2^2 - w1^2, w1 = 1.
Re-derivee (rotation x -> e^{i theta} x, p -> e^{-i theta} p : w/2 (e^{-2i theta} p^2 + e^{2i theta} x^2) - w/2,
soit w [cos 2theta n + (i/2) sin 2theta (a^2 + a^+2)] + (w/2)(cos 2theta - 1)) ; verifiee a theta = 0 contre H_2D
du moteur (garde R1).

CE SCRIPT NE LIT NI LA SONDE NI LA FEUILLE NI AUCUNE LARGEUR MESUREE. Il n'importe le moteur que pour la garde R1
(H a theta = 0 == H_2D) ; la reference elle-meme est construite ici, sans lui.

SORTIES (interface P-1 du gel v2) :
  tp_retenus_machine2_v1.json    {"w2": "39/20", "p": 5, "retenus": [{"j", "g"}]}   AUCUNE largeur
  tp_reference_machine2_v1.json  {"retenus": [{"j", "g"}], "balayage": [{"j", "g", "Gamma_ref", "u_ref",
                                  "raffine", ...}]}   les 17 g_j, TOUJOURS des nombres
  tp_reference_machine2_v1_calculs.json   tous les points calcules (j, N, theta, E, Gamma, recouvrement)

LECTURE DU GEL (declaree, sections 5.1) :
  g_j = 0.05 * 2.0 ** (j / 8.0), j = 0..16 ; theta dans {0.10, 0.15, 0.20, 0.25, 0.30} ; N dans {50, 60, 70}.
  Etat : celui de plus grand recouvrement hermitien |<0,0|v>|^2 (v de norme hermitienne 1) avec le vide de Fock.
  Gamma = -2 Im E. "theta de plus petite variation" : parmi les TROIS theta centraux, a N = 70, celui dont le
  plus grand ecart |ln| de Gamma a ses deux theta voisins est le plus petit (egalite : le plus petit theta).
  Gamma_ref = Gamma a ce theta, N = 70. u_ref = max |Gamma(theta, N) / Gamma_ref - 1| sur theta dans
  {0.15, 0.20, 0.25} et N dans {60, 70}. Toute autre lecture de "plus petite variation" deplace Gamma_ref d'au
  plus u_ref : c'est la raison d'etre de u_ref.
  RETENUS : parmi les g_j dont Gamma_ref est dans [1e-11, 1e-7] avec u_ref <= 0.01, les deux dont
  ln(Gamma_ref) est le plus proche de ln(1e-10) et de ln(1e-8) (egalite : le plus petit j). La selection ne lit
  QUE cette table.
  RAFFINEMENT (economie de calcul, DECLAREE) : les 17 g_j sont d'abord calcules a (N = 50, theta = 0.20) ; la grille
  complete n'est jouee que pour ceux dont ce Gamma est dans [1e-12, 1e-6] (une decade de marge de chaque cote de
  la fenetre du gel). Les autres portent Gamma_ref = ce Gamma, u_ref = 1.0 et raffine = false : ils ne peuvent
  pas etre retenus (u_ref > 0.01).

Reprise par fichier SOUS IDENTITE (lecon de D-1) : un fichier de calcul repris doit porter la meme identite
(w1, w2, p, signe, j, g, N, theta, formule) que le calcul demande, sinon ARRET code 2.
Usage : python -P reference_TP_rotation_complexe_machine2_v1.py --moteur m17_chaine_v17.py --sortie DOSSIER
            [--travailleurs K] [--threads T] [--prevol]
"""
import os
import sys

for _i, _a in enumerate(sys.argv):                    # avant numpy : fils de calcul des bibliotheques
    if _a == "--threads" and _i + 1 < len(sys.argv):
        for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
            os.environ[_v] = sys.argv[_i + 1]

import argparse
import hashlib
import importlib.util
import json
import math
import time
import unicodedata
from fractions import Fraction

import numpy as np

sys.dont_write_bytecode = True

W1 = 1.0
W2_TXT = "39/20"
W2 = float(Fraction(39, 20))
PUISS = 5
THETAS = [0.10, 0.15, 0.20, 0.25, 0.30]
CENTRAUX = [0.15, 0.20, 0.25]
NS = [50, 60, 70]
THETA_GROS = 0.20
N_GROS = 50
FENETRE_GEL = (1e-11, 1e-7)
FENETRE_RAFFINE = (1e-12, 1e-6)
U_MAX = 0.01
CIBLES_GEL = (1e-10, 1e-8)
CANON_MOTEUR = "82a0be882568fe0c"
CANON_GEL = "cde0cd11a763f26d"
FORMULE = "rotation-complexe-v1"
SPREAD_E = 1e-6
REC_MIN = 0.5


def emp(raw):
    """Empreinte convention B : sha256 du texte NFC, CRLF -> LF, 16 hex."""
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
    except UnicodeDecodeError:
        t = raw
    return hashlib.sha256(t).hexdigest()[:16]


def g_de(j):
    return 0.05 * 2.0 ** (j / 8.0)


def arret(code, msg):
    print("ARRET (code %d) : %s" % (code, msg), flush=True)
    sys.exit(code)


# ---------------------------------------------------------------------------
# H(theta)
# ---------------------------------------------------------------------------
_BLOCS = {}


def blocs(N):
    """Parties de H independantes de (theta, g), a la dimension N x N (cache d'un seul N)."""
    if N in _BLOCS:
        return _BLOCS[N]
    _BLOCS.clear()
    Mx = N + PUISS                                   # base etendue : x^j (j <= 5) exact dans le bloc N x N
    a = np.diag(np.sqrt(np.arange(1, Mx)), 1)
    xt = a + a.T
    Xj = [np.linalg.matrix_power(xt, j)[:N, :N] for j in range(PUISS + 1)]
    D = W2 * W2 - W1 * W1
    l1 = (2.0 * D * W1) ** -0.5
    l2 = (2.0 * D * W2) ** -0.5
    dim = N * N
    x5 = np.zeros((dim, dim))
    for j in range(PUISS + 1):
        x5 += math.comb(PUISS, j) * l1 ** j * l2 ** (PUISS - j) * np.kron(Xj[j], Xj[PUISS - j])
    aN = np.diag(np.sqrt(np.arange(1, N)), 1)
    sq = aN @ aN + aN.T @ aN.T                        # a^2 + a^+2, exact dans le bloc N x N
    I = np.eye(N)
    SQ = W1 * np.kron(sq, I) + W2 * np.kron(I, sq)
    n1 = np.repeat(np.arange(N, dtype=float), N)      # indice (a, b) -> a * N + b
    n2 = np.tile(np.arange(N, dtype=float), N)
    ntot = W1 * n1 + W2 * n2
    _BLOCS[N] = (x5, SQ, ntot)
    return _BLOCS[N]


def H_rot(N, g, theta, puiss_phase=PUISS):
    """H(theta). puiss_phase : l'exposant de e^{i * puiss_phase * theta} ; 5 est la formule, 4 sert a la garde R6."""
    x5, SQ, ntot = blocs(N)
    c2, s2 = math.cos(2.0 * theta), math.sin(2.0 * theta)
    H = (np.exp(1j * puiss_phase * theta) * (g / PUISS)) * x5
    H += (0.5j * s2) * SQ
    d = np.arange(N * N)
    H[d, d] += c2 * ntot + 0.5 * (W1 + W2) * (c2 - 1.0)
    return H


def etat_du_vide(vals, vecs):
    """Indice de l'etat de plus grand recouvrement hermitien avec |0,0> (indice 0) ; ex aequo : plus petite
    partie reelle. Rend (indice, recouvrement, second recouvrement)."""
    rec = np.abs(vecs[0, :]) ** 2
    ordre = np.lexsort((vals.real, -rec))
    nu = int(ordre[0])
    return nu, float(rec[nu]), float(rec[ordre[1]])


def resoudre(N, g, theta, puiss_phase=PUISS):
    t0 = time.time()
    H = H_rot(N, g, theta, puiss_phase)
    vals, vecs = np.linalg.eig(H)
    del H
    nu, rec, rec2 = etat_du_vide(vals, vecs)
    E = vals[nu]
    del vecs
    return {"E_re": float(E.real), "E_im": float(E.imag), "gamma": float(-2.0 * E.imag),
            "recouvrement": rec, "recouvrement_2": rec2, "duree_s": round(time.time() - t0, 1)}


# ---------------------------------------------------------------------------
# calculs sous identite, avec reprise par fichier
# ---------------------------------------------------------------------------
def identite(j, g, N, theta):
    return {"w1": W1, "w2": W2_TXT, "p": PUISS, "signe": 1, "j": j, "g": g, "N": N, "theta": theta,
            "formule": FORMULE}


def chemin_calcul(rep, j, N, theta):
    return os.path.join(rep, "j%02d_N%d_th%.2f.json" % (j, N, theta))


def calculer(tache):
    rep, j, N, theta = tache
    g = g_de(j)
    f = chemin_calcul(rep, j, N, theta)
    ident = identite(j, g, N, theta)
    if os.path.exists(f):
        r = json.load(open(f))
        if r.get("identite") != ident:
            ecart = sorted(c for c in set(ident) | set(r.get("identite") or {})
                           if (r.get("identite") or {}).get(c) != ident.get(c))
            arret(2, "reprise refusee : %s porte une autre identite, cles en ecart %s" % (f, ecart))
        r["repris"] = True
        return r
    r = resoudre(N, g, theta)
    r["identite"] = ident
    r["repris"] = False
    tmp = f + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(r, fh, sort_keys=True)
    os.replace(tmp, f)
    return r


def executer(taches, K):
    """Joue les taches (la plus grande dimension d'abord) ; rend {(j, N, theta): resultat}."""
    ordre = sorted(taches, key=lambda t: (-t[2], t[1], t[3]))
    out = {}
    if K <= 1:
        it = (((t[1], t[2], t[3]), calculer(t)) for t in ordre)
        for cle, r in it:
            out[cle] = r
            ecrire(cle, r)
    else:
        import multiprocessing as mp
        ctx = mp.get_context("spawn")
        with ctx.Pool(K) as pool:
            for r_t, r in zip(ordre, pool.imap(calculer, ordre, chunksize=1)):
                cle = (r_t[1], r_t[2], r_t[3])
                out[cle] = r
                ecrire(cle, r)
    return out


def ecrire(cle, r):
    j, N, th = cle
    print("  j=%02d g=%.6f N=%d theta=%.2f : Gamma=%.6e E=%.10f %+.3e i rec=%.4f (2e: %.2e)  %s" % (
        j, g_de(j), N, th, r["gamma"], r["E_re"], r["E_im"], r["recouvrement"], r["recouvrement_2"],
        "repris" if r["repris"] else "%.1f s" % r["duree_s"]), flush=True)


# ---------------------------------------------------------------------------
# reduction : Gamma_ref, u_ref
# ---------------------------------------------------------------------------
def reduire(j, res, ns):
    """res : {(N, theta): resultat}. Rend la ligne de la table pour un g_j raffine."""
    g = g_de(j)
    nmax = max(ns)
    n2 = sorted(ns)[-2:]
    G = {t: res[(nmax, t)]["gamma"] for t in THETAS}
    ligne = {"j": j, "g": g, "raffine": True, "N": nmax}
    motifs = []
    if not all(v > 0 and math.isfinite(v) for v in G.values()):
        motifs.append("Gamma non strictement positif a N = %d" % nmax)
        th = THETA_GROS
    else:
        LG = {t: math.log(G[t]) for t in THETAS}

        def variation(t):
            # DIFFERENCES de logarithmes, pas log d'un rapport : x - y et y - x sont exactement opposes, donc
            # deux theta voisins qui partagent leur plus grand ecart sont a EGALITE EXACTE et la regle declaree
            # (egalite : le plus petit theta) s'applique, au lieu d'un arrondi de 1e-16 (defaut du premier jet).
            i = THETAS.index(t)
            return max(abs(LG[t] - LG[THETAS[i - 1]]), abs(LG[t] - LG[THETAS[i + 1]]))
        th = min(CENTRAUX, key=lambda t: (variation(t), t))
        ligne["variation_theta"] = variation(th)
    gref = G[th]
    ligne["theta"] = th
    ligne["Gamma_ref"] = gref
    ligne["E_re"] = res[(nmax, th)]["E_re"]
    ligne["recouvrement"] = res[(nmax, th)]["recouvrement"]
    ligne["Gamma_par_theta_Nmax"] = {"%.2f" % t: G[t] for t in THETAS}
    pts = [(n, t) for n in n2 for t in CENTRAUX]
    if gref > 0 and math.isfinite(gref):
        u = max(abs(res[p]["gamma"] / gref - 1.0) for p in pts)
    else:
        u = 1.0
    er = [res[p]["E_re"] for p in pts]
    ligne["spread_E_re"] = max(er) - min(er)
    if ligne["spread_E_re"] > SPREAD_E:
        motifs.append("Re E non stable (%.2e > %g) : l'etat n'est pas le meme" % (ligne["spread_E_re"], SPREAD_E))
    if min(res[p]["recouvrement"] for p in pts) < REC_MIN:
        motifs.append("recouvrement avec le vide < %g" % REC_MIN)
    if motifs:
        u = 1.0
    ligne["u_ref"] = float(u)
    if motifs:
        ligne["motifs"] = motifs
    n0 = sorted(ns)[0]
    if (n0, THETA_GROS) in res:
        ligne["Gamma_Nmin_theta_0.20"] = res[(n0, THETA_GROS)]["gamma"]
    return ligne


def selection(balayage):
    """Regle du gel 5.1, sur la table seule (ecrite ici, sans lire la feuille)."""
    c = [r for r in balayage if FENETRE_GEL[0] <= r["Gamma_ref"] <= FENETRE_GEL[1] and r["u_ref"] <= U_MAX]
    if not c:
        return []
    js = set()
    for cible in CIBLES_GEL:
        js.add(min(c, key=lambda r: (abs(math.log(r["Gamma_ref"] / cible)), r["j"]))["j"])
    return sorted(js)


# ---------------------------------------------------------------------------
# gardes
# ---------------------------------------------------------------------------
def gardes(moteur_chemin):
    ok = True

    def dire(nom, tient, detail):
        nonlocal ok
        print("GARDE %-3s %-58s %s  %s" % (nom[0], nom[1], "TIENT" if tient else "MORD", detail), flush=True)
        ok = ok and tient

    # R1 : H a theta = 0 contre H_2D du moteur
    raw = open(moteur_chemin, 'rb').read()
    canon = emp(raw)
    spec = importlib.util.spec_from_file_location("moteur_ref", moteur_chemin)
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)
    dire(("R0", "moteur au canon %s" % CANON_MOTEUR), canon == CANON_MOTEUR, "canon lu %s" % canon)
    N0 = 14
    Hm, _ = M.H_2D(N0, Fraction(39, 20), 0.10, +1, "x5", 0.0, None)
    Hr = H_rot(N0, 0.10, 0.0)
    e = float(np.max(np.abs(Hr - Hm)))
    dire(("R1", "H(theta = 0) == H_2D du moteur, N = 14, g = 0.10"), e <= 1e-12, "ecart max %.3e" % e)
    # R2 : symetrie complexe
    Hs = H_rot(N0, 0.10, 0.20)
    e = float(np.max(np.abs(Hs - Hs.T)))
    dire(("R2", "H(theta) complexe symetrique (H == H^T), theta = 0.20"), e <= 1e-12, "ecart max %.3e" % e)
    # R3 : g = 0, la rotation laisse le spectre de l'oscillateur inchange
    Nq = 40
    vals = np.linalg.eigvals(H_rot(Nq, 0.0, 0.20))
    bas = np.sort(vals.real)[:6]
    att = np.array([0.0, 1.0, 1.95, 2.0, 2.95, 3.0])
    e = float(np.max(np.abs(bas - att)))
    dire(("R3", "g = 0 : six premiers niveaux 0, 1, 1.95, 2, 2.95, 3 (N = 40)"), e <= 1e-6, "ecart max %.3e" % e)
    # R6 : la garde mord -- une phase fausse e^{4 i theta} fait varier Gamma avec theta au-dela de u_ref
    Nm, gm = 30, 0.10
    def spread(pp):
        gs = [resoudre(Nm, gm, t, pp)["gamma"] for t in CENTRAUX]
        return (max(gs) / min(gs) - 1.0 if min(gs) > 0 else float("inf")), gs
    (s_ok, g_ok), (s_mut, g_mut) = spread(PUISS), spread(PUISS - 1)
    dire(("R6", "la formule tient en theta (N = 30, g = 0.10)"), s_ok <= 1e-3,
         "etalement %.2e, Gamma %s" % (s_ok, ["%.4e" % x for x in g_ok]))
    dire(("R6b", "la phase fausse e^{4 i theta} MORD (u > 0.01)"), s_mut > U_MAX,
         "etalement %.2e, Gamma %s" % (s_mut, ["%.4e" % x for x in g_mut]))
    # R4 : la regle de selection, sur une table synthetique (celle du G-Q7 de la feuille, retapee)
    bal = [{"j": j, "Gamma_ref": 10.0 ** (-13 + j), "u_ref": 0.001} for j in range(9)]
    bal[5]["u_ref"] = 0.02
    dire(("R4", "selection du gel sur une table synthetique -> [3, 4]"), selection(bal) == [3, 4],
         "obtenu %s" % selection(bal))
    bal2 = [dict(r) for r in bal]
    for r in bal2:
        r["u_ref"] = 0.5
    dire(("R4b", "aucun u_ref <= 0.01 -> aucun retenu"), selection(bal2) == [], "obtenu %s" % selection(bal2))
    return ok


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--moteur", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--travailleurs", type=int, default=1)
    ap.add_argument("--threads", type=int, default=0)
    ap.add_argument("--prevol", action="store_true",
                    help="geometrie reduite, NON OPPOSABLE : N = 20, 24, 28 ; sorties suffixees _prevol")
    a = ap.parse_args()
    global NS, N_GROS
    if a.prevol:
        NS, N_GROS = [20, 24, 28], 20
    os.makedirs(a.sortie, exist_ok=True)
    rep = os.path.join(a.sortie, "calculs_prevol" if a.prevol else "calculs")
    os.makedirs(rep, exist_ok=True)
    suf = "_prevol" if a.prevol else ""
    mon_canon = emp(open(os.path.abspath(__file__), 'rb').read())
    print("reference TP par rotation complexe -- script %s -- python %s numpy %s -- %s" % (
        mon_canon, sys.version.split()[0], np.__version__, "PREVOL (non opposable)" if a.prevol else "REEL"))
    print("travailleurs %d, fils de bibliotheque %s" % (a.travailleurs, os.environ.get("OPENBLAS_NUM_THREADS", "defaut")))
    if not gardes(a.moteur):
        arret(3, "une garde mord : aucune reference n'est ecrite")
    t0 = time.time()
    # --- etape A : les 17 g_j a (N_gros, theta = 0.20)
    print("ETAPE A : 17 g_j a (N = %d, theta = %.2f)" % (N_GROS, THETA_GROS), flush=True)
    A = executer([(rep, j, N_GROS, THETA_GROS) for j in range(17)], a.travailleurs)
    raff = [j for j in range(17) if FENETRE_RAFFINE[0] <= A[(j, N_GROS, THETA_GROS)]["gamma"] <= FENETRE_RAFFINE[1]]
    print("A termine (%.0f s) : a raffiner (Gamma dans [%g, %g]) : %s" % (
        time.time() - t0, FENETRE_RAFFINE[0], FENETRE_RAFFINE[1], raff), flush=True)
    # --- etape B : grille complete pour les raffines
    ns = sorted(NS)
    taches = []
    for j in raff:
        for n in ns:
            ths = THETAS if n in (ns[0], ns[-1]) else CENTRAUX
            for t in ths:
                if not (n == N_GROS and t == THETA_GROS):
                    taches.append((rep, j, n, t))
    print("ETAPE B : %d calculs pour %d g_j raffines" % (len(taches), len(raff)), flush=True)
    B = executer(taches, a.travailleurs)
    tous = dict(B)
    for j in range(17):
        tous[(j, N_GROS, THETA_GROS)] = A[(j, N_GROS, THETA_GROS)]
    # --- reduction
    bal = []
    for j in range(17):
        if j in raff:
            res = {(n, t): tous[(j, n, t)] for n in ns for t in THETAS if (j, n, t) in tous}
            bal.append(reduire(j, res, ns))
        else:
            r = A[(j, N_GROS, THETA_GROS)]
            bal.append({"j": j, "g": g_de(j), "raffine": False, "N": N_GROS, "theta": THETA_GROS,
                        "Gamma_ref": r["gamma"], "u_ref": 1.0, "E_re": r["E_re"],
                        "recouvrement": r["recouvrement"]})
    ret = selection(bal)
    print("TABLE (j, g, Gamma_ref, u_ref, raffine) :")
    for r in bal:
        print("  j=%02d g=%.6f Gamma_ref=%.6e u_ref=%.2e %s%s" % (
            r["j"], r["g"], r["Gamma_ref"], r["u_ref"], "raffine" if r["raffine"] else "non raffine",
            "  theta=%.2f ReE=%.10f rec=%.4f%s" % (r["theta"], r["E_re"], r["recouvrement"],
                                                    "  MOTIFS %s" % r["motifs"] if r.get("motifs") else "")))
    print("RETENUS (regle du gel, sur la table seule) : %s" % (ret if ret else "AUCUN -> TP NON CONCLUANT"))
    ents = {"script_canon": mon_canon, "moteur": CANON_MOTEUR, "gel": CANON_GEL, "formule": FORMULE,
            "w2": W2_TXT, "p": PUISS, "prevol": bool(a.prevol), "thetas": THETAS, "Ns": ns}
    lst = [{"j": j, "g": g_de(j)} for j in ret]
    with open(os.path.join(a.sortie, "tp_retenus_machine2_v1%s.json" % suf), "w") as fh:
        json.dump({"w2": W2_TXT, "p": PUISS, "retenus": lst, "prevol": bool(a.prevol)}, fh, indent=1, sort_keys=True)
    with open(os.path.join(a.sortie, "tp_reference_machine2_v1%s.json" % suf), "w") as fh:
        json.dump(dict(ents, retenus=lst, balayage=bal), fh, indent=1, sort_keys=True)
    calc = [dict(j=j, N=n, theta=t, **{k: v for k, v in r.items() if k not in ("identite", "repris")})
            for (j, n, t), r in sorted(tous.items())]
    with open(os.path.join(a.sortie, "tp_reference_machine2_v1_calculs%s.json" % suf), "w") as fh:
        json.dump(dict(ents, calculs=calc), fh, indent=1, sort_keys=True)
    print("ECRIT : tp_retenus_machine2_v1%s.json, tp_reference_machine2_v1%s.json, "
          "tp_reference_machine2_v1_calculs%s.json (%.0f s au total)" % (suf, suf, suf, time.time() - t0))


if __name__ == "__main__":
    main()
