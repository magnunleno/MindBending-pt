Registradores no VIM
####################
:date: 2014-06-16 16:30
:category: VIM
:tags: vim, registradores, registers
:image: /images/vim.png
:description: Se tem algo que eu sou realmente fanático, é o VIM. Curiosamente este é um assunto que eu raramente consigo abordar aqui. Não era bem assim que eu planejava escrever sobre VIM, meu intuito era primeiro escrever sobre a base do VIM, e só então abordar assuntos mais avançados. Mas vamos atender a pedidos!
:slug: registradores-no-vim

Esses dias surgiu uma pergunta do Arthur na `lista de discussão de usuários de VIM do Brasil`_ sobre "realizar deleções sem sobrescrever o texto já copiado". Parece uma coisa boba para quem vem de outros editores, mas tudo no VIM é extremamente profundo, se você se dedicar a explorar uma pequena funcionalidade você pode perder o dia todo e não ter lido/entendido tudo sobre o assunto.

.. image:: {filename}/images/vim.jpg
        :target: {filename}/images/vim.jpg
        :alt: VIM Rocks
        :align: center

"E por quê perder tanto tempo entendendo uma funcionalidade do VIM pode ser útil? Não basta apenas saber o básico e seguir adiante?" Não, não basta. Simplesmente porque o VIM é como um monstro de LEGO e se você entender melhor uma pequena peça, você vai ver que pode usar essa peça combinada com centenas de outras, e assim ter um fluxo de trabalho extremamente otimizado.

.. more

Registradores
-------------

Os registradores no VIM são como variáveis em um programa. Eles podem ser divididos em 2 grupos:

Registradores de leitura e escrita
        Nos quais você (ou o próprio VIM) irão inserir dados e ler dados.
Registradores somente leitura
        Nos quais apenas o próprio VIM irá inserir dados, e você poderá apenas ler dados.

O VIM usa um "endereço" de apenas um caractere para nomear os registradores, e você pode referenciá-los em uma séries de comandos, como por exemplo em uma cópia ``Y``, em uma deleção ``D`` e etc.

Por exemplo, se você quiser colar o conteúdo do registrador ``1`` no seu texto, vasta você utilizar o seguinte comando ``"1p``. O caractere ``"`` neste comando está informando ao VIM que deve interpretar o próximo caractere como um endereço de registrador. Desta forma, se fizermos o comando ``"add`` estaremos deletando todo o conteúdo da linha corrente (`dd`) para e copiando seu conteúdo para o registrador ``a``.

Para listar todos os registradores e seus respectivos conteúdo utilize o comando ``:registers`` ou ``:display``. Para visualizar apenas o conteúdo de um ou mais registradores, basta utilizar o comando da seguintes forma;

* ``:display a`` - irá apresentar o conteúdo do registrador ``a``;
* ``:display :%.`` - irá apresentar o conteúdo dos registradores ``:``, ``%`` e ``.``;

Registradores Somente Leitura
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vamos começar com estes que são menor número e possuem pouca funcionalidade. Existem 4 registradores *somente leitura*:

* ``:`` - Este registrador possui seu último comando.
* ``.`` - Este registrador possui o último texto que você inseriu.
* ``%`` - Este registrador possui o nome completo do arquivo em edição.
* ``#`` - Este registrador possui o nome completo do arquivo editado anteriormente.

Qual o sentido de ter esse registradores? Eu pessoalmente uso muito o registrador ``%`` pois sempre que escrevo sobre programação coloco o nome do arquivo como o primeiro comentário. Então basta um comando e o VIM se encarrega de tudo, eu não preciso ficar lembrando em que arquivo estou. O registrador ``:`` é muito útil também para editar o seu ``.vimrc``, pois todo usuário de VIM testa diversas configurações e depois coloca as quais melhor se adaptou no seu ``.vimrc``. Mas e se o seu último comando foi muito grande, por exemplo:

.. code::

        set hlsearch incsearch smartcase nocompatible number ruler showcmd showmatch cursorline wrap linebreak hidden nobackup noswapfile splitbelow splitright

E aí meu amigo, você vai digitar tudo novamente? Não! Você vai chegar no seu ``.vimrc`` e digitar ``":p`` (não, isso não é um *emoticon*).

Registradores de Leitura e Escrita
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Os registradores de leitura e escrita podem ser lidos (com os comandos demonstrados anteriormente) e podem ser escritos utilizando comandos de deleção (`dDCScsx` dentre outros), gravação de macro (`q`) e via VimScript, com o comando ``let``, por exemplo: ``let @a="teste"``

O VIM tem os seguintes registradores:
* ``"`` - *Unnamed Register*;
* ``0`` a ``9`` - *Numbered registers*;
* ``-`` -  - *Small Delete Register*;
* ``a`` a ``z`` ou ``A`` a ``Z`` - *Named registers* (26 ao todo);
* ``=`` - *Expression Register*;
* ``*``, ``+`` e ``~`` - *Selection and Drop Registers*;
* ``_`` - *Black Hole Register*;
* ``/`` - *Last Search Register*;

A princípio parece que são muitos registradores, mas com um pouco de uso tudo começa a faze sentido. Vamos começar devagar:

*Unnamed Register* (``"``):
        Este registrador é preenchido pelo VIm toda vez que você deleta ou
        copia um texto, mesmo que você especifique outro registrador. Ele serve
        como um "atalho" para o último registrador utilizado, com exceção de
        quando é utilizado o Black Hole (``_``).
*Numbered register* (``0``):
        Este registrador numerado se comporta de forma diferente do restante.
        Este **apenas** o conteúdo que você copia, a não ser que você
        especifique outros registrador durante a cópia.
*Numbered registers* (``1`` a ``9``):
        Estes registradores funcionam como uma fila para toda **linha** que
        você deleta. O conteúdo mais recentemente deletado estará em ``1`` e o
        mais velho em ``9``. Quando você deleta algo ele vai diretamente para
        ``1`` e o antigo conteúdo do ``1`` vai para o ``2``, e assim
        sucessivamente. Lembrando que quando você cola um texto sobre outro,
        você está fazendo uma deleção.
*Small Delete Register* (``-``):
        Você notaram que nos registradores de ``1`` a ``9`` eu falei que eles
        recebem toda **linha** deletada? Pois é, se você deletar menos de uma
        linha completa ele vem para neste registrador. Isso foi criado para
        evitar que pequenas deleções (``x``), que geralmente são feitas em
        sequência e um número significativo, sobrescrevessem todos os
        registradores rapidamente.
*Named registers* (26 ao todo) (``a`` a ``z`` ou ``A`` a ``Z``):
        Estes registradores só são preenchido quando você informa, o VIM não
        faz nada de automático neles. Vale ressaltar que os registradores
        minúsculos se comportam de maneira diferente dos registradores
        maiúsculos. Ao se escrever em um registrador minúsculo o conteúdo
        anterior é sobrescrito. Já em um registrador maiúsculo, o conteúdo
        antigo é preservado e o conteúdo novo e adicionado ao final do conteúdo
        antigo.
*Expression Register* (``=``):
        Este registrador incomum, ele serve para fazer cálculos. O quê? Você
        não sabia que o VIM é uma calculadora também? Basta (no modo de
        inserção) você digitar ``CTRL-r=32*64`` e o VIM vai inserir o resultado
        do cálculo.
*Selection and Drop Registers* (``*``, ``+`` e ``~``):
        Este é outro grupo de registradores bizarros. O ``+`` é o *clipboard*
        do sistema operacional, então quando você copia algo do Firefox e quer
        colar no VIM você pode simplesmente fazer ``"+p`` (você nem precisa
        usar o ``:set paste`` pra funcionar). Já o ``*`` é utilizado pelo GVIM
        quando você faz uma seleção com o mouse (no próprio GVIM). Por último o
        registrador ``~`` armazena aquilo que é arrastado para dentro do GVIM
        (sim, clique e arrasta, o VIM faz isso também!).
*Black Hole Register* (``_``):
        Como o nome sugere, ele é um buraco negro. Serve como uma lixeira,
        quando você não quer que algum conteúdo para para nenhum registrador.
*Last Search Register* (``/``):
        Este registrador possui a última pesquisa realizada. Você escreve nele
        ao fazer uma busca ou com o comando ``let``, conforme explicado
        anteriormente.

Mas e o Problema Inicial
------------------------

Agora voltando ao problema inicial: "realizar deleções sem sobrescrever o texto já copiado". Uma vez que entendemos que cada registrador possui um propósito específico, percebemos que o "problema" inicial na verdade não existe, pois o próprio VIM favorece o seu *workflow* com o conceito de registradores exposto anteriormente. A pergunta correta é: "Como eu colo um texto já copiado sendo que eu já fiz deleções após a cópia?". E a resposta deste problema se resume a três letras: ``"0p``

Não entendeu? Não se acanhe, algumas coisas no VIM são difíceis de se entender à primeira vista. Vou explicar detalhadamente:

Cópia do Texto:
        Digamos que você está em uma linha específica e realiza uma cópia de
        toda a linha com o comando ``yy``. O conteúdo desta linha vai para dois
        registradores, o "*Yank Register*" (``0``) e o *Unnamed Register*
        (``"``).
Deleção de Texto:
        Em seguida você realiza diversas deleções, digamos, com o comando
        ``dd``. O conteúdo deletado sobrescreve o *Unnamed Register* (``"``) e
        os *Numebred Registers* (de ``1`` a ``9``, dependendo do número de
        deleções). Entretanto, a deleção não sobrescreve o "*Yank Register*"
        (``0``), pois este registrador é apenas para cópias.
Colagem do Texto Copiado:
        Por fim você deseja colar o conteúdo copiado anteriormente, que agora
        sabemos estar no registrador ``0``. Para isso podemos usar co comando
        de "colagem" (``p``) indicando o conteúdo do "*Yank Register*"
        (``"0``), ou seja: ``"0p``

Aí você me pergunta: "Mas e se eu colar por cima de um texto, eu vou escrever em qual registrador". Uma "colagem" por cima de um texto, nada mais é que um deleção seguida de uma "colagem", logo você sobrescreve os mesmos registradores citados anteriormente (``"`` e do ``1`` ao ``9``).

Bonus Track
-----------

Tem muita gente que começa a usar registradores e acha um empecilho sair do modo de inserção para colar o conteúdo de um registrador. A boa notícia é, você não precisa sair do modo de inserção. Durante a digitação de uma texto basta invocar o comando ``CTRL-r<nome do registrado>`` para inserir o conteúdo desejado. Exemplo: para inserir o conteúdo do registrador ``0`` basta usar a sequência de teclas ``CTRL-r-0``. O ``CTRL-R`` tem diversas funcionalidades, como por exemplo, no modo de comando, ``CTRL-r CTRL-w`` insere a palavra sobre o cursor (dica do  Amadeus Folego na lista de *VIM Users BR*). Note que você não precisa segurar o ``CTRL-r`` enquanto tecla o número 0 (ou o ``CTRL-w``), pode soltá-lo, afinal de contas, um dos objetivos do VIM é reduzir problemas como LER.

.. _lista de discussão de usuários de VIM do Brasil: https://groups.google.com/forum/#!forum/vim-users-br
