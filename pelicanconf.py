#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Fabien Dovero"
SITENAME = u"/dev/log"
SITESUBTITLE = u"Journal d'un dev"
SITEURL = ''

THEME = 'vautour'


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

LICENSE = 'CC-BY-SA'

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),)

# Social widget
SOCIAL = (('twitter', '//twitter.com/azhagg'),
          ('github', '//github.com/fdovero'),)

MENUITEMS = (('Home', '/'),)

TEMPLATE_PAGES = {'404.html': '404.html'}

FILES_TO_COPY = (('extra/CNAME', 'CNAME'),)

DEFAULT_PAGINATION = False

DISPLAY_PAGES_ON_MENU = True
