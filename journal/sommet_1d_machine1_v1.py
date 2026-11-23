# -*- coding: ascii -*-
"""LE SOMMET DU PROFIL, A UNE DIMENSION -- machine 1, v1, 2026-11-22. Hors chaine, classe 3. AUCUN CALCUL 2D.
Ce script n'ecrit aucune piece de gel. Il prepare la qualification du lecteur au sommet et l'esquisse du gel (B).
Il charge, AU CANON CONTROLE et sans les editer, le moteur et les trois blocs deposes (ordre 2, ordre 3, absorbeur adapte),
lus dans un clone du registre public (tete 055be58).
Parties :
  1  la barriere du moteur et les kappa de bord : ou finit la barriere du vide, en kappa et en |d| / g ;
  2  le predicteur (chaines d'ordre 1, 2, 3 sous l'absorbeur adapte, dix-huit variantes) aux points de qualification
     et sur une grille (kappa, g, signe) du sommet ; a la resonance exacte la regle de lecture du bloc divise par |d| :
     la meme lecture (flux) est refaite ici sans cette division, et controlee contre le bloc la ou d n'est pas nul ;
  3  le MANDATAIRE du lecteur : la chaine du premier ordre a qui l'on donne les quatre absorbeurs DU LECTEUR lus le long
     de l'echelle (r = 2 m ; F1 : eta (r - bord)^2 ; F2 : eta (r - bord)^4 / L^2), douze barreaux, sous deux regles pour
     eta0 : celle du depot (|w2 - 2|) et une regle en absolu (eta0 = t_0 / kappa_3, kappa_3 = 0.0262) ; regle de plateau
     de la feuille deposee (cinq barreaux consecutifs, max <= 1.05 min), accord de B, C, D avec A a 0.05 pres.
Usage : python3 -I -B sommet_1d_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <sortie.json>"""
import sys, math, json, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A, SORTIE = sys.argv[1:6]
CANONS = {"moteur": "82a0be882568fe0c", "bloc2": "7cd5977bc27bebc1", "bloc3": "534ba246aa3b8973", "bloc_adapte": "49a40d9098b55361"}
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
for nom, chemin in (("moteur", MOTEUR), ("bloc2", BLOC2), ("bloc3", BLOC3), ("bloc_adapte", BLOC_A)):
    if canon_B(chemin) != CANONS[nom]:
        raise SystemExit("REFUS : %s n'est pas au canon %s (%s)" % (nom, CANONS[nom], canon_B(chemin)))
print("canons controles : moteur %s ; bloc 2 %s ; bloc 3 %s ; bloc adapte %s" % tuple(CANONS[k] for k in ("moteur", "bloc2", "bloc3", "bloc_adapte")))
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):
    cle = (p, k, l, n1, n2, w2)
    if cle not in _cache:
        _cache[cle] = _brut(p, k, l, n1, n2, w2)
    return _cache[cle]
M.X_saut_reel = _X
for bloc in (BLOC2, BLOC3, BLOC_A):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))
KAPPA3 = 0.0262
TAU0 = _brut(M.P, 2, 1, 0.0, 0.0, F(2)) / M.P
def tau2(m):
    return _brut(M.P, 2, 1, float(2 * m), float(m), F(2)) / M.P
sortie = {}

# ------------------------------------------------------------------ partie 1
print()
print("=== PARTIE 1 : la barriere du vide, en kappa = t_0 / |d| et en |d| / g (limite du desaccord nul, w2 = 2)")
print("tau_0 = X(2) / P = %.9f ; forme close 1 / (4 sqrt 6) = %.9f" % (TAU0, 1.0 / (4.0 * math.sqrt(6.0))))
bords = []
for m in range(1, 7):
    xm = 2.0 * tau2(m) / m                      # le site m entre dans la barriere quand |d| / g depasse 2 tau_m / m
    bords.append((m, xm, TAU0 / xm))
    print("   le site %d entre dans la barriere pour |d| / g > %.4f, soit kappa < %.5f" % (m, xm, TAU0 / xm))
print("   profondeur 0 (fenetre SANS barriere) : kappa > %.5f, |d| / g < %.4f" % (bords[0][2], bords[0][1]))
kmil = {}
for m in range(1, 5):
    km = math.sqrt(bords[m - 1][2] * bords[m][2]); kmil[m] = km
    print("   profondeur %d : kappa de %.5f a %.5f ; milieu geometrique %.4f ; |d| / g = %.3f" % (m, bords[m][2], bords[m - 1][2], km, TAU0 / km))
print("   kappa_3 du gel du vide : 0.0262 ; |d| / g = tau_0 / kappa aux sept profondeurs du gel du vide :")
print("   " + " ; ".join("m = %d : %.2f" % (m, TAU0 / k) for m, k in ((3, 0.0262), (4, 0.0200), (5, 0.0159), (6, 0.0130), (8, 0.00928), (12, 0.00558), (16, 0.00382))))
sortie["partie1"] = {"tau0": TAU0, "bords": bords, "kappa_milieu": kmil}

# ------------------------------------------------------------------ partie 2
def tables(w2, g):
    """Barriere du moteur ; si elle est vide (fenetre sans barriere), m_bord = 0 est pose a la main : dit dans le journal."""
    sites = M.barriere(0.0, 0.0, w2, g, True)
    vide = (len(sites) == 0)
    if vide:
        sites = [(0, 0.0, abs(M.t_site(0, 0.0, 0.0, w2, g)))]
    m_bord = sites[-1][0]
    tb = tables_ordre2(0.0, 0.0, w2, g, sites, M_facteur=(5 if m_bord < 3 else 4))
    t3 = tables_ordre3(0.0, 0.0, w2, g, tb)
    return tb, t3, m_bord, vide

def flux_sans_division(H, Wd, i0):
    val, vec = np.linalg.eig(H)
    poids = np.abs(vec[i0, :]) ** 2
    nu = np.lexsort((val.real, -poids))[0]
    psi2 = np.abs(vec[:, nu]) ** 2
    return float(2.0 * (Wd @ psi2) / psi2.sum()), float(poids[nu] / psi2.sum()), complex(val[nu])

def matrice_ordre1(tb, a, c, L):
    d, m_min = tb["d"], tb["m_min"]; debut = tb["m2_bord"] + c; Mh = debut + L; n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min; H[i, i] = m * d
        if m > debut:
            Wd[i] = a * abs(tb["t"][m]) * ((m - debut) / float(L)) ** 2; H[i, i] += -1j * Wd[i]
        if m < Mh:
            H[i, i + 1] = tb["t"][m]; H[i + 1, i] = tb["t"][m]
    return H, Wd, -m_min

def plateau_par_flux(tb, t3, ordre):
    """Mediane et etendue des dix-huit ln Gamma, lecture par le flux sans division par |d| (ordre 1, 2 ou 3)."""
    v = []
    for (a, c, L) in VARIANTES_ADAPTEES:
        H, Wd, i0 = matrice_ordre1(tb, a, c, L) if ordre == 1 else matrice_adaptee(tb, t3, a, c, L, ordre)
        G, p, E = flux_sans_division(H, Wd, i0)
        v.append(math.log(G))
    s = sorted(v); n = len(s)
    return 0.5 * (s[n // 2 - 1] + s[n // 2]), s[-1] - s[0]

def predire(w2, g):
    _cache.clear()
    tb, t3, m_bord, vide = tables(w2, g)
    d = float(w2) - 2.0
    l1, e1 = plateau_par_flux(tb, t3, 1); l2, e2 = plateau_par_flux(tb, t3, 2); l3, e3 = plateau_par_flux(tb, t3, 3)
    rec = {"w2": str(w2), "d": d, "g": g, "x": abs(d) / g, "kappa": (g * _brut(M.P, 2, 1, 0.0, 0.0, w2) / (M.P * abs(d)) if d != 0.0 else None),
           "m_bord": m_bord, "barriere_vide": vide, "ln_G1": l1, "et1": e1, "ln_G2": l2, "et2": e2, "ln_G3": l3, "et3": e3}
    if d != 0.0:                                 # controle de ma lecture contre le bloc depose, la ou il est defini
        p3 = plateau_adapte(tb, t3, 3); p2 = plateau_adapte(tb, t3, 2)
        rec["ecart_au_bloc"] = max(abs(p3["ln_G"] - l3), abs(p2["ln_G"] - l2), abs(p3["etendue"] - e3))
    return rec, tb, t3

def g_de(kappa, w2):
    d = abs(float(w2) - 2.0)
    return float("%.5e" % (kappa * d * M.P / _brut(M.P, 2, 1, 0.0, 0.0, w2)))

print()
print("=== PARTIE 2 : le predicteur (ordres 1, 2, 3 sous l'absorbeur adapte, dix-huit variantes), une dimension")
print("    G / g aux trois ordres, etendues, ecarts entre ordres en logarithme")
print("    point                     w2            g            |d|/g   kappa    m_bord  G1*/g       et1     G2*/g       et2     G3*/g       et3     ln(G2/G1)  ln(G3/G2)  ecart au bloc")
def ligne(nom, rec):
    print("    %-24s  %-12s  %.5e  %6.3f  %-7s  %d%s      %.5e  %.4f  %.5e  %.4f  %.5e  %.4f  %+.4f    %+.4f    %s" % (
        nom, rec["w2"], rec["g"], rec["x"], ("%.4f" % rec["kappa"]) if rec["kappa"] else "infini", rec["m_bord"], "*" if rec["barriere_vide"] else " ",
        math.exp(rec["ln_G1"]) / rec["g"], rec["et1"], math.exp(rec["ln_G2"]) / rec["g"], rec["et2"], math.exp(rec["ln_G3"]) / rec["g"], rec["et3"],
        rec["ln_G2"] - rec["ln_G1"], rec["ln_G3"] - rec["ln_G2"], ("%.1e" % rec["ecart_au_bloc"]) if "ecart_au_bloc" in rec else "-"), flush=True)
points = {}
print("  -- points de qualification (sacrifies) : w2 = 2 exactement ; w2 = 2.0001")
for nom, w2, g in (("Q-a  w2 = 2", F(2), 2.5e-4), ("Q-b  w2 = 2", F(2), 5e-4), ("Q-c  w2 = 2", F(2), 1e-3), ("Q-d  w2 = 2", F(2), 2e-3),
                   ("Q-e  w2 = 2.0001", F("2.0001"), 3e-4), ("Q-f  w2 = 2.0001", F("2.0001"), 1.5e-4)):
    rec, tb, t3 = predire(w2, g); points[nom] = rec; ligne(nom, rec)
print("  -- grille du sommet : kappa x couplage vise x signe (le couplage ecrit suit la regle du gel du vide) ; * = barriere vide")
grille = []
KAPPAS = (0.0363, 0.0530, 0.0800, 0.1300, 0.2000, 0.4000, 1.0000)
for kappa in KAPPAS:
    for gv in (2.5e-4, 1e-3, 3e-3):
        for signe in (-1, +1):
            dd = float("%.3g" % (gv * TAU0 / kappa))
            w2 = F(2) + signe * F(repr(dd))
            g = g_de(kappa, w2)
            rec, tb, t3 = predire(w2, g); rec["kappa_vise"] = kappa; rec["g_vise"] = gv; grille.append(rec)
            ligne("k = %.4f %s g ~ %.1e" % (kappa, "-" if signe < 0 else "+", gv), rec)
sortie["partie2"] = {"points": points, "grille": grille}
print("  lecture de la grille, par kappa : G3* / g (min, max sur 6 cellules) ; plus grand |ln(G3/G1)| ; plus grand |ln(G3/G2)| ; plus grande etendue d'ordre 3")
for kappa in KAPPAS:
    L = [r for r in grille if r["kappa_vise"] == kappa]
    v = [math.exp(r["ln_G3"]) / r["g"] for r in L]
    print("    kappa = %.4f : m_bord %s ; G3*/g de %.4e a %.4e ; |ln(G3/G1)| <= %.4f ; |ln(G3/G2)| <= %.4f ; etendue <= %.4f ; G3*/|d| de %.4e a %.4e" % (
        kappa, sorted(set(r["m_bord"] for r in L)), min(v), max(v), max(abs(r["ln_G3"] - r["ln_G1"]) for r in L), max(abs(r["ln_G3"] - r["ln_G2"]) for r in L),
        max(r["et3"] for r in L), min(math.exp(r["ln_G3"]) / abs(r["d"]) for r in L), max(math.exp(r["ln_G3"]) / abs(r["d"]) for r in L)))
print("  etalement de ln(G3* / |d|) a kappa fixe, sur les six cellules (trois couplages, deux signes) :")
for kappa in KAPPAS:
    L = [r for r in grille if r["kappa_vise"] == kappa]
    v = [r["ln_G3"] - math.log(abs(r["d"])) for r in L]
    print("    kappa = %.4f : etalement %.4f" % (kappa, max(v) - min(v)))
print("  plus grand etalement a kappa fixe : %.4f ; sur la grille : etendue d'ordre 3 max %.4f ; |ln(G3 / G1)| max %.4f ; |ln(G3 / G2)| max %.4f" % (
    max(max(r["ln_G3"] - math.log(abs(r["d"])) for r in grille if r["kappa_vise"] == k) - min(r["ln_G3"] - math.log(abs(r["d"])) for r in grille if r["kappa_vise"] == k) for k in KAPPAS),
    max(r["et3"] for r in grille), max(abs(r["ln_G3"] - r["ln_G1"]) for r in grille), max(abs(r["ln_G3"] - r["ln_G2"]) for r in grille)))
print("  aux points de qualification : G3* / g, G3*, etendue d'ordre 3")
for nom in sorted(points):
    r = points[nom]
    print("    %-18s g = %.1e  G3* / g = %.6f  G3* = %.5e  etendue %.4f" % (nom, r["g"], math.exp(r["ln_G3"]) / r["g"], math.exp(r["ln_G3"]), r["et3"]))
print("  a la resonance exacte (Q-a) : G1* / g = %.6f ; G1* / t_0 = %.5f" % (math.exp(points["Q-a  w2 = 2"]["ln_G1"]) / points["Q-a  w2 = 2"]["g"], math.exp(points["Q-a  w2 = 2"]["ln_G1"]) / points["Q-a  w2 = 2"]["g"] / TAU0))
ec = [r["ecart_au_bloc"] for r in grille + list(points.values()) if "ecart_au_bloc" in r]
print("  controle de ma lecture par le flux contre plateau_adapte du bloc depose : %d points ; plus grand ecart %.1e" % (len(ec), max(ec)))

# ------------------------------------------------------------------ partie 3
KS = list(range(-3, 9))
ABSORBEURS = [("A", "F2", 0, 80), ("B", "F2", 0, 100), ("C", "F1", 0, 100), ("D", "F2", 10, 80)]

def lecteur_1d(d, t, forme, bord, L, eta):
    """Chaine du premier ordre sous un absorbeur du lecteur ; lecture comme le lecteur : l'etat le plus proche de l'energie 0
    (iteration inverse a decalage 0), largeur par le flux 2 <W>, poids au site 0 ; et, a cote, l'etat de plus grand poids."""
    m_max = (bord + L - 1) // 2; n = m_max + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(n):
        H[m, m] = m * d
        x = 2 * m - bord
        if x > 0:
            Wd[m] = eta * (float(x * x) if forme == "F1" else float(x ** 4) / float(L * L)); H[m, m] += -1j * Wd[m]
        if m < m_max:
            H[m, m + 1] = t[m]; H[m + 1, m] = t[m]
    val, vec = np.linalg.eig(H)
    nrm = (np.abs(vec) ** 2).sum(axis=0)
    poids = np.abs(vec[0, :]) ** 2 / nrm
    j0 = int(np.argmin(np.abs(val))); jp = int(np.argmax(poids))
    fl = lambda j: float(2.0 * (Wd @ (np.abs(vec[:, j]) ** 2)) / nrm[j])
    return fl(j0), float(poids[j0]), fl(jp), float(poids[jp]), (j0 == jp)

def plateau(ser):
    best = None
    for k0 in range(-3, 5):
        v = [ser[k] for k in range(k0, k0 + 5)]
        r = max(v) / min(v)
        if best is None or r < best[0] - 1e-15:
            best = (r, k0)
    return best

def mandataire(nom, w2, g, m_bord, ln_G1, regles):
    d = float(w2) - 2.0
    r_c = 2 * (m_bord + max(8, m_bord)) + 2
    t = [(g / M.P) * _brut(M.P, 2, 1, float(2 * m), float(m), w2) for m in range((r_c + 10 + 100) // 2 + 2)]
    t0 = t[0]; out = []
    for regle, eta0 in regles(d, t0):
        if eta0 == 0.0:
            print("    %-18s %-22s eta0 = 0 : l'echelle du depot est degeneree, rien ne se lit" % (nom, regle)); continue
        res = {}
        for (an, forme, dr, L) in ABSORBEURS:
            ser, pds, meme = {}, {}, True
            for k in KS:
                G0, p0, Gp, pp, m_ = lecteur_1d(d, t, forme, r_c + dr, L, eta0 * 2.0 ** (-k)); ser[k] = G0; pds[k] = p0; meme = meme and m_
            r, k0 = plateau(ser)
            res[an] = {"serie": [ser[k] for k in KS], "poids": [pds[k] for k in KS], "k0": k0, "rapport": r, "plateau": bool(r <= 1.05), "valeur": ser[k0],
                       "meme_etat": meme, "poids_min_fenetre": min(pds[k] for k in range(k0, k0 + 5))}
        qual = all(res[a]["plateau"] for a in "ABCD") and all(abs(math.log(res[a]["valeur"] / res["A"]["valeur"])) <= 0.05 for a in "BCD") and all(res[a]["poids_min_fenetre"] >= 0.5 for a in "ABCD")
        for an in "ABCD":
            x = res[an]
            print("    %-18s %-22s eta0/g = %7.3f  %s  %s  k = %+d a %+d  rapport %.4f %s  ln(plateau / G1*) = %+.4f  poids >= %.3f" % (
                nom, regle, eta0 / g, an, " ".join("%.4f" % (v / g) if v / g >= 1e-4 else "%.1e" % (v / g) for v in x["serie"]), x["k0"], x["k0"] + 4, x["rapport"],
                "OUI" if x["plateau"] else "non", math.log(x["valeur"]) - ln_G1, x["poids_min_fenetre"]))
        print("    %-18s %-22s -> %s ; plus grand |ln(X / A)| : %.4f ; plus grand |ln(plateau / G1*)| : %.4f ; fenetres k0 : %s" % (
            nom, regle, "QUALIFIE (mandataire)" if qual else "NON QUALIFIE (mandataire)", max(abs(math.log(res[a]["valeur"] / res["A"]["valeur"])) for a in "BCD"),
            max(abs(math.log(res[a]["valeur"]) - ln_G1) for a in "ABCD"), " ".join("%s %+d" % (a, res[a]["k0"]) for a in "ABCD")), flush=True)
        out.append({"regle": regle, "eta0": eta0, "eta0_sur_g": eta0 / g, "r_c": r_c, "absorbeurs": res, "qualifie": qual})
    return out

print()
print("=== PARTIE 3 : le MANDATAIRE a une dimension du lecteur (premier ordre, absorbeurs du lecteur le long de l'echelle)")
print("    par absorbeur : Gamma_k / g pour k = -3 ... 8 ; fenetre retenue ; rapport ; plateau ; ecart au plateau adapte du premier ordre")
regles = lambda d, t0: (("depot : |w2 - 2|", abs(d)), ("absolu : t_0 / kappa_3", t0 / KAPPA3), ("absolu / 4", t0 / KAPPA3 / 4.0), ("absolu x 4", t0 / KAPPA3 * 4.0))
sortie["partie3"] = {}
for nom in ("Q-a  w2 = 2", "Q-c  w2 = 2", "Q-d  w2 = 2", "Q-e  w2 = 2.0001", "Q-f  w2 = 2.0001"):
    rec = points[nom]
    sortie["partie3"][nom] = mandataire(nom[:4], F(rec["w2"]), rec["g"], rec["m_bord"], rec["ln_G1"], regles)
print("  -- sur la grille, regle en absolu seule, g vise 1e-03, les deux signes")
regle_abs = lambda d, t0: (("depot : |w2 - 2|", abs(d)), ("absolu : t_0 / kappa_3", t0 / KAPPA3))
for rec in grille:
    if rec["g_vise"] == 1e-3:
        nom = "k=%.3f%s" % (rec["kappa_vise"], "-" if rec["d"] < 0 else "+")
        sortie["partie3"][nom] = mandataire(nom, F(rec["w2"]), rec["g"], rec["m_bord"], rec["ln_G1"], regle_abs)
print()
print("=== RESUME du mandataire, regle en absolu (eta0 = g X(w2) / (P kappa_3), ecrit a six chiffres)")
for nom, L in sortie["partie3"].items():
    for e in L:
        if e["regle"].startswith("absolu : "):
            A_ = e["absorbeurs"]
            print("    %-18s eta0 = %.5e  eta0 / g = %.4f  r_c = %d  %s  fenetres k0 : A %+d B %+d C %+d D %+d  plus grand |ln(X / A)| %.4f  poids >= %.3f" % (
                nom, e["eta0"], e["eta0_sur_g"], e["r_c"], "QUALIFIE" if e["qualifie"] else "NON QUALIFIE", A_["A"]["k0"], A_["B"]["k0"], A_["C"]["k0"], A_["D"]["k0"],
                max(abs(math.log(A_[a]["valeur"] / A_["A"]["valeur"])) for a in "BCD"), min(A_[a]["poids_min_fenetre"] for a in "ABCD")))
nq = [nom for nom, L in sortie["partie3"].items() for e in L if e["regle"].startswith("absolu : ") and not e["qualifie"]]
nd = [nom for nom, L in sortie["partie3"].items() for e in L if e["regle"].startswith("depot") and e["eta0"] != 0.0 and not e["qualifie"]]
tous = [nom for nom, L in sortie["partie3"].items()]
print("regle en absolu : %d points sur %d qualifies par le mandataire ; non qualifies : %s" % (len(tous) - len(nq), len(tous), nq if nq else "aucun"))
print("regle du depot  : non qualifies par le mandataire (hors w2 = 2, ou elle est degeneree) : %s" % (nd if nd else "aucun"))
json.dump(sortie, open(SORTIE, "w"), indent=1, sort_keys=True, default=str)
print()
print("ecrit %s" % SORTIE)
