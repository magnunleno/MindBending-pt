Python e UDisks – Parte 3
#########################
:date: 2011-04-25 13:32
:category: Python
:tags: dbus, dispositivos, python udisks
:image: /images/Python_logo.png
:series: Python e UDisks
:description: Nesta continuação vamos aprender a utilizar alguns métodos para listagem de Devices e Files.

No último post desta série eu mostrei como obter algumas informações úteis sobre o daemon UDisks, agora vamos ver como buscar dispositivos com ele.

O primeiro método que iremos ver é o EnumerateDevices:

.. code-block:: python
    
    >>>
    >>> bus = dbus.SystemBus()
    >>> proxy = bus.get_object("org.freedesktop.UDisks",
    ...     "/org/freedesktop/UDisks")
    ...
    >>> iface = dbus.Interface(proxy, "org.freedesktop.UDisks")
    >>>
    >>> devs = iface.EnumerateDevices()
    >>> print devs
    dbus.Array([dbus.ObjectPath('/org/freedesktop/UDisks/devices/fd0'),
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdb'),
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sr0'),
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sda1'),
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sda2'),
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdc1'),
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdb1'),
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sda'),
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdb3'),
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdc'),
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdb2')],
    signature=dbus.Signature('o'))
    >>> devs[0]
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/fd0')
    >>> type(devs[0])
    <type 'dbus.ObjectPath'>
    >>> dir(devs[0])
    ['__add__', '__class__', '__contains__', '__delattr__', '__doc__',
    '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
    '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__',
    '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
    '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
    '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center',
    'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format',
    'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle',
    'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace',
    'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
    'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
    'upper', 'zfill']
    >>>

.. more

O método EnumerateDevices é usado para listar todos os dispositivos de armazenamento conectados ao seu PC. Ele não precisa de nenhum argumento e retorna uma lista contendo objetos do tipo. De acordo com a `documentação do DBus`_ um ObjectPath se comporta exatamente como uma string e não possui nenhuma utilidade além de identificar únicamente um objeto. Com a saída do comando :code:`dir(devs[0])` é possível visualizar que ele é uima mera string. O valor do :code:`ObjectPath` será útil para obtermos um volume object e/ou um volume interface, veremos como fazer isso em breve.

O próximo método é o :code:`EnumerateDeviceFiles`, o qual lista todos os "device files" (incluindo symlinks):

.. code-block:: python

    >>> for i in iface.EnumerateDeviceFiles(): print i
    ...
    /dev/fd0
    /dev/sdb
    /dev/disk/by-id/ata-SAMSUNG_HD161GJ_S14DJA0Z108748
    /dev/disk/by-id/scsi-SATA_SAMSUNG_HD161GJS14DJA0Z108748
    /dev/disk/by-id/wwn-0x50024e9201d01d37
    /dev/disk/by-path/pci-0000:00:1f.5-scsi-1:0:0:0
    /dev/sr0
    /dev/disk/by-path/pci-0000:00:1f.5-scsi-0:0:0:0
    /dev/sda1
    /dev/disk/by-id/ata-MAXTOR_STM31000340AS_9QJ3JDHV-part1
    /dev/disk/by-id/scsi-SATA_MAXTOR_STM31000_9QJ3JDHV-part1
    /dev/disk/by-id/wwn-0x5000c500113ce6fc-part1
    /dev/disk/by-uuid/659c06c3-9b37-4be3-915b-545998d37f7a
    /dev/disk/by-path/pci-0000:00:1f.2-scsi-0:0:0:0-part1
    /dev/sda2
    /dev/disk/by-id/ata-MAXTOR_STM31000340AS_9QJ3JDHV-part2
    /dev/disk/by-id/scsi-SATA_MAXTOR_STM31000_9QJ3JDHV-part2
    /dev/disk/by-id/wwn-0x5000c500113ce6fc-part2
    /dev/disk/by-uuid/eba43f19-65f0-45e0-b24e-68db4b3fbe19
    /dev/disk/by-path/pci-0000:00:1f.2-scsi-0:0:0:0-part2
    /dev/sdc1
    /dev/disk/by-id/usb-Kingston_DataTraveler_2.0_5B7616A2C81C-0:0-part1
    /dev/disk/by-uuid/48D5-32CD
    /dev/disk/by-path/pci-0000:00:1d.7-usb-0:3:1.0-scsi-0:0:0:0-part1

Um trecho dessa saída foi omitida.

Outro método muito útil é o :code:`EnumerateDeviceByDeviceFile`, o qual encontra o ObjectPath de um sipositivo baseado em um arquivo:

.. code-block:: python

    >>> iface.FindDeviceByDeviceFile('/dev/sda1')
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sda1')
    >>> iface.FindDeviceByDeviceFile('/dev/disk/by-uuid/48D5-32CD')
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdc1')
    >>> iface.FindDeviceByDeviceFile('/error/error')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/usr/lib/pymodules/python2.6/dbus/proxies.py", line 140, in __call__
    **keywords)
    File "/usr/lib/pymodules/python2.6/dbus/connection.py", line 620, in
    call_blocking message, timeout)
    dbus.exceptions.DBusException: org.freedesktop.UDisks.Error.Failed: No such
    device
    >>>

Conforme visto acima, esse método retorna um erro do tipo :code:`DBus Exception` caso o arquivo não se refira a um dispositivo válido.

Por último (e o mais complicado) é o :code:`FindDeviceByMajorMinor`. Ele usa os números major e minor (mais informações sobre isso `aqui`_) de um dispositido para retornar um :code:`ObjectPath`:

.. code-block:: python

    >>> import os
    >>> info = os.stat('/dev/sda1')
    >>> iface.FindDeviceByMajorMinor(os.major(info.st_rdev),
    ... os.minor(info.st_rdev))
    ...
    dbus.ObjectPath('/org/freedesktop/UDisks/devices/sda1')
    >>>

Existem outros métodos nesta interface mas estas são as mais úteis para programas comums. Para todas as restantes basta uma olhada na documentação (que não está mais online).

.. _documentação do DBus: http://dbus.freedesktop.org/doc/dbus-python/api/dbus.ObjectPath-class.html
.. _aqui: http://uw714doc.sco.com/en/HDK_concepts/ddT_majmin.html
