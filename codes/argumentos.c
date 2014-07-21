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
	
	char optc = 0;

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
