Gimp 2.7.3 Com Janela Única
###########################
:date: 2011-08-24 22:45
:category: Notícias
:tags: arch, gimp, janela única, ubuntu
:image: /images/gimp-logo.png

Finalmente, após um longo período de espera, uma das funcionalidades mais cobiçadas do GIMP (GNU Image Manipulation Tool) foi implementada, o modo "Janela-Única". Mas antes de sair instalando essa versão, aviso que toda a família GIMP 2.7.x é considerada instável e em desenvolvimento.  Todas as novidades consideradas estáveis serão liberadas na versão 2.8 futura (ainda sem data prevista de lançamento.


.. figure:: {filename}/images/gimp-2.7.3.png
        :target: {filename}/images/gimp-2.7.3.png
        :align: center
        :alt: GIMP 2.7.3

        GIMP Versão 2.7.3

Mas como instalar e ativar essa nova funcionalidade? Confira os detalhes abaixo...

.. more

Instalando no Arch Linux
------------------------

A instalação no Arch Linux é extremamente simples e intuitiva, basta utilizar o seguinte comando:

.. code-block:: bash

    $ pacman -S gimp-devel

Instalando no Ubuntu
--------------------

O Processo de instalação no Ubuntu é um pouco mais difícil e trabalhoso.  Abaixo estão os comandos:

.. code-block:: bash

    $ sudo apt-add-repository ppa:matthaeus123/mrw-gimp-svn
    $ sudo apt-get update
    $ sudo apt-get install gimp

Mas Cadê a Janela Única?
------------------------

Um pequeno detalhe é que esta funcionalidade não vem ativa por padrão, para ativá-la basta seguir os seguintes passos:

Clique no menu Janelas->Modo Janela-Única.

Aproveitem...
