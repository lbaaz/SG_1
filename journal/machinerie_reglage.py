import math
from fractions import Fraction as F
INF = 1.659260768e-05
DISP = {4: 1.97714978966701e-06, 5: 2.393510486697892e-06, 7: 7.43220491195018e-06}
AL = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
A = {4: 48.98979, 5: 9.65048, 7: 3.14244}
D0, r, M, k, dt1, g, T_MAX = F(1, 100), F(1, 10), 20, 2, 0.006, 0.05, 400.0
W2 = (1.73, 2.27, 2.80)
SUP1 = min(DISP[p] * float((AL[p] + 2) * (AL[p] + 3)) for p in (4, 5, 7))


def R(n):
    """Toutes les grandeurs du reglage delta' = delta_0 / n^2, comme au v6."""
    d = {}
    DP = D0 / n ** 2
    d['n'], d['DP'], d['kT'], d['m'] = n, DP, float(DP) / INF, SUP1 / float(DP)
    d['plancher'] = {p: DP / ((AL[p] + 2) * (AL[p] + 3)) for p in (4, 5, 7)}
    d['ratio'] = {p: float(d['plancher'][p]) / DISP[p] for p in (4, 5, 7)}
    tau_dom = {w: math.sqrt(float(DP) / (1 + w * w)) for w in W2}
    tau_cap = {w: float(r) * tau_dom[w] for w in W2}
    d['tau_dom'], d['tau_cap'] = tau_dom, tau_cap
    d['dt2a'] = {w: k * tau_dom[w] / M for w in W2}
    d['dt2b'] = {w: tau_cap[w] / M for w in W2}
    d['basc'] = {(p, w): A[p] * (k * tau_dom[w]) ** (-float(AL[p])) for p in (4, 5, 7) for w in W2}
    d['cap'] = {(p, w): A[p] * tau_cap[w] ** (-float(AL[p])) for p in (4, 5, 7) for w in W2}
    d['deb'] = max((g * d['cap'][(p, w)] ** (p - 1), p, w) for p in (4, 5, 7) for w in W2)
    d['n2a'] = M * (n - 1)
    d['ret'] = {w: math.ceil(dt1 / d['dt2a'][w]) for w in W2}
    d['bornes'] = {w: (d['n2a'] - d['ret'][w], d['n2a'] + 1) for w in W2}
    tau_dom_0 = {w: math.sqrt(float(D0) / (1 + w * w)) for w in W2}
    n2s = {}
    for w in W2:
        depart_2s = T_MAX - k * tau_dom_0[w]
        t_start = math.floor(depart_2s / dt1) * dt1
        n2s[w] = math.ceil((T_MAX - k * tau_dom[w] - t_start) / (k * tau_dom[w] / M))
    d['n2s'] = n2s
    d['i2s'] = {w: (d['n2a'], d['n2a'] + d['ret'][w]) for w in W2}
    d['n2a_k'] = M * (4 * n // 2 - 1)
    return d


def frags(d):
    """Les fragments de TEXTE du gel qui dependent du reglage, dans le format de la construction v6."""
    n, DP, kT, m, pl, ra = d['n'], d['DP'], d['kT'], d['m'], d['plancher'], d['ratio']
    f = {}
    f['h19'] = "#       delta' = delta_0 / n^2 avec n = %d : delta' = %s = %.6e, DANS la fenetre --" % (n, DP, float(DP))
    f['h20'] = "#       marge T kT = delta'/INF = %.4f, marge A m = %.4f (delta 90, nn.4 : les deux" % (kT, m)
    f['s0'] = "descend la fenetre (delta' = %s, soit 1/%d de la fenetre du 85 ; le v5" % (DP, n * n)
    f['s33a'] = "    **n = %d    delta' = %s = %.6e    delta'/delta_0 = 1/%d**" % (n, DP, float(DP), n * n)
    f['s33b'] = "    kT = delta'/INF = %.4f  (D-t-25 a mesure le besoin du volet T entre" % kT
    f['s33c'] = "                            1.15 et 1.74) ; m = SUP(1)/delta' = %.4f" % m
    f['s33t'] = "\n".join("    %d    %-22s  %.6e     %.4f" % (p, str(pl[p]), float(pl[p]), ra[p]) for p in (4, 5, 7))
    f['s41'] = "fenetre tombe a tau = k tau_dom' = %.3e / %.3e / %.3e" % tuple(k * d['tau_dom'][w] for w in W2)
    f['s43'] = "\n".join("    %.2f    %.6e   %.6e   %.6e   %.6e" % (w, d['tau_dom'][w], d['tau_cap'][w], d['dt2a'][w], d['dt2b'][w]) for w in W2)
    f['s44'] = "\n".join("    p = %d        %s" % (p, "    ".join("%.4e" % d['basc'][(p, w)] for w in W2)) for p in (4, 5, 7))
    f['s45'] = "\n".join("    p = %d        %s" % (p, "    ".join("%.4e" % d['cap'][(p, w)] for w in W2)) for p in (4, 5, 7))
    f['deb'] = "max g |x|^(p-1) au CAP' = %.3e\n    (p = %d, w2 = %.2f)" % d['deb']
    f['n2a'] = "n_2a nominal = M (sqrt(delta_0/delta') - 1) = 20 x %d = %d" % (n - 1, d['n2a'])
    f['bornes'] = "    n_2a dans [ %d - ceil(dt_1/dt_2a(w2)) , %d ]\n         soit %s   (w2 = 1.73/2.27/2.80)" % (
        d['n2a'], d['n2a'] + 1, " / ".join("[%d, %d]" % d['bornes'][w] for w in W2))
    f['cout'] = "Cout nominal de la descente : ~%d pas par serie sur-seuil" % (d['n2a'] + 380)
    f['pas'] = "-- son compte n'est PAS %d :" % d['n2a']
    f['i47'] = "    %d <= n_2s <= %d + ceil(dt_1/dt_2a(w2))\n    soit %s    (w2 = 1.73/2.27/2.80)" % (
        d['n2a'], d['n2a'], " / ".join("[%d, %d]" % (d['n2a'], d['n2a'] + d['ret'][w]) for w in W2))
    f['n2s'] = "n_2s = %d / %d / %d" % tuple(d['n2s'][w] for w in W2)
    f['j2a'] = "    n_2a jumelle : %s" % " / ".join("[%d, %d]" % (2 * d['bornes'][w][0], 2 * d['bornes'][w][1]) for w in W2)
    f['j2s'] = "    n_2s jumelle : %s" % " / ".join("[%d, %d]" % (2 * d['i2s'][w][0], 2 * d['i2s'][w][1]) for w in W2)
    f['s471'] = "MEME reglage (delta' = %s, r, M, k, la regle du pas par etage) et sur" % DP
    f['s6'] = ("    delta' = %s    DERIVE en 3 (le pre-vol est le nombre, regle 3.2)\n"
               "    n = %d              choisi par le balayage, jamais tape (3.2)\n"
               "    kT = %.4f, m = %.4f DERIVES en 3.3 (les marges se mesurent, ne se tapent pas)" % (DP, n, kT, m))
    f['s7'] = "attendu de conception : %.2f / %.2f / %.2f\naux p = 4 / 5 / 7 (3.3, m = %.2f au plus contraint)" % (
        1 / ra[4], 1 / ra[5], 1 / ra[7], m)
    f['s10'] = "le reglage (DELTA = %s ; B_DESC, M_MARGE, J_DESC = %d, 1, 2 -- la racine\nde descente vaut %d, PURE ;" % (DP, n, n)
    f['s12'] = "n = %d, les deux marges partielles, a la plume de machine 1" % n
    f['r2'] = "1/%d" % (n * n)
    f['r2v4'] = "%.4e" % float(DP / D0)
    f['r2v3'] = "%.3e" % float(DP / D0)
    return f



def attentes(d):
    """Les attentes du selftest, typees au v9 (n = 21) et re-derivees a n = 18."""
    n, DP = d['n'], d['DP']
    a = {}
    a['DELTA'] = "DELTA = Fraction(%d, %d)" % (DP.numerator, DP.denominator)
    a['BJ'] = "B_DESC, M_MARGE, J_DESC = %d, 1, 2              # gel v6 3.2 : delta' = delta_0 / %d^2 ; m derive = %.2f > M_MARGE" % (n, n, d['m'])
    a['pl'] = "for p, att in ((4, Fraction(%s)), (5, Fraction(%s)), (7, Fraction(%s))):" % tuple(str(d['plancher'][p]).replace('/', ', ') for p in (4, 5, 7))
    a['nom'] = '    test("n_2b\' = M k / r = 400 ; fenetre = 180 ; nominaux %d / 380 (derives, v6 4.6-4.7)",\n         N_2BP == 400 and N_FENETRE == 180 and n_2a_nominal() == %d and n_2b_nominal() == 380)' % (d['n2a'], d['n2a'])
    a['l46'] = 'test("intervalles 4.6 : n_2a %s ; n_2b [360,381] (derives, entiers)",' % '/'.join('[%d,%d]' % d['bornes'][w] for w in W2)
    a['i46'] = '         == [%s]' % ', '.join('(%d, %d)' % d['bornes'][w] for w in W2)
    a['n2ak'] = '         and n_2a_nominal_k(K_GARDE) == %d)' % d['n2a_k']
    a['l47'] = 'test("intervalles 4.7 : n_2s %s ; jumelle 4.8 : bornes x2",' % '/'.join('[%d,%d]' % d['i2s'][w] for w in W2)
    a['i47'] = '         [intervalle_2s(w) for w in W2S] == [%s]' % ', '.join('(%d, %d)' % d['i2s'][w] for w in W2)
    a['j47'] = '         and [intervalle_2s(w, 2) for w in W2S] == [%s]' % ', '.join('(%d, %d)' % (2 * d['i2s'][w][0], 2 * d['i2s'][w][1]) for w in W2)
    a['j2a'] = '         and intervalle_evenement(n_2a_nominal(), retard_2a(1.73), 2) == (%d, %d)' % (2 * d['bornes'][W2[0]][0], 2 * d['bornes'][W2[0]][1])
    a['g24'] = '"un %d asserte ne l\'aurait pas vu"' % d['n2a']
    w0 = W2[0]
    a['g25'] = ('scenario("G25 n_2s > %d SANS morsure : %d dans [%d, %d] a w2=1.73 (un %d asserte = banc mort)",\n             intervalle_2s(1.73) == (%d, %d) and %d < %d <= %d and not (%d == %d),\n             "n_2s derive = %d", gardes=())'
                % (d['n2a'], d['n2s'][w0], d['i2s'][w0][0], d['i2s'][w0][1], d['n2a'], d['i2s'][w0][0], d['i2s'][w0][1], d['n2a'], d['n2s'][w0], d['i2s'][w0][1], d['n2s'][w0], d['n2a'], d['n2s'][w0]))
    a['json'] = '"reglage": {"delta": "%s"}' % DP
    a['st'] = '    test("delta\' = %s et delta_0 = b^J delta\' = 1/100 (EXACT, v6 3)",\n         DELTA == Fraction(%d, %d)' % (DP, DP.numerator, DP.denominator)
    a['ldesc'] = 'refute R~1, ne confirme pas 1/%d' % (n * n)
    tab = 'TABLES_GEL_ALPHA = {   # gel constante A v6, 4.3 (tau_dom\', dt_2b), 4.4 (bascule 2b), 4.5 (CAP\') -- re-derivees au reglage v6\n'
    tab += '    "tau_dom": {%s},\n' % ', '.join('%.2f: "%.4e"' % (w, d['tau_dom'][w]) for w in W2)
    tab += '    "dt2": {%s},\n' % ', '.join('%.2f: "%.4e"' % (w, d['dt2b'][w]) for w in W2)
    tab += '    "dt2a": {%s},\n' % ', '.join('%.2f: "%.4e"' % (w, d['dt2a'][w]) for w in W2)
    tab += '    "CAP": {%s},\n' % ',\n            '.join(', '.join('(%d, %.2f): "%.4e"' % (p, w, d['cap'][(p, w)]) for w in W2) for p in (4, 5, 7))
    tab += '    "bascule": {%s},\n' % ',\n                '.join(', '.join('(%d, %.2f): "%.4e"' % (p, w, d['basc'][(p, w)]) for w in W2) for p in (4, 5, 7))
    tab += '    "A": {4: "48.98979", 5: "9.65048", 7: "3.14244"},\n}\n'
    a['tab'] = tab
    return a


