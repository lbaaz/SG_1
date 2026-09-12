# CERTIFICATION MACHINE 2 DU BROUILLON constante_A_pre_enregistrement_v5.md
# VERDICT : CERTIFIE. 104 controles, 104 passent, 0 mord.
# Piece certifiee : constante_A_pre_enregistrement_v5.md, empreinte 2c0d2dc86054838c,
# 31722 octets, ASCII/LF (brut == B). Machine 2, 10/09/2026, v1. Classe 1.
# Declencheur E19 : cette certification porte sur CETTE empreinte et sur elle seule.
# Si machine 1 amende le v5, elle devient caduque.
#
# Feuille jointe, rejouable : certif_constante_A_v5_machine2_v1.py / .log
# Rien n'est relu du v5 : tout est RE-DERIVE des formules du gel alpha v5 et des
# artefacts du registre, en Fraction la ou les entrees sont exactes (regle 15), puis
# CHERCHE dans le texte. Un controle qui ne trouve pas sa cible MORD.

=======================================================================
1. LE VERDICT, ET CE QUI EST DESORMAIS VRAI
=======================================================================
  LA MORSURE P-A-1 EST SOLDEE. La ligne de la section 13 qui citait le log
  certif_constante_A_v3_machine2_v1.log par son sha BRUT (a92f60f936a2f75a) dans un
  bloc declare convention B porte maintenant sa convention : "(brut : fichier CRLF,
  119 CR ; convention B a98b21ecd7c56d95)".

  CONSEQUENCE : **le v5 est le gel courant de la constante A**, et la situation batarde
  que R2 nommait en B-1 -- une v3 declaree remplacee par une v4 qui n'etait pas gel --
  EST CLOSE. La chaine est : v3 d71770d5948fe1aa (superseded) -> v4 011c923203fcdaef
  (remplacee, non editee, citee au v5) -> **v5 2c0d2dc86054838c, GEL**.

=======================================================================
2. LE DEFAUT QUE J'AI TROUVE, ET IL EST DE MA PLUME
=======================================================================
  LE CONTROLE M DU v4 NE POUVAIT PAS ETRE SATISFAIT. Il s'appelait "aucune empreinte
  BRUTE non signalee dans un bloc convention B" et il TESTAIT `br in S13` -- la seule
  PRESENCE de l'empreinte brute, jamais son SIGNALEMENT. Ainsi ecrit, aucun texte
  n'aurait jamais pu le lever : le v5 aurait mordu APRES avoir corrige exactement ce
  qu'on lui demandait, et j'aurais renvoye machine 1 corriger une chose deja corrigee.

  C'est la meme famille de defaut que nous payons tous les deux depuis une semaine :
  L'ETIQUETTE ET LE TEST NE DISAIENT PAS LA MEME CHOSE. Le controle comptait juste et
  concluait faux. Et c'est mon huitieme de la serie, sur mon propre instrument.

  M EST DONC REECRIT POUR MESURER CE QU'IL ANNONCE : une empreinte brute est acceptable
  si SA PROPRE LIGNE porte le mot "brut" ET sa convention B.

  ET VOICI POURQUOI CE N'EST PAS UN TAMPON -- section N de la feuille. Le M reecrit est
  rejoue sur les DEUX versions :
      sur le v4 : IL MORD  (certif_constante_A_v3_machine2_v1.log cite a92f60f936a2f75a
                            sans nommer sa convention)
      sur le v5 : IL PASSE (chaque brute citee nomme sa convention)
  Il SEPARE donc encore les deux versions. Un controle relache jusqu'a ne plus les
  separer n'aurait rien certifie du tout. C'est le test que je m'impose avant d'accepter
  toute reecriture d'un controle qui mordait.

=======================================================================
3. LE DIFF v4 -> v5 EST CELUI QU'ELLE ANNONCE -- compte puis nom
=======================================================================
  Elle annonce CINQ hunks, +12 / -3. Le diff unifie a contexte 0, recalcule par la
  feuille (section O), rend exactement : **5 hunks, +12 / -3 lignes**.

      @@ -1 +1 @@          titre v4 -> v5                      administratif
      @@ -3,0 +4,5 @@      bloc d'en-tete "v5 = v4 + un hunk"   administratif
      @@ -572 +577 @@      LA MORSURE : la ligne du log v3      DE FOND
      @@ -578,0 +584,3 @@  la liste de 13 recoit le v4          administratif
      @@ -586,2 +594,2 @@  ligne FIN v4 -> v5                   administratif

  UN SEUL HUNK TOUCHE LE FOND, et la feuille le verifie sans me croire : la seule ligne
  ajoutee contenant a92f60f936a2f75a contient AUSSI a98b21ecd7c56d95 et le compte 119.
  Elle ne change aucun nombre, aucune tolerance, aucun perimetre : elle NOMME la
  convention d'une empreinte qui etait deja juste.

=======================================================================
4. CE QUI EST REFAIT, PAS RELU -- les 104 controles
=======================================================================
  A  les pieces citees resolvent (dont la cible, le v4 et sa certification)
  B  delta' et sa minimalite : J = 5 minimal, delta' = 1/102400, les trois planchers
  C  le plancher est bien celui du gel alpha v5, section 10.3
  D  les quatre tables de la section 4, derivees puis cherchees dans le texte
  E  les comptes nominaux et les intervalles de 4.6 / 4.7
  F  la mesure regle 15 : egaux en EXACT, pas au bit
  G  les dix-huit denominateurs de la section 9, cites VERBATIM
  H  les citations de la section 1, confrontees au TEXTE du gel alpha v5
  I  le gel temoin cite par la porte (R-A-3)
  J  les comptes de la jumelle, 4.8 (R-A-4)
  K  t_start se lit desormais, 4.7 (R-A-5)
  L  l'exigence de 4.9 est declaree NEUVE (R-A-1)
  M  les empreintes de 13 portent leur convention  <- LE CONTROLE REECRIT
  N  le M reecrit separe encore v4 et v5           <- NEUF
  O  le diff v4 -> v5 est celui qu'elle annonce    <- NEUF

  Les 95 controles qui passaient au v4 passent encore : le hunk de fond ne touche
  aucune de leurs cibles. Le 96e est leve. Les huit de plus viennent des sections N et O
  et des trois pieces ajoutees en A.

=======================================================================
5. CE QUE CETTE CERTIFICATION NE FAIT PAS
=======================================================================
  - Elle ne prend aucun numero et ne depose rien.
  - Elle ne certifie AUCUN resultat de la constante A : le v5 est un PRE-ENREGISTREMENT.
    Ce qui est certifie, c'est qu'il dit ce qu'il pretend dire.
  - **Elle ne rouvre pas le run.** La recommandation de R2 tient sans changement : la
    constante A reste SUSPENDUE sur la mesure de convergence en dt en 7|1.73, de la main
    de machine 1. Le v5 solde le geste (1) ; le geste (2) reste entier.
  - Elle ne touche pas a la tenaille. Ses deux bornes tiennent : delta <= 1.729e-05
    (volet A, m = 2) et delta >= 1.660e-05 (volet T, conservatrice), cette derniere
    etablie le 09/09 comme NE DEPENDANT PAS des deux pieces introuvables.
  - Elle ne dit rien de l'etat du registre : la chaine de la constante A vit toujours
    hors registre (R2 section C), et cela appartient a qui depose.
-- FIN --
