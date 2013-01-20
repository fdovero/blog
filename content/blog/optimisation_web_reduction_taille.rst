==================================================================
Optimiser un site web : réduire la taille des ressources statiques
==================================================================

:date: 2013-01-12

:tags: web, optimisation, bonne pratique

La rapidité du web est le maitre mot depuis que les accès haut débit se sont démocratisés.
Aujourd'hui plus que jamais, la réactivité d'un site web est un objectif à atteindre surtout que ces mêmes sites ont tendance à enfler.
Google en fait même un critère de qualité pour son algorithme d'indexation.
J'ai été confronté a cette problématique et je vais présenté dans une série de billets différentes techniques d'optimisation, de la plus évidente à la plus tordue !
Cette série est amenée à évoluer.

Dans ce premier billet de la série je vais donc parler  de ce qui est évident pour tout développeur web qui veut accélérer le rendu de son site : réduire la taille des ressources !

Réduire le Javascript
=====================

Il existe plusieurs réducteur de javascript. J'aime la simplicité et la puissance de uglifyjs_.
Pour l'installer :

.. code-block:: console

    $ npm install -g uglify-js

Ensuite pour compresser le javascript :

.. code-block:: console

    $ uglifyjs -c app.js -o app.min.js

Réduire les CSS
===============

J'utilise stylus_ comme préprocesseur CSS. La commande stylus propose un paramètre pour compresser la sortie

.. code-block:: console

    $ npm install -g stylus
    $ stylus --compress app.styl

Et comme j'aime les solutions tordues, on peut également passer un css pour le transformer en fichier stylus et compresser le css en sortie !

.. code-block:: console

    $ stylus --css app.css & stylus --compress app.styl

Si vous préférez les solutions simples il existe csso_ qui rempli cette tâche à merveille :

.. code-block:: console

    $ npm install -g csso
    $ csso app.css app.min.css

Et voilà ! 

Réduire les images
==================

Les images sont les ressources le plus lourdes à transférer. Pourtant il y a un moyen simple et sans perte de réduire leur taille de 50% en moyenne. En effet les images embarquent toutes sortes de tags qui prennent une place non négligable.

Pour optimiser des PNG il existe optipng_ et jpegoptim_ pour les JPEG !

.. code-block:: console

   $ optipng -o 7 ./images

Cas des « icon fonts »
======================
J'utilise de plus en plus ces polices d'icones (grâce à la propriété @font-face de CSS3). Seulement je n'utilise jamais toutes les icones proposées. J'aimerai pouvoir récupérer uniquement les icones qui m'interessent afin de réduire la taille des fichiers de la fonte et du css associé.
Pour `font awesome`_ il existe icnfnt_ qui justement permet de se constituer son fichier aux petits ognions.


.. _uglifyjs: //lisperator.net/uglifyjs/ 
.. _stylus: //learnboost.github.com/stylus/
.. _csso: //github.com/css/csso
.. _optipng: //optipng.sourceforge.net/
.. _jpegoptim: //www.kokkonen.net/tjko/projects.htm
.. _`font awesome`: //fortawesome.github.com/Font-Awesome/ 
.. _icnfnt: //icnfnt.com
