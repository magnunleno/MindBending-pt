SystemD v197 Renomeiará Interfaces
##################################
:date: 2013-01-18 20:52
:category: Arch Linux
:tags: arch, enp0s3, eth, eth0, inet, interfaces, linux, rede, systemd
:image: /images/archlogo.png

Okay, eu sei que eu não costumo reclamar muito de mudanças e até gostei
quando o SystemD se tornou um padrão no Arch Linux, mas a última versão
deste gerenciador de serviços irá causar **muita** dor de cabeça.

.. image:: {filename}/images/arch-broken.jpg
	:align: center
	:target: {filename}/images/arch-broken.jpg
	:alt: Arch Broken

Nesta nova versão do SystemD os desenvolvedores do `freedesktop.org`_
simplesmente decidiram que vão renomear **todas as interfaces de rede**
do seu sistema operacional.

.. more

Mudanças no SystemD
-------------------

No momento tudo o que posso afirmar é que durante uma instalação do Arch
Linux (usando a mídia archlinux-2013.01.04-dual.iso) sua interface é
chamada de ``eth0`` normalmente, porém após o boot a minha interface se
chamava ``enp0s3``. Ou seja, após a instalação eu tive que reconfigurar
todos os arquivos que referenciavam o nome ``eth0``.

Não afirmo com certeza, mas é bem provável que logo após um update e um
reboot no seu desktop todas as comunicações de rede irão cessar, pois a
interface ``eth0`` não irá mais existir. Qual a melhor parte? Você não
terá acesso a internet para consultar uma possível solução, você estrá
por sua própria conta e risco :).

.. figure:: {filename}/images/i-have-no-idea-what-im-doing-dog.jpg
	:align: center
	:target: {filename}/images/i-have-no-idea-what-im-doing-dog.jpg
	:alt: image1

	Ele desenvolve para o Freedesktop.org

Baseado na explicação do site `freedesktop.org`_ a nova nomenclatura se
baseia nas seguintes informações:

-  Índices do Firmware/BIOS providos pelos dispositivos on-board
   (exemplo: eno1);
-  Número do slot provido pelo Firmware/BIOS do barramento PCI Express
   (exemplo: ens1);
-  Localização física/geográfica do conector de hardware (exemplo:
   enp2s0);
-  Endereço MAC do dispositivo (exemplo: enx78e7d1ea46da);
-  Em último caso, numeração sequencial clássica provida pelo kernel
   (exemplo: eth0).

E qual a vantagem de tudo isso? Isso é o que eles alegam:

-  Nomes constantes mesmo após reboots;
-  Nomes constantes mesmo após a substituição das placas ou
   remanejamento de slots;
-  Nomes de interface estáveis mesmo após atualizações e mudanças de
   Kernel e/ou drivers;
-  Nome de interface estáveis mesmo que você substitua uma interface
   defeituosa;
-  Os nomes são determinados automaticamente sem a configuração do
   usuário;
-  Os nomes de interface são totalmente previsíveis, por exemplo, apenas
   olhando pelo ``lspci`` você pode deduzir como a interface irá se
   chamar;
-  Operações totalemente stateless, mudanças de hardware não resultarão
   em mudanças no /etc;
-  Compatibilidade com permissões de apenas-leitura;
-  Os nomes de interface agora são mais condizentes com os alias dos
   dispositivos de bloco e o no /dev;
-  Aplica-se em todas as as arquiteturas, x86 e non-x86;
-  Nomeclatura consistente para todos os sistemas que adotam o
   SystemD/Udev;

Desabilitando
-------------

Bem, se você usa o Arch Linux ou qualquer outra distribuição que se
utiliza do SystemD e não gostou desta alteração ela pode ser facilmente
revertida. Basta utilizar o seguintes comando:

.. code-block:: bash

    $ ln -s /dev/null /etc/udev/rules.d/80-net-name-slot.rules

Boa sorte :)

.. _freedesktop.org: http://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames
