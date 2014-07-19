Automatizando a Instalação do Arch Linux - ISO 2012.08.04
#########################################################
:date: 2012-09-05 13:58
:category: Arch Linux
:tags: arch, automação, expressões, gist, git, gnu, hostname, instalação, linux, locale, mkfs, parted, programação, regexp, regulares, script, sed, shell, tutorial, vim
:image: /images/archlogo.png
:slug: automatizando-a-instalacao-do-arch-linux

Enquanto eu escrevia o `Guia de Instalação do Arch Linux`_ percebi que este novo método de instalação possibilitava a criação de um script para automatização do processo.

.. image:: {filename}/images/archlinux-curved2.png
	:align: center
	:target: {filename}/images/archlinux-curved2.png
	:alt: Arch Linux

A automatização da instalação é algo extremamente proveitoso para aqueles que precisam realizar diversas instalações, que gostam de *"fresh installs"*, precisa o Arch Linux repetidas vezes em uma Virtual Machine ou para queles que querem instalar o Arch Linux em um hardwares sem sistemas de entrada e saída.

.. more

Mas Antes Um Aviso e Um Alerta
------------------------------

Antes de tudo é bom alertar que esse script **apaga completamente** os dados do HD (especificado na variável ``HD``) e que ele possui uma pequena limitação: (até o momento) ele só é capaz de realizar a instalação em um único HD, também especificado na variável ``HD``. Para um particionamento diferenciado verifique a sugestão na sessão **Usuários Avançados**.

Ah, e certifíque-se de estar utilizando a nova ISO 2012.08.04. Para mais informações leia `este artigo`_.

Entendendo o Script
-------------------

Basicamente eu fiz uma automação do processo de instalação usando ferramentas como o sed, algumas expressões regulares bem simplórias e um pariticonador que permite a interface via script (o GNU Parted).

Segue abaixo uma versão simplificada do script (sem verificações de erro e etc) que eu acredito ser bem intuitiva:

.. code-block:: bash

        #!/bin/bash
        # encoding: utf-8

        ##################################################
        #		    Variables 			 #
        ##################################################
        # Computer Name
        HOSTN=Arch-VM

        # Keyboard Layout
        KEYBOARD_LAYOUT=br-abnt2

        # Your language, used for localization purposes
        LANGUAGE=pt_BR

        # Geography Localization. Verify the directory /usr/share/zoneinfo/<Zone>/<SubZone>
        LOCALE=America/Sao_Paulo

        # Root password for the brand new installed system
        ROOT_PASSWD=123456

        ########## Hard Disk Partitioning Variable
        # ANTENTION, this script erases ALL YOU HD DATA (specified bt $HD)
        HD=/dev/sda
        # Boot Partition Size: /boot
        BOOT_SIZE=200
        # Root Partition Size: /
        ROOT_SIZE=10000
        # Swap partition size: /swap
        SWAP_SIZE=2000
        # The /home partition will occupy the remain free space

        # Partitions file system
        BOOT_FS=ext4
        HOME_FS=ext4
        ROOT_FS=ext4

        # Extra packages (not obligatory)
        EXTRA_PKGS='vim'


        ######## Auxiliary variables. THIS SHOULD NOT BE ALTERED
        BOOT_START=1
        BOOT_END=$(($BOOT_START+$BOOT_SIZE))

        SWAP_START=$BOOT_END
        SWAP_END=$(($SWAP_START+$SWAP_SIZE))

        ROOT_START=$SWAP_END
        ROOT_END=$(($ROOT_START+$ROOT_SIZE))

        HOME_START=$ROOT_END

        ##################################################
        #		    Script 			 #
        ##################################################
        # Loads the keyboard layout
        loadkeys $KEYBOARD_LAYOUT

        #### Partitioning
        echo "HD Initialization"
        # Set the partition table to MS-DOS type 
        parted -s $HD mklabel msdos &> /dev/null

        # Remove any older partitions
        parted -s $HD rm 1 &> /dev/null
        parted -s $HD rm 2 &> /dev/null
        parted -s $HD rm 3 &> /dev/null
        parted -s $HD rm 4 &> /dev/null

        # Create boot partition
        echo "Create boot partition"
        parted -s $HD mkpart primary $BOOT_FS $BOOT_START $BOOT_END 1>/dev/null
        parted -s $HD set 1 boot on 1>/dev/null

        # Create swap partition
        echo "Create swap partition"
        parted -s $HD mkpart primary linux-swap $SWAP_START $SWAP_END 1>/dev/null

        # Create root partition
        echo "Create root partition"
        parted -s $HD mkpart primary $ROOT_FS $ROOT_START $ROOT_END 1>/dev/null

        # Create home partition
        echo "Create home partition"
        parted -s -- $HD mkpart primary $HOME_FS $HOME_START -0 1>/dev/null

        # Formats the root, home and boot partition to the specified file system
        echo "Formating boot partition"
        mkfs.$BOOT_FS /dev/sda1 -L Boot 1>/dev/null
        echo "Formating root partition"
        mkfs.$ROOT_FS /dev/sda3 -L Root 1>/dev/null
        echo "Formating home partition"
        mkfs.$HOME_FS /dev/sda4 -L Home 1>/dev/null
        # Initializes the swap
        echo "Formating swap partition"
        mkswap /dev/sda2
        swapon /dev/sda2


        echo "Mounting partitions"
        # mounts the root partition
        mount /dev/sda3 /mnt
        # mounts the boot partition
        mkdir /mnt/boot
        mount /dev/sda1 /mnt/boot
        # mounts the home partition
        mkdir /mnt/home
        mount /dev/sda4 /mnt/home


        #### Installation
        echo "Setting up pacman"
        cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bkp
        sed "s/^Ser/#Ser/" /etc/pacman.d/mirrorlist > /tmp/mirrors
        sed '/Brazil/{n;s/^#//}' /tmp/mirrors > /etc/pacman.d/mirrorlist

        if [ "$(uname -m)" = "x86_64" ]
        then
                cp /etc/pacman.conf /etc/pacman.conf.bkp
                # Adds multilib repository
                sed '/^#\[multilib\]/{s/^#//;n;s/^#//;n;s/^#//}' /etc/pacman.conf > /tmp/pacman
                mv /tmp/pacman /etc/pacman.conf

        fi

        echo "Running pactrap base base-devel"
        pacstrap /mnt base base-devel
        echo "Running pactrap grub-bios $EXTRA_PKGS"
        pacstrap /mnt grub-bios `echo $EXTRA_PKGS`
        echo "Running genfstab"
        genfstab -p /mnt >> /mnt/etc/fstab


        #### Enters in the new system (chroot)
        arch-chroot /mnt << EOF
        # Sets hostname
        echo $HOSTN > /etc/hostname
        cp /etc/hosts /etc/hosts.bkp
        sed 's/localhost$/localhost '$HOSTN'/' /etc/hosts > /tmp/hosts
        mv /tmp/hosts /etc/hosts

        # Configures the keyboard layout
        echo 'KEYMAP='$KEYBOARD_LAYOUT > /etc/vconsole.conf
        echo 'FONT=lat0-16' >> /etc/vconsole.conf
        echo 'FONT_MAP=' >> /etc/vconsole.conf

        # Setup locale.gen
        cp /etc/locale.gen /etc/locale.gen.bkp
        sed 's/^#'$LANGUAGE'/'$LANGUAGE/ /etc/locale.gen > /tmp/locale
        mv /tmp/locale /etc/locale.gen
        locale-gen

        # Setup locale.conf
        export LANG=$LANGUAGE'.utf-8'
        echo 'LANG='$LANGUAGE'.utf-8' > /etc/locale.conf
        echo 'LC_COLLATE=C' >> /etc/locale.conf
        echo 'LC_TIME='$LANGUAGE'.utf-8' >> /etc/locale.conf

        # Setup clock (date and time)
        ln -s /usr/share/zoneinfo/$LOCALE /etc/localtime
        echo $LOCALE > /etc/timezone
        hwclock --systohc --utc

        # Setup the network (DHCP via eth0)
        cp /etc/rc.conf /etc/rc.conf.bkp
        sed 's/^# interface=/interface=eth0/' /etc/rc.conf > /tmp/rc.conf
        mv /tmp/rc.conf /etc/rc.conf

        # Setup initial ramdisk environment
        mkinitcpio -p linux

        # Installs and generates GRUB's settings
        grub-install /dev/sda
        grub-mkconfig -o /boot/grub/grub.cfg

        # Changes the root password
        echo -e $ROOT_PASSWD"\n"$ROOT_PASSWD | passwd
        EOF

        echo "Umounting partitions"
        umount /mnt/{boot,home,}
        reboot

A versão acima eu sugiro que ela seja utilizada apenas para aprendizado pois não realiza nenhuma verificação de erro. Por este motivo escrevi uma versão com um mínimo de verificação:

.. code-block:: bash
        
        #!/bin/bash
        # encoding: utf-8

        ##################################################
        #		    Variaveis 			 #
        ##################################################
        # Nome do Computador
        HOSTN=Arch-VM

        # Localização. Verifique o diretório /usr/share/zoneinfo/<Zone>/<SubZone>
        LOCALE=America/Sao_Paulo

        # Senha de Root do sistema após a instalação
        ROOT_PASSWD=123456

        ########## Variáveis Para Particionamento do Disco
        # ATENÇÃO, este script apaga TODO o conteúdo do disco especificado em $HD.
        HD=/dev/sda
        # Tamanho da Partição Boot: /boot
        BOOT_SIZE=200
        # Tamanho da Partição Root: /
        ROOT_SIZE=10000
        # Tamanho da Partição Swap:
        SWAP_SIZE=2000
        # A partição /home irá ocupar o restante do espaço livre em disco

        # File System das partições
        BOOT_FS=ext4
        HOME_FS=ext4
        ROOT_FS=ext4

        # Pacote extras (não são obrigatórios)
        EXTRA_PKGS='vim'

        ######## Variáveis menos suscetíveis a mudanças
        KEYBOARD_LAYOUT=br-abnt2
        LANGUAGE=pt_BR

        ######## Variáveis auxiliares. NÃO DEVEM SER ALTERADAS
        BOOT_START=1
        BOOT_END=$(($BOOT_START+$BOOT_SIZE))

        SWAP_START=$BOOT_END
        SWAP_END=$(($SWAP_START+$SWAP_SIZE))

        ROOT_START=$SWAP_END
        ROOT_END=$(($ROOT_START+$ROOT_SIZE))

        HOME_START=$ROOT_END

        ##################################################
        #		    functions 			 #
        ##################################################
        function inicializa_hd
        {
                echo "Inicializando o HD"
                # Configura o tipo da tabela de partições (Ignorando erros)
                parted -s $HD mklabel msdos &> /dev/null

                # Remove qualquer partição antiga
                parted -s $HD rm 1 &> /dev/null
                parted -s $HD rm 2 &> /dev/null
                parted -s $HD rm 3 &> /dev/null
                parted -s $HD rm 4 &> /dev/null
        }

        function particiona_hd
        {
                ERR=0
                # Cria partição boot
                echo "Criando partição boot"
                parted -s $HD mkpart primary $BOOT_FS $BOOT_START $BOOT_END 1>/dev/null || ERR=1
                parted -s $HD set 1 boot on 1>/dev/null || ERR=1

                # Cria partição swap
                echo "Criando partição swap"
                parted -s $HD mkpart primary linux-swap $SWAP_START $SWAP_END 1>/dev/null || ERR=1

                # Cria partição root
                echo "Criando partição root"
                parted -s $HD mkpart primary $ROOT_FS $ROOT_START $ROOT_END 1>/dev/null || ERR=1

                # Cria partição home
                echo "Criando partição home"
                parted -s -- $HD mkpart primary $HOME_FS $HOME_START -0 1>/dev/null || ERR=1

                if [[ $ERR -eq 1 ]]; then
                        echo "Erro durante o particionamento"
                        exit 1
                fi
        }

        function cria_fs
        {
                ERR=0
                # Formata partições root, home e boot para o File System especificado
                echo "Formatando partição boot"
                mkfs.$BOOT_FS /dev/sda1 -L Boot 1>/dev/null || ERR=1
                echo "Formatando partição root"
                mkfs.$ROOT_FS /dev/sda3 -L Root 1>/dev/null || ERR=1
                echo "Formatando partição home"
                mkfs.$HOME_FS /dev/sda4 -L Home 1>/dev/null || ERR=1
                # Cria e inicia a swap
                echo "Formatando partição swap"
                mkswap /dev/sda2 || ERR=1
                swapon /dev/sda2 || ERR=1

                if [[ $ERR -eq 1 ]]; then
                        echo "Erro ao criar File Systems"
                        exit 1
                fi
        }

        function monta_particoes
        {
                ERR=0
                echo "Montando partições"
                # Monta partição root
                mount /dev/sda3 /mnt || ERR=1
                # Monta partição boot
                mkdir /mnt/boot || ERR=1
                mount /dev/sda1 /mnt/boot || ERR=1
                # Monta partição home
                mkdir /mnt/home || ERR=1
                mount /dev/sda4 /mnt/home || ERR=1

                if [[ $ERR -eq 1 ]]; then
                        echo "Erro ao criar File Systems"
                        exit 1
                fi
        }

        function configurando_pacman
        {
                echo "Configurando pacman"
                cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bkp
                sed "s/^Ser/#Ser/" /etc/pacman.d/mirrorlist > /tmp/mirrors
                sed '/Brazil/{n;s/^#//}' /tmp/mirrors > /etc/pacman.d/mirrorlist

                if [ "$(uname -m)" = "x86_64" ]
                then
                        cp /etc/pacman.conf /etc/pacman.conf.bkp
                        # Adiciona o Multilib 
                        sed '/^#\[multilib\]/{s/^#//;n;s/^#//;n;s/^#//}' /etc/pacman.conf > /tmp/pacman
                        mv /tmp/pacman /etc/pacman.conf

                fi
        }

        function instalando_sistema
        {
                ERR=0
                echo "Rodando pactrap base base-devel"
                pacstrap /mnt base base-devel || ERR=1
                echo "Rodando pactrap grub-bios $EXTRA_PKGS"
                pacstrap /mnt grub-bios `echo $EXTRA_PKGS` || ERR=1
                echo "Rodando genfstab"
                genfstab -p /mnt >> /mnt/etc/fstab || ERR=1

                if [[ $ERR -eq 1 ]]; then
                        echo "Erro ao instalar sistema"
                        exit 1
                fi
        }

        ##################################################
        #		    Script 			 #
        ##################################################
        # Carrega layout do teclado ABNT2
        loadkeys $KEYBOARD_LAYOUT

        #### Particionamento
        inicializa_hd
        particiona_hd
        cria_fs
        monta_particoes

        #### Instalação
        configurando_pacman
        instalando_sistema

        #### Entra no novo sistema (chroot)
        arch-chroot /mnt << EOF
        # Configura hostname
        echo $HOSTN > /etc/hostname
        cp /etc/hosts /etc/hosts.bkp
        sed 's/localhost$/localhost '$HOSTN'/' /etc/hosts > /tmp/hosts
        mv /tmp/hosts /etc/hosts

        # Configura layout do teclado
        echo 'KEYMAP='$KEYBOARD_LAYOUT > /etc/vconsole.conf
        echo 'FONT=lat0-16' >> /etc/vconsole.conf
        echo 'FONT_MAP=' >> /etc/vconsole.conf

        # Configura locale.gen
        cp /etc/locale.gen /etc/locale.gen.bkp
        sed 's/^#'$LANGUAGE'/'$LANGUAGE/ /etc/locale.gen > /tmp/locale
        mv /tmp/locale /etc/locale.gen
        locale-gen

        # Configura locale.conf
        export LANG=$LANGUAGE'.utf-8'
        echo 'LANG='$LANGUAGE'.utf-8' > /etc/locale.conf
        echo 'LC_COLLATE=C' >> /etc/locale.conf
        echo 'LC_TIME='$LANGUAGE'.utf-8' >> /etc/locale.conf

        # Configura hora
        ln -s /usr/share/zoneinfo/$LOCALE /etc/localtime
        echo $LOCALE > /etc/timezone
        hwclock --systohc --utc

        # Configura rede (DHCP via eth0)
        cp /etc/rc.conf /etc/rc.conf.bkp
        sed 's/^# interface=/interface=eth0/' /etc/rc.conf > /tmp/rc.conf
        mv /tmp/rc.conf /etc/rc.conf

        # Configura ambiente ramdisk inicial
        mkinitcpio -p linux

        # Instala e gera configuração do GRUB Legacy
        grub-install /dev/sda
        grub-mkconfig -o /boot/grub/grub.cfg

        # Altera a senha do usuário root
        echo -e $ROOT_PASSWD"\n"$ROOT_PASSWD | passwd
        EOF

        echo "Umounting partitions"
        umount /mnt/{boot,home,}
        reboot


Adequando o Script
------------------

A primeira seção do script (da linha 8 à 33) deve ser adequada para suas necessidades. As linhas 36 e 37 (referentes à língua do sistema) são passíveis de mudança apenas se você tiver interesse de instalar o sistema em outra língua que não seja o Português do Brasil.

Abaixo alguns detalhes das variáveis que podem ser adequadas.

Configurações Básicas
~~~~~~~~~~~~~~~~~~~~~

Hostname
^^^^^^^^

O ``hostname`` do seu computador é definido na variável ``HOSTN`` e é utilizado para "nomear" a sua estação/servidor. Este valor é utilizado nos arquivos de configuração ``/etc/hostname`` e ``/etc/hosts``

Região
^^^^^^

É importante adequar a variável ``LOCALE`` pois ela define a sua região (zona e sub-zona), e consequentemente o seu fuso horário. Para verificar todas as regiões suportadas consulte o diretório ``/usr/share/zoneinfo/<Zone>/<SubZone>``.

Pacotes Adicionais
^^^^^^^^^^^^^^^^^^

A variável ``EXTRA_PKGS`` define os pacotes adicionais (além dos pacotes ``base``, ``base-devel`` e ``grub-bios``) que serão instalados no sistema, você pode definir diversos pacotes como:

::

    EXTRA_PKGS='vim git subversion'

Senha do Usuário Root
^^^^^^^^^^^^^^^^^^^^^

A variável ``ROOT_PASSWD`` define a senha de root que será configurada no seu novo sistema, é imprescindível que esse valor seja alterado.

Configurações de Particionamento e Formatação
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Identificado do Disco Rígido
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Também é imprescindível a adequação do identificador do disco rígido definido pela variável ``HD``. Esta variável define qual HD será particionado e formatado.

Tamanho das Partições
^^^^^^^^^^^^^^^^^^^^^

Neste script é utilizado as partições recomendadas (boot, swap, root e home). Para definir o tamanho (em Mega Bytes) das 3 primeiras partições altere as seguitnes variáveis: ``BOOT_SIZE``, ``SWAP_SIZE`` e ``ROOT_SIZE``. O script utilizará todo o espaço livre restante para a partição home.

File System das Partições
^^^^^^^^^^^^^^^^^^^^^^^^^

Para definir o file system das partições swap, root e home altere as variáveis ``BOOT_FS``, ``HOME_FS`` e ``ROOT_FS``. Estas variáveis são utilizadas como complemento para o comando ``mkfs``, desta forma são suportados os seguintes file systems:

-  ``bfs``
-  ``btfs``
-  ``cramfs``
-  ``ext2``
-  ``ext3``
-  ``ext4``
-  ``ext4dev``
-  ``jfs``
-  ``minix``
-  ``msdos``
-  ``nilfs2``
-  ``ntfs``
-  ``reiserfs``
-  ``vfat``
-  ``xfs``

Utilizando o Script
-------------------

Para utilizar o script acima basta dar boot em sua máquina com o ISO do Arch Linux e emitir os seguintes comandos:

.. code-block:: bash

    $ curl https://gist.github.com/gists/3320266/download | tar xvz
    $ mv gist*/*.sh .
    $ chmod 777 arch-install.sh

Em seguida edite as variáveis do script conforme instruído anteriormente e ao final da adequação execute o script:

.. code-block:: bash

    $ ./arch-install.sh

Agora recline-se em sua cadeira e assista as letrinhas passarem!

Usuários Avançados
------------------

Conforme destacado pelo leitor Vítor, os usuários avançados que queiram usar um particionamento mais "incrementado" basta ignorar os ajustes nas variáveis de HD, particionamento e FileSystem, comentar as linhas 173 a 176 e montar todo o sistema de arquivos em ``/mnt`` (por exemplo ``/mnt/home`` e ``/mnt/boot``) e executar o sctipt normalmente. Desta forma o script irá apenas instalar os pacotes necessários, o GRUB e realizar as configurações necessárias.

Futuro
------

É verdade, me diverti muito fazendo esse script, por isso estou considerando a possibildiade de ampliá-lo e criar uma interface amigavel. Quem sabe fazer um substituto do AIF?! Quem tiver interessado em colaborar é só avisar :D

.. _Guia de Instalação do Arch Linux: /pt/instalando-o-arch-linux-iso-20120804/
.. _este artigo: /pt/instalando-o-arch-linux-iso-20120804/
