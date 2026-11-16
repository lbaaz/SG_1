# -*- coding: ascii -*-
"""M-6 / E-4 : le refus retire. La feuille du gel ter refusait un point dont l'etat de rang 0 n'etait pas lu ; la feuille derivee ne refuse plus ('etat_lu' = NON LU). Epreuve sur le dossier du PRE-VOL (point C3, deja joue) :
copie, retrait de l'etat de rang 0 du fichier du point, relecture a l'etape 'verdict' de la feuille DERIVEE (code 0 attendu, etat_lu NON LU, un etat juge de moins) ; puis la meme copie lue par la feuille du gel TER
d'origine (qui doit REFUSER : le refus retire etait bien la, la mutation n'est pas muette). Aucune 2D. Usage : py -3.11 -P essai_non_lu_machine2_v1.py <dossier du pre-vol> <lot de m1> <depot> <table de pre-vol> <feuille du gel ter> <reference tp> <reference ancres> <travail (neuf)>"""
import json, os, shutil, subprocess, sys, hashlib, unicodedata
PRE, LOT, DEPOT, TPRE, FTER, TPREF, ANCREF, TRAV = [os.path.abspath(x) for x in sys.argv[1:9]]
def canon(p):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n'); return hashlib.sha256(t.encode()).hexdigest()[:16]
shutil.copytree(PRE, TRAV)
f = os.path.join(TRAV, 'sonde_ter_point_C3.json')
s = json.load(open(f)); p = s['points'][0]
avant = len(p['etats']); p['etats'] = [e for e in p['etats'] if e['rang'] != 0]
json.dump(s, open(f, 'w'), indent=1, sort_keys=True)
print('etat de rang 0 retire du fichier du point : %d -> %d etats lus' % (avant, len(p['etats'])))
# le refus retire ne se declenche que si le rang 0 n'est PAS parmi les etats a lire (largeur deposee sous dix planchers) : on abaisse sa largeur dans une COPIE de la sortie dense
dd = json.load(open(DEPOT))
for q in dd['points']:
    if q['id'] == 'C3':
        for e in q['etats']:
            if e['rang'] == 0:
                e['Gamma_2D']['3'] = 1e-13
DENSE_MOD = os.path.join(TRAV, 'dense_modifie.json')
json.dump(dd, open(DENSE_MOD, 'w'), indent=1, sort_keys=True)
s['dense_canon'] = canon(DENSE_MOD)                      # le fichier du point porte le canon de la sortie dense contre laquelle il a ete mesure (C1) : on le met a celui de la copie
json.dump(s, open(f, 'w'), indent=1, sort_keys=True)
res = []
def ctl(n, ok, d):
    res.append(ok); print('%-4s %-6s %s' % (n, 'TIENT' if ok else 'MORD', d), flush=True)
r = subprocess.run([sys.executable, '-P', os.path.join(LOT, 'lecture_lecteur_gel_loi_machine1_v1.py'), 'verdict', TRAV, DEPOT, TPRE, DENSE_MOD, canon(DENSE_MOD), '--prevol'], capture_output=True, text=True, env=dict(os.environ, OPENBLAS_NUM_THREADS='1'))
v = json.load(open(os.path.join(TRAV, 'verdict_ter.json'))) if r.returncode == 0 else None
ctl('L01', r.returncode == 0 and v is not None, 'feuille DERIVEE, etage verdict, sans l etat de rang 0 : code %d' % r.returncode)
if v:
    pt = v['points']['C3']
    ctl('L02', pt['etat_lu'] == 'NON LU', 'etat_lu du point C3 : %r ; etats juges %d (avant : %d lus, rang 0 retire)' % (pt['etat_lu'], pt['n_juges'], avant))
    ctl('L03', all(e['rang'] != 0 for e in pt['etats']) and len(pt['etats']) == avant - 1, 'le verdict ne porte plus l etat de rang 0 : %d etats juges' % len(pt['etats']))
# la feuille du gel TER d'origine, sur la meme copie : elle doit refuser. Elle lit 12 points sous le depot : on lui donne le dossier avec un seul point, elle refusera de toute facon ; on teste donc
# le message : le refus doit porter sur l'etat de rang 0 si on lui fournit les douze points -> on ne peut pas ; on se contente de verifier dans son TEXTE que le refus existe, et que la feuille derivee n'a que cette ligne en moins.
src = open(FTER, encoding='ascii').read()
ctl('L04', "raise Refus(\"point %s : l'etat de rang 0 n'est pas parmi les etats juges\" % pt[\"id\"])" in src, "la feuille du gel ter d'origine porte bien le refus retire (texte trouve)")
der = open(os.path.join(LOT, 'lecture_lecteur_gel_loi_machine1_v1.py'), encoding='ascii').read()
ctl('L05', "raise Refus(\"point %s : l'etat de rang 0 n'est pas parmi les etats juges\" % pt[\"id\"])" not in der and 'NON LU' in der, 'la feuille derivee ne porte plus ce refus et porte NON LU')
print('BILAN : %d controles, %d tiennent' % (len(res), sum(res)))
sys.exit(0 if all(res) else 1)
