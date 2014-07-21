USBManager
##########
:date: 2010-03-10 11:53
:author: Magnun
:slug: projetos/usbmanager

.. raw:: html

   <div class="alert alert-info">

Atenção, o USBManager está desatualizado e está sendo reescrito! Acompanhe `o blog`_ para mais informações.

.. raw:: html

   </div>

O USBManager é uma gerenciador de dispositivos de armazenamento via USB escrito em Python. É uma ferramenta simples e intuitiva desenvolvida para ajudar pessoas que têm dificuldade de administrar seus dispositivos de armazenamento USB no GNU/Linux.

.. image:: {filename}/images/USBManager_icon_192.png
        :target: {filename}/images/USBManager_icon_192.png
        :alt: USBManager Icon
        :align: center

Algumas das funcionalidades do USBManager:

-  Notificações para manter o usuário informado;
-  Auxílio gráfico para a montagem e desmontagem de dispositivos;
-  Auxilia o usuário a modificar o nome (*label*) do dispositivo. Atualmente suporta FAT16. 
   FAT32, NTFS, EXT2, EXT3 and EXT4;
-  Provê informações detalhadas sobre o dispositivo;
-  Realiza análise da utilização do disco, apresentando uma visualização superficial do uso e uma visualização detalhada do consumo por pasta;

**Baixando e Instalando**
=========================

A versão USBManager 1.0.0 pode ser obtida `aqui`_. Para instalar, descompacte o arquivo e execute com o seguinte comando:

.. code-block:: bash

        $ sudo ./setup.py install

**Utilização**
==============

O USBManager pode ser chamado através do menu de Aplicação, na seção sistemas. Alternativamente, você pode invocá-lo pela linha de comando com o comando ``usbmanager``.

.. figure:: {filename}/images/USBManager_mainwindow.png
        :target: {filename}/images/USBManager_mainwindow.png
        :align: center
        :alt: USBManager Main Window

        Janela Principal do USBManager
        
        Aqui você pode montar/desmontar seus dispositivos, ver algumas informações básica, formatá-los e ver a utilização de cada dispositivo.

Mantendo-o na Barra de Status
-----------------------------

A funcionalidade da barra de status pode ser utilizada invocando o USBManager da seguinte forma:

.. code-block:: bash

        $ usbmanager --tray

.. figure:: {filename}/images/USBManager_tray_icon.png
        :target: {filename}/images/USBManager_tray_icon.png
        :align: center
        :alt: USBManager Tray Icon

        Ícone do USBManager na barra de status
        
        Clique com o botão esquerdo no ícone e a janela principal do USBManager será invocada. Clicando com o botão direito irá mostrar um menu de contexto (*popup*), conforme abaixo.

A barra de status lhe provê a funcionalidade de montar/desmontar o dispositivo com apenas 2 cliques. Com esta funcionalidade você pode interagir com o USBManager rapidamente.

.. figure:: {filename}/images/USBManager_tray_context_menu.png
        :target: {filename}/images/USBManager_tray_context_menu.png
        :align: center
        :alt: USBManager Tray Icon Context Menu

        Menu de contexto do USBManager
        
        Torna possível montar e desmontar dispositivos ou invocar a janela principal do USBManager

Uma boa sugestão é colocar o USBManager para iniciar na barra de status juntamente com o ambiente gráfico, desta forma você pode monitorar a atividade dos seus dispositivos USB através de algumas notificações.

.. figure:: {filename}/images/USBManager_old_notification3.png
        :target: {filename}/images/USBManager_old_notification3.png
        :align: center
        :alt: Novo dispositivo adicionado

        Novo dispositivo adicionado

.. figure:: {filename}/images/USBManager_old_notification2.png
        :target: {filename}/images/USBManager_old_notification2.png
        :align: center
        :alt: Device Removed
        
        Dispositivo Removido

.. figure:: {filename}/images/USBManager_old_notification1.png
        :target: {filename}/images/USBManager_old_notification1.png
        :align: center
        :alt: Dispositivo removido incorretamente

        Dispositivo removido incorretamente

Propriedades Do Dispositivo
---------------------------

Para obter informações sobre um certo dispositivo, basta selecioná-lo na janela principal e clique no ícone de propriedades, ou simplesmente clique duas vezes no dispositivo.

.. figure:: {filename}/images/USBManager_properties1.png
        :target: {filename}/images/USBManager_properties1.png
        :align: center
        :alt: Device Properties

        Informação Básica
        
.. figure:: {filename}/images/USBManager_properties2.png
        :target: {filename}/images/USBManager_properties2.png
        :align: center
        :alt: Device Properties

        Informação Avançada
        
Na janela de propriedades você pode modificar a etiqueta do dispositivo e ver várias informações, como:

-  Fabricante;
-  Tamanho;
-  Modelo;
-  Se este está montado ou não;
-  Se este é apenas leitura ou não;
-  Ponto de montagem;
-  Categoria;
-  Número de Série;
-  Tipo do sistema de arquivos;
-  Versão do sistema de arquivos;
-  Dispositivo de bloco;

Formatação
----------

Além disso, o USBManager provê uma forma rápida e simples de formatar o seu dispositivo USB. basta selecionar o dispositivo desejado e clicar no ícone de formatação (vassoura). Os seguintes sistemas de arquivos são suportados: FAT16, FAT32, NTFS, EXT2, EXT3 e EXT4.

.. figure:: {filename}/images/USBManager_formating_ext4.png
        :target: {filename}/images/USBManager_formating_ext4.png
        :align: center
        :alt: USBManager Formating Dialog

        Diálogo de formatação do USBManager
        
Para utilizar todos estes sistemas de arquivos é necessário instalar os seguintes pacotes: ``mlabel``, ``ntfsprogs`` e ``e2label``.

Utilização de Disco
-------------------

A janela de utilização do disco utiliza barras coloridas para destacar os maiores arquivos e diretórios do dispositivo. Além disso, ele também apresenta uma macro visualização do consumo, mostrando o número total de arquivos, tamanho médio de arquivos, total de diretórios e tamanho médio de diretórios.

.. figure:: {filename}/images/USBManager_disk_usage.png
        :target: {filename}/images/USBManager_disk_usage.png
        :align: center
        :alt: USBManager Disk Usage

        Utilização de Disco

Traduções
=========

O USBManager foi traduzido para 6 línguas diferentes (graças à comunidade de contribuidores do launchpad):

- Inglês;
- Holandês;
- Francês;
- Alemão;
- Russo;
- Espanhol;
- Português do Brasil;

E também existem traduções não concluídas para:


- Tailandês;
- Turco;
- Árabe;
- Búlgaro;
- Sueco;
- Hebraico;

Agradecimentos à Comunidade
===========================

Apesar de eu ser o único desenvolvedor, eu devo agradecer a algumas pessoas da comunidade que me ajudaram a concluir esse trabalho. Agradeço a todos que ajudaram comentando e escrevendo sobre o USBManager na internet e a todos que reportaram erros e bugs neste projeto.

Agradeço especialmente ao **Fabian Affolter** por me ajudar a melhorar esse projeto com sugestões e empacotamento para o Fedora.

-  **Traduções para o Árabe:** Nizar Kerkeni
-  **Traduções para o Holandês:** Donkade e cumulus007
-  **Traduções para o Francês:** Guillaume Mazoyer, Nicolas Delvaux, Nizar Kerkeni, Pascal Lemazurier e Sorkin.
-  **Traduções para o Alemão:** BBO, Fabian Affolter, Fred Seidemann, Georg Engelmann e mogli.
-  **Traduções para o Russo:** Nikolay Edigaryev, Petron, Sergey Sedov e vsink.
-  **Traduções para o Espanhol:** Demuxer, Monkey, Paco Molinero, guillemsster e kaeltas.
-  **Traduções para o Tailandês:** Krit Marukawisutthigul.
-  **Traduções para o Turco:** zeugmano

.. _o blog: http://mindbending.org/
.. _aqui: https://launchpad.net/usbmanager/+download
