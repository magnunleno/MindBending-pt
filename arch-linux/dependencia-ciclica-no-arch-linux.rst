Dependência Cíclica no Arch Linux
#################################
:date: 2012-10-18 14:30
:category: Arch Linux
:tags: arch, atualizar, cíclica, deadlock, dependência, gcc-libs-multilib, gerenciador, instalar, lib32-gcc-libs, linux, multilib, pacman, pacote, remover
:image: /images/archlogo.png

Ontem, ao tentar atualizar meu Arch Linux acabe passando por um problema de dependência cíclica com o ``gcc-libs``. "Mas o que é dependência cíclica?" você me pergunta. Basicamente é o mesmo que um deadlock, mas no âmbito de um gerenciador de pacotes. Isto é, quando a atualização do "Pacote A" depende da atualização do "Pacote B" e a atualização do "Pacote B" depende da atualização do "Pacote A", desta forma o sistema não consegue se atualizar e fica preso. Para entender melhor, que tal uma imagem?

.. image:: {filename}/images/deadlock.jpg
	:align: center
	:target: {filename}/images/deadlock.jpg
	:alt: Deadlock

O meu caso o caso de dependência cíclica ocorreu entre as bibliotecas ``lib32-gcc-libs`` e sua dependência ``gcc-libs-multilib``. É importante ressaltar que isto ocorre apenas para quem usa o repositório ``multilib``. Mesmo este não sendo um problema difícil de se resolver, estou escrevendo sobre ele pois a solução se aplica a outros casos de dependência cíclica do ``pacman`` e além disso esse problema pode vir a ocorrer com outras pessoas que utilizam o Arch Linux.

.. more

A Dependência Cíclica
---------------------

Para ajudar as pessoas a identificar o problema, vou apresentar a mensagem de erro que ocorreu após emitir o comando de atualização:

.. code-block:: bash

    $ sudo pacman -Suy
    [sudo] password for magnun: 
    :: Sincronizando a base de dados de pacotes...
     core está atualizado
     extra está atualizado
     community está atualizado
     multilib está atualizado
     archlinuxfr está atualizado
     xyne-x86_64 está atualizado
    :: Iniciando atualização completa do sistema...
    :: Substituir python-imaging por community/python2-imaging? [S/n] s
    :: Substituir python-notify por extra/python2-notify? [S/n] s
    resolvendo dependências...
    atenção: dependência cíclica detectada:
    atenção: lib32-gcc-libs será instalado antes de sua dependência gcc-libs-multilib
    procurando por conflitos inter-relacionados...
    erro: falha ao preparar a transação (não foi possível satisfazer as dependências)
    $ 

Atenção para as 2 linhas que seguem abaixo de ``"resolvendo dependências..."``, elas identificam o tipo de erro (dependência cíclica) e os pacotes envolvidos (``lib32-gcc-libs`` e ``gcc-libs-multilib``).

Geralmente esse tipo de problema ocorre quando, durante alguma migração ou atualização, um "Pacote B" deixou de depender de um "Pacote A", ou algo similar. Como você "perdeu" essa atualização, o banco de dados do seu pacman ainda acha que o "Pacote B" depende do "Pacote A".

Resolvendo a Dependência Cíclica
--------------------------------

Basicamente para se resolver o problema de dependência cíclica devemos reinstalar a dependência do pacote. Mas o grande problema é que o pacman não nos permite removê-lo apenas emitindo o comando de remoção tradicional. Para conseguirmos removê-lo devemos informar ao pacman que ele deve ignorar a verificação de dependências, o que pode ser feito com a *flag* ``-dd``.

Confiram abaixo a execução do comando:

.. code-block:: bash

    $ sudo pacman -Rdd gcc-libs-multilib

    Alvos (1): gcc-libs-multilib-4.7.1-6

    Total removido:     2,95 MiB

    Deseja remover estes pacotes? [S/n] s
    (1/1) removendo gcc-libs-multilib           [##########] 100%
    $

Agora, basta reinstalar o pacote que você acabou de remover, normalmente:

.. code-block:: bash

    $ sudo pacman -S gcc-libs-multilib
    resolvendo dependências...
    atenção: dependência cíclica detectada:
    atenção: lib32-gcc-libs será instalado antes de sua
    dependência gcc-libs-multilib
    procurando por conflitos inter-relacionados...

    Alvos (2): lib32-gcc-libs-4.7.2-1  gcc-libs-multilib-4.7.2-1

    Tamanho Total Download:    1,46 MiB
    Tamanho Total Instalado:   5,79 MiB
    Alteração no Tamanho:      2,95 MiB

    Prosseguir com a instalação? [S/n] s
    :: Obtendo pacotes de multilib...
     lib32-gcc-libs-4.7.2-1-x86_64      732,4 KiB   312K/s 00:02 [######] 100%
     gcc-libs-multilib-4.7.2-1-x86_64   767,6 KiB   330K/s 00:02 [######] 100%
    (2/2) verificando integridade do pacote                      [######] 100%
    (2/2) carregando arquivos do pacote                          [######] 100%
    (2/2) verificando conflitos de arquivo                       [######] 100%
    (2/2) verificando espaço em disco disponível                 [######] 100%
    (1/2) atualizando lib32-gcc-libs                             [######] 100%
    (2/2) instalando gcc-libs-multilib                           [######] 100%

Por fim, mande atualizar o sistema normalmente:

.. code-block:: bash

    $ sudo pacman -Suy
    :: Sincronizando a base de dados de pacotes...
     core está atualizado
     extra está atualizado
     community está atualizado
     multilib está atualizado
     archlinuxfr está atualizado
     xyne-x86_64 está atualizado
    :: Iniciando atualização completa do sistema...
    :: Substituir python-imaging por community/python2-imaging? [S/n] s
    :: Substituir python-notify por extra/python2-notify? [S/n] s
    resolvendo dependências...
    procurando por conflitos inter-relacionados...

    Alvos (118): ati-dri-9.0-1  blender-5:2.64a-2  (...)

    Tamanho Total Download:    386,91 MiB
    Tamanho Total Instalado:   1821,38 MiB
    Alteração no Tamanho:      81,00 MiB
    (...)
    $

Pronto, seu Arch Linux está livre da dependência cíclica e irá atualizar com sucesso.

Happy hacking :)
