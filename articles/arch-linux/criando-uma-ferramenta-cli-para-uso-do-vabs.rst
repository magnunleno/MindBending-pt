Criando Uma Ferramenta CLI Para Uso do vABS
###########################################
:date: 2011-08-12 15:09
:category: Arch Linux
:tags: abs, arch, beautifulsoup, download, linux, pacotes, pkgbuild, programa, python, urllib2, vabs
:image: /images/archlogo.png
:description: Apesar do vABS ser extremamente útil e funcional, ele não possui uma boa usabilidade.

Como já havia citado no post anterior, `o recente lançamento do vABS`_ promete e muito ajudar a vida dos usuários do Arch Linux no gerenciamento do ABS em modo gráfico. Porém, para os que vivem da linha (como eu) o movimento de retirar a mão do teclado e colocá-la sobre o mouse pode ser extenuante (manias de um usuário do VIM). Além disso, e se alguém (algum dia) não tiver um servidor X rodando apropriadamente, ficará impossibilitada de usufruir do vABS.

.. image:: {filename}/images/archlinux-curved2.png
        :target: {filename}/images/archlinux-curved2.png
        :align: center
        :alt: Arch Linux

Atualmente esse é o meu problema. E parando para pensar que o meu problema pode ser o problema de muitos outros usuários do Arch Linux, resolvi começar a brincar com a possibilidade de escrever um buscador para o vABS. E a linguagem de programação escolhida? Python! :D

.. more

.. raw:: html

        <div class="alert alert-warning"><strong>Atenção:</strong>  Não tenho a intenção de propor uma solução ou criar uma ferramenta oficial, apenas quero demonstrar como podemos resolver nossos problemas com um pouco de esforço e criatividade!</div>

Qual a Ideia?!
--------------

A ideia básica desse recente projeto está na criação de uma ferramenta de linha de comando, que permita ao usuário buscar e baixar diretamente do site do vABS, um ou mais pacotes informados através do terminal. Para isso penso em utilizar os módulos ``urllib2`` e ``BeautifulSoup`` para efetuar a comunicação desta ferramenta com o servidor e assim interpretar a resposta do mesmo. Também será necessário o uso do modulo ``platform`` para detectar a atual arquitetura da máquina (se a mesma é i686 ou x86\_64), e por fim o modulo ``sys`` para obter os argumentos da linha de comando.

Como o vABS indexa pacotes de repositórios diferentes também será necessário criar uma tupla para armazenar as possíveis localizações (os repositórios destinados para o vABS) a serem buscados. Além disso é preciso que a ferramenta armazene a URL base em uma string global, permitindo seu acesso por todas as funções disponíveis, além de efetuar a verificação da arquitetura (i686 ou x86\_64) correta do sistema do usuário.

Então, para começar o programa, o cabeçalho seria composto basicamente de:

.. code-block:: python

    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-

    from platform import architecture
    from BeautifulSoup import BeautifulSoup
    import urllib2
    from sys import argv

    BASE_URL = "http://vabs.archlinux-br.org/"
    if '64bit' == architecture():
        BASE_URL += "x86_64/"
    else:
        BASE_URL += "i686/"

    REPOS = (
            'community-testing',
            'community',
            'core',
            'extra',
            'kde-unstable',
            'multilib',
            'testing',
            )

Analisando os Argumentos
------------------------

Como toda ferramenta CLI que se preze, essa também precisa de argumentos, que serão disponibilizados para os usuários utilizarem de acordo com suas necessidades. Para isso vamos analisar a seguinte situação: vamos assumir que o usuário terá apenas duas opções básicas nessa ferramenta CLI: Buscar o pacote e baixar o pacote.

::

    Buscar um pacote: vabs-tool -s
    Baixa pacote: vabs-tool -d

Para isso, vamos criar o seguinte trecho de código (que já seria suficiente) para realizar a análise dos argumentos e chamar a respectiva função escolhida pelo usuário (buscar ou baixar):

.. code-block:: python

    def valida_args():
        if len(argv) <= 2 or len(argv) > 3:
            # Argumentos de menos ou de mais
            print "Por favor informe os argumentos corretamente"
            print "Utilização: vabs-tool [-s|-d] n"
            exit(1)

        if argv[1] not in ("-d", "-s"):
            # Argumento desconhecido
            print "Por favor informe uma das seguintes opções: -d ou -sn"
            exit(1)

        if argv[1] == "-d":
            # Função a ser criada
            baixa_pacote(argv[2])
        else:
            # Função a ser criada
            busca_pacote(argv[2])

Agora falta começarmos a implementar, em código, as funções descritas pelos argumentos acima.

Realizando a Busca do Pacote
----------------------------

Vamos começar pela parte do programa relacionada à busca do pacote.  Podemos considerar essa função um pouco mais complexa de se construir, além de exige a criação de mais de uma função encadeada para seu correto funcionamento. Para que todo o procedimento seja executado de acordo, a função principal, que aqui chamaremos de ``busca_pacote``, teria como única ação, chamar uma função de nome ``busca_pacote_em`` para efetuar a busca em cada repositório cadastrado do vABS.

Assim sendo, foram separadas todas as funções somente para deixar o bloco de código menos aninhado e mais modular. E todo o trabalho sujo será feito pela função ``busca_pacote_em``, esta responsável por prever a URL-alvo, por exemplo vabs.archlinux-br.org/i686/community/W, a qual nem sempre irá existir (por isso utilizamos a instrução ``try... except...``). Após a previsão, esta função deverá baixar o conteúdo da URL e buscar todos os links usando o módulo ``BeautifulSoup``. Para finalizar, ela deverá filtrar todos os links referentes ao pacote solicitado.

Veja o código abaixo:

.. code-block:: python

    def busca_pacote_em(repo, nome_pkt):
        '''
        Função repensável por buscar e imprimir todos os pacotes que coincidem
        com o nome informado pelo usuário.
        '''
        # URL é  $BASE_URL/$repo/$letra_M/
        url = BASE_URL + repo + "/" + nome_pkt[0].upper() + "/"
        # onde:
        #  -BASE_URL: vabs.archlinux-br.org/ seguido pela arquitetura
        #             que pode ser x86_64 ou i686
        #  -repo: É o nome do repositório (valores da tupla REPO)
        #  -letra_M: Primeira letra do nome do pacote em Maiúsculo

        # Baixa a página indicada pela variável url
        try:
            # A página pode não ser encontrada (404) uma vez que nem todas as
            # letras constam em todos os repos.
            resposta = urllib2.urlopen(url)
        except urllib2.HTTPError as err:
            # Se o erro for diferente de 404 (não encontrado) mostra a exceção
            if '404' not in str(err):
                raise err
            # Finaliza a execução da função.
            return

        # Processa a resposta com a biblioteca BeautifulSoup
        html = resposta.read()
        soup = BeautifulSoup(html)

        # Busca todos os elementos do tipo a
        # Isto porque (se você olhar o código fonte da página do vABS
        # verá que) todo pacote esta dentro de uma tag
        for line in soup.findAll('a'):
            # Converte o objeto para string
            line = str(line)
            if '[DIR]' not in line:
                # Descarta todas as linhas que não tenham o texto [DIR].
                # Esse texto faz parte do elemento alt dos links dos pacotes
                continue
            if 'parent' in line:
                # Descarta o 'parent folder' que também é identificado por [DIR]
                continue
            # Retira o somente o texto entre aspas (") da linha encontrada
            line = line[line.index('"')+1:]
            line = line[:line.index('"')]

            if nome_pkt in line:
                # Imprime os pacotes encontrados no formato "nome_repo/nome_pkt"
                print repo+"/"+line[:-1]

    def busca_pacote(nome_pkt):
        for repo in REPOS:
            busca_pacote_em(repo, nome_pkt)

Baixar o Pacote
---------------

Agora estamos na parte mais complexa do programa. Para seu correto funcionamento, será necessário a criação de 3 funções distintas:

-  A primeira é a função ``valida_url``, responsável por testar se uma dada URL existe e se a mesma está disponível;
-  A segunda é a função ``baixa``, responsável por baixar um arquivo indicado por ``url`` e imprimir uma barra de progresso durante todo o processo de download e;
-  A terceira é a função ``baixa_pacote``, responsável por verificar se foi ou não informado o repositório do pacote, buscar o pacote nos repositórios (caso o usuário não tenha especificado o repositório), montar a URL de download do ``PKGBUILD``, e finalmente chamar a função ``baixa``.

A partir de agora, vamos ver em detalhes, cada uma das funções supracitadas e desenvolver um pouco a sua lógica. Vamos começar com a função mais simples, a ``valida_url``:

.. code-block:: python

    def valida_url(url):
        '''
        Requisita uma página e retorna True caso ela exista e
        Fale caso não exista.
        '''
        try:
            urllib2.urlopen(urllib2.Request(url))
            return True
        except:
            return False

Basicamente essa função utiliza o método ``urlopen`` do módulo ``urllib2`` para solicitar a determinada página, uma página indicada por ``url``, retornar *False* caso a página não seja encontrada, ou *True* caso tudo ocorra bem. Essa função será usada apenas para testar a existência de alguns diretórios no vABS.

Abaixo vamos analisar o conteúdo da função ``baixa``:

.. code-block:: python

    def baixa(url):
        '''
        Responsável por tentar baixar um arquivo do vABS para o diretório corrente.
        '''
        # Inicia a variável resposta
        resposta = None
        # Separa o nome do arquivo para utilizar na criação do arquivo de destino
        nome = url.split("/")[-1]

        # Instrução try utilizada para "captar" qualquer erro de página
        # Uma página pode não ser encontrada (404) uma vez que nem todas as
        # letras constam em todos os repos.
        try:
            # Solicita a página através do módulo urllib2
            resposta = urllib2.urlopen(url)
        except urllib2.HTTPError as err:
            if '404' not in str(err):
                # Se o erro for diferente de 404 (não encontrado) mostra uma
                # exceção não tratada
                raise err
            # Finaliza a execução da função caso o erro seja 404
            print "Pacote não encontrado:", nome
            print "URL buscada:",url
            return

        # Cria uma arquivo vazio (em modo binário) no diretório corrente
        f = open(nome, 'wb')
        # Obtêm metadados da página para deduzir a porcentagem do download
        meta = resposta.info()
        # Converte para int o tamanho do arquivo
        tamanho = int(meta.getheaders("Content-Length")[0])
        print "Realizando Download: %s Bytes: %s" % (nome, tamanho)

        # Inicia a variável que indica quantos bytes já foram baixados
        tamanho_baixado = 0
        # Tamanho do bloco (8 KBytes)
        tamanho_bloco = 8192
        while True:
            # Lê 8 KBytes do servidor
            buffer = resposta.read(tamanho_bloco)
            # Caso a resposta esteja vazia, significa que o download acabou
            if not buffer:
                # fim do download
                break
            # Incrementa o tamanho baixado com o tamanho de buffer
            tamanho_baixado += len(buffer)
            # Escreve o conteúdo baixado no arquivo
            f.write(buffer)
            # Cria linha de status
            status = r"%10d  [%3.2f%%]" % 
                    (tamanho_baixado, tamanho_baixado * 100.0/tamanho)
            # Adiciona à linha de status alguns caracteres de backspace
            # (0x8 na tabela ASCII). Isso faz com que ele volte para o
            # início da linha, assim criamos uma "barra de progresso"
            status = status + chr(8)*(len(status)+1)
            print status,

        f.close()

Esta função é um pouco mais complexa que a anterior, mas lendo atentamente os comentários é possível compreendê-la corretamente. O único ponto que vale ressaltar é o uso do caractere ``0x8`` da tabela ASCII para voltar ao início da linha. A lógica que utilizamos aqui nessa função é, se digitamos 15 caracteres, precisamos de 15 *backspaces* para voltar ao início da linha. Isso fica mais claro quando baixamos um arquivo muito grande. Como o vABS possui apenas arquivos pequenos (menos que 8 KBytes) quase não é possível ver essa função em ação, porém inserimos esse código para mostrar que é possível efetuar corretamente essa ação (além de demonstrar como criar a mesma).

Em seguida vamos ver a última função necessária para esse nosso pequeno programa – a ``baixa_pacote``:

.. code-block:: python

    def baixa_pacote(nome_pkt):
        '''
        Função utilizada para solicitar a verificação de links e o download
        do pacote tgz.
        Ela é dividida em 2 pelo primeiro if:
          - A parte do if é executada quando o usuário informa um pacote com
            seu respectivo repositório: "nome_repo/nome_pkt". Essa parte é
            responsável por separar o nome do repositório e do pacote e chamar
            a função "baixa".
          - Já a parte do else é executada quando o usuário não informa o nome
            do repositório e força a aplicação a buscar o pacote em todos os
            repositórios. A função joga todas as ocorrência exatas do pacote
            e adiciona-o em uma lista. Ao final é verificado se essa lista possui:
              - uma ocorrência: baixa essa única ocorrência
              - nenhuma ocorrência: emite uma mensagem de erro
              - mais de uma: e emite uma mensagem de inconsistência.
        '''
        if '/' in nome_pkt:
            #Nome do pacote inclui o repositório
            repo, nome_pkt = nome_pkt.split("/")
            # Cria a URL
            url = BASE_URL + repo + "/" + nome_pkt[0].upper() + "/" + nome_pkt + 
                    "/" + nome_pkt + ".tgz"
            # Solicita o Download
            baixa(url)
        else:
            print "Repositório não especificado"
            print "Buscando pacote nos repositórios..."
            repos_encontrados = []
            for repo in REPOS:
                # Cria URL para o repo/pacote desta interação
                url = BASE_URL + repo + "/" + nome_pkt[0].upper() +
                        "/" + nome_pkt + "/" + nome_pkt + ".tgz"
                # Solicita verificação da URL
                if valida_url(url):
                    # Se ela existir insere na lista
                    repos_encontrados.append(repo)

            # Pacote não encontrado em nenhum repositório
            if len(repos_encontrados) == 0:
                print "nNão foi possível encontrar o pacote em nenhum repositório.n"
                return

            # Pacote encontrado em mais de um repositório
            if len(repos_encontrados) != 1:
                print "nNão foi possível baixar o pacote pois ele existe em mais "+
                        "de um repositório."
                print "Repositorios encontrados:", ", ".join(repos_encontrados)
                return

            # Apenas um pacote encontrado. Extrai o nome e adiciona a barra
            repo = repos_encontrados[0] + "/"
            # Monta a URL
            url = BASE_URL + repo + nome_pkt[0].upper() + "/" + nome_pkt + "/" + nome_pkt + ".tgz"
            # Solicita o download do pacote
            baixa(url)

Pra finalizar, é necessário incluir o código responsável por chamar a função principal ``valida_args``;

.. code-block:: python

    if __name__ == '__main__':
        valida_args()

Pronto, agora temos uma ferramenta que busca e baixa pacotes para a pasta atual através da linha de comando! Assim não precisaremos mais mover a mão até o mouse para navegar na *Internet* e encontrar o pacote que queremos no vABS.

Utilização
----------

Agora que juntamos tudo, vamos ver alguns exemplos de execução. Para fins de teste criei um diretório em */tmp/teste* e copiei a ferramenta (com o nome de ``vabs-tool``) para esta pasta:

.. code-block:: bash


    $ cd /tmp/teste
    $ ls
    vabs-tool
    $ ./vabs-tool
    Por favor informe os argumentos corretamente
    Utilização: vabs-tool [-s|-d] <nome_do_pacote>
    $

Conforme mostrado acima, vemos que a ferramenta está identificando a ausência de argumentos corretamente. Abaixo vamos ver exemplos de busca e *download* de pacotes, especificando ou não o repositório):

.. code-block:: bash

    $ ./vabs-tool -s wine
    community/wine-1.3.24-1
    community/wine-1.3.25-1
    community/wine-1.3.26-1
    community/winefish-1.3.3-9
    community/winegame-0.2.0-1
    community/winestuff-0.2.0-1
    community/winetricks-20110629-1
    community/wine_gecko-1.2.0-1
    multilib/wine-1.3.18-1
    $ ./vabs-tool -d community/wine-1.3.24-1
    Realizando Download: wine-1.3.24-1.tgz Bytes: 1740
          1740  [100.00%]
    $ ls
    vabs-tool  wine-1.3.24-1.tgz
    $ ./vabs-tool -d wine-1.3.25-1
    Repositório não especificado
    Buscando pacote nos repositórios...
    Realizando Download: wine-1.3.25-1.tgz Bytes: 1746
          1746  [100.00%]
    $ ls
    vabs-tool  wine-1.3.24-1.tgz  wine-1.3.25-1.tgz
    $

Agora vamos ver um exemplo onde a ferramenta desenvolvida não é capaz determinar de qual repositório deve ser baixado o pacote solicitado:

.. code-block:: bash

    $ ./vabs-tool -s wesnoth
    extra/wesnoth-1.8.6-1
    extra/wesnoth-1.8.6-2
    extra/wesnoth-data-1.8.6-1
    testing/wesnoth-1.8.6-2
    $ ./vabs-tool -d wesnoth-1.8.6-2
    Repositório não especificado
    Buscando pacote nos repositórios...
    Não foi possível baixar o pacote pois ele existe em mais de um repositório.
    Repositorios encontrados: extra, testing
    $ ls
    vabs-tool  wine-1.3.24-1.tgz  wine-1.3.25-1.tgz
    $

Considerações
-------------

Para aqueles que se interessaram pela solução mas estão com preguiça de juntar todo o código em um único arquivo executável, poderá baixar o arquivo completo aqui:

.. image:: {filename}/images/download-button.png
        :align: center
        :target: https://gist.github.com/magnunleno/1141065/raw/cd9973d12c5375e81115594e2d0d11cc8565d2c5/vabs-tool
        :alt: Download vabs-tool


Código disponibilizado no `GitHub`_

Após o download basta confirmar as permissões do arquivo com o comando ``chmod +x vabs-tool`` e movê-lo para o caminho */usr/local/bin*, dessa forma é possível utilizá-lo sem mais problemas.

Não tenho a intenção de manter ou melhorar esse programa, até mesmo porque ele não é a melhor solução para o problema. Uma melhor solução seria obter um banco de dados remoto através do comando ``rsync`` ou (o mais provável) esperar que o vABS, no futuro, venha a oferecer uma *url* para consulta direta. Em quanto isso não acontece, temos essa solução paliativa.

Até a próxima...

.. _o recente lançamento do vABS: /pt/usando-o-vabs-para-instalar-o-wine-1-3-24/
.. _GitHub: https://gist.github.com/1141065

