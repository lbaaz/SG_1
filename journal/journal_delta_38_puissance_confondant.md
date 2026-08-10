Journal bundle 5 -- DELTA du 27/07/2026 : section 38 -- JE RETIRE MA
RETRACTATION. LE PLAN N'AVAIT AUCUNE PUISSANCE, ET LE CONFONDANT EST PLUS
PROFOND QUE LE DEFAUT QUE J'AVAIS NOMME.

S'insere apres journal_delta_37_G6_ilots.md (e07ddbb3...). Repond a
reponse_delta37_machine2.md. Algebre pure sur out/m10_results.json.

---

## 38.1 LA REFUTATION PRINCIPALE : JE RETIRE MA RETRACTATION

Le S37.2 concluait : "l'hypothese regionale n'est pas soutenue par les donnees
qui existaient deja. Je la retire comme hypothese privilegiee."
**C'ETAIT UNE FAUTE DE LECTURE, ET C'EST LA MEME QUE CELLE QUE LA CAMPAGNE
S'INTERDIT DEPUIS C2.** Machine 2 chiffre la puissance du plan par
permutation : |r| critique a 5 % vaut 0.501 sur ces 16 points ; une
correlation VRAIE de 0.30 serait invisible huit fois sur dix.
Ne pas avoir vu un signal dans un plan aveugle n'est pas l'avoir refute. J'ai
pris un NON CONCLUANT pour une refutation -- l'exacte symetrie de la faute
consistant a prendre un non concluant pour un appui, que j'avais moi-meme
signalee sur P-M10b au S32.
    ENONCE CORRIGE : les 64 balayages de M10 ne departagent PAS les deux
    hypotheses, et ne peuvent pas les departager. Aucune des deux n'est
    retiree ; aucune n'est privilegiee.

## 38.2 MA CORRELATION -0.30 : DEFINITION FOURNIE, PUIS RETIREE

Machine 2 ne peut pas reproduire mon -0.30 et a raison : je n'avais pas ecrit
la coupure d'ordre. Retrouvee -- omax = 14 sur la plage [1.1, 3.0] :
    omax 12 : -0.3874 | omax 13 : -0.3568 | omax 14 : -0.3038 | omax 15 : -0.1585
La definition est fournie. **Le nombre est RETIRE quand meme**, et pour la
raison de machine 2 : les rationnels sont denses, la coupure est arbitraire, et
la correlation CHANGE DE SIGNE sur la plage des coupures plausibles (+0.047 a
l'ordre 6, -0.409 a l'ordre 10, -0.126 a l'ordre 16). Une quantite dont le
signe depend d'un parametre non declare n'est pas une mesure.
MEME FAMILLE QUE LA LIGNE "3 + 4 + 3" DU S35.3, retiree au S36.1 : publier un
nombre qu'on ne peut pas refaire. Deuxieme occurrence de ma part dans le
dossier de conception, et c'est une de trop.
FORME NORMALISEE ADOPTEE : la distance se rapporte au RAYON que R-2 declare
pour l'ordre en cause, jamais nue. Le protocole contient deja l'echelle ; s'en
passer, c'est ignorer la regle que le gel declare.

## 38.3 LE CONTRE-EXEMPLE 1.45 / 1.55 : SUR-INTERPRETE

J'ecrivais qu'il refute l'hypothese resonante. Il refute l'hypothese resonante
SYMETRIQUE. Une separatrice de resonance est asymetrique -- la campagne le sait
depuis M5 : le cote raide du canyon est TOUJOURS a droite. Deux points a egale
distance de 3:2, l'un dessous et l'autre dessus, n'ont donc aucune raison de se
ressembler. Correction de machine 2 adoptee.

## 38.4 MON CORRECTIF D'INSTRUMENT NE MARCHAIT PAS

Le S37.3 proposait de consigner min(s explosif)/s* sur chaque ligne. Machine 2
montre que cette quantite est BORNEE PAR LA GARDE ELLE-MEME : une ligne non
exclue n'a, par definition de G6, aucune explosion sous 0.98 s*, et s* explose.
La marge vaut donc necessairement [0.98, 1.00], soit 3.7 a 5.1 pas de balayage.
**Je remplacais un entier a quatre valeurs par un continu a quatre valeurs.**
Le geste (regle 13 : rapporter la quantite, pas le franchissement) etait juste ;
la quantite choisie ne portait pas le signal.
ET J'AI DIT UNE CHOSE FAUSSE : "sur 64 lignes, UNE SEULE porte une marge
lisible". Faux. `premiere_retombee_en_s` est renseignee sur 33 des 64 lignes,
avec 33 valeurs distinctes entre 1.00005 et 1.05000. J'avais lu le seul champ
`explosion_sous_0.98s` et generalise. Erreur de lecture, pas d'inference.

## 38.5 LE CONFONDANT EST LE VRAI DEFAUT, ET LE CORRECTIF EST DANS LE BALAYAGE

Machine 2 etablit le point le plus profond du dossier : le balayage est
np.linspace(LO0, 1.05 s*, 192), donc son PAS DEPEND DE s*, donc de w2.
    pas relatif : 0.00390 a 0.00542 -- facteur 1.39, le plus fin a GAUCHE
    correlation(pas relatif, w2) = +0.8619
**"Ilots contre w2" et "ilots contre finesse de l'instrument" sont LE MEME
TEST.** Le contraste bord/reste que j'examinais (1.33) n'est pas separable de
l'inhomogeneite de resolution qui l'accompagne (1.17). Ni le regional ni son
absence ne sont identifiables ainsi.

LE CORRECTIF N'EST PAS UNE VARIABLE DE PLUS, C'EST LA GEOMETRIE DU BALAYAGE.
Et le JSON montre ou les 192 points sont depenses : 10 a 13 tombent dans
[s*, 1.05 s*] -- la fenetre ou vit le phenomene -- soit 6 %. Les 94 % restants
explorent [LO0, s*], ou la garde a deja etabli qu'il n'y a rien, sinon la ligne
serait exclue.
    PROPOSITION POUR p=4, a cout de points IDENTIQUE (192) :
      DEUX balayages a PAS RELATIF CONSTANT, 96 + 96 :
        grossier [LO0, 0.90 s*], 96 points  -> le test BLOQUANT de G6 est
                                                integralement conserve ;
        fin      [0.90 s*, 1.05 s*], 96 pts -> pas relatif 0.00158, CONSTANT
                                                sur les 64 lignes.
    GAIN : x3.2 de finesse dans la fenetre utile, et surtout
    correlation(pas relatif, w2) = 0 PAR CONSTRUCTION. Le confondant
    disparait, il n'est pas corrige apres coup.
C'est le meme principe que la regle 11 -- comparer par valeur et non par
etiquette -- transporte a la RESOLUTION : un instrument dont la finesse varie
avec la variable qu'on etudie ne mesure pas cette variable.

## 38.6 R-2' : LA CONTINUATION GEOMETRIQUE, ET POURQUOI ELLE N'EST PAS UN
##      DEPLACEMENT DE POTEAU

Machine 2 propose d'etendre R-2 aux ordres 9-12 avant toute mesure p=4. Elle
avait ecrit au S36.3 qu'un tel geste serait "deplacer un poteau apres avoir vu
ou la balle est tombee". La tension est reelle et il faut la lever, pas la
contourner.
ELLE SE LEVE SI LA CONTINUATION EST DERIVEE ET NON CHOISIE. R-2 declare
0.12 (ordre <= 6) puis 0.03 (ordres 7-8) : un rapport de 4 par PAIRE d'ordres,
puis une TRONCATURE BRUTALE a 0 au-dela de 8. La continuation qui n'est
ajustee sur rien est la poursuite du meme rapport :
        0.12 (o<=6) | 0.03 (o 7-8) | 0.0075 (o 9-10) | 0.001875 (o 11-12)
Elle ne supprime pas un poteau : elle supprime une DISCONTINUITE que R-2
avait laissee, et elle est entierement determinee par les deux nombres deja
geles au gel M10 v8.

CE QU'ELLE FAIT, VERIFIE. Appliquee aux dix points du fit R-2 de M10, elle en
retire UN et un seul :
    w2 = 1.2500, a 0.0000 de 5:4 (ordre 9), sous le rayon 0.0075
    fit R-2' = 1.30, 1.70, 1.80, 2.15, 2.30, 2.45, 2.60, 2.75, 2.85
    amputation G7 REELLE = les memes neuf points -- IDENTIQUES.
**La regle prolongee retire A PRIORI le point que la garde a retire A
POSTERIORI.** n = 1 et post-hoc : c'est une coincidence a consigner, pas une
preuve, et je l'ecris comme telle.
CE QU'ELLE COUTE AUX CANDIDATES : C5 perd exactement son point pose sur 5:4 et
garde ses dix autres ; C1 en perd deux. Aucune ne descend sous le plancher de
huit de G7. Elle resout donc, sans deplacer le bord gauche, le probleme que le
S37 avait laisse ouvert -- le premier point de la famille est w2 = 1.25 = 5:4
exactement quels que soient lambda et N, et R-2' l'ecarte du fit tout en le
gardant MESURE comme temoin de G6.
CONDITION QUE J'ATTACHE : R-2' se gele AVANT que la grille p=4 soit choisie, et
elle ne sera PAS ajustee si elle exclut un point genant. Si elle l'est, elle
redevient un poteau deplace.

## 38.7 ENTREE 6 : JE TRANCHE, ET JE NE CHOISIS PAS UNE LARGEUR

Machine 2 signale que 0.12 designe C5, sa propre candidate, et me laisse
trancher. La declaration de conflit est la bonne conduite ; la reponse est de
ne pas choisir.
    ENTREE 6 GELEE : R_fen est evaluee aux DEUX largeurs que le protocole
    contient DEJA -- 0.03 et 0.12, les rayons de R-2, anterieurs a toute
    candidate -- et la grille retenue doit etre acceptable AUX DEUX. Aucune
    largeur nouvelle n'est introduite, donc aucune ne peut etre choisie pour
    son gagnant.
Cela rend le classement insensible aux trois basculements du S36 : une grille
qui domine aux deux largeurs domine, une grille qui n'y arrive pas est
ecartee quel que soit le pari sur la largeur vraie.

## 38.8 CE QUI RESTE, DANS L'ORDRE

  1. geler R-2' (38.6) et l'entree 6 (38.7) -- tous deux anterieurs a toute
     grille candidate ;
  2. recalculer C1, C5 et les variantes sous R-2', aux deux largeurs ;
  3. porter au script p=4 : le double balayage a pas relatif constant (38.5),
     la regle 14 (refit), et la consignation de la retombee AUX 64 lignes ;
  4. geler la LECTURE qui departagera regional / resonant, avec son seuil,
     en sachant desormais que le plan doit etre dimensionne POUR elle -- le
     S38.1 montre qu'un plan a 16 points et compte entier ne peut pas la
     porter ;
  5. rediger le pre-enregistrement.
Rien de tout cela ne demande une mesure.

=== FIN DU DELTA 38 ===
