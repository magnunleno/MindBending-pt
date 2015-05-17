Hack 'n' Cast - v0.3 Introdução ao GNU/Linux
############################################
:date: 2014-07-07 01:38
:category: Hack 'n' Cast
:tags: hack 'n' cast, podcast, beta, gnu, linux, linus torvalds, tanenbaum, dennis ritchie, ken thompson, minix, kansas
:image: /images/hack-n-cast/v0.3-cover-sqr.png
:length: 49361899
:duration: 101:03
:podcast: http://archive.org/download/HNC.v0.3-Introducao-ao-GNU-Linux/HNC.v0.3-Introducao-ao-GNU-Linux.mp3
:podcastembed: http://archive.org/embed/HNC.v0.3-Introducao-ao-GNU-Linux/HNC.v0.3-Introducao-ao-GNU-Linux.mp3
:podcast_old: True
:description: O GNU/Linux foi a mola propulsora da Internet como a conhecemos hoje e, por isso, é uma peça de tecnologia fundamental pra qualquer profissional. Hoje vamos saber um pouco de sua história, entender porquê escrevemos GNU antes de Linux e discutir um pouco sobre a disputa épica entre Linus e Tanenbaum.

Olá pessoal! Na v0.3 do `Hack 'n' Cast`_ voltamos cheios de novidades! Além do `desconto nos livros da Novatec`_ agora estamos promovendo um sorteio de 2 livros (mais detalhes `aqui`_). Além disso, nesse episódio o nosso primeiro convidado, Gilson Filho, nos ajuda a falar de GNU/Linux.

.. image:: {filename}/images/hack-n-cast/v0.3-cover.png
        :target: {filename}/images/hack-n-cast/v0.3-cover.png
        :alt: v0.3 Cover
        :align: center

Sendo assim, vamos ver conceitos como: o que é o kernel, o primeiro kernel, a origem do Linux, o que é GNU, o que é MINIX, o que a Valesca Popuzuda tem a ver com tudo isso, o que é uma distribuição, tipos de distribuição, distribuições brasileiras, distribuições mais usadas e muito mais. Para não perder nenhum episódio siga-nos nas redes sociais (`Twitter`_ e `Facebook`_) ou inscreva-se (`Feed`_, `Podflix`_, `iTunes`_ e `Pocket Casts`_). Você quer colaborar com o Hack 'n' Cast? Sugira um tema, nos ajude a produzir uma pauta ou participe conosco! Entre em contato por `E-mail`_, `Facebook`_ ou `Twitter`_.

.. more

.. podcast:: HNC.v0.3-Introducao-ao-GNU-Linux
        :rss: http://feeds.feedburner.com/hack-n-cast
        :itunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846

O Sorteio
=========

A partir deste episódio estaremos promovendo um sorteio de 2 livros com o apoio da `Editora Novatec`_:

- `Descobrindo o Linux`_ (João Eriberto)
- `Shell Script Profissional`_ (Aurélio Marinho)

As regras são simples, basta curtir a `fanpage da Editora Novatec`_, a `fanpage do Hack 'n' Cast`_, estar no Brasil e pronto! O vencedor será anunciado no próximo episódio, isso quer dizer que vocês tem um mês para curtir as duas páginas.

Comunidade & Pesquisa
=====================

Uma ideia que eu já tinha ha algum tempo, mas o Thiago Perrotta me fez levá-la a um novo patamar, é a criação de uma comunidade para dar suporte ao Hack 'n' Cast. A ideia é termos uma forma de nos aproximarmos dos ouvintes (por meio de envio de notícias, sugestões, ideias, convidados e etc) e reunir pessoas interessadas em contribuir com o Hack 'n' Cast (gravar conosco).

Entretanto não gostaríamos de ditar uma ferramenta, deixaremos para vocês escolherem. Para isso basta responder esse formulário online: `1ª Pesquisa Hack 'n' Cast`_

Introdução
==========

Desde o seu surgimento, a Internet era algo para poucos e voltado para uma minoria: universidades, centros de pesquisas, governo e exército. Isto devido ao alto custo e complexidade de se manter (e de se utilizar) um sistema conectado e funcional. Entretanto, com o advento da linguagem HTML e do protocolo HTTP um desses problemas estava sanado. Entretanto, custear a licença de servidores para prover conteúdo ainda era algo inviável para reles mortais. Até que uma revolução começou, seu nome: GNU/Linux

Componentes de Um Sistema Operacional
-------------------------------------

Antes de tratarmos do que é GNU/Linux é importante explicar o que compõe um sistema operacional.  Um sistema operacional é composto por um **núcleo** e por **ferramentas/componentes** que se utilizam do núcleo:

Um núcleo (kernel)
        É responsável por realizar toda a troca de informações entre a parte
        física da máquina (hardware) e a parte lógica (software). Isto é, o
        kernel realizar operações como leitura e escrita de arquivos,
        comunicação de redes, gerencia de processos e etc, ele é responsável
        pelos conceitos de mais baixo nível, por exemplo, ele não tem visão de
        que tipo de arquivo (imagem, vídeo e etc) ele está salvando, para ele é
        apenas uma sequencia de bits.
Ferramentas/componentes 
        Responsáveis por conceitos mais abstratos e operações mais lógicas como
        implementar protocolos, sistemas de arquivos, interfaces de comunicação
        com o usuário e etc.

Estes dois componentes vivem em mutualismo, para nós humanos de nada serviria um kernel sem as ferramentas e, sem o kernel, as ferramentas não podem desempenhar suas funções.

Uma boa abstração para se compreender esse conceito é imaginar o kernel como um motor de carro e os outros componentes como as rodas, carroceria, sistema de descarga, sistema de direção, pedais e etc.

GNU/Linux
=========

O Projeto GNU (acrônimo recursivo que quer dizer "*Gnu is not Unix*") foi criado por Richard Stallman com o intuito de implementar uma versão livre do (na época) famoso sistema operacional Unix utilizado em sua universidade.

Uma vez que o Unix e suas diversas ferramentas ainda estava em uso, ele resolveu substituir o Unix da maneira mais transparente e imperceptível possível, trocando seus componentes/ferramentas mais externos primeiro. Uma vez concluída esta troca, então seria a hora de trocar o núcleo do sistema operacional.

Exemplos de ferramentas GNU:

- o compilador GCC;
- bibliotecas básicas como a glib;
- o shell Bash, diversos utilitários da linha de comando (grep, find, history, ls, cd e etc);
- e ambientes gráficos como o Gnome.

Antes que Richard Stallman pudesse iniciar a troca do kernel surgiu o Linux, um kernel livre implementado pelo finlandês Linus Torvalds. Seguindo o exemplo de Linus (com o compilador GCC e o bash), em pouco tempo a comunidade GNU portou toda a suite de ferramentas do projeto GNU para o kernel Linux, o que se tornou um enorme sucesso e hoje é conhecido como GNU/Linux. Claro que isso só foi possível uma vez que o Linux também foi construído seguindo os padrões POSIX.

Desde o início Linus teve o intuito de criar um sistema livre e gratuito para uso pessoal. O Linux teve como "inspiração" primordial o MINIX (Mini UNIX), kernel puramente acadêmico implementado pelo professor E. Tanenbaum. Linus sempre descreveu o kernel Linux como "um MINIX melhor que o MINIX".

Em 25 de Agosto de 1991 Linus (com apenas 21 anos) enviou a seguinte mensagem à *comp.os.minix*:

        **Assunto:** O que você mais gostaria de ver no MINIX?

        Olá a todos que estão usando MINIX

        Eu estou fazendo um sistema operacional livre (é apenas um hobby, não
        será grande e profissional como o GNU) para AT 386(486) e demais
        clones. Está sendo desenvolvido desde abril e está quase pronto.
        Gostaria de receber qualquer feedback sobre o que as pessoas gostam/não
        gostam no MINIX, uma vez que o meu SO se parece um pouco com ele (mesmo
        layout físico de sistema de arquivos (devido a razões práticas) entre
        outras coisas.

        No momento eu o portei para bash(1.08) e gcc(1.40), e as coisas parecem
        funcionar. Isso implica que irei conseguir algo prático dentro de
        poucos meses e gostaria de saber quais características a maioria das
        pessoas gostaria que ele tivesse. Quaisquer sugestões são bem-vindas,
        mas não prometo que eu vá implementá-las :-)

        PS. Sim — ele não tem nenhum código MINIX, e possui um fs multitarefa.
        Ele NÃO é portável (usa troca de contexto 386, etc), e provavelmente
        nunca será compatível com nada além de discos rígidos AT, uma vez que
        isso é tudo o que eu tenho :-(.

        .. class:: text-right

                *— Linus Torvalds*

A característica aberta do GNU/Linux incentivou sua adoção por agentes de governos mundiais que prezam por segurança e adaptabilidade, como: NASA, NSA, Forças Armadas (Exército, Marinha e Aeronáutica) e governos em geral (alguns poucos países). Já sua  característica gratuita e suas ferramentas poderosas, foi propício para o uso e desenvolvimento da Internet como a conhecemos hoje. Sem o GNU/Linux a internet não seria acessível a todos a um baixo custo.

Vídeos sobre a história do GNU/Linux:

- `How Linux is Build`_ - Linux Foundation
- `Linux History`_ - Linux Foundation
- `The Code Linux`_ - Documentário
- `Revolution OS`_ - Documentário

O crescimento do Linux
----------------------

Se você diz que o GNU/Linux é um SO pouco utilizado, repense sua frase: 

- 850.000 celulares com Android são ativados todos os dias;
- 700.000 *Smart* TVs são vendidas todos os dias com GNU/Linux;
- 8 de 10 transações financeiras em todos os bancos do mundo são executadas em sistemas GNU/Linux;
- 9 de 10 supercomputadores rodam GNU/Linux;
- 58% a 78% de todos os sites da internet rodam GNU/Linux;
- Seu *access point* Wi-Fi roda GNU/Linux, assim como seu modem;
- Diversos ativos de rede são baseados em GNU/Linux, como roteadores, *switches*, *bridges*, balanceadores de carga, dentre outros;
- O GNU/Linux está presente em sistemas embarcados simples (como esteiras, bicicletas ergométricas, câmeras fotográficas e etc) e complexos (sistemas de controles de mísseis militares, controladores de fissão nuclear, sistemas elétricos automotivos e etc);

.. image:: {filename}/images/quadrinhos/linux-free-zone.png
        :target: http://www.icanbarelydraw.com/comic/1043
        :alt: Linux Free Zone
        :align: center

O kernel Linux se tornou o maior projeto e com a maior equipe de desenvolvimento do mundo. Dizer que o GNU/Linux é apenas outros sistema operacional é o mesmo que dizer que a Internet é apenas outra rede.

Relação entre GNU e Linux
-------------------------

Dada esta relação de mutualismo, a comunidade do Projeto GNU se sente ofendida por não ser creditada quando todos se referem ao sistema operacional apenas como "Linux". Muitos acham que é exagero, e que temos que nos dar por satisfeito pelo sucesso do GNU/Linux. Já outros, acham importante a citação, para que todos conheçam o projeto GNU, que é muito mais que apenas uma suite de ferramentas e engloba também uma filosofia. Para entender melhor, leia o texto da *Free Software Foundation* "`Por que GNU/Linux`_".

Além disso, após um estudo constatou-se que o kernel Linux compunha apenas 3% do código fonte utilizado para construir um distribuição GNU/Linux, enquanto o código do sistema GNU eram expressivos 28%.

Distribuições
-------------

O Linux pode ser distribuído livremente, você mesmo pode gravar um CD com o Linux e mais alguns programas e vendê-lo para quem se interessar.  Isto é o que chamamos de "distribuição". A única restrição é que você não pode estabelecer nenhum tipo de restrição de uso.

Você pode cobrar:

- pela gravação do CD;
- pelos manuais;
- pelo suporte técnico;
- mas não pelo software e seus direitos;

Existem `inúmeras`_ `distribuições`_ Linux, as principais são:

- Red Hat;
- Slackware;
- Debian;
- SuSE;
- Linux Mint;
- Ubuntu;
- Arch Linux;
- Fedora;

Para todas estas o kernel Linux é o mesmo, porém, cada distribuição vem com um conjunto diferente de aplicativos, certas facilidades, um instalador gráfico, pré configurações e etc. Isto é o que diferencia uma distribuição de outra.

Algumas distribuições são mais voltadas para o servidor como, Debian, Red Hat, Slackware, Ubuntu Server e OpenSUSE. Já outras são voltadas para o usuário doméstico como, Ubuntu, OpenSUSE, Fedora, Mandriva e Linux Mint.

Ao longo da história tivemos duas distribuições brasileiras relevantes: Kurumin e Conectiva

Para testar as distribuições você tem três opções: Live CDs, Virtual Machines (VMWare e VirtualBox) ou Dual Boot.

Links
=====

- `Brackets`_;
- `Lista de IDEs`_;
- `Página criada pelo "Davi, o Hacker"`_
- `Alan Moore anuncia app open source para quadrinhos`_
- `ZapZap tem código fonte liberado após polêmica sobre legalidade`_
- `Transforme o LED de Num/Scroll/Caps do seu teclado em um Indicador de uso de disco (Thinkpad)`_
- `Google Chromecast`_
- `Qual distribuição mais adequada para você?`_

Aprenda Mais
============

**Online:**

- `EdX - Introduction to Linux`_;
- `Guia Foca GNU/Linux online`_ (ou para Download);
- `Linux, Guia Prático`_ - Carlos E. Morimoto;

**Livros:**

- `Descobrindo o Linux - 3ª Edição`_ (Eriberto, João);
- `Linux - Guia do Administrado de Sistemas`_ (E. Ferreira, Rubem);
- `Certificação Linux LPI`_ (Haeder, Adam; Pessanha, Bruno Gomes; Schneiter, Stephen Addison);

.. class:: panel-body bg-info

        Na compra de qualquer livro na Novatec utilize o código **MINDBENDING** para conseguir 20% de desconto.

Trilha Sonora
=============

A trilha sonora de hoje é uma homenagem à banda Kansas, e foi escolhida pelo Gilson Filho:

- Death of Mother Nature Suite (1974 - Kansas)
- Down the Road (1975 - Song for America)
- Carry On Wayward Son (1976 - Leftoverture)
- Child of Innocence (1975 - Masque)
- The Wall (1976 - Leftoverture)
- Lightning's Hand (1977 - Point of Know Return)
- On the Other Side (1979 - Monolith)
- Angels Have Fallen (1979 - Monolith)
- Stay Out of Trouble (1979 - Monolith)
- Dust in the Wind (1977 - Point of Know Return)
- Relentless (1980 - Audio-Visions)
- Borderline (1982 - Vinyl Confessions)
- Fair Exchange (1982 - Vinyl Confessions)
- Mainstream (1983 - Drastic Measures)
- Silhouettes in Disguise (1986 - Power)
- Freaks Of Nature (1995 - Freaks of Nature)
- Grand Fun Alley (2000 - Somewhere to Elsewhere)



Licença
=======

O Hack 'n' Cast é distribuído sobre a licença `Creative Commons Attribution-ShareAlike 4.0 International`_ (CC BY-SA 4.0). Você é livre para compartilhar, copiar, redistribuir (em qualquer mídia ou formato), adaptar, remixar transformar ou ampliar esse material, contato que sejam mantidas as atribuições e os autores sejam devidamente citados e que esta mesma licença seja utilizada nos trabalhos derivados.

.. _Creative Commons Attribution-ShareAlike 4.0 International: http://creativecommons.org/licenses/by-sa/4.0/
.. _Hack 'n' Cast: /pt/sobre-hack-n-cast
.. _aqui: #o-sorteio
.. _desconto nos livros da Novatec: #aprenda-mais
.. _Descobrindo o Linux: http://www.novatec.com.br/livros/linux3/
.. _Shell Script Profissional: http://www.novatec.com.br/livros/shellscript/
.. _fanpage da Editora Novatec: https://www.facebook.com/novatec
.. _fanpage do Hack 'n' Cast: https://www.facebook.com/hackncast
.. _1ª Pesquisa Hack 'n' Cast: https://docs.google.com/forms/d/1mvwrBpPfMHvvNzEBGHSxVxoQNNvzpywHerL4cnpbtDc/viewform

.. _Editora Novatec: http://www.novatec.com.br/
.. _inúmeras: http://distrowatch.com/search.php?status=All
.. _distribuições: http://en.wikipedia.org/wiki/List_of_Linux_distributions

.. _Por que GNU/Linux: http://www.gnu.org/gnu/why-gnu-linux.pt-br.html
.. _Alan Moore anuncia app open source para quadrinhos: http://meiobit.com/288626/ocastastudios-electricomics-app-para-quadrinhos-apoiado-por-alan-moore/
.. _ZapZap tem código fonte liberado após polêmica sobre legalidade: http://www.techtudo.com.br/noticias/noticia/2014/06/zapzap-tem-codigo-fonte-liberado-apos-polemica-sobre-legalidade-entenda.html
.. _Transforme o LED de Num/Scroll/Caps do seu teclado em um Indicador de uso de disco (Thinkpad): https://github.com/MeanEYE/Disk-Indicator
.. _Google Chromecast: http://www.google.com/intl/pt-BR/chrome/devices/chromecast/
.. _Qual distribuição mais adequada para você?: http://www.zegeniestudios.net/ldc/index.php?lang=pt-br

.. _How Linux is Build: https://www.youtube.com/watch?v=yVpbFMhOAwE
.. _Linux History: https://www.youtube.com/watch?v=5ocq6_3-nEw
.. _The Code Linux: https://www.youtube.com/watch?v=YPqVO2L3K7M
.. _Revolution OS: https://www.youtube.com/watch?v=plMxWpXhqig
.. _EdX - Introduction to Linux: https://www.edx.org/course/linuxfoundationx/linuxfoundationx-lfs101x-introduction-1621
.. _Guia Foca GNU/Linux online: http://www.guiafoca.org/
.. _Linux, Guia Prático: http://www.hardware.com.br/livros/linux/

.. Social
.. _E-mail: mailto: hackncast@gmail.com
.. _Twitter: http://twitter.com/hackncast
.. _Facebook: http://facebook.com/hackncast
.. _Feed: http://feeds.feedburner.com/hack-n-cast
.. _Podflix: http://podflix.com.br/hackncast/
.. _iTunes: https://itunes.apple.com/br/podcast/hack-n-cast/id884916846?l=en
.. _Pocket Casts: http://pcasts.in/hackncast

.. Livros
.. _Descobrindo o Linux - 3ª Edição: http://www.submarino.com.br/produto/111414273/descobrindo-o-linux-entenda-o-sistema-operacional-gnu-linux?epar=lomadee&opn=AFLNOVOSUB&utm_campaign=lomadee&utm_medium=lomadee&utm_source=lomadee
.. _Linux - Guia do Administrado de Sistemas: http://www.submarino.com.br/produto/6774464/livro-linux-guia-do-administrador-do-sistema?epar=lomadee&opn=AFLNOVOSUB&utm_campaign=lomadee&utm_medium=lomadee&utm_source=lomadee
.. _Certificação Linux LPI: http://www.livrariasaraiva.com.br/produto/4081171?utm_source=lomadee&utm_campaign=lomadee&utm_medium=lomadee&PAC_ID=30393


.. _Brackets: http://brackets.io/
.. _Lista de IDEs: https://wiki.archlinux.org/index.php/List_of_applications/Utilities#Integrated_development_environments
.. _Página criada pelo "Davi, o Hacker": http://www.inf.pucrs.br/~pinho/LaproI/IntroC/IntroC.htm

