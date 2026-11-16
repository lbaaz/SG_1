# -*- coding: ascii -*-
"""MON BALAYAGE E19, 2e volet : mes archives portent-elles une lecture 2D de l'etat (0, 0) ? Recherche, dans les .json de l'arbre BOCAL4 (et les
membres .json des zips), d'une etiquette d'etat n1 = 0 ET n2 = 0 (cles "n1"/"n2" voisines ; ou "site": [0, 0]) ; pour chaque fichier trouve, la
liste des signes/w2 voisins (cles "w2", "signe"), afin de distinguer le JUMEAU (signe +1) du systeme a fantome. Ecartes : dossiers de cette etape.
Usage : py -3.11 -I balayage_etat_00_machine2_v1.py"""
import json
import os
import re
import zipfile

R = r'd:\devs\bocal\BOCAL4'
ECARTES = ('livraison_16e_vide_etape_sans_run', 'livraison_16f_gel_vide_partie1', 'rejeu_vide_machine2', 'certif_gel_vide_partie1_machine2')
re_n = re.compile(r'"n1"\s*:\s*0(?:\.0)?\s*,\s*"n2"\s*:\s*0(?:\.0)?\s*[,}\n]')
re_n_inv = re.compile(r'"n2"\s*:\s*0(?:\.0)?\s*,\s*"n1"\s*:\s*0(?:\.0)?\s*[,}\n]')
re_site = re.compile(r'"(?:site|etiquette|etat)"\s*:\s*\[\s*0\s*,\s*0\s*\]')
trouves = []
n_json = 0


def examine(nom, data):
    global n_json
    n_json += 1
    t = data.decode('utf-8', 'replace')
    k = len(re_n.findall(t)) + len(re_n_inv.findall(t)) + len(re_site.findall(t))
    if k:
        w2 = sorted(set(re.findall(r'"w2"\s*:\s*"?([0-9/.]+)"?', t)))[:6]
        sg = sorted(set(re.findall(r'"signe"\s*:\s*(-?\d)', t)))
        trouves.append((nom, k, w2, sg))


for dossier, sous, fichiers in os.walk(R):
    top = os.path.relpath(dossier, R).split(os.sep)[0]
    if top in ECARTES:
        sous[:] = []
        continue
    for f in fichiers:
        p = os.path.join(dossier, f)
        e = os.path.splitext(f)[1].lower()
        try:
            if e == '.json':
                if os.path.getsize(p) < 300 * 1024 * 1024:
                    examine(os.path.relpath(p, R), open(p, 'rb').read())
            elif e == '.zip':
                with zipfile.ZipFile(p) as z:
                    for i in z.infolist():
                        if not i.is_dir() and i.filename.lower().endswith('.json') and i.file_size < 300 * 1024 * 1024:
                            examine(os.path.relpath(p, R) + '::' + i.filename, z.read(i))
        except Exception:
            pass
print('fichiers .json lus :', n_json, '; fichiers portant une etiquette (0, 0) :', len(trouves))
vus = set()
for nom, k, w2, sg in sorted(trouves):
    cle = nom.split('::')[-1]
    print('  %s : %d occurrence(s) ; w2 voisins %s ; signes %s' % (nom[:150], k, w2, sg))
