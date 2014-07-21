Preparem-se Irmãos do Arch Linux
################################
:date: 2012-07-11 23:40
:category: Arch Linux
:tags: /lib, arch, atualização, erro, gcc, glibc, gnu, ignore, linux, pacman
:image: /images/archlogo.png

É da natureza do ser humano reclamar, isto é um fato. Porém, é curioso
como dentro da comunidade GNU/Linux as reclamações são mais inflamadas.
Sempre que alguma atualização quebra o sistema, dezenas de milhares de
usuários distribuem seu ódio em fóruns, listas de discussões, blogs e
demais meios de comunicação. Porém muitos deles se esquecem que o
transtorno pelos quais estão passando é (boa parte das vezes) causado
por mera falta de informação. Mais curioso ainda é como no pequeno mundo
de usuários do Arch Linux a proporção desses acontecimentos é bem maior.
E já vou adiantando, a próxima tragédia anunciada está a caminho.

.. image:: {filename}/images/brace-yourselves.jpg
	:align: center
	:target: {filename}/images/brace-yourselves.jpg
	:alt:  Brothers Brace Yourselves

Foi `anunciado no dia 3 de Julho`_ em diversas listas de discussão do
Arch da última etapa de migração do diretório ``/lib`` que (a esta
altura) já deve estar no repositório *testing*. Para ajudar essa
migração (provavelmente traumática para muitos usuários) foi
disponibilizada uma nova versão do *pacman* `feita especialmente para
lidar com esta atualização`_.

.. more

Como podemos ver os desenvolvedores e responsáveis por essa distribuição
estão anunciando previamente e tomando todas as medidas para reduzir
qualquer problema que o usuário venha a encontrar. O mínimo que estes
usuários deveriam fazer é se manter informados. Então, companheiros de
Arch, ao menos acompanhem a `lista de discussão do ArchLinux-BR`_, pois
esta mudança foi anunciada com antecedência pelo colega Leandro Inácio.
Caso você não goste de listas de discussão, acompanhe o `portal
ArchLinux-BR`_ pois este tipo de notícia sempre aparece por lá.

E para ninguém reclamar que as explicações estão em inglês eu estou
escrevendo esse artigo. Então vamos ver como nos prevenir.

Como Se Preparar Para o Inevitável
----------------------------------

Já dizia o sábio, de nada lhe vale saber lutar se você não sabe quem é
seu inimigo. Então vamos à parte mais importante, identificar quando a
mudança atingir o seu repositório. Na verdade é bem simples, o
``pacman`` irá te mostrar a seguinte mensagem indicando um conflito no
diretório ``/lib``:

::

    erro: falha em submeter a transação (arquivos conflitantes)
    glibc: /lib existe no sistema de arquivos
    Ocorreram erros e, portanto, nenhum pacote foi atualizado.

.. raw:: html

   <div class="alert alert-info">

**Atenção** Nesta atualização, nunca (eu disse **nunca**) use a força pequeno
Obi-Wan (estou me referindo ao comando ``--force``) pois isso resultará
na quebra de sistema.

.. raw:: html

   </div>

Caso essa mensagem apareça não tema, apenas emita o seguinte comando que
atualizará o seu sistema ignorando a atualização da glibc (incluí a
saída do comando gerada pelo meu Arch para te assegurar que tudo está
indo bem):

.. code-block:: bash

    $ pacman -Suy --ignore glibc
    :: Iniciando atualização completa do sistema...
    atenção: glibc: ignorando atualização do pacote (2.16.0-1 => 2.16.0-2)
    resolvendo dependências...
    procurando por conflitos inter-relacionados...

    Alvos (7): kmod-9-2  lib32-glibc-2.16.0-2  libsystemd-186-2  linux-3.4.4-3
    lirc-utils-1:0.9.0-20  syslog-ng-3.3.5-2  systemd-tools-186-2

    Tamanho Total Instalado:   79,69 MiB
    Alteração no Tamanho:      -0,15 MiB

    Prosseguir com a instalação? [S/n] s
    (7/7) verificando integridade do pacote                  [###############] 100%
    (7/7) carregando arquivos do pacote                      [###############] 100%
    (7/7) verificando conflitos de arquivo                   [###############] 100%
    (7/7) verificando espaço em disco disponível             [###############] 100%
    (1/7) atualizando kmod                                   [###############] 100%
    ==> Kernel modules are now only read from /usr/lib/modules, all custom
        built kernels and modules must be moved there before rebooting.
    (2/7) atualizando lib32-glibc                            [###############] 100%
    (3/7) atualizando libsystemd                             [###############] 100%
    (4/7) atualizando linux                                  [###############] 100%
    >>> Updating module dependencies. Please wait .
    >>> Generating initial ramdisk, using mkinitcpi..
    ==> Building image from preset: 'default'
      -> -k /boot/vmlinuz-linux -c /etc/mkinitcpio.conf -g /boot/initramfs-linux.img
    ==> Starting build: 3.4.4-3-ARCH
      -> Running build hook: [base]
      -> Running build hook: [udev]
      -> Running build hook: [autodetect]
      -> Running build hook: [pata]
      -> Running build hook: [scsi]
      -> Running build hook: [sata]
      -> Running build hook: [filesystems]
      -> Running build hook: [usbinput]
      -> Running build hook: [fsck]
    ==> Generating module dependencies
    ==> Creating gzip initcpio image: /boot/initramfs-linux.img
    ==> Image generation successful
    ==> Building image from preset: 'fallback'
      -> -k /boot/vmlinuz-linux -c /etc/mkinitcpio.conf -g
      /boot/initramfs-linux-fallback.img -S autodetect
    ==> Starting build: 3.4.4-3-ARCH
      -> Running build hook: [base]
      -> Running build hook: [udev]
      -> Running build hook: [pata]
      -> Running build hook: [scsi]
      -> Running build hook: [sata]
      -> Running build hook: [filesystems]
      -> Running build hook: [usbinput]
      -> Running build hook: [fsck]
    ==> Generating module dependencies
    ==> Creating gzip initcpio image: /boot/initramfs-linux-fallback.img
    ==> Image generation successful
    (5/7) atualizando lirc-utils                             [###############] 100%
    (6/7) atualizando syslog-ng                              [###############] 100%
    (7/7) atualizando systemd-tools                          [###############] 100%
    $ 

Por fim atualize todo o sistema (dessa vez incluindo a ``glibc``):

.. code-block:: bash

    $ pacman -Su
    :: Iniciando atualização completa do sistema...
    resolvendo dependências...
    procurando por conflitos inter-relacionados...

    Alvos (3): glibc-2.16.0-2  gparted-0.13.0-1  util-linux-2.21.2-5

    Tamanho Total Download:    2,67 MiB
    Tamanho Total Instalado:   50,42 MiB
    Alteração no Tamanho:      0,04 MiB

    Prosseguir com a instalação? [S/n] s
    :: Obtendo pacotes de core...
     util-linux-2.21.2-5-x86_64     1406,9 KiB  230K/s 00:06 [###############] 100%
    :: Obtendo pacotes de extra...
     gparted-0.13.0-1-x86_64        1328,7 KiB  235K/s 00:06 [###############] 100%
    (3/3) verificando integridade do pacote                  [###############] 100%
    (3/3) carregando arquivos do pacote                      [###############] 100%
    (3/3) verificando conflitos de arquivo                   [###############] 100%
    (3/3) verificando espaço em disco disponível             [###############] 100%
    (1/3) atualizando glibc                                  [###############] 100%
    Generating locales...
      pt_BR.UTF-8... done
      pt_BR.ISO-8859-1... done
    Generation complete.
    (2/3) atualizando gparted                                [###############] 100%
    (3/3) atualizando util-linux                             [###############] 100%
    $ 

Pronto, seu sistema deve ter sido atualizado com sucesso. Para ter
certeza verifique se o diretório /lib é um link simbólico (com o
seguinte comando):

.. code-block:: bash

    $ ls -ld /lib
    lrwxrwxrwx   1 root root     7 Jul 11 21:10 lib -> usr/lib

Agora, só por medida de precaução, reinicie seu sistema :D.

Resolução de sistema
--------------------

De acordo com a `nova página da Wiki do Arch Linux`_, podem ocorrer 2
tipos de problemas, descritos adiante.

Problema 1: erro de dependências da glibc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Caso o ``pacman`` acuse algum outro pacote que dependa da biblioteca
``glibc`` será apresentada a seguinte mensagem:

::

    warning: ignoring package glibc-2.16.0-2
    warning: cannot resolve "glibc>=2.16", a dependency of "gcc-libs"

    (...) # Algumas saídas omitidas

    :: The following packages cannot be upgraded due to unresolvable dependencies:
         binutils  gcc  gcc-libs

    Do you want to skip the above packages for this upgrade [y/N] y

Ao confirmar a pergunta acima o pacman irá adicionar os pacotes à "lista
de ignorados" para esta atualização. Em seguida será necessário
atualizá-los explicitamente, porém solicitando que o pacman ignore as
versões de suas dependências (-Sd):

.. code-block:: bash

    $ pacman -Sd binutils gcc gcc-libs

Ao final será necessário atualizar o restante do sistema:

.. code-block:: bash

    $ pacman -Su

Para ter certeza que a atualização foi realizada com sucesso, verifique
se o diretório /lib é um link simbólico (com o seguinte comando):

.. code-block:: bash

    $ ls -ld /lib
    lrwxrwxrwx   1 root root     7 Jul 11 21:10 lib -> usr/lib

Agora, só por medida de precaução, reinicie seu sistema :D

Problema 2: O último comando (pacman -Su) reporta conflitos em /lib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se o ``pacman`` continuar reclamando de conflitos no ``/lib`` isso quer
dizer que você ainda possui arquivos/diretórios no seu diretório
``/lib`` ou o pacman acredita que um outro pacote além do glibc ainda é
proprietário do diretório ``/lib``.

Primeiro vamos tentar resolver o problema através dos pacotes, para isso
vamos listar quais pacotes são detentores de arquivos/diretórios no
``/lib``:

.. code-block:: bash

    $ find /lib -exec pacman -Qo -- {} +

Se algum pacote além do glibc for listado como proprietário de um
arquivo, esse pacote precisa ser atualizado/reinstalados manualmente
para que suas bibliotecas sejam movidas de ``/lib`` para ``/usr/lib``.
Para isso utilize o comando de atualização do pacman:

.. code-block:: bash

    $ pacman -S 

Outro caso (porém mais raro) é quando outro pacote além do glibc
acredita ser "dono" do diretório ``/lib``. Para detectar esse pacote
utilize o comando abaixo:

.. code-block:: bash

    $ grep '^lib/' /var/lib/pacman/local/*/files | grep -v glibc

Estes pacotes precisam ser reconstruídos para que não incluam o
diretório ``/lib``. Desta forma o comando ``pacman -Su`` será executado
com sucesso.

Se (mesmo após a atualização/reinstalação) houverem arquivos sem dono no
diretório ``/lib``, será necessária uma intervenção manual. Mais uma
vez, **atenção** pois as manipulações descritas abaixo só devem ser
feitas para arquivos/diretórios que não são propriedade de nenhum
pacote, confirme anteriormente se algum arquivo é propriedade de um
pacote com o comando ``find /lib -exec pacman -Qo -- {} +``.

-  **Intervenção Manual 1**: Se existir algum arquivo/diretório no
   ``/lib`` e este também exista em ``/usr/lib`` ele poderá ser apagado;
-  **Intervenção Manual 2**: Caso o arquivo/diretório exista apenas em
   ``/lib`` mova-o para o diretório ``/usr/lib``;
-  **Intervenção Manual 3**: Caso o arquivo/diretório em ``/lib`` seja
   um link simbólico para ``/usr/lib`` remova-o;
-  **Intervenção Manual 4**: Caso o arquivo/diretório em ``/lib`` seja
   um link simbólico para uma outro lugar além de ``/usr/lib`` mova-o
   para ``/usr/lib``.

Para que a atualização seja concluída com sucesso **não deve haver
nenhum subdiretório em /lib**. Quando esta condição estiver satisfeita,
emita o comando ``pacman -Su`` novamente.

Para ter certeza que a atualização foi realizada com sucesso, verifique
se o diretório /lib é um link simbólico (com o seguinte comando):

.. code-block:: bash

    $ ls -ld /lib
    lrwxrwxrwx   1 root root     7 Jul 11 21:10 lib -> usr/lib

Agora, só por medida de precaução, reinicie seu sistema :D

A Pior Parte
------------

Após isso tudo ainda tem uma má notícia. Para aqueles que utilizam algum
*custom kernel* só me resta desejar boa sorte. Devida a atualização
concomitante do ``kmod`` essa atualização **quebrará** todos os módulos
do seu kernel. Então, após a atualização vocês terão que recompilar o
kernel.

.. raw:: html

   <div class="alert alert-info">

**Update** De acordo com a `descrição do colega Erico Nunes`_ basta trocar o *custom kernel* pelo kernel do repositório core. Consequentemente tudo dentro do ``/lib`` irá pertencer ao glibc e a atualização ocorrerá conforme esperado e sem problemas.

.. raw:: html

   </div>

Mais uma vez, mantenham-se informados sobre o sistema que você usa, isso
é o mínimo que você pode fazer.

.. _anunciado no dia 3 de Julho: http://mailman.archlinux.org/pipermail/arch-dev-public/2012-July/023178.html
.. _feita especialmente para lidar com esta atualização: http://mailman.archlinux.org/pipermail/arch-dev-public/2012-July/023207.html
.. _lista de discussão do ArchLinux-BR: https://groups.google.com/forum/?fromgroups#!forum/archlinux-br
.. _portal ArchLinux-BR: http://archlinux-br.org/
.. _nova página da Wiki do Arch Linux: https://wiki.archlinux.org/index.php/DeveloperWiki:usrlib
.. _descrição do colega Erico Nunes: https://groups.google.com/d/msg/archlinux-br/q3vswN-fyRM/WnOO7CdQ8ioJ
