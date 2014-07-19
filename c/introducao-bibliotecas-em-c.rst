Introdução à Bibliotecas em C
#############################
:date: 2012-07-03 15:50
:category: C
:tags: bibliotecas, c, compartilhadas, dinâmicas, disco, espaço, estáticas, execução, libraries, ligação, memória, programação, tempo
:image: /images/libraries.jpg
:slug: introducao-bibliotecas-em-c
:series: Bibliotecas em C

Quando o assunto é aquisição de conhecimento, eu sempre faço questão de
sair da minha `"zona de conforto"`_ para aprender coisas novas.
Recentemente uma ideia tem martelado minha cabeça e voltei a programar
em C ANSI onde estou (re-)aprendendo a criar bibliotecas.

.. image:: {filename}/images/libraries.jpg
	:align: center
	:target: {filename}/images/libraries.jpg
	:alt: Libraries

Vocês devem estar se perguntando: por que um defensor do Python está
programando em C? O fato é que a linguagem C ANSI (além de possuir um
ótimo desempenho) foi a primeira linguagem de programação que aprendi.
Pode parecer contra-mão utilizar a linguagem C hoje em dia, mas a
linguagem além de extremamente poderosa é essencial para qualquer
programador de verdade -- que deseje criar programas de verdade -- e
que goste de programar, pois ela oferecer ao programador o aprendizado
de conceitos importantíssimos."Mas e quanto às bibliotecas?" vocês me
perguntam. Bem, isso eu não posso explicar ainda, mas espero escrever
sobre isso em breve. Deixando de lado o bate-papo, tenho que responder
alguns questionamentos básicos como: O que são bibliotecas? Qual a
diferença entre **bibliotecas estáticas** e **bibliotecas
compartilhadas**?

.. more

O Que São Bibliotecas
---------------------

Uma biblioteca é uma coleção de funções e definições escritas para um
propósito definido. Qualquer programador C já utilizou pelo menos uma
biblioteca, a `stdio`_, que define funções como, ``printf``,
``scanf``, ``fopen``, ``getchar`` e etc.

Por Que Utilizar Bibliotecas
----------------------------

No mundo OpenSource é extremamente comum um programador, ao precisar
resolver determinado problema, se utilizar de uma biblioteca escrita por
outro programador. Isso pode ser extremamente vantajoso, pois reduz a
necessidade de criar códigos (que já foram criados por outras pessoas)
mas também pode ser perigoso, pois você pode acabar optando por uma
biblioteca mal implementada (ou até mesmo maliciosa) e acabar tendo
grandes dores de cabeça. Por isso, evite utilizar qualquer biblioteca
encontrada pela internet sem antes pesquisar sobre esta e (em casos de
tratamento de dados sensíveis) realizar uma auditoria pelo código. Pense
em bibliotecas como *plugins* para seu navegador, você não instala
qualquer *plugin* sem antes pesquisar e conhecê-lo, uma vez que este
pode conter códigos maliciosos que terão acesso direto a seus dados,
contas e senhas.

Tipos De Bibliotecas
--------------------

Existem basicamente dois tipos de bibliotecas, as bibliotecas estáticas
e as bibliotecas compartilhadas. Antes de entrar nos detalhes mais
técnicos deste assunto, vale ressaltar que algumas características
dependem do Sistema Operacional, logo, terei que reduzir um pouco o
escopo deste texto restringindo ao **mundo Unix** (e, obviamente,
GNU/Linux). Entretanto, muito do que explicarei também será valido para
sistemas como o Windows e o Mac OS.

Bibliotecas Estáticas
~~~~~~~~~~~~~~~~~~~~~

As bibliotecas estáticas podem ser identificadas pela extensão ``.a``.
Ao compilar um programa que chama uma biblioteca estática, todo o código
da biblioteca é copiado e inserido dentro do binário final. O termo
"estática" se deve ao fato da linguagem se tornar uma parte estática do
binário final, e consequentemente, não podendo ser compartilhada por
outros programas. Se você quiser ter uma ideia de quantas e quais
bibliotecas estáticas existem no seu sistema atualmente basta executar o
seguinte comando:

.. code-block:: bash

    $ ls /usr/lib/*.a; echo "::: Total: `ls -l /usr/lib/*.a | wc -l`"

Ao utilizar esta abordagem você garante que, mesmo quando a biblioteca
presente no seu sistema mude, seja removida ou corrompida, o seu
programa continuará funcionando. Porém ela tem seu lado negativo, além
do seu binário final ocupar mais espaço em disco e memória (já que ele
inclui a biblioteca estática) o seu programa não poderá usufruir de
qualquer melhoria que venha a ocorrer nesta biblioteca, a não ser que o
seu programa seja recompilado/reinstalado.

Bibliotecas Compartilhadas
~~~~~~~~~~~~~~~~~~~~~~~~~~

As bibliotecas compartilhadas são identificadas pela extensão ``.so``.
Ao contrário das bibliotecas estáticas, estas não são inseridas em sua
totalidade, elas são apenas referenciadas no binário final. O termo
compartilhada expressa exatamente a característica de um ou mais
programas poder utilizar a mesma biblioteca, ocupando assim menos espaço
em disco e na memória. De forma similar, você pode listar as bibliotecas
dinâmicas existentes em seu computador com o seguinte comando:

.. code-block:: bash

    $ ls /usr/lib/*.so; echo "::: Total: `ls -l /usr/lib/*.so | wc -l`"

Para entender melhor a questão do tamanho e memória, vou ilustar com um
breve exemplo:

    Vamos supor que você acabou de criar dois programas, o *ProgA*,
    previsto pra gerar um binário de 200k, e o *ProgB*, previsto para
    gerar um binário de 100K. Ambos os programas se utilizam de uma
    biblioteca etsática chamada *LibA*. Lembrando que um programa que
    utiliza bibliotecas estáticas inclui em seu binário todo o código da
    biblioteca, ao final da compilação (e ligação com a *LibA*) os
    progrmas *ProgA* e *ProgB* terão respectivamente 700K (200K + 500K)
    e 600K (100K + 500K).

    Quando um programa é executado no computador, ele é "copiado" para a
    memória, então ao executar o programa *ProgA* e o *ProgB* você terá
    1300K de memória ocupada, onde 1000K corresponde à *LibA*. Se fosse
    utilizado uma biblioteca compartilhada, os programas compartilhariam
    a biblioteca e esta seria carregada separadamente na memória. Desta
    forma os programas teriam aproximadamente o mesmo tamanho após a
    compilação (já que é incluída durante a ligação apenas algumas
    definições da biblioteca) e ocupariam em memória apenas 800K (100K +
    200K + 500K).

Além da redução do espaço em disco e do uso de memória, a característica
dinâmica da biblioteca compartilhada confere ao seu programa a
possibilidade de usufruir de atualizações nas bibliotecas sem a
necessidade de um nova compilação/instalação. Entretanto, como as
bibliotecas dinâmicas são chamadas em tempo de execução, seu programa
correrá o risco de não executar corretamente, seja por não encontrar a
biblioteca ou (após uma atualização) pela biblioteca não ser mais
compatível com seu programa. O último ponto negativo da biblioteca
compartilhada é que, devido seu tempo de carregamento é adicionada uma
pequena latência nas chamadas a esta biblioteca, consequentemente seu
programa será ligeiramente mais lento que o mesmo utilizando bibliotecas
estáticas.

Com todos estes pontos negativos e positivos para ambas as modalidades,
fica ao critério do desenvolvedor escolher que tipo de biblioteca ele
irá desenvolver/utilizar, por isso diversas bibliotecas são distribuídas
em ambas as modalidades:

.. code-block:: bash

    $ ls /usr/lib/*.so | grep mysql
    /usr/lib/libmysqlclient_r.so
    /usr/lib/libmysqlclient.so

    $ ls /usr/lib/*.a | grep mysql
    /usr/lib/libmysqlclient.a
    /usr/lib/libmysqlclient_r.a
    /usr/lib/libmysqld.a
    /usr/lib/libmysqlservices.a

Resumo
------

Como tudo na vida, as bibliotecas estáticas possuem seus prós e contras,
assim como as bibliotecas compartilhadas. Cabe apenas a você
programador, decidir que tipo de biblioteca você irá utilizar/criar. A
baixo uma pequena tabela resumindo o que vimos acima:

.. table::
        :class: table

        ===================================== ===============================
        Bibliotecas Compartilhadas             Bibliotecas Estáticas         
        ===================================== ===============================
        Maior modularidade                     Mais estabilidade             
        Menor consumo de disco/memória         Maior consumo de disco/memória
        Não precisa de nova compilação         Necessita de nova compilação  
        Pequena latência ao chamar funções     Sem latência ao chamar funções
        ===================================== ===============================

Em Breve...
-----------

Agora que entendemos o que são as bibliotecas e suas vantagens, no
próximo artigo irei mostrar como você pode criar suas próprias
bibliotecas, sejam elas estáticas ou compartilhadas. Até lá!

.. _"zona de conforto": http://pt.wikipedia.org/wiki/Zona_de_conforto
.. _stdio: http://www.cplusplus.com/reference/clibrary/cstdio/
