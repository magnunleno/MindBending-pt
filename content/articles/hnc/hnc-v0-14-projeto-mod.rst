Hack 'n' Cast v0.14 - Projeto MOD
#################################
:date: 2015-05-28 00:11
:authors: Magnun
:category: Hack 'n' Cast
:tags: hardware, pedaleira, pedal, arduino, dsp, mod, projeto, gnu/linux, lv2, hacklab, python, tornado, nginx, arch, pacman
:image: /images/hack-n-cast/v0.x/v0.14-cover-sqr.jpg
:length: 76765450
:duration: 79:11
:podcast: http://archive.org/download/HNC.v0.14-Projeto-MOD/HNC.v0.14-Projeto-MOD.mp3
:podcastembed: http://archive.org/embed/HNC.v0.14-Projeto-MOD/HNC.v0.14-Projeto-MOD.mp3
:description: Todo músico que entende um pouco de tecnologia já se irritou com a necessidade de comprar diversos hardwares para melhorar o som produzido pelo seu instrumento. Mas e se existisse um hardware único que pudesse programado e atualizado de forma a atender todas as suas necessidades? Então, agora ele existe...

De forma sucinta, o projeto MOD é um processador de sons digitais 100% customizável, com suporte a diversos instrumentos (não somente instrumentos de corda) e foi idealizado pelo brasileiro Gianfranco Ceccolini. Atualmente o Projeto MOD roda sobre GNU/Linux (Kernel RT) e está em fase de `pre-venda no site do projeto`_ pelo valor de U$349 (mais frete). Veja alguns vídeos de demonstração na `seção de vídeos do Portal MOD`_ e na `página do Kickstarter`_.

Prestem muita atenção nas vírgulas sonoras e viradas deste episódio, pois todas foram feitas por usuários do MOD.

.. image:: {filename}/images/hack-n-cast/v0.x/v0.14-cover-wide.jpg
        :target: {filename}/images/hack-n-cast/v0.x/v0.14-cover-wide.jpg
        :alt: Hack 'n' Cast v0.14 - Projeto MOD
        :align: center


Para não perder nenhum episódio siga-nos nas redes sociais (`Twitter`_ e `Facebook`_) ou inscreva-se (`Feed`_, `Podflix`_, `iTunes`_ e `Pocket Casts`_). Você quer colaborar com o Hack 'n' Cast? Sugira um tema, nos ajude a produzir uma pauta ou participe conosco! Basta entrar em contato por `E-mail`_, `Facebook`_ ou `Twitter`_. E agora temos a nossa lista de discussão no `Google Groups`_!

.. more

.. podcast:: HNC.v0.14-Projeto-MOD
        :rss: http://feeds.feedburner.com/hack-n-cast
        :itunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846


Tá Mas e Daí?
=============

Claro que ao primeiro ver esse projeto pode não parecer grande coisa, mas vamos explicar melhor. Imagine um "pedalzinho" (similar aos pedais de efeitos de guitarra que você está acostumado a ver) mas que por dentro funciona como diversos pedais intercomunicados da maneira que você quiser. Não entendeu? Veja a imagem abaixo:

.. image:: {filename}/images/hack-n-cast/v0.x/conexoes-mod.png
    :target: {filename}/images/hack-n-cast/v0.x/conexoes-mod.png
    :align: center
    :alt: Conexões MOD

Impressionado? Mas isso não é tudo, agora imagine que cada "plugin" (nome dado a cada "caixinha" de efeitos/distorções) pode ser atualizado ou instalado via internet. Melhora ainda, você pode programar seus próprios plugins! E no final, ainda temos a característica social. Cada plugins que você escreve, ou pedalboard que você monta pode ser compartilhado com a comunidade e instalado em um único clique. Veja `esse link para ver os diversos pedalboards compartilhados`_ atualmente e `este link para os diversos plugins existentes`_.

Não satisfeito? Então vou jogar a pá de cal em todos os outros pedais/pedaleiras existentes. O Projeto MOD roda sobre GNU/Linux (mais especificamente o Arch Linux), utiliza como servidor de apresentação o NGINX e como servidor de aplicação o Tornado (Python). O MOD visa ser a última pedaleira que você precisará comprar, pois todas as novas funcionalidades (efeitos, distorções e etc) serão entregues via atualização de software (inclusive de maneira social) e quando da necessidade de upgrade de hardware, todo o projeto elétrico do projeto MOD foi feito pensando em possuir partes intercambiáveis. Além disso uma das premissas do projeto MOD é rodar 100% sobre Hardware Aberto e utilizar apenas Software Livre!

Para empolgar, que tal um vídeozinho?

.. vimeo:: 92739423
    :align: center
    :width: 500
    :height: 375


História
========

A trajetória do MOD começou em 2008. Movido pela insatisfação com os pedais/pedaleiras existentes e pela imposição de upgrades quando precisa-se de novos efeitos, Gianfranco Ceccolini resolveu projetar uma pedaleira digital que desse mais liberdade para os músicos. Gian se associou à Angoera Sistemas Eletrônicos e ambos começaram a trabalhar no primeiro protótipo, baseado em um DSP.

Primeiro Protótipo
------------------

A primeira tentativa de protótipo utilizou inicialmente como hardware base um `SHARC da Analog Devices`_ porém, após dificuldades com o `uclinux`_, tomou-se a decisão de mudar o hardware base para `Blackfin`_ (também da Analog Devices). Entretanto, o Blackfin não suportava o ponto flutuante e não havia nada nativo que auxiliava a produção de efeitos sonoros.

.. figure:: {filename}/images/hack-n-cast/v0.x/mod-proto-01.jpg
    :target: {filename}/images/hack-n-cast/v0.x/mod-proto-01.jpg
    :alt: Projeto MOD - Primeiro Protótipo
    :align: center

    Primeiro Protótipo

O desenvolvimento seguiu em ritmo lento até 2010, quando o projeto foi contemplado pelo Programa Prime e o primeiro protótipo foi finalizado.

Segundo Protótipo
-----------------

Por influências do `PureDyne`_ o time de desenvolvimento se focou em trocar o DSP por uma arquitetura baseada em PC e GNU/Linux. Coincidentemente este foi o ano em que começaram a surgir as placas `Mini-ITX`_. 

.. figure:: {filename}/images/hack-n-cast/v0.x/mod-proto-02.jpg
    :target: {filename}/images/hack-n-cast/v0.x/mod-proto-02.jpg
    :alt: Projeto MOD - Segundo Protótipo
    :align: center

    Segundo Protótipo

Com as mudança de arquitetura (DSP para x86) e de software (controlador para Sistema Operacional) as possibilidades se tornaram infinitas e o projeto deixou de ser um simples pedal para ser uma pedaleira, ou seja, uma grafo de efeitos interconectados.

No início de 2012, já com uma nova versão do protótipo funcionando, o `Hacklab`_, empresa de desenvolvimento de software, com vasta experiência em desenvolvimento web e software livre, juntou-se à empreitada. Nasceram a interface de construção de pedaleiras, o `MOD Social`_ e o `MOD Cloud`_.

Neste protótipo ainda era utilizado uma conexão USB Serial para realizar a interface de configuração da pedaleira. Posteriormente a conexão USB Serial foi trocada para rede TCP/IP e com o auxílio do `Hacklab`_ foi criada uma nova interface mais amigável, visualmente agradável e bem executada, além de estar disponível para acesso via todos os tipos de dispositivos que possuem um navegador baseado em `Webkit`_. Após algumas melhorias surgiu o "primeiro" produto, o MOD Quadra.

MOD Quadra
----------

O MOD Quadra surgiu em 2013 e, em setembro deste ano, este produto foi lançado oficialmente durante a ExpoMusic Brasil. A repercussão foi excelente, centenas de curiosos, jornalistas e músicos passaram pelo estande do MOD e ficaram muito entusiasmados com o que viram. Em outubro do mesmo ano, o MOD Quadra começou a ser comercializado e o que era uma ideia virou, finalmente, um produto!

.. figure:: {filename}/images/hack-n-cast/v0.x/mod-quadra.jpg
    :target: {filename}/images/hack-n-cast/v0.x/mod-quadra.jpg
    :alt: Projeto MOD Quadra
    :align: center

    Projeto MOD Quadra

Demais Links
------------

- `Kernel RT`_;
- `LV2`_;
- `Jack`_;
- `NGINX`_;
- `Tornado`_;
- `Arch Linux`_;
- `LADSPA`_;
- `RDF Turtle`_;
- `LILV (Library to manage LV2 plugins)`_;
- `Portal MOD no GitHub`_;
- `Linux Audio Community`_;


Créditos Das Viradas e Vírgulas Sonoras
---------------------------------------

Todas as vírgulas sonoras e viradas utilizadas nesse episódios foram obtidas no site do portal MOD (`MOD Social`_) sob a licença Creative Commons.

- `Hoedown por Kleber K. Shima`_;
- `Bass Fuzz por Kleber K. Shima`_;
- `Distortion por Kleber K. Shima`_;
- `LeDamien por Gianfranco Ceccolini`_;
- `Caio willi por Gianfranco Ceccolini`_;
- `Live Guitar por Breno Ghiorzi`_;
- `Mesa + delay + clean cab por Niper`_;
- `Repeat por Habacuque`_;
- `Wah + Modulation Reverb por Asa`_;

.. class:: panel-body bg-info

        **Musicas**: Toda a trilha sonora deste episódio é composta por canções do album `Okay! Okay!`_ da Banda `Break The Bans`_, que está disponível sob a licença `Creative Commons by 4.0`_.

.. Links Gerais
.. _Hack 'n' Cast: /pt/category/hack-n-cast
.. _E-mail: mailto: hackncast@gmail.com
.. _Twitter: http://twitter.com/hackncast
.. _Facebook: http://facebook.com/hackncast
.. _Feed: http://feeds.feedburner.com/hack-n-cast
.. _Podflix: http://podflix.com.br/hackncast/
.. _iTunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846?l=en
.. _Pocket Casts: http://pcasts.in/hackncast
.. _Google Groups: https://groups.google.com/forum/?hl=pt-BR#!forum/hackncast

.. _pre-venda no site do projeto: http://portalmod.com/store
.. _seção de vídeos do Portal MOD: http://portalmod.com/blog/category/videos/
.. _página do Kickstarter: https://www.kickstarter.com/projects/modduo/mod-duo-the-limitless-multi-effects-pedal/description
.. _esse link para ver os diversos pedalboards compartilhados: http://portalmod.com/social
.. _este link para os diversos plugins existentes:  http://portalmod.com/plugins
.. _SHARC da Analog Devices: http://www.analog.com/en/products/processors-dsp/sharc.html
.. _uclinux: http://www.uclinux.org/
.. _Blackfin: http://www.analog.com/en/products/processors-dsp/blackfin.html
.. _PureDyne: http://puredyne.org/about.html
.. _Mini-ITX: http://en.wikipedia.org/wiki/Mini-ITX
.. _MOD Social: http://portalmod.com/social
.. _MOD Cloud: http://cloud.portalmod.com/
.. _Hacklab: http://hacklab.com.br/
.. _Webkit: http://cloud.portalmod.com/

.. Demais Links
.. _Kernel RT: https://rt.wiki.kernel.org/index.php/Main_Page
.. _LV2: http://lv2plug.in/
.. _Jack: http://jackaudio.org/
.. _NGINX: http://nginx.org/
.. _Tornado: http://www.tornadoweb.org/en/stable/
.. _Arch Linux: https://www.archlinux.org/
.. _LADSPA: http://www.ladspa.org/
.. _RDF Turtle: http://en.wikipedia.org/wiki/Turtle_%28syntax%29
.. _LILV (Library to manage LV2 plugins): http://drobilla.net/software/lilv/
.. _Portal MOD no GitHub: https://github.com/portalmod
.. _Linux Audio Community: http://www.linuxaudio.org/

.. Virgulas
.. _Hoedown por Kleber K. Shima: http://portalmod.com/social/pedalboard/?5432bf48f53ed50311cdff1e
.. _Bass Fuzz por Kleber K. Shima: http://portalmod.com/social/pedalboard/?53a203aff53ed545e28206d3
.. _Distortion por Kleber K. Shima: http://portalmod.com/social/pedalboard/?53a20221f53ed545e28206cf
.. _LeDamien por Gianfranco Ceccolini: http://portalmod.com/social/pedalboard/?5424bd9ff53ed512f1d11fb0
.. _Caio willi por Gianfranco Ceccolini: http://portalmod.com/social/pedalboard/?54664661f53ed5701a7f27f6
.. _Live Guitar por Breno Ghiorzi: http://portalmod.com/social/pedalboard/?53f25c23f53ed53adc3097ce
.. _Mesa + delay + clean cab por Niper: http://portalmod.com/social/pedalboard/?5390f7dff53ed56a882b590c
.. _Repeat por Habacuque: http://portalmod.com/social/pedalboard/?538e3d40f53ed52b336a292f
.. _Wah + Modulation Reverb por Asa: http://portalmod.com/social/pedalboard/?53b6ff50f53ed56c791bdf10

.. Musicas
.. _`Creative Commons by 4.0`: http://creativecommons.org/licenses/by/4.0/
.. _Okay! Okay!: http://freemusicarchive.org/music/Break_The_Bans/Okay_Okay/
.. _Break The Bans: http://freemusicarchive.org/music/Break_The_Bans
