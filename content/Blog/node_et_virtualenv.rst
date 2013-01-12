=============================================
Installer des paquets Node.js dans virtualenv
=============================================

:date: 2012-12-14

:tags: virtualenv, node.js


Virtualenv est un outil formidable. Si vous ne l'utilisez pas encore il faut vous y mettre absoluement !
Pour résumer rapidement c'est un outil qui sert à créer des environnements de développements python isolés les uns des autres.

Il m'arrive d'avoir besoin de modules d'autres languages que python notemment pour le développement web.

Ce qui m'interresse aujourd'hui, c'est d'obtenir un environnement virtualisé avec virtualenv et des modules node.js (stylus jade et coffee-script)

Mise en place de l'environnement
================================

Tout d'abord, il faut mettre en place un environnement virtuel avec virtualenv (j'utilise personnellement virtualenvwrapper_)

.. code:: console
    
    $ mkdir devnode
    $ mkvirtualenv devnode

Et c'est tout !
Enfin... pour l'environnement de developpement seulement. Mais la suite est tout aussi triviale.

Configuration des « hooks »
===========================

virtualenvwrapper propose des fichiers qui seront lus apres l'installation de l'environnement (postinstall) et surtout celui qui nous intéresse après l'activation de l'environnement (postactivate).
Il nous suffit alors de le modifier afin d'y inclure certaines directives :

.. code:: console

    $ workon devnode
    $ cdvirtualenv bin

Editez ensuite le fichier postactivate et y ajouter les lignes suivantes :

.. code:: bash

    # node.js packages
    export npm_config_prefix=$VIRTUAL_ENV

et dans le fichier predeactivate :

.. code:: bash

    # remove node.js config
    export npm_config_prefix=""

Si virtualenv est configuré correctement il vous suffit de lancer les commandes d'installation des paquets habituelles :

.. code:: console

    $ npm install -g stylus jade coffee-script

Notez l'utilisation de l'option -g (installation globale).

Et voilà. Rien de plus compliqué que ça ! Et ça fonctionne également avec les gem ruby etc...

Comme ce billet le laisse entrevoir, je parlerai bientôt des préprocesseurs css (stylus) html (jade) et javascript (coffee-script).

.. _virtualenvwrapper: //www.doughellmann.com/projects/virtualenvwrapper/
