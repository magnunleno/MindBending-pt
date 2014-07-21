Corrigindo Arquivos CSV com Python
##################################
:date: 2014-05-16 14:32
:category: Python
:tags: python, csv, processamento, arquivo
:image: /images/python.png
:description: Muitas vezes o trabalho braçal parece mais cômodo que uma automatização, já que este último muitas vezes envolve relembrar conceitos já apagados da sua mente. Mas é sempre importante lembrar que, uma rotina automatizada corretamente, é uma rotina que nunca mais será executa manualmente.

Ontem eu estava conversando com alguns colegas e um deles acabou soltando que estava tendo que fazer um trabalho braçal: Corrigir um arquivo CSV manualmente, pois a rotina que processava sua entrada só compreendia campos do CSV se eles estivessem envolvidos entre aspas duplas.

.. image:: {filename}/images/logos/csv.png
        :target: {filename}/images/logos/csv.png
        :alt: CSV
        :align: center


Na hora eu falei pra ele, "Use Python!", e em seguida todos me disseram que era trabalho de mais escrever um programa só pra isso. Será mesmo?

.. more

Bem, aceitei o desafio... Agora são exatas 14hs. Este é meu arquivo de entrada (``entrada.csv``):

.. code-block:: csv

        Data 1;Data 2;Data 3;Data 4;Data 5
        Data 1;Data 2;Data 3;Data 4;Data 5
        Data 1;Data 2;Data 3;Data 4;Data 5
        Data 1;Data 2;Data 3;Data 4;Data 5
        Data 1;Data 2;Data 3;Data 4;Data 5

Muito bem! Meu programa precisa ler este arquivo (``input_fd = open()``) em seguida iterar sobre todas as linhas (``for line in input_fd.readlines()``), separar os campos divididos por ponto e vírgula (``line.split(';')``), envolver cada resultado entre aspas (``'"%s"'%field.strip()``) e por fim juntá-los todos novamente com ponto e virgula (``';'.join(lista)``).

Pronto, agora vamos ver o código:

.. code-block:: python

        #!/usr/bin/env python
        # encoding: utf-8

        input_fd = open('entrada.csv', 'r')
        output_fd = open('saida.csv', 'w')
        for line in input_fd.readlines():
            line = ';'.join(['"%s"'%field.strip() for field in line.split(';')])+'\n'
            output_fd.write(line)
        input_fd.close()
        output_fd.close()

Após executar o script temos a seguinte saída (``saida.csv``):

.. code-block:: csv

        "Data 1";"Data 2";"Data 3";"Data 4";"Data 5"
        "Data 1";"Data 2";"Data 3";"Data 4";"Data 5"
        "Data 1";"Data 2";"Data 3";"Data 4";"Data 5"
        "Data 1";"Data 2";"Data 3";"Data 4";"Data 5"
        "Data 1";"Data 2";"Data 3";"Data 4";"Data 5"

Agora são exatamente 14hs e 10min. Considerando que gastei um tempo escrevendo esse texto, o tempo de codificação ficou em torno de 3 minutos. Acho que é um trabalho que vale a pena, o que acham?

**Update:** Levando em consideração o comentário do Jorge (e se algum campo já estiver envolto em aspas duplas), a possibilidade do CSV não ser separado por ponto e vírgulas e a necessidade de ter que editar o código para que este funcione para arquivos com outros nomes resolvi criar uma versão mais incrementada, incluindo interpretação de argumentos de linha de comando.

O código está disponível `aqui`_ e pode ser utilizado da seguinte forma:

.. code-block:: bash

        # Obtendo o Arquivo e tornando executável
        $ wget http://mindbending.org/pt/codes/processa_xml
        $ chmod +x processa_xml

        # Mensagem de utilização
        $ ./processa_xml
        usage: processa_xml [-h] [--version] -i INPUT -o OUTPUT [-s SEP]
        processa_xml: error: argument -i is required

        # Mensagem de ajuda
        $ ./processa_xml -h
        usage: processa_xml [-h] [--version] -i INPUT -o OUTPUT [-s SEP]

        optional arguments:
          -h, --help     show this help message and exit
          --version, -v  Mostra a versão
          -i INPUT       Arquivo de entrada
          -o OUTPUT      Arquivo de saída
          -s SEP         Separador do CSV (Padrão: ;)

        # Validação de arquivo de entrada
        $ ./processa_xml -i erro.csv -o saida.csv
        Arquivo de entrada não encontrado: erro.csv

        # Exemplo de arquivo de entrada
        $ cat entrada.csv 
        Data 1;Data 2;Data 3;Data 4;Data 5
        Data 1;Data 2;Data 3;Data 4;Data 5
        Data 1;Data 2;Data 3;"Data 4";Data 5
        Data 1;Data 2;Data 3;Data 4;Data 5
        Data 1;Data 2;Data 3;Data 4;Data 5

        # Processando arquivo de entrada
        $ ./processa_xml -i entrada.csv -o saida.csv
        $ cat saida.csv 
        "Data 1";"Data 2";"Data 3";"Data 4";"Data 5"
        "Data 1";"Data 2";"Data 3";"Data 4";"Data 5"
        "Data 1";"Data 2";"Data 3";"Data 4";"Data 5"
        "Data 1";"Data 2";"Data 3";"Data 4";"Data 5"
        "Data 1";"Data 2";"Data 3";"Data 4";"Data 5"

        # Trocando ponto e virgula por virgulas
        $ sed 's/;/,/g' entrada.csv -i
        $ cat entrada.csv 
        Data 1,Data 2,Data 3,Data 4,Data 5
        Data 1,Data 2,Data 3,Data 4,Data 5
        Data 1,Data 2,Data 3,"Data 4",Data 5
        Data 1,Data 2,Data 3,Data 4,Data 5
        Data 1,Data 2,Data 3,Data 4,Data 5

        # Processando com virgulas
        $ ./processa_xml -i entrada.csv -o saida.csv -s ,
        $ cat saida.csv 
        "Data 1","Data 2","Data 3","Data 4","Data 5"
        "Data 1","Data 2","Data 3","Data 4","Data 5"
        "Data 1","Data 2","Data 3","Data 4","Data 5"
        "Data 1","Data 2","Data 3","Data 4","Data 5"
        "Data 1","Data 2","Data 3","Data 4","Data 5"


Esse sim me consumiu um certo tempo. Algo em torno de 20 minutos. Mas está bem melhor agora, não?

.. _aqui: /pt/codes/processa_xml
