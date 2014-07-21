Bug Afeta o Blender no Arch Linux
#################################
:date: 2012-01-02 11:04
:category: Arch Linux
:tags: arch, blender, bug, debug, falha de segmentação, linux, openimageio, pacman, vabs, valgrind
:image: /images/LogoBlender.jpg

Ontem no início da noite resolvi retomar meus trabalhos de modelagem e renderização no `Blender`_, porém tive uma desagradável surpresa: O Blender não iniciava mais. Mais alguém ai está passando pelo mesmo problema? Eu não encontrei muitos brasileiros reclamando, apenas alguns gringos...

.. raw:: html

   <div class="alert alert-info">

**Update:** Já foi liberada uma correção, continue lendo para saber mais....

.. raw:: html

   </div>

.. image:: {filename}/images/LogoBlender.jpg
	:align: center
	:target: {filename}/images/LogoBlender.jpg
	:alt: Blender Logo

Mas que ótimo presente de Natal/Ano Novo, não?! Com não gosto de reclamar, resolvi partir para uma análise do problema. A regra número 1 do **Guia do Mochileiro do Linux** nos diz: **"Execute pelo terminal!!!"**. E foi exatamente o que eu fiz:

.. more

.. code-block:: bash

    magnun»~$ blender
    Falha de segmentação

Dizem que uma imagem vale por mil palavras, então a única imagem pode expressar meu estado mental é esta:

.. figure:: {filename}/images/WTF.jpg
	:align: center
	:target: {filename}/images/WTF.jpg
	:alt: WTF?!

	WTF?!

Após alguma horas de pesquisa encontrei o seguinte `*Bug Report* para o Arch Linux`_. Aparentemente (baseado na análise do `Valgrind`_) a biblioteca `OpenImageIO`_ está tentando acessar um endereço de memória não mapeado, resultando uma falha de segmentação:

::

    ==15854== Invalid read of size 4
    ==15854==    at 0x4B0BABF: OpenImageIO::v0::ustring::make_unique(char const*) (in /usr/lib/libOpenImageIO.so)
    ==15854==    by 0x4C3678F: ??? (in /usr/lib/libOpenImageIO.so)
    ==15854==  Address 0x27a9 is not stack'd, malloc'd or (recently) free'd
    ==15854== 
    ==15854== 
    ==15854== Process terminating with default action of signal 11 (SIGSEGV)
    ==15854==  Access not within mapped region at address 0x27A5
    ==15854==    at 0x4B0BABF: OpenImageIO::v0::ustring::make_unique(char const*) (in /usr/lib/libOpenImageIO.so)
    ==15854==    by 0x4C3678F: ??? (in /usr/lib/libOpenImageIO.so)
    ==15854==  If you believe this happened as a result of a stack
    ==15854==  overflow in your program's main thread (unlikely but
    ==15854==  possible), you can try to increase the size of the
    ==15854==  main thread stack using the --main-stacksize= flag.
    ==15854==  The main thread stack size used in this run was 8388608.

Para realizar este mesmo teste, basta executar o seguinte comando: ``$ valgrind blender``.

Continuando com o *Bug Report*, mesmo após atualizarem a biblioteca ``openimageio`` (dia 31/12/2011) o problema ainda persiste (mesmo adicionando as *flags* de *debug*), pelo menos na minha máquina. Esta era uma excelente hora para utilizarmos o `vABS`_ do nosso colega Estevão Valadão, porém ele encontra-se "indisponível".

.. role:: strike

:strike:`Então, utilizadores do Blender & Arch Linux, segurem-se nas cadeiras e aguardem uma solução pois ainda não temos informações concretas de uma solução que funcione para todos. Se mais alguém estiver passando por este problema ou tenha conseguido alguma solução de contorno, avise nos comentários. Por hora, acho que vou adiar por mais uns dias meus vídeos sobre o VIM :(`

A Correção
----------

Enquanto escrevia (dia 01/02) realizei diversas tentativas de correção, porém nenhuma delas resultou em sucesso. Então finalizei este artigo sem uma solução definitiva, apenas aguardando que os desenvolvedores resolvessem o problema e liberassem uma nova versão, o que costuma levar um certo tempo!

Mas como a equipe do Arch Linux sempre se supera e me surpreende, foi verificado hoje (dia 02/01 às 08:15) que, ao alterar o ``makepkg.conf`` e para que a biblioteca OpenImageIO fosse compilada com o comando ``make debug`` sem o parâmetro ``-O2`` o problema desaparecia. Logo a correção foi testada por mais membros do Arch Linux e em seguida foi liberada nos repositórios oficiais para a comunidade de usuários.

De acordo com o pacman o pacote atingiu os repositórios exatamente às 11:19, praticamente 03 horas depois:

.. code-block:: bash

    $ sudo pacman -Si openimageio
    Repositório          : community
    Nome                 : openimageio
    Versão               : 0.10.4-3
    URL                  : http://www.openimageio.org/
    Licenças             : custom
    Grupos               : Nenhum
    Provê                : Nenhum
    Depende De           : openexr  boost-libs  jasper  glew
    Depend. Opcionais    : qt: iv image viewer
                           python2: bindings support
    Conflita Com         : Nenhum
    Substitui            : Nenhum
    Tamanho do Download  : 2039,79 K
    Tamanho Instalado    : 9212,00 K
    Empacotador          : Sven-Hendrik Haase 
    Arquitetura          : i686
    Data da Compilação   : Seg 02 Jan 2012 11:19:48 BRST
    Soma MD5             : 37e4cfc628daa51e9a0207e995c3d2d2
    Descrição            : A library for reading and writing images, including classes, utilities, and applications.

Então, pra resolvermos o problema basta a seguinte linha:

.. code-block:: bash

    $ sudo pacman -Suy

Por essas e outras não canso de dizer que o Arch Linux é uma das melhores distribuições Linux que existem! Obrigado a todos vocês que ajudam a construir esse maravilhoso sistema operacional!

.. _Blender: http://www.blender.org/
.. _*Bug Report* para o Arch Linux: https://bugs.archlinux.org/task/27771
.. _Valgrind: http://valgrind.org/
.. _OpenImageIO: https://sites.google.com/site/openimageio/home
.. _vABS: http://vabs.archlinux-br.org/i686/
