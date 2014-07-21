Os Botões do Gnome 3 Não Se foram
#################################
:date: 2011-03-07 00:16
:category: Gnome
:tags: botões, gnome, gnome 3, gnome shell
:description: Graças ao poder do mundo OpenSource e a capacidade de ouvir do grupo de desenvolvimento do Gnome 3, o botão de minimizar não foi completamente banido deste ambiente desktop.
:image: /images/gnome.png

Conforme eu havia `postado anteriormente`_, o time de design e desenvolvimento do Gnome 3 tomou a decisão de remover os botões de maximizar e minimizar de suas janelas. Porém eles ainda não haviam decidido se a funcionalidade seria permanentemente desativada ou somente ocultada.

.. image:: {filename}/images/gnome.png
        :align: center
        :target: {filename}/images/gnome.png
        :alt: Gnome Logo

Ontem, foi postado no `Blog do Diego`_ (um contribuidor do projeto Gnome) que a funcionalidade de maximizar e minimizar as janelas continuarão disponíveis e funcionais, podendo ser acessadas pelo menu da janela (clique com o botão direito) ou por atalhos convencionais, além dos novos gestos previstos para o Gnome 3.

.. more

Outro detalhe é que será possível reativar os controles de minimizar e maximizar utilizando o "gsettings" (linha de comando) ou o Gconf-editor.  Para reativar os botões no Gnome 3 basta utilizar a linha abaixo:

.. code-block:: bash

    $ gconftool-2 -s -t string /desktop/gnome/shell/windows/button_layout ":minimize,maximize,close"

Utilizando o Gconf-Editor, basta navegar em desktop > gnome > shell e mudar a chave "button\_layout" para o valor ":minimize,maximize,close", conforme o screenshot abaixo:

.. figure:: {filename}/images/gnome-shell-buttons.png
        :align: center
        :target: {filename}/images/gnome-shell-buttons.png
        :alt: Botões do Gnome Shell

        Botões do Gnome Shell

.. _postado anteriormente: /pt/mais-mudancas-previstas-no-gnome-3
.. _Blog do Diego: http://blogs.gnome.org/diegoe/2011/03/05/minimize-and-maximize-in-gnome3/
