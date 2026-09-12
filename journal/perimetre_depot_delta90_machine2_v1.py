#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LE PERIMETRE DU DEPOT delta 90 -- ENUMERE DEPUIS LES CITATIONS DE L'ACTE. machine 2, v1,
12/09/2026.

Le perimetre ne s'ecrit pas a la main : il s'ENUMERE. Cette feuille lit l'acte
`journal_delta_nn_constante_A_v1.md`, en extrait tous les jetons de 16 hex, et resout chacun
PAR CANON (convention B, ou brut pour les ZIP et les logs cites en brut) :
  -- sur le CLONE FRAIS du registre (chemin en argument ; `git ls-files`) : AU REGISTRE ;
  -- sinon sur TOUT le poste BOCAL4 (hors .git et __pycache__) : A DEPOSER ;
  -- sinon : NON RESOLU, et c'est une morsure -- un acte ne cite pas ce qu'il n'a pas.
Trois jetons de l'acte ne sont pas des empreintes de FICHIER mais des VALEURS (les bits d'un
double sous mutation ; deux empreintes de champ de forces lues dans des JSON) : ils sont
DECLARES ici, la feuille verifie qu'ils sont bien cites, et la relecture des nombres les
recalcule a la source.
Tout LOT cite (un manifeste .txt) entre AVEC SES PIECES DE TABLE, chacune verifiee contre sa
ligne (canon B ou brut) a cote du manifeste -- la regle 8 de l'acte, payee la veille : le
compte de table egale le `pieces : N` declare. Un lot de TRANSPORT (la re-livraison, qui
re-emet les pieces d'autres lots sous leurs chemins) entre par son manifeste seul.
Une piece a un seul canon et un seul chemin de depot : la table d'un lot nomme la piece (le
nom de table gagne sur le nom d'une copie flottante, D-ACA-5) ; deux pieces de meme nom a
canons differents portent le prefixe de leur lot (regle du 29/08 : un nom qui collisionne
porte le prefixe de sa plume) ; une piece deja au registre par canon n'entre pas.

Il DERIVE ensuite le manifeste de depot `MANIFEST_DEPOT_delta90_machine2.txt` : chemin cible
(gels/ pour les gels, scripts/ pour l'instrument et ses scripts de construction, journal/ a
plat pour le reste, forme des deltas 88 et 89), empreinte B, empreinte brute, les deux
tailles, la source au poste, l'origine ; et l'acte copie OCTET POUR OCTET sous son nom
numerote. Les comptes sont etablis APRES le dernier ajout. Les ZIP ne sont pas deposes
(precedent non pris) : ils sont listes a part, en brut.

DEUX VERBES : `chk` mesure et compte ; `note` porte la prose. PB-1 : rien n'est edite.
"""
import hashlib, os, re, subprocess, sys, unicodedata

if len(sys.argv) != 2:
    sys.exit('usage : perimetre_depot_delta90_machine2_v1.py <clone frais du registre>')
CLONE = os.path.abspath(sys.argv[1])
ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
ACTE = os.path.join(ICI, 'journal_delta_nn_constante_A_v1.md')
NUMERO = '90'
# jetons de 16 hex cites par l'acte qui sont des VALEURS, pas des empreintes de fichier
VALEURS = {
    '3ef1660b5147653b': 'bits du double INF sous mutation (derivation v3, section 6)',
    '0491b83e6893dbbf': 'champ_forces_empreinte du JSON pre-vol NOYAU de machine 1',
    'f150f2685187b9d2': 'champ_forces_empreinte du JSON pre-vol LIBM de machine 1',
}
# lots de TRANSPORT : leur manifeste entre, leur table (chemins d'autres lots) ne se deplie pas
TRANSPORT = {'d0ab94382e1b5808': 're-livraison du fond a machine 1, 158 pieces sous leurs chemins'}
OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-58s %s' % ('PASSE' if c else 'MORD ', n[:58], d))


def note(n, d=''):
    print('  [ note] %-58s %s' % (n[:58], d))


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8'))
        t = t.replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
        return (hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16],
                len(t), len(raw))
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return (h, h, len(raw), len(raw))


_E = {}


def emp_de(p):
    if p not in _E:
        _E[p] = emp(open(p, 'rb').read())
    return _E[p]


def rel(p, base):
    return os.path.relpath(p, base).replace('\\', '/')


HEX = re.compile(r'\b[0-9a-f]{16}\b')
NOM = re.compile(r'[\w.\-+@]+\.(?:md|py|log|json|txt|zip|csv|npz|png)\b')
TABLE = re.compile(r'^[0-9a-f]{16}\s')
PIECES = re.compile(r'^pieces\s*:\s*(\d+)\b', re.M)

# =====================================================================
print('\n1. LES CITATIONS DE L ACTE, ET LES DEUX INDEX PAR CANON')
# =====================================================================
texte = open(ACTE, encoding='utf-8').read()
raw_acte = open(ACTE, 'rb').read()
chk('l acte est ASCII pur, LF, newline final',
    all(b < 128 for b in raw_acte) and b'\r' not in raw_acte and raw_acte.endswith(b'\n'),
    '%d octets' % len(raw_acte))
cites = []
for t in HEX.findall(texte):
    if t not in cites:
        cites.append(t)
chk('l acte cite des empreintes (compte etabli apres extraction)', len(cites) > 0,
    '%d jetons distincts de 16 hex' % len(cites))
chk('chaque VALEUR declaree est bien citee par l acte', all(v in cites for v in VALEURS),
    ', '.join(VALEURS))
chk('chaque lot de TRANSPORT declare est bien cite par l acte', all(v in cites for v in TRANSPORT),
    ', '.join(TRANSPORT))

head = subprocess.check_output(['git', '-C', CLONE, 'rev-parse', '--short', 'HEAD']).decode().strip()
suivis = [f for f in subprocess.check_output(['git', '-C', CLONE, 'ls-files']).decode().split('\n') if f]
reg, reg_noms = {}, {}
for f in suivis:
    e = emp_de(os.path.join(CLONE, f))
    reg.setdefault(e[0], f)
    reg.setdefault(e[1], f)
    reg_noms.setdefault(os.path.basename(f), []).append(f)
plafond = max(int(m) for f in suivis for m in re.findall(r'delta_?(\d+)', f))
chk('releve : HEAD %s, plafond %d, aucun fichier delta_%s' % (head, plafond, NUMERO),
    head == 'd037d21' and plafond == 89 and not [f for f in suivis if 'delta_' + NUMERO in f],
    '%d fichiers suivis' % len(suivis))

# le poste : tout fichier (hors .git, __pycache__ et ce depot), tous les chemins par canon ;
# et l'ensemble des (repertoire, nom) declares en TABLE par un manifeste quelconque
poste, tables = {}, set()
for d, dn, fs in os.walk(RAC):
    dn[:] = [x for x in dn if x not in ('.git', '__pycache__')]
    if os.path.abspath(d) == ICI:
        continue
    for f in fs:
        p = os.path.join(d, f)
        try:
            e = emp_de(p)
        except OSError:
            continue
        poste.setdefault(e[0], []).append(p)
        if e[1] != e[0]:
            poste.setdefault(e[1], []).append(p)
        if f.upper().startswith('MANIFEST') and f.endswith('.txt'):
            for l in open(p, encoding='utf-8', errors='replace').read().split('\n'):
                if TABLE.match(l) and NOM.findall(l):
                    tables.add(os.path.normcase(os.path.join(d, NOM.findall(l)[0])))
note('index du poste', '%d canons distincts (B et brut), %d noms de table' % (len(poste), len(tables)))


def chemin_de(canon):
    """Le chemin d'une piece au poste : un chemin de TABLE si un lot la nomme, sinon le premier."""
    ps = poste[canon]
    for p in ps:
        if os.path.normcase(p) in tables:
            return p
    return ps[0]


# =====================================================================
print('\n2. RESOLUTION DE CHAQUE CITATION -- AU REGISTRE, AU POSTE, OU NULLE PART')
# =====================================================================
au_registre, a_deposer, non_resolus, zips = [], [], [], []
for t in cites:
    if t in VALEURS:
        continue
    if t in reg:
        au_registre.append((t, reg[t]))
    elif t in poste:
        p = chemin_de(t)
        (zips if p.lower().endswith('.zip') else a_deposer).append((t, p))
    else:
        non_resolus.append(t)
for t, f in au_registre:
    print('   registre  %s  %s' % (t, f))
for t, p in a_deposer:
    print('   poste     %s  %s' % (t, rel(p, RAC)))
chk('toute empreinte citee resout par canon (registre, poste, ou valeur)', not non_resolus,
    ','.join(non_resolus) or '%d au registre, %d au poste, %d zip, %d valeurs'
    % (len(au_registre), len(a_deposer), len(zips), len(VALEURS)))
for t, p in zips:
    note('ZIP cite en brut, NON depose (precedent non pris)', '%s  %s' % (t, rel(p, RAC)))

# =====================================================================
print('\n3. LES LOTS CITES ENTRENT AVEC LEURS PIECES DE TABLE')
# =====================================================================
# retenues : canon B -> (chemin au poste, lot d'origine ou 'cite'). Les tables d'abord (elles
# nomment les pieces), les citations isolees ensuite.
retenues, lot_de = {}, {}
lots = [(t, p) for t, p in a_deposer if os.path.basename(p).upper().startswith('MANIFEST')]
faux_comptes, ecarts, introuvables = [], [], []
for t, chemin in lots:
    e = emp_de(chemin)
    retenues.setdefault(e[0], (chemin, 'cite'))
    if t in TRANSPORT:
        note('lot de TRANSPORT %s : manifeste seul' % t, TRANSPORT[t])
        continue
    d = os.path.dirname(chemin)
    tx = open(chemin, encoding='utf-8').read()
    n_tab, vus = 0, set()
    for l in tx.split('\n'):
        if not TABLE.match(l):
            continue
        jetons, noms = HEX.findall(l), NOM.findall(l)
        if not jetons or not noms:
            continue
        nom = noms[0]
        if nom in vus:
            continue
        p = os.path.join(d, nom)
        if not os.path.exists(p):
            introuvables.append('%s : %s' % (t, nom))
            continue
        e = emp_de(p)
        if e[0] not in jetons and e[1] not in jetons:
            ecarts.append('%s : %s' % (t, nom))
            continue
        vus.add(nom)
        n_tab += 1
        if e[0] in reg or e[1] in reg:
            continue
        if e[0] not in retenues:
            retenues[e[0]] = (p, 'lot ' + t)
            lot_de[e[0]] = t
    m = PIECES.search(tx)
    att = int(m.group(1)) if m else None
    if att is None or att != n_tab:
        faux_comptes.append('%s : table %d, declare %s' % (t, n_tab, att))
    print('   lot %s  table %2d / declare %-4s %s' % (t, n_tab, att, rel(chemin, RAC)))
for t, p in a_deposer:
    e = emp_de(p)
    retenues.setdefault(e[0], (p, 'cite'))
chk('%d lots cites a deposer, chacun au compte de table declare' % (len(lots) - len(TRANSPORT)),
    not faux_comptes, '; '.join(faux_comptes) or '0 faux compte')
chk('aucune piece de table ne s ecarte de son manifeste', not ecarts, ','.join(ecarts[:5]) or '0 ecart')
chk('aucune piece de table n est introuvable a cote de son manifeste', not introuvables,
    ','.join(introuvables[:5]) or '0 introuvable')
deja = [t for t, p in a_deposer if emp_de(p)[0] in reg or emp_de(p)[1] in reg]
chk('aucune piece retenue n est deja au registre par canon', not deja and not [c for c in retenues if c in reg],
    '%d retenues' % len(retenues))

# =====================================================================
print('\n4. LE MANIFESTE DE DEPOT -- DERIVE, JAMAIS ECRIT A LA MAIN')
# =====================================================================
def dossier(b):
    if re.match(r'.*_pre_enregistrement_v\d+\.md$', b):
        return 'gels/'
    if re.match(r'(banc_qualification_machine1_v\d+|construction_banc_v\d+_machine1_v\d+)\.py$', b):
        return 'scripts/'
    return 'journal/'


# collisions de nom : entre pieces retenues, et avec le registre ; les deux membres d'une
# collision entre retenues prennent le prefixe de leur lot ; une collision avec le registre
# a autre canon prend le prefixe aussi ; une piece dont le chemin cible existe deja au
# registre AU MEME canon n'entre pas (elle y est).
par_nom = {}
for c, (p, orig) in retenues.items():
    par_nom.setdefault(os.path.basename(p), []).append(c)
lignes, prefixes, sans_lot = [], [], []
for c, (p, orig) in sorted(retenues.items(), key=lambda kv: (dossier(os.path.basename(kv[1][0])), os.path.basename(kv[1][0]))):
    b = os.path.basename(p)
    homonymes_reg = [f for f in reg_noms.get(b, []) if emp_de(os.path.join(CLONE, f))[0] != c]
    if len(par_nom[b]) > 1 or homonymes_reg:
        if c in lot_de:
            b2 = 'lot_%s__%s' % (lot_de[c], b)
        else:
            b2 = 'canon_%s__%s' % (c, b)
            sans_lot.append(b)
        prefixes.append('%s -> %s' % (b, b2))
        b = b2
    e = emp_de(p)
    lignes.append((dossier(b) + b, e[0], e[1], e[2], e[3], rel(p, RAC), orig))
ea = emp_de(ACTE)
lignes.insert(0, ('journal/journal_delta_%s_constante_A_v1.md' % NUMERO, ea[0], ea[1], ea[2], ea[3],
                  rel(ACTE, RAC), 'cet acte, copie de journal_delta_nn_constante_A_v1.md'))
for f in ('relecture_nombres_delta90_machine2_v1.py', 'relecture_nombres_delta90_machine2_v1.log',
          'perimetre_depot_delta90_machine2_v1.py'):
    p = os.path.join(ICI, f)
    if os.path.exists(p):
        e = emp_de(p)
        lignes.append(('journal/' + f, e[0], e[1], e[2], e[3], rel(p, RAC), 'lot de ce delta'))
for x in prefixes:
    note('collision de nom, prefixe du lot applique', x)
cibles = [l[0] for l in lignes]
chk('aucun chemin cible en double ni deja au registre', len(cibles) == len(set(cibles))
    and not [c for c in cibles if c in suivis], '%d chemins cibles' % len(cibles))
canons_dep = [l[1] for l in lignes]
chk('aucun doublon de canon dans le depot', len(canons_dep) == len(set(canons_dep)), '%d pieces' % len(lignes))
chk('toute collision resolue porte le prefixe de son LOT (aucune piece flottante)', not sans_lot,
    ','.join(sans_lot) or '%d prefixes' % len(prefixes))
non_ascii = [c for c, B, br, oB, obr, src, orig in lignes if c.endswith(('.md', '.py', '.txt')) and B != br]
chk('les .md/.py/.txt deposes sont B == brut (ASCII/LF)', not non_ascii,
    ','.join(non_ascii[:5]) or '%d pieces texte' % sum(1 for l in lignes if l[0].endswith(('.md', '.py', '.txt'))))
par_dossier = {}
for c, *_ in lignes:
    par_dossier[c.split('/')[0]] = par_dossier.get(c.split('/')[0], 0) + 1

corps = ("MANIFESTE DU LOT DE DEPOT -- DELTA %s (LA CHAINE DE LA CONSTANTE A) -- 12/09/2026 -- "
         "assemble par machine 2\n" % NUMERO)
corps += ("Convention B (sha256 NFC+LF, 16 hex) et empreinte brute, les deux tailles ; le depot, "
          "le numero et les series sont de la main de l'operateur.\n")
corps += ("PERIMETRE ENUMERE, PAS ECRIT : chaque ligne vient d'une empreinte CITEE par l'acte, "
          "resolue par canon au poste, ou d'une piece de TABLE d'un lot cite (verifiee contre "
          "son manifeste) ; ce qui est deja au registre par canon n'entre pas ; le lot de "
          "transport (re-livraison) entre par son manifeste seul. Feuille : "
          "perimetre_depot_delta%s_machine2_v1.py, log livre a cote.\n" % NUMERO)
corps += ("Releve du registre ordonnant sur clone frais lbaaz/SG_1 : HEAD %s, plafond %d, aucun "
          "fichier delta_%s -> %s est libre ; a rejouer par qui depose.\n" % (head, plafond, NUMERO, NUMERO))
corps += ("Piece de depot : journal_delta_%s_constante_A_v1.md, COPIE OCTET POUR OCTET de "
          "journal_delta_nn_constante_A_v1.md (corps 'nn', numero dans le nom seulement, forme (a) "
          "des deltas 88 et 89) ; canon %s.\n" % (NUMERO, ea[0]))
corps += ("Emplacements : gels/ pour les gels (*_pre_enregistrement_v*.md), scripts/ pour "
          "l'instrument et ses scripts de construction, journal/ a plat pour le reste. Un nom qui "
          "collisionne (deux canons sous le meme nom, entre les deux plumes) porte le prefixe "
          "lot_<canon du lot>__ ; %d cas, listes dans le log.\n" % len(prefixes))
corps += ("NON DEPOSES, ASSUMES : les ZIP des lots (precedent non pris ; listes en brut en fin de "
          "manifeste) ; MANIFEST.sha256 (dette anterieure).\n")
corps += "colonnes : chemin_cible  empreinte_B  empreinte_brute  octets_B  octets_bruts  source (relative a BOCAL4)  [origine]\n\n"
for c, B, br, oB, obr, src, orig in lignes:
    corps += "%-84s %s %s %9d %9d  %s  [%s]\n" % (c, B, br, oB, obr, src, orig)
corps += "\nZIP CITES EN BRUT, NON DEPOSES :\n"
for t, p in zips:
    corps += "  %s  %s\n" % (t, rel(p, RAC))
corps += "\nEMPREINTES CITEES DEJA AU REGISTRE (%d) : %s\n" % (
    len(au_registre), ', '.join('%s (%s)' % (t, f) for t, f in au_registre))
corps += "VALEURS CITEES (pas des fichiers ; recalculees par la relecture) : %s\n" % ', '.join(
    '%s (%s)' % kv for kv in VALEURS.items())
corps += "\npar dossier : %s\n" % ', '.join('%s %d' % kv for kv in sorted(par_dossier.items()))
corps += "pieces : %d (compte etabli APRES le dernier ajout)\n" % len(lignes)
corps += "-- FIN MANIFESTE --\n"
MAN = os.path.join(ICI, 'MANIFEST_DEPOT_delta%s_machine2.txt' % NUMERO)
open(MAN, 'w', encoding='utf-8', newline='\n').write(corps)

relu = open(MAN, encoding='utf-8').read()
n_lignes = sum(1 for l in relu.split('\n') if re.match(r'^(gels|scripts|journal)/\S+\s+[0-9a-f]{16} [0-9a-f]{16} ', l))
chk('le manifeste relu porte autant de lignes que de pieces', n_lignes == len(lignes),
    '%d lignes, %d pieces' % (n_lignes, len(lignes)))
faux = [src for c, B, br, oB, obr, src, orig in lignes if emp_de(os.path.join(RAC, src))[0] != B]
chk('chaque source du manifeste resout encore au canon ecrit', not faux, ','.join(faux[:3]) or '0 ecart')
m = PIECES.search(relu)
chk('le manifeste declare son compte, egal aux lignes', m is not None and int(m.group(1)) == n_lignes,
    m.group(0) if m else 'aucun')
chk('le manifeste est ASCII', all(b < 128 for b in open(MAN, 'rb').read()), '%d octets' % os.path.getsize(MAN))

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN PERIMETRE : %d/%d controles PASSENT' % (k, n))
print('%d empreintes citees : %d au registre, %d au poste, %d zip, %d valeurs, %d non resolues'
      % (len(cites), len(au_registre), len(a_deposer), len(zips), len(VALEURS), len(non_resolus)))
print('DEPOT : %d pieces (%s) ; manifeste %s'
      % (len(lignes), ', '.join('%s %d' % kv for kv in sorted(par_dossier.items())), emp_de(MAN)[0]))
print('=====================================================================')
sys.exit(0 if k == n else 1)
