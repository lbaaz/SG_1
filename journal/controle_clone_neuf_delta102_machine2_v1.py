# -*- coding: ascii -*-
"""CONTROLE SUR CLONE NEUF du depot du delta 102 (apres le push) : le clone est fait de zero depuis le registre public, jamais depuis le clone qui a pousse.
Lit journal/MANIFEST_DEPOT_delta102_machine2_v2.txt AU REGISTRE ; chaque ligne de sa table : le fichier du registre est au canon B et a l'empreinte brute ecrits ;
l'acte numerote est identique, octet pour octet, a la piece recue de machine 1 ; les deux pieces ajoutees (le manifeste et le journal du perimetre) sont identiques
aux fichiers du poste ; le plafond est 99 ; la tete est celle attendue ; l'auteur est celui du depot ; aucun trailer.
Usage (depuis BOCAL4) : python -P DEPOT_delta102/controle_clone_neuf_delta102_machine2_v1.py <clone neuf> <tete attendue> <acte recu>"""
import hashlib
import os
import re
import subprocess
import sys
import unicodedata

CL, TETE, RECU = os.path.abspath(sys.argv[1]), sys.argv[2], os.path.abspath(sys.argv[3])
ICI = os.path.dirname(os.path.abspath(__file__))


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16]
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h


def git(*a):
    return subprocess.check_output(['git', '-C', CL] + list(a)).decode().strip()


OK = []


def chk(n, c, d=''):
    OK.append(bool(c))
    print('  [%s] %-70s %s' % ('PASSE' if c else 'MORD ', n[:70], d))


suivis = [f for f in git('ls-files').split('\n') if f]
plafond = max(int(m) for f in suivis for m in re.findall(r'delta_?(\d+)', f))
chk('tete du clone neuf == la tete attendue', git('rev-parse', '--short', 'HEAD') == TETE, git('rev-parse', '--short', 'HEAD'))
man = open(os.path.join(CL, 'journal', 'MANIFEST_DEPOT_delta102_machine2_v2.txt'), encoding='ascii').read()
N = int(re.search(r'^pieces : (\d+)', man, re.M).group(1))
chk('plafond 102, 2465 + N + 2 fichiers suivis (N lu dans le manifeste)', plafond == 102 and len(suivis) == 2465 + N + 2, '%d fichiers, plafond %d, N %d' % (len(suivis), plafond, N))
lignes = [l.split() for l in man.split('\n') if re.match(r'^(gels|scripts|journal)/\S+\s+[0-9a-f]{16} [0-9a-f]{16} ', l)]
ok = sum(1 for p in lignes if emp(open(os.path.join(CL, p[0]), 'rb').read()) == (p[1], p[2]))
chk('chaque piece de la table du manifeste, au registre, est au canon B et brut ecrits', ok == len(lignes) == N, '%d sur %d (N %d)' % (ok, len(lignes), N))
acte = os.path.join(CL, 'journal', 'journal_delta_102_largeur_vide_v2.md')
chk('l acte numerote est identique, octet pour octet, a la piece recue de machine 1', open(acte, 'rb').read() == open(RECU, 'rb').read() and emp(open(acte, 'rb').read())[0] == '16ba5e594ab18717',
    'canon %s' % emp(open(acte, 'rb').read())[0])
v1 = os.path.join(CL, 'journal', 'journal_delta_102_largeur_vide_v1.md')
chk('la v1 de l acte est a cote, au canon 464ba00a6905e3a5', os.path.isfile(v1) and emp(open(v1, 'rb').read())[0] == '464ba00a6905e3a5', '')
_excl = ['af1b49cfdf3bde0c', '6412b757b22b3736', '6399794d3aa15110', '5a73b5a492d5d4a2', 'fcfa1e8671b724d1', '3c2704eb97619d75']
_reg = set()
for _f in suivis:
    _reg.update(emp(open(os.path.join(CL, _f), 'rb').read()))
chk('les six pieces exclues (vie privee) ne sont PAS au registre', not [c for c in _excl if c in _reg], '%d exclues, aucune au registre' % len(_excl))
for nom, src in (('MANIFEST_DEPOT_delta102_machine2_v2.txt', os.path.join(ICI, 'MANIFEST_DEPOT_delta102_machine2_v2.txt')),
                 ('perimetre_depot_delta102_sur_acte_v2_machine2.log', os.path.join(ICI, 'perimetre_depot_delta102_sur_acte_v2_machine2.log'))):
    chk('piece ajoutee %s identique au poste' % nom, open(os.path.join(CL, 'journal', nom), 'rb').read() == open(src, 'rb').read(), '')
msg = git('log', '-1', '--format=%B')
chk('auteur et message : Baaz, aucun trailer d outillage', git('log', '-1', '--format=%an <%ae>') == 'Baaz <13465543+lbaaz@users.noreply.github.com>' and 'Co-Authored' not in msg
    and 'Claude' not in msg and 'Generated' not in msg, git('log', '-1', '--format=%an <%ae>'))
chk('le commit n ajoute que des fichiers sous gels/ scripts/ journal/ (N + 2), rien de modifie ni de supprime',
    all(l.startswith('A\t') and l.split('\t')[1].startswith(('gels/', 'scripts/', 'journal/')) for l in git('diff', '--name-status', 'HEAD~1', 'HEAD').split('\n')) and
    len(git('diff', '--name-status', 'HEAD~1', 'HEAD').split('\n')) == N + 2, '')
print('TOTAL : %d/%d controles PASSENT' % (sum(OK), len(OK)))
sys.exit(0 if all(OK) else 1)
