# -*- coding: ascii -*-
"""MON BALAYAGE E19 (certification (d)) : mes archives (arbre BOCAL4) contiennent-elles la trace d'un w2 CANDIDAT du gel du vide ?
Candidats : les 36 w2 au millieme de 1.981-1.989, 1.991-1.999, 2.001-2.009, 2.011-2.019. Deux ecritures : decimale (jeton isole, pas un morceau d'un
plus long nombre) et fraction irreductible. Texte seulement (.json .log .py .md .txt .csv .sh .tsv) et membres texte des .zip lisibles.
Ecartes (ils portent des candidats PAR CONSTRUCTION, 1D) : les dossiers de cette etape (livraison_16e, livraison_16f, rejeu_vide_machine2,
certif_gel_vide_partie1_machine2). Une recherche de texte n'est pas une preuve d'absence : elle ne voit pas un w2 note autrement (delta seul, fraction non reduite).
Usage : py -3.11 -I balayage_E19_vide_machine2_v1.py"""
import os
import re
import sys
import zipfile
from fractions import Fraction as F

RACINE = r'd:\devs\bocal\BOCAL4'
ECARTES = ('livraison_16e_vide_etape_sans_run', 'livraison_16f_gel_vide_partie1', 'rejeu_vide_machine2', 'certif_gel_vide_partie1_machine2')
EXT = ('.json', '.log', '.py', '.md', '.txt', '.csv', '.sh', '.tsv')
cands = [F(n, 1000) for n in list(range(1981, 1990)) + list(range(1991, 2000)) + list(range(2001, 2010)) + list(range(2011, 2020))]
dec = [('%.3f' % float(c)) for c in cands]
frac = [str(c) for c in cands]
re_dec = re.compile(r'(?<![0-9.])(' + '|'.join(re.escape(d) for d in dec) + r')(?![0-9])')
re_frac = re.compile(r'(?<![0-9/])(' + '|'.join(re.escape(f) for f in frac) + r')(?![0-9])')
hits = {}
n_files = n_zip = n_zipmembers = 0
erreurs = 0


re_w2 = re.compile(r'w\s*_?2|omega|\bW2\b', re.I)
lignes_w2 = []          # (fichier, jeton, ligne) : le jeton figure sur une ligne qui parle de w2


def scan(nom, data):
    try:
        t = data.decode('utf-8', 'replace')
    except Exception:
        return
    a = re_dec.findall(t)
    b = re_frac.findall(t)
    if a or b:
        hits[nom] = (len(a), len(b), sorted(set(a))[:6], sorted(set(b))[:6])
        for ligne in t.split('\n'):
            if (re_dec.search(ligne) or re_frac.search(ligne)) and re_w2.search(ligne):
                m = re_dec.search(ligne) or re_frac.search(ligne)
                lignes_w2.append((nom, m.group(1), ligne.strip()[:260]))


for dossier, sous, fichiers in os.walk(RACINE):
    rel = os.path.relpath(dossier, RACINE)
    top = rel.split(os.sep)[0]
    if top in ECARTES:
        sous[:] = []
        continue
    for f in fichiers:
        p = os.path.join(dossier, f)
        e = os.path.splitext(f)[1].lower()
        try:
            if e in EXT:
                if os.path.getsize(p) > 200 * 1024 * 1024:
                    continue
                n_files += 1
                scan(os.path.relpath(p, RACINE), open(p, 'rb').read())
            elif e == '.zip':
                n_zip += 1
                with zipfile.ZipFile(p) as z:
                    for i in z.infolist():
                        if i.is_dir() or os.path.splitext(i.filename)[1].lower() not in EXT or i.file_size > 200 * 1024 * 1024:
                            continue
                        n_zipmembers += 1
                        scan(os.path.relpath(p, RACINE) + '::' + i.filename, z.read(i))
        except Exception as ex:
            erreurs += 1
print('fichiers texte lus : %d ; zips ouverts : %d ; membres texte de zips lus : %d ; erreurs de lecture : %d' % (n_files, n_zip, n_zipmembers, erreurs))
print('fichiers avec au moins une ecriture d un w2 candidat :', len(hits))
par_dossier = {}
for k, v in hits.items():
    top = k.split(os.sep)[0].split('::')[0]
    par_dossier.setdefault(top, []).append((k, v))
for top in sorted(par_dossier):
    print('--', top, ':', len(par_dossier[top]), 'fichier(s)')
    for k, v in sorted(par_dossier[top])[:8]:
        print('     %s  dec %d %s  frac %d %s' % (k[:150], v[0], v[2], v[1], v[3]))
print()
print('LIGNES OU LE JETON FIGURE AVEC "w2"/"omega" : %d ligne(s) dans %d fichier(s)' % (len(lignes_w2), len(set(x[0] for x in lignes_w2))))
vus = set()
for nom, jeton, ligne in lignes_w2:
    cle = (nom, ligne)
    if cle in vus:
        continue
    vus.add(cle)
    print('  [%s] %s :: %s' % (jeton, nom[:130], ligne))
