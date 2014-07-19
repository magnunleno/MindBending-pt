Aí Vem O Gnome-Pie 0.5
######################
:date: 2012-02-29 20:28
:category: Gnome
:tags: aplicativo, arch, cmake, git, gnome, gnome-pie, instalação, linux, make, pacman, ubuntu, yaourt
:image: /images/gnome-pie.png

Olá pessoal, como faço parte de grupo de traduções do `Gnome-Pie`_ trago essa notícia de primeira mão: O Gnome-Pie versão 0.5 está para ser lançado! Isso mesmo, `Simon Schneegans`_ -- o autor -- acabou de solicitar que eu atualizasse a tradução do projeto para o Português do Brasil.

.. image:: {filename}/images/gnome-pie-0-5.png
	:align: center
	:target: {filename}/images/gnome-pie-0-5.png
	:alt: Gnome-Pie 0.5

O Gnome-Pie é um aplicativo que além de ser muito útil é extremamente robusto e bonito, por esses e outros fatores ele já apareceu aqui no Mind Bending Blog outras duas vezes (`sobre sua instalação`_ e `sobre sua versão 0.3`_). Caso você não saiba do que se trata, recomendo que assista aos vídeos abaixo:

.. more

.. vimeo:: 30618179
	:align: center
	:width: 500
	:height: 375

.. vimeo:: 35385121
	:align: center
	:width: 500
	:height: 375

Instalando no Arch Linux
------------------------

Já que esta versão ainda não está oficialmente liberada é necessário compilá-la manualmente. Para isso vamos precisar do GIT e do Yaourt para instalar algumas dependências. Para instalar o Yaourt, verifique a sessão **Yaourt e o AUR** neste meu `artigo`_.

Agora vamos para o GIT, certifique-se que ele está apropriadamente instalado utilizando o comando ``$ pacman -Qi git``. Caso ele retorne alguma mensagem de erro do tipo ``erro: pacote "git" não foi encontrado``, instale o git com o seguinte comando: ``sudo pacman -S git``

Em seguida vamos confirmar se todas as dependências estão instaladas.  Vamos começar com as dependências que estão no repositório oficial do Arch Linux, para isso utilize o seguinte comando, ``sudo pacman -S libgee libxtst libunique libwnck gnome-menus hicolor-icon-theme``.  Agora, vamos instalar a biblioteca *bamf*, disponível apenas pelo Yaourt. Para instalá-la utilize o seguinte comando: ``yaourt -S bamf``.

Agora que todo o nosso ambiente está preparado, vamos baixar o código fonte do Gnome-Pie 0.5 com a tradução para o Português do Brasil:

.. code-block:: bash

    $ cd /tmp
    $ git clone git://github.com/magnunleno/Gnome-Pie-pt_br.git Gnome-Pie
    $ cd Gnome-Pie

Agora que temos todo o código fonte, vamos inicia o processo de compilação e instalação:

.. code-block:: bash

    $ mkdir build
    $ cd build
    $ cmake -DCMAKE_INSTALL_PREFIX=/usr ..
    $ make
    $ sudo make install

Instalando no Ubuntu
--------------------

Já que esta versão ainda não está oficialmente liberada é necessário compilá-la manualmente. Para isso vamos precisar do GIT e de algumas dependências. Use o seguinte comando para instalar o GIT e todas as dependências do Gnome-Pie: 

.. code-block:: bash 

        $ sudo apt-get install libgtk-3-dev libcairo2-dev libappindicator3-dev
        libgee-dev libxml2-dev libxtst-dev libgnome-menu-3-dev valac cmake
        libunique-3.0-dev libbamf3-dev libwnck-3-dev

Agora que todo o nosso ambiente está preparado, vamos baixar o código fonte do Gnome-Pie 0.5 com a tradução para o Português do Brasil:

.. code-block:: bash

    $ cd /tmp
    $ git clone git://github.com/magnunleno/Gnome-Pie-pt_br.git Gnome-Pie
    $ cd Gnome-Pie

Agora que temos todo o código fonte, vamos inicia o processo de compilação e instalação:

.. code-block:: bash

    $ ./make.sh
    $ cd build
    $ sudo make install

Após a Instalação
-----------------

Pronto, a esta altura tudo deve ter corrido bem! Em seguida basta chamar a aplicação e configurar os menus e seus itens. Veja abaixo alguns *screenshots* da aplicação (clique para ampliar):


.. raw:: html

        <div class="row"><div class="col-md-3 col-xs-6">

.. figure:: {filename}/images/Selecao_005.png
	:align: center
	:target: {filename}/images/Selecao_005.png
	:alt: Configurações Gnome-Pie

.. raw:: html

        </div><div class="col-md-3 col-xs-6">

.. figure:: {filename}/images/Selecao_006.png
	:align: center
	:target: {filename}/images/Selecao_006.png
	:alt: Configurações Gerais - Gnome-Pie

.. raw:: html

        </div><div class="col-md-3 col-xs-6">

.. figure:: {filename}/images/Selecao_008.png
	:align: center
	:target: {filename}/images/Selecao_008.png
	:alt: Adicionando nova Fatia - Gnome-Pie

.. raw:: html

        </div><div class="col-md-3 col-xs-6">

.. figure:: {filename}/images/Selecao_009.png
	:align: center
	:target: {filename}/images/Selecao_009.png
	:alt: Novo Menu - Gnome-Pie

.. raw:: html

        </div><div class="col-md-3 col-xs-6">

.. figure:: {filename}/images/Selecao_011.png
	:align: center
	:target: {filename}/images/Selecao_011.png
	:alt: Aplicativos - Gnome-Pie

.. raw:: html

        </div><div class="col-md-3 col-xs-6">

.. figure:: {filename}/images/Selecao_012.png
	:align: center
	:target: {filename}/images/Selecao_012.png
	:alt: Créditos - Gnome-Pie

.. raw:: html

        </div>
        </div>


Feedback
--------

Caso alguém tenha alguma feedback sobre a tradução basta entrar em contato comigo, ficarei feliz em corrigir qualquer erro ou considerar qualquer correção. Só peço que levem em consideração que realizei a tradução de 107 *strings* em menos de 20 min :D.

.. _Gnome-Pie: http://www.simonschneegans.de/?page_id=12
.. _Simon Schneegans: http://www.simonschneegans.de
.. _sobre sua instalação: /pt/instalando-o-gnome-pie-ubuntu-e-arch-linux/
.. _sobre sua versão 0.3: /pt/lancado-o-gnome-pie-0-3/
.. _artigo: /pt/programas-essenciais-apos-a-instalacao-do-arch/
