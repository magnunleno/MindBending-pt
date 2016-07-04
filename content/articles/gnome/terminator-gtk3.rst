Instalando o Terminator GTK3
############################
:date: 2016-07-04 16:26
:category: Gnome
:tags: gnome, terminator, gtk3, terminal
:image: /images/logos/terminator.png

Todo mundo que me conhece sabe que eu adoro o ambiente de linha de comando. E não é de hoje que muita gente tenta me convencer a usar o `Tmux`_. O Tmux combina muito com o meu Workflow na linha de comando, entretando, todas as vezes que eu o testei, não me adaptei com seus atalhos e ele não me instigou o suficiente para estudar seus arquivos de configuração a ponto de customizá-lo. Não, não... O problema não é com o Tmux, na verdade é que eu já uso um terminal que tem boa parte das funcionalidades do Tmux, o `Terminator`_.

.. figure:: {filename}/images/apps/terminator-not.jpg
    :target: {filename}/images/apps/terminator-not.jpg
    :align: center
    :alt: Terminator...

.. more

Não esse Terminator... o outro terminator...

.. figure:: {filename}/images/apps/terminator.png
    :target: {filename}/images/apps/terminator.png
    :align: center
    :alt: Terminator!

Para instalá-lo é muito simples:

.. code-block:: bash

    $ # Arch Linux
    $ sudo pacman -S terminator
    $ # Debian/Ubuntu/Linux Mint
    $ sudo aptitude install terminator
    $ # RedHat/CentOS
    $ sudo yum install terminator
    $ # Fedora
    $ sudo dnf install terminator

Entretanto, ele ainda é em GTK2, e destoa um pouco do restante do meu ambiente no GNOME. Mas para minha alegria, recentemente descobri que existe um branch do Terminator para GTK3! Downside: Não está empacotado para nenhum distribuição.

Felizmente, o Terminator é feito em Python (yay!), o que torna seu processo de instalação extremamente fácil. Primeiramente temos que instalar o ``bzr`` (git da Canonical) e algumas outras dependências:

.. code-block:: bash

    $ # Arch Linux
    $ sudo pacman -S bzr intltool python2-psutil
    $ # Debian/Ubuntu/Linux Mint
    $ sudo aptitude install bzr intltool python2-psutil
    $ # RedHat/CentOS
    $ sudo yum install bzr intltool python2-psutil
    $ # Fedora
    $ sudo dnf install bzr intltool python2-psutil

Agora nos resta apenas obter o código fonte e instalar o Terminator:

.. code-block:: bash

    $ cd /tmp
    $ bzr branch lp:terminator/gtk3 terminator-gtk3
    $ cd terminator-gtk3
    $ sudo ./setup.py install

Depois de algumas poucas customizações, o meu Terminator tem a seguinte aparência (não, ele não está maximizado, eu oculto a decoração da janela pra ganhar mais linhas):

.. figure:: {filename}/images/apps/meu-terminator.png
    :target: {filename}/images/apps/meu-terminator.png
    :align: center
    :alt: Meu Terminator...


.. _Tmux: https://tmux.github.io/
.. _Terminator: http://gnometerminator.blogspot.com.br
