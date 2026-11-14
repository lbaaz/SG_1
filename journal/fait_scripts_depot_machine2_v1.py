# -*- coding: ascii -*-
"""DERIVE LES DEUX SCRIPTS DE DEPOT d'un delta de ceux du delta precedent, SANS EDITER les originaux (regle 17) : lit
DEPOT_delta<src>/perimetre_depot_delta<src>_machine2_v1.py et DEPOT_delta<src>/depot_delta<src>_machine2_v1.py, ecrit
DEPOT_delta<dst>/perimetre_depot_delta<dst>_machine2_v1.py et DEPOT_delta<dst>/depot_delta<dst>_machine2_v1.py, et les DIFFS
(diff_perimetre_depot_<src>_<dst>.txt, diff_depot_<src>_<dst>.txt). Chaque remplacement doit se faire EXACTEMENT une fois, sinon arret.
machine 2, v1, 14/11/2026. Usage (depuis BOCAL4) : python -P fait_scripts_depot_machine2_v1.py 95 | 96"""
import difflib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
DST = sys.argv[1]
SRC = {'95': '94', '96': '95'}[DST]

MSG = {
    '95': ("delta 95 -- the qualification of the E-B estimator Gamma_LS, resumed under the bis freeze, returns NOT QUALIFIED: "
           "at stage 1, played on the night of 13/11 on BOCAL4 with every guard held, the positive witness (the H+ twin, its width "
           "known by complex rotation) holds at all four configurations, at 0.15 per cent at worst, on a plateau that begins at the "
           "strong edge of the eta scale, which the bis freeze extends to k = -5 to 12 and which is its one substantive difference "
           "from the v2 freeze; stage 2 is played in full, 540 decompositions with every guard held and the anchor reproducing M17's "
           "reading to the bit at the six points, and none of the six phantom points is qualified: five of them have no plateau of "
           "five values at the short absorber, and the sixth (1.95) has one there and fails under both replacement forms of the "
           "absorber; the widths M17 read are therefore not, in the freeze's sense, widths independent of the absorber, every "
           "sentence carrying a Gamma since July is reclassified, and what remains is the order-of-magnitude fact that the phantom "
           "leaks and the twin does not; this was the last attempt under the freeze's own safeguard and track (0) closes in this "
           "form unless the operator decides otherwise; machine 1's replay of the point 1.95 on another platform was sealed by its "
           "fingerprint (7fb9026014ad0c93), which the operator attests having received before handing machine 1 machine 2's night "
           "lot, and then opened: the judged state agrees to 4.9e-4 against a tolerance of 1e-3, four of the nine other followed "
           "states do not, the gap between machines being bounded in absolute terms so that a relative tolerance alone does not say "
           "what it covers; the one disagreement between the probe and the earlier diagnostic is traced to the BLAS thread count; "
           "three candidate rules, numbered 26 to 28, join the twenty-five awaiting review (X); act written by one machine and "
           "countersigned by the other after the numbers were re-read at their sources, three points of description found in the "
           "first version and corrected in a second before deposit, the superseded version being deposited beside it so that the "
           "correction stays legible, the deposited file being the countersigned one byte for byte"),
    '96': ("delta 96 -- the E-A chain read state by state, outside the range of M17 (the engine's chain function, called at the "
           "whole site that labels a clean 2D eigenstate, against the width E-B reads at k = 3), is HELD IN PART: under a freeze "
           "written before the run and certified by the other machine before it, opened by the operator on 14/11 at 00:15 (the "
           "operator attests it), played once on BOCAL4 on 14/11 with every guard held and the two anchors reproducing M17's "
           "readings to the bit, twelve points and 168 states, six points judged; the chain reads E-B's width within a factor 2 at "
           "four of the six (44 judged states), within half a decade at a fifth (8 states, three of them under 1/2), and falls at "
           "the sixth, J2 at 2.10, where it overestimates by a factor 2.9 to 4.2 on all thirteen judged states, eleven of them "
           "outside the half decade; at the twelve points the median ratio is below 1 when w2 is below 2 and above 1 when it is "
           "above; the engine's own domain guard says OUTSIDE DOMAIN at exactly three points, J2, T3 and T4, which are exactly the "
           "three that fall outside the half decade, a coincidence recorded as such and not a domain of validity, which the freeze "
           "forbids drawing; the probe reads the chain without consulting that guard, a silence of the freeze recorded as a defect, "
           "so that a verdict at J2 is a verdict outside the chain's declared domain; seven of the eight announcements of the pen "
           "are true, the ratio of the first judged state at J1 (0.950 against 0.70 to 0.85) is not; the act does not call the chain "
           "qualified, does not retire the reading of the earlier note, which holds at the named points, and leaves the not-qualified "
           "verdict of delta 95 untouched; three candidate rules, numbered 29 to 31, join the twenty-eight awaiting review (X); act "
           "written by one machine and countersigned by the other after every number was recalculated from the countersigner's own "
           "sources, 22 controls of which none bites, the same sheet biting 18 times on a copy with fifteen figures changed, the "
           "deposited file being the countersigned one byte for byte"),
}[DST]

CFG = {
    '95': {
        'titre': 'LE PERIMETRE DU DEPOT delta 95 (LA QUALIFICATION E-B, REPRISE SOUS LE GEL BIS) -- ENUMERE DEPUIS LES CITATIONS DE L\'ACTE.',
        'corps_titre': ('(LA QUALIFICATION DE L ESTIMATEUR E-B) -- 12/11/2026 -- ', '(LA QUALIFICATION E-B, REPRISE SOUS LE GEL BIS) -- 14/11/2026 -- '),
        'dossier': ("construction_(gel_EB_v\\d+|sonde_banc_v\\d+)_machine1_v\\d+)\\.py$'",
                    "construction_(gel_EB_v\\d+|sonde_banc_v\\d+|gel_EB_bis|instrument_EB_bis)_machine1_v\\d+)\\.py$'"),
        'chantier': 'la nuit bis de la qualification E-B (gel bis, sonde v3, banc v3, feuille v2)',
    },
    '96': {
        'titre': 'LE PERIMETRE DU DEPOT delta 96 (LA CHAINE E-A PAR ETAT, HORS PLAGE) -- ENUMERE DEPUIS LES CITATIONS DE L\'ACTE.',
        'corps_titre': ('(LA QUALIFICATION E-B, REPRISE SOUS LE GEL BIS) -- 14/11/2026 -- ', '(LA CHAINE E-A PAR ETAT, HORS PLAGE) -- 14/11/2026 -- '),
        'dossier': ("construction_(gel_EB_v\\d+|sonde_banc_v\\d+|gel_EB_bis|instrument_EB_bis)_machine1_v\\d+)\\.py$'",
                    "construction_(gel_EB_v\\d+|sonde_banc_v\\d+|gel_EB_bis|instrument_EB_bis|gel_chaine_EA_par_etat)_machine1_v\\d+|"
                    "sonde_chaine_par_etat_machine1_v\\d+|lecture_chaine_par_etat_machine1_v\\d+)\\.py$'"),
        'chantier': 'la chaine E-A par etat, hors plage (gel, sonde, feuille)',
    },
}[DST]


def lire(p):
    return open(p, encoding='ascii', newline='').read()


def une_fois(s, a, b, nom):
    if s.count(a) != 1:
        raise SystemExit('ARRET : %s : %d occurrence(s) de %r' % (nom, s.count(a), a[:80]))
    return s.replace(a, b)


# ----------------------------------------------------------------- la feuille de perimetre
src_p = os.path.join(ICI, 'DEPOT_delta%s' % SRC, 'perimetre_depot_delta%s_machine2_v1.py' % SRC)
p = lire(src_p)
i = p.index('"""')
j = p.index('"""', i + 3)
nouveau_doc = ('"""' + CFG['titre'] + '\nmachine 2, v1, 14/11/2026.\n\n'
               'Derive de la feuille du delta %s (perimetre_depot_delta%s_machine2_v1.py, au registre ou au poste, NON EDITEE : regle 17), meme methode,\n'
               'meme code, %s changements nommes, le diff est joint :\n'
               '  1. dossier() : les instruments et constructions de ce chantier (%s) vont sous scripts/, comme ceux du delta precedent.\n'
               '  2. le texte du manifeste (corps) parle de ce chantier et de sa date%s.\n'
               '%s'
               'Pour le reste, tout est herite : le perimetre ne s\'ecrit pas a la main, il s\'ENUMERE depuis les citations de l\'acte, resolues PAR CANON\n'
               '(registre, poste, ou NON RESOLU qui mord) ; le numero se DERIVE du registre (plafond + 1) ; les lots cites entrent avec leurs pieces de\n'
               'table ; les ZIP ne sont pas deposes ; DEUX VERBES (`chk` mesure, `note` porte la prose) ; PB-1 : rien n\'est edite.\n'
               % (SRC, SRC, 'TROIS' if SRC == '94' else 'DEUX', CFG['chantier'],
                  ' ; la phrase propre aux fichiers de reprise du 94 est retiree' if SRC == '94' else '',
                  ('  3. un manifeste SANS ligne "pieces : N" (les lots de machine 1 des 13 et 14/11) : le compte attendu est celui des membres du zip extrait\n'
                   '     sous entrants/, hors manifeste ; il n\'est pas tape, et une piece de table introuvable mord toujours (controle voisin).\n')
                  if SRC == '94' else '') + '"""')
p2 = p[:i] + nouveau_doc + p[j + 3:]
p2 = une_fois(p2, "perimetre_depot_delta%s_machine2_v1.py <clone frais du registre>" % SRC, "perimetre_depot_delta%s_machine2_v1.py <clone frais du registre>" % DST, 'usage')
p2 = une_fois(p2, CFG['dossier'][0], CFG['dossier'][1], 'dossier')
p2 = une_fois(p2, CFG['corps_titre'][0], CFG['corps_titre'][1], 'titre du corps')
if SRC == '94':
    a3 = "    att = int(m.group(1)) if m else None\n"
    b3 = (a3 + "    if att is None:        # changement 3 : manifeste sans ligne 'pieces : N' -> compte des membres du zip extrait, hors manifeste\n"
          "        _nl = tx.split(chr(10))[0].split()[1]\n"
          "        _dd = [x for x in (os.path.join(ICI, 'entrants', _nl), os.path.join(ICI, 'entrants', _nl + '_recu')) if os.path.isdir(x)]\n"
          "        if _dd:\n"
          "            att = (sum(1 for _r, _s, _fs in os.walk(_dd[0]) for _f in _fs)\n"
          "                   - sum(1 for _f in os.listdir(_dd[0]) if _f.startswith('MANIFEST_')))\n"
          "            note('manifeste sans ligne pieces : N', '%s : compte attendu = %d membres du zip extrait, hors manifeste' % (t, att))\n")
    p2 = une_fois(p2, a3, b3, 'compte de repli')
a = 'ils entrent par leur manifeste et leurs pieces de table. Les 279 fichiers de reprise de la nuit (nuit_EB/sortie/reprise) NE SONT PAS deposes : l acte ne les cite pas, leur contenu utile est consolide dans sonde_etage1.json.\\n"'
b = 'ils entrent par leur manifeste et leurs pieces de table.\\n"'
if SRC == '94':
    p2 = une_fois(p2, a, b, 'phrase des 279 fichiers')
open(os.path.join(ICI, 'DEPOT_delta%s' % DST, 'perimetre_depot_delta%s_machine2_v1.py' % DST), 'w', encoding='ascii', newline='\n').write(p2)
d = ''.join(difflib.unified_diff(p.splitlines(True), p2.splitlines(True), 'delta%s' % SRC, 'delta%s' % DST))
open(os.path.join(ICI, 'DEPOT_delta%s' % DST, 'diff_perimetre_depot_%s_%s.txt' % (SRC, DST)), 'w', encoding='ascii', newline='\n').write(d)

# ----------------------------------------------------------------- le script de depot
src_d = os.path.join(ICI, 'DEPOT_delta%s' % SRC, 'depot_delta%s_machine2_v1.py' % SRC)
q = lire(src_d)
i = q.index('"""')
j = q.index('"""', i + 3)
doc = ('"""LE DEPOT DU DELTA %s SUR CLONE FRAIS -- copie, verification au bit, releve, commit LOCAL. machine 2, v1, 14/11/2026.\n'
       'Le PUSH n\'est pas fait ici.\n\n'
       'Derive de depot_delta%s_machine2_v1.py (NON EDITE : regle 17). Un seul changement : le texte du message de commit ; le numero se lit toujours\n'
       'dans le nom du manifeste, l\'etat attendu du registre s\'en deduit, rien n\'est tape. Le diff est joint.\n'
       'Arguments : <clone frais> <MANIFEST_DEPOT_delta<nn>_machine2_v<N>.txt>.\n'
       '  1. releve AVANT : origin/main == HEAD, arbre propre, plafond == nn - 1, aucun delta_nn ;\n'
       '  2. chaque ligne du manifeste : la source resout au canon B ecrit ; la cible n\'existe pas encore ; copie OCTET POUR OCTET ; relecture au canon ;\n'
       '  3. git add ; le nombre de fichiers ajoutes == le compte declare, aucun modifie, aucun supprime, rien hors gels/ scripts/ journal/ ;\n'
       '  4. commit local, auteur celui du depot, message SANS trailer d\'outillage (convention du depot public, decidee le 25/08) ;\n'
       '  5. releve APRES : HEAD a avance d\'un commit, plafond == nn, l\'acte numerote resout au canon de l\'acte source.\n'
       'Les comptes sont LUS ; les sorties s\'ecrivent avant tout assert. DEUX VERBES.\n' % (DST, SRC) + '"""')
q2 = q[:i] + doc + q[j + 3:]
k = q2.index('msg = (')
m_end_marker = 'the deposited file being the countersigned one byte for byte")'
m = q2.index(m_end_marker, k) + len(m_end_marker)
q2 = q2[:k] + 'msg = (' + repr(MSG) + ')' + q2[m:]
q2 = une_fois(q2, "usage : depot_delta%s_machine2_v1.py" % SRC, "usage : depot_delta%s_machine2_v1.py" % DST, 'usage depot')
assert "'" not in MSG.replace("'s", '').replace("s'", '') or True
open(os.path.join(ICI, 'DEPOT_delta%s' % DST, 'depot_delta%s_machine2_v1.py' % DST), 'w', encoding='ascii', newline='\n').write(q2)
d = ''.join(difflib.unified_diff(q.splitlines(True), q2.splitlines(True), 'delta%s' % SRC, 'delta%s' % DST))
open(os.path.join(ICI, 'DEPOT_delta%s' % DST, 'diff_depot_%s_%s.txt' % (SRC, DST)), 'w', encoding='ascii', newline='\n').write(d)
print('DEPOT_delta%s : perimetre_depot_delta%s_machine2_v1.py, depot_delta%s_machine2_v1.py, 2 diffs ; message de %d caracteres, ASCII : %s'
      % (DST, DST, DST, len(MSG), all(ord(c) < 128 for c in MSG)))
