# -*- coding: ascii -*-
"""TABLE GELEE DES CELLULES DU GEL "LARGEUR DU VIDE", AVEC LEURS PREDICTIONS -- machine 1, v1, 2026-11-16.
CHAINES A UNE DIMENSION SEULEMENT : aucun calcul 2D. Rejoue le tirage (script de la premiere partie, en sous-processus),
puis, a chaque cellule tiree (w2, m, couplage ecrit g) :
  - barriere du moteur, e_bord, r_c = 2 (m + max(8, m)) + 2, eta0 = |w2 - 2| ;
  - G3* et son etendue (chaine d'ordre 3 sous absorbeur adapte, bloc de la premiere partie, dix-huit variantes) ;
  - G2* (ordre 2, meme absorbeur) et G1* (premier ordre : sauts t_m seuls, ni decalage ni second voisin, meme absorbeur) ;
  - Phi* : la chaine de la limite du desaccord nul (w2 = 2, unites de |delta|, sauts kappa tau_m / tau_0, meme absorbeur),
    au kappa de la cellule ; r3 = ln(G3* / (|delta| Phi*)) : ce que la chaine ajoute a la loi d'echelle ;
  - la forme fermee a trois termes de la note sur la loi d'echelle : ln Phi = -B M0 + c ln M0 + d ;
  - la tolerance de sa ligne ; et, pour l'annonce de la plume, DEUX lectures du residu ln(G3* / Gamma_plateau) tirees des etats
    deja joues : (a) il a le signe de delta ; (b) la chaine manque une part f de sa correction, soit - f / (1 - f) r3, f etant
    la part manquee aux etats deja joues. Aux etats joues les deux lectures donnent le meme signe ; au vide elles peuvent differer.
Usage : python3 -I -B predictions_vide_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <tirage_vide.py>
        <graine> <table machine 1.json> <table machine 2.json> <forme_phi_v1.json> <superposition_v1.json>
        <verifie_variantes_joues_v1.json> <sortie table.json>"""
import sys, os, re, math, json, subprocess, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
(MOTEUR, BLOC2, BLOC3, BLOC_A, TIRAGE, GRAINE, TABLE1, TABLE2, FORME, SUPER, VERIF, SORTIE) = sys.argv[1:13]
CANONS = {"moteur": "82a0be882568fe0c", "bloc2": "7cd5977bc27bebc1", "bloc3": "534ba246aa3b8973", "bloc_adapte": "49a40d9098b55361",
          "tirage": "cc1b2df637a9f3cd", "table1": "7b278d2b5a34d0a3", "table2": "84bffbbd2f675181", "forme": "2e2ed5b9b745790c",
          "superposition": "aeb9fc40ecc43899"}
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
for nom, chemin in (("moteur", MOTEUR), ("bloc2", BLOC2), ("bloc3", BLOC3), ("bloc_adapte", BLOC_A), ("tirage", TIRAGE), ("table1", TABLE1),
                    ("table2", TABLE2), ("forme", FORME), ("superposition", SUPER)):
    if canon_B(chemin) != CANONS[nom]:
        raise SystemExit("REFUS : %s n'est pas au canon %s (%s)" % (nom, CANONS[nom], canon_B(chemin)))
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
LISIBLES = (3, 4, 5, 6); TOL = {"lisible": 0.02, "profonde": 0.05}

# --- le tirage, rejoue par le script de la premiere partie ---
r = subprocess.run([sys.executable, "-I", "-B", TIRAGE, GRAINE, TABLE1, TABLE2], capture_output=True, text=True)
if r.returncode != 0 or not re.search(r"^TIRAGE : \d+ cellules", r.stdout, re.M):
    raise SystemExit("REFUS : le tirage n'a pas abouti\n" + r.stdout)
rangs = {m.group(1): int(m.group(2)) for m in re.finditer(r"^creneau (\S+)\s+rang (\d) : .* ELIGIBLE, retenu$", r.stdout, re.M)}
tires = [m.groups() for m in re.finditer(r"^\s+(\S+)\s+w2 = (\S+)\s+m = (\d+)\s+g = (\S+)\s+(lisible|profonde)$", r.stdout, re.M)]
n_annonce = int(re.search(r"^TIRAGE : (\d+) cellules", r.stdout, re.M).group(1))
assert len(tires) == n_annonce and sorted(rangs) == ["MG", "MP", "PG", "PP"], (len(tires), n_annonce, rangs)

def largeur_de(H, Wd, i0, echelle):
    """Meme regle que le bloc : flux en double precision tant que flux / echelle > seuil, sinon precision arbitraire."""
    val, vec = np.linalg.eig(H)
    poids = np.abs(vec[i0, :]) ** 2; nu = np.lexsort((val.real, -poids))[0]
    psi2 = np.abs(vec[:, nu]) ** 2; flux = float(2.0 * (Wd @ psi2) / psi2.sum())
    if flux / echelle > SEUIL_FLUX_ADAPTE:
        return flux
    return float(-2 * _valeur_propre_mp(H, vec[:, nu])[0].imag)

def mediane_et_etendue(v):
    s = sorted(v); n = len(s)
    return 0.5 * (s[n // 2 - 1] + s[n // 2]), s[-1] - s[0]

def plateau_ordre1(tb):
    """Premier ordre a la cellule : diagonale m delta, sauts t_m, absorbeur adapte ; mediane des dix-huit ln Gamma."""
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
        v.append(math.log(largeur_de(H, Wd, -m_min, abs(d))))
    return mediane_et_etendue(v)

TAU2 = {}
def tau_limite(j):
    if j not in TAU2:
        TAU2[j] = _brut(M.P, M.CANAL[0], M.CANAL[1], float(M.CANAL[0] * j), float(M.CANAL[1] * j), F(2)) / M.P
    return TAU2[j]

def phi_etoile(kappa, signe):
    """Chaine de la limite sous l'absorbeur adapte ; rend (ln Phi*, etendue, dernier site de la barriere a la limite)."""
    t0 = tau_limite(0); T = lambda j: kappa * tau_limite(j) / t0
    m_bord = 0
    while (m_bord + 1) > 2.0 * T(m_bord + 1):
        m_bord += 1
    v = []
    for (a, c, L) in VARIANTES_ADAPTEES:
        debut = m_bord + c; Mh = debut + L; n = Mh + 1
        H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
        for j in range(n):
            H[j, j] = signe * j
            if j > debut:
                Wd[j] = a * abs(T(j)) * ((j - debut) / float(L)) ** 2; H[j, j] += -1j * Wd[j]
            if j < Mh:
                H[j, j + 1] = T(j); H[j + 1, j] = T(j)
        v.append(math.log(largeur_de(H, Wd, 0, 1.0)))
    med, et = mediane_et_etendue(v)
    return med, et, m_bord

# --- ce que la chaine a manque aux etats deja joues (apres coup ; sert a l'annonce, pas a un enonce) ---
SU = {(e["source"], e["id"], e["rang"]): e for e in json.load(open(SUPER))["etats"] if e["domaine"]}
VE = json.load(open(VERIF))["etats"]
par_cellule = {}
for e in VE:
    s = SU[(e["source"], e["id"], e["rang"])]
    par_cellule.setdefault((e["source"], e["id"]), []).append(-e["q_mediane"] / s["r"])      # part manquee : (r - r_chaine) / r
f_cellules = sorted(mediane_et_etendue(v)[0] if len(v) % 2 == 0 else sorted(v)[len(v) // 2] for v in par_cellule.values())
f_tous = sorted(x for v in par_cellule.values() for x in v)
F_MED = f_tous[len(f_tous) // 2]; F_MIN, F_MAX = f_cellules[0], f_cellules[-1]
print("part de la correction manquee par la chaine aux %d etats joues (absorbeur adapte) : mediane %.3f ; medianes par cellule de %.3f a %.3f ; signe positif a %d etats sur %d" % (
    len(f_tous), F_MED, F_MIN, F_MAX, sum(1 for x in f_tous if x > 0), len(f_tous)))

# --- la forme fermee ---
FP = json.load(open(FORME)); B_FF = 2.0 * FP["I"]
ref = [x for x in FP["B"] if (x["n1"], x["n2"], x["M0"]) == (0, 0, 4096)][0]; C_FF, D_FF = ref["c_L"], -ref["reste3"]
XC = M.coeff_homogene_X_s(F(2))

cellules = []
print("cellule  w2          m   g            m_bord e_bord  r_c  ln G3*      etendue  ln(G3*/G2*) ln(G3*/G1*)  r3       ferme-G3*  residu si sous-correction (f median, pire f)")
for (ident, w2s, ms, gs, ligne) in tires:
    _cache.clear()
    w2 = F(w2s); m = int(ms); g = float(gs); d = float(w2) - 2.0; s = 1 if d > 0 else -1
    sites = M.barriere(0.0, 0.0, w2, g, True); m_bord, e_bord = sites[-1][0], sites[-1][1]
    assert m_bord == m, (ident, m_bord, m)
    tb = tables_ordre2(0.0, 0.0, w2, g, sites, M_facteur=4); t3 = tables_ordre3(0.0, 0.0, w2, g, tb)
    p3 = plateau_adapte(tb, t3, 3); p2 = plateau_adapte(tb, t3, 2); l1, e1 = plateau_ordre1(tb)
    kappa = g * _brut(M.P, M.CANAL[0], M.CANAL[1], 0.0, 0.0, w2) / (M.P * abs(d))
    lphi, ephi, mb_lim = phi_etoile(kappa, s); assert mb_lim == m, (ident, mb_lim, m)
    r3 = p3["ln_G"] - math.log(abs(d)) - lphi
    lam = kappa * XC / (M.P * tau_limite(0)); M0 = (2.0 * lam) ** (-2.0 / 3.0)
    l_ferme = math.log(abs(d)) - B_FF * M0 + C_FF * math.log(M0) + D_FF
    r_c = 2 * (m + max(8, m)) + 2
    att = lambda f: -f / (1.0 - f) * r3
    rec = {"id": ident, "creneau": ident[:2], "ligne": ligne, "w2": w2s, "delta": d, "m": m, "g": gs, "kappa": kappa, "m_bord": m_bord, "e_bord": e_bord,
           "r_c": r_c, "eta0": abs(d), "N_max": r_c + 100,
           "ln_G3": p3["ln_G"], "etendue": p3["etendue"], "ln_G2": p2["ln_G"], "etendue_ordre2": p2["etendue"], "ln_G1": l1, "etendue_ordre1": e1,
           "ln_Phi_etoile": lphi, "etendue_Phi_etoile": ephi, "r3": r3, "M0": M0, "ln_forme_fermee": l_ferme, "tolerance": TOL[ligne],
           "attente": {"signe_de_delta": s, "sous_correction_mediane": att(F_MED), "sous_correction_pire": att(F_MAX)}}
    cellules.append(rec)
    print("%-7s  %-10s  %-2d  %s  %-6d %.3f   %-3d  %+.4f  %.4f   %+.4f     %+.4f      %+.4f  %+.4f    %+.4f, %+.4f" % (
        ident, w2s, m, gs, m_bord, e_bord, r_c, p3["ln_G"], p3["etendue"], p3["ln_G"] - p2["ln_G"], p3["ln_G"] - l1, r3, l_ferme - p3["ln_G"],
        rec["attente"]["sous_correction_mediane"], rec["attente"]["sous_correction_pire"]), flush=True)
table = {"gel": "largeur du vide", "graine": GRAINE, "rangs": rangs, "cellules": cellules,
         "canons": {"moteur": CANONS["moteur"], "bloc2": CANONS["bloc2"], "bloc3": CANONS["bloc3"], "bloc_adapte": CANONS["bloc_adapte"], "tirage": CANONS["tirage"],
                    "table_machine1": CANONS["table1"], "table_machine2": CANONS["table2"], "forme_phi": CANONS["forme"], "superposition": CANONS["superposition"],
                    "verification_joues": canon_B(VERIF)},
         "regle": {"tolerance": TOL, "absorbeurs_du_lecteur": [["A", "F2", 0, 80], ["B", "F2", 0, 100], ["C", "F1", 0, 100], ["D", "F2", 10, 80]], "barreaux": list(range(-3, 9)),
                   "r_c": "2 (m + max(8, m)) + 2", "eta0": "|w2 - 2|", "site": [0, 0], "E_depart": 0.0},
         "joues": {"etats": len(f_tous), "part_manquee_mediane": F_MED, "part_manquee_par_cellule_min": F_MIN, "part_manquee_par_cellule_max": F_MAX},
         "forme_fermee": {"B": B_FF, "c": C_FF, "d": D_FF, "X_c": XC}}
json.dump(table, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit %s : %d cellules (%d lisibles, %d profondes) ; canon %s" % (SORTIE, len(cellules), sum(c["ligne"] == "lisible" for c in cellules),
      sum(c["ligne"] == "profonde" for c in cellules), canon_B(SORTIE)))
