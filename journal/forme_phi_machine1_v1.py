# -*- coding: ascii -*-
"""FORME DE Phi QUAND LA BARRIERE DEVIENT PROFONDE -- machine 1, v1, 2026-11-16. Hors chaine, classe 3. Aucun 2D.
Variable sans etiquette : lambda = g X_c / (P |delta|), X_c coefficient dominant du moteur (coeff_homogene_X_s, w2 = 2) :
loin sur l'echelle t_m / |delta| -> lambda m^(5/2). Alors
  kappa = t_0 / |delta| = lambda P tau_0 / X_c ;   bout de barriere M0 = (2 lambda)^(-2/3) ;
  occupation de seuil classique du moteur nu0* = ((P-2)/P) (P lambda)^(-2/(P-2)), soit M0 = (5/2)^(2/3) (5/3) nu0*.
A. Constantes. Terme dominant attendu (WKB discret) : -ln Phi -> 2 I M0, I = integrale de 0 a 1 de arccosh(x^(-3/2)) dx.
B. A etiquette fixee : -ln Phi contre 2 I M0 - c_L ln M0, avec c_L = (18 + 19 n1 + 17 n2) / 11 (comptage WKB des
   logarithmes : -3 de kappa^2, -1 du point tournant, +3/2 de Stirling, +2 a_L du premier ecart de tau_m a m^(5/2)).
C. Exposant local p = -d ln(-ln Phi) / d ln kappa.
D. Graines a fraction f du seuil classique (occupations reelles (n1, n2) = f^2 nu0* ((D+2)^2 / (4 w2), 1), D = w2^2 - 1) :
   -ln Phi / nu0* de la chaine contre l'integrale WKB F(f) = 2 int arccosh(x / h(x ; f)) dx (h : saut double rapporte
   au desaccord, en variables x = m / nu0*).
E. Profondeur atteinte dans le domaine garde : a |delta| donne, -ln Phi au site ou m_bord |delta| vaut 0.3 et 0.7.
Usage : python3 -I forme_phi_machine1_v1.py <moteur> <phi_echelle.py> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import mpmath as mp
MOTEUR, PHI, SORTIE = sys.argv[1:4]
spec = importlib.util.spec_from_file_location("phi_echelle", PHI); PH = importlib.util.module_from_spec(spec); spec.loader.exec_module(PH)
M = PH.charger(MOTEUR)
P = M.P
XC = M.coeff_homogene_X_s(F(2))
_, L1, L2 = M.lambdas(F(2))
out = {"X_c": XC}

# --- A : constantes ---
mp.mp.dps = 30
I = float(mp.quad(lambda x: mp.acosh(x ** (-mp.mpf(3) / 2)), [0, mp.mpf(1) / 2, 1]))
RAPPORT_M0_NU = (5.0 / 2.0) ** (2.0 / 3.0) * (5.0 / 3.0)
out.update({"I": I, "M0_sur_nu0": RAPPORT_M0_NU, "constante_en_nu0": 2.0 * I * RAPPORT_M0_NU,
            "M0_sur_delta_sur_g_puissance_2_3": (P / (2.0 * XC)) ** (2.0 / 3.0), "constante_en_delta_sur_g": 2.0 * I * (P / (2.0 * XC)) ** (2.0 / 3.0),
            "poids_j2": 60.0 * L1 ** 2 * L2 ** 3 / XC, "poids_j4": 80.0 * L1 ** 4 * L2 / XC})
print("A. X_c(w2 = 2) = %.6f (parts %.6f et %.6f, soit 3/11 et 8/11) ; I = %.6f ; 2 I = %.6f" % (XC, out["poids_j2"], out["poids_j4"], I, 2 * I))
print("   M0 = %.5f nu0* = %.5f (|delta| / g)^(2/3) ; 2 I M0 = %.4f nu0* = %.4f (|delta| / g)^(2/3)" % (
    RAPPORT_M0_NU, out["M0_sur_delta_sur_g_puissance_2_3"], out["constante_en_nu0"], out["constante_en_delta_sur_g"]))

def kappa_de_lambda(lam, n1, n2):
    return lam * P * PH.tau(n1, n2, 0) / XC

def c_L(n1, n2):
    return (18.0 + 19.0 * n1 + 17.0 * n2) / 11.0

# --- B : a etiquette fixee ---
print()
print("B. a etiquette fixee : -ln Phi = 2 I M0 - c_L ln M0 - d_L + o(1) ?   c_L = (18 + 19 n1 + 17 n2) / 11")
print("   etiquette   c_L       M0      nu0*      kappa        m_bord   -ln Phi       / (2 I M0)   -ln Phi - 2 I M0   pente par doublement / ln 2   + c_L ln M0 (-> -d_L)")
out["B"] = []
for (n1, n2) in ((0, 0), (2, 1), (6, 2), (10, 3)):
    prec = None
    for M0 in (4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096):
        lam = 0.5 * M0 ** -1.5
        k = kappa_de_lambda(lam, n1, n2)
        f = PH.phi_fc(k, n1, n2)
        if f is None:
            print("   (%2d,%2d)   %7.4f  %5d   %8.3f  %.4e   barriere vide" % (n1, n2, c_L(n1, n2), M0, M0 / RAPPORT_M0_NU, k)); continue
        L = -f["ln_Phi"]; reste = L - 2 * I * M0
        pente = (reste - prec) / math.log(2.0) if prec is not None else None
        prec = reste
        out["B"].append({"n1": n1, "n2": n2, "c_L": c_L(n1, n2), "M0": M0, "nu0": M0 / RAPPORT_M0_NU, "lambda": lam, "kappa": k, "m_bord": f["m_bord"], "moins_ln_Phi": L,
                         "rapport": L / (2 * I * M0), "reste": reste, "pente_par_doublement": pente, "reste3": reste + c_L(n1, n2) * math.log(M0), "E": f["E"], "Z": f["Z"]})
        print("   (%2d,%2d)   %7.4f  %5d   %8.3f  %.4e   %5d   %12.4f   %.5f      %+11.4f        %s            %+9.4f" % (
            n1, n2, c_L(n1, n2), M0, M0 / RAPPORT_M0_NU, k, f["m_bord"], L, L / (2 * I * M0), reste, ("%+8.4f" % pente) if pente is not None else "    -   ", reste + c_L(n1, n2) * math.log(M0)))

# --- C : exposant local ---
print()
print("C. exposant local p = - d ln(-ln Phi) / d ln kappa (difference centree a 1 pour cent) ; attendu 2/3 quand kappa -> 0")
print("   etiquette   kappa      m_bord   -ln Phi      p        pente d ln Phi / d ln kappa")
out["C"] = []
for (n1, n2) in ((0, 0), (6, 2), (10, 3)):
    for k in (0.40, 0.30, 0.22, 0.15, 0.10, 0.06, 0.03, 0.01, 0.003, 0.001, 0.0003, 0.0001):
        f = PH.phi_fc(k, n1, n2)
        if f is None:
            continue
        a, b = PH.phi_fc(k * 1.01, n1, n2), PH.phi_fc(k / 1.01, n1, n2)
        if a is None or b is None:
            continue
        pente = (a["ln_Phi"] - b["ln_Phi"]) / (2 * math.log(1.01))
        p = -(math.log(-a["ln_Phi"]) - math.log(-b["ln_Phi"])) / (2 * math.log(1.01))
        out["C"].append({"n1": n1, "n2": n2, "kappa": k, "m_bord": f["m_bord"], "moins_ln_Phi": -f["ln_Phi"], "p": p, "pente": pente})
        print("   (%2d,%2d)   %.4f   %5d   %10.3f   %.4f   %8.2f" % (n1, n2, k, f["m_bord"], -f["ln_Phi"], p, pente))

# --- D : graines a fraction f du seuil classique ---
D_norm = 3.0; w2f = 2.0
A1 = (D_norm + 2.0) ** 2 / (4.0 * w2f)          # n1 / (f^2 nu0*) a w2 = 2 : 25/8
PREF = (2.0 / P) * ((P - 2.0) / P) ** ((P - 2.0) / 2.0) / XC

def h(x, f_s):
    """2 t / (|delta| nu0*) au site m = nu0* x, limite des grandes occupations."""
    a = A1 * f_s ** 2 + 2.0 * x; b = f_s ** 2 + x
    return PREF * (30.0 * L1 ** 2 * L2 ** 3 * a * b ** 1.5 + 20.0 * L1 ** 4 * L2 * a * a * math.sqrt(b))

def F_wkb(f_s):
    """2 int arccosh(x / h) dx entre les deux points tournants x = h(x ; f) ; None s'il n'y a pas de barriere."""
    xs = [i * 1e-4 for i in range(1, 60001)]
    dans = [x for x in xs if x > h(x, f_s)]
    if not dans:
        return None
    def racine(lo, hi):
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if (lo - h(lo, f_s)) * (mid - h(mid, f_s)) <= 0.0: hi = mid
            else: lo = mid
        return 0.5 * (lo + hi)
    x_in = racine(max(dans[0] - 1e-4, 0.0), dans[0]) if dans[0] > 1.5e-4 else 0.0
    x_out = racine(dans[-1], dans[-1] + 1e-4)
    val = mp.quad(lambda x: mp.acosh(max(mp.mpf(1), mp.mpf(x) / h(float(x), f_s))), mp.linspace(x_in, x_out, 9))
    return 2.0 * float(val), x_in, x_out

print()
print("D. graines a fraction f du seuil classique (occupations reelles) : -ln Phi / nu0* (chaine) contre F(f) (integrale WKB)")
NUS = [5.241482788417793 * 2 ** j for j in range(0, 7)]
out["D"] = []; out["F_wkb"] = {}
for f_s in (0.0, 0.30, 0.50, 0.60, 0.70, 0.75, 0.80, 0.85, 1.00):
    fw = F_wkb(f_s)
    out["F_wkb"]["%.2f" % f_s] = None if fw is None else {"F": fw[0], "x_in": fw[1], "x_out": fw[2]}
    print("   f = %.2f : F(f) = %s" % (f_s, ("%.4f (points tournants x = %.4f et %.4f)" % fw) if fw else "pas de barriere"))
    for nu in NUS:
        lam = (1.0 / P) * ((P / (P - 2.0)) * nu) ** (-(P - 2.0) / 2.0)
        n1, n2 = A1 * f_s ** 2 * nu, f_s ** 2 * nu
        k = kappa_de_lambda(lam, n1, n2)
        f = PH.phi_fc(k, n1, n2)
        if f is None:
            out["D"].append({"f": f_s, "nu0": nu, "n1": n1, "n2": n2, "kappa": k, "vide": True})
            print("       nu0* = %8.2f  kappa = %8.4f  barriere vide" % (nu, k)); continue
        out["D"].append({"f": f_s, "nu0": nu, "n1": n1, "n2": n2, "kappa": k, "vide": False, "m_bord": f["m_bord"], "moins_ln_Phi": -f["ln_Phi"], "F": -f["ln_Phi"] / nu, "Z": f["Z"], "E": f["E"]})
        print("       nu0* = %8.2f  kappa = %8.4f  m_bord = %5d  poids du site 0 = %.3f  E = %+.4f   -ln Phi / nu0* = %8.4f%s" % (
            nu, k, f["m_bord"], f["Z"], f["E"], -f["ln_Phi"] / nu, "" if k < 0.5 else "   (kappa > 1/2 : l'etat n'est plus porte par un site)"))

# --- E : profondeur atteinte dans le domaine garde ---
def kappa_pour_m_bord(n1, n2, m_cible):
    def mb(k):
        rg = PH.reglage(k, n1, n2)
        return 0 if rg is None else rg["m_bord"]
    a, b = 1e-7, 2.0
    for _ in range(80):
        c = math.sqrt(a * b)
        if mb(c) >= m_cible: a = c
        else: b = c
    k_haut = a
    a, b = 1e-7, 2.0
    for _ in range(80):
        c = math.sqrt(a * b)
        if mb(c) <= m_cible: b = c
        else: a = c
    return math.sqrt(b * k_haut)

print()
print("E. profondeur atteinte par la loi dans le domaine garde (e_bord pris egal a m_bord |delta|)")
print("   |delta|   etiquette   e = 0.3 : m_bord  kappa      nu0*    -ln Phi  (decades)      e = 0.7 : m_bord  kappa      nu0*    -ln Phi  (decades)")
out["E"] = []
for d in (0.10, 0.065, 0.035, 0.02, 0.01):
    for (n1, n2) in ((0, 0), (6, 2), (10, 3)):
        ligne = {"delta": d, "n1": n1, "n2": n2}
        txt = "   %.3f     (%2d,%2d)   " % (d, n1, n2)
        for e in (0.3, 0.7):
            mc = int(math.floor(e / d + 1e-9))
            k = kappa_pour_m_bord(n1, n2, mc); f = PH.phi_fc(k, n1, n2)
            lam = k * XC / (P * PH.tau(n1, n2, 0)); nu = ((P - 2.0) / P) * (P * lam) ** (-2.0 / (P - 2.0))
            ligne["e_%.1f" % e] = {"m_bord": mc, "kappa": k, "nu0": nu, "moins_ln_Phi": -f["ln_Phi"], "decades": -f["ln_Phi"] / math.log(10.0)}
            txt += "          %4d    %.3e  %6.2f  %8.2f  (%6.1f)    " % (mc, k, nu, -f["ln_Phi"], -f["ln_Phi"] / math.log(10.0))
        out["E"].append(ligne); print(txt)
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
