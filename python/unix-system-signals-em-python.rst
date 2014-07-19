UNIX System Signals em Python
#############################
:date: 2014-06-30 18:00
:category: Python
:tags: python, unix, signals, programação, desenvolvimento, posix, linux, bsd, processos
:image: /images/python.png
:description: A integração do UNIX System Signals também está presente no Python e na maioria das linguagens disponíveis para o sistema operacional GNU/Linux. Afinal de contas, é um padrão!

Após publicar o texto sobre `UNIX System Signals em C`_, percebi que pode ter dado a impressão que apenas a linguagem C possui essa integração. Com isso, escrevi este artigo para demonstrar o mesmo mecanismo demonstrado pelo `Fernando Almeida`_.

.. image:: {filename}/images/python/zen-of-python-poster.png
        :target: {filename}/images/python/zen-of-python-poster.png
        :alt: Zen of Python
        :align: center


Todo o conceito de sinais, sua dinâmica de envio e uma tabela listando todos os sinais existentes está disponível `aqui`_. Então vamos direto para o código!

.. more

Mão Na Massa
------------

O objetivo deste artigo é a implementação de um *system handler* em Python. Para mais detalhes sobre os *system signals*, você pode usar *man signal* no seu GNU/Linux. Incluí também alguns links sobre o assunto no `final`_ do artigo.

Para usar os *system signals* no seu programa, precisamos fazer uso módulo ``signal``, disponível na biblioteca padrão. A nossa função de *signal handler* se chamará ``sig_handler`` e deverá ter dois argumentos ``signum`` e ``stack`` respectivamente, o identificador do sinal e o *stack frame* (ou ``None``). Um *stack frame* é um objeto nativo do Python que representa a execução atual do programa. Para mais detalhes sobre `stack frame, veja a documentação do Python`_. Um exemplo da função:

.. code-block:: python

        def sig_handler(signum, stack):
            if signum == signal.SIGINT:
                print "SIGINT"
                print "O usuario pressionou CTRL+C, entao sair!"
                exit(signum)
            elif signum == signal.SIGSYS:
                print "SIGSYS"
                print "Bad system call"
            elif signum == signal.SIGHUP:
                print "SIGHUP"
                print "Hangup (POSIX)"
            elif signum == signal.SIGTERM:
                print "SIGTERM"
                print "Termination (ANSI)"
                print "O usuario quer parar o processo. Mas nao vou parar!"
            elif signum == signal.SIGUSR1:
                print "SIGUSR1"
                print "User-defined signal 1"
            elif signum == signal.SIGUSR2:
                print "SIGUSR2"
                print "User-defined signal 2"
            else:
                print "SIGNAL %i"%signum

Até agora só criamos os *handlers* e definimos como tratar cada sinal. Veja que dentro da função temos cada sinal que desejamos tratar e o que fazer caso eles ocorram, mas também defini o *default* (usando o ``else``) para exibir qual o sinal recebido e que não fora tratado em separado.

Bom, agora a parte legal: Colocar nossos *system handlers* no modo escuta. Isto é feito através da função *signal.signal*. É necessário ligar cada *signal* que você deseja ouvir no seu processo:

.. code-block:: python

    signal.signal(signal.SIGINT, signal.SIG_IGN)
    if signal.signal(signal.SIGINT, sig_handler):
        print "Impossivel inciar o handler SIGINT"
    if signal.signal(signal.SIGSYS, sig_handler):
        print "Impossivel inciar o handler SIGSYS"
    if signal.signal(signal.SIGHUP, sig_handler):
        print "Impossivel inciar o handler SIGHUP"
    if signal.signal(signal.SIGTERM,sig_handler):
        print "Impossivel inciar o handler SIGTERM"
    if signal.signal(signal.SIGUSR1,sig_handler):
        print "Impossivel inciar o handler SIGUSR1"
    if signal.signal(signal.SIGUSR2,sig_handler):
        print "Impossivel inciar o handler SIGUSR2"

Note que, como o Python já escuta por padrão o sinal ``SIGINT`` precisamos primeiramente desativá-lo com o comando ``signal.signal(signal.SIGINT, signal.SIG_IGN)``. Posteriormente iniciei cada *handler* com um teste ``if``. Isso garante que foi possível (ou não) iniciar a escutar daquele sinal em particular. Lembrando que não é possível se conectar a sinais não manejáveis (veja a tabela).

Pronto. Colocamos em modo escuta somente os sinais ``SIGINT``, ``SIGSYS``, ``SIGHUP``, ``SIGTERM``, ``SIGUSR1`` e ``SIGUSR2``. Lembre-se de inciar cada *handler* que deseja escutar, mas também lembre-se de tratá-lo na função ``sig_handler``, ou o sinal será interpretado pelo *default* dentro do ``else``.

A implementação completa do nosso programa seria:

.. code-block:: python

        #!/usr/bin/env python
        # encoding: utf-8

        import os
        import signal

        def sig_handler(signum, stack):
            if signum == signal.SIGINT:
                print "SIGINT"
                print "O usuario pressionou CTRL+C, entao sair!"
                exit(signum)
            elif signum == signal.SIGSYS:
                print "SIGSYS"
                print "Bad system call"
            elif signum == signal.SIGHUP:
                print "SIGHUP"
                print "Hangup (POSIX)"
            elif signum == signal.SIGTERM:
                print "SIGTERM"
                print "Termination (ANSI)"
                print "O usuario quer parar o processo. Mas nao vou parar!"
            elif signum == signal.SIGUSR1:
                print "SIGUSR1"
                print "User-defined signal 1"
            elif signum == signal.SIGUSR2:
                print "SIGUSR2"
                print "User-defined signal 2"
            else:
                print "SIGNAL %i"%signum


        if __name__ == '__main__':
            signal.signal(signal.SIGINT, signal.SIG_IGN)
            if signal.signal(signal.SIGINT, sig_handler):
                print "Impossivel inciar o handler SIGINT"
            if signal.signal(signal.SIGSYS, sig_handler):
                print "Impossivel inciar o handler SIGSYS"
            if signal.signal(signal.SIGHUP, sig_handler):
                print "Impossivel inciar o handler SIGHUP"
            if signal.signal(signal.SIGTERM,sig_handler):
                print "Impossivel inciar o handler SIGTERM"
            if signal.signal(signal.SIGUSR1,sig_handler):
                print "Impossivel inciar o handler SIGUSR1"
            if signal.signal(signal.SIGUSR2,sig_handler):
                print "Impossivel inciar o handler SIGUSR2"

            print 'Meu PID é:', os.getpid()
            print "Programa principal rodando..."

            while(True):
                pass # Outras funções do programa

Executando
----------

Agora executamos nosso programa ``getsignal.py`` e vamos aos testes. O primeiro teste é verificar o programa está rodando corretamente.

.. image:: {filename}/images/python/executando-getsignal.png
        :target: {filename}/images/python/executando-getsignal.png
        :alt: Executando getsignal.py
        :align: center

Nosso primeiro teste é enviar um sinal do tipo ``SIGINT`` para o processo. Ou seja: Vamos enviar um ``CTRL+C`` e ver o que acontece.

.. image:: {filename}/images/python/executando-getsignal-SIGINT.png
        :target: {filename}/images/python/executando-getsignal-SIGINT.png
        :alt: Enviando SIGINT
        :align: center


Perceba que nosso programa fez o que estava definido a ser feito dentro do ``if`` na nossa função ``sig_handler``. Verifique que usei a função ``exit(signum);`` Esta função termina o processo e retorna ``2``, ou ``SIGINT`` para o ``EXIT CODE`` do SO.

O ``EXIT CODE`` de um processo é um número passado de um processo filho (ou receptor) para um processo pai (ou chamador), quando terminar a execução de um procedimento específico ou tarefa delegada. No nosso caso o processo filho é o ``getsignal.py`` e o processo pai é o *bash*.

Para verificar qual é o ``EXIT CODE`` atual, podemos usar ``echo $?`` Conforme a seguir:

.. image:: {filename}/images/python/executando-getsignal-retcode.png
        :target: {filename}/images/python/executando-getsignal-retcode.png
        :alt: Verificando EXIT CODES
        :align: center

Antes de executar o ``getsignal`` tínhamos um ``EXIT CODE = 0``. Depois que executamos e enviamos ``CTRL+C`` para o processo, o programa interpretou nosso comando e terminou nosso processo, retornando ``EXIT CODE = 2``.

Para o nosso segundo teste vamos deixar o ``getsinal`` rodando no TTY1 e vamos para outro terminal TTY2 enviar um sinal do tipo ``SIGSYS`` (valor 31) para o nosso processo.

.. image:: {filename}/images/python/executando-getsignal-kill-31.png
        :target: {filename}/images/python/executando-getsignal-kill-31.png
        :alt: Enviando SIGSYS
        :align: center

Neste exemplo nosso processo estava sendo executado normalmente em TTY1 quando recebeu um ``SIGSYS`` enviado pelo usuário em TTY2. Nosso processo interpretou esse sinal e continuou sendo executado.

É isso! Tentei migrar todas as ideias da demostração dos *system signals* e implementados em C para a linguagem Python. A partir daqui é possível criar programas para GNU/Linux que tratam os sinais corretamente.

Saiba Mais
----------

Para mais informações sobre os *system signals* recomendo os seguintes links:

- `Introduction to UNIX Signals and System Calls`_
- `C/C++ signal handling`_

E para mais informações sobre *EXIT CODES*, recomendo o seguinte link:

- `Chapter 6. Exit and Exit Status`_

Até mais...

.. _UNIX System Signals em C: /pt/unix-system-signals-em-c
.. _Fernando Almeida: /pt/author/fernando-almeida
.. _aqui: /pt/unix-system-signals-em-c
.. _final: #saiba-mais
.. _stack frame, veja a documentação do Python: https://docs.python.org/2/reference/datamodel.html#frame-objects

.. _Introduction to UNIX Signals and System Calls: http://ph7spot.com/musings/introduction-to-unix-signals-and-system-calls
.. _C/C++ signal handling: http://www.yolinux.com/TUTORIALS/C++Signals.html
.. _Chapter 6. Exit and Exit Status: http://www.tldp.org/LDP/abs/html/exit-status.html
