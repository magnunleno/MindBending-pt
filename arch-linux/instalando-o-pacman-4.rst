Instalando o Pacman 4
#####################
:date: 2012-01-17 14:31
:category: Arch Linux
:tags: arch, atualização, chave, debian, erro, gnu, gpg, instalação, linux, pacman, pacman-key, pacotes, ubuntu
:image: /images/archlogo.png

Hoje `foi disponibilizado no repositório`_ ``core``, o *pacman* 4. Esta
nova versão traz diversas `novas funcionalidades`_ para o gerenciamento
de pacotes do Arch Linux, porém a que mais se destaca é a assinatura GPG
(*GNU Privacy Guard*) de pacotes, que garante a integridade e a
confiabilidade dos pacotes e/ou repositórios para essa distribuição. É
fato que essa funcionalidade já existia há algum tempo em outras
distribuições GNU/Linux, como o Debian e derivados. Entretanto, no Arch
Linux ainda estava em fase de testes e só podia ser obtida ativando o
repositório *testing* ou compilando o mesmo através do AUR (ou
utilizando a ferramenta ``yaourt``).

.. image:: {filename}/images/pacman.png
	:align: center
	:target: {filename}/images/pacman.png
	:alt: Pacman

O Arch Linux, diferente de outras distribuições, sempre se esforça para
tornar mais suave qualquer processo migratório. E nenhuma grande mudança
é `"enfiada goela a baixo do usuário"`_ do usuário. Assim sendo, esta
funcionalidade vem desabilitada por padrão nesta atualização. Mas mesmo
com todo o cuidado do mundo, uma mudança significativa pode exigir certo
nível de intervenção manual, e esta atualização não é uma exceção.
Quando tentei atualizar o *pacman* hoje, recebi a seguinte mensagem:

.. more

.. code-block:: bash

    $ sudo pacman -Suy
    resolvendo dependências...
    procurando por conflitos interrelacionados...
    erro: falha ao preparar a transação (não foi possível satisfazer as dependências)
    :: package-query: requer pacman<3.6
    :: pacman-color: requer pacman<3.6

Para resolver esse problema, basta que o usuário remova alguns pacotes
anteriormente instalados (*package-query*, *pacman-color* e *yoaurt*) e,
em seguida, efetue novamente (e de modo forçado) a atualização do
*pacman*:

.. code-block:: bash

    $ pacman -R package-query pacman-color yaourt
    $ sudo pacman -S pacman
    resolvendo dependências...
    procurando por conflitos interrelacionados...

    Alvos (2): libarchive-3.0.3-2  pacman-4.0.1-4

    Tamanho Total do Download:   2,17 MB
    Tamanho Total da Instalação:   5,97 MB

    Prosseguir com a instalação? [S/n] s
    :: Obtendo pacotes de core...
     libarchive-3.0.3-2-i686         1215,4K  212,2K/s 00:00:06 [###########] 100%
     pacman-4.0.1-4-i686             1005,0K  159,0K/s 00:00:06 [###########] 100%
    (2/2) verificando integridade do pacote                     [###########] 100%
    (2/2) verificando conflitos de arquivo                      [###########] 100%
    (1/2) atualizando libarchive                                [###########] 100%
    (2/2) atualizando pacman                                    [###########] 100%
    atenção: /etc/pacman.conf instalado como /etc/pacman.conf.pacnew
     >>> Run `pacman-key --init` to set up your pacman keyring.

Em seguida podemos reinstalar os programas removidos anteriormente:

.. code-block:: bash

    $ pacman -S package-query pacman-color yaourt

Após esta atualização, mesmo que não seja útil em seu ambiente de
trabalho o uso de chaves GPG, é interessante que você inicie (pelo
menos) o uso do keyring do pacman. O motivo para essa ativação é já
preparar o ambiente do usuário para utilizar as chaves GPG, pois em
breve será padrão em todas as distribuições Linux. Para isso utilize o
seguinte comando:

.. code-block:: bash

    $ sudo pacman-key --init
    gpg: /etc/pacman.d/gnupg/trustdb.gpg: banco de dados de confiabilidade criado
    gpg: no ultimately trusted keys found
    gpg: Generating pacman keychain master key...

    Não há bytes aleatórios suficientes. Por favor, faça algum outro trabalho
    para que o sistema possa coletar mais entropia!
    (São necessários mais 281 bytes)
    ...
    gpg: key XXXXXXXX marked as ultimately trusted
    gpg: Done
    ==> Atualizando base de dados de confiança...
    gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
    gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u

Após inicializar o *keyring*, renomeie o novo arquivo de configuração
que foi instalado junto com a atualização do *pacman*:

.. code-block:: bash

    $ sudo mv /etc/pacman.conf /etc/pacman.conf.old
    $ sudo mv /etc/pacman.conf.pacnew /etc/pacman.conf

.. raw:: html

   <div class="alert alert-info">Durante esse processo de atualização do pacman, vale ressaltar que, se você utilizava repositórios de terceiros, terá que incluí-los novamente de forma manual.</div>

Este novo arquivo de configuração para o *pacman* possui uma nova (e
melhorada) sintaxe para os repositórios de pacotes do Arch Linux. E uma
das novidades é o uso de uma chave do tipo ``SigLevel``, criada para
controlar a verificação das chaves GPG para cada repositório ativo. Esta
chave pode ter os seguinte valores:

-  **Required:** Força a verificação de assinaturas;
-  **Optional (valor padrão):** Irá verificar as assinaturas caso elas
   existam, mas também podrá aceitar pacotes sem assinaturas;
-  **Never:** Desabilita a verificação de assinaturas (não é
   aconselhável);

Vale lembrar que o uso do *Never* não é aconselhável em um ambiente de
produção. Porém, caso você não queira utilizar as assinaturas, basta
editar o arquivo ``/etc/pacman.conf`` trocando o valor de ``SigLevel``
para ``Never``.

Caso você deseje utilizar a verificação de chaves GPG (o mais
aconselhável) você verá algumas mensagens como esta abaixo:

.. code-block:: bash

    $ sudo pacman -S gvim
    resolvendo dependências...
    procurando por conflitos inter-relacionados...

    Alvos (2): vim-runtime-7.3.401-1  gvim-7.3.401-1

    Tamanho Total Download:    5,27 MiB
    Tamanho Total Instalado:   27,99 MiB
    Alteração no Tamanho:      0,03 MiB

    Prosseguir com a instalação? [S/n] s
    :: Obtendo pacotes de extra...
     vim-runtime-7.3.401-1-i686             4,2 MiB   227K/s 00:19 [#########] 100%
     gvim-7.3.401-1-i686                 1048,6 KiB   211K/s 00:05 [#########] 100%
    (2/2) verificando integridade do pacote                        [#########] 100%
    erro: vim-runtime: key "FCF2CB179205AC90" is unknown
    :: Importar chave PGP 9205AC90, [...], criada 2011-04-19? [S/n] s
    (1/1) checking package integrity [##################] 100%
    error: vim-runtime: signature from “*****” is unknown trust
    error: failed to commit transaction (invalid or corrupted package (PGP signature))
    Errors occurred, no packages were upgraded.

Como podemos ver, o próprio *pacman* nos questiona se desejamos importar
esta chave porém, logo em seguida, falha informando que a assinatura da
chave é desconhecida. A assinatura da chave só pode ser realizada
manualmente através do seguinte comando:

.. code-block:: bash

    $ sudo pacman-key --lsign-key FCF2CB179205AC90
    ==> Atualizando base de dados de confiança...
    gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
    gpg: depth: 0  valid:   1  signed:   1  trust: 0-, 0q, 0n, 0m, 0f, 1u
    gpg: depth: 1  valid:   1  signed:   0  trust: 1-, 0q, 0n, 0m, 0f, 0u

    $ sudo pacman -S gvim

No início, as chaves GPG podem ser bastante chatas de se manusear. Isso
se deve pelo constante questionamento do sistema durante as diversas
etapas do processo de ativação das chaves dentro de seu ambiente de
trabalho (para todos os pacotes e programas envolvidos). Porém, após a
inclusão de todas as chaves necessárias para a segurança de seu sistema,
essas mensagens não mais aparecerão em sua tela.

Para o futuro, será extremamente recomendado à todos os usuários Arch
Linux que **sempre** utilizem a verificação de chaves GPG em seus
sistemas. Ela será a garantia de que o pacote utilizado em seu ambiente
de produção esteja sendo **realmente** distribuído por uma fonte
confiável.

Porém, nos dias de hoje, uma boa (porém temporária) pratica seria manter
o nível de verificação de chaves como Optional, já que existem muitos
pacotes dentro dos diversos repositórios para o Arch Linux que ainda não
estão assinados.

Assim sendo, com o tempo -- quando a prática de assinatura de pacotes
estiver completamente difundida na distribuição, abrangendo todos os
seus repositórios (oficiais e de terceiros) -- você poderá efetuar a
troca **permanente** do nível de verificação, de Optional para Required,
garantindo assim maior nível de segurança para o seu ambiente de
trabalho.

.. _foi disponibilizado no repositório: http://archlinux-br.org/noticias/178/
.. _novas funcionalidades: http://projects.archlinux.org/pacman.git/tree/NEWS
.. _"enfiada goela a baixo do usuário": http://unity.ubuntu.com/
