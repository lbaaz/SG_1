#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LE DEPOT DU DELTA 98 SUR CLONE FRAIS -- copie, verification au bit, releve, commit LOCAL. machine 2, v1, 15/11/2026.
Le PUSH n'est pas fait ici.

Derive de depot_delta97_machine2_v1.py (NON EDITE : regle 17). Un seul changement : le texte du message de commit ; le numero se lit toujours
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
    sys.exit('usage : depot_delta98_machine2_v1.py <clone frais> <MANIFEST_DEPOT_delta<nn>_machine2_v<N>.txt>')
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
msg = ('delta 98 -- the E-A chain completed by its second order HOLDS against the width E-B reads at k = 3: under a freeze written before the run and certified by the other machine before it, opened by the operator\'s "ok go" on 14/11 at 22:04 as machine 1 declares it (machine 2 cannot check it), played once on BOCAL4 on 14 and 15/11 with every guard held and the two anchors reproducing M17\'s readings to the bit, on twelve judged points never played, at factors 2/3 to 3/2 and in three bands of |delta| (to 0.06, to 0.10, to 0.12), the chain with the level shift of each site and the hop to the second neighbour reads that width within a factor 1.25, 1.6 and 2 in the three bands, on 132 judged states, the largest ratio being 1.679 against a bound of 2 at L4: THE ORDER 2 HOLDS; it does better than the engine\'s own chain at the worst state at all twelve points, and it reads the energy shift of the states to one per cent, the largest gap being 0.0046; the residual is on one side only (the smallest ratio is 1.002) and grows with the disagreement, and the act does not say where it comes from; the verdict is unchanged under the thread noise up to seven times the noise measured at the anchors and may change from eight times, that noise not having been measured at the boxes of 73 and 74; the witness W2, played and not readable (3 judged states out of 14), and W1 (largest ratio 2.047), outside the statement, carry no weight; eighteen of the twenty announcements of the pen that can be judged are true; the act says nothing outside factors 2/3 to 3/2, the fraction 0.70, the 2:1 channel of x^5 and |delta| from 0.03 to 0.12, does not call the chain qualified and states no intrinsic width; the run was played on battery, which lengthened it to 4524 s and changed no number; no new candidate rule, thirty-four await review (X); act written by one machine and countersigned by the other after every number was recalculated from the countersigner\'s own sources, 16 controls of which one bites (a quotation from machine 1\'s own note that lost one word, with no consequence), the same sheet biting 14 times on a copy with nineteen figures or words changed, the deposited file being the countersigned one byte for byte')
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
