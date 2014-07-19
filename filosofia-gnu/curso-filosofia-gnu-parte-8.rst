Curso de Filosofia GNU - Parte 8
################################
:date: 2014-04-28 10:13
:category: Filosofia GNU
:tags: curso, filosofia gnu, cdtc, richard stallman, FSF, hurd, linux
:image: /images/The_GNU_logo-300x293.png
:series: Curso de Filosofia GNU
:description: Neste texto Stallman deixa claro o motivo pelo qual a não citação do GNU antes do Linux o irrita tanto.

No penúltimo texto do `Curso de Filosofia GNU`_ "Linux e o Sistema GNU" o autor, Richard Stallman, retoma o conflito "Sistema GNU" e "Sistema Linux". Para muitos pode soar como purismo e minúcia, mas para Stallman é assunto sério. Acredito que depois de lerem este texto todos vão entender por que sempre uso o termo GNU/Linux neste site.

.. image:: {filename}/images/filosofia-gnu/gnu-linux.png
        :target: {filename}/images/filosofia-gnu/gnu-linux.png
        :alt: GNU/Linux
        :align: center

Lembrando que este é um conteúdo livre obtido no `CDTC`_.

.. more

8. Linux e o Sistema GNU
------------------------

.. class:: text-right text-warning

        -- Escrito por Richard Stallman

O projeto GNU começou 12 anos atrás com o objetivo de desenvolver um sistema operacional *Unix-like* totalmente livre. "Livre" se refere à liberdade, e não ao preço; significa que você está livre para executar, distribuir, estudar, mudar e melhorar o software.

Um sistema *Unix-like* consiste de muitos programas diferentes. Nós achamos alguns componentes já disponíveis como softwares livres -- por exemplo, X Window e TeX. Obtemos outros componentes ajudando a convencer seus desenvolvedores a tornarem eles livres -- por exemplo, o *Berkeley Network Utilities*. Outros componentes nós escrevemos especificamente para o GNU -- por exemplo, GNU Emacs, o compilador GNU C, a GNU C *library*, Bash e Ghostscript. Os componentes desta última categoria são "software GNU". O sistema GNU consiste de todas as três categorias reunidas.

O projeto GNU não é somente desenvolvimento e distribuição de alguns softwares livres úteis. O coração do projeto GNU é uma ideia: que software deve ser livre, e que a liberdade do usuário vale a pena ser defendida. Se as pessoas têm liberdade mas não a apreciam conscientemente, não irão mantê-la por muito tempo. Se queremos que a liberdade dure, precisamos chamar a atenção das pessoas para a liberdade que elas têm em programas livres.

O método do projeto GNU é que programas livres e a ideia da liberdade dos usuários ajudam-se mutuamente. Nós desenvolvemos software GNU, e conforme as pessoas encontrem programas GNU ou o sistema GNU e comecem a usá-los, elas também pensam sobre a filosofia GNU. O software mostra que a ideia funciona na prática. Algumas destas pessoas acabam concordando com a ideia, e então escrevem mais programas livres. Então, o software carrega a ideia, dissemina a ideia e cresce da ideia.

Em 1992, nós encontramos ou criamos todos os componentes principais do sistema exceto o *kernel*, que nós estávamos escrevendo (este *kernel* consiste do *microkernel* Mach mais o GNU HURD). Atualmente ele está funcionando, mas não está preparado para os usuários. Uma versão alfa deverá estar pronta em breve.

Então o *kernel* do Linux tornou-se disponível. Linux é um *kernel* livre escrito por Linus Torvalds compatível com o Unix. Ele não foi escrito para o projeto GNU, mas o Linux e o quase completo sistema GNU fizeram uma combinação útil. Esta combinação disponibilizou todos os principais componentes de um sistema operacional compatível com o Unix, e, com algum trabalho, as pessoas o tornaram um sistema funcional. Foi um sistema GNU variante, baseado no *kernel* do Linux.

Ironicamente, a popularidade destes sistemas desmerece nosso método de comunicar a ideia GNU para as pessoas que usam GNU. Estes sistemas são praticamente iguais ao sistema GNU -- a principal diferença é a escolha do *kernel*. Porém as pessoas normalmente os chamam de "sistemas Linux" (Linux *systems*). A primeira impressão que se tem é a de que um "sistema Linux" soa como algo completamente diferente de "sistema GNU", e é isto que a maioria dos usuários pensam que acontece.

A maioria das introduções para o "sistema Linux" reconhece o papel desempenhado pelos componentes de software GNU. Mas elas não dizem que o sistema como um todo é uma variante do sistema GNU que o projeto GNU vem compondo por uma década. Elas não dizem que o objetivo de um sistema *Unix-like* livre como este veio do projeto GNU. Daí a maioria dos usuários não saber estas coisas.

Como os seres humanos tendem a corrigir as suas primeiras impressões menos do que as informações subsequentes tentam dizer-lhes, estes usuários que depois aprendem sobre a relação entre estes sistemas e o projeto GNU ainda geralmente o subestima.

Isto faz com que muitos usuários se identifiquem como uma comunidade separada de "usuários de Linux", distinta da comunidade de usuários GNU. Eles usam todos os softwares GNU; de fato, eles usam quase todo o sistema GNU; mas eles não pensam neles como usuários GNU, e frequentemente não pensam que a filosofia GNU está relacionada a eles.

Isto leva a outros problemas também -- mesmo dificultando cooperação com a manutenção de programas. Normalmente quando usuários mudam um programa GNU para fazer ele funcionar melhor em um sistema específico, eles mandam a mudança para o mantenedor do programa; então eles trabalham com o mantenedor explicando a mudança, perguntando por ela, e às vezes reescrevendo-a para manter a coerência e manutenibilidade do pacote, para ter o *patch* instalado.

Mas as pessoas que pensam nelas como "usuários Linux" tendem a lançar uma versão "*Linux-only*" do programa GNU, e consideram o trabalho terminado. Nós queremos cada e todos os programas GNU que funcionem "*out of the box*" em sistemas baseados em Linux; mas se os usuários não ajudarem, este objetivo se torna muito mais difícil de atingir.

Como deve o projeto GNU lidar com este problema? O que nós devemos fazer agora para disseminar a ideia de que a liberdade para os usuários de computador é importante?

Nós devemos continuar a falar sobre a liberdade de compartilhar e modificar software -- e ensinar outros usuários o valor destas liberdades. Se nós nos beneficiamos por ter um sistema operacional livre, faz sentido para nós pensar em preservar estas liberdades por um longo tempo. Se nós nos beneficiamos por ter uma variedade de software livres, faz sentido pensar sobre encorajar outras pessoas a escrever mais software livre, em vez de software proprietário.

Nós não devemos aceitar a ideia de duas comunidades separadas para GNU e Linux. Ao contrário, devemos disseminar o entendimento de que "sistemas Linux" são variantes do sistema GNU, e que os usuários destes sistemas são tanto usuários GNU como usuários Linux (usuários do *kernel* do Linux). Usuários que têm conhecimento disto irão naturalmente dar uma olhada na filosofia GNU que fez estes sistemas existirem.

Eu escrevi este artigo como um meio de fazer isto. Outra maneira é usar os termos "sistema GNU baseado em Linux (*Linux-based* GNU *system*)" ou "sistema GNU/Linux (GNU/Linux *system*)", em vez de "sistema Linux", quando você escreve sobre ou menciona este sistema.

.. class:: text-right text-muted

        Copyright 1996 Richard Stallman


Créditos
--------

O material foi desenvolvido por Djalma Valois Filho e é o resultado de uma compilação das duvidas mais usuais que surgiram ao longo das inúmeras palestras apresentadas desde o ano 2000 pelo CIPSGA - Comitê de Incentivo a Produção do Software GNU e Alternativo em todo Brasil.

Todo o conteúdo encontrado neste curso é oriundo dos textos publicados pela FSF, bem como outros textos publicados pelo CIPSGA até a presente data. Críticas e sugestões construtivas são bem vindas a qualquer tempo, podendo ser enviadas para *email [at] dvalois [dot] net*.

Texto traduzido por Erik Kohler.

.. _Erik Kohler: http://www.geocities.com/CollegePark/Union/3590/linuxgnu.html
.. _CIPSGA: http://www.cipsga.org.br/sections.php?op=viewarticle&artid=49
.. _Curso de Filosofia GNU: /pt/series/curso-de-filosofia-gnu
.. _CDTC: http://cursos.cdtc.org.br/
