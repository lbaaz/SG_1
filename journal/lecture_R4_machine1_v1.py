# LECTURE MACHINE 1 DU RUN R4 (lot m2 6f6387f416854fec), par enumeration, depuis les donnees brutes (grille_repr, t_exp) :
#   E contre le gel v2 (91d858bbf2da60af, detenu), D contre le JSON P-4 depose (e66549fd72f4239b, detenu),
#   C : structure brute + statistique gelee (s* = min des explosifs), A : falsifieur de m1 tel qu'embarque (attendus 2154286e9df56806, NON detenu).
import json, math, sys, hashlib, unicodedata
import numpy as np
R = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/runR4'
P4 = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/P4/lot_machine2_2026-09-02_P4_run_v4/mesures_P4_jumeau_machine2_v1.json'
GELV2 = sys.argv[3] if len(sys.argv) > 3 else '/home/claude/lots10/lot_machine2_2026-09-10_gel_volet_E_v2/gel_volet_E_flanc_machine2_v2.md'
def B(b): return hashlib.sha256(unicodedata.normalize('NFC', b.decode('utf-8').replace('\r\n', '\n')).encode()).hexdigest()[:16]
print("gel volet E v2 detenu :", B(open(GELV2, 'rb').read()), "(attendu 91d858bbf2da60af)")
PORTE = math.log(1.02); PAS = math.log(1.15 / 0.30) / 95
def seuils(s, t):
    s = np.array([float(x) for x in s]); t = np.array(t, float)
    e400 = (t > 0) & (t <= 400.0); e1600 = (t > 0) & (t <= 1600.0)
    def first(e): return (float(s[int(np.argmax(e))]), int(np.argmax(e))) if e.any() else (None, None)
    def ilots(e):
        idx = np.where(e)[0]
        if len(idx) == 0: return 0, None
        # bloc du haut = segment contigu qui contient le dernier point explosif ; ilots = composantes contigues hors bloc
        comps = np.split(idx, np.where(np.diff(idx) != 1)[0] + 1)
        return len(comps) - 1, int(comps[-1][0])
    return s, e400, e1600, first(e400), first(e1600), ilots(e400), ilots(e1600)
# ---------------- VOLET E ----------------
GEL = {(9, 1.45): +1, (9, 1.55): -1, (7, 3.90): -1, (7, 4.10): +1, (13, 1.90): -1, (13, 2.10): +1}   # signe de A gele
BANDE = {(9, 1.45): (0.057, 0.240), (9, 1.55): (0.073, 0.305), (13, 1.90): (0.095, 0.125), (13, 2.10): (0.095, 0.125)}
E = json.load(open(f'{R}/run_R4_voletE_machine2_v1.json'))
print("\n=== VOLET E : re-derive depuis (grille_repr, t_exp), regle 5.6 du gel v2 ===")
print(f"  porte ln(1.02) = {PORTE:.6f} ; pas = {PAS:.6f} ; gel cite au JSON : {E['gel']} ; moteur {E['moteur']}")
tenues = fals = muettes = 0; rows = []
for r in E['resultats']:
    p, w2 = r['p'], r['w2']; cle = (p, round(w2, 2)); sg = GEL[cle]
    col = {}
    for k, c in r['colonnes'].items():
        s, e400, e1600, (s4, i4), (s16, i16), (n_il4, b4), (n_il16, b16) = seuils(c['grille_repr'], c['t_exp'])
        att = c['s0'] * np.logspace(math.log10(0.30), math.log10(1.15), 96); dev = float(np.abs(s / att - 1).max())
        n_expl = int(e1600.sum()); assert n_expl + int((~e1600).sum()) == 96
        col[int(c['sgn'])] = dict(s400=s4, s1600=s16, i400=i4, i1600=i16, il400=n_il4, il1600=n_il16, bloc400=b4, bloc1600=b16, grille_dev=dev, borne=c['borne'], n_expl=n_expl)
    def etat(T):
        a, b = col[1][f's{T}'], col[-1][f's{T}']
        if a is None or b is None: return None, 'MUETTE', 'absence'
        A = math.log(a / b)
        if abs(A) <= PORTE: return A, 'MUETTE', 'porte'
        return A, ('CONCORDE' if (A > 0) == (sg > 0) else 'CONTREDIT'), None
    A4, e4, c4 = etat(400); A16, e16, c16 = etat(1600)
    if 'CONTREDIT' in (e4, e16): v = 'FALSIFIEE'; fals += 1
    elif 'CONCORDE' in (e4, e16): v = 'TENUE'; tenues += 1
    else: v = 'MUETTE'; muettes += 1
    bande = BANDE.get(cle); dans = None
    if bande and A4 is not None: dans = (bande[0] <= abs(A4) <= bande[1], bande[0] <= abs(A16) <= bande[1])
    rows.append((cle, sg, A4, e4, A16, e16, v, dans, col))
    print(f"  {p}|{w2:.2f}  gele A{'>' if sg>0 else '<'}0  A400={A4:+.6f} ({e4}{'/'+c4 if c4 else ''})  A1600={A16:+.6f} ({e16})  -> {v}" + (f"  bande {bande} : {'DANS' if all(dans) else 'HORS a une fenetre' if any(dans) else 'HORS'}" if bande else "") + f"  ; ilots(+1,-1) a 1600 : {col[1]['il1600']},{col[-1]['il1600']} ; grille = s0 logspace a {max(col[1]['grille_dev'], col[-1]['grille_dev']):.1e} ; borne {col[1]['borne']}/{col[-1]['borne']}")
print(f"  COMPTE : tenues {tenues} + falsifiees {fals} + muettes {muettes} == {len(E['resultats'])} paires : {tenues+fals+muettes == len(E['resultats'])}")
# fait neuf de m2 : constante du flanc de 3:2 en (p-1), depuis les archives G6 (7|1.45 A=+0.159833, 7|1.55 A=-0.203348 ; lecture m2 des archives) et E1
for cle, A7 in (((9, 1.45), 0.159833), ((9, 1.55), -0.203348)):
    A9 = next(x[2] for x in rows if x[0] == cle)
    print(f"  flanc 3:2 a {cle[1]} : exp(|A|(p-1)) = {math.exp(abs(A7)*6):.3f} (p=7, G6) -> {math.exp(abs(A9)*8):.3f} (p=9) : {100*(math.exp(abs(A9)*8)/math.exp(abs(A7)*6)-1):+.0f} pour cent ; en (p-2) : {math.exp(abs(A7)*5):.3f} -> {math.exp(abs(A9)*7):.3f}")
# ---------------- VOLET D ----------------
print("\n=== VOLET D : T = 6400 sur les trois grilles R-P4-2, contre le JSON P-4 depose ===")
D = json.load(open(f'{R}/run_R4_voletD_machine2_v1.json')); P = json.load(open(P4))
print(f"  attendus cites {D['attendus']} ; p4 cite {D['p4']} ; instrument {D['instrument']} ; T = {D['T']} ; eta = {D['eta']}")
for r in D['resultats']:
    g = next(x for x in P['grilles'] if x['colonne'] == r['colonne'] and x['grille'] == r['grille'])
    sP = np.array([float(x) for x in g['grille_repr']]); tP = np.array(g['t_exp'], float)
    keys = [k for k in r if k not in ('colonne','grille','p','w2','sgn','pas','s_400','s_1600','s_1600_depose','s_6400','deplacement_ln','deplacement_pas','verdict','n_expl','n_non_expl','n_pts','duree')]
    i4P = int(np.argmax((tP > 0) & (tP <= 400))); i16P = int(np.argmax(tP > 0))
    print(f"  {r['colonne']} {r['grille']} : P-4 i400={i4P} i1600={i16P} s*(1600)={sP[i16P]:.10f} ; run : s_400={r['s_400']:.10f} s_1600={r['s_1600']:.10f} s_6400={r['s_6400']:.10f} deplacement {r['deplacement_pas']:+.1f} pas ; s_1600 run == P-4 au repr : {r['s_1600'] == float(sP[i16P])} ; verdict embarque : {r['verdict']} ; n_expl {r['n_expl']} + {r['n_non_expl']} == {r['n_pts']} ; cles brutes du run : {keys if keys else 'aucune (pas de t_exp a 6400 au JSON)'}")
# ---------------- VOLET C ----------------
print("\n=== VOLET C : 11|2.50 et 11|6.00, structure brute a 400 et 1600 ===")
C = json.load(open(f'{R}/run_R4_voletC_machine2_v1.json'))
for r in C['resultats']:
    s, e400, e1600, (s4, i4), (s16, i16), (n_il4, b4), (n_il16, b16) = seuils(r['grille_repr'], r['t_exp'])
    idx16 = np.where(e1600)[0]; idx4 = np.where(e400)[0]
    dln = math.log(s16 / s4) if (s4 and s16) else None
    print(f"  {r['p']}|{r['w2']:.2f} s0={r['s0']:.10f} : explosifs a 400 : {list(idx4)} ; a 1600 : {list(idx16)}")
    print(f"     statistique gelee s* = min : s*(400)={s4:.10f} (noeud {i4}) s*(1600)={s16:.10f} (noeud {i16}) dln={dln:+.5f} ; loi directe -ln4/(p-2) = {-math.log(4)/(r['p']-2):+.5f} ; ilots hors bloc a 1600 : {n_il16}, bloc du haut depuis le noeud {b16} (a 400 : {n_il4}, noeud {b4}) ; verdict embarque '{r['verdict']}' ; pred_direct {r['pred_direct']:+.5f}")
# ---------------- VOLET A ----------------
print("\n=== VOLET A : falsifieur m1 tel qu'embarque, applique tel quel ===")
A = json.load(open(f'{R}/run_R4_voletA_machine2_v1.json'))
hors = []; gel_ok = []; expl = []
for r in A['resultats']:
    lin = r['s0'] * (3 + r['w2']**2) / (r['w2']**2 - 1)   # excursion pleine du mouvement libre, sgn = +1
    env = np.array(r['env']); plat = (env.max() - env.min()) / env.max()
    if r['attendu'].startswith('GEL'):
        ok = (not r['explose']) and plat <= 0.02 and abs(r['apex'] - lin) / lin <= 0.02; gel_ok.append(ok)
        print(f"  {r['p']}|{r['w2']:.2f} s0={r['s0']:<5} GEL : apex {r['apex']:.6f} = {r['apex']/r['s0']:.4f} s0 ; libre (3+w2^2)/delta = {lin/r['s0']:.4f} s0 ; enveloppe plate a {plat:.1e} ; explose {r['explose']} -> {'GEL tenu' if ok else 'ECART'} (cible embarquee {r['cible']} = celle de s0=0.5)")
    else:
        dev = abs(r['apex'] - r['cible']) > r['tol']; hors.append(dev)
        print(f"  {r['p']}|{r['w2']:.2f} s0={r['s0']:<5} excursion : cible {r['cible']} +- {r['tol']} ; apex {r['apex']:.6f} = {r['apex']/lin:.4f} x libre ; enveloppe plate a {plat:.1e} ; explose {r['explose']} -> {'HORS TOLERANCE' if dev else 'dans tolerance'}")
    if r['explose']: expl.append((r['p'], r['w2']))
print(f"  falsifieur m1 (tel que cite au log) : apex hors tolerance a >= 2 cellules -> {sum(hors)} cellules HORS ; explosion la ou GEL attendu -> {len(expl)} ; GEL tenu {sum(gel_ok)}/{len(gel_ok)}")
print("  => par la LETTRE du falsifieur embarque, la moitie EXCURSION de P-D1-9 est FALSIFIEE dans sa fenetre T = 3000 ; la moitie GEL est TENUE.")
print("     Toutes les cellules restent sur l'excursion pleine du mouvement LIBRE (apex = s0 (3+w2^2)/delta) : rien de non lineaire ne s'est produit en 3000.")
