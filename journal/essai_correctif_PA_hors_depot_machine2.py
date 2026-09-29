"""essai_correctif_PA_hors_depot_machine2.py -- machine 2, 2026-09-18.

EXECUTION D'UNE PRESCRIPTION (protocole 8) : porter la P-A CORRIGEE dans l'instrument
(arbitrage operateur du 18/09). Ce script APPLIQUE le correctif a une COPIE du banc v14, hors
depot, sous un nom qui n'est PAS un numero de version -- `essai_banc_PA_corrigee_hors_depot.py`.
La plume de l'instrument reste a machine 1 : ceci mesure une prescription, ne la publie pas.

TROIS AXES, MESURES (protocole 8), et le test negatif :
  A1  chaque ancre de remplacement est trouvee EXACTEMENT UNE FOIS, et le compte est ecrit ;
  A2  IL GUERIT : sur le chemin synthetique de l'instrument lui-meme (pre-vol alpha), la P-A
      corrigee est calculee, G-plancher se compare au plancher CORRIGE, et le verdict cesse
      d'etre NON CONCLUANT DE PLANCHER par construction ;
  A3  IL NE CASSE RIEN : le selftest de la copie reste 103/103.
  TEST NEGATIF : une ancre volontairement fausse doit faire ARRETER ce script avant ecriture.

CE QUE LE CORRECTIF FAIT, en trois remplacements :
  H-a  les coefficients c1 ET c2 en forme CLOSE et exacte (Fraction) :
       c1 = (1+w2^2) a(a+1) / ((p-1)K - P2),  P2 = a(a+1)(a-1)(a-2)
       c2 = [ K (p-1)(p-2)/2 c1^2 - (1+w2^2) c1 (2-a)(1-a) - w2^2 ] / [ P4 - (p-1)K ],
       P4 = (4-a)(3-a)(2-a)(1-a)   -- verifiee EXACTE aux neuf points contre la derivation
       b70fca94d72822ad ; plus l'ajustement corrige M1 (p = 4, 5) / M2 (p = 7).
  H-b  chaque cellule porte `lnA_M` (ajustement corrige) a cote de `lnA_II` (conserve, R1).
  H-c  au depouillement : q MESURE par point sur les trois niveaux, Richardson, S(p),
       plancher CORRIGE (borne : proj4 <= 1, donc plancher_corr(p) = max_w2 |c2| tau_dom'^4),
       G-plancher et P-A portes sur le couple CORRIGE ; les grandeurs du v14 sont CONSERVEES
       sous leurs noms, prefixees `v14_`, pour que rien ne se perde.
"""
import hashlib
import os
import re
import subprocess
import sys
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, 'banc_qualification_machine1_v14.py')
SRC_B = 'dc91676c640d4323'
CIBLE = os.path.join(ICI, 'essai_banc_PA_corrigee_hors_depot.py')
LOG = os.path.join(ICI, 'essai_correctif_PA_hors_depot_machine2.log')
lignes, bilan = [], {'chk': 0, 'mord': []}


def out(s=''):
    print(s)
    lignes.append(s)


def chk(nom, cond, detail=''):
    bilan['chk'] += 1
    if not cond:
        bilan['mord'].append(nom)
    out('  [chk %s] %s%s' % ('PASSE' if cond else 'MORD ', nom, (' -- ' + detail) if detail else ''))
    return cond


def note(nom, detail):
    out('  [note] %s -- %s' % (nom, detail))


def B(p):
    b = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', b.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


AIDES = '''
# ---------------------------------------------------------------------------
# CORRECTIF D ESSAI (machine 2, hors depot) : la lecture CORRIGEE portee dans l instrument.
# c1 et c2 en forme close exacte ; ajustement M1 (p = 4, 5) / M2 (p = 7) ; Richardson a ordre
# MESURE ; S(p) ; plancher CORRIGE borne par max_w2 |c2| tau_dom^4 (proj4 <= 1).
# ---------------------------------------------------------------------------
def coeffs_c1_c2(p, w2):
    """Exact (Fraction). c1 : terme en tau^2 ; c2 : terme en tau^4 -- gel alpha v5 2.1."""
    a = alpha_de(p)
    w = Fraction(str(w2))
    K = a * (a + 1) * (a + 2) * (a + 3)
    P2 = a * (a + 1) * (a - 1) * (a - 2)
    P4 = (4 - a) * (3 - a) * (2 - a) * (1 - a)
    c1 = (1 + w * w) * a * (a + 1) / ((p - 1) * K - P2)
    c2 = (K * Fraction((p - 1) * (p - 2), 2) * c1 * c1 - (1 + w * w) * c1 * (2 - a) * (1 - a) - w * w) \\
        / (P4 - (p - 1) * K)
    return c1, c2


def modele_de(p):
    """Ecrit AVANT le run (gel v8, 5bis) : M1 aux degres 4 et 5, M2 au degre 7."""
    return "M2" if p == 7 else "M1"


def ajuster_corrige(t, x, w2, p, dt, mode=None):
    """lnA avec c1 tau^2 SOUSTRAIT (c1 derive), plus le mode libre a p = 7 (b, w derives).
    Meme fenetre, meme minimisation de t* que l ajustement II : seule la forme change."""
    mode = mode or modele_de(p)
    c1 = float(coeffs_c1_c2(p, w2)[0])
    a = float(alpha_de(p))
    b, wlib = float(a + Fraction(3, 2)), FREQ_MODE_LIBRE[p]
    tc, td = tau_cap(w2), tau_dom(w2)
    ok = np.isfinite(x) & (x != 0)
    t, x = t[ok], x[ok]
    y = np.log(np.abs(x))
    ref = ajuster_point_fixe(t, x, w2, p, dt)
    if ref["statut"] != "POINT_FIXE":
        return {"statut": ref["statut"]}
    fen = fenetre_de(t, ref["t_star"], tc, td, 1e-6 * dt)
    tt, yy = t[fen], y[fen]

    def systeme(ts):
        tau = ts - tt
        u = yy + a * np.log(tau) - c1 * tau ** 2
        if mode == "M1":
            return u, None
        s = tau / td
        X = np.column_stack([np.ones_like(s), s ** b * np.cos(wlib * np.log(s)),
                             s ** b * np.sin(wlib * np.log(s))])
        return u, X

    def SS(ts):
        u, X = systeme(ts)
        if X is None:
            return float(((u - u.mean()) ** 2).sum())
        coef = np.linalg.lstsq(X, u, rcond=None)[0]
        return float(((u - X @ coef) ** 2).sum())

    lo, hi = float(tt[-1]) * (1 + 1e-12) + 1e-12 * tc, float(t[-1]) + 2 * td
    ts, ss = _minimiser_1d(SS, lo, hi)
    u, X = systeme(ts)
    if X is None:
        return {"statut": "AJUSTE", "modele": mode, "lnA_M": float(u.mean()), "t_star_M": ts, "SS_M": ss}
    coef, _, rang, _ = np.linalg.lstsq(X, u, rcond=None)
    return {"statut": "AJUSTE", "modele": mode, "lnA_M": float(coef[0]), "t_star_M": ts, "SS_M": ss,
            "a_mode": float(coef[1]), "c_mode": float(coef[2]), "rang_M": int(rang)}


def plancher_corrige(p):
    """Borne DERIVEE du terme suivant : max_w2 |c2(p,w2)| tau_dom'(w2)^4, proj4 <= 1."""
    return max(abs(float(coeffs_c1_c2(p, w2)[1])) * tau_dom(w2) ** 4 for w2 in W2S)


def richardson_q(l0, l1, l2):
    """q MESURE sur trois niveaux (dt, dt/2, dt/4) puis extrapolation ; (None, None) si q
    sort de [3, 5] ou si les differences ne le permettent pas (point NON LU)."""
    d1, d2 = l0 - l1, l1 - l2
    if d2 == 0 or d1 / d2 <= 0:
        return None, None
    q = math.log2(d1 / d2)
    if not (3.0 <= q <= 5.0):
        return q, None
    return q, l2 + (l2 - l1) / (2 ** q - 1)


FREQ_MODE_LIBRE = {4: 4.2130748865881615, 5: 3.4920538553569353, 7: 2.8965496715920477}
'''

BLOC_C = '''            # --- CORRECTIF D ESSAI : la lecture CORRIGEE (machine 2, hors depot) ---
            D["v14_dispersion_lnA"] = D["dispersion_lnA"]
            D["v14_tol_lnA"] = D["tol_lnA"]
            D["v14_G_plancher_mord"] = D["G_plancher_mord"]
            D["v14_P_A"] = D["P_A"]
            lnA_R, q_par_point, non_lus = {}, {}, []
            for w2 in W2S:
                for c in C_PLAN:
                    cle = "%d|%.2f|%.2f" % (p, w2, c)
                    cells = (plan.get(cle), gdt.get(cle), (gdt4 or {}).get(cle))
                    vals = [((cc or {}).get("ajustement_corrige") or {}).get("lnA_M") for cc in cells]
                    if None in vals:
                        non_lus.append(cle + " (cellule ou ajustement corrige absent)")
                        continue
                    q, lR = richardson_q(*vals)
                    q_par_point[cle] = q
                    if lR is None:
                        non_lus.append(cle + " (q = %s hors [3, 5])" % ("indefini" if q is None else "%.3f" % q))
                        continue
                    lnA_R[cle] = lR
            D["q_mesure"] = q_par_point
            D["lnA_R"] = lnA_R
            D["points_non_lus"] = non_lus
            D["modele"] = modele_de(p)
            if len(lnA_R) >= 2:
                D["S_p"] = max(lnA_R.values()) - min(lnA_R.values())
                D["plancher_corrige"] = plancher_corrige(p)
                D["tol_lnA"] = max(D["S_p"], D["plancher_corrige"])
                D["tol_lnA_sur_plancher"] = D["tol_lnA"] / D["plancher_corrige"]
                D["G_plancher_mord"] = D["tol_lnA"] <= D["plancher_corrige"]
                lnAK = math.log(float(K_de(p)) / G_REF) / (p - 2)
                D["ecarts_corriges"] = {cle: v - lnAK for cle, v in lnA_R.items()}
                D["P_A"] = all(abs(v - lnAK) <= D["tol_lnA"] for v in lnA_R.values())
            else:
                # PREMIER ESSAI (log 623bc17a04259d7d) : ici le correctif posait exploitable =
                # False, et TOUT le chemin synthetique (pre-vol, banc qui tue) tombait en
                # branche 3 -- le banc cessait de pouvoir tuer. Une lecture corrigee ABSENTE
                # est une CONSIGNE, jamais une invalidation : les grandeurs du v14 restent.
                D["S_p"] = None
                D["lecture_corrigee"] = ("NON JOUEE : %d point(s) lisible(s) sur 6 (%s)"
                                         % (len(lnA_R), "; ".join(non_lus)[:160]))
            # --- fin du correctif d essai ---
'''

REMPLACEMENTS = [
    ('H-a aides (c1, c2, ajustement corrige, Richardson)',
     'def ajuster_point_fixe(t, x, w2, p, dt):',
     AIDES + '\ndef ajuster_point_fixe(t, x, w2, p, dt):'),
    ('H-b lnA_M pose a cote de lnA_II, a chaque cellule',
     '    aj = ajuster_point_fixe(ph2["t"], x, w2, p, dt2)\n    rec["ajustement"] = aj',
     '    aj = ajuster_point_fixe(ph2["t"], x, w2, p, dt2)\n'
     '    rec["ajustement"] = aj\n'
     '    rec["ajustement_corrige"] = ajuster_corrige(ph2["t"], x, w2, p, dt2)'),
    ('H-c G-plancher et P-A portes sur le couple CORRIGE',
     '            D["P_A"] = all(abs(math.log(v)) <= (p - 2) * D["tol_lnA"] for v in ratios.values())',
     '            D["P_A"] = all(abs(math.log(v)) <= (p - 2) * D["tol_lnA"] for v in ratios.values())\n' + BLOC_C),
]


def appliquer(src, remplacements, arret_si_compte_autre_que=1):
    s, comptes = src, []
    for nom, ancre, neuf in remplacements:
        n = s.count(ancre)
        comptes.append((nom, n))
        if n != arret_si_compte_autre_que:
            return None, comptes
        s = s.replace(ancre, neuf)
    return s, comptes


out('CORRECTIF D ESSAI -- P-A CORRIGEE DANS L INSTRUMENT (hors depot)')
out('python %s' % sys.version.split()[0])
out()
out('0. ANCRES')
chk('le banc v14 a son empreinte', B(SRC) == SRC_B, B(SRC))
src = open(SRC, encoding='utf-8').read()

out()
out('1. A1 -- LES ANCRES, COMPTEES')
patch, comptes = appliquer(src, REMPLACEMENTS)
for nom, n in comptes:
    chk('A1 %s : ancre trouvee exactement une fois' % nom, n == 1, '%d occurrence(s)' % n)
chk('A1 : le correctif est applique', patch is not None)

out()
out('2. TEST NEGATIF DE CE SCRIPT -- une ancre fausse doit arreter avant ecriture')
faux = [(REMPLACEMENTS[0][0], 'def ancre_qui_n_existe_pas(', 'x')]
p2, c2 = appliquer(src, faux)
chk('le script ARRETE sur une ancre absente (0 occurrence)', p2 is None and c2[0][1] == 0, str(c2))
double = [(REMPLACEMENTS[0][0], 'def ', 'x')]
p3, c3 = appliquer(src, double)
chk('le script ARRETE sur une ancre multiple', p3 is None and c3[0][1] > 1, '%d occurrences' % c3[0][1])

if patch is None:
    out('ARRET : aucune ecriture.')
else:
    with open(CIBLE, 'w', encoding='utf-8', newline='\n') as f:
        f.write(patch)
    out()
    note('copie ecrite', '%s (%d octets, convention B %s) -- HORS DEPOT, nom sans numero de version'
         % (os.path.basename(CIBLE), os.path.getsize(CIBLE), B(CIBLE)))
    out()
    out('3. A3 -- IL NE CASSE RIEN : le selftest de la copie')
    reg = os.path.join(os.environ.get('TEMP', '.'), 'reg729')
    r = subprocess.run([sys.executable, CIBLE, '--selftest', '--registre', reg],
                       capture_output=True, text=True, timeout=900)
    m = re.findall(r'bilan (\d+/\d+)', r.stdout)
    chk('A3 : selftest de la copie = 103/103', bool(m) and m[-1] == '103/103', (m[-1] if m else r.stdout[-200:]))
    open(os.path.join(ICI, 'essai_correctif_selftest.log'), 'w', encoding='utf-8', newline='\n').write(r.stdout)

    out()
    out('4. A2 -- IL GUERIT : le pre-vol alpha de la copie, chemin synthetique complet')
    r2 = subprocess.run([sys.executable, CIBLE, '--mode', 'alpha', '--prevol', '--registre', reg,
                         '--sortie', os.path.join(ICI, 'out_prevol_essai_PA')],
                        capture_output=True, text=True, timeout=1800)
    open(os.path.join(ICI, 'essai_correctif_prevol_alpha.log'), 'w', encoding='utf-8', newline='\n').write(r2.stdout)
    verdicts = re.findall(r'VERDICT\s+(.+)', r2.stdout)
    note('A2 verdict du pre-vol de la copie', verdicts[-1].strip()[:110] if verdicts else 'aucun verdict')
    chk('A2-1 : le chemin synthetique garde le verdict du v14 (la lecture corrigee ne l invalide pas)',
        bool(verdicts) and 'NON CONCLUANT DE FENETRE' not in verdicts[-1], verdicts[-1][:100] if verdicts else '')
    note('A2-1 portee', 'le pre-vol joue un moteur FACTICE : ses cellules ne portent pas d ajustement '
         'corrige, donc la lecture corrigee y est NON JOUEE et consignee -- c est le defaut que le '
         'premier essai a revele (log 623bc17a04259d7d) et que le v15 doit traiter a la source')
    for motif in (r'q = [\d.]+', r'S_p', r'plancher_corrige'):
        note('A2 trace', '%s : %d occurrence(s) au journal du pre-vol' % (motif, len(re.findall(motif, r2.stdout))))

    out()
    out('5. CE QUE LE BANC QUI TUE EN DIT -- scenario G22 (il encode le plancher ANCIEN)')
    r3 = subprocess.run([sys.executable, CIBLE, '--banc', '--registre', reg],
                        capture_output=True, text=True, timeout=1800)
    open(os.path.join(ICI, 'essai_correctif_banc.log'), 'w', encoding='utf-8', newline='\n').write(r3.stdout)
    g22 = [l for l in r3.stdout.splitlines() if 'G22' in l]
    bil = re.findall(r'bilan (\d+/\d+) scenarios mordent', r3.stdout)
    note('G22 de la copie', (g22[-1][:150] if g22 else 'absent'))
    chk('A3-2 : le banc qui tue de la copie reste 56/56', bool(bil) and bil[-1] == '56/56', bil[-1] if bil else 'absent')

    out()
    out('6. A2 -- IL GUERIT, MESURE SUR DES SERIES A TROIS NIVEAUX')
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location('essai_banc', CIBLE)
    bc = _iu.module_from_spec(_sp); _sp.loader.exec_module(bc)
    import numpy as _np
    for p_ in (4, 5, 7):
        lnA_R, qs = {}, []
        for w2 in bc.W2S:
            for cc in bc.C_PLAN:
                td, tc = bc.tau_dom(w2), bc.tau_cap(w2)
                c1 = float(bc.coeffs_c1_c2(p_, w2)[0]); c2 = float(bc.coeffs_c1_c2(p_, w2)[1])
                a, A = float(bc.alpha_de(p_)), bc.A_de(p_)
                vals = []
                for div in (1, 2, 4):
                    dt = tc / bc.M_PAS / div
                    n = int(_np.ceil((1.5 * td - tc) / dt)) + 1
                    taus = tc + dt * _np.arange(n)
                    # serie EXACTE du modele + une erreur d integrateur en dt^4 (ce que
                    # Richardson doit retirer), amplitude declaree 1e-6 x (dt/dt_2b)^4
                    err = 1e-6 * (dt / (tc / bc.M_PAS)) ** 4
                    xx = A * taus ** (-a) * (1 + c1 * taus ** 2 + c2 * taus ** 4) * (1 + err)
                    tt = (1.0 - taus)[::-1]
                    aj = bc.ajuster_corrige(tt, xx[::-1], w2, p_, dt)
                    vals.append(aj.get('lnA_M'))
                q, lR = bc.richardson_q(*vals)
                qs.append(q)
                if lR is not None:
                    lnA_R['%d|%.2f|%.2f' % (p_, w2, cc)] = lR
        S = max(lnA_R.values()) - min(lnA_R.values()) if len(lnA_R) >= 2 else None
        pc = bc.plancher_corrige(p_)
        lnAK = _np.log(float(bc.K_de(p_)) / bc.G_REF) / (p_ - 2)
        ec = max(abs(v - lnAK) for v in lnA_R.values()) if lnA_R else None
        note('A2-2 p=%d' % p_, 'q mesure de %.3f a %.3f ; %d/6 points lus ; S = %.3e ; plancher CORRIGE = %.3e ; '
             'G-plancher corrige mord : %s ; ecart max a ln(K/g)/(p-2) = %.3e'
             % (min(q for q in qs[-6:] if q), max(q for q in qs[-6:] if q), len(lnA_R), S, pc,
                max(S, pc) <= pc, ec))
        chk('A2-2 p=%d : le plancher CORRIGE ne mord pas par construction (S > plancher)' % p_, S > pc,
            'S %.3e vs plancher %.3e' % (S, pc))

out()
out('BILAN : %d controles, %d mordent %s' % (bilan['chk'], len(bilan['mord']), bilan['mord']))
with open(LOG, 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(lignes) + '\n')
print('log convention B %s' % B(LOG))
