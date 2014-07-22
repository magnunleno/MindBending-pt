Instalação do Arch Linux Sem Dor
################################
:date: 2011-06-06 19:16
:category: Arch Linux
:tags: arch, guia, instalação, linux, tutorial
:image: /images/archlogo.png
:featured: /images/ArchLinux2.png
:description: Vamos desmistificar o processo de instalação do Arch Linux que, apesar de toda a sua fama de difícil e de 'somente para iniciados', é uma distribuição GNU/Linux muito eficiente.
:slug: guia-de-instalacao-do-arch-linux
:series: Instalando e Configurando o Arch Linux

.. raw:: html

   <div class="alert alert-warning">Esse artigo está desatualizado, leia a nova versão <a class="reference external" href="/pt/instalando-o-arch-linux-iso-20120804/" target="_blank">aqui</a></div>

De acordo com seu `Guia de Instalação Oficial`_, o Arch Linux é uma Distribuição GNU/Linux otimizada e desenvolvida para arquiteturas i686 e x86\_64 de forma independente. Para quem não sabe, a ideia inicial para a criação do Arch Linux veio da distribuição Linux chamada CRUX.

.. image:: {filename}/images/ArchLinux2.png
        :target: {filename}/images/ArchLinux2.png
        :align: center
        :alt: Arch Linux

O CRUX é uma distribuição GNU/Linux bastante leve, otimizada para arquiteturas i686 e voltada para usuários mais experientes no mundo Linux. O foco principal desta distribuição é "keep it simple", que reflete em um sistema de pacotes simples baseado em arquivos tar.gz, enquanto seu objetivo secundário é a utilização de novos recursos do Linux, ferramentas inovadoras e bibliotecas. O CRUX utiliza apenas pacotes estáveis na sua instalação, podendo requerer a compilação de alguns aplicativos.

.. more

O desenvolvimento do Arch é focado no equilíbrio entre simplicidade, elegância, retidão de código e programas “bleeding edge” (extremamente recentes). Sua leveza e simplicidade o torna fácil de estender e/ou moldar para qualquer tipo de sistema que você esteja construindo.

O Arch Linux é considerado por muitos como um Linux difícil de usar e, principalmente, de instalar. Mas vou provar neste post que isso é uma inverdade, e uma injustiça com essa poderosa distribuição Linux. Por isso, deixe seu medo de lado e saiba que qualquer usuário Linux, independente de seu conhecimento sobre o sistema, pode usar essa poderosa distribuição no seu dia-à-dia, seja no trabalho, em casa, ou mesmo em seus estudos (escola, faculdade). E o primeiro empurrão, nós damos aqui.

Obtendo o Arch Linux
--------------------

Você pode baixar o ISO do Arch Linux no `site oficial`_. Esta imagem pode ser grboavada em um CD-ROM ou em um pen-drives (através do comando ``dd``). A imagem está disponível em duas variantes:

-  *core*- contém um conjunto de pacotes básicos e atualizados. São votadas para quem não tem conexão com a internet;
-  *net*- essa imagem contém apenas o básico para subir um sistema virtual e baixar os pacotes da internet.

Similar ao Debian (que possui a sua versão *netinstall*), até ai nenhuma grande surpresa. Como às vezes eu uso os CDs de GNU/Linux para recuperar outros dispositivos, prefiro sempre baixar e gravar a versão "core".

Gravando no Pen-Drive
---------------------

Para aqueles que estão com problemas no drive de CD (eu aqui ó) uma boa dica é gravar a imagem do Arch Linux no pen-drive. Todo mundo sempre tem um pendrive de 1G encostada em algum lugar. Então, faça um backup dos dados contidos nele, plugue-o em um PC com GNU/Linux, abra um terminal e navegue até o diretório que contem o ISO do Arch. Em seguida emita o seguinte comando:

.. code-block:: bash

    $ dd if=archlinux-XXX.iso of=/dev/sdX

Muita atenção e cuidado, o comando ``dd`` não perdoa falhas. Tenha certeza de qual sdX é o seu pendrive.

Efetuando o Boot pelo CD
------------------------

Para quem está acostumado com a instalação do Debian antigo, a instalação do Arch Linux não assusta. Mas ao mesmo tempo ela faz o usuários se esforçar muito mais. As telas me lembra de algumas telas do Red Hat.

O que eu mais estranhei é que após o boot ele me joga em um bash e me manda chamar o script de instalação. Por que não iniciar automaticamente? Bem, isso eu imagino que se deva ao fato desse mesmo CD poder ser utilizado para reparar o seu sistema e como uma "caixa de ferramentas para emergências". Claro, também é pelo fato do Arch não querer facilitar as coisas pra seus usuários :D. Agora vamos ver o passo a passo da instalação:

Bootando o Sistema
------------------

O processo de *boot*é simples. Após inserir o sistema é apresentada a *splash screen*. Bastando apenas escolher a opção "*Boot Arch Linux*". A propósito, é uma bela splashscreen, não?!

.. figure:: {filename}/images/01-Arch-Linux-ISO-Splash-Screen.jpg
        :target: {filename}/images/01-Arch-Linux-ISO-Splash-Screen.jpg
        :align: center
        :alt: Arch Linux ISO Splash Screen

        Arch Linux ISO Splash Screen

Após o *boot*, é apresentada a tela de login. Acima uma mensagem de onde tiramos as seguintes informações fundamentais: Os logins padrões são *root*e *arch*, ambos sem senha.

Após o *logon* é apresentado a mensagem informando como iniciar a instalação e que existe uma guia de instalação em ``/usr/share/aif/docs``. Ótimo, caso tenhamos dúvidas não será necessário um Notebook ou coisa parecida para consultar a internet. Para os que querem se antecipar, esse mesmo `guia está disponível aqui`_, leiam pois vale a pena.

.. figure:: {filename}/images/02-Apos-Login.jpg
        :target: {filename}/images/02-Apos-Login.jpg
        :align: center
        :alt: Após o Login

        Após o Login

Configurando o Teclado
----------------------

Na mesma mensagem é informado o utilitário ``km``, muito útil para nos brasileiros, que utilizamos o *layout* ABNT-2. Chamando o utilitário temos a seguinte tela:

.. figure:: {filename}/images/03-Esolher-Teclado-ABNT-2.jpg
        :target: {filename}/images/03-Esolher-Teclado-ABNT-2.jpg
        :align: center
        :alt: Esolher Teclado ABNT 2

        Esolher Teclado ABNT 2

Conforme mostra a imagem acima, basta escolher a opção ``i386/qwerty/br-abnt2.map.gz``. Depois é questionado sobre a fonte utilizada no terminal, recomendo ir na opção '*skip*' (pular).

Iniciando a Instalação
----------------------

Ao sair do ``KM``, estaremos de volta ao *bash*. Para começar o processo de instalação basta chamar o instalador ``/arch/setup`` ou ``aif -p interactive``. Caso precise de um console extra durante a instalação (para fazer verificações e/ou configurações), pressione Ctrl+Alt+F2.

.. figure:: {filename}/images/04-Alerta-de-Instalacao.jpg
        :target: {filename}/images/04-Alerta-de-Instalacao.jpg
        :align: center
        :alt: Alerta de Instalação

        Alerta de Instalação

Logo no início temos uma mensagem interessante, e um pouco assustadora.  Após a mensagem, é mostrado um "*script* de instalação":

.. figure:: {filename}/images/05-Ordem-de-Instalacao.jpg
        :target: {filename}/images/05-Ordem-de-Instalacao.jpg
        :align: center
        :alt: Ordem de Instalação

        Ordem de Instalação

Se você tentar pular qualquer passo dessa sequência o instalador irá reclamar. A vantagem dessa tela é que você pode refazer algum passo (que tenha sido feito incorretamente) a hora que quiser, mas bem que o processo de instalação poderia ser forçadamente linear. Detalhes a parte, vamos selecionar a origem da instalação.

Origem da Instalação
--------------------

Para ajustar a origem de instalação escolha a opção "*Select Source*".  Aqui temos a opção de mudar as fontes de onde serão "puxados" os arquivos para instalação, temos a opção CD ou Net (internet). Para obter os pacotes mais atuais sugiro selecionar a opção Net.

.. figure:: {filename}/images/06-Escolhendo-a-Fonte.jpg
        :target: {filename}/images/06-Escolhendo-a-Fonte.jpg
        :align: center
        :alt: Escolhendo a Fonte

        Escolhendo a Fonte

Para baixar da internet temos que configurar a interface de rede, para isso escolha a opção "*Setup Network*", em seguida escolha uma interface (no meu caso ``eth0``) e escolha usar DHCP (caso sua rede tenha um).  Após isto estará concluída a configuração da interface.

.. figure:: {filename}/images/07-Configurando-a-Rede1.gif
        :target: {filename}/images/07-Configurando-a-Rede1.gif
        :align: center
        :alt: Configurando a Rede

        Esta animação mostra o processo de configuração da interface eth0

Agora vamos escolher um Mirror. Um Mirror é um servidor que contem os pacotes que serão baixados e posteriormente instalados. Para um melhor desempenho é sempre aconselhável escolher um Mirror perto de você. Como estamos no Brasil, vou escolher o Mirror da Unicamp, para isso escolha a opção "2 Choose Mirror" e em seguida procure pela opção que mais se te agrada. Em seguida retornamos para o menu principal.

.. figure:: {filename}/images/08-Mirrors.jpg
        :target: {filename}/images/08-Mirrors.jpg
        :align: center
        :alt: Mirrors

        Mirrors

Ao final desse processo escolha a opção "Return to Main Menu" (retornar ao menu principal).

Configurando a Hora
===================

Em Seguida precisamos configurar o relógio.

.. figure:: {filename}/images/09-Hora.jpg
        :target: {filename}/images/09-Hora.jpg
        :align: center
        :alt: Configurar a Hora

        Configurar a Hora

A primeira opção é selecionar a região e o fuso horário. Em seguida Verificamos a hora e a data. Caso você tenha um *dualboot*com o Windows, sugiro escolher *localtime*. No meu caso escolhi UTC. Eu gosto de usar o NTP para manter o relógio atualizado, mas você pode também setar o relógio manualmente. Depois escolha a opção "retornar" e "retornar ao menu principal".

.. figure:: {filename}/images/10-Configurando-Regiao-e-Hora1.gif
        :target: {filename}/images/10-Configurando-Regiao-e-Hora1.gif
        :align: center
        :alt: 10 - Configurando Região e Hora

        Esta animação mostra o processo de configuração do relógio utilizando o NTP.

Preparando o Disco Rígido
-------------------------

Aqui definiremos as partições e etc. Vou mostrar um guia para dois cenários:

-  Um HD vazio, logo podemos formatar-lo sem problemas;
-  Um HD com 4 partições, /boot (sda1), swap (sda2), / (sda3) e /home (sda4), onde não iremos apagar o conteúdo do /home.

Instalando em Um Diso Rígido Vazio
----------------------------------

Escolha a opção *auto-prepare*, que irá apagar totalmente o HD e criar as partições automaticamente. Ele somente irá te questionar sobre tamanhos das partições (``/boot``, ``swap`` e /) e o *filesystem* a ser utilizado para cada partição. Caso você esteja instalando em uma máquina virtual, utilize os valores padrões. Caso seja uma máquina de uso diário e com um HD de tamanho razoável, recomendo que o / tenha de 10 a 15 Giga (é nessa partição que ficam os programas e o cache do pacman). Para o ``/boot`` pode ser mantido o valor padrão de 100 Mega. Já o *swap* depende de quanta memória seu PC terá.

Em seguida ele irá te perguntar o *filesystem* a ser usado. Eu escolheria o ext4, mas isso é gosto pessoal. Agora basta esperar a formatação concluir e no final escolha a opção "*Return to Main Menu*".

.. figure:: {filename}/images/11-Preparando-HD-Simples1.gif
        :target: {filename}/images/11-Preparando-HD-Simples1.gif
        :align: center
        :alt: 11 - Preparando HD Simples

        Animação mostrando o processo de formatação automática do HD

Instalando em um HDD com /home
------------------------------

Para esse caso, selecione a opção "*Manually configure block devices, filesystem and mountpoints*" e escolha o método de identificação por dispositivo (dev). Neste exemplo temos o HD dividido da seguinte forma:

-  sda1 - /boot (será formatado utilizando o filesystem ext4);
-  sda2 - swap (será formatado);
-  sda3 - / (será formatado utilizando o filesystem ext4);
-  sda4 - /home (NÃO será formatado, pois possui uma partição ext4 com dados).

Partição sda1: ponto de montagem /boot
--------------------------------------

Escolha a partição sda1, em seguida informe que irá formatar, escolha o *filesystem* ext4, o ponto de montagem ``/boot``, informe um *label* (eu geralmente uso *boot*) e pule a parte de opções adicionais para o mkfs.ext4.

Ao final, a linha que representa a partição sda1 deve ter ficado da seguinte forma:

::

    /dev/sda1   raw->ext4;yes;/boot;no_opts;boot;no_params

**Traduzindo isso ai em cima:** será utilizado o *filesystem* ext4; será formatado; partição ``/boot``; sem opções adicionais; o *label* é *boot*; sem parâmetros adicionais.

Partição sda2: ponto de montagem swap
-------------------------------------

Escolha a partição sda2, em seguida informe que irá formatar, escolha o *filesystem swap* e pule a parte de opções adicionais para o mkswap.

Ao final, a linha que representa a partição sda2 deve ter ficado da seguinte forma:

::

    /dev/sda2   raw->swap;yes;no_mountpoint;no_opts;no_label;no_params

**Traduzindo:** será uma área de *swap*; será formatado; não possui *mountpoint*; sem opções adicionais; sem *label*; sem parâmetros adicionais.

Partição sda3: ponto de montagem /
----------------------------------

Escolha a partição sda3, em seguida informe que irá formatar, escolha o *filesystem* ext4, o ponto de montagem /, informe um *label* (eu geralmente uso *root*) e pule a parte de opções adicionais para o mkfs.ext4.

Ao final, a linha que representa a partição sda3 deve ter ficado da seguinte forma:

::

    /dev/sda3   raw->ext4;yes;/;no_opts;root;no_params

**Traduzindo:** será utilizado o filesystem ext4; será formatado; o *mountpoint* será /; sem opções adicionais; sem o *label root*; sem parâmetros adicionais.

Partição sda4: ponto de montagem /home
--------------------------------------

Esta partição é a que contêm dados do usuário e **NÃO** será formatada.  Escolha a partição sda4, em seguida informe que **NÃO** irá formatar, escolha o *filesystem* ext4, o ponto de montagem ``/home`` e pronto.  escolha a opção "*Done*" e finalize o processo.

Ao final, a linha que representa a partição sda4 deve ter ficado da seguinte forma:

::

    /dev/sda4   raw->ext4;no;/home;no_opts;no_label;no_params

**Traduzindo:** será utilizado o *filesystem* ext4; **NÃO** será formatado; o *mountpoint* será ``/home``; sem opções adicionais; o label não será alterado; sem parâmetros adicionais.

Abaixo uma animação mostrando todo o processo:

.. figure:: {filename}/images/12-Preparando-HD-Avancado1.gif
        :target: {filename}/images/12-Preparando-HD-Avancado1.gif
        :align: center
        :alt: 12 - Preparando HD Avançado

        Esta animação mostra o processo de formatação de um HD que possui dados na partição /home que não podem ser perdidos.

Escolhendo e Instalando Pacotes
-------------------------------

Ao terminar o particionamento do HD, escolha a opção "*Select Packages*". A não ser que você saiba exatamente o que está fazendo, sugiro simplesmente clicar em Ok até voltar ao menu principal. Em seguida, escolha "*Install Packages*" e aguarde...

.. figure:: {filename}/images/13-Selecionando-e-Instalando-Pacotes1.gif
        :target: {filename}/images/13-Selecionando-e-Instalando-Pacotes1.gif
        :align: center
        :alt: 13 - Selecionando e Instalando Pacotes

        Esta animação mostra o processo de escolha e instalação dos pacotes.

Configurando o Sistema
----------------------

Ao termino da instalação dos pacotes escolha a opção "*Configure System*". O instalador irá te questionar sobre a utilização das configurações de rede durante a instalação, escolha a opção "*Yes*". Em seguida escolha o editor a ser utilizado. Como esta será uma máquina *desktop*, não há muito o que alterar. Como sou usuário do VIM, escolhi o editor VI, caso você não conheça o VI, utilize outro editor como o Nano. Ao final o processo de instalação irá te apresentar uma lista de arquivos para edição, conforme a imagem abaixo:

.. figure:: {filename}/images/14-Arquivos-de-configuracao.jpg
        :target: {filename}/images/14-Arquivos-de-configuracao.jpg
        :align: center
        :alt: Arquivos de configuração

        Arquivos de configuração

O Arch segue o princípio do FreeBSD de utilizar o arquivo ``/etc/rc.conf`` como local principal de configuração do sistema. Este arquivo contém um vasto leque de informação, e como o nome implica, também contém configurações para os arquivos sob ``/etc/rc*``.

Na tela acima, escolha a opção ``/etc/rc.conf``. Procure a linha *HOSTNAME* e altere o valor entre aspas colocando o nome que você quer para sua máquina, no exemplo coloquei *magnun-Desktop*. Ainda no *rc.conf* procure a linha *LOCALE* e altera para *pt\_BR.utf8*, essa linha define que seu GNU/Linux será em português.

.. figure:: {filename}/images/15-Editando-o-rcconf.jpg
        :target: {filename}/images/15-Editando-o-rcconf.jpg
        :align: center
        :alt: Editando o rc.conf

        Editando o rc.conf

Para completar a configuração de localização do Arch, edite o arquivo ``/etc/local.gen``. Nele descomente as linhas *pt\_BR.ISO-8859-1* e *pr\_BR.UTF-8*.

Em seguida vá na opção "*Root-Password*", e insira a senha do root. Para finalizar, vá em "*Done*" e escolha OK.

Instalando o *Bootloader*
-------------------------

Aqui vamos instalar o Bootloader GRUB. Claro, hoje em dia existem diversos *bootloaders* diferentes e mais bonitos que o GRUB, mas como o foco é apenas a instalação básica do sistema, vamos proceder com a instalação do GRUB.

Escolha a opção "*Install Bootloader*", em seguida escolha *Grub*. Após isso o instalador irá te apresentar o arquivo de configuração do GRUB, simplesmente passe adiante. Após esse passo, lhe será perguntado onde instalar o GRUB, escolha o seu HD onde foi feita a instalação (nesse caso sda). O GRUB é instalado na MBR, logo não é necessário informar nenhuma partição.

Para finalizar a instalação, escolha a opção "*Exit Install*" e você cairá de volta ao *shell*. Reinicie seu computador com o comando ``reboot`` e em seguida retire o CD do Arch. Após o POST você verá a tela do GRUB abaixo:

.. figure:: {filename}/images/16-GRUB.jpg
        :target: {filename}/images/16-GRUB.jpg
        :align: center
        :alt: Hello GRUB

        Hello GRUB

Ao final do carregamento do sistema, você verá a tela de boas vindas:

.. figure:: {filename}/images/17-Login.jpg
        :target: {filename}/images/17-Login.jpg
        :align: center
        :alt: Tarde de mais! Agora você está infectado pelo Arch!

        Tarde de mais! Agora você está infectado pelo Arch!

Pronto, estamos com o Arch instalado no computador.

No próximo post mostrarei como configurar seu Arch Linux para o uso do dia a dia.

Até mais...

.. _aqui: /pt/instalando-o-arch-linux-iso-20120804/
.. _Guia de Instalação Oficial: https://wiki.archlinux.org/index.php/Official_Arch_Linux_Install_Guide
.. _site oficial: http://www.archlinux.org/download/
.. _guia está disponível aqui: https://wiki.archlinux.org/index.php/Official_Arch_Linux_Install_Guide

