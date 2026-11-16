#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LE DEPOT DU DELTA 100 SUR CLONE FRAIS -- copie, verification au bit, releve, commit LOCAL. machine 2, v1, 16/11/2026.
Le PUSH n'est pas fait ici.

Derive de depot_delta99_machine2_v1.py (NON EDITE : regle 17). Un seul changement : le texte du message de commit ; le numero se lit toujours
dans le nom du manifeste, l'etat attendu du registre s'en deduit, rien n'est tape. Le diff est joint.
Arguments : <clone frais> <MANIFEST_DEPOT_delta<nn>_machine2_v<N>.txt>.
  1. releve AVANT : origin/main == HEAD, arbre propre, plafond == nn - 1, aucun delta_nn ;
  2. chaque ligne du manifeste : la source resout au canon B ecrit ; la cible n'existe pas encore ; copie OCTET POUR OCTET ; relecture au canon ;
  3. git add ; le nombre de fichiers ajoutes == le compte declare, aucun modifie, aucun supprime, rien hors gels/ scripts/ journal/ ;
  4. commit local, auteur celui du depot, message SANS trailer d'outillage (convention du depot public, decidee le 25/08) ;
  5. releve APRES : HEAD a avance d'un commit, plafond == nn, l'acte numerote resout au canon de l'acte source.
Les comptes sont LUS ; les sorties s'ecrivent avant tout assert. DEUX VERBES.
"""
import hashlib, os, re, shutil, subprocess, sys, unicodedata

if len(sys.argv) != 3:
    sys.exit('usage : depot_delta100_machine2_v1.py <clone frais> <MANIFEST_DEPOT_delta<nn>_machine2_v<N>.txt>')
CLONE, MAN = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
# Le numero du delta se LIT dans le nom du manifeste de depot ; l'etat attendu du registre s'en
# deduit. Rien n'est tape.
import re as _re
_mn = _re.search(r'MANIFEST_DEPOT_delta(\d+)_', os.path.basename(MAN))
if not _mn:
    sys.exit('le manifeste ne nomme pas son delta : %s' % os.path.basename(MAN))
NUMERO = int(_mn.group(1))
OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-58s %s' % ('PASSE' if c else 'MORD ', n[:58], d))


def note(n, d=''):
    print('  [ note] %-58s %s' % (n[:58], d))


def git(*a):
    return subprocess.check_output(['git', '-C', CLONE] + list(a)).decode().strip()


def emp(p):
    raw = open(p, 'rb').read()
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16]
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h


print('\n1. RELEVE AVANT')
git('fetch', '-q', 'origin')
head, orig = git('rev-parse', '--short', 'HEAD'), git('rev-parse', '--short', 'origin/main')
suivis = [f for f in git('ls-files').split('\n') if f]
plafond = max(int(m) for f in suivis for m in re.findall(r'delta_?(\d+)', f))
note('delta LU dans le nom du manifeste, non tape', 'delta %d ; attendu : plafond %d, aucun '
     'delta_%d' % (NUMERO, NUMERO - 1, NUMERO))
chk('origin/main == HEAD (clone frais, rien de local)', head == orig, '%s / %s' % (head, orig))
chk('arbre propre', git('status', '--porcelain') == '', '%d fichiers suivis' % len(suivis))
chk('plafond %d, aucun delta_%d' % (NUMERO - 1, NUMERO),
    plafond == NUMERO - 1 and not [f for f in suivis if 'delta_%d' % NUMERO in f],
    'plafond %d' % plafond)
AVANT = head

print('\n2. COPIE ET VERIFICATION AU BIT, LIGNE PAR LIGNE')
lignes = []
for l in open(MAN, encoding='utf-8'):
    m = re.match(r'^((?:gels|scripts|journal)/\S+)\s+([0-9a-f]{16}) ([0-9a-f]{16})\s+(\d+)\s+(\d+)\s+(\S+)', l)
    if m:
        lignes.append(m.groups())
declare = int(re.search(r'^pieces : (\d+)', open(MAN, encoding='utf-8').read(), re.M).group(1))
chk('lignes lues == compte declare du manifeste', len(lignes) == declare, '%d / %d' % (len(lignes), declare))
# Le manifeste de depot et le journal du perimetre ne peuvent pas figurer dans leur propre table : ils entrent ici,
# nommes, sous journal/, et verifies au bit comme les autres.
for _f in (MAN, MAN.replace('MANIFEST_DEPOT_delta%d_machine2_v' % NUMERO, 'perimetre_depot_delta%d_sur_acte_v' % NUMERO)
           .replace('.txt', '_machine2.log')):
    _e = emp(_f)
    chk('piece ajoutee %s existe' % os.path.basename(_f), os.path.isfile(_f), os.path.basename(_f))
    lignes.append(('journal/' + os.path.basename(_f), _e[0], _e[1], 0, 0, os.path.relpath(_f, RAC).replace(chr(92), '/')))
copiees, fautes = 0, []
for cible, B, br, oB, obr, src in lignes:
    s = os.path.join(RAC, src)
    d = os.path.join(CLONE, cible)
    if not os.path.exists(s) or emp(s)[0] != B:
        fautes.append('source %s' % src)
        continue
    if os.path.exists(d):
        fautes.append('cible existe %s' % cible)
        continue
    os.makedirs(os.path.dirname(d), exist_ok=True)
    shutil.copyfile(s, d)
    if open(d, 'rb').read() != open(s, 'rb').read() or emp(d) != (B, br):
        fautes.append('copie %s' % cible)
        continue
    copiees += 1
chk('chaque piece copiee OCTET POUR OCTET et relue au canon', not fautes and copiees == len(lignes),
    ', '.join(fautes[:5]) or '%d copiees' % copiees)
# L'acte ne se reconnait plus a un motif de nom : celui herite du 91 codait 'delta_91' et
# 'run' en dur (meme racine que E-92-1, troisieme occurrence de la meme faute) et ne trouvait
# donc pas l'acte du 92. Le manifeste DECLARE lui-meme quelle piece est la piece de depot :
# c'est cette declaration qu'on lit, et rien d'autre.
_mpd = re.search(r'^Piece de depot : (\S+?),', open(MAN, encoding='utf-8').read(), re.M)
chk('le manifeste declare sa piece de depot', _mpd is not None,
    _mpd.group(1) if _mpd else 'ligne "Piece de depot :" absente')
acte = [c for c, B, *_ in lignes if _mpd and c == 'journal/' + _mpd.group(1)]
chk('l acte numerote est une des pieces copiees', len(acte) == 1, acte[0] if acte else 'aucun')

print('\n3. GIT ADD')
git('add', '--', 'gels', 'scripts', 'journal')
st = [l for l in git('status', '--porcelain').split('\n') if l]
ajoutes = [l[3:] for l in st if l.startswith('A ')]
autres = [l for l in st if not l.startswith('A ')]
chk('fichiers ajoutes == compte du manifeste, rien d autre', len(ajoutes) == len(lignes) and not autres,
    '%d ajoutes, %d autres' % (len(ajoutes), len(autres)))
chk('tous sous gels/ scripts/ journal/', all(a.startswith(('gels/', 'scripts/', 'journal/')) for a in ajoutes), '')
chk('l ensemble des chemins ajoutes == l ensemble des cibles', set(ajoutes) == set(c for c, *_ in lignes), '')

print('\n4. COMMIT LOCAL (pas de push ici)')
auteur = git('log', '-1', '--format=%an <%ae>')
msg = ("delta 100 -- the one-dimensional chain pushed to third order reads the plateau width of states on twelve cells drawn at random and never played, to within 0.05 in logarithm where e_bord is below 0.3 and within 0.10 beyond, and is closer to it than order 2 on the negative line: E1 HELD (ten line cells of ten, none fallen), E2 HELD (five of five), E1B HELD (the two border cells), E3 HELD (the order-2 bound of delta 98 at all twelve cells); under a freeze in two parts, the draw rule, certified by the other machine with zero bite, the seed (200482) being given by the operator after it so that neither machine chose the cells, both machines drawing the same twelve (N1 to N5 at delta -0.065, P1 to P5 at +0.035, BN at -0.076, BP at +0.067), then the instrument and the statements, certified by the other machine before the run with zero bite on the instrument and one on a description (0.164 written for 0.163, no rule depending on it); played once on BOCAL4 on 16/11 from 01:49:18 to 03:32:04 (6166 s, 19 calls, every exit code 0, on mains) with a pilot derived by machine 2 from machine 1's (-P for -I because numpy sits in the user site, one BLAS thread outside the dense probe), launched on the operator's written green light of 00:54, conditional on that certification, the operator attesting the message and its time; 144 states read, 141 judged, 129 in the domain, 12 outside it (BN 4, BP 8); the widest |ln q3| of a line cell is 0.0740 (N1) and its narrowest margin +0.0164 (P1); the border cell BP holds by +0.000383 (|ln q3| 0.099617 for 0.10, at rank 3), three of its five domain states lying within 0.0026 of the tolerance and the plateau spread that the reader publishes at rank 3 being 0.0024, 6.2 times that margin, so that the verdict of BP is the reading of the frozen rule and not a measurement at that precision; machine 1's replay of the sheets on its own machine agrees to 1.6e-9 on ln q3, and a second sheet written by machine 2 from sections 5 and 6 alone agrees on the 141 judged states; the pen's regularity at delta > 0 does not hold as a bound (ln q3 / delta^3 reaches 784 against 493 before the run) though everything stays under the tolerance, and the pen, which gave E1 holding everywhere a probability of 0.35, was pessimistic; the act states no law in delta, each line having a single w2, and does not extend the domain beyond its guards; it rests on the reader of delta 99, deposited just before; act written by machine 1 and countersigned by machine 2 in two versions, the first by 68 controls recomputed from machine 2's own sources with one bite of description (0.173 written for 0.1738) and a precision requested on BP, the second, deposited here byte for byte with the first beside it, by 73 controls of which none bites; no new candidate rule, thirty-four await review (X)")
open(os.path.join(ICI, 'message_commit_delta%d.txt' % NUMERO), 'w', encoding='utf-8', newline='\n').write(msg + '\n')
chk('le message ne porte aucun trailer d outillage (convention du depot public, 25/08)',
    'Co-Authored' not in msg and 'Claude' not in msg and 'Generated' not in msg, '%d caracteres' % len(msg))
git('-c', 'user.name=' + auteur.split(' <')[0], '-c', 'user.email=' + auteur.split('<')[1].rstrip('>'),
    'commit', '-q', '-m', msg)
h2 = git('rev-parse', '--short', 'HEAD')
chk('commit local cree au-dessus de %s' % AVANT, git('rev-parse', '--short', 'HEAD~1') == AVANT,
    '%s, auteur %s' % (h2, auteur))
chk('le commit ne porte aucun trailer', 'Co-Authored' not in git('log', '-1', '--format=%B'), '')

print('\n5. RELEVE APRES (local)')
suivis2 = [f for f in git('ls-files').split('\n') if f]
plafond2 = max(int(m) for f in suivis2 for m in re.findall(r'delta_?(\d+)', f))
chk('plafond %d ; %d fichiers suivis (+%d)' % (plafond2, len(suivis2), len(suivis2) - len(suivis)),
    plafond2 == NUMERO and len(suivis2) - len(suivis) == len(lignes), '%d attendus' % len(lignes))
ea = [B for c, B, *_ in lignes if c == acte[0]][0] if acte else None
chk('l acte numerote resout, dans l arbre, au canon de l acte source', acte and emp(os.path.join(CLONE, acte[0]))[0] == ea, ea)
chk('git diff HEAD~1 --stat : que des ajouts', all(l.strip().endswith(('+', '++', '+++')) or '|' not in l
    for l in git('diff', 'HEAD~1', '--stat=200').split('\n')[:-1]), '')

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN DEPOT (local) : %d/%d controles PASSENT ; HEAD local %s au-dessus de %s ; push NON fait'
      % (k, n, h2, AVANT))
print('=====================================================================')
sys.exit(0 if k == n else 1)
