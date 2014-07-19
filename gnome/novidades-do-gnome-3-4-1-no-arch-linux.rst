Novidades do Gnome 3.4.1 No Arch Linux
######################################
:date: 2012-04-25 12:28
:category: Gnome
:tags: aplicativos, arch, atualização, extensões, funcionalidade, gnome, gnome 3, gnome shell, interface, linux, pacman
:image: /images/gnome.png
:slug: novidades-do-gnome-3-4-1-no-arch-linux

Finalmente, o GNOME 3.4.1 está disponível no repositório *extra* do Arch
Linux! O GNOME 3.4 foi `originalmente lançado em 28 de Março`_, mas em
18 de Abril recebeu sua primeira atualização, a versão 3.4.1. Desde o
seu lançamento o GNOME 3 tem causado muita discussão, seja pela completa
quebra de paradigma -- boa parte causada pelo Gnome-Shell --, ou pela
falta de polimento em detalhes. Mas não se esqueçam, o GNOME 3 ainda é
um trabalho em andamento e aos poucos todos os seus detalhes serão
corrigidos e suas funcionalidades (que ainda estão ausentes) serão
reimplementadas.

.. image:: {filename}/images/gnome-3.41.jpg
	:align: center
	:target: {filename}/images/gnome-3.41.jpg
	:alt: Gnome 3.4.1 Banner

Mas como todos já sabem, sou um entusiasta deste novo ambiente desde que
ele tinha uma cara horrível (procurem no Google o princípio do
Gnome-Shell), então eu estava aguardando a chegada desta *release* nos
repositórios do Arch Linux.

.. more

Mas antes um aviso
==================

Antes de tudo tenho que avisar que muitos das extensões do Gnome-Shell
pararam de funcionar. Isto já é rotina após as atualizações do GNOME,
provavelmente parte da API é alterada e algumas extensões param de
funcionar. Ah, isso também vale para alguns dos Temas, tanto do
Gnome-Shell quanto do GTK3...

.. image:: {filename}/images/broken-gnome-shell-extensions.png
	:align: center
	:target: {filename}/images/broken-gnome-shell-extensions.png
	:alt: Broken Gnome Shell Extensions

Então um recomendação extremamente válida é excluir toda e qualquer
extensão que você possua no seu Gnome-shell (bem como temas) e, após a
atualização, reinstale-os para garantir que está rodando a versão mais
recente.

Atualizando o GNOME
===================

A atualização é bem simples, basta emitir os seguintes comandos:

.. code-block:: bash

    $ pacman -Suy
    $ pacman -S gnome gnome-extra

Em uma outra atualização do Gnome (se não me engano Gnome 3.2) novos
pacotes foram adicionados aos grupos ``gnome`` e ``gnome-extra`` e, após
a atualização, eles não foram instalados automaticamente, por isso
incluí a última linha, que reinstala todos os pacotes dos grupos
supracitados. Agora só mais um aviso antes das novidades...

Principais Novidades
====================

Certamente a melhor forma de demonstrar as prinicpais novidades é
através de imagens! Então vamos lá...

.. raw:: html

   <div class="row"><div class="col-md-6 col-xs-6">

.. figure:: {filename}/images/document-search.png
	:align: center
	:target: {filename}/images/document-search.png
	:alt: Documents Search

        Agora é possível realziar buscas dedocumentos pelo Gnome-Shell, lembrando que os documentos devem estar"listados" através da aplicação Documents.

.. raw:: html

   </div><div class="col-md-6 col-xs-6">

.. figure:: {filename}/images/application-menu.png
	:align: center
	:target: {filename}/images/application-menu.png
	:alt: Application Menu

        Finalmente o menu de aplicação estárecebendo alguma atualização.

.. raw:: html

   </div></div>
   <div class="row"><div class="col-md-6 col-xs-6">

.. figure:: {filename}/images/background.jpg
	:align: center
	:target: {filename}/images/background.jpg
	:alt: Background

        O papel de parede padrão do GNOME 3 agora éanimado, ele passa por uma transação suave baseada na hora dodia!

.. raw:: html

   </div><div class="col-md-6 col-xs-6">

.. figure:: {filename}/images/power-settings.png
	:align: center
	:target: {filename}/images/power-settings.png
	:alt: Power Settings

        A tela de configurações de energia foi completamenteredesenhada

.. raw:: html

   </div></div>
   <div class="row"><div class="col-md-6 col-xs-6">

.. figure:: {filename}/images/video-calling.png
	:align: center
	:target: {filename}/images/video-calling.png
	:alt: Video Calling

        Chamadas em Vídeo através do Empathy

.. raw:: html

   </div><div class="col-md-6 col-xs-6">

.. figure:: {filename}/images/boxes.png
	:align: center
	:target: {filename}/images/boxes.png
	:alt: Boxes

        A aplicação Boxes: Um gerenciado de MáquinasVirtuais

.. raw:: html

   </div></div>

.. figure:: {filename}/images/scrollbars.png
	:align: center
	:target: {filename}/images/scrollbars.png
	:alt: Novas barras de rolagens

        Scrollbars

Novidades "Menores"
===================

Estas são algumas outras novidades interessantes mas que não mereçem um
screenshot:

-  Smoother scrolling e um painel de configurações melhorado;
-  Chamadas de vídeo adicionada ao Empathy;
-  Popups e System Tray mais inteligente;
-  Melhor suporte à deficientes;
-  Navegador Epiphany renomeado pra "Web";
-  Melhor suporte a Hardware;
-  Vários pequenos melhoramentos listados no "projeto" `*Every Detail
   Matters*`_ (pode ser traduzido para "Todo Detalhe Conta");

Diversos outros aplicativos tiveram sua interface gráfica modificada:

-  Documents
-  Epiphany
-  Contacts
-  Disks

Repositório de Extensões
========================

Por último, mas não menos importante, agora existe um `"repositório"
oficial`_ para as extensões do Gnome-Shell. Basta acessá-lo via web,
escolher as extensões que mais te agradam e ativá-las, elas serão
baixadas e instaladas automaticamente no seu sistema, no diretório
``~/.local/share/gnome-shell/extensions/``.

.. figure:: {filename}/images/gnome-extensions-page.png
	:align: center
	:target: {filename}/images/gnome-extensions-page.png
	:alt: Gnome Extensions Page

        Página Extensions do Gnome.org

Minha decepção
==============

Dessa atualização eu tive apenas uma decepção, o aplicativos Boxes
(gerenciador de máquinas virtuais) não está nos repositórios oficiais do
Arch Linux. Encontrei ele apenas no AUR e ainda não tive tempo de
instalá-lo. Mas assim que possível retornarei com mais novidades!

.. _originalmente lançado em 28 de Março: http://library.gnome.org/misc/release-notes/3.4/
.. _*Every Detail Matters*: https://live.gnome.org/EveryDetailMatters
.. _"repositório" oficial: https://extensions.gnome.org
