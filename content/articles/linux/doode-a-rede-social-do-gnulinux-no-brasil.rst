Doode: A rede social do GNU/Linux no Brasil
###########################################
:date: 2011-07-30 13:04
:category: Linux
:tags: doode, gtk, python, qt, rede, social, twitter
:image: /images/doode-sqr.png

Olá leitores desse blog! Este é um post curto mas muito importante. O nosso colega Vitor Micillo, do blog O Oráculo, liberou no dia 03/07 o seu projeto ambicioso, o `Doode`_. Agora ele precisa da ajuda de todos os usuários GNU/Linux para atingir um objetivo ainda mais ambicioso: Colocar o Doode no repositório oficial do Ubuntu e futuramente ser um programa padrão desta plataforma.

Ok, vocês devem estar perdidos pensando: "Por que uma rede social precisa estar no repositório do Ubuntu?". Vou explicar, mas primeiro vamos esclarecer para quem ainda nao conhece, o que é o Doode.

.. image:: {filename}/images/doode_center.png
        :target: {filename}/images/doode_center.png
        :alt: Doode Logo
        :align: center

.. more

O Que é O Doode
---------------

O Doode começou como um projeto de fim de semana do nosso colega Vitor Micillo e tinha como objetivo criar um misto de rede social e twitter dedicada aos usuários GNU/Linux. O nome veio da gíria dos surfistas americanos e havaianos que significa amigo.

O Doode levou 1 ano e 6 meses para ser concluí­do. Foi feito totalmente em Software Livre e de Código Aberto e se baseia em uma mistura do CMS `floopo`_ e o renomado sistema de blogs `Wordpress`_. Mas simplesmente juntar essas duas ferramentas não foi o suficiente.

Para garantir uma melhor segurança foi utilizado no projeto o sistema de criptografia do IonCube (disponível no pacote `Zend-PHP`_), alguns scripts em Python para comunicação e proteção do Banco de Dados MySQL, além da alteração de todo o sistema de autenticação de usuário. Em resumo, a parte de infra-estrutura foi feita basicamente em PHP, ajax, jQuery, MySql e Python enquanto para o design foram utilizadas as ferramentas Inkscape e GIMP.

E o Ubuntu?
-----------

O Doode conseguiu visibilidade! Em menos de um mês o projeto já conta com mais de 1300 usuários cadastrados. O autor recentemente foi entrevistado pela revista `Info`_ e entrou em contato com a `Canonical`_. Agora ele está em numa corrida contra o tempo para conseguir 50.000 membros para sua rede social, e ainda desenvolver um aplicativo em Python e GTK e QT para possibilitar seu acesso via Desktop. Se tudo isso for concluí­do à tempo o projeto se tornará uma aplicação padrão da distribuição e virá pré-instalado.

Como Eu Posso Ajudar
--------------------

Existem tês formas de contribuir: a primeira é se `cadastrar`_ e utilizar a rede social (ela possui integração com o Twitter) para atingirmos os 50.000 usuários; a segunda é ajudar a divulgar o projeto (e a rede social) para seus amigos e colegas; a terceira e última é ajudar no desenvolvimento do aplicativo para Desktop do Doode.

Para isso precisamos apenas de pessoas que tenham conhecimento Python e que tenham interesse de trabalhar no desenvolvimento de uma aplicação que poderá ter patrocínio da Canonical. Não é obrigatório ter conhecimento em GTK, mas se você estiver disposto e quiser aprender iremos ajudar, então entre em contato!

Então pessoal, o que vocês estão esperando? Cadastrem-se logo! :D

.. _Doode: http://doode.com.br/
.. _|image1|: {filename}/images/doode_center.png
.. _floopo: http://www.floopo.com/
.. _Wordpress: http://wordpress.org/
.. _Zend-PHP: http://www.zend.com/en/
.. _Info: http://info.abril.com.br/
.. _Canonical: http://www.canonical.com/
.. _cadastrar: http://doode.com.br/signup
