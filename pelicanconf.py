#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wallace Coelho'
SITENAME = 'Wallace Coelho'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/wac2007', 'fa-facebook'),
          ('Twitter', 'https://twitter.com/wac2007', 'fa-twitter'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# THEME RELATED
# NEST Template
THEME = 'themes/nest'
SITESUBTITLE = u'Magia e Tecnologia'
# Minified CSS
NEST_CSS_MINIFY = False
# Add items to top menu before pages
MENUITEMS = [('Homepage', '/'),('Categories','/categories.html')]
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = ''
NEST_HEADER_LOGO = '/image/logo.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archives', '/archives.html'),('Tags','/tags.html'), ('Authors','/authors.html')]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Links'
NEST_COPYRIGHT = u'&copy; Wallace Coelho 2016'
# Footer optional
NEST_FOOTER_HTML = ''
# index.html
NEST_INDEX_HEAD_TITLE = u'Homepage'
NEST_INDEX_HEADER_TITLE = u'Wallace Coelho'
NEST_INDEX_HEADER_SUBTITLE = u'Magia e Tecnologia'
NEST_INDEX_CONTENT_TITLE = u'Últimos Posts'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Posts'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts'
NEST_ARCHIVES_HEADER_TITLE = u'Posts'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Todos os Posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Posts'
# article.html
NEST_ARTICLE_HEADER_BY = u'Por'
NEST_ARTICLE_HEADER_MODIFIED = u'modificado'
NEST_ARTICLE_HEADER_IN = u'na categoria'
# author.html
NEST_AUTHOR_HEAD_TITLE = u'Posts por'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts por'
NEST_AUTHOR_HEADER_SUBTITLE = u'Posts'
NEST_AUTHOR_CONTENT_TITLE = u'Posts'
# authors.html
NEST_AUTHORS_HEAD_TITLE = u'Lista do Autor'
NEST_AUTHORS_HEAD_DESCRIPTION = u'Lista do Autor'
NEST_AUTHORS_HEADER_TITLE = u'Lista do Autor'
NEST_AUTHORS_HEADER_SUBTITLE = u'Listados por Autor'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categorias'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Listado por Categorias'
NEST_CATEGORIES_HEADER_TITLE = u'Categorias'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Posts por Categorias'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Categoria'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Categoria'
NEST_CATEGORY_HEADER_TITLE = u'Categoria'
NEST_CATEGORY_HEADER_SUBTITLE = u'Categoria'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Anterior'
NEST_PAGINATION_NEXT = u'Próximo'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Tags'
NEST_TAG_HEAD_DESCRIPTION = u'Tags'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tags'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Lista de Tags'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Lista de Posts por Tags'
NEST_TAGS_CONTENT_TITLE = u'Lista de Posts'
NEST_TAGS_CONTENT_LIST = u'marcado pela tag'
# Static files
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.svg': {'path': 'logo.svg'}
}