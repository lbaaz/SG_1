# -*- coding: ascii -*-
"""Balayage machine 2 : les quatre canons de l'ETAPE 0 cites par le gel E-B v1 (section 2) sont-ils
sur ce poste ? Usage : python cherche_etape0_machine2_v1.py RACINE [RACINE ...]
Lit chaque fichier (et chaque membre de zip, 20 Mo au plus) sous les racines, en empreinte B et en
empreinte brute, et compare aux quatre canons. Lecture seule ; ne decompresse rien sur disque."""
import hashlib
import os
import sys
import unicodedata
import zipfile

CIBLES = {'20cbc762d58ce1ca': 'etape 0 : lecture pre-declaree',
          '2d246b2a5c60c244': 'etape 0 : note de lecture',
          '37169cd7d595c575': 'etape 0 : JSON v2',
          '94c3749c83d4b044': 'etape 0 : lot m1'}
LIMITE = 20000000
trouve, nf, nz, nm = {}, 0, 0, 0


def empreintes(raw):
    hs = {hashlib.sha256(raw).hexdigest()[:16]}
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8').replace('\r\n', '\n')).encode('utf-8')
        hs.add(hashlib.sha256(t).hexdigest()[:16])
    except UnicodeDecodeError:
        pass
    return hs


for racine in sys.argv[1:]:
    for d, _, fs in os.walk(racine):
        if '__pycache__' in d:
            continue
        for f in fs:
            p = os.path.join(d, f)
            try:
                if os.path.getsize(p) <= LIMITE:
                    raw = open(p, 'rb').read()
                    nf += 1
                    for h in empreintes(raw) & set(CIBLES):
                        trouve[h] = p
            except OSError:
                continue
            # un zip est ouvert QUELLE QUE SOIT SA TAILLE (seuls ses membres sont plafonnes)
            if f.lower().endswith('.zip'):
                try:
                    z = zipfile.ZipFile(p)
                except (zipfile.BadZipFile, OSError):
                    continue
                nz += 1
                for i in z.infolist():
                    if i.is_dir() or i.file_size > LIMITE:
                        continue
                    try:
                        r = z.read(i)
                    except Exception:
                        continue
                    nm += 1
                    for h in empreintes(r) & set(CIBLES):
                        trouve[h] = p + ' :: ' + i.filename

print('racines : %s' % ' ; '.join(sys.argv[1:]))
print('fichiers lus %d ; zips ouverts %d ; membres lus %d' % (nf, nz, nm))
for h, nom in CIBLES.items():
    print('%s  %-34s -> %s' % (h, nom, trouve.get(h, 'NON RETROUVE')))
print('retrouves : %d sur 4' % len(trouve))
