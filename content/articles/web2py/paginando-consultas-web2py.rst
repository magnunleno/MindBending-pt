Paginando Consultas no Web2Py
#############################
:date: 2013-08-21 13:43
:category: Web2Py
:tags: banco, consultas, dados, dal, db, desempenho, divisão, modulo, paginação, python, web2py
:image: /images/web2py_logo.png
:slug: paginando-consultas-web2py

Dando continuidade ao assunto de `melhoria de desempenho em consultas
utilizando a DAL (Database Abstraction Layer) do Web2Py`_, hoje vou
abordar brevemente um assunto útil para reduzir o tempo de resposta de
algumas páginas: Paginação.

.. figure:: {filename}/images/w2p.png
	:align: center
	:target: {filename}/images/w2p.png
	:alt: Web2Py Banner

É extremamente comum que novos desenvolvedores criem páginas que listam,
por exemplo, todos os clientes do sistema de uma única vez. Entretanto,
quanto mais complexo é a visualização mais lenta a criação da página se
torna, por esses motivos é útil saber fazer a paginação de algumas
*views*.

.. more

O Conceito
----------

O conceito é extremamente simples: Reduzir o volume de dados a ser
consultado no banco de dados e, consequentemente, trafegado entre as
camadas da aplicação (*model*, *controller* e *view*), o servidor de
aplicação e a estação do cliente.

Digamos que no banco de dados temos 12 clientes e utilizaremos uma
paginação de 5 clientes por página. Desta forma, acabaremos com 3
páginas, sendo que a última terá apenas 2 clientes. Para auxiliar a
visualização, fiz um esquema gráfico:

.. figure:: {filename}/images/web2py-paginacao-clientes.png
	:align: center
	:target: {filename}/images/web2py-paginacao-clientes.png
	:alt: Diagrama de Paginacao dos Clientes - Web2Py

Para que possamos implementar isso, precisamos entender duas coisas,
como calcular a paginação e como fazer a consulta paginada no banco de
dados.

Calculando Páginas
~~~~~~~~~~~~~~~~~~

Primeiramente, para calcularmos o número de páginas precisamos saber
quantos clientes existe. Para isso, vamos utilizar o método ``count``.
Conforme abaixo:

.. code-block:: python

    total = db(db.cliente).count()

Já o calculo de páginas é bem simples, basta dividir o número total de
clientes (12 neste exemplo) pelo número de clientes que serão exibidos
por página (paginação), que neste caso é 5.

Se você testar isso no shell interativo do Python, verá que o resultado
é 2. Vemos que o Python nos ajuda em um ponto, pois ele já despreza a
parte fracionária e retorna apenas o número inteiro.

Entretanto, se verificarmos, de acordo com esse valor calculado serão
exibidos apenas 10 clientes (5\*2=10). Para o funcionamento correto
temos que verificar se a divisão é ou não exata, e para isso
utilizaremos a *divisão em módulo*, representada no Python pelo
caractere ``%``. Ao executar a divisão 12%5 você receberá um retorno
igual a 2, isto quer dizer que "o resto da divisão" é igual a 2. Em
outras palavras ele quer dizer que 2 + 2\*5 = 12 (o resto somado ao
inverso da divisão é igual ao valor inicial). Complicou? Simplificando,
isso quer dizer que ainda temos dois clientes para buscar :D.

No fim das contas, teremos um algoritmo similar a este:

.. code-block:: python

    paginacao = 5
    total = db(db.cliente).count()
    total_paginas = total/paginacao
    if (total%paginacao):
        total_paginas += 1

Pronto, agora sabemos que nossa consulta terá da página 1 até a página 3
(armazenada em ``total_paginas``), com isso podemos evitar a consulta a
uma página inexistente.

Realizando a Consulta Paginada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para realizar a consulta paginada precisamos saber de duas coisas: os
limites superiores e inferiores da consulta, isto é, quais clientes
serão exibidos na página informada. Se voltarmos no diagrama anterior,
vocês verão que a página 1 deve exibir os registro de 0 a 4 (clientes 1
a 5), a página 2 deve exibir os registros 5 a 9 (clientes 6 a 10) e a
página 3 deve exibir os registros 10 a 11 (clientes de 11 até o 12).
Para este exemplo vamos supor que o número da página está armazenado na
variável ``página``. Segue o código para este calculo:

.. code-block:: python

    limite_inferior = paginacao*(pagina-1)
    limite_superior = paginacao*pagina

Muito bem, agora basta realizar a consulta com estes limites. Para isto
utilizaremos o modificador de consulta ``limitby``, da seguinte forma:

.. code-block:: python

    db(db.cliente).select(limitby=(limite_superior, limite_inferior))

Código definitivo
-----------------

Muito bem, esta é base do conceito. Agora basta juntar tudo, colocar em
uma ``view``, implementar uma validação de número de página e dar uma
refatorada. No fim vamos ter algo mais ou menos assim:

.. code-block:: python

        def clientes():
            # Se não for unformado o número da página, deduzimos que é a primeira
            paginacao = 5
            if len(request.args) == 0:
                pagina = 1
            else:
                # Tenta converter o número da página
                try:
                    pagina = int(request.args[0])
                except ValueError:
                    # Redireciona para a página de erro
                    redirect(URL('erro', vars={
                            'msg':'Numero da página inválido'
                            }))

            # Se a página informada é 0, redireciona para a página 1
            if pagina <= 0:
                redirect(URL(args=1))

            # Total de clientes
            total = db(db.cliente).count()

            # Calcula o total de páginas
            paginas = total/paginacao
            if total%paginacao:
                paginas+=1

            # Se o número de página extrapolou o possível, redirecione para a 
            # última página
            if pagina > paginas:
                redirect(URL(args=[paginas]))

            # Calcula os limites da consulta
            limites = (paginacao*(pagina-1), (paginacao*pagina))
            registros = db(db.cliente).select(
                    limitby=limites,
                    )
            return dict(registros=registros, pagina=pagina, paginas=paginas)

Para a *view* vou apresentar um código bem simples que traz a opção de
passar para navegar nas páginas:

.. code-block:: jinja

        {{extend 'layout.html'}}

        <h1>Clientes</h1>


        <div id='contents'>
            <table class="table">
                <tr>
                <th>ID</th>
                <th>Cliente</th>
                <th>E-mail</th>
                </tr>
                {{ for registro in registros: }}
                <tr>
                <td>{{ =registro.id }}</td>
                <td>{{ =registro.nome }}</td>
                <td>{{ =registro.email }}</td>
                </tr>
                {{ pass }}
            </table>
        </div>

        <div id="paginacao">
            <ul class="pager">
                {{ if pagina != 1: }}
                <li class="previous">
                    <a href="{{ =URL(args=pagina-1) }}">&larr; Anterior</a>
                </li>
                {{ pass }}

                {{ if pagina != paginas: }}
                <li class="next">
                    <a href="{{ =URL(args=pagina+1) }}">Próxima &rarr;</a>
                </li>
                {{ pass }}
            </ul>
        <div>

Abaixo a captura dos testes:

.. raw:: html

        <div class="row"><div class="col-md-4 col-xs-6">

.. figure:: {filename}/images/web2py-paginacao-pagina-1.png
	:align: center
	:target: {filename}/images/web2py-paginacao-pagina-1.png
	:alt: Paginacao Web2Py - Pagina 1

        Clientes - Pagina 1

.. raw:: html

        </div><div class="col-md-4 col-xs-6">

.. figure:: {filename}/images/web2py-paginacao-pagina-2.png
	:align: center
	:target: {filename}/images/web2py-paginacao-pagina-2.png
	:alt: Paginacao Web2Py - Pagina 2

        Clientes - Pagina 2

.. raw:: html

        </div><div class="col-md-4 col-xs-6">

.. figure:: {filename}/images/web2py-paginacao-pagina-3.png
	:align: center
	:target: {filename}/images/web2py-paginacao-pagina-3.png
	:alt: Paginacao Wev2Py - Pagina 3

        Clientes - Pagina 3

.. raw:: html

        </div></div>

Bem, é isso. :)

.. _melhoria de desempenho em consultas utilizando a DAL (Database Abstraction Layer) do Web2Py: /pt/melhorando-desempenho-das-consultas-web2py-2
