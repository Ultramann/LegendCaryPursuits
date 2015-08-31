#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cary Goltermann'
SITENAME = u'LegendCaryPursuits'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']

MD_EXTENSIONS = ['codehilite']

TIMEZONE = 'America/Denver'

DEFAULT_LANG = u'en'

THEME = './themes/myidea'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('DataTau', 'http://datatau.com/'),
         ('yHat', 'http://blog.yhathq.com'),
         ('DataElixir', 'http://dataelixir.com/'),
         ('DataScienceWeekly', 'http://www.datascienceweekly.org'),
         ('LifeHacker', 'http://lifehacker.com'),
         ('Gizmodo', 'http://gizmodo.com/'))

# Social widget
SOCIAL = (('github', 'http://github.com/Ultramann'),
          ('linkedin', 'https://www.linkedin.com/in/carygoltermann'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
