# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Paul Brabban'
SITENAME = u'Sheffield ML'
#SITEURL = 'https://sheffieldml.org.uk'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Sheffield Meetups', 'http://sheffieldgeeks.org.uk'),
         ('Python Sheffield', 'https://twitter.com/pysheff'),
         ('SheffieldR', 'http://www.meetup.com/SheffieldR-Sheffield-R-Users-Group/'),
         ('SheffieldML on OpenTechCalendar', 'https://opentechcalendar.co.uk/group/474-sheffieldml'))

# Social widget
SOCIAL = (('shef_ml', 'https://twitter.com/shef_ml'),
          ('shefml', 'https://github.com/shefml'),
          ('slack', 'https://sheffield.digital/slack/'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Home', '/'),
    ('About', '/pages/about.html'),
    ('Participate', '/pages/participate.html'),
    ('Sponsors', '/pages/sponsors.html')
)

THEME='../pelican-themes/plumage'

#GITHUB_URL='https://github.com/Shef_ML'
GOOGLE_ANALYTICS='UA-112392981-1'
TWITTER_USERNAME='Shef_ML'
