# -*- coding: ascii -*-
"""ELIGIBILITE DES CELLULES CANDIDATES DU GEL "SOMMET" -- machine 1, v1, 2026-11-22.
CHAINE SEULE : aucun calcul 2D, ni dense ni creux. Etat : celui que porte le site (0, 0).
Derive de eligibilite_vide_machine1_v1.py (registre) : memes moteur, blocs, plateau et etendue ; les cellules, la
profondeur cible, la regle de la barriere vide, M_facteur et le seuil d'etendue sont ceux de ce gel.
Une CELLULE est un couple (w2, kappa). Ses trois nombres ecrits :
    g    = kappa |w2 - 2| P / X(w2),  X(w2) = X_saut_reel(P, 2, 1, 0, 0, w2) du moteur, ecrit "%.5e" : le couplage EST ce decimal ;
    eta0 = max(|w2 - 2|, g X(w2) / (P kappa_3)), kappa_3 = 0.0262, g etant le couplage ECRIT, ecrit "%.5e" ;
    r_c  = 2 (m_bord + max(8, m_bord)) + 2.
Barriere : sites = barriere(0, 0, w2, g, avec Sigma2) du moteur. Si la liste est VIDE : m_bord = 0, e_bord = 0, et les
tables recoivent sites = [(0, 0.0, |t_site(0, 0, 0, w2, g)|)]. Sinon m_bord et e_bord sont ceux de son dernier site.
Tables des blocs deposes d'ordre 2 et 3 avec M_facteur = 5 ; plateau G3* et etendue de la chaine d'ordre 3 sous
l'absorbeur adapte (plateau_adapte du bloc depose, dix-huit variantes), tels quels.
La cellule est ELIGIBLE si m_bord = la profondeur cible de son kappa, si e_bord < 0.7, si les dix-huit largeurs sont
strictement positives et si leur etendue est <= 0.005. Un w2 est ELIGIBLE si ses SEPT cellules le sont.
CONSIGNE (ne decide de rien) : le plateau d'ordre 2 (meme bloc), le plateau du premier ordre sous les memes dix-huit
variantes (flux), le premier site m* ou le saut depasse 1, le poids du site 0.
Usage : python3 -I -B eligibilite_sommet_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <sortie.json> <creneau> [...]"""
import sys, math, json, time, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A, SORTIE = sys.argv[1:6]
ARGS = sys.argv[6:]
CANONS = {"moteur": "82a0be882568fe0c", "bloc2": "7cd5977bc27bebc1", "bloc3": "534ba246aa3b8973", "bloc_adapte": "49a40d9098b55361"}
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
for nom, chemin in (("moteur", MOTEUR), ("bloc2", BLOC2), ("bloc3", BLOC3), ("bloc_adapte", BLOC_A)):
    if canon_B(chemin) != CANONS[nom]:
        raise SystemExit("REFUS : %s n'est pas au canon %s" % (nom, CANONS[nom]))
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
assert M.P == 5 and tuple(M.CANAL) == (2, 1) and M.W1 == 1
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):                    # memoire des appels : memes valeurs, moins de calcul
    cle = (p, k, l, n1, n2, w2)
    if cle not in _cache:
        _cache[cle] = _brut(p, k, l, n1, n2, w2)
    return _cache[cle]
M.X_saut_reel = _X
for bloc in (BLOC2, BLOC3, BLOC_A):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))

PAS = F(1, 100000)                               # les w2 candidats sont au cent-millieme ; |w2 - 2| = 0.0005 n'en est pas
CRENEAUX = {"MP": sorted(F(2) - k * PAS for k in range(5, 21) if k != 10), "PP": sorted(F(2) + k * PAS for k in range(5, 21) if k != 10),
            "MG": sorted(F(2) - k * PAS for k in range(25, 50)), "PG": sorted(F(2) + k * PAS for k in range(25, 50))}
ORDRE = ("MP", "PP", "MG", "PG")
KAPPAS = (("0.0363", 2), ("0.0530", 1), ("0.0800", 0), ("0.1300", 0), ("0.2000", 0), ("0.4000", 0), ("1.0000", 0))   # (kappa, profondeur cible)
KAPPA3 = "0.0262"
SEUIL_ETENDUE = 0.005; GARDE_E_BORD = 0.7; M_FACTEUR = 5

def nombres_ecrits(w2, kappa):
    """Le couplage et l'echelle de l'absorbeur de la cellule : les decimaux a six chiffres significatifs."""
    X = _brut(M.P, M.CANAL[0], M.CANAL[1], 0.0, 0.0, w2); d = abs(float(w2) - 2.0)
    g_txt = "%.5e" % (float(F(kappa)) * d * M.P / X); g = float(g_txt)
    eta_txt = "%.5e" % max(d, g * X / (M.P * float(F(KAPPA3))))
    return g_txt, g, eta_txt

def plateau_ordre1(tb):
    """Premier ordre (sauts t_m seuls, diagonale m delta) sous les dix-huit variantes de l'absorbeur adapte ; lecture par le flux."""
    d, m_min = tb["d"], tb["m_min"]; v = []
    for (a, c, L) in VARIANTES_ADAPTEES:
        debut = tb["m2_bord"] + c; Mh = debut + L; n = Mh - m_min + 1
        H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
        for m in range(m_min, Mh + 1):
            i = m - m_min; H[i, i] = m * d
            if m > debut:
                Wd[i] = a * abs(tb["t"][m]) * ((m - debut) / float(L)) ** 2; H[i, i] += -1j * Wd[i]
            if m < Mh:
                H[i, i + 1] = tb["t"][m]; H[i + 1, i] = tb["t"][m]
        val, vec = np.linalg.eig(H); poids = np.abs(vec[-m_min, :]) ** 2; nu = np.lexsort((val.real, -poids))[0]
        psi2 = np.abs(vec[:, nu]) ** 2; v.append(math.log(float(2.0 * (Wd @ psi2) / psi2.sum())))
    s = sorted(v); return 0.5 * (s[8] + s[9])

def cellule(w2, kappa, cible):
    g_txt, g, eta_txt = nombres_ecrits(w2, kappa)
    rec = {"kappa": kappa, "cible": cible, "g": g_txt, "eta0": eta_txt}
    sites = M.barriere(0.0, 0.0, w2, g, True); vide = not sites
    if vide:
        sites = [(0, 0.0, abs(M.t_site(0, 0.0, 0.0, w2, g)))]
    m_bord, e_bord = sites[-1][0], sites[-1][1]
    rec.update({"barriere_vide": vide, "m_bord": m_bord, "e_bord": e_bord, "r_c": 2 * (m_bord + max(8, m_bord)) + 2})
    tb = tables_ordre2(0.0, 0.0, w2, g, sites, M_facteur=M_FACTEUR); t3 = tables_ordre3(0.0, 0.0, w2, g, tb)
    pl = plateau_adapte(tb, t3, 3); p2 = plateau_adapte(tb, t3, 2); l1 = plateau_ordre1(tb)
    d = abs(float(w2) - 2.0)
    rec.update({"ln_G3": pl["ln_G"], "etendue": pl["etendue"], "poids_min": pl["poids_min"], "methodes": sorted(set(x[:2] for x in pl["methodes"])),
                "ln_Phi": None if pl["ln_G"] is None else pl["ln_G"] - math.log(d), "ln_G2": p2["ln_G"], "ln_G1": l1,
                "m_etoile": next(m for m in range(1, 4000) if abs(M.t_site(m, 0.0, 0.0, w2, g)) > 1.0)})
    motifs = []
    if m_bord != cible: motifs.append("barriere a %d barreaux" % m_bord)
    if not e_bord < GARDE_E_BORD: motifs.append("e_bord %.3f" % e_bord)
    if pl["ln_G"] is None: motifs.append("largeur non positive")
    elif not pl["etendue"] <= SEUIL_ETENDUE: motifs.append("etendue %.4f" % pl["etendue"])
    rec["eligible"] = not motifs
    if motifs: rec["motif"] = " ; ".join(motifs)
    return rec

assert ARGS and all(s in CRENEAUX for s in ARGS), "creneaux : MP PP MG PG"
assert [len(CRENEAUX[s]) for s in ORDRE] == [15, 15, 25, 25]
out = {"regle": {"kappas": KAPPAS, "kappa_3": KAPPA3, "seuil_etendue": SEUIL_ETENDUE, "garde_e_bord": GARDE_E_BORD, "M_facteur": M_FACTEUR,
                 "variantes": VARIANTES_ADAPTEES, "seuil_flux": SEUIL_FLUX_ADAPTE, "chiffres": CHIFFRES_ADAPTE}, "creneaux": {}}
t0 = time.time()
for s in ARGS:
    cands = []
    print("creneau %s : %d w2 candidats" % (s, len(CRENEAUX[s])), flush=True)
    for w2 in CRENEAUX[s]:
        _cache.clear()
        cs = [cellule(w2, kappa, cible) for (kappa, cible) in KAPPAS]
        el = all(c["eligible"] for c in cs)
        cands.append({"w2": "%d/%d" % (w2.numerator, w2.denominator), "eligible": el, "cellules": cs})
        print("  %.5f  %s  %s" % (float(w2), "  ".join("%s %s %s%s" % (c["kappa"], c["g"], ("%.4f" % c["etendue"]) if c.get("etendue") is not None else "----",
              "" if c["eligible"] else " !") for c in cs), "ELIGIBLE" if el else "INELIGIBLE"), flush=True)
    out["creneaux"][s] = {"candidats": cands}
    print("  -> %d w2 eligibles sur %d ; %.0f s" % (sum(c["eligible"] for c in cands), len(cands), time.time() - t0), flush=True)
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit : %s" % SORTIE)
