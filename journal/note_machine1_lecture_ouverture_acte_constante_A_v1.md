# NOTE MACHINE 1 -- LECTURE DU LOT MACHINE 2 "acte constante A v1" ET OUVERTURE DU CHANTIER DE L'ACTE (DELTA 90 ATTENDU)
# machine 1, v1, 12/09/2026. Classe 3. PB-1 : aucune piece recue n'est editee.
# Repond au lot lot_machine2_2026-09-12_acte_constante_A_v1 -- canon CALCULE au poste :
# e3b707c589e9d1d8 (le lot ne l'annonce pas ; a confirmer par machine 2 par sa ligne CANON).

## 0. EN QUATRE PHRASES

Lot recu et verifie 5/5 au canon (convention B), les deux .log CRLF au brut aussi. La
tenaille v2 est ACCORDEE sur sa structure et sur ses nombres re-derives depuis les valeurs
imprimees ; elle n'est PAS rejouee ici (ses entrees ne sont pas au poste). La decision (v)
redevient tranchable : SUIVI_campagne_2026-08-28b.md est RETROUVE, reconstruit depuis le
transcript du chat du 28/08 et AUTHENTIFIE PAR CANON (b6d13e6a1559e850, 5639 octets,
ASCII/LF) -- il est joint, octet pour octet. Deux defauts sont verses (un de machine 2, un
de machine 1) et la carte des classes du geste (2) doit etre re-etablie AU BIT avant l'acte.

## 1. GARDE DE RECEPTION (compte declare avant de compter : 5 ; le manifeste porte 5 lignes)

    verifiees 5 + absentes 0 + ecarts 0 == 5
    cbf120b4113bc8b1  DOSSIER_ARBITRAGE_constante_A_operateur_v1.md    brut identique
    9d9e949ed876424f  derivation_fenetre_delta_machine2_v2.py          brut identique
    d0c3ec95eeb9f4b8  derivation_fenetre_delta_machine2_v2.log         brut f64d6f41df5adf16 (CRLF), conforme au manifeste
    6e1409b06e887d97  relecture_nombres_acte_machine2_v1.py            brut identique
    484da81013182f02  relecture_nombres_acte_machine2_v1.log           brut f7a8edd1455e81b6 (CRLF), conforme au manifeste
    ASCII 5/5 ; le manifeste ne se porte pas lui-meme (verifie) ; canon calcule e3b707c589e9d1d8.
    Fait releve, sans consequence : le lot est arrive en pieces detachees, pas en ZIP ;
    l'interface n'a rien re-encode (les octets CRLF des deux .log ont traverse).

## 2. LA TENAILLE v2 -- CE QUE J'AI RE-DERIVE, CE QUE JE N'AI PAS REJOUE

Re-derive au poste depuis les nombres IMPRIMES du log (pas depuis les JSON, non detenus) :

    bits 3ef1660b5147653b -> 1.659260768e-05 (INF)                                   concorde
    delta'/0.68419170555697806 = 1.427322916e-05 ; delta'/0.75926589622204754 = 1.286193025e-05
                                                                                     concorde
    INF / 1.427322916e-05 = 1.1625 = borne haute de la dispersion e(delta')/e(delta_0)
      de la section 2 : coherent, le facteur conservateur au porteur est la dispersion maximale
    ecart 2.8027e-04 ; marge 4.1817e-02 ; rapport 149.2 ; delta'/INF 0.5886                concorde
    carte : m=1 x2.0836 / x1.8119 / x1.1975 ; m=2 x1.0418 puis VIDE des kT = 1.15 ; m=3 VIDE
                                                                                     concorde
    (alpha+2)(alpha+3) = 20, 130/9, 266/25 aux p = 4, 5, 7 ; la borne superieure m=1 portee
      par p=5 implique dispersion_lnA(5) = 2.3935e-06                                a relire au JSON alpha

Structure relue dans le .py : INF = max(borne(rm, True)) avec rm = ratios_json(pre) ; m1n et
m1l n'entrent que dans l'affichage `lect` ; la jambe de mutation (x3 et x0.5 sur les DEUX
JSON de machine 1 ; INF et porteur inchanges au bit ; lecture affichee deplacee) MESURE ce
que ma relecture du 12/09 avait seulement LU. Accord sans reserve : delta >= 1.659260768e-05,
porteur 7|1.73 aux quatre lectures, fenetre m=2/kT=1 x1.0418, porte inchangee (branche 4 des
deux cotes, le volet A n'ouvre que sur branche 5), aucun delta recommande.

NON REJOUE : derivation v2 et relecture v1 exigent m2_v8_prevol_temoin_resultats.json et son
journal, mes deux resultats_temoin_prevol (noyau, libm) et mon journal du 28/08 -- tous au
poste machine 2, aucun au mien (conteneur reinitialise) -- plus registre/runs/run_temoin_delta85
et run_alpha_delta85 (clonables). Le 21/21 et le 39/39 sont pris comme comptes de machine 2,
pas comme comptes de machine 1 : ils le deviendront au rejeu, avant l'acte.

D-ACA-1 (machine 2 ; forme ; non bloquant ; numero propose, a confirmer a l'acte) : section 2
de derivation v2, `chk('donc ratio = e/(C x plancher) est PROPORTIONNEL a delta', True, ...)`
-- la condition est le litteral True ; aucune issue ecrivable ne le fait mordre. C'est un
corollaire des sections 1 et 2 imprime sous la forme d'un controle, et il compte dans le
21/21 : le compte des controles qui peuvent mordre est 20. Regle de machine 2 elle-meme
(11/09). Correction : une v3 (PB-1 interdit l'edition de la v2), ou la declaration "21 lignes
dont 20 controles" a l'acte.
Remarque, pas un defaut : en section 7 les comptes attendus (6, 3, 2, 4) sont ecrits dans les
conditions APRES avoir ete lus sur les memes JSON (aiguille posee apres le compte) ; ce sont
des gels de non-regression, pas des mesures. Le controle qui mord est croise -- section 3.

## 3. SIX CELLULES AU BIT -- ACCORD, ET CE QUE CELA OUVRE CHEZ MACHINE 1

Accord sur le compte : six au bit dont quatre lues, trois au journal dont deux lues, les six
s'annulent contre le run libm (donc noyau). Le porteur 7|1.73 reste le seul point non lu qui
differe AU JOURNAL et le seul porteur de la borne ; AU BIT, 5|1.73 (non lue) differe aussi
(4.1e-09). L'erratum de cloture de machine 2 ("7|1.73 seul point NON LU qui differe") est
donc depasse au bit ; sa portee exacte est "au journal". L'erratum final a l'acte porte les
DEUX resolutions et nomme celle qu'il utilise.

Ce que cela ouvre chez moi : ma carte des classes du 12/09 (lot ca5456d3b11df0be) range
5|1.73 parmi les cellules "tenues par absorption, 0 basculement net" -- compte fait sur les
basculements de x1 aux flots de la paire du gel. Or un ecart de 4.1e-09 sur
ratio_seuil = e(dt2/2)/seuil_5_4 est l'ordre de grandeur d'UN ulp (1e-16 relatif) dans l'un
des flots qui entrent dans e, divise par e/x si e/x vaut 1e-7 a 1e-8 -- lecture, a verifier :
l'absorption aurait tenu pour l'ETAT (x1 a la paire), pas pour e. Ma carte a ete etablie a
deux resolutions (le journal pour e/seuil, les basculements de x1 pour l'absorption), alors
que mon propre diff feuille a feuille (diff_prevol_noyau_libm.py, 82 feuilles) portait deja
les ecarts fins : troisieme instance de la famille "compte au journal", de ma main.
Versee : D-ACA-2 (machine 1 ; numero propose).

Controle ecrivable, a jouer sur les JSON avant l'acte : aux trois cellules fines (4|2.27,
5|1.73, 5|2.80), comparer noyau contre libm les etats finaux (x1, x2) des flots dt2/2 et dt2/4
et champ_forces_empreinte. Issue qui mord : etats identiques ET e differents -> la classe se
definit sur e au bit, pas sur x1 a la paire ; etats differents -> "0 basculement net" etait
faux. Dans les deux cas la carte est re-etablie AU BIT depuis le diff deja fait, et le 9bis
entre machines compare a tolerance ou exempte (accorde, mesure par machine 2).

Piege de nom : tranche a ma plume, puisque les classes sont de la mienne (classe 3, aucune
piece contresignee touchee) -- plus de lettres. Les classes s'appellent desormais EXPOSEE
(differe entre noyau et libm), EXPOSEE-LIBM (differe entre libm ; trois valeurs du champ de
forces), ABSORBEE (cas durs sans ecart au bit), NON SEPAREE (jumeau non construit). Les
issues de N-70 gardent (a) (b) (c). Cette note applique deja la regle.

## 4. DECISION (v) -- L'OBJET EST RETROUVE

SUIVI_campagne_2026-08-28b.md a ete redige par machine 1 le 28/08 dans le chat "Mesure de A"
(e9aa93d2), livre en sortie de chat, jamais verse au projet (le projet porte 28, 28c, 28d),
jamais transite en lot -- d'ou "detenu nulle part", fait deja verse le 28/08 au soir.
Retrouve aujourd'hui dans le transcript de ce chat (l'appel create_file porte le texte
entier), reconstruit au poste, entites HTML du transcript de-echappees, et AUTHENTIFIE PAR
CANON AVANT TOUTE LECTURE : sha256 b6d13e6a1559e850, 5639 octets, ASCII, LF, newline final
-- identiques a l'annonce du 28/08. La piece est jointe a ce lot, octet pour octet. Le 28c
(au projet) le remplace comme etat et le cite (l.4, l.104) ; le gel v5 le cite a la
provenance (l.587) : cette citation resout desormais.

L'OBJET DE (v), citable : section 2 du 28b. Les deux captures des runs du delta 85 sont
deposees en octets CRLF (brut 3833ba551a390945, 717b61caa5921aaa) et citees a l'acte sous
convention B (10a7ce5688f515d5, 0e7e56006d2e200a). Deux lectures a l'arbitrage : (a) conforme
-- la convention B definit l'empreinte apres normalisation, .gitattributes garde les octets ;
(b) fait de forme numerote au prochain acte (E18) et regle d'ecriture : toute piece CRLF
citee declare sa forme a la citation.
Etat de fait depuis : la pratique est (b) -- le 28b lui-meme (section 5 : "brut ... (NFC+LF
...)"), tous les manifestes des deux machines depuis (deux empreintes, deux tailles), le
manifeste de ce lot de machine 2. Ma plume : (b) ; le fait de forme prend son numero a
l'acte ; la regle d'ecriture est deja acquise si la clause "toute transformation CRLF -> LF
est declaree a l'application" figure au texte qui porte la convention B (a verifier a ce
texte, pas depuis la memoire) ; sinon elle est la QUATRIEME candidate sous (X), revue 28/09.
(v) ne "suit" plus (iv) : elle est tranchable seule, des maintenant.

Les deux autres pieces introuvables (128d0c0a, a6415de8) : meme voie possible (transcript du
chat du 09/09), non tentee ici ; citees par aucune mesure, aucun gel, aucun acte. Ma plume :
les declarer a l'acte "non detenues, non porteuses" plutot que d'y depenser un geste, sauf
demande explicite.

## 5. LES QUATRE AUTRES DECISIONS -- LECTURE MACHINE 1 (l'operateur tranche)

(i) LD-16 / depot. Accord sur le prealable : l'acte ecrit sous quel gel LD-16 lit (v11), que
sa clause d'ancrage (5.4, W-plancher) est abrogee par la v11 "et remplacee par aucune autre",
et -- selon le dossier -- que le v5 emet c_pl_ld16_herite: 10 au reglage du JSON : un run
depose sous v11 porterait une constante que son gel declare retiree. Si LD-16 releve de (X),
c'est une occasion nommee : erratum de re-ancrage (forme de 7 (i), sans editer v11) ou
retrait a l'acte. Accord aussi que (i) et (ii)-(c) voyagent ensemble sans se substituer
(29/08, contresigne).
(ii) N-70. Accord sur la contrainte mesuree : le 9bis entre machines compare a tolerance ou
exempte, meme noyau desactive (residuelle glibc/UCRT a un ulp sur dix tolerances ; champ de
forces a trois valeurs). (a) est deja l'etat de fait (huit cles tol_int a la valeur machine
2 dans run_temoin_delta85, releve 2/2 par machine 2). Ma plume, sans decider : (c) est la
seule issue coherente avec un instrument portable ; (a) ecrit une contrainte muette ; (b)
affaiblit le controle la ou il mesure.
(iii) Accord : les deux errata (7 (i) ; "seul point", corrige six au bit / trois au journal)
prennent leur numero au meme geste et partent au meme depot.
(iv) Accord, la plus urgente : l'acte constante A (delta 90) est le vehicule du depot groupe,
avant la revue du 28/09. Son perimetre ne s'ecrit pas a la main : il s'enumere depuis les
citations de l'acte -- toute empreinte citee est dans l'arbre au clone frais, comme les 54/54
du 85 -- et les absences deja mesurees par machine 2 (dossier, section 6) en font partie.

Regle candidate n. 3 de machine 2 : accord ; elle et ma regle du 12/09 ("un ecart plus fin que
le pas de lecture n'est pas une mesure") sont les deux faces d'une seule, a fusionner a la
revue : tout nombre qui entre dans une borne, un compte ou un ecart se lit a la source, et un
ecart plus fin que le pas de lecture n'est pas une mesure.

## 6. CE QU'IL FAUT POUR ECRIRE L'ACTE (DELTA 90 ATTENDU ; corps "nn", numero dans le nom)

    a re-livrer en lot (conteneur reinitialise) : gel v5 (lot d5ace962a3a6e413) ; certification
      13d2973b0e143a20 ; chaine a4c35a2ee691c9a7 ; lot 7883311c6e363b02 (tenaille v1,
      comparaison a trois) ; m2_v8_prevol_temoin_resultats.json et son journal ; mes deux
      resultats_temoin_prevol (noyau, libm) et mon journal du 28/08 ; les lots du geste (2) :
      machine 1 2b155abffbe4f6ff, 117bcfaa1f283059, 5ea2fa8d7457a125, ca5456d3b11df0be,
      4cb991ce22ca35d0, 1859bbc126bb52c7 ; machine 2 eb7fb1cefbf2cec4, f9e1c1922e32220d,
      3675daba802cbc6c, cd70cda556d60380.
    a jouer par machine 1 sur clone frais avant l'acte : rejeu de derivation v2 et de relecture
      v1 (les deux comptes deviennent des comptes de machine 1) ; le controle croise de la
      section 3 ; R-G2-5 (grep des ** de tableau sur les 91 .py du registre, moteur compris) ;
      le releve du registre (origin/main d037d21, plafond 89 ; 90 libre a verifier au depot).
    a l'operateur : (i) a (v) -- (v) tranchable seule des maintenant -- et l'arbitrage du
      29/08 (marge du volet A ou marge cote T, pas les deux) ; le chat : la meme conversation
      si les lots arrivent maintenant (pieces detenues), sinon chat neuf avec la liste ci-dessus.

## 7. PIECES DE CE LOT

    note_machine1_lecture_ouverture_acte_constante_A_v1.md   cette note (empreinte au manifeste)
    SUIVI_campagne_2026-08-28b.md                             b6d13e6a1559e850, 5639 octets :
                                                              re-emission octet pour octet de la
                                                              piece du 28/08, authentifiee par canon

-- FIN note_machine1_lecture_ouverture_acte_constante_A_v1 --
