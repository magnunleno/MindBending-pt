Dobrando o Python Com Expressões Regulares
##########################################
:date: 2011-09-05 10:00
:category: Python
:tags: endereço ip, expressão regular, python, regexp
:image: /images/regex.jpg

Dando continuidade no assunto de `Expressões Regulares`_, hoje vou
mostrar em que casos o uso de uma expressão regular supera (e muito) um
trecho (relativamente complexo) de código Python.

.. figure:: {filename}/images/regex.jpg
	:align: center
	:target: {filename}/images/regex.jpg
	:alt: RegEx

        Expressões Regulares

Respirem fundo e vamos lá...

.. more

Contexto
--------

Para este exemplo vou usar um contexto simples: uma aplicação que valida
endereços IPs. Caso alguém esteja se perguntando, sim, este é um exemplo
real. Em uma de minhas aplicações preciso verificar se um dado digitado
pelo usuário é um endereço IP ou não.

Abaixo irei mostrar diversos trechos de código, caso você queira
testá-los, todos devem ser inseridos em um mesmo arquivo. No meu caso
utilizei um arquivo chamado ``valida_ip.py``.

Entendendo O Código
-------------------

Todo o código está bem comentado e documentado, mas mesmo assim vou
explicar alguns trechos para facilitar o entendimento.

Vamos ver o "cabeçalho" do nosso programa:

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    '''
    Programa responsável por realizar testes de performance na detecção e análise
    de endereços IPs utilizando códigos de Python puro e expressões regulares.

    Autor: Magnun Leno
    Licença: GPLv3
    Nome do Arquivo: valida_ip.py
    '''

    # Importando módulo de expressões regulares
    import re
    # Importando módulo "temporizador" de execuções
    import timeit

    # RegEx responsável por analisar o formato de um IP
    ip_re = re.compile(r'^d{1,3}.d{1,3}.d{1,3}.d{1,3}$')

    # Tupla que contém os dados a serem analisados (IPs válidos ou não)
    dados = (
            '10.0.2.1',
            '192.168.1.1',
            'endereço.ip.incorreto',
            '172.16.32.1',
            '10.0.0.396',
            'outro.endereço.ip.errado',
            '172.16.80.1',
            '172.erro.80.2',
            'Com certeza isso não é um IP!!!',
            '172.16.80',
            )

Neste programa vou utilizar apenas os módulos `er`_ e o `timeit`_. O módulo
``er`` já é um conhecido nosso, para aqueles que acompanharam o `último
artigo`_, já o módulo ``timeit``, é "novo" até mesmo pra mim (descobri ele
recentemente). Na função ``cronometro`` veremos como ele funciona.

Após os módulos temos a compilação de uma expressão regular utilizando o
método ``compile`` do módulo ``re``. Como explicar o funcionamento das
expressões regulares não é o escopo deste artigo, vou pedir para que
acreditem que esta expressão regular verifica o "formato" de um endereço
IP, ou seja, quatro grupos de números (de um a 3 dígitos) separados por
pontos. Quem sabe no futuro eu não escrevo uma série de artigos sobre
RegEx no Python :D.

Após a expressão regular, temos a tupla ``dados`` que armazena todos os
dados (endereços IPs válidos e inválidos) a serem processados pelo nosso
programa. Vejam que tentei incluir diversas possibilidades, desde
endereços IPs válidos, IPs fora do escopo, texto puro, texto "no formato
de um endereço IP" e endereços IPs incompletos.

Agora vamos ver duas funções utilizadas para decodificar os endereços
IP:

.. code-block:: python

    def valida_py():
        '''Função responsável por validar os endereços IPs na tupla dados'''
        for endereco in dados:
            # Um endereço IP sempre tem 3 pontos
            if endereco.count('.') != 3:
                continue
            # Corta a string nos pontos, gerando um tupla
            campos = endereco.split('.')
            # Verifica se todos os campos são numéricos
            campos = [not campo.isdigit() for campo in campos]
            # Se algum deles não for numérico, despreza e passa para o próximo
            if any(campos):
                continue
            else:
                # IP Válido
                #print 'IP Válido:',endereco
                pass

    def valida_er():
        '''Função responsável por validar os endereços IPs na tupla dados
        utilizando expressões regulares.
        '''
        for endereco in dados:
            # Verifica se o endereço IP "casa" com a expressão regular
            if ip_re.match(endereco):
                # IP Válido
                #print 'IP Válido:',endereco
                pass

A primeira função, utiliza apenas códigos Python para analisar se uma
das strings contidas em ``dados`` é um IP válido. O trecho mais
complicado dessa função eu considero que seja a *list comprehension* e a
instrução ``any``.

No trecho "``campos = [not campo.isdigit() for campo in campos]``"
criamos uma lista que contém os valores booleanos invertidos (notem a
instrução ``not``) retornados pelo método ``campo.isdigit()``. Este
método informa caso a *string* ``campo`` seja composta somente por
valores numéricos. Já o trecho ``any(campos),`` retorna ``True`` caso
exista algum valor ``True`` dentro da lista ``campos``.

Analisando rapidamente a segunda função, chamada ``valida_er``, podemos
ver como as RegExp são poderosas pois, além da função ter ficado
extremamente curta ela ficou fácil de entender.

Para finalizar esse primeiro ciclo de teste, vamos agora criar uma
função chamada ``cronometro`` que utiliza a classe ``Timer`` para
cronometrar o tempo de 20.000 execuções de uma dada função:

.. code-block:: python

    def cronometro(func):
        t = timeit.Timer(setup='from __main__ import '+ func, stmt=func+'()')
        print func.ljust(16)+':', t.timeit(number=20000)

    if __name__ == '__main__':
        print 'Python timing...'
        cronometro('valida_py')

        print 'nRegEx timing...'
        cronometro('valida_er')

Além da função ``cronometro`` escrevi também uma "função main" do Python
que chama a função ``cronometro`` para as funções ``valida_py`` e
``valida_er``. Salvando tudo e executando, temos o seguinte resultado:

.. code-block:: bash

    $ python valida_ip.py 
    Python timing...
    valida_py       : 0.481071233749

    RegEx timing...
    valida_er       : 0.185606956482

Uau! Isso que é humilhação! A RegEx foi 2.6 vezes mais rápida que o
Python puro! Tudo bem que eu não estou sendo justo, o código em Python
pode ser otimizado. Para provar isso criei a função ``valida_py2``:

.. code-block:: python

    def valida_py2():
        '''Função responsável por validar os endereços IPs na tupla dados
        Essa versão possui um desempenho um pouco superior à valida_py
        '''
        for endereco in dados:
            if endereco.count('.') != 3:
                continue
            campos = endereco.split('.')
            for campo in campos:
                if not campo.isdigit():
                    break
            else:
                # IP Valido
                #print 'IP Valido:',endereco
                pass

Para fazer o teste altere o "main" do programa para ficar da seguinte
forma:

.. code-block:: python

    if __name__ == '__main__':
        print 'Python timing...'
        cronometro('valida_py')
        cronometro('valida_py2')

        print 'nRegEx timing...'
        cronometro('valida_er')

Ao executarmos temos uma alegria inesperada:

.. code-block:: bash

    $ python valida_ip.py 
    Python timing...
    valida_py       : 0.495260000229
    valida_py2      : 0.367525100708

    RegEx timing...
    valida_er       : 0.186715841293

Mesmo melhorando o nosso código a expressão regular ainda é mais
eficiente (praticamente 2 vezes mais rápido) que o código Python puro.

Isso É Tudo?
------------

Mas é claro que não! Nosso "validador de IPs" ainda tem falhas. Ele
somente verifica se a ``string`` passada é composta por quatro grupos de
números separados por pontos e nada mais. Agora precisamos verificar se
eles são válidos, para isso vamos considerar que um IP válido está no
intervalo 0.0.0.0 até 255.255.255.255.

Para atender essa necessidade vamos adicionar 2 códigos no "cabeçalho"
do nosso programa, da seguinte forma:

.. code-block:: python

    # Importando módulo de expressões regulares
    import re
    # Importando módulo "temporizador" de execuções
    import timeit

    # RegEx responsável por analisar o formato de um IP
    ip_re = re.compile(r'^d{1,3}.d{1,3}.d{1,3}.d{1,3}$')
    # RegEx responsável por analisar o conteúdo de um IP
    conteudo_ip_re = re.compile(r'^'+
            r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]).'+
            r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]).'+
            r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]).'+
            r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$'
            )
    # Lambda que informa caso um número esteja dentro ou fora do intervalo
    eh_valido = lambda n : not(255 >= int(n) >= 0)

O primeiro código inserido é uma nova expressão regular chamada
``conteudo_ip_re``, enquanto o segundo código é o *lambda*
``eh_valido``, ambos responsáveis por analisar se o número informado
está dentro ou fora do intervalo válido entre 0 e 255.

Agora criamos mais duas funções:

.. code-block:: python

    def valida_tudo_py():
        '''Função responsável por validar o conteúdo dos endereços IPs
        na tupla dados
        '''
        for endereco in dados:
            if endereco.count('.') != 3:
                continue
            campos = endereco.split('.')
            for campo in campos:
                if not campo.isdigit():
                    break
            else:
                if any(map(eh_valido, campos)):
                    continue
                # IP Valido
                #print 'IP Valido:',endereco
                pass

    def valida_tudo_er():
        '''Função responsável por validar o conteúdo dos endereços IPs na tupla 
        dados utilizando expressões regulares.
        '''
        for endereco in dados:
            # Verifica se o endereço IP "casa" com a expressão regular
            if conteudo_ip_re.match(endereco):
                # IP Válido
                #print 'IP Válido:',endereco
                pass

Estas funções não diferem muito das apresentadas anteriormente, apenas
adicionamos a linha que utiliza a instrução ``map`` em conjunto com o
*lambda*, na função ``valida_tudo_py``, e o uso da nova expressão
regular ``conteudo_ip_re``. Para finalizar essa bateria de testes basta
adicionar uma chamada função ``cronômetro`` para cada nova função. Nossa
"função main" ficará assim:

.. code-block:: python

    if __name__ == '__main__':
        print 'Python timing...'
        cronometro('valida_py')
        cronometro('valida_py2')
        cronometro('valida_tudo_py')

        print 'nRegEx timing...'
        cronometro('valida_er')
        cronometro('valida_tudo_er')

Agora vamos ao teste final:

.. code-block:: bash

    $ python valida_ip.py 
    Python timing...
    valida_py       : 0.496430158615
    valida_py2      : 0.377727985382
    valida_tudo_py  : 1.28690600395

    RegEx timing...
    valida_er       : 0.186795949936
    valida_tudo_er  : 0.310018062592

Agora, conseguimos derrubar de vez o Python! As expressões regulares
conseguiram ser 4,15 vezes mais rápido que o código de Python puro.

Código Fonte
------------

Todo o código fonte utilizado está disponível `aqui`_. Lembre-se este é
um código GPL então podem usar sem medo!

Conclusão
---------

Após essa breve análise do uso de expressões regulares no Python podemos
ver que existem casos que elas não são a melhor escolha, já em outros
podem te dar um ganho de desempenho e reduzir drasticamente seu código.
Mas cuidado, as expressões regulares são extremamente traiçoeiras,
teste-as exaustivamente antes de considerá-las totalmente válidas, ou
você pode acabar tendo um comportamento inesperado na sua aplicação.

Ah, e é claro, as expressões regulares podem se tornar verdadeiros
bichos de 7 cabeças devoradores de fígado de programador! Se sua
expressão regular está fincando muto complexa, considere quebrá-la em
diversos pedaços, isso pode conservar sua sanidade por mais tempo!

Até a próxima...

.. _Expressões Regulares: /pt/brincando-expressoes-regulares-no-python
.. _último artigo: /pt/brincando-expressoes-regulares-no-python
.. _aqui: https://gist.github.com/1190466
.. _er: http://docs.python.org/library/re.html
.. _timeit: http://docs.python.org/library/timeit.html
