Atualizando o Firefox 5 no Arch Linux
#####################################
:date: 2011-06-24 16:07
:category: Arch Linux
:tags: arch, atualizar, firefox 5
:image: /images/ff-logo.png
:description: Novamente, tentarei refutar um pouco o conceito de que o Arch Linux é uma distribuição GNU/Linux difícil de se utilizar. Vejam o processo de atualização do navegador Firefox.
:slug: atualizand-o-firefox-5-no-arch-linux

Como todos já sabem, no dia 21/06 foi lançado uma nova versão de um dos mais populares navegadores, o Firefox 5. Mas já?! Sim, o novo Firefox levou apenas 3 meses para ser finalizado, ao contrário da versão anterior que levou 3 anos para ser finalizado. Isso faz parte da nova estratégia da Mozilla que visa acompanhar as atualizações frequentes do Chrome. Possivelmente eles perceberam que máxima de Eric S. Raymond também se aplicam a eles: `Release early, release often`_.


.. image:: {filename}/images/firefox_5_beta.jpg
        :target: {filename}/images/firefox_5_beta.jpg
        :align: center
        :alt: Firefox 5

.. more

Novas Funcionalidades
---------------------

O Firefox5 não conta com grandes mudanças como o Firefox 4, mas ele traz melhorias muito importantes. Dentre elas destaco as seguintes:

-  Mais `estabilidade e segurança`_;
-  Suporte melhorado para: HTML5, CSS3, MathML, XHR e SMIL;
-  Melhorias para a `funcionalidade "Do not track header"`_;
-  Melhorias na performance.
-  Novos parâmetros para As abas inativas, `melhorando a performance`_.

Como atualizar
--------------

Com esse lançamento fiquei curioso, como atualizar o Firefox no Arch Linux?! Simples...

.. code-block:: bash

    $ sudo pacman -S firefox

Abaixo a saída do comando só a título de documentação

.. code-block:: bash

    $ sudo pacman -S firefox
    resolvendo dependências…
    procurando por conflitos interrelacionados…

    Alvos (1): firefox-5.0-1

    Tamanho Total do Download: 10,60 MB
    Tamanho Total da Instalação: 27,32 MB

    Prosseguir com a instalação? [S/n] s
    :: Obtendo pacotes de extra…
    firefox-5.0-1-i686              10,6M 191,4K/s 00:00:57 [#################] 100%
    (1/1) verificando integridade do pacote                 [#################] 100%
    (1/1) verificando conflitos de arquivo                  [#################] 100%
    (1/1) atualizando firefox                               [#################] 100%
    $

Amigo do usuário
----------------

O que me levou a um pensamento interessante: Isso é complexo? Claro que não! Isso é mais que simples, pra mim isso é *user friendly*. Esse mesmo processo em uma outra distribuição mais voltada para usuário, seria assim:

.. code-block:: bash

    $ sudo add-apt-repository ppa:mozillateam/firefox-stable
    $ sudo apt-get update
    $ sudo apt-get upgrade

.. image:: {filename}/images/wheres-your-god-kitten.jpg
        :target: {filename}/images/wheres-your-god-kitten.jpg
        :align: center
        :alt: Where's your god now?

.. _Release early, release often: http://en.wikipedia.org/wiki/Release_early,_release_often
.. _estabilidade e segurança: http://www.hexus.net/content/item.php?item=30901
.. _funcionalidade "Do not track header": http://en.wikipedia.org/wiki/Do_not_track_header
.. _melhorando a performance: https://developer.mozilla.org/en/DOM/window.setTimeout#Inactive_tabs

