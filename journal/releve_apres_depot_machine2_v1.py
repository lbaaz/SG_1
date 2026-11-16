# -*- coding: ascii -*-
"""MON RELEVE DU REGISTRE APRES LES DEPOTS 99 ET 100 -- machine 2, 2026-11-16. Independant du releve de machine 1 (son script n'est pas lu). Lit un CLONE NEUF du registre public (tete attendue 54da87a), ne l'ecrit pas.
1. Pour chacun des SEPT lots que machine 1 dit absents : le manifeste du lot est cherche PAR CANON sur le poste (tout BOCAL4), puis ses pieces de table sont cherchees par canon (B ou brut) au registre.
2. Pour les deux gels de la loi et le gel ter deposes : chaque empreinte de 16 hex qu'ils citent est cherchee au registre (fichier ou manifeste de lot).
3. La remarque sur le 98 : les empreintes citees par les gels des deltas 97 et 98 qui ne resolvent pas.
Usage (depuis BOCAL4) : py -3.11 -P certif_depot_99_100_machine2/releve_apres_depot_machine2_v1.py <clone neuf> <sortie.json>"""
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata

CL, SORTIE = os.path.abspath(sys.argv[1]), sys.argv[2]
RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16]
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h


def git(*a):
    return subprocess.check_output(['git', '-C', CL] + list(a)).decode().strip()


print('tete du clone :', git('rev-parse', '--short', 'HEAD'), '; fichiers suivis :', len(git('ls-files').split('\n')))
REG = {}
for f in git('ls-files').split('\n'):
    if not f:
        continue
    b, r = emp(open(os.path.join(CL, f), 'rb').read())
    REG.setdefault(b, []).append(f)
    if r != b:
        REG.setdefault(r, []).append(f)
print('canons distincts au registre :', len(REG))

# les manifestes du poste, par canon
MANS = {}
for d, dn, fs in os.walk(RAC):
    dn[:] = [x for x in dn if x not in ('.git', '__pycache__')]
    for f in fs:
        if f.upper().startswith('MANIFEST_') and f.lower().endswith('.txt') and 'DEPOT_delta' not in f:
            p = os.path.join(d, f)
            MANS.setdefault(emp(open(p, 'rb').read())[0], []).append(p)
SEPT = [('26b3912297b31713', 'machine 1', 'acte du gel ter (delta 99)', (30, 8, 22)), ('d9250297bf7d2f77', 'machine 1', 'acte du run, v1 (delta 100)', (23, 5, 18)),
        ('0a5741ff95e7136c', 'machine 1', 'acte du run, v2 (delta 100)', (10, 1, 9)), ('e93f1898dcd78a8f', 'machine 1', 'note sur la loi de la largeur', (21, 2, 19)),
        ('1e8413aed149429f', 'machine 1', 'note de la carte', (16, 1, 15)), ('889fe9b4c1c1c60a', 'machine 2', 'mon bloc d\'ordre 3 rederive', (11, 1, 10)),
        ('548fb2ba8793ecfe', 'machine 2', 'ma reponse a la carte', (8, 0, 8))]
TABLE = re.compile(r'^[0-9a-f]{16}\s')
res = {'lots': {}, 'gels': {}}
ecarts = []
print('\n1. LES SEPT LOTS')
for c, plume, objet, att in SEPT:
    ps = MANS.get(c)
    if not ps:
        print('  %s (%s) : manifeste INTROUVABLE au poste' % (c, objet))
        ecarts.append((c, 'manifeste introuvable au poste'))
        continue
    pieces = []
    for l in open(ps[0], encoding='utf-8', errors='replace'):
        if TABLE.match(l):
            ch = l.split()
            jet = [x for x in ch[:2] if re.fullmatch(r'[0-9a-f]{16}', x)]
            pieces.append((ch[-1] if len(ch) > 3 else ch[1], jet))
    presentes = [n for n, jet in pieces if any(j in REG for j in jet)]
    man_au_reg = c in REG
    mon = (len(pieces), len(presentes), len(pieces) - len(presentes))
    ok = mon == att
    print('  %s %-9s %-40s pieces %2d, au registre %2d, absentes %2d ; manifeste au registre : %-3s ; machine 1 dit %s : %s' % (c, plume, objet, mon[0], mon[1], mon[2], 'oui' if man_au_reg else 'non', att, 'MEMES' if ok else 'DIFFERENT'))
    res['lots'][c] = {'objet': objet, 'pieces': mon[0], 'presentes': mon[1], 'absentes': mon[2], 'manifeste_au_registre': man_au_reg, 'comme_machine1': ok}
    if not ok:
        ecarts.append((c, 'comptes differents de ceux de machine 1'))
print('\n2. LES GELS DEPOSES : empreintes citees non resolues au registre')
for nom, fichier in (('gel ter 432319b9feb34b82', 'gels/qualification_EB_ter_pre_enregistrement_v1.md'), ('gel loi partie 1 b56ca5cb2dd25da1', 'gels/gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md'),
                     ('gel loi partie 2 543d8b33e5c9afb8', 'gels/gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1.md')):
    t = open(os.path.join(CL, fichier), encoding='utf-8').read()
    cites = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', t)))
    nr = [x for x in cites if x not in REG]
    print('  %-36s %2d citees, %d non resolues : %s' % (nom, len(cites), len(nr), nr))
    res['gels'][nom] = {'citees': len(cites), 'non_resolues': nr}
print('\n3. LES GELS DES DELTAS 97 ET 98')
for nom in sorted(f for f in git('ls-files').split('\n') if f.startswith('gels/') and re.search(r'(domaine_G1|ordre2)', f)):
    t = open(os.path.join(CL, nom), encoding='utf-8').read()
    cites = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', t)))
    nr = [x for x in cites if x not in REG]
    print('  %-80s %2d citees, %d non resolues : %s' % (nom, len(cites), len(nr), nr))
    res['gels'][nom] = {'citees': len(cites), 'non_resolues': nr}
json.dump(res, open(SORTIE, 'w'), indent=1)
print('\nECARTS A CE QUE DIT MACHINE 1 (sur les sept lots) :', ecarts or 'aucun')
sys.exit(0 if not ecarts else 1)
