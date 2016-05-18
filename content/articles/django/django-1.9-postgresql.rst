Instalando o Django 1.9 com PostgreSQL para Desenvolvimento
###########################################################
:date: 2016-05-18 11:31
:category: Django
:tags: django, postgresql, tutorial, instalação, spycopg3, ubuntu, fedora, debian, red hat, centos, arch linux, virtualenv, virtualenvwrapper, python, psql
:image: /images/django/django-logo.png
:description: Eu sempre adiei os meus estudos de Django com a desculpa de que eu não precisava de um framework tão poderoso para meus pequenos projetos. Mas como tudo na vida, chegou a hora de aprender Django.

Eu sempre me foquei em *frameworks* mais simples (Web2py) ou em *microframeworks* (Flask), por achar que "*full stack frameworks*" poderiam adicionar um overhead muito grande, tanto na execução do sistema quando no meu fluxo de desenvolvimento.

.. image:: {filename}/images/django/django-name.jpg
        :target: {filename}/images/django/django-name.jpg
        :alt: Django Name
        :align: center

Porém, no segundo semestre do ano passado, a comunidade do `GrupyDF`_ fez uma compra coletiva do livro `Two Scoops of Django`_. Foi então que eu pensei, "talvez, comprar um livro desses seja uma boa forma de me forçar a aprender esse *framework*". Curiosamente, junto com o livro começaram a chegar propostas de projetos pra mim em Django. Resultado? Está na hora de correr atrás do prejuízo e aprender Django em tempo recorde. Agora que estou tempo um pouco de tempo livre vou tentar despejar aqui algumas "memórias" do que aprendi e outras que não quero esquecer. Neste primeiro artigo vou tratar do Django para desenvolvedor em uma estação de trabalho comum (GNU/Linux).

.. .. more

Ambiente Virtual
----------------

Como para qualquer outro ambiente, seja Python, JavaScript ou Ruby, é interessante trabalhar com ambientes virtuais (*Virtual Enviroment*). Não, não estou me referindo a máquinas virtuais, isso fica pra outro dia (com Vagrant, claro). Estou me referindo a separar o ambiente no qual você instala suas dependências e as verões do framework. Imagine que em um projeto você está usando a lib-XYZ versão 1.2 e em outro projeto você precisa desta mesma biblioteca, mas na versão 1.8? Como manter ambas as versões sem que uma conflite com a outra? Ou que por acidente o software que deveria utilizar a versão 1.2 acabe importando a versão 1.8? Pra isso usamos ambientes virtuais.

A melhor forma de lidar com ambientes virtuais no Pyhon é com o pacote **virutalenvwrapper**. para instalá-lo utilize a seguinte linhas de comando:

.. code-block:: bash

    $ # Debian, Ubuntu e etc
    $ sudo aptitude install virtualenvwrapper
    $ # Fedora, Red Hat e CentOS
    $ sudo yum install python-virtualenvwrapper
    $ # Arch Linux
    $ sudo pacman -S python-virtualenvwrapper

Em seguida, adicione a seguinte linha no seu ``.bashrc`` ou ``.zshrc`` (caso utilize zsh):

.. code-block:: bash

    export WORKON_HOME=~/venv

Note que o nome de diretório pode ser customizado. Esse é o que eu utilizo.

Em seguida vamos criar um ambiente virtual com Python 3:

.. code-block:: bash

    $ mkvirtualenv -p /usr/bin/python3 MeuProjeto
    Running virtualenv with interpreter /usr/bin/python3
    Using base prefix '/usr'
    New python executable in MeuProjeto/bin/python3
    Also creating executable in MeuProjeto/bin/python
    Installing setuptools, pip...done.

Ao final desse comando você terá um texto adicional (muito provavelmente será ``(MeuProjeto)``) no início do seu prompt. Isso indica que você está usando o ambiente virtual criado, e que todas as bibliotecas e pacotes instaladas, não serão instaladas no sistema operacional, mas sim nesse diretório especificado.

Para sair do ambiente virtual utilize o comando ``deactivate``. Para ativar um ambiente virtual, ou trocar de ambientes, utilize o comando ``workon <nome-do-venv>``.

Pronto, agora vamos instalar o Django!

Instalando o Django
-------------------

Para instalar o django é muito simples:

.. code-block:: bash

    $ pip install django==1.9 psycopg2
    Collecting django==1.9
    Downloading Django-1.9-py2.py3-none-any.whl (6.6MB)
      100% |################################| 6.6MB 81kB/s
      Installing collected packages: django
    Successfully installed django-1.9

Pronto, agora temos o Django instalado! Agora vamos criar nosso projeto.

Criando um projeto e um app
---------------------------

Eu armazeno todos os meus projetos dentro de um mesmo diretório, mas isso é uma coisa pessoal...

.. code-block:: bash

    $ mkdir ~/Projetos && cd ~/Projetos
    $ django-admin startproject MeuProjeto
    $ cd MeuProjeto
    $ tree
    .
    ├── MeuProjeto
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py

    1 directory, 5 files

Podemos ver este comando cria o *template* de um projeto Django. Muitos customizam esta estrutura baseado em algumas boas práticas (algumas delas do livro *Two Scoops of Django*), mas vou deixar isso pra outro artigo. No momento quero ver nosso projeto rodando! Para isso utilize o comando ``./manage.py runserver``.

.. image:: {filename}/images/django/meuprojeto-firstrun.png
        :target: {filename}/images/django/meuprojeto-firstrun.png
        :alt: MeuProjeto - First Run
        :align: center

Muito bem, tudo funcionando até aqui. Mas espere... Não configuramos nenhum banco de dados! Se você der um ``ls`` no diretório do seu projeto verá o seguinte arquivo: ``db.sqlite3``. Sim, por padrão o Django inicia um banco SQLite3. Onde isso é configurado? ~Não sei, vamos descobrir?~

.. code-block:: bash

    $ ag --python "sqlite"
    MeuProjeto/settings.py
    79:        'ENGINE': 'django.db.backends.sqlite3',
    80:        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

Pronto aí está! Vamos corrigir esse erro, começando com o seguinte comando: ``rm -rf db.sqlite3``


Instalando o PostgreSQL
-----------------------

Para instalar o PostgreSQL no seu computador utilize um dos comandos abaixo:

.. code-block:: bash

    $ # Debian, Ubuntu e etc
    $ sudo yum install postgresql-server postgresql
    $ # Fedora, Red Hat e CentOS
    $ sudo aptitude install postgresql postgresql-client
    $ # Arch Linux
    $ sudo pacman -S postgresql

Diferentemente do Debian/Ubuntu/Outros, no Arch Linux, Fedora, Red Hat e CentOS o PostgreSQL demanda uma configuração manual. Primeiramente temos que inciar o SGBD e iniciar o serviço.

Para o Fedora/Red Hat/CentOS utilize os seguintes comandos:

.. code-block:: bash

    $ sudo postgresql-setup --initdb --unit postgresql
    $ sudo systemctl enable postgresql

Para o Arch Linux utilize os seguintes comandos:

.. code-block:: bash

    $ sudo -i -u postgres
    $ initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data'

Por padrão o PostgreSQL escuta na porta 5432/TCP no endereço ``localhost``. Para um ambiente de desenvolvimento isso não é um problema, mas caso seja necessário alterar o *bind address* e a porta TCP utilizada edite a linha ``listen_addresses = 'localhost'`` e a linha ``port = 5432`` no seguinte arquivo de configuração:

*Debian/Ubuntu*
    ``/etc/postgresql/9.4/main/postgresql.conf``
*Fedora/Red Hat/CentOS*
    ``/var/lib/pgsql/data/postgresql.conf``
*Arch Linux*
    ``/var/lib/postgres/data/postgresql.conf``

Muito bem. Agora que o PostgreSQL está em execução, vamos criar uma base e um usuário para o nosso projeto:

.. code-block:: bash

    $ sudo -iu postgres psql
    psql (9.3.9, servidor 9.4.5)
    AVISO: psql versão 9.3, servidor versão 9.4.
             Algumas funcionalidades do psql podem não funcionar.
    Digite "help" para ajuda.

    postgres=# create user meu_projeto_db_user with password 'nR9f9tw+sk5yLvROCQodPLqbyAdPKReal41FKvLB/qE=' createdb;
    postgres=# create database meu_projeto_db owner meu_projeto_db_user;

Para as senhas, chaves e etc eu sempre gero valores aleatórios com o comando openssl:

.. code-block:: bash

    $ openssl rand -base64 32
    nR9f9tw+sk5yLvROCQodPLqbyAdPKReal41FKvLB/qE=

Sim, mesmo para ambientes de desenvolvimento, eu sou louco a este ponto... Vamos continuar!

Agora que temos o PostgreSQL instalado, com usuário, senha e banco de dados configurados, vamos testar o acesso para não termos nenhuma surpresa no futuro:

.. code-block:: bash

    $ psql -h localhost -U meu_projeto_db_user meu_projeto_db
    psql: FATAL:  autenticação do tipo Ident falhou para usuário "meu_projeto_db_user"

Calma, o erro era esperado. Mostrei exatamente para que vocês poderem reconhecer esse tipo de erro no futuro. O PostgreSQL está reclamando que não conseguiu autenticar o usuário no modo *Ident*. Este modo de autenticação é especificado na `RFC-1413`_ e se utiliza das credenciais do seu usuário do sistema operacional para realizar a autenticação (mais detalhes em `Auth methods - PostgreSQL Docs`_). Para o Django vamos utilizar o método de autenticação *md5*, que se utiliza do hash da senha que criamos anteriormente. Para isso precisamos adicionar a linha ``host meu_projeto_db meu_projeto_db_user 127.0.0.1/32 md5`` no arquivo ``pg_hba.conf``:

*Debian/Ubuntu*
    ``/etc/postgresql/9.4/main/pg_hba.conf``
*Fedora/Red Hat/CentOS*
    ``/var/lib/pgsql/data/pg_hba.conf``
*Arch Linux*
    ``/var/lib/postgres/data/pg_hba.conf``

Note que lá eu preciso informar o ip de origem da conexão (127.0.0.1/32). Caso você esteja utilizando um PostgreSQL remoto, ou não esteja realizando conexões através da porta de loopback, será necessário adequar esta linha. Após salvar o arquivo, vamos reiniciar o PostgreSQL, ``sudo systemctl restart postgresql``. Em seguida vamos testar novamente a conexão:

.. code-block:: bash

    $ psql -h localhost -U meu_projeto_db_user meu_projeto_db
    Senha para usuário meu_projeto_db_user:
    psql (9.3.9, servidor 9.4.5)
    AVISO: psql versão 9.3, servidor versão 9.4.
             Algumas funcionalidades do psql podem não funcionar.
    Digite "help" para ajuda.

    meu_projeto_db=> \q
    $

Muito bem, estabelecemos uma conexão com sucesso. Agora vamos configurar o Django para usar o PostgreSQL.

Conexão Django/PostgreSQL
-------------------------

Essa é a parte mais simples. Edite o arquivo ``MeuProjeto/settings.py`` e altere a variável ``DATABASES`` para refletir o exemplo abaixo:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'meu_projeto_db',
            'USER': 'meu_projeto_db_user',
            'PASSWORD': 'nR9f9tw+sk5yLvROCQodPLqbyAdPKReal41FKvLB/qE=',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

Agora que temos uma base descente, e não um SQLite3, vale a pena rodar as *migrations*.

Executando a Primeira *Migration*
---------------------------------

As *migrations* do Django são a forma com que o *framework* gerencia a sua base de dados, criando/deletando/alterando tabelas, índices, *constraints* e etc. Ou seja, ele faz o trabalho sujo no PostgreSQL pra você. Então vamos lá...

.. code-block:: bash

    $ ./manage.py migrate
    Operations to perform:
      Apply all migrations: contenttypes, sessions, auth, admin
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying sessions.0001_initial... OK
    $


Se você quiser confirmar que o Django realmente criou tabelas e tudo mais na sua base, conecte-se novamente através do ``psql`` e utilize o comando ``\dt``:

.. code-block:: bash

    $ psql -h localhost -U meu_projeto_db_user meu_projeto_db                                                                                                                              ❰
    Senha para usuário meu_projeto_db_user:
    psql (9.3.9, servidor 9.4.5)
    AVISO: psql versão 9.3, servidor versão 9.4.
             Algumas funcionalidades do psql podem não funcionar.
    Digite "help" para ajuda.

    meu_projeto_db=> \dt
                             Lista de relações
     Esquema |            Nome            |  Tipo  |         Dono
    ---------+----------------------------+--------+---------------------
     public  | auth_group                 | tabela | meu_projeto_db_user
     public  | auth_group_permissions     | tabela | meu_projeto_db_user
     public  | auth_permission            | tabela | meu_projeto_db_user
     public  | auth_user                  | tabela | meu_projeto_db_user
     public  | auth_user_groups           | tabela | meu_projeto_db_user
     public  | auth_user_user_permissions | tabela | meu_projeto_db_user
     public  | django_admin_log           | tabela | meu_projeto_db_user
     public  | django_content_type        | tabela | meu_projeto_db_user
     public  | django_migrations          | tabela | meu_projeto_db_user
     public  | django_session             | tabela | meu_projeto_db_user
    (10 registros)

    meu_projeto_db=>

Como podem ver, o Django já criou 10 tabelas, dentre elas tabelas pada administração/meta-informação do próprio Django (``django_admin_log``, ``django_content_type``, ``django_migrations`` e ``django_session``) e tabelas para armazenar dados de autenticação (``auth_group``, ``auth_group_permissions``, ``auth_permission``, ``auth_user``, ``auth_user_groups`` e ``auth_user_user_permissions``).

Para ter certeza, basta iniciar o Django ``./manage.py runserver`` e acessar novamente pelo navegador.

Conclusão
---------

Como podemos ver, não é nada muito complexo iniciar um ambiente de desenvolvimento. Em breve tentarei postar aqui algumas das boas práticas de estruturação do projeto e (a parte que eu considero mais importante) como configurar um ambiente de produção para o Django utilizando NGINX, uWSGI, e PostgreSQL.

.. _GrupyDF: http://df.python.org.br/
.. _Two Scoops of Django: https://www.twoscoopspress.com/products/two-scoops-of-django-1-8
.. _RFC-1413: https://tools.ietf.org/html/rfc1413
.. _Auth methods - PostgreSQL Docs: http://www.postgresql.org/docs/9.4/static/auth-methods.html#AUTH-IDENT
