#!/usr/bin/env python3
# -*- coding: ascii -*-
"""extraction_e33_e36_machine1_v2.py -- dossier de contresignature, v2.

Repond a : note_machine2_contresignature_E33_E36_v1.md (E34 refuse pour
ambiguite du ratio r ; correctif en forme executable, lecture A). PB-1 :
la v1 (instrument, log, brouillon) reste intacte.

Ce que fait la v2 :
  1. extrait les cinq blocs de l'acte (memes ancres que la v1) ;
  2. VERROUILLE les quatre blocs non touches sur leurs empreintes
     CONTRESIGNEES (clause l.170 de la note : les signatures E33/E35/E36
     valent telles quelles si les empreintes ne bougent pas ; l'amendement
     E34 signe avec le texte corrige, appariement non defait) ;
  3. extrait PAR STRUCTURE la forme proposee de la note machine 2, la
     depouille de son habillage ("..." et guillemets) ;
  4. COMPOSE le bloc E34_TEXTE_v2 : suite de mots de l'acte, le segment
     'et le RESIDU ... r/(1-r))' substitue par les mots de la forme --
     garde d'unicite du segment, garde MOT A MOT entre la forme extraite
     et le segment insere, re-pliage deterministe DECLARE (indent 2,
     largeur 72, coupure aux espaces, glouton) ; jamais retape ;
  5. test negatif : une mutation d'un mot de la forme -> la garde MORD ;
  6. assemble le brouillon delta 81 v2 ; log auto-empreinte (N-61).
Machine 2 re-execute la meme composition sur SES copies : memes octets,
puis signature unique couvrant E34_TEXTE_v2 + E34_amendement.
"""
import hashlib, unicodedata

ACTE = "journal_delta_80_acte_M17_v2.md"
EMPREINTE_ACTE = "a2b80c149d6a05bc"
NOTE_M2 = "note_machine2_contresignature_E33_E36_v1.md"
EMPREINTE_NOTE_M2 = "f9de93f16c5382ed"      # copie recue machine 1
LOG = "extraction_e33_e36_machine1_v2.log"
DELTA = "journal_delta_81_contresignature_E33_E36_v2.md"

CONTRESIGNEES = {                             # note m2, section 1-2
    "E33": "076e110c6a0a53c7",
    "E34_amendement": "5b16b328a1e843fd",
    "E35": "febc6ef278392136",
    "E36": "6d808620ab1df171",
}
E34_TEXTE_V1 = "cbf046e533c2c94d"             # concorde mais NON SIGNE

ANCRES = [
    ("E33",            "80.2 E33", "  TEXTE :", "\n  FONDEMENT"),
    ("E34_texte",      "80.3 E34", "  TEXTE :", "\n  FONDEMENT"),
    ("E34_amendement", "80.3 E34", "  AMENDEMENT AU TEXTE", "\n  Regle M15"),
    ("E35",            "80.4 E35", "  TEXTE PROPOSE", "\n  FONDEMENT"),
    ("E36",            "80.5 E36", "  TEXTE :", "\n  FONDEMENT"),
]

SEGMENT_ANCIEN = ("et le RESIDU estime par le ratio mesure r"
                  " (residu = pas x r/(1-r))")

def convention_B(texte):
    return hashlib.sha256(
        unicodedata.normalize("NFC", texte).encode("utf-8")).hexdigest()[:16]

def lire(chemin, attendu):
    brut = open(chemin, "rb").read()
    src = unicodedata.normalize(
        "NFC", brut.decode().replace("\r\n", "\n").replace("\r", "\n"))
    e = hashlib.sha256(src.encode()).hexdigest()[:16]
    assert e == attendu, "custody %s : %s != %s" % (chemin, e, attendu)
    return src

def extraire(src):
    blocs = {}
    for nom, a_sec, a_deb, a_fin in ANCRES:
        assert src.count(a_sec) == 1, a_sec
        i_sec = src.index(a_sec)
        section = src[i_sec:src.index("\n80.", i_sec + 1)]
        assert section.count(a_deb) == 1, (nom, a_deb)
        i_deb = section.index(a_deb)
        assert section.count(a_fin) >= 1, (nom, a_fin)
        i_f = section.index(a_fin, i_deb)
        bloc = section[i_deb:i_f]
        l0 = src[:i_sec + i_deb].count("\n") + 1
        l1 = src[:i_sec + i_f].count("\n") + 1
        blocs[nom] = {"nom": nom, "bloc": bloc, "l0": l0, "l1": l1,
                      "octets": len(bloc.encode()),
                      "empreinte": convention_B(bloc)}
    return blocs

def extraire_forme(note):
    marque = "forme proposee, a inserer dans le bloc E34_TEXTE :"
    assert note.count(marque) == 1, "marque de forme non unique"
    apres = note[note.index(marque) + len(marque):]
    lignes = []
    l_deb = note[:note.index(marque)].count("\n") + 2
    for l in apres.split("\n")[1:]:
        if l.strip().startswith("controle execute"):
            break
        if l.strip():
            lignes.append(l.strip())
    assert lignes, "forme vide"
    brut = " ".join(lignes)
    assert brut.startswith('"...') and brut.endswith('"'), \
        "habillage de forme inattendu : " + brut[:20]
    texte = brut[len('"...'):-1].strip()
    return texte, l_deb, l_deb + len(lignes) - 1

def replier(mots, indent="  ", largeur=72):
    """Re-pliage deterministe DECLARE : glouton, coupure aux espaces."""
    lignes, courante = [], indent
    for m in mots:
        essai = (courante + " " + m) if courante.strip() else (indent + m)
        if len(essai) > largeur and courante.strip():
            lignes.append(courante)
            courante = indent + m
        else:
            courante = essai
    if courante.strip():
        lignes.append(courante)
    return "\n".join(lignes)

def composer(bloc_acte, forme_texte):
    mots = bloc_acte.split()
    anciens = SEGMENT_ANCIEN.split()
    nouveaux = forme_texte.split()
    # unicite du segment dans la suite de mots
    pos = [i for i in range(len(mots) - len(anciens) + 1)
           if mots[i:i + len(anciens)] == anciens]
    assert len(pos) == 1, "segment ancien : %d occurrences" % len(pos)
    i0 = pos[0]
    mots_v2 = mots[:i0] + nouveaux + mots[i0 + len(anciens):]
    # garde MOT A MOT : la forme inseree est exactement la forme extraite
    assert mots_v2[i0:i0 + len(nouveaux)] == nouveaux
    return replier(mots_v2), mots, mots_v2, nouveaux

def main():
    acte = lire(ACTE, EMPREINTE_ACTE)
    note = lire(NOTE_M2, EMPREINTE_NOTE_M2)
    blocs = extraire(acte)

    # verrous : quatre blocs inchanges == empreintes contresignees
    for nom, att in sorted(CONTRESIGNEES.items()):
        assert blocs[nom]["empreinte"] == att, \
            "VERROU %s : %s != %s" % (nom, blocs[nom]["empreinte"], att)
    assert blocs["E34_texte"]["empreinte"] == E34_TEXTE_V1

    forme, f_l0, f_l1 = extraire_forme(note)
    bloc_v2, mots_v1, mots_v2, nouveaux = composer(
        blocs["E34_texte"]["bloc"], forme)
    e_v2 = convention_B(bloc_v2)

    # test negatif : un mot mute dans la forme -> la garde mot a mot MORD
    forme_mut = forme.replace("DERNIER", "DERNIERx")
    mordu = False
    try:
        composer(blocs["E34_texte"]["bloc"], forme_mut)
        _, _, mv2m, nvm = composer(blocs["E34_texte"]["bloc"], forme_mut)
        mordu = (convention_B(replier(mv2m)) != e_v2)
    except AssertionError:
        mordu = True
    assert mordu, "test negatif : mutation de la forme non detectee"

    lignes = [
        "COMPOSITION E34 v2 -- machine 1, 2026-08-24",
        "acte source : %s  %s  (custody PASSEE)" % (ACTE, EMPREINTE_ACTE),
        "note m2     : %s  %s  (custody PASSEE, copie recue)"
        % (NOTE_M2, EMPREINTE_NOTE_M2),
        "",
        "verrous contresignes (clause l.170) :",
    ]
    for nom, att in sorted(CONTRESIGNEES.items()):
        lignes.append("  %-15s %s == %s  TENU"
                      % (nom, blocs[nom]["empreinte"], att))
    lignes += [
        "  E34_texte v1    %s (concorde, NON SIGNE, remplace ici)"
        % E34_TEXTE_V1,
        "",
        "forme machine 2 extraite : note l.%d-%d, %d mots" % (
            f_l0, f_l1, len(nouveaux)),
        "segment substitue : 1 occurrence (unicite asseree)",
        "bloc E34_TEXTE_v2 : %d o, %d mots (v1 : %d), empreinte %s" % (
            len(bloc_v2.encode()), len(mots_v2), len(mots_v1), e_v2),
        "re-pliage declare : glouton, indent 2, largeur 72,"
        " coupure aux espaces",
        "garde mot a mot : forme inseree == forme extraite, PASSEE",
        "test negatif : mutation d'un mot de la forme -> MORD",
        "",
        "comptes : 5 blocs extraits + 1 compose + 0 echoues",
    ]
    contenu_log = "\n".join(lignes) + "\n"
    open(LOG, "w", newline="\n").write(contenu_log)
    relu = open(LOG, "rb").read().decode()
    e_log = convention_B(relu)
    with open(LOG, "a", newline="\n") as f:
        f.write("EMPREINTE (convention B, contenu jusqu'a la ligne"
                " precedente incluse) : %s\n" % e_log)
    print(contenu_log)
    print("log auto-empreinte (N-61) :", e_log)

    def cadre_signe(nom, b):
        return ("  Source : acte 80 v2 (%s), l.%d-%d, %d octets.\n"
                "  Empreinte du bloc (convention B) : %s\n"
                "  ----- BLOC %s (verbatim, ne pas editer) -----\n"
                "%s\n"
                "  ----- FIN BLOC %s -----\n"
                "  CONTRESIGNE (note %s, empreinte re-derivee concordante)"
                " --\n  la signature vaut telle quelle, empreinte"
                " inchangee (clause l.170).\n"
                % (EMPREINTE_ACTE, b["l0"], b["l1"], b["octets"],
                   b["empreinte"], nom, b["bloc"], nom, EMPREINTE_NOTE_M2))

    d = blocs
    corps = ("""JOURNAL DELTA 81 -- CONTRESIGNATURE DES TEXTES E33..E36 -- VERSION 2
(redaction machine 1, contresignatures machine 2, depot operateur,
2026-08-24) -- BROUILLON : le depot suit la signature E34
=======================================================================
Repond a : note_machine2_contresignature_E33_E36_v1.md """
+ EMPREINTE_NOTE_M2 + """
(TROIS SIGNEES -- E33, E35, E36 -- au bit et par spans derives ; E34
REFUSEE : le ratio r du residu etait resolu differemment par deux
implementations, en silence -- E29 applique a sa propre lettre. Le
correctif machine 2, lecture A, est insere ICI au mot pres). Remplace
le brouillon v1 53b3485b3e66715e (non edite, PB-1). S'insere apres le
delta 80 (a2b80c149d6a05bc). Numero pris A L'ACTE au depot (66.5.c).
Acte de CLASSE B (delta 71).

81.1 OBJET ET METHODE (v2)
  Quatre blocs INCHANGES, verrouilles par l'instrument sur leurs
  empreintes contresignees (clause l.170 de la note : les signatures
  E33/E35/E36 valent telles quelles ; l'amendement E34 signe avec le
  texte corrige, appariement non defait). Le bloc E34_TEXTE_v2 est
  COMPOSE, jamais retape : suite de mots du bloc de l'acte, le segment
  'et le RESIDU ... r/(1-r))' substitue par les MOTS de la forme
  machine 2 extraite par structure de sa note (l.au log), garde mot a
  mot executee, re-pliage deterministe declare (glouton, indent 2,
  largeur 72, coupure aux espaces). Machine 2 re-execute la meme
  composition sur SES copies (memes octets), puis signe. Test negatif :
  une mutation d'un mot de la forme change l'empreinte composee, MORD.
  Instrument : extraction_e33_e36_machine1_v2.py (couple au pied,
  N-61).

81.2 E33 -- FRACTION DE LA SERIE P6 (gel 4.11-bis) -- SIGNE
""" + cadre_signe("E33", d["E33"]) + """
81.3 E34 -- STATIONNARITE eta DE Gamma_c (gel 4.7) -- TEXTE v2
  (lecture A inscrite) + AMENDEMENT, une signature pour les deux
  Composition : acte l.%d-%d (bloc v1 %s, concorde non signe)
  + forme machine 2 (note %s, span au log de l'instrument).
  Empreinte du bloc compose : %s
  ----- BLOC E34_TEXTE_v2 (compose, ne pas editer) -----
%s
  ----- FIN BLOC E34_TEXTE_v2 -----
""" % (d["E34_texte"]["l0"], d["E34_texte"]["l1"], E34_TEXTE_V1,
       EMPREINTE_NOTE_M2, e_v2, bloc_v2) + """
  Source amendement : acte 80 v2 (""" + EMPREINTE_ACTE + """), l.%d-%d,
  %d octets. Empreinte : %s
  ----- BLOC E34_AMENDEMENT (verbatim, ne pas editer) -----
%s
  ----- FIN BLOC E34_AMENDEMENT -----
""" % (d["E34_amendement"]["l0"], d["E34_amendement"]["l1"],
       d["E34_amendement"]["octets"], d["E34_amendement"]["empreinte"],
       d["E34_amendement"]["bloc"]) + """
  CONTRESIGNATURE machine 2 (une signature, les deux blocs : empreintes
  re-derivees de SA composition et de SA copie, puis signature) :
  E34_TEXTE_v2 = ................  E34_AMENDEMENT = ................
  signe : ......
  DEFAUT DE L'ACTE, DECLARE (inchange depuis la v1, exact selon la
  note, numero a prendre machine 2) : quatre lignes de fondement
  echouees entre l'amendement et EFFET SCRIPT (acte l.77-80, 266 o,
  empreinte 151063c2614891f9), NON SIGNEES, lues comme fondement.

81.4 E35 -- LECTURE DES OCCUPATIONS DE LA GRAINE (gel 4.4) -- SIGNE
  La signature a transforme le TEXTE PROPOSE en texte INSCRIT.
""" + cadre_signe("E35", d["E35"]) + """
81.5 E36 -- EX AEQUO EXACT DANS UN RANG (section 8) -- SIGNE
""" + cadre_signe("E36", d["E36"]) + """
81.6 EFFET
  E33, E35, E36 : OPPOSABLES des le depot (signatures portees par la
  note """ + EMPREINTE_NOTE_M2 + """ et la clause l.170). E34 :
  opposable a la signature du bloc compose ; jusque-la sa cle reste a
  None et la garde D-S4 continue d'arreter -- le refus etait prevu par
  le dispositif, rien ne casse, un tour se paie. Inscription au gel PAR
  REFERENCE (PB-1) ; les cinq ancres du script s'inscrivent ensemble a
  la contre-certification, apres la v9.

PIECES (convention B ; detenteurs declares)
  acte : journal_delta_80_acte_M17_v2.md a2b80c149d6a05bc 18049 o
  (depose, numero 80, commit d761523) ; note de contresignature
  machine 2 """ + EMPREINTE_NOTE_M2 + """ 9527 o + log fbdaf54b0c888d9f
  2746 o (detenteur machine 2, copies recues) ; instrument v2
  (detenteur machine 1, JOINT) : extraction_e33_e36_machine1_v2.py /
  .log ; v1 : 53b3485b3e66715e (brouillon, depasse) ; patron : delta 79
  a5175671f93dfaf9.

-- FIN journal_delta_81_contresignature_E33_E36_v2 (brouillon) --
""")
    open(DELTA, "w", newline="\n").write(corps)
    print("brouillon v2 assemble :", DELTA)

if __name__ == "__main__":
    main()
