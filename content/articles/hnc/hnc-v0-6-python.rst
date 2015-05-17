Hack 'n' Cast v0.6 - Python
###########################
:date: 2014-10-15 03:00
:category: Hack 'n' Cast
:tags: hack 'n' cast, podcast, beta, python, linguagem, programação, história, orientação a objetos, System of a down, databasecast, piratas da internet, zen of python
:image: /images/hack-n-cast/v0.x/v0.6-cover-sqr.jpg
:length: 88737172
:duration: 92:07
:podcast: http://archive.org/download/HNC.v0.6-Python/HNC.v0.6-Python.mp3
:podcastembed: http://archive.org/embed/HNC.v0.6-Python/HNC.v0.6-Python.mp3
:podcast_old: True
:description: Python é uma das linguagens que mais cresceram nos últimos anos. Boa parte se deve ao fato de sua simplicidade, sintaxe intuitiva e de fácil aprendizagem, mas não podemos negligenciar a grande força motriz desta linguagem, sua comunidade.

Hoje no `Hack 'n' Cast`_, com a ajuda do `Eric Hideki`_ (`twitter do Eric`_), falaremos de uma das linguagens mais amadas da história, o Python é utilizado para scripts simples, programas comuns, programas para simulação científica, scripting e interligação de módulos de jogos, cálculo numérico, desenvolvimento front-end e back-end e etc.

.. image:: {filename}/images/hack-n-cast/v0.x/v0.6-cover-wide.jpg
        :target: {filename}/images/hack-n-cast/v0.x/v0.6-cover-wide.jpg
        :alt: Hack 'n' Cast v0.6 - Python
        :align: center

Para não perder nenhum episódio siga-nos nas redes sociais (`Twitter`_ e `Facebook`_) ou inscreva-se (`Feed`_, `Podflix`_, `iTunes`_ e `Pocket Casts`_). Você quer colaborar com o Hack 'n' Cast? Sugira um tema, nos ajude a produzir uma pauta ou participe conosco! Basta entrar em contato por `E-mail`_, `Facebook`_ ou `Twitter`_. E agora temos a nossa lista de discussão no `Google Groups`_!

.. more

.. podcast:: HNC.v0.6-Python
        :rss: http://feeds.feedburner.com/hack-n-cast
        :itunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846

O que é?
--------

Python é uma linguagem de programação de propósitos gerais, isto é, ela não foi criada com um propósito específico. Exemplos de linguagens de domínio específico: HTML, VHDL, Shell Script, Matlab, SQL e etc.

A linguagem Python foi criada em 1989 para ser a sucessora da linguagem `ABC`_ com o intuito inicial de ser uma linguagem intermediária entre o Shell Script e a linguagem C. O Python é um software livre desde sua criação e até a presente data é mantida pela comunidade com o apoio da `Python Sofware Foundation`_ (PSF). Apesar de ser um software livre o direcionamento desta linguagem é gerenciado por seu criador, `Guido Van Rossum`_, carinhosamente apelidado de `BDFL`_ (*Benevolent Dictator for Life*).

Influências da linguagem Python:

- ABC (Principal inspiração);
- BASIC;
- ALGOL 68;
- Modula-2 e Modula-3;
- C/C++;
- Haskell;
- Lisp;
- Perl.

Características da linguagem:

- Ela é uma linguagem intuitiva, fácil e agradável de ser utilizada;
- Possui uma sintaxe concisa e clara;
- Criado para ser semelhante a um pseudocódigo;
- Visa reduzir o esforço do programador e favorecer o esforço computacional;
- Prioriza a legibilidade do código (o foco não é a velocidade);
- Excelente `biblioteca padrão`_ (*batteries included*);
- Diversos módulos/frameworks desenvolvidos por terceiros;


Uma lista completa de casos de sucesso está disponível no `site oficial do Python`_.

História
--------

Há alguns anos, quando eu tinha o projeto de escrever um livro sobre Python, eu fiz uma pesquisa extensa sobre a história do Python. O resultado foram quase três páginas com diversos detalhes interessantes sobre a história desta linguagem. Infelizmente nem todos os pontos da história do Python puderam ser abordados neste episódio (por motivos de duração) então, tireia poeira dos arquivos, limpei os excessos e o resultado está disponível para todos lerem `aqui`_.


Características
---------------

O Python possuí algumas características importantes:

É um Software Livre
        Você pode distribuir cópias, ter acesso ao código fonte, alterar,
        modificar, redistribuir e utilizar pedaços dele em outros programas.
        Além disso, isso garante seu constante aperfeiçoamento e que todo
        o trabalho é feito por uma comunidade que quer ver a linguagem crescer.

Portável
        Isto é, roda em diversas arquiteturas. Seu programa pode facilmente rodar
        em: Linux, Windows, FreeBSD, Macintosh, Solaris, OS/2, Amiga, AROS,
        AS/400, BeOS, OS/390, z/OS, Palm OS, QNX, VMS, Psion, Acorn RISC OS,
        VxWorks, PlayStation, Sharp Zaurus, Windows, PocketPC e Symbian OS
        (utilizado por exemplo no Nokia S60).

De altíssimo nível
        Conforme nosso `penúltimo episódio`_, as linguagens podem ser divididas
        em níveis. Esta é uma linguagem de alto nível, mas alguns gostam de
        defini-la como de altíssimo nível (termo não aceito no meio acadêmico).


Interpretada
        Conforme nosso `penúltimo episódio`_, as linguagens de programação
        podem ser classificadas como compiladas ou interpretadas. Como Python
        é interpretada, ela não gera arquivos binários, mas *bytecodes*
        interpretados pela máquina virtual do Python. Consequentemente sua
        performance não é excelente.

Interativa
        Esta característica permite que você tenha "acesso ao programa" durante
        sua execução, além de te prover um shell interativo.

Orientada a objetos (ou não)
        Conforme nosso `penúltimo episódio`_ a Orientação a Objetos é um modelo
        de programação. Apesar do Python ser 100% orientada a objeto (até os
        erros são objetos), você não é obrigado a programar orientado a objeto.
        Esta linguagem lhe permite realizar programação estruturada e possui
        elementos de programação funcional.

Extensível e Integrável
        Possui suporte de integração de diversos tipos, incluindo *Enterprise
        Application Integration* (EAI), invocação de componentes COM
        ou CORBA e a chamar ou ser chamada diretamente por códigos C, C++, ou Java
        (via Jython). Dessa forma é possível "envelopar", de maneira rápida
        e simples, tecnologias existentes em C/C++ e Java para serem usadas
        pelo Python.

Tipagem Dinâmica
        Tipagem dinâmica quer dizer que não há pré-declaração de variáveis,
        pois o tipo é definido dinamicamente durante a execução do programa.
        Consequentemente, uma variável que neste momento é um inteiro,
        posteriormente pode vir a ser uma *string*. Esta funcionalidade remove
        complexidades mas exige do programador uma disciplina peculiar ao
        escrever seus programas.

Tipagem Forte
        Apesar da tipagem ser dinâmica, ela possui tipagem forte, isto implica
        que a linguagem possui um comportamento bem definido ao realizarmos
        "operações" entre tipos descasados.

Indentação e Blocos de Códigos
        Um dos focos do Python é ter um código legível e bem organizado. Todo
        programador sabe que, na pressa para atender um prazo, o código se
        torna desorganizado, e a indentação do código é a primeira
        característica a ser deixada para trás. Por isso a indentação é algo
        obrigatório na linguagem. Diferente de outras linguagens, que utilizam
        delimitadores como ``BEGIN`` e ``END`` ou ``{`` e ``}``, o Python
        utiliza a indentação (tanto com espaços ou com tabulações) como
        controle de bloco de códigos.

Bibliotecas e Módulos
        O Python possui uma vasta biblioteca desde a mais básicas, como
        expressões regulares, chegando até o manuseio de conexões HTTP seguras,
        processamento de XML e HTML, bancos de dados, ftp, e-mail,
        manipulamento de imagens, *engine* de jogos, criptografia, GUIs
        (interfaces gráficas), manipulamento de arquivos WAV e muito mais.
        Todos os modulos externos estão organizados e indexados no `PyPi`_

Zen of Python
-------------

Um mantra criado por `Tim Peters`_ (criador do `Timsort`_) que tinha como objetivo guiar o estilo de programação de todos os programadores Python, ela é quase uma "filosofia". Toda a Zen of Python está disponível juntamente com a linguagem, bastando um `import this`_.

        | Beautiful is better than ugly.
        | Explicit is better than implicit.
        | Simple is better than complex.
        | Complex is better than complicated.
        | Flat is better than nested.
        | Sparse is better than dense.
        | Readability counts.
        | Special cases aren't special enough to break the rules.
        | Although practicality beats purity.
        | Errors should never pass silently.
        | Unless explicitly silenced.
        | In the face of ambiguity, refuse the temptation to guess.
        | There should be one-- and preferably only one --obvious way to do it.
        | Although that way may not be obvious at first unless you're Dutch.
        | Now is better than never.
        | Although never is often better than *right* now.
        | If the implementation is hard to explain, it's a bad idea.
        | If the implementation is easy to explain, it may be a good idea.
        | Namespaces are one honking great idea -- let's do more of those!

        -- The Zen of Python, by Tim Peters

Exemplos de Códigos
-------------------

O típico *Hello World*:

.. code-block:: python

        print "Hello World!"


Um código que imprime o conteúdo de uma lista:

.. code-block:: python

        lista = [1, 2, 3, 4, 5]

        for item in lista:
                print item

Um código que sorteia uma pessoa em uma lista:

.. code-block:: python

        import random
        nomes = [
                "José",
                "João",
                "Maria",
                "Ana"
                ]

        print random.choice(nomes)

Um função que calcula a série de Fibonacci:

.. code-block:: python

        def fibonacci(n):
                a,b = 0,1
                for i in range(n):
                        a,b = b,a+b
                return a

Jogo de adivinhar o número (de 1 a 100):

.. code-block:: python

        from random import randint
        print ('Bem vindo!')
        sorteado = randint(1, 100)
        chute = 0
        while chute != sorteado:
            chute = int(input ('Chute: '))
            if chute == sorteado:
                print ('Você venceu!')
            else:
                if chute > sorteado:
                    print ('Alto')
                else:
                    print ('Baixo')
        print ('Fim do jogo!')


Jogo de adivinhar um nome feminino entre os mais frequentes no Brasil (feito por uma menina de 12 anos)

.. code-block:: python

        import random

        nomes = '''Júlia Sophia Isabella Manuela Giovanna Alice Laura
                Luiza Beatriz Mariana Yasmin Gabriela Rafaela Isabelle Lara
                Letícia Valentina Nicole Sarah Vitória Isadora Lívia Helena
                Lorena Clara Larissa Emanuelly Heloisa Marina Melissa Gabrielly
                Eduarda Rebeca Amanda Alícia Bianca Lavínia Fernanda Ester
                Carolina Emily Cecília Pietra Milena Marcela Laís Natália
                Maria Bruna Camila Luana Catarina Olivia Agatha Mirella
                Sophie Stella Stefany Isabel Kamilly Elisa Luna Eloá Joana
                Mariane Bárbara Juliana Rayssa Alana Caroline Brenda Evelyn
                Débora Raquel Maitê Ana Nina Hadassa Antonella Jennifer
                Betina Mariah Sabrina'''.split()

        nomes.sort()
        print (' '.join(nomes))
        sorteado = random.choice(nomes)
        chute = ''
        while chute != sorteado:
                chute = input('Chute: ')
                if chute == sorteado:
                        print ('Parabéns!')
                elif chute > sorteado:
                        print ('Alto')
                else:
                        print ('Baixo')




Modulos Externos
----------------

Frameworks para Desenvolvimento Web
        - Django
        - Pylons
        - TurboGears
        - Plone
        - CherryPy
        - Web2py
        - Flask
        - Bottle

Processamento de Imagem/dados e geração de gráficos
        - Matplotlib
        - Pylab
        - Numarray
        - Numpy
        - Scipy
        - Python Imaging Library (PIL)
        - Pillow
        - PyOpenGL
        - Visual Python
        - Pandas

GUI Development
        - wxPython
        - tkInter
        - PyGtk
        - PyQt

System Administration
        - Ansible
        - Salt
        - OpenStack

Fontes de Aprendizado
---------------------

- `Site oficial`_;
- `Beginners Guide`_;
- `Documentação Oficial`_;
- `Tutorial Python 2`_;
- `Tutorial Python 3`_;
- `Best Free Python Books`_;
- `Vídeo Aulas Gratuitas`_;
- `PythonHelp`_;

Livros da Novatec
        - `Python para Desenvolvedores`_;
        - `Introdução à Programação com Python – 2ª Edição`_;
        - `Python Cookbook`_;
        - `Python e Django`_;

.. class:: panel-body bg-info

        Na compra de qualquer livro na Novatec utilize o código **MINDBENDING** para conseguir 20% de desconto.

Outros Links Citados
--------------------

- `Python + Haskell`_;
- `Python Brochure`_;
- `BioPython`_;
- `Sentibol`_ (Projeto do Cássio Botaro);
- `Python tocando Sweet Child O'Mine`_;
- `iPython`_;
- `Curto Circuito Podcast`_;
- `PEP8`_;
- `O Que Python Pode Fazer e Você Não Sabia`_;

Links Citados no Bug Report
---------------------------

- `DatabaseCast`_;
- `Nossa Participação no DatabaseCast`_;
- `Neto Cast`_;
- `Piratas da Internet`_;

Trilha Sonora
-------------

A trilha sonora deste episódio foi escolhida pelo Eric Hideki e é uma homenagem ao System of a Down.

System Of A Down (1998)
	- P.L.U.C.K
	- War
	- Suite-Pee
	- Know
	- Spiders
	- Soil

Toxicity (2001)
	- Prison Song
	- Needles
	- Deer Dance
	- Chop Suey!
	- Forest
	- ATWA
	- Toxicity

Steal This Album (2002)
	- I-E-A-I-A-I-O
	- Bubbles
	- Boom!
	- Ego Brain
	- Roulette


.. Links genéricos
.. _Hack 'n' Cast: /pt/category/hack-n-cast
.. _Eric Hideki: https://ericstk.wordpress.com/
.. _twitter do Eric: https://twitter.com/erichideki
.. _ABC: http://en.wikipedia.org/wiki/ABC_%28programming_language%29
.. _Python Sofware Foundation: https://www.python.org/psf/
.. _Guido Van Rossum: http://en.wikipedia.org/wiki/Guido_van_Rossum
.. _BDFL: http://www.artima.com/weblogs/viewpost.jsp?thread=235725
.. _biblioteca padrão: https://docs.python.org/2/library/index.html
.. _site oficial do Python: https://www.python.org/about/success
.. _aqui: /pt/a-historia-do-python
.. _Tim Peters: http://c2.com/cgi/wiki?TimPeters
.. _Timsort: http://en.wikipedia.org/wiki/Timsort
.. _import this: http://legacy.python.org/dev/peps/pep-0020/
.. _penúltimo episódio: /pt/hack-n-cast-v04-introducao-a-programacao
.. _PyPi: https://pypi.python.org/pypi

.. Social
.. _E-mail: mailto: hackncast@gmail.com
.. _Twitter: http://twitter.com/hackncast
.. _Facebook: http://facebook.com/hackncast
.. _Feed: http://feeds.feedburner.com/hack-n-cast
.. _Podflix: http://podflix.com.br/hackncast/
.. _iTunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846?l=en
.. _Pocket Casts: http://pcasts.in/hackncast
.. _Google Groups: https://groups.google.com/forum/?hl=pt-BR#!forum/hackncast

.. Fontes de Aprendizado
.. _Site oficial: https://www.python.org/
.. _Beginners Guide: https://wiki.python.org/moin/BeginnersGuide
.. _Documentação Oficial: https://www.python.org/doc/
.. _Tutorial Python 2: https://docs.python.org/2/tutorial/index.html
.. _Tutorial Python 3: https://docs.python.org/3/tutorial/index.html
.. _Best Free Python Books: http://pythonbooks.revolunet.com/
.. _Vídeo Aulas Gratuitas: http://ericstk.wordpress.com/2013/08/19/video-aulas-gratuitas-de-python/
.. _PythonHelp: http://pythonhelp.wordpress.com/
.. _Python tocando Sweet Child O'Mine: https://www.youtube.com/watch?v=p403HD74eu0
.. _Python para Desenvolvedores: http://www.novatec.com.br/livros/pythondesenvolvedores/
.. _Introdução à Programação com Python – 2ª Edição: http://www.novatec.com.br/livros/introducao-python-2ed/
.. _Python Cookbook: http://www.novatec.com.br/livros/python-cookbook/
.. _Python e Django: http://www.novatec.com.br/livros/pythonedjango/


.. Links
.. _Sentibol: http://www.sentibol.com/
.. _BioPython: http://biopython.org/wiki/Main_Page
.. _Python Brochure: http://brochure.getpython.info/
.. _Python + Haskell: https://github.com/mattgreen/hython
.. _iPython: http://ipython.org/notebook.html
.. _Curto Circuito Podcast: http://www.curtocircuito.cc/aprendizagem-e-programacao/
.. _PEP8: http://legacy.python.org/dev/peps/pep-0008/
.. _O Que Python Pode Fazer e Você Não Sabia: https://speakerdeck.com/erichideki/o-que-python-pode-fazer-e-voce-nao-sabia

.. Bug Report Links
.. _Neto Cast: http://www.josecastanhasneto.blogspot.com.br/
.. _DatabaseCast: http://imasters.com.br/perfil/databasecast/
.. _Nossa Participação no DatabaseCast: http://imasters.com.br/infra/seguranca/databasecast-databasenhacking/
.. _Piratas da Internet: http://piratasdainternet.com.br/
