Gnome 3.10 no Arch Linux
########################
:date: 2013-10-08 15:48
:category: Gnome
:tags: aplicações, arch, atualização, configurações, gnome, linux
:image: /images/gnome.png

No último dia `25 de Setembro foi lançado o Gnome 3.10`_, e no dia 07 de
Outubro (12 dias depois) a nova versão do meu ambiente desktop favorito
chegou aos repositórios oficiais do Arch Linux.

.. image:: {filename}/images/gnome310-new-apps.png
	:align: center
	:target: {filename}/images/gnome310-new-apps.png
	:alt: Gnome 3.10 New Apps

Este novo Gnome traz `diversas melhorias`_ e `novos aplicativos`_ e sua
instalação no Arch Linux está bem simples.

.. more

Acho que posso afirmar que, desde o lançamento do Gnome 3 esta foi a
versão que, nos primeiros dias de instalação, está mais estável,
resolvendo inclusive algumas falhas que eu estava tendo com o cursor no
último Gnome 3.8.

A instalação no Arch Linux foi muito tranquila e não tive nenhum
problema, apenas precisei instalar os novos programas que foram
incluídos no Gnome. Então esses são os comandos que você precisa
executar para ter o Gnome 3.10 totalmente funcional no seu Arch Linux:

.. code-block:: bash

    $ sudo pacman -Suy
    $ sudo pacman -S gnome gnome-extra

Este último comando "reinstala" todo o grupo `gnome`_ e `gnome-extra`_.
Isto é necessário pois uma vez que novos pacotes foram adicionados a
este grupo eles não são instalados automaticamente quando realizamos uma
atualização, uma vez que o comando ``pacman -Suy`` apenas atualiza os
pacotes já instalados.

Como última dica, sugiro que você exclua as configurações/customizações
que você tenha feito no Gnome 3.8, uma vez elas podem interferir no
funcionamento desta nova versão. Como eu não gosto de "excluir" nada, eu
fiz da seguinte forma:

.. code-block:: bash

    $ cd ~
    $ mkdir bkp_dotconfig
    $ mv .local bkp_dotconfig/
    $ mv .config bkp_dotconfig/

Após isso basta reiniciar o seu computador e desfrutar dos novos
recursos.

.. _25 de Setembro foi lançado o Gnome 3.10: http://www.gnome.org/news/2013/09/gnome-3-10-released/
.. _diversas melhorias: https://help.gnome.org/misc/release-notes/3.10/
.. _novos aplicativos: https://help.gnome.org/misc/release-notes/3.10/more-apps.html.en
.. _gnome: https://www.archlinux.org/groups/i686/gnome/
.. _gnome-extra: https://www.archlinux.org/groups/i686/gnome-extra/
