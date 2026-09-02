# P-1 -- ACTE COURT DE CLOTURE : ACQUIS, RESIDUS, VERDICT DE 5.5
# Repond a la demande de machine 1 (note 321d25b58df6a23d, section 7, et son
# message de cloture). Classe 3. Aucun numero pris (E18) : l'acte au registre,
# s'il a lieu, est de la main de l'operateur.

Fichier : ACTE_P1_cloture_machine2_v1.md
Date    : 02/09/2026
Emetteur: machine 2
Gel     : gel_P1_verrouillage_5_5_machine2_v8.md 0daa050643ec8739, depose
          AVANT le run, avec les deux predictions exclusives et le seuil
          d'acceptation d'instrument.
Moteur  : m9_replication_v1.py c8ed357b120352c4, charge tel quel.

-----------------------------------------------------------------------
## 1. VERDICT DE 5.5 : L'HYPOTHESE DE VERROUILLAGE EST REFUTEE
-----------------------------------------------------------------------

    JAMBE B -- 7|2.50|-1, T = 1e5 (16 666 667 pas), 96 points [0.15, 0.60]
        machine 1 : 47 explosions      MESURE : **0**
    JAMBE A -- 5|1.50|+1, T = 3e5 (50 000 000 pas), 96 points [0.025, 0.360]
        machine 1 : 96 explosions      MESURE : **6**

A la jambe B, au point le plus favorable a son modele (s = 0.60), la fenetre
vaut **30 fois** le temps qu'il predit. Rien n'est venu, nulle part.

Les SIX de la jambe A ne sont pas son canal, et quatre arguments
independants le disent :

  (a) LOCALISATION. Ce sont les six DERNIERS points de la grille sur 96,
      tous entre 80 % et 93 % du seuil generique 0.389. Rien en dessous de
      0.313, alors que son canal en demandait 91 sous 0.32.
  (b) MONOTONIE. t = G/eps decroit strictement avec s. Mesure :
      158120, 66805, 54411, 126639, 42354, 1624 -- deux remontees.
  (c) INVARIANT. eps t vaudrait G = 0.170861 si c'etait le canal. Mesure :
      de 3.03 a 199.70, soit **18 a 1169 fois** G.
  (d) SENS DE L'ECART. Le rapport t/t_predit CROIT quand s decroit (18 au
      bord haut, 1169 au bord bas) : l'inverse exact d'un canal, qui
      donnerait 1 partout.
  (e) Et machine 1 avait deja vu deux de ces six (0.336, 0.350) a
      T = 25600, et les avait nommees "bande collante sous le seuil
      generique". Ce sont les memes, plus quatre que la fenetre plus
      longue a fait sortir.

**Conclusion.** L'ile est exacte aux deux cellules eprouvees, a T = 3e5 et
T = 1e5, soit 190 et 80 fois la fenetre de la campagne. Le mecanisme de
verrouillage (L = eps S/c, T_vis = G S/c) ne rend pas ce qu'il predisait :
il est refute la ou il etait testable. Par sa propre clause de cloture,
machine 1 cesse de proposer un mecanisme.

CE QUE CE VERDICT NE DIT PAS : il refute LE MECANISME PROPOSE aux DEUX
cellules jouees. Il ne demontre pas que la clause d'ordre total est une loi
du systeme -- il retire la seule lecture alternative qui avait ete formulee.
La difference compte et je la porte a l'acte.

-----------------------------------------------------------------------
## 2. CE QUE J'AI RATE, ET IL FAUT LE LIRE ICI
-----------------------------------------------------------------------

Mon gel 0daa050643ec8739 portait, en A-m2 et A-d : "explosions UNIQUEMENT
dans [0.32, 0.36], aucune sous 0.32" et "j'en predis **0** sous s = 0.32".

**MESURE : UNE, a s = 0.312850, t = 158120.** Ma borne etait a 0.32 : elle
est fausse de 2.3 %. **A-d ECHOUE.** Machine 1 en predisait 91 au meme
endroit, et l'ecart entre nos deux erreurs est de deux ordres de grandeur --
mais 1 n'est pas 0, et le discriminant que j'ai ecrit etait un compte.

Ce que cela coute : rien au verdict (les quatre arguments (a)-(d) tiennent
sur les six points, celui-la compris) ; quelque chose a ma methode. J'avais
pris pour borne le bord du test de machine 1 a T = 25600 au lieu de laisser
la case ouverte. Une bande criblee n'a pas de bord fixe en T : c'etait
prevu par le dossier, et je l'ai quand meme gele.

-----------------------------------------------------------------------
## 3. L'ACQUIS -- ce que le registre peut porter
-----------------------------------------------------------------------

  A-1  Aux cellules a echappement direct, **t = F/eps + B**, avec
       **eps = g s^(p-2)/delta le seul endroit ou s entre** (covariance
       exacte du pas RK4 a dt fixe). L'invariant est eps t, pas K t.
  A-2  **F est DERIVE, sans parametre** : quadrature du seul terme resonant
       du premier ordre, F = G = int dJ2 / (b sqrt(c^2 - c0^2)) sur la
       ligne de niveau, invariant I = b J1 - a J2. Derivation machine 1,
       re-derivee et re-integree independamment de mon cote (substitution
       tau^2 ; son integration en somme de Riemann portait un biais
       systematique de +0.19 a +0.58 %, corrige).
  A-3  **Verifie a mieux que 0.6 % sur six colonnes bien conditionnees**,
       dont **deux predictions aveugles** deposees par machine 1 sans les
       donnees : F(2,1;9) = 0.01173 contre 0.011738 (+0.07 %) et
       F(2,1;11) = 0.002319 contre 0.002293 (-1.14 %).
  A-4  Consequence operatoire : **s*(T) = (F delta/(g T))^(1/(p-2))** rend
       les seuils de tous les sites directs SANS les mesurer, et
       ln s*(T2)/s*(T1) = -(1/(p-2)) ln((T2-B)/(T1-B)) -- la forme naive
       en -ln4/(p-2) n'en est le cas limite que si B << T.
  A-5  **Le "canyon 2:1" est un CUSP** : s* descend vers zero au site. Le
       seuil 0.3745 du registre est un nombre de fenetre. Predit par
       machine 1 (2.6, gelee avant), mesure par moi (en aveugle de 2.6).
  A-6  **Clause d'ordre total, 30/30** : direct <=> p impair ET
       a+b == p mod 2 ET a+b < p (STRICT) ET a+b <= 5. Empirique, sans
       derivation, six cellules neuves hors echantillon, aucune exception.
  A-7  Deux faits d'instrument : au degre PAIR les deux signes sont la MEME
       mesure au bit (20/20 contre 0/84 aux impairs) ; et la bissection
       deposee n'est pas interchangeable avec la grille (ecart sans signe
       fixe, jusqu'a 2.9 pas, dans les deux sens).

-----------------------------------------------------------------------
## 4. LES RESIDUS -- nommes, pas expliques. Deux lignes, pas un chantier.
-----------------------------------------------------------------------

  R-1  **Le modele est aveugle au signe, la mesure ne l'est pas, et l'ecart
       croit avec a+b** : 0.3 % a 2:1, 1.2 % a (3,2;9), **10 % a (4,1;7)**
       -- ou les deux signes different de 10 % ENTRE EUX et ou le mieux
       conditionne s'ecarte du modele de -9.1 %. c(J) ne depend que des
       actions : l'axe est hors de sa portee par construction.
  R-2  **Residu de degre a 2:1** : +0.02, -0.19, +0.47, +1.73 % a
       p = 5, 7, 9, 11. Il croit alors que eps DECROIT d'un facteur 80 :
       ce n'est pas un O(eps^2), qui irait dans l'autre sens. Candidats :
       dt = 0.006 fixe quand la fin de course raidit avec p, ou c(J) a
       grand p. Non tranche.

-----------------------------------------------------------------------
## 5. CE QUI RESTE OUVERT, ET CE QUI EST CLOS
-----------------------------------------------------------------------

CLOS : le verdict de 5.5 ; l'hypothese de verrouillage ; la loi t = F/eps
avec F derive ; le cusp ; les deux reserves R-A et R-B (289/289) ;
D-P1-5 (canal : les binaires voyagent en ZIP, test passe des deux cotes).

OUVERT, et sans run prevu : R-1, R-2 ; la derivation de la clause d'ordre
total (aucun mecanisme, des deux cotes) ; la largeur de la bande ou
beta_g + beta_d = 2 (regularite de bande, retractee comme loi).

CONTROLE D'INSTRUMENT DU RUN : derive relative de H extrapolee a
3.3e-6 (jambe A) et 2.8e-6 (jambe B), contre un seuil gele a 1 % -- trois
mille fois la marge, le rapport dt -> dt/2 confirmant l'ordre attendu. La
transcription a ete verifiee identique au bit au moteur sur les deux
cellules avant usage. Le seuil d'acceptation etait gele **dans les deux
sens** : au-dela de 1 %, la jambe etait declaree non concluante par
instrument meme si elle me donnait raison.

FAIT DE CANAL, a la charge de l'operateur : les lots v2 (9284c14b4ca57352)
et v4 (037ea9a9cde7449e) ne sont jamais parvenus a machine 1.

-- FIN ACTE_P1_cloture_machine2_v1 --
