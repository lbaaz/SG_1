# RELEVE DE CLOTURE DU DELTA 90 -- machine 1, v1, 12/09/2026 (nuit). Classe 1.
# releve 9/9 controles PASSENT ; 101 empreintes citees : 97 au registre, 0 au poste, 1 zip, 3 valeurs, 0 non resolues. LA RESERVE DE MA CERTIFICATION EST CLOSE. Rien n'est edite (PB-1) ; aucun numero de serie pris.

## 0. EN TROIS PHRASES

Le lot de depot 27e15bfbb99c661c est recu 6/6 au canon ; son erratum (le diff retire 12 lignes,
pas 11 -- la ligne FIN avalee par un filtre de prefixe, D-CERT-5 rejouee) est pris tel quel.
Sur un clone frais qui n'a jamais servi a pousser, HEAD e68341f au-dessus de d037d21, les 212
lignes du manifeste de depot v2 (672b06b2686d3a82) sont retrouvees AU BIT (canon B et brut),
l'acte depose journal/journal_delta_90_constante_A_v2.md resout a 11f86226cf4aa612, l'acte v2
certifie, plafond 90, 676 fichiers suivis. Le perimetre v2 rejoue avec ce clone rend 101 empreintes citees : 97 au registre, 0 au poste, 1 zip, 3 valeurs, 0 non resolues --
les 18 empreintes que je ne detenais pas resolvent desormais au registre, comme H1 le disait.

## 1. LE RELEVE (feuille releve_depot_delta90_machine1_v1.py, clone et manifeste en arguments)

[PASSE] HEAD du clone frais == e68341f                             e68341f
      [PASSE] le manifeste de depot v2 resout a 672b06b2686d3a82         672b06b2686d3a82
      [PASSE] 212 lignes de depot, compte declare avant de compter       212
      [PASSE] retrouvees + absentes + ecarts == 212                      212 + 0 + 0
      [PASSE] 212/212 retrouvees AU BIT (canon B et brut)                212
      [PASSE] toutes les lignes de depot sont des fichiers SUIVIS par gi 676 suivis
      [PASSE] l acte depose est AU BIT l acte v2 certifie (11f86226cf4aa 11f86226cf4aa612
      [PASSE] plafond du registre == 90, un seul fichier delta_90        plafond 90
      [PASSE] 676 fichiers suivis (464 + 212)                            676
    
    =====================================================================
    BILAN RELEVE : 9/9 controles PASSENT
    =====================================================================

## 2. LE PERIMETRE v2 REJOUE AVEC LE NOUVEAU HEAD (feuille 3c916ed41e85f3d7 de machine 2)

    BILAN PERIMETRE : 16/18 controles PASSENT
    101 empreintes citees : 97 au registre, 0 au poste, 1 zip, 3 valeurs, 0 non resolues
    DEPOT : 3 pieces (journal 3) ; manifeste MANIFEST_DEPOT_delta90_machine2_v2.txt 17914629c3f82d27
    Les deux MORD sont attendus et nommes, pas des defauts : la feuille asserte l'etat
    d'AVANT depot (plafond 89, aucun delta_90, aucun chemin cible deja au registre) ; rejouee
    APRES depot elle mord exactement la ou le depot a eu lieu, et ne derive plus que les 3
    pieces de son propre lot qu'elle ne cherche jamais au registre. Ce qui compte est la ligne
    des citations : 101/101 resolvent, 97 au registre, 0 non resolue -- les 18 empreintes a
    detention unique sont desormais au registre. Le compte "101 au registre" de l'etape se lit
    "101 resolues" : 97 au registre, 3 valeurs declarees, 1 ZIP declare.

## 3. CE QUE CELA CLOT, ET CE QUE CELA NE CLOT PAS

Clos : la reserve de detention de ma certification (18 empreintes, 38 lignes) -- tout est
verifiable par quiconque sur clone frais ; le chantier de l'acte constante A (delta 90) ;
la journee du 12/09. Le registre porte la chaine entiere : gel courant v5, temoin v11 et son
erratum 7 (i), instrument v8, N-70 v2, les pre-vols, la tenaille, le geste (2), les tours.
Non clos, et a l'operateur : les numeros de serie (E18) des errata (1)(2)(3), du fait de forme
de (v), de D-ACA-1..7, D-G2-1..4, D-I-1..9, D-v5-1 ; les decisions (i), (ii), (v), (vii) ; l'arbitrage
du 29/08 (marge du volet A ou marge cote T) ; la revue (X) du 28/09 avec ses huit candidates.
La mesure de la constante A n'est pas faite : le pre-vol rend branche 4 et aucun run n'est
lance ; aucun delta n'est recommande.

## 4. PIECES DE CE LOT

    releve_depot_delta90_machine1_v1.py / .log       le releve, 9/9 controles PASSENT
    rejeu_perimetre_v2_HEAD_e68341f_machine1.log     le perimetre v2 au nouveau HEAD

-- FIN note_machine1_releve_cloture_delta90_v1 --
