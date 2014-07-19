Reutilizando Consultas no Web2py
################################
:date: 2013-08-22 17:17
:category: Web2Py
:tags: banco, consulta, dados, database, desenvolvimento, programação, python, refatoramento, reutilização, web, web2py
:image: /images/web2py_logo.png
:slug: reutilizando-consultas-web2py

Apesar da DAL (Database Abstraction Layer) do Web2py ser excelente, ela
geralmente é utilizada erroneamente. É muito comum ver consultas
escritas na camada do *controller* sendo que este tipo de trabalho deve
ser feito pela camada *model* e sanando assim um grande dilema: o reuso
de consultas.

.. image:: {filename}/images/web2py.jpg
	:align: center
	:target: {filename}/images/web2py.jpg
	:alt: web2py

Como vocês podem ver, graças ao `Criandeiros`_ eu tenho retornada a este
`assunto`_ `algumas`_ `vezes`_. E da forma como eu tenho brincado com a
camada de abstração do Web2Py, podem ter certeza de que esse assunto vai
voltar mais algumas vezes.

.. more

Muitas pessoas vão dizer que não há problema nenhum em realizar
consultas dentro das *views*. Para estas, aqui vai uma história.

O Problema
----------

Para entender porque eu considero o reuso de consultas essencial, tentem
ver o seguinte ambiente: uma aplicação intermediária que possui uma base
com uma porção considerável de tabelas interligadas por relacionamentos.

Agora imagine todas as consultas espalhadas pelas diversas *views* da
aplicação, mais cedo ou mais tarde você vai precisar repetir uma
consulta. E agora? Onde você fez essa consulta? Uma pequena busca por
todos os arquivos da camada *view* resolve o problema.

Mais alguns dias de trabalho e você tem uma sensação de *deja vú* ao
escrever uma consulta. Alguns minutos pesquisando na base de código e
**bang**, lá está ela de novo. Mas tudo bem, foram apenas três
repetições, *not a big deal*.

Então, em uma bela manhã você percebe uma necessidade pontual de adaptar
levemente o modelo de dados, um trabalho trivial eu diria. Depois de
realizar a alteração você precisa buscar por todas as *views* e realizar
a mesma alteração em várias consultas repetidas. Mas tudo bem, depois de
um pouco de retrabalho a alteração está feita, podemos dar o dia como
fechado.

Mas é então que começa a chuva de reclamações: *views* inconsistentes,
*tracebacks* em diversas páginas, consultas retornando dados
duplicados... Tudo por quê você não rastreou todas as consultas que
utilizam esta tabela. Não teria sido melhor ter concentrado e
reutilizado algumas consultas por meio de funções parametrizadas?

Como Evitar
-----------

Simples, basta criar um (ou alguns) arquivo dentro da pasta *models*
contendo algumas funções com nomes sugestivos, por exemplo:
``busca_clientes_inadimplentes``, ``busca_cliente_paginado``,
``busca_pagamento_por_cliente`` e etc.

Basta lembrar que dentro da pasta *model* os arquivos são importados em
ordem alfabética. Logo talvez valha a pena pensar bem no nome destes
arquivos.

Exemplo de Função Parametrizada
-------------------------------

Um exemplo simples de função parametrizada pode ser buscar o cliente e
seu endereço (o *join* de duas tabelas) mas sem limitar o usuário,
permitindo a ele informar a forma de ordenação (``orderby``), os campos
a serem retornados e etc.

.. code-block:: python

    def busca_cliente_mensalidades(id_cliente, condicoes=[], campos=[], filtros={}):
        return db(
            (db.cliente.id == id_cliente) &
            (db.clienteid == db.mensalidade.cliente), 
            *condicoes
            ).select(*campos, **filtros)

Abaixo alguns exemplos de chamada:

.. code-block:: python

    # Busca todas as mensalidades do cliente com ID = 10
    busca_cliente_mensalidade(10)

    # Busca todas as mensalidades do cliente com ID = 10 ordenadas pela
    # data de vencimento
    busca_cliente_mensalidade(10, filtros={'orderby' : db.mensalidade.vencimento})

    # Busca apenas os IDs das mensalidades do cliente com ID=10 com 
    # vencimento superior a 22/08/2012
    busca_cliente_mensalidade(10, 
            condicoes=[db.mensalidade.vencimento>=datetime.date(2012, 08, 22)], 
            campos=[db.mensalidade.id]
        )

Exemplo Mais Complexo
---------------------

Um bom exemplo de consulta parametrizada pode ser feito tendo como base
o artigo anterior sobre paginação de consultas. O exemplo abaixo
possibilita paginar **qualquer** consulta:

.. code-block:: python

    def consultaComPaginacao(consulta, pagina=1, paginacao=10, campos=[], filtros={}):
        if pagina <= 0:
            redirect(URL(args=[pagina]))

        total = consulta.count()
        paginas = total/paginacao
        if total%paginacao:
            paginas+=1

        if pagina > paginas:
            redirect(URL(args=[paginas]))

        limites = (paginacao*(pagina-1), (paginacao*pagina))
        registros = consulta.select(
                limitby=limites,
                *campos,
                **filtros
                )
        return (registros, paginas)

Parece meio absurdo, mas essa função pode ser utilizada para paginar
qualquer consulta, conforme exemplos abaixo:

.. code-block:: python

    # Consulta a página 2 contendo o nome e o endereço de todos os clientes
    # tendo como com paginação=20 e ordenados pelo nome
    consultaComPaginacao(
        consulta=db(db.cliente),
        pagina=2,
        paginacao=10,
        campos=(db.cliente.id, db.cliente.nome),
        filtros={'orderby': db.cliente.nome}
    )

    # Consulta a página 1 de todos endereços ativos dos cliente dos clientes
    # Limitando o retorno a apenas o id e o nome do cliente e todos os 
    # dados do endereço)
    consultaComPaginacao(
        consulta=db(
            (db.cliente.id == db.cliente_endereco.cliente) &
            (db.cliente_endereco.ativo == True)
            )
        paginacao=10,
        campos=(db.cliente.id, db.cliente.nome, db.endereco.ALL),
        filtros={'orderby': db.cliente.nome|db.endereco.id}
    )

Como podem ver, nada muito complexo :)

.. _Criandeiros: /pt/tag/criandeiros
.. _assunto: /pt/melhorando-desempenho-das-consultas-web2py-2
.. _algumas: /pt/conhecendo-dal-framework-web2py
.. _vezes: /pt/paginando-consultas-web2py
