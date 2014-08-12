Makefile Para Java
##################
:date: 2014-07-29 00:56
:category: Java
:tags: java, makefile, command line, programação, gnu, vim, maps, make
:image: /images/logos/java.jpg
:description: Nesta continuação do assunto de "Java na Mão" resolvi mostrar uma forma de simplificar todo o processo de compilação e geração de pacotes no Java. Para isso vamos usar a ferramenta GNU Make.

No `artigo anterior`_, mostrei como realizar uma série de compilações e empacotamentos usando os utilitários do Java. Entretanto, utilizar a linha de comando constantemente para esse tipo de tarefa é um trabalho árduo.

.. image:: {filename}/images/java/java-gnu.jpg
        :target: {filename}/images/java/java-gnu.jpg
        :alt: Java & GNU
        :align: center

Agora que sabemos exatamente como podemos compilar um código Java e gerar seus respectivos pacotes manualmente, podemos escrever um GNU Makefile para automatizar essa tarefa.

.. more

Introdução ao Make
------------------

Apesar do que muitas pessoas vão te dizer por aí, o GNU Make não é uma ferramenta velha, antiquada, ultrapassada e etc. Na verdade ela é uma excelente ferramente que eu utilizo diariamente para encadear "receitas", controlar interdependências e gerar conteúdo de forma automatizada. Só pra você ter ideia, até na geração deste site eu utilizo o GNU Make.

Vamos rapidamente entender como é estruturado um Makefile. Veja a imagem abaixo:

.. image:: {filename}/images/java/makefile-ilustrado.png
        :target: {filename}/images/java/makefile-ilustrado.png
        :alt: Java Makefile Ilustrado
        :align: center

Primeira característica básica, todo Makefile é identado por tabs, isso faz parte de sua sintaxe. Segunda parte importante, o Makefile é composto por alvos (*targets*), dependências (*dependencies*) e receitas (*recipes*):

Um alvo (*target*)
        É uma arquivo que você deseja gerar ou um nome predeterminado que representa uma ação.
Uma dependência (*dependencie*)
        É uma lista de arquivos que são necessários para que o alvo seja executado. Também podem incluir uma lista de alvos existentes no Makefile que devem ser executados **com sucesso** antes da execução do alvo atual.
Uma receita (*recipe*)
        Contém uma lista de passos a ser executado para que um alvo seja gerado. Caso um passo incorra em erro, toda a receita é abortada por padrão.

Agora que entendemos esse passo, vamos compreender sua interface com o usuário. Ao criar uma arquivo Makefile, você pode invocar qualquer alvo utilizando o comando ``make``. Se você deseja, por exemplo, invocar a receita identificada pelo alvo ``clean``, basta invocar o comando ``make clean``.

Pronto, agora você tem uma ideia básica de como um Makefile e o utilitário ``make`` funcionam.


Criando seu Makefile
--------------------

Antes de criar o seu Makefile é necessário compreender que processo você quer automatizar. Nesse caso, é a compilação, execução e geração de pacotes Java.

Vamos primeiro analisar esses processos separadamente.

Compilação
        Ao compilar um programa java é utilizado o comando ``javac`` e é gerado um arquivo ``.class`` (alvo) e para isso é necessário uma arquivo ``.java`` (dependência).
Execução
        Para executar um programa, é necessário que este já tenha sido compilado (dependência). Em seguida invocamos o comando ``java`` apontando o arquivo de extensão ``.java`` (dependência).
Gerar Pacote
        Para gerar um pacote é necessário que este programa já tenha sido compilado (dependência). Em seguida invocamos o comando ``jar`` apontando os arquivos de extensão ``.java`` (dependência).

Então podemos delinear que nosso Makefile terá um esqueleto similar ao descrito abaixo:

.. code-block:: makefile

        %.class: %.java
                # Receita para compilar...

        %: %.class
                # Receita para executar...

        %.jar: %.class
                # Receita para gerar pacote...

Caso alguém esteja se perguntando o que são os sinais ``%``, eles são caracteres coringas que casam com qualquer nome passado. Ou seja, para compilar meu programa que está no arquivo ``HelloWorld.java`` eu vou chamar o ``make`` da seguinte forma: ``make HelloWorld.java``. Já para executá-lo eu vou invocar o ``make`` da seguinte forma: ``make HelloWorld``. Por que a diferença? Pois para executar eu precisava de algo que identificasse o programa mas que não fosse o nome do arquivo (ou entraria em conflito com a primeira receita). Por último, para gerar um ``.jar`` do programa ``HelloWorld`` eu invocarei o comando da seguinte forma: ``make HelloWorld.jar``.

Agora vamos à parte difícil, escrever as receitas. O GNU Makefile possui uma linguagem funcional própria documentada `aqui`_, mas que lembra um pouco o shell script. As variáveis são definidas normalmente (``JAVA=/usr/bin/java``) mas referenciadas utilizando o cifrão e o parêntese (``echo $(JAVA)``).

Para escrever uma receita simples que compila um programa ``.java`` basta escrever o seguinte:

.. code-block:: makefile

        JAVAC=/usr/bin/javac

        %.class: %.java
                $(JAVAC)  $*.java

Whoa! De onde saiu aquele ``$*.java``? Bem, o Make ele possui várias variáveis especiais que ele chama de `Automatic Variables`_. Elas são geradas a partir do nome do alvo, de suas dependências e etc. Esta (``$*``), por exemplo, armazena o nome do arquivo alvo sem a extensão definida, neste caso ``.class``. Ou seja, se eu executar um ``make MyApp.class`` esta variável possuirá a string ``MyApp``.

Já uma receita simples de execução do programa pode ser escrita da seguinte forma:

.. code-block:: makefile

        JAVA=/usr/bin/java

        %: %.class
                $(JAVA) $*

Ou seja, o comando a ser executado (dado que o nome do arquivo é ``HelloWorld.java``) será ``/usr/bin/java HelloWorld``. A esta altura você está se perguntando, "então para compilar meu programa ``HelloWorld.java`` vou precisar executar dois passos? ``make HelloWorld.class && make HelloWorld``?". A resposta é **não**. Como o alvo de execução possui como dependência o arquivo já compilado (``.class``) o ``make`` é inteligente o suficiente para saber que ele mesmo deve copilar o seu java. Ou seja, basta invocar o comando ``make HelloWorld`` que o ``make`` se encarregará de compilar e executar seu programa.


Complicando Um Pouco As Coisas
------------------------------

Entretanto, no mundo real nossos projetos não serão tão simples como neste exemplo e nem poderemos compilar desta forma, deixando os binários no mesmo diretório do código fonte e etc, conforme `explicado anteriormente`_. Vamos tomar como base o exemplo do `artigo anterior`_ e recriar os seguintes diretórios/artigos:

.. code::

        .
        ├── HelloWorld.java
        ├── Makefile
        ├── myjar
        │   └── MyJar.java
        └── world
            ├── HelloWorld.java
            └── Other.java

Com os seguintes códigos:

.. code-block:: java

        // Arquivo /tmp/project/HelloWorld.java

        public class HelloWorld
        {
            public static void main(String[] args)
            {
                System.out.println("Hello, World!");
            }
        }

.. code-block:: java

        // Arquivo /tmp/project/myjar/MyJar.java
        package myj;

        public class MyJar
        {
            public static void call()
            {
                System.out.println("Hello, World from my jar!");
            }
        }

.. code-block:: java

        // Arquivo /tmp/project/world/HelloWorld.java
        package world;
        import world.Other;
        import myj.MyJar;

        public class HelloWorld
        {
            public static void main(String[] args)
            {
                System.out.println("Hello, World!");
                Other.call();
                MyJar.call();
            }
        }

.. code-block:: java

        // Arquivo /tmp/project/world/Other.java
        package world;
        import java.util.Hashtable;

        public class Other
        {
            public static void call()
            {
                 System.out.println("Hello, World from other place!");
            }
        }


Notem a interdependência dos códigos ``world/HelloWorld.java``, ``world/Other.java`` e ``myjar/MyJar.java``. Notem também que os códigos agora possuem *packages* e estes devem ser invocados de forma diferente. Para isso vamos utilizar um Makefile mais elaborado:

.. code-block:: makefile

        # Ignore isso...
        space:=$(empty) $(empty)

        # Binários
        JAVAC=/usr/bin/javac
        JAVA=/usr/bin/java
        JAR=/usr/bin/jar

        # Diretórios...
        BINDIR=bin
        JARDIR=jars

        # Adicione qualquer classpath externo que você precise
        USERCLASSPATH=.

        # Criando classpath dinâmico
        TMPCLASSPATH=$(USERCLASSPATH):$(realpath $(BASE)$(BINDIR))
        ifneq (,$(wildcard $(jars)/*))
                CLASSPATH=$(TMPCLASSPATH):$(subst $(space),:,$(foreach jar,$(wildcard $(JARDIR)/*.jar),$(realpath $(jar))))
        endif

        # Flags de compilação
        JCFLAGS=-g -d $(BASE)$(BINDIR) -classpath $(CLASSPATH)
        # Flags de execução
        JFLAGS=-classpath $(CLASSPATH)

        %.class: %.java
                $(eval BASE=$(dir $<))
                rm -rf $(BASE)$(BINDIR) && mkdir $(BASE)$(BINDIR)
                $(JAVAC) $(JCFLAGS) $*.java

        %: %.class
                echo $*
                cd $(BASE)$(BINDIR) && $(JAVA) $(JFLAGS) $(subst /,.,$*)

        %.jar: %.class
                -mkdir -p $(JARDIR)
                $(JAR) cfe $(JARDIR)/$(subst /,-,$*.jar) $(subst /,.,$*) -C $(BASE)$(BINDIR)/ .

        clean:
                -find . -type d -name $(BINDIR) | xargs -I{} rm -rf {}
                -rm -rf $(JARDIR)

        PHONY: clean

Este Makefile já é um pouco mais complicado, mas ele já faz segmentação de binários e pacotes e controle de dependências e inclusão no ``classpath``.

Um Programa Simples
-------------------

Primeiro vamos a uma exemplo simples, compilar, executar e gerar um pacote do programa ``HelloWorld.java``:

.. code-block:: bash

        $ make HelloWorld
        rm -rf ./bin && mkdir ./bin
        /usr/bin/javac -g -d ./bin -classpath .:/tmp/java/bin: HelloWorld.java
        cd ./bin && /usr/bin/java -classpath .:/tmp/java/bin: HelloWorld
        Hello, World!

Notem que esta invocação já realiza a limpeza do arquivo de binários (``./bin``), compila o código e o invoca. Por fim temos a saída: ``Hello, World!``. Agora vamos gerar o pacote:

.. code-block:: bash

        $ make HelloWorld.jar
        rm -rf ./bin && mkdir ./bin
        /usr/bin/javac -g -d ./bin -classpath .:/tmp/java/bin: HelloWorld.java
        mkdir -p jars
        /usr/bin/jar cfe jars/HelloWorld.jar HelloWorld -C ./bin/ .

        $ ls -la jars/
        total 12
        drwxrwxr-x 2 magnun magnun 4096 Jul 29 00:25 .
        drwxrwxr-x 6 magnun magnun 4096 Jul 29 00:25 ..
        -rw-rw-r-- 1 magnun magnun  821 Jul 29 00:25 HelloWorld.jar

        $ java -jar jars/HelloWorld.jar
        Hello, World!

Note que esta regra não executa o ``.jar`` pois este não necessariamente é executável, pode ser apenas uma biblioteca conforme o próximo exemplo.


Uma Biblioteca
--------------

A biblioteca ``MyJar`` não deve ser executada, apenas compilada pois esta é dependência para o próximo programa, presente no *package* ``world``. Veja como é simples a execução e compilação:

.. code-block:: bash

        $ make myjar/MyJar.jar
        rm -rf myjar/bin && mkdir myjar/bin
        /usr/bin/javac -g -d myjar/bin -classpath .:: myjar/MyJar.java
        mkdir -p jars
        /usr/bin/jar cfe jars/myjar-MyJar.jar myjar.MyJar -C myjar/bin/ .

Pronto! Note que:

- Eu precisei informar o caminho completo (incluindo o diretório raiz do projeto);
- Que o make já separa os binários em ``myjar/bin``;
- Que o make gera nomes de pacotes baseado na estrutura de pastas, ``myjar-MyJar.jar``;


Um Programa com Dependências
----------------------------

Agora vamos ao desafio, o programa ``world/HelloWorld.java``, que possui dependências dentro de si (``world/Other.java``) e dependência de um ``.jar`` externo:

.. code-block:: bash

        $ make world/HelloWorld
        rm -rf world/bin && mkdir world/bin
        /usr/bin/javac -g -d world/bin -classpath .::/tmp/java/jars/myjar-MyJar.jar world/HelloWorld.java
        cd world/bin && /usr/bin/java -classpath .:/tmp/java/world/bin:/tmp/java/jars/myjar-MyJar.jar world.HelloWorld
        Hello, World!
        Hello, World from other place!
        Hello, World from my jar!

Note que o Makefile já populou o ``classpath`` corretamente para a invocação do programa ``java``.

Uma Falha
---------

Da forma como este Makefile foi idealizado (100% automático) ele não é capaz de deduzir que o programar ``world.HelloWorld`` tem como dependência a biblioteca ``myjar.MyJar`` e requer que nos invoquemos sua compilação manualmente. Veja o erro:

.. code-block:: bash

        $ make clean
        find . -type d -name bin | xargs -I{} rm -rf {}
        rm -rf jars

        $ make world/HelloWorld
        rm -rf world/bin && mkdir world/bin
        /usr/bin/javac -g -d world/bin -classpath .:: world/HelloWorld.java
        world/HelloWorld.java:4: error: package myj does not exist
        import myj.MyJar;
                  ^
        world/HelloWorld.java:12: error: cannot find symbol
                MyJar.call();
                ^
          symbol:   variable MyJar
          location: class HelloWorld
        2 errors
        make: ** [world/HelloWorld.class] Erro 1

O erro ocorre pois o programa ``MyJar`` não foi compilado ainda. Basta executar um ``make myjar/MyJar.jar`` e repetir o comando ``make world/HelloWorld`` que a execução concluirá com sucesso.

Bonus Track
-----------

Vocês se lembram que eu comecei o `artigo anterior`_ dizendo que aprendi a compilar em Java apenas para usar o VIM? Então... eu aprendi a usar o Makefile pois este se integra muito com com o VIM também.

Se você estiver programando no VIM e colocar esse Makefile na raiz do seu projeto você pode compilar e quiser executar seu programa sem sair do VIM, basta você invocar o ``make`` através do modo de comandos do VIM da seguinte forma: ``:make world/HelloWorld``. Qual a vantagem em relação a invocar o ``make`` pelo terminal? A integração entre ambas as ferramentas! O VIM interpreta a saída do ``make`` realizar o *parsing* encontra os erros de compilação e move o seu cursor para as linhas que contêm erros. Veja:

.. image:: {filename}/images/java/integracao-vim-make.png
        :target: {filename}/images/java/integracao-vim-make.png
        :alt: Intrgração VIM & Makefile
        :align: center

Muito interessante não? Mas é claro que você não precisa ficar digitando esse comando constantemente. Para isso você pode criar os seguintes atalhos:

.. code-block:: vim

        nnoremap <F1> :make %:r.class<CR>
        nnoremap <F2> :make %:r<CR>
        nnoremap <F3> :make %:r.jar<CR>

Estes mapeamentos configuram as teclas ``F1`` para compilar o programa, a tecla ``F2``  para compilar e executar o programa e a tecla ``F3`` para compilar e empacotar.

Caso você seja como eu, e não goste de mover a mão até a fileira de teclas ``F1`` a ``F12``, faça a seguinte configuração de atalhos:

.. code-block:: vim

        nnoremap <leader>jc :make %.class<CR>
        nnoremap <leader>jr :make %:r<CR>
        nnoremap <leader>jj :make %:r.jar<CR>

Sendo estes minemônicos para *java compile*, *java run* e *java jar*.

Por enquanto é só pessoal!

.. _artigo anterior: /pt/programado-em-java-sem-ide
.. _aqui: http://www.gnu.org/software/make/manual/make.html
.. _Automatic Variables: http://www.gnu.org/software/make/manual/make.html#Automatic-Variables
.. _explicado anteriormente: /pt/programado-em-java-sem-ide
