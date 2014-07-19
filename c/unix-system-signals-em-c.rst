UNIX System Signals em C
########################
:date: 2014-06-25 15:51
:category: C
:tags: c, unix, signals, programação, desenvolvimento, posix, linux, bsd, processos
:image: /images/logos/tcpl.jpg
:author: Fernando Almeida
:description: Conhecer plenamente as ferramentas e plataformas com as quais trabalhamos pode ser quase impossível, mas é sempre divertido aprender as particularidades e peculiaridades para (então) podermos tornar nossas soluções cada vez mais nativas.

Sempre que desenvolvo programas, tento saber as regras básicas de cada sistema operacional. Os motivos? Bem, por dois simples motivos: Compatibilidade e Praticidade

.. image:: {filename}/images/c/tcpl.jpg
        :target: {filename}/images/c/tcpl.jpg
        :alt: C - The Programming Languagen
        :align: center

Compatibilidade porque esses programas, para serem considerados compatíveis, devem obedecer as regras e práticas do sistema operacional alvo. Essa compatibilidade também pode ser chamada de *compliance*. Praticidade porque muito do que o programador precisa já existe no sistema operacional. Nada de reinventar a roda!

.. more

Quando desenvolvendo programas para  sistemas operacionais padrão UNIX, como o Linux e o FreeBSD por exemplo, principalmente *daemons* ou programas específicos, é importante conhecer o conceito de sinais. Esses sinais, ou *UNIX SYSTEM SIGNALS*, é a interface entre os processos e o *kernel* do SO. Um processo é qualquer programa rodando no SO.

A dinâmica de envio dos sinais é bem simples:

- Quando um processo recebe um sinal que não pode ser ignorado, este programa é imediatamente interrompido;
- O controle é recebido por um *signal handler*, definido dentro do processo. *Signal Handler* é basicamente colocar o processo em modo escuta (*listen mode*);
- Após o *signal handler* completar, o programa retorna de onde estava no momento do *listner*.

Enviando Sinais
---------------

Quando executamos o comando kill -9 Process_ID o que na verdade estamos fazendo é enviar um sinal do tipo SIGKILL para um processo. O número 9 é na verdade o valor para SIGKILL. Outro exemplo é o pressionamento das teclas CTRL+C dentro de um programa. Esta combinação envia SIGINT para o processo. Abaixo temos uma tabela dos códigos padrão UNIX:

.. table::
        :class: table

        ========== ====== =============================================== =========
        Sinal      Valor  Descrição                                       Manejável
        ========== ====== =============================================== =========
        SIGHUP     1      Hangup (POSIX)                                  Sim
        SIGINT     2      Interrupt (ANSI) – O mesmo que CTRL+C           Sim
        SIGQUIT    3      Quit (POSIX)                                    Sim
        SIGILL     4      Illegal Instruction (ANSI)                      Sim
        SIGTRAP    5      Trace trap (POSIX)                              Sim
        SIGABRT    5      Trace trap (POSIX)                              Sim
        SIGIOT     6      Abort (ANSI)                                    Sim
        SIGIOT     6      IOT trap (4.2 BSD)                              Sim
        SIGBUS     7      BUS error (4.2 BSD)                             Sim
        SIGFPE     8      Floating-Point arithmetic Exception (ANSI)      Sim
        SIGKILL    9      Kill, unblockable (POSIX)                       Não
        SIGUSR1    10     User-defined signal 1                           Sim
        SIGEGV     11     Segmentation Vionation (ANSI)                   Sim
        SIGUSR2    12     User-defined signal 2                           Sim
        SIGPIPE    13     Broken pipe (POSIX)                             Sim
        SIGALRM    14     Alarm clock (POSIX)                             Sim
        SIGTERM    15     Termination (ANSI)                              Sim
        SIGTKFLT   16     Stack fault                                     Sim
        SIGCHLD    16     Stack fault                                     Sim
        SIGCLD     17     Child status has changed (POSIX)                Sim
        SIGCONT    18     Continue (POSIX)                                Sim
        SIGSTOP    19     Stop, unblockable (POSIX)                       Não
        SIGTSTP    20     Keyboard stop (POSIX) – O mesmo que CTRL+Z      Sim
        SIGTTIN    21     Background read from tty (POSIX)                Sim
        SIGTTOU    22     Background write from tty (POSIX)               Sim
        SIGURG     23     Urgent condition on socket (4.2 BSD)            Sim
        SIGXCPU    24     CPU limit exceeded (4.2 BSD)                    Sim
        SIGXFSZ    25     File size limie exceeded (4.2 BSD)              Sim
        SIGVTALRM  26     Virtual Time Alarm (4.2 BSD)                    Sim
        SIGPROF    27     Profiling alarm clock (4.2 BSD)                 Sim
        SIGWINCH   28     Window size change (4.3 BSD, Sun)               Sim
        SIGIO      28     Window size change (4.3 BSD, Sun)               Sim
        SIGPOLL    29     I/O now possible (4.2 BSD)                      Sim
        SIGPOLL    29     Pollable event ocurred (System V)               Sim
        SIGPWR     30     Power failure restart (System V)                Sim
        SIGSYS     31     Bad system call                                 Sim
        ========== ====== =============================================== =========

Podemos ver na tabela que são poucos os sinais que não podem ser manejáveis. Isso significa que para esses sinais não é possível implementar *signal handlers*. Em poucas palavras: o processo não pode ignorar um sinal do tipo ``SIGSTOP`` ou ``SIGKILL``.

Mão Na Massa
------------

O objetivo deste artigo é a implementação de um *system handler* em C. Para mais detalhes sobre os *system signals*, você pode usar *man signal* no seu GNU/Linux. Inclui também alguns links sobre o assunto no `final`_ do artigo.

Para usar os system signals no seu programa, precisamos fazer uso da biblioteca signal.h conforme abaixo:

.. code-block:: c

	#include <signal.h>

O *header* ``signal.h`` define as constantes simbólicas da tabela de sinais acima. Feito isso, vamos à nossa função de *signal handler*. Você pode chamar esta função como bem desejar. No programa exemplo eu chamei de *sig_handler*:

.. code-block:: c

	void sig_handler(int signo) {
		switch(signo) {
			case SIGINT :
				printf("SIGINT\nO usuario pressionou CTRL+C, entao sair!\n");
				exit(signo);
			case SIGSYS :
				printf("SIGSYS\nBad system call\n");
				break;
			case SIGHUP :
				printf("SIGHUP\nHangup (POSIX)\n");
				break;
			case SIGTERM :
				printf("SIGTERM\nTermination (ANSI)\nO usuario quer parar o processo. Mas nao vou parar!\n");
				break;
			case SIGUSR1 :
				printf("SIGUSR1\nUser-defined signal 1\n");
				break;
			case SIGUSR2 :
				printf("SIGUSR2\nUser-defined signal 2\n");
				break;
			default :
				printf("SIGNAL %d\n", signo);
		}
	}

Até agora só criamos os *handlers* e definimos como tratar cada sinal. Veja que dentro do ``switch`` temos cada sinal que desejamos tratar e o que fazer caso eles ocorram, mas também defini o *default* para exibir qual o sinal recebido e que não fora tratado em separado.

Bom, agora a parte legal: Colocar nossos *system handlers* no modo escuta. Isto é feito através da função *signal*. É necessário ligar cada *signal* que você deseja ouvir no seu processo:

.. code-block:: c

	if(signal(SIGINT, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGINT\n");
	if(signal(SIGSYS, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGSYS\n");
	if(signal(SIGHUP, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGHUP\n");
	if(signal(SIGTERM, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGTERM\n");
	if(signal(SIGUSR1, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGUSR1\n");
	if(signal(SIGUSR2, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGUSR2\n");

Veja que iniciei cada *handler* com um teste ``if``. Isso garante que foi possível (ou não) iniciar a escuta daquele sinal em particular. Tente por exemplo iniciar um handler para o SIGKILL e você receberá a mensagem de erro. Você deve ter visto na tabela que o ``SIGKILL`` não é manejável, certo? Então...

Pronto. Colocamos em modo escuta somente os sinais ``SIGINT``, ``SIGSYS``, ``SIGHUP``, ``SIGTERM``, ``SIGUSR1`` e ``SIGUSR2``. Lembre-se de inciar cada *handler* que deseja escutar, mas também lembre-se de tratá-lo na função ``sig_handler``, ou o sinal será interpretado pelo *default* dentro do ``switch``.

A implementação completa do nosso programa seria:

.. code-block:: c

	#include <stdio.h>
	#include <stdlib.h>
	#include <string.h>
	#include <signal.h> // para as constantes de signal handler
	#include <unistd.h>

	void sig_handler(int signo) {
		switch(signo) {
			case SIGINT :
            	printf("SIGINT\nO usuario pressionou CTRL+C, entao sair!\n");
				exit(signo);
			case SIGSYS :
				printf("SIGSYS\nBad system call\n");
				break;
			case SIGHUP :
				printf("SIGHUP\nHangup (POSIX)\n");
				break;
			case SIGTERM :
				printf("SIGTERM\nTermination (ANSI)\nO usuario quer parar o processo. Mas nao vou parar!\n");
				break;
			case SIGUSR1 :
				printf("SIGUSR1\nUser-defined signal 1\n");
				break;
			case SIGUSR2 :
				printf("SIGUSR2\nUser-defined signal 2\n");
				break;
			default :
				printf("SIGNAL %d\n", signo);
		}
	}

	int main(void) {

		if(signal(SIGINT, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGINT\n");
		if(signal(SIGSYS, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGSYS\n");
		if(signal(SIGHUP, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGHUP\n");
		if(signal(SIGTERM, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGTERM\n");
		if(signal(SIGUSR1, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGUSR1\n");
		if(signal(SIGUSR2, sig_handler) == SIG_ERR) printf("\nImpossivel iniciar o handler SIGUSR2\n");

		printf("Programa principal rodando...\n");

		while(1)  {
			sleep(1); // Outras funções do programa
		}

		return 0;
	}

Todo o código fonte está disponível no `GitHub`_.

Executando
----------

Agora vamos compilar o programa. Não é necessário nenhum parâmetro específico para o compilador.

.. image:: {filename}/images/c/1-Compilando.jpg
        :target: {filename}/images/c/1-Compilando.jpg
        :alt: Compilando
        :align: center

Feito isso temos o nosso ``getsignal`` binário, pronto para ser executado. Vamos executar agora nosso programa e vamos aos testes. O primeiro teste é verificar o programa está rodando corretamente.

.. image:: {filename}/images/c/2-Rodando.jpg
        :target: {filename}/images/c/2-Rodando.jpg
        :alt: Rodando
        :align: center


Nosso primeiro teste é enviar um sinal do tipo ``SIGINT`` para o processo. Ou seja: Vamos enviar um ``CTRL+C`` e ver o que acontece.

.. image:: {filename}/images/c/3-Enviando-SIGINT.jpg
        :target: {filename}/images/c/3-Enviando-SIGINT.jpg
        :alt: Enviando SIGINT
        :align: center


Perceba que nosso programa fez o que estava definido a ser feito dentro do ``switch`` na nossa função ``sig_handler``. Verifique que usei a função ``exit(signo);`` Esta função termina o processo e retorna ``2``, ou ``SIGINT`` para o ``EXIT CODE`` do SO.

O ``EXIT CODE`` de um processo é um número passado de um processo filho (ou receptor) para um processo pai (ou chamador), quando terminar a execução de um procedimento específico ou tarefa delegada. No nosso caso o processo filho é o ``getsignal`` e o processo pai é o *bash*.

Para verificar qual é o ``EXIT CODE`` atual, podemos usar ``echo $?`` Conforme a seguir:

.. image:: {filename}/images/c/4-Verificando-EXIT-CODE.jpg
        :target: {filename}/images/c/4-Verificando-EXIT-CODE.jpg
        :alt: Verificando EXIT CODES
        :align: center

Antes de executar o ``getsignal`` tinhamos um ``EXIT CODE = 0``. Depois que executamos e enviamos ``CTRL+C`` para o processo, o programa interpretou nosso comando e terminou nosso processo, retornando ``EXIT CODE = 2``.

Para o nosso segundo teste vamos deixar o ``getsinal`` rodando no TTY1 e vamos para outro terminal TTY2 enviar um sinal do tipo ``SIGSYS`` (valor 31) para o nosso processo.

.. image:: {filename}/images/c/5-Enviando-SIGSYS.jpg
        :target: {filename}/images/c/5-Enviando-SIGSYS.jpg
        :alt: Enviando SIGSYS
        :align: center

Neste exemplo nosso processo estava sendo executado normalmente em TTY1 quando recebeu um ``SIGSYS`` enviado pelo usuário em TTY2. Nosso processo interpretou esse sinal e continuou sendo executado.

É isso! Tentei ser o mais prático na demostração dos *system signals* e como implementá-los em C. A partir daqui é possível criar programas para Linux que tratam os sinais corretamente.

Saiba Mais
----------

Para mais informações sobre os *system signals* recomendo os seguintes links:

- `Introduction to UNIX Signals and System Calls`_
- `C/C++ signal handling`_

E para mais informações sobre *EXIT CODES*, recomendo o seguinte link:

- `Chapter 6. Exit and Exit Status`_

Obrigado!

.. _final: #saiba-mais
.. _Introduction to UNIX Signals and System Calls: http://ph7spot.com/musings/introduction-to-unix-signals-and-system-calls
.. _C/C++ signal handling: http://www.yolinux.com/TUTORIALS/C++Signals.html
.. _Chapter 6. Exit and Exit Status: http://www.tldp.org/LDP/abs/html/exit-status.html
.. _GitHub: https://github.com/fer-almeida/getsignal
