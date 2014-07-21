Curso de Filosofia GNU - Parte 4
################################
:date: 2014-04-11 11:13
:category: Filosofia GNU
:tags: curso, filosofia gnu, cdtc, richard stallman, FSF, free software, open source, hurd, linux, freebsd
:image: /images/The_GNU_logo-300x293.png
:series: Curso de Filosofia GNU
:description: Linux, Hurd e FreeBSD. A combinação dessa sopa de letrinhas com o termo GNU gera muita discussão dentro do mundo do Software Livre. Muitos dizem que é purismo dos adeptos da FSF, outros acham justo.

Essa é uma parte delicada na Filosofia GNU, muitas pessoas não entendem porquê `Richard Stallman`_ implica tanto com a nomenclatura de sistemas operacionais. Muitas pessoas dizem que Stallman começou da forma errada, escrevendo as ferramentas antes do kernel. Mas se analisarmos o contexto histórico (a "decadência" do Unix), fazia sentido escrever primeiro as ferramentas para substituir aos poucos as ferramentas não livres, para posteriormente escrever um novo kernel.

.. image:: {filename}/images/filosofia-gnu/typisk_gnu.jpg
        :target: {filename}/images/filosofia-gnu/typisk_gnu.jpg
        :alt: I Want GNU!
        :align: center

Lembrando que o `Curso de Filosofia GNU`_ é um conteúdo livre obtido no `CDTC`_.

.. more

4 Sistema Operacional e Kernel
------------------------------

4.1 O Sistema GNU
^^^^^^^^^^^^^^^^^

`GNU`_ é o nome do sistema operacional criado por `Richard Stallman`_ no ano de 1984. Era muito comum na época os programadores darem nomes aos seus programas utilizando-se de acrônimos recursivos (acrônimo - sm., conjunto de letras, pronunciado como uma palavra normal, formado a partir das letras iniciais -- ou de sílabas -- de palavras sucessivas que constituem uma denominação), assim o Stallman a partir da afirmação "*GNU Not Unix*", criou o nome do sistema operacional, GNU.

4.2 O Kernel
^^^^^^^^^^^^

No centro de um sistema operacional está o *kernel*. Ele é composto por vários programas que intermediam os aplicativos que você usa no seu sistema operacional e a máquina, o hardware.

Quando você manda o seu programa de edição de textos gravar um arquivo, ele faz uma chamada ao *kernel* e "diz para ele": grave estes dados!. O *kernel* então verifica se existe espaço no disco, qual a primeira trilha livre para gravar, faz a gravação do seu arquivo, grava a tabela de índice do disco, retorna ao seu editor de textos e "diz para ele": gravei o arquivo!, ao que, para você, simplesmente a tela que você utilizou para mandar gravar o arquivo vai fechar (se tudo correu bem), se houver um erro na gravação, ou a falta de espaço em disco por exemplo, o seu aplicativo vai jogar outra tela no vídeo informando o "Erro na Gravação".

O Linux é um *kernel*, é um projeto iniciado em 25 de agosto de 1991 pelo finlandês `Linus Torvalds`_, e foi apoiado por milhares de programadores ao redor do mundo.

O Hurd é um outro projeto, que vem sendo produzido pela *Free Software Foundation*, que utiliza um outro conceito, baseado em micro *kernel*, implementando características diferentes.

O FreeBSD é um outro *kernel*, produzido pelo projeto BSD, e já existe projeto de implementá-lo junto a distribuição Debian.

Logo, GNU/Linux é o nome correto para o conjunto do Sistema Operacional GNU acrescido do *kernel* de Linux Torvalds. Se o Sistema Operacional GNU for acrescido do *kernel* FreeBSD, então o correto é chamar o conjunto de GNU/FreeBSD.

Note, o projeto de criação do *kernel* de Linux Torvalds é de 1991, portanto, 7 anos após o projeto da *Free Software Foundation* ter iniciado. A GPL, o compilador GCC e o editor Emacs já estavam prontos e disponíveis juntamente com uma infinidade de programas que compunham o sistema operacional.


Créditos
--------

O material foi desenvolvido por Djalma Valois Filho e é o resultado de uma compilação das duvidas mais usuais que surgiram ao longo das inúmeras palestras apresentadas desde o ano 2000 pelo CIPSGA - Comitê de Incentivo a Produção do Software GNU e Alternativo em todo Brasil.

Todo o conteúdo encontrado neste curso é oriundo dos textos publicados pela FSF, bem como outros textos publicados pelo CIPSGA até a presente data. Críticas e sugestões construtivas são bem vindas a qualquer tempo, podendo ser enviadas para *email [at] dvalois [dot] net*.

.. _CDTC: http://cursos.cdtc.org.br/
.. _Curso de Filosofia GNU: /pt/series/curso-de-filosofia-gnu
.. _Richard Stallman: http://stallman.org
.. _GNU: http://www.gnu.org/
.. _Linus Torvalds: https://plus.google.com/+LinusTorvalds
