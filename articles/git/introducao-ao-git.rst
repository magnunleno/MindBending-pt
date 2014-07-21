Introdução ao GIT
#################
:date: 2011-11-09 10:44
:category: Git
:tags: arch, bazaar, configuração, controle de versão, cvs, debian, ubuntu, editor, git, instalação, kubuntu, linus torvalds, linux, repositório, svn, vcs, vim
:image: /images/git-logo_4.png
:series: Git Para Todos

O GIT é um VCS, *version control system* (sistema de controle de
versões) distribuído com enfase na velocidade. A maioria das pessoas
esquece que um sistema de controle de versão não serve apenas para
trabalhar com códigos de programas, mas com qualquer tipo de arquivo que
precise ser versionado. Desta forma o GIT pode ser útil para qualquer um
que queira manter e controlar versões/alterações em qualquer tipo de
arquivo, seja ele um código fonte, um documento textual (por exemplo,
sua monografia), imagens e etc. Exatamente, ele pode auxiliar desde a um
estudante, passando por um designer gráfico até chegar em um
desenvolvedor.

.. image:: {filename}/images/git-logo_4.png
	:align: center
	:target: {filename}/images/git-logo_4.png
	:alt: Git Logo

A esta altura vocês me perguntam, "Mas e quanto a infraestrutura para
manter um sistema de controle de versão?", esse é outro ponto que todos
se enganam! Você pode usar o GIT apenas no seu desktop, sem depender de
um servidor, mas é claro que ele também funciona remotamente, usando o
modelo cliente-servidor.

.. more

Por isso estarei criando uma série de artigos, que terá como intuito ajudar a todos aqueles que querem
aprender a usar esta poderosa ferramenta. Então me acompanhe nesta série
de artigos pois vou ensinar (e aprender) como instalar, configurar e
utilizar o GIT, seja em um simples desktop ou até mesmo em um servidor.

O que é Um VCS?
---------------

Antes de falarmos do GIT é importante ressaltar o que é um VCS. Para
isso vou pedir uma ajuda da nossa Wikipédia...

Um sistema de controle de versão (ou versionamento), VCS (do inglês
version control system) é um software com a finalidade de gerenciar
diferentes versões no desenvolvimento de um documento qualquer. Esses
sistemas são comumente utilizados no desenvolvimento de software para
controlar as diferentes versões — histórico e desenvolvimento — dos
códigos-fontes e também da documentação.

As principais vantagens de se utilizar um sistema de controle de versão
para rastrear as alterações feitas durante o desenvolvimento de software
ou o desenvolvimento de um documento qualquer são:

-  **Controle do histórico**: facilidade em desfazer e possibilidade de
   analisar o histórico do desenvolvimento, como também facilidade no
   resgate de versões mais antigas e estáveis. A maioria das
   implementações permitem analisar as alterações com detalhes, desde a
   primeira versão até a última.
-  **Trabalho em equipe**: um sistema de controle de versão permite que
   diversas pessoas trabalhem sobre o mesmo conjunto de documentos ao
   mesmo tempo e minimiza o desgaste provocado por problemas com
   conflitos de edições. É possível que a implementação também tenha um
   controle sofisticado de acesso para cada usuário ou grupo de
   usuários.
-  **Marcação e resgate de versões estáveis**: a maioria dos sistemas
   permite marcar onde é que o documento estava com uma versão estável,
   podendo ser facilmente resgatado no futuro.
-  **Ramificação de projeto**: a maioria das implementações possibilita
   a divisão do projeto em várias linhas de desenvolvimento, que podem
   ser trabalhadas paralelamente, sem que uma interfira na outra.

Basicamente um VCS utiliza um "repositório", que é um local onde são
armazenados os arquivos a serem versionados. Esse repositório geralmente
se encontra em um servidor, mas pode também estar localizado na sua
própria máquina. A ideia principal de um VCS gira em torno do seguinte
processo:

#. Obter uma cópia de um repositório remoto;
#. Realizar alterações nos arquivos do repositório;
#. Realizar um *commit*, confirmar as alterações e inserir uma mensagem
   descri vendo-as;
#. Enviar suas alterações de volta para o servidor remoto.

Além do GIT existem diversos outros sistemas de controle de versão
livres como o CVS, Mercurial, GIT, SVN, RCS, Bazaar, dentre outras.

Para mais informações acerca do conceito de VCS recomendo a leitura
`desta página da Wikipédia`_.

E o GIT?
--------

O GIT foi inicialmente desenvolvido por Linus Torvalds para auxiliar no
desenvolvimento do Kernel Linux. Ele é um software livre *open source*
desenvolvido usando a linguagem C, Shell Script e Perl e é distribuído
sob a licensa GNU GPLv2.

O GIT se destaca pela sua simplicidade, agilidade e possibilidade de
customização através de *hooks*, muitas pessoas utilizam esta
funcionalidade para, após atualizar o repositório de código, um script
realiza o deploy da aplicação em um servidor JBoss, por exemplo. Mas
nada de pressa, vamos primeiro aprender o básico, como utilizar o GIT
apenas localmente, isto é, no seu desktop.

Instalando e Configurando o GIT
-------------------------------

A instalação do GIT é realmente muito simples, para quem utiliza o Arch
Linux basta utilizar o seguinte comando:

.. code-block:: bash

    $ sudo pacman -S git

Já para quem usa o Debian e outras distribuições similares (Linux Mint,
Ubuntu, Kubuntu e etc.), utilize o seguinte comando:

.. code-block:: bash

    $ sudo apt-get install git-core

Após a instalação precisamos configurar suas informações pessoais no
cliente do GIT. Exatamente, para que o Git registre quem realizou uma
certa alteração ele precisa de um nome e um email. Para isso utilize o
seguinte comando:

.. code-block:: bash

    $ git config --global user.name "Seu Nome"
    $ git config --global user.email "seu@email.com"

Atenção, estas configurações realizadas acima são globais, isto é,
funcionarão para todos os repositórios que você venha a trabalhar. Caso
você precise usar uma outra "identidade" em um certo repositório basta
utilizar o seguinte comando dentro do repositório:

.. code-block:: bash

    $ cd meu_repositorio
    $ git config user.name "Seu Outro Nome"
    $ git config user.email "outro@email.com"

Outra configuração que considero passível de alteração é
``core.editor``, que altera o editor padrão que o GIT usa para criar as
mensagens de *commit*. Por padrão, ele vem configurado para utilzar o VI
mas como me acostumei às melhorias do VIM, prefiro editar essa
configuração:

.. code-block:: bash

    $ git config --global core.editor vim

Git Colorido!
-------------

Outra característica configurável do GIT é a colorização de sua saída,
facilitando a identificação de certos contextos. Para ativar esta
funcionalidade utilize o seguinte comando:

.. code-block:: bash

    $ git config --global color.branch auto
    $ git config --global color.diff auto
    $ git config --global color.grep auto
    $ git config --global color.status auto

Um exemplo de saída colorida que o GIT passa a gerar:

.. image:: {filename}/images/git-colored.png
	:align: center
	:target: {filename}/images/git-colored.png
	:alt: Git Colored Output

Configuração Global e Local?!
-----------------------------

Isso mesmo, no GIT você tem configurações globais, que funcionam para
qualquer repositório, e configurações locais, que valem apenas dentro de
um certo repositório. Uma configuração local tem precedência sobre uma
configuração global, ou seja, ela "sobrescreve" a configuração global.

A configuração global é armazenada no arquivo ``~/.gitconfig``, enquanto
a configuração local é armazenada em ``$REPO/.git/config``. No exemplo
abaixo vemos um exemplo de configuração de um editor globalmente e outro
editor configurado localmente:

.. code-block:: bash

    $ cat ~/.gitconfig | grep editor
    $ git config --global core.editor vim
    $ git config core.editor
    vim
    $ cat ~/.gitconfig | grep editor
        editor = vim

Neste primeiro exemplo mostrei que não vem nenhum editor configurado no
GIT (conforme arquivo ``~/.gitconfig`` na linha 1). Depois configurei o
GIT para utilizar o editor VIM (linha 2) em seguida verifiquei se a
configuração funcionou (linhas 3 e 5). Agora vamos verificar como o GIT
se comporta em um outro repositório:

.. code-block:: bash

    $ cd repo1
    $ git config core.editor
    vim
    $ cat .git/config | grep editor

De acordo com a linha 2, podemos ver que o GIT utilizará o VIM (pois
está configurado globalmente), apesar de nenhuma configuração de editor
estar presente no arquivo de configuração local (linha 4). Agora vamos
configurar um editor diferente apenas para este repositório:

.. code-block:: bash

    $ git config core.editor emacs
    $ git config core.editor
    emacs
    $ cat .git/config | grep editor
        editor = emacs

Podemos ver que ao alterar o editor (sem utilizar a chave ``--global``)
para *emacs* uma nova chave foi criada no arquivo de configuração.
Conforme esperado, a configuração global vale para todos os repositórios
que não sobre escrevam esta configuração. Para mais opções de
configurações consulte a seção "*Variables*" no comando
``git config --help`` ou ``man git-config``. Existem diversas opções
interessantes como, taxa de compressão, *case sensitive*, abreviações,
criação de *alias*, opções de *diff* e diversas outras.

No próximo artigo vou demonstrar como criar um repositório local,
realizar nossas alterações e (o mais divertido) voltar no tempo! Até
lá...

.. _**Git Para Todos**: /pt/series/git-para-todos/
.. _desta página da Wikipédia: http://pt.wikipedia.org/wiki/Sistema_de_controle_de_vers%C3%A3o
