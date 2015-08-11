D1X-Rebirth no Arch e no Ubuntu
###############################
:date: 2011-07-25 09:00
:category: Games
:tags: arch, d1x-rebirth, dependências, descent, jogos, ubuntu, yaourt
:image: /images/Glowing_ball.jpg

Muitos podem discordar, mas os jogos de hoje em dia simplesmente não são tão bons quanto os de antigamente. Sim, eu sou "velho", joguei em consoles com 8 bits, utilizei `disquetes 5¼`_ para armazenar dados, o `ARJ`_ para descompactar e como sistema operacional utilizava o MS-DOS.  Talvez seja por isso que eu acho o "ambiente" do terminal aconchegante.  Muitos de você devem achar inconcebível um jogo somente com 16 cores, mas era esse o auge da tecnologia que eu tinha acesso durante uma parte da minha infância. Lembro até hoje da revolução que foi o mouse e os jogos "point-and-click".

.. image:: {filename}/images/descent11.png
        :target: {filename}/images/descent11.png
        :align: center
        :alt: Descent 1 Banner

Ainda hoje jogo esses jogos antigos com uma mãozinha do `DosBox`_ e meus backups antigos (mas isso é assunto para outro artigo). Alguns desses jogos antigos se tornaram `abandonware`_ ou tem o código fonte liberado sob alguma licença. Quando este último acontece geralmente a comunidade de fãs se junta com a comunidade Open Source/Software Livre e escrever um `port`_ desse jogo para o GNU/Linux e outros sistemas operacionais.

.. more

Alguns jogos que servem de exemplo são, Abuse, Wolf 3D, Doom, Doom 2, Duke Nukem 3D, entre outros. Muitos desses receberam inclusive melhorias nos gráficos e nos controles (chegando a suportar gamepads) e alguns passaram a suportar jogos multiplayer sobre protocolos mais atuais como o TCP e o UDP (na época muitas empresas apostavam no IPX/SPX).

Descent no Arch Linux
---------------------

Esses dias encontrei meu CD do Descent 1 e resolvi testar o port (com melhoramentos) chamado `D1X-Rebirth`_. Bastou uma simples busca no Yaourt para ficar mais empolgado:

.. code-block:: bash

    $ yaourt -Ss d1x

Em seguida uma simples instalação:

.. code-block:: bash

    $ yaourt -S d1x-rebirth

Depois copiei os arquivos \*.PIG e \*.HOG para a pasta ~/.d1x-rebirth (conforme instruído durante o processo de instalação do yaourt). O processo completo levou menos de 5 minutos.

Em seguida executei o jogo:

.. figure:: {filename}/images/descent.png
        :align: center
        :target: {filename}/images/descent.png
        :alt: D1X-Rebirth (Descent)

        D1X-Rebirth (Descent)

Descent no Ubuntu 10.10
-----------------------

Meu irmão mais novo ficou impressionado com o jogo (mesmo sendo uma tecnologia de 1995). Então resolvi instalar o jogo para ele no seu Ubuntu 10.10. Para minha surpresa não encontrei o jogo nos repositórios.  Procurei pela internet se havia algum PPA ou pacote pre-compilado (.deb) mas também não encontrei. A solução foi compilar o programa na mão. Após alguns minutos de tentativas, erros e instalações de bibliotecas consegui compilar o jogo. Ao final fiz o levantamento das bibliotecas necessárias para esse jogo:

-  gcc;
-  scons;
-  libsdl1.2-dev;
-  libphysfs-dev;
-  libsdl-mixer1.2-dev;
-  libglu1-mesa-dev.

Estas dependências foram instaladas com a seguinte linhas de comando:

.. code-block:: bash

    $ sudo apt-get install gcc scons libsdl1.2-dev libphysfs-dev libsdl-mixer1.2-dev libglu1-mesa-dev

Após isso bastou executar os seguintes comandos para compilar e instalar o jogo D1X-Rebirth:

.. code-block:: bash

    $ sudo scons && scons install

Ao final, realizei o mesmo processo de cópia dos arquivos \*.PIG e \*.HOG para a pasta ~/.d1x-rebirth mas tive um pequeno contratempo, tive que criar manualmente o arquivo descent.desktop (este arquivo é necessário para que o jogo esteja disponível no menu do Gnome) uma vez que o jogo compilado não gerou esses arquivos para mim. O processo completo durou pouco mais de 30 minutos.

Arch vs. Ubuntu
---------------

Agora após essa descrição minuciosa do processo de instalação em ambos os sistemas, levanto a mesma questão que eu levantei no meu artigo de `atualização do Firefox no Arch Linux`_: Por que até hoje reina a falácia de que o Ubuntu é mais amigável que o GNU/Linux mais amigavel?

Entendo que o Ubuntu é muito amigável em alguns pontos, mas em outros (principalmente quando o assunto é instalação de programas extras) o Arch é extremamente superior. Então vamos parar com essa difamação de que o o Arch Linux é uma distribuição difícil de usar e não indicada para iniciantes, OK?!

E vocês leitores, qual a "facilidade" que mais te agrada no Arch Linux?

.. _disquetes 5¼: http://pt.wikipedia.org/wiki/Disquete#Disquete_de_5.221.2F4
.. _ARJ: http://pt.wikipedia.org/wiki/ARJ
.. _DosBox: http://www.dosbox.com/
.. _abandonware: http://en.wikipedia.org/wiki/Abandonware
.. _port: http://en.wikipedia.org/wiki/Porting
.. _D1X-Rebirth: http://www.dxx-rebirth.com/
.. _|image3|: {filename}/images/descent.png
.. _atualização do Firefox no Arch Linux: /pt/atualizand-o-firefox-5-no-arch-linux/

