Novidades do Xfce 4.10 no Arch Linux
####################################
:date: 2012-04-30 18:17
:category: Notícias
:tags: ambiente, arch, atualização, gráfico, linux, mime, pacman, xfce
:image: /images/xfce-logo.png

Neste último dia 28 de Abril, após 1 ano e 4 meses de trabalho, foi
liberada a nova versão estável do ambiente gráfico Xfce, o Xfce 4.10, e
hoje (dia 30 de Abril) esta atualização foi disponibilizada no
repositório *extra* do Arch Linux. O Xfce, assim como o GNOME, é um
ambiente de trabalho gráfico que se baseia na biblioteca GTK para compor
sua interface mas, em contrapartida, possui a visa ser um ambiente de
trabalho gráfico leve e rápido, próprio para computadores com poucos
recursos de hardware. O Xfce incorpora a tradicional filosofia UNIX de
modularidade e reusabilidade, sendo assim composto por diversos módulos
e bibliotecas independentes que são combinados para criar uma ambiente
funcional e personalizado.

.. image:: {filename}/images/xfce-logo.png
	:align: center
	:target: {filename}/images/xfce-logo.png
	:alt: Xfce Logo

Recentemente -- devido ao hardware limitado do meu notebook de quase 6
anos -- tenho brincado bastante com o Xfce e, ao contrário do que eu
esperava, tenho gostado muito do resultado. Consequentemente esta
atualização me chamou a atenção pois traz algumas novas funcionalidades
que eu já estava desejando. Mas antes vamos atualizar o Xfce...

.. more

Atualizando
-----------

Para atualizar o Xfce basta emitir o seguinte comando:

.. code-block:: bash

    $ sudo pacman -Suy

Em seguida seria bom reiniciar a sessão.

Novidades
---------

Do mesmo jeito que fiz no artigo sobre o `GNOME 3.4.1`_, vou apresentar
as novidades com imagens:

.. figure:: {filename}/images/appfinder-normal-expandido.png
	:align: center
	:target: {filename}/images/appfinder-normal-expandido.png
	:alt: Appfinder Expandido e Normal

        O lançador de aplicaçõesfoi completamente reescrito e agora combina a funcionalidade do antigoxfce4-appfinder e o xfrun4.

.. figure:: {filename}/images/panel-rows.png
	:align: center
	:target: {filename}/images/panel-rows.png
	:alt: Panel Rows
        
	Agora o painel tem suporte a várias linhas.

.. figure:: {filename}/images/panel-deskbar.png
	:align: center
	:target: {filename}/images/panel-deskbar.png
	:alt: Panel Deskbar

	O painel agora tem o modo Deskbar.

.. figure:: {filename}/images/settings-mime.png
	:align: center
	:target: {filename}/images/settings-mime.png
	:alt: Settings Mime

	O novo editor de MIME types, muito útil para editar os vínculosentre tipos de arquivos e aplicações.

.. figure:: {filename}/images/settings-manager.png
	:align: center
	:target: {filename}/images/settings-manager.png
	:alt: Settings Manager

	O gerenciador de aplicações agora agrupa as aplicações por"classes".

Para um tour **completo** pela funcionalidades do Xfce 4.10 acesse o
site oficial do projeto: `http://xfce.org/about/tour`_

.. _GNOME 3.4.1: /pt/novidades-do-gnome-3-4-1-no-arch-linux
.. _`http://xfce.org/about/tour`: http://xfce.org/about/tour
