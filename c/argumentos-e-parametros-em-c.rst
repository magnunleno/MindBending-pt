Argumentos e Parâmetros em C
############################
:date: 2014-07-11 12:22
:category: C
:tags: c, argumentos, parâmetros, , programação, desenvolvimento, linha de comando, posix
:image: /images/logos/c-programming.jpg
:author: Fernando Almeida
:description: Seguindo a mesma ideia de implementar padrões POSIX e aumentar a integração de programas em C, hoje vamos ver um assunto bem mais denso e complexo, argumentos e parâmetros.

Os parâmetros e argumentos são aquelas opções que usamos quando executamos um programa na linha de comando, como ``df -h``  ou ``ls -la --color``. Tratar esses parâmetros e argumentos faz com que nossos programas estejam em *compliance* com o sistema operacional.

.. image:: {filename}/images/logos/c-programming.jpg
        :target: {filename}/images/logos/c-programming.jpg
        :alt: C Language
        :align: center



A implementação dos parâmetros e argumentos da linha de comando é um assunto complexo e requer dedicação. Abaixo explico de maneira prática como implementá-los através de funções GNU. No entanto, vou explicar também um pouco desse padrão da linha de comando, dos parâmetros e dos argumentos, pois é imprescindível saber como eles funcionam para uma correta implementação.

.. more

No geral quando estamos desenvolvendo um programa, usaremos pouquíssimos argumentos, mas em alguns casos precisaremos usar todas as opções na íntegra (Principalmente se vamos desenvolver ferramentas para linha de comando GNU/Linux).


Parâmetros e Argumentos?
------------------------

Primeiramente, vamos esclarecer a diferença entre o termo parâmetro e o termo argumento. Um parâmetro é uma 'propriedade' passada pela linha de comando. Um exemplo de um parâmetro seria a opção ``-h`` passada para o comando ``df``. Este parâmetro define ao programa ``df`` que a saída das informações deve ser de fácil leitura (Em KB, MB, GB - *Human-Readable*).

.. image:: {filename}/images/c/4-Comando-df-h.jpg
        :target: {filename}/images/c/4-Comando-df-h.jpg
        :alt: Exemplo df -h
        :align: center

Os argumentos são as opções para cada parâmetro. Um exemplo de um parâmetro com argumento obrigatório seria a opção ``-t`` passada para o comando ``df``. Este parâmetro limita o programa ``df`` a exibir apenas os tipos de partições definidas no argumento. Portanto, o parâmetro ``-t`` requer o argumento 'tipo de arquivo':

.. image:: {filename}/images/c/5-Comando-df-t-ext4.jpg
        :target: {filename}/images/c/5-Comando-df-t-ext4.jpg
        :alt: Comando df -t ext4
        :align: center

Funcionamento dos Parâmetros e Argumentos da linha de comando
-------------------------------------------------------------
Em sistemas operacionais padrão POSIX e GNU é possível combinar dois parâmetros na linha de comando através de uma única entrada.
Em outras palavras, caso necessite utilizar o parâmetro ``-l`` e o parâmetro ``-h``, é possível combiná-los em um único parâmetro ``-lh`` ou ``-hl``

Perceba que a ordem não é importante. No entanto, caso o parâmetro desejado necessite de argumentos, este parâmetros deve ser deixado por último afim de permitir a inclusão de seu argumento, conforme a seguir:

.. image:: {filename}/images/c/6-Parametro-e-Argumento.jpg
        :target: {filename}/images/c/6-Parametro-e-Argumento.jpg
        :alt: Parâmetro e Argumento
        :align: center
	
Os parâmetros ``-l`` e ``-h`` são do tipo ``no_arguments``, sem argumentos - Enquanto o parâmetro ``-t`` é do tipo ``required_arguments``, portanto obrigatórios.
As constantes de parâmetros são definidas abaixo:

.. table::
        :class: table

        ======================= ============
        Nome			Argumentos
        ======================= ============
        ``no_arguments``	Não
        ``optional_arguments``	Opcionais
        ``required_arguments``	Obrigatórios
        ======================= ============

Parâmetros Simples, Longos e Restantes
--------------------------------------
Parâmetros simples são aqueles parâmetros curtos (apenas 1 caractere), precedidos pelo sinal de ``-``. Já os parâmetros longos são palavras, precedidas pelos sinais ``--``. É uma boa prática que todos os parâmetros longos possuam parâmetro simples equivalentes, no entanto não é possível combinar os parâmetros longos como fazemos com os curtos. Eles devem ser passados de forma literal.

Usando ainda o comando ``df``, um exemplo de parâmetro curto que possui um parâmetro longo equivalente é o ``-h``. Seu parâmetro equivalente é o ``--human-readable``

O padrão POSIX utiliza apenas parâmetros simples. Já o padrão GNU usado no GNU/Linux utiliza tanto os parâmetros simples quanto os parâmetros longos.

Ainda temos outro tipo de parâmetro, que chamo de parâmetros restantes. Esses parâmetros são aqueles **não precedidos** pelos caracteres ``-`` ou ``--``.

O argc e argv
-------------
Existem duas variáveis que fazem a ponte entre os parâmetros e argumentos passados na linha de comando para nosso programa. 

A primeira delas é a variável ``argc``, que entra na nossa velha ``main()`` e é do tipo ``INT``. Ela nos informa o número de parâmetros passados mais 1. Vamos ver isso na prática? Considere o seguinte programa simples:

.. code-block:: c

	#include <stdio.h>

	void main(int argc, char** argv) {
		printf("Valor de argc: %d\n", argc);
                exit(0);
	}

Agora vamos executar:

.. image:: {filename}/images/c/1-Programa-simples.jpg
        :target: {filename}/images/c/1-Programa-simples.jpg
        :alt: Programa Simples
        :align: center

Veja que quando executamos nosso programa sem nenhum parâmetro na linha de comando, ``argc`` retorna 1. Quando executamos com os parâmetros adicionais ``argc`` retorna 1 + numero de parâmetros. Isso porque o "nome do programa" - ``./simples`` - também é considerado.

Quando usamos os parâmetros ``param1``, ``param2`` e ``param3`` nosso ``argc`` retornou 4 (o "nome do programa" + 3 argumentos).

Então, caso a variável ``argc`` seja igual a 1 sabemos que nenhum parâmetro foi passado na linha de comando. A partir daí é possível parar nosso programa, caso necessitemos desses parâmetros para que o mesmo seja executado corretamente:

.. code-block:: c

	if(argc == 1) { // Sem parametros
		printf("Parametros faltando\n");
		exit(0);
	}
	
A segunda variável que nos auxilia no tratamento de argumentos e parâmetros é a variável ``argv``, que também entra na ``main()`` do nosso programa. Esta variável é um ponteiro para um *Array* de *strings* e que contém os parâmetros da linha de comando. Como sabemos, em C não é possível deduzir o fim de um *array*, caso este não possua um terminador pré-definido. Por isso temos que combinar o valor de ``argc`` para ler todos os parâmetros corretamente.

Vamos alterar nosso programa ``simples.c`` para que ele exiba todos nossos parâmetros da linha de comando:

.. code-block:: c

	#include <stdio.h>

	void main(int argc, char** argv) {
		int i;

		printf("Valor de argc: %d\n", argc);
	
		for(i = 0; i < argc; i++) {
			printf("Valor de argv[argc %d]: %s\n", i, argv[i]);
		}
                exit(0);
	}

Compilamos e rodamos. Vamos ao resultado:

.. image:: {filename}/images/c/2-Programa-simples-mostrando-argc-e-argv.jpg
        :target: {filename}/images/c/2-Programa-simples-mostrando-argc-e-argv.jpg
        :alt: Programa simples mostrando argc e argv
        :align: center

Opa! Então quer dizer que que ``argv[0]`` é o nome do nosso programa? Não exatamente, ``argv[0]`` exibe exatamente a linha de comando que foi usado para executar nosso programa. Caso usemos o caminho completo do executável, veremos um valor de ``argv[0]`` respectivo:

.. image:: {filename}/images/c/3-Caminho-completo.jpg
        :target: {filename}/images/c/3-Caminho-completo.jpg
        :alt: Caminho completo
        :align: center

Aqui vai uma dica ótima: O nome do nosso programa (ou processo) puro, sem o caminho ou o diretório pode ser conseguido através uma variável externa especial chamada ``__progname``. Antes de usá-la é necessário declará-la:

.. code-block:: c

        extern __progname;
        printf("Nome do Programa: %s\n", __progname);

A diretiva ``extern`` amplia a visibilidade das variáveis e funções no C. No caso da variável ``__progname`` esta informação vem da biblioteca ``LibC``.

Interpretando Parâmetros e Argumentos
-------------------------------------
Vimos que a passagem dos parâmetros e argumentos pode ser muito flexível, aceitando uma infinidade de combinações. Para atender o *compliance* POSIX e GNU, precisamos interpretar todas essas variações, opções e argumentos da linha de comando.

Para essa finalidade, podemos contar com ``getopt()`` e ``getopt_long()``. Ainda bem! Imagine fazer o *parse* de cada combinação dessas manualmente! Seria trabalhoso, não?

Aqui entra novamente a praticidade de estar de acordo com as normas GNU: Essas funções estão disponíveis nas bibliotecas padrão do ``gcc``. Para isso precisamos incluí-las no nosso programa:

.. code-block:: c

        #include <unistd.h> // *POSIX* Para o getopt() original
        #include <getopt.h> // *GNU* Para o getopt_long()

O padrão POSIX faz leitura apenas de parâmetros simples (curtos, precedidos apenas por ``-`` ), por isso usaremos o ``getopt_long()``, que dá suporte tanto aos parâmetros simples e aos parâmetros longos.

Abaixo uma tabela que descreve os argumentos que nosso pequenos programa de exemplo irá implementar;

.. table::
        :class: table

        ======================= =========== ===========
        Função                  Forma longa Forma Curta
        ======================= =========== ===========
        Controla a verbosidade  --verbose   -v
        Formatação tabular      --tabular   -t
        Define Usuário          --usuario   -u
        Mensagem de ajuda       --ajuda     N/A
        Versão do programa      --versao    N/A
        Preenchimento com zeros N/A         -v
        ======================= =========== ===========

Primeiro vamos definir quais são os parâmetros longos que nosso programa aceitará:

.. code-block:: c

	struct option OpcoesLongas[] = {
		{"verbose", no_argument, NULL, 'v'},
		{"tabular", no_argument, NULL, 't'},
		{"usuario", required_argument, NULL, 'u'},
		{"ajuda", no_argument, NULL, 1}
		{"versao", no_argument, NULL, 2}
		{0, 0, 0, 0}
	};

O formato para cada opção longa é:

.. image:: {filename}/images/c/7-Formato-OpcoesLongas.jpg
        :target: {filename}/images/c/7-Formato-OpcoesLongas.jpg
        :alt: Formato Opções Longas
        :align: center

O terceiro argumento é uma *flag* que indica se o valor do quarto argumento (as letras ``v``, ``t`` e ``u`` ou os números ``1`` e ``2``) deve ser retornado ou se deve preencher uma variável específica.

Note que não foram definidos os argumentos que possuem **apenas** a forma curta. Os parâmetros simples (ou curtos) são definidos diretamente na chamada à função `'getopt_long()'`. Eles são definidos pelo caractere que representará cada parâmetro e finalizados com o símbolo ``:``, conforme a seguir:

.. image:: {filename}/images/c/8-Formato-getopt_long.jpg
        :target: {filename}/images/c/8-Formato-getopt_long.jpg
        :alt: Ofrmato getopt long
        :align: center

Os parâmetros longos já explicamos acima. Vamos dar um zoom nos parâmetros simples: Veja que as opções ``ztuv`` são finalizadas com o ``:`` e logo depois temos a opção ``a`` e o finalizador ``:``.
Isto agrupa quais os parâmetros poderão ser usados em conjunto (``z``, ``t``, ``u``, ``v``) e qual o parâmetro que deve ser usado separado (``a``).

Agora vamos implementar a leitura de todos os parâmetros (simples e longos) e seus argumentos e os parâmetros restantes com os seguintes códigos:

**Passo 1:** Ler os parâmetros (simples e longos) e seus argumentos

.. code-block:: c

	char optc = 0; // Parece estranho... Mas todo CHAR é na verdade um INT
	
	while((optc = getopt_long(argc, argv, "ztvu:a:", OpcoesLongas, NULL)) != -1) {
		switch(optc) {
			// código...
			// código...
			case 'u' :
				printf("Arquivo: %s\n", optarg);
				break;
			// código...
			// código...
		}
	}
	
Para cada parâmetro temos um argumento referente. Esse argumento pode ser lido pelo ponteiro ``optarg``. Este ponteiro irá ser automaticamente atualizado para cada argumento a cada rodada do *loop* ``while``.

**Passo 2:** Ler os parâmetros restantes com um *loop* ``while`` e incrementar a variável especial ``optind`` usada como indexador de ``argv``

.. code-block:: c

	printf("Parâmetros Restantes:\n");
	do {
		printf("%s\n", argv[optind]);
	}
	while(++optind < argc);

Mão Na Massa
------------
Agora que expliquei cada parte do código, vamos fazer um teste com nosso programa na íntegra. Vamos chamar nosso programa de ``argumentos``, conforme o código abaixo:

.. code-block:: c

	#include <stdio.h>
	#include <unistd.h> // *POSIX* Para o getopt() original
	#include <getopt.h> // *GNU* Para o getopt_long()
	#include <string.h>
	#include <stdlib.h>

	#define MAJOR_VERSION	1
	#define MINOR_VERSION	0

	int main(int argc, char** argv) {
		// Variaveis para os parametros e argumentos
		short tabular = 0; // Opcao 't'
		short verbose = 0; // Opcao 'v'
		short zero    = 0; // Opcao 'z'
	
		char optc = 0;	// Parece estranho... Mas todo CHAR é na verdade um INT

		struct option OpcoesLongas[] = {
			{"verbose", no_argument, NULL, 'v'},
			{"tabular", no_argument, NULL, 't'},
			{"usuario", required_argument, NULL, 'u'},
			{"arquivo", required_argument, NULL, 'a'},
			{"ajuda", no_argument, NULL, 1},
			{"versao", no_argument, NULL, 2},
			{0, 0, 0, 0}
		};

		if(argc == 1) { // Sem argumentos
			printf("Parametros faltando\n");
			exit(0);
		}

		while((optc = getopt_long(argc, argv, "ztvu:a:", OpcoesLongas, NULL)) != -1) {
			switch(optc) {
				case 1 : // Ajuda
					printf("Mensagem de ajuda do programa\n");
					exit(0);
				case 2 : // Versao
					printf("Versão %d.%d\n", MAJOR_VERSION, MINOR_VERSION);
					exit(0);
				case 'u' : // Usuario
					printf("Usuario: %s\n", optarg);
					break;
				case 'a' : // Arquivo
					printf("Arquivo: %s\n", optarg);
					break;
				case 't' : // Tabular
					tabular = 1;
					break;
				case 'v' : // Verbose
					verbose = 1;
					break;
				case 'z' : // Zero
					zero = 1;
					break;
				default : // Qualquer parametro nao tratado
					printf("Parametros incorretos.\n");
					exit(0);
			}
		}
		
		printf("Argumentos e Parametros do programa:\n");
		
		printf("Verbose: %c - Tabular: %c - Zero: %c\n\n", ((verbose) ? ('S') : ('N')), ((tabular) ? ('S') : ('N')), ((zero) ? ('S') : ('N')));	

		if(optind < argc) { // Se optind for menor que argc entao nao temos parametros restantes
			printf("Parametros Restantes:\n");
			do {
				printf("\t%s\n", argv[optind]);
			}
			while(++optind < argc);
	
			printf("\n");
		}
	}

Todo o código acima está disponível para download `aqui`_.

Vamos compilar e rodar o programa. Use todas as combinações diferentes de parâmetros e argumentos e veja como o programa se comporta. Em especial eu gostaria de demonstrar o que acontece se usamos um parâmetro inválido, não tratado pelo programa.

Veja o que acontece se usarmos o parâmetro ``-f``, por exemplo:

.. image:: {filename}/images/c/9-Parametro-Invalido.jpg
        :target: {filename}/images/c/9-Parametro-Invalido.jpg
        :alt: Parâmetro Inválido
        :align: center

Perceberam alguma coisa estranha aqui? Bem, esta mensagem ``invalid option -- 'f'`` está aonde no nosso código? Na verdade esta mensagem de erro não veio do nosso código, mas sim da biblioteca ``LibC`` - a mesma onde se encontra o ``getopt()`` e o ``getopt_long()``.

Esta mensagem foi mostrada em inglês porque o meu GNU/Linux está em inglês. Caso tivéssemos um sistema em português, esta mensagem seria mostrada neste idioma. Tratarei o assunto "Regionalização" no meu próximo artigo.

É isso! Tentei ser o mais prático na demostração dos parâmetros e argumentos e como implementá-los em C. A partir daqui é possível criar programas para GNU/Linux que tratam os parâmetros e argumentos corretamente.

Saiba Mais
----------

Para mais informações sobre os parâmetros e argumentos recomendo os seguintes links:

- `Arguments, Options, and the Environment`_
- `Anatomy of command line arguments in Linux`_
	
Obrigado!

.. _Arguments, Options, and the Environment: http://www.informit.com/articles/article.aspx?p=175771&seqNum=3
.. _Anatomy of command line arguments in Linux: http://mylinuxbook.com/command-line-arguments-in-linux-part2/
.. _aqui: /pt/codes/argumentos.c
