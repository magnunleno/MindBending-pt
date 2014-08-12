PyCon Uk 2012: Criando Interfaces para Linha de Comando
#######################################################
:date: 2012-10-22 13:36
:category: PyCon 2012
:tags: 2012, comando, command, command-line, docopt, installation, interface, line, linha, pycon, pyconuk, python, united kingdom, usage
:image: /images/pyconuk-2012-logo.png

Este ano nos tivemos a PyCon US 2012, a PyCon UK 2012, a PyOhio 2012 e
(e claro) a Python Brasil 2012. Estamos quase no fim do ano e **eu
simplesmente não tive tempo de assistir às palestras destes eventos!**
*What the hell*?! Definitivamente esta Pós-Graduação (e alguns problemas
pessoais) estão tirando o meu ritmo... Mas graças a alguns bons amigos,
uma ou outra palestra excelente tem chegado ao meu conhecimento. E um
desses foi a excelente palestra `"Creating Beautiful Command-Line
Interfaces With Python"`_, feita pelo `Vladimir Keleshev`_.

.. image:: {filename}/images/pyconuk-2012.png
	:align: center
	:target: {filename}/images/pyconuk-2012.png
	:alt: PyConUK 2012

Basicamente nesta palestra Keleshev faz um *rant* a respeito da
bibliotecas para criação de interfaces linha de comando existentes para
a linguagem Python. Em seguida ele apresenta um módulo feito por ele
mesmo, chamado `Docopt`_, que se mostra extremamente simples, flexível e
eficaz. Um modulo que segue o `Zen of Python`_.

.. more

A Palestra
----------

.. youtube:: pXhcPJK5cMc
	:align: center
	:width: 560
	:height: 315

O Módulo Docopt
---------------

Para instalar o Docopt utilize o seguinte comando:

.. code-block:: bash

    $ pip install docopt

O módulo Docopt é tão simplista e tão eficiente que toda a API desse
modulo é composta por apenas um método. Descrito abaixo:

.. code-block:: python

    docopt(doc[, argv][, help][, version])

Como podemos ver os argumentos ``argv``, ``help`` e ``version`` são
opcionais e possuem os seguintes valores padrões:

.. code-block:: python

    docopt(doc, argv=sys.argv[1:], help=True, version=None)

Um exemplo prático de uso deste módulo é o seguinte:

.. code-block:: python

    """Naval Fate.

    Usage:
      naval_fate.py ship new <name>...
      naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
      naval_fate.py ship shoot <x> <y>
      naval_fate.py mine (set|remove) <x> <y> [--moored|--drifting]
      naval_fate.py -h | --help
      naval_fate.py --version

    Options:
      -h --help     Show this screen.
      --version     Show version.
      --speed=<kn>  Speed in knots [default: 10].
      --moored      Moored (anchored) mine.
      --drifting    Drifting mine.

    """
    from docopt import docopt


    if __name__ == '__main__':
        arguments = docopt(__doc__, version='Naval Fate 2.0')
        print(arguments)

A utilização deste módulo é tão "mágico" que é difícil de entender o que
ele faz. Basicamente ele se utiliza da docstring (``__doc__``) para
criar toda a interface, uma vez que a docstring está escrita seguindo as
normas do padrão IEEE 1003.1 (também conhecido como POSIX).

Atualmente o Docopt está disponível para as linguagens Python, Ruby,
CoffeeScript, JavaScript, PHP e Bash. Estão sendo construídos também
traduções para Lua e C.

Ficou curioso mas não quer ter que instalar no seu computador? Teste via
Web no `Try Docopt`_!

Até a próxima!

.. _"Creating Beautiful Command-Line Interfaces With Python": http://www.youtube.com/watch?v=pXhcPJK5cMc
.. _Vladimir Keleshev: http://www.keleshev.com/
.. _Docopt: http://docopt.org/
.. _Zen of Python: http://www.python.org/dev/peps/pep-0020
.. _Try Docopt: http://try.docopt.org/

