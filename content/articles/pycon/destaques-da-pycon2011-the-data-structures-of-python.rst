Destaques da PyCon2011: The Data Structures of Python
#####################################################
:date: 2011-08-10 08:00
:category: PyCon
:tags: benchmark, collections, dicionarios, estruturas de dados, forzensets, listas, palestra, python, sets, tuplas
:image: /images/pycon2010.png
:series: Destaques da Pycon 2011

Vou iniciar esse artigo da mesma forma que `Alex Gaynor <http://alexgaynor.net/>`_ (o palestrante) começou. "Quem aqui se lembra das aulas de estruturas de dados?". Em seguida, ele complementa: "E quem se importa?".

.. figure:: {filename}/images/pycon2010.png
    :alt: PyCon 2010
    :align: center

Para os que aprenderam a programar em linguagens de alto nível, estruturas de dado não é nada demais. Mas para as pessoas mais velhas como eu, que começaram a programar em C, estruturas de dados é algo extremamente difícil, porém valioso. O que ocorre é que as linguagens de alto nível já possuem diversas estruturas de dados implementadas, tornando sua utilização algo simples e indolor.

.. more

O Python não é exceção dessa regra, mas eu não concordo plenamente com a ideia de que esse conhecimento é descartável. O palestrante cita uma frase de Tim Peters, um dos grandes gurus do Python: "We read Knuth so you don't have to." (Nós lêmos Knuth para que você não precise ler).  Knuth, é um renomado professor da Universidade de Stanford e autor do livro *The Art of Computer Programming*, uma das principais referência na área de ciência da computação.

O Python implementa por padrão diversos tipos de estruturas de dados ``listas``, ``tuplas``, ``dicionários``, ``sets``, ``frozensets``, ``arrays``, ``bytearrays`` e outros menos utilizados ou mais recentes (como o ``OrderedDict``). Esta palestra tenta mostrar como e onde utilizar alguns desses tipos (``listas``, ``tuplas``, ``sets`` e ``frozensets``):


.. raw:: html

        <p><center><iframe src="http://blip.tv/play/g4Vigqr7VAI.html" width="550" height="442" frameborder="0" allowfullscreen></iframe><embed type="application/x-shockwave-flash" src="http://a.blip.tv/api.swf#g4Vigqr7VAI" style="display:none"></embed></center></p>

Números, números, números...
----------------------------

Em minha humilde opinião, acho que faltaram números e estatísticas na
palestra. Por exemplo, durante a comparação entre listas e sets ele cita
a seguinte função:

.. code-block:: python
    :linenos: table

    def remove_dups(seq):
        seen = set()
        items = []
        for item in seq:
            if item not in seen:
                seen.add(item)
                items.append(item)
        return items

Ele cita também, que se você trocar o set ``seen`` por uma lista, o
funcionamento seria o mesmo porem, o desempenho seria inferior. Como
provar isso? Simples, basta criar a segunda função sugerida por ele:

.. code-block:: python
    :linenos: table

    def bad_remove_dups(seq):
        seen = []
        items = []
        for item in seq:
            if item not in seen:
                seen.append(item)
                items.append(item)
        return items

Além disso, precisamos de dois módulos (``random`` e ``time``), de uma
função de bechmark e de uma massa de dados, conforme abaixo:

.. code-block:: python
    :linenos: table

    from random import random
    from time import time

    def bench(func):
        results = []
        for i in range(10):
            ini = time()
            func(data)
            results.append(time() - ini)
        print "Mean time:", sum(results)/10

    data = [int(random()*50)for i in range(900000)]

Após isso, basta chamar a função de benchmark e passar as funções a
serem testadas, conforme abaixo:

.. code-block:: python

    bench(remove_dups)
    bench(bad_remove_dups)

Apesar de estarmos calculando a média de dez execuções, ainda ocorre uma
leve variação nos tempos, mas todos sempre estão muito próximos. Abaixo
segue a saída de uma execução que realizei:

::

    Mean time: 0.0723000049591
    Mean time: 0.580800008774

Podemos ver que o a função ``remove_dups`` é pouco além de 8 vezes mais
rápida que a função ``bad_remove_dups``.

Faça Você Mesmo
---------------

Uma dos pontos mais importantes para mim nessa palestra foi a utilização
das classes abstratas do módulo ``collections``. Eu já cometi várias
vezes o erro de estender os tipos padrões do Python. Nunca façam isso...
Nunca!
