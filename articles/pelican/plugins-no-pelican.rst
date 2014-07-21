Plugins no Pelican
##################
:date: 2014-03-13 18:07
:category: Pelican
:tags: blog, pelican, projeto, plugin
:image: /images/pelican/flying_pelican.png
:series: Migrando Para o Pelican

Como já `demonstrei`_ nos `artigos`_ `anteriores`_, o Pelican é extremamente flexível e poderoso. Mas algumas funcionalidades só podem ser obtidas através de plugins. 

.. image:: {filename}/images/pelican/pelican_drawing2.jpg
        :target: {filename}/images/pelican/pelican_drawing2.jpg
        :alt: Pelican
        :align: center



Felizmente, os desenvolvedores do Pelican fizeram um repositório para hospedar os principais plugins existentes.

.. more

Obtendo Os Plugins
------------------

A lista de plugins fica hospedada em um `repositório no GitHub`_ e pode ser baixada da seguinte forma:

.. code-block:: bash

        $ git clone --recursive http://github.com/getpelican/pelican-plugins

Eu decidi por armazenar os plugins em um diretório oculto, dentro do diretório em que criei o site. Da seguinte forma:

.. code-block:: bash

        $ mkdir ~/mindbending/.plugins
        $ cd ~/mindbending/.plugins
        $ git clone --recursive http://github.com/getpelican/pelican-plugins

E alterei a configuração `PLUGIN_PATH` para ter o seguinte valor: `PLUGIN_PATH = './.plugins'`. Desta forma posso listar apenas os nomes do plugins que utilizo:

.. code-block:: python

        PLUGINS = [
                'better_figures_and_images',
                'pelican-youtube',
                'pelican-vimeo',
                'summary', 
                'feed_summary', 
                'gzip_cache', 
                'optimize_images',
                'sitemap',
                'related_posts',
            ]

Vamos ver alguns plugins interessantes da lista.


Assets
------

Apesar de não utilizá-lo (ainda) achei este plugin muito interessante, pois ele possibilita a utilização do `Webassets`_ nos templates do Pelican. De forma simplificada o Webassets possibilita a execução de pré-processadores e compressores em arquivos CSS e Javascript, como por exemplo `cssmin`, `yui_css`, `less`, `sass`, `uglifyjs`, `yui_js`, `closure` e etc. Para uma lista completa dos filtros suportados, leia `esta documentação do Webassets`.

Better Figures and Images
-------------------------

Este plugin inclui em todas as imagens o atributo `style` com o seguinte valor: `style="width: XXXpx; height: auto;"`. Este plugin utiliza a biblioteca `pillow` (continuação da antiga biblioteca `pil`) para descobrir as dimensões da imagem. Entretanto, a funcionalidade que mais me chamou a atenção neste plugin e que me fez adotá-lo foi a funcionalidade de imagens responsivas, bastando adicionar a seguinte linha na configuração do Pelican:

.. code-block:: python

        RESPONSIVE_IMAGES = True

Summary
-------

O Pelican possibilita que nos índices do seu site, seus artigos apareçam integralmente (o que me desagrada, uma vez que os texto podem ser bem extensos) ou somente o primeiro parágrafo (o que não é muito descritivo). Eu prefiro poder escolher em que momento um artigo será "cortado" no índice (assim como eu fazia no Wordpress), e é exatamente isso que este plugin faz.

Após ativá-lo, basta inserir a seguinte configuração: `SUMMARY_END_MARKER = '<!-- more -->'`

Quando você estiver escrevendo um artigo e quiser definir o "ponto de corte" para o índice utilize uma das seguintes formas:

.. code-block:: bash

        # Para ReStructured Text
        .. more

        # Para Markdown
        <!-- more -->


Feed Summary
------------

Particularmente não gosto de deixar o meu Feed RSS/Atom com o conteúdo completo do site, já tive algumas experiências de ruins de pessoas "roubando" meus textos logo após eu fazer uma publicação. Entretanto, também não gosto do que muitos fazem, publicam no Feed apenas uma linha sobre o artigo e o link para o artigo original. Eu prefiro que ele seja apresentado no Feed exatamente da mesma forma que ele é apresentado no índice do site. Associando o plugin *Summary* com o plugin *Feed Summary* eu tenho o resultado esperado.

Para a ativação do plugin basta adicionar a seguinte linha no arquivo de configuração do Pelican: `FEED_USE_SUMMARY = True`


Gzip Cache
----------

Esse é um dos plugins que mais me deixou esbabacado. Ele faz uma coisa muito simples, mas que provê um grande desempenho para o seu site (se você usar o NGINX): ele somente compacta todos os arquivos do seu site usando o gzip. Qual a utilidade disso? Com a configuração correta do NGINX (que vou explicar em um outro artigo) é possível fazer o NGINX servir os arquivos compactados ao invés dos arquivos *plain text*, reduzindo absurdamente o consumo de banda e de processamento. Sim, reduz o processamento. Uma vez que os arquivos são pré compactados, o NGINX não precisa compactá-los toda vez que um cliente o requisite.

Basta incluir o plugin na lista de plugins e ele vai funcionar. Não tem segredo nenhum. Abaixo uma demonstração dos arquivos gerados para o índice:

.. code-block:: bash

        $ find  ./page/ -type f
        ./page/7/index.html.gz
        ./page/7/index.html
        ./page/6/index.html.gz
        ./page/6/index.html
        ./page/5/index.html.gz
        ./page/5/index.html
        ./page/4/index.html.gz
        ./page/4/index.html
        ./page/3/index.html.gz
        ./page/3/index.html
        ./page/2/index.html.gz
        ./page/2/index.html

Optimize Images
---------------

Este plugin é bem simples também, ele apenas otimiza as imagens para a web, utilizando ferramentas como `jpegtran` e `optipng`. Para isso você precisa ter certeza de que esses programas estejam instalados:

.. code-block:: bash

        $ sudo aptitude install libjpeg-progs optipng

Abaixo uma pequena comparação de tamanho de uma imagem antes e depois da otimização:

.. code-block:: bash

        $ ls -l pelican-blog-01.png ../output/images/pelican-blog-01.png 
        -rw-rw-r-- 1 git git 35127 Mar 13 22:28 pelican-blog-01.png
        -rwxrwxr-x 1 git git 27981 Mar 13 14:18 ../output/images/pelican-blog-01.png

Como podem ver caiu de 35127 bytes para 27981 bytes, uma redução de 7146 bytes. Parece pouco a primeira vista, mas considere isso ao longo de 4 anos de publicações você vai ver que você terá uma redução considerável de tamanho e tráfego de rede. Sim, não se esqueça que essas imagens são transferidas toda vez que alguém as acessa, então cada byte faz diferença.

**Atenção:** Como esse plugin processa todas as imagens do site site ele pode tornar a compilação mais demorar, eu sugiro ativar esse plugin apenas no ambiente de produção.


Pelican Vimeo & Youtube
-----------------------

Este plugin não faz nada além de possibilitar a inserção de vídeos do Youtube e do Vimeo através de tags rst:

.. code-block:: rst

        .. vimeo:: <video ID>
                :width: 800
                :height: 500
                :align: center

        .. youtube:: <video ID>
                :width: 800
                :height: 500
                :align: center

Post Statistics
---------------

Apesar de não usá-lo achei ele bem nerd e interessante. Este plugin provê a você informações sobre cada artigo, como:

wc
    Quantas palavras existem no artigo
read_mins
    Estimativa de quantos minutos serão necessários para ler este artigo, tomando como base 250 wpm (250 palavras por minuto).
word_counts
    Contávem de frequência de palavas. Pode ser utilizada para criar tag/word clouds.
fi
    Índice Flesch-kincaid
fk
    Nota de Nível Flesch-kincaid

Related Posts
-------------

Também considero este plugin como sendo essencial. Ele se limita a adicionar a cada artigo uma lista de artigos relacionados tomando como base as tags utilizadas na marcação. Você pode controlar o número de artigos relacionados utilizando a seguinte configuração: `RELATED_POSTS_MAX = 10`

Já no seu template basta adicionar o seguinte código:

.. code-block:: jinja

        {% if article.related_posts %}
            <ul>
            {% for related_post in article.related_posts %}
                <li><a href="{{ SITEURL }}/{{ related_post.url }}">{{ related_post.title }}</a></li>
            {% endfor %}
            </ul>
        {% endif %}

Sitemap
-------

Bem, não tem muito o que falar sobre este plugin, ele gera o sitemap do seu site. Se você não sabe o que é um sitemap, você realmente precisa sair do Wordpress e aprender um pouco mais sobre tecnologias web. Um sitemap um arquivo XML que contém todas as URLs do seu site com alguns dados prioridade e frequência de alteração. Estes arquivos são utilizados pelos *crawlers* de sites como Google.

É recomendado adicionar a seguinte configuração no `pelicanconf.py`:

.. code-block:: python

    SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
        },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
        }
    }


Outros Plugins
--------------

Não se prendam apenas aos plugins desses repositórios. Claro, eu utilizei-o como base pois todos que usam o Pelican enviam seus plugins para este repositório. Mas tem muitas pessoas que não publicam seus plugins por aí, então sugiro que você pesquise plugins baseado na sua necessidade. Outra dica importante é: fique de olho nos `pull requests`_. Pois neles estão as solicitações de inclusão de plugins no repositório.

Outro ponto importante é, se você tem uma necessidade e não encontrou um plugin escreva o seu próprio plugin, é muito simples e fácil. Desde que comecei com o pelican já escrevi 2 plugins. Além disso o Pelican possui uma ótima documentação sobre `como escrever plugins`_.

Fechamento
----------

Bem pessoal, por hoje é isso. Nos artigos seguintes vou mostrar como produzir o pelican com o NGINX.

Até mais...

.. _demonstrei: http://mindbending.org/pt/instalando-o-pelican
.. _artigos: http://mindbending.org/pt/migrando-do-wordpress-para-o-pelican
.. _anteriores: http://mindbending.org/pt/configurando-o-pelican
.. _repositório no GitHub: http://github.com/getpelican/pelican-plugins
.. _Webassets: https://github.com/miracle2k/webassets
.. _esta documentação do Webassets: http://webassets.readthedocs.org/en/latest/builtin_filters.html
.. _pull requests: https://github.com/getpelican/pelican-plugins/pulls
.. _como escrever plugins: http://docs.getpelican.com/en/3.3.0/plugins.html#how-to-create-plugins
