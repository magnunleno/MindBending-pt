Python e UDisks - Parte 1
#########################
:date: 2011-03-14 12:27
:category: Python
:tags: dbus, devicekit, dispositivos, hal, python, udev, udisks, usb
:image: /images/Python_logo.png
:series: Python e UDisks
:description: Dando início a uma nova série de artigos sobre desenvolvimento Python.

Recentemente recebi diversos contatos de pessoas querendo saber se o USBManager iria suportar ou não o DeviceKit/UDev, uma vez que o `HAL foi oficialmente descontinuado`_, então acabei retomando o desenvolvimento desse aplicativo.

.. image:: {filename}/images/python.png
        :align: center
        :alt: Python Logo

Acabei percebendo algumas diferenças e pouca referência na internet, por isso vou postar algumas informações a respeito do desenvolvimento usando o DBus e o DeviceKit para trabalhar com dispositivos de armazenamento via USB.

.. more

Há algum tempo, fiz uma pesquisa sobre Python e o DeviceKit e encontrei esse post: `Accessing DeviceKit with DBus and Python`_. Eu havia feito alguns testes e o código funcionou perfeitamente. Escrevi algumas linhas a mais e guardei para mexer em um outro dia. Depois de muito tempo (e uma atualização de distribuição) resolvi mexer novamente no USBManager e percebi que o trecho de código não funciona mais:

.. code-block:: python

    >>> import dbus
    >>>
    >>> bus = dbus.SystemBus()
    >>>
    >>> proxy = bus.get_object("org.freedesktop.DeviceKit.Disks", "/org/freedesktop/DeviceKit/Disks")
    Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
    File "/usr/lib/pymodules/python2.6/dbus/bus.py", line 244, in get_object
    follow_name_owner_changes=follow_name_owner_changes)
    File "/usr/lib/pymodules/python2.6/dbus/proxies.py", line 241, in __init__
    self._named_service = conn.activate_name_owner(bus_name)
    File "/usr/lib/pymodules/python2.6/dbus/bus.py", line 183, in activate_name_owner
    self.start_service_by_name(bus_name)
    File "/usr/lib/pymodules/python2.6/dbus/bus.py", line 281, in start_service_by_name
    'su', (bus_name, flags)))
    File "/usr/lib/pymodules/python2.6/dbus/connection.py", line 620, in call_blocking
    message, timeout)
    dbus.exceptions.DBusException: org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.DeviceKit.Disks was not provided by any .service files
    >>>

Ao verificar no caminho onde são armazenados os serviços constatei que
realmente esse serviço não existia:

.. code-block:: bash

    $ ls /etc/dbus-1/system.d/ | grep freedesktop
    org.freedesktop.ModemManager.conf
    org.freedesktop.PolicyKit1.conf
    org.freedesktop.RealtimeKit1.conf
    org.freedesktop.SystemToolsBackends.conf
    org.freedesktop.UDisks.conf
    org.freedesktop.UPower.conf

De acordo com o `anúncio do udisks 1.0.0`_ o System Bus Name
org.freedesktop.DeviceKit.Disks foi substituído por
org.freedesktop.UDisks. Com isso já conseguimos listar tidos os
dispositivos de armazenamento ligados ao nosso computador:

.. code-block:: python

    >>> import dbus
    >>>
    >>> bus = dbus.SystemBus()
    >>> proxy = bus.get_object("org.freedesktop.UDisks", "/org/freedesktop/UDisks")
    >>> iface = dbus.Interface(proxy, "org.freedesktop.UDisks")
    >>> print iface.EnumerateDevices()
    dbus.Array([dbus.ObjectPath('/org/freedesktop/UDisks/devices/fd0'), dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdc'), dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdb'), dbus.ObjectPath('/org/freedesktop/UDisks/devices/sr0'), dbus.ObjectPath('/org/freedesktop/UDisks/devices/sda1'), dbus.ObjectPath('/org/freedesktop/UDisks/devices/sda2'), dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdb1'), dbus.ObjectPath('/org/freedesktop/UDisks/devices/sda'), dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdb2'), dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdc1'), dbus.ObjectPath('/org/freedesktop/UDisks/devices/sdb3')], signature=dbus.Signature('o'))
    >>>
    >>> for i in iface.EnumerateDevices(): print i
    ...
    /org/freedesktop/UDisks/devices/fd0
    /org/freedesktop/UDisks/devices/sdc
    /org/freedesktop/UDisks/devices/sdb
    /org/freedesktop/UDisks/devices/sr0
    /org/freedesktop/UDisks/devices/sda1
    /org/freedesktop/UDisks/devices/sda2
    /org/freedesktop/UDisks/devices/sdb1
    /org/freedesktop/UDisks/devices/sda
    /org/freedesktop/UDisks/devices/sdb2
    /org/freedesktop/UDisks/devices/sdc1
    /org/freedesktop/UDisks/devices/sdb3
    >>>

Isso já é um bom começo! No próximo post vamos ver como listar as
propriedades dos dispositivos. Até mais...

.. _HAL foi oficialmente descontinuado: http://en.wikipedia.org/wiki/HAL_%28software%29
.. _Accessing DeviceKit with DBus and Python: http://moserei.de/2010/01/08/accessing-devicekit-with-dbus-and-python.html
.. _anúncio do udisks 1.0.0: http://lists.freedesktop.org/archives/devkit-devel/2010-March/000758.html
