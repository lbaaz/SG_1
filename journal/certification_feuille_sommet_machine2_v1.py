# -*- coding: ascii -*-
"""CERTIFICATION (c) du gel "SOMMET", seconde partie : SA FEUILLE (feuille_gel_sommet_machine1_v1.py, ac934e0caaa59c08) FAIT-ELLE CE QUE DISENT LES SECTIONS 5 ET 6 DE LA PIECE ?
Methode : (1) MON JUGE, ecrit des SEULES sections 5 et 6 (juge_sommet() ci-dessous ; il appelle juger_etat de la feuille DEPOSEE, comme la section 5 le dit, et rien d'autre de la feuille de machine 1 ; je n'avais pas lu la logique de sa feuille en l'ecrivant, seulement son mode d'emploi) ;
(2) un GENERATEUR de dossiers de run SYNTHETIQUES a partir de la table gelee (56 cellules, neuf temoins positifs, instrument), a partir d'un vrai fichier de lecture de Q2 comme gabarit de forme ; les plateaux sont poses a la main autour de la prediction : ils ne disent rien des cellules ;
(3) des SCENARIOS ou je change UNE chose a la fois (ou un petit groupe), avec l'effet ECRIT AVANT dans ce fichier (colonne "attendu", fixe par le TEXTE de la piece, pas par ma sortie) ;
(4) pour chaque scenario : mon juge ET sa feuille (par son interface : lecture_lecteur, table, dossier, sortie ; etape --temoins pour la garde) jouent le meme dossier ; je compare le verdict, la garde, et cellule par cellule le statut du lecteur, la lecture, le jugement, la portee.
Sortie : un tableau, un "TIENT" ou "ECHOUE" par scenario, et le total. Aucune 2D, aucune cellule reelle : toutes les largeurs sont posees.
Usage : py -3.11 -P certification_feuille_sommet_machine2_v1.py <feuille de machine 1> <feuille deposee du lecteur> <table gelee JSON> <modele : un vrai lect2D de Q2 (fantome)> <dossier de travail (neuf)>"""
import copy
import importlib.util
import json
import math
import os
import re
import shutil
import subprocess
import sys
from fractions import Fraction as F

FEUILLE_M1, FEUILLE_DEP, TABLE, MODELE, TRAV = sys.argv[1:6]
os.makedirs(TRAV, exist_ok=False)
T = json.load(open(TABLE))
MOD = json.load(open(MODELE))
spec = importlib.util.spec_from_file_location('feuille_deposee', FEUILLE_DEP)
FE = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FE)
KS = list(range(-3, 9))
TOL = T['regle']['tolerance']                     # 0.01
TOL_POS = T['regle']['tolerance_temoin_positif']   # 0.001
TEMOIN_MAX = T['regle']['temoin_max']              # 1e-6
CELLS = {c['id']: c for c in T['cellules']}
TPOS = {w['id']: w for w in T['temoins_positifs']}


# ------------------------------------------------------------------ generateur
def traj_plate(gamma, suivi=True):
    """quatre trajectoires de douze barreaux, plates a gamma (liste de quatre valeurs, ou un nombre)"""
    if not isinstance(gamma, (list, tuple)):
        gamma = [gamma] * 4
    out = {}
    for x, g in zip('ABCD', gamma):
        out[x] = {str(k): {'E_re': -1e-7, 'decalage_repris': False, 'gamma': g, 'gamma_im': g, 'iterations': 3, 'poids_site': 0.95, 'residu': 1e-12, 'suivi': suivi} for k in KS}
    return out


def fichier(pt, signe, traj):
    """pt : dict avec id, w2, g (chaine), m, eta0 (chaine), r_c. Gabarit : un vrai fichier de Q2."""
    d = copy.deepcopy(MOD)
    rc = pt['r_c']
    d['cellule'] = {'P': 5, 'W1': 1.0, 'eta0': float(pt['eta0']), 'g': pt['g'], 'id': pt['id'], 'm': pt['m'], 'r_c': rc, 'w2': pt['w2']}
    d['lecture']['signe'] = signe
    d['lecture']['absorbeurs'] = {'A': {'N': rc + 80, 'bord': rc, 'couches': 80, 'forme': 'F2'}, 'B': {'N': rc + 100, 'bord': rc, 'couches': 100, 'forme': 'F2'},
                                  'C': {'N': rc + 100, 'bord': rc, 'couches': 100, 'forme': 'F1'}, 'D': {'N': rc + 90, 'bord': rc + 10, 'couches': 80, 'forme': 'F2'}}
    d['lecture']['traj'] = traj
    return d


def nom(pt, signe):
    return 'lect2D_%s_%s.json' % (pt['id'], 'fantome' if signe == -1 else 'jumeau')


class Scenario:
    """un dossier de run ; mut(self) change des choses AVANT ecriture"""
    def __init__(self, nom_s):
        self.nom = nom_s
        self.lnq = {}           # id de cellule -> ln q voulu (defaut 0)
        self.profil = {}        # id -> liste de quatre ln(Gamma_X / Gamma_A) (defaut 0)
        self.ftraj = {}         # (id, signe) -> trajectoire de remplacement
        self.dev_pos = {}       # id de temoin positif -> deviation en ln
        self.instrument = 'TIENT'
        self.absent = set()     # noms de fichiers a ne pas ecrire
        self.mut = []           # fonctions (self, dossier) appelees apres ecriture
        self.pt_modifie = {}    # id -> dict de champs de la cellule ecrits dans le fichier (g, eta0, ...)

    def ecrire(self, dos):
        os.makedirs(dos)
        json.dump({'instrument': self.instrument}, open(os.path.join(dos, 'verdict_ter_instrument.json'), 'w'))
        for w in T['temoins_positifs']:
            gam = math.exp(w['ln_Gamma_pl_reference'] + self.dev_pos.get(w['id'], 0.0))
            pt = {'id': w['id'], 'w2': w['w2'], 'g': w['g'], 'm': w['m'], 'eta0': w['eta0'], 'r_c': w['r_c']}
            for signe in (-1, 1):
                tr = self.ftraj.get((w['id'], signe)) or traj_plate(gam if signe == -1 else 1e-40)
                if nom(pt, signe) not in self.absent:
                    json.dump(fichier(dict(pt, **self.pt_modifie.get(w['id'], {})), signe, tr), open(os.path.join(dos, nom(pt, signe)), 'w'))
        for c in T['cellules']:
            gam = math.exp(c['ln_G3'] - self.lnq.get(c['id'], 0.0))
            prof = self.profil.get(c['id'], [0.0, 0.0, 0.0, 0.0])
            pt = {'id': c['id'], 'w2': c['w2'], 'g': c['g'], 'm': c['m'], 'eta0': c['eta0'], 'r_c': c['r_c']}
            for signe in (-1, 1):
                tr = self.ftraj.get((c['id'], signe)) or traj_plate([gam * math.exp(p) for p in prof] if signe == -1 else 1e-40)
                if nom(pt, signe) not in self.absent:
                    json.dump(fichier(dict(pt, **self.pt_modifie.get(c['id'], {})), signe, tr), open(os.path.join(dos, nom(pt, signe)), 'w'))
        for f in self.mut:
            f(self, dos)


# ------------------------------------------------------------------ mon juge, des sections 5 et 6
def lire(dos, pt, signe):
    p = os.path.join(dos, nom(pt, signe))
    return json.load(open(p))['lecture']['traj'] if os.path.isfile(p) else None


def point(dos, pt):
    """section 5 : LECTEUR, ETALEMENT, TEMOIN, POINT LU. rend (statut, motif, Gamma_pl, s)"""
    fan, jum = lire(dos, pt, -1), lire(dos, pt, 1)
    if fan is None or jum is None:
        return 'MANQUE', 'fichier absent', None, None
    J = FE.juger_etat({x: fan[x] for x in 'ABCD'}, None)
    P = J['plateaux']
    if J['statut'] != 'QUALIFIE':
        return J['statut'], 'lecteur %s' % J['statut'], None, None
    gam = P['A']['Gamma_pl']
    s = max([math.log(1.0 + P['A']['etalement'])] + [abs(math.log(P[x]['Gamma_pl'] / gam)) for x in 'BCD'])
    suivies = sum(1 for x in 'ABCD' for k in KS if jum[x][str(k)]['suivi'])
    larg = [abs(jum[x][str(k)]['gamma']) for x in 'ABCD' for k in KS if jum[x][str(k)]['suivi'] and jum[x][str(k)]['gamma'] is not None]
    tient = suivies == 48 and larg and max(larg) <= TEMOIN_MAX * gam
    if not tient:
        return 'QUALIFIE', 'temoin non tenu', gam, s
    return 'LU', '', gam, s


def juge_sommet(dos, etape_temoins=False):
    out = {'guard': None, 'cells': {}, 'S1': None, 'portee': None}
    try:
        inst = json.load(open(os.path.join(dos, 'verdict_ter_instrument.json'))).get('instrument')
    except Exception:
        inst = None
    pos = {}
    for w in T['temoins_positifs']:
        pt = {'id': w['id']}
        st, motif, gam, s = point(dos, pt)
        pos[w['id']] = (st == 'LU' and abs(math.log(gam / math.exp(w['ln_Gamma_pl_reference']))) <= TOL_POS + 1e-15)
        if st == 'MANQUE':
            out['guard'] = 'INCOMPLET'
    if out['guard'] != 'INCOMPLET':
        out['guard'] = 'TIENT' if (inst == 'TIENT' and all(pos.values())) else 'NE TIENT PAS'
    out['guard_detail'] = {'instrument': inst, 'temoins': {k: v for k, v in pos.items()}}
    if etape_temoins or out['guard'] != 'TIENT':
        return out
    lus = {}
    for c in T['cellules']:
        st, motif, gam, s = point(dos, {'id': c['id']})
        if st == 'MANQUE':
            out['S1'] = 'RUN INCOMPLET'
            return out
        if st != 'LU':
            out['cells'][c['id']] = {'lu': False, 'statut': st, 'jug': 'NON LUE'}
            continue
        lnq = math.log(math.exp(c['ln_G3']) / gam)
        b = c['etendue'] + s
        jug = 'TIENT' if abs(lnq) <= TOL - b else ('TOMBE' if abs(lnq) > TOL + b else 'NON JUGEABLE')
        out['cells'][c['id']] = {'lu': True, 'statut': 'QUALIFIE', 'jug': jug, 'lnq': lnq, 'bande': b, 'gam': gam, 's': s}
    tient = [i for i, v in out['cells'].items() if v['jug'] == 'TIENT']
    tombe = [i for i, v in out['cells'].items() if v['jug'] == 'TOMBE']
    jugees = len(tient) + len(tombe)
    par_w2 = {}
    for i in tient:
        par_w2[CELLS[i]['w2']] = par_w2.get(CELLS[i]['w2'], 0) + 1
    w2_ko = any(par_w2.get(w, 0) < 4 for w in set(c['w2'] for c in T['cellules']))
    if len(tombe) >= 2:
        out['S1'] = 'TOMBE'
    elif jugees < 42 or w2_ko:
        out['S1'] = 'NON CONCLUANT'
    elif len(tombe) == 1:
        out['S1'] = 'TENU SAUF UNE CELLULE'
    else:
        out['S1'] = 'TENU'
    par_k = {}
    for i in tient:
        par_k[CELLS[i]['kappa']] = par_k.get(CELLS[i]['kappa'], 0) + 1
    out['portee'] = sorted(k for k, n in par_k.items() if n >= 4)
    out['comptes'] = {'tenues': len(tient), 'tombees': len(tombe), 'jugees': jugees}
    return out


# ------------------------------------------------------------------ sa feuille
def sa_feuille(dos, etape_temoins=False):
    sortie = os.path.join(dos, 'sortie_feuille_m1.json')
    cmd = [sys.executable, '-I', FEUILLE_M1, FEUILLE_DEP, TABLE, dos, sortie] + (['--temoins'] if etape_temoins else [])
    r = subprocess.run(cmd, capture_output=True, text=True)
    res = {'code': r.returncode, 'stdout': r.stdout, 'stderr': r.stderr[-300:], 'json': None}
    if os.path.isfile(sortie):
        res['json'] = json.load(open(sortie))
    return res


if __name__ == '__main__':
    # scenarios : (nom, fabrication, attendu-ecrit-avant)
    TOUS = []

    def sc(nom_s, attendu, fab=None, etape=False):
        s = Scenario(nom_s)
        if fab:
            fab(s)
        TOUS.append((s, attendu, etape))

    idsL = list(CELLS)
    b_of = lambda i: CELLS[i]['etendue']
    # --- verdicts de l'enonce S1
    sc('s01 base : tout a ln q = 0, plateaux plats', {'S1': 'TENU', 'garde': 'TIENT', 'portee': 7})
    sc('s02 une cellule tombe (ln q = +0.02)', {'S1': 'TENU SAUF UNE CELLULE'}, lambda s: s.lnq.update({'MPa4': 0.02}))
    sc('s03 une cellule tombe de l autre cote (ln q = -0.02)', {'S1': 'TENU SAUF UNE CELLULE'}, lambda s: s.lnq.update({'PGb6': -0.02}))
    sc('s04 deux cellules tombent (+0.02, -0.02)', {'S1': 'TOMBE'}, lambda s: s.lnq.update({'MPa4': 0.02, 'PGb6': -0.02}))
    sc('s05 une cellule non jugeable (ln q = 0.01)', {'S1': 'TENU'}, lambda s: s.lnq.update({'MGa3': 0.01}))
    sc('s06 bornes : T - b - 1e-6 (tient), T - b + 1e-6 (non jugeable), T + b - 1e-6 (non jugeable), T + b + 1e-6 (tombe)',
       {'S1': 'TENU SAUF UNE CELLULE', 'jug': {'PPa3': 'TIENT', 'PPa4': 'NON JUGEABLE', 'PPb3': 'NON JUGEABLE', 'PPb4': 'TOMBE'}},
       lambda s: s.lnq.update({'PPa3': TOL - b_of('PPa3') - 1e-6, 'PPa4': TOL - b_of('PPa4') + 1e-6, 'PPb3': TOL + b_of('PPb3') - 1e-6, 'PPb4': TOL + b_of('PPb4') + 1e-6}))
    sc('s07 deux tombent ET quinze non lues : TOMBE l emporte', {'S1': 'TOMBE'},
       lambda s: (s.lnq.update({'MPa4': 0.02, 'PGb6': -0.02}), s.ftraj.update({(i, 1): traj_plate(1e-5 * math.exp(CELLS[i]['ln_G3'])) for i in idsL[1::4][:14]})))
    # --- le lecteur et le temoin
    sc('s08 jumeau trop large a MPa2 : cellule non lue, 55 jugees', {'S1': 'TENU', 'lu': {'MPa2': False}},
       lambda s: s.ftraj.update({('MPa2', 1): traj_plate(1e-5 * math.exp(CELLS['MPa2']['ln_G3']))}))
    sc('s09 jumeau a 0.999999e-6 Gamma_pl a MPa2 : tient (au plus 1e-6)', {'S1': 'TENU', 'lu': {'MPa2': True}},
       lambda s: s.ftraj.update({('MPa2', 1): traj_plate(0.999999e-6 * math.exp(CELLS['MPa2']['ln_G3']))}))
    def jum_non_suivi(s):
        t = traj_plate(1e-40)
        t['C']['4']['suivi'] = False
        s.ftraj[('PPa5', 1)] = t
    sc('s10 jumeau a 47 lectures suivies sur 48 : non lue', {'S1': 'TENU', 'lu': {'PPa5': False}}, jum_non_suivi)
    def sans_plateau_A(s):
        g0 = math.exp(CELLS['MGb2']['ln_G3'])
        t = traj_plate(g0)
        for k in KS:
            t['A'][str(k)]['gamma'] = g0 * (1.2 ** (k + 3))
        s.ftraj[('MGb2', -1)] = t
    sc('s11 pas de plateau sous A a MGb2 : non lue', {'S1': 'TENU', 'lu': {'MGb2': False}}, sans_plateau_A)
    sc('s12 B s ecarte de A de 0.06 en ln a PGa2 : non qualifie, non lue', {'S1': 'TENU', 'lu': {'PGa2': False}}, lambda s: s.profil.update({'PGa2': [0.0, 0.06, 0.0, 0.0]}))
    sc('s13 B s ecarte de A de 0.04 a PGa2 : qualifie, s = 0.04, bande > T : ni tient ni tombe', {'S1': 'TENU', 'lu': {'PGa2': True}, 'jug': {'PGa2': 'NON JUGEABLE'}}, lambda s: s.profil.update({'PGa2': [0.0, 0.04, 0.0, 0.0]}))
    sc('s14 C s ecarte de 0.049 (qualifie) puis D de 0.051 (non qualifie)', {'S1': 'TENU', 'lu': {'MPb5': True, 'MPb6': False}}, lambda s: s.profil.update({'MPb5': [0.0, 0.0, 0.049, 0.0], 'MPb6': [0.0, 0.0, 0.0, 0.051]}))
    def non_lisible_C(s):
        g0 = math.exp(CELLS['PPb7']['ln_G3'])
        t = traj_plate(g0)
        for k in (-1, 2, 5, 8):
            t['C'][str(k)]['suivi'] = False
        s.ftraj[('PPb7', -1)] = t
    sc('s15 C sans cinq barreaux lisibles consecutifs a PPb7 : non lisible, non lue', {'S1': 'TENU', 'lu': {'PPb7': False}}, non_lisible_C)
    def hors_fenetre(s):
        g0 = math.exp(CELLS['MGa1']['ln_G3'])
        t = traj_plate(g0)
        t['C']['8']['suivi'] = False
        s.ftraj[('MGa1', -1)] = t
    sc('s16 une lecture non suivie HORS de la fenetre retenue (C, k = 8) : sans consequence', {'S1': 'TENU', 'lu': {'MGa1': True}}, hors_fenetre)
    def dans_fenetre(s):
        g0 = math.exp(CELLS['MGa1']['ln_G3'])
        t = traj_plate(g0)
        for k in range(-3, 8):
            t['C'][str(k)]['suivi'] = (k % 2 == 0)
        s.ftraj[('MGa1', -1)] = t
    sc('s17 une lecture sur deux non suivie sous C : aucune fenetre de cinq : non lue', {'S1': 'TENU', 'lu': {'MGa1': False}}, dans_fenetre)
    # --- comptes de S1 et portee
    def non_lues(ids):
        return lambda s: s.ftraj.update({(i, 1): traj_plate(1e-5 * math.exp(CELLS[i]['ln_G3'])) for i in ids})
    ids_w2 = lambda pref, n: ['%s%d' % (pref, j) for j in range(1, n + 1)]
    sc('s18 un w2 avec trois cellules non lues (quatre tenues sur sept) : TENU', {'S1': 'TENU'}, non_lues(ids_w2('MPa', 3)))
    sc('s19 un w2 avec quatre cellules non lues (trois tenues) : NON CONCLUANT', {'S1': 'NON CONCLUANT'}, non_lues(ids_w2('MPa', 4)))
    # 14 non lues a raison de <= 3 par w2 : 42 jugees -> TENU ; 15 : 41 -> NON CONCLUANT
    rep = []
    for pref in ('MPa', 'MPb', 'PPa', 'PPb', 'MGa', 'MGb', 'PGa', 'PGb'):
        rep.append(ids_w2(pref, 7)[::2][:3])
    n14 = [i for g in rep for i in g][:14]
    n15 = [i for g in rep for i in g][:15]
    sc('s20 quatorze cellules non lues : 42 jugees : TENU', {'S1': 'TENU'}, non_lues(n14))
    sc('s21 quinze cellules non lues : 41 jugees : NON CONCLUANT', {'S1': 'NON CONCLUANT'}, non_lues(n15))
    kap1 = [CELLS_id for CELLS_id in idsL if CELLS[CELLS_id]['numero_kappa'] == 1]
    kap_n = lambda n, num: [i for i in idsL if CELLS[i]['numero_kappa'] == num][:n]
    sc('s22 le kappa 1 (0.0363) perd 5 cellules sur 8 (3 tenues) : hors portee', {'S1': 'TENU', 'portee_sans': ['0.0363']}, non_lues(kap_n(5, 1)))
    sc('s23 le kappa 1 perd 4 cellules sur 8 (4 tenues) : dans la portee', {'S1': 'TENU', 'portee': 7}, non_lues(kap_n(4, 1)))
    # --- la garde
    sc('s24 instrument NON TENU : rien n est lu ni juge', {'garde': 'NE TIENT PAS'}, lambda s: setattr(s, 'instrument', 'NE TIENT PAS'))
    sc('s25 temoin positif hors de sa reference de 0.002 : la garde ne tient pas', {'garde': 'NE TIENT PAS'}, lambda s: s.dev_pos.update({'Qd': 0.002}))
    sc('s26 temoin positif a 0.0009 de sa reference : la garde tient', {'garde': 'TIENT', 'S1': 'TENU'}, lambda s: s.dev_pos.update({'Q2b': 0.0009}))
    sc('s27 temoin positif a -0.0011 : la garde ne tient pas', {'garde': 'NE TIENT PAS'}, lambda s: s.dev_pos.update({'Qa': -0.0011}))
    def pos_non_qualifie(s):
        g0 = math.exp(TPOS['Qc']['ln_Gamma_pl_reference'])
        s.ftraj[('Qc', -1)] = traj_plate([g0, g0 * math.exp(0.06), g0, g0])
    sc('s28 temoin positif non qualifie (B a 0.06) : la garde ne tient pas', {'garde': 'NE TIENT PAS'}, pos_non_qualifie)
    sc('s29 jumeau d un temoin positif trop large : la garde ne tient pas', {'garde': 'NE TIENT PAS'}, lambda s: s.ftraj.update({('Q2d', 1): traj_plate(1e-5 * math.exp(TPOS['Q2d']['ln_Gamma_pl_reference']))}))
    # --- fichiers et formes
    sc('s30 fichier d une cellule absent : RUN INCOMPLET, rien n est juge', {'S1': 'RUN INCOMPLET'}, lambda s: s.absent.add('lect2D_PGb7_fantome.json'))
    sc('s31 fichier d un temoin positif absent : rien n est juge', {'garde': 'INCOMPLET'}, lambda s: s.absent.add('lect2D_Qe_jumeau.json'))
    sc('s32 couplage ecrit different dans un fichier de cellule : refuse', {'refus': True}, lambda s: s.pt_modifie.update({'MGb4': {'g': '5.59520e-04'}}))
    sc('s33 eta0 different dans un fichier de cellule : refuse', {'refus': True}, lambda s: s.pt_modifie.update({'PPa6': {'eta0': '1.22138e-03'}}))
    sc('s34 r_c different (et boites coherentes) dans un fichier : refuse', {'refus': True}, lambda s: s.pt_modifie.update({'PGa7': {'r_c': 20}}))
    def mauvais_canon(s, dos):
        p = os.path.join(dos, 'lect2D_MPa1_fantome.json')
        d = json.load(open(p))
        d['pilote_canon'] = '0000000000000000'
        json.dump(d, open(p, 'w'))
    sc('s35 canon du pilote de lecture different dans un fichier : refuse', {'refus': True}, lambda s: s.mut.append(mauvais_canon))
    def mauvais_bloc(s, dos):
        p = os.path.join(dos, 'lect2D_MPa1_jumeau.json')
        d = json.load(open(p))
        d['bloc_sha256_16'] = '0000000000000000'
        json.dump(d, open(p, 'w'))
    sc('s36 empreinte du bloc du lecteur differente : refuse', {'refus': True}, lambda s: s.mut.append(mauvais_bloc))
    def trois_barreaux(s, dos):
        p = os.path.join(dos, 'lect2D_MPa1_fantome.json')
        d = json.load(open(p))
        del d['lecture']['traj']['B']['8']
        json.dump(d, open(p, 'w'))
    sc('s37 une trajectoire de onze barreaux : refuse', {'refus': True}, lambda s: s.mut.append(trois_barreaux))

    bilan = []
    for s, att, etape in TOUS:
        dos = os.path.join(TRAV, s.nom.split()[0])
        s.ecrire(dos)
        # garde seule + verdict
        dosg = dos + '_garde'
        os.makedirs(dosg)
        for f in os.listdir(dos):
            if not re.match(r'lect2D_(MP|PP|MG|PG)[ab]\d_', f) and f != 'sortie_feuille_m1.json':
                shutil.copy(os.path.join(dos, f), os.path.join(dosg, f))
        mj_g = juge_sommet(dosg, True)
        sf_g = sa_feuille(dosg, True)
        mj = juge_sommet(dos, False)
        sf = sa_feuille(dos, False)
        ok, raisons = True, []
        J = sf['json'] or {}
        # attendus ecrits avant
        if att.get('refus'):
            vv = str((sf['json'] or {}).get('verdict', ''))
            refus = vv.startswith(('REFUS', 'RUN INCOMPLET')) and not (sf['json'] or {}).get('S1', {}).get('issue') and not any((c.get('jugement') in ('TIENT', 'TOMBE', 'NON JUGEABLE')) for c in (sf['json'] or {}).get('cellules', []))
            # mon juge n'a pas a refuser : seul sa feuille a le controle de forme (G-3) ; je note ce que MON juge rend sur le meme dossier
            if not refus:
                ok = False
                raisons.append('sa feuille ne rend pas RUN INCOMPLET sur le dossier malforme (code %s, %s)' % (sf['code'], sf['stdout'][-120:].replace('\n', ' | ')))
        else:
            if 'garde' in att:
                if mj['guard'] != att['garde']:
                    ok = False
                    raisons.append('mon juge : garde %s, attendu ecrit %s' % (mj['guard'], att['garde']))
                gm = (sf_g['json'] or {}).get('verdict', '')
                g_attendu_tient = att['garde'] == 'TIENT'
                if g_attendu_tient != gm.startswith('TIENT'):
                    ok = False
                    raisons.append('sa garde : %r, attendu %s' % (gm, att['garde']))
            if 'S1' in att:
                if mj['S1'] != att['S1']:
                    ok = False
                    raisons.append('mon juge : S1 %s, attendu ecrit %s' % (mj['S1'], att['S1']))
                v = J.get('verdict', '') if J else ''
                if J and (att['S1'] not in v):
                    ok = False
                    raisons.append('sa feuille : verdict %r, attendu %s' % (v, att['S1']))
                if not J and att['S1'] not in ('RUN INCOMPLET',):
                    ok = False
                    raisons.append('sa feuille n a rien ecrit (code %s)' % sf['code'])
            if 'portee' in att and len(mj['portee'] or []) != att['portee']:
                ok = False
                raisons.append('mon juge : portee %s, attendu ecrit %d kappa' % (mj['portee'], att['portee']))
            for kp in att.get('portee_sans', []):
                if kp in (mj['portee'] or []):
                    ok = False
                    raisons.append('mon juge : le kappa %s est dans la portee, attendu ecrit : hors' % kp)
            for i, v in (att.get('lu') or {}).items():
                if mj['cells'].get(i, {}).get('lu') != v:
                    ok = False
                    raisons.append('mon juge : %s lue = %s, attendu ecrit %s' % (i, mj['cells'].get(i, {}).get('lu'), v))
            for i, v in (att.get('jug') or {}).items():
                if mj['cells'].get(i, {}).get('jug') != v:
                    ok = False
                    raisons.append('mon juge : %s jugement = %s, attendu ecrit %s' % (i, mj['cells'].get(i, {}).get('jug'), v))
        if not att.get('refus') and J and J.get('cellules') and mj['S1'] and mj['S1'] != 'RUN INCOMPLET':
            ncmp = 0
            for c in J['cellules']:
                m_ = mj['cells'][c['id']]
                tc = CELLS[c['id']]
                ncmp += 1
                if bool(c['lu']) != m_['lu'] or c['jugement'] != m_['jug']:
                    ok = False
                    raisons.append('cellule %s : sa feuille lu=%s jugement=%s ; mon juge lu=%s jugement=%s' % (c['id'], c['lu'], c['jugement'], m_['lu'], m_['jug']))
                    continue
                if m_['lu']:
                    for cle, mien in (('ln_q', m_['lnq']), ('bande', m_['bande']), ('ln_Gamma_pl', math.log(m_['gam'])), ('etalement_du_lecteur', m_['s'])):
                        if abs(c[cle] - mien) > 1e-9:
                            ok = False
                            raisons.append('cellule %s : %s : sa feuille %.12g ; mon juge %.12g' % (c['id'], cle, c[cle], mien))
                    cs = c['consigne']
                    dl = tc['delta']
                    chk = (('ln_q_ordre1', tc['ln_G1'] - math.log(m_['gam'])), ('ln_q_ordre2', tc['ln_G2'] - math.log(m_['gam'])), ('ln_Phi_lu', math.log(m_['gam']) - math.log(abs(dl))), ('ln_Phi_chaine', tc['ln_Phi']))
                    for cle, mien in chk:
                        if abs(cs[cle] - mien) > 1e-9:
                            ok = False
                            raisons.append('cellule %s : consigne %s : sa feuille %.12g ; mon calcul %.12g' % (c['id'], cle, cs[cle], mien))
                    if cs['signe_de_delta'] != (1 if dl > 0 else -1) or (abs(m_['lnq']) > 1e-9 and cs['signe_de_ln_q'] != (1 if m_['lnq'] > 0 else -1)):
                        ok = False
                        raisons.append('cellule %s : signes consignes : %s / mon calcul %s %s' % (c['id'], (cs['signe_de_delta'], cs['signe_de_ln_q']), 1 if dl > 0 else -1, m_['lnq']))
            if J['S1']['issue'] != mj['S1'] or sorted(J['S1']['portee_kappa']) != sorted(mj['portee']):
                ok = False
                raisons.append('S1 : sa feuille %s portee %s ; mon juge %s portee %s' % (J['S1']['issue'], J['S1']['portee_kappa'], mj['S1'], mj['portee']))
            # paires miroirs : cellules de meme kappa et de meme |delta|, signes opposes
            mi = {}
            for i, cl in CELLS.items():
                mi.setdefault((cl['kappa'], round(abs(cl['delta']) * 1e9)), []).append(i)
            mien_p = {}
            for (kp, ad), ids in mi.items():
                neg = [i for i in ids if CELLS[i]['delta'] < 0]
                pos = [i for i in ids if CELLS[i]['delta'] > 0]
                if neg and pos and mj['cells'][neg[0]]['lu'] and mj['cells'][pos[0]]['lu']:
                    a, b_ = mj['cells'][neg[0]], mj['cells'][pos[0]]
                    mien_p[kp] = (neg[0], pos[0], math.log(a['gam'] / abs(CELLS[neg[0]]['delta'])) - math.log(b_['gam'] / abs(CELLS[pos[0]]['delta'])))
            ses_p = {x['kappa']: (x['moins'], x['plus'], x['ln_rapport_lu']) for x in J['consigne']['paires_miroirs']}
            for kp in set(mien_p) | set(ses_p):
                if kp not in mien_p or kp not in ses_p or mien_p[kp][:2] != ses_p[kp][:2] or abs(mien_p[kp][2] - ses_p[kp][2]) > 1e-9:
                    ok = False
                    raisons.append('paire miroir kappa %s : sa feuille %s ; mon calcul %s' % (kp, ses_p.get(kp), mien_p.get(kp)))
        bilan.append((s.nom, ok, raisons, mj, sf, mj_g, sf_g))
        print('%s : %s' % ('TIENT ' if ok else 'ECHOUE', s.nom))
        for r in raisons:
            print('        - %s' % r)
    # s38 : la garde refuse un dossier ou une cellule a deja un fichier
    d0 = os.path.join(TRAV, 's01')
    if os.path.isfile(os.path.join(d0, 'sortie_feuille_m1.json')):
        os.remove(os.path.join(d0, 'sortie_feuille_m1.json'))
    r38 = sa_feuille(d0, True)
    ok38 = r38['code'] != 0 and str((r38['json'] or {}).get('verdict', '')).startswith('REFUS')
    print('%s : s38 la garde (--temoins) REFUSE un dossier ou une cellule a deja un fichier (code %s)' % ('TIENT ' if ok38 else 'ECHOUE', r38['code']))
    bilan.append(('s38 refus de la garde', ok38, [] if ok38 else ['la garde ne refuse pas'], {}, r38, {}, r38))
    # sa sortie JSON : cles, pour la comparaison cellule par cellule (second temps)
    json.dump({'scenarios': [{'nom': b[0], 'ok': b[1], 'raisons': b[2], 'mon_juge': {k: v for k, v in b[3].items()}, 'sa_sortie': (b[4]['json'] or {}), 'sa_garde': (b[6]['json'] or {})} for b in bilan]}, open(os.path.join(TRAV, 'bilan.json'), 'w'), indent=1, default=str)
    print('\nSCENARIOS : %d ; TIENNENT %d ; ECHOUENT %d' % (len(bilan), sum(1 for b in bilan if b[1]), sum(1 for b in bilan if not b[1])))
