Instalando e Configurando o LibreOffice e Uma Multifuncional HP
###############################################################
:date: 2011-10-21 13:25
:category: Arch Linux
:tags: arch, cups, deskjet, escritório, f4480, fonts, gimp, gnome, hp, hpaio, hplip, impressora, instalação, libreoffice, linux, multifuncional, scanner, tutorial, usbcore, xsane
:image: /images/archlinux-curved2.png
:series: Instalando e Configurando o Arch Linux

Olá caros leitores! Esta é a quarta parte do guia `Instalando e
Configurando o Arch Linux`_. Neste artigo mostrarei como configurar a
suite de aplicativos para escritório LibreOffice e como instalar e
configurar uma impressora multifincional (com scanner integrado).

.. image:: {filename}/images/archlinux-curved2.png
	:align: center
	:target: {filename}/images/archlinux-curved2.png
	:alt: Arch Linux

O que é o LibreOffice
---------------------

Com a ajuda da nossa colega Wikipedia, vamos entender o que é o
LibreOffice e a sua relação com o OpenOffice.

.. more

O LibreOffice é uma suíte de aplicativos para escritório livre
multiplataforma. A suíte utiliza o formato OpenDocument (ODF) - formato
homologado como ISO/IEC 26300 e NBR ISO/IEC 26300 - e é também
compatível com os formatos do Microsoft Office, além de outros formatos
legados, inclusive alguns mais antigos que o Microsoft Office parou de
suportar podem ser abertos sem problemas no LibreOffice.

O LibreOffice surgiu como uma ramificação do projeto original
OpenOffice.org, que, por sua vez, é oriundo do StarOffice 5.1, adquirido
pela Sun Microsystems ao adquirir a Star Division em agosto de 1999. O
código fonte da suíte foi liberado para que fosse possível a
participação de contribuintes para desenvolvê-lo, dando início ao
projeto de desenvolvimento de um software de código aberto em 13 de
outubro de 2000, o OpenOffice.org. O principal objetivo era fornecer uma
alternativa de baixo custo, de alta qualidade e de código aberto.

Em 2010 a Sun foi comprada pela Oracle, consequentemente os
desenvolvedores decidiram sair da empresa devido a desconfiança da
comunidade de software livre em relação à aquisição da Oracle e a
credibilidade fragilizada dos projetos de código aberto da empresa. Com
isso deu-se o início da suite de escritórios LibreOffice.

Os repositórios do Arch Linux pararam de oferecer os pacotes OpenOffice
em 17 de Março de 2011.

Instalando o LibreOffice
------------------------

Para instalar o OpenOffice é imprescindível instalar primeiro os pacotes
de fontes abaixo:

.. code-block:: bash

    $ sudo pacman -S ttf-dejavu artwiz-fonts

Em seguida vamos instalar os pacotes do LibreOffice e o corretor
ortográfico *hunspell*:

.. code-block:: bash

    $ sudo pacman -S hunspell libreoffice-common libreoffice-{writer,base,
    calc,impress,math,draw,sdk,sdk-doc,gnome} 
    $ yaourt hunspell-pt-br

.. raw:: html

   <div class="alert alert-info">

Caso você não saiba o que é, como usar ou instalar o **yaourt**, leia
`este artigo`_

.. raw:: html

   </div>

Por padrão o LibreOffice não traz nenhum pacote de linguagem,
consequentemente toda a sua interface é em inglês. Para instalar a
tradução do LibreOffice para o português do Brasil basta instalar o
seguinte pacote:

.. code-block:: bash

    $ sudo pacman -S libreoffice-pt-BR

CUPS - Common Unix Printing System
----------------------------------

O CUPS é um sistema de impressão modular *open source* e padronizado
inicialmente desenvolvido pela Apple para o Mac OS X e outros sistemas
UNIX-like, mas atualmente é desenvolvido pela `Easy Software Products`_.
O CUPS possui diversas funcionalidades para servidores de impressão mas
como nosso objetivo é utilizá-lo como desktop, vou explorar somente as
características de uso do dia a dia.

.. image:: {filename}/images/logo_cups.jpg
	:align: center
	:target: {filename}/images/logo_cups.jpg
	:alt: CUPS Unix Printing System Logo

Além de simples impressão, muitas vezes nos defrontamos com a
necessidade de gerar PDFs de documentos. Quanto o caso é um documento
criado no Writer o problema é facilmente resolvido, pois o libreoffice
possui esta funcionalidade integrada, mas quando necessitamos gerar um
PDF de uma página Web pode ser necessário utilizar um impressora
virtual. Para utilizar a impressora virtual se torna necessário o pacote
cups-pdf e consequentemente precisamos do GhostScript, interpretador da
linguagem PostScript.

.. raw:: html

   <div class="alert alert-success">

**Nota** Existem plug-ins para os diversos navegadores que realizam essa tarefa
sem necessitarmos de um impressora virtual, mas como existem pessoas que
não gostam de utilizar plug-ins estou ensinado este método.

.. raw:: html

   </div>

Em resumo, precisamos instalar os seguintes pacotes:

.. code-block:: bash

    $ sudo pacman -S cups ghostscript gsfonts cups-pdf

Após a instalação precisamos alterar adicionar o módulo ``usbcore`` e o
*daemon* ``cups``, para isso adicione edite o arquivo ``/etc/rc.conf`` e
adicione a palavra *usbcore* na lista MODULES e a palavra *cups* na
lista DAEMONS:

::

    MODULES=(... usbcore ...)
    DAEMONS=(... cups ...)

Instalando um Impressora
------------------------

Infelizmente, neste passo, devido a diversidade de fabricantes, marcas e
modelos de impressoras, não serei capaz de ajudar a todos. Na `Wiki do
Arch Linux`_ existem algumas instruções para diversos modelos e marcas,
mas irei exemplificar com uma HP DeskJet F4480 (família F4400), pois é a
única que eu possuo. Basicamente, todo o processo se resume a instalar
um driver de impressora. Nesta caso, boa parte da família de impressoras
da HP tem suporte através da ``hplip``, então vamos instalá-la:

.. code-block:: bash

    $ sudo pacman -S hplip

Configurando a Impressora
-------------------------

Antes de tudo certifique-se de que a impressora está corretamente
conectada ao computador, energizada e ligada :). Em seguida, para não
ser necessário reiniciar o computador, vamos carregar o módulo do
*kernel* e em seguida iniciar o *daemon* ``cups``:

.. code-block:: bash

    $ sudo modprobe usbcore
    $ sudo rc.d start cupsd

Em seguida inicie o aplicativo de gerenciamento de impressoras,
``Aplicativos->Outros->Impressão``:

.. figure:: {filename}/images/impressora-1.png
	:align: center
	:target: {filename}/images/impressora-1.png
	:alt: Instalando a Impressora - 1

	Aplicativo de Gerenciamento de Impressoras - Sem impressoras ainda...

Agora clique em adicionar...

.. figure:: {filename}/images/impressora-2.png
	:align: center
	:target: {filename}/images/impressora-2.png
	:alt: Instalando a Impressora - 2

	Aplicativo de Gerenciamento de Impressoras - Detectando impressoras

Aguarde um momento pois o sistema está detectando as impressoras
conectadas ao seu computador. Em seguida escolha sua impressora, neste
caso HP Deskjet F4400, selecione-a e clique em avançar. Novamente
aguarde um momento pois o sistema irá detectar algumas informações desta
impressora:

.. figure:: {filename}/images/impressora-3.png
	:align: center
	:target: {filename}/images/impressora-3.png
	:alt: Instalando a Impressora - 3


	Aplicativo de Gerenciamento de Impressoras - Detalhes da impressora

Clique em aplicar e pronto.

.. figure:: {filename}/images/impressora-4.png
	:align: center
	:target: {filename}/images/impressora-4.png
	:alt: Instalando a Impressora - 4

	Aplicativo de Gerenciamento de Impressoras - Impressora instalada

Configurações Avançadas
-----------------------

Infelizmente existem algumas configurações no modo de impressão que não
podem ser configurados através da interface citada anteriormente. Para
este tipo de configurações temos o aplicativo instalado pelo pacote
``hplip``, o *HP Device Manager*, localizado em
``Aplicativos->Acessórios->HP Device Manger``:

.. figure:: {filename}/images/impressora-5.png
	:align: center
	:target: {filename}/images/impressora-5.png
	:alt: HP Device Manger

	HP Device Manger - Algumas opções avançadas

Com este aplicativos podemos administrar nossa impressora completamente,
desde simples impressão de páginas de testes, limpeza e alinhamento de
cartuchos, verificação de níveis de tinta e etc. Mas o recurso que mais
me interessa neste caso é a "Ordem de Impressão", o que possibilita
configurar a impressora para imprimir "de trás para frente", desta
forma, ao termino da impressão de um longo trabalho, eu não tenho que
reorganizar as páginas.

Scanner Integrado
-----------------

Esta minha impressora possui a funcionalidade de scanner integrado, ou
como costumam chamar, ela é uma "multifuncional". Quando comecei a ler
sobre scanners no Arch achei que esta seria uma funcionalidade difícil
de configurar, mas me enganei completamente, foi mais simples do que eu
imaginei.

Para que você possa utilizar o scanner, seu usuário deve estar no grupo
scanner. Verifique os grupos vinculados ao seu usuário da seguinte
forma:

.. code-block:: bash

    $ groups
    lp wheel games video audio optical storage camera power users admin

Caso você não esteja incluso no grupo scanner utilize o seguinte
comando:

.. code-block:: bash

    $ sudo usermod -a -G scanner magnun
    $ groups
    lp wheel games video audio optical storage scanner camera power users admin

Agora vamos instalar os pacotes necessários através do ``yaourt``:

.. code-block:: bash

    $ sudo pacman -S xsane xsane-gimp

O segundo pacote só é necessário caso você seja usuário do GIMP, ele
permite que você envie imagens escaneadas diretamente para o GIMP. Após
a instalação dos pacotes, adicione a linha ``hpaio`` dentro do aquivo
``/etc/sane.d/dll.conf`` com o seguinte comando:

.. code-block:: bash

    $ sudo echo "hpaio" >> /etc/sane.d/dll.conf

Em seguida teste o scanner iniciando o programa xssane, localizado em
``Aplicativos->Gráficos->XSane - Scanning``.

Por enquanto é só pessoal! Até mais...

.. _Instalando e Configurando o Arch Linux: /pt/series/instalando-e-configurando-o-arch-linux/
.. _este artigo: /pt/programas-essenciais-apos-a-instalacao-do-arch/
.. _Easy Software Products: http://www.easysw.com/
.. _Wiki do Arch Linux: https://wiki.archlinux.org/index.php/CUPS#Printer_driver
