#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LE PERIMETRE DU DEPOT delta 95 (LA QUALIFICATION E-B, REPRISE SOUS LE GEL BIS) -- ENUMERE DEPUIS LES CITATIONS DE L'ACTE.
machine 2, v1, 14/11/2026.

Derive de la feuille du delta 94 (perimetre_depot_delta94_machine2_v1.py, au registre ou au poste, NON EDITEE : regle 17), meme methode,
meme code, TROIS changements nommes, le diff est joint :
  1. dossier() : les instruments et constructions de ce chantier (la nuit bis de la qualification E-B (gel bis, sonde v3, banc v3, feuille v2)) vont sous scripts/, comme ceux du delta precedent.
  2. le texte du manifeste (corps) parle de ce chantier et de sa date ; la phrase propre aux fichiers de reprise du 94 est retiree.
  3. un manifeste SANS ligne "pieces : N" (les lots de machine 1 des 13 et 14/11) : le compte attendu est celui des membres du zip extrait
     sous entrants/, hors manifeste ; il n'est pas tape, et une piece de table introuvable mord toujours (controle voisin).
Pour le reste, tout est herite : le perimetre ne s'ecrit pas a la main, il s'ENUMERE depuis les citations de l'acte, resolues PAR CANON
(registre, poste, ou NON RESOLU qui mord) ; le numero se DERIVE du registre (plafond + 1) ; les lots cites entrent avec leurs pieces de
table ; les ZIP ne sont pas deposes ; DEUX VERBES (`chk` mesure, `note` porte la prose) ; PB-1 : rien n'est edite.
"""
import hashlib, os, re, subprocess, sys, unicodedata

if len(sys.argv) != 3:
    sys.exit('usage : perimetre_depot_delta95_machine2_v1.py <clone frais du registre> <acte journal_delta_nn_..._vN.md>')
CLONE = os.path.abspath(sys.argv[1])
ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
ACTE = os.path.abspath(sys.argv[2])
VERSION = re.search(r'_v(\d+)\.md$', os.path.basename(ACTE)).group(1)
# Le nom de depot se DERIVE du nom de l'acte : 'nn' -> le numero, le reste inchange. La v1 du 91
# fabriquait ce nom par un gabarit '..._constante_A_run_v%s.md' ou 'run' etait code en dur ; la
# meme feuille rejouee sur l'acte du 92 ('..._second_ordre_v1.md') l'aurait donc depose sous
# 'journal_delta_91_constante_A_run_v1.md' -- un acte du 92 classe sous un nom du 91 (E-92-1,
# releve par machine 2 au contreseing). Le nom ne se fabrique plus : il se derive.
_base = os.path.basename(ACTE)
if '_nn_' not in _base:
    sys.exit("l'acte doit porter '_nn_' dans son nom (corps 'nn', numero au depot) : %s" % _base)
# Le NUMERO se DERIVE du registre (plafond + 1) : voir l'en-tete, correctif 1. Il est etabli
# ici, avant que quoi que ce soit porte un nom, parce que les sorties elles-memes le portent.
_head = subprocess.check_output(['git', '-C', CLONE, 'rev-parse', '--short', 'HEAD']).decode().strip()
_suivis = [f for f in subprocess.check_output(['git', '-C', CLONE, 'ls-files']).decode().split(chr(10)) if f]
_plafond = max(int(m) for f in _suivis for m in re.findall(r'delta_?(\d+)', f))
NUMERO = str(_plafond + 1)
MAN = os.path.join(ICI, 'MANIFEST_DEPOT_delta%s_machine2_v%s.txt' % (NUMERO, VERSION))
SORTIES = {os.path.normcase(MAN),
           os.path.normcase(os.path.join(
               ICI, 'perimetre_depot_delta%s_sur_acte_v%s_machine2.log' % (NUMERO, VERSION)))}
VALEURS = {}
TRANSPORT = {}
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
PIECES = re.compile(r'^#?\s*pieces\s*:\s*(\d+)\b', re.M)

# =====================================================================
print('\n1. LES CITATIONS DE L ACTE, ET LES DEUX INDEX PAR CANON')
# =====================================================================
texte = open(ACTE, encoding='utf-8').read()
raw_acte = open(ACTE, 'rb').read()
note('acte', '%s (version %s)' % (os.path.basename(ACTE), VERSION))
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

head, suivis = _head, _suivis
reg, reg_noms = {}, {}
for f in suivis:
    e = emp_de(os.path.join(CLONE, f))
    reg.setdefault(e[0], f)
    reg.setdefault(e[1], f)
    reg_noms.setdefault(os.path.basename(f), []).append(f)
plafond = _plafond
note('numero DERIVE du releve, non tape', 'plafond %d -> le delta de cet acte porte le %s ; '
     'le numero reste de la main de l operateur (E18)' % (plafond, NUMERO))
chk('releve : HEAD %s, plafond %d, aucun fichier delta_%s -- le numero derive est LIBRE'
    % (head, plafond, NUMERO),
    plafond >= 90 and not [f for f in suivis if 'delta_' + NUMERO in f],
    '%d fichiers suivis' % len(suivis))
chk('le delta PRECEDENT est bien au registre -- le releve porte sur un arbre a jour',
    bool([f for f in suivis if 'delta_%d' % plafond in f]), 'delta_%d present' % plafond)

poste, tables = {}, set()
for d, dn, fs in os.walk(RAC):
    dn[:] = [x for x in dn if x not in ('.git', '__pycache__')]
    for f in fs:
        p = os.path.join(d, f)
        if os.path.normcase(p) in SORTIES:
            continue
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
note('balayage : tout BOCAL4 hors .git et __pycache__ ; exclues, les seules sorties de cette feuille',
     ', '.join(os.path.basename(s) for s in sorted(SORTIES)))


def chemin_de(canon):
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

# LOTS DE CE DELTA, DERIVES : un manifeste dont la ligne d'en-tete porte le canon de l'acte ne peut pas etre cite
# par l'acte (il est fait apres lui) ; il entre par son manifeste et ses pieces de table.
canon_acte = emp_de(ACTE)[0]
lots_delta = []
for _c, _ps in list(poste.items()):
    for _p in _ps:
        _b = os.path.basename(_p)
        if (_b.upper().startswith('MANIFEST_') and _b.lower().endswith('.txt') and _c not in reg and
                _c not in [x[0] for x in a_deposer] and
                open(_p, encoding='utf-8', errors='replace').readline().startswith('MANIFESTE lot_') and
                canon_acte in open(_p, encoding='utf-8', errors='replace').readline()):
            lots_delta.append((_c, _p))
            a_deposer.append((_c, _p))
            break
chk('les lots de ce delta (manifeste dont l en-tete porte le canon de l acte) sont derives, non tapes',
    len(lots_delta) >= 1, '; '.join('%s %s' % (c, rel(p, RAC)) for c, p in lots_delta))

# =====================================================================
print('\n3. LES LOTS CITES ENTRENT AVEC LEURS PIECES DE TABLE')
# =====================================================================
# Ce chantier n'a pas d'erratum : aucune piece scellee n'a ete modifiee apres coup. Le mecanisme des
# divergences declarees du 93 est retire ; toute divergence entre une table et un fichier MORD.
declarees = {}
note('erratum', 'aucun dans ce chantier : une divergence de table mord')
divergences = []
retenues, lot_de = {}, {}
lots = [(t, p) for t, p in a_deposer
        if os.path.basename(p).upper().startswith('MANIFEST_')
        and os.path.basename(p).lower().endswith('.txt')]
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
        if not jetons:   # une ligne de TABLE se lit par son DERNIER champ, pas par une extension
            continue
        # le fichier d'une ligne de TABLE est son DERNIER champ, pas un nom devine par son
        # extension : une extension hors liste (.sh) etait sautee en silence, et deux pieces de
        # meme basename dans deux sous-dossiers (MANIFEST.sha256) se recouvraient. Le compte
        # declare l'a montre -- c'est a cela qu'il sert.
        _champs = l.split()
        # format ancien (etape 0 de machine 1) : "canon  nom  octets" -> le nom est le champ du milieu
        nom = (_champs[1] if len(_champs) == 3 and _champs[-1].isdigit() else _champs[-1]).replace(chr(92), '/')
        if nom in vus:
            continue
        # D-ACA-5 : une piece se resout par son CANON. D'abord a cote de son manifeste (le cas
        # normal), sinon PARTOUT au poste -- les lots de ce chantier ont des pieces dispersees
        # (un instrument a la racine, ses logs ailleurs). Elle ne MORD que si son canon ne
        # resout nulle part : c'est alors une piece dont le manifeste parle et que personne n'a.
        p = os.path.join(d, *nom.split('/'))
        if not (os.path.exists(p) and (emp_de(p)[0] in jetons or emp_de(p)[1] in jetons)):
            cands = [q for j in jetons for q in poste.get(j, []) if os.path.basename(q) == os.path.basename(nom)]
            if not cands:
                # Divergence DECLAREE ? le fichier local doit porter le canon DEPOSE annonce par
                # l'erratum, et la table le canon SCELLE qu'il annonce. Les deux, ou rien : un
                # erratum qui ne nomme pas une divergence ne l'excuse pas.
                _d = declarees.get(os.path.basename(nom))
                if _d and os.path.exists(p) and emp_de(p)[0] == _d[1] and _d[0] in jetons:
                    divergences.append('%s : %s  scelle %s -> depose %s (fait foi)'
                                       % (t, os.path.basename(nom), _d[0], _d[1]))
                    vus.add(nom)
                    n_tab += 1
                    e = emp_de(p)
                    if not (e[0] in reg or e[1] in reg) and e[0] not in retenues:
                        retenues[e[0]] = (p, 'lot ' + t)
                        lot_de[e[0]] = t
                    continue
                (ecarts if os.path.exists(p) else introuvables).append('%s : %s' % (t, nom))
                continue
            p = cands[0]
        e = emp_de(p)
        vus.add(nom)
        n_tab += 1
        if e[0] in reg or e[1] in reg:
            continue
        if e[0] not in retenues:
            retenues[e[0]] = (p, 'lot ' + t)
            lot_de[e[0]] = t
    m = PIECES.search(tx)
    att = int(m.group(1)) if m else None
    if att is None:        # changement 3 : manifeste sans ligne 'pieces : N' -> compte des membres du zip extrait, hors manifeste
        _nl = tx.split(chr(10))[0].split()[1]
        _dd = [x for x in (os.path.join(ICI, 'entrants', _nl), os.path.join(ICI, 'entrants', _nl + '_recu')) if os.path.isdir(x)]
        if _dd:
            att = (sum(1 for _r, _s, _fs in os.walk(_dd[0]) for _f in _fs)
                   - sum(1 for _f in os.listdir(_dd[0]) if _f.startswith('MANIFEST_')))
            note('manifeste sans ligne pieces : N', '%s : compte attendu = %d membres du zip extrait, hors manifeste' % (t, att))
    if att is None or att != n_tab:
        faux_comptes.append('%s : table %d, declare %s' % (t, n_tab, att))
    print('   lot %s  table %2d / declare %-4s %s' % (t, n_tab, att, rel(chemin, RAC)))
for t, p in a_deposer:
    e = emp_de(p)
    retenues.setdefault(e[0], (p, 'cite'))
chk('%d lots cites a deposer, chacun au compte de table declare' % (len(lots) - len(TRANSPORT)),
    not faux_comptes, '; '.join(faux_comptes) or '0 faux compte')
for _d in divergences:
    note('divergence DECLAREE par erratum, admise', _d)
chk('aucune piece de table ne s ecarte de son manifeste HORS erratum', not ecarts,
    ','.join(ecarts[:5]) or '0 ecart')
chk('aucune piece de table n est introuvable a cote de son manifeste', not introuvables,
    ','.join(introuvables[:5]) or '0 introuvable')
deja = [t for t, p in a_deposer if emp_de(p)[0] in reg or emp_de(p)[1] in reg]
chk('aucune piece retenue n est deja au registre par canon', not deja and not [c for c in retenues if c in reg],
    '%d retenues' % len(retenues))

# =====================================================================
print('\n4. LE MANIFESTE DE DEPOT -- DERIVE, JAMAIS ECRIT A LA MAIN')
# =====================================================================
def nom_cible(b):
    """Le nom de depot se DERIVE : toute piece dont le nom porte le corps '_nn_' recoit le
    NUMERO du delta, pas seulement l'acte courant. Sans cela une version anterieure de l'acte,
    citee comme remplacee, entrerait au registre sous 'journal_delta_nn_...' -- un fichier sans
    numero a cote de son propre delta. Extension naturelle de E-92-1 : un nom ne se fabrique pas,
    il se derive, et cela vaut pour TOUTE piece, pas pour la seule qui est en argument."""
    return b.replace('_nn_', '_%s_' % NUMERO)


def dossier(b):
    if re.match(r'.*_pre_enregistrement_v\d+\.md$', b):
        return 'gels/'
    if re.match(r'(sonde_qualification_EB_machine1_v\d+|banc_qui_tue_qualification_EB_machine1_v\d+|'
                r'lecture_qualification_EB_machine1_v\d+|reference_TP_rotation_complexe_machine2_v\d+(_premier_jet)?|'
                r'estimation_TP_wkb_machine1_v\d+|construction_(gel_EB_v\d+|sonde_banc_v\d+|gel_EB_bis|instrument_EB_bis)_machine1_v\d+)\.py$', b):
        return 'scripts/'
    return 'journal/'


par_nom = {}
for c, (p, orig) in retenues.items():
    par_nom.setdefault(nom_cible(os.path.basename(p)), []).append(c)
lignes, prefixes, sans_lot = [], [], []
for c, (p, orig) in sorted(retenues.items(), key=lambda kv: (dossier(os.path.basename(kv[1][0])), os.path.basename(kv[1][0]))):
    b = nom_cible(os.path.basename(p))
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
series_ajoutees = []                       # specifique au 93 : retire (voir l en-tete, changement 2)

ea = emp_de(ACTE)
NOM_DEPOT = _base.replace('_nn_', '_%s_' % NUMERO)
lignes = [l for l in lignes if l[1] != ea[0]]      # sa copie dans le lot de l acte n entre pas deux fois
lignes.insert(0, ('journal/' + NOM_DEPOT, ea[0], ea[1], ea[2], ea[3],
                  rel(ACTE, RAC), 'cet acte, copie de %s' % os.path.basename(ACTE)))
# LES PIECES DE CETTE FEUILLE. La v1 les listait par leur NOM, en dur -- il aurait donc fallu
# re-editer la feuille a chaque version, ce que la regle 17 interdit. La v2 prend TOUT ce que
# porte le repertoire de la feuille, hors ses propres sorties (qui s'ecrivent apres, et qui
# entrent par le lot ou elles sont scellees). Ce qui est deja retenu ou deja au registre par
# canon n'entre pas deux fois.
for f in sorted(os.listdir(ICI)):
    p = os.path.join(ICI, f)
    if not os.path.isfile(p) or os.path.normcase(p) in SORTIES:
        continue
    e = emp_de(p)
    if e[0] not in [l[1] for l in lignes] and not (e[0] in reg or e[1] in reg):
        lignes.append(('journal/' + nom_cible(f), e[0], e[1], e[2], e[3], rel(p, RAC), 'lot de ce delta'))
# passe finale de DE-COLLISION : deux pieces du MEME lot peuvent porter le meme basename (deux
# MANIFEST.sha256, un par sortie de run) ; le prefixe du lot ne les separe pas. Le canon, si --
# il est unique par construction (controle ci-dessous). Deterministe et sans nom invente.
vues, final = {}, []
for i, (c, B, br, oB, obr, src, orig) in enumerate(lignes):
    if c in vues:
        d, b_ = c.rsplit('/', 1)
        c2 = '%s/canon_%s__%s' % (d, B, b_)
        prefixes.append('%s -> %s (meme lot, meme nom)' % (c, os.path.basename(c2)))
        c = c2
    vues[c] = B
    final.append((c, B, br, oB, obr, src, orig))
lignes = final
for x in prefixes:
    note('collision de nom, prefixe applique', x)
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

corps = ("MANIFESTE DU LOT DE DEPOT -- DELTA %s (LA QUALIFICATION E-B, REPRISE SOUS LE GEL BIS) -- 14/11/2026 -- "
         "assemble par machine 2 -- derive de l'acte v%s\n" % (NUMERO, VERSION))
corps += ("Convention B (sha256 NFC+LF, 16 hex) et empreinte brute, les deux tailles ; le depot et "
          "le numero sont de la main de l'operateur.\n")
corps += ("PERIMETRE ENUMERE, PAS ECRIT : chaque ligne vient d'une empreinte CITEE par l'acte, "
          "resolue par canon au poste, ou d'une piece de TABLE d'un lot cite (verifiee contre "
          "son manifeste) ; ce qui est deja au registre par canon n'entre pas ; le lot de "
          "transport (re-livraison) entre par son manifeste seul. Feuille : "
          "perimetre_depot_delta%s_machine2_v1.py, log livre a cote.\n" % NUMERO)
corps += ("Releve du registre ordonnant sur clone frais lbaaz/SG_1 : HEAD %s, plafond %d, aucun "
          "fichier delta_%s -> %s est libre ; a rejouer par qui depose.\n" % (head, plafond, NUMERO, NUMERO))
corps += ("Piece de depot : %s, COPIE OCTET POUR OCTET de "
          "%s (corps 'nn', numero dans le nom seulement, forme (a) "
          "des deltas 88 et 89) ; canon %s.\n" % (NOM_DEPOT, _base, ea[0]))
corps += ("Emplacements : gels/ pour les gels (*_pre_enregistrement_v*.md), scripts/ pour "
          "les instruments de ce chantier (sonde, banc, feuille, reference du temoin) et leurs scripts de construction, journal/ a plat pour le reste. Un nom qui "
          "collisionne (deux canons sous le meme nom, entre les deux plumes) porte le prefixe "
          "lot_<canon du lot>__ ; %d cas, listes dans le log.\n" % len(prefixes))
corps += ("LOTS DE CE DELTA, DERIVES (manifeste dont l en-tete porte le canon de l acte) : %s. NON CITES PAR L ACTE (ils sont faits apres lui), ils entrent par leur manifeste et leurs pieces de table.\n" % (", ".join(c for c, p in lots_delta) or "aucun"))
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
print('DEPOT : %d pieces (%s) ; manifeste %s %s'
      % (len(lignes), ', '.join('%s %d' % kv for kv in sorted(par_dossier.items())), os.path.basename(MAN), emp_de(MAN)[0]))
print('=====================================================================')
sys.exit(0 if k == n else 1)
