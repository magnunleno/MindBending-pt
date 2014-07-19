Destaques da PyCon2011: Everything You Wanted to Know About Pickling
####################################################################
:date: 2011-07-19 14:48
:category: PyCon
:tags: pickle, pycon2011, python
:image: /images/pycon2010.png
:description: A PyCon sempre é cheia de grandes surpresas e ótimas palestras. Mas em certos momentos aparecem palestras que simplesmente te deixa de queixo aberto, este é o cado desta palestra.
:series: Destaques da Pycon 2011

Fiquei pensando em como descrever sucintamente essa palestra de Richard T. Saunders. Encontrei apenas essa frase: Esta é uma daquelas palestras que abre a sua mente.

.. figure:: {filename}/images/pycon2010.png
        :target: {filename}/images/pycon2010.png
        :alt: PyCon2011 Logo
        :align: center

        PyCon2011 Logo

Uma das coisas mais misteriosas no Python é o módulo pickle. Ele é capaz de serializar praticamente qualquer objeto no Python e, simetricamente, desserializa-lo. A sua utilização chega a parecer mágica, de tão simples e intuitivo que é. Nessa palestra, após uma introdução sobre o que o pickle, outras opções e algumas comparações, o Sr, Saunders explica minuciosamente a lógica de funcionamento do pickle.

.. more

Muitos vão dizer que não é necessário saber (ou é uma perda de tempo estudar) como pickle funciona, basta saber usá-lo. Eu acredito que ter esse tipo de conhecimento é um carta na manga! Em um belo dia, quando você estivar lidando com um problema real, seu subconsciente irá lhe cutucar e falar: "Você pode resolver esse problema usando a mesma lógica que o pickle usa!".

Richard T. Saunders utiliza o Python há 10 anos em seu trabalho na corporação `Rincon Research`_ e também é professor da matéria de Engenharia de Software na Universidade do Arizona. Em seu trabalho precisou fazer o trabalho de "engenharia reversa" no módulo pickle e como "consequência" de seu trabalho, criou a `biblioteca PicklingTools`_, uma biblioteca open source para realizar a comunicação entre o Python e C++.

Nessa palestra o Sr. Saunders cobre diversos pontos como:

-  Origem do nome pickle;
-  O que é pickle, pickling and unpickling;
-  O que é a serialização;
-  Exemplos de código de pickling e unpickling para salvar o estado de um jogo;
-  Alternativas ao pickle (marshall, XML, JSON e Google protocol buffers);
-  Por que usar o pickle (vantagens e desvantagens);
-  Comparações entre as alternativas do pickle;
-  Versões do pickle (0, 1, 2 e 3) e uma breve história de cada um;
-  Comparação entre as versões do pickle;
-  Análise do código de máquina (opcodes, pilha de valor e a pilha de marcação) utilizada pelo pickle;

Os slides da palestra estão disponíveis pra download em `PDF aqui`_.

.. raw:: html

   <p><center><iframe src="http://blip.tv/play/g4VigquQRwI.html" width="550" height="442" frameborder="0" allowfullscreen></iframe><embed type="application/x-shockwave-flash" src="http://a.blip.tv/api.swf#g4VigquQRwI" style="display:none"></embed></center></p>

Assumo que ao final dessa palestra fiquei extremamente tentado a escrever um módulo "simplificado" do pickle, simplesmente para saber se sou capaz.

.. _Rincon Research: http://www.rincon.com/
.. _biblioteca PicklingTools: http://www.picklingtools.com/
.. _PDF aqui: http://www.picklingtools.com/PyCon2011PresV2.pdf

