# -*- coding: ascii -*-
"""SONDE DE LA QUALIFICATION E-B TER -- machine 1, v1, 2026-11-15. CLASSE 2. Elle MESURE et ne juge pas.
Lecture, par le lecteur creux, de la largeur d'etats du H 2D du moteur sous absorbeur long.
Usage :
  python -I sonde_qualification_EB_ter_machine1_v1.py <moteur_v17.py> <sonde_ordre2.json> <tp_retenus.json>
         <dossier de sortie> <mode> [<id> ...]
  modes :
    etage0   les deux ancres A1 et A2, tous leurs etats, F1 a 20 couches (la geometrie deposee), k = 2, 3, 4
    ancres   les deux etats de rang 0 et 1 des ancres A1 et A2, sous les quatre absorbeurs, k = -3 a 8
    etage1   le temoin positif (jumeau H+, w2 = 39/20, les couplages retenus) et le temoin negatif (le jumeau H+
             a la geometrie de chaque ancre, a l'etiquette de son etat de rang 0), quatre absorbeurs, k = -3 a 8
    point    un ou plusieurs des douze points juges (C1 ... L4), nommes en argument : leurs etats dont la
             largeur deposee a k = 3 depasse dix planchers, sous les quatre absorbeurs, k = -3 a 8
Chaque appel ecrit UN fichier, sonde_ter_<mode>[_<id>].json, et ne lit aucune largeur d'un autre script :
du depot du delta 98 il ne prend que w2, g, r_c, eta0, les etiquettes (n1, n2), l'energie reelle a k = 3 et,
pour choisir les etats, la largeur deposee a k = 3 ; il ne la recopie que pour que la feuille la compare.
Les appels sont independants : ils peuvent etre lances en parallele, un processus par point."""
import sys, os, math, json, time, hashlib, unicodedata, importlib.util, platform
from fractions import Fraction as F
import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as sl

MOTEUR, DEPOT, RETENUS, DOSSIER, MODE = sys.argv[1:6]
IDS = sys.argv[6:]
CANON_MOTEUR, CANON_DEPOT, CANON_RETENUS = "82a0be882568fe0c", "10887c60d5f55bcf", "69b3bab3bb8480b7"
JUGES = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4"]
ANCRES = ["A1", "A2"]
KS = list(range(-3, 9))                                  # douze barreaux, eta_k = eta0 * 2^(-k)
KS_ETAGE0 = [2, 3, 4]
ABSORBEURS = [("A", "F2", 0, 80), ("B", "F2", 0, 100), ("C", "F1", 0, 100), ("D", "F2", 10, 80)]   # nom, forme, bord - r_c, couches
PLANCHER10 = 1.33e-12                                    # dix planchers de la decomposition dense (delta 95)
TP_W2, TP_RC, TP_ETA0 = F(39, 20), 40, 0.05

def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

for chemin, attendu, quoi in ((MOTEUR, CANON_MOTEUR, "moteur"), (DEPOT, CANON_DEPOT, "depot du delta 98"), (RETENUS, CANON_RETENUS, "couplages retenus")):
    if canon_B(chemin) != attendu:
        raise SystemExit("REFUS : le canon du %s (%s) n'est pas %s" % (quoi, canon_B(chemin), attendu))
spec = importlib.util.spec_from_file_location("moteur", MOTEUR)
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

# --- LECTEUR CREUX (bloc de machine 1, v1, 2026-11-15 ; insere tel quel dans la sonde) ---
# Le hamiltonien est celui de H_2D du moteur, element par element (X_saut_reel du moteur), assemble creux.
# UN etat par lecture : iteration inverse a decalage fixe (l'energie cible, reelle), factorisation creuse
# (scipy.sparse.linalg.splu, ordre MMD_ATA), depart au vecteur du barreau precedent ou au site de Fock de
# l'etiquette. Largeur : Gamma = 2 eta <x|W|x> / <x|x>, exacte pour un vecteur propre droit de H0 - i eta W
# quand H0 est hermitien ; -2 Im(lambda) est consignee a cote. Aucun tirage aleatoire. Si la factorisation
# se dit exactement singuliere, le decalage est repris une fois a 1e-12 pres ; un second echec rend "non suivi".
# Depend de M (le moteur), np, sp (scipy.sparse), sl (scipy.sparse.linalg) et math, charges par l'appelant.
ITER_MIN, ITER_MAX, TOL_RESIDU, POIDS_MIN = 2, 12, 1e-11, 0.5

def assembler(w2, g, Nmax, signe=-1):
    """H0 (partie hors diagonale, reelle symetrique, creuse) et diagonale libre, sur la boite Nmax x Nmax."""
    p = M.P; w = float(w2); W1 = float(M.W1)
    moitie = sorted((k, l) for k in range(-p, p + 1) for l in range(-p, p + 1)
                    if abs(k) + abs(l) <= p and (k + l) % 2 == p % 2 and (k, l) > (0, 0))
    I, J, V = [], [], []
    for a in range(Nmax):
        for b in range(Nmax):
            i = a * Nmax + b
            for (k, l) in moitie:
                a2, b2 = a + k, b + l
                if 0 <= a2 < Nmax and 0 <= b2 < Nmax:
                    v = (g / p) * M.X_saut_reel(p, k, l, float(a), float(b), w2)
                    if v:
                        j = a2 * Nmax + b2
                        I += [j, i]; J += [i, j]; V += [v, v]
    H0 = sp.csr_matrix((V, (I, J)), shape=(Nmax * Nmax, Nmax * Nmax), dtype=float)
    diag = np.array([signe * W1 * a + w * b for a in range(Nmax) for b in range(Nmax)])
    return H0, diag

def restreindre(H0max, diagmax, Nmax, N):
    sel = np.array([a * Nmax + b for a in range(N) for b in range(N)])
    return H0max[sel][:, sel].tocsc(), diagmax[sel]

def table_W(N, forme, r_c, L):
    """F1 : (r - r_c)^2 ; F2 : (r - r_c)^4 / L^2 ; r = max(a, b) ; nul si r <= r_c (gel bis, 3.4)."""
    W = np.zeros(N * N)
    for a in range(N):
        for b in range(N):
            x = max(a, b) - r_c
            if x > 0:
                W[a * N + b] = float(x * x) if forme == "F1" else float(x ** 4) / float(L * L)
    return W

def lire_etat(H0, diag, W, eta, N, site, E_cible, x0=None):
    A = (H0 + sp.diags(diag - 1j * eta * W)).tocsc().astype(complex)
    n = N * N; i0 = site[0] * N + site[1]
    lu, repris = None, False
    for E in (E_cible, E_cible + 1e-12 * max(1.0, abs(E_cible))):   # second essai seulement si la factorisation
        try:                                                        # rend "exactement singuliere"
            lu = sl.splu((A - E * sp.identity(n, format="csc", dtype=complex)).tocsc(), permc_spec="MMD_ATA")
            break
        except RuntimeError:
            repris = True
    if lu is None:
        return {"gamma": None, "gamma_im": None, "E_re": None, "poids_site": None, "residu": None, "iterations": 0,
                "suivi": False, "decalage_repris": True}, x0
    if x0 is None:
        x = np.zeros(n, dtype=complex); x[i0] = 1.0
    else:
        x = x0 / np.linalg.norm(x0)
    lam, res, it = complex(E_cible), float("inf"), 0
    for it in range(1, ITER_MAX + 1):
        y = lu.solve(x); x = y / np.linalg.norm(y)
        Ax = A @ x; lam = complex(np.vdot(x, Ax)); res = float(np.linalg.norm(Ax - lam * x))
        if it >= ITER_MIN and res <= TOL_RESIDU * max(1.0, abs(lam)):
            break
    poids = float(abs(x[i0]) ** 2)
    return {"gamma": float(2.0 * eta * np.sum(W * np.abs(x) ** 2)), "gamma_im": float(-2.0 * lam.imag),
            "E_re": float(lam.real), "poids_site": poids, "residu": res, "iterations": it, "decalage_repris": repris,
            "suivi": bool(res <= TOL_RESIDU * max(1.0, abs(lam)) and poids >= POIDS_MIN)}, x

def trajectoire(H0, diag, W, eta0, N, site, E_depart, ks):
    """Barreaux ks, parcourus de k = 3 vers les k croissants, puis de k = 2 vers les k decroissants ; l'energie
    cible et le vecteur de depart sont ceux du barreau voisin deja lu (ceux du depart a k = 3)."""
    out = {}
    haut = [k for k in sorted(ks) if k >= 3]; bas = [k for k in sorted(ks, reverse=True) if k < 3]
    for serie in (haut, bas):
        E, x = E_depart, None
        if serie is bas and haut and out[str(haut[0])]["suivi"]:
            E, x = out[str(haut[0])]["E_re"], x3
        for k in serie:
            r, xk = lire_etat(H0, diag, W, eta0 * 2.0 ** (-k), N, site, E, x)
            out[str(k)] = r
            if serie is haut and k == haut[0]:
                x3 = xk
            if r["suivi"]:
                E, x = r["E_re"], xk
    return out
# --- fin du bloc ---

def etats_du_point(p, choix):
    out = []
    for e in p["etats"]:
        G3 = (e.get("Gamma_2D") or {}).get("3")
        if choix == "tous" or (choix == "rangs01" and e["rang"] in (0, 1)) or (choix == "juges" and G3 is not None and G3 > PLANCHER10):
            out.append(e)
    return out

def mesurer_point(p, choix, absorbeurs, ks):
    t0 = time.time()
    num, den = p["w2"].split("/"); w2 = F(int(num), int(den)); g = p["g"]; r_c = p["r_c"]; eta0 = p["eta0"]
    geo = [(nom, forme, r_c + dr, L, r_c + dr + L) for nom, forme, dr, L in absorbeurs]
    Nmax = max(x[4] for x in geo)
    H0m, dm = assembler(w2, g, Nmax)
    blocs = {}
    for nom, forme, bord, L, N in geo:
        H0, dg = restreindre(H0m, dm, Nmax, N); blocs[nom] = (H0, dg, table_W(N, forme, bord, L), N)
    pt = {"id": p["id"], "w2": p["w2"], "facteur": p["facteur"], "g": g, "r_c": r_c, "eta0": eta0,
          "absorbeurs": {nom: {"forme": forme, "bord": bord, "couches": L, "N": N} for nom, forme, bord, L, N in geo}, "etats": []}
    for e in etats_du_point(p, choix):
        site = (int(e["n1"]), int(e["n2"]))
        rec = {"rang": e["rang"], "n1": site[0], "n2": site[1], "E_depart": e["E_re"], "G_dep": (e.get("Gamma_2D") or {}), "traj": {}}
        for nom, forme, bord, L, N in geo:
            H0, dg, W, N = blocs[nom]
            rec["traj"][nom] = trajectoire(H0, dg, W, eta0, N, site, e["E_re"], ks)
        pt["etats"].append(rec)
        print("  %s rang %2d (%2d,%d) : %s" % (p["id"], e["rang"], site[0], site[1], " ".join("%s %d/%d" % (
            nom, sum(rec["traj"][nom][str(k)]["suivi"] for k in ks), len(ks)) for nom, _, _, _, _ in geo)), flush=True)
    pt["duree_s"] = round(time.time() - t0, 1)
    return pt

def mesurer_temoin(r):
    t0 = time.time(); g = r["g"]
    geo = [(nom, forme, TP_RC + dr, L, TP_RC + dr + L) for nom, forme, dr, L in ABSORBEURS]
    Nmax = max(x[4] for x in geo)
    H0m, dm = assembler(TP_W2, g, Nmax, signe=+1)
    rec = {"j": r["j"], "g": g, "w2": "39/20", "r_c": TP_RC, "eta0": TP_ETA0, "site": [0, 0], "E_depart": 0.0, "traj": {},
           "absorbeurs": {nom: {"forme": forme, "bord": bord, "couches": L, "N": N} for nom, forme, bord, L, N in geo}}
    for nom, forme, bord, L, N in geo:
        H0, dg = restreindre(H0m, dm, Nmax, N)
        rec["traj"][nom] = trajectoire(H0, dg, table_W(N, forme, bord, L), TP_ETA0, N, (0, 0), 0.0, KS)
    rec["duree_s"] = round(time.time() - t0, 1)
    print("  temoin j = %d : %s" % (r["j"], " ".join("%s %d/%d" % (nom, sum(rec["traj"][nom][str(k)]["suivi"] for k in KS), len(KS)) for nom, _, _, _, _ in geo)), flush=True)
    return rec

def mesurer_temoin_negatif(p):
    """Le jumeau H+ (signe +1) aux w2, g, r_c et eta0 de l'ancre, a l'etiquette de son etat de rang 0 : une largeur
    que seul l'absorbeur fabrique. Energie de depart : l'energie libre du jumeau au site."""
    t0 = time.time()
    num, den = p["w2"].split("/"); w2 = F(int(num), int(den)); g = p["g"]; r_c = p["r_c"]; eta0 = p["eta0"]
    e = [x for x in p["etats"] if x["rang"] == 0][0]; site = (int(e["n1"]), int(e["n2"]))
    E0 = float(M.W1) * site[0] + float(w2) * site[1]
    geo = [(nom, forme, r_c + dr, L, r_c + dr + L) for nom, forme, dr, L in ABSORBEURS]
    Nmax = max(x[4] for x in geo)
    H0m, dm = assembler(w2, g, Nmax, signe=+1)
    rec = {"id": p["id"], "w2": p["w2"], "g": g, "r_c": r_c, "eta0": eta0, "site": list(site), "E_depart": E0, "traj": {},
           "absorbeurs": {nom: {"forme": forme, "bord": bord, "couches": L, "N": N} for nom, forme, bord, L, N in geo}}
    for nom, forme, bord, L, N in geo:
        H0, dg = restreindre(H0m, dm, Nmax, N)
        rec["traj"][nom] = trajectoire(H0, dg, table_W(N, forme, bord, L), eta0, N, site, E0, KS)
    rec["duree_s"] = round(time.time() - t0, 1)
    print("  temoin negatif %s : %s" % (p["id"], " ".join("%s %d/%d" % (nom, sum(rec["traj"][nom][str(k)]["suivi"] for k in KS), len(KS)) for nom, _, _, _, _ in geo)), flush=True)
    return rec

def main():
    D = json.load(open(DEPOT)); P = {p["id"]: p for p in D["points"]}
    sortie = {"sonde": "sonde_qualification_EB_ter_machine1_v1", "sonde_canon": canon_B(os.path.abspath(__file__)),
              "moteur_canon": canon_B(MOTEUR), "depot_canon": canon_B(DEPOT), "retenus_canon": canon_B(RETENUS), "mode": MODE, "ids": IDS,
              "reglage": {"ks": KS, "ks_etage0": KS_ETAGE0, "absorbeurs": [list(a) for a in ABSORBEURS], "plancher10": PLANCHER10,
                          "iter_min": ITER_MIN, "iter_max": ITER_MAX, "tol_residu": TOL_RESIDU, "poids_min": POIDS_MIN},
              "plateforme": {"systeme": platform.system(), "machine": platform.machine(), "python": platform.python_version(),
                             "numpy": np.__version__, "scipy": scipy.__version__, "coeurs": os.cpu_count(),
                             "fils": {v: os.environ.get(v) for v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                             "levier": os.environ.get("NPY_DISABLE_CPU_FEATURES")}}
    t0 = time.time()
    if MODE == "etage0":
        if IDS: raise SystemExit("REFUS : etage0 ne prend pas d'identifiant")
        sortie["points"] = []
        for pid in ANCRES:
            p = P[pid]; L = p["N"] - p["r_c"]
            sortie["points"].append(mesurer_point(p, "tous", [("depot", "F1", 0, L)], KS_ETAGE0))
        nom = "sonde_ter_etage0.json"
    elif MODE == "ancres":
        if IDS: raise SystemExit("REFUS : ancres ne prend pas d'identifiant")
        sortie["points"] = [mesurer_point(P[pid], "rangs01", ABSORBEURS, KS) for pid in ANCRES]
        nom = "sonde_ter_ancres.json"
    elif MODE == "etage1":
        if IDS: raise SystemExit("REFUS : etage1 ne prend pas d'identifiant")
        R = json.load(open(RETENUS))
        if R.get("w2") != "39/20" or R.get("p") != 5: raise SystemExit("REFUS : la liste des retenus n'est pas celle du temoin")
        sortie["temoin"] = [mesurer_temoin(r) for r in R["retenus"]]
        sortie["temoin_negatif"] = [mesurer_temoin_negatif(P[pid]) for pid in ANCRES]
        nom = "sonde_ter_etage1.json"
    elif MODE == "point":
        if not IDS or any(i not in JUGES for i in IDS): raise SystemExit("REFUS : point demande un ou plusieurs identifiants parmi %s" % JUGES)
        sortie["points"] = [mesurer_point(P[pid], "juges", ABSORBEURS, KS) for pid in IDS]
        nom = "sonde_ter_point_%s.json" % "_".join(IDS)
    else:
        raise SystemExit("REFUS : mode inconnu %s" % MODE)
    sortie["duree_s"] = round(time.time() - t0, 1)
    os.makedirs(DOSSIER, exist_ok=True)
    chemin = os.path.join(DOSSIER, nom)
    json.dump(sortie, open(chemin, "w"), indent=1, sort_keys=True)
    print("ecrit %s (%.0f s)" % (chemin, time.time() - t0))

main()
