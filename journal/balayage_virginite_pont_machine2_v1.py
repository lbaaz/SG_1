# -*- coding: ascii -*-
"""BALAYAGE DE VIRGINITE du gel "pont" (machine 2, 2026-11-17), section 10 (d) : cherche, dans mes archives (dossier BOCAL4 entier, zips lus de l'interieur) et dans un clone du registre,
les seize w2 candidats du gel (section 2) : leur ecriture decimale au millieme ("1.981") et leur fraction irreductible ("1981/1000"), avec des bornes qui ecartent les nombres plus longs.
Une recherche de texte n'est pas une preuve d'absence (le gel le dit) : le balayage liste les fichiers touches, il ne juge pas ; le tri des touches est fait a la main, a part.
Usage : py -3.11 -I balayage_virginite_pont_machine2_v1.py <racine a balayer> [<racine> ...] --exclure <fragment de chemin> [...]"""
import os
import re
import sys
import zipfile
from fractions import Fraction as F

args = sys.argv[1:]
if '--exclure' in args:
    i = args.index('--exclure'); RACINES, EXCL = args[:i], args[i + 1:]
else:
    RACINES, EXCL = args, []
W2 = [F(k, 1000) for k in (1981, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 2011, 2012, 2013, 2014, 2015, 2016, 2018, 2019)]
PAT = {}
for w in W2:
    dec = ('%.3f' % float(w)).replace('.', r'\.')
    PAT[w] = [re.compile(('(?<![0-9.])' + dec + '(?![0-9])').encode('ascii')), re.compile(('(?<![0-9/])%d/%d(?![0-9])' % (w.numerator, w.denominator)).encode('ascii'))]
touches = {}      # chemin -> {w2: [nb decimal, nb fraction]}
nfich = 0; noctets = 0


def chercher(nom, octets):
    global nfich, noctets
    nfich += 1; noctets += len(octets)
    for w, (pd, pf) in PAT.items():
        a, b = len(pd.findall(octets)), len(pf.findall(octets))
        if a or b:
            touches.setdefault(nom, {})[w] = [a, b]


for racine in RACINES:
    for r, ds, fs in os.walk(racine):
        for f in fs:
            p = os.path.join(r, f)
            if any(x in p.replace('\\', '/') for x in EXCL):
                continue
            try:
                if os.path.getsize(p) > 600 * 1024 * 1024:
                    print('trop gros, ignore :', p); continue
                if zipfile.is_zipfile(p):
                    with zipfile.ZipFile(p) as z:
                        for n in z.namelist():
                            if not n.endswith('/'):
                                chercher(p + '::' + n, z.read(n))
                else:
                    chercher(p, open(p, 'rb').read())
            except Exception as e:
                print('illisible :', p, type(e).__name__)
print('fichiers lus (zips deplies) : %d ; octets : %d' % (nfich, noctets))
print('fichiers touches : %d' % len(touches))
for p in sorted(touches):
    print('  %s : %s' % (p.replace('\\', '/'), '  '.join('%.3f[%d,%d]' % (float(w), c[0], c[1]) for w, c in sorted(touches[p].items()))))
