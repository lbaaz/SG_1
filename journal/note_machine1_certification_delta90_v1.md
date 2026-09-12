# CERTIFICATION MACHINE 1 -- ACTE DELTA nn (CONSTANTE A), PROJET v1, CANON 932fa1cdfa823672
# VERDICT : CERTIFIABLE -- BON POUR DEPOT APRES DEUX HUNKS DE FORME (H1 detention unique,
# H2 date), AUCUN NOMBRE NE CHANGE ; LA RESERVE DE DETENTION SE CLOT PAR LE RELEVE 198/198
# SUR CLONE FRAIS APRES DEPOT, A LA PLUME DE MACHINE 1.
# machine 1, v1, 12/09/2026 (nuit). Classe 1. PB-1 : aucune piece recue n'est editee ; les
# rejeux se font sur des copies placees dans l'arbre re-livre, jamais sur les pieces du lot.

## 0. EN QUATRE PHRASES

Le lot 7b8c7398a755c28e est recu 7/7 au canon ; l'acte est lu en entier. Tout ce qui est
verifiable a mon poste l'est et concorde : la structure (insertion apres le 89, 90 libre),
les nombres de la tenaille (rejoues au bit la nuit derniere), mes propres nombres (cause de
l'ecart, R-G2-5, garde, rejeu), le temoin d'arrondi remesure sur machine 1 sous trois
environnements, le manifeste de depot derive ici identique ligne pour ligne sur les 160 lignes
que mon poste peut deriver, les quatre collisions prefixees des deux cotes. Ce qui ne l'est
pas : 18 des 95 empreintes citees ne sont detenues qu'au poste machine 2 (jamais transmises
a machine 1), soit 38 des 198 lignes du depot ; elles sont prises sur la derivation de machine
2 et se verifieront au clone frais apres depot. L'acte ne le declare pas : c'est le hunk H1.

## 1. RECEPTION

    verifiees 7 + absentes 0 + ecarts 0 == 7 ; canon 7b8c7398a755c28e ; ZIP brut de77b2e10121d89a
    932fa1cdfa823672  journal_delta_nn_constante_A_v1.md  (42696 octets, ASCII, LF)
    9a3e72664e4a13c2 / e00c3cd55d8b25e5 (brut 5aed5e45fb7c3fe6)   perimetre .py / .log
    0aae5d85df39862b / e38900f7ffd7da69 (brut 70e59105db537578)   relecture .py / .log
    d32ccd1be84d07f7  MANIFEST_DEPOT_delta90_machine2.txt (198 lignes)
    76393d1e22e9a300  POUR_MACHINE1_acte_delta90_machine2_v1.md
    Son accuse de mon lot be5ee780388d1965 (5/5) est pris.

## 2. CE QUI EST REJOUE A MON POSTE

Clone frais lbaaz/SG_1 : HEAD d037d21, plafond 89, aucun fichier delta_90, 90 libre ;
journal_delta_89_R4R5_v5.md resout a c0f0f4f3b5477310 -- la ligne d'insertion de l'acte tient.

Perimetre (feuille 9a3e72664e4a13c2, rejouee dans l'arbre re-livre d0ab94382e1b5808 avec le
clone en argument) : 17/18 controles PASSENT ; 95 empreintes citees : 11 au registre, 62 au poste, 1 zip, 3 valeurs, 18 non resolues ; DEPOT : 160 pieces (gels 3, journal 156, scripts 1) ; manifeste f91164f1c44de662. Les 18 non resolues sont EXACTEMENT les pieces jamais
livrees a machine 1 : gel v3 (d71770d5), temoin v9 (403488b4), certification temoin v11
(7fc5f241), depot 9bis (c4310e33), bancs v4 a v7 et leurs deux constructions (36a3f06f,
b8a0f753, 56c2ebfc, 9a6e8b61 ; 35b9ff3b, 81730d2b), trois notes (be633ae9, aa98fa8b), SUIVI
29a (d0747b01), N-70 v1 (4ef8235b), lot R2 (7ee2d2d4), lots de certification du 89 v3 et v4
(bdd00189, 704f2b6b) et leur controle (0c577a23). Le manifeste de depot derive ici
(MANIFEST_DEPOT_delta90_derive_machine1.txt, joint) porte 160 lignes ; les 160 sont IDENTIQUES
(chemin cible et canon) aux lignes correspondantes du manifeste de machine 2 ; les 38 lignes
qu'il a en plus sont les pieces de table des 18 lots ou pieces ci-dessus (37) plus le log de sa
propre relecture (1, artefact d'emplacement : je le detiens dans le lot 7b8c7398). Section 4 :
les quatre collisions (diagnostic_pow_cas_durs_machine1_v1.json et .log, lots 117bcfaa et
f9e1c192) prennent le prefixe lot_<canon>__ DES DEUX COTES, aucune ne garde le nom nu :
forme acceptee, rien a changer.
Fait d'arbre, sans consequence : la feuille exclut son propre repertoire du balayage, et
l'assemblage de la re-livraison avait place les quatre lots des tours du 12/09 dans ce meme
repertoire (ACTE_constante_A) ; 15 empreintes ne resolvaient qu'apres copie hors de ce
repertoire, et le ZIP de la re-livraison n'est resolu que s'il est a la racine. Une piece se
resout par canon n'importe ou au poste, sauf la ou la feuille declare ne pas regarder -- que
le log le dise.

Relecture des nombres (feuille 0aae5d85df39862b, rejouee dans le meme arbre, mon lot de rejeu
place sous entrant_machine1_2026-09-12_rejeu_relivraison/lot/ et l'assemblage v2 a cote de la
feuille) : 137 controles rejoues, 137 PASSE, 0 MORD ; la feuille s'arrete sur la premiere piece
non detenue (enumeration_cles_prevol_N70_machine2_v1.md) -- 23 controles ne sont pas rejoues
ici et restent au compte de machine 2 (160/160). Remarque de forme, non bloquante : une
lecture de source qui echoue devrait rendre NON JOUE et continuer, pas arreter la feuille --
c'est l'esprit de la candidate 7.

## 3. CE QUE J'AI MESURE MOI-MEME, HORS DES DEUX FEUILLES

    temoin d'arrondi (temoin_arrondi_machine1_2026-09-12.log, joint) : sur cette machine 1,
      numpy 2.4.4, (1765.6704444885254)**6 en tableau rend ...9c5 sans levier, ...9c6 avec
      NPY_DISABLE_CPU_FEATURES=X86_V4 seul, ...9c6 avec les trois groupes ; le pow de Python
      rend ...9c6 dans les trois cas. La phrase de nn.5 (b) "levier X86_V4" est MESUREE vraie
      aujourd'hui ; ma note du 12/09 donnait la forme a trois groupes, qui vaut aussi.
    nn.4 : tous les nombres sont ceux du log f60104c0c3ba7ec4 que j'ai reproduit au bit
      (lot be5ee780388d1965) ; J = 5 (1/102400) sous INF et J = 4 (1/25600 = 3.906e-05)
      au-dessus de 3.457e-05 : "aucun barreau de l'echelle b = 4" tient a l'arithmetique.
    nn.5 (a) : 0.759/0.684 = 1.1096, "11.0 pour cent" tient ; nn.5 (e) et nn.7 : 91 .py, 545,
      232 dans 41 fichiers, m9_replication_v1.py:324, 57/42/9/6, 36 au v3, 5 appels a
      condition constante sur 7 feuilles, l.69/126/180 -- tous mes nombres, tels que mesures.
    nn.1 : la feuille d'assemblage v2 resout a df3bd37cbca40c36 (recalcule sur l'exemplaire
      recu) ; nn.11 : sept lots sur l'acte le 12/09 (quatre de machine 2, trois de machine 1)
      et onze sur le geste (2) (six et cinq) -- comptes tenus.
    presences, dans mes notes du geste (2), des nombres que l'acte cite de ma plume
      (grep sur les quatre lots, occurrences) : 15 pas 707;     10 1, 2, 2, 0;      5 44/44;      1 5.2 a 5.5 pour cent;

## 4. DEUX HUNKS DEMANDES AVANT DEPOT (forme ; aucun nombre ne change ; l'acte passe en v2)

H1 -- nn.1 (ou nn.11), a inserer apres la liste des pieces citees :
  "Au 12/09, 18 des 95 empreintes citees ne sont detenues qu'au poste machine 2 et n'ont
  jamais ete transmises a machine 1 : d71770d5948fe1aa 403488b4f6c319e9 7fc5f2412b99ad50 c4310e33da6b9759 35b9ff3b8e5b7ef0 36a3f06f19871c38 81730d2bf7095c1f b8a0f75323182e55 56c2ebfcfd84671e 9a6e8b6192d4f163 be633ae91ae295b5 aa98fa8b4ba921d8 d0747b01700e4ad8 4ef8235b16f26210 7ee2d2d4fc0b27a1 bdd00189e68b61dc 704f2b6b84f4c6a0 0c577a23d67586c8. Elles entrent au registre par cet acte et
  deviennent verifiables par quiconque sur clone frais ; les 77 autres resolvent aux deux
  postes (rejeu machine 1 du perimetre : 11 au registre, 62 au poste, 1 ZIP, 3 valeurs)."
  Motif : toute piece detenue par une seule machine est declaree telle a la citation
  (discipline du protocole, deja payee au 85 avec l'ordre 6e176705468a4834). Sans H1, un
  lecteur croit les 95 detenues des deux cotes.
H2 -- nn.11, premiere ligne : "Le conteneur de machine 1 a ete reinitialise le 07/09" ->
  "Le conteneur de machine 1 est reinitialise a chaque conversation (perte constatee le 09/09,
  lors de la recherche des pieces 128d0c0a et a6415de8)". Je ne peux pas dater une
  reinitialisation ; c'est une propriete du canal, pas un evenement.
La v2 se certifie par DIFF contre la v1 : si le diff est exactement H1 + H2 (et la ligne de
version), la presente certification vaut pour la v2 sans nouveau tour ; le perimetre se
re-derive (la ligne journal_delta_90_constante_A_v1.md du depot change de canon avec l'acte).

## 5. MA PLUME (l'operateur tranche ; rien n'est pris ici)

nn.8, les huit candidates : accord pour les porter toutes a la revue du 28/09. A la revue :
fusionner 2 et 6 en une seule discipline de feuille de controle (l'affirmation vit dans la
condition ; deux verbes chk/note ; la garde syntaxique avant emission) ; noter que 5 a deja
une seconde instance, ma propre discipline str_replace (src.count(old) != 1 -> arret) --
comme 4, c'est une pratique des deux plumes que le texte ne porte pas ; ajouter a 1 que la
ligne de plateforme porte aussi la version de numpy et le niveau de dispatch, le temoin
datant l'exposition et le couple roue x dispatch en datant la cause ; sortir de 8 la clause
"un controle d'absence balaye tout le poste par canon", qui est une regle a elle seule.
Numeros de chantier : garder D-ACA-1..7, D-G2-1..4, D-I-1..9, D-v5-1 comme etiquettes dans
le corps ; les numeros de serie (D, E, N) en un seul bloc au depot par l'operateur (E18),
les errata (1)(2)(3) et le fait de forme de (v) dans le meme bloc -- c'est (iii).
Collisions : la forme lot_<canon>__<nom> est prise telle quelle, aux deux membres.

## 6. VERDICT

CERTIFIABLE. Bon pour depot des que H1 et H2 sont portes (v2, certifiee par diff). Reserve
declaree et bornee : 18 empreintes, 38 lignes du depot, prises sur la derivation de machine
2 (18/18) et sur sa relecture (23 controles non rejoues ici) ; elle se clot par le RELEVE
198/198 sur clone frais apres depot, a ma plume, en un tour (le perimetre rejoue avec le
nouveau HEAD doit rendre 95 au registre, 0 non resolue). La porte n'a pas bouge ; aucun run,
aucun delta, aucun verdict de gel ; rien n'est tranche pour l'operateur.

## 7. PIECES DE CE LOT

    note_machine1_certification_delta90_v1.md          cette certification
    rejeu_perimetre_delta90_machine1.log               perimetre rejoue ici (17/18, 18 non resolues)
    rejeu_relecture_delta90_machine1.log               relecture rejouee ici (137 PASSE, arret sur N-70 v1)
    MANIFEST_DEPOT_delta90_derive_machine1.txt         160 lignes derivees ici, toutes identiques a m2
    temoin_arrondi_machine1_2026-09-12.log             le temoin sous trois environnements

-- FIN note_machine1_certification_delta90_v1 --
