Google Chrome Não Gosta De Fusões
#################################
:date: 2012-06-04 15:46
:category: Arch Linux
:tags: atualização, chrome, chromium, erro, fusão, libudev, pacman, problema, solução, systemd, udev
:image: /images/chrome-logo.jpg

E não é que a fusão entre o `Systemd`_ e o `Udev`_ (parte do projeto do
Kernel Linux) não foi tão tranquila quanto eu esperava. Esta fusão já
havia sido anunciada em Abril (veja a notícia `aqui`_) mas só realmente
ocorreu (para nós usuários) no dia 02 de Junho. Eu temi muitos conflitos
ao ordenar que o pacman substituísse o udev, mas para minha felicidade
não notei nenhuma consequência da fusão. Não de imediato.

.. image:: {filename}/images/fusao.jpg
	:align: center
	:target: {filename}/images/fusao.jpg
	:alt: Fusão

Após a atualização (noticiada tanto no site oficial do `ArchLinux
Brasil`_ quanto no `Planeta ArchLinux Brasil`_) todos os meus drivers,
discos e módulos do kernel estavam funcionando perfeitamente, mas o
Google Chrome não iniciava! A mensagem de erro era a seguinte:

.. more

::

    /usr/bin/google-chrome: error while loading shared libraries: libudev.so.0: cannot open shared object file: No such file or directory

Após uma breve pesquisa descobri que, durante a transição, a biblioteca
``/usr/lib/libudev.so.0`` foi renomeada para
``/usr/lib/libudev.so.1.0.1``. Uma opção que temos para corrigir o erro
é criar um link simbólico da seguinte forma:

.. code-block:: bash

    $ sudo ln -sf /usr/lib/libudev.so.1.0.1 /usr/lib/libudev.so.0

Outra solução, caso você não queira remendar bibliotecas dessa forma, é
remover o Google Chrome e instalá-lo novamente:

.. code-block:: bash

    $ sudo paman -R google-chrome
    $ sudo yaourt -S google-chrome

.. raw:: html

   <div class="alert alert-info">

**Update** De acordo com nosso amigo `Vinipsmaker`_, isso não ocorre com o Chromium.

.. raw:: html

   </div>

.. role:: strike

:strike:`Como eu não tinha o Chromium (versão "Open Source" do Chrome)
instalado no momento da atualização eu posso afirmar com certeza se ele
também foi afetado. Mas a solução citada acima também funciona pro
Chromium.`

Mas tem uma coisa que me tira o sono, **porque o chrome precisa da
biblioteca do udev**?

.. _Systemd: http://www.freedesktop.org/wiki/Software/systemd
.. _Udev: https://wiki.archlinux.org/index.php/Udev
.. _aqui: http://www.h-online.com/open/news/item/Udev-will-become-part-of-systemd-1500832.html
.. _ArchLinux Brasil: http://archlinux-br.org
.. _Planeta ArchLinux Brasil: http://planeta.archlinux-br.org/
.. _Vinipsmaker: http://vinipsmaker.wordpress.com/
