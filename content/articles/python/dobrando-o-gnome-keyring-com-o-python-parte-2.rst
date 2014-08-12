Dobrando o Gnome Keyring Com o Python – Parte 2
###############################################
:date: 2010-12-07 08:00
:category: Python
:tags: gnome keyring, keyring, passwords, python, seahorse, tiamat, tutorial, username
:description: Esta continuação demonstra como utilizar a biblioteca em Python para integrar com o Gnome Keyring.
:image: /images/gkeyring.png
:series: Dobrando o Gnome Keyring Com o Python

.. default-role:: code

No nosso `último post </pt/dobrando-o-gnome-keyring-com-o-python-parte>`_
nós começamos a introduzir como o Gnome Keyring funciona. Eu mostrei como criar
um chaveiro (keyring) e seus itens utilizando o Seahorse, agora irei mostrar
como fazer a mesma coisa usando o Python. Para tornar a interação entre o GNome
Keyring e o Python nós precisamos da biblioteca python-gnomekeyring instalada.
Vamos começar a dobrar...

.. image:: {filename}/images/gkeyring.png
    :align: center
    :target: {filename}/images/gkeyring.png
    :alt: Gnome Keyring

.. more

Explorando o Gnome Keyring
--------------------------

Como o primeiro passo irei mostrar como "explorar" o Gnome Keyring. A melhor
forma de começar é ter certeza que o Daemon do Gnome keyring Daemon está
disponível utilizando o método `is_available`. Para buscar por chaveiros
existentes nós utilizaremos o método `list_keyring_names_sync`. Se você testar
isto a partir de uma console Python você receberá uma mensagem recorrente:
`g_set_application_name not set`. Um exemplo:

.. code-block:: python

    >>> import gnomekeyring as gk
    >>> gk.list_keyring_names_sync()

    ** (process:1737): WARNING **: g_set_application_name not set.
    ['login', 'MyKeyring', 'session']
    >>>

Isto acontece porque o daemon requer informações sobre a aplicação que está tentando acessar as informações do Gnome Keyring. Como estamos utilizando uma console Python nós não possuímos nenhum nome de aplciação. Para resolver isso, é possível importar a biblioteca gobject e utilizar o método `set_application_name`. Abaixo, segue um exemplo simples de listagem dos chaveiros:

.. code-block:: python

    >>> import gnomekeyring as gk
    >>> import glib
    >>> glib.set_application_name('gk-test')
    >>> gk.is_available()
    True
    >>> gk.list_keyring_names_sync()
    ['login', 'MyKeyring', 'session']
    >>>

Aqui podemos ver que o chaveiro chamado "MyKeyring", criado no último post, está presente. Para explorar nossa senha armazenada nós podemos utilziar o método `list_item_ids_sync`, o qual retorna um tipo long que representa os itens armazenados. O método item\_get\_info\_sync irá retornar uma instância de KeyringItemInfo que armazenará as informações básicas que nós definimos no último post. Quando buscamos essas informações, você verá um diálogo questionando se sua aplicação deveria ter acesso à informação sensível deste item.

.. figure:: {filename}/images/GnomeKeyring_Allow_access_Dialog.png
    :align: center
    :target: {filename}/images/GnomeKeyring_Allow_access_Dialog.png
    :alt: Gnome Keyring Allow Access Dialog

    Dialogo de Acesso

    Diálogo solicitando permissão para acessar a senha armazenada para magnun@Neptune:22

Esta tela é apresentada uma vez que a aplicação que está solicitando não é a criadora da informação solicitada. Os atributos de `KeyringItemInfo` podem sr acessados pelos métodos `get_secret` e `get_display_name`. Segue um exemplo abaixo:

.. code-block:: python

        >>>
        >>> def list_keyring_items(keyring_name):
        ...     item_keys = gk.list_item_ids_sync(keyring_name)
        ...     print 'Existing item Keys:',item_keys
        ...     for key in item_keys:
        ...         item_info = gk.item_get_info_sync(keyring_name, key)
        ...         print "* Item number",key
        ...         print "\tName:", item_info.get_display_name()
        ...         print "\tPassword:", item_info.get_secret()
        ...
        >>> list_keyring_items('MyKeyring')
        Existing item Keys: [1L]
        * Item number 1
            Name: magnun@Neptune:22
            Password: mypasswd
        >>>

Considerando que nos iremos desenvolver uma aplicação que irá armazenar vários itens de um *keyring*, é interessante que nossa aplicação possua um *keyring* próprio. Usando esta gancho, vou mostrar como remover um *keyring* existente e os seus itens. Lembre-se, nunca remova o *keyring* `login` e `session`, eles são utilizados pelo sistema operacional.

Removendo um *Keyring*
----------------------

Depois de compreender como o *Gnome Keyring* funciona, remover um *keyring* e os seus respectivos itens se torna uma tarefa fácil. Você pode remover um único item de um *keyring* utilizando o método `item_delete_sync` ou utilizar o método `delete_sync` para remover o *keyring* juntamente com todos os seus itens.

.. code-block:: python

        >>> gk.list_keyring_names_sync()
        ['MyKeyring', 'login', 'session']
        >>> gk.list_item_ids_sync('MyKeyring')
        [1L, 2L]
        >>> gk.item_delete_sync('MyKeyring', 2L)
        >>>
        >>> gk.list_item_ids_sync('MyKeyring')
        [1L]
        >>> gk.delete_sync('MyKeyring')
        >>> gk.list_keyring_names_sync()
        ['login', 'session']
        >>>

Criando e Populando Um *Keyring*
--------------------------------

A criação do *keyring* é um processo simples e que lembra muito o processo realizado através da interface gráfica. É necessário informar apenas o nome a senha:

.. code-block:: python

        >>> gk.list_keyring_names_sync()
        ['login', 'session']
        >>> gk.create_sync('GKApp', 'gkpass')
        >>> gk.list_keyring_names_sync()
        ['GKApp', 'login', 'session']
        >>>

A criação de um item no *keyring* já é um pouco diferente, existe um novo campo chamado `attributes`. Veja um exemplo abaixo:

.. code-block:: python

        >>> atts = {'username':'magnun',
        ...         'server':'Neptune',
        ...         'service':'SSH',
        ...         'port':'22',
        ...        }
        >>> gk.item_create_sync('GKApp', gk.ITEM_GENERIC_SECRET,
        .... 'magnun@Neptune:22', atts, 'mypasswd', True)
        ....
        1L
        >>> item_keys = gk.list_item_ids_sync('GKApp')
        >>> item_info = gk.item_get_info_sync('GKApp', item_keys[0])
        >>> item_info.get_display_name()
        'magnun@Neptune:22'
        >>> item_info.get_secret()
        'mypasswd'
        >>> 

Como mostrado, o processo de criação de um item é um pouco diferente. Quando utilizamos o *SeaHorse* existem apenas 3 campos (*Keyring*, *description* e *password*), e previamente selecionamos o tipo do item. Utilizando a API existem seis campos:

.. class:: dl-horizontal

        Keyring
                Define a qual *keyring* este item irá pertencer. Neste exemplo é GKApp;
        Tipo de Item
                Descreve o item que está sendo adicionado. Pode ser `ITEM_GENERIC_SECRET`, `ITEM_NETWORK_PASSWORD` e `ITEM_NOTE`;
        Descrição
                Também descrito como *display name* ou "nome de apresentação". Este nome é utilizado como chave, e necessita ser único dentro de um *keyring*.
        Atributos
                Um dicionário representando atributos definidos pelo usuário. Estes podem ser qualquer coisa, a funcionalidade deste campo será mostrada no futuro;
        Senha
                Também descrita como "segredo". Esto pode ser qualquer informação que precise ser armazenada secretamente;
        Atualização
                Se `True` itens existentes (mesma descrição e atributos) seão atualizados.

Simples não? Agora, olhando através do *SeaHorse* nos podemos ver algumas diferenças dos itens criados no último artigo. Veja algumas imagens:

.. figure:: {filename}/images/GnomeKeyring_Keyring-Item-Properties-Datails.png
        :align: center
        :target: {filename}/images/GnomeKeyring_Keyring-Item-Properties-Datails.png
        :alt: Seahorse Keyring Item Properties Dialog - Details

        Dialogo de Propriedades

        Diálogo de Item do Seahorse Keyring mostrando os detalhes do item

.. figure:: {filename}/images/GnomeKeyring_Keyring-Item-Properties-Applications.png
        :align: center
        :target: {filename}/images/GnomeKeyring_Keyring-Item-Properties-Applications.png
        :alt: Seahorse Keyring Item Dialog - Applications

        Dialogo de Aplicações

        Diálogo de Item do Seahorse Keyring mostrando a "aplicação dona"

Como podemos ver, agora os atributos estão preenchidos com informações e o nome da aplicação está gravado para `gk-test`, que foi informado através de `glib.set_application_name`. No próximo artigo eu irei mostrar um pouco mais sobre como usar corretamente os *keyrings*, um pouco sobre segurança e vou mostrar também alguns scripts de exemplos.

