Lançado o Gnome 3.12
####################
:date: 2014-03-26 16:26
:category: Gnome
:tags: gnome, lançamento, desktop
:image: /images/iamgnome.png
:description: Hoje o Projeto GNOME lançou o GNOME 3.12 um dos ambientes de trabalho mais utilizados nas distribuições GNU/Linux.

Hoje, dia 26 de Março de 2014, o `foi lançado o GNOME 3.12`_, o próximo *milestone* da série GNOME 3. Esta *release* contém diversas melhorias, atualizações, novas funcionalidades, bem como diversas mudanças na API para desenvolvedores. Já está disponível a `Press Release`_ e o `Release Notes`_.

.. image:: {filename}/images/window-selection-3.12.png
        :align: center
        :alt: GNOME 3.12 Window Selection
        :target: {filename}/images/window-selection-3.12.png

Citando Matthias Clasen, da Equipe de Lançamento do GNOME

        Esta é uma versão emocionante para GNOME, traz muitas novidades e
        melhorias, incluindo pastas de aplicativos, melhorias no *system status* e
        suporte a monitores de alta resolução.

.. more

Algumas das melhorias desta versão:

* Uma atualização significativa na experiência de encontrar e instalar novas aplicações;
* Diversas melhorias visuais para as aplicações 'Videos' e 'GEdit';
* Melhorias no suporte a *displays* de alta resolução;
* Grandes mudanças nas aplicações 'Software' e 'Web';
* Melhoria no tempo de *start up*, assim como um uso de recursos mais eficiente;
* A funcionalidade de criar "pastas" para as aplicações, permitindo organizá-las.

Abaixo um vídeo demonstrando algumas das mudanças:

.. youtube:: n77cwRJUrLg
        :width: 560 
        :height: 315
        :align: center

Testando o Gnome 3.12
---------------------

GNOME 3.12 estará disponível nas principais distribuições em breve. Neste meio tempo você pode se divertir com a imagem *Live Demo* que pode ser obtida aqui.

.. raw:: html

        <div style="text-align:center; padding-bottom: 20px;">
        <button type="button" class="btn btn-primary"><a target="_blank" href="http://download.gnome.org/misc/promo-usb/gnome-3.12.iso">Download do Live Demo</a>
        </button>
        </div>

Instructions for installing the image on to a USB stick with GNU/Linux:
Instruções para a cópia da imagem para um dispositivo de armazenamento USB utilizando o GNU/Linux:

* Insira o dispositivo (qualquer dado contido no dispositivo será apagado!);
* Execute `dmesg` em um terminal: Isto irá te dizer a localização do seu dispositivo entre chaves, por exemplo `sdb`;
* Para escrever a imagem execute o comando `sudo dd if=gnome-3.12.iso of=/dev/DRIVE bs=8M conv=fsync`, substituindo *DRIVE* com a localização obtida anteriormente (ex: `/dev/sdb`, mas não `/dev/sdb1`);
* Uma vez que a operação tenha terminado, você pode reiniciar o seu computador com o dispositivo USB inserido.


Sobre o Gnome
-------------

O GNOME foi iniciado em 1997 por dois estudantes universitários, Miguel de Icaza e Federico Mena Quintero. Seu objetivo: produzir um ambiente de trabalho livre. Desde então o GNOME ser tornou uma organização de enorme sucesso. Utilizado por milhões de pessoas ao redor do mundo, é o ambiente mais popular para os sistemas operacionais do GNU/Linux e UNIX-Like. O software do GNOME tem sido utilizado com sucesso em empresas de grande escala e empresas públicas.

A comunidade GNOME é composta de centenas de colaboradores de todo o mundo, muitos dos quais são voluntários. Esta comunidade é apoiado pela Fundação GNOME, uma organização independente sem fins lucrativos que presta assistência financeira, organizacional e legal. A Fundação é uma instituição democrática dirigida pelos seus membros, todos contribuidores ativos do GNOME. O GNOME e sua Fundação trabalha para promover a liberdade de software através da criação da experiência de usuário inovadora, acessível e bela.

.. _foi lançado o GNOME 3.12: http://www.gnome.org/news/2014/03/gnome-3-12-released/
.. _Press Release: http://www.gnome.org/press/2014/03/gnome-3-12-released-with-new-features-for-users-and-developers/
.. _Release Notes: https://help.gnome.org/misc/release-notes/3.12/
.. _Download do Live Demo: http://download.gnome.org/misc/promo-usb/gnome-3.12.iso
