#!/usr/bin/env python3
# -*- coding: ascii -*-
"""RELEVE DE CLOTURE DU DELTA 90 -- machine 1, v1, 12/09/2026 (nuit).

Sur un clone frais du registre (chemin en argument) qui n'a jamais servi a pousser, chaque
ligne du manifeste de depot v2 (chemin en argument ; canon attendu 672b06b2686d3a82) est
relue par canon (convention B) ET au brut ; l'acte depose est relu contre le canon certifie
(11f86226cf4aa612). Compte declare avant de compter : 212 lignes, HEAD attendu e68341f.
Rien n'est edite (PB-1).
"""
import hashlib, os, re, subprocess, sys, unicodedata

if len(sys.argv) != 3:
    sys.exit('usage : releve_depot_delta90_machine1_v1.py <clone frais> <MANIFEST_DEPOT_delta90_machine2_v2.txt>')
CLONE, MAN = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-58s %s' % ('PASSE' if c else 'MORD ', n[:58], d))


def emp(p):
    raw = open(p, 'rb').read()
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n').encode()
    except UnicodeDecodeError:
        t = raw
    return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16]


head = subprocess.check_output(['git', '-C', CLONE, 'rev-parse', '--short', 'HEAD']).decode().strip()
suivis = [f for f in subprocess.check_output(['git', '-C', CLONE, 'ls-files']).decode().split('\n') if f]
chk('HEAD du clone frais == e68341f', head == 'e68341f', head)
chk('le manifeste de depot v2 resout a 672b06b2686d3a82', emp(MAN)[0] == '672b06b2686d3a82', emp(MAN)[0])
lignes = []
for l in open(MAN, encoding='utf-8', errors='replace'):
    t = l.rstrip('\r\n').split()
    if len(t) >= 5 and re.fullmatch('[0-9a-f]{16}', t[1]) and re.fullmatch('[0-9a-f]{16}', t[2]):
        lignes.append((t[0], t[1], t[2]))
chk('212 lignes de depot, compte declare avant de compter', len(lignes) == 212, '%d' % len(lignes))
ok = absents = ecarts = 0
for ch, B, br in lignes:
    p = os.path.join(CLONE, ch)
    if not os.path.exists(p):
        absents += 1
        print('      ABSENTE  %s' % ch)
        continue
    b, r = emp(p)
    if b == B and r == br:
        ok += 1
    else:
        ecarts += 1
        print('      ECART    %s attendu %s/%s trouve %s/%s' % (ch, B, br, b, r))
chk('retrouvees + absentes + ecarts == 212', ok + absents + ecarts == 212, '%d + %d + %d' % (ok, absents, ecarts))
chk('212/212 retrouvees AU BIT (canon B et brut)', ok == 212 and absents == 0 and ecarts == 0, '%d' % ok)
chk('toutes les lignes de depot sont des fichiers SUIVIS par git', all(ch in set(suivis) for ch, _, _ in lignes), '%d suivis' % len(suivis))
acte = os.path.join(CLONE, 'journal', 'journal_delta_90_constante_A_v2.md')
chk('l acte depose est AU BIT l acte v2 certifie (11f86226cf4aa612)', os.path.exists(acte) and emp(acte)[0] == '11f86226cf4aa612', emp(acte)[0] if os.path.exists(acte) else 'ABSENT')
deltas = sorted(int(m.group(1)) for f in suivis for m in [re.search(r'journal_delta_(\d+)_', f)] if m)
chk('plafond du registre == 90, un seul fichier delta_90', deltas[-1] == 90 and sum(1 for f in suivis if 'delta_90' in f) == 1, 'plafond %d' % deltas[-1])
chk('676 fichiers suivis (464 + 212)', len(suivis) == 676, '%d' % len(suivis))
n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN RELEVE : %d/%d controles PASSENT' % (k, n))
print('=====================================================================')
