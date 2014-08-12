Python e UDisks - Parte 4
#########################
:date: 2011-05-23 15:53
:category: Python
:tags: dbus, gobject, python, sinais, udisks, usbmanager
:image: /images/Python_logo.png
:series: Python e UDisks
:description: Na quarta parte deste tutorial de exploração da biblioteca UDisks serão apresentadas formas de monitorar a insersão e remoção de dispositivos e como reagir a estes sinais.

Nos já vimos, como conectar ao DBus e o UDisks, em seguida vimos como verificar algumas configurações e informações do daemon do UDisks e também como buscar por dispositivos conectados. Tudo isso não é muito "usável" se você não souber quando uma novo dispositivo foi conectado ao seu computador. Claro que você pode ficar testando periodicamente se algum dispositivo foi adicionado, mas esta não é uma solução muito elegante. Para uma detecção de dispositivos "em tempo real" nos utilizamos sinais.

.. image:: {filename}/images/python.png
        :target: {filename}/images/python.png
        :align: center
        :alt: Python Logo

Existem diversos sinais especificados no Udisks, mas os mais úteis (para o nosso caso) são:

.. more

-  O sinal DeviceAdded - Emitido sempre que um dispositivo é adicionado.
-  O sinal DeviceRemoved - Emitido quando um dispositivo é removido.
-  O sinal DeviceChanged - Emitido sempre que a propriedade de um dispositivo é alterada.

Essas descrições foram tiradas do Manual de Referência do UDisks (que não está mais online).

Mas antes de seguirmos adiante, o que são sinais? Sinais são chamadas assíncronas, de uma forma simples podemos dizer que são "eventos". Com a utilização de chamadas assíncronas nosso programa pode realizar operações e processamentos e ser "interrompido" quando um evento ocorrer. Vinculado a esse evento está uma função de tratamento (handler).

Agora vamos ver um trecho de código Python que mostra como lidar com esses sinais.

.. code-block:: python

    >>> import dbus #Importa módulos necessários
    >>> import gobject
    >>> from dbus.mainloop.glib import DBusGMainLoop
    >>>
    >>> DBusGMainLoop(set_as_default=True) #Informa a utilização de um main loop
    >>>
    >>> bus = dbus.SystemBus()  #Inicia o DBus
    >>> proxy = bus.get_object("org.freedesktop.UDisks", "/org/freedesktop/UDisks")
    >>> iface = dbus.Interface(proxy, "org.freedesktop.UDisks")
    >>>
    >>> def on_device_add(dev_path):
    ...  '''Handler para o evento DeviceAdded'''
    ...  print 'Adicionado:',dev_path
    ...
    >>> def on_device_changed(dev_path):
    ...  '''Handler para o evento DeviceChanged'''
     ...  print 'Modificado:',dev_path
    ...
    >>> def on_device_removed(dev_path):
    ...  '''Handler para o evento DeviceRemoved'''
    ...  print 'Removido:',dev_path
    ...
    >>>
    >>> iface.connect_to_signal('DeviceAdded', on_device_add) < at 9cb8b0c "type='signal',sender=':1.38',path='/org/freedesktop/UDisks',interface='org.freedesktop.UDisks',member='DeviceAdded'" on conn >
    >>> iface.connect_to_signal('DeviceChanged', on_device_changed) < at 9cb8c2c "type='signal',sender=':1.38',path='/org/freedesktop/UDisks',interface='org.freedesktop.UDisks',member='DeviceChanged'" on conn >
    >>> iface.connect_to_signal('DeviceRemoved', on_device_removed) < at 9cb8cec "type='signal',sender=':1.38',path='/org/freedesktop/UDisks',interface='org.freedesktop.UDisks',member='DeviceRemoved'" on conn >
    >>>
    >>> loop = gobject.MainLoop()
    >>> loop.run() #loop infinito

    Adicionado: /org/freedesktop/UDisks/devices/sdc
    Adicionado: /org/freedesktop/UDisks/devices/sdc1
    Modificado: /org/freedesktop/UDisks/devices/sdc1
    Modificado: /org/freedesktop/UDisks/devices/sdc1
    Modificado: /org/freedesktop/UDisks/devices/sdc
    Removido: /org/freedesktop/UDisks/devices/sdc1
    Removido: /org/freedesktop/UDisks/devices/sdc

As linhas 24, 26 e 28 são responsáveis por conectar o "evento" do sinal à função de tratamento do evento (event handler).

Após a linha ``loop.run()``, o programa parece que está "suspenso", mas está apenas aguardando a ocorrência de algum sinal. Após isso, eu inseri uma pen drive, e ela foi montada automaticamente. Em seguida eu a desmontei e a removi. Olhando rapidamente (pelo menos se você estiver olhando a saída estática acima) temos a impressão de que estão sendo geradas outputs duplicadas. Mas isso tem uma boa explicação...

-  As primeiras duas linhas notificam que um novo "root device" (tabela de partição) foi detectado (sdc), em seguida a "nova partição" (sdc1) foi detectada. Se sua pendrive tivesse mais partições teríamos mais outputs.
-  A terceira linha notifica que a partição sdc1 foi montada.
-  A quarta, quinta e sexta linha notifica que o dispositivo foi
   desmontado (ambas as partições) e a partição "removida".
-  E a última linha notifica que o dispositivo foi realmente removido.

Agora tudo parece mais claro, não? Então, quando buscamos por novos dispositivos é interessante filtrar essas notificações e manter somente as que são relevantes. Isso será feito buscando informações sobre o dispositivo. Eu irei mostrar como fazer isso no próximo post, até lá...

