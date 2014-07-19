Corrigindo Erro de Chaves no Ubuntu
###################################
:date: 2014-05-05 10:11
:category: Tutorial
:tags: ubuntu, ssh, git, chave, ssh-agent, ssh-add, id_rsa
:image: /images/logos/ubuntu-gnome.png

Há alguns meses acabei precisando voltar a utilizar o Ubuntu no meu notebook (problemas de *drivers* no Arch Linux). Claro, quem me conhece sabe que o Unity não me agrada muito, e por isso optei pelo Ubuntu Gnome.

.. image:: {filename}/images/logos/ubuntu-gnome.png
        :target: {filename}/images/logos/ubuntu-gnome.png
        :alt: Ubuntu Gnome
        :align: center

Recentemente, como todos sabem, foi lançada versão 14.04 do Ubuntu e, consequentemente, surgiu uma atualização para o meu notebook. A atualização ocorreu bem, exceto por um detalhe...

.. more

O Erro
------

Depois de atualizar o sistema eu revisando a penúltima parte do `Curso de Filosofia GNU`_. Quando fui publicar (através do Git) me deparei com o seguinte problema:

.. code-block:: bash

        $ git push origin master
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        Permissions 0755 for '/home/username/.ssh/id_rsa' are too open.
        It is required that your private key files are NOT accessible by others.
        This private key will be ignored.
        bad permissions: ignore key: /home/username/.ssh/id_rsa

Pfff, isso é simples -- eu pensei -- basta um simples comando: ``chmod 700 /home/magnun/.ssh/id_rsa``. Para minha surpresa após essa "simples correção" o verdadeiro problema apareceu. Toda vez que eu tentava realizar um ``git push`` ou conectar via ``ssh`` em um servidor era necessário inserir a senha de segurança da minha chave privada (``id_rsa``). Veja evidência abaixo:

.. code-block:: bash

        $ git push origin master
        Enter passphrase for /home/username/.ssh/id_rsa: 

Possivelmente, em algum momento da atualização do Ubuntu as permissões das chaves foram alteradas (algo desnecessário) e o bash foi removido da lista de clientes do ``ssh-agent``.

De forma simples, toda vez que você inicia o seu GNU/Linux, uma instância do ``ssh-agent`` é iniciada. Esta instância tem controle da sua chave criptográfica privada, podendo "cedê-la" para alguns clientes sem a solicitação de senhas, pois o ``ssh-agent`` "destrava" a sua chave privada após o login (após você inserir sua senha de login).

A solução
---------

Após a explicação acima a solução é bem lógica: adicionar o ``bash`` à lista de clientes do ``ssh-agent``. para isso utilize os seguintes comandos:

.. code-block:: bash

        $ ssh-agent bash
        $ ssh-add /home/username/.ssh/id_rsa

Após esses comandos será solicitada a senha da sua chave de criptografia privada. Uma vez inserida, você deverá ver uma mensagem semelhante à abaixo:

.. code-block:: bash

        Identity added: /home/username/.ssh/id_rsa (/home/username/.ssh/id_rsa)

Por fim, reinicie a sua sessão no ambiente de trabalho (GNOME ou outro), e tudo estará normalizado.

.. _Curso de Filosofia GNU: /pt/series/curso-de-filosofia-gnu
