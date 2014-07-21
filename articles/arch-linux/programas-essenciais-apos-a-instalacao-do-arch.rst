Programas Essenciais Após a Instalação do Arch
##############################################
:date: 2011-07-15 16:27
:category: Arch Linux
:tags: arch, aspell, aur, bzip, chromium, empathy, faenza, firefox, flash, gnash, gstreamer, gzip, opera, p7zip, pacman, tar, unrar, unzip, yaourt
:image: /images/archlogo.png
:description: Já temos nosso sistema instalado e com o ambiente gráfico rodando, e agora? Vamos adicionar os programas mais utilizados!
:series: Instalando e Configurando o Arch Linux

Nessa terceira parte da série de artigos "Instalando o Arch Linux Sem Dor", vou indicar algumas instalações a serem feitas para tornar seu Arch Linux ainda mais amigável para o seu dia-a-dia.

.. image:: {filename}/images/ArchLinux2.png
        :target: {filename}/images/ArchLinux2.png
        :align: center
        :alt: ArchLinux2

Nesse artigo iremos utilizar muito o comando pacman (gerenciador de pacotes do Arch Linux), caso tenham dúdivas basta uma consulta ao meu `último artigo`_.

.. more

Navegadores
~~~~~~~~~~~

Para as pessoas mais velhas no mundo GNU/Linux, escolher um navegador Web é uma lembrança um pouco incerta. Naquela época (tempos remotos), praticamente a única opção disponível para o mundo Linux era o Firefox.  Hoje em dia temos diversas opções, sendo cada uma com seu diferencial no mercado, além de recursos exclusivos. A escolha de um navegador nos dias de hoje é algo muito pessoal, então mostrarei como instalar os principais navegadores no seu Arch Linux. Veja os comandos simples descritos abaixo:

.. code-block:: bash

    $ sudo pacman -S firefox
    $ sudo pacman -S chromium
    $ sudo pacman -S opera

Vale lembrar que no Arch Linux, você encontra não somente as opções de navegadores disponíveis, mas suas versões de desenvolvimento, versões alfa e versões beta. Se não for feita nenhuma especificação no comando de instalação dos pacotes de interesse (como nos comandos acima), o Pacman irá instalar apenas as versões consideradas estáveis desses navegadores.

Flash
~~~~~

Apesar de concordar com o fato do Flash ser uma tecnologia velha, 100% proprietária, recordista em falhas de segurança, completamente fora dos padrões Web, sem possibilidade do uso de SEO apropriado, e que consome muitos (i. é: praticamente todos) os recursos disponíveis em seu computador (memória RAM e processamento), energia e largura de banda, ela ainda é (infelizmente) muito utilizada na Internet. Dessa forma somos "forçados" a instalar um *flash player*.

Para aqueles que são adeptos da filosofia Livre, existe um *flash player* livre chamado Gnash que pode ser instalado com o comando abaixo:

.. code-block:: bash

    $ sudo pacman -S gnash-gtk

Para os que gostam (contraditoriamente) de apoiar o uso de tecnologias não livres em sistemas livres como o Linux, poderão instalar o flashplugin com a seguinte linha de comando:

.. code-block:: bash

    $ sudo pacman -S flashplugin

Corrigindo o Empathy
~~~~~~~~~~~~~~~~~~~~

Algumas atualizações do Arch Linux pós-instalação são a título de correção, como é o caso do popular cliente de mensagens instantâneas Empathy. Por algum motivo, após a instalação do Arch Linux, o Empathy (substituto oficial do Pidgin no Gnome) abria corretamente. Porém, ao tentar adicionar uma conta de bate papo, a janela de gerenciador de contas não abria. O interessante é que, mesmo utilizando o atalho F4 (tecla F4 de seu teclado), nada acontecia. Para piorar a situação, o Empathy tinha o mesmo comportamento quando chamado pelo terminal, mas nenhuma mensagem de erro aparecia.

Após um breve pesquisa na internet descobri que isso acontecia porque nem todos os componentes do Empathy são instalados por padrão pelo Arch Linux. Para resolver esse problema você precisa instalar todos os componentes e dependências opcionais do Empathy, através do Pacman. Para isso, digite o seguinte comando abaixo (composto por uma longa linha de dependências a serem instaladas):

.. code-block:: bash

    $ sudo pacman -S telepathy-mission-control libcanberra  libnotify  libunique libwebkit evolution-data-server telepathy-gabble telepathy-idle telepathy-salut telepathy-haze

Após essa "atualização", seu Empathy voltará a funcionar normalmente.

Instalando Dicionário
~~~~~~~~~~~~~~~~~~~~~

Um recurso que eu aprecio muito em um Linux é a correção ortográfica, que funciona de forma global para toda a instalação. Na maioria dos aplicativos no ambiente GNOME como o Empathy, br-office e etc, essa funcionalidade é provida pelos pacotes de localização do aspell. Para instalá-lo utilize o seguinte comando:

.. code-block:: bash

    $ sudo pacman -S aspell-pt

Plugins para o GStreamer
~~~~~~~~~~~~~~~~~~~~~~~~

Provavelmente à essa altura vocês já devem ter tentado executar em suas instalações Arch, algum vídeo no formato avi – ou mesmo músicas em MP3 – e se depararam com a mensagem padrão do sistema indicando a ausência de codecs/plugins, certo?! Para resolver esse problema precisamos instalar as codecs do gstreamer. Estas codecs são largamente utilizadas por aplicações como o Totem e o Rhythmbox. Para prosseguir com essa instalação basta utilizar o seguinte comando:

.. code-block:: bash

    $ sudo pacman -S gstreamer0.10 gstreamer0.10-plugins gstreamer0.10-base gstreamer0.10-good gstreamer0.10-python gstreamer0.10-ugly

Após a instalação, você poderá ouvir suas músicas preferidas em formato MP3, assim como assistir a seus videos em diversos formatos proprietários.

Compactadores (e Descompactadores)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Outro tipo de aplicativo usado recorrentemente pelos usuários Linux são as ferramentas de compactação (e descompactação). Nos repositórios do Arch Linux você encontra diversas ferramentas de compactação (e descompactação) disponíveis. E fica à gosto do freguês qual (ou quais) utilizar. Para instalar os pacotes mais básicos no seu sistema (e que correspondem por 98% da necessidade da maioria dos usuários Linux), utilize o seguinte comando abaixo:

.. code-block:: bash

    $ sudo pacman -S tar gzip bzip2 unzip unrar p7zip

Se tiverem curiosidade, aproveitem para ler cuidadosamente o man de cada um desses aplicativos. Você conhecerá o verdadeiro poder (e as vantagens) de cada um deles.

Yaourt e o AUR
--------------

O AUR (*Arch User Repository*), é um repositório dirigido pela comunidade para usuários do Arch. Ele contém descrições de pacotes (PKGBUILDs) lhe permitem compilar um pacote de um fonte com o ``makepkg`` e depois instalar via ``pacman``. O AUR foi criado para organizar e compartilhar novos pacotes da comunidade ajudando a acelerar a inclusão dos pacotes populares. Esse recurso se tornou a porta de entrada de novas aplicações para os repositórios oficiais do Arch Linux.

O AUR possui uma proposta muito boa, pois ajuda a estreitar o relacionamento entre mantenedores da distribuição/repositórios e a comunidade. Ele também ajuda os "desenvolvedores de fim de semana" a publicar seus softwares para os usuários do Arch Linux de uma maneira mias fácil, simples e automatizada. Apesar disso, o fluxo exigido para obter um programa do AUR é um pouco dispendioso, ele exige que o usuário visite a página do `AUR`_, efetue a busca o software de interesse, baixe os arquivos de construção, construa o pacote com o comando ``makepkg -s`` e em seguida instale o arquivo ``.pkg.tar.gz`` gerado utilizando o comando ``pacman -U``.

Para automatizar todo esse processo foi criado pela `Comunidade Francesa do Arch Linux`_ um aplicativo chamado *Yaourt* (*Yet AnOther User Repository Tool*). O Yaourt engloba todas as funcionalidades do gerenciador de pacotes Pacman, além de estender sua "abrangência" ao AUR, tornando o processo de download, compilação e instalação de pacotes da comunidade, algo transparente e automatizado. A melhor parte de todo o processo é que o Yaourt utiliza a mesma sintaxe do Pacman, praticamente zerando a necessidade aprender e adaptar-se a uma nova ferramenta.

Aos interessados, mais informações sobre o AUR (e como criar um pacote para o AUR) estão disponíveis `neste artigo`_. Outro link interessante sobre o AUR pode ser encontrado no `seguinte artigo`_.

Instalando o Yaourt
~~~~~~~~~~~~~~~~~~~

Para instalar o **yaourt** é necessário inserir um novo repositório no seu Arch Linux. Para isso edite o arquivo ``/etc/pacman.conf`` com o seguinte comando:

.. code-block:: bash

    $ sudo vim /etc/pacman.conf

No final do arquivo adicione as seguintes linhas:

::

    [archlinuxfr]
    Server = http://repo.archlinux.fr/$arch

Em seguida instale os seguintes pacotes:

.. code-block:: bash

    $ sudo pacman -Sy yaourt base-devel

Pronto, o *yaourt* está pronto para ser utilizado.

Um Conjunto de Ícones
~~~~~~~~~~~~~~~~~~~~~

Na minha opinião os ícones do GNOME 3 estão ótimos, mas eu ainda acho o conjunto de ícones `Faenza`_ incríveis! Então para quem quiser testar, eles estão disponíveis pelo yaourt e pode ser instalado com o seguinte comando:

.. code-block:: bash

    $ yaourt -S faenza-icon-theme

Pronto agora temos um desktop 100% funcional e bonito para as usuários mais comuns. A partir do próximo artigo irei mostrar a instalação de aplicações mais específicas que nem todos os usuários precisam (como o inkscape, deluge, openshot, openssh e etc), um artigo voltado para impressoras e scanners HP, artigos somente sobre temas e plugins do gnome shell e um artigo sobre jogos no Arch Linux.

Até lá...

.. _último artigo: /pt/configuracao-basica-do-arch-linux-sem-dor/
.. _AUR: https://aur.archlinux.org/
.. _Comunidade Francesa do Arch Linux: http://archlinux.fr/yaourt-en#get_it
.. _neste artigo: https://wiki.archlinux.org/index.php/Arch_User_Repository_%28Portugu%C3%AAs%29
.. _seguinte artigo: https://wiki.archlinux.org/index.php/Yaourt
.. _Faenza: http://tiheum.deviantart.com/art/Faenza-Icons-173323228

