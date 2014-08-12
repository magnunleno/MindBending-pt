Dobrando o Gnome Keyring Com o Python – Parte 7
###############################################
:date: 2011-02-15 14:11
:category: Python
:tags: bending, code, gnome, keyring, lock, passwords, python, security, tiamat, timeout, tutorial, wrapper
:description: Nesta última parte vamos aprender uma outra opção para envolver o GnomeKeyring e adicionar a funcionalidade de timeout.
:image: /images/gkeyring.png
:series: Dobrando o Gnome Keyring Com o Python


.. default-role:: code

Alguns posts atrás eu falei sobre `duas formas de resolver`_ um problema com o Python & Gnome Keyring. A primeira forma (apresentada `aqui`_) propôs criar uma classe que "envolve" a libgnome-keyring e a cada requisição ela destranca e tranca o chaveiro. Essa não é a forma mais perfeita e permitia a exploração de algumas falhas de segurança. A segunda solução, e também a mais elegante, é criar uma outra classe para "envolver" libgnome-keyring e adiciona a funcionalidade de temporizador de inatividade.

.. image:: {filename}/images/gkeyring.png
    :align: center
    :target: {filename}/images/gkeyring.png
    :alt: Gnome Keyring

.. more

Neste post eu irei mostrar um exemplo de implementação. O código apresentado aqui está baseado na último código que postei. Eu alterei somente algumas linhas adicionando uma janela GTK para simular uma aplicação. Vamos ver o código:


.. code-block:: python

    # Written by Magnun Leno. License: GPLv3
    import gnomekeyring as gk
    import glib
    import gtk
    from gobject import timeout_add, source_remove

    APP_NAME = 'MyApp'
    IDLE_TIME = 0.1 # In minutes

    glib.set_application_name(APP_NAME)

    if not gk.is_available():
        print 'Gnome Keyring is unavailable!'
        exit()

    class KeyringManager:
        '''
            The KeyringManager class wraps the main functions used to manage
            keyrings.
        '''
        def __init__(self):
            '''
                Load the basic informations:
                - Keyring names;
                - default keyring.
            '''
            self.default_keyring = gk.get_default_keyring_sync()
            self.keyrings = gk.list_keyring_names_sync()

        def __update_keyring_names(when):
            '''
                Descriptor used to auto update some attributes in the KeyringManager
                class. Currently it just reloads the keyring names but can be expanded
                to update any other information.
            '''
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
            '''
                Create a keyring. Don't return any value.
            '''
            gk.create_sync(name, password)

        @__update_keyring_names('after')
        def delete_keyring(self, name):
            '''
                Delete a Keyring. Don't return any value
            '''
            gk.delete_sync(name)

        def lock_all_keyrings(self):
            '''
                Lock all Keyrings. Don't return any value
            '''
            gk.lock_all_sync()

        def set_default_keyring(self, name):
            gk.set_default_keyring_sync(name)
            self.default_keyring = gk.get_default_keyring_sync()

        @__update_keyring_names('before')
        def __contains__(self, name):
            '''
                Return a boolean value based in the existence of an Keyring with the
                informed name. can e used with the in statement:
                >>> 'mykeyring' in keyringmanager
                True
            '''
            return name in self.keyrings

        @__update_keyring_names('before')
        def __getitem__(self, name):
            '''
                Mimics the dictionary behaviour:
                >>> keyringmanager['mykeyring']
            '''
            if name in self:
                return Keyring(name)
            return None

    class Keyring:
        '''
            The Keyring class wrapps some basic actions to the Gnome Keyring and it's
            items, such as:
             - lock;
             - unlock;
             - list items id;
             - change password;
             - access it's items;
             - get items secret.
        '''
        def __init__(self, name):
            '''
                Automatically lock the keyring and starts its basic informations:
                 - default idle timeout;
                 - keyring name;
                 - keyring info;
                 - lock on idle flag.
            '''
            global IDLE_TIME
            self.idle_timeout = IDLE_TIME # In minutes
            self.name = name
            self.info = gk.get_info_sync(name)

            if self.info.get_is_locked():
                self.__idle_timeout = None
                self.lock_on_idle = False
            else:
                self.__idle_timeout = self.__set_timeout(self.__autolock)
                self.lock_on_idle = True
                self.lock()

        def __set_timeout(self, func, *args):
            '''
                Auxiliar function. Just returns a gobject timeout.
            '''
            idle_time = int(self.idle_timeout*1000*60)
            timeout = timeout_add(idle_time, func, *args)
            return timeout

        def __autolock(self):
            '''
                Function used by the gobject timout to atomically lock the keyring.
            '''
            if not self.is_locked():
                self.lock()
            source_remove(self.__idle_timeout)
            self.__idle_timeout = None
            self.lock_on_idle = False

        def __restart_timeout(self):
            '''
                Just restarts the timeout in case of any activity. Must be called by
                every method that access restricted information.
            '''
            source_remove(self.__idle_timeout)
            self.__idle_timeout = self.__set_timeout(self.__autolock)

        def lock(self):
            '''
                Just lock the keyring.
            '''
            gk.lock_sync(self.name)

        def unlock(self, passwd):
            '''
                Just unlock the keyring.
            '''
            gk.unlock_sync(self.name, passwd)
            if self.__idle_timeout is None:
                self.lock_on_idle = True
                self.__idle_timeout = self.__set_timeout(self.__autolock)

        def list_items_id(self):
            '''
                List items id and restarts the idle timeout.
            '''
            if self.is_locked():
                raise Exception("Keyring '"+self.name+"' is locked")

            self.items_id = gk.list_item_ids_sync(self.name)
            self.__restart_timeout()
            return self.items_id

        def is_locked(self):
            '''
                Informs if the Keyring is locked.
            '''
            self.update_info()
            return self.info.get_is_locked()

        def update_info(self):
            '''
                Update keyring information. Is called by methods that alters the Keyring
                information.
            '''
            self.info = gk.get_info_sync(self.name)

        def change_password(self, old_passwd, new_passwd):
            '''
                Change the Keyring password.
            '''
            if self.is_locked():
                raise Exception("Keyring '"+self.name+"' is locked")

            self.__restart_timeout()
            gk.change_password_sync(self.name, old_passwd, new_passwd)
            return True

        def get_item_secret(self, item_id):
            '''
                Return the secret of a Keyring Item.
            '''
            if self.is_locked():
                raise Exception("Keyring '"+self.name+"' is locked")

            item_info = gk.item_get_info_sync(self.name, item_id)
            self.__restart_timeout()
            return item_info.get_secret()

        def __getitem__(self, count):
            '''
                Used to mimic the dictionary behaviour.
            '''
            if self.is_locked():
                raise Exception("Keyring '"+self.name+"' is locked")

            item_id = gk.list_item_ids_sync(self.name)[count]
            attr = gk.item_get_attributes_sync(self.name, item_id)
            attr['id'] = item_id
            self.__restart_timeout()
            return attr

    class Application:
        '''
            Simulate an application
        '''
        def __init__(self):
            self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
            self.window.connect("destroy", self.destroy)
            self.window.set_border_width(10)
            self.vbox = gtk.VBox()
            self.window.add(self.vbox)

            self.check_btn = gtk.Button("Check Keyring")
            self.check_btn.connect("clicked", self.show_status)

            self.query_btn = gtk.Button("Query Keyring")
            self.query_btn.connect("clicked", self.query_info)

            self.vbox.pack_start(self.check_btn)
            self.vbox.pack_start(self.query_btn)
            self.window.show_all()

            self.km = KeyringManager()
            self.mykey = self.km['mykeyring']
            if self.mykey is None:
                self.km.create_keyring('mykeyring', 'mypasswd')
                self.mykey = self.km['mykeyring']

            self.count = 0

            print '-> %3i:'%(self.count),
            print 'Keyring:',self.mykey.name,'t Lock:',self.mykey.is_locked()
            self.count += 1
            if self.mykey.is_locked():
                self.mykey.unlock('mypasswd')
                self.show_status(None)

        def show_status(self, widget):
            print '-> %3i:'%(self.count),
            print 'Keyring:',self.mykey.name,'t Lock:',self.mykey.is_locked()
            self.count += 1

        def query_info(self, widget):
            print '->',self.mykey.name, 'items:', self.mykey.list_items_id()

        def destroy(self, widget, data=None):
            gtk.main_quit()

        def main(self):
            gtk.main()

    if __name__ == "__main__":
        app = Application()
        app.main()

Aqui eu utilizei uma janela GTK com 2 botões (um simples HelloWorld com pyGTK). O primeiro botão imprime o nome do chaveiro e o seu status (se está trancado ou não), enquanto o segundo busca os itens do chaveiro e imprime os seus identificadores. Durante essa busca o temporizador de inatividade é restartado. No início da aplicação ela chama o KeyringManager (linha 248) e tenta buscar o chaveiro 'mykeyring'. Caso ele não exista, ele será criado (linha 251). Depois de imprimir i status do chaveiro, que provavelmente estará trancado, a aplicação tentará destrancar o chaveiro (em uma aplicação real deverá ser criada uma caixa de diálogo solicitando ao usuários a senha do chaveiro) e logo após imprimirá o seu status novamente. Se continuarmos pressionando o botão 'Check Keyring' notaremos que eventualmente o chaveiro será automaticamente trancado . Após isso o botão 'Query Keyring' irá causar uma exceção. Neste exemplo o timeout do keyring está configurado para 0.1 minutos (veja a linha 8) ou 6 segundos. Em uma aplicação real este tempo poderia ser algo em torno de 5 minutos, para prevenir que o usuário se incomode com diversas solicitações para destrancar o chaveiro.

Vamos ver um exemplo desta execução:

.. code-block:: bash

    $ python KeyringWrapper.py
    ->   0: Keyring: mykeyring    Lock: True
    ->   1: Keyring: mykeyring    Lock: False
    ->   2: Keyring: mykeyring    Lock: False
    ->   3: Keyring: mykeyring    Lock: False
    ->   4: Keyring: mykeyring    Lock: False
    ->   5: Keyring: mykeyring    Lock: False
    ->   6: Keyring: mykeyring    Lock: True
    ->   7: Keyring: mykeyring    Lock: True
    ->   8: Keyring: mykeyring    Lock: True

Provavelmente esse seja o meu último post acerca do Gnome Keyring e o
Python. Eventualmente posso retornar a este assunto uma vez que irei
trabalhar com o Gnome Keyring diversas vezes no futuro. Qualquer
comentário ou sugestão é extremamente bem vindo.

.. _duas formas de resolver: /pt/dobrando-o-gnome-keyring-com-o-python-parte-5/
.. _aqui: /pt/dobrando-o-gnome-keyring-com-o-python-parte-6/
