#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LE DEPOT DU DELTA 105 SUR CLONE FRAIS -- copie, verification au bit, releve, commit LOCAL. machine 2, v1, 23/11/2026.
Le PUSH n'est pas fait ici.

Derive de depot_delta104_machine2_v1.py (NON EDITE : regle 17). Un seul changement : le texte du message de commit ; le numero se lit toujours
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
    sys.exit('usage : depot_delta105_machine2_v1.py <clone frais> <MANIFEST_DEPOT_delta<nn>_machine2_v<N>.txt>')
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
msg = ("delta 105 -- the width of the vacuum at the SUMMIT of the profile, from kappa = 0.0363 (two rungs of barrier) to kappa = 1 (no barrier), where the jump at the foot of the ladder is no longer small against the detuning: the one-dimensional chain at third order, under the chain absorber adapted to the jump, renders the plateau width of the state carried by site (0, 0) of the phantom system, as read in two dimensions by the deposited hollow reader, to 0.01 in logarithm band included on fifty-six cells drawn at random and never played, S1 HELD, fifty-six of fifty-six held, none fallen, none unjudgeable, none unread, seven of seven at every one of the eight values of w2 and eight of eight at every one of the seven kappa, the range being all seven kappa; under a freeze in two parts, the draw and eligibility rule (eighty candidate values of w2 at the hundred-thousandth, seven kappa, five hundred and sixty cells, two values of w2 per slot, eight draws), then the instrument and the statement, each certified by the other machine before the run (the first with no disagreement on any written number of the five hundred and sixty cells, the second at its six points, with five non-blocking remarks), the seed (114565) being given by the operator after the certification of the first part so that neither machine chose the cells, both machines drawing the same fifty-six (w2 = 1.99989, 1.99993, 2.00008, 2.00011, 1.99968, 1.99956, 2.00039, 2.00048); nine sacrificed points (two qualifications Q and Q2, declared before any reading) serve as positive witnesses and are re-read before any cell by a guard that refuses the run if they do not hold; played once on BOCAL4 on 23/11 from 00:16:01 to 01:05:05 (2944 s, 136 calls, every exit code 0, on mains) after a pre-flight that read no cell, on the operator's written word RUn; the widest |ln q| is 0.00025 against a tolerance of 0.01 and the narrowest margin 0.00436, below the extent of the chain's own eighteen absorber variants at all fifty-six cells: the freeze is held to its tolerance and does not measure the chain's error below what its absorber leaves undetermined, and it does not separate the third order from the first; the residual by kappa (the sign of ln q is the same at the eight values of w2 at five kappa of seven, up to 2.5e-04) is that of the median of the chain's eighteen absorber variants and not of the reader, by a one-dimensional calculation of machine 2 made after the run and not written in the act; the act writes LESS than the freeze allowed: it does not say that the scale law of the width of the vacuum is tested from the wings to the summit, the two freezes testing the chain and their domains (|delta| from 0.003 to 0.018 there, 0.00007 to 0.00048 here) not touching; one of the pen's nine announcements falls (ten of sixteen barrier cells, twelve announced); machine 1's replay of its sheet on machine 2's 130 reading files gives the same verdict and the same fifty-six judgements to 3.7e-15, and an independent judge written by machine 2 from the text before the run agrees cell by cell; the act is machine 1's PROJECT version 1, deposited byte for byte, which machine 2 countersigns for its numbers and its facts (thirty-six controls recomputed from its own files, none biting) and not for two sentences of text that it bit and that this version does not correct (a note of deposit says so, and a later version would enter as a complement, as at delta 102); twelve lots enter with their manifests and pieces (five of machine 1, seven of machine 2); ten other lots of 22/11 that the act does not cite are not deposited; the chain and the two-dimensional system share the engine, so the agreement tests the reduction to one dimension and the absorbers, not the engine; the act says nothing of the lifetime of the closed system, of w2 = 2 exactly, or of |delta| beyond 0.0005; no rule is adopted, thirty-four await review (X); deposited on the operator's word, Depot alors.")
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
chk('git diff HEAD~1 --name-status : que des ajouts (A), aucun M ni D, autant que de pieces', len(git('diff', '--name-status', 'HEAD~1', 'HEAD').split('\n')) == len(lignes)
    and all(l.startswith('A\t') for l in git('diff', '--name-status', 'HEAD~1', 'HEAD').split('\n')), '%d fichiers ajoutes' % len(lignes))

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN DEPOT (local) : %d/%d controles PASSENT ; HEAD local %s au-dessus de %s ; push NON fait'
      % (k, n, h2, AVANT))
print('=====================================================================')
sys.exit(0 if k == n else 1)
