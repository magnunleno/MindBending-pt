WordPress Com Dois Idiomas de Forma Simples
###########################################
:date: 2011-09-19 10:00
:category: Wordpress
:tags: blog, categorias, hack, idiomas, inglês, php, português, wordpress
:image: /images/wordpress.png

.. raw:: html

   <div class="alert alert-danger"><strong>Atenção:</strong> Este artigo está desatualizado e não reflete mais o modo de funcionamento deses blog.</div>

Olá pessoal, este é um artigo completamente fora do padrão de assuntos
que eu costumo abordar, vou falar de PHP e WordPress. Como vocês já
devem ter notado, eu escrevo artigos em português e inglês, o que muitas
vezes gera uma visualização não muito agradável na página principal:

.. image:: {filename}/images/main_mb.png
	:align: center
	:target: {filename}/images/main_mb.png
	:alt: Mind Bending - Main Page

Essa apresentação me incomodava a muito tempo, tentei diversos
*plug-ins* para tentar resolver o meu problema, mas eles traziam mais
problemas do que resolviam. Então decidi que um dia iria criar algo em
PHP para garantir que os artigos em português fossem mostrados apenas
para o visitantes que falam português e para todos os outros visitantes
(que falam qualquer outra língua) fosse mostrado apenas os artigos em
inglês (isso na página principal, todos os artigos continuam disponíveis
nas categorias para qualquer visitante). Pensando nisso, quando comecei
o blog organizei duas categorias (como pode ser visto no painel
lateral), mas como não sou nenhum especialista em PHP e WordPress acabei
adiando esta tentativa de correção. Mas nesse fim de semana criei
coragem e coloquei a mão na massa e, como vocês podem ver, na página
inicial agora não aparace mais os artigos em inglês para nos
brasileiros.

.. more

Como eu resolvi isso? Foi até simples...

Detectando o Idioma
-------------------

Primeiramente temos que garantir uma forma de obter o idioma principal
configurado no navegador. Para isso usei o seguinte trecho de código
obtido `neste endereço`_:

.. code-block:: css+php

    function getDefaultLanguage() {
        if (isset($_SERVER["HTTP_ACCEPT_LANGUAGE"]))
            return parseDefaultLanguage($_SERVER["HTTP_ACCEPT_LANGUAGE"]);
        else
            return parseDefaultLanguage(NULL);
    }

    function parseDefaultLanguage($http_accept, $deflang = "en") {
        if(isset($http_accept) && strlen($http_accept) > 1)  {
            //Split possible languages into array
            $x = explode(",",$http_accept);
            foreach ($x as $val) {
                //check for q-value and create associative array. No q-value means 1 by rule
                if(preg_match("/(.*);q=([0-1]{0,1}.d{0,4})/i",$val,$matches))
                    $lang[$matches[1]] = (float)$matches[2];
                else
                    $lang[$val] = 1.0;
            }

            // return default language (highest q-value)
            $qval = 0.0;
            foreach ($lang as $key => $value) {
                if ($value > $qval) {
                    $qval = (float)$value;
                    $deflang = $key;
                }
            }
        }
        return strtolower($deflang);
    }

Basicamente a função acima retorna uma string indicando o idioma padrão
configurada no navegador, alguns exemplos retornados podem ser: pt,
pt-br, en, en-us, en-uk, es e etc. Este trecho de código deve ser
adicionado a um arquivo ``.php`` que contém as funções usadas pelo seu
tema WordPress, geralmente existe um arquivo chamado ``functions.php``.

Você Fala Portugês?
-------------------

Daqui pela frente todas as alterações serão realizadas na página
``index.php``, responsável pela página inicial do seu blog. Neste
arquivo encontra-se o *loop* principal do WordPress, que pode ser
identificado por seguir o seguinte padrão:

.. code-block:: css+php

    if (have_posts()):
        while (have_posts()):
        the_post();  

O trecho a seguir deve ser colocado imediatamente antes do *loop* principal:

.. code-block:: css+php

    if (ereg('^pt', getDefaultLanguage())){
        $is_pt = TRUE;
    }

Este trecho utiliza uma verificação por meio de expressões regulares
para iniciar uma variável indicando que nosso visitante tem configurada
alguma variação da íngua portuguesa. Nada muito complexo, certo?

Mostrando Uma Categoria na Página Principal
-------------------------------------------

O grande *hack* deste artigo vem a seguir. Como separei todos os artigos
do meu blog em duas categorias (*blog-pt* e *bog-en*) tudo que tenho que
fazer é alterar a página inicial para exibir (ao invés de todos os
artigos) apenas os artigos de uma categoria, tendo como base da escolha
a variável ``$is_pt`` criada anteriormente.

O trecho a seguir deve ser inserido entre o trecho anterior e o *loop*
principal:

.. code-block:: css+php

    $paged = (get_query_var('paged')) ? get_query_var('paged') : 1;
    if ($is_pt){
        query_posts("category_name=blog-pt&paged=$paged");
    } else {
        query_posts("category_name=blog-en&paged=$paged");
    }

A primeira linha obtêm informações acerca da paginação, que mais tarde
serão repassadas para as linhas 3 e 4. As linhas 3 e 4 são responsáveis
por alterar a lista de artigos a serem exibidos dentro do
*loop* principal. Como podem ver, a busca solicita que sejam listados os
artigos dentro da respectiva categoria (baseado no idioma do visitante)
e dada uma certa paginação.

Para quem não precisa verificar mais de uma vez a variável ``$is_pt``
(não é meu caso), é interessante utilizar o seguinte trecho de código
mais reduzido:

.. code-block:: css+php

    $paged = (get_query_var('paged')) ? get_query_var('paged') : 1;
    if (ereg('^pt', getDefaultLanguage())){
        query_posts("category_name=blog-pt&paged=$paged");
    } else {
        query_posts("category_name=blog-en&paged=$paged");
    }

Então é isso caros leitores, espero que esta mudança ajude vocês a
navegarem no blog.

Até mais...

.. _neste endereço: http://www.dyeager.org/post/2008/10/getting-browser-default-language-php
