# -*- coding: ascii -*-
"""Contexte des touches du balayage de virginite (machine 2) : pour chaque fichier touche liste dans le journal, hors les familles deja comprises (gel du vide, registre, lot 17a, mes propres
dossiers de certification), imprime la premiere occurrence de chaque w2 avec 70 caracteres autour. Lecture seule.
Usage : py -3.11 -I contexte_touches_machine2_v1.py <journal du balayage> <filtre : sous-chaine de chemin a inclure, repetable>"""
import re
import sys
import zipfile

JOURNAL = sys.argv[1]; FILTRES = sys.argv[2:]
W = ['1.981', '1.983', '1.984', '1.985', '1.986', '1.987', '1.988', '1.989', '2.011', '2.012', '2.013', '2.014', '2.015', '2.016', '2.018', '2.019']
for l in open(JOURNAL, encoding='utf-8'):
    if not l.startswith('  '):
        continue
    ch = l.strip().split(' : ', 1)[0]
    if not any(f in ch for f in FILTRES):
        continue
    if '::' in ch:
        z, n = ch.split('::', 1)
        try:
            octets = zipfile.ZipFile(z).read(n)
        except Exception as e:
            print(ch, 'illisible', e); continue
    else:
        octets = open(ch, 'rb').read()
    t = octets.decode('latin-1')
    print('== ' + ch.replace('D' + ':/devs/bocal/', ''))          # retire le prefixe de disque des chemins du journal pour l'affichage
    vus = set()
    for w in W:
        m = re.search(r'(?<![0-9.])' + w.replace('.', r'\.') + r'(?![0-9])', t)
        if m and w not in vus:
            vus.add(w); a, b = max(0, m.start() - 70), min(len(t), m.end() + 70)
            print('   %s : ...%s...' % (w, re.sub(r'\s+', ' ', t[a:b])))
