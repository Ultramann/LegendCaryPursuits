#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cary Goltermann'
SITENAME = u'LegendCaryPursuits'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

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
         ('DataScienceWeekly', 'http://www.datascienceweekly.org'))

# Social widget
SOCIAL = (('github', 'http://github.com/Ultramann'),
          ('linkedin', 'https://www.linkedin.com/pub/cary-goltermann/85/b19/1'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
