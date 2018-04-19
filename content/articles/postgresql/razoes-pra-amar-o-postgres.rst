Algumas Razões Para Amar o PostgresSQL
######################################
:date: 2018-04-19 15:02
:category: PostgreSQL
:tags: python, django, postgresql, query, sql, orm, ingress
:image: /images/logos/postgresql.png

Geralmente, quando se fala em SGBDs OpenSource, a primeira resposta que se ouve é MySQL/MariaDB. Eu sempre torço meu nariz para respostas como essa... Implicancia pessoal? Talvez um pouco, mas existem `muitos fundamentos`_...

.. more

.. figure:: {filename}/images/postgres/elephant_by_robbertdb.jpg
	:target: {filename}/images/postgres/elephant_by_robbertdb.jpg
	:align: center
	:alt: Elephants by RobbertDB

        `Elephants by RobbertDB`_

Breve Histórico
===============

As raízes do PostgreSQL (comumente referido como Postgres), está em outro SGBD (`Ingress`_). Este foi um projeto de pesquisa na Universidade da Califórnia, Berkeley, que surgiu no início dos anos 70 e terminou em 1985. O Ingress também foi a origem para diversos outros SGBDs relacionais como, Sybase, Microsoft SQL Server, NonStop SQL e alguns outros.

Michael Stonebraker, um dos líderes de desenvolvimento do Ingress, abandonou Berkeley em 1982 para criar uma versão proprietária deste SGBD, porém retornou para a universidade rapidamente em 1985 e iniciou um novo projeto chamado Post-Ingress (um trocadilho se referindo a uma nova geração do Ingress). Stonebraker ganhou o prêmio `Turing Award em 2014`_  por ambos os projetos e por todas as técnicas pioneiras criadas por ele.

Posteriormente o projeto foi renomeado para POSTGRES e visava adicionar a capacidade de tipagem  e descrição de relacionamentos (tempos difíceis esse não?), ambos eram obrigação do "usuário do banco" (aplicação). O POSTGRES foi um dos primeiro bancos de dados a "entender" os relacionamentos entre tabelas e podia obter informações em tabelas relacionadas de maneira natural.

Vale ressaltar que o POSTGRES utilizou muitas das ideias do Ingress, mas nenhum código de seu ancestral.


Minhas Razões
=============

Como podemos ver, o Postgres foi inovador desde sua concepção, e hoje ele incorpora funcionalidades que outros SGBDs demoraram para adotar. 

Um bom exemplo foi a criação dos JSON Types (utilizando BJSON) na época do boom dos banco de dados não relacionais (NoSQL):

.. code-block:: sql

    CREATE TABLE perfil (
        ID serial NOT NULL PRIMARY KEY,
        /* ... */
        social_profiles json NULL
    );

    INSERT INTO perfil (social_profiles) VALUES (
        '{"twitter": "@magnun", "facebook": "@MindBending42"}'
    );

E sim, é possível realizar buscas e filtros dentro de campos JSON...

.. code-block:: sql

    /* Busca todos os perfis quetem conta no twitter cadastrada */
    SELECT * FROM perfil WHERE social_profiles ? 'twitter';

Mais sobre operações em JSON na `documentação oficial`_ e nesse `excelente artigo`_.

Parece pouco, mas para o mundo de APIs REST que vivemos hoje em dia, esse tipo de funcionalidade reduz absurdamente a carga cognitiva de criar uma tabela auxiliar ou criar um CSV dentro de um campo no banco de dados.

Outra funcionalidade muito útil são os Arrays Types:

.. code-block:: sql

    CREATE TABLE perfil (
        ID serial NOT NULL PRIMARY KEY,
        /* ... */
        telefones TEXT []
    );

    INSERT INTO contacts (name, phones) VALUES (
        ARRAY [ '(99) 9999-9999', '(66) 6666-6666' ]
    );

Só um alerta para os *newbyes*, não use Arrays e JSON Types para substituir relações, normalização de base ainda é muito importante.


Uma Última Funcionalidade
=========================

Recentemente descobri mais uma funcionalidade muito boa, e esta é o motivador deste texto.

Uma vez ou outra você se encontra na seguinte situação:

.. code-block:: sql

    CREATE TABLE usuario (
        id integer NOT NULL,
        username character varying(150) NOT NULL,
        /* ... */
    ) ;

    CREATE TABLE usuario_grupo (
        id integer NOT NULL DEFAULT,
        usuario_id integer NOT NULL,
        grupo_id integer NOT NULL,
        /* ... */
    );

    CREATE TABLE grupos (
        id integer NOT NULL DEFAULT,
        nome character varying(80) NOT NULL,
        /* ... */
    );

Na minha interface REST quero retornar algo como:

.. code-block:: json

    [
        {
            "id": 1,
            "username": "usuario_1",
            "grupos": ["escritor", "editor", "revisor"]
        },
        {
            "id": 2,
            "username": "usuario_2",
            "grupos": ["revisor"]
        },
        {
            "id": 3,
            "username": "usuario_3",
            "grupos": ["editor"]
        },
    ]

Para fazer algo assim, você tem duas opções. A primeira é obter a lista de usuários com join dos grupos e, na linguagem de programação, agrupar pelo id do usuário. A outra é fazer um SQL bizarro que retorna um texto no campo grupos concatenando o nome de todos os grupos separados por um delimitador. Aí na linguagem de programação você só faz um split. Não pegou a ideia? Aqui, leia essa pergunta do `StackOverflow`_.

Mas como o título do artigo diz, o Postgres é motivo de muito amor, já que ele tem suporte a um agregador chamado ``array_agg``. Veja-o em ação:

.. code-block:: sql

    SELECT
        usuario.id,
        usuario.username,
        ARRAY_AGG(grupo.nome) AS grupos
    FROM usuario
    LEFT JOIN usuario_grupo
        ON (usuario.id = usuario_grupo.usuario_id)
    LEFT JOIN grupo
        ON (usuario_grupo.grupo_id = grupo.id)
    GROUP BY usuario.id;

    /*
        id |  username |         grupos
        ----+----------+------------------------
        1 | usuario_1 | {escritor,editor,revisor}
        2 | usuario_2 | {revisor}
        3 | usuario_3 | {editor}
        (3 rows)
    */

.. image:: {filename}/images/meme/omg.jpg
    :target: {filename}/images/meme/omg.jpg
    :align: center
    :alt: OMG


E o Quico?
==========

"Tá, mas eu uso Django e ele tem um ORM, de que isso me server?". Bem, pequeno padawan, quando se usa um ORM é sempre muito importante observar a melhor forma de criar consultas, ou uma simples instrução pode resultar em diversas consultas ao banco de dados.

Felizmente, o Django também ama o PostgreSQL, pois, nativamente, ele também suporta o ``array_agg`` :D. Segue pequeno exemplo de uso:

.. code-block:: python

    >>> queryset = User.objects\
    ...     .annotate(arr=ArrayAgg('groups__name'))\
    ...     .values('id', 'username', 'grupos')
    ...
    >>> pprint([ i for i in queryset])
    [{'grupos': ['escritor', 'editor', 'revisor'],
      'id': 1,
      'username': 'usuario_1'},
     {'grupos': ['revisor'], 'id': 3, 'username': 'usuario_2'},
     {'grupos': ['editor'], 'id': 4, 'username': 'usuario_3'}]

Pronto, agora é só entregar esse ``queryset`` pra um ``serializer`` e correr pro *frontend* :)

.. _Elephants by RobbertDB: https://stocksnap.io/author/45460
.. _muitos fundamentos: https://www.cybertec-postgresql.com/en/why-favor-postgresql-over-mariadb-mysql/
.. _Ingress: https://en.wikipedia.org/wiki/Ingres_(database)
.. _Turing Award em 2014: https://amturing.acm.org/award_winners/stonebraker_1172121.cfm
.. _documentação oficial: https://www.postgresql.org/docs/9.5/static/functions-json.html
.. _excelente artigo: http://schinckel.net/2014/05/25/querying-json-in-postgres/
.. _StackOverflow: https://stackoverflow.com/questions/26846983/sql-join-and-group-items-as-an-array
