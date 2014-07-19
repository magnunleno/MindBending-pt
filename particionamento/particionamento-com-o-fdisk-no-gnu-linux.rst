Particionamento Com o Fdisk No GNU/Linux
########################################
:date: 2012-07-30 17:04
:category: Fdisk
:tags: aif, arch, bootable, cfdisk, ext4, fdisk, formatação, gnu, parted, linux, mbr, mkfs, ext4, mkswap, partição, sfdisk, swap
:image: /images/partitioning-sqr.png
:slug: particionamento-com-o-fdisk-no-gnu-linux

Particionar o HDD (Hard Disk Drive) utilizando o fdisk se tornará uma
tarefa corriqueira para aqueles que se aventurarem a instalar o Arch
Linux em seus computadores pois, Conforme noticiado `aqui`_, esta
distribuição descontinuou o uso do AIF (*Arch Installation Framework*)
em seu processo de instalação. Considerando que muitos usuários estão
mal acostumados a utilizarem particionadores gráficos decidi escrever
uma série de artigos ensinando a utilizar alguns particionadores em
linha de comando.

.. image:: {filename}/images/partitioning.jpg
	:align: center
	:target: {filename}/images/partitioning.jpg
	:alt: Partitioning

Para a formatação sem terminal gráfico são sugeridos na `Wiki oficial do
Arch Linux`_ o uso dos particionadores ``fdisk``, ``cfdisk`` ou
``GNU Parted``, porém eu adicionarei outro muito útil: o ``sfdisk``.
Antes de prosseguir, gostaria de ressaltar que esta dica servirá para
qualquer usuário GNU/Linux, apesar de eu me referir tanto ao Arch Linux
e sua documentação. Dado este aviso, vamos lá!

.. more

Este guia faz parte de um `tutorial que re-ensina a instalar o Arch
Linux`_ em sua máquina, utilizando o novo `processo definido pelos
desenvolvedores`_.

Cenário
-------

Nesta primeira parte ensinarei a utilizar o ``fdisk`` para particionar
um HDD vazio ou um HDD no qual você não deseja manter nenhuma partição
existente.

.. raw:: html

   <div class="alert alert-info">

**Nota** Caso seu HDD possua uma partição com o ponto de montagem (*mountpoint*)
do tipo ``home`` e você queira manter seu conteúdo, eu irei demonstrar
este processo em um próximo artigo.

.. raw:: html

   </div>

Neste cenário utilizaremos um HDD de 20 GByte que será particionado em 4
partições primárias:

-  ``/boot`` - 200 MBytes com o formato ext4;
-  ``/swap`` - 2 GBytes com o formato Linux Swap;
-  ``/ (root)`` - 10 GBytes com o formato ext4;
-  ``/home`` - 7.8 GBytes com o formato ext4.

Vale ressaltar que esses valores são apenas para demonstração, em um
sistema para uso de verdade é recomendado reservar:

-  De 100 a 200 MBytes para o ``/boot``;
-  De 1 a 2 vezes o tamanho da sua memória RAM (dependendo de quanto
   seja) o ``/swap``. Para mais informações leia a `página da Wiki`_;
-  De 20 a 20 GBytes para o ``/ (root)``;
-  O espaço restante (a partir de 5 GBytes) para o ``/home`` que
   hospedará os dados do seu usuário.

Pre-requisitos Para Uso do Fdisk
--------------------------------

Antes de iniciar esse processo é necessário (e obrigatório)
certificar-se que o fdisk está presente no seu sistema, identificar o
HDD a ser particionado e assegurar que nenhuma partição do HDD a ser
formatado está montada.

Para assegurar a primeira condição utilize o comando ``whereis fdisk``
ou simplesmente ``fdisk -v``. Ele deverá apresentar uma das saídas
abaixo:

.. image:: {filename}/images/01-whereis-fdisk-and-ver.png
	:align: center
	:target: {filename}/images/01-whereis-fdisk-and-ver.png
	:alt: Output from Whereis fdisk & fdisk -v

Para identificarmos o HDD a ser particionado utilize o comando
``fdisk -l`` (ou ``fdisk -l | grep Disk``) para visualizar o
identificador e tamanho do respectivo HDD:

.. image:: {filename}/images/02-fdisk-l-grep.png
	:align: center
	:target: {filename}/images/02-fdisk-l-grep.png
	:alt: Fdisk -l \| grep Disk

Após analisarmos a saída do comando constatamos que o disco a ser
utilizado é o /dev/sda.

Para garantir que nenhuma partição do HDD ``/dev/sda`` está montado
utilize o comando ``mount | grep sda``. Caso nenhuma partição esteja
montada, não será retornada nenhuma linha. Caso negativo, você
visualizará o nome das partições e seu respectivo ponto de montagem.

.. image:: {filename}/images/03-mount-grep-sda-notas2.png
	:align: center
	:target: {filename}/images/03-mount-grep-sda-notas2.png
	:alt: Mount \| grep sda

Neste caso, é obrigatório desmontar essas partições, para isso utilize o
comando ``umount [mount_point]``, substituindo ``[mount_point]`` pelo
ponto de montagem apresentado na saída do comando ``mount``.

Satisfeitas todos os pre-requisitos vamos iniciar o processo de
particionamento do HDD.

Iniciando o Particionador Fdisk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para iniciar o particionador vinculado ao disco que será particionado,
neste caso ``/dev/sda``, utilize o comando ``fdisk /dev/sda``. Após
emitir este comando você visualizará o seguinte prompt:

.. image:: {filename}/images/04-fdisk-sda.png
	:align: center
	:target: {filename}/images/04-fdisk-sda.png
	:alt: Fdisk - Inicio

O fdisk tem um funcionamento bem básico. Você sempre partirá do prompt
``Command (m for help):``. Após digitar uma letra (**apenas** uma letra)
você acionará uma opção. Para visualizar todas as opções visíveis
utilize o comando ``m``, que apresentará a seguinte mensagem:

.. image:: {filename}/images/05-fdisk-m.png
	:align: center
	:target: {filename}/images/05-fdisk-m.png
	:alt: Fdisk - Ajuda

Uma vez emitido um comando você passará por um diálogo que lhe informará
algo e pedirá um retorno (argumentos), mas no fim você sempre retornará
ao prompt citado anteriormente.

Listando Partições Com o Fdisk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

É sempre bom, assim que iniciar o ``fdisk``, listar as partições
existentes no HDD. Caso seu HDD esteja completamente vazio será mostrado
as seguintes informações:

.. image:: {filename}/images/06-fdisk-p-empty.png
	:align: center
	:target: {filename}/images/06-fdisk-p-empty.png
	:alt: Fdisk - Conteúdo do Disco sda

Caso seu disco possua outras partições serão apresentadas informações
conforme abaixo:

.. image:: {filename}/images/07-fdisk-p-with-partitions.png
	:align: center
	:target: {filename}/images/07-fdisk-p-with-partitions.png
	:alt: image7

Caso seu HDD possua partições será necessário deletá-las antes de
prosseguirmos.

Deletando Partições Com o Fdisk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para deletar uma partição basta utilizar a opção ``d`` e em seguida
informar ao fdisk o número da partição a ser deletada. Ao final deste
procedimento você retornará ao prompt inicial. Abaixo uma imagem
demonstrando a deleção de uma partição:

.. image:: {filename}/images/08-fdisk-d.png
	:align: center
	:target: {filename}/images/08-fdisk-d.png
	:alt: Fdisk - Deletando Partição 1

Para seguir com a instalação é necessário repetir esse procedimento para
todas as partições existentes, até que seu HDD esteja sem nenhum
partição.

Criando Partições Com o Fdisk
-----------------------------

Para criar uma partição é utilizado comando ``n``. Em seguida será
necessário informar o tipo de partição (primária ou estendida), o número
da partição (geralmente sequencial), o (primeiro) setor a partir do qual
a partição será alocada e o último setor (que indicará o tamanho da
partição).

.. raw:: html

   <div class="alert alert-info">

**Nota** Um setor é a menor divisão física do disco, e possui na grande maioria
das vezes 512 Bytes. Ao emitir o comando ``p`` o fdisk mostra o tamanho
do setor. No exemplo anterior 1 setor é igual a 512 Bytes.

.. raw:: html

   </div>

Para evitar a necessidade de realizar cálculos convertendo setor para
GBytes o fdisk te dá a possibilidade de escrever o tamanho do último
setor em Bytes, bastando apenas adicionar o símbolo + seguido do tamanho
e do identificador K (KBytes), M (MBytes) ou G (GBytes). Atenção, é de
suma importância utilizar o sinal + no início do tamanho.

Vocês notarão que eu sempre utilizarei o valor sugerido (padrão) na
solicitação de "primeiro setor", pois ele sempre sugere o setor
adjacente à última partição criada. Desta forma eu não precisarei
digitar um número enorme e as partições sempre estarão próximas e sem
espaços vazios.

Criando o /boot
~~~~~~~~~~~~~~~

A partição o ``/boot`` é criada com os seguintes atributos: ela será a
**primeira** partição, começará no setor 2048 com o tamanho de partição
de 200 MBytes. Abaixo a demonstração deste processo:

.. image:: {filename}/images/09-fdisk-n-boot.png
	:align: center
	:target: {filename}/images/09-fdisk-n-boot.png
	:alt: Fdisk - Nova partição sda1

Criando o /swap
~~~~~~~~~~~~~~~

A partição o ``/swap`` é criada com os seguintes atributos: ela será a
**segunda** partição, começará no setor 411648 com o tamanho de partição
de 2 GBytes. Abaixo a demonstração deste processo:

.. image:: {filename}/images/10-fdisk-n-swap.png
	:align: center
	:target: {filename}/images/10-fdisk-n-swap.png
	:alt: Fdisk - Nova partição sda2

Criando o / (root)
~~~~~~~~~~~~~~~~~~

A partição o ``/ (root)`` é criada com os seguintes atributos: ela será
a **terceira** partição, começará no setor 4605952 com o tamanho de
partição de 10 GBytes. Abaixo a demonstração deste processo:

.. image:: {filename}/images/11-fdisk-n-root.png
	:align: center
	:target: {filename}/images/11-fdisk-n-root.png
	:alt: Fdisk - Nova partição sda3

Criando o /home
~~~~~~~~~~~~~~~

A partição o ``/home`` é criada com os seguintes atributos: ela será a
**quarta** partição, começará no setor 25577472 com o restante do espaço
livre (7,8 GBytes). Abaixo a demonstração deste processo:

.. image:: {filename}/images/12-fdisk-n-home.png
	:align: center
	:target: {filename}/images/12-fdisk-n-home.png
	:alt: Fdisk - Nova partição sda4

Notem que quando o fdisk solicitou que fosse informado o "último setor",
eu simplesmente pressionei enter para que ele utilizasse o valor
sugerido, ou seja, o restante do disco.

Partições Lógicas Com o Fdisk
-----------------------------

Com a queda dos preços dos HDDs o uso de partições estendidas está
caindo em desuso, mas como este artigo visa ensinar o uso da ferramenta
fdisk, irei demonstrar como criar 1 partição primária e uma partição
estendida (que abrigará duas partições lógicas). Mas antes disso vamos
entender qual a utilidade as partições lógicas.

Devida a restrição de endereçamento na MBR, um HDD consegue abrigar
apenas 4 partições. Caso você precise de mais partições será
**obrigatório** o uso de uma partição estendida, que conterá diversas
parições lógicas. A restrição de endereçamento de uma partição estendida
está diretamente vinculada ao Kernel e, atualmente, o GNU/Linux consegue
armazenar até 59 partições lógicas. No GNU/Linux toda e qualquer
partição lógica será endereçada a partir do número 5, isto é, a partir
do dispositivo /dev/sda5.

O desenho abaixo representa as partições que iremos criar neste exemplo:

.. image:: {filename}/images/extended-partition.png
	:align: center
	:target: {filename}/images/extended-partition.png
	:alt: extended-partition

Abaixo segue a criação da primeira partição, uma partição primária de 2
GByte:

.. image:: {filename}/images/23-fdisk-extended-sda1.png
	:align: center
	:target: {filename}/images/23-fdisk-extended-sda1.png
	:alt: image14

Em seguida criamos uma partição estendida que ocupará o restante do HDD
(18 GByte):

.. image:: {filename}/images/24-fdisk-extended-sda2.png
	:align: center
	:target: {filename}/images/24-fdisk-extended-sda2.png
	:alt: image15

Nesta partição estendida criamos a primeira partição lógica, que conterá
5 GBytes:

.. image:: {filename}/images/25-fdisk-extended-sda5.png
	:align: center
	:target: {filename}/images/25-fdisk-extended-sda5.png
	:alt: Fdisk - Nova partição sda5

E por último uma partição lógica que ocupará o restante do HDD (13
GBytes):

.. image:: {filename}/images/26-fdisk-extended-sda5.png
	:align: center
	:target: {filename}/images/26-fdisk-extended-sda5.png
	:alt: Fdisk - Nova partição sda6

Ao final seu HDD estará da seguinte forma:

.. image:: {filename}/images/27-fdisk-extended-p.png
	:align: center
	:target: {filename}/images/27-fdisk-extended-p.png
	:alt: image18

As cores estão de acordo com o diagrama mostrado inicialmente.

Alterando Partições
-------------------

Além do tamanho uma partição possui algumas propriedades a mais. Ao
final podemos revisar a estrutura do HDD utilizando o comando ``p``:

.. image:: {filename}/images/13-fdisk-p.png
	:align: center
	:target: {filename}/images/13-fdisk-p.png
	:alt: image19

Podemos notar que existem 2 pontos a serem corrigidos: definir a parição
/dev/sda1 como *bootable* e definir o formato da partição /dev/sda2 como
*swap*. Em outras palavras vamos alterar duas propriedades das
partições: a flag de boot da partição /dev/sda1 e o tipo da partição
/dev/sda2.

Definindo a Partição de Boot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para definirmos a partição /dev/sda1 como uma partição de boot, isto é,
torná-la *bootable* basta utilizar o comando ``a`` e em seguida informar
o número da partição:

.. image:: {filename}/images/14-fdisk-a-bootable.png
	:align: center
	:target: {filename}/images/14-fdisk-a-bootable.png
	:alt: Fdisk - Marcando partição como "bootable"

Ao final teremos as partições organizadas da seguinte forma:

.. image:: {filename}/images/15-fdisk-p-bootable.png
	:align: center
	:target: {filename}/images/15-fdisk-p-bootable.png
	:alt: image21

Note o \* na coluna *Boot*.

Configurar Partição de Swap
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para definir a partição /dev/sda2 como uma partição de swap utilizamos o
comando ``t`` e em seguida informaremos o número da partição (2) e o
código hexadecimal 82 (Linux swap). Conforme imagem abaixo:

.. image:: {filename}/images/16-fdisk-t-swap.png
	:align: center
	:target: {filename}/images/16-fdisk-t-swap.png
	:alt: Fdisk - Mudando tipo da partição 2

Para a lista completa de formatos suportados pela ferramenta fdisk
utilize o comando ``L`` quando você for requisitado a digitar o código
hexadecimal. Abaixo a lista completa:

.. image:: {filename}/images/17-fdisk-t-l.png
	:align: center
	:target: {filename}/images/17-fdisk-t-l.png
	:alt: Fdisk - Tipos de partições

Ao final teremos as partições organizadas da seguinte forma:

.. image:: {filename}/images/18-fdisk-p.png
	:align: center
	:target: {filename}/images/18-fdisk-p.png
	:alt: image24

Note o nome ``Linux swap / Solaris`` na coluna *System* e o código 82 na
colina *Id*.

Aplicando Alterações
~~~~~~~~~~~~~~~~~~~~

Ao final de todo o procedimento, e após revisarmos se tudo está
configurado corretamente, devemos utilizar o comando ``w`` para que
todas as alterações sejam escritas na tabela de partição. Após emitir
este comando o programa fdisk irá finalizar sua execução:

.. image:: {filename}/images/19-fdisk-w.png
	:align: center
	:target: {filename}/images/19-fdisk-w.png
	:alt: Fdisk - Gravando alterações

Formatando Partições
--------------------

Você certamente notou que nos deletamos partições, criamos partições,
alteramos o tipo da partição e marcamos partições como bootáveis mas em
momento nenhum fizemos uma formatação sequer. Exatamente, a ferramenta
fdisk é exclusivamente utilizada para particionar, para formatar as
partições serão utilizadas as ferramentas ``mkfs``, ``mkswap`` e
``swapon``.

Neste exemplo utilizaremos o formato ext4 para as partições ``/boot``,
``/ (root)`` e ``/home``. Para formatar a partição /dev/sda1 com o
formato ext4 utilize o comando ``mkfs.ext4 /dev/sda1``. Segue abaixo
exemplo das criações das partições para as partições sda1, sda3 e sda4:

.. image:: {filename}/images/20-mkfs-sda1-boot.png
	:align: center
	:target: {filename}/images/20-mkfs-sda1-boot.png
	:alt: 20-mkfs-sda1-boot

.. image:: {filename}/images/21-mkfs-sda3-root.png
	:align: center
	:target: {filename}/images/21-mkfs-sda3-root.png
	:alt: 21-mkfs-sda3-root

.. image:: {filename}/images/22-mkfs-sda4-home.png
	:align: center
	:target: {filename}/images/22-mkfs-sda4-home.png
	:alt: 22-mkfs-sda4-home


A parição swap possui um formato específico e por isso é utilizado um
comando diferente. Para preparar a partição /dev/sda2 utilizaremos o
comando ``mkswap /dev/sda2 && swapon /dev/sda2``. O comando ``mkswap`` é
responsável por criar uma área de swap em um dado dispositivo, enquanto
o comando ``swapon`` ativa o dispositivo e os arquivos de paginação.
Segue abaixo exemplo da execução:

.. image:: {filename}/images/23-mkswap-swapon.png
	:align: center
	:target: {filename}/images/23-mkswap-swapon.png
	:alt: 23-mkswap-swapon

Conclusão
---------

Apesar do longo artigo (2200 palavras) podemos constatar que a
utilização do fdisk não é complexa, apenas exige do utilizador que ele
aprenda o significado de algumas letras e o básico de formatação.

Comparando um pouco com o processo antigo (via AIF), eu considero que a
diferença de processos é mínima. O AIF possuía como vantagem apenas o
fato de podermos indicar o *mount point* das partições, o que teremos
que fazer manualmente mais para frente.

.. _aqui: /pt/arch-linux-sem-aif/
.. _Wiki oficial do Arch Linux: https://wiki.archlinux.org/index.php/Partitioning
.. _tutorial que re-ensina a instalar o Arch Linux: /pt/instalando-o-arch-linux-iso-20120804/
.. _processo definido pelos desenvolvedores: https://wiki.archlinux.org/index.php/Arch_Install_Scripts
.. _página da Wiki: https://wiki.archlinux.org/index.php/Partitioning
