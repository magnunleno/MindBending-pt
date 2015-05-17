Hack 'n' Cast v0.2 - HTML & CSS
###############################
:date: 2014-06-13 04:59
:category: Hack 'n' Cast
:tags: hack 'n' cast, hacker, podcast, beta, html, css, black sabbath
:image: /images/logos/HNC-beta.png
:length: 60669449
:duration: 63:07
:podcast: http://archive.org/download/HnC.v0.2-HTML-e-CSS/HnC.v0.2-HTML-e-CSS.mp3
:podcastembed: https://archive.org/embed/HnC.v0.2-HTML-e-CSS/HnC.v0.2-HTML-e-CSS.mp3
:podcast_old: True
:description: O HTML é co-responsável pela grande revolução que foi a internet. Junte-se a trupe do Hack 'n' Cast e descubra se isso é uma tecnologia, doença ou solução. E saiba porquê você deve usar um guarda-chuva ao escrever CSS.

No episódio de hoje do `Hack 'n' Cast`_ voltamos com tudo e vamos falar sobre a linguagem de programação (sic!) dos verdadeiros `hackers`_, o HTML! Assim como visto na TV...

.. figure:: {filename}/images/html-css/davi-o-hacker.jpg
        :target: {filename}/images/html-css/davi-o-hacker.jpg
        :alt: Davi o Hacker
        :align: center

        `Davi o Hacker`_

Também neste episódio, inauguramos a seção de notícias, dicas e *Bug Reports* deste *podcast*! Para não perder nenhum episódio siga-nos nas redes sociais (`Twitter`_ e `Facebook`_) ou inscreva-se (`Feed`_, `Podflix`_, `iTunes`_ e `Pocket Casts`_).

.. more

.. podcast:: HnC.v0.2-HTML-e-CSS
        :rss: http://feeds.feedburner.com/hack-n-cast
        :itunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846

Introdução
==========

Todos os dias você cruza com centenas de tipos diferentes de documentos impressos, cartazes, outdoors, folhetos distribuídos no semáforo, (agora nesta época) santinho de políticos, jornais, agenda de ónibus/metrô, revistas, livros e etc. Todos estes tipos de documentos compartilham um conceito, o uso de palavras, imagens, gráficos ou tabelas para apresentar informações, e compartilham também uma estrutura básica: título, descrição e texto. Esta é a forma de comunicação que o ser humano está acostumado a lidar, entretanto, a Internet (*World Wide Web*) não é composta apenas de humanos, mas de computadores/servidores. A Internet é como um mar de documentos que se interligam, e para permitir que tanto a máquina quanto o ser humano pudesse entender a semântica desses documentos foi necessário criar algo que integrasse a estrutura semântica compreendida pela máquina e pelo ser humano. Este algo é a linguagem HTML.

HTML
====

HTML é uma linguagem de marcação na qual você escreve utilizando elementos HTML, que consistem de *tags* circundadas por colchetes angulares (sinal de menor/maior). Geralmente as *tags* HTML possuem pares, sendo que a primeira a aparecer é a *tag* de abertura e segunda é a *tag* de fechamento. Para diferenciar uma *tag* de abertura de uma *tag* de fechamento, esta última possui uma barra logo após o sinal de menor.

.. image:: {filename}/images/html-css/xkcd-1367-installing.png
        :target: {filename}/images/html-css/xkcd-1367-installing.png
        :align: center
        :alt: XKCD 1367

Os elementos HTML são as peças que constroem sites, eles criam documentos estruturados denotando a semântica do texto, como *headings*, parágrafos, listas, citações e outros itens. O propósito de um navegador é ler o HTML, interpretar as *tags* e compor uma página legível para humanos.


Todo código HTML deve possuir pelo menos estes quatro "pedaços":

* ``<!DOCTYPE>``: O *doctype* não é uma *tag* em si, na verdade é uma instrução especial. Ela indica ao navegador qual a versão do HTML este arquivo está utilizando. Antigamente a *doctype* era complexa e recheada de informações, porém, com o HTML5, esta *tag* foi extremamente simplificada.
* ``<html>``: Esta *tag* é a *tag* raiz (ou *tag* pai) de todo o documento que iremos criar. Pense nela como o próprio documento HTML (por isso a *tag* se chama *html*).
* ``<head>``: A *tag head* (assim como sua *tag* irmã *body*) devem estar dentro da *tag* HTML.  Nela são definidas as metainformações sobre nossa página ou informações que são importantes somente para o *browser*. Nenhuma informação da *tag* *head* serão exibidas na área de documento.
* ``<body>``: A *tag body* é o corpo do nosso documento, ela possui todos os dados textuais que serão exibidos na página.

Abaixo um exemplo de uma página HTML:

.. code-block:: html

        <!DOCTYPE html>
        <html>
        <head>
            <title>Página de Exemplo</title>
            <meta charset=”utf-8”>
        </head>
        <body>
            <h1>Página de exemplo</h1>
            <p>Este é um parágrafo</p>
        </body>
        </html>

Uma *tag* HTML pode conter um conteúdo (``<nome_de_tag>conteúdo da tag</nome_de_tag>``) e vários atributos (``<nome_de_tag atributo1=”valor”>conteúdo da tag</nome_de_tag>``), no formato chave/valor. Alguns atributos são específicos de algumas *tags*, enquanto outros atributos valem para qualquer *tag* e possuem um significado específico:

CSS
===

É uma linguagem de folhas de estilo utilizada pra descrever a aparência e formatação de um documento escrito em uma linguagem de marcação. Apesar de ser amplamente utilizada para a linguagem HTML, ela também pode ser associada a outros documentos como XML, SVG e XUL.

.. figure:: {filename}/images/html-css/css-blinds.gif
        :target: {filename}/images/html-css/css-blinds.gif
        :align: center
        :alt: CSS Blinds

        Como eu me sinto corrigindo o CSS dos outros

O CSS foi criado primariamente para permitir a separação do conteúdo e da semântica de um documento de sua apresentação (cor, fonte, *layout*, posicionamento e etc).

A sintaxe do CSS é composta por seletores e regras, do tipo chave-valor. O seletor funciona como uma expressão que “seleciona” um grupo/tipo de elementos HTML, por tipo, classe ou id. As regras são aplicadas dentro de um seletor, e possuem uma estrutura de chave-valor, isto é, um atributo (``font-family``, ``color``, ``font-size``) e o valor a ser atribuído (``sans-serif``, ``#ff0000``, ``12px``).

.. image:: {filename}/images/html-css/css-selector.gif
        :target: {filename}/images/html-css/css-selector.gif
        :alt: CSS Selector
        :align: center

A inclusão de um arquivo CSS deve ser feito da seguinte maneira:

.. code-block:: html

        <link href=”caminho/arquivo.css” rel=”stylesheet”>

Entretanto, é possível embutir o CSS dentro de uma página HTML usando a *tag* HTML *style:*

.. code-block:: html

    <style type=”text/css”>
    // CSS aqui
    </style>

Citados no Episódio
===================

* Artigo: `Ragget on HTML`_
* Artigo: `John McCarthy`_
* Artigo: `Lista de Tags HTML`_
* Artigo: `Diversas ferramentas no site Web Social Dev`_
* Artigo: `Lista com os melhores Frameworks CSS (também do Web Social Dev)`_
* Artigo: `Mozilla Foundation - Introduction to HTML`_
* Artigo: `Uma em cada dez pessoas pensa que HTML é uma doença`_
* Artigo: `Por que o cursor do mouse é inclinado? Eis o motivo`_
* Artigo: `Tron Interface Design`_
* Curso: `CodeCademy - HTML & CSS`_
* Curso: `Apostila da Caelum - Desenvolvimento Web com HTML, CSS e JavaScript`_
* Site: `Akademia Kolaborativa - Webdev`_
* Site: `Maujor`_
* Site: `Tableless`_
* Site: `Cosmos - Uma Odisseia no Espaço-Tempo`_
* Projeto: `OpenRA`_
* Projeto: `Phonegap`_
* Imagem: `Estação de trabalho NeXT de Tim Berners Lee`_
* Imagem: `Neil deGrasse Tyson`_
* Vídeo: `Silicon Valley 1x01 - Steve Jobs was a poser`_


Livros
======

.. class:: panel-body bg-info

        Na compra de qualquer livro na Novatec utilize o código **MINDBENDING** para conseguir 20% de desconto.

* `Programaçao Profissional com HTML5`_
* `Smashing HTML5`_
* `O’Reilly - HTML5 Entendendo e Executando`_
* `CSS - O Manual que Faltava`_
* `O’Reilly - CSS Cookbook`_
* `Smashing CSS`_
* `Construindo Sites com CSS e (X)HTML`_
* `HTML5 - A Linguagem de Marcação que Revolucionou a Web`_


Trilha Sonora
=============
A trila deste episódio é uma homenagem ao Black Sabbath:

* Symptom Of The Universe (Sabotage - 1975)
* The Wizard (Black Sabbath - 1970)
* Paranoid (Paranoid - 1970)
* Iron Man (Paranoid - 1970)
* Supernaut (Black Sabbath 4 - 1972)
* Sabbath Bloody Sabbath (Sabbath Bloody Sabbath 1973)
* Sabbra Cadabra (Sabbath Bloody Sabbath 1973)
* War Pigs (Paranoid - 1970)
* Turn Up The Night (Mob Rules - 1981)
* Country Girl (Mob Rules - 1981)
* Loner (13 - 2013)
* Peace Of Mind (13 - 2013)

Agradecimentos
==============

Agradecemos a todo o *feedback* recebido (por e-mail, comentário e twitter). Agradecemos especialmente ao Diego "R4bugento" Sorrilha pela colaboração com a pauta!

Você quer colaborar com o Hack 'n' Cast? Sugira um tema, nos ajude a produzir uma pauta ou participe conosco! Entre em contato por `E-mail`_, `Facebook`_ ou `Twitter`_.

Licença
=======

O Hack 'n' Cast é distribuído sobre a licença `Creative Commons Attribution-ShareAlike 4.0 International`_ (CC BY-SA 4.0). Você é livre para compartilhar, copiar, redistribuir (em qualquer mídia ou formato), adaptar, remixar transformar ou ampliar esse material, contato que sejam mantidas as atribuições e os autores sejam devidamente citados e que esta mesma licença seja utilizada nos trabalhos derivados.

.. _hackers: /pt/hack-n-cast-v01-cultura-hacker
.. _Hack 'n' Cast: /pt/sobre-hack-n-cast
.. _Davi o Hacker: http://vidadeprogramador.com.br/2014/05/07/davi-e-um-hacker-de-html-geracao-brasil/
.. _Estação de trabalho NeXT de Tim Berners Lee: http://thoth3126.com.br/wp-content/uploads/2014/03/www-First_Web_Server.jpg
.. _Ragget on HTML: http://www.w3.org/People/Raggett/book4/ch02.html
.. _Creative Commons Attribution-ShareAlike 4.0 International: http://creativecommons.org/licenses/by-sa/4.0/

.. _Uma em cada dez pessoas pensa que HTML é uma doença: http://www.tecmundo.com.br/pesquisa/52100-uma-em-cada-dez-pessoas-pensa-que-html-e-uma-doenca.htm
.. _Por que o cursor do mouse é inclinado? Eis o motivo: http://gizmodo.uol.com.br/por-que-cursor-mouse-inclinado/
.. _OpenRA: http://www.openra.net/
.. _Cosmos - Uma Odisseia no Espaço-Tempo: http://www.cosmosontv.com/

.. Social
.. _E-mail: mailto: hackncast@gmail.com
.. _Twitter: http://twitter.com/hackncast
.. _Facebook: http://facebook.com/hackncast
.. _Feed: http://feeds.feedburner.com/hack-n-cast
.. _Podflix: http://podflix.com.br/hackncast/
.. _iTunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846?l=en
.. _Pocket Casts: http://pcasts.in/hackncast

.. Links
.. _John McCarthy: http://en.wikipedia.org/wiki/John_McCarthy_%28computer_scientist%29
.. _Lista de Tags HTML: http://www.htmldog.com/reference/htmltags/
.. _Diversas ferramentas no site Web Social Dev: http://websocialdev.com/melhores-ferramentas-para-auxliar-o-desenvolvimento-front-end/
.. _Lista com os melhores Frameworks CSS (também do Web Social Dev): http://websocialdev.com/lista-com-os-melhores-frameworks-css/
.. _CodeCademy - HTML & CSS: http://www.codecademy.com/pt-BR/tracks/web?jump_to=5024844597a4040002069e67
.. _Apostila da Caelum - Desenvolvimento Web com HTML, CSS e JavaScript: http://www.caelum.com.br/apostila-html-css-javascript/
.. _Mozilla Foundation - Introduction to HTML: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Introduction
.. _Akademia Kolaborativa - Webdev: http://akademia-webdev.forumeiros.com/
.. _Maujor: http://www.maujor.com/index.php
.. _Tableless: http://tableless.com.br/
.. _Phonegap: http://phonegap.com/
.. _Neil deGrasse Tyson: http://i0.kym-cdn.com/entries/icons/original/000/007/508/watch-out-we-got-a-badass-over-here-meme.png
.. _Silicon Valley 1x01 - Steve Jobs was a poser: https://www.youtube.com/watch?v=PodwJmtn-iQ
.. _Tron Interface Design: http://jtnimoy.net/workviewer.php?q=178

.. Livros
.. _Programaçao Profissional com HTML5: http://www.submarino.com.br/produto/112690739/livro-programacao-profissional-em-html-5-?opn=AFLNOVOSUB&WT.mc_id=lomadeexml&epar=lomadee&utm_campaign=lomadee&utm_medium=lomadee&utm_source=lomadee
.. _Smashing HTML5: http://www.submarino.com.br/produto/111165191/smashing-html5-tecnicas-para-a-nova-geracao-da-web-?opn=AFLNOVOSUB&WT.mc_id=lomadeexml&epar=lomadee&utm_campaign=lomadee&utm_medium=lomadee&utm_source=lomadee
.. _O’Reilly - HTML5 Entendendo e Executando: http://www.submarino.com.br/produto/110531638/livro-html-5-entendendo-e-executando?epar=lomadee&opn=AFLNOVOSUB&utm_campaign=lomadee&utm_medium=lomadee&utm_source=lomadee
.. _CSS - O Manual que Faltava: http://www.submarino.com.br/produto/7121066/livro-css-o-manual-que-faltava?opn=AFLNOVOSUB&WT.mc_id=lomadeexml&epar=lomadee&utm_campaign=lomadee&utm_medium=lomadee&utm_source=lomadee
.. _O’Reilly - CSS Cookbook: http://www.submarino.com.br/produto/7288845/livro-css-cookbook-solucoes-rapidas-para-problemas-comuns-com-css?epar=lomadee&opn=AFLNOVOSUB&utm_campaign=lomadee&utm_medium=lomadee&utm_source=lomadee
.. _Smashing CSS: http://www.livrariasaraiva.com.br/produto/3674334?utm_source=lomadee&utm_campaign=lomadee&utm_medium=lomadee&PAC_ID=30393
.. _Construindo Sites com CSS e (X)HTML: http://www.novatec.com.br/livros/csshtml/
.. _HTML5 - A Linguagem de Marcação que Revolucionou a Web: http://www.novatec.com.br/livros/html5/
