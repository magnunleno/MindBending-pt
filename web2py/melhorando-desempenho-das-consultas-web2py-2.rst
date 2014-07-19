Melhorando o Desempenho das Consultas no Web2Py
###############################################
:date: 2013-08-13 16:49
:category: Web2Py
:tags: banco de dados, dal, datqabase, desempenho, framework, guppy, pygal, pympler, python, select, web, web2py
:image: /images/web2py_logo.png
:slug: melhorando-desempenho-das-consultas-web2py-2

Conforme mostrado `ontem`_, o framework Web2Py não se utiliza de um ORM
para realizar a abstração do banco de dados, ele utiliza o que ele mesmo
chama de DAL (Database Abstraction Layer). A DAL é uma biblioteca que
provê uma maneira mais "pythonica" de acessar o banco de dados,
utilizando uma estrutura que "lembra" uma consulta SQL mas sem utilizar
nenhuma linhas desta linguagem.

.. image:: {filename}/images/w2p.png
	:align: center
	:target: {filename}/images/w2p.png
	:alt: Web2Py Banner

Esta abordagem traz consigo uma maleabilidade excelente e (ao contrário
dos ORMs) mantem a consulta ao banco de dados inteiramente sob sua
administração. Entretanto, mesmo sendo maleável e customizável, ele
sofre do mesmo mal que os ORMs: Mal uso.

.. more

O Problema
----------

Como eu comentei anteriormente, eu tenho trabalhado com o Criandeiros
(mais informações `aqui`_) e foi em um projeto deles que eu lidei um
grande dilema: Limitar os campos de busca.

Estou me referindo à possibilidade de limitar quais campos serão
buscados no banco de dados, pois vi algumas consultas a uma tabela com
26 colunas sendo que eram necessários apenas alguns poucos campos, por
exemplo, ``db.cliente.nome`` e ``db.cliente.email``. Pensando
rapidamente (conforme citado `anteriormente`_) eu afirmaria que
restringir o número de colunas a serem buscadas durante a consulta ao
banco de dados pode trazer diversas vantagens, tanto sob a ótica do
tempo de execução quando do consumo de memória.

Sobre o consumo de memória podemos ressaltar o seguinte:

-  Reduz a alocação de memória no servidor de banco de dados;
-  Reduz a alocação de memória no servidor de aplicação;
-  Um objeto menor é passado da camada "*Controller*" para a camada
   "*View*";
-  Reduz o número de objetos a serem tratados pelo *garbage collector*.

Já sobre o tempo de execução, os seguintes fatores contribuem para sua
redução:

-  Uma consulta menor é executada em menos tempo no banco de dados;
-  Um *result set* menor é transferido em menos tempo entre o banco de
   dados e a aplicação;
-  Um *result set* menor é interpretado em menos tempo pelo Python;

Além destas melhorias mensuráveis, existe também uma melhoria de não
mensurável: Melhoria da segurança. Uma vez que menos dados são passados
para a camada "*view*", menos dados são expostos e menos informações
sensíveis estarão sujeitos a serem capturados devido a uma falha do
programador, como por exemplo:

-  Esquecer de definir uma *view*;
-  Implementar um XML WebService genérico;
-  Implementar uma API XML/JSON genérica;
-  Implementar um XML RPC genérico;

Antes que alguém fale que isso é difícil de acontecer, saiba que as
"`*generic views*`_" eram distribuídas por padrão até o Web2Py v.1.95.2
e foram removidas por gerar exposição indevida de dados. Mas apesar de
ter sido removida, `ainda é possível implementá-la`_.

Mas vamos deixar de falação e vamos para a parte prática...

O ambiente
----------

Neste ambiente estaremos trabalhando em um *desktop* com as seguintes
especificações:

CPU:
    Intel® Pentium(R) Dual Core - CPU G870 @ 3.10GHz
Memória:
    8 GBytes
Arquitetura:
    64 Bits
Python:
    2.7.3
Web2Py:
    Version 2.6.0-development

O banco de dados e a aplicação estão rodando no mesmo servidor, pois
estamos usando o banco de dados `SQLite`_.

A base utilizada possui uma tabela chamada ``cliente``, com 26 colunas
(atributos) e 19 linhas (19 clientes).

Faremos um teste bem drástico para ressaltar bem o comportamento que
desejamos exemplificar: Uma consulta que retorna **todas** as colunas e
uma consulta que retorna apenas dois campos, nome e email. Para isso
utilizaremos as seguintes consultas:

.. code-block:: python

    s1 = db(db.cliente).select()
    s2 = db(db.cliente).select(db.cliente.nome, db.cliente.email)

O Código
--------

Para este teste de tempo de execução utilizaremos o seguinte
*controller*:

.. code-block:: python

    def __consulta_todos_campos(count):
        inicio = time()
        for i in range(count):
            db(Cliente).select()
        return round(time() - inicio, 4)

    def __consulta_alguns_campos(count):
        inicio = time()
        for i in range(count):
            db(Cliente).select(Cliente.nome, Cliente.email)
        return round(time() - inicio, 4)

    def testa_consulta():
        import pygal
        from pygal.style import CleanStyle

        bar_chart = pygal.HorizontalBar(style=CleanStyle, 
                width=1200, 
                height=400,
                explicit_size=True)

        x_axis = [1, 10, 100, 1000, 10000]
        y_axis1 = []
        for n in x_axis:
            y_axis1.append(__consulta_todos_campos(n))

        y_axis2 = []
        for n in x_axis:
            y_axis2.append(__consulta_alguns_campos(n))

        bar_chart.add('Alguns Campos', y_axis2[:-1])
        bar_chart.add('Todos Campos', y_axis1[:-1])
        bar_chart.x_labels = map(str, x_axis[:-1])

        return dict(
                result1=y_axis1, 
                result2=y_axis2, 
                chart=bar_chart.render(), 
                x_axis=x_axis
                )

Notem que a medição é realizada nas funções ``__consulta_todos_campos``
e ``__consulta_alguns_campos`` com o módulo ``time`` e é utilizada a
biblioteca `PyGal`_ para a plotagem do gráfico. Outro ponto importante é
que, apesar das medições serem feitas para 1 consulta, 10 consultas, 100
consultas, 1.000 consultas e 10.000 consultas, eu ploto no gráfico
apenas o intervalo de 1 consulta a 1.000 consultas. Isso se deve ao fato
do crescimento do tempo de resposta para 10.000 consultas, o que torna
quase invisível os outros resultados.

Para visualizar o resultado utilizaremos a seguinte *view*:

.. code-block:: jinja

    Consulta Todos os Campos
    {{ for n,val in zip(x_axis, result1): }}
        {{ =n }}: {{ =val }}
    {{ pass }}



    Consulta Alguns os Campos
    {{ for n,val in zip(x_axis, result2): }}
        {{ =n }}: {{ =val }}
    {{ pass}}

    Gráfico

    {{ =XML(chart) }}

Agora vamos para resultados mensuráveis....

O Tempo de Execução
-------------------

Após a execução temos os seguintes resultados:

.. table::
        :class: table

        ====================== ================ ====================== ================================
        Número de Consultas    Alguns Campos    Todos os Campos        Ganho [100 - 100\*(menor/maior)]
        ====================== ================ ====================== ================================
        1                      0.0005           0.0069                 92.75%
        10                     0.0036           0.0447                 91.95%
        100                    0.0348           0.438                  92.05%
        1.000                  0.3474           4.4669                 92.22%
        10.000                 3.4757           42.7637                91.87%
        ====================== ================ ====================== ================================

Com estes dados (desprezando o resultado de 10.000 consultas) plotamos o
seguinte gráfico:

.. image:: {filename}/images/web2py-DAL-benchmark.png
	:align: center
	:target: {filename}/images/web2py-DAL-benchmark.png
	:alt: web2py DAL benchmark

Com uma análise rápida, podemos afirmar que se você pretende servir sua
aplicação para algo por volta de 1.000 clientes e deseja que sua
aplicação responda em menos de 4 segundos, você deve tomar muito cuidado
como você faz as suas consultas.

Consumo de Memória
------------------

Infelizmente, por algum motivo absurdo e alheio ao meu conhecimento, eu
não consegui colocar a minha biblioteca de *Memory Profiling* predileta,
a `Guppy`_, e tive que usar uma que eu não conheço muito, a `Pympler`_.

Infelizmente esta biblioteca não interpreta muito bem os Objetos
``Rows`` e ``Row`` do Web2Py, desta forma os resultados de memoria
alocada que são medidos são inferiores aos reais, já que ao converter a
``Rows`` para uma ``list`` e a ``Row`` para ``dict`` perdemos o
*overhead* das classes originais (já que usamos objetos nativos do
Python).

Mas mesmo diante desdas discrepâncias, o resultado ainda é interessante.
Vejam abaixo:

.. code-block:: python

    >>> from pympler import summary
    >>> s1 = db(db.cliente).select()
    >>> s2 = db(db.cliente).select(db.cliente.nome, db.cliente.email)
    >>> sum1 = summary.summarize([i.as_dict() for i in s1])
    >>> sum2 = summary.summarize([i.as_dict() for i in s2])
    >>> sum1
    [['dict', 19, 63688]]
    >>> sum2
    [['dict', 19, 5320]]
    >>> summary.print_(sum1)
      types |   # objects |   total size
    ======= | =========== | ============
       dict |          19 |     62.20 KB
    >>> summary.print_(sum2)
      types |   # objects |   total size
    ======= | =========== | ============
       dict |          19 |      5.20 KB
    >>> 

Como podemos ver, uma consulta da tabela inteira (19 linhas) com todas
as suas colunas (26) resulta na alocação de 62.20 KBytes, enquanto uma
consulta da tabela inteira (19 linhas) com apenas 2 colunas (nome e
e-mail do cliente) ocupa apenas 5.20 KBytes, uma diferença de 57 KBytes.
Lembrando que isso é para apenas **uma** consulta, em um sistema
concorrente isso pode ser multiplicado pelo número de usuários
concorrentes no sistema.

Conclusão
---------

Tendo como base todo o contexto acima, vemos que restringir o retorno da
consulta, apesar de amarrar um pouco a *view* aos *controllers* e
*models*, é extremamente vantajoso para aqueles que querem garantir o
bom funcionamento de sua aplicação.

Até a próxima...

.. _ontem: /pt/conhecendo-dal-framework-web2py
.. _aqui: /pt/criandeiros-particularidades-python
.. _anteriormente: /pt/conhecendo-dal-framework-web2py
.. _*generic views*: http://www.web2py.com/book/default/chapter/10#Generic-views
.. _ainda é possível implementá-la: http://comments.gmane.org/gmane.comp.python.web2py/67902
.. _SQLite: http://www.sqlite.org/
.. _PyGal: http://pygal.org/
.. _Guppy: http://guppy-pe.sourceforge.net/
.. _Pympler: http://pythonhosted.org/Pympler/muppy.html
