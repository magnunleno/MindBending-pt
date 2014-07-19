Preparem-se Irmãos do Arch Linux - Parte 2
##########################################
:date: 2013-06-06 16:22
:category: Arch Linux
:tags: /bin, /lib, /sbin, /usr/bin, /usr/lib, arch, atualização, filesystem, freedesktop, linux, pacman
:image: /images/archlogo.png

Aproximadamente `um ano atras`_ o Arch Linux abandonou o ``/lib`` em
prol do ``/usr/lib``. Muitos reclamaram, se debateram e xingaram muito
no twitter, mas nada mudou o fato do ``/lib`` ser migrado. Muito bem
irmãos Arch Linux, agora `é a vez do /bin ser migrado`_.

.. image:: {filename}/images/bin-is-phasing-out-e1370546036778.jpg
	:align: center
	:target: {filename}/images/bin-is-phasing-out-e1370546036778.jpg
	:alt: /bin is phasing out

Desde a época da migração do ``/lib`` foi noticiado que este era apenas
o inicio de uma grande remodelagem do sistema de arquivos. O fato é que
este procedimento não foi inventado ou iniciado pelo Arch Linux, mas sim
solicitado pelos desenvolvedores do grupo `Freedesktop`_ e,
consequentemente, essas mudanças entrarão em vigor não somente no Arch
Linux mas em vários outras distribuições GNU/Linux.

.. more

Migrando
--------

Muito bem, como eu acabei me atrasando pra escrever esse artigo acredito
que muitos já tenham se deparado com o problema, caso negativo basta
você usar o comando ``sudo pacman -Suy``. Ao final da atualização você
verá a seguinte mensagem:

::

    erro: falha em submeter a transação (arquivos conflitantes)
    filesystem: /bin existe no sistema de arquivos
    filesystem: /sbin existe no sistema de arquivos
    filesystem: /usr/sbin existe no sistema de arquivos
    Ocorreram erros e, portanto, nenhum pacote foi atualizado.

.. raw:: html

   <div class="alert alert-info">

**Atenção** Nesta atualização, nunca (eu disse **nunca**) use a força pequeno
Obi-Wan (estou me referindo ao comando ``--force``) pois isso resultará
na quebra de sistema.

.. raw:: html

   </div>

Isso simplesmente quer dizer que ele não pode concluir toda a
atualização devido ao conflito do ``/bin``, ``/sbin`` e ``/usr/sbin``.
Tudo que devemos fazer é esvaziar completamente esses diretórios.

A princípio todos os pacotes oficiais já estão corrigidos, com isso
devemos nos preocupar apenas com pacotes não oficiais, como por exemplo
os pacotes do AUR e outros manualmente instalados. Para consultar todos
os pacotes "não oficiais" que possuem arquivos nesse diretório utilize o
seguinte comando:

.. code-block:: bash

    $ sudo pacman -Qqo /bin /sbin /usr/sbin | pacman -Qm -
    uml_utilities 20070815-5

No meu caso havia apenas o pacote ``uml_utilities``. Neste ponto temos
duas opções:

-  Mover manualmente os arquivos do ``/bin`` e do ``/sbin`` para o
   diertório ``/usr/sbin``;
-  Desinstalar esses pacotes para reinstalá-los posteriormente.

A primeira opção envolve em você manipular esses diretórios manualmente,
o que é meio arriscado, logo optei pela segunda opção: Desinstalar os
pacotes. Para isso utilize um comando simples e comum para qualquer
usuários Arch Linux: ``sudo pacman -Rns uml_utilities``. Após remover os
pacotes listados consulte se existe mais alguma coisa repetindo o
comando ``sudo pacman -Qqo /bin /sbin /usr/sbin | pacman -Qm -``.

Por último vamos procurar por pacotes instalados de repositórios não
oficiais. Para saber quais repositórios não oficiais você possui,
consulte o arquivo ``/etc/pacman.conf`` e descarte os repositórios
oficiais (para mais uma demonstração dos repositórios padrões consulte
essa `página da Wiki`_). Muito bem, para mim havia o ``archlinuxfr``, o
qual utilizo para instalar o ``yaourt``. Desta forma, para consultar os
pacotes do ``archlinuxfr`` que devem ser adequados utilize o seguinte
comando:

.. code-block:: bash

    $ paclist archlinuxfr | awk ' { print $1 } ' | pacman -Ql - | grep ' /s\?bin/\| /usr/sbin/'

Importante notar que o comando acima consulta somente o ``archlinuxfr``,
se você possuir outro repositório consulte por ele também substituindo o
nome do repositório.

Muito bem, aqui temos um ponto importante. Se no seu arquivo
``/etc/pacman.conf`` existir algum pacote em ``IgnorePkg`` ou
``IgnoreGroup`` você deverá mover os arquivos em ``/bin`` ou ``/sbin``
manualmente. Para listar os arquivos vinculados a um pacote utilize o
seguinte comando: 

.. code-block:: bash

        $ pacman -Ql package_name

Muito bem, feito tudo isso, só para ter certeza que não haverá nenhum
arquivo nos diretórios mencionado utilize o seguinte comando:
``find /bin /sbin /usr/sbin -exec pacman -Qo -- {} + >/dev/null``

Por último vamos atualizar o sistema ignorando os pacotes ``filesystem``
e ``bash``:

.. code-block:: bash

    $ sudo pacman -Syu --ignore filesystem,bash
    :: Sincronizando a base de dados de pacotes...
     core está atualizado
     extra está atualizado
     community está atualizado
     multilib está atualizado
    :: Iniciando atualização completa do sistema...
    atenção: bash: ignorando atualização do pacote (4.2.045-1 => 4.2.045-4)
    atenção: filesystem: ignorando atualização do pacote (2013.03-2 => 2013.05-2)
    resolvendo dependências...
    procurando por conflitos inter-relacionados...
    (...)

Muito bem, agora podemos atualizar o ``bash``:

.. code-block:: bash

    $ sudo pacman -S bash
    resolvendo dependências...
    procurando por conflitos inter-relacionados...

    Pacotes (1): bash-4.2.045-4

    Tamanho total instalado:   3,51 MiB
    Alteração no tamanho:    -0,10 MiB

    :: Continuar a instalação? [S/n] s
    (1/1) verificando chaves no chaveiro                [########] 100%
    (1/1) verificando integridade do pacote             [########] 100%
    (1/1) carregando arquivos do pacote                 [########] 100%
    (1/1) verificando conflitos de arquivo              [########] 100%
    (1/1) verificando espaço em disco disponível        [########] 100%
    (1/1) atualizando bash                              [########] 100%

Por último atualize todo o sistema:

.. code-block:: bash

    $ sudo pacman -Su
    :: Iniciando atualização completa do sistema...
    resolvendo dependências...
    procurando por conflitos inter-relacionados...

    Pacotes (1): filesystem-2013.05-2

    Tamanho total instalado:   0,01 MiB
    Alteração no tamanho:    -0,30 MiB

    :: Continuar a instalação? [S/n] s
    (1/1) verificando chaves no chaveiro             [#########] 100%
    (1/1) verificando integridade do pacote          [#########] 100%
    (1/1) carregando arquivos do pacote              [#########] 100%
    (1/1) verificando conflitos de arquivo           [#########] 100%
    (1/1) verificando espaço em disco disponível     [#########] 100%
    (1/1) atualizando filesystem                     [#########] 100%

Pronto, ao final tudo deve ter corrido bem. Agora que todo o sistema
está atualizado, reinstale aqueles pacotes que foram removidos.

Para finalizar reinicie seu computador, acenda 3 velas, realize um
sacrifício celta com aquele seu CD do Windows XP pirata, rogue seu santo
padrinho e reverencie 7 vezes o gabinete do seu computador durante o
carregamento do bootloader. No fim, garanto que seu sistema voltará
normalmente.

Boas Novas
----------

Após toda esse trabalho temos uma boa notícia, conforme `proposta
original na lista de discussão oficial do Arch Linux Dev`_ essa migração
foi a última. Ou pelo menos a última dessa série :).

.. _um ano atras: /pt/preparem-se-irmaos-do-arch-linux
.. _é a vez do /bin ser migrado: http://archlinux-br.org/noticias/212/
.. _Freedesktop: http://www.freedesktop.org/wiki/Software/systemd/TheCaseForTheUsrMerge/
.. _página da Wiki: https://wiki.archlinux.org/index.php/Pacman#Repositories
.. _proposta original na lista de discussão oficial do Arch Linux Dev: https://mailman.archlinux.org/pipermail/arch-dev-public/2012-March/022625.html
