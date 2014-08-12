Um Tour Pelo Novo Gnome 3.2
###########################
:date: 2011-10-03 15:58
:category: Gnome
:tags: arch, atualização, gnome, gnome 3.2, linux
:image: /images/gnome.png

Neste último dia 01/10, o Gnome 3.2 foi movido para o repositório Extra
do Arch Linux. Diversas novas funções e aplicações foram adicionadas
nesta nova versão, mas nem todas são instaladas automaticamente quando
realizamos uma atualização a partir do Gnome 3.0. Isso mesmo, este é um
dos males de uma "rolling release".

.. figure:: {filename}/images/gnome-3.2.png
	:align: center
	:target: {filename}/images/gnome-3.2.png
	:alt: Hello Gnome 3.2!

        Olá Gnome 3.2!

Então me acompanhe neste pequeno *tour* pelo novo Gnome, e venha ver com
instalar e usar estas novas funcionalidades!

.. more

Atualizando
-----------

Para começar, vamos atualizar o Gnome 3.0, para isto basta utilizar o
seguinte comando:

.. code-block:: bash

    $ sudo pacman -Suy

Após finalizar a atualização recomendo o bom e reboot, *a lá windows*.
Se você tiver algum problema de login, tente redefinir suas
configurações movendo-as de ~/.config/dconf e ~/.gconf para outro local.

Agora vamos fazer um *tour* pelas novas funcionalidades e programas...

Online Accounts
---------------

O GNOME *Online Accounts* é uma espécie de "central" para configuração
de contas. Ela pode ser acessada clicando no nome do seu usuário (canto
superior direito) e em seguida na opção "Contas Online". Nela é possível
gerenciar suas contas de e-mail, calendário, contatos, bate-papo e
documentos de uma só vez. Atualmente este recurso suporta apenas contas
providas pelo Google, mas a intenção é expandi-lo para diversos outros
provedores.

.. figure:: {filename}/images/gnome-online-accounts.png
	:align: center
	:target: {filename}/images/gnome-online-accounts.png
	:alt: Gnome Online Accounts

        Gnome Online Accounts

Ao adicionar sua conta, ele automaticamente irá configurar sua conta
para e-mail e calendário (evolution), contatos (GNOME Contacts),
bate-papo (empathy) e documentos (GNOME Documents). O Gnome Online
Accouts é instalado automaticamente pois é dependência do Gnome.

Gnome Documents
---------------

O Gnome Documents permite que você liste, visualize, edite e administre
seus documentos, tanto locais quanto *on-line* (no Google Docs). Para
mim ele não veio instalado por padrão, para instalá-lo basta chamar o
seguinte comando:

.. code-block:: bash

    $ sudo pacman -S gnome-documents


.. figure:: {filename}/images/documents.png
	:align: center
	:target: {filename}/images/documents.png
	:alt: Gnome Documents

        Gnome Documents

Gnome Contacts
--------------

Este aplicativo sincroniza seus contatos do Google (configurados no
GNOME Accounts), do Empahty e do Evolution em um Único lugar. Eu
sinceramente espero que um dia este aplicativo tenha integração com o
Android, assim (no dia em que eu comprar um Android) o gerenciamento dos
meus contatos será infinitamente facilitado!

.. figure:: {filename}/images/gnome-contacts.png
	:align: center
	:target: {filename}/images/gnome-contacts.png
	:alt: Gnome Contacts

        Gnome Contacts

Ele também não veio instalado por padrão, mas para instalá-lo é bem
simples:

.. code-block:: bash

    $ sudo pacman -S gnome-contacts

O Gnome Contacts traz uma outra funcionalidade excepcional, é possível
pesquisar contatos a partir do Gnome-Shell:

.. image:: {filename}/images/search-contacts.png
	:align: center
	:target: {filename}/images/search-contacts.png
	:alt: Gnome Shell Contacts Search


Eu só senti falta da possibilidade de iniciar uma conversa a partir da
busca do Gnome-Shell :(.

Web Application Mode
--------------------

Agora todas as aplicações Web podem ser podem ser visualizadas como uma
aplicação desktop. Para isto basta abrir uma página Web utilizando o
Epiphany e escolher a opção ``Arquivo->Salvar Como Aplicativo Wewb...``

.. figure:: {filename}/images/webapplication.png
	:align: center
	:target: {filename}/images/webapplication.png
	:alt: Gnome Web Application

        Gnome Web Application

Desabilitar Notificações
------------------------

Esta funcionalidade também será muito utilizada por mim, de vez em
quando as notificações de bate-papo e etc me desconcentram enquanto
programo. Pena que o Gnome ainda não oferece uma integração com as
mensagens de status personalizadas do Empathy.

.. image:: {filename}/images/notificacoes.png
	:align: center
	:target: {filename}/images/notificacoes.png
	:alt: Notificações

Sushi
-----

Esta é outra funcionalidade muito esperada por mim mas que não veio
instalada por padrão. Para instalá-la utilize o seguinte comando:

.. code-block:: bash

    $ sudo pacman -S sushi

Esta aplicação permite uma pré-visualização (de forma similar ao
Gloobus) de diversos tipos de arquivos como, imagens, músicas, vídeos,
documentos e etc. Para utilizá-lo basta escolher um arquivo no nautilus
e pressionar a tecla ``espaço``:

.. figure:: {filename}/images/sushi.png
	:align: center
	:target: {filename}/images/sushi.png
	:alt: Gnome Sushi

        Gnome Sushi

Por enquanto é só pessoal! Mas fiquem ligados, em breve postarei sobre o
tema secreto do Gnome 3.2!

Até lá...
