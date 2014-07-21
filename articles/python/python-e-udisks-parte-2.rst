Python e UDisks - Parte 2
#########################
:date: 2011-03-30 16:37
:category: Python
:tags: dbus, devicekit, luks, python, sistema de arquivos, udisks
:image: /images/Python_logo.png
:series: Python e UDisks
:description: Nesta segunda parte vamos explorar a Interface de Disks e Devices.

.. role:: strike

Há alguns posts eu mostrei como listar todos os dispositivos de armazenamento conectados ao seu PC usando Python e UDisks. Neste post irei mostrar como trabalhar com a interface Disks do DeviceKit.

.. image:: {filename}/images/python.png
        :align: center
        :alt: Python Logo

Primeiramente vamor ler algumas documentações! A documentação do UDisks é dividida em cinco sessões:

.. more

-  Interface Disks;
-  Interface Device;
-  Interface Adapter;
-  Interface Expander;
-  Interface Port.

Nesta série de posts irei dar foco somente às duas primeira sessões, pois elas fornecem mais informações e consequentemente são as mais úteis. Neste post irei focar na interface Disks o qual provê: informações sobre o próprio UDisks e métodos para listar os dispositivos;

Como esse assunto é escasso na internet, utilizei como alguns testes da `suite de testes do UDisks`_ para entender como utilizar algumas funcionalidades.

Primeiro:
    Sempre verifique a versão do daemon;
Segundo:
    Assegure-se que o daemon não esteja inibido durante a inicialização
    do seu aplicativo;
Terceiro:
    Se sua aplicação for utilizar o `LUKS`_, verifique se ele é
    suportado;
Quarto:
    É importante ter certeza que o sistema de arquivos que você irá
    tratar é suportado pelo daemon. Além disso, assegure-se que a
    operação que você pretende executar é suportada no sistema de
    arquivo desejado. O trecho de código abaixo reúne algumas
    informações e a imprime de uma maneira organizada. É altamente
    recomendado realizar verificações antes de algumas tarefas como,
    criar um sistema de arquivos, montar volume, desmontar volume e etc.

Mais informações sobre as propriedades apresentadas :strike:`podem ser encontradas aqui` podiam ser encontradas na antiga documentação que não está mais online.

.. code-block:: python

    >>> # Written by Magnun Leno. License: GPLv3
    >>> import dbus
    >>>
    >>> bus = dbus.SystemBus()
    >>> proxy = bus.get_object("org.freedesktop.UDisks", "/org/freedesktop/UDisks")
    >>> iface = dbus.Interface(proxy, "org.freedesktop.UDisks")
    >>>
    >>> print "Daemon Version",proxy.Get('org.freedesktop.UDisks', 'DaemonVersion')
    Daemon Version 1.0.2
    >>>
    >>> print "Daemon is Inhibited",proxy.Get('org.freedesktop.UDisks', 'daemon-is-inhibited')
    Daemon is Inhibited 0
    >>>
    >>> print "Support LUKS",proxy.Get('org.freedesktop.UDisks', 'supports-luks-devices')
    Support LUKS 1
    >>>
    >>> formatting = '''id: %s;
    ... name: %s;
    ... supports_unix_owners: %s;
    ... can_mount: %s;
    ... can_create: %s;
    ... max_label_len: %s;
    ... supports_label_rename: %s;
    ... supports_online_label_rename: %s;
    ... supports_fsck: %s;
    ... supports_online_fsck: %s;
    ... supports_resize_enlarge: %s;
    ... supports_online_resize_enlarge: %s;
    ... supports_resize_shrink: %s;
    ... supports_online_resize_shrink: %s;n'''
    >>>
    >>>
    >>> for fs_info in proxy.Get('', 'KnownFilesystems'):
    ...     print formatting%tuple(fs_info)
    ...
    id: vfat;
    name: FAT;
    supports_unix_owners: 0;
    can_mount: 1;
    can_create: 1;
    max_label_len: 254;
    supports_label_rename: 1;
    supports_online_label_rename: 0;
    supports_fsck: 1;
    supports_online_fsck: 0;
    supports_resize_enlarge: 0;
    supports_online_resize_enlarge: 0;
    supports_resize_shrink: 0;
    supports_online_resize_shrink: 0;

    id: ext2;
    name: Linux Ext2;
    supports_unix_owners: 1;
    can_mount: 1;
    can_create: 1;
    max_label_len: 16;
    supports_label_rename: 1;
    supports_online_label_rename: 1;
    supports_fsck: 1;
    supports_online_fsck: 0;
    supports_resize_enlarge: 1;
    supports_online_resize_enlarge: 1;
    supports_resize_shrink: 1;
    supports_online_resize_shrink: 1;

Parte da saída desse código foi omitido. Atualmente, são suportados 9 sistemas de arquivos: FAT, Linux Ext2, Linux Ext3, Linux Ext4, XFS, ReiserFS, Minix, NTFS and Swap Space. Um pequeno detalhe: FAT inclui FAT16 and FAT32.

No próximo post iremos ver como encontrar e listar alguns ou todos os dispositivos.

.. _suite de testes do UDisks: http://cgit.freedesktop.org/udisks/tree/tests/run?h=gdbus-port&=switch
.. _LUKS: http://en.wikipedia.org/wiki/Linux_Unified_Key_Setup
