# -*- coding: ascii -*-
"""Canon de la TABLE COMMUNE (section 5 du gel "pont") : la mienne, et le sous-ensemble 'format de la section 5' de la table de machine 1, serialise par json.dumps(indent=1, sort_keys=True).
Machine 2, 2026-11-17. Usage : py -3.11 -I canon_table_commune_machine2_v1.py <sa table.json> <ma table commune.json>"""
import hashlib
import json
import sys
import unicodedata


def canon(b):
    t = unicodedata.normalize('NFC', b.decode('utf-8')).replace('\r\n', '\n').encode()
    return hashlib.sha256(t).hexdigest()[:16]


sa = json.load(open(sys.argv[1])); mine_bytes = open(sys.argv[2], 'rb').read(); mon = json.loads(mine_bytes)
sub = {'creneaux': {s: {'candidats': [{'w2': c['w2'], 'eligible': c['eligible'], 'cellules': [{'m': x['m'], 'g': x['g'], 'eligible': x['eligible']} for x in c['cellules']]} for c in d['candidats']]} for s, d in sa['creneaux'].items()}}
sa_bytes = json.dumps(sub, indent=1, sort_keys=True).encode('ascii')
print('sous-ensemble de SA table (format section 5) == MA table commune, objet par objet : %s' % (sub == mon))
print('serialisation (indent=1, cles triees, LF) de son sous-ensemble == octets de mon fichier : %s' % (sa_bytes == mine_bytes))
print('canon B de ma table commune (octets du fichier) : %s ; canon B du sous-ensemble de la sienne : %s' % (canon(mine_bytes), canon(sa_bytes)))
print('octets : %d ; aucun CR : %s ; canon B = empreinte brute : %s' % (len(mine_bytes), b'\r' not in mine_bytes, canon(mine_bytes) == hashlib.sha256(mine_bytes).hexdigest()[:16]))
