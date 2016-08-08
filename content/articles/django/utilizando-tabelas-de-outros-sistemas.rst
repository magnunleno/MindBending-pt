Django: Utilizando Tabelas de Outros Sistemas Parte 1/2
#######################################################
:date: 2016-08-08 16:25
:category: Django
:tags: django, tutorial, tabela, banco de dados, sistema
:image: /images/django/django-logo.png

Recentemente tive a necessidade de fazer o Django ler 3 tabelas de um outro sistema para cruzamento de informações. Como essa necessidade pode ser a necessidade de outras pessoas, achei, por mais simples que seja, que seria útil escrever sobre o assunto.

.. image:: {filename}/images/django/django-text.png
        :target: {filename}/images/django/django-text.png
        :alt: Django
        :align: center


.. more

Para este exemplo (e o próximo) vamos considerar que meu sistema precisa acessar dados de RH da empresa, realizando assim, cruzamento de dados como:

- nome;
- endereço;
- telefone.

Nesta primeira parte, vou considerar que seus dados de outro estão na mesma base de dados que o seu sistema Django (porém em outro esquema, no caso de PostgreSQL). Na parte 2 veremos como lidar com isso utilizando bases diferentes.

Primeiros Passos
----------------

Primeiramente vamos criar um projeto do zero:

.. code-block:: bash

    $ django-admin startproject projeto
    $ cd projeto
    $ django-admin startapp users

Note que eu criei a *app* `users` na raiz do projeto para simplificar, aplique aqui a sua boa prática de organizar suas *apps* em uma pasta específica.

Configurando a Aplicação
------------------------

Precisamos, antes de tudo, configurar nossa aplicação para acessar o banco de dados, no meu caso, um PostgreSQL. Para isso vamos editar o arquivo ``projeto/settings.py``:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_db'
            'USER': 'django_user'
            'PASSWORD': 'password',
            'HOST': 'postgresql.domain'
            'PORT': 5432,
        },
    }

Agora podemos executar a migração da base:

.. code-block:: bash

    $ ./manage.py makemigrations && ./manage.py migrate
    No changes detected
    Operations to perform:
      Apply all migrations: admin, sessions, auth, contenttypes
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


Agora vamos ativar esta nova *app* editando o arquivo ``projeto/settings.py`` e adicionando-a no dicionário ``INSTALLED_APPS``:


.. code-block:: python

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'users'
    ]


Mãos à Obra
-----------

Antes de começarmos é imprescindível analisar a tabela com a qual iremos trabalhar. O Django possui um comando chamado ``inspectdb`` que pode lhe auxiliar nesse caso:

.. code-block:: bash

    $ ./manage.py inspectdb

Esse comando deve gerar uma output que é código Python que corresponde a todo o banco de dados que você possui mas, por algum motivo, isso não funcionou pra mim. Muito provavelmente por devido ao uso de esquemas no PostgreSQL...

Então vamos fazer da maneira mais difícil...

.. code-block:: bash

    $ psql -h postgresql.domain -p 5432 -U django_user django_db
    Senha para usuário django_user: 
    psql (9.5.3, servidor 9.1.9)
    conexão SSL (protocolo: TLSv1, cifra: AES256-SHA, bits: 256, compressão: desabilitado)
    Digite "help" para ajuda.

    django_db=> \d+ rh.rh_funcionario
                                        Tabela "rh.rh_funcionario"
           Coluna       |     Tipo       |   Modificadores     | Armazenamento | Estatísticas | Descrição 
     -------------------+----------------+---------------------+---------------+--------------+-----------
     matricula          | integer        | não nulo            | plain         |              | 
     nome               | character(200) | não nulo            | extended      |              | 
     email              | character(200) | não nulo            | main          |              | 
     endereco           | text           | não nulo            | extended      |              | 
     cpf                | numeric(11,0)  | não nulo            | main          |              | 
     telefone           | character(50)  | não nulo            | main          |              | 
     vinculacao         | smallint       |                     | plain         |              | 
     admissao           | date           | não nulo            | plain         |              | 
     nascimento         | date           | não nulo            | plain         |              | 
     cargo              | character(6)   | valor padrão de har | extended      |              | 
     (...)

Como podem ver, na tabela tem mais campos do que eu preciso (bem mais, essa tabela tem quase 80 campos!!!). Vamos nos focar no que eu preciso:

- email: ``char(200)``;
- endereço: ``text``;
- telefone: ``char(50)``.

Em seguida basta traduzir campo a campo... Este é o meu resultado em ``users/models.py``:

.. code-block:: python

    # -*- coding: utf-8 -*-

    from django.db import models

    class RHFuncionario(models.Model):
        email = models.CharField(max_length=200, primary_key=True)
        nome = models.CharField(max_length=200)
        telefone = models.CharField(max_length=50)
        endereco = models.TextField()

        class Meta:
            managed = False
            db_table = '"rh"."rh_funcionario"'

Todo o "segredo" desse código está dentro da subclasse ``Meta``. O *field* ``managed = False`` diz ao Django que essa tabela é apenas leitura e que ele não deve ser preocupar com as mudanças em seu modelo. Já o *field* ``db_table`` informa o nome da tabela que será executada. Como essa tabela fica em outro esquema (``scheme rh``), é necessário informar o nome do esquema antes da tabela.

Pronto, agora podemos rodar a *migration* e, em seguida, a aplicação:

.. code-block:: bash

    $ ./manage.py makemigrations && ./manage.py migrate
    Migrations for 'users':
      0001_initial.py:
        - Create model RHFuncionario

    $ ./manage.py migrate
    Operations to perform:
      Apply all migrations: users, contenttypes, auth, admin, sessions
    Running migrations:
      Rendering model states... DONE
      Applying users.0001_initial... OK

Apesar dele dizer que existe uma *migration* a ser executada para ``RHFuncionario``, isso não quer dizer que ele tentará criar a tabela, pode ficar tranquilo. O Django está apenas dizendo que irá registrar na sua tabela ``django_migrations`` a existência dessa tabela (note a linha 13 da tabela ``django_migrations`` e a linha 7 da tabela ``django_content_type``):

.. code-block:: bash

    django_db=#  select * from django_migrations;
     id |     app      |                   name                   |            applied
    ----+--------------+------------------------------------------+-------------------------------
      1 | contenttypes | 0001_initial                             | 2016-08-08 17:29:40.010196-03
      2 | auth         | 0001_initial                             | 2016-08-08 17:29:40.027248-03
      3 | admin        | 0001_initial                             | 2016-08-08 17:29:40.037895-03
      4 | admin        | 0002_logentry_remove_auto_add            | 2016-08-08 17:29:40.048169-03
      5 | contenttypes | 0002_remove_content_type_name            | 2016-08-08 17:29:40.076099-03
      6 | auth         | 0002_alter_permission_name_max_length    | 2016-08-08 17:29:40.085555-03
      7 | auth         | 0003_alter_user_email_max_length         | 2016-08-08 17:29:40.096129-03
      8 | auth         | 0004_alter_user_username_opts            | 2016-08-08 17:29:40.107211-03
      9 | auth         | 0005_alter_user_last_login_null          | 2016-08-08 17:29:40.116552-03
     10 | auth         | 0006_require_contenttypes_0002           | 2016-08-08 17:29:40.117427-03
     11 | auth         | 0007_alter_validators_add_error_messages | 2016-08-08 17:29:40.126812-03
     12 | sessions     | 0001_initial                             | 2016-08-08 17:29:40.129669-03
     13 | users        | 0001_initial                             | 2016-08-08 18:39:01.117818-03

    (13 registros)


    django_db=#  select * from django_content_type;
     id |  app_label   |     model
    ----+--------------+---------------
      1 | admin        | logentry
      2 | auth         | permission
      3 | auth         | group
      4 | auth         | user
      5 | contenttypes | contenttype
      6 | sessions     | session
      7 | users        | rhfuncionario

    (7 registros)

Agora vamos testar no Django shell:

.. code-block:: python

    $ ./manage.py shell
    Python 3.5.1 (default, Jul 10 2016, 20:36:01) 
    [GCC 6.1.1 20160621 (Red Hat 6.1.1-3)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from users.models import RHFuncionario
    >>> RHFuncionario.objects.all().exists()
    True
    >>> RHFuncionario.objects.get(email='magnun************com')
    <RHFuncionario: RHFuncionario object>
    >>> funcionario = RHFuncionario.objects.get(email='magnun************com')
    >>> funcionario.nome
    'Magnun Leno'
    >>>

Detalhe
-------

Não sei se alguém notou, mas na tabela original, a PK é a matrícula do funcionário, enquanto no meu código a PK é o email. Fiz desse jeito pois não adianta pra mim buscar pela PK do funcionário, já que eu não a obtenho pelo meu sistema, apenas o seu email. Se no seu sistema você tiver como obter essa PK, é preferível utilizá-la, pois os *indexes* do banco de dados criados sobre a PK, irão aumentar o desempenho das consultas. Além disso, se eu não informar um PK, o Django infere uma PK com o nome ``id``, um campo que não existe nessa tabela e iria incorrer em erros durante a busca.

Conclusão
---------

Como eu disse, é bem simples o processo. Basta utilizar o comando ``inspectdb`` ou, caso você seja sem sorte como eu, realizar uma tradução manual dos campos necessários.

Happy coding...
