Dobrando o Gnome Keyring Com o Python – Parte 3
###############################################
:date: 2010-12-29 17:46
:category: Python
:tags: bending, gnome, keyring, passwords, python, seahorse, ssh, store, tiamat, tutorial, username
:description: Nesta continuação são demonstradas formas de inserir e buscar informações no Gnome Keyring.
:image: /images/gkeyring.png
:series: Dobrando o Gnome Keyring Com o Python

.. default-role:: code

No `ultimo post </pt/dobrando-o-gnome-keyring-com-o-python-parte-2/>`_ eu mostrei como criar chaveiros usando o Python e mencionei as "pequenas diferenças" com o processo de armazenamento de senhas pelo SeaHorse. Bem, acontece que, quando começamos a cavar mais fundo, essa diferença se mostrai um pouco maior. Usando o SeaHorse todo chaveiro é criado a flag *Update if Exists* com o valor False, com isso é possível criar itens idênticos no chaveiro. Essa não é uma abordagem muito segura e pode resultar em um chaveiro inconsistente. Mas ao utilizarmos a flag *Update if Exists* com o valor True, algo inesperado acontece:

.. image:: {filename}/images/gkeyring.png
    :align: center
    :target: {filename}/images/gkeyring.png
    :alt: Gnome Keyring

.. more

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

    id = gk.item_create_sync(KEYRING_NAME, gk.ITEM_GENERIC_SECRET, 
        'magnun@Neptune:22', {'application':APP_NAME}, 'passwd', True)
    print 'New host added (key=%i)'%(key)

    id = gk.item_create_sync(KEYRING_NAME, gk.ITEM_GENERIC_SECRET,
        'guest@Neptune:22', {'application':APP_NAME}, 'passwd', True)
    print 'New host added (key=%i)'%(key)

    id = gk.item_create_sync(KEYRING_NAME, gk.ITEM_GENERIC_SECRET,
        'magnun@Jupiter:22', {'application':APP_NAME}, 'passwd', True)
    print 'New host added (id=%i)'%(id)

Salve esse código como `my_keyring_creator.py` e execute-o.

Note que ao executar é mostrado sempre o mesmo id. Ao abrir o SeaHorse
(após a execução desse script) podemos notar que existe **somente um**
item no chaveiro, `magnun@Jupiter:22`. Isso acontece porque o Daemon do
Gnome Keyring usa os **atributos** para definir quando um item do
chaveiro está duplicado ou não. Então precisamos definir alguns
atributos que identificam unicamente cada item do chaveiro. O seguinte
script mostra um bom exemplo disso:

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
        attr = {
                'application':APP_NAME,
                'username':username,
                'server':server,
                'protocol':protocol,
                'port':str(port),
            }
        name = username+'@'+server+':'+port
        id = gk.item_create_sync(KEYRING_NAME, gk.ITEM_GENERIC_SECRET, name,
        attr, password, True)
        return id

    id = add_item('magnun', 'mypasswd', 'Neptune', 'ssh', '22')
    print 'New host added (id=%i)'%(id)
    id = add_item('guest', 'mypasswd', 'Neptune', 'ssh', '22')
    print 'New host added (id=%i)'%(id)
    id = add_item('magnun', 'mypasswd', 'Jupiter', 'ssh','22')
    print 'New host added (id=%i)'%(id)

Salve esse código como `my_keyring_creator.py` e execute-o.

Agora, como cade item é único, é apresentado identificadores diferentes
para cada item e eles são armazenados corretamente. Os atributos possuem
outras funcionalidades além de identificar cada item unicamente.

Buscando por itens
------------------

Vamos supor novamente que você possui um chaveiro chamado *MyKeyring*
para sua aplicação chamada *MyApp* e diversos itens no chaveiro. Se você
quiser acompanhar esse teste, você pode usar o código acima para criar o
ambiente. Em um dado momento, sua aplicação precisará buscar por um item
específico do chaveiro, vamos supor que você precise buscar a senha de
magnun@Neptune:22. Usando o que sabemos até o momento, essa tarefa pode
ser realizada usando o seguinte algoritmo:

.. code-block:: python

    #!/usr/bin/env python

    import gnomekeyring as gk
    import glib

    APP_NAME = 'MyApp'
    KEYRING_NAME = 'MyKeyring'

    glib.set_application_name(APP_NAME)

    keyrings = gk.list_keyring_names_sync()

    # Quit if the keyring don't exist
    if KEYRING_NAME not in keyrings:
    print 'Keyring',KEYRING_NAME,'not found'
    print 'Exiting...'
    exit()

    def search_secret(username, server, port):
        name = username+'@'+server+':'+port
        items_ids = gk.list_item_ids_sync(KEYRING_NAME)
        for item_id in items_ids:
            item_info = gk.item_get_info_sync(KEYRING_NAME, item_id)
            if name == item_info.get_display_name():
                secret = item_info.get_secret()
                return secret
            else:
                return None

    print 'Searching magnun@Neptune:22 secret:',
    print search_secret('magnun', 'Neptune', '22')

    print 'Searching guest@Neptune:22 secret:',
    print search_secret('magnun', 'Neptune', '22')

    print 'Searching magnun@Jupiter:22 secret:',
    print search_secret('magnun', 'Jupiter', '22')

    print 'Searching guest@Jupiter:22 secret:',
    print search_secret('guest', 'Jupiter', '22')

Salve esse código como `my_keyring_inspector.py` e execute-o.

Há uma outra forma de resolver esse problema, nós podemos utilizar o
método `find_items_sync`. Esse método retorna uma lista do tipo
GnomeKeyringFound, que contem os atributos secret, parent keyring e id
dos itens do chaveiro. Este método é mais rápido e possui a
flexibilidade de realizar buscas customizáveis. Com o método
`find_items_sync` podemos buscar por todos os itens armazenados no
chaveiro com um username ou server específico. Vamos ver um exemplo:

.. code-block:: python

    #!/usr/bin/env python

    import gnomekeyring as gk
    import glib

    APP_NAME = 'MyApp'
    KEYRING_NAME = 'MyKeyring'

    glib.set_application_name(APP_NAME)

    keyrings = gk.list_keyring_names_sync()

    # Quit if the keyring don't exist
    if KEYRING_NAME not in keyrings:
    print 'Keyring',KEYRING_NAME,'not found'
    print 'Exiting...'
    exit()

    def search_secret(username, server, port):
        attr = {
            'username':username,
            'server':server,
            'port':port,
            'application':APP_NAME,
            }
            try:
                result_list = gk.find_items_sync(gk.ITEM_GENERIC_SECRET, attr)
            except gk.NoMatchError:
                return None

            secrets = [result.secret for result in result_list]
            if len(secrets) == 1:
                secrets = secrets[0]
            return secrets

    print 'Searching magnun@Neptune:22 secret:',
    print search_secret('magnun', 'Neptune', '22')

    print 'Searching guest@Neptune:22 secret:',
    print search_secret('magnun', 'Neptune', '22')

    print 'Searching magnun@Jupiter:22 secret:',
    print search_secret('magnun', 'Jupiter', '22')

    print 'Searching guest@Jupiter:22 secret:',
    print search_secret('guest', 'Jupiter', '22')

Salve esse código como `my_keyring_inspector.py` e execute-o.

Como todos sabemos, tudo o que é bom possui um lado ruim. Como esse
método realiza a busca em **todos** os chaveiros existentes, ele requer
acesso a todos os chaveiros, o que pode ser uma coisa ruim já que o
GNOME Keyring apresenta um diálogo perguntando se você quer permitir
esse acesso. Mas como dito anteriormente, essa abordagem é muito
mais**rápida**. Com um simples benchmark utilizando um chaveiro com 500
itens, as execuções do programa `my_keyring_inspector.py` utilizando o
método `list_item_ids_sync` levou aproximadamente 0.615 segundos,
enquanto a execução do programa `my_keyring_inspector.py` utilizando o
método `find_items_sync` levou aproximadamente 0.037 segundos.
Praticamente 16 vezes mais rápido.

A decisão de qual método de busca utilziar fica a escolha do
programador, cada um possui suas vantagens e desvantagens, eu apresentei
aqui somente algumas possibilidades e uma analise básica. Se eu não
deixar nenhum esforço mental para você leitor, eu não poderia chamar
esse blog de "Mind Bending".
