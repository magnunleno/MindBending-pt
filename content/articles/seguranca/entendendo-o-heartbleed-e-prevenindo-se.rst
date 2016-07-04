Entendendo o Heartbleed e Previnendo-se
#######################################
:date: 2014-04-10 11:26
:category: Segurança
:tags: segurança, heartbleed, linux, ubuntu, debian, centos, fedora, redhat, ssl, tls, http
:image: /images/logos/heartbleed.jpg
:description: O Heartbleed possivelmente é a falha de segurança que mais comprometeu a Web nos últimos anos. Com esta falha é possível obter qualquer informação que esteja armazenada na memória do servidor, desde usuário, senha, certificados ou conteúdo.

Há um tempo nos acostumamos a pensar que, se estamos em um site com HTTPS (Protocolo HTTP encriptado por SSL/TLS) estamos seguros, assim como nossos dados. A criptografia SSL/TLS baseada em certificados supostamente previne qualquer tipo de interceptação de dados entre você e o servidor. Isso até aparecer o `Heartbleed`_.

.. image:: {filename}/images/news/heartbleed.jpg
        :target: {filename}/images/news/heartbleed.jpg
        :alt: Heartbleed
        :align: center

O Heartbleed é uma vulnerabilidade séria que afeta a biblioteca e os softwares de criptografia contidos no OpenSSL. Esta falha permite que informações protegidas sejam roubadas (mesmo em circunstâncias normais de uso) em diversos serviços como web, email, *instant messaging* (IM) e algumas VPNs (*virtual private networks*).

.. more

Como Funciona
-------------

O Heartbleed bug (erro em código) permite que qualquer um na Internet a ler a memória de sistemas protegidos pela versão falha do software OpenSSL. A falha compromete: a *secret key* utilizada para identificar os provedores de serviço e para encriptar o tráfego, os nomes e senhas de usuários e o próprio conteúdo do site. Permitindo assim o ataque do tipo `eavesdrop`_ (interceptação de comunicações) roubo de dados diretamente do serviço e a impersonificacão do provedor do serviço e do usuário.

Quem é Afetado
--------------

A falha existe na OpenSSL versões 1.0.1 até 1.0.1f (inclusive) e são afetados sistemas distribuídos com estas versões da biblioteca ou com certificados gerados por essas versões da biblioteca. É importante ressaltar que os certificados para SSH não são afetados. Abaixo um lista de distribuições GNU/Linux que são afetadas:

* Debian Wheezy (stable), OpenSSL 1.0.1e-2+deb7u4;
* Ubuntu 12.04.4 LTS, OpenSSL 1.0.1-4ubuntu5.11;
* CentOS 6.5, OpenSSL 1.0.1e-15;
* Fedora 18, OpenSSL 1.0.1e-4;
* OpenBSD 5.3 (OpenSSL 1.0.1c 10 May 2012) and 5.4 (OpenSSL 1.0.1c 10 May 2012);
* FreeBSD 10.0 - OpenSSL 1.0.1e 11 Feb 2013;
* NetBSD 5.0.2 (OpenSSL 1.0.1e);
* OpenSUSE 12.2 (OpenSSL 1.0.1c).

Encontrei orientações de correções para as seguintes distribuições:

* Ubuntu: `USN-2165-1`_;
* Fedora: `CVE-2014-0160`_;
* RedHat: `RHSA-2014-0376`_;
* CentOS: `CESA-2014-0376`_.

Esta vulnerabilidade foi introduzida em Dezembro de 2011 e ficou disponível ao públlico na release 1.0.1 em 14 de Março de 2012. A versão OpenSSL 1.0.1g, liberada em 7 de Abril de 2014 corrige o defeito. Abaixo um detalhamento das versões que possuem a falha:

* OpenSSL 1.0.1 até 1.0.1f (inclusive) são vulneráveis;
* OpenSSL 1.0.1g não está vulnerável;
* OpenSSL 1.0.0 branch não está vulnerável;
* OpenSSL 0.9.8 branch não está vulnerável.

Dada a amplitude da falhar centenas de sites que não são atualizados pode estar vulneráveis. Alguém já se encarregou de fazer uma varredura nos *Top 100* sites da internet, a `lista está disponível aqui`_. Segue alguns destaques:

* yahoo.com;
* imgur.com;
* stackoverflow.com;
* flickr.com;
* addthis.com;
* stackexchange.com;
* xda-developers.com;
* steamcommunity.com;
* duckduckgo.com;
* elegantthemes.com.

Eu Sou Afetado?
---------------

Claro que seu próprio site (ou outro site que você se utiliza) não está na lista, então existem algumas formas de se testar. A primeira delas é via Web utilizando `este site`_. Outras formas, via linha de comado, é utilizando este `script python`_, da seguinte forma:

.. code-block:: bash

        $ python ssltest.py meusite.com 443
        Connecting...
        Sending Client Hello...
        Waiting for Server Hello...
        ... received message: type = 22, ver = 0302, length = 61
        ... received message: type = 22, ver = 0302, length = 3804
        ... received message: type = 22, ver = 0302, length = 331
        ... received message: type = 22, ver = 0302, length = 4
        Sending heartbeat request...
        Unexpected EOF receiving record header - server closed connection
        No heartbeat response received, server likely not vulnerable


.. _Heartbleed: http://heartbleed.com/
.. _eavesdrop: http://en.wikipedia.org/wiki/Eavesdropping
.. _USN-2165-1: http://www.ubuntu.com/usn/usn-2165-1/
.. _lista está disponível aqui: https://github.com/musalbas/heartbleed-masstest/blob/master/top1000.txt
.. _este site: http://filippo.io/Heartbleed/
.. _script python: https://gist.github.com/sh1n0b1/10100394
.. _CVE-2014-0160: https://lists.fedoraproject.org/pipermail/announce/2014-April/003205.html
.. _CESA-2014-0376: http://lists.centos.org/pipermail/centos-announce/2014-April/020249.html
.. _RHSA-2014-0376: https://rhn.redhat.com/errata/RHSA-2014-0376.html
