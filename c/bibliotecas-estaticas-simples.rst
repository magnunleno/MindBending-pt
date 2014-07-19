Bibliotecas Estáticas Simples
#############################
:date: 2012-10-01 14:10
:category: C
:tags: ar, bibliotecas, c, código, compartilhada, desenvolvimento, double, elif, else, endif, estática, gcc, guards, if, ifdef, ifndef, include, inclusion, índice, linguagem, nm, preprocessador, programação, projeto, shared, static
:image: /images/bilbiotecas-sqr-2.jpg
:series: Bibliotecas em C

Dando continuidade ao `assunto de bibliotecas estáticas e compartilhadas`_, neste artigo irei ensinar como escrever uma biblioteca etática simples (um único arquivo) na poderosa e universal linguagem C.

.. image:: {filename}/images/bilbiotecas-2.jpg
	:align: center
	:target: {filename}/images/bilbiotecas-2.jpg
	:alt: Bibliotecas 2

Esse é um assunto divertido e ao mesmo tempo desafiante, já que existem poucas informações disponíveis. Se você não sabe o que são bibliotecas estáticas (static libraries) e/ou compatilhadas (shared libraries), visite meu outro artigo e compreenda a diferença: `Introdução à Bilbiotecas em C`_. Agora vamos lá!

.. more

Estrutura da Biblioteca
-----------------------

Uma biblioteca precisa de **pelo menos** dois arquivos: um arquivo de código (.c) e um arquivo de cabeçalho (.h). O arquivo de código será compilado e agrupado posteriormente em um arquivo com a extensão *.a* e tem como finalidade conter todo o código que se tornará programa, já a arquivo .h deverá ser movido para um diretório que o compilador (ou as ferramenta pkg-config e libtool) possa encontrá-los e tem como finalidade apenas "indicar" as funções/rotinas que são divulgadas para os programas que importarão nossa biblioteca.

Desta forma, nossa biblioteca será composta de um arquivo chamado *myprint.c* e um arquivo chamado *myprint.h*. Para uma boa organização do nosso projeto estes arquivos estarão dentro da pasta lib. Para fins de testes utilizarei mais um aquivo, o arquivo *main*, que estará dentro da pasta src -- este aquivo representará o usuário de nossa biblioteca.  Por último nosso projeto terá também uma pasta chamada build para onde irá todos binários que iremos compilar, gosto de utilizar isso para facilitar a limpeza do projeto e facilitar a indicação do arquivos ignorados em ferramentas de versionamento (como o git). Abaixo uma representação de como fica o nosso projeto:


.. figure:: {filename}/images/bibliotecas-estaticas-simples.png
	:align: center
	:target: {filename}/images/bibliotecas-estaticas-simples.png
	:alt: Estrutura do código fonte de uma biblioteca estática simples

        Estrutura do código fonte de uma biblioteca estática simples

Código da Biblioteca
--------------------

Arquivo *myprint.h*
~~~~~~~~~~~~~~~~~~~

Nossa biblioteca no possuirá muito código e, assim como qualquer outro programa em C, iniciaremos por criar o arquivo de cabeçalho da biblioteca (arquivo myprint.h). Este aquivo terá o seguinte conteúdo:

.. code-block:: c

        /*
         * myprint.h
         *
         * Biblioteca de exemplo para a criação e uso de bibliotecas estáticas na
         * linguagem C. 
         *
         * Esta arquivo de cabeçalho possui apenas as definições de funções e rotinas.
         *
         * Licença: GPL 3.0
         * Mais informações: http://www.mindbending.org
         *
        */

        #ifndef _MYPRINT_LIB_
        #define _MYPRINT_LIB_

        void my_print(char *str);

        #endif // _MYPRINT_LIB_

Basicamente não há muito o que explicar nesse arquivo, apenas o uso das diretivas do preprocessador ``#ifndef``, ``#define`` e ``#endif``, também chamadas de `*Include Guards*`_ (em uma adaptação para o português significaria "proteção de inclusão"). Para um melhor entendimento destas instruções explicarei "de dentro para fora", isto é, primeiro o ``#define`` e em seguida o par ``#ifndef ... #endif``.

A instrução ``#define`` é usada em C para definir macros, isto é, pequenas tarefas executadas durante a compilação do código. Estas macros podem ser valores fixos -- como #define TAMANHO = 10 -- ou pequenas instruções -- como #define MAX(a, b) a>b ? a : b -- que facilitam a vida do programador, seja "memorizando" para ele pequenas instruções que não merecem uma função ou pra reduzir o número de comandos digitados.  Quando usamos o define com apenas um argumento (como visto acima, ``#define _MYPRINT_LIB_``) apenas define para o preprocessador C que existe uma variável chamada *\_MYPRINT\_LIB\_*.

Já o par ``#ifndef ... #endif`` faz parte de "um pacote maior" de diretivas do preprocessador, são elas:

-  ``#if`` - Verificar se a expressão a seguir é verdadeira ou não;
-  ``#elif`` - Abreviação de ``else if``;
-  ``#ifdef`` - Verifica se uma próxima variável foi definida (pela diretiva ``#define``);
-  ``#ifndef`` - Verifica se uma próxima variável **não** foi definida (pela diretiva ``#define``);
-  ``#else`` - Funciona como um ``else`` comum;
-  ``#endif`` - Marca o fim do bloco;

Basicamente estas instruções funcionam como ``ifs ... else`` comum, porém definem que trecho de código **será ou não incluído** durante a compilação, desta forma podemos escrever um código voltado apenas para uma arquitetura e outro código mais genérico ou até mesmo diferenciar a compilação para cada sistema operacional.

Juntando as duas ideias o *"Include Guards"* primeiro verifica se uma variável foi ou não definida anteriormente e, em caso negativo, permite a execução do bloco de códigos que, logo em seguida, define a variável verificada pelo ``#ifndef`` anterior. Resumindo, você está restringindo que o código a seguir seja "processado mais de uma vez", o que geralmente incorre no problema de *double inclusion* (inclusão dupla) e em conflitos de variáveis/funções/tipos previamente definidos. Para mais informações leia `a documentação do compilador GCC`_.

Em seguida definimos uma função chamada ``my_print`` que não retorna nada mas que recebe como argumento um ponteiro para um array de caracteres que iremos chamar de ``str``. Geralmente essa definição é chamada de "assinatura da função" ou protótipo.

Arquivo *myprint.c*
~~~~~~~~~~~~~~~~~~~

Já o arquivo *myprint.c* (par do arquivo *myprint.h*) possuirá a implementação (código) da função definida anteriormente. Abaixo o conteúdo do arquivo:

.. code-block:: c

        /*
         * myprint.c
         *
         * Biblioteca de exemplo para a criação e uso de bibliotecas estáticas na
         * linguagem C. 
         *
         * Esta arquivo possui a implementação da função my_print.
         *
         * Licença: GPL 3.0
         * Mais informações: http://www.mindbending.org
         *
        */

        #include <stdio.h>
        #include "myprint.h"

        void my_print(char *str){
                printf("My Print: %s\n", str);
                return;
        }


Aqui podemos verificar a inclusão da biblioteca ``stdio.h`` (que possui a definição da função ``printf``) e do arquivo de cabeçalho *myprint.h*.  Você por acaso já se perguntou qual a diferença de se utilizar as aspas ou o sinal de maior/menor? Quando utilizamos um include que se utiliza dos sinais de maior/menos ao redor do nome da biblioteca estamos indicando para o preprocessador que busque estes arquivos de cabeçalho em uma conjunto de diretórios predefinidos (no GNU/Linux geralmente dentro de */usr/lib*), enquanto o outro modo (com aspas) busca apenas no diretório corrente. Desta forma utilizamos os sinal de maior/menor que para bibliotecas instaladas no sistema e aspas para bibliotecas escritas por nos.

Dentro da função ``my_print`` vemos que ela não passa de um ``printf`` que inclui uma descrição *My Print:* antes do texto passado como argumento.

Arquivo *main.c*
~~~~~~~~~~~~~~~~

Muito bem, este é o mais simples dos arquivos de código. Basicamente ele é constituído de um import da biblioteca *myprint.h* (notem que utilizamos o sinal de maior/menos que, uma vez que esta se tratará de uma biblioteca de sistema e não um código fonte simples) e da função ``main``, que por sua vez chama a função ``my_printf`` da biblioteca que criamos.

.. code-block:: c

        /*
         * main.c
         *
         * Programa de exemplo para a criação e uso de bibliotecas estáticas na
         * linguagem C. 
         *
         * Esta arquivo se utiliza da biblioteca my_print.a construída anteriormente.
         *
         * Licença: GPL 3.0
         * Mais informações: http://www.mindbending.org
         *
        */

        #include <myprint.h>

        int main(int argc, char *argv[]){
                my_print("Teste!");
                return 0;
        }

Construíndo a Biblioteca
------------------------

A construção da biblioteca é a parte que requer mais cuidado e atenção, pois existem alguns padrões a serem seguidos. Todos os comandos apresentados aqui devem ser executados a partir da pasta raiz do projeto, isto é, a pasta *prj*.

Primeiramente temos que compilar o arquivo *myprint.c*, e para isso utilize o seguinte comando:

.. code-block:: bash

    $ gcc -c lib/myprint.c -o build/myprint.o

Primeiramente vamos entender o uso das flags. A flag *-c* indica que iremos compilar o código mas não linkar o código, isto é necessário quando nosso código não irá gerar um executável final e, consequentemente, não possui a função ``main``. Já a flag *-o* é utilizada para que possamos definir onde e com que nome o arquivo *.o* será gerado. Desta forma, este comando irá gerar apenas o código de máquina (binário) que precisamos para nossa biblioteca.

A seguir é necessário criar um arquivo com a extensão *.a*. Este arquivo será criado com o comando ``ar``, responsável por criar, modificar e extrair pacotes de arquivos. Este pacote pode conter um ou mais membros (arquivos binários) em estruturas predefinidas. Esse arquivo gerado é "similar" a um arquivo compactado comum (tar, tar.gz, zip e etc), porém é utilizado para gerar bibliotecas. Segue abaixo o comando a ser emitido:

.. code-block:: bash

    $ ar rcs build/libmyprint.a build/myprint.o

Pronto, é apenas isso que é necessário para construir uma biblioteca estática. Mas vamos novamente analisando as flags:

-  A flag r indica que queremos adicionar um membro (*build/myprint.o*) para o arquivo (*build/libmyprint.a*).
-  A flag c indica que, caso o arquivo (*build/libmyprint.a*) não exista, ele deverá ser criado.
-  A flag s solicita ao comando ``ar`` que seja criado um índice no arquivo final.

É **extremamente importante** que o arquivo de saída comece com a palavra lib seguido do exato nome do arquivo de cabeçalho e com a extensão *.a*, pois estes padrões serão buscados pelo compilador C. Para consular o conteúdo do arquivo gerado utilize o comando ``ar`` da seguinte forma:

.. code-block:: bash

    $ ar tv build/libmyprint.a
    rw-r--r-- 1000/1000   1512 Sep 28 14:06 2012 myprint.o

Caso você queira mais detalhes do arquivo gerado no passo anterior utilize o comando ``nm``, um utilitário para listagem de símbolos em arquivos de objetos. Utilize-o da seguinte forma:

.. code-block:: bash

    $ nm -s build/libmyprint.a 

    Archive index:
    my_print in myprint.o

    myprint.o:
    0000000000000000 T my_print
                     U printf

A flag *-s* indica que queremos que seja listado também a índice do arquivo. No arquivo de índice podemos ver as funções que serão externalizadas pela nossa biblioteca, neste caso apenas a função ``my_print``. Na listagem detalhada do arquivo *myprint.o* notamos que são apresentadas duas funções ``my_print`` e ``printf``, porém esta última está com a flag U (simbolo indefinido) e deve ser ignorado. Para que o ``nm`` liste apenas os símbolos **realmente definidos nos arquivos** utilize-o da seguinte forma:

.. code-block:: bash

    $ nm -s --defined-only build/libmyprint.a

Para fins de facilitação e organização, após construir a biblioteca eu gosto de apagar os arquivos *.o* antigos e também gosto de mover o arquivo de cabeçalho para dentro da pasta build. Para isso utilize os seguintes comandos:

.. code-block:: bash

    $ cp lib/myprint.h build/myprint.h
    $ rm build/*.o

Construindo o Programa Cliente
------------------------------

Agora basta construirmos o programa cliente que irá se utilizar da nossa biblioteca. Para isso utilizaremos novamente o GCC, porém com várias flags a mais. Execute conforme abaixo:

.. code-block:: bash

    $ gcc -static src/main.c -L./build -I./build -lmyprint -o build/main.run

Como podemos ver existe uma boa diferença, então vamos analisar uma a uma:

-  *-static* - Indica ao GCC que ele deve linkar utilizando bibliotecas estáticas;
-  *src/main.c* - Informa o nome do arquivo a ser compilado;
-  *-L./build* - Indica onde devem ser buscados os arquivos de biblioteca (extensão *.a*), neste caso indicamos o diretório *build*;
-  *-I./build* - Indica onde devem ser buscados os arquivos de cabeçalho (extensão *.h*), neste caso também indicamos o diretório *build* pois movemos o arquivo *myprint.h* para este diretório;
-  *-lmyprint* - Informa que este programa se utiliza da biblioteca *libmyprint.a*;
-  *-o build/main.run* - Informa o nome do arquivo executável de saída;

Executando o Programa Cliente
-----------------------------

Agora vem a parte mais simples do nosso artigo, executar o programa cliente. Para isso utilize o seguinte comando:

.. code-block:: bash

    $ ./build/main.run
    My Print: Teste!

Pronto! Parece muito trabalho para pouca coisa, mas uma vez que entendemos a grandiosidade dessa ideia vislumbramos que o desenvolvimento de excelentes bibliotecas para propósitos específicos não é restrita apenas aos grandes Gurus e Hackers do mundo GNU/Linux, todas as ferramentas estão disponíveis bastando apenas ter força de vontade e muita curiosidade!

Resumo dos Comandos
-------------------

Abaixo um pequeno script que resume todo o processo explicado nesse artigo:

.. code-block:: c

        echo "Cleaning build dir..."
        rm build/*

        echo
        echo "Compiling files"
        gcc -c lib/myprint.c -o build/myprint.o

        echo
        echo "Building lib archive"
        ar rcs build/libmyprint.a build/myprint.o

        echo
        echo "libmyprint built with these files"
        ar -t build/libmyprint.a

        echo
        echo "Simbols in libmyprint"
        nm -s build/libmyprint.a

        echo
        echo "Coping definition file to build dir"
        cp lib/myprint.h build/myprint.h

        echo
        echo "Cleaning .o files"
        rm build/*.o

        echo
        echo "Compiling client program"
        gcc -static src/main.c -L./build -I./build -lmyprint -o build/main.run

        echo
        echo "Running program"
        ./build/main.run


Finalização
-----------

Espero que tenham gostado deste artigo. Ainda tenho mais 3 encaminhados, explicando como criar uma biblioteca estática mais complexa (isto é, com mais arquivos e um arquivo de cabeçalho principal), como criar uma biblioteca compartilhada simples e por último como criar uma biblioteca compartilhada complexa. Claro que para fechar ainda tenho que explicar como criar "instaladores" para essas bibliotecas, mas este é uma assunto tão incerto (devido às inúmeras possibilidades) que ainda não estou prevendo-o nesta "lista de tarefas". E vocês, tem algo a mais que vocês gostariam que eu explicasse?

.. _assunto de bibliotecas estáticas e compartilhadas: /pt/introducao-bibliotecas-em-c
.. _Introdução à Bilbiotecas em C: /pt/introducao-bibliotecas-em-c
.. _*Include Guards*: http://en.wikipedia.org/wiki/Include_guard
.. _a documentação do compilador GCC: http://gcc.gnu.org/onlinedocs/cpp/Include-Syntax.html
