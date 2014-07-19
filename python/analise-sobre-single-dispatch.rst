Análise sobre o Single-dispatch
###############################
:date: 2013-06-10 15:40
:category: Python
:tags: desempenho, desenvolvimento, profile, programação, python, singledispatch, tempo, teste
:image: /images/snake-skeleton-thumb.jpg

Há alguns dias eu escrevi sobre a `PEP 434 e o conceito do single-dispatch`_, demonstrando como usufruir das funcionalidades dessa PEP sem ter que esperar a próxima versão do Python, prevista somente para 2014. Hoje vamos fazer uma breve análise sobre o comportamento do Python ao realizar essas chamadas e seus impactos no desempenho.

.. figure:: {filename}/images/snake-skeleton.jpg
   :align: center
   :alt: Snake Skeleton

   Snake Skeleton

Não sou nenhum especialista em Python, logo minhas análises e conclusões podem não ser 100% corretas, mas uma coisa é certa, as medições estão corretas.

.. more

O Código
--------

Para estes testes estendemos o `código incial`_ com o intuito de simular o comportamento do *single-dispatch* sem o uso de dicionários, apenas usando *ifs e elses*. Abaixo o código:

.. code-block:: python

        #!/usr/bin/env python
        # encoding: utf-8

        import cProfile

        class singledispatch(object):
            __slots__ = (
                    'resolver',
                    'default',
                    'last',
                    )
            def __init__(self, func):
                self.resolver = {}
                self.default = func
                self.last = None

            def register(self, *signature):
                def wrapper(function):
                    if isinstance(function, singledispatch):
                        self.resolver[signature] = self.last
                    else:
                        self.resolver[signature] = function
                        self.last = function
                    return self
                return wrapper

            def __call__(self, *args):
                signature = tuple(map(type, args))
                func = self.resolver.get(signature, self.default)
                return func(*args)


        @singledispatch
        def echo(arg):
            #print 'Fallback mode:',arg
            pass

        @echo.register(float)
        @echo.register(int)
        def echo(number):
            #print 'Number:', number
            pass

        @echo.register(str)
        def echo(text):
            #print 'Text:', text
            pass

        def _echo_static_fallback(arg):
            #print 'Fallback mode:',arg
            pass

        def _echo_static_num(number):
            #print 'Number:', number
            pass

        def _echo_static_str(text):
            #print 'Text:', text
            pass

        def echo_static1(arg):
            if type(arg) == str:
                _echo_static_str(arg)
            if (type(arg) == int) or (type(arg) == float):
                _echo_static_num(arg)
            else:
                _echo_static_fallback(arg)

        def echo_static2(arg):
            if isinstance(arg, str):
                _echo_static_str(arg)
            if isinstance(arg, int) or isinstance(arg, float):
                _echo_static_num(arg)
            else:
                _echo_static_fallback(arg)

        def test_decorated_dispatch():
            for i in xrange(100000):
                echo("asd")
                echo(42)
                echo(3.42)
                echo([1, 2, 3])

        def test_static_dispatcher1():
            for i in xrange(100000):
                echo_static1("asd")
                echo_static1(42)
                echo_static1(3.42)
                echo_static1([1, 2, 3])

        def test_static_dispatcher2():
            for i in xrange(100000):
                echo_static2("asd")
                echo_static2(42)
                echo_static2(3.42)
                echo_static2([1, 2, 3])

        if __name__ == '__main__':
            cProfile.run('test_decorated_dispatch()')
            cProfile.run('test_static_dispatcher1()')
            cProfile.run('test_static_dispatcher2()')

Como podem ver eu criei mais 3 funções (``_echo_static_fallback``, ``_echo_static_num`` e ``_echo_static_str``) para realizar o *single-dispatch* baseado "manualmente". Além dessa também foi necessário criar 2 funções "centrais" (``echo_static1`` e ``echo_static2``), responsáveis por analisar os argumentos e realizar o *single-dispatch* (substituindo a necessidade do decorador). Por fim criei mais três funções (``test_decorated_dispatch``, ``test_static_dispatcher1`` e ``test_static_dispatcher2``) que realizarão 100.000 chamadas de seus respectivos *single-dipatchers*. Uma vez que todas as funções serão executadas 100.000 vezes, foi necessário comentar todos os comandos ``print``, caso contrário esse programa geraria uma saída monstruosa.

Execução do Teste
-----------------

Muito bem, após a execução foi gerada a seguinte saída:

::

           1600003 function calls in 0.688 seconds

     Ordered by: standard name

     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
          1    0.000    0.000    0.688    0.688 :1()
     400000    0.365    0.000    0.543    0.000 sindis-cmp.py:27(__call__)
     100000    0.010    0.000    0.010    0.000 sindis-cmp.py:33(echo)
     200000    0.018    0.000    0.018    0.000 sindis-cmp.py:38(echo)
     100000    0.010    0.000    0.010    0.000 sindis-cmp.py:44(echo)
          1    0.145    0.145    0.688    0.688 sindis-cmp.py:77(test_decorated_dispatch)
     400000    0.095    0.000    0.095    0.000 {map}
          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     400000    0.045    0.000    0.045    0.000 {method 'get' of 'dict' objects}


           900003 function calls in 0.364 seconds

     Ordered by: standard name

     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
          1    0.000    0.000    0.364    0.364 :1()
     200000    0.015    0.000    0.015    0.000 sindis-cmp.py:49(_echo_static_fallback)
     200000    0.017    0.000    0.017    0.000 sindis-cmp.py:53(_echo_static_num)
     100000    0.009    0.000    0.009    0.000 sindis-cmp.py:57(_echo_static_str)
     400000    0.247    0.000    0.288    0.000 sindis-cmp.py:61(echo_static1)
          1    0.075    0.075    0.364    0.364 sindis-cmp.py:94(test_static_dispatcher1)
          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


           2000003 function calls in 0.622 seconds

     Ordered by: standard name

     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
          1    0.000    0.000    0.622    0.622 :1()
          1    0.079    0.079    0.622    0.622 sindis-cmp.py:101(test_static_dispatcher2)
     200000    0.016    0.000    0.016    0.000 sindis-cmp.py:49(_echo_static_fallback)
     200000    0.018    0.000    0.018    0.000 sindis-cmp.py:53(_echo_static_num)
     100000    0.010    0.000    0.010    0.000 sindis-cmp.py:57(_echo_static_str)
     400000    0.346    0.000    0.543    0.000 sindis-cmp.py:69(echo_static2)
    1100000    0.153    0.000    0.153    0.000 {isinstance}
          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Como podem ver, a execução com o decorador *single-dispatch* levou 0.688 segundos, enquanto as execuções com o *single-dispatch* manual levaram 0.364 segundos e 0.622 segundos, respectivamente.

Análises
--------

Apenas pelo tempo de execução já podemos deduzir que a execução por meio do decorador é mais lenta e, dentre as duas implementações do *single-dispatch* manual, a que se utiliza do método ``type`` possui um melhor desempenho. Para um melhor entendimento deste comportamento vamos analisar todo o programa por etapas.

Invocando o *Dispatcher*
~~~~~~~~~~~~~~~~~~~~~~~~

Uma das coisas mais curiosas que eu encontrei foi a diferença de tempo de execução (quase o dobro) das funções de teste do *dispatch*, tendo como base apenas a coluna *tottime* que, conforme `documentação do Python`_, expressa o tempo total gasto na função excluindo os tempos gastos na subfunção. Veja abaixo uma seleção dos tempos agrupados para melhor visualização:

::

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         1    0.145    0.145    0.688    0.688 sindis-cmp.py:77(test_decorated_dispatch)
         1    0.075    0.075    0.364    0.364 sindis-cmp.py:94(test_static_dispatcher1)
         1    0.079    0.079    0.622    0.622 sindis-cmp.py:101(test_static_dispatcher2)

Esta diferença me leva a acreditar que o processo de invocar uma função decorada leva quase o dobro do tempo gasto ao invocar uma função comum.

Decisão do *Dispatcher*
~~~~~~~~~~~~~~~~~~~~~~~

Ao destacarmos o tempo de execução de cada função que toma a decisão de qual subfunção será executada, e nos focarmos na coluna *tottime*, constatamos a diferença de tempo entre as seguintes operações: consulta no dicionário (método ``__call__``), verificação do tipo (método ``echo_static1``) e verificação de herança (método ``echo_static2``).

::

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    400000    0.365    0.000    0.543    0.000 sindis-cmp.py:27(__call__)
    400000    0.247    0.000    0.288    0.000 sindis-cmp.py:61(echo_static1)
    400000    0.346    0.000    0.543    0.000 sindis-cmp.py:69(echo_static2)

Execução das subfunções
~~~~~~~~~~~~~~~~~~~~~~~

Com exceção da função de *fallback* todas as outras tiveram tempos extremamente próximos (com diferenças de 0.001 segundos):

**Função de *Fallback***

::

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    100000    0.010    0.000    0.010    0.000 sindis-cmp.py:33(echo)
    200000    0.015    0.000    0.015    0.000 sindis-cmp.py:49(_echo_static_fallback)
    200000    0.016    0.000    0.016    0.000 sindis-cmp.py:49(_echo_static_fallback)

**Função para Números**

::

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    200000    0.018    0.000    0.018    0.000 sindis-cmp.py:38(echo)
    200000    0.017    0.000    0.017    0.000 sindis-cmp.py:53(_echo_static_num)
    200000    0.018    0.000    0.018    0.000 sindis-cmp.py:53(_echo_static_num)

**Função para *Strings***

::

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    100000    0.010    0.000    0.010    0.000 sindis-cmp.py:44(echo)
    100000    0.009    0.000    0.009    0.000 sindis-cmp.py:57(_echo_static_str)
    100000    0.010    0.000    0.010    0.000 sindis-cmp.py:57(_echo_static_str)

Conclusões
----------

Bem, creio que este tipo de conclusão cada um deve tomar a sua, eu sei que eu continuarei utilizando o meu *duck-typing* como sempre fiz.

Até a próxima.

.. _PEP 434 e o conceito do single-dispatch: /pt/fazendo-seu-proprio-single-dispatch
.. _código incial: /pt/fazendo-seu-proprio-single-dispatch
.. _documentação do Python: http://docs.python.org/2/library/profile.html
