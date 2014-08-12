Instalando o Gnome Pie - Ubuntu e Arch Linux
############################################
:date: 2011-09-28 10:00
:category: Gnome
:tags: arch, gnom-pie, gnome, guia, instalação, tutorial, ubuntu
:image: /images/gnome-pie.png

Recentemente foi lançada uma aplicação muito legal chamada `Gnome-Pie`_,
escrita por Simon Schneegans. De acordo com o autor ela foi inspirada no
*add-on* escrito para o jogo Word of Warcraft chamado `O-Pie`_. Tenho
que admitir que sua parte gráfica me lembra muito uma outra aplicação
chamada `PieDock`_, já o seu funcionamento e comportamento tem uma
abordagem completamente diferente, possibilitando ao usuário invocar
diversos "menus" diferentes baseado em teclas de atalho, ele possibilita
até mesmo o controle de aplicações multimídia!

.. figure:: {filename}/images/gnome-pie.png
	:align: center
	:target: {filename}/images/gnome-pie.png
	:alt: Gnome Pie Logo

	Logo do Gnome Pie

Apesar de ter sido lançado recentemente o Gnome-Pie já possui diversas
funcionalidades interessantes e muitos temas agradáveis. Vamos ver um
vídeo de exemplo para entendermos melhor como ele funciona, após isso
irei mostrar o processo de instalação no Ubuntu e no Arch Linux.

.. more

.. youtube:: TFQDyZyMxO4
	:align: center
	:width: 560
	:height: 315

Instalando no Ubuntu
--------------------

Se você utiliza o Ubuntu, a instalação é bem simples, basta lanças as
seguintes linhas em um terminal:

.. code-block:: bash

    $ sudo add-apt-repository ppa:simonschneegans/testing
    $ sudo apt-get update
    $ sudo apt-get install gnome-pie

Instalando no Arch Linux
------------------------

Exite um pacote de instalação do Gnome-Pie no AUR, mas está incorreto.
Por isso vamos instalá-lo manualmente. Primeiro vamos obter o código
fonte do Gnome-Pie através do GitHub e compilá-lo em seguinda:

.. code-block:: bash

    $ cd /tmp
    $ git clone https://github.com/Simmesimme/Gnome-Pie.git
    $ cd Gnome-Pie
    $ ./make.sh

Pronto, tudo deve ter sido concluído com sucesso! Agora tente iniciar o
programa com ``./gnome-pie``. Perfeito certo? Então vamos instalá-lo:

.. code-block:: bash

    $ cd build
    $ sudo make install

Pronto, agora temos o programa propriamente instalado!

Usando o Gnome-Pie
------------------

Utilizar o Gnome-Pie é bem simples, por padrão ele é instalado com seis
*"pies"* (tortas) padrões "pies", cada uma possui seu atalho de teclado
próprio:

-  Sessão: ``<ctrl><alt>Q``
-  Multimídia: ``ctrl><alt>M``
-  Aplicações: ``ctrl><alt>A``
-  Favoritos: ``ctrl><alt>B``
-  Janela: ``ctrl><alt>W``
-  Menu Principal: ``ctrl><alt>Espaço``

Pra customizar as "tortas" (adicionando novas "fatias") ou até mesmo
adicionando novas "tortas", basta clicar com o botão direto sobre o
ícone quebrado do Gnome-Pie na área de notificação e selecionar a opção
de menu chamada "Preferências".

.. figure:: {filename}/images/gnome-pie-settings.png
	:align: center
	:target: {filename}/images/gnome-pie-settings.png
	:alt: Gnome-Pie Settings

        Gnome-Pie Settings

**Agora** sim está tudo pronto! Como diriam os americanos "as easy as
pie" (tão fácil como uma torta).

.. _Gnome-Pie: https://github.com/Simmesimme/Gnome-Pie
.. _O-Pie: http://go-hero.net/opie/
.. _PieDock: http://markusfisch.de/
