# -*- coding: ascii -*-
"""MON BALAYAGE DE VIRGINITE (certification (d)) du gel "SOMMET" : mes archives contiennent-elles la trace d'un calcul 2D (systeme a fantome OU jumeau) a l'un des 80 w2 CANDIDATS ?
Candidats : w2 = 2 +/- k / 100000, MP et PP k = 5 a 20 sauf 10 ; MG et PG k = 25 a 49. Trois balayages :
 (1) TEXTE : l'ecriture decimale a cinq decimales (jeton isole), sa forme sans zero final ("1.9998"), et la fraction irreductible ("9999/5000") ; fichiers .json .log .py .md .txt .csv .sh .tsv et membres texte des .zip lisibles ;
 (2) JSON STRUCTURE : toute cle "w2", "w2n" ou "w2_frac" dont la valeur (chaine, fraction ou nombre) vaut un candidat ; plus tout w2 lu dans une chaine "w2 = <valeur>" ;
 (3) les VALEURS DISTINCTES de w2 de TOUTES mes sorties 2D (cle "cellule" -> "w2" des JSON de lecteur) : la liste est imprimee en entier, avec le nombre de fichiers par valeur.
Ecartes (ils portent des candidats PAR CONSTRUCTION, 1D, ou sont la piece elle-meme) : les dossiers de cette etape (livraison_22i_*, certif_gel_sommet_partie1_machine2). Les dossiers de machine 1 qui citent des candidats en 1D (livraison_22g_*, livraison_22h_*) sont BALAYES et leurs touches rapportees.
Une recherche de texte n'est pas une preuve d'absence : elle ne voit pas un w2 note autrement (delta seul, fraction non reduite, forme a plus de cinq decimales, note dans une image).
Usage : py -3.11 -I balayage_virginite_sommet_machine2_v1.py <racine de mes archives> <autre racine facultative>"""
import json
import os
import re
import sys
import zipfile
from fractions import Fraction as F

RACINES = sys.argv[1:]
ECARTES = ('livraison_22i_Q2_notee_gel_sommet_partie1', 'certif_gel_sommet_partie1_machine2')
EXT = ('.json', '.log', '.py', '.md', '.txt', '.csv', '.sh', '.tsv', '.out')
cands = []
for s, ks in (('MP', [k for k in range(5, 21) if k != 10]), ('PP', [k for k in range(5, 21) if k != 10]), ('MG', range(25, 50)), ('PG', range(25, 50))):
    sg = -1 if s[0] == 'M' else 1
    for k in ks:
        cands.append((s, F(2) + sg * F(k, 100000)))
valeurs = {w for _, w in cands}
dec5 = {('%.5f' % float(w)): w for w in valeurs}
dec_court = {}
for d, w in dec5.items():
    c = d.rstrip('0')
    if c != d:
        dec_court[c] = w
frac = {str(w): w for w in valeurs}
toks_dec = sorted(set(dec5) | set(dec_court), key=len, reverse=True)
re_dec = re.compile(r'(?<![0-9.])(' + '|'.join(re.escape(d) for d in toks_dec) + r')(?![0-9])')
re_frac = re.compile(r'(?<![0-9/])(' + '|'.join(re.escape(f) for f in frac) + r')(?![0-9/])')
re_w2 = re.compile(r'w\s*_?2|omega|\bW2\b', re.I)
hits, lignes_w2 = {}, []
n_files = n_zip = n_zipmembers = erreurs = 0
json_cles = []          # (fichier, cle, valeur) : cle w2 dont la valeur est un candidat
w2_vus = {}             # valeur -> nombre de fichiers JSON de lecteur ou de sortie 2D
re_w2eq = re.compile(r'\bw2\s*=\s*([0-9]+(?:\.[0-9]+)?(?:/[0-9]+)?)', re.I)


def val(x):
    try:
        if isinstance(x, str):
            return F(x)
        if isinstance(x, (int, float)):
            return F(str(x)) if isinstance(x, float) else F(x)
    except Exception:
        return None
    return None


def parcours(nom, o, haut=True):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ('w2', 'w2n', 'w2_frac') and not isinstance(v, (dict, list)):
                w = val(v)
                if w is not None:
                    w2_vus[w] = w2_vus.get(w, 0) + (1 if (nom, k) not in parcours.deja else 0)
                    parcours.deja.add((nom, k))
                    if w in valeurs:
                        json_cles.append((nom, k, str(v)))
            parcours(nom, v, False)
    elif isinstance(o, list):
        for v in o:
            parcours(nom, v, False)


parcours.deja = set()


def scan(nom, data):
    try:
        t = data.decode('utf-8', 'replace')
    except Exception:
        return
    a, b = re_dec.findall(t), re_frac.findall(t)
    if a or b:
        hits[nom] = (len(a), len(b), sorted(set(a))[:6], sorted(set(b))[:6])
        for ligne in t.split('\n'):
            if (re_dec.search(ligne) or re_frac.search(ligne)) and re_w2.search(ligne):
                m = re_dec.search(ligne) or re_frac.search(ligne)
                lignes_w2.append((nom, m.group(1), ligne.strip()[:240]))
    if nom.lower().endswith('.json') or '.json' in nom.lower():
        try:
            parcours(nom, json.loads(t))
        except Exception:
            pass
    for m in re_w2eq.finditer(t):
        w = val(m.group(1))
        if w in valeurs:
            json_cles.append((nom, 'texte w2 =', m.group(1)))


for racine in RACINES:
    for dossier, sous, fichiers in os.walk(racine):
        rel = os.path.relpath(dossier, racine)
        top = rel.split(os.sep)[0]
        if top in ECARTES:
            sous[:] = []
            continue
        if '__pycache__' in dossier:
            continue
        for f in fichiers:
            p = os.path.join(dossier, f)
            e = os.path.splitext(f)[1].lower()
            nom = os.path.basename(racine.rstrip('/' + chr(92))) + os.sep + os.path.relpath(p, racine)
            try:
                if e in EXT:
                    if os.path.getsize(p) > 200 * 1024 * 1024:
                        continue
                    n_files += 1
                    scan(nom, open(p, 'rb').read())
                elif e == '.zip':
                    n_zip += 1
                    with zipfile.ZipFile(p) as z:
                        for i in z.infolist():
                            if i.is_dir() or os.path.splitext(i.filename)[1].lower() not in EXT or i.file_size > 200 * 1024 * 1024:
                                continue
                            n_zipmembers += 1
                            scan(nom + '::' + i.filename, z.read(i))
            except Exception:
                erreurs += 1
print('80 candidats ; jetons de texte recherches : %d decimaux (dont %d sans zero final) et %d fractions' % (len(toks_dec), len(dec_court), len(frac)))
print('racines : %d ; fichiers texte lus : %d ; zips ouverts : %d ; membres texte de zips lus : %d ; erreurs de lecture : %d' % (len(RACINES), n_files, n_zip, n_zipmembers, erreurs))
print('\n(1) TEXTE : fichiers avec au moins un jeton candidat : %d' % len(hits))
par = {}
for k, v in hits.items():
    par.setdefault(k.split(os.sep)[0] + os.sep + (k.split(os.sep)[1].split('::')[0] if os.sep in k else ''), []).append((k, v))
for top in sorted(par):
    print('--', top, ':', len(par[top]), 'fichier(s)')
    for k, v in sorted(par[top])[:5]:
        print('     %s  dec %d %s  frac %d %s' % (k[:140], v[0], v[2], v[1], v[3]))
print('\n    lignes ou un jeton candidat figure sur une ligne parlant de w2 / omega : %d ligne(s) dans %d fichier(s)' % (len(set((a, c) for a, b, c in lignes_w2)), len(set(x[0] for x in lignes_w2))))
vus = set()
n = 0
for nom, jeton, ligne in lignes_w2:
    if (nom, ligne) in vus:
        continue
    vus.add((nom, ligne))
    n += 1
    if n <= 40:
        print('  [%s] %s :: %s' % (jeton, nom[:120], ligne))
print('\n(2) JSON STRUCTURE / "w2 = valeur" : cles w2 ou ecritures "w2 = ..." dont la valeur est un candidat : %d' % len(json_cles))
for x in json_cles[:40]:
    print('   ', x)
print('\n(3) VALEURS DISTINCTES de w2 dans les JSON balayes (cles w2, w2n, w2_frac) : %d valeurs' % len(w2_vus))
for w in sorted(w2_vus):
    print('   %-16s = %.8f  (%d cle(s))%s' % (w, float(w), w2_vus[w], '   <-- CANDIDAT' if w in valeurs else ''))
print('\nVALEURS CANDIDATES VUES COMME w2 DANS UN JSON : %d' % len([w for w in w2_vus if w in valeurs]))
