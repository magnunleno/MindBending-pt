Python e UDisks - Parte 5
#########################
:date: 2011-07-05 18:01
:category: Python
:tags: dbus, python, udisks, usb, usbmanager
:image: /images/Python_logo.png
:series: Python e UDisks
:description: Retomando a séries de artigos sobre Python e UDisks, veremos como algumas partes da interface desta API foram modificadas.

Ressuscitando a série de artigos sobre `Python e Udisks`_ hoje vou mostrar como obter mais informações dos dispositivos através das propriedades.

.. image:: {filename}/images/python.png
        :target: {filename}/images/python.png
        :align: center
        :alt: Python Logo

Sobre o Atraso
--------------

Antes de tudo, peço desculpas pela demora em postar essa continuação, ela foi mais difícil de escrever do que parece. Essa demora se deve à mudança da forma como o DBus se comunica com o UDisks. Como tudo ainda é muito novo e não há um documentação completa e tão pouco tutoriais na internet, minhas buscas pela linha de erro não retornavam nenhum resultado. Abaixo está o código que eu estava utilizando e o erro que o DBus me apresentava:

.. more

.. code-block:: python
    :linenos: table

    >>> import dbus
    >>>
    >>> bus = dbus.SystemBus()
    >>> proxy = bus.get_object("org.freedesktop.UDisks",
    ...    "/org/freedesktop/UDisks")
    ...
    >>> iface = dbus.Interface(proxy, "org.freedesktop.UDisks")
    >>>
    >>> devs = iface.EnumerateDevices()
    >>> print devs
    >>>
    >>> device = devs[14]
    >>> volume_obj = bus.get_object("org.freedesktop.UDisks", device)
    >>> volume = dbus.Interface(volume_obj, "org.freedesktop.UDisks.Device")
    >>> volume_obj.Get('','DriveConnectionInterface')
    dbus.exceptions.DBusException: org.freedesktop.DBus.Error.AccessDenied:
    Rejected send message, 4 matched rules; type="method_call", sender=":1.60"
    (uid=1000 pid=19165 comm="/usr/bin/python2 ./test-me ") interface="(unset)"
    member="Get" error name="(unset)" requested_reply="0" destination=":1.19"
    (uid=0 pid=1010 comm="/usr/lib/udisks/udisks-daemon ")

.. role:: strike

Após dias de pesquisas e tentativas frustradas resolvi fazer algo que muitos evitam: ler código fonte de outros projetos. Depois de algumas pesquisas acabei encontrando o projeto `liveusb-creator`_ que utiliza o UDisks e o DBus para detectar dispositivos removíveis. Minha solução estava no arquivo ``creator.py`` (mais especificamente no método ``handle_reply``, linhas 445 a 450) :strike:`disponível aqui`.

Vamos ao Código
---------------

Esclarecido o problema, vamos mostrar a solução. Nossa intenção é obter informações a respeito de um pendrive, ou qualquer dispositivo de armazenamento removível, conectado ao nosso computador, para isso vamos testar se o dispositivo de armazenamento utiliza como interface de comunicação o USB. Veja o código abaixo:

.. code-block:: python
    :linenos: table

    >>> import dbus
    >>>
    >>> bus = dbus.SystemBus()
    >>> proxy = bus.get_object("org.freedesktop.UDisks",
    ...     "/org/freedesktop/UDisks")
    ...
    >>> iface = dbus.Interface(proxy, "org.freedesktop.UDisks")
    >>>
    >>> devs = iface.EnumerateDevices()
    >>>
    >>> dev_obj = bus.get_object("org.freedesktop.UDisks", devs[0])
    >>> type(dev_obj)
    <class 'dbus.proxies.ProxyObject'>
    >>>
    >>> dev = dbus.Interface(dev_obj, "org.freedesktop.DBus.Properties")
    >>> type(dev_obj)
    <class 'dbus.proxies.Interface'>
    >>> print dev.Get('', 'DriveConnectionInterface')
    ata

Como podem ver, das linhas 1 até a linha 8 não há nenhuma novidade. Toda a "mágica" é feita nas linhas 09 até a 17:

-  Linha 09 - Obtemos um objeto do tipo ProxyObject utilizando o método
   ``bus.get_object``;
-  Linha 10 - Utilizamos o comando ``type`` para mostrar o tipo
   retornado;
-  Linha 13 - "Solicitarmos" uma interface utilizando o método
   ``dbus.Interface`` e passamos como parêntese o ProxyObject obtido na
   linha 09;
-  Linha 14 - Utilizamos o comando ``type`` para mostrar o tipo
   retornado;
-  Linha 16 - Utilizamos o método ``Get`` disponível no tipo Interface
   para solicitarmos a propriedade ``DriveConenctionInterface``;

Como podemos ver na última linha de código, esse dispositivo utiliza a interface 'ata' para comunicação com o sistema, logo não é um dispositivo removível. Como estamos interessados somente nos dispositivos que se conectam via USB vamos iterar sobre o vetor de dispositivos ``devs`` e testar se a propriedade ``DriveConenctionInterface`` é igual a 'usb':

.. code-block:: python
    :linenos: table

    >>> for dev in devs:
    ...     dev_obj = bus.get_object("org.freedesktop.UDisks", dev)
    ...     dev = dbus.Interface(dev_obj, "org.freedesktop.DBus.Properties")
    ...     if str(dev.Get('', 'DriveConnectionInterface')) == 'usb':
    ...         nome = str(dev.Get('', 'DeviceFile'))
    ...         print 'Dispositivo de armazenamento: ' + nome
    Dispositivo de armazenamento: /dev/sdd
    Dispositivo de armazenamento: /dev/sdd1

Note que utilizei a propriedade ``DeviceFile`` para retornar o caminho completo do dispositivo de bloco.

Dispositivos Repetidos
----------------------

Como pode ser visto na iteração sobre o vetor ``devs`` ele encontrou os dispositivos /dev/sdd e /dev/sdd1, mas ambos são o mesmo dispositivo físico. No `artigo anterior`_ eu comentei sobre esse fato, para evitá-lo basta testar, antes de emitir qualquer sinalização se o dispositivo é uma tabela de partição (é o caso de /dev/sdd):

.. code-block:: python
    :linenos: table

    >>> for dev in devs:
    ...     dev_obj = bus.get_object("org.freedesktop.UDisks", dev)
    ...     dev = dbus.Interface(dev_obj, "org.freedesktop.DBus.Properties")
    ...     if bool(dev.Get('', 'DeviceIsPartitionTable')):
    ...         continue
    ...     if str(dev.Get('', 'DriveConnectionInterface')) == 'usb':
    ...         nome = str(dev.Get('', 'DeviceFile'))
    ...         print 'Dispositivo de armazenamento: ' + nome
    Dispositivo de armazenamento: /dev/sdd1

Pronto, assim conseguimos distinguir e selecionar somente os dispositivos que realmente nos interessa.

Quais Propriedades Existem?
---------------------------

Na seção Properties da documentação oficial do UDisks há uma lista completa de todas as propriedades e uma breve explanação sobre cada uma delas.

Para simplificar um pouco o trabalho existe também o método GetAll que retorna um dicionário com todas as propriedades e seus respectivos valores. Ele pode ser utilizado da seguinte forma (parte da saída será omitida):

.. code-block:: python
    :linenos: table

    >>> dev_obj = bus.get_object("org.freedesktop.UDisks", devs[15])
    >>> dev = dbus.Interface(dev_obj, "org.freedesktop.DBus.Properties")
    >>> dados = dev.GetAll('')
    >>> for i in dados: print i+': '+str(dados[i])
    ...
    DeviceIsMounted: 1
    LinuxLvm2PVNumMetadataAreas: 0
    LinuxLvm2LVGroupUuid:
    LinuxLoopFilename:
    LinuxDmmpComponentHolder: /
    DeviceIsPartitionTable: 0
    (...)
    DriveVendor: Kingston
    (...)
    IdLabel: MAGNUN
    (...)
    IdVersion: FAT32
    DriveSerial: 001CC0EC34C8F071A645131E
    (...)
    DeviceSize: 16011330048
    (...)
    DriveModel: DataTraveler G3
    (...)
    DriveConnectionInterface: usb
    DriveRevision: 1.00
    LinuxLvm2LVGroupName:
    PartitionType: 0x0b
    PartitionSize: 16011330048
    (...)
    DriveConnectionSpeed: 480000000
    (...)

No próximo artigo mostrarei como chamar alguns dos métodos apresentados na documentação do Udisks.

Até lá...

.. _Python e Udisks: /pt/series/python-e-udisks/
.. _|image1|: {filename}/images/python.png
.. _liveusb-creator: https://fedorahosted.org/liveusb-creator/
.. _artigo anterior: /pt/python-e-udisks-parte-4/

