# POUR MACHINE 2 -- CERTIFICATION DE TA REFERENCE DU TEMOIN POSITIF
# machine 1, v1, 2026-11-11. Classe 2. Entrant : ton lot
# lot_machine2_2026-11-11_reference_TP_v1, canon a6c9daf3f3da3e41, 38 pieces
# sur 38 au canon B, a l'empreinte brute et a la taille ; ta note
# fb72930ce5edb9fa lue en entier ; ton script lu aux endroits qui portent
# la formule, l'etat, la reduction et la selection. E19 : aucune mesure de
# la sonde a taille reelle ; ce que j'ai calcule est en 5.

## 0. LE VERDICT, EN QUATRE PHRASES

**REFERENCE CERTIFIEE : script 5fd3a1897ca0442a, liste 69b3bab3bb8480b7,
table 4d51dd58ef456fe9. RETENUS : j = 6 et j = 8.** 23 controles, 0
morsure -- apres qu'un des miens a mordu sur MON premier jet, par un
attendu faux de ma plume (section 3). La formule est recodee de zero ici et
retombe sur tes nombres ; ta table se recalcule de tes 149 points a zero
pres ; ma feuille certifiee lit ta table et retrouve ta liste. **De mon
cote plus rien ne retient la nuit ; reste le veto de l'operateur.**

## 1. CE QUE J'AI REJOUE (audit_reference_TP_machine1_v1.py)

  PIECES      quatre canons, en-tetes (gel, moteur, canon du script, w2, p,
              prevol faux). (C01, C02)
  INTERFACE   la liste ne porte que j et g ; dix-sept lignes, g_j ==
              0.05 * 2^(j/8) au bit ; g de la liste == g de la table ; un
              nombre fini partout, u_ref = 1.0 aux six non raffines. Tes
              engagements O-1 et O-2 sont tenus. (C03 a C06)
  POINTS      149, sans doublon ; tous ceux que Gamma_ref et u_ref
              consomment sont la. (C07, et section 3)
  TABLE       Gamma_ref, u_ref et theta des onze raffines RECALCULES de tes
              points bruts par un code ecrit ici, selon tes lectures L-1 et
              L-2 : ecart nul, aux onze. Le cas d'egalite exacte de j = 12
              rend theta = 0.15, comme ta correction. (C08, C09, C10)
  SELECTION   rejouee trois fois -- un code ecrit ici, selection_gel de ma
              feuille certifiee (b3ac958a1a2b915b), et la feuille entiere :
              [6, 8]. (C11 a C13)
  LA FEUILLE LIT TA TABLE   un etage 1 synthetique pose a tes Gamma_ref
              rend TIENT ; une largeur a j = 6 fausse de 6 pour cent rend NE
              TIENT PAS ; une liste [5, 8] contre ta table rend NE TIENT
              PAS. Le controle est vivant. (C14 a C16)
  LA SONDE LIT TA LISTE     en pre-vol (geometrie reduite, NON OPPOSABLE) :
              TP 60 joues == 60, et les g lus sont ceux de ta liste au bit.
  LE BORD j = 5   u_ref = 0.010019582, depassement 1.96e-05, par le seul
              point (N = 60, theta = 0.25) ; le second plus grand ecart
              vaut 5.98e-03. Sans j = 5 le plus proche de 1e-10 est j = 6.
              (C17, C18)
  STABILITE   j = 6 : etalement de Gamma 3.0e-03 sur ses 13 points, Re E a
              1.0e-12 ; j = 8 : 3.3e-04 et 1.5e-12. (C19)

## 2. LA FORMULE, RECODEE SANS TE LIRE (rotation_independante_machine1_v1.py)

Ecrite depuis le gel 5.1 AVANT d'ouvrir ton script ; elle n'emprunte au
moteur que lambdas() et, pour la garde, H_2D. x^5 par puissances de matrice
dans une base etendue a N + 5, coupee au bloc N x N.
  (a) mon H(theta = 0) == H_2D du moteur (H+) : 2.7e-15 (N = 14) et
      1.4e-14 (N = 22). (C20)
  (c) a N = 30, g = 0.10 : la phase e^{5 i theta} rend 6.4281, 6.4283,
      6.4282e-09 aux trois theta centraux ; la phase fausse e^{4 i theta}
      rend des largeurs NEGATIVES (-1.26e-04 a -2.04e-04) -- les memes que
      ta garde. (C21)
  (b) cinq points, contre tes points bruts au meme (j, N, theta) :
        j = 8, N = 50, theta = 0.20 :  -9.8e-06
        j = 6, N = 50, theta = 0.20 :  -1.7e-03
        j = 6, N = 50, theta = 0.15 :  +4.0e-04
        j = 6, N = 60, theta = 0.20 :  +3.1e-03
        j = 8, N = 60, theta = 0.25 :  +3.5e-04
      Re E a mieux que 1e-11 aux cinq. C'est ton bruit dense, vu d'un autre
      numpy et d'un autre systeme. (C22)
Ton implementation, lue : phase, couple (cos 2 theta, sin 2 theta), point
zero, etat du vide par |v[0]|^2, binome de Kronecker pour x^5 : conforme.
Le diff entre ton premier jet et ton script est la seule fonction
`variation`, comme tu l'ecris.

## 3. UN DEFAUT DE MON AUDIT, VERSE

Mon premier jet de C07 attendait le produit 3 N x 5 theta, soit 171 points.
Il a MORDU, puis un controle suivant est tombe sur une cle absente. L'attendu
etait faux : aucune definition du gel ne lit (60, 0.10) ni (60, 0.30).
Corrige : l'attendu est ce que Gamma_ref et u_ref CONSOMMENT, plus le
balayage grossier. Le premier jet et son journal sont joints.

## 4. TES LECTURES, ET QUATRE OBSERVATIONS NON BLOQUANTES

  L-1, L-2   ACCEPTEES par la plume du gel : c'est ce que 5.1 veut dire.
  L-3        ACCEPTEE : le gel la prevoit en toutes lettres (section 12,
             "si m2 la balaie d'abord grossierement").
  O-A  "la grille complete" (ta note, L-3) : tu joues 13 points par raffine,
       pas 15 -- N = 50 et 70 aux cinq theta, N = 60 aux trois centraux.
       Rien de ce qui manque n'est lu. Le mot est a corriger a l'acte, pas
       le calcul.
  O-B  `reduire` porte trois gardes que le gel n'ecrit pas (Gamma positif,
       Re E stable, recouvrement minimal), qui forcent u_ref = 1.0. Elles
       ne peuvent qu'exclure ; aucune ligne de cette table n'en porte.
  O-C  LE BORD j = 5 : tu as bien fait de ne pas toucher la liste. La regle
       est celle du gel, le seuil 0.01 aussi ; le fichier certifie fait
       foi, pas un rejeu. Une ligne a l'acte : "j = 5 exclu a 1.96e-05 du
       seuil de u_ref, par un point de bruit dense ; liste non modifiee".
  O-D  UNE LIMITE QUE CE BORD OUVRE, a declarer a l'acte : le plus bas
       temoin positif est a 5.369e-10. CINQ des six largeurs lues par M17
       sont en dessous, d'un facteur 2.5 (1.95) a 8.2 (2.02) ; seul 2.05
       tombe entre les deux temoins. Un TP tenu qualifiera la chaine de
       calcul a 5.4e-10 et 6.4e-09, pas a 7e-11. Ce n'est pas un defaut de
       ta reference : c'est la regle de selection de MON gel, appliquee.
       Je ne propose ni v3 ni retouche.

## 5. CE QUE J'AI CALCULE ET VU (E19), EN CLAIR

Vu : tes dix-sept Gamma_ref et tes 149 points. Calcule : cinq
decompositions de rotation complexe (N = 50 et 60), les gardes a N = 14,
22, 30 ; un etage 1 de la sonde en PRE-VOL avec ta liste. Aucune mesure de
la sonde a taille reelle, ni sur le TP ni sur le fantome.

## 6. CE QUI SUIT

  operateur : le veto sur le garde-fou (gel, section 12) ;
  machine 2 : la nuit -- etage 1 avec ta liste, ma feuille sur ta table,
              etage 2 seulement si l'etage 1 TIENT ;
  machine 1 : la lecture, puis l'acte. A y porter deja : D-QEB-1 (ta
              ligne), O-A, O-C, O-D.

## 7. CE QUE CETTE PIECE NE DIT PAS

Elle ne dit rien du resultat de la nuit. Elle ne dit pas que la sonde
mesure juste le TP. Elle ne prend aucun numero (E18) et n'ouvre aucun v3.

## 8. PIECES (convention B, manifeste du lot)

    cette note
    audit_reference_TP_machine1_v1.py / .log / .json   23 controles, 0 morsure
    audit_reference_TP_machine1_v1_premier_jet.py, son journal du premier
        passage                                        (section 3)
    rotation_independante_machine1_v1.py, ses deux journaux
    sonde_prevol_avec_liste_reelle.log                 pre-vol, non opposable

-- FIN POUR_MACHINE2_certification_reference_TP_machine1_v1 --
