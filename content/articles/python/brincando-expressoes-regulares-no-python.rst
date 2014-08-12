Brincando com Expressões Regulares no Python
############################################
:date: 2011-08-23 21:45
:category: Python
:tags: er, expressões regurales, python, regex
:image: /images/regex.jpg
:slug: brincando-expressoes-regulares-no-python

Muitas vezes durante o nosso dia-a-dia de programador nos deparamos com a necessidade de analisar, buscar e retornar valores dentro de uma *string*. Existem duas formar de se fazer esse processamento, uma é você escrever manualmente a análise da *string* e a outra é utiliza `expressões regulares`_, ou como também são chamadas: RegEx (abreviação para *Regular Expressions*)

.. figure:: {filename}/images/regex.jpg
        :target: {filename}/images/regex.jpg
        :align: center
        :alt: RegExp

        Expressões Regulares

Expressões regulares são uma cadeia de caracteres com significados próprios utilizados para buscar padrões de texto. Elas possuem diversas aplicações, mas geralmente são utilizadas para extrair informações de um texto ou saber se um grupo predefinido de sequência está presente em um texto. Meu objetivo neste texto não é explicar expressões regulares, mas sim mostrar sua utilidade. Então vamos lá...

.. more

Um Exemplo Simples
------------------

As expressões regulares são ferramentas extremamente poderosas e podem passar de trechos simples de caracteres à um emaranhado ininteligível de caracteres, por isso use com parcimônia. Aqui vou da um exemplo simples sobre como uma expressão regular pode ser utilizada para resumir alguns poucos trechos de código Python.

Neste nosso exemplo temos uma *string* chamada ``dados`` que contém um pequeno trecho HTML. Nossa tarefa é analisar a *string* e retornar apenas os links que existem nela. Primeiro vamos ver como fazer isso em Python puro:

.. code-block:: python

    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-

    # Arquivo: busca_link.py
    # Licença: GPLv3

    dados = '''<HTML>
        <HEAD>
            <TITLE>Mind Bending Blog</TITLE>
        </HEAD>

        <BODY>
            <H1>Bem Vindo!</H1>
            Bem vindo! Acesse o meu blog
            Visite também o portal de notícias
        </BODY>

    </HTML>'''.split('n')

    def busca_links(dados):
        ret = []
        for linha in dados:
            if 'href' not in linha:
                continue
            ret.append(linha.split('"')[1])
        return ret

    if __name__ == '__main__':
        print busca_links(dados)

Ao executarmos o código acima obtemos o seguinte resultado:

.. code-block:: python

    $ python busca_link.py
    ['http://mindbending.org', 'http://news.codecommunity.org']

Como podemo fazer isso com RegEx? Simples:

.. code-block:: python

    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-

    # Arquivo: busca_link_re.py
    # Licença: GPLv3

    import re
    dados = '''<HTML>
        <HEAD>
            <TITLE>Mind Bending Blog</TITLE>
        </HEAD>

        <BODY>
            <H1>Bem Vindo!</H1>
            Bem vindo! Acesse o meu blog
            Visite também o portal de notícias
        </BODY>

    </HTML>'''.split('n')

    link_re = re.compile(r'href="(.*?)"')

    def busca_links_re(dados):
        ret = []
        for linha in dados:
            ret += link_re.findall(linha)
        return ret

    if __name__ == '__main__':
        print busca_links_re(dados)

Ao executarmos o código acima obtemos o seguinte resultado:

.. code-block:: bash

    $ python busca_link_re.py
    ['http://mindbending.org', 'http://news.codecommunity.org']

Tirando a dificuldade de compreender o significado da expressão regular, o código Python ficou bem mais compacto. Agora eu pergunto, será que vale a pena substituir o uso do ``split`` e ``find`` em todos os nossos programas em Python? A resposta é simples: Não.

Por Que Não?
------------

Alguma rotinas (como a demonstrada acima) são tão simples que o uso das expressões regulares é um custo muito alto. Para provar isso vamos executar o um teste para medir o tempo que levamos para executar 1.000.000 vezes as funções ``busca_link`` e ``busca_link_re``:

.. code-block:: python

    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-

    # Arquivo: timer_link.py
    # Licença: GPLv3

    import time
    import busca_link
    import busca_link_re

    dados  = busca_link.dados
    busca_links  = busca_link.busca_links
    busca_links_re = busca_link_re.busca_links_re

    def timing(func, resp, count):
        i = time()
        for n in range(count):
            func(resp)
        print 'Tempo medido com '+func.func_name+':',time()-i

    n = 1000000
    timing(busca_links, dados, n)
    timing(busca_links_re, dados, n)

Ao executar temos a seguinte resposta:

.. code-block:: bash

    $ python timer_link.py
    Tempo medido com busca_links: 3.89300012589
    Tempo medido com busca_links_re: 11.4989998341

Podemos ver claramente que para tratamentos simples como este basta um ``split`` :D. Mas, se utilizarmos um tipo de dado que favorece as expressões regulares, podemos melhorar esse tempo. Para isso modificamos a função ``busca_links_re`` no arquivo *busca\_link\_re* conforme abaixo:

.. code-block:: python

    def busca_links_re(dados):
        ret = []
        for match in link_re.finditer(dados):
            ret.append(match.group(1))
        return ret

e alteramos o arquivo *timer\_link* da seguinte forma:

.. code-block:: python

    dados2 = ''.join(dados)
    timing(busca_links_re, dados2, n)

Ao reexecutarmos os testes, temos os seguintes tempos:

.. code-block:: bash

    $ python timer_link.py
    Tempo medido com busca_links: 4.00200009346
    Tempo medido com busca_links_re: 6.77699995041

Isso sim é uma melhora!

Só Isso?
--------

Por enquanto só! Mas fiquem ligados, em breve vou mostrar que é possível sim ter menos código, mais eficiência e desempenho usando expressões regulares.

Até mais...

.. _expressões regulares: http://pt.wikipedia.org/wiki/Expressão_regular
