# -*- coding: ascii -*-
"""BANC DE SORTIES de machine 2 pour la feuille ter de machine 1 (b2d6d7cfaf30f1cf) : ce que son selftest et son banc ne jouent PAS.
Le selftest de la feuille ne couvre que plateau, etat, cascade, issue de (e) et la tolerance de l'etage 0 ; les etapes "instrument" (juger_etage0,
juger_ancres, juger_etage1, controler_entete) et "verdict" (juger_point, lecture des fichiers) n'ont jamais tourne sur des sorties alterees.
  PARTIE I  : l'etape "instrument" sur MES sorties du pre-vol de sa sonde (qui rendent TIENT), puis sur des COPIES ALTEREES, 21 alterations ; chaque
              alteration a une reponse attendue DECLAREE ICI avant le passage : REFUS (code 2), NE TIENT PAS, ou TIENT (pas de fausse alerte) ;
  PARTIE II : l'etape "verdict" sur des sorties synthetiques aux douze points (les vrais etats juges du depot, des trajectoires fabriquees), 12 scenarios ;
              la reponse attendue est calculee par MA feuille (feuille_independante_ter_machine2_v1.py) sur les memes trajectoires, ou REFUS.
Aucune sonde n'est jouee, aucun calcul 2D : il n'y a que des fichiers.
Usage : py -3.11 -I banc_sorties_ter_machine2_v1.py <dossier lot m1> <prevol> <sonde_ordre2.json> <tp_reference.json> <travail> <sortie.json>"""
import copy
import importlib.util
import json
import math
import os
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import feuille_independante_ter_machine2_v1 as MA

LOT, PREVOL, DEPOT, TPREF, TRAVAIL, SORTIE = [os.path.abspath(a) for a in sys.argv[1:7]]
FEUILLE = os.path.join(LOT, 'lecture_qualification_EB_ter_machine1_v1.py')
REFANC = os.path.join(LOT, 'reference_ancres_ter_machine1_v1.json')
spec = importlib.util.spec_from_file_location('feuille_m1', FEUILLE)
M1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M1)
os.makedirs(TRAVAIL, exist_ok=True)
resultats = []


def jl(p):
    return json.load(open(p))


def ecrire(p, o):
    json.dump(o, open(p, 'w'), indent=1, sort_keys=True)


def lancer(args):
    r = subprocess.run([sys.executable, '-I', FEUILLE] + args, capture_output=True, text=True)
    return r.returncode, r.stdout


def verdict_instrument(dossier, depot=DEPOT, tp=TPREF, anc=REFANC):
    code, out = lancer(['instrument', dossier, depot, tp, anc])
    if code == 2:
        return 'REFUS'
    v = jl(os.path.join(dossier, 'verdict_ter_instrument.json'))
    return 'TIENT' if v['instrument'] == 'TIENT' else 'NE TIENT PAS'


def copie(nom):
    d = os.path.join(TRAVAIL, nom)
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    for f in ('sonde_ter_etage0.json', 'sonde_ter_ancres.json', 'sonde_ter_etage1.json'):
        shutil.copy(os.path.join(PREVOL, f), os.path.join(d, f))
    return d


def noter(nom, attendu, obtenu):
    ok = (obtenu != 'TIENT') if attendu == 'PAS TIENT' else (attendu == obtenu)
    resultats.append({'nom': nom, 'attendu': attendu, 'obtenu': obtenu, 'ok': ok})
    print('  %-62s attendu %-12s obtenu %-12s %s' % (nom, attendu, obtenu, 'OK' if ok else 'MORD'), flush=True)


# ------------------------------------------------------------------ PARTIE I
print('PARTIE I : etape "instrument"')
base = copie('base')
noter('I00 base : mes sorties du pre-vol', 'TIENT', verdict_instrument(base))


def alterer(nom, attendu, fichier, f, depot=DEPOT, tp=TPREF, anc=REFANC):
    d = copie(nom.split()[0])
    p = os.path.join(d, fichier)
    o = jl(p)
    f(o)
    ecrire(p, o)
    noter(nom, attendu, verdict_instrument(d, depot, tp, anc))


def e0(o, i=0, j=3, k='3', facteur=None, absolu=None, suivi=None):
    t = o['points'][i]['etats'][j]['traj']['depot'][k]
    if facteur is not None:
        t['gamma'] *= facteur
    if absolu is not None:
        t['gamma'] += absolu
    if suivi is not None:
        t['suivi'] = suivi


alterer('I01 etage 0 : une largeur +0.2 %', 'NE TIENT PAS', 'sonde_ter_etage0.json', lambda o: e0(o, facteur=1.002))
alterer('I02 etage 0 : une largeur +0.05 % (dans la tolerance)', 'TIENT', 'sonde_ter_etage0.json', lambda o: e0(o, facteur=1.0005))
alterer('I03 etage 0 : une largeur non suivie', 'NE TIENT PAS', 'sonde_ter_etage0.json', lambda o: e0(o, suivi=False))
alterer('I04 etage 0 : un etat retire', 'REFUS', 'sonde_ter_etage0.json', lambda o: o['points'][1]['etats'].pop())
alterer('I05 etage 0 : canon de la sonde altere', 'REFUS', 'sonde_ter_etage0.json', lambda o: o.__setitem__('sonde_canon', '0000000000000000'))
alterer('I06 etage 0 : reglage altere (poids_min 0.4)', 'REFUS', 'sonde_ter_etage0.json', lambda o: o['reglage'].__setitem__('poids_min', 0.4))
alterer('I07 etage 0 : mode altere', 'REFUS', 'sonde_ter_etage0.json', lambda o: o.__setitem__('mode', 'ancres'))
alterer('I08 etage 0 : un point echange (ordre A2, A1)', 'REFUS', 'sonde_ter_etage0.json', lambda o: o['points'].reverse())


def an(o, i=0, j=0, ab='A', k='3', facteur=None, suivi=None):
    t = o['points'][i]['etats'][j]['traj'][ab][k]
    if facteur is not None:
        t['gamma'] *= facteur
    if suivi is not None:
        t['suivi'] = suivi


alterer('I09 ancres : une largeur x (1 + 2e-6)', 'NE TIENT PAS', 'sonde_ter_ancres.json', lambda o: an(o, facteur=1.000002))
alterer('I10 ancres : une largeur x (1 + 5e-7)', 'TIENT', 'sonde_ter_ancres.json', lambda o: an(o, facteur=1.0000005))
alterer('I11 ancres : un statut de suivi change', 'NE TIENT PAS', 'sonde_ter_ancres.json', lambda o: an(o, ab='C', k='-3', suivi=False))
alterer('I12 ancres : les rangs 0 et 1 d\'une ancre echanges', 'NE TIENT PAS', 'sonde_ter_ancres.json', lambda o: (o['points'][0]['etats'][0].__setitem__('traj', o['points'][0]['etats'][1]['traj'])))
alterer('I13 ancres : un absorbeur retire', 'REFUS', 'sonde_ter_ancres.json', lambda o: o['points'][1]['etats'][0]['traj'].pop('D'))
alterer('I14 ancres : un barreau retire', 'REFUS', 'sonde_ter_ancres.json', lambda o: o['points'][0]['etats'][1]['traj']['B'].pop('8'))
alterer('I15 ancres : un etat de rang 2 ajoute', 'REFUS', 'sonde_ter_ancres.json', lambda o: o['points'][0]['etats'].append(copy.deepcopy(o['points'][0]['etats'][0]) | {'rang': 2}))


def tp(o, j=0, ab='C', facteur=1.0):
    for rec in o['temoin'][j]['traj'][ab].values():
        rec['gamma'] *= facteur


alterer('I16 temoin positif : j = 6 sous C x exp(0.06)', 'NE TIENT PAS', 'sonde_ter_etage1.json', lambda o: tp(o, 0, 'C', math.exp(0.06)))
alterer('I17 temoin positif : j = 6 sous C x exp(0.04)', 'TIENT', 'sonde_ter_etage1.json', lambda o: tp(o, 0, 'C', math.exp(0.04)))


def tn_plat(o):
    for k, rec in o['temoin_negatif'][0]['traj']['B'].items():
        rec['gamma'] = 1e-10


alterer('I18 temoin negatif : A1 sous B rend un plateau', 'NE TIENT PAS', 'sonde_ter_etage1.json', tn_plat)
alterer('I19 temoin positif : un barreau retire', 'REFUS', 'sonde_ter_etage1.json', lambda o: o['temoin'][1]['traj']['A'].pop('-3'))
alterer('I20 temoin : liste des retenus alteree (j = 6 devient 7)', 'PAS TIENT', 'sonde_ter_etage1.json', lambda o: o['temoin'][0].__setitem__('j', 7))

# alterations des fichiers d'entree : la feuille doit refuser un canon qui n'est pas le sien
d = copie('I21')
dep_alt = os.path.join(d, 'depot_altere.json')
t = open(DEPOT, 'rb').read()
assert b'"id": "A1"' in t
open(dep_alt, 'wb').write(t.replace(b'"id": "A1"', b'"id": "A1 "', 1))
noter('I21 depot altere d un octet', 'REFUS', verdict_instrument(d, depot=dep_alt))
d = copie('I22')
tp_alt = os.path.join(d, 'tp_altere.json')
assert b'"p": 5' in open(TPREF, 'rb').read()
open(tp_alt, 'wb').write(open(TPREF, 'rb').read().replace(b'"p": 5', b'"p": 7', 1))
noter('I22 table de reference du temoin alteree', 'REFUS', verdict_instrument(d, tp=tp_alt))
d = copie('I23')
anc_alt = os.path.join(d, 'anc_altere.json')
assert b'"mode": "ancres"' in open(REFANC, 'rb').read()
open(anc_alt, 'wb').write(open(REFANC, 'rb').read().replace(b'"mode": "ancres"', b'"mode": "ancrEs"', 1))
noter('I23 reference des ancres alteree', 'REFUS', verdict_instrument(d, anc=anc_alt))

# ------------------------------------------------------------------ PARTIE II
print('')
print('PARTIE II : etape "verdict" sur des sorties synthetiques aux douze points')
dep = jl(DEPOT)
PD = {p['id']: p for p in dep['points']}
KS = list(range(-3, 9))
ETA = {k: 0.05 * 2.0 ** (-k) for k in KS}


def juges(i):
    return [e for e in PD[i]['etats'] if (e.get('Gamma_2D') or {}).get('3') is not None and e['Gamma_2D']['3'] > 1.33e-12]


def plateau_traj(base, bruit=0.001):
    return {str(k): {'gamma': base * (1.0 + bruit * (-1) ** k), 'suivi': True, 'poids_site': 0.9, 'residu': 1e-13} for k in KS}


def lineaire(base):
    return {str(k): {'gamma': base * ETA[k] / ETA[3], 'suivi': True, 'poids_site': 0.9, 'residu': 1e-13} for k in KS}


def non_suivi(base):
    return {str(k): {'gamma': base, 'suivi': False, 'poids_site': 0.1, 'residu': 1.0} for k in KS}


def fabrique(defauts=None, ecart_dep=0.0, absents=(), doublons=(), entete=None, etat_en_trop=None, etat_manquant=None):
    """Renvoie {id: objet point}. defauts : {(id, rang): {'C': 'lin', 'D': 'non'}} ; ecart_dep : {(id, rang): ln de G_dep / Gamma_pl(A)}."""
    defauts = defauts or {}
    pts = {}
    for i in M1.JUGES:
        if i in absents:
            continue
        etats = []
        for e in juges(i):
            g3 = e['Gamma_2D']['3']
            ed = ecart_dep.get((i, e['rang']), 0.0) if isinstance(ecart_dep, dict) else ecart_dep
            base = g3 * math.exp(-ed)                     # Gamma_pl(A) tel que ln(G_dep / Gamma_pl) = ed
            traj = {x: plateau_traj(base * (1.0 + 0.0005 * n)) for n, x in enumerate('ABCD')}
            for x, t in defauts.get((i, e['rang']), {}).items():
                traj[x] = lineaire(base) if t == 'lin' else non_suivi(base)
            etats.append({'rang': e['rang'], 'n1': e['n1'], 'n2': e['n2'], 'E_depart': e['E_re'], 'G_dep': e['Gamma_2D'], 'traj': traj})
        if etat_en_trop and i == etat_en_trop:
            etats.append(dict(etats[0], rang=99))
        if etat_manquant and i == etat_manquant:
            etats.pop()
        pts[i] = {'id': i, 'w2': PD[i]['w2'], 'facteur': PD[i]['facteur'], 'g': PD[i]['g'], 'r_c': PD[i]['r_c'], 'eta0': PD[i]['eta0'], 'etats': etats}
    return pts


def ecrire_dossier(nom, pts, instrument='TIENT', entete=None, doublon=None):
    d = os.path.join(TRAVAIL, nom)
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    ecrire(os.path.join(d, 'verdict_ter_instrument.json'), {'instrument': instrument, 'motifs': []})
    for i, p in pts.items():
        s = {'sonde': 'sonde_qualification_EB_ter_machine1_v1', 'sonde_canon': M1.CANON_SONDE, 'moteur_canon': M1.CANON_MOTEUR, 'depot_canon': M1.CANON_DEPOT,
             'retenus_canon': M1.CANON_RETENUS, 'mode': 'point', 'ids': [i], 'reglage': M1.REGLAGE, 'points': [p]}
        if entete:
            s.update(entete)
        ecrire(os.path.join(d, 'sonde_ter_point_%s.json' % i), s)
        if doublon == i:
            ecrire(os.path.join(d, 'sonde_ter_point_%s_bis.json' % i), s)
    return d


def jouer_verdict(d):
    code, out = lancer(['verdict', d, DEPOT])
    if code == 2:
        return 'REFUS', None
    return jl(os.path.join(d, 'verdict_ter.json'))['verdict'], jl(os.path.join(d, 'verdict_ter.json'))


def attendu_ma(pts, instrument=True):
    """Le verdict que MA feuille rend sur les memes trajectoires."""
    lus, nj, nq, npl, nlu = {}, 0, 0, 0, 0
    for i, p in pts.items():
        for e in p['etats']:
            if e['rang'] == 99:
                continue
            j = MA.juger_etat(e['traj'], e['G_dep']['3'])
            nj += 1
            nq += j['statut'] == 'QUALIFIE'
            npl += j['lu'] is not None
            nlu += j['lu'] is True
            if e['rang'] == 0:
                lus[i] = j['statut']
    return MA.cascade(instrument, lus, nj, nq), MA.issue_consigne(npl, nlu), (nj, nq, npl, nlu)


def scenario(nom, pts, attendu=None, **kw):
    d = ecrire_dossier(nom.split()[0], pts, **kw)
    obtenu, v = jouer_verdict(d)
    if attendu is None:
        attendu, issue_att, comptes = attendu_ma(pts, kw.get('instrument', 'TIENT') == 'TIENT')
        ok_issue = True
        if v is not None and kw.get('instrument', 'TIENT') == 'TIENT':
            ok_issue = (v['issue_depot'] == issue_att and (v['n_juges'], v['n_qualifies'], v['n_plateau_A'], v['n_lus_sur_le_plateau']) == comptes)
        if not ok_issue:
            noter(nom + ' (issue de (e) et comptes)', issue_att + ' %s' % (comptes,), '%s %s' % (v['issue_depot'], (v['n_juges'], v['n_qualifies'], v['n_plateau_A'], v['n_lus_sur_le_plateau'])))
    noter(nom, attendu, obtenu)


tous0 = {(i, 0) for i in M1.JUGES}
scenario('V01 tout QUALIFIE, depot a 0.01 du plateau', fabrique(ecart_dep=0.01))
# 14 etats NON QUALIFIES (pas de plateau sous C), aucun de rang 0 : 123 sur 137, juste sous les neuf dixiemes
rang_ge1 = [(i, e['rang']) for i in M1.JUGES for e in juges(i) if e['rang'] >= 1]
scenario('V02 14 etats non qualifies (123 sur 137)', fabrique(defauts={t: {'C': 'lin'} for t in rang_ge1[:14]}, ecart_dep=0.01))
scenario('V03 13 etats non qualifies (124 sur 137)', fabrique(defauts={t: {'C': 'lin'} for t in rang_ge1[:13]}, ecart_dep=0.01))
scenario('V04 etat lu de C1 non qualifie', fabrique(defauts={('C1', 0): {'C': 'lin'}}, ecart_dep=0.01))
scenario('V05 etats lus tous non qualifies', fabrique(defauts={t: {'B': 'lin'} for t in tous0}, ecart_dep=0.01))
scenario('V06 etats lus tous non lisibles', fabrique(defauts={t: {'D': 'non'} for t in tous0}, ecart_dep=0.01))
scenario('V07 L4 absent', fabrique(absents=('L4',), ecart_dep=0.01), attendu='RUN INCOMPLET')
scenario('V08 L4 lu deux fois', fabrique(ecart_dep=0.01), attendu='REFUS', doublon='L4')
scenario('V09 canon de la sonde altere dans un point', fabrique(ecart_dep=0.01), attendu='REFUS', entete={'sonde_canon': '1111111111111111'})
scenario('V10 un etat de trop a C1', fabrique(ecart_dep=0.01, etat_en_trop='C1'), attendu='REFUS')
scenario('V11 un etat manquant a M2', fabrique(ecart_dep=0.01, etat_manquant='M2'), attendu='REFUS')
scenario('V12 instrument ne tient pas', fabrique(ecart_dep=0.01), attendu="NON CONCLUANT D'INSTRUMENT", instrument='NE TIENT PAS')
# consigne (e) : 15 etats a 0.06 du plateau sur 137 (122 sur 137 = 89 %, sous les neuf dixiemes), tous QUALIFIES
dep6 = {t: 0.06 for t in rang_ge1[:15]}
scenario('V13 consigne (e) : 15 etats sur 137 a 0.06 du plateau', fabrique(ecart_dep=dep6))
dep6b = {t: 0.06 for t in rang_ge1[:13]}
scenario('V14 consigne (e) : 13 etats sur 137 a 0.06 du plateau', fabrique(ecart_dep=dep6b))

print('')
n = len(resultats)
nok = sum(1 for r in resultats if r['ok'])
print('BANC DE SORTIES : %d cas, %d conformes a l attendu declare, %d mordent' % (n, nok, n - nok))
ecrire(SORTIE, resultats)
sys.exit(0 if nok == n else 1)
