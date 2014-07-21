Dobrando o Gnome Keyring Com o Python – Parte 5
###############################################
:date: 2011-01-31 16:40
:category: Python
:tags: bending, bug, gnome, idle, keyring, lock, passwords, python, security, tiamat, tutorial
:description: Apesar de todas as vantagens nem tudo é perfeito da terra do Gnome Keyring, algumas funcionalidades essenciais para garantir a segurança não funcionam no binding para Python.
:image: /images/gkeyring.png
:series: Dobrando o Gnome Keyring Com o Python

.. default-role:: code

Seguindo a linha do meu `último post </pt/dobrando-o-gnome-keyring-com-o-python-parte/>`_, existe uma "falha de segurança" no Gnome Keyring. Ainda bem que há um mecanismo que nos traz um pouco de paz. A `API do Gnome Keyring <http://library.gnome.org/devel/gnome-keyring/stable/index.html>`_ (ligbnome-keyring) nós provê uma forca de "trancar" uma chaveiro específico usando os métodos: `set_lock_on_idle <http://library.gnome.org/devel/gnome-keyring/stable/gnome-keyring-Keyring-Info.html#gnome-keyring-info-set-lock-on-idle>`_ and `set_lock_timeout <http://library.gnome.org/devel/gnome-keyring/stable/gnome-keyring-Keyring-Info.html#gnome-keyring-info-set-lock-timeout>`_.

.. image:: {filename}/images/gkeyring.png
    :align: center
    :target: {filename}/images/gkeyring.png
    :alt: Gnome Keyring

De acordo com a documentação da API do Gnome Keyring (disponível somente
em C) o método `set_lock_on_idle` recebe um valor booleano (True of
False), o qual define se um chaveiro específico deveria ou não ser
"trancado" após um tempo de inatividade. O método `set_lock_timeout`
define após quantos segundos o chaveiro seria considerado como inativo.
Uma vez que não consegui encontrar nenhuma exemplo de uso e eu não muito
menos ajuda com a comunidade/desenvolvedores eu imagino que a utilização
correta para esse método ser algo assim:

.. more

.. code-block:: python

    >>> import gnomekeyring as gk
    >>> import glib
    >>>
    >>> glib.set_application_name('MyApp')
    >>> my_keyring = gk.get_info_sync('MyKeyring')
    >>>
    >>> my_keyring.set_lock_timeout(10) #10 seconds
    >>> my_keyring.set_lock_on_idle(True)

Mas adivinha, não funcionou! Eu esperei por vinte segundo e submeti o
comando `my_keyring.get_is_locked()` mas ele retornou False. Eu esperei
por 10 minutos, caso a API não estivesse considerando a entrada em
minutos, mas nada aconteceu. Eu pensei até mesmo que o processo do
Python contasse como atividade no chaveiro, então configurei tudo
novamente e saí da Shell do Python e monitorei o processo via Seahorse.
Novamente nada. Talvez essa implementação esteja incorreta ou eu entendi
incorretamente a sua utilização, então eu tentei novamente contactar os
desenvolvedores do Gnome submetendo o seguinte bug: `Bug #614350 <https://bugzilla.gnome.org/show_bug.cgi?id=614350>`_. Após
um mês não obtive respostas. Semana passada eu fiz uma pergunta no
Launchpad para o Time de empacotamento do *libgnome-keyring* para o Ubuntu
(`Question #110067 <https://answers.launchpad.net/ubuntu/+source/libgnome-keyring/+question/110067>`_) mas novamente não tive respostas. Se eu entendi
incorretamente o conceito de "*lock on idle*" e alguém aí fora conhece a
forma correta, por favor, me avise!

Uma vez que não tenho perspectiva de correção desse bug e exauri minha
fonte de ideias de como seria a "forma correta" de uso do idle timeout,
eu sugiro duas implementações para manter o chaveiro seguro:

#. Sempre tanque o chaveiro após uma pesquisa. Para implementar isso
   você precisará armazenar a senha do chaveiro em uma certa variável e
   seguir os seguintes passos: verificar a "tranca"; obter a senha;
   destrancar; pesquisar; trancar.
#. Encapsular o chaveiro em outra classe e utilizar um "contador
   regressivo" (ex: `gobject.timepout_add`) para definir quando o ele irá
   se tornar inativo.

A primeira sugestão é muito simples de se implementar enquanto a segunda
demanda um trabalho extra. Em posts futuros irei mostrar meu exemplo de
implementação.
