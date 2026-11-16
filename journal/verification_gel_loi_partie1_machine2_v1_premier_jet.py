# -*- coding: ascii -*-
"""VERIFICATION DU GEL 'LOI DE LA LARGEUR, ORDRE 3', PREMIERE PARTIE (b56ca5cb2dd25da1, machine 1) -- machine 2, 2026-11-15. Hors chaine, 1D seulement : AUCUN calcul 2D.
Chaque controle recalcule de MES sources un fait que le texte du gel affirme, et le cherche dans le texte (blancs libres) ; il mord si le texte et mes sources different. Un controle qui mord n'est pas
un verdict : c'est une morsure a consigner.
  C01 forme : le canon du texte, ASCII, pas de caractere hors ASCII.
  C02 sources : les canons de la section 1, recalcules depuis mes copies (moteur, bloc d'ordre 2, bloc d'ordre 3, gel du delta 98, note de la carte, mon lot de reponse).
  C03 creneaux : les quatre listes de candidats (fenetres, comptes, bornes) contre MON script de tirage ; centiemes exclus.
  C04 tirage : l'exemple de la section 3 ; la forme de la chaine hachee ; les huit lignes de l'autotest de machine 1 contre mon tirage.
  C05 definitions : les definitions 4.1 a 4.6 contiennent les seuils que MON evaluateur applique (0.7, 0.05, 1.33e-12, 74, 8, 5, 2 et 2, facteurs 1/8 et 1/32, recul de 4 sites).
  C06 rangs : section 6 (cinq rangs, de 0 a 4, creneau entier, ordre N P BN BP, pas de retrait).
  C07 table de la section 7 contre le JSON de machine 1 (cellule par cellule : boite, jugeables, domaine, hors) et contre MA table.
  C08 comptes : les phrases de comptage du gel et de sa note (N 9/9, P 18/18, BN 7/8, BP 9/9 ; 152 cellules ; 44 w2).
  C09 pieces : les canons de la section 11, recalcules depuis le lot de machine 1 (le script de construction, qui porte le gel, n'est pas compare a lui-meme).
Usage : py -3.11 -I verification_gel_loi_partie1_machine2_v1.py <gel.md> <dossier du lot de machine 1> <ma table.json> <table commune.json> <tirage_gel_loi_machine2_v1.py> <dossier scripts du registre>
        <dossier lot ordre 3 de machine 1 (livraison 15e)> <manifeste de mon lot carte_reponse> <note de la carte de machine 1> <sortie.json>
Variable d'environnement SUFFIXE_SORTIE : pour la contre-epreuve."""
import hashlib
import importlib.util
import json
import os
import re
import sys
import unicodedata
from fractions import Fraction as F

GEL, LOT1, MATABLE, COMMUNE, TIRAGE, REGS, LOT15E, MANI_REP, NOTE_CARTE, SORTIE = sys.argv[1:11]


def canon(raw):
    t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
    return hashlib.sha256(t).hexdigest()[:16]


def rd(p):
    return open(p, 'rb').read()


txt = rd(GEL).decode('utf-8')
nt = re.sub(r'\s+', ' ', txt)
spec = importlib.util.spec_from_file_location('tirage', TIRAGE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
SUITE = {}


def chk(cid, ok, msg):
    SUITE[cid] = {'tient': bool(ok), 'detail': msg}
    print('%s %s   %s' % (cid, 'TIENT' if ok else 'MORD ', msg))


def contient(*xs):
    return [x for x in xs if re.sub(r'\s+', ' ', x) not in nt]


# C01
chk('C01', canon(txt.encode('utf-8')) == 'b56ca5cb2dd25da1' and all(ord(c) < 128 for c in txt), 'canon du texte %s (annonce b56ca5cb2dd25da1) ; ASCII : %s' % (canon(txt.encode('utf-8')), all(ord(c) < 128 for c in txt)))
# C02
src = {'82a0be882568fe0c': os.path.join(REGS, 'm17_chaine_v17.py'), '7cd5977bc27bebc1': os.path.join(REGS, 'chaine_ordre2_bloc_machine1_v1.py'),
       '534ba246aa3b8973': os.path.join(LOT15E, 'ordre3_bloc_machine1_v1.py'), '41153158190cf7f1': os.path.join(REGS, '..', 'gels', 'gel_ordre2_chaine_EA_pre_enregistrement_v1.md'),
       '1f6cfb5f9472b1b4': NOTE_CARTE}
mq = [c for c, p in src.items() if canon(rd(p)) != c]
mq += [c for c in src if c not in txt]
rep = canon(rd(MANI_REP))
chk('C02', not mq and rep == '548fb2ba8793ecfe' and '548fb2ba8793ecfe' in txt, 'canons de la section 1 recalcules depuis mes copies : %s ; mon lot de reponse %s' % ('tous tiennent' if not mq else 'MORDENT %s' % mq, rep))
# C03
att = {'N': (9, '1.931', '1.939'), 'P': (18, '2.031', '2.049'), 'BN': (8, '1.916', '1.924'), 'BP': (9, '2.061', '2.069')}
mq = []
for s, (n, a, b) in att.items():
    L = T.liste(s)
    lo, hi, fac = T.CRENEAUX[s]
    ok = len(L) == n and '%.3f' % float(L[0]) == a and '%.3f' % float(L[-1]) == b and all((w * 100).denominator != 1 for w in L)
    fen = ']%+.3f, %+.3f[' % (float(lo), float(hi))
    if not ok or ('delta dans %s' % fen) not in nt:
        mq.append(s)
    if re.search(r'\b%s\s+delta dans \]%s.*?\s%d valeurs' % (s, re.escape('%+.3f' % float(lo)), n), txt) is None:
        mq.append(s + ' (compte)')
mq += contient('w2 = 1.931 a 1.939', 'w2 = 2.031 a 2.039 et 2.041 a 2.049', 'w2 = 1.916 a 1.919 et 1.921 a 1.924', 'w2 = 2.061 a 2.069', '3/4, 5/6, 1, 6/5, 4/3')
chk('C03', not mq, 'quatre creneaux : listes de 9, 18, 8 et 9 valeurs, fenetres et bornes contre mon script de tirage%s' % ('' if not mq else ' ; MORD : %s' % mq))
# C04
m = re.search(r'sha256\("DEMONSTRATION\|N\|0"\) = ([0-9a-f]{16})\.\.\. ; modulo\s+(\d+) =\s+(\d+) -> w2 = (\d\.\d{3})', txt)
hh = hashlib.sha256(b'DEMONSTRATION|N|0').hexdigest()
ok = m is not None and m.group(1) == hh[:16] and int(m.group(2)) == len(T.liste('N')) and int(m.group(3)) == int(hh, 16) % 9 and m.group(4) == '%.3f' % float(T.tire('DEMONSTRATION', 'N', 0))
l1 = open(os.path.join(LOT1, 'tirage_machine1_v1_autotest.log'), encoding='utf-8').read()
n8 = 0
for mm in re.finditer(r'sha256\("DEMONSTRATION\|(\w+)\|(\d)"\) = ([0-9a-f]{16})\.\.\. ; modulo\s+(\d+) =\s+(\d+) -> w2 = (\d\.\d{3})', l1):
    s, r = mm.group(1), int(mm.group(2))
    h = hashlib.sha256(('DEMONSTRATION|%s|%d' % (s, r)).encode('ascii')).hexdigest()
    n8 += (mm.group(3) == h[:16] and int(mm.group(5)) == int(h, 16) % len(T.liste(s)) and mm.group(6) == '%.3f' % float(T.tire('DEMONSTRATION', s, r)))
chk('C04', ok and n8 == 8 and '"<graine>|<s>|<r>"' in txt and 'caractere 124' in nt, 'exemple de la section 3 et huit lignes de l autotest de machine 1 contre mon tirage : %d sur 8 ; forme de la chaine hachee presente' % n8)
# C05
mq = contient('e_bord < 0.7', 'stabilite est definie et <= 0.05', 'G > 1.33e-12', 'N <= 74, au moins 8 etiquettes jugeables sur les 14, dont au moins 5 dans le domaine',
              'N <= 74, au moins 8 etiquettes jugeables, dont au moins 2 dans le domaine ET au moins 2 hors du domaine', 'au facteur 1/8, au facteur 1/32, et au facteur 1/16 avec l\'absorbeur recule de 4 sites',
              'max / min <= 2', 'M_facteur 4', 'avec Sigma2', 'ordre 2 au facteur 1/16', 'a poids egal, le plus petit a, puis le plus petit b', 'plafond(n1g) + 2 (m + max(8, m)) + 2', 'boite N = r_c + 20',
              's = 0.70 s_ff(w2, g)')
chk('C05', not mq, 'definitions 4.1 a 4.6 : seuils et formules que mon evaluateur applique%s' % ('' if not mq else ' ; ABSENTS : %s' % mq))
# C06
mq = contient('Au plus cinq rangs, de 0 a 4', 'pour le CRENEAU ENTIER (jamais cellule par cellule)', 'dans l\'ordre N, P, BN, BP', 'il n\'est pas retire de la liste', 'PAS DE GEL')
chk('C06', not mq, 'regle des rangs : cinq rangs de 0 a 4, creneau entier, ordre N P BN BP, pas de retrait%s' % ('' if not mq else ' ; ABSENTS : %s' % mq))
# C07
his = json.load(open(os.path.join(LOT1, 'eligibilite_candidates_v1.json')))
mine = json.load(open(MATABLE))
hcel = {(c['creneau'], F(c['w2']), F(c['facteur'])): c for c in his['cellules']}
mcel = {(c['creneau'], F(c['w2']), F(c['facteur'])): c for c in mine['cellules']}
tab = {}
cur = None
for l in txt.split('\n'):
    mm = re.match(r'\s+creneau (\w+) : \d+ w2 eligibles sur \d+', l)
    if mm:
        cur = mm.group(1)
        continue
    mm = re.match(r'\s+(\d\.\d{3})\s+(x.*?)\s+(ELIGIBLE|INELIGIBLE)\s*$', l)
    if mm and cur:
        w = F(mm.group(1))
        cells = re.findall(r'x(\d/\d|\d)\s+(\d+)\s+(\d+/\d+(?:/\d+)?)(?: !)?', mm.group(2))
        for f, N, cnt in cells:
            tab[(cur, w, F(f))] = (int(N), [int(x) for x in cnt.split('/')], mm.group(3))
n_texte, mq_json, mq_mine = len(tab), [], []
for k, (N, cnt, st) in tab.items():
    h, mm_ = hcel[k], mcel[k]
    hh_ = [h['n_jug'], h['n_dom']] + ([h['n_hors']] if k[0] in ('BN', 'BP') else [])
    if N != h['N'] or cnt != hh_:
        mq_json.append(k)
    mm_c = [mm_['n_jug'], mm_['n_dom']] + ([mm_['n_hors']] if k[0] in ('BN', 'BP') else [])
    if N != mm_['N'] or cnt != mm_c:
        mq_mine.append(k)
chk('C07', n_texte == 152 and not mq_json and not mq_mine, 'table de la section 7 : %d cellules lues dans le texte ; differentes du JSON de machine 1 : %d ; differentes de MA table : %d' % (n_texte, len(mq_json), len(mq_mine)))
# C08
elig = {s: sum(1 for c in his['creneaux'][s]['candidats'] if c['eligible']) for s in his['creneaux']}
mq = contient('creneau N : 9 w2 eligibles sur 9', 'creneau P : 18 w2 eligibles sur 18', 'creneau BN : 7 w2 eligibles sur 8', 'creneau BP : 9 w2 eligibles sur 9', '152 cellules candidates (44 w2 au millieme)')
chk('C08', not mq and elig == {'N': 9, 'P': 18, 'BN': 7, 'BP': 9} and sum(len(his['creneaux'][s]['candidats']) for s in his['creneaux']) == 44 and len(his['cellules']) == 152,
    'comptes : 152 cellules, 44 w2, eligibles %s (JSON de machine 1)%s' % (elig, '' if not mq else ' ; ABSENTS : %s' % mq))
# C09
liste = re.findall(r'^\s{4}([0-9a-f]{16})\s+(\S+)\s*$', txt.split('11. PIECES DE CE LOT')[1], re.M) if '11. PIECES DE CE LOT' in txt else []
mq = []
for c, nom in liste:
    p = os.path.join(LOT1, nom)
    if not os.path.isfile(p) or canon(rd(p)) != c:
        mq.append(nom)
chk('C09', len(liste) == 11 and not mq, 'section 11 : %d canons de pieces ; recalcules depuis le lot de machine 1, differents : %s (le script de construction, qui porte ce texte, n est pas compare a lui-meme)' % (len(liste), mq))
bilan = [k for k, v in SUITE.items() if not v['tient']]
print('BILAN : %d controles, %d mordent %s' % (len(SUITE), len(bilan), bilan))
suf = os.environ.get('SUFFIXE_SORTIE', '')
json.dump({'canon': canon(txt.encode('utf-8')), 'controles': SUITE, 'bilan': {'mord': len(bilan), 'ids': bilan}}, open(SORTIE + suf, 'w'), indent=1, sort_keys=True)
