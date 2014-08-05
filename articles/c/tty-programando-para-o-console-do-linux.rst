TTY - Programando para o console do Linux
=========================================
:date: 2014-08-04 13:55
:category: C
:tags: c, linux, tty, programção, terminal, cr, lf, flush
:image: /images/logos/terminal.jpg
:author: Fernando Almeida
:description: É curioso como certas coisas (mesmo defasadas caídas em desuso) se mantêm no mundo da tecnologia, o disquete como símbolo de salvar, as teclas HJLK no VIM, o conceito de TTY no GNU/Linux...

Outro dia eu estava desenvolvendo um programa para o GNU/Linux em modo texto e esse programa executaria algumas operações e deveria exibir o status dessa execução no terminal. Pois bem, foi aí que me deparei com algumas características interessantes do famoso "modo texto" do GNU/Linux. Acabei tropeçando também em muita história interessante que gostaria de compartilhar.

.. image:: {filename}/images/tty/terminal.jpg
        :target: {filename}/images/tty/terminal.jpg
        :alt: Terminal
        :align: center

Na verdade o correto não é modo texto, mas sim "Terminal". Terminal, Modo Texto, TTY? *What the Hell*?

.. more

Um pouco de história
--------------------
O TTY, ou *teletypewriter*, era uma espécie de maquina de escrever eletrônica usada para enviar e receber mensagens ponto-a-ponto ou mensagens ponto-a-multiponto através de vários tipos de canais de comunicação. Mais tarde esses terminais TTY foram adaptados afim de serem usados como interface do usuário em sistemas de Mainframes e Minicomputadores. Vejam só! A primeira interface de usuário era um dispositivo eletro-mecânico!

.. figure:: {filename}/images/tty/asr33.jpg
        :target: {filename}/images/tty/asr33.jpg
        :alt: Teletype Modelo 33 ASR Teleprinter
        :align: center

        Teletype Modelo 33 ASR Teleprinter

Esses terminais TTY trabalhavam com um conjunto de caracteres e imprimiam em papel a mensagem - Por isso também eram conhecidos como *Hard Copy Terminal*, e também possuíam um conjunto de caracteres de controle que serviam para executar operações como mover o cursor de volta para o inicio da linha (CR - *Carriage Return*), avançar uma linha na mesma coluna (LF - *Line Feed*), e assim por diante.

A evolução dos terminais TTY se deu com a adição de um monitor de vídeo como saída padrão das informações. Esses terminais ficaram conhecidos como *Computer Terminals*. A partir desses terminais de texto era feita toda a entrada e saída de dados de um sistema de computador. Os terminais mais comuns na época eram o IBM 3270 e o DEC VT100.

.. raw:: html

        <div class="row">
                  <div class="col-sm-6 col-md-6">

.. figure:: {filename}/images/tty/ibm3270.jpg
        :target: {filename}/images/tty/ibm3270.jpg
        :alt: Terminal IBM 3270
        :align: center

        Terminal IBM 3270 (Não, este não sou eu trabalhando...)

.. raw:: html

        </div>
        <div class="col-sm-6 col-md-5">

.. figure:: {filename}/images/tty/decvt100.jpg
        :target: {filename}/images/tty/decvt100.jpg
        :alt: Terminal DEC VT100
        :align: center

        Terminal DEC VT100

.. raw:: html

        </div>
        </div>

Terminais de Texto
------------------
Sistemas operacionais padrão Unix (como o GNU/Linux e o FreeBSD) possuem consoles virtuais para fornecer vários terminais de texto em um único computador. A principal função do terminal de texto é de interpretador de linha de comando (ou shell), que interpreta os comandos do usuário, executa cada comando e então retorna informações.

Terminais Burros - São chamados assim porque de nada servem se não estão em conexão com um servidor. Nenhum processo é executado no terminal, mas sim no servidor. No Terminal Burro temos apenas a entrada de dados (via teclado) e a saída ou retorno de dados (via monitor). Existem também Terminais Gráficos que exibem imagens, o X11 é um servidor de terminais gráficos usados para enviar imagens à terminais gráficos.

O Problema
----------

Agora que conhecemos um pouco da história dos TTY, vamos ver um pouco das características do TTY. Vamos imaginar um programa em C desenvolvido para GNU/Linux, que irá executar
em modo texto. Esse programa irá executar algumas operações e gostaríamos de ter um *feedback* afim de saber em que passo estamos e quanto falta para terminar. Então podemos considerar o seguinte programa:

.. code-block:: c

        #include <stdio.h>

        int main(void) {
                int status;
                long int d1, d2;

                for(status = 1; status <= 100; status++) {
                        printf("Processando - %u%%\n", status);
                        // Operacoes do programa
                        for(d1 = 1; d1 <= 6500; d1++) for(d2 = 1; d2 <= 6500; d2++); // Tarefa DUMMY - Apenas para consumir tempo e simular funcionamento.
                }
                printf("\nFinalizado!\n");
        }

Neste caso teríamos uma saída assim:

.. code::

        Processando - 1%
        Processando - 2%
        Processando - 3%
        Processando - 4%
        Processando - 5%
        .
        .
        .
        Processando - 96%
        Processando - 97%
        Processando - 98%
        Processando - 99%
        Processando - 100%

        Finalizado!

Estranho não? Uma linha para cada atualização do status da execução - Nada profissional. Não existe um meio de exibir a atualização na mesma linha?

A Herança do TTY
----------------
Agora vamos perceber o seguinte: Muito foi herdado dos terminais TTY, como os caracteres de controle por exemplo.

No nosso programa exemplo o ideal é mover o cursor para o início da mesma linha a cada passo que o programa atualize o status. Usaremos o caractere especial
*Carriage Return* (CR). No C ele é representado pelo ``\r``.

Você deve conhecer o caractere especial chamado *Line Feed* (LF). No C ele é representado pelo ``\n`` e serve para mover o cursor para a próxima linha. Veja que ele está presente no nosso programa no comando ``printf``. Vamos atualizar nosso programa, removendo o ``\n`` no final da *string* do ``printf`` e incluindo o ``\r`` no início.

.. code-block:: c

        #include <stdio.h>

        int main(void) {
                int status;

                for(status = 1; status <= 100; status++) {
                        printf("\rProcessando - %u%%", status);
                        // Operacoes do programa
                        for(d1 = 1; d1 <= 6500; d1++) for(d2 = 1; d2 <= 6500; d2++); // Tarefa DUMMY - Apenas para consumir tempo e simular funcionamento.
                }
                printf("\nFinalizado!\n");
        }

Pela lógica tudo nos parece bem. Agora vamos ter a atualização do status na mesma linha. Vamos testar? Vai lá... Compile e execute o código. Eu espero.

.. image:: {filename}/images/tty/waiting.jpg
        :target: {filename}/images/tty/waiting.jpg
        :alt: Esperando...
        :align: center

Ei! O que está acontecendo? O programa está estranho... lá pelos 63% que tivemos a primeira atualização de tela e logo depois o programa terminou. Mas afinal, o que
aconteceu aqui?

Bem, o que aconteceu aqui não pode ser chamado de **erro**, mas sim de **característica**. Explico: Do mesmo modo que herdamos os caracteres de controle como o *Carriage Return* (CR)
e o *Line Feed* (LF), herdamos algumas outras características como a velocidade dos terminais e o conceito de *buffer* de dados. A atualização de dados do nosso programa foi
mais rápido do que o terminal, e por isso pouco vimos da execução do nosso programa.

Para ver qual é a velocidade do nosso terminal podemos usar o comando ``stty`` do GNU/Linux. Este comando é usado para alterar ou exibir as configurações do terminal.

No entanto não adianta alterar a velocidade do nosso terminal. Isso não resolve o problema porque velocidade máxima do terminal ainda é inferior ao fluxo de dados do
nosso programa. Então o problema que ocorre aqui refere-se ao fluxo de dados do terminal, portanto é será necessário atualizar o terminal manualmente, despejando todo o
fluxo de dados no *buffer* para a tela usando a função ``fflush()`` - *Flush* também é o termo em inglês para dar a descarga... Vamos dar descarga no terminal!

.. image:: {filename}/images/tty/flush.jpg
        :target: {filename}/images/tty/flush.jpg
        :alt: Flushing...
        :align: center

Resolvendo o Problema
---------------------

O terminal é considerado um arquivo (ou *stream*) no GNU/Linux. Então a função ``fflush()`` força uma gravação de todos os dados em *buffer* para a saída de dados. Se o argumento
da função for ``NULL``, ``fflush()`` dá a descarga em todos os *streams* abertos. Então vejamos:

.. code-block:: c

        #include <stdio.h>

        int main(void) {
                int status;

                for(status = 1; status <= 100; status++) {
                        printf("\rProcessando - %u%%", status);
                        fflush(stdout); // Dando descarga de stdout...
                        // Operacoes do programa
                        for(d1 = 1; d1 <= 6500; d1++) for(d2 = 1; d2 <= 6500; d2++); // Tarefa DUMMY - Apenas para consumir tempo e simular funcionamento.
                }
                printf("\nFinalizado!\n");
        }


Feito isso está garantido. Toda informação será descarregada do *buffer* para o terminal.

BONUS AREA
----------
Que tal exibir uma barra de status ao invés de exibir a porcentagem? Vamos ao código:

.. code-block:: c

        #include <stdio.h>

        #define BS_SZ 60 // Tamanho da barra de status

        int main(void) {
            int status;
                long int d1, d2;

                for(status = 0; status <= BS_SZ; status++) {
                    printf("\rProcessando: ["); // Abre a barra de status
                        for(d1 = 1; d1 <= status; d1++) printf("="); // Exibe status atual
                    for(d1 = (status + 1); d1 <= BS_SZ; d1++) printf(" "); // Preenche com espaco em branco
                        printf("]"); // Fecha a barra de status
                        fflush(stdout);
                    for(d1 = 1; d1 <= 9900; d1++) for(d2 = 1; d2 <= 9900; d2++);
                }
                printf("\nFinalizado!\n");
        }

Para alterar o tamanho da barra de status, altere o valor da constante BS_SZ para o tamanho que desejar. Lembre-se apenas de usar um número menor do que o
número de colunas do terminal para não ficar estranho!

Para um pouco mais de história ou mais informações, seguem alguns links interessantes:

- `O Teleprinter TTY`_
- `Computer Terminal`_
- `fflush()`_

.. _O Teleprinter TTY: http://en.wikipedia.org/wiki/Teletypewriter
.. _Computer Terminal: http://en.wikipedia.org/wiki/Computer_terminal
.. _fflush(): http://man7.org/linux/man-pages/man3/fflush.3.html

Até a próxima!
