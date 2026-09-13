#!/usr/bin/env python3
# -*- coding: ascii -*-
"""N-70 v3 : l'enumeration des cles du pre-vol, RE-ANCREE sur le pre-vol de l'instrument v10 au
reglage du gel v7 (delta' = 1/44100). machine 2, 13/09/2026. Tout est DERIVE, comme en v2
(derivation_cles_N70_machine2_v2.py, non editee) ; les entrees sont des ARGUMENTS et chaque
entree est authentifiee par canon avant lecture ; une entree absente rend sa jambe NON JOUEE,
declaree, jamais tue.

Usage : derivation_cles_N70_machine2_v3.py <prevol_1.json> <prevol_2.json> <depot_9bis.json>
        <reference run 85.json> <sortie .md> [<prevol machine 1.json>]
Les trois jambes de la v2 : (1) stabilite sur ma machine (deux pre-vols) ; (2) accord entre
machines (son pre-vol v10 : NON JOUEE si absent) ; (3) presence dans la reference deposee.
"""
import hashlib, json, os, re, struct, sys, unicodedata

P1, P2, DEPF, REFF, OUT = sys.argv[1:6]
PM1 = sys.argv[6] if len(sys.argv) > 6 else None


def canon(p):
    s = open(p, 'rb').read().decode('utf-8')
    return hashlib.sha256(unicodedata.normalize('NFC', s.replace('\r\n', '\n').replace('\r', '\n')).encode()).hexdigest()[:16]


def plat(o, pre=''):
    if isinstance(o, dict):
        for k, v in sorted(o.items()):
            yield from plat(v, pre + '/' + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from plat(v, pre + '/%d' % i)
    else:
        yield pre, o


def pas(a, b):
    if not (isinstance(a, float) and isinstance(b, float)):
        return None
    ia = struct.unpack('<q', struct.pack('<d', a))[0]
    ib = struct.unpack('<q', struct.pack('<d', b))[0]
    return abs(ia) + abs(ib) if (ia < 0) != (ib < 0) else abs(ia - ib)


J1, J2 = json.load(open(P1, encoding='utf-8')), json.load(open(P2, encoding='utf-8'))
M1, M2 = dict(plat(J1)), dict(plat(J2))
DEP = json.load(open(DEPF, encoding='utf-8'))
RJ = json.load(open(REFF, encoding='utf-8'))
REF = dict(plat(RJ))
EL = dict(plat(json.load(open(PM1, encoding='utf-8')))) if PM1 and os.path.exists(PM1) else None
assert J1['meta']['version'] == 'banc_qualification_machine1_v10', J1['meta']['version']
assert J1['reglage']['delta'] == '1/44100', J1['reglage']['delta']
assert J1['meta']['gel_alpha'][0].endswith('constante_A_pre_enregistrement_v7.md'), J1['meta']['gel_alpha']
GEL7 = J1['meta']['gel_alpha'][1]
SCRIPT = J1['meta']['script_sha256_brut'][:16]

EXEMPT = DEP['exemptes']
PERIM = tuple('/%s/' % c for c in sorted(DEP['reference'].keys()))
dans = lambda k: k.startswith(PERIM)
est_exempt = lambda k: any(e in k for e in EXEMPT)

groupes = []
for etq, D in (('pre-vol', M1), ('reference', REF)):
    for g in sorted(set(k.rsplit('/', 1)[0] for k in D if k.endswith('/statut') and '/integrales/' in k)):
        groupes.append((etq, g, D[g + '/statut'], (g + '/ecart_a_4') in D))
LUE = lambda st: not st.startswith('NON LUE')
contre = [(e, g, st, p) for e, g, st, p in groupes if p != LUE(st)]

perim = sorted(k for k in M1 if dans(k))
absentes = sorted(k for k in perim if k not in REF)
exemptes = sorted(k for k in perim if est_exempt(k) and k not in absentes)
if EL is not None:
    inter = set(k for k in M1 if k in EL and M1[k] != EL[k])
    mordantes = sorted(k for k in perim if k in inter and k not in exemptes and k not in absentes)
else:
    # jambe (2) NON JOUEE : les cles NON PREDITES de la v2 (4867dffe3392dea6) sont HERITEES telles
    # quelles, LUES dans sa section 3, a confirmer sur son JSON v10
    V2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chaine_constante_A_pour_machine1', 'enumeration_cles_prevol_N70_machine2_v2.md')
    assert canon(V2) == '4867dffe3392dea6', canon(V2)
    t2 = open(V2, encoding='ascii').read()
    bloc = t2[t2.index('NON PREDITES (inchangees'):t2.index('PREDITES IDENTIQUES : les')]
    herit = sorted(m.group(1) for m in re.finditer(r'^    (/\S+)\s+\d+ pas', bloc, re.M))
    assert len(herit) == 4, herit
    mordantes = sorted(k for k in perim if k in herit and k not in exemptes and k not in absentes)
identiques = sorted(k for k in perim if k not in exemptes and k not in absentes and k not in mordantes)
instables = sorted(k for k in M1 if M1[k] != M2.get(k))
perim_run = sorted(k for k in perim if k not in absentes)
assert len(identiques) + len(exemptes) + len(mordantes) + len(absentes) == len(perim)
assert len(perim_run) == len([k for k in REF if dans(k)]), 'le perimetre du RUN doit egaler la reference'
assert all(est_exempt(k) or not dans(k) for k in instables), 'une cle instable hors exemptions : %s' % [k for k in instables if dans(k) and not est_exempt(k)]

L = []
w = L.append
w('ENUMERATION DES CLES DU PRE-VOL -- N-70 -- MACHINE 2 -- **v3**')
w('===============================================================')
w('Plume : machine 2. Se DEPOSE AVANT le run du volet T.')
w('Ancree sur le JSON du pre-vol temoin, instrument v10 (script brut')
w('%s..., meta), gel constante A v7 %s, gel temoin v11' % (SCRIPT, GEL7))
w('a2e7ef3e237c5acf + son erratum 7 (i), reglage delta\' = 1/44100.')
w('SUPERSEDE la v2 (4867dffe3392dea6, ancree sur le v8 a 1/102400),')
w('qui n est PAS editee (PB-1). Meme regle, memes classes, meme')
w('feuille de derivation (v3 : entrees en arguments, jambe absente')
w('declaree NON JOUEE).')
w('')
w('Entrees, authentifiees par canon avant lecture :')
w('  pre-vol 1 (BOCAL4)   %s  %s' % (canon(P1), os.path.basename(P1)))
w('  pre-vol 2 (BOCAL4)   %s  %s' % (canon(P2), os.path.basename(P2)))
w('  depot 9bis           %s  %s' % (canon(DEPF), os.path.basename(DEPF)))
w('  reference run 85     %s  %s' % (canon(REFF), os.path.basename(REFF)))
if EL is not None:
    w('  pre-vol machine 1    %s  %s' % (canon(PM1), os.path.basename(PM1)))
else:
    w('  pre-vol machine 1    ABSENT -> jambe (2) NON JOUEE : les cles NON PREDITES')
    w('                       sont celles de la v2 (4 tol_int a appel libm), HERITEES,')
    w('                       a confirmer sur son JSON de pre-vol v10.')
w('')
w('E18 : aucun numero pris, aucun propose.')
w('')
w('=========================================================')
w('1. LA REGLE D EMISSION CONDITIONNELLE -- DERIVEE')
w('=========================================================')
w('')
w('Sur les %d groupes `integrales/*` des DEUX fichiers :' % len(groupes))
w('')
w('    **ecart_a_4 est EMISE si et seulement si l integrale est LUE**')
w('    (statut PASSE ou MORD) ; elle est ABSENTE si le statut est')
w('    "NON LUE (plancher, LD-16)".')
w('')
w('  verifie %d/%d groupes, %d contre-exemple.' % (len(groupes) - len(contre), len(groupes), len(contre)))
for e, g, st, p in groupes:
    w('    %-9s %-42s %-26s %s' % (e, g[-42:], st, 'EMISE' if p else 'ABSENTE'))
w('')
w('=========================================================')
w('2. LE PERIMETRE, ET LES DEUX COMPTES QU IL FAUT DISTINGUER')
w('=========================================================')
w('')
w('  depot 9bis, cles de reference ... %s' % ' '.join(sorted(DEP['reference'].keys())))
w('  exemptions declarees ............ %s' % EXEMPT)
w('')
w('  feuilles du JSON de PRE-VOL ..................... %d' % len(M1))
w('  perimetre au PRE-VOL ............................ %d' % len(perim))
w('  **perimetre au RUN** ............................ **%d**' % len(perim_run))
w('  perimetre de la REFERENCE deposee ............... %d' % len([k for k in REF if dans(k)]))
w('')
w('=========================================================')
w('3. LES QUATRE CLASSES')
w('=========================================================')
w('')
w('  PREDITES IDENTIQUES ....... %d' % len(identiques))
w('  EXEMPTES .................. %d' % len(exemptes))
w('  NON PREDITES .............. %d%s' % (len(mordantes), '' if EL is not None else '   (HERITEES de la v2 ; jambe (2) NON JOUEE)'))
w('  PREDITES ABSENTES ......... %d' % len(absentes))
w('  ------------------------------')
w('  perimetre au pre-vol ...... %d' % len(perim))
w('  moins les absentes ........ %d = perimetre au RUN' % len(perim_run))
w('')
w('STABILITE SUR MA MACHINE (jambe 1) : %d feuilles different entre les deux' % len(instables))
w('pre-vols, toutes exemptees (durees) :')
for k in instables:
    w('    %s' % k)
w('')
w('PREDITES ABSENTES -- emises au pre-vol, ABSENTES au run :')
for k in absentes:
    st = k.rsplit('/', 1)[0] + '/statut'
    w('    %s' % k)
    w('       pre-vol : statut %r -> emise' % M1.get(st))
    w('       run     : statut %r -> ABSENTE' % REF.get(st))
w('')
w('EXEMPTES :')
for k in exemptes:
    w('    %s' % k)
w('')
w('NON PREDITES :')
for k in mordantes:
    w('    %-46s  %s' % (k, ('%s pas' % pas(M1[k], EL[k])) if EL is not None else 'heritee v2 (libm), a confirmer'))
w('')
w('PREDITES IDENTIQUES : les %d autres. Elles se comparent AU BIT a' % len(identiques))
w('la reference deposee ; tout ecart -> NON CONCLUANT D INSTRUMENT')
w('avant toute lecture. Enumeration complete en annexe A.')
w('')
w('=========================================================')
w('4. CE QUE CETTE ENUMERATION NE FAIT PAS')
w('=========================================================')
w('')
w('Elle ne prend aucun numero (E18) et ne depose rien -- elle est LA')
w('PIECE A DEPOSER. Elle ne predit aucune VALEUR : le pre-vol est un')
w('factice (N-62), il fournit la LISTE des cles et leur regime, les')
w('valeurs viennent de la reference. Elle ne predit rien hors')
w('perimetre. L issue N-70 (a)(b)(c) est tranchee par le gel v7 ((c),')
w('tolerance en ulp pour les cles EXPOSEE-LIBM) : sous ce regime les')
w('%d cles NON PREDITES se comparent a tolerance, pas au bit.' % len(mordantes))
w('')
w('=========================================================')
w('ANNEXE A -- LES %d CLES PREDITES IDENTIQUES' % len(identiques))
w('=========================================================')
w('')
for k in identiques:
    w('  %s' % k)
w('')
w('-- FIN enumeration_cles_prevol_N70_machine2_v3 --')
txt = '\n'.join(L) + '\n'
assert all(ord(c) < 128 for c in txt) and '\r' not in txt
assert not contre, 'la regle d emission a un contre-exemple : %s' % contre
open(OUT, 'w', encoding='ascii', newline='\n').write(txt)
print('N-70 v3 : %s ; perimetre pre-vol %d, run %d ; identiques %d, exemptes %d, non predites %d, absentes %d ; instables %d ; jambe 2 %s'
      % (os.path.basename(OUT), len(perim), len(perim_run), len(identiques), len(exemptes), len(mordantes), len(absentes), len(instables),
         'JOUEE' if EL is not None else 'NON JOUEE'))
