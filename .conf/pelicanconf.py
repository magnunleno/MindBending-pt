#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

### Base config ########################################### {{{
AUTHOR = 'Magnun'
SITENAME = u'Mind Bending'
SITEURL = 'http://localhost:8000'
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt'
LANG = 'pt_BR.UTF-8'
DEFAULT_PAGINATION = 10
TYPOGRIFY = True
# }}}

#### Social ############################################### {{{
GITHUB_URL = 'http://github.com/magnunleno/'
LINKS =  (
          ('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          )
SOCIAL = (
        ('envelope', 'mailto: &#109;&#105;&#110;&#100;&#098;&#101;&#110;&#100;&#105;&#110;&#103;&#098;&#108;&#111;&#103;&#064;&#103;&#109;&#097;&#105;&#108;&#046;&#099;&#111;&#109;'),
        ('github', 'https://github.com/magnunleno'),
        ('twitter', 'https://twitter.com/magnunleno'),
        ('google+', 'http://plus.google.com/102063745956138544914'),
        ('facebook', 'http://facebook.com/MindBendingBlog'),
        ('stack-overflow', 'http://stackoverflow.com/users/498227'),
        ('gittip', 'https://www.gittip.com/magnunleno/'),
        ('linux', 'http://linuxcounter.net/user/477991.html'),
        )
GPLUS_AUTHOR = "https://plus.google.com/+MindbendingOrg?rel=author"
GITHUB_USER = 'magnunleno'
# }}}

#### Site items ########################################### {{{
MENUITEMS = (
        ('Projetos', 'projetos'),
        ('Series', (
            ('Bibliotecas em C', 'series/bibliotecas-em-c'),
            ('Curso de Filosofia GNU', 'series/curso-de-filosofia-gnu'),
            ('Destaques da Pycon 2011', 'series/destaques-da-pycon-2011'),
            ('Dobrando o Gnome Keyring Com o Python', 'series/dobrando-o-gnome-keyring-com-o-python'),
            ('Git Para Todos', 'series/git-para-todos'),
            ('Instalando e Configurando o Arch Linux', 'series/instalando-e-configurando-o-arch-linux'),
            ('Migrando Para o Pelican', 'series/migrando-para-o-pelican'),
            ('Python e UDisks', 'series/python-e-udisks'),
            )
        ),
        ('Contato', 'contato'),
        ( 'Sobre', (
            ("Hack 'n' Cast", 'sobre-hack-n-cast'),
            ('Magnun', 'sobre-mim'),
            ),
        ),
        )
SITE_LINKS = (
        ("Home", ""),
        ("Autores", "authors"),
        ("Arquivos", "archives"),
        ("Categorias", "categories"),
        ("Tags", "tags"),
        ("RSS", "feeds.rss"),
        )
AUTHORS = {
        'Magnun' : {
            'avatar' : '/images/magnun_avatar.jpg',
            'bio' : 'Engenheiro de telecomunicações por formação, mas ' +\
                    'trabalha com suporte à infraestrutura GNU/Linux, ' +\
                    'e nas horas vagas é Programador OpenSource (Python e C) '+\
                    'desenhista e escritor do Mind Bending Blog.',
            'links' : (
                ('Twitter', 'https://twitter.com/magnunleno'),
                ('Google+', 'https://plus.google.com/+MindbendingOrg?rel=author'),
                ('GitHub', 'https://github.com/magnunleno'),
                ('Facebook', 'https://www.facebook.com/MindBendingBlog'),
                )
            },
        'Fernando Almeida' : {
            'avatar' : '/images/avatars/fernando-almeida.jpg',
            'bio' : 'Formado em Gestão da Tecnologia da Informação, divide ' +\
                'seu dia entre dois mundos: A vida de “engravatado” como ' +\
                'analista de risco e broker para empresa de Leasing OPEX ' +\
                'e a vida de desenvolvedor de sistemas embarcados para ' +\
                'empresa de telecomunicações. Grande entusiasta do ' +\
                'movimento OpenSource, aproveita suas horas vagas para ' +\
                'um bom passeio de moto com sua esposa.',
            'links' : (
                ('Facebook', 'http://facebook.com/fernando.ti'),
                ('LinkedIn', 'http://br.linkedin.com/in/fealmeida'),
                ('Email', 'mailto: fernandoalmeida@ig.com.br'),
                ('GitHub', 'https://github.com/fer-almeida'),
                ),
            },
        }
# }}}

#### Site URL writing ##################################### {{{
ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}/index.html"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

SERIES_URL = "series/{slug}"
SERIES_SAVE_AS = "series/{slug}/index.html"

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'
# }}}

#### Plugins  ############################################# {{{
PLUGIN_PATHS = ['./plugins']
PLUGINS = [
        'better_figures_and_images',
        'pelican-youtube',
        'pelican-vimeo',
        'summary', 
        'series',
        'archive-podcast',
    ]
SUMMARY_END_MARKER = "<!-- more -->"
RESPONSIVE_IMAGES = True
# }}}

#### Theme settings ####################################### {{{
JINJA_EXTENSIONS = ['jinja2.ext.do']
THEME = "./boothack"
BOOTSTRAP_THEME = 'readable'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False

TAG_CLOUD_STEPS = 8

SITELOGO = '/images/MB_Logo_2014.png'
SITELOGO_SIZE = '20px'

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True

CUSTOM_CSS = 'custom.css'
PYGMENTS_STYLE = 'monokai'

HIDE_SIDEBAR_IN = ['article', 'page', 'archives']
SIDEBAR_ELEMENTS = ['condensed', 'links']
SIDE_BRAND_ELEMENTS = []

SITE_BANNER_BACKGROUND_IMAGE = "/images/gnome-bkg.jpg"
SHOW_SITE_BANNER_IN = ['article', 'page']
SHOW_SITE_BANNER_IN = 'all'
SITE_BANNER_ELEMENTS = ['logo', 'name', 'social']
SITE_BANNER_BACKGROUND_COLOR = "#eeeeec"

NAVBAR_ELEMENTS = ['brand-dropdown', 'menu-items', 'search']
FAVICON = 'favicon.ico'
# }}}

#### Extra and Static ##################################### {{{
STATIC_PATHS = [
    'audio', 
    'images', 
    'codes',
    'extra/robots.txt', 
    'extra/favicon.ico',
    'extra/custom.css',
    ]
EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/favicon.ico': {'path': 'favicon.ico'},
        'extra/custom.css': {'path': 'custom.css'},
        }
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
# }}}
