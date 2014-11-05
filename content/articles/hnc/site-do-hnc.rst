Site do Hack 'n' Cast
#####################
:date: 2014-11-05 13:39
:category: Hack 'n' Cast
:tags: site, pelican, hack 'n' cast, open source, software livre, contribuição
:image: /images/logos/HNC-beta.png
:description: Agora que já liberamos uma versão beta do site do Hack 'n' Cast, estou publicando aqui um guia de como contribuir para o desenvolvimento deste.

Olá pessoal! Como todos que nos acompanham pelas redes sociais já sabem, na madrugada do dia 29/10 liberamos a versão beta do site, escondida atrás de alguns *puzzles* simples, mas que não exigem nada de programação (talvez um pouco de cálculo). Ainda não estava sabendo? Veja `aqui`_...

.. image:: {filename}/images/logos/HNC-beta.png
        :target: {filename}/images/logos/HNC-beta.png
        :alt: Hack 'n' Cast Beta
        :align: center

.. more

Como era de se esperar, esta publicação ainda está em beta e tem como objetivo atrair contribuidores, e para facilitar esta contribuição estou escrevendo este "guia", para servir de referência. Lembrando que toda a discussão do desenvolvimento do site será realizada no nosso `Grupo de Discussão`_.

Descrição do Ambiente
---------------------

A infraestrutura do Hack 'n' Cast consiste apenas do Python (algumas bibliotecas), do *virtual environment* (não obrigatório), Jinja e do Pelican. Vamos a algumas descrições:

Python
        Linguagem utilizada para escrever os *plugins* do site e um pouco do seu backend. Muito provavelmente essa parte do desenvolvimento estará a meu cargo, já que estou mais habituado. Você não conhece Python? Ouça nosso `episódio sobre esta linguagem`_!

*Virtual Environment*
        É apenas um software que cria uma "jaula" e isola uma ambiente Python do resto do sistema operacional. Útil para desenvolvedores que precisam trabalhar com versões diferentes de bibliotecas (meu caso). Essa dependência é não obrigatório e você pode muito bem se virar sem ela. Mas é uma boa prática ;)

Jinja
        O `Jinja`_ é um sistema de *templates* escrito em Python e para o Python. Ele é bem simples e basta a leitura rápida `dessa página`_ para entender como ele funciona. Para uma documentação mais completa, visite `esta outra página`_.

Pelican
        O Pelican é um gerador de sites estáticos que eu aprendi a mexer quando perdi a paciência com o Wordpress. Ele é bem simples e intuitivo. Se quiser saber mais sobre ele eu já escrevi diversos `artigos sobre ele aqui`_.


Instalando o Ambiente
---------------------

Muito bem, primeiramente vamos obter os códigos do Hack 'n' Cast. Este projeto é constituído de dos repositórios, o `hackncast`_ e o `hackncast_theme`_. O primeiro possui os artigos, imagens, plugins e configurações do site, enquanto o último possui apenas o tema que utilizamos no site. Muito provavelmente você precisará mexer apenas no tema (a não ser que você queira corrigir algum erro ou link nos textos).

Muito bem, para obter o código vamos fazer o seguinte:

.. code::

        $ cd ~
        $ git clone https://github.com/hackncast/hackncast
        $ cd hackncast
        $ git clone https://github.com/hackncast/hackncast_theme .theme


Em seguida precisamos instalar o Python 3 e todas as suas dependências. Segue a lista de comandos:

Debian e variantes
        .. code::

                $ sudo aptitude install python3 python-setuptools python-virtualenv libxml2-dev libxslt-dev python3.3-dev

Fedora e variantes
        .. code::

                $ sudo yum install python3 python3-devel python-setuptools python-virtualenv libxml2-devel libxslt-devel

Arch e Variantes
        .. code::

                $ pacman -S python-setuptools python-virtualenv libxml2 libxslt

Em seguida criamos o ambiente virtual e instalamos todas as dependências no ambiente virtual:

.. code::

        $ mkdir ~/venv
        $ virtualenv -p /usr/bin/python3 --prompt "(pelican-3.4)" ~/venv/pelican-3.4
        $ . ~/venv/pelican-3.4/bin/activate; pip3 install -r ~/hackncast/requirements.txt; deactivate

Pronto! Está tudo preparado para compilar o site e ver o resultado!

*Atenção:* Caso você não vá utilizaro ambiente virtual instale as dependências via ``pip`` com o seguinte comando: ``pip3 install -r ~/hackncast/requirements.txt``.

Compilando o Site (sem *virtual environment*)
---------------------------------------------

Para aqueles que não querem utilizar o *virtual environment*, compilem o site da seguinte forma:

.. code::

        $ make html
        $ make serve

O comando ``make html`` gera o site estático e o comando ``make serve`` inicializa um servidor web através do Python 3 para "entregar" o HTML estático. Após isso acesse o site do Hack 'n' Cast (no seu computador) através da URL http://localhost:8000.

Existe uma outra forma de servir o site para quando estamos alterando-o com muita frequência, através do comando ``make devserver``. Este comando inicia o servidor que monitora as alterações do site e recompila-o quando necessário. É importante ressaltar que este modo inicia um processo em background que precisa ser finalizado, para isso utilize o comando ``make stopserver``.

Compilando o Site (com *virtual environment*)
---------------------------------------------

Para compilar o site com *virtual environment* utilize os seguintes comandos:

.. code::

        $ make build
        $ make envserve

O comando ``make html`` gera o site estático e o comando ``make envserve`` inicializa um servidor web através do Python 3 para "entregar" o HTML estático. Após isso acesse o site do Hack 'n' Cast (no seu computador) através da URL http://localhost:8000.

Existe uma outra forma de servir o site para quando estamos alterando-o com muita frequência, através do comando ``make envdevserver``. Este comando inicia o servidor que monitora as alterações do site e recompila-o quando necessário. É importante ressaltar que este modo inicia um processo em background que precisa ser finalizado, para isso utilize o comando ``make stopserver``.

Templates Jinja
---------------

Se vocês olharem os templates (em ``hackncast/.theme/templates``) verão que a sintaxe o Jinja não é muito complexa e que 90% das páginas são HTML puro, e somente 10% é do Jinja. Logo, mesmo uma pessoa com pouca experiência em Jinja e Python consegue colaborar na codificação do site. A única coisa que é necessário entender é a estrutura dos templates.

A parte boa do Jinja é que ele trabalha com "herança", isto é, um template herda do outro. No caso do Hack 'n' Cast, todos os templates herdam de ``templates/base.html``. Logo, algumas coisas precisam ser alteradas apenas no template base e isto se replica para todos os outros. Eu ainda estou melhorando a modularização e o acoplamento dos templates, ainda está tudo muito crú, mas aos poucos eu vou organizando isso.

Outro ponto importante é entender o que cada template faz. Segue abaixo uma breve descrição de cada arquivo:

templates/article.html
        Gera as páginas de artigos, ou seja, por exemplo esta página que você está lendo.

templates/page.html
        Template utilizado para gerar uma página aleatória. Veja o conteúdo de ``hackncast/content/pages``.

templates/archives.html
        Mostra a listagem de arquivos, ou seja, uma visão histórica de todos os textos já publicados.

templates/authors.html
        Gera uma página mostrando todos os autores do site.

templates/tags.html
        Gera uma página mostrando todas as tags do site.

templates/categories.html
        Gera uma página listando todas as categorias do site.

templates/index.html
        Template de índice genérico. Primordialmente utilizado como base para todos os índices.

templates/author.html
        Gera a página listando os artigos deste autor, tendo como base o template ``index.html``.

templates/category.html
        Gera a página listando os artigos de uma certa categoria, tendo como base o template ``index.html``.

templates/tag.html
        Gera a página listando os artigos de uma certa tag, tendo como base o template ``index.html``.

Recebendo e Aprovando Contribuições
-----------------------------------

Todas as contribuições serão gerenciadas pelo GitHub, isto é, a forma correta de enviar uma correção é criar um fork do repositório, realizar suas correções/melhorias, criar um *commit*, seguido de um *pull request*.

A princípio pode parecer algo complexo e assustador, mas pode ser feito 100% via interface web do GitHub. O próprio GitHub possui ótimas documentações:

- `Fork a Repo`_;
- `Creating a pull request`_;

O site tableless também tem um bom texto sobre como contribuir através do GitHub: `Contribuindo em projetos open source com o github`_

Em breve tentarei escrever sobre o sistema de templates Jinja2.

.. _aqui: http://hackncast.org
.. _Grupo de Discussão: https://groups.google.com/forum/?hl=pt#!forum/hackncast
.. _episódio sobre esta linguagem: /pt/hack-n-cast-v06-python
.. _Jinja: http://jinja.pocoo.org/
.. _dessa página: http://jinja.pocoo.org/docs/dev/templates/
.. _esta outra página:
.. _artigos sobre ele aqui: /pt/category/pelican
.. _hackncast: https://github.com/hackncast/hackncast
.. _hackncast_theme: https://github.com/hackncast/hackncast_theme
.. _Fork a Repo: https://help.github.com/articles/fork-a-repo/
.. _Creating a pull request: https://help.github.com/articles/creating-a-pull-request/
.. _Contribuindo em projetos open source com o github: http://tableless.com.br/contribuindo-em-projetos-open-source-com-o-github/
