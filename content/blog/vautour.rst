===========================
Vautour: thème pour pelican
===========================

:tags: pelican, blog, vautour

:date: 2013-01-20

Ce blog est construit grâce à Pelican_. Le thème par défaut ( qui s'appelle notmyidea ) ne me convenait pas. J'ai donc commencer par modifier ce thème pour finalement repartir de zéro ou presque.

Point de départ
===============

Je suis parti du template « simple » sans CSS et me suis imposé certaines contraintes :

    - Ressources compréssées et compatibles avec des licences libres
    - Servir en un minimum de fichiers
    - Ne pas me servir des extensions propriétaires des navigateurs ( les -webkit- -moz- -o- )
    - Ne pas imposer google aux visiteurs ( aucune ressource servie par google )

Le but étant de fournir un site le plus réactif et léger possible.

J'ai utilisé Stylus_ pour générer le CSS. En effet il me permet de construire mes CSS en plusieurs fichiers distincts mais de générer une sortie dans un unique fichier CSS compréssé. De plus l'utilitaire fourni une fonction de surveillance de fichier : quand le fichier surveillé est modifié il est compilé instantanément ( ce qui est un énorme avantage quand on développe pour le web ).

Pour la police de caractères, il s'agit de Jura_ sous licence OFL servit par openfontlibrary_ ( pour éviter google web font ), la texture de fond de la page est grid_ trouvée sur subtlepatterns_ et l'echantillon d'icones est issu d' entypo_ sous licence CC-BY-SA.
Pour les icones j'ai généré un subset avec les seules icones qui m'interessent grace à l'application d'icomoon_ pour réduire la taille du fichier servi.

La suite
========

J'ai construis ce thème pour mes besoins personnels et il est donc très loin de couvrir tous les usages de Pelican. De plus, je ne l'ai testé que sur Firefox et Opera.

Mon objectif pour la suite est de le rendre pleinements compatible sans utiliser des tricks ( commes les commentaires conditionnels ou des attributs non standardisés ) et d'englober le maximum d'usages.

Choix de licence
================

J'ai choisi de placer le code de vautour_ sous licence MIT donc amusez-vous !


.. _entypo: //entypo.com
.. _icomoon: //icomoon.io/app
.. _grid: //subtlepatterns.com/grid
.. _subtlepatterns: //subtlepatterns.com
.. _Jura: //openfontlibrary.org/en/font/jura
.. _openfontlibrary: //openfontlibrary.org
.. _Stylus: //learnboost.github.com/stylus
.. _Pelican: //blog.getpelican.com
.. _vautour: //github.com/fdovero/vautour
