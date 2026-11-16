# -*- coding: ascii -*-
"""DEPENDANCE A LA DEFINITION DU HAMILTONIEN EFFECTIF -- machine 1, v1, 2026-11-16. Chaines a une dimension ; aucun calcul 2D.
La chaine jugee par le gel est la forme SYMETRIQUE (Lowdin) tronquee a l'ordre 3. Ici, UNE autre definition, tronquee au
meme ordre : la forme de BLOCH (non hermitienne), ou tous les denominateurs d'un element <a|H|b> sont comptes de l'energie
du ket b :
  ordre 2 : somme_q V_aq V_qb / (E_b - E_q)
  ordre 3 : somme_{q,q'} V_aq V_qq' V_q'b / ((E_b - E_q)(E_b - E_q'))  -  somme_{q,c} V_aq V_qc V_cb / ((E_b - E_q)(E_c - E_q))
(q, q' hors de l'echelle ; c sur l'echelle). La forme symetrique est la demi-somme de la matrice de Bloch et de sa
transposee. Les deux definitions ont le meme spectre a tous les ordres ; tronquees a l'ordre 3 elles different a l'ordre 4.
Les boucles sont celles des blocs d'ordre 2 et 3, recopiees, les deux moities des denominateurs gardees a part.
Controles : (C1) demi-somme des deux moities = tables symetriques ; (C2) l'ecart d'energie entre les deux chaines varie
comme g^4 quand g tend vers 0 (pentes locales, a barriere tenue) ; (D) diagnostic a un etat : taille des deux moities le
long de l'echelle, et largeur de chaque forme aux quatre forces d'absorbeur de la chaine ; puis l'ecart des largeurs, ln(G_Bloch / G_sym), aux etats du domaine des points deja joues et aux etiquettes
predites du domaine des douze cellules. Largeur lue : -2 Im de la valeur propre, pour les deux formes.
Usage : python3 -I definition_bloch_machine1_v1.py <moteur> <bloc2> <bloc3> <feuille retrospective.json> <ancres
        retrospectif.json> <table du gel.json> <sortie.json> <eligibilite_*.json> [...]"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
MOTEUR, BLOC2, BLOC3, RETRO, ANCRES, TABLE, SORTIE = sys.argv[1:8]; ENTREES = sys.argv[8:]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):
    c = (k, l, n1, n2, w2)
    if c not in _cache:
        _cache[c] = _brut(p, k, l, n1, n2, w2)
    return _cache[c]
M.X_saut_reel = _X
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec")); exec(compile(open(BLOC3, encoding="ascii").read(), BLOC3, "exec"))
EF = 0.0625

def moities(n1, n2, w2, g, tb):
    """Pour s = 1, 3, 5 et pour le saut au second voisin (s = 2) : haut[s][m] = <m|H|m+s> (ket m+s), bas[s][m] = <m+s|H|m> (ket m)."""
    w = float(w2); w1 = float(M.W1); c0, c1 = M.CANAL; d = tb["d"]; m_min, Mh = tb["m_min"], tb["Mh"]
    def V(k, l, a, b):
        if a < 0 or b < 0 or a + k < 0 or b + l < 0 or abs(k) + abs(l) > M.P or (k == 0 and l == 0):
            return 0.0
        return (g / M.P) * M.X_saut_reel(M.P, k, l, float(a), float(b), w2)
    def e(k, l):
        return -w1 * k + w * l
    def sur_echelle(k, l):
        return k * c1 == l * c0 and k % c0 == 0
    def t_voisin(m):
        if m < m_min:
            return 0.0
        return V(c0, c1, n1 + c0 * m, n2 + c1 * m)
    haut = {s: {} for s in (1, 2, 3, 5)}; bas = {s: {} for s in (1, 2, 3, 5)}
    for m in range(m_min, Mh + 1):
        a, b = n1 + c0 * m, n2 + c1 * m
        uh = ub = 0.0                                  # ordre 2, second voisin (boucle du bloc d'ordre 2)
        for (k, l) in SAUTS_HORS_ECHELLE:
            v = V(k, l, a, b)
            if v == 0.0:
                continue
            ej = e(k, l); k2, l2 = 2 * c0 - k, 2 * c1 - l
            if abs(k2) + abs(l2) <= M.P and (k2, l2) != (c0, c1):
                x = v * V(k2, l2, a + k, b + l); ub += x / (-ej); uh += x / (2.0 * d - ej)
        haut[2][m], bas[2][m] = uh, ub
        for s in (1, 3, 5):                            # ordre 3 (boucles du bloc d'ordre 3)
            h = bs = 0.0
            for (k1, l1) in PAS_IMPAIRS:
                if sur_echelle(k1, l1):
                    continue
                v1 = V(k1, l1, a, b)
                if v1 == 0.0:
                    continue
                e1 = e(k1, l1)
                for (k2, l2) in PAS_IMPAIRS:
                    K, L = k1 + k2, l1 + l2
                    if sur_echelle(K, L):
                        continue
                    k3, l3 = s * c0 - K, s * c1 - L
                    if abs(k3) + abs(l3) > M.P or (k3 + l3) % 2 != M.P % 2:
                        continue
                    v2 = V(k2, l2, a + k1, b + l1)
                    if v2 == 0.0:
                        continue
                    v3 = V(k3, l3, a + K, b + L)
                    if v3 == 0.0:
                        continue
                    e2 = e(K, L); x = v1 * v2 * v3
                    bs += x / ((-e1) * (-e2)); h += x / ((s * d - e1) * (s * d - e2))
            for j in (0, 2, -2):                       # m -> l -> m'' -> m + s : denominateurs comptes de m + s (ket m + s)
                if abs((m + j) - (m + s)) != 1 or m + j < m_min:
                    continue
                tv = t_voisin(min(m + j, m + s))
                if tv == 0.0:
                    continue
                for (k1, l1) in PAS_IMPAIRS:
                    if sur_echelle(k1, l1):
                        continue
                    v1 = V(k1, l1, a, b)
                    if v1 == 0.0:
                        continue
                    v2 = V(j * c0 - k1, j * c1 - l1, a + k1, b + l1)
                    if v2 == 0.0:
                        continue
                    e1 = e(k1, l1)
                    h += -v1 * v2 * tv / ((s * d - e1) * (j * d - e1))
            for mm in (m + 1, m - 1):                  # m -> m'' -> l -> m + s : denominateurs comptes de m (ket m)
                j = (m + s) - mm
                if j not in (0, 2, -2) or mm < m_min:
                    continue
                tv = t_voisin(min(m, mm))
                if tv == 0.0:
                    continue
                aa, bb2 = n1 + c0 * mm, n2 + c1 * mm
                for (k1, l1) in PAS_IMPAIRS:
                    if sur_echelle(k1, l1):
                        continue
                    v1 = V(k1, l1, aa, bb2)
                    if v1 == 0.0:
                        continue
                    v2 = V(j * c0 - k1, j * c1 - l1, aa + k1, bb2 + l1)
                    if v2 == 0.0:
                        continue
                    e1 = e(k1, l1)
                    bs += -tv * v1 * v2 / ((-(mm - m) * d - e1) * (-e1))
            haut[s][m], bas[s][m] = h, bs
    return haut, bas

def chaine(tb, haut, bas, forme, eta_facteur=EF):
    """forme "bloch" : <m|H|m+s> = haut, <m+s|H|m> = bas ; forme "sym" : la demi-somme des deux, des deux cotes."""
    d, Mh, m_min = tb["d"], tb["Mh"], tb["m_min"]; eta_c = abs(d) * eta_facteur; debut_cap = tb["m2_bord"] + tb["b_M"] // 2
    n = Mh - m_min + 1; H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min; H[i, i] = m * d + (tb["S"][m] - tb["S"][0])
        if m > debut_cap:
            Wd[i] = eta_c * (m - debut_cap) ** 2; H[i, i] += -1j * Wd[i]
        for s in (1, 2, 3, 5):
            if m + s > Mh:
                continue
            base = tb["t"][m] if s == 1 else 0.0
            if forme == "bloch":
                H[i, i + s] = base + haut[s][m]; H[i + s, i] = base + bas[s][m]
            else:
                x = base + 0.5 * (haut[s][m] + bas[s][m]); H[i, i + s] = x; H[i + s, i] = x
    val, vec = np.linalg.eig(H); recs = np.abs(vec[-m_min, :]) ** 2; nu = np.lexsort((val.real, -recs))[0]; psi2 = np.abs(vec[:, nu]) ** 2
    chaine.flux = float(2.0 * (Wd @ psi2) / psi2.sum())          # lecture par le flux : n'a de sens que pour la forme symetrique
    return float(-2.0 * val[nu].imag), float(val[nu].real + tb["S"][0])

def etat(w2, g, a, b, sites=None):
    sites = M.barriere(float(a), float(b), w2, g, True) if sites is None else sites
    tb = tables_ordre2(float(a), float(b), w2, g, sites, M_facteur=4); t3 = tables_ordre3(float(a), float(b), w2, g, tb); h, bs = moities(float(a), float(b), w2, g, tb)
    ec = 0.0                                           # C1 : demi-somme des moities contre les tables symetriques
    for s, T in ((1, t3["T3"]), (2, tb["U"]), (3, t3["W3"]), (5, t3["W5"])):
        for m in T:
            x = 0.5 * (h[s][m] + bs[s][m])
            if T[m] != 0.0 or x != 0.0:
                ec = max(ec, abs(x - T[m]) / max(abs(T[m]), 1e-300))
    Gs, Es = chaine(tb, h, bs, "sym"); Fs = chaine.flux; Gb, Eb = chaine(tb, h, bs, "bloch"); G3 = gamma_chaine_ordre3(tb, t3, EF)
    return {"G_sym": Gs, "G_sym_flux": Fs, "G_bloch": Gb, "E_sym": Es, "E_bloch": Eb, "ecart_tables": ec, "G_im_bloc": G3["Gamma_im"], "G_flux_bloc": G3["Gamma_flux"], "sites": sites}

def med(v):
    v = sorted(v); n = len(v); return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])
out = {}
# --- C2 : loi d'echelle de l'ecart d'energie, a barriere tenue ---
w2 = F(387, 200); g0 = float(M.g_du_point(w2)); ref = etat(w2, g0, 7, 2); ecarts = []
for f in (0.03125, 0.0625, 0.125, 0.25, 0.5, 1.0):
    r = etat(w2, g0 * f, 7, 2, sites=ref["sites"]); ecarts.append((f, abs(r["E_bloch"] - r["E_sym"])))
pentes = [math.log(ecarts[i + 1][1] / ecarts[i][1]) / math.log(2.0) for i in range(len(ecarts) - 1)]
print("C2 (w2 = 387/200, etiquette (7,2), barriere tenue) : |E_Bloch - E_sym| aux couplages x%s : %s" % (" x".join("%g" % x[0] for x in ecarts), " ".join("%.2e" % x[1] for x in ecarts)))
print("     pentes locales (d'un couplage au double) : %s ; attendue : 4 a petit couplage" % " ".join("%.2f" % x for x in pentes))
out["C2"] = {"ecarts": ecarts, "pentes": pentes}
# --- D : diagnostic a un etat deja joue (C2 du delta 98, w2 = 97/50, facteur 3/4, etiquette (9,2)) ---
w2 = F(97, 50); g = float(M.g_du_point(w2)) * 0.75; sites = M.barriere(9.0, 2.0, w2, g, True)
tb = tables_ordre2(9.0, 2.0, w2, g, sites, M_facteur=4); t3 = tables_ordre3(9.0, 2.0, w2, g, tb); h, bs = moities(9.0, 2.0, w2, g, tb); mb = tb["m2_bord"]; cap = mb + tb["b_M"] // 2
r_bord = (abs(h[1][mb]) / abs(t3["T3"][mb]), abs(bs[1][mb]) / abs(t3["T3"][mb])); m_un = min(m for m in range(0, tb["Mh"]) if abs(h[1][m]) > abs(tb["t"][m]))
gs = [chaine(tb, h, bs, "sym", x)[0] for x in (0.25, 0.125, 0.0625, 0.03125)]; gb = [chaine(tb, h, bs, "bloch", x)[0] for x in (0.25, 0.125, 0.0625, 0.03125)]
print("D  etat (9,2) de C2 : dernier site de la barriere m = %d, debut de l'absorbeur m = %d, fin de l'echelle m = %d" % (mb, cap, tb["Mh"]))
print("     correction du saut au dernier site de la barriere, en parts du saut : symetrique %+.4f ; moitie haute %+.4f ; moitie basse %+.4f (rapports a la symetrique : %.1f et %.1f)" % (
    t3["T3"][mb] / tb["t"][mb], h[1][mb] / tb["t"][mb], bs[1][mb] / tb["t"][mb], r_bord[0], r_bord[1]))
print("     au debut de l'absorbeur : moitie haute %+.3f, moitie basse %+.3f du saut ; la moitie haute depasse le saut lui-meme a partir de m = %d" % (h[1][cap] / tb["t"][cap], bs[1][cap] / tb["t"][cap], m_un))
print("     saut au second voisin au dernier site de la barriere : moitie haute %+.2f, moitie basse %+.2f fois la valeur symetrique" % (h[2][mb] / tb["U"][mb], bs[2][mb] / tb["U"][mb]))
print("     largeur (-2 Im) aux forces d'absorbeur 1/4, 1/8, 1/16, 1/32 : symetrique %s (plus grande / plus petite %.3f) ; Bloch %s (plus grande / plus petite %.2f)" % (
    " ".join("%.3e" % x for x in gs), max(gs) / min(gs), " ".join("%.3e" % x for x in gb), max(gb) / min(gb)))
out["D"] = {"m_bord": mb, "debut_absorbeur": cap, "rapports_bord": r_bord, "m_moitie_depasse_saut": m_un, "G_sym": gs, "G_bloch": gb, "U_haut": h[2][mb] / tb["U"][mb], "U_bas": bs[2][mb] / tb["U"][mb]}
_cache.clear()
# --- les etats du domaine des points deja joues ---
D = json.load(open(RETRO)); A = json.load(open(ANCRES)); DEPg = {}
rows = []; pire_tab = 0.0; pire_bloc = 0.0; pire_flux = 0.0
for c in D["cellules"]:
    for r in c["etats"]:
        if r["exclu"] is None and r["dans_le_domaine"]:
            x = etat(F(c["w2"]), c["g"], r["n1"], r["n2"]); pire_tab = max(pire_tab, x["ecart_tables"]); pire_bloc = max(pire_bloc, abs(x["G_sym"] / x["G_im_bloc"] - 1.0)); pire_flux = max(pire_flux, abs(x["G_sym_flux"] / x["G_flux_bloc"] - 1.0))
            rows.append({"id": c["id"], "delta": c["delta"], "rang": r["rang"], "ln_B_S": math.log(x["G_bloch"] / x["G_sym"]), "ln_q3": r["ln_q3"],
                         "ln_q3_bloch": r["ln_q3"] + math.log(x["G_bloch"] / x["G_sym"]) + math.log(x["G_sym"] / r["G3"]), "flux_sur_im": x["G_flux_bloc"] / x["G_im_bloc"]})
            _cache.clear()
print("C1 : demi-somme des deux moities contre les tables symetriques des blocs, pire ecart relatif %.1e ; ma chaine symetrique contre celle du bloc, largeur lue par le flux : pire ecart relatif %.1e" % (pire_tab, pire_flux))
print("     la lecture -2 Im, seule possible pour la forme de Bloch, est plus bruitee : dans le bloc lui-meme, flux / (-2 Im) va de %.4f a %.4f ; entre ma chaine symetrique et le bloc, -2 Im s'ecarte d'au plus %.1e" % (
    min(r["flux_sur_im"] for r in rows), max(r["flux_sur_im"] for r in rows), pire_bloc))
print("POINTS DEJA JOUES, etats du domaine : ln(G_Bloch / G_sym), puis |ln q3| de la forme symetrique et de la forme de Bloch (plateau du run ter)")
for pid in sorted(set(r["id"] for r in rows)):
    v = [r for r in rows if r["id"] == pid]
    print("  %-3s delta %+.2f : %2d etats ; ln(G_Bloch / G_sym) de %+.4f a %+.4f ; |ln q3| mediane : symetrique %.4f, Bloch %.4f ; plus grand : symetrique %.4f, Bloch %.4f" % (
        pid, v[0]["delta"], len(v), min(r["ln_B_S"] for r in v), max(r["ln_B_S"] for r in v), med([abs(r["ln_q3"]) for r in v]), med([abs(r["ln_q3_bloch"]) for r in v]),
        max(abs(r["ln_q3"]) for r in v), max(abs(r["ln_q3_bloch"]) for r in v)))
print("  les %d etats : |ln(G_Bloch / G_sym)| mediane %.4f, plus grand %.4f ; Bloch plus pres du plateau que la forme symetrique a %d etats" % (
    len(rows), med([abs(r["ln_B_S"]) for r in rows]), max(abs(r["ln_B_S"]) for r in rows), sum(abs(r["ln_q3_bloch"]) < abs(r["ln_q3"]) for r in rows)))
out["joues"] = rows; out["C1"] = {"pire_ecart_tables": pire_tab, "pire_ecart_chaine_im": pire_bloc, "pire_ecart_chaine_flux": pire_flux}
# --- les douze cellules, etiquettes predites du domaine ---
cells = []
for f in ENTREES:
    cells += json.load(open(f))["cellules"]
print("DOUZE CELLULES, etiquettes predites du domaine : ln(G_Bloch / G_sym)")
out["cellules"] = []
for pt in json.load(open(TABLE))["points"]:
    if pt["role"] != "juge":
        continue
    c = [x for x in cells if F(x["w2"]) == F(pt["w2"]) and F(x["facteur"]) == F(pt["facteur"])][0]; v = []
    for s in c["etats"]:
        if s["rang_predit"] is None or s["rang_predit"] >= 14 or s["vide"]:
            continue
        if s["e_bord"] < 0.7 and s["stab3"] is not None and s["stab3"] <= 0.05 and s["stable1"] and s["stable2"] and s["G3"] > 1.33e-12:
            x = etat(F(pt["w2"]), c["g"], s["n1"], s["n2"]); v.append(math.log(x["G_bloch"] / x["G_sym"])); pire_tab = max(pire_tab, x["ecart_tables"]); _cache.clear()
    out["cellules"].append({"id": pt["id"], "n": len(v), "min": min(v), "max": max(v), "mediane": med(v)})
    print("  %-3s %2d etats : de %+.4f a %+.4f, mediane %+.4f" % (pt["id"], len(v), min(v), max(v), med(v)), flush=True)
out["C1"]["pire_ecart_tables"] = pire_tab
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
