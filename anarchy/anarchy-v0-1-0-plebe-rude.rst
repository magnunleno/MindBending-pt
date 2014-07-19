Anarchy v0.1.0 - Codinome "Plebe Rude"
######################################
:date: 2013-01-24 09:11
:category: Anarchy
:tags: arch, bash, git, instalação, iso, linux, make, makefile, projeto, python, script, shell
:image: /images/Anarchy-Logo-small.png
:slug: anarchy-v010-codinome-plebe-rude

Há alguns meses eu escrevi um artigo sobre a `automação da instalação do Arch Linux`_, e dada a sua repercussão e o número de interessados resolvi criar um projeto para desenvolver um "instalador não oficial" do Arch Linux.


.. image:: {filename}/images/anarchy.png
	:align: center
	:target: {filename}/images/anarchy.png
	:alt: Anarchy

Logo em seguida o Arch Linux implementou o SystemD, o que tornou meu script levemente obsoleto. Como minha vida pessoal andava bem conturbada acabei não tendo tempo de revisitá-lo e ele foi esquecido. Porém a ideia do projeto nunca morreu, graças aos meus colegas Henrique Leal e Valter Sage (que desapareceu após o Ano Novo).

Então, hoje, depois de algumas semanas sentado na frente do velho script e das novas especificações do Arch Linux, eu e Henrique Leal temos o prazer de apresentar a todos o "Anarchy Project" (Projeto Anarquia).

.. more

Anarquia Geral
--------------

O nome do projeto nasceu de uma (óbvia) brincadeira com o nome da distribuição Arch Linux e com a minha ideia de alterar a ISO do Arch Linux. Porém, se somente eu alterasse a ISO esse projeto não teria a característica socialista do movimento anárquico. Desta forma, este projeto visa não somente auxiliar os usuários que têm dificuldade em instalar o Arch Linux, mas irá também auxiliar os usuários que desejarem alterar a ISO do Arch Linux e inserir novas informações, programas, scripts e etc. Ou seja, uma forma de combate à coerção, tudo a ver com o movimento anarquista :).

.. image:: {filename}/images/Anarchy-Logo.png
	:align: center
	:target: {filename}/images/Anarchy-Logo.png
	:alt: Anarchy Logo

Ainda influênciado pela ideia da anarquia resolvi usar nome de bandas de Punk Rock para os codinomes de lançamento. Este primeiro lançamento tem o codinome "Plebe Rude", uma das primeiras bandas Punk que eu ouvi, com o sucesso "Até Quando Esperar".

.. youtube:: 4FqhorPvSEQ
	:align: center
	:width: 560
	:height: 315

O projeto já possui `um repositório`_, o qual possui uma pequena porção de documentação e orientações de uso. Entretanto o projeto ainda é muito limitado e não suporta grandes customizações, vide `artigo anterior`_, o que será sanado em breve com sua versão escrita totalmente em Python.

Todos os interessados em contribuir são bem vindos, seja com código, ideias, sugestões, bug reports e críticas.

Como usar o Anarchy
-------------------

Basicamente o Anarchy é composto por 2 scripts (``anarchy.sh`` e ``anarchy-post.sh``) e um arquivo de configuração (``anarchy.conf``).  Estes 3 arquivos devem ser utilizados em conjunto com a imagem de instalação do Arch Linux, que pode ser obtido `aqui`_.

Para usar o Anarchy em conjunto com a mídia de instalação do Arch Linux, você tem 3 opções:

-  Customizar a mídia de instalação em uma outra máquina;
-  Clonar o repositório do Anarchy após inciar o Live CD do Arch Linux;
-  Baixar a última versão estável do Anarchy após inciar o Live CD do
   Arch Linux;

Customizar o ISO
~~~~~~~~~~~~~~~~

Para customizar a ISO do Arch Linux, primeiro obtenha-a na página de `download do projeto`_, em seguida obtenha a última versão do Anarchy via Git:

.. code-block:: bash

    $ git clone http://github.com/magnunleno/Anarchy.git

Ou via download:

.. code-block:: bash

    $ wget https://github.com/magnunleno/Anarchy/archive/latest.tar.gz

Em seguida (descompacte o arquivo, se necessário) e acesse a pasta do projeto. Emita os seguintes comandos:

.. code-block:: bash

    $ make ISO=/caminho/para/o/iso
    $ make iso

Se tudo correr bem uma nova ISO estará disponível no diretório ``./build/out/``.

Em seguida inicialize o seu computador com o novo ISO. Após o boot customize suas configurações no arquivo ``anarchy.conf`` e execute o comando ``./anarchy.sh``. Este script irá instalar e realizar configurações básicas no seu novo Arch Linux e ao final reiniciará o computador. Para mais informações como ele funciona veja o `artigo anterior`_.

Não usar um ISO customizado
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Claro, você não é obrigado a criar um ISO para usar o Anarchy, basta você inciar com o ISO original do Arch Linux e, após o boot, realizar o download do código do Anarchy via git:

.. code-block:: bash

    $ pacman -Sy && pacman -S git
    $ git clone http://github.com/magnunleno/Anarchy.git

Ou via download:

.. code-block:: bash

    $ wget https://github.com/magnunleno/Anarchy/archive/latest.tar.gz

Em seguida (descompacte o arquivo, se necessário) e acesse a pasta do projeto, customize as configurações em ``anarchy.conf``, vide `artigo anterior`_, e execute o script de instalação:

.. code-block:: bash

    $ ./anarchy.sh

Conclusão
---------

Com esse projeto, tudo o que você precisa é customizar meia dúzia de variáveis, executar um comando e sair pra fazer um sanduíche, ou assistir o script fazer todo o trabalho manual.

Espero que aproveitem.

.. _automação da instalação do Arch Linux: /pt/automatizando-a-instalacao-do-arch-linux/
.. _um repositório: http://github.com/magnunleno/Anarchy.git
.. _artigo anterior: /pt/automatizando-a-instalacao-do-arch-linux/
.. _aqui: https://www.archlinux.org/download/
.. _download do projeto: https://www.archlinux.org/download/
