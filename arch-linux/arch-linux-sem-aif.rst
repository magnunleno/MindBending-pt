Arch Linux sem AIF
##################
:date: 2012-07-25 11:49
:category: Arch Linux
:tags: aif, arhc, ask_checklist, dhcp, dhcpcd, erro, github, instalação, instalaçãokvm, iso, linux, machine, packages, pacman, python, script, select_source, shell, tutorial, virtual
:image: /images/archlogo.png

Foi noticiado neste último Domingo (dia 22/07/2012) no `portal brasileiro do Arch Linux`_ a liberação da nova ISO de instalação do Arch Linux. Esta é a primeira imagem de instalação desde Agosto do ano passado. Dentre as novidades, que podem ser `lidas na íntegra aqui`_, a que mais me chamou a atenção foi a remoção do AIF (Arch Installation Framework) -- o framework de instalação do Arch Linux -- também conhecido como "aquele diálogo de instalação".

.. image:: {filename}/images/aif-forever-alone.png
	:align: center
	:target: {filename}/images/aif-forever-alone.png
	:alt: aif-forever-alone

De acordo com a `declaração de Pierre Schmitz`_, um dos mantenedores do sistema, o AIF está sendo abandonado "devido à falta de manutenção e contribuição". O novo processo de instalação do Arch Linux será realizado através do `Arch Install Scripts`_, para mais informações consulte a página (em inglês) `*Beginners Guide*`_ na Wiki do projeto.  Será que isso realmente era necessário? Eu resolvi tirar essa prova...

.. more

.. raw:: html

   <div class="alert alert-info">

**Update 1** De acordo com o Leandro, ainda existe a opção do `ArchBoot`_ que é tão intuitiva quanto o AIF.

.. raw:: html

   </div>

.. raw:: html

   <div class="alert alert-info">

**Update 2** Para quem quiser aprender a instalar o Arch Linux sem o AIF leia `este artigo`_.

.. raw:: html

   </div>

Um Pouco de História
--------------------

O AIF foi proposto por Dieter Plaetnick (também desenvolvedor do Arch Linux) no dia 31/08/2008 no `Fórum Oficial desta distribuição`_. O projeto foi incorporado pelo grupo `Arch-Releng`_, *Arch Linux Release Engineering*, e logo o projeto se tornou um engenhoso pedaço de software (escrito em Shell Script) que objetivava tornar o processo de instalação do Arch Linux "extremamente fácil". Porém a manutenção deste software era difícil e sofrida, como declarou o proprio criador: "Se ele fosse escrito em Python ele seria mais simples e elegante, e provavelmente teria tido uma vida diferente (com mais interesse da comunidade e de outros desenvolvedores)"

Curiosamente, alguns dias antes desta última *release* (14/07/2012), Dieter anunciou que `não será mais um desenvolvedor do Arch Linux`_. De acordo com o ex-desenvolvedor a decisão foi incentivada pela "queda de interesse no projeto" e pela "pequeno time de desenvolvedores". Com isso podemos constatar que o AIF não consegui acompanhar o ritmo de evolução exigido pela distribuição e que a culpa da descontinuação do AIF é de todos nos que não contribuímos com projeto.

Meu Ponto de Vista
------------------

Primeiro eu gostaria de elucidar a todos aqueles que estão reclamando da descontinuação do AIF que vocês (e me incluo nesse grupo) têm parte da culpa. Sim, o projeto só está morrendo por falta de interesse da comunidade (nos). Como eu me incluí nesse grupo, vocês sabem que minha primeira reação foi de descontentamento, pois considero que o AIF tornava a instalação do Arch Linux um processo muito mais intuitivo. Mas após alguns estudos e testes, percebi que os mantenedores do Arch Linux tomaram a decisão correta. Pois o código do AIF é realmente sofrível e este possui muitos erros operacionais.

Como vocês sabem, desde que comecei a utilizar o Arch Linux decidi que tentaria ajudar esta distribuição a ganhar visibilidade e perder o título de "distribuição não amigável". Sabendo que haveria um descontentamento geral da nação Arch resolvi insistir um pouco mais no AIF, mesmo que este não estivesse na imagem oficial. A única forma de testar é fazer a instalação do Arch Linux puxando o AIF do repositório oficial. Porém, após algumas horas de testes constatei o mesmo que os mantenedores do Arch, a utilização do AIF se tornou inviável.

Para comprovar isso utilizei uma máquina virtual (via KVM) e iniciei a instalação através da imagem do dia 15/07/2012 (Netinstall) disponível `neste link`_.

Instalando o AIF
----------------

Após a *splash screen* que estamos acostumados, percebemos uma pequena diferença nas "boas vindas" do Arch Linux.

.. figure:: {filename}/images/arch-hello.png
	:align: center
	:target: {filename}/images/arch-hello.png
	:alt: Sem boas vindas...

        Sem boas vindas...

Após essa fria boas vindas, abri o link do Guia de Instalação Oficial (em inglês) disponibilizado na Wiki do projeto. Depois de uma leitura atenciosa fechei a página. Para meu propósito (reabilitar o AIF) ele era inútil. Então segui o caminho básico, configurei a interface *eth0* para utilizar DHCP (``dhcpcd eth0``), inicializei o banco de dados do *pacman* (``pacman -Syy``) e instalei o AIF (``pacman -S aif``), conforme abaixo:

.. image:: {filename}/images/arch-dhcpcd-aif-install.png
	:align: center
	:target: {filename}/images/arch-dhcpcd-aif-install.png
	:alt: arch-dhcpcd-aif-install

Em seguida inicializei o AIF com o comando ``aif -p interactive`` e logo na primeira opção (*Select Sources*) já encontramos o seguinte erro:

.. image:: {filename}/images/aif-error.png
	:align: center
	:target: {filename}/images/aif-error.png
	:alt: aif-error

::

    ERROR: ask_checklist makes only sense if you specify at least 1 thing (tag, item and ON/OFF switch)

Em uma rápida pesquisa no Google descobri que esse problema está ocorrendo há um bom tempo, para ser mais preciso `desde 18/03/2012`_.

Tentei seguir adiante com a instalação. Consegui passar com sucesso pelos passos "Set Editor", Set clock" e "Prepare Hard Drive(s)", porém o passo "Select packages" apresentou a seguinte mensagem:

.. image:: {filename}/images/aif-deadlock.png
	:align: center
	:target: {filename}/images/aif-deadlock.png
	:alt: aif-deadlock

::

    You must do worker select_source first before going here!.

Infelizmente, para passar pela etapa "Select Packages" é obrigatório ter passado pela etapa "Select Source". Consequentemente, o AIF não está usável para realizar instalações.

Obtendo Código do GitHub
------------------------

A título de curiosidade (já que a data da última atualização do AIF no GitHub e no repositório do Arch se diferem) realizei o mesmo teste clonando o repositório do AIF. Para isso utilizei os seguintes comandos:

.. code-block:: bash

    $ dhcpcd eth0
    $ pacman -Syy
    $ pacman -S libui-sh git make
    $ cd /tmp
    $ git clone http://github.com/Dieterbe/aif
    $ cd aif
    $ make install
    $ aif

Porém, apesar do trabalho, ocorreram os mesmos error.

Conclusão
---------

Uma solução rápida para o AIF neste momento é reescrever o menu principal forçando que a instalação seja feito por padrão a partir do Netinstall e desativar a condição da etapa "Select Packages".  Infelizmente não sei quase nada de Shell Script, mas mesmo assim tentarei hackear esse código em breve. Mas por enquanto, nada de AIF pra nos usuários de Arch, o jeito é atualizar o guia de instalação para utilizar o Arch Install Scripts.

.. _portal brasileiro do Arch Linux: http://archlinux-br.org
.. _lidas na íntegra aqui: http://archlinux-br.org/noticias/192/
.. _declaração de Pierre Schmitz: https://www.archlinux.org/news/install-media-20120715-released/
.. _Arch Install Scripts: https://wiki.archlinux.org/index.php/Arch_Install_Scripts
.. _*Beginners Guide*: https://wiki.archlinux.org/index.php/Beginners%27_Guide
.. _ArchBoot: https://wiki.archlinux.org/index.php/Archboot
.. _este artigo: /pt/instalando-o-arch-linux-iso-20120804/
.. _Fórum Oficial desta distribuição: https://bbs.archlinux.org/viewtopic.php?id=58110
.. _Arch-Releng: https://mailman.archlinux.org/mailman/listinfo/arch-releng
.. _não será mais um desenvolvedor do Arch Linux: http://mailman.archlinux.org/pipermail/arch-releng/2012-July/002628.html
.. _neste link: https://www.archlinux.org/releng/releases/2012.07.15/torrent
.. _desde 18/03/2012: https://bbs.archlinux.org/viewtopic.php?id=137873
