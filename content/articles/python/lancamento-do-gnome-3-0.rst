Lançamento do Gnome 3.0
#######################
:date: 2011-04-08 10:19
:category: Python
:tags: download, fedora, gnome, identica, lançamento, opensuse, twitter, ubuntu 11.04, video
:image: /images/gnome.png
:description: Finalmente, depois de diversas iterações, foi lançado o Gnome 3.0 uma das maiores revoluções do desktop open source.

Nesse último dia 7, finalmente o Gnome 3.0 foi lançado. Como o pessoal do Gnome sempre estava divulgando todas as novidades desenvolvidas, não tivemos muitas surpresas além do que já conhecíamos.

.. image:: {filename}/images/iamgnome.png
        :alt: I Am Gnome!
        :align: center
        :target: https://live.gnome.org/ThreePointZero/Promote


Além disso, houveram atualizações na `página do projeto`_ que agora apresenta vídeos demonstrando o uso do novo Gnome. Para mais vídeos visite o `canal no Youtube`_ e não se esqueçam de acompanhar o Gnome no `twitter`_ e no `Identica`_. Para os que usam Ubuntu 11.04 é fácil instalar:

.. more

.. code-block:: bash

    $ sudo add-apt-repository ppa:gnome3-team/gnome3
    $ sudo apt-get update
    $ sudo apt-get dist-upgrade
    $ sudo apt-get install gnome-shell

Caso não goste e queira remover o Gnome 3, basta usar os seguintes comandos:

.. code-block:: bash

    $ sudo apt-get install ppa-purge
    $ sudo ppa-purge ppa:gnome3-team/gnome3

Para os curiosos e inseguros, existem imagens para download baseadas no openSuSe ou Fedore que podem rodar direto em uma pendrive, mais instruções na `página de download do Gnome 3.0`_.

.. _página do projeto: http://www.gnome3.org/
.. _canal no Youtube: http://www.youtube.com/user/GNOMEDesktop
.. _twitter: http://twitter.com/#!/gnome/
.. _Identica: http://identi.ca/gnome
.. _página de download do Gnome 3.0: http://www.gnome3.org/tryit.html

