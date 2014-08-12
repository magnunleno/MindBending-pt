Conhecendo a DAL do Framework Web2Py
####################################
:date: 2013-08-12 18:40
:category: Web2Py
:tags: banco de dados, count, dal, database, framework, inner, insert, join, python, select, update, web, web2py
:image: /images/web2py_logo.png
:slug: conhecendo-dal-framework-web2py

Recentemente, graças aos trabalhos em conjunto com o `Criandeiros`_,
acabei me envolvendo de verdade com a área de desenvolvimento Web, mais
especificamente com o `framework Web2Py`_. E quem acompanha meu blog, já
sabe que minha "zona de conforto" se estende somente sobre o domínio do
desenvolvimento Desktop, logo estou tendo que aprender **muita** coisa
nova.

.. image:: {filename}/images/w2p.png
	:align: center
	:target: {filename}/images/w2p.png
	:alt: Web2Py Banner

Mas uma das áreas do desenvolvimento que tenho me dedicado muito é ao
framework Web2Py e suas características. Uma das partes que mais me
chamou a atenção é a `DAL (Database Abstraction Layer)`_, em tradução
livre: camada de abstração de banco de dados.

.. more

Database Abstraction Layer
--------------------------

A DAL não é nem de longe um ORM, e sou grato Massimo Di Pierro (criador
do Web2Py) por isso. Por quê? Pelo simples fato de que (em minha opinião
e de maneira geral) este tipo de ferramenta geralmente retira a
complexidade e prejudica o desempenho. Claro, muitas ferramentas de ORM
possuem funcionalidades para otimizar as consultas, por isso coloquei a
ressalva "de maneira geral" na frase anterior. Esta ressalva se refere
justamente ao uso descuidado ou simplesmente à falta de conhecimento da
ferramenta. E é neste momento que a DAL do Web2Py mostra seu poder, pois
sua utilização é similar a uma consulta SQL, sendo assim extremamente
intuitiva.

Vejam alguns exemplos...

.. code-block:: python

        # Consulta Todos os Cliente
        db(db.cliente).select()
        # Conta Clientes Existentes
        db(db.cliente).count()
        # Consulta Todos os Cliente e Ordena Pelo Nome
        db(db.cliente).select(orderby=db.cliente.nome)
        # Consulta Cliente com ID Igual a 10
        db(db.cliente.id == 10).select()
        # Verifica se Existe algum Cliente com ID Igual a 10
        db(db.cliente.id == 10).isempty()
        # Insere Cliente
        db.cliente.insert(nome="Fulano", email="fulano@mail.com")
        # Atualiza Cliente com ID 10
        db(db.cliente.id == 10).update(email="cliente@mail.com")
        # Consulta Cliente e Sua Mensalidade (Inner Join)
        db(db.cliente.id == db.cliente_mensalidade.cliente).select()

Esse é só um rápido *overview* das possibilidades que a DAL proporciona,
existem várias outras disponíveis, basta ler `sua documentação`_.

Curiosamente, uma das funcionalidades mais interessantes da DAL, a
restrição de campos na consulta, é citada pouquíssimas vezes em sua
documentação. A funcionalidade deste campo é simplesmente limitar as
colunas a serem retornadas do banco de dados. Reduzindo assim o tempo de
consulta, o fluxo de dados entre o banco de dados e a aplicação, a
alocação de memória (tanto no banco quanto na aplicação) para a
consulta, a quantidade de lixo a ser coletada pelo garbage collector do
Python e reduzindo a exposição de dados para as views.

Para limitar as colunas que serão retornadas basta informar os campos
desejados dentro do método select, conforme exemplos abaixo:


.. code-block:: python

        # Consulta Todos os Cliente
        db(db.cliente).select(
            db.cliente.id, db.cliente.nome, db.cliente.nome
        )

        # Consulta Cliente e Sua Mensalidade (Inner Join)
        db(db.cliente.id == db.cliente_mensalidade.cliente).select(
            db.cliente.id, db.cliente.nome, db.cliente.email,
            db.cliente_mensalidade.data_vencimento
        )
            

Em um próximo artigo darei um exemplo que mensura bem a vantagem que é
utilizar as restrições de campos na DAL do Web2Py.

Até lá...

.. _Criandeiros: /pt/criandeiros-particularidades-python
.. _framework Web2Py: http://web2py.com/
.. _DAL (Database Abstraction Layer): http://www.web2py.com/book/default/chapter/06
.. _sua documentação: http://www.web2py.com/book/default/chapter/06
