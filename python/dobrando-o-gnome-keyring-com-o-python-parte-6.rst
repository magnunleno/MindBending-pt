Dobrando o Gnome Keyring Com o Python – Parte 6
###############################################
:date: 2011-02-01 16:13
:category: Python
:tags: bending, code, gnome, keyring, lock, passwords, python, security, tiamat, tutorial, wrapper
:description: Neste resumo da exploração do Gnome Keyring é demonstrada uma forma de abstrarir sua complexidade por meio de uma wrapper class.
:image: /images/gkeyring.png
:series: Dobrando o Gnome Keyring Com o Python

.. default-role:: code

Continuando a partir do `último post </pt/dobrando-o-gnome-keyring-com-o-python-parte-5/>`_, irei mostrar como podemos implementar uma "wrapper class" para mudar o comportamento do Gnome Keyring. Esta não é a forma mais segura, uma vez que armazenamos a senha do chaveiro em uma variável. Mas essa abordagem é muito melhor do que deixar o chaveiro aberto para várias outras aplicações consultarem os seus dados.

.. image:: {filename}/images/gkeyring.png
    :align: center
    :target: {filename}/images/gkeyring.png
    :alt: Gnome Keyring

Primeiramente temos que criar um a classe para gerenciar o chaveiro. Ela
será responsável por:

.. more

-  consulstar os keyrings existentes;
-  criar chaveiros;
-  deletar chaveiros;
-  alterar o keyring default;
-  trancar todos os chaveiros.

Após isso, precisamos de uma classe para "envolver" o chaveiros. Uma vez
que o chaveiro possui diversas funcionalidades e não é minha intenção
recriar todas elas eu irei mostrar somente as essenciais. Desta forma,
minha classe estará apta a:

-  tranchar o chaveiro;
-  destrancar o chaveiro;
-  mostrar se o chaveiro está ou não trancado;
-  listar o identificador dos itens que compõem o chaveiro;
-  dar acesso ao `GnomeKeyringInfo <http://library.gnome.org/devel/gnome-keyring/stable/gnome-keyring-Keyring-Info.html#GnomeKeyringInfo>`_;
-  mudar a senha do chaveiro;
-  listar os atributos dos itens que compõem o chaveiro;
-  retornar a senha dos itens que compõem o chaveiro.

Em meu código utilizei alguns decoradores para garantir que algumas
informações estariam atualizadas antes/depois da execução de algumas
tarefas. Este é meu código:

.. code-block:: python

    import gnomekeyring as gk
    import glib

    APP_NAME = 'MyApp'

    glib.set_application_name(APP_NAME)

    if not gk.is_available():
        print 'Gnome Keyring is unavailable!'
        exit()

    class KeyringManager:
        def __init__(self):
            self.default_keyring = gk.get_default_keyring_sync()
            self.keyrings = gk.list_keyring_names_sync()

        def __update_keyring_names(when):
            def func(f):
                def func_params(self, *args, **kwargs):
                    if when == 'before':
                        self.keyrings = gk.list_keyring_names_sync()

                    ret = f(self, *args, **kwargs)

                    if when == 'after':
                        self.keyrings = gk.list_keyring_names_sync()

                    return ret
                return func_params
            return func

        @__update_keyring_names('after')
        def create_keyring(self, name, password):
            gk.create_sync(name, password)

        @__update_keyring_names('after')
        def delete_keyring(self, name):
            gk.delete_sync(name)

        def lock_all_keyrings(self):
            gk.lock_all_sync()

        def set_default_keyring(self, name):
            gk.set_default_keyring_sync(name)
            self.default_keyring = gk.get_default_keyring_sync()

        @__update_keyring_names('before')
        def __contains__(self, name):
            return name in self.keyrings

        @__update_keyring_names('before')
        def __getitem__(self, name):
            if name in self:
                return Keyring(name)
            return None

    class Keyring:
        def __init__(self, name):
            self.name = name
            self.info = gk.get_info_sync(name)
            self.passwd = None
            if not self.info.get_is_locked():
                self.lock()

        def lock(self):
            gk.lock_sync(self.name)

        def unlock(self, passwd):
            gk.unlock_sync(self.name, passwd)
            self.passwd = passwd

        def __lock_unlock_dec(func):
            def decorator(self, *args, **kwargs):
                self.unlock(self.passwd)
                ret = func(self, *args, **kwargs)
                self.lock()
                return ret
            return decorator

        @__lock_unlock_dec
        def list_items_id(self):
            self.items_id = gk.list_item_ids_sync(self.name)
            return self.items_id

        def is_locked(self):
            self.update_info()
            return self.info.get_is_locked()

        def update_info(self):
            self.info = gk.get_info_sync(self.name)

        def change_password(self, old_passwd, new_passwd):
            gk.change_password_sync(self.name, old_passwd, new_passwd)

        @__lock_unlock_dec
        def __getitem__(self, count):
            item_id = gk.list_item_ids_sync(self.name)[count]
            attr = gk.item_get_attributes_sync(self.name, item_id)
            attr['id'] = item_id
            return attr

        @__lock_unlock_dec
        def get_item_secret(self, item_id):
            item_info = gk.item_get_info_sync(self.name, item_id)
            return item_info.get_secret()

    if __name__ == '__main__':
        km = KeyringManager()
        print km.keyrings
        mykey = km['MyKeyring']
        mykey.passwd = 'mypasswd'
        print mykey.list_items_id()

        print '#'*10

        for item in mykey:
            print item

        print '#'*10

        print mykey[0]
        print 'item', mykey[0]['id'], 'secret:', mykey.get_item_secret(mykey[0]['id'])

Eu salvei esse código como `KeyringWrapper.py`. A sua execução me retornou a seguinte saída:

.. code-block:: bash

    $ python KeyringWrapper.py
    ['Beholder', 'login', 'MyKeyring', 'session']
    [1L, 2L, 3L]
    ##########
    {'username': 'magnun', 'protocol': 'ssh', 'port': '22', 
    'application': 'MyApp', 'server': 'Neptune', 'id': 1L}
    {'username': 'guest', 'protocol': 'ssh', 'port': '22', 
    'application': 'MyApp', 'server': 'Neptune', 'id': 2L}
    {'username': 'magnun', 'protocol': 'ssh', 'port': '22', 
    'application': 'MyApp', 'server': 'Jupiter', 'id': 3L}
    ##########
    {'username': 'magnun', 'protocol': 'ssh', 'port': '22', 
    'application': 'MyApp', 'server': 'Neptune', 'id': 1L}
    item 1 secret: mypasswd

Este código é apenas uma base. É necessário expandi-lo para contemplar
funções essenciais como `item_set_attributes <http://library.gnome.org/devel/gnome-keyring/stable/gnome-keyring-Keyring-Items.html#gnome-keyring-item-set-attributes>`_, `set_info_sync <http://library.gnome.org/devel/gnome-keyring/stable/gnome-keyring-Keyrings.html#gnome-keyring-set-info-sync>`_,
`item_create <http://library.gnome.org/devel/gnome-keyring/stable/gnome-keyring-Keyring-Items.html#gnome-keyring-item-create>`_ dentre outros. Mas como eu disse, esta não é a forma
mais segura então eu não acho que escrever essas funções valham a pena.
