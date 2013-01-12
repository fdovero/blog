#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Fabien Dovero"
SITENAME = u"Journal d'un dev"
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),)

# Social widget$
SOCIAL = (('twitter', 'http://twitter.com/azhagg'),
          ('github', 'http://github.com/fdovero'),)

DEFAULT_PAGINATION = False

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = ((u'À propos', 'pages/a-propos.html'),
             ('Accueil', '/'),
             ('Projets', 'pages/projets.html'),)
