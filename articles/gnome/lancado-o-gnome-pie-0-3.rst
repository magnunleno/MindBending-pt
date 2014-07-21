Lançado o Gnome-Pie 0.3!
########################
:date: 2011-11-16 14:30
:category: Gnome
:tags: arch, build, cmake, gnome-pie, instalação, lançamento, linux, mouse, o-pie, ppa, teclado, tradução, ubuntu, word of warcraft, wow
:image: /images/gnome-pie.png
:description: O Gnome-Pie, um lançador de aplicações baseado em menus, atinge a sua versão 0.3 trazendo diversas novas funcionalidades e traduções para outros 3 idiomas.
:slug: lancado-o-gnome-pie-0-3

.. default-role:: code

Neste último dia 12 de Novembro |foi lançada a versão 0.3 do maravilhoso Gnome-Pie|_, desenvolvido por Simon Schneegans. De acordo com o autor ele foi inspirada no add-on do jogo Word of Warcraft chamado O-Pie. O Gnome-Pie traz ao usuário o poder de invocar diversos "menus" diferentes baseado em teclas de atalho, possibilitando até mesmo o controle de aplicações multimídia e navegação entre as janelas abertas!  Mais informações sobre o projeto estão disponíveis `aqui`_.

.. image:: {filename}/images/gnomepie.png
        :align: center
        :alt: Gnome Pie

Esta nova versão traz diversas novas funcionalidades, além de estar totalmente traduzida para o Português do Brasil e ser mais simples de instalar. Abaixo, temos um pequeno *tour*...

.. more

Traduções
---------

Esta não é uma das grandes novidades desta versão, mas a aplicações foi completamente traduzida para o o Português do Brasil por ninguém mais ninguém menos do que **eu**! Fazia tempo que eu não contribuía com projetos de tradução e, como esta aplicação me interessou muito desde o início do seu desenvolvimento, resolvi arregaçar as mangas e me envolver desde o início.

.. image:: {filename}/images/gnome-pie-credits.png
        :align: center
        :alt: Gnome Pie Credits

Foram `238 linhas`_ traduzidas em incríveis **25 minutos** usando apenas o **VIM**! Então, se vocês notarem algum erro ou quiserem sugerir alguma tradução melhor, basta entrar em contato!

Novas Funcionalidades
---------------------

Diversas novas funcionalidades foram adicionadas ao Gnome-Pie! Algumas foram escritas nestas últimas 3 semanas e podem estar instáveis, caso alguém encontre um erro reporte `no GitHub`_. Agora alguns destaques:

-  **Atalhos de Mouse:** De acordo com Simmon esta foi uma das
   funcionalidades mais requisitadas, agora você pode invocar os menus
   através de clique do mouse!
-  **Atalhos Turbo:** Com esta opção ativa, não é necessário clicar
   sobre uma opção de menu, basta levar o mouse até e soltar as teclas
   de atalho!
-  **Atalhos com Atraso:** Com esta opção, o menu será invocado somente
   se o conjunto de teclas for pressionado e mantido por alguns
   segundos.
-  **Gerenciamento de Janela:** Este é um novo menu que funciona como um
   alternador de janelas!
-  **Novo Tema:** Foi criado um novo tema inspirado no Elementary OS!
-  **Gerenciamento de Memória:** Gnome-Pie agora utiliza menos memória!
   O consumo de memória gira em torno de 15 MB.

Instalação No Ubuntu
--------------------

Desde o início do desenvolvimento do Gnome-Pie a instalação no Ubuntu sempre foi simples, basta adicionar um PPA e em seguida instalar o pacote `gnome-pie`. Atualmente o Gnome-Pie está disponível para Ubuntu **10.10** (Maverick Meerkat), **11.04** (Natty Narwhal), **11.10** (Oneiric Ocelot) e **12.04** (Precise Pangolin):

.. code-block:: bash

    $ sudo add-apt-repository ppa:simonschneegans/testing
    $ sudo apt-get update
    $ sudo apt-get install gnome-pie

Instalação No Arch Linux
------------------------

Há alguns meses eu escrevi sobre `como instalar-lo no Ubuntu e no Arch`_, fico feliz de dizer que atualmente o processo de instalação está muito mais simplificado, e que eu ajudei a tornar este processo mais "redondo".

Antes de tudo é bom verificar se você possui todas as dependências para instalá-lo: bamf-bin, cairo, gdk-pixbuf2, gnome-menus, gtk2, hicolor-icon-theme, libgee, libunique, libxml2 e libxtst.

Você pode compilá-lo e instalá-lo da seguinte forma:

.. code-block:: bash

    $ cd /tmp
    $ git clone https://github.com/Simmesimme/Gnome-Pie.git
    $ cd Gnome-Pie
    $ ./make.sh
    $ cd build
    $ sudo make install

ou instalá-lo através do pacote `gnome-pie` disponível no **AUR**. A maneira mais simples é utilizar o seguinte comando:

.. code-block:: bash

    $ yaourt -S gnome-pie

Aproveitem este ótimo aplicativos! Até mais...

.. |foi lançada a versão 0.3 do maravilhoso Gnome-Pie| replace:: foi lançada a versão 0.3 do maravilhoso **Gnome-Pie**
.. _foi lançada a versão 0.3 do maravilhoso Gnome-Pie: http://www.simonschneegans.de/?p=426
.. _aqui: http://www.simonschneegans.de/?page_id=12
.. _|image2|: {filename}/images/gnomepie.png
.. _|image3|: {filename}/images/gnome-pie-credits.png
.. _238 linhas: https://github.com/Simmesimme/Gnome-Pie/commit/1ee90aaefb109eb420141e7570a7784f8f004f03
.. _no GitHub: https://github.com/Simmesimme/Gnome-Pie/issues?sort=created&direction=desc&state=open
.. _como instalar-lo no Ubuntu e no Arch: /pt/instalando-o-gnome-pie-ubuntu-e-arch-linux/

