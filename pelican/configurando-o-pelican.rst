Configurando o Pelican
######################
:date: 2014-03-13 15:14
:category: Pelican
:tags: pelican, configuração, blog
:image: /images/pelican/pelican_blueprint.png
:series: Migrando Para o Pelican

Conforme destacado `nesses`_ `outros`_ artigos, agora estou usando o `Pelican`_. Mas simplesmente instalá-lo não é o suficiente, é necessário customizá-lo para atender suas necessidades. Para isso, hoje vamos ver como configurar o Pelican através do comando `pelicanconf.py`.

.. image:: {filename}/images/pelican/pelican_drawing.jpg
        :target: {filename}/images/pelican/pelican_drawing.jpg
        :alt: Pelican
        :align: center

É importante lembrar que **todas as configurações** estão `documentadas aqui`_ e eu não vou poder explicar todas, vou passar rapidamente pelas mais importantes e as que eu precisei modificar.

.. more

Configuração Básica
-------------------

Primeiro confirme a configuração básica do Pelican, isto é, `SITENAME`, `AUTHOR`, `TIMEZONE` e paginação:

.. code-block:: python

        AUTHOR = u'Magnun'
        SITENAME = u'Mind Bending'
        TIMEZONE = 'America/Sao_Paulo'
        DEFAULT_PAGINATION = 10

Para uma lista completa dos fusos existentes (e seu respectivo TZ) veja `este artigo da Wikipédia`_.


Configurando Links e Redes Sociais
----------------------------------

É padronizado na configuralçao do Pelican uma uma lista com as redes sociais do site (`SOCIAL`), seu perfil no GitHub (`GITHUB_URL`), no Twitter (`TWITTER_USERNAME`) ou sites que você recomenda (`LINK`).

.. code-block:: python

        # Github Profile
        GITHUB_URL = 'http://github.com/magnunleno/'

        # Twitter
        TWITTER_USERNAME = 'mind_bend'

        # Social widget
        SOCIAL = (
                ('github', 'https://github.com/magnunleno'),
                ('twitter', 'https://twitter.com/mind_bend'),
                ('google+', 'http://plus.google.com/102063745956138544914'),
                ('facebook', 'http://facebook.com/MindBendingBlog'),
                ('stack-overflow', 'http://stackoverflow.com/users/498227'),
                ('gittip', 'https://www.gittip.com/magnunleno/'),
                )

        # Blogroll
        LINKS =  (
                  ('Pelican', 'http://getpelican.com/'),
                  ('Python.org', 'http://python.org/'),
                  ('Jinja2', 'http://jinja.pocoo.org/'),
                  )


Configurando Seu Feed
---------------------

Na documentação oficial do Pelican, exitem diversas configurações para o seu feed, seja ele RSS ou Atom, para uma lista completa de configurações veja a seção `Feed Settings`_.

Mas as principais configurações que você talvez precise alterar são:

#. `FEED_ALL_RSS` e `FEED_ALL_ATOM`: Que define o nome do arquivo onde será armazenado o feed de todos os seus artigos, em RSS ou Atom;
#. `CATEGORY_FEED_RSS` e `CATEGORY_FEED_ATOM`: Que definne o nome do arquivo onde será armazenado o feed de cada categoria (o nome da categoria é definido por `%s`), seja ele RSS ou Atom.

Abaixo as minhas configurações:

.. code-block:: python

        FEED_ALL_RSS = 'feeds.rss'
        CATEGORY_FEED_RSS = 'feeds/%s.rss'
        FEED_ALL_ATOM = 'feeds.atom'
        CATEGORY_FEED_ATOM = 'feeds/%s.atom'
        FEED_USE_SUMMARY = True


Customização do Menu e Tag Cloud
--------------------------------

Estas configurações estão intimamente ligadas a implementação do tema que você está usando, ou seja, elas podem vir a não funcionar caso o autor do tema não as tenha implementado corretamente.

As seguintes configurações definem se será exibido (ou não) links para categorias e páginas no menu do seu site:

.. code-block:: python

        DISPLAY_CATEGORIES_ON_MENU = False
        DISPLAY_PAGES_ON_MENU = False


Já as configurações abaixo definem o tamanho da *tagcloud* e a quantidade de variações de tamanho de fonte:

.. code-block:: python

        TAG_CLOUD_STEPS = 8
        TAG_CLOUD_MAX_ITEMS = 100

Configurando Temas e Plugins
----------------------------

Este tema é extremamente extenso e não vou cobrir com muitos detalhes neste momento. Vou apenas demonstrar como ativar plugins e selecionar um tema par seu site:

.. code-block:: python

        # Plugins 
        PLUGIN_PATH = './.plugins'
        PLUGINS = [
                'gzip_cache', 
                'sitemap',
                'related_posts',
            ]

        THEME = "./.themes/boothack"

Convenientemente o pelican tem uma configuração chamada `PLUGIN_PATH` (seu uso não é obrigatório), responsável por indicar onde todos os plugins estão armazenados. Sendo possível, em seguida, apenas informar uma lista (ou tupla) contendo os nomes dos plugins que você deseja ativar.

Uma vez que só é possível ativa um tema por vez no Pelican, os desenvolvedores acharam desnecessário a definição de uma variável similar ao `PLUGIN_PATH` para os temas. Desta forma, para ativar um tema para seu site, basta informar seu nome (e caminho) na variável `THEME`.

É importante lembrar que muitos temas e plugins possuem configurações próprias que podem ser incluídas neste mesmo arquivo. Então recomendo que leia atentamente a documentação dos plugins e tema utilizados.


Arquivos Estáticos
------------------

Para a devida configuração do seu site você pode precisar usar alguns arquivos estáticos, como o `robots.txt` ou `favicon.ico`, ou até mesmo informar onde estarão armazenadas suas imagens e áudios.

Para informar onde estão estes arquivos basta você informá-los na variável `STATIC_PATH`, todos estes diretórios serão copiados para o destino mantendo a estrutura das pastas.

.. code-block:: python

        STATIC_PATHS = [
            'audio', 
            'images', 
            'extra/robots.txt', 
            'extra/favicon.ico',
            ]

Infelizmente nem todos os arquivos devem ser copiados mantendo a mesma estrutura, por exemplo os arquivos `robots.txt` e `favicon.ico`. Estes arquivos deveriam estar na raiz do site.

Para controlar o destino dos arquivos estáticos podemos utilizar a variável `EXTRA_PATH_METADATA`, conforme exemplo abaixo:

.. code-block:: python

        EXTRA_PATH_METADATA = {
            'extra/robots.txt': {'path': 'robots.txt'},
            'extra/favicon.ico': {'path': 'favicon.ico'},
            }


Paginação
---------

Não sei dizer se é algo pessoal, ou se é resquício do Wordpress, mas a forma como o Pelican faz paginações (do índice por exemplo) me incomodou bastante. Por padrão o Pelican monta os índices da seguinte forma: `index.html`, `index2.html`, `index3.html` e etc. Eu realmente esperava que o índice fosse organizado da seguinte forma: `/index.html`, `/page/2/index.html`, `/page/3/index.html` e etc.

Felizmente, encontrei uma configuração que resolve isso:

.. code-block:: python

        PAGINATION_PATTERNS = (
            (1, '{base_name}/', '{base_name}/index.html'),
            (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
        )


Artigos, Páginas, Categorias, Tags e Autores
--------------------------------------------

Da mesma forma não me agradou muito a forma como o Pelican salva os artigos, páginas, categorias, tags e autores. Todos são salvos nos formatos `{slug}.html`, `category/{slug}.html` e assim por diante.

Pessoalmente eu prefiro que as páginas sigam a estrutura similar ao utilizado para os índices, por exemplo, `category/{slug}/index.html`. Para que este comportamento seja atingido utilizei a seguinte configuração:

.. code-block:: python

        ARTICLE_URL = "{slug}"
        ARTICLE_SAVE_AS = "{slug}/index.html"

        PAGE_URL = "{slug}"
        PAGE_SAVE_AS = "{slug}/index.html"

        CATEGORY_URL = "category/{slug}"
        CATEGORY_SAVE_AS = "category/{slug}/index.html"

        TAG_URL = "tag/{slug}"
        TAG_SAVE_AS = "tag/{slug}/index.html"

        AUTHOR_URL = 'author/{slug}'
        AUTHOR_SAVE_AS = 'author/{slug}/index.html'

Notem que boa parte dessas configurações refletem preferências minhas e não devem ser um padrão para todos.


Próximos Artigos
----------------
Por enquanto é só pessoal, mas vou continuar tentando escrever sobre o Pelican com a mesma frequência pois, ainda quero mostrar como utilizar e configurar plugins, temas, NGINX e o Git como gestor de workflow.

Até mais...

.. _Pelican: http://docs.getpelican.com/en/3.3.0/
.. _nesses: /pt/adeus-wordpress
.. _outros: /pt/migrando-do-wordpress-para-o-pelican
.. _documentadas aqui: http://docs.getpelican.com/en/3.3.0/settings.html
.. _este artigo da Wikipédia: http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
.. _Feed Settings: http://docs.getpelican.com/en/3.3.0/settings.html#feed-settings
