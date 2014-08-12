Dobrando o Gnome Keyring Com o Python – Parte 4
###############################################
:date: 2011-01-24 17:55
:category: Python
:tags: bending, gnome, keyring, passwords, python, seahorse, ssh, store, tiamat, tutorial, username
:description: Uma breve análise sobre a segurança do Gnome Keyring e aplicações Python.
:image: /images/gkeyring.png
:series: Dobrando o Gnome Keyring Com o Python

.. default-role:: code

Mantendo o assunto `anterior </pt/dobrando-o-gnome-keyring-com-o-python-parte-3/>`_, hoje vou escrever um pouco sobre a segurança do Gnome Keyring. Conforme apresentado no último post o Gnome Keyring é responsável por armazenar informações sensíveis em bases de dados encriptadas chamadas keyrings. Eu mostrei como criar um Keyring e armazenar alguns dados. Mas agora eu pergunto, essas informações estão seguras? Elas podem ou não estar, depende de você.

.. image:: {filename}/images/gkeyring.png
    :align: center
    :target: {filename}/images/gkeyring.png
    :alt: Gnome Keyring

Existe uma discussão recorrente sobre o comportamento do Gnome Keyring.
Quando fazemos log-on, o Gerenciado de Sessão "destranca" o chaveiro
padrão com sua senha de logon para evitar muitos popups perguntando se
você quer permitir que uma certa aplicação acesse o Gnome Keyring.
Muitas pessoas encaram isso como uma falha de segurança, Eu não concordo
totalmente. O Gnome Keyring também utiliza o nome da aplicação para
confirmar as permissões. Vamos ver um exemplo, vou supor que estamos
desenvolvendo uma certa aplicação chamada *MyApp* e que ela irá criar um
chaveiro simples. O trecho de código a seguir cuida disso:

.. more

.. code-block:: python

    import gnomekeyring as gk
    import glib

    APP_NAME = 'MyApp'
    KEYRING_NAME = 'MyKeyring'

    glib.set_application_name(APP_NAME)

    keyrings = gk.list_keyring_names_sync()

    # If this keyring already exist, let's remove it
    if KEYRING_NAME in keyrings:
        # Gnome Keyring Daemon may ask for a password here
        gk.delete_sync(KEYRING_NAME)

    # If anyone asks, the password is 'mypasswd'
    gk.create_sync(KEYRING_NAME, 'mypasswd')

    id = gk.item_create_sync(KEYRING_NAME, gk.ITEM_GENERIC_SECRET, 
        'magnun@Neptune:22', {'application':APP_NAME}, 'passwd', True)
    print 'New host added (key=%i)'%(key)

    id = gk.item_create_sync(KEYRING_NAME, gk.ITEM_GENERIC_SECRET, 
        'guest@Neptune:22', {'application':APP_NAME}, 'passwd', True)
    print 'New host added (key=%i)'%(key)

    id = gk.item_create_sync(KEYRING_NAME, gk.ITEM_GENERIC_SECRET, 
        'magnun@Jupiter:22', {'application':APP_NAME}, 'passwd', True)
    print 'New host added (id=%i)'%(id)

Uma parte dessa aplicação irá solicitar acesso às informações, vamos
supor que isto é feito por esse "verificador":

.. code-block:: python

    #!/usr/bin/env python

    import gnomekeyring as gk
    import glib

    APP_NAME = 'MyApp'
    KEYRING_NAME = 'MyKeyring'

    glib.set_application_name(APP_NAME)

    keyrings = gk.list_keyring_names_sync()

    # If this keyring already exist, let's remove it
    if KEYRING_NAME in keyrings:
        # Gnome Keyring Daemon may ask for a password here
        gk.delete_sync(KEYRING_NAME)

    # If anyone asks, the password is 'mypasswd'
    gk.create_sync(KEYRING_NAME, 'mypasswd')

    def add_item(username, password, server, protocol, port):
        atts = {
                'application': APP_NAME,
                'username' : username,
                'server' : server,
                'protocol' : protocol,
                'port' : str(port),
               }
        name = username+'@'+server+':'+port
        id = gk.item_create_sync(KEYRING_NAME, gk.ITEM_GENERIC_SECRET, 
                name, atts, password, True)
        return id

    id = add_item('magnun', 'mypasswd', 'Neptune', 'ssh', '22')
    print 'New host added (id=%i)'%(id)
    id = add_item('guest', 'mypasswd', 'Neptune', 'ssh', '22')
    print 'New host added (id=%i)'%(id)
    id = add_item('magnun', 'mypasswd', 'Jupiter', 'ssh','22')
    print 'New host added (id=%i)'%(id)

Todas as senhas serão impressas. Vamos fingir agora que estamos
escrevendo outro aplicativo chamado *MyApp2* a qual irá acessar as
senhas armazenadas por *MyApp*. Obviamente o Gnome Keyring irá
apresentar uma caixa de diálogo questionando se você quer permitir que a
aplicação MyApp2 acesse este Chaveiro:

.. figure:: {filename}/images/GnomeKeyring_Grant_Access.png
        :align: center
        :target: {filename}/images/GnomeKeyring_Grant_Access.png
        :alt: GnomeKeyring_Grant_Access

        Permissão de Acesso

        Caixa de diálogo do Gnome Keyring - Será que o MyApp2 deve acessar esse item do chaveiro?

Isso ocorre pois o Gnome Keyring usa o nome da aplicação e o seu caminho
para tomar decisões, como uma exemplo, eu tentei acessar o chaveiro de
nome *MyKeyring* usando Seahorse e me foi apresentado o seguinte
diálogo:

.. figure:: {filename}/images/GnomeKeyring_Grant_Access_Seahorse.png
        :align: center
        :target: {filename}/images/GnomeKeyring_Grant_Access_Seahorse.png
        :alt: GnomeKeyring_Grant_Access_Seahorse

        Permissão de acesso - Seahorse

        Caixa de Diálogo do Gnome Keyring - Seahorse - Atenção para o caminho informado `/user/bin/seahorse`

Mas se nós mudássemos o nome da nossa aplicação para *MyApp* a aplicação
"não confiável" iria acessar livremente as senhas armazenadas. Porque
isso ocorre se elas são aplicações diferentes? Como eu disse, o Gnome
Keyring utiliza o caminho da aplicação para tomar decisões, mas as
aplicações em Python sempre utilizam o caminho /usr/bin/python2.6 (nesse
caso), com isso essa "proteção" se torna inexistente. Digamos que,
**isso** é uma grande falha! Você pode fazer com que qualquer aplicação
desconhecida se torna "confiável" aos olhos do Gnome Keyring somente
mudando o nome da aplicação. Um `bug report <https://bugzilla.gnome.org/show_bug.cgi?id=342144>`_ foi devidamente preenchido
mas a solução ainda está pendente. Para evitar que esse tipo de falha
seja explorada nós podemos utilizar a função de "trancar" (*lock*) o
chaveiro. No próximo post irei mostrar como fazer isso.
