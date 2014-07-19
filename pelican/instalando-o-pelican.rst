Instalando o Pelican
####################
:date: 2014-03-10 15:17
:category: Pelican
:tags: pelican, wordpress, python, shell, migração
:image: /images/pelican/flying_pelican.png
:series: Migrando Para o Pelican

Conforme relatado `neste outro artigo`_, migrei este blog para o `Pelican`_. Como é de praxe, acabei anotando tudo o que fiz e realizando uma documentação. Para essa instalação utilizei o Pelican 3.3, `virtualenv`_ e o Python 2.7.

.. image:: {filename}/images/pelican/pelican_blueprint.png
        :align: center
        :alt: Pelican
        :target: {filename}/images/pelican/pelican_blueprint.png

É muito raro você precisar recriar o ambiente do Pelican, mas como outros podem ter dúvidas resolvi disponibilizar todas as minhas notas em forma de artigo.

.. more

Instalação de Dependências
--------------------------

O pelican tem uma série de dependências, mas a forma mais simples de instalá-las é utilizar o `pip` e o `virtualenv`.

O `pip`_ é um gestor de pacotes para a linguagem Python e é disponibilizado no pacote `python-setuptools`. Ele funciona de forma similar ao aptitude, yum e etc. Para que está acostumado com distribuições GNU/Linux é algo bem comum.

Já o virtualenv é um "sandbox" para o Python, ele armazena diversas bibliotecas sem que estas influenciem as bibliotecas já instaladas na sua distribuição GNU/Linux (ou Mac OS). Esta é uma ferramenta fundamental para quem desenvolve em Python e precisa trabalhar em diversas versões de uma mesma biblioteca.

Para instalar o `virtualenv`, o `pip` (através do pacote `python-setuptools`) e as bibliotecas `libxml2` e `libxslt-dev` (bibliotecas em C necessárias para o módulo `lxml` do Python) eu utilizei o gerenciador de pacotes da minha distribuição:

.. code-block:: bash

        $ sudo aptitude install python-setuptools python-virtualenv libxml2-dev libxslt-dev

Em seguida criei o virtualenv no `home` do meu usuário:

.. code-block:: bash

        $ mkdir ~/venv
        $ virtualenv ~/venv/pelican

Em seguida criei o arquivo `~/venv/pelican/requirements.txt` com o seguinte conteúdo:

.. code-block:: python

        Fabric==1.8.1
        Jinja2==2.7.1
        Markdown==2.3.1
        MarkupSafe==0.18
        Pillow==2.2.2
        Pygments==1.6
        Unidecode==0.04.14
        argparse==1.2.1
        beautifulsoup4==4.3.2
        blinker==1.3
        docutils==0.11
        ecdsa==0.10
        feedgenerator==1.7
        lxml==3.2.4
        mdx-video==0.1.7.5
        paramiko==1.12.0
        pelican==3.3
        pycrypto==2.6.1
        pytz==2013.8
        six==1.4.1
        smartypants==1.8.3
        typogrify==2.0.0
        wsgiref==0.1.2

Em fim realizei a instalação de todas as dependências tornando-as restritas ao `virtualenv` chamado `pelican` com os seguintes comandos:

.. code-block:: bash

        $ . ~/venv/pelican/bin/activate
        $ pip install -r ~/venv/pelican/requirements.txt

Ao fim do processo nosso ambiente estará pronto para uso.

Criando o Site
--------------

Para criar o seu site o Pelican tem um pequeno tutorial chamado `pelican-quickstart` que gera um arquivo Makefile que o auxiliará a gerar o site. Inicialmente eu utilizei este script gerado pelo próprio Pelican, mas como o Mind Bending tem as suas peculiaridades e eu tenho as minhas manias acabei construindo meu próprio Makefile. Mas isso é assunto para um outro artigo. Segue abaixo o processo de criação do site com o `pelican-quickstart`:

.. code-block:: bash

        $ cd ~
        $ pelican-quickstart 
        Welcome to pelican-quickstart v3.3.0.

        This script will help you create a new Pelican-based website.

        Please answer the following questions so this script can generate the files
        needed by Pelican.

            
        > Where do you want to create your new web site? [.] mindbending
        > What will be the title of this web site? Mind Bending
        > Who will be the author of this web site? Magnun
        > What will be the default language of this web site? [en] pt
        > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) y                     
        > What is your URL prefix? (see above example; no trailing slash) http://mindbending.org
        > Do you want to enable article pagination? (Y/n) y
        > How many articles per page do you want? [10] 10
        > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
        > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
        > Do you want to upload your website using FTP? (y/N) n
        > Do you want to upload your website using SSH? (y/N) n
        > Do you want to upload your website using Dropbox? (y/N) n
        > Do you want to upload your website using S3? (y/N) n
        > Do you want to upload your website using Rackspace Cloud Files? (y/N) n
        Done. Your new project is available at /tmp/teste/mindbending

Claro que este site ainda não tem nenhum artigo, mas já é possível ver como o site vai estar com os seguintes comandos:

.. code-block:: bash
        
        $ make html
        pelican /tmp/teste/mindbending/content -o /tmp/teste/mindbending/output -s /tmp/teste/mindbending/pelicanconf.py 
        WARNING: No valid files found in content.
        Done: Processed 0 articles and 0 pages in 0.16 seconds.
        $ make serve
        cd /tmp/teste/mindbending/output && python -m pelican.server

Em seguida acesse com o seu navegador favorito a URL `http://127.0.0.1:8000`. Este é o resultado:

.. figure:: {filename}/images/pelican/pelican-blog-01.png
        :align: center
        :alt: Primeira Build do Mind Bending
        :target: {filename}/images/pelican/pelican-blog-01.png

        Resultado da Primeira build do site

Primeiro Artigo
---------------

Para criar o primeiro artigo, crie o diretório *articles*  (`mkdir ~/mindbending/content/article`) e crie o arquivo `~/mindbending/content/article/hello-world.rst` com o seguinte conteúdo:

.. code-block:: rst

        Hello World
        ###########
        :date: 2014-03-10 15:17
        :category: Categoria
        :tags: tag01, tag02, tag03

        Olá! Este é o primeiro artigo. Então vamos de lorem ipsum!

        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
        minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
        ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
        voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
        sint occaecat cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum.

        E claro, um código Python!

        .. code-block:: python
                
                print "Hello World!"

Em seguida repita o processo de "compilação" do site:

.. code-block:: bash

        $ make html
        pelican /tmp/teste/mindbending/content -o /tmp/teste/mindbending/output -s /tmp/teste/mindbending/pelicanconf.py 
        Done: Processed 1 articles and 0 pages in 0.32 seconds.
        $ make serve
        cd /tmp/teste/mindbending/output && python -m pelican.server

E o resultado gerado será este:

.. figure:: {filename}/images/pelican/pelican-blog-02.png
        :align: center
        :alt: Segunda Build do Mind Bending
        :target: {filename}/images/pelican/pelican-blog-02.png

        Resultado da Segunda build do site

Por hoje é só pessoal. Fiquem atentos que em breve irei publicar artigos ensinando a migrar todos os seus textos do Wordpress para o Pelican, e também irei explicar como utilizar plugins, customizar as configurações e alterar o tema padrão.

Até mais...


.. _neste outro artigo: /pt/adeus-wordpress
.. _Pelican: http://docs.getpelican.com/en/3.3.0/
.. _virtualenv: http://www.virtualenv.org/en/latest/
.. _pip: http://www.pip-installer.org/en/latest/
