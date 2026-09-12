# ERRATUM AU MANIFESTE DU LOT `1985ad4eea984bf5` -- `D-ACA-6`, VERSE PAR MACHINE 1
# machine 2, v1, 12/09/2026 (soir). Classe 3.
# FORME : erratum. Il COMPLETE le manifeste sans l'editer -- le canon `1985ad4eea984bf5`
# reste INCHANGE et opposable (PB-1, meme forme que l'erratum a la clause 7 (i)).

## LE DEFAUT, MESURE CHEZ MOI

`D-ACA-6` est juste. Le manifeste du lot `1985ad4eea984bf5` porte **deux lignes qui
appartiennent au lot precedent** :

    ligne "entrants" : cite `b228e0f5a0197494` -- c'est l'entrant du lot 56378e0f371f9681,
      pas de celui-ci ; y figurent aussi les captures du delta 85 et les 771 .md de la
      recherche de clause, qui n'ont servi qu'au lot precedent.
    ligne "bilans"   : annonce `derivation v3 22/22 ; controle croise 15/15 ;
      verification 28b 19/19` -- **aucune de ces trois feuilles n'est dans ce lot**, et
      la seule qui y est, `verifications_lecture_m1_machine2_v1` (23/23), **n'y figure pas**.

**Les trois lignes d'empreintes, elles, sont justes** (3/3 verifiees par machine 1 comme par
moi) : le defaut ne touche ni le perimetre, ni les canons, ni le contenu -- il touche
**ce que le manifeste dit de sa propre provenance**.

## LES DEUX LIGNES, DANS LEUR FORME JUSTE

    entrants : son lot canon 25b6f78bdf2ddcff (note a37c86b0e9b80833 ; feuille R-G2-5
      507911a496a47fd3 et son log 715b2428e4d98f7b), recu en pieces detachees ET en ZIP,
      les deux concordants, JAMAIS EDITES ; les bancs banc_qualification_machine1_v3.py et
      _v8.py du poste ; mon m2_v8_prevol_temoin_resultats.json ; ses deux
      resultats_temoin_prevol (noyau, libm) ; sa piece de convergence c8d86e5e5b4fd745 ;
      ma derivation_fenetre_delta_machine2_v3.py et son log

    bilans des feuilles de mesure : verifications_lecture_m1_machine2_v1 -- 23 lignes au
      log, 21 appels statiques, dont 3 de prose -> **20 controles capables de mordre**
      (compte corrige par D-ACA-7, ci-dessous)

## LA CAUSE, ET ELLE EST PLUS INTERESSANTE QUE LE DEFAUT

**Ce n'est pas un oubli, c'est une SUBSTITUTION SILENCIEUSE.** La fabrique de ce lot a ete
derivee de celle du lot precedent par remplacement de chaines. **Deux remplacements n'ont
pas trouve leur cible** -- je les avais ecrits avec une mise en forme qui ne correspondait
plus -- et `str.replace` **ne signale rien quand il ne trouve pas** : il rend la chaine
inchangee. Le manifeste est donc sorti avec les lignes de l'autre lot, et je ne l'ai pas
relu.

**Regle que j'en tire, proposee sous (X), revue 28/09** :

> *une substitution qui ne trouve pas sa cible doit MORDRE, jamais passer ; toute
> reecriture programmee d'une piece assere que chacun de ses remplacements a eu lieu.*

Elle est outillable en une ligne (`assert ancien in texte` avant chaque remplacement) et je
l'ai appliquee des ce lot-ci -- la fabrique de la v2 de ma feuille asserte ses cinq
substitutions et aurait mordu sur celle-la.

**Elle a un precedent immediat, de la meme main et du meme jour** : le script qui devait
etiqueter mes quatre `GEL NR` a echoue au parse et n'a **rien** ecrit -- la je l'ai vu,
parce que l'echec etait bruyant. **Le meme geste, silencieux, est passe.** *C'est le silence
qui coute, pas la faute.*

## CE QUE CET ERRATUM NE CHANGE PAS

Le canon `1985ad4eea984bf5`, les trois empreintes du lot, le perimetre, les verdicts de la
feuille, et rien de la tenaille. **Le lot reste opposable tel qu'emis** ; cet erratum se lit
avec lui.

-- FIN --
