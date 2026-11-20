# --- BLOC CHAINE DU PONT (machine 1, v1, 2026-11-17) ---
# La chaine d'une cellule (w2, m) du gel "pont" : couplage ecrit, barriere, tables, et la DENSITE du site 0 hors de
# l'energie du vide, ordre 2 ou 3, aux dix-huit variantes de l'absorbeur adapte. Memes definitions que la premiere
# partie du gel (735ce41be200c5cd, sections 2 et 4) et que eligibilite_pont_machine1_v1.py (733369d4b82e0b1b).
# CHAINE SEULE : aucune 2D. Depend de M (moteur), np, math, F (Fraction) et des blocs deposes d'ordre 2, d'ordre 3 et de
# l'absorbeur adapte (tables_ordre2, tables_ordre3, VARIANTES_ADAPTEES, matrice_adaptee, plateau_adapte).
KAPPA_PONT = {3: "0.0262", 4: "0.0200", 5: "0.0159"}
ECARTS_PONT = (0.05, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0)
M_FACTEUR_PONT = 4

def couplage_pont(w2, m):
    """Le couplage ecrit de la cellule : decimal a six chiffres significatifs ("%.5e")."""
    brut = float(F(KAPPA_PONT[m])) * abs(float(w2) - 2.0) * M.P / M.X_saut_reel(M.P, M.CANAL[0], M.CANAL[1], 0.0, 0.0, w2)
    return "%.5e" % brut

def chaine_pont(w2, m, g_texte):
    """Barriere, tables et matrices des dix-huit variantes, ordres 2 et 3, pour la cellule (w2, m) au couplage ecrit."""
    g = float(g_texte)
    sites = M.barriere(0.0, 0.0, w2, g, True)
    tb = tables_ordre2(0.0, 0.0, w2, g, sites, M_facteur=M_FACTEUR_PONT); t3 = tables_ordre3(0.0, 0.0, w2, g, tb)
    assert abs(tb["d"] - (float(w2) - 2.0)) < 1e-15
    ch = {"w2": w2, "m": m, "g": g_texte, "delta": tb["d"], "m_bord": sites[-1][0], "e_bord": sites[-1][1],
          "tb": tb, "t3": t3, "var": {2: [], 3: []}}
    for ordre in (2, 3):
        for (a, c, L) in VARIANTES_ADAPTEES:
            H, Wd, i0 = matrice_adaptee(tb, t3, a, c, L, ordre)
            val, vec = np.linalg.eig(H); nu = np.lexsort((val.real, -np.abs(vec[i0, :]) ** 2))[0]
            ch["var"][ordre].append((H, Wd, i0, float(val[nu].real)))
    return ch

def ln_rho_pont(ch, xs, ordre=3):
    """Aux ecarts xs (en |delta|, du cote oppose au desaccord) : mediane et etendue des dix-huit ln rho du site 0.
    rho = -(1 / pi) Im [(E - H)^(-1)]_00 , E = E_v - x delta, lue par le flux (1 / pi) somme_m W_m |y_m|^2."""
    LN = []
    for (H, Wd, i0, Ev) in ch["var"][ordre]:
        e0 = np.zeros(len(H), dtype=complex); e0[i0] = 1.0; r = []
        for x in xs:
            y = np.linalg.solve((Ev - x * ch["delta"]) * np.eye(len(H)) - H, e0)
            v = float((Wd @ (np.abs(y) ** 2)) / math.pi)
            r.append(math.log(v) if (v > 0.0 and math.isfinite(v)) else None)
        LN.append(r)
    med, et = [], []
    for i in range(len(xs)):
        col = [r[i] for r in LN]
        if any(v is None for v in col):
            med.append(None); et.append(None); continue
        s = sorted(col); n = len(s); med.append(0.5 * (s[n // 2 - 1] + s[n // 2])); et.append(s[-1] - s[0])
    return med, et
# --- fin du bloc ---
