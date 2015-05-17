Hack 'n' Cast v0.8 - JavaScript
###############################
:date: 2014-12-02 01:06
:category: Hack 'n' Cast
:tags: hack 'n' cast, podcast, beta, javascript, linguagem, programação, história, programação funcional, Dr. Sin
:image: /images/hack-n-cast/v0.x/v0.8-cover-sqr.png
:length: 79033531
:duration: 81:05
:podcast: http://archive.org/download/HNC.v0.8-JavaScript/HNC.v0.8-JavaScript.mp3
:podcastembed: http://archive.org/embed/HNC.v0.8-JavaScript/HNC.v0.8-JavaScript.mp3
:podcast_old: True
:description: JavaScript é uma das poucas linguagens que podem ser consideradas como lingua franca, isto é, que todo programador deveria saber e que uma hora vai acabar lidando com ela.

Hoje no `Hack 'n' Cast`_, com a ajuda do Diego "Boot" (|Twitter Diego|_ e |Facebook Diego|_) e do Átila Camurça (|Twitter Atila|_ e |GitHub Atila|_), falaremos de uma das linguagens utilizadas e incompreendidas, o JavaScript! Desde seu nome (que apesar da referência textual, não possui correlação com Java), áreas de aplicação e funcionamento, esta linguagem sempre foi tratada como um brinquedo ou "ferramenta menor" que serve para criar "pequenos efeitos" em sites. 

.. image:: {filename}/images/hack-n-cast/v0.x/v0.8-cover-wide.png
        :target: {filename}/images/hack-n-cast/v0.x/v0.8-cover-wide.png
        :alt: Hack 'n' Cast v0.8 - JavaScript
        :align: center

Para não perder nenhum episódio siga-nos nas redes sociais (`Twitter`_ e `Facebook`_) ou inscreva-se (`Feed`_, `Podflix`_, `iTunes`_ e `Pocket Casts`_). Você quer colaborar com o Hack 'n' Cast? Sugira um tema, nos ajude a produzir uma pauta ou participe conosco! Basta entrar em contato por `E-mail`_, `Facebook`_ ou `Twitter`_. E agora temos a nossa lista de discussão no `Google Groups`_!

.. more

Introdução
----------

Sabemos que linguagem de programação é quase o mesmo que religião, partido político ou time de futebol, cada um tem uma opinião, uma preferida, um preconceito ou uma rixa. Mas poucas linguagens são tratadas como onipresente e onipotente. Pois a vemos sendo utilizada na web (tanto front-end quanto back-end), em aplicativos moveis, em aplicativos desktops, na comunicação entre sistemas e diversas outras áreas. Esta é uma das poucas linguagens que podem ser consideradas uma “língua franca”. Sim, estamos falando de JavaScript!

.. podcast:: HNC.v0.8-JavaScript
        :rss: http://feeds.feedburner.com/hack-n-cast
        :itunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846

O que é?
--------

O JavaScript é uma linguagem de programação multiparadigmas, dinâmica, interpretada e com sintaxe inspirada no C e Java. Ela é comumente é confundida como parte integrante da suíte Java. Entretanto, JavaScript está para Java como "*Car*" esta para "Carpet", ou seja, não possui nenhuma relação! Por essas e outras ela é `uma das linguagens mais incompreendidas do mundo`_.

Apesar desta linguagem ser tratada como uma linguagem menor ou de pouco importância você está em contato com ela linguagem todo dia e ela facilita muito o seu interfaceamento com o internet. Ela é uma linguagem aberta por natureza, uma vez que você não consegue ocultar o código fonte, aparentemente "simples" mas com recursos poderosos. O conhecimento mais profundo desta tecnologia é uma habilidade importante para qualquer desenvolvedor web ou mobile.

Entretanto, é uma linguagem com comportamentos bem adversos, como a palestra `WAT do Destroy All Software`_ demonstra.

História
--------

A linguagem JavaScript foi criada em 1995 por Brendan Eich, um engenheiro de software da Netscape. Sua primeira release foi no início de 1996. Brendan afirma que levou apenas 10 dias para pensar e criar um protótipo que rodasse no Netscape.

Originalmente a linguagem tinha o nome LiveScript, mas foi trocado para JavaScript, tendo como objetivo uma jogada de marketing devido à crescente popularidade do Java na época. Pouco depois a Microsoft lança uma versão similar para competir com a Netscape. Temendo uma fragmentação e a criação de um monopólio por parte da Microsoft, como já estava ocorrendo com o HTML e o CSS, a Netscape submeteu a linguagem a uma entidade, a `ECMA International`_. Em 1997 foi criado o padrão ECMAScript.

Mais:

- `Java Script - Designing a Language in 10 Days`_;
- `História da World Wide Web (Palestra de 2012 com Timeline)`_;
- `Uma Reintrodução à JavaScript`_;

Características
---------------

Uma das características mais destacadas no JavaScript é o suporte a `Multi-Paradigmas`_ e as First-class Functions, ou seja, a capacidade de tratar funções como objetos nativos da linguagem, podendo, por exemplo, serem passadas como como parâmetros de outras funções. Além disto, esta linguagem possui uma ótima implementação de paralelismo e comportamento assíncrono, além de operar no *Client Side*, reduzindo assim o consumo de recursos no servidor.

Esta linguagem muitas vezes é criticada por não possuir "classes" expressamente ditas, porém esta funcionalidade é entregue por uma outra funcionalidade chamada `object prototypes`_. Apesar de sua principal aplicação ser na Web, ela possui usos fora deste universo, `conforme listado aqui`_. 

A linguagem suporta os seguintes tipos nativos:

- Number;
- String;
- Boolean;
- Object;
- Function;
- Array;
- Date;
- RegExp;
- Null;
- NaN;
- Undefined;

Como afirmado anteriormente, todo o padrão e comportamento da linguagem é padronizado pelo ECMA International, diversas empresas ou organizações possuem suas implementações da máquina virtual (também chamado de "motor" JavaScript). Alguns exemplos são:

- `V8`_, implementado pelo Google;
- `SpiderMonkey`_ e `asm.js`_, implementado pela Mozilla/Netscape;
- `Rhino`_, OpenSource mas coordenado pela Mozilla;
- `JavaScriptCore`_ (ou Nitro), implementado pela Apple;
- `KJS`_, implementado pelo Projeto KDE;
- `Chakra`_, implementado pela Microsoft para o Explorer 9;
- `Nashorm`_, implementado pela Oracle.

Para mais informações sobre todo esse "mundo do JavaScript", recomendamos a leitura do artigo The World of ECMAScript, por John Resig.

Em breve será lançado o `ECMAScript 6`_, que trará as seguintes melhoras:

- Suporte a classes;
- Maps e Sets;
- Valores default na passagem de parâmetros;
- Módulos;
- Funções anônimas;
- Melhor comportamento do NaN;

Ferramentas, Bibliotecas, IDEs e Frameworks
-------------------------------------------

Bilbiotecas:

- `jQuery`_;
- `JQueryUI`_;
- `Kendo UI`_;

Minimizadores:

- `UglifyJS`_;
- `UglifyJS2`_;

Linguagens que compilam para JavaScript:

- Bryton;
- CoffeeScript;
- TypeScript;
- Opal ;
- `Uma lista mais expandida`_;

IDEs:

- NetBeans;
- Atom;
- Brackets;
- Sublime Text, VIM & EMACS;
- WebStorms JetBrain (Não livre, mas possui licença de estudante);

Hardware:

- `Tessel`_;
- `Espruino`_;

Ferramentas:

- `JSLint`_;
- `JSDB`_;
- `Breach`_;
- `Codepen`_;
- `JSFiddle`_;

Frameworks:

- `AngularJS`_;
- `React`_;
- `BackBoneJS`_;
- `JavaScriptMVC`_;

Exemplos de Códigos
-------------------

O típico *Hello World*.

.. code-block:: javascript

        console.log("Hello World");


Um exemplo de manipulação de listas.

.. code-block:: javascript

        var list = [1, 2, 3, 4, 5];
        for (var i = 0; i < list.length; i++) {
                console.log(i);
        }

Utilização de "Objetos".

.. code-block:: javascript

        var flight = {
                airline: "Oceanic",
                number: 815,
                departure: {
                        IATA: "SYD",
                        time: "2004-09-22 14:55",
                        city: "Sydney"
                },
                arrival: {
                        IATA: "LAX",
                        time: "2004-09-23 10:42",
                        city: "Los Angeles"
                }
        };
        console.log(flight.departure.IATA);

Uso de funções e seus "valores padrões" atuais.

.. code-block:: javascript

        function add(a, b) {
                return a + b;
        }

        var factorial = function factorial(i, a) {
                a = a || 1;
                if (i < 2) {
                        return a;
                }
                return factorial(i - 1, a * i);
        };
        console.log(factorial(4)); // 24


Trecho de código retirado do UnderscoreJS que demonstra todo o poder do JavaScript.

.. code-block:: javascript

        // The cornerstone, an `each` implementation, aka `forEach`.
        // Handles raw objects in addition to array-likes. Treats all
        // sparse array-likes as if they were dense.
        _.each = _.forEach = function(obj, iteratee, context) {
                if (obj == null) return obj;
                iteratee = createCallback(iteratee, context);
                var i, length = obj.length;
                if (length === +length) {
                        for (i = 0; i < length; i++) {
                        iteratee(obj[i], i, obj);
                        }
                } else {
                        var keys = _.keys(obj);
                        for (i = 0, length = keys.length; i < length; i++) {
                        iteratee(obj[keys[i]], keys[i], obj);
                        }
                }
                return obj;
        };


Fontes de Aprendizado
---------------------

Sites, Blogs e Twitters:

- `Página sobre Javscript do MDN (Mozilla Developer Network)`_;
- `Reintrodução ao Javascript`_;
- `Blog Pessoal de Douglas Crockford`_, autor do livro Javascript: The Good Parts, criador do JSON;
- `Criador do Javascript`_;
- `JavaScript Weekly`_;
- `Twitter do criador do jQuery`_;

Cursos:

- `JavaScript no CodeCademy`_;
- `JavaScript no CodeSchool`_;

Livros

- `Lista de livros gratuitos`_;
- `JavaScript, The Good Parts`_;
- `Secrets of the JavaScript Ninja`_;
- `Segredos do Ninja JavaScript`_;
- `Learning JavaScript Design Patterns`_ (Grátis para ler online);

.. class:: panel-body bg-info

        Na compra de qualquer livro na Novatec utilize o código **MINDBENDING** para conseguir 20% de desconto.

Outros Links Citados
--------------------

- `SIGE`_ (Projeto do Átila);
- `COMSOLID`_;
- `HackingnRoll`_;
- `Emulador de Nintendo 64`_;


Trilha Sonora
-------------

A trilha sonora deste episódio foi escolhida pelo Diego "Boot" e é uma homenagem ao Dr. Sin.

Dr. Sin (1993)
        - Emotional Catastrophe
        - Stone Cold Dead
        - Howlin' In The Shadows
        - Lonely World
        - Scream & Shout

Brutal (1995)
        - Karma
        - Isolated
        - Fire
        - Child of Sin

Insinity (1997)
        - Sometimes
        - Futebol, Mulher e Rock'n Roll
        - Zero

Dr. Sin II (2000)
        - Time After Time

.. Links genéricos
.. _Hack 'n' Cast: /pt/category/hack-n-cast
.. _uma das linguagens mais incompreendidas do mundo: http://javascript.crockford.com/javascript.html
.. _WAT do Destroy All Software: https://www.destroyallsoftware.com/talks/wat
.. _ECMA International: http://www.ecma-international.org/
.. _Java Script - Designing a Language in 10 Days: http://www.computer.org/csdl/mags/co/2012/02/mco2012020007.html
.. _História da World Wide Web (Palestra de 2012 com Timeline): http://atilacamurca.github.io/press-www-history
.. _Uma Reintrodução à JavaScript: https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/A_re-introduction_to_JavaScript
.. _Multi-Paradigmas: https://developer.mozilla.org/en-US/docs/multiparadigmlanguage.html
.. _object prototypes: https://en.wikipedia.org/wiki/Prototype-based
.. _The World of ECMAScript: http://ejohn.org/blog/the-world-of-ecmascript/
.. _ECMAScript 6: https://wiki.mozilla.org/ES6_plans
.. _conforme listado aqui: http://en.wikipedia.org/wiki/JavaScript#Uses_outside_web_pages

.. |Twitter Diego| replace:: Twitter
.. |Facebook Diego| replace:: Facebook
.. |Twitter Atila| replace:: Twitter
.. |GitHub Atila| replace:: GitHub
.. _Twitter Diego: https://twitter.com/diegoboot
.. _Facebook Diego: https://www.facebook.com/diegoboot
.. _Twitter Atila: https://twitter.com/atilacamurca
.. _GitHub Atila: https://github.com/atilacamurca

.. JS Engines
.. _V8: http://code.google.com/p/v8/
.. _SpiderMonkey: https://developer.mozilla.org/pt-BR/docs/Mozilla/Projects/SpiderMonkey
.. _asm.js: http://asmjs.org/
.. _Rhino: https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino
.. _JavaScriptCore: https://www.webkit.org/projects/javascript/
.. _KJS: http://api.kde.org/4.11-api/kdelibs-apidocs/kjs/html/index.html
.. _Chakra: http://en.wikipedia.org/wiki/Chakra_%28JScript_engine%29
.. _Nashorm: http://docs.oracle.com/javase/8/docs/technotes/guides/scripting/nashorn/

.. Ferramentas, IDES, bibliotecas e frameworks
.. _jQuery: https://jquery.org/history/
.. _JQueryUI: http://jqueryui.com/
.. _Kendo UI: http://www.kendoui.com
.. _UglifyJS: https://github.com/mishoo/UglifyJS
.. _UglifyJS2: https://github.com/mishoo/UglifyJS2
.. _Uma lista mais expandida: https://github.com/jashkenas/coffeescript/wiki/list-of-languages-that-compile-to-js
.. _Espruino: http://www.espruino.com/
.. _Tessel: https://tessel.io/
.. _JSLint: http://www.jslint.com/lint.html
.. _JSDB: http://www.jsdb.io/
.. _Breach: http://breach.cc/
.. _Codepen: http://codepen.io/
.. _JSFiddle: http://jsfiddle.net/
.. _AngularJS: https://angularjs.org/
.. _React: http://facebook.github.io/react/
.. _BackBoneJS: http://backbonejs.org/
.. _JavaScriptMVC: http://javascriptmvc.com

.. Fontes de Aprendizado
.. _Lista de livros gratuitos: http://codecondo.com/free-javascript-books/
.. _Página sobre Javscript do MDN (Mozilla Developer Network): https://developer.mozilla.org/pt-BR/docs/Web/JavaScript 
.. _Reintrodução ao Javascript: https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/A_re-introduction_to_JavaScript
.. _Blog Pessoal de Douglas Crockford: http://javascript.crockford.com/
.. _Criador do Javascript: https://brendaneich.com/
.. _JavaScript Weekly: http://javascriptweekly.com/
.. _JavaScript no CodeCademy: http://www.codecademy.com/pt/tracks/javascript
.. _JavaScript no CodeSchool: https://www.codeschool.com/paths/javascript
.. _Twitter do criador do jQuery: https://twitter.com/jeresig
.. _JavaScript, The Good Parts: http://www.amazon.com/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742
.. _Secrets of the JavaScript Ninja: http://www.amazon.com/Secrets-JavaScript-Ninja-John-Resig/dp/193398869X/
.. _Learning JavaScript Design Patterns: http://addyosmani.com/resources/essentialjsdesignpatterns/book/ 
.. _Segredos do Ninja JavaScript: http://novatec.com.br/livros/ninja-javascript/


.. Social
.. _E-mail: mailto: hackncast@gmail.com
.. _Twitter: http://twitter.com/hackncast
.. _Facebook: http://facebook.com/hackncast
.. _Feed: http://feeds.feedburner.com/hack-n-cast
.. _Podflix: http://podflix.com.br/hackncast/
.. _iTunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846?l=en
.. _Pocket Casts: http://pcasts.in/hackncast
.. _Google Groups: https://groups.google.com/forum/?hl=pt-BR#!forum/hackncast

.. Links Diversos
.. _SIGE: https://github.com/comsolid/sige
.. _COMSOLID: http://www.comsolid.org/
.. _HackingnRoll: http://www.hackingnroll.com/
.. _Emulador de Nintendo 64: https://github.com/hulkholden/n64js/

