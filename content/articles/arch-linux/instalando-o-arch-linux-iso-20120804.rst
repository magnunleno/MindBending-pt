Instalando o Arch Linux - ISO 2012.08.04
########################################
:date: 2012-08-22 14:26
:category: Arch Linux
:tags: aif, arch, arch-chroot, cfdisk, dhcp, endereço ip, estático, gateway, genfstab, gnu, parted, grub, hwclock, instalação, linux, mkfs, particionador, particionamento, sfdisk, tutorial
:image: /images/archlogo.png
:series: Instalando e Configurando o Arch Linux

Conforme já foi `noticiado aqui`_, o processo de instalação do Arch
Linux mudou. Isso mesmo, não há mais um auxiliar de instalação, tudo é
responsabilidade do usuário. A princípio achei que esta mudança
dificultaria o processo de instalação desta ótima distribuição, mas após
alguns testes percebi que (na verdade) este "novo modo" de instalação é
muito mais interessante e divertido.

.. image:: {filename}/images/Arch_wite_on_scratched.png
	:align: center
	:target: {filename}/images/Arch_wite_on_scratched.png
	:alt: Arch\_wite\_on\_scratched

Entretanto, como já sabemos, o ser humano não se adapta bem a mudanças e
tende a impor dificuldades e barreiras. Levando isso em consideração (e
minha empolgação por essa distro) resolvi reescrever o meu `antigo guia
de instalação`_. Este novo guia revê todos os conceitos abordados
anteriormente porém não faz uso de animações em GIF pois, devido a
natureza deste novo instalador, há menos imagens a serem apresentadas.
Então vamos (re)começar do básico...

.. more

O Que é o Arch Linux
--------------------

O Arch Linux é uma Distribuição GNU/Linux otimizada e desenvolvida para
arquiteturas i686 e x86\_64 de forma independente. Para quem não sabe, a
ideia inicial para a criação do Arch Linux veio da distribuição Linux
chamada CRUX.

O CRUX é uma distribuição GNU/Linux bastante leve, otimizada para
arquiteturas i686 e voltada para usuários mais experientes no mundo
Linux. O foco principal desta distribuição é "keep it simple", que
reflete em um sistema de pacotes simples baseado em arquivos tar.gz,
enquanto seu objetivo secundário é a utilização de novos recursos do
Linux, ferramentas inovadoras e bibliotecas. O CRUX utiliza apenas
pacotes estáveis na sua instalação, podendo requerer a compilação de
alguns aplicativos.

O desenvolvimento do Arch é focado no equilíbrio entre simplicidade,
elegância, retidão de código e programas “bleeding edge” (extremamente
recentes). Sua leveza e simplicidade o torna fácil de estender e/ou
moldar para qualquer tipo de sistema que você esteja construindo.

O Arch Linux é considerado por muitos como um Linux difícil de usar e,
principalmente, de instalar. Porém, com um pouco de afinco, você logo
perceberá que esta distribuição é na verdade muito interessante, de
dificuldade média e que serve como uma "escola". Digo isso pois ao
entender o processo de instalação desta distribuição GNU/Linux você terá
uma compreensão mais ampla do sistema que você usa. Então deixe seu medo
de lado pois o primeiro empurrão, será dado agora.

Obtendo o Arch Linux
--------------------

Você pode baixar o ISO do Arch Linux no `site oficial`_, onde são
oferecidas as opções *torrent* e *HTTP*.

Anteriormente, o Arch Linux distribuía 2 imagens, uma para sistemas
32bits (i686) e outra para sistemas 64 bits (x86\_64), porém desde o dia
15 de Julho de 2012 deste ano a mídia de instalação desta distribuição
passou a suportar ambas as arquiteturas. Por esse motivo a imagem de
instalação termina em *-dual.iso*.

Os antigos usuários também devem estar se perguntando por que não há
mais distinção entre imagens *core* e *net install*. O fato é que agora,
o único método existente para a instalação do Arch Linux é o *net
install*. Podem verificar que o imagem de instalação ocupa apenas
incríveis 384 MBytes. Ou seja, apenas necessário.

Verificando a Imagem de Instalação
----------------------------------

Outra coisa que passou a ser oferecida desde o dia 15 de Julho de 2012 é
a assinatura do arquivo *.iso* disponibilizado no site. Para verificar a
assinatura da ISO -- o que é altamente recomendado uma vez que concede
a segurança de estar utilizando a ISO original do projeto Arch Linux --
é necessário estar em um computar rodando Arch Linux e baixar o arquivo
de assinatura (arquivo com extensão *.iso.sig*) para a mesma pasta em
que se encontra a ISO e executar o seguinte comando:

.. code-block:: bash

    $ pacman-key -v archlinux-2012.08.04-dual.iso.sig
    gpg: Signature made Sun Jul 15 17:19:46 2012 EEST using RSA key ID 9741E8AC
    gpg: Good signature from "Pierre Schmitz "

Vale ressaltar que durante o processo de verificação da assinatura
também é verificado o Hash do ISO, garantindo assim a integridade. Para
quem não possui um computador rodando Arch Linux mas também quer se
assegurar da integridade da ISO pode fazer uso do hash MD5 ou SHA1, para
isso baixe também o *md5sums.txt* ou o *sha1sums.txt* e emita o seguinte
comando para calcular o checksum:

.. code-block:: bash

    $ md5sum archlinux-2012.08.04-dual.iso
    83f3b08a58ce7397ec760817de05d8cb  archlinux-2012.08.04-dual.iso

    $ sha1sum archlinux-2012.08.04-dual.iso
    d5fb2364f9967e458984b8050724c749213152b2  archlinux-2012.08.04-dual.iso

Por fim, compare o resultado com o conteúdo dos arquivos baixados, caso
haja discrepância seu arquivo foi corrompido durante o download.

Gravando no Pen-Drive
---------------------

Para aqueles que não querem gastar mídia de CD (eu aqui ó) uma boa dica
é gravar a imagem do Arch Linux no pen-drive. Todo mundo sempre tem um
pendrive maior que 400 MBytes encostada em algum lugar. Então, faça um
backup dos dados contidos nele, plugue-o em um PC com GNU/Linux, abra um
terminal e navegue até o diretório que contem o ISO do Arch. Em seguida
emita o seguinte comando:

.. code-block:: bash

    $ dd if=archlinux-2012.08.04-dual.iso of=/dev/sdx bs=4M

Muita atenção e cuidado, o comando dd não perdoa falhas. Tenha certeza
de qual sdX é o seu pendrive.

Instalação do Arch Linux
------------------------

Bootando o Sistema
~~~~~~~~~~~~~~~~~~

O processo de boot não sofreu grandes alterações, apenas uma opção a
mais na splash screen. Agora cabe a você escolher entre as opções *Boot
Arch Linux (i686)* e *Boot Arch Linux (x86\_64)*, para arquiteturas 32
bits e 64 bits, respectivamente.

.. image:: {filename}/images/01-splash.png
	:align: center
	:target: {filename}/images/01-splash.png
	:alt: 01 - Arch Linux ISO Splash Screen

Após alguns segundos (sim, segundos) o Arch Linux já estará iniciado e
pronto para instalar. O que você verá é a seguinte imagem:

.. image:: {filename}/images/02-login.png
	:align: center
	:target: {filename}/images/02-login.png
	:alt: 02 - Arch Linux Login Screen

Note que nesta mídia de instalação não estamos usando o Bash, e sim o
Zsh. Para quem não está acostumado com este outro terminal, isso pode
ser um pouco frustrante no início, mas com o tempo você se acostuma :D.

Analisando As Possibilidades
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Por incrível que pareça, os criadores do Arch Linux atenderam meus
pedidos(!) e disponibilizaram um *"Install Guida"* na mídia de
instalação. Para isto basta consultar o arquivo *install.txt* que consta
no diretório */root*. Para isso utilize seu editor de texto predileto, o
meu é o VI então utilizei o seguinte comando [code]vi
install.txt[/code]:

.. image:: {filename}/images/03-install-guide.png
	:align: center
	:target: {filename}/images/03-install-guide.png
	:alt: 03 Arch Linux Shipped Install Guide

Okay, esquece o que eu disse sobre o *install guide*, ele simplesmente
incluíram `esta página`_ sendo que eles deveriam ter incluído `esta`_
que é muito mais completa e detalhada.

Bem, quem sabe da próxima vez eles não acertam. Quem sabe...

Pre-Configuraçções
~~~~~~~~~~~~~~~~~~

Layout de Teclado
^^^^^^^^^^^^^^^^^

Antes de instalarmos o sistema temos que preparar o ambiente. O primeiro
passo é **configurar o teclado**. Caso você utilize um teclado ABNT2,
como 90% dos Brasileiros, utilize o seguinte comando para configurá-lo
corretamente: ``loadkeys br-abnt2``

.. image:: {filename}/images/04-loadkeys.png
	:align: center
	:target: {filename}/images/04-loadkeys.png
	:alt: 04 - Arch Linux loadkeys

Interface de Rede
^^^^^^^^^^^^^^^^^

Em seguida precisamos verificar a **interface de rede**. Se sua rede
possui DHCP, apenas confirme que existe conectividade com a internet
utilizando o comando ``ping archlinux.org``, em caso de sucesso siga
adiante.

Caso algum erro tenha ocorrido verifique se seu computador conseguiu
obter a rede corretamente, para isso utilize o comando ``ip addr``:

.. image:: {filename}/images/05-ip-addr.png
	:align: center
	:target: {filename}/images/05-ip-addr.png
	:alt: 05 Arch Linux ip addr

Caso sua interface de rede não esteja aparecendo (e você utilize uma
rede cabeada comum) você terá que forçar a subida da sua interface, para
isso utilize o seguinte comando: ``ip link set eth0 up``

Caso sua interface de rede (geralmente a eth0) não possuir um endereço
IP (similar ao ressaltado acima) você deverá tentar duas abordagens:

-  Obter um IP via DHCP;
-  Configurar um IP manualmente (estático).

Para tentar obter um IP via DHCP utilize o comando ``dhcpcd eth0``. Em
seguida, verifique novamente com o comando ``ip addr`` se o sistema
obteve um IP com sucesso. Em caso negativo, será necessário utilizar IP
estático.

Utilizar um endereço estático implica em configurar 4 parâmetros no
sistema operacional, e para isso você deve obtê-los de antemão com seu
administrador de rede (ou com alguém com mais conhecimento de rede que
você), são eles: o endereço IP, a máscara de rede, o endereço IP do
gateway, e o endereço IP do servidor DNS.

Neste exemplo, utilizarei o endereço IP 192.168.1.123 a máscara de rede
255.255.255.0 (ou /24), o gateway 192.168.1.1 e o servidor DNS
192.168.1.1. O endereço IP e a máscara de rede podem são informadas em
um único comando:

.. code-block:: bash

    $ ip addr add 192.168.1.123/24 dev eth0

Para adicionar a rota padrão para o *gateway* 192.168.1.1 utilize o
comando ``ip route`` da seguinte forma:

.. code-block:: bash

    $ ip route add default via 192.168.1.1

Abaixo o exemplo da execução:

.. image:: {filename}/images/07-ip-addr-and-route.png
	:align: center
	:target: {filename}/images/07-ip-addr-and-route.png
	:alt: 07 - Arch Linux set ip addr and route

Em seguida edite o arquivo ``/etc/resolv.conf`` e deixe apenas a
seguinte linha:

.. code-block:: bash

    $ nameserver 192.168.1.1

Por fim, teste novamente o comando ``ping archlinux.org``, este deve
deve obter respostas positivas do servidor do Arch Linux.

Particionar Discos
^^^^^^^^^^^^^^^^^^

Neste exemplo de instalação utilizarei um HDD de 20 GBytes que será
dividido em 4 partições primárias:

-  /boot – 200 MBytes com o formato ext4;
-  /swap – 2 GBytes com o formato Linux Swap;
-  / (root) – 10 GBytes com o formato ext4;
-  /home – 7.8 GBytes com o formato ext4.

Vale ressaltar que esses valores são apenas para demonstração, em um
sistema para uso de verdade é recomendado reservar:

-  De 100 a 200 MBytes para o /boot;
-  De 1 a 2 vezes o tamanho da sua memória RAM (dependendo de quanto
   seja) o /swap. Para mais informações leia a página da Wiki;
-  De 20 a 20 GBytes para o / (root);
-  O espaço restante (a partir de 5 GBytes) para o /home que hospedará
   os dados do seu usuário.

Com este novo modo de instalação não estamos mais amarrados a nenhum
particionador, pelo contrário, podemos escolher o particionador que mais
nos agrada em uma lista relativamente variada. Atualmente o Arch Linux é
distribuído com os seguintes particionadores: ``fdisk``, ``cfdisk``,
``sfdisk`` e o ``GNU Parted``.

**Atenção:** Estou escrevendo (à medida que minha vida pessoal permite)
um tutorial para cada particionador. Atualmente escrevi apenas um
tutorial para o ``fdisk``, disponível `aqui`_. Para quem não gostou da
cara do ``fdisk`` recomendo que teste o ``cfdisk``, pois ele apresenta
menus e é extremamente intuitivo.

Preparando o Disco
^^^^^^^^^^^^^^^^^^

Em seguida é necessário formatar as partições, para isso utilizaremos os
comandos ``mkfs.ext4`` (para formatar as partições para o formato ext4),
``mkswap`` (para configurar uma área de swap) e ``swapon`` (para ativar
os arquivos de paginação para swap).

Abaixo o exemplo de formatação das partições ``/boot``, ``/ (root)`` e
``/home`` para o formato ``ext4`` e a preparação da partição
``/dev/sda2`` para funcionar como área de swap:


.. figure:: {filename}/images/40-mkfs-sda1.png
	:align: center
	:target: {filename}/images/40-mkfs-sda1.png
	:alt: 40-mkfs-sda1

        mkfs.ext4 sda1

.. figure:: {filename}/images/41-mkfs-sda3.png
	:align: center
	:target: {filename}/images/41-mkfs-sda3.png
	:alt: 41-mkfs-sda3

        mkfs.ext4 sda3

.. figure:: {filename}/images/42-mkfs-sda4.png
	:align: center
	:target: {filename}/images/42-mkfs-sda4.png
	:alt: 42-mkfs-sda4

        mkfs.ext4 sda4

.. figure:: {filename}/images/43-mkswap-swapon.png
	:align: center
	:target: {filename}/images/43-mkswap-swapon.png
	:alt: 43-mkswap-swapon

        mkswap && swapon

Em seguida basta montar as partições, para isso utilize os seguintes
comandos:

.. code-block:: bash

    $ mount /dev/sda3 /mnt
    $ mkdir /mnt/boot && mount /dev/sda1 /mnt/boot
    $ mkdir /mnt/home && mount /dev/sda4 /mnt/home

Configurando o Pacman
^^^^^^^^^^^^^^^^^^^^^

Como dito anteriormente essa instalação busca todos os pacotes da
internet, logo é imprescindível que o pacman esteja configurado
corretamente.

O primeiro passo é definir os servidores de origem que utilizaremos para
baixar os pacotes. Geralmente é mais rápido utilizar os servidores do
Brasil, para isso abra o arquivo ``/etc/pacman.d/mirrorlist`` com seu
editor de texto predileto e comente todas as linhas com exceção das
destacadas abaixo:

::

    Server = http://www.bitwave.com.br/downloads/archlinux/$repo/os/$arch
    Server = http://www.las.ic.unicamp.br/pub/archlinux/$repo/os/$arch
    Server = http://archlinux.c3sl.ufpr.br/$repo/os/$arch
    Server = http://pet.inf.ufsc.br/mirrors/archlinux/$repo/os/$arch

Caso ache um trabalho muito grande comentar tantas linhas (e realmente
é) utilize os seguintes comandos para reduzir o trabalho:

.. code-block:: bash

    $ sed "s/^Ser/#Ser/" /etc/pacman.d/mirrorlist > /tmp/mirrors
    $ sed '/Brazil/{n;s/^#//}' /tmp/mirrors > /etc/pacman.d/mirrorlist

Este último passo se aplica somente para sistemas 64 bits (e para
aqueles que queiram utilizar pacotes do repositório ``multilib``. Para
finalizar as alterações de configurações do pacman, edite o arquivo
``/etc/pacman.conf`` e remova o comentário das seguintes linhas:

::

    [multilib]
    SigLevel = PackageRequired
    Include = /etc/pacman.d/mirrorlist

Instalação do Sistema Básico
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Agora falta apenas instalar os pacotes do Arch Linux e o bootloader,
neste exemplo utilizarei o GRUB 2 como bootloader. Para isso utilize o
seguinte comando:

.. code-block:: bash

     $pacstrap /mnt base base-devel
     $pacstrap /mnt grub-bios

Para finalizar, vamos configurar o arquivo ``/etc/fstab``, responsável
por montar todas as partições do seu sistema durante o processo de boot.
A configuração é extremamente simples, basta o seguinte comando:

.. code-block:: bash

    $ genfstab -p /mnt >> /mnt/etc/fstab

Configurações Pós-instalação
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Muito bem, a partir deste momento faremos alterações no seu sistema já
instalado. Para isso utilizaremos uma variante do comando ``chroot``
criado pela equipe de desenvolvimento do Arch Linux, o comando
``arch-chroot``. Execute o comando da seguinte forma:
``arch-chroot /mnt``. Agora, e até a próxima vez que você emita o
comando ``exit``, você estará no seu novo sistema, então toda alteração
que você fizer será refletida no seu novo sistema.

Configurar Hostname
^^^^^^^^^^^^^^^^^^^

A primeira configuração a se fazer em um novo sistema operacional é
dar-lhe um nome (um *hostname* ). Como estou instalando o Arch Linux em
uma VM (*Virtual Machine*) vou chamar essa máquina de "Arch-VM". Para
configurar o *hostname* de uma máquina devemos alterar dois arquivos,
``/etc/hostname`` e ``/etc/hosts``.

No arquivo */etc/hostname* basta uma linha com o noma da máquina, então
utilize o comando ``echo Arch-VM > /etc/hostname`` para configurá-lo
corretamente. Já o arquivo ``/etc/hosts`` é um pouco mais complexo.
Originalmente ele estará no seguinte formato:

::

    #
    # /etc/hosts: static lookup table for host names
    #

    #<ip-address>   <hostname.domain.org>   <hostname>
    127.0.0.1       localhost.localdomain   localhost
    ::1             localhost.localdomain   localhost

    # End of file

Este arquivo funciona como um DNS estático, isto é, quando você digita
um nome no navegador ou na linha de comando (por exemplo www.google.com)
seu sistema operacional precisa converter esse nome para endereço IP
(por exemplo 187.7.130.52). A sequência utilizada para essa conversão é:
consultar a tabela definida em ``/etc/hosts`` e em seguida (caso não o
encontre) consultar o servidor DNS.

O arquivo ``/etc/hosts`` funciona como uma tabela, em sua primeira
coluna encontra-se o endereço IP, em sua segunda coluna encontra-se o
FQDN (*Fully Qualified Domain Name*) e na última coluna uma série de
apelidos, também conhecidos como alias. O endereço IP (versão 4)
127.0.0.1 e o endereço IP (versão 6) ::1 indicam o seu próprio
computador, esse endereço é chamado de *loopback*. O nome localhost ou
endereço IP 127.0.0.1 (ou ::1) é utilizado por vários componentes do
sistema operacional (como o Xorg, GNOME, KDE e etc).

Desta forma, temos que adicionar o nome da nossa máquina para essa
"tabela". Altere-a para que ela fique da seguinte forma:

::

    #
    # /etc/hosts: static lookup table for host names
    #

    #<ip-address>   <hostname.domain.org>   <hostname>
    127.0.0.1       localhost.localdomain   localhost Arch-VM
    ::1             localhost.localdomain   localhost Arch-VM

    # End of file

Configurar Layout de Teclado
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A configuração do teclado e da fonte a ser utilizada no console é
extremamente simples, basta editar o arquivo ``/etc/vconsole.conf`` para
que ele fique da seguinte forma:

::

    KEYMAP=br-abnt2
    FONT=lat0-16
    FONT_MAP=

Configurar o Idioma
^^^^^^^^^^^^^^^^^^^

Já a configuração do idioma do sistema demanda um trabalho um pouco
maior, pois será necessário editar 2 arquivos (``/etc/locale.gen`` e
``/etc/locale.conf``) e em seguida executar o comando ``locale-gen``.

Vamos começar pelo arquivo ``/etc/locale.gen``, este arquivo serve de
"arquivo de configuração" para o comando ``locale-gen`` (que
executaremos em breve). Abra-o com seu editor de texto predileto e
busque as seguintes linhas:

::

    #pt_BR.UTF-8 UTF-8
    #pt_BR ISO-8859-2

Remova o caractere que indica o comentário, deixando-as da seguinte
forma:

::

    pt_BR.UTF-8 UTF-8
    pt_BR ISO-8859-2

Por fim execute o comando ``local-gen``, que irá gerar a seguinte saída:

.. image:: {filename}/images/61-locale-gen.png
	:align: center
	:target: {filename}/images/61-locale-gen.png
	:alt: 61-locale-gen

O último arquivo que editaremos na configuração de idiomas será o
``/etc/locale.conf``, responsável por setar as variáveis de ambiente que
determinam a língua do sistema operacional. Essas variáveis definem,
além da tradução das páginas de ajuda (*man pages*) e outras mensagens,
formatos de data e hora, moeda e etc. Crie este aquivo com as seguintes
linhas:

::

    LANG=pt_BR.utf-8 
    LC_COLLATE=C 
    LC_TIME=pt_BR.utf-8 

Como este arquivo não existia anteriormente nenhuma destas configurações
estão surtindo efeito, para evitar problemas com isso emita o seguinte
comando: ``export LANG=pt_BR.utf-8``. Você pode verificar que esta
alteração surtiu efeito emitindo o comando ``date``. Anteriormente,
quando seu *locale* era indefinido ele te retornaria uma mensagem
similar à seguinte:

.. code-block:: bash

    $ date
    Sat Aug 18 19:23:24 BRT 2012

Porém, após a exportação, você verá a seguinte mensagem:

.. code-block:: bash

    $ date
    Sáb Ago 18 19:23:52 BRT 2012

Configurando Região/Hora
^^^^^^^^^^^^^^^^^^^^^^^^

Já que falamos de hora, talvez o resultado do comando anterior esteja
incorreto, então é hora da configurar de configurar o relógio. Caso a
hora esteja incorreta utilize o comando abaixo para configurar a data e
hora corretamente:

.. code-block:: bash

    $ hwclock --set --date="YYYY-MM-DD hh:mm:ss"

Agora vamos configurar a zona/região, para isso verifique o diretório
``/usr/share/zoneinfo/`` e busque o seu continente, no nosso caso é
America. Entre no diretório America e busque sua região, que no meu caso
é Sao\_Paulo. Este último é um arquivo, não tente abri-lo.

Uma vez descoberto isso volte para o diretório ``/etc`` (com o comando
``cd /tec``) e crie um link para o arquivo encontrado. Veja o exemplo
abaixo:

.. code-block:: bash

    $ ln -s /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

Agora, adicione a mesma informação no arquivo ``/etc/timezone``. Para
isso edite o arquivo e adicione o texto ``America/Sao_Paulo``. Por
último vamos configurar o relógio do hardware, existem 2 opção, o uso de
localtime e UTC. O UTC é o mais recomendado porém ele não se dá bem com
sistemas dual boot (com Windows).

Para configura o relógio utilizando localtime emita o comando
``hwclock --systohc --localtime``, já se você for utilizar UTC utilize o
seguinte comando ``hwclock --systohc --utc``.

Configurando o rc.conf
^^^^^^^^^^^^^^^^^^^^^^

Uma das últimas configurações a serem feitas será no arquivo
``/etc/rc.conf``. Esta configuração depende muito do que você quer fazer
daqui para frente. Como o intuito deste tutorial é apenas a instalação
básica não realizarei nenhuma alteração na chave ``DAEMONS``, apenas na
chave interface (para que a interface eth0 seja configurada
automaticamente durante o boot).

Caso você esteja utilizando DHCP, basta editar a linha ``#interface``
para que ela fique da seguinte forma:

::

    interface=eth0

Já se você precisou configurar um IP estático, é necessário informar
novamente todas aquelas informações (endereço IP, mascara de rede e o
endereço IP do gateway). Para isso edite o arquivo e deixe-o similar ao
mostrado abaixo:

::

    interface=eth0
    address=192.168.1.123
    netmask=255.255.255.0
    broadcast=192.168.1.255
    gateway=192.168.1.1

Preparando o Boot
^^^^^^^^^^^^^^^^^

Como últimos retoques iremos preparar o "ambiente de boot".
Primeiramente vamos preparar o ambiente de ramdisk inicial. Para isso
emita o seguinte comando:

.. code-block:: bash

    $ mkinitcpio -p linux

Agora vamos instalar o bootloader, neste caso o Grub 2. Para isso basta
emitir os seguintes comando:

.. code-block:: bash

    $ grub-install /dev/sda
    $ grub-mkconfig -o /boot/grub/grub.cfg

Por último altere a senha do usuário root com o comando ``passwd``,
apenas siga as instruções. Ao final digite ``exit`` para sair do
ambiente *chroot*.

Últimos Comandos
^^^^^^^^^^^^^^^^

Por fim apenas desmonte os discos com o seguinte comando:

.. code-block:: bash

    $ umount /mnt/{boot,home,}

Agora sim, emita o comando reboot e aguarde o Arch Linux iniciar em toda
a sua glória! Ah, e não se esqueça de comemorar como um cientista maluco
gritando: **It's alive!!! It's Alive!!!**

.. youtube:: QuoKNZjr8_U
        :align: center

Conclusão
---------

Como vocês podem perceber, a instalação do Arch Linux **realmente** não
é nenhum bixo-de-sete-cabeças. Na minha humilde opinião ela é bem
intuitiva e divertida, basta apenas ter um "pequeno guia" indicando tudo
o que deve ser alterado e os parâmetros a serem inseridos. Outro ponto
positivo para este novo método de instalação é a facilidade de
automatização da instalação, estou trabalhando em um script (que
postarei em breve) que automatiza todo o processo de instalação e
configuração do Arch Linux coberto neste pequeno tutorial. Este tipo de
facilidade é muito útil para instalar o Arch Linux em um sistema
embarcado dispositivos de entrada/saída (teclados, mouses e monitores).
Eu mesmo vou utilizar isto para criar minha central multimídia :D.

.. _noticiado aqui: /pt/arch-linux-sem-aif/
.. _antigo guia de instalação: /pt/guia-de-instalacao-do-arch-linux/
.. _site oficial: http://www.archlinux.org/download/
.. _esta página: https://wiki.archlinux.org/index.php/Installation_Guide
.. _esta: https://wiki.archlinux.org/index.php/Beginners%27_Guide
.. _aqui: /pt/particionamento-com-o-fdisk-no-gnu-linux/
