#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LE DEPOT DU DELTA 94 (LA QUALIFICATION E-B) SUR CLONE FRAIS -- copie, verification au bit, releve, commit LOCAL.
machine 2, v1, 12/11/2026. Le PUSH n'est pas fait ici : il est un geste de l'operateur.

Derive de depot_delta93_machine2_v1.py (canon 4433985da357483e, au registre, NON EDITE : regle 17). Trois changements :
le texte du message de commit ; DEUX PIECES EXPLICITES AJOUTEES au manifeste lu, le manifeste de depot lui-meme et
le journal du perimetre, qui ne peuvent pas se porter eux-memes (ils sont ecrits par la feuille de perimetre,
apres coup) et entrent sous journal/ avec leur nom ; et les noms de ce fichier. Le numero se lit toujours dans le
nom du manifeste ; l'etat attendu du registre s'en deduit ; rien n'est tape.

Arguments : <clone frais> <MANIFEST_DEPOT_delta<nn>_machine2_v<N>.txt>.
  1. releve AVANT : origin/main == HEAD, arbre propre, plafond == nn - 1, aucun delta_nn ;
  2. chaque ligne du manifeste : la source resout au canon B ecrit ; la cible n'existe pas
     encore dans l'arbre ; copie OCTET POUR OCTET ; relecture de la copie au canon ;
  3. git add ; le nombre de fichiers ajoutes == le compte declare du manifeste, aucun modifie,
     aucun supprime, rien hors gels/ scripts/ journal/ ;
  4. commit local, auteur celui du depot, message SANS trailer d'outillage (convention du
     depot public, decidee le 25/08) ; le message est ecrit ici d'un bloc ;
  5. releve APRES : HEAD a avance d'un commit sur le HEAD d'avant, plafond == nn, l'acte
     numerote resout au canon de l'acte source.
Les comptes sont LUS ; les sorties s'ecrivent avant tout assert. DEUX VERBES.
"""
import hashlib, os, re, shutil, subprocess, sys, unicodedata

if len(sys.argv) != 3:
    sys.exit('usage : depot_delta94_machine2_v1.py <clone frais> <MANIFEST_DEPOT_delta<nn>_machine2_v<N>.txt>')
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
msg = ("delta 94 -- the qualification of the E-B estimator Gamma_LS (the quantum branch's outgoing "
       "width, read with a complex absorber at eta0/8) returns INCONCLUSIVE ON THE INSTRUMENT: at "
       "stage 1 of the v2 freeze, played on 12/11 on BOCAL4 with every guard held, the positive "
       "witness (the H+ twin, its width known by complex rotation, reference and retained couplings "
       "certified across the two machines) holds at the long absorber, with a plateau and agreement "
       "to the reference at 0.6 and 0.8 per cent, and does not hold at the short one, where no "
       "plateau of five values exists, at both couplings retained, and the freeze requires both; "
       "stage 2 is not played, the phantom is not read, and nothing is said of the six M17 widths, "
       "whose status is unchanged; the known width is returned to 0.5 per cent at the strongest rung"
       " of the eta scale, while at the rung M17 reads (k = 3, short absorber) the absorber returns "
       "0.435 and 0.422 times the known width and M17's own descent gate refuses the point; the eta "
       "scale of the freeze covered the witness plateau only by its strong edge, a design defect of "
       "the freeze's author recorded as such, and the negative witness cannot be played at full "
       "size, a second one; under the freeze's own safeguard of one freeze, one correction round, "
       "one run and one act the work stops here, a resumption being a new freeze and the operator's "
       "decision; four candidate rules, numbered 22 to 25, join the twenty-one awaiting review (X); "
       "act written by one machine and countersigned by the other after the numbers were re-read at "
       "their sources, three errors of description found in the first version and corrected in a "
       "second before deposit, the superseded version being deposited beside it so that the "
       "correction stays legible, the deposited file being the countersigned one byte for byte")
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
