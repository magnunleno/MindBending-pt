Dica Rápida Sobre o Pacman
##########################
:date: 2011-07-08 16:18
:category: Arch Linux
:tags: arch, erro, pacman
:image: /images/archlogo.png
:description: Recentemente meu pacman tem mostrado uma mensagem de erro muito estranha. Será que é só comigo??

.. image:: {filename}/images/archlogo.png
        :target: {filename}/images/archlogo.png
        :align: center
        :alt: Arch Linux Logo

Olá pessoal! Essa é uma dica rápida de como resolver um problema que estava acontecendo comigo. Não sei direito ao certo quando, como ou porque começou a acontecer, mas o pacman começou a emitir a seguinte mensagem de erro:

::

    erro: não foi possível abrir o arquivo /var/lib/pacman/local/libreoffice-3.4.1-1/desc: Arquivo ou diretório não encontrado

Se fosse um simples *warning* isso não me incomodaria, mas o número de vezes que esse erro apareceu começou a se multiplicar e começou a interferir no funcionamento do*Yaourt*. Simplesmente não consegui mais instalar nenhum software pelo Yaourt devido a essa mensagem de erro.

.. more

Após pesquisar o erro no Google de diversas maneiras não encontrei uma solução. Mas a solução era mais simples do que eu imaginei: remover e instalar novamente o libreoffice. Para isso utilizei o seguinte comando:

.. code-block:: bash

    $ sudo pacman -Rns libreoffice libreoffice-pt-BR

Em seguida reinstalei com o seguinte comando:

.. code-block:: bash

    $ sudo pacman -S libreoffice libreoffice-pt-BR

Pronto, tudo estava perfeito novamente. E vocês, usuários do Arch Linux, já passaram por algo desse tipo? Existe uma solução melhor?
