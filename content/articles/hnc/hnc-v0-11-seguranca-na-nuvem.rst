Hack 'n' Cast v0.11 - Segurança na Nuvem
########################################
:date: 2015-01-27 01:14
:category: Hack 'n' Cast
:tags: hack 'n' cast, podcast, beta, segurança, nuvem, scicast, dropbox, computação na nuvem, fappening, vazamento de informações, SpiderOak, TrueCrypt, owncloud, criptografia, partição, gmail, peer-to-mail, google drive, apple, icloud, sony, hash, chiptune, filevault, bitlocker, volume virtual, btsync, senhas, lastpass, 1password, keepass, autenticação em dois fatores, e-mails descartáveis, openid, hashapass, openssl, nsa
:image: /images/hack-n-cast/v0.x/v0.11-cover-sqr.png
:length: 63560720
:duration: 65:20
:podcast: http://archive.org/download/HNC.v0.11-Seguranca-na-Nuvem/HNC.v0.11-Seguranca-na-Nuvem.mp3
:podcastembed: http://archive.org/embed/HNC.v0.11-Seguranca-na-Nuvem/HNC.v0.11-Seguranca-na-Nuvem.mp3
:podcast_old: True
:description: Neste mundo atual, onde tudo é conectado e armazenado remotamente, podemos agrupar os usuários em duas classes, os paranoicos, que acreditam que nunca estão seguros o suficiente, e os anestesiados, que acreditam piamente que estão seguros e que essas coisas nunca vão acontecer com eles.

Neste mais novo episódio do `Hack 'n' Cast`_ recebemos um convidado de renome, o `Jorge`_ do `SciCast`_ para falarmos um pouco sobre a sua segurança na nuvem! É isso mesmo, você lembrou de pegar seu guarda-chuva antes de sair de casa?

.. image:: {filename}/images/hack-n-cast/v0.x/v0.11-cover-wide.png
        :target: {filename}/images/hack-n-cast/v0.x/v0.11-cover-wide.png
        :alt: Hack 'n' Cast v0.11 - Segurança na Nuvem
        :align: center

Para não perder nenhum episódio siga-nos nas redes sociais (`Twitter`_ e `Facebook`_) ou inscreva-se (`Feed`_, `Podflix`_, `iTunes`_ e `Pocket Casts`_). Você quer colaborar com o Hack 'n' Cast? Sugira um tema, nos ajude a produzir uma pauta ou participe conosco! Basta entrar em contato por `E-mail`_, `Facebook`_ ou `Twitter`_. E agora temos a nossa lista de discussão no `Google Groups`_!

.. more

Já há alguns anos a modinha da vez é a nuvem. Todos querem utilizá-la, todos querem estar nela, todos confiam nela. Ela é prática, rápida, simples e o mais importante: funciona. Você só precisa de uma conexão à Internet para sincronizar ou acessar seus dados. Ninguém se incomoda ou se preocupa com o fato de que, quando usamos a nuvem você deixa de ser o dono dos seus dados. Até que temos os primeiros sinais de insegurança, fotos de nudez, listas de e-mails (com suas respectivas senhas), dentre outros casos menos divulgados. E então, de repente, todos percebem como estavam "confortavelmente anestesiados".

.. podcast:: HNC.v0.11-Seguranca-na-Nuvem
        :rss: http://feeds.feedburner.com/hack-n-cast
        :itunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846

Mas o que é Nuvem?
------------------

Do ponto de vista científico, a nuvem é um conjunto visível de partículas diminutas de gelo ou água em seu estado líquido ou ainda de ambos ao mesmo tempo (mistas), que se encontram em suspensão na atmosfera, após terem se condensado ou liquefeito em virtude de fenômenos atmosféricos.

Já na ciência da computação a nuvem (*Cloud Computing*), ou o conceito de computação em nuvem, refere-se à utilização da memória e das capacidades de armazenamento e cálculo de computadores (servidores) compartilhados e interligados por meio da Internet, seguindo o princípio da computação em grade (grid computing).

Algumas características da "nuvem":

* O armazenamento de dados é feito em serviços que poderão ser acessados de qualquer lugar do mundo, a qualquer hora, não havendo necessidade de instalação de programas ou de armazenar dados na máquina do usuário.

* O acesso a programas, serviços e arquivos é remoto, através da Internet - daí a alusão à nuvem. O uso desse modelo (ambiente) é mais tolerante à falhas (de hardware) do que o uso de unidades físicas;

* A partir de qualquer computador e em qualquer lugar, pode-se ter acesso a informações, arquivos e programas num sistema único, independente de plataforma. O requisito mínimo é um computador compatível com os recursos disponíveis na Internet. O PC torna-se apenas um chip ligado à Internet — a "grande nuvem" de computadores — sendo necessários somente os dispositivos de entrada (teclado, mouse) e saída (monitor).


Mas nem tudo são flores
-----------------------

Como sabemos, a história da nuvem é recheada de casos de falhas, invasões e vazamento de informações. Recentemente tivemos um caso muito famoso do vazamento de fotos "com conteúdo íntimo" de atrizes e celebridades através da iCloud, que ficou conhecido como "The Fappening" (não pesquise pelo termo se você não estiver em um ambiente seguro). Tivemos também alguns vazamentos de informações da Sony, o vazamento de usuários e senhas do `GMail da Google`_ e o `vazamento da senha de um funcionário do Dropbox`_.


Além de vazamento de informações, também sempre há casos de "mau uso" da nuvem, como o Dropbox que está sendo acusado de, inadvertidamente, estar `compartilhando seus arquivos com outros usuários`_, de `possuir uma forma de autenticação insegura`_ e a existência de um `bug que já apagou mais de 8000 fotos de um único usuários`_.

Como cereja do bolo, a Gartner, empresa de consultoria renomada na área de tecnologia, listou `7 riscos de segurança para a computação na nuvem`_.


Melhorando sua Segurança
------------------------

Como formas de melhorar sua segurança, trazemos algumas alternativas ao Dropbox:

* `SpiderOak`_;
* `TrueCrypt`_;
* `OwnCloud`_ (crie sua própria nuvem).

Mas de que adianta ter seus dados seguros se suas senhas são fracas e repetitivas, certo? Então temos aqui algumas sugestões de como melhorar suas senhas:

* `Heurística para criação de senhas`_;
* Gere sua senha via linha de comando: ``openssl rand -base64 32``;
* "Gere" senhas com o `Hashapass`_;
* Gerencie suas senhas com o `Lastpass`_;
* Gerencie suas senhas com o `1Password`_;
* Gerencie suas senhas com o `KeePass`_;

Mas muitas vezes, nem mesmo a senha mais segura é o suficiente, então lembre de utilizar a autenticação em dois passos nos sites que suportam essa funcionalidade:

* `O Google`_;
* `O Facebook`_;
* `O Twitter`_;
* `E diversos outros`_.

Além disso, o Google também permite o uso de `uma senha por dispositivo/aplicação`_!

E Fora da Nuvem
---------------

Okay, agora que você está relativamente seguro na nuvem, vamos nos manter seguros em casa e no trabalho? Muito bem, então comece a encriptar seus dados localmente com as seguintes ferramentas:

* MacOS: `FileVault`_;
* Windows: `BitLocker`_;
* Linux: Nativo, pode ser habilitado durante a instalação.

Demais links
------------

* `OpenID`_;
* `oAuth`_;
* `Histórico de Localização do Google`_;
* Aplicativo `Authy`_;
* `Prism-Break`_;
* `Hide My Ass`_;



.. container:: panel-body bg-info

        **Musicas**:

        Todas as músicas deste episódio são do album `Straw Fields`_ do projeto `Rolemusic`_ e estão sob a licença `Creative Commons by 4.0`_.


.. .. Links Gerais
.. _Hack 'n' Cast: /pt/category/hack-n-cast
.. _E-mail: mailto: hackncast@gmail.com
.. _Twitter: http://twitter.com/hackncast
.. _Facebook: http://facebook.com/hackncast
.. _Feed: http://feeds.feedburner.com/hack-n-cast
.. _Podflix: http://podflix.com.br/hackncast/
.. _iTunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846?l=en
.. _Pocket Casts: http://pcasts.in/hackncast
.. _Google Groups: https://groups.google.com/forum/?hl=pt-BR#!forum/hackncast

.. Convidado
.. _Jorge: https://twitter.com/JFCostta
.. _SciCast: http://www.scicast.com.br/

.. Falhas de Segurança
.. _GMail da Google: http://meiobit.com/297666/credenciais-de-5-milhoes-de-contas-google-foram-publicadas/
.. _compartilhando seus arquivos com outros usuários: http://paranoia.dubfire.net/2011/04/how-dropbox-sacrifices-user-privacy-for.html
.. _vazamento da senha de um funcionário do Dropbox: http://www.infoworld.com/article/2617858/malware/dropbox-blames-employee-account-breach-for-spam-attack.html
.. _possuir uma forma de autenticação insegura: http://dereknewton.com/2011/04/dropbox-authentication-static-host-ids/
.. _bug que já apagou mais de 8000 fotos de um único usuários: https://medium.com/@jan.curn/how-bug-in-dropbox-permanently-deleted-my-8000-photos-cb7dcf13647b
.. _7 riscos de segurança para a computação na nuvem: http://www.infoworld.com/article/2652198/security/gartner--seven-cloud-computing-security-risks.html

.. Ferramentas
.. _SpiderOak: https://spideroak.com/signup/referral/ab8fa2ff30da02c01dafa207e4f45080/
.. _TrueCrypt: http://truecrypt.sourceforge.net/
.. _OwnCloud: https://owncloud.com/
.. _FileVault: http://en.wikipedia.org/wiki/FileVault
.. _BitLocker: http://en.wikipedia.org/wiki/BitLocker

.. Tecnicas
.. _Heurística para criação de senhas: http://www.efetividade.net/2007/06/senhas-internet.html
.. _Hashapass: http://www.hashapass.com/pt-BR/index.html
.. _Lastpass: https://lastpass.com/
.. _1Password: https://agilebits.com/onepassword
.. _KeePass: http://keepass.info

.. Two-factor-authentication
.. _O Google: https://www.google.com/landing/2step
.. _O Facebook: https://www.facebook.com/notes/facebook-engineering/introducing-login-approvals/10150172618258920
.. _O Twitter: https://blog.twitter.com/2013/getting-started-with-login-verification
.. _E diversos outros: https://twofactorauth.org
.. _uma senha por dispositivo/aplicação: https://support.google.com/mail/answer/1173270?hl=pt

.. Demais links
.. _OpenID: http://openid.net/
.. _oAuth: http://oauth.net/
.. _Histórico de Localização do Google: https://maps.google.com/locationhistory/b/0/
.. _Authy: https://www.authy.com/how-use-authy-google-authenticator
.. _Hide My Ass: https://securemail.hidemyass.com/
.. _Prism-Break: https://prism-break.org/en/

.. Musicas
.. _`Rolemusic`: http://freemusicarchive.org/music/Rolemusic/
.. _`Straw Fields`: http://freemusicarchive.org/music/Rolemusic/Straw_Fields/
.. _`Creative Commons by 4.0`: http://creativecommons.org/licenses/by/4.0/
