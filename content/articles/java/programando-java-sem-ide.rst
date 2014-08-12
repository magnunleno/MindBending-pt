Programando Java sem IDE
########################
:date: 2014-06-05 14:23
:category: Java
:tags: java, ide, vim, linha de comando, jar, javac, manifest, meta-inf
:image: /images/logos/java.jpg
:description: Eu defendo veementemente a ideia de que devemos conhecer bem aquilo com que trabalhamos. E esta é uma máxima que eu não vejo sendo colocada em prática no mundo Java. Se você tirar a IDE de um programador Java, ele não sabe compilar nem um Hello World.

Há algum tempo eu concluí minha Pós-Graduação (ainda estou devendo um texto sobre isso aqui) e, devido a "regras institucionais", fui "instigado" (\*cof\*obrigado\*cof\*) a usar Java. Sendo eu um usuário de VIM, uma das coisas que mais me irrita ao programar em Java é essa amarração de IDE. Então resolvi fazer algo que poucos programadores Java sabem, programar sem IDE.

.. figure:: {filename}/images/java-na-mao.jpg
        :target: {filename}/images/java-na-mao.jpg
        :alt: Java na mão!
        :align: center

        Escrevendo Java na mão!!


Sim, eu sou cabeça dura a esse ponto. Meu fluxo de trabalho no VIM já é muito bem estabelecido, e me adaptar a uma nova ferramenta com inúmeras limitações (quando comparado à edição no VIM) não é nada agradável.

.. more

E por mais que me digam que o Eclipse tem um "modo VIM", ele não tem 5% das funcionalidades que eu preciso (e uso) constantemente. Logo fui à pesquisa, e pasmem, para quem está acostumado a programar em C sem IDE não foi nada difícil...

Compilando um Programa Simples
------------------------------

Vamos ao nosso primeiro exemplo, um simples *hello world*. Eis o código fonte:

.. code-block:: java

        // Arquivo /tmp/project/HelloWorld.java

        public class HelloWorld
        {
            public static void main(String[] args)
            {
                System.out.println("Hello, World!");
            }
        } 

Muito bem, vamos compilar esse arquivo. E para isso usamos o comando ``javac``:

.. code::

        magnun@/tmp/project$ javac HelloWorld.java 

Após esse comando será criado um arquivo compilado em ``/tmp/project/HelloWorld.class``. Em seguida podemos executá-lo. Para isso iremos invocar o comando ``java`` passando como argumento o nome da classe que possui o método ``main``. Vamos lá:

.. code::

        magnun@/tmp/project$ java HelloWorld
        Hello, World!

Pronto. Esse foi simples!

Compilando um Programa Simples
------------------------------

No nosso segundo exemplo temos um *hello world* dentro de um pacote. Eis o código fonte:

.. code-block:: java

        // Arquivo /tmp/project/world/HelloWorld.java
        package world;

        public class HelloWorld
        {
            public static void main(String[] args)
            {
                System.out.println("Hello, World!");
            }
        } 

Três pontos muito importantes:
* Esse programa já está dentro de um pacotes chamado ``world``;
* Ele deve estar em uma estrutura de pastas similar ao denotado no comentário;
* Todos os comandos abaixo devem ser emitidos a partir do diretório ``/tmp/project``

Muito bem, vamos compilar esse arquivo. E para isso usamos o comando ``javac``:

.. code::

        magnun@/tmp/project$ javac world/HelloWorld.java 

Após esse comando será criado um arquivo compilado em ``/tmp/project/world/HelloWorld.class``. Em seguida podemos executar:

.. code::

        magnun@/tmp/project$ java world.HelloWorld
        Hello, World!

Note a diferença do nome da classe na invocação, ela possui o nome do pacote.


Compilando um Programa Com Mais de Uma Classe
---------------------------------------------

Neste terceiro exemplo serei mais breve, pois ele serve apenas para demonstrar que compilar um programa com mais de uma classe não é muito diferente. Eis os códigos:

.. code-block:: java

        // Arquivo /tmp/project/world/HelloWorld.java
        package world;
        import world.Other;

        public class HelloWorld
        {
            public static void main(String[] args)
            {
                System.out.println("Hello, World!");
                Other.call();
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


Compilando o programa com o ``javac``:

.. code::

        magnun@/tmp/project$ javac world/HelloWorld.java 

Executando normalmente, como se fosse apenas um arquivo:

.. code::

        magnun@/tmp/project$ java world.HelloWorld
        Hello, World!
        Hello, World from other place!


Segmentando Código de Binários
------------------------------

Apesar de simples, esta forma não é a mais "recomendada", pois a compilação mistura os códigos fontes com os binários. A maneira mais indicada é segmentar os arquivos binários em um diretório ``bin``. Exemplo de compilação e execução do último código:

.. code::

        magnun@/tmp/project$ mkdir world/bin
        magnun@/tmp/project$ javac -d world/bin world/HelloWorld.java 

Executando normalmente, como se fosse apenas um arquivo:

.. code::

        magnun@/tmp/project$ cd world/bin
        magnun@/tmp/project/world/bin$ java world.HelloWorld
        Hello, World!
        Hello, World from other place!

Note que para executar é necessário mudar o diretório de operação para ``bin``.

Criando um Pacote JAR Executável
--------------------------------

O processo de criação de um ``.jar`` executável exige um pouco mais de trabalho. Primeiro vamos criar um diretório chamado ``jars`` e em seguida empacotar os binários informando o nome da classe a ser executada por padrão (``entry-point``):

.. code::

        magnun@/tmp/project$ mkdir jars
        magnun@/tmp/project$ jar cfe jars/helloworld.jar world.HelloWorld -C world/bin/ .

Note que esse comando criar um arquivo ``.jar`` no diretório ``jars``.  Você pode inspecionar o conteúdo desse arquivo com o seguinte comando:

.. code::

        magnun@/tmp/project$ jar -ft jars/hw.jar 
        META-INF/
        META-INF/MANIFEST.MF
        world/
        world/HelloWorld.class
        world/Other.class


Para executá-lo utilizamos o seguinte comando:

.. code::

        magnun@/tmp/project$ java -jar jars/helloworld.jar 
        Hello, World!
        Hello, World from other place!

Usando Uma Biblioteca JAR
-------------------------

Ok, agora é a parte mais feia do Java, usar uma biblioteca empacotada. Primeiro vamos criar a biblioteca:

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

Nada muito complexo. Agora temos que compilar esta biblioteca e criar um pacote JAR:

.. code::

        magnun@/tmp/project$ mkdir myjar/bin
        magnun@/tmp/project$ javac -d myjar/bin myjar/MyJar.java 
        magnun@/tmp/project$ jar cfe jars/myjar.jar myj.MyJar -C myjar/bin/ .

Vejam que no arquivo ``.jar`` não tem nada além do compilado do arquivo ``MyJar.java``:

.. code::

        magnun@/tmp/project$ jar -ft jars/myjar.jar 
        META-INF/
        META-INF/MANIFEST.MF
        myj/
        myj/MyJar.class

Muito bem, agora vamos modificar nosso programa inicial (``HelloWorld.java``) para que este invoque o conteúdo do JAR:

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

Em seguida vamos re-compilar o pacote ``world``:

.. code::

        magnun@/tmp/project$ rm -rf world/bin/*
        magnun@/tmp/project$ javac -classpath .:jars/myjar.jar -d world/bin world/HelloWorld.java 

Note o detalhe da compilação, é necessário informar o *classpath*, ou seja, onde o java irá buscar as classes. Os elementos do *classpath* são separados por ``:``, desta forma informamos os seguintes caminhos: 

. (diretório corrente)
        Ou ele não encontraria o código das classes do pacote ``world``;
jars/myjar.jar
        O jar que iremos utilizar. Note que é necessário informar **todos** os ``.jars``. Para usar *wildcards* é necessário informar o *classpath* entre aspas: ``-classpath ".:jar/*"``

Em seguida iremos executar o programa que acabamos de compilar:

.. code::

        magnun@/tmp/project$ cd world/bin/
        magnun@/tmp/project$ java world.
        world.HelloWorld  world.Other       
        magnun@/tmp/project$ java -classpath .:../../jars/myjar.jar world.HelloWorld 
        Hello, World!
        Hello, World from other place!
        Hello, World from my jar!

É importante ressaltar que precisamos especificar o *classpath* novamente. Sim, é um saco...

Empacotando um Programa que utiliza um JAR
------------------------------------------

Muito bem, essa é pra fechar. Às vezes você pode precisar criar um ``.jar`` executável, mas este ``.jar`` se utiliza de outros ``.jars``. E agora?

Para isso vamos construir manualmente o arquivo ``MANIFES.MF``. Crie o seguinte arquivo em ``world/META-INF/MANIFEST.MF``:

.. code::

        Manifest-Version: 1.0
        Created-By: 1.7.0_51 (Oracle Corporation)
        Main-Class: world.HelloWorld
        Class-Path: myjar.jar
        
        
Note que após o ``Class-Path`` existem 2 linhas em branco. Em seguida vamos criamos o pacote com o seguinte comando:

.. code::

        magnun@/tmp/project$ jar cfm jars/helloworld.jar world/META-INF/MANIFEST.MF -C world/bin/ . -C jars myjar.jar

O conteúdo de deste pacote deve estar conforme abaixo:

.. code::

        magnun@/tmp/project$ jar -tf jarx/helloworld.jar
        META-INF/
        META-INF/MANIFEST.MF
        world/
        world/HelloWorld.class
        world/Other.class
        myjar.jar

Em seguida podemos executar sem nenhuma preocupação de *classpath*:

.. code::

        magnun@/tmp/project$ java -jar jars/helloworld.jar 
        Hello, World!
        Hello, World from other place!
        Hello, World from my jar!

Pronto! É isso aí. Espero que ajuda alguém, pois eu espero nunca mais ter que usar esse tipo de ferramenta. :(
