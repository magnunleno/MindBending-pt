Hack 'n' Cast v0.4 - Introdução à Programação
#############################################
:date: 2014-08-07 02:04
:category: Hack 'n' Cast
:tags: hack 'n' cast, podcast, beta, programação, orientação a objetos, estruturada, funcional, babbage, ada lovelace, computadores, ábaco, calculadoras, sintaxe, semântica, AC/DC
:image: /images/hack-n-cast/v0.x/v0.4-cover-sqr.png
:length: 86272963
:duration: 89:00
:podcast: http://archive.org/download/HNC.v0.4-Introducao-a-programacao/HNC.v0.4-Introducao-a-programacao.mp3
:podcastembed: http://archive.org/embed/HNC.v0.4-Introducao-a-programacao/HNC.v0.4-Introducao-a-programacao/mp3
:podcast_old: True
:description: Ah, A programação! A bela arte de gerar códigos! Linus Torvalds já dizia: programar é para poucos. Eu ainda acrescento: programar bem é para raríssimos. Você também não está neste seleto grupo? Então junte-se a nos e venha se divertir com esse tópico!

E no episódio deste mês do `Hack 'n' Cast`_ abordamos o assunto de introdução à programação. O quê? Você não programa? Mas até o Schwarzenegger programa! E mais, em `sua língua nativa`_? Não acredita? Quem afirma é o Davi Sanches (nosso convidado de hoje) e também o nosso especialista, pois ele acompanhou de perto a criação da `La pascaline`_ e deu seu pitaco na `Máquina Diferencial`_ de `Babbage`_. Sim, temos conosco hoje um herói, saído da sessão da tarde e diretamente das *Highlands*, o nosso Guerreiro Imortal: Ricardo Medeiros! Ou seria ele o `Rei de Vida Eterna`_?

.. image:: {filename}/images/hack-n-cast/v0.x/v0.4-cover.png
        :target: {filename}/images/hack-n-cast/v0.x/v0.4-cover.png
        :alt: Hack 'n' Cast v0.4 - Introdução à Programação
        :align: center

Para não perder nenhum episódio siga-nos nas redes sociais (`Twitter`_ e `Facebook`_) ou inscreva-se (`Feed`_, `Podflix`_, `iTunes`_ e `Pocket Casts`_). Você quer colaborar com o Hack 'n' Cast? Sugira um tema, nos ajude a produzir uma pauta ou participe conosco! Basta entrar em contato por `E-mail`_, `Facebook`_ ou `Twitter`_.

.. more

.. podcast:: HNC.v0.4-Introducao-a-programacao
        :rss: http://feeds.feedburner.com/hack-n-cast
        :itunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846

Sorteio Novatec
===============

Lembrando que neste episódio temos o resultado do sorteio dos dois livros da `Novatec`_:

- `Descobrindo o Linux`_ (João Eriberto)
- `Shell Script Profissional`_ (Aurélio Marinho)

Ouça e veja se você ganhou!

.. _Novatec: http://novatec.com.br/

Introdução
==========

Os computadores são mais antigos do que imaginamos, eles sempre nos ajudaram a calcular, contar, acompanhar a mudança do tempo e das estações. Por boa parte do tempo foram usados para executar automaticamente tarefas que nos entediavam ou consumiam tempo. Entretanto, em um certo ponto da história, eles passaram a realizar tarefas que não somos capazes de executar, como quebra de criptografias, cálculos instantâneos de balística, previsões estocásticas e diversas outras. Entretanto, todo esse poder computacional seria desperdiçado se não fosse por um componente fundamental: Sua Programação.

.. image:: {filename}/images/hack-n-cast/v0.x/keep-calm-and-program-on.png
        :target: {filename}/images/hack-n-cast/v0.x/keep-calm-and-program-on.png
        :alt: Keep Calm And Program On
        :align: center

Mas antes de falarmos de programação precisamos entender o que é um computador!

O que é um computador
---------------------

Atualmente um compputador é um dispositivo eletrônico composto basicamente por:

Sistemas de Entrada e Saída
        Dispositivos como monitor, impressoras, teclado, mouse e etc.
CPU (Central Processing Unit)
        Podemos dizer que é o "cérebro" do computador, é aqui que todo processamento ocorre.
Memória
        A memória é uma método de armazenamento transiente (não persistente) de rápido acesso.
Sistema de armazenamento
        Qualquer tipo de armazenamento (discos, hard drives, disquetes, fitas magnéticas, pen drives e etc) persistente.

Todos os elementos acima compõem a parte físcia do computador (hardware) e o programa (objetivo deste episódio) é a parte lógica (software). É esta parte lógica (o programa) que diferencia-o de uma calculadora, pois um computador tem a capacidade de carregar e executar instruções sem auxílio humano, enquanto uma calculadora (comum) precisa que nós (humanos) "operemos" seu programa.

Um programa é basicamente uma coleção de instruções (um passo-a-passo) que descrevem para o computador uma tarefa a ser realizada/executada. Sem esse programa o computador é um amontoado de ferro e silício, pois eles dão toda a inteligência ao computador.

História
--------

Tecnicamente podemos dizer que os primeiros "computadores" foram as primeiras calculadoras entretanto toda a "programação" desses computadores era responsabilidade de seu "operador". A forma mais antiga de caulcular que temos notícia é o ábaco, que provavelmente teve origem na china há mais de 5.500 anos.

Em seguida tivemos várias "calculadores" automatizadas:

- **O Relógio Calculador (Wilhel Schickard):** Era operado através de manivelas, somava e subtraía números de até 6 dígitos e quando o valor extrapolava 6 dígitos ele tocava uma sineta;
- **La Pascaline (Blaise Pascal):** Uma máquina que somava números e era inferior ao "relógio calculador", entretanto este se tornou mais popular devido ao prestígio de Blaise Pascal;
- **Aprimoramento da Le Pascaline (Gottfried Wilhelm Von Leibnitz):** Sua máquina podia realizar as quatro operações básicas e realizar cálculos de raiz quadradas;

Em seguida tivemos a primeira aplicação prática de um computador rudimentar, a "Máquinas de Tear Automatizado" criado pelo mecânico francês Joseph Marie Jacquard. Esta máquina computava, com base em cartões perfurados, a posição dos fios na hora de tear e, consequentemente, controlava os padrões produzidos no tecido.

A ideia do primeiro "computador programável" foi criado por Charles Babbage, uma matemático nascido em Londres em 26 de Dezembro de 1791 (considerado o pai da computação). A "organização computacional" criada por Babbage ainda pode ser vista nos computadores atuais, como:

- Dados e memória de um programa;
- Instruções;
- Controle de fluxo;
- Dispositivos de Entrada/Saída.

Babbage construiu duas máquinas, a máquina diferencial e a máquina analítica.

Máquina diferencial
~~~~~~~~~~~~~~~~~~~

A máquina diferencial seria capaz de calcular e imprimir valores de funções polinomiais, ela utilizava um método chamado "diferenças finitas", daí o nome da máquina. Esta já era capaz de receber dados, processá-los e exibir os resultados.

Apesar de extremamente bem planejada, o projeto nunca foi concluído por dificuldades de produção e custeio (por parte do governo). Posteriormente, em 1991, foi construído uma versão da máquina seguindo as especificações de Babbage, a quela funcionou perfeitamente e com precisão. Outro motivo para o fim do projeto da máquina diferencial era o interesse de Babbage pelo seu novo projeto, a máquina analítica.

Máquina Analítica
~~~~~~~~~~~~~~~~~

Esta máquina marcou a transição de mecanismos aritméticos para computação de propósitos genéricos, e sua grande "inovação" era a capacidade de ser programada usando cartões perfurados e de utilizar em seu calculo o resultado do calculo anterior. Em teoria esta máquina seria a primeira a atingir o status de "Turing Complete". Como saída a máquina teria uma impressora, um plotador de curva e uma sineta.

Ada Lovelace (Ada Byron)
~~~~~~~~~~~~~~~~~~~~~~~~

Foi a primeira programadora (e a primeira a escrever um algoritmo) da história, ela influenciou muito os trabalhos de Babbage durante suas trocas de cartas. É a ela que atribuímos a criação de conceitos importantes como if-eles, loops, goto, funções, variáveis e etc.

Linguagens
----------

É um procedimento para escrever instruções para um computador, usando regras para a construção de um programa. O computador é burro e não sabe o que fazer, com isso as linguagens são uma forma de expressar o que ele precisa fazer para solucionar o seu problema.

Características consideradas importantes em uma linguagem:

- Função ou objetivo;
- Abstração;
- Expressividade;

Sintaxe & Semântica
~~~~~~~~~~~~~~~~~~~

Sintaxe é a linguagem com todos os seus verbos, substantivos e adjetivos, ela define a combinação destes "objetos" com o objetivo de formar uma estrutura concisas. Já a semântica diz se um texto sintaticamente correto possui um significado lógico e correto. Um código pode estar sintaticamente correto mas semanticamente errado.

Tipos de linguagens
~~~~~~~~~~~~~~~~~~~

As linguagens geralmente são classificadas também com base no seu tipo de compilação e comunicação com o sistema operacional. Existem basicamente dois grupos, as linguagens compiladas e as linguagens interpretadas:

Compilada
        Gera um código binário voltado para uma arquitetura. Este tipo é extremamente atrelado ao processador e seus binários não são portáveis, pois incorre em compatibilidades de arquitetura como notação numérica (*littleendian* ou *bigendian*) e o tamanho de seus tipos. Muitas pessoas incorrem no erro de dizer que um nem mesmo códigos da uma linguagem compilada é portável, mas tomados os devidos cuidados e utilizando os padrões corretos, um código de uma linguagem compilada pode ser facilmente portado.
Interpretada
        Gera um código (bytecode) para um máquina virtual, e esta máquina é responsável por interpretar e executar o código compilado para Bytecode. Essa máquina virutal é reescrita para várias arquiteturas, tornando assim o compilado portável.

As linguagens também pode ser divididas com base na sua abstração:

- Baixo nível ou linguagem de máquina (Assembly ou Binário);
- Médio nível (C, Fortran, BASIC e etc);
- Alto nível (Java);
- Altíssimo Nível (Python, Ruby, Lua e etc);

Entretanto as classificações de médio e altíssimo nível são pouco aceitas no meio acadêmico.

As linguagens também são agrupadas com base no seu paradigma suportado. Um paradigma dita como você pode ou deve estruturar seu código e a forma como seu programa será processado, interpretado ou compilado:

Procedural ou Imperativa
        Recebeu esse nome por ser construída ao redor de procedimentos (*procedures*), ou funções. Simplesmente executa uma série de instruções sequencialmente.
Funcional
        Tem como base o cálculo de lambdas. Trata a computação como uma série de funções matemáticas. Uma f(x) sempre retornará um mesmo valor se x sempre possuir o mesmo valor.
Orientado a Objetos
        Tudo é estruturado sob o conceito de classes, objetos, atributos, métodos e trocas de mensagens;
Modular:
        Separa os programas em partes modulares Onde cara modulo executa bem apenas uma tarefa. Tem como foco a separação de responsabilidades e apresenta uma melhora a manutenabilidade.


Por último temos as linguagens exotéricas que falam por si só:

- Whitespace;
- Brainfuck;
- ArnoldC;
- LOLCODE.


Saiba Mais
==========

`Code.org`_
        Organização sem fins lucrativos dedicada à crescente educação de ciência da computação. Tem a visão de que todos podem aprender programação.
`Codecademy`_
        Aprender sozinho ou em grupo é uma possibilidade na Code Academy, onde os cursos são gratuitos. A plataforma conta com versão em português, mas apenas nas páginas iniciais.
`Try Ruby`_
        Menos popular entre os iniciantes e com menos espaço no mercado, a linguagem de programação Ruby tem espaços divertidos para os dispostos a explorá-la. A home do Try Ruby é quase um afago ao usuário, com os seus desenhos delicados e indicações de "como fazer" que quase conduzem o aprendiz pela mão.
`Code School`_
        Apoiada pela IBM e também desenvolvida para oferecer uma experiência semelhante a de um game. O lema por lá é "Aprenda Fazendo". Tutoriais estão presentes, mas exercícios e recompensas etapa a etapa são o forte da proposta.

Links
=====

- `Adolescentes Canadenses Hackeiam ATM com Informações da Internet`_;
- `Criaram uma linguagem de programação inspirada em Arnold Schwarzenegger`_;
- `Scicast sobre Orientação a Objeto`_;
- `Hello World em diversas linguagens`_.
- `Curto Circuito Podcast - Aprendizagem e Programação`_

Trilha Sonora
=============

A trilha sonora de hoje é uma homenagem à banda AC/DC, e foi escolhida pelo Davi Sanches:

Album "High Voltage" (1975)
        - It's A Long Way To The Top (If You Wanna Rock 'N' Roll)
        - Rock 'N' Roll Singer
        - The Jack
        - Live Wire
        - T.N.T.
        - Can I Sit Next To You Girl
        - Little Lover
        - She's Got Balls
        - High Voltage
Album "Dirty Deeds Done Dirt Cheap" (1976)
        - Dirty Deeds Done Dirt Cheap
        - Love At First Feel
        - Big Balls
        - Rocker
        - Problem Child
        - There's Gonna Be Some Rockin'


.. _Hack 'n' Cast: /pt/category/hack-n-cast
.. _sua língua nativa: https://github.com/lhartikk/ArnoldC
.. _La pascaline: http://pt.wikipedia.org/wiki/La_pascaline
.. _Máquina Diferencial: http://pt.wikipedia.org/wiki/M%C3%A1quina_diferencial
.. _Babbage: http://pt.wikipedia.org/wiki/Charles_Babbage
.. _Rei de Vida Eterna: http://pt.wikipedia.org/wiki/Mumm-Ra#Mumm-Ra

.. _Descobrindo o Linux: http://www.submarino.com.br/produto/111414273/descobrindo-o-linux-entenda-o-sistema-operacional-gnu-linux?epar=lomadee&opn=AFLNOVOSUB&utm_campaign=lomadee&utm_medium=lomadee&utm_source=lomadee
.. _Shell Script Profissional: http://www.submarino.com.br/produto/6774464/livro-linux-guia-do-administrador-do-sistema?epar=lomadee&opn=AFLNOVOSUB&utm_campaign=lomadee&utm_medium=lomadee&utm_source=lomadee

.. Social
.. _E-mail: mailto: hackncast@gmail.com
.. _Twitter: http://twitter.com/hackncast
.. _Facebook: http://facebook.com/hackncast
.. _Feed: http://feeds.feedburner.com/hack-n-cast
.. _Podflix: http://podflix.com.br/hackncast/
.. _iTunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846?l=en
.. _Pocket Casts: http://pcasts.in/hackncast

.. saiba mais
.. _Code.org: http://code.org/
.. _Codecademy: http://www.codecademy.com/pt
.. _Try Ruby: http://tryruby.org/levels/1/challenges/2
.. _Code School: https://www.codeschool.com/

.. Links
.. _Adolescentes Canadenses Hackeiam ATM com Informações da Internet: http://meiobit.com/289571/adolescentes-canadenses-hackeiam-caixa-eletronico-com-instrucoes-encontradas-na-internet/
.. _Criaram uma linguagem de programação inspirada em Arnold Schwarzenegger: http://gizmodo.uol.com.br/programacao-schwarzenegger/
.. _Scicast sobre Orientação a Objeto: http://www.scicast.com.br/scicast-032-programacao-orientada-a-objetos/
.. _Hello World em diversas linguagens: https://github.com/leachim6/hello-world
.. _Curto Circuito Podcast - Aprendizagem e Programação: http://www.curtocircuito.cc/aprendizagem-e-programacao/
