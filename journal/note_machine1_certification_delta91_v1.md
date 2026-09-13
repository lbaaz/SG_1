# CERTIFICATION MACHINE 1 -- ACTE DELTA nn (RUN DE LA CONSTANTE A), PROJET v1, CANON f1e3530df9b0958c
# VERDICT : CERTIFIABLE -- BON POUR DEPOT APRES UN HUNK DE FORME (H1 : le lot 435302fae671f4f8,
# "le reglage mesure", est detenu par machine 2 seule, jamais transmis a machine 1 ; l'acte le
# declare ou l'operateur me le transmet) ; RESERVE CLOSE PAR LE RELEVE 104/104 APRES DEPOT.
# machine 1, v1, 13/09/2026. Classe 1. PB-1 : rien d'edite. Lot m2 2ad85332a2e35877 recu 9/9.

## 1. CE QUE JE CERTIFIE, ET COMMENT

  STRUCTURE : s'insere apres le delta 90 (e68341f, 11f86226cf4aa612) -- clone frais : plafond
    90, aucun delta_91, 91 libre ; nn dans le corps, numero au depot (E18).
  NOMBRES DE nn.5, RECALCULES ICI depuis mon propre JSON alpha v13 et le reglage :
    planchers delta'/((alpha+2)(alpha+3)) = 1.1338e-06 / 1.5699e-06 / 2.1312e-06 (delta' = 1/44100) ;
    rapports dispersion/plancher 0.869 / 0.208 / 0.042 (mon JSON : 0.869 / 0.207 / 0.042 -- la
    dispersion a p = 5 differe de 0.3 pour cent entre machines, nn.3 le dit) ; bornes
    disp x (alpha+2)(alpha+3) = 1.9707e-05 / 4.7099e-06 / 9.4867e-07 ; INF/9.4867e-07 = 17.49 ;
    residuels delta' x plancher = 2.571e-11 / 3.562e-11 / 4.833e-11 ; gains 3.83e+04 / 9.15e+03 /
    1.85e+03 ; pentes 2.01 / 7.34 / 83.36 -> 0.114 / 0.327 / 0.726 ; n = 23 : 9.65e-07 contre
    9.45e-07, marge 1.02. Tous concordent avec l'acte au chiffre pres.
  D-v13-1 : PRIS. Mon "5e-06 x plancher" et mon "1e+04 a 1e+05" etaient faux ; le residuel est
    delta' fois le plancher et les gains sont ceux de l'acte. Meme famille que D-ACA-3 : un
    ordre de grandeur tape au lieu d'etre derive. La conclusion ne bouge pas, l'acte porte les
    bons nombres, le mien reste faux dans ma note ddf2070b, qui n'est pas editee.
  nn.6 : les quatre defauts sont ceux que les runs ont mesures ; (d) reprend exactement mes sept
    feuilles a un ulp et leurs noms ; le correctif v13 est decrit comme construit (6
    remplacements, pin inchange). nn.7 et les errata : lus, concordants avec les lots.
  CITATIONS ET PERIMETRE : feuille de perimetre de machine 2 rejouee a mon poste (arbre de tous
    mes lots + clone frais) : 17/18 -- 23 empreintes citees, 8 au registre, 14 au poste, 1 NON
    RESOLUE : 435302fae671f4f8, le lot machine 2 "reglage mesure" (6 pieces et son manifeste :
    note, brouillons n18/n20/n24, selftest n20, construction du brouillon v9), jamais recu
    ici. Depot derive a mon poste : 98 lignes ; 97 identiques (chemin cible et canon) aux 104
    de machine 2 ; les 7 lignes qu'elle a en plus sont ce lot ; 1 ligne de mon derive n'est
    pas dans le sien -- journal/relecture_nombres_delta91_machine2_v1.py (7ff64ccffdcb3022), la
    feuille de relecture du lot de l'acte : sa feuille de perimetre l'exclut chez elle
    (repertoire de l'acte), la mienne l'a trouvee ailleurs a mon poste ; artefact
    d'emplacement, meme canon. Aucune autre difference.
  RELECTURE des nombres (feuille de machine 2) : rejouee a mon poste dans son arbre, elle passe
    8 controles puis s'arrete sur une source absente (ses runs v13 sur BOCAL4,
    out_run_delta91/temoin_v13 et alpha_v13, non recus) -- 114/114 reste son compte pour le
    reste ; remarque deja faite au 90 : une source absente se declare NON JOUEE, elle n'arrete
    pas la feuille. Sa certification de mon v13 (24/24, dont la sonde a 1, 2, 3 ulp) : lue,
    non rejouee (memes sources).

## 2. H1, ET LA RESERVE

  H1 (nn.1 ou nn.11) : "Au 13/09, 1 des 23 empreintes citees, 435302fae671f4f8 (lot machine 2
  reglage_v6_v1, 6 pieces), est detenue au seul poste machine 2 et n'a pas ete transmise a
  machine 1 ; elle entre au registre par cet acte et devient verifiable sur clone frais ; les
  22 autres resolvent aux deux postes." Ou bien le lot m'est transmis avec le depot et la
  phrase devient inutile. Sans l'un ou l'autre, un lecteur croit les 23 detenues des deux cotes.
  La v2 se certifie par diff, sans nouveau tour, si le diff est H1 et la ligne de version.
  Reserve : les 6 lignes du depot et les controles de relecture portant sur ses runs v13 sont
  pris sur machine 2 ; le releve 104/104 sur clone frais apres depot, a ma plume, la clot.

## 3. MA PLUME SUR LES QUATRE CANDIDATES (nn.8, revue du 28/09 ; l'operateur tranche)

  9  (un pre-vol ne certifie pas) : OUI, avec la borne qui la rend jouable -- "a mordu au moins
     une fois sur un run reel" se lit "sur un run reel qui EXERCE le controle" ; le banc qui
     tue le dit de ses gardes, le pre-vol declare ce qu'il ne joue pas, le run reel ferme la
     liste. Les trois defauts sont sa preuve, et ils sont tombes UN par run.
  10 (comparaison sur la serialisation) : OUI ; c'est la regle des empreintes etendue aux
     comparaisons ; a fusionner avec elle a la revue plutot que de compter deux regles.
  11 (une tolerance se sonde a son bord) : OUI, et c'est contre moi : mon v13 declarait 2 ulp
     sans sonder 3 ; machine 2 l'a fait. A ecrire avec ses trois points (n-1, n, n+1 de
     l'unite) et l'obligation d'ENUMERER ce qui est tolere -- une tolerance muette est une
     exemption.
  12 (reproductibilite passee par construction sur la machine de reference) : OUI, et elle
     implique une pratique : une reference de 9bis se DECLARE avec sa machine, et son premier
     jeu utile -- sur l'autre machine -- precede le depot, pas le run. Le depot 9bis c4310e33
     a ete etabli sur BOCAL4 seule ; la prochaine reference se joue des deux cotes avant d'etre
     deposee. C'est l'issue (c) de N-70 rendue operatoire.
  Je ne propose aucune regle de plus.

## 4. PIECES

  rejeu_perimetre_delta91_machine1.log (17/18, 1 non resolue nommee) ;
  rejeu_relecture_delta91_machine1.log (8 PASSE, arret sur source absente) ;
  MANIFEST_DEPOT_delta91_derive_machine1.txt (98 lignes ; 97 identiques aux 104 de m2, 7 lignes du lot non recu chez elle seule).

-- FIN note_machine1_certification_delta91_v1 --
