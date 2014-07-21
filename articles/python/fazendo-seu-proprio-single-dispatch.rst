Fazendo seu Próprio Single-dispatch
###################################
:date: 2013-06-05 16:02
:category: Python
:tags: 443, decoradores, decorators, desenvolvimento, pep, programação, python, singledispatch
:image: /images/python.png

Há alguns dias, pra ser mais exato em 22 de Maio de 2013, foi proposta a
`PEP 443 -- Single-dispatch Generic Functions`_. Esta proposta foi
aceita ontem, dia 04 de Junho de 2013, e esta nova funcionalidade deve
estar presente na próxima versão do Python. Em resumo, ela "resolve" um
problema inerente à característica de tipagem dinâmica do Python, a
criação de uma mesma função porém com vários tipos de argumentos
diferentes.

.. image:: {filename}/images/Python_logo_and_name.png
	:align: center
	:target: {filename}/images/Python_logo_and_name.png
	:alt: Python logo and name

Pessoalmente eu não acho que isso seja um grande problema e sempre usei
o conceito de duck typing para tratar argumentos, porém, em certos
momentos este, esta funcionalidade pode ser útil, e confesse que eu já
havia brincado com essa ideia antes. Como o Python 3.4 está previsto
apenas para o ano de 2014 resolvi compartilhar meu rascunho que atende
em 50% os requisitos da PEP 443.

.. more

Pontos Chaves
-------------

O código deste decorador é até bem simples, e possui apenas 2 pontos
chaves:

-  Utiliza um dicionário ``self.resolver`` para mapear os possíveis
   argumentos com as suas respectivas funções;
-  Armazenar em um variável específica (``self.last``) a ultima função
   recebida pelo decorador;

Creio que, destes dois pontos, apenas este última valha uma boa
explicação. Porquê armazenar em uma variável a última função atribuída?
Devido ao funcionamento interno do decorador. Quando utilizamos um
decorador sobre outro decorador, o Python atribui o decorador de dentro
para fora. Vamos ao exemplo:

.. code-block:: python

    @decorador2
    @decorador1
    def funcao(argumentos):
        pass

Neste exemplo o ``decorador1`` recebe a ``funcao`` e o ``decorador2``
recebe a ``funcao`` já decorada pelo ``decorador1``. E isso pode gerar
um loop infinito na nossa implementação.

Para evitar esse tipo de comportamento, verificamos no método
``register`` se a função passada é uma função decorada ou não (instância
da classe ``singledispatch``). Caso positivo podemos afirmar
categoricamente que esta última função decorada pelo nosso decorador é a
mesma que deve ser aplicada nesse caso, isto é, esta função possui 2
assinaturas diferentes.

Código
------

Muito bem, vamos ao código!

.. code-block:: python

        #!/usr/bin/env python2
        # encoding: utf-8

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
            print 'Fallback mode:',arg

        @echo.register(float)
        @echo.register(int)
        def echo(number):
            print 'Number:', number

        @echo.register(str)
        def echo(text):
            print 'Text:', text

        if __name__ == '__main__':
            echo(42)
            echo(3.14)
            echo('Testing')
            echo([1, 2, 3]) 

1, 2, 3, testando...
--------------------

Abaixo a saída da execução:

.. code-block:: bash

    $ python singledispatch.py
    Number: 42
    Number: 3.14
    Text: Testing
    Fallback mode: [1, 2, 3]

Conclusão
---------

Esta é uma funcionalidade muito interessante, mas deve ser utilizada com
parcimônia pois toda vez que a função é executada um dicionário é
consultado, adicionando uma certa latência em cada requisição, além de
crescer um pouco mais a stack do Python.

.. _PEP 443 -- Single-dispatch Generic Functions: http://www.python.org/dev/peps/pep-0443/

