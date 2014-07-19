Fonte Oxygen Liberada para Testes
#################################
:date: 2012-01-06 17:50
:category: Notícias
:tags: arch, design, fonte, gnome, kde, linux, oxygen
:image: /images/kde.jpg

A equipe de desenvolvimento do KDE, seguindo o mesmo caminho que a
Canonical e o GNOME, resolveu criar sua própria fonte para uso em seus
projetos digitais: a fonte Oxygen. A Oxygen Fonts foi projetada por
`Vernon Adams`_ e pode ser obtida neste `repositório do projeto KDE`_.

.. image:: {filename}/images/kde.jpg
	:align: center
	:target: {filename}/images/kde.jpg
	:alt: KDE Logo

O objetivo do Projeto está na criação de uma fonte para uso integrado ao
ambiente KDE. De acordo com o `README`_ encontrado no repositório, a
fonte Oxygen tem como objetivo ser clara, legível, sem serifa (i. é:
basicamente, uma fonte com a mesma espessura em todo o seu contorno, o
que aumenta e muito sua legibilidade à distância), e que possa ser
renderizada com qualidade em sistemas GNU/Linux utilizando o Freetype
Font Engine.

.. more

.. image:: {filename}/images/oxygen-demo-1.png
	:align: center
	:target: {filename}/images/oxygen-demo-1.png
	:alt: Oxygen Demo 1

.. image:: {filename}/images/oxygen-demo-2.png
	:align: center
	:target: {filename}/images/oxygen-demo-2.png
	:alt: Oxygen Demo 2

.. image:: {filename}/images/oxygen-demo-3.png
	:align: center
	:target: {filename}/images/oxygen-demo-3.png
	:alt: Oxygen Demo 3

O projeto utiliza a licença OFL (*Open Font License*) e encontra-se
ainda em estado *Alfa*. Consequentemente, por estar em fase inicial de
desenvolvimento, essa nova fonte possui apenas os caracteres básicos e
os seguintes tipos de apresentação: regular, monoespaçada e negrito
regular. Porém, espera-se que dentro de pouco tempo, o projeto libere
novas variações de tipos de apresentação, como itálico regular e negrito
itálico.

Esta é uma tendência interessante que antigamente não existia no mundo
FOSS (Free Open Source Software): o desgin de fontes para uso digital.
Inclusive, a ausência desse investimento de design sempre foi apontado
como uma das fraquezas no mundo do software livre e de código aberto. Em
contrapartida, o KDE sempre se destacou por sua beleza e design (muitas
vezes expondo claramente que a Apple é sua fonte de inspiração). Por
isso, me surpreendi por eles não terem sido os "pioneiros" nesta área de
fontes própria

Olhando o blog do `desenvolvedor`_, não pude deixar de notar alguns
comparativos feitos por ele entre a fonte Oxygen e diversas outras
fontes digitais no mercado. Gostaria de destacar a comparação entre a
fonte Oxygen e a fonte do Ubuntu, pois é notável a variação suave de
tamanhos da Oxygen, e como ela continua a ser legível e sem distorções
em tamanhos pequenos.

.. figure:: {filename}/images/ubuntu-oxygen.png
	:align: center
	:target: {filename}/images/ubuntu-oxygen.png
	:alt: Comparativo Ubuntu vs Oxygen

        Comparativo Ubuntu vs Oxygen

Após essas demonstrações, eu espero que essa mais recente variação de
fonte monoespaçada tenha também as opções de negrito e itálico, pois
estou pensando em utilizá-las no VIM.

Instação
--------

Para quem quiser testar a fonte, basta baixá-la do `repositório
oficial`_, ou clonar o repositório usando o seguinte comando:

.. code-block:: bash

    $ git clone git://anongit.kde.org/oxygen-fonts

Já para os usuários do **Arch Linux**, basta instalar com o utilitário
``yaourt``:

.. code-block:: bash

    $ yaourt -S oxygen-fonts-git

E vocês, caros leitores, o que acharam desta fonte?

.. _Vernon Adams: http://code.newtypography.co.uk/
.. _repositório do projeto KDE: https://projects.kde.org/projects/playground/artwork/oxygen-fonts/repository
.. _README: https://projects.kde.org/projects/playground/artwork/oxygen-fonts/repository/revisions/master/entry/README
.. _desenvolvedor: http://code.newtypography.co.uk/
.. _repositório oficial: https://projects.kde.org/projects/playground/artwork/oxygen-fonts/repository
