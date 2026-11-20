#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LE DEPOT DU DELTA 103 SUR CLONE FRAIS -- copie, verification au bit, releve, commit LOCAL. machine 2, v1, 20/11/2026.
Le PUSH n'est pas fait ici.

Derive de depot_delta102_machine2_v1.py (NON EDITE : regle 17). Un seul changement : le texte du message de commit ; le numero se lit toujours
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
    sys.exit('usage : depot_delta103_machine2_v1.py <clone frais> <MANIFEST_DEPOT_delta<nn>_machine2_v<N>.txt>')
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
msg = ("delta 103 -- the bridge between the absorber and the closed box: the density that the absorber reads at the phantom system's site (0, 0), from which delta 102 drew the width of the vacuum, is tested as the strength that the vacuum carries onto the levels of the CLOSED box, on six cells drawn at random and never played (two values of w2, 397/200 for delta -0.015 and 2019/1000 for delta +0.019, each at 3, 4 and 5 rungs of chain), four absorbers and twenty closed boxes (sides 180 to 189 and 291 to 300) per cell; (S) HELD and (C) HELD at all six cells, readable six of six, the sum of the weights that the levels of the closed box carry on site (0, 0) being 0.98 to 1.03 per cell against the chain's third-order smooth (tolerance 0.85 to 1.15 per cell, 0.80 to 1.20 per group of sides) and the number of levels growing as the side times |delta| (reduced count 0.434 to 0.486 against 0.33 to 0.55, ratio of the two groups 1.43 to 1.59 against 1.25 to 1.85); (L) FELL and (L2) FELL at the three cells of negative disagreement (MG3, MG4, MG5), where at 8 |delta| from the vacuum the chain at third order departs from the two-dimensional density by 0.0502, 0.0608 and 0.0745 in logarithm against a tolerance of 0.05 (MG3 by 0.00024 only) and the second order is closer than the third at the four judged distances, and both HELD at the three cells of positive disagreement (worst 0.0180); the act writes what this carries and what it does not: the bridge holds for the sum at both signs, played blind at negative delta, and at positive delta the chain's smooth is within the tolerances, but at negative delta the third-order chain does not render the density to 5 per cent far from the vacuum, so that by the judged statements the bridge is not reached there, as the freeze had written beforehand for this outcome, and the sum re-read with the two-dimensional density itself, which is not judged, is 0.998 to 1.011; the act does not say that the bridge holds at negative delta as a judged statement, nor anything of the infinite box, the exact resonance or the lifetime of the closed system, and it does not explain why the third-order chain corrects too far at negative delta while it is right at the vacuum (within 0.0004 at all six cells, one of the four absorbers aside); five of the pen's twenty-four announcements go against the run, all at negative delta and all on the chain; under a freeze in two parts (the draw and eligibility rule, then the instrument and the statements, with a rectificatif before the run), each certified by the other machine before the run (the first with one drafting reserve, the second with eight, all taken by the pen before the run), the seed (456823) being given by the operator after the certification of the first part so that neither machine chose the cells, both machines drawing the same six; played once on BOCAL4 on 18/11 by a pilot of machine 2 (48 calculations, eight at a time, 11185 s, none replayed, 24 density outputs complete out of 24 and 120 boxes out of 120), the operator having written the date of the green light but not its hour, machine 2's reception time (00:11) standing in its journal as no attested hour; the run's three sheets of machine 1 and three sheets of machine 2 written from the text alone give the same 24 judgements and the same four family verdicts; act written by machine 1 and countersigned by machine 2 without condition, by sixteen controls recomputed from machine 2's own sheets and the raw outputs, none biting, the same sheet biting thirty times on a copy with one thing corrupted at a time (twenty-nine at the second pass: the control that did not bite is kept), machine 1's own sheet replayed on machine 2's workstation (ten controls, none biting, twenty corruptions, twenty bitten), and two drafting imprecisions pointed out without condition; the reading of the weights by partition is not verified in extended precision, as the act says; nine lots enter with their manifests and pieces (four of machine 1, five of machine 2); no rule is adopted; deposited on the operator's word, Ordre de deposer !")
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
