#!/usr/bin/env python3
# patch_gel_m15_v3_to_v4.py -- machine 1, 2026-08-09 (delta 53)
# Gel v4 HERITAGE = gel v3 (e41f4da3685e6d1b) + corrections prescrites
# (N-13 : un mot ; N-15 : le chiffre aux LIMITATIONS) + section PORTAGE
# (definition E29 + N-13 + N-15, extraits BYTE-VERBATIM des sources).
# Rejouable sur BOCAL4 : sources par nom dans CWD, empreintes asserties,
# patchs assertes (count == 1, sinon sys.exit), aucune re-frappe.
import hashlib, sys, unicodedata

def die(msg):
    print("ECHEC :", msg); sys.exit(1)

def lis(nom, sha16):
    b = open(nom, 'rb').read()
    h = hashlib.sha256(b).hexdigest()[:16]
    if h != sha16: die(f"{nom} : empreinte {h} != {sha16}")
    print(f"source OK  {nom}  {h}  {len(b)} octets")
    return b.decode('utf-8')

def patch(src, ancien, nouveau, nom):
    n = src.count(ancien)
    if n != 1: die(f"patch {nom} : ancre presente {n} fois (exige 1)")
    print(f"patch OK   {nom}")
    return src.replace(ancien, nouveau)

def extrait(src, debut, fin, nom):
    i = src.find(debut)
    if i < 0: die(f"extrait {nom} : marqueur de debut absent")
    j = src.find(fin, i)
    if j < 0: die(f"extrait {nom} : marqueur de fin absent")
    if src.find(debut, i + 1) >= 0: die(f"extrait {nom} : debut non unique")
    bloc = src[i:j]
    print(f"extrait OK {nom}  ({len(bloc)} car., "
          f"'{bloc.splitlines()[0][:44]}...')")
    return bloc

gel  = lis('m15_pre_enregistrement_v3.md',    'e41f4da3685e6d1b')
cert = lis('m15_certification_croisee_v3.md', '8081a0325e0821de')
err  = lis('m15_erratum_grossiere_mordue_v3.md', '16c6d86e389da2a9')

TERM = "\n=== FIN DU GEL M15 ===\n"
if gel.count(TERM) != 1: die("invariant de cloture v3 : terminateur != 1")

# ---- extractions byte-verbatim -------------------------------------
e29 = extrait(err,  '3. CORRECTION', '4. MOTIVATION', 'E29.3')
n13 = extrait(cert, '### N-13', '### N-14', 'N-13')
n15 = extrait(cert, '### N-15', '\n---\n',  'N-15')
for nom, bloc in (('E29.3', e29), ('N-13', n13), ('N-15', n15)):
    if '### N-14' in bloc: die(f"{nom} : N-14 present dans l'extrait")
    if TERM.strip() in bloc: die(f"{nom} : terminateur dans l'extrait")
for temoin in ('grossiere mordue', 'b_fond = 3/96'):
    if temoin not in e29: die(f"E29.3 : temoin '{temoin}' absent")

# ---- patch A/B : en-tete (convention de bloc, version) -------------
gel = patch(gel,
    "bloc ASCII, canonique NFC+LF ;",
    "bloc ASCII hors PORTAGE v4 (extraits NFC verbatim de source), "
    "canonique NFC+LF ;",
    "A en-tete convention")
gel = patch(gel,
    "version v3, machine 1, 2026-08-07)",
    "version v4 HERITAGE, machine 1, 2026-08-09)",
    "B en-tete version")

# ---- patch C : N-13, le mot (la v3 presentait la marge NORMALISEE
#      comme la lecture machine 2 ; la v2 appliquait la marge ABSOLUE)
i = gel.find("(Lecture argmin")
if i < 0: die("patch C : parenthese argmin absente")
j = gel.find(")", i)
ancien_C = gel[i:j + 1]
gel = patch(gel, ancien_C,
    "(Lecture argmin ; N-13 : la certification v2 de machine 2 "
    "appliquait la marge ABSOLUE -- meme mot, pas la meme regle ; "
    "ensemble F identique, six points d'assignation divergents)",
    "C mot N-13")

# ---- patch D : N-15, le chiffre aux LIMITATIONS --------------------
gel = patch(gel,
    "moins profonde que le seuil (COURBURES",
    "moins profonde que le seuil -- CHIFFRE N-15 : marge 1.117 contre "
    "1 sur le seul indice mesure, P(n_disc >= 1) = 0.399 sous q_L "
    "local, controle positif du gel a 1.025 ; voir PORTAGE P4.3 -- "
    "(COURBURES",
    "D chiffre N-15")

# ---- patch E : section PORTAGE avant le terminateur ----------------
portage = (
    "PORTAGE v4 (HERITAGE)\n"
    "  Actes : delta 52.6 (prescription arbitree), delta 53\n"
    "  (execution) ; contre-signature du delta 52 : ae7b7015bb166b57.\n"
    "  La v4 = la v3 (e41f4da3685e6d1b) + les patchs du present acte\n"
    "  (script patch_gel_m15_v3_to_v4.py, empreinte au delta 53) :\n"
    "  deux lignes d'en-tete, le mot N-13, le chiffre N-15 aux\n"
    "  LIMITATIONS, la presente section. Sources extraites\n"
    "  BYTE-VERBATIM, jamais re-frappees (regle 12 ; 49.5) :\n"
    "  definition E29 depuis m15_erratum_grossiere_mordue_v3.md\n"
    "  (16c6d86e389da2a9, sect. 3) ; N-13 et N-15 depuis\n"
    "  m15_certification_croisee_v3.md (8081a0325e0821de, sect. 5,\n"
    "  NFC accentue). N-14 n'est PAS porte ici : sa destination est\n"
    "  la regle de comptage du script et l'artefact du run\n"
    "  (prescription E29 sect. 7 : portage = definition + N-13 +\n"
    "  N-15). Les blocs suivants font foi par leur source ; la\n"
    "  presente section ne les commente pas.\n"
    "\n"
    "-- P4.1 DEFINITION \"grossiere mordue\" (erratum E29, sect. 3,\n"
    "   verbatim, ASCII) :\n"
    "<<<DEBUT EXTRAIT E29.3>>>\n" + e29 +
    "<<<FIN EXTRAIT E29.3>>>\n"
    "\n"
    "-- P4.2 N-13 (certification croisee v3, sect. 5, verbatim, NFC) :\n"
    "<<<DEBUT EXTRAIT N-13>>>\n" + n13 +
    "<<<FIN EXTRAIT N-13>>>\n"
    "\n"
    "-- P4.3 N-15 (certification croisee v3, sect. 5, verbatim, NFC) :\n"
    "<<<DEBUT EXTRAIT N-15>>>\n" + n15 +
    "<<<FIN EXTRAIT N-15>>>\n")
for m in ("<<<DEBUT EXTRAIT", "<<<FIN EXTRAIT", "PORTAGE v4 (HERITAGE)"):
    if m in gel: die(f"portage : marqueur '{m}' deja present en v3")
gel = patch(gel, TERM, "\n" + portage + TERM, "E insertion PORTAGE")

# ---- invariants de sortie ------------------------------------------
if gel.count(TERM) != 1: die("invariant de cloture v4 : terminateur != 1")
for m in ("<<<DEBUT EXTRAIT E29.3>>>", "<<<FIN EXTRAIT E29.3>>>",
          "<<<DEBUT EXTRAIT N-13>>>", "<<<FIN EXTRAIT N-13>>>",
          "<<<DEBUT EXTRAIT N-15>>>", "<<<FIN EXTRAIT N-15>>>"):
    if gel.count(m) != 1: die(f"marqueur '{m}' : count != 1")
if not unicodedata.is_normalized('NFC', gel): die("v4 non NFC")
if not gel.endswith("\n") or gel.endswith("\n\n"): die("LF final non unique")

b = gel.encode('utf-8')
open('m15_pre_enregistrement_v4.md', 'wb').write(b)
print(f"\nGEL v4 ECRIT  m15_pre_enregistrement_v4.md")
print(f"  {len(b)} octets | sha16 {hashlib.sha256(b).hexdigest()[:16]}")
print(f"  sha256 complet {hashlib.sha256(b).hexdigest()}")
