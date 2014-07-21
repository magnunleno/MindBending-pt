Usando o vABS Para Instalar o Wine 1.3.24
#########################################
:date: 2011-08-02 14:11
:category: Arch Linux
:tags: abs, arch, aur, compilar, linux, makepkg, pacman, pacotes, som, vabs, wine, yaourt
:image: /images/archlogo.png
:description: A comunidade brasileira geralmente é bem parada no mundo Open Source, Entretanto, Estêvão Valadão crirou uma ferramenta que pode benenficiar toda a comunidade de usuário do Arch Linux.
:slug: usando-o-vabs-para-instalar-o-wine-1-3-24

Recentemente nosso colega Estêvão Valadão lançou o **vABS** (Versioned Arch Build System), um complemento do **ABS** que tem como principal objetivo possibilitar a compilação e instalação de versões antigas de programas no Arch Linux.

.. image:: {filename}/images/arch-linux-logo2.png
        :target: {filename}/images/arch-linux-logo2.png
        :align: center
        :alt: Arch Linux Logo

Antes de entendermos como o vABS funciona, precisamos entender como o ABS funciona.

.. more

O Que é o ABS
-------------

O ABS, acrônimo para Arch Build System, é um sistema *ports-like* para construção e empacotamento de software à partir do código fonte. Ao dizer *ports-like*, estou querendo dizer que ele é baseado e inspirado no sistema `ports`_, uma ferramenta que automatiza o processo de compilação de código fonte em sistemas BSD, e utiliza a mesma lógica (baixar, desempacotar, aplicar patch, compilar e instalar), onde todo o processo é baseado nas orientações de pequenos *scripts*, chamados de PKGBUILDs.

No Arch, o ABS armazena uma árvore de diretórios contento os PKGBUILDs no diretório ``/var/abs``. Para compilar o código fonte utilizando as instruções do PKGBUILD basta utilizar o comando ``makepkg``. Logo após a compilação do código fonte, será gerado um pacote compilado com a extensão ``.pkg.tar.gz``. E para instalar, é fácil! Você só precisa do ``pacman``, a ferramenta oficial do Arch Linux para gerenciamento de pacotes binários.

Na teoria parece ser muito complicado, mas na prática é tudo muito simples. Com os exemplos tudo ficará claro.

Utilizando o ABS
----------------

Antes de qualquer coisa, para utilizar o ABS é necessário que o próprio ABS e o pacote *base-devel* do sistema (que contém o programa makepkg) já esteja instalado em seu sistema. Para isso utilize a seguinte linha de comando abaixo:

.. code-block:: bash

    $ sudo pacman -S abs base-devel

Após concluir a instalação, vamos atualizar nossa árvore do ABS com o comando ``abs``:

.. code-block:: bash

    $ sudo abs

Em seguida vamos procurar a pasta do programa que pretendemos instalar.  Como exemplo, vamos utilizar o ABS para instalar o Wine versão 1.3.25, desta forma vamos entrar no seguinte diretório com o comando abaixo:

.. code-block:: bash

    $ cd /var/abs/community/

E efetuar a busca pelo pacote:

.. code-block:: bash

    $ ls | grep wine
    q4wine
    wine
    winefish
    winegame
    wine_gecko
    winestuff
    winetricks

Ok, encontramos a pasta. Agora vamos copiá-la para o diretório raiz do nosso usuário criando uma nova pasta chamada wine:

.. code-block:: bash

    $ cp -R wine ~/wine
    $ cd ~/wine
    $ ls
    PKGBUILD  wine.install

Agora vamos executar o comando makepkg:

.. code-block:: bash

    $ makepkg

Não se assustem, o processo é um pouco demorado e gera bastante informação da saída, afinal ele está compilando o código fonte do Wine.  Quando tudo terminar teremos o pacote ``.pkg.tar.xz`` compilado e pronto para instalação:

.. code-block:: bash

    $ ls
    pkg  PKGBUILD  src  wine-1.3.25-1-i686.pkg.tar.xz  wine-1.3.25.tar.bz2  wine.install

Para instalar o wine, vamos utilizar o pacman:

.. code-block:: bash

    $ sudo pacman -U wine-1.3.25-1-i686.pkg.tar.xz

Pronto, o processo está concluído! Para confirmar a instalação vamos fazer o seguinte teste:

.. code-block:: bash

    $ wine --version
    wine-1.3.25

Ok, tudo conforme o esperado! Viu como é mais simples do que parecia?!  Para desinstalar o pacote basta utilizar o seguinte comando:

.. code-block:: bash

    $ sudo pacman -R wine
    verificando dependências...

    Remover (1): wine-1.3.25-1

    Tamanho Total dos Pacotes a Remover:   119,47 MB

    Deseja remover estes pacotes? [S/n] s
    (1/1) removendo wine       [#############] 100%

Mas e o vABS?
-------------

Bem, como vocês devem ter notado, o ABS oferece somente a versão mais recente dos PKGBUILDs. Caso seja verificado algum problema na versão mais recente do software instalado, isso pode ser um complicador pois não existe uma possibilidade de *downgrade* (retorno para versões anteriores). Já o vABS mantem versões diferentes dos PKGBUILDs oficiais, o que é extremamente útil nas horas de necessidade.

Por coincidência, os desenvolvedores do Wine `modificaram drasticamente`_ a camada de virtualização de som no Wine, o que resultou em `alguns problemas`_. Isto significa que precisamos desinstalar o wine 1.3.25 e instalar o wine 1.3.24. Para isso utilizaremos a ajuda do vABS.

Como Utilizar o vABS
--------------------

Usar o vABS é muito simples. Primeiramente, vamos acessar a URL vabs.archlinux-br.org com seu navegador favorito. Em seguida escolheremos nossa arquitetura (no meu caso i686) e navegamos para o seguinte diretório: community/W/wine-1.3.24-1. Neste diretório encontramos os seguintes arquivos:

::

    PKGBUILD
    wine-1.3.24-1.tgz
    wine.install

Vamos baixar o pacote ``.tgz``, que contém todos os arquivos que vamos precisar para compilar o Wine, para a pasta raíz do usuário. Para isso utilize os seguintes comandos:

.. code-block:: bash

    $ cd ~
    $ wget http://vabs.archlinux-br.org/i686/community/W/wine-1.3.24-1/wine-1.3.24-1.tgz

Em seguida descompacte-o com o seguinte comando:

.. code-block:: bash

    $ tar -zxf wine-1.3.24-1.tgz
    $ cd wine-1.3.24-1

Agora compile o pacote como fizemos no caso do ABS:

.. code-block:: bash

    $ makepkg
    $ ls
    pkg  PKGBUILD  src  wine-1.3.24-1-i686.pkg.tar.xz  wine-1.3.24.tar.bz2  wine.install
    $ sudo pacman -U wine-1.3.24-1-i686.pkg.tar.xz
    resolvendo dependências...
    procurando por conflitos interrelacionados...

    Alvos (1): wine-1.3.24-1

    Tamanho Total do Download:   0,00 MB
    Tamanho Total da Instalação:   119,28 MB

    Prosseguir com a instalação? [S/n] s
    (1/1) verificando integridade do pacote      [###########] 100%
    (1/1) verificando conflitos de arquivo       [###########] 100%
    (1/1) instalando wine                        [###########] 100%
    This wine package is wow64 enabled. This means it can run 32bit/64bit Windows apps on x86_64.
    If you are on x86_64, the default WINEARCH will be win64.
    This will cause a lot of Windows applications to malfunction even if they usually work in wine.
    Please create your ~/.wine with 'WINEARCH=win32 winecfg' if you are unsure and on x86_64.
    See the Arch wiki on wine for more information.
    Dependências opcionais para wine
        giflib
        libpng
        libldap
        lcms
        libxml2
        mpg123
        openal
        jack
        libcups
        gnutls
        v4l-utils
        oss

Agora um pequeno teste para provar que a instalação da versão antiga (1.3.24) do Wine foi concluída com sucesso:

.. code-block:: bash

    $ wine --version
    wine-1.3.24

Conclusão
---------

O ABS é uma ferramenta incrível para os usuários do Arch Linux mas possui suas limitações. O vABS veio preencher as lacunas do ABS e, ao meu ver, se tornará para o usuário Arch uma ferramenta quase tão essencial quanto o AUR. Claro, ainda precisamos de uma ferramenta que automatize esse processo, similar com o yaourt. Talvez, quem saiba, até mesmo o yaourt pode vir a oferecer uma integração com o vABS.

Pensando um pouco mais à frente, acho que seria interessante criar uma forma do ABS absorver a funcionalidade do vABS, se tornando uma ferramenta unificada. Pelo que conversei com o Estêvão (e pelo pouco conhecimento que tenho da infraestrutura da solução), isso não é tão simples de se fazer pela forma como o ABS já trabalha. Mas quem sabe, esta não seria uma boa hora para pensarmos em uma quebra de paradigma e retrocompatibilidade?! Nem sempre suportar o obsoleto é uma boa política, sempre devemos permitir espaço para o novo, nem que seja rodando em paralelo com o antigo.

.. _|image1|: {filename}/images/arch-linux-logo2.png
.. _ports: http://pt.wikipedia.org/wiki/FreeBSD#Ports
.. _modificaram drasticamente: http://www.winehq.org/news/2011072201
.. _alguns problemas: http://www.omgubuntu.co.uk/2011/07/latest-wine-update-breaks-pulseaudio

