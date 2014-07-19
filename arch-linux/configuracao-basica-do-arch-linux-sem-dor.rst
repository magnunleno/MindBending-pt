Configuração Básica do Arch Linux Sem Dor
#########################################
:date: 2011-06-10 19:57
:category: Arch Linux
:tags: arch, configuração, gdm, gnome3, guia, instalação, sudo, tutorial, xorg
:image: /images/archlogo.png
:description: Apesar da instalação do Arch Linux ser bem exigente ela não entrega o sistema pronto para utilização, ainda é necessário que realizemos uma série de configurações e instalações para que o nosso computador se torne usável após a instalação.
:series: Instalando e Configurando o Arch Linux

Dando prosseguimento ao nosso `Guia de Instalação e Configuração do Arch Linux`_, hoje veremos algumas configurações básicas do sistema e a instalação dos componentes básicos do sistema (sudo, Xorg, GDM e o Gnome 3).

.. image:: {filename}/images/archlogo.png
        :target: {filename}/images/archlogo.png
        :alt: Arch Logo
        :align: center

Utilizando o Pacman
-------------------

Um dos destaques do Arch Linux é o seu gerenciador de pacotes padrão, o Pacman. Ele é simples, rápido, robusto e combina formatos simples de pacotes binários com um sistema de construção de pacotes simplificado. O Pacman também mantem o sistema atualizado através da sincronização de listas de pacotes com um servidor "mestre". Este modelo de cliente/servidor permite ao usuário fazer o download e instalar seus pacotes de interesse, utilizando um simples comando para resolver todas as dependências (algo semelhante ao ``apt-get`` do Debian). Ele é escrito em linguagem C e utiliza extensões do tipo ``.pkg.tar.xz`` para representar seus pacotes.

.. more

Assim como o ``apt-get``, o pacman também possui uma lista de repositórios (similar aos PPAs) localizada em ``/etc/pacman.d/mirrorlist``. Através do uso dessa lista, é possível adicionar diversos repositórios, fornecendo ao sistema diversas origens disponíveis. Esse tipo de funcionalidade é muito utilizada no Debian/Ubuntu para manter seus programas sempre atualizados. Já no Arch Linux essa função é pouco utilizada pois seus repositórios oficiais possuem praticamente todos os programas necessários para o usuário, além de serem atualizados com frequência. Afinal o Arch é uma rolling release.

Aprender a utilizar o pacman é extremamente simples. Abaixo uma tabela mostrando a função de cada comando:

.. table::
        :class: table

        ===================================== =========================================
        Funcionalidade                        Comando
        ===================================== =========================================
        Buscar pacote                         pacman -Ss <palavra-chave>
        Instalar pacote                       pacman -S <nome-do-pacote>
        Instalar pacote de um repositório     pacman -S <nome-do-repo>/<nome-do-pacote>
        Remover pacote                        pacman -R <nome-do-pacote>
        Remover pacote e suas dependências    pacman -Rs <nome-do-pacote>
        Mostrar informações detalhadas        pacman -Si <nome-do-pacote>
        ===================================== =========================================

Neste tutorial, apenas os comandos e funções mais simples serão usados, para a construção de seu ambiente de trabalho pós-instalação. Para mais informações sobre o uso mais aprofundado do Pacman recomendo a leitura de seu Wiki oficial (disponível em Português do Brasil `aqui`_), além desse `ótimo artigo do Berlotto`_

Atualização do Banco de Dados do Pacman
---------------------------------------

.. raw:: html

   <div class="alert alert-warning"><strong>Atenção</strong>, nesta nova versão do ArchLinux não é mais necessário executar estes passos. Pule para próxima sessão ;)</div>

Mas antes de qualquer coisa, vamos atualizar o banco de dados do pacman.  Não sei ao certo se isso é um problema que ocorre somente na instalação com a imagem de 05/2010, mas ao tentar usar o pacman sem efetuar a atualização da lista de repositórios, ele me mostra a seguinte mensagem:

.. code-block:: bash

    (…)
    >>> The pacman database format has changed as of pacman 3.5.0.
    >>> You will need to run `pacman-db-upgrade` as root.
    >>>
    [root@Arch ~]# pacman-db-upgrade
    ==> Detetado um formato de base de dados pré 3.5 – atualizando…
    ==> Feito.
    [root@Arch ~]# pacman –version

     ..–.                  Pacman v3.5.2 – libalpm v6.0.2
    / _.-’ .-.  .-.  .-.   Copyright (C) 2006-2011 Pacman Development Team
    \  ‘-. ‘-’  ‘-’  ‘-’   Copyright (C) 2002-2006 Judd Vinet
     .’–’
    Este programa pode ser redistribuído livremente sob
    os termos da GNU General Public License

    [root@Arch ~]#

Eu imagino que isso ocorra durante a instalação, com a geração de um banco de dados desatualizado (anterior à versão anterior 3.5.2) e ao baixar a versão mais nova do pacman (apenas durante a instalação) ele encontra um problema de compatibilidade. Para resolver esse pequeno empecilho basta chamar o seguinte comando:

.. code-block:: bash

    $ pacman-db-upgrade

Em seguida, efetue o comando seguinte para verificar se não existem atualizações disponíveis:

.. code-block:: bash

    $ pacman -Suy

.. raw:: html

   <div class="alert alert-warning"><strong>Cuidado ao atualizar todo o sistema</strong>, pois o Arch utiliza softwares recém lançados que podem vir a lhe trazer dor de cabeça no futuro (incompatibilidades, instabilidades, etc). Então esteja precavido quando for atualizá-lo.</div>

Instalando o Sudo
-----------------

O primeiro componente que iremos adicionar ao sistema pós-instalação é o ``sudo``. É de conhecimento de todos que, utilizar o sistema com a conta de super usuário (*root*) não é uma boa politica de segurança. O sudo permite aos usuários comuns obter privilégios de super usuário para executar tarefas específicas de maneira segura, controlável, rastreável e aditável. O nome é uma forma abreviada de se referir a super user do (fazer como super usuário).

Para instalar o sudo utilize o seguinte comando:

.. code-block:: bash

    $ pacman -S sudo

Após a instalação do sudo é necessário editar o arquivo ``/etc/sudoers``. Para isso você pode utilizar o comando visudo (que abrirá uma sessão do VI) ou abrir o arquivo diretamente com seu editor de textos predileto (caso não saiba usar o VI). Ao abrir o arquivo vá até a linha:

::

    #%wheel  ALL=(ALL) ALL

e descomente (retire o símbolo "#" do início da linha). Ela ficará da seguinte forma:

::

    %wheel  ALL=(ALL) ALL

Criando um Usuário
------------------

Agora que já instalamos o sudo podemos criar um novo usuário e abandonar o uso da conta de root eternamente. Para criar o usuário basta usar o comando adduser e informar os dados solicitados, conforme Log abaixo:

.. code-block:: bash

    $ adduser

    Login name for new user []: magnun

    User ID (‘UID’) [ defaults to next available ]:

    Initial group [ users ]:

    Additional groups (comma separated) []:
    lp,wheel,games,video,audio,optical,storage,scanner,power,users

    Home directory [ /home/magnun ]

    Shell [ /bin/bash ]

    Expiry date (YYYY-MM-DD) []:

    New account will be created as follows:

    —————————————
    Login name…….: magnun
    UID…………..: [ Next available ]
    Initial group….: users
    Additional groups:
    lp,wheel,games,video,audio,optical,storage,scanner,power,users
    Home directory…: /home/magnun
    Shell…………: /bin/bash
    Expiry date……: [ Never ]

    This is it… if you want to bail out, hit Control-C. Otherwise, press
    ENTER to go ahead and make the account.

As opções entre colchetes ("[" "]") são as opções-padrão das informações solicitadas pelo sistema, caso você deixe vários deses campos em branco (apenas pressionando a tecla Enter a cada opção).

É Importante ressaltar os grupos que adicionamos (na quarta linha do comando ``adduser``). Abaixo uma breve explicação de alguns dos grupo mais importantes:

-  audio - tarefas que envolvem a placa de som e aplicativos relacionados;
-  wheel - para usar o ``sudo``;
-  storage - para gerenciar mídias;
-  video - tarefas que envovem aceleração de hardware 3D;
-  optical - para gerenciar CDs e DVDs;
-  floppy - para acessar o drive de disquete;
-  lp - para gerenciar tarefas de impressão.

Para uma lista completa dos grupos e uma breve explanação sobre eles, veja `esse artigo sobre usuários e grupos`_ da Arch Linux Wiki.

Veja que o processo de criação de seu novo usuário ainda não terminou.  Quando ele chegar nesse ponto:

::

    This is it... if you want to bail out, hit Control-C.  Otherwise, press
     ENTER to go ahead and make the account.

pressione a tecla Enter para continuar (**NUNCA** pressione Control-C ou a criação de seu novo usuário será interrompida). Em seguida, serão questionados alguns dados irrelevantes, mas no final do procedimento aparecem alguns campos que podem ser de seu interesse implementar:

::

    Creating new account…

    Changing the user information for magnun
    Enter the new value, or press ENTER for the default
    Full Name []: Magnun Leno
    Room Number []:
    Work Phone []:
    Home Phone []:
    Other []:
    Digite a nova senha UNIX:
    Redigite a nova senha UNIX:
    passwd: senha atualizada com sucesso

    Account setup complete.

Pronto! Agora temos um usuário pronto para uso. A seguir, efetue o *logout* do sistema e entre com o seu novo usuário para efetuar seu novo *login*! E nada de usar seu PC como *root* daqui em diante, ok?!

Habilitando autocompletar no sudo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Muitas pessoas reclamam do sudo, pois ele não dá a opção de autocompletar comandos no terminal. Mas existe uma solução para essa "particularidade". Para isso basta configurar propriamente o seu sudo recém-instalado, entrando no arquivo ``~/.bashrc`` e adicionando a seguinte linha no final do arquivo:

.. code-block:: bash

    $ complete -cf sudo

.. raw:: html

   <div class="alert alert-success"><strong>Atenção</strong> ao alterar o <code>~/.bashrc</code> você precisa fechar e abrir seu terminal, para que todas as suas modificações passem a ter efeito.</div>

Repassando alias
~~~~~~~~~~~~~~~~

Outra coisa que incomoda no sudo é que os *alias* (uma alcunha, ou nome secundário) criados os nós para a renomeação de comandos só funcionam dentro do shell de nosso usuário, e não no sistema como um todo. Uma solução "feia" que muitos costumam fazer para resolver esse problema, é a criação desses mesmos alias para a conta do *root*, mas no wiki do Arch Linux você encontrará uma solução mais "inteligente".

Novamente volte no ``~/.bashrc`` e adicione a seguinte linhas no final do arquivo:

::

    alias sudo='sudo '

Adicione essa linha exatamente como descrita (se precisar, recorte e cole esta linha do tutorial). Para maiores informações a respeito de configurações do sudo leia `essa página do Wiki do Arch Linux`_.

Instalando os Drivers Proprietários da NVIdia
---------------------------------------------

Sei que existem *drivers* livres para placas NVidia, mas, vamos admitir, eles não são tão bons quanto os proprietários. Para placas mais novas basta usar o seguinte comando para instalar os drivers de interesse:

.. code-block:: bash

    $ pacman -S nvidia nvidia-utils

Para mais informações sobre a instalação dos drivers proprietários da NVidia, veja `esse artigo sobre o driver oficial da NVidia`_ presente no Wiki do Arch Linux. Mas caso você deseje instalar apenas os drivers livres, siga as instruções `desse artigo`_.

Instalando o Xorg
-----------------

O Xorg é uma implementação pública de código aberto do sistema *X11 X Window System*. Basicamente, se você deseja utilizar uma GUI (Interface Gráfica de Usuário) no Arch, vai precisar ter o Xorg instalado em seu computador. Para isso basta usar o seguinte comando e aguardar sua finalização:

.. code-block:: bash

    $ pacman -S xorg-server xorg-xinit xorg-utils xorg-server-utils

Para maiores informações sobre a instalação e configuração do Xorg, veja `esse artigo sobre o Xorg`_ no wiki do Arch Linux

Vale lembrar que o Arch é aquilo que você faz, então vamos instalar algumas fontes nele. Isso vai ajudar a deixá-lo mais bonito.

.. code-block:: bash

    $ sudo pacman -S ttf-dejavu ttf-bitstream-vera ttf-liberation

E pronto! Você agora tem em seu sistema o uso de fontes mais agradáveis para uso em seu dia-à-dia.

Instalando o GDM
----------------

GDM é sigla para *GNOME Display Manager* (Gerenciador de Display do GNOME), um pequeno programa que roda no seu sistema em segundo plano carregando suas sessões do X. O GDM se apresenta a você como uma tela de *login*, e para sua segurança, irá impedir o seu acesso ao sistema, caso tenha esquecido sua senha (ou outra pessoa tente acessar seu sistema sem sua permissão). Em outras palavras ele é aquela telinha de boas vindas que te pergunta seu usuário e senha após o *boot* de seu computador.  Para instalá-lo basta utilizar o seguinte comando abaixo:

.. code-block:: bash

    $ sudo pacman -S gdm

Para mais informações sobre o GDM veja `o seguinte artigo`_ no Wiki do Arvh Linux.

Instalando o GNOME 3
--------------------

O GNOME 3 é, até o presente momento, a versão mais nova do ambiente de trabalho da Fundação GNOME. O GNOME (acrônimo para *GNU Network Object Model Environment*) é um projeto de software livre para um Ambiente de Trabalho para os usuários. Já os desenvolvedores também poderão utilizar a Plataforma de Desenvolvimento GNOME no intuito de contribuir para o desenvolvimento desse fantástico projeto. Vale lembrar que o GNOME dá ênfase especial a usabilidade, acessibilidade e internacionalização de seu ambiente de trabalho.

A comunidade de desenvolvimento do GNOME conta tanto com voluntários mundo afora, quanto com empregados de várias empresas. Inclusive grandes empresas como Hewlett-Packard, IBM, Mandriva, Novell, Red Hat, e Sun, contribuem de forma contínua com seu desenvolvimento. Por sua vez, o GNOME também é filiado ao Projeto GNU, de onde herdou a missão de prover um ambiente de trabalho composto inteiramente por software livre. Por isso mesmo, esse ambiente de trabalho pode ser utilizado por vários sistemas baseados em Unix, principalmente pelos sistemas Linux e BSD-like. Atualmente o GNOME é um dos ambientes de trabalho mais usados pelos usuários GNU/Linux competindo lado a lado com o também poderosíssimo KDE.

Para instalar o GNOME em seu Arch Linux, utilize o comando abaixo:

.. code-block:: bash

    $ sudo pacman -S gnome gnome-extra gnome-tweak-tool gnome-system-tools

Com a nova versão do Arch e do Gnome, alguns pacotes foram reformulados. Utilize o comando abaixo.

.. code-block:: bash

    $ sudo pacman -S gnome gnome-extra gnome-tweak-tool gnome-utils rhythmbox

Para mais informações sobre a instalação e configuração do GNOME veja `esse artigo`_ da wiki do Arch Linux.

Configurando Tudo
-----------------

Configurar?! Sim! Ou você acha que o GNOME e o GDM vão iniciar sozinhos sem você ordenando para que eles o façam? Isso é o Arch, ele só faz o que você manda ele fazer, nada acontece sem você querer, ou por "debaixo dos panos digitais" do sistema. Vamos então começar com o básico de configuração de seu novo sistema gráfico.

Alterando de runlevel 3 para runlevel 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edite o arquivo ``/etc/inittab`` através do comando sudo, utilizando o editor de textos vi. como mostrado abaixo:

.. code-block:: bash

    $ sudo vi /etc/inittab

Procute a linha:

::

    id:3:initdefault:

e comente-a (coloque o símbolo "#" no início da linha), deixando-a assim:

::

    #id:3:initdefault:

Essa linha é a responsável por subir o *runlevel* 3 em seu sistema, ou seja, o uso do "terminal", e representa o uso do sistema multi-usuário em modo texto. Com a sua desativação do *runlevel* 3, você precisa agora ativar o *runlevel* 5 (uso do sistema multiusuário em modo gráfico).  Para isso, descomente a linha abaixo (retirando o símbolo "#" do início da linha):

::

    #id:5:initdefault:

de forma que ela fique assim:

::

    id:5:initdefault:

Com isso, o seu Arch recém instalado com GDM e GNOME poderá iniciar sempre em modo gráfico (*runlevel* 5), e com isso permitir o uso de um *login* gráfico.

Trocando o XDM pelo GDM
~~~~~~~~~~~~~~~~~~~~~~~

Mas ainda é preciso desativar um sistema de *login* concorrente ao GDM, o XDM (o *login* gráfico genérico do GNU/Linux). Para isso, neste mesmo arquivo, procure a linha

::

    x:5:respawn:/usr/bin/xdm -nodaemon

e comente-a (acrescentando o símbolo "#" ao início da linha), deixando-a assim:

::

    #x:5:respawn:/usr/bin/xdm -nodaemon

Com isso, informamos ao Arch que não queremos utilizar o XDM como "tela de boas vindas". Agora vamos informar ao sistema que queremos utilizar o GDM. Para isso descomente a seguinte linha (retirando o símbolo "#" do início da linha):

::

    #x:5:respawn:/usr/sbin/gdm -nodaemon

de forma que ela fique assim:

::

    x:5:respawn:/usr/sbin/gdm -nodaemon

Configurando alguns daemons
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ao finalizar esse procedimento, só faltará configurarmos alguns daemons para iniciar automaticamente junto ao boot do Arch Linux. Para isso edite o arquivo ``/etc/rc.conf`` e na linha:

::

    DAEMONS=(syslog-ng network crond)

insira a palavra ``dbus`` e ``networkmanager`` ao final, ainda dentro dos parênteses. No final ela deverá ficar parecido com:

::

    DAEMONS=(syslog-ng network crond dbus networkmanager)

Reiniciando o Sistema
---------------------

Depois de todas essas etapas de configuração, você precisa reiniciar seu sistema para validação a execução das mesmas. Para reiniciar o sistema utilize com o sudo o comando reboot:

.. code-block:: bash

    $ sudo reboot

Após o reinício do computador você deve ser recepcionado por essa belezinha aqui:

.. figure:: {filename}/images/gnome3-gdm.png
        :target: {filename}/images/gnome3-gdm.png
        :alt: Gnome 3 GDM
        :align: center

        Gnome 3 GDM

Basta logar no sistema e apreciar seu novo sistema operacional Arch Linux. O mesmo ainda não está totalmente configurado para o seu dia-a-dia. Isso significa que ainda tem muitos outros tutoriais pela frente, para lhe ajudar a ter o melhor Arch Linux em seu computador, do jeito que você quer! Do jeito que você gosta!

No próximo artigo irei mostrar como instalar o ``yaourt`` (além de explicar o que é o ``yaourt`` e para que ele serve) e como instalar os principais players, plugins, temas, descompactadores e muito mais!

Até lá...

.. _Guia de Instalação e Configuração do Arch Linux: /pt/guia-de-instalacao-do-arch-linux/
.. _aqui: https://wiki.archlinux.org/index.php/Pacman_%28Portugu%C3%AAs%29
.. _ótimo artigo do Berlotto: http://berlotto.blog.br/dicas-para-trabalhar-com-o-pacman/1726/
.. _esse artigo sobre usuários e grupos: https://wiki.archlinux.org/index.php/Users_and_Groups#Groups
.. _essa página do Wiki do Arch Linux: https://wiki.archlinux.org/index.php/Sudo
.. _esse artigo sobre o driver oficial da NVidia: https://wiki.archlinux.org/index.php/Nvidia
.. _desse artigo: https://wiki.archlinux.org/index.php/Nouveau
.. _esse artigo sobre o Xorg: https://wiki.archlinux.org/index.php/Xorg_%28Portugu%C3%AAs%29
.. _o seguinte artigo: https://wiki.archlinux.org/index.php/GDM
.. _esse artigo: https://wiki.archlinux.org/index.php/Gnome
