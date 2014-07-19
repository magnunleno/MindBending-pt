Dobrando o Gnome Keyring Com o Python – Parte 1
###############################################
:date: 2010-10-27 15:15
:category: Python
:tags: bending, empaphy, gnome keyring, introduction, keyring, passwords, pidgin, python, seahorse, ssh, tiamat, tutorial, username
:description: Este é o artigo de abertura de uma série de como utilizar o Gnome Keyring para o armazenamento de informaçõessensíveis.
:image: /images/gkeyring.png
:series: Dobrando o Gnome Keyring Com o Python
:slug: dobrando-o-gnome-keyring-com-o-python-parte

.. default-role:: code

A um tempo atrás eu criei uma série de posts sobre como usar o Gnome Keyring e a sua biblioteca para o Python. Devido a alguns contratempos não tive tempo de postá-los em português, agora que estou um pouco mais disponível estou reescrevendo-os para o português. Desculpe-me pela demora.

.. image:: {filename}/images/gkeyring.png
    :align: center
    :target: {filename}/images/gkeyring.png
    :alt: Gnome Keyring

Nos últimos dias eu me ocupei principalmente com o desenvolvimento do meu projeto Tiamat. Durante esse trabalho me deparei com a necessidade de armazenar senhas para acesso remoto de hosts via SSH e Telnet. Eu nem hesitei, apenas uma palavra veio a minha mente: **Gnome Keyring**. Ele é simples, seguro e possui bibliotecas de binding para o Python. Então o que faltava?! Saber como usá-la. Antes de começar a trabalhar com ele, eu gostaria de discutir um pouco sobre a forma como certas aplicações armazenam nossas senhas.

.. more

É muito comum encontrar aplicações que armazenam senhas de forma "incorreta" e "insegura". É fácil encontrar clientes IM (Internet Messengers), e-mail, dentre outros, que armazenam nossas senhas em **arquivos de configuração oculto** na pasta home do usuário. Algumas vezes esse arquivo de configuração que contém as senhas recebem uma "pequena proteção", é aplicada uma senha sobre a senha. Isso quer dizer que é usando um **algoritmo reversível** que "ofusca" a senha. Isso simplesmente não é correto, é uma falsa segurança. A senha não é nem mesmo encriptada. Com um **pequeno esforço** de "força bruta" é possível descobrir a senha armazenada.

Um exemplo perfeito é o **Pidgin**, o famoso cliente de bate-papo. Ele armazena sua senha em `/home/<nome_do_usuario>/.purple/accounts.xml`.  Você não acredita? Pode `conferir aqui <https://bugs.launchpad.net/ubuntu/+source/pidgin/+bug/226974>`_. Ainda não consegue acreditar ne?! O time de desenvolvedores inclusive se pronunciou `sobre isso aqui <http://developer.pidgin.im/wiki/PlainTextPasswords>`_. Vou citar o primeiro parágrafo (tradução livre):

    Purple não encripta as senhas no arquivo accounts.xml, também não é
    provável que as senhas venham a ser encriptadas em uma versão futura. Isto
    é um pouco controverso no Windows, especialmente no Windows 98 devido a
    sua proteção fraca de arquivos, mas é assim que as coisas são.

Então devido a uma "falta de capacidade" no Windows todos os outros usuários são afetados. Resolver esse problemas é muito simples mas os desenvolvedores elencaram quatro sugestões:

#. armazenar as senhas "sobre" uma senha;
#. Obscurecer as senhas;
#. Armazenar as senhas in **texto claro** e controlar o acesso ao arquivo;
#. Por último, **não serão armazenadas as senhas**.

Não farai nenhuma observação sobre essas quatro sugestões, já estou cheio disso. Essa é uma das razões de eu estar mudando para o Empaphy.  Espero que alguém do time de desenvolvimento do Pidgin leia isso.

Vamos começar a brincar...

O que é o Gnome Keyring.
========================

`Gnome Keyring <http://live.gnome.org/GnomeKeyring>`_ é um aplicativo daemon o qual armazena credenciais do usuário. Os dados sensíveis são encriptados e armazenados em um arquivo "keyring" localizado na pasta "home" do usuário. Outros aplicativos podem armazenar e requerer senhas para o daemon Gnome Keyring usando a biblioteca libgnome-keyring. O binding do Python com o Gnome Keyring é provido através do pacote python-gnomekeyring. Para visualizar os dados armazenados no Gnome Keyring você pode utilziar o aplicativo `Seahorse <http://projects.gnome.org/seahorse/>`_.

.. figure:: {filename}/images/GnomeKeyring_Seahorse.png
    :align: center
    :target: {filename}/images/GnomeKeyring_Seahorse.png
    :alt: Gnome Keyring

    Gnome Keyring - Seahorse
   
    Esta é tela principal do SeaHorse. Ela apresenta ao usuário keyrings existentse em um TreeView bem simples.

O Gnome Keyring é complexo e muito bem estruturado, há bastante `documentação sobre ele aqui <http://live.gnome.org/GnomeKeyring>`_. Vamos nos focar no nosso objetivo:

Criar um módulo para armazenar com segurança informações de autenticação do usuário como nome de usuário, senhas, protocolos e outros.

Vamos começar do início e tentar entender como o Gnome Keyring funciona.  Adiantando um pouco, o binding do Python para o Gnome Keyring não possui documentação então estarei utilizando a `documentação existente para a linguagem C disponível aqui <http://library.gnome.org/devel/gnome-keyring/stable/index.html>`_. Por último mas não menos importante, o binding para o Python ainda está incompleto e algumas funções não estão disponíveis.

Usando o Gnome Keyring através do SeaHorse
==========================================

O Gnome Keyring gerencia e armazena informações sensíveis do usuário em uma ou mais bases de dados. Essas bases são chamadas de **Keyrings**. A tradução da palavra keyring é chaveiro, nada mais conveniente já que vamos armazenas nele nossas "chaves". Vamos ver como criar um keyring (aqui chamaremos de MyKeyring) e como ele funciona.

Primeiro abre o SeaHorse. Então clique em File->New. Escolha "Password Keyring" e aperte em continue. Infrome o nome e a senha para o chaveiro:

.. figure:: {filename}/images/GnomeKeyring_New_Keyring2.png
    :align: center
    :target: {filename}/images/GnomeKeyring_New_Keyring2.png
    :alt: Gnome Keyring

    GnomeKeyring New Keyring
   
    Novo chaveiro adicionado

A senha definida para esse keyring é utilizada para encriptar e decriptar seus itens. Utilizando os termos do Gnome Keyring, com essa senha você pode "trancar" (encriptar) e "destrancar" (decriptar) os itens do "chaveiro". Estes itens irão armazenar qualquer tipo de informação sensível que você deseje. Neste exemplo, vamos armazenar o nome de usuário Magnun e a sua senha de SSH para o servidor Neptune.

Clique em File->New. Escolha "Stored Password" e clique em continue.  Preencha os campos da caixa de diálogo "Add Password" de acordo com a imagem abaixo:

.. figure:: {filename}/images/GnomeKeyring_New_Item.png
    :align: center
    :target: {filename}/images/GnomeKeyring_New_Item.png
    :alt: Gnome Keyring

    GnomeKeyring New Item
   
    Caixa de diálogo para adicionar uma nova senha ao SeaHorse - Selecione o chaveiro e preencha a descrição e a senha.

Pronto, agora nosso usuário e senha SSH está seguramente armazenado.  Podemos verificar se realmente está tudo ok aqui:

.. figure:: {filename}/images/GnomeKeyring_New_Keyring_Item.png
    :align: center
    :target: {filename}/images/GnomeKeyring_New_Keyring_Item.png
    :alt: Gnome Keyring

    GnomeKeyring New Keyring Item
   
    SeaHorse - Novo item do chaveiro

Mas isso não é muito inútil pois, eu terei que abrir o "chaveiro" toda vez que eu quiser lembrar da senha. Nós precisamos de uma integração, veremos como implementar isso no próximo post.
