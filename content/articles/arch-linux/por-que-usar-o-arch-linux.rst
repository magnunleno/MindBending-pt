Por Que Usar o Arch Linux?
##########################
:date: 2011-06-26 18:50
:category: Arch Linux
:tags: arch
:image: /images/archlogo.png

Essa pergunta é mais profunda do que se pode imaginar. E ela pode ser traduzida por: O quão **Livre** você deseja ser? Se você é um usuário GNU/Linux que apoia com sinceridade a Filosofia GNU, e preza por toda a Liberdade que o Software Livre de Código Aberto pode lhe proporcionar, você é um usuário GNU/Linux consciente. Sabemos que o GNU/Linux é Livre o suficiente para lhe oferecer a cada dia, não somente uma miríade de Software Livre, mas também uma infinidade de distribuições GNU/Linux à sua disposição.

.. figure:: {filename}/images/arch-linux-logo2.png
        :target: {filename}/images/arch-linux-logo2.png
        :align: center
        :alt: Arch Linux Logo

        Arch Linux Logo

O Mais Alto Grau de Liberdade
-----------------------------

Independente do fato de todas as distribuições serem um tipo de GNU/Linux é possível observar que cada uma oferece um nível variado de liberdade. Porém, na hora de escolher uma distribuição, se sua vontade é abraçar toda a Liberdade disponível no mundo GNU/Linux, você tem poucas opções e uma delas é o Arch Linux.

.. more

Sabemos que a Liberdade de software possui quatro pilares básicos:

-  A liberdade de executar o software, para qualquer uso;
-  A liberdade de estudar o funcionamento de um programa e de adaptá-lo
   às próprias necessidades;
-  A liberdade de redistribuir cópias do software e;
-  A liberdade de melhorar o programa e de tornar as modificações
   públicas de modo que a comunidade inteira beneficie da melhoria.

Uma distribuição GNU/Linux é um passo à frente desses quatro princípios básicos. Uma distribuição representa um sistema automatizado que tenta lhe oferecer toda Liberdade da forma mais fácil possível, entregando para qualquer usuário GNU/Linux, independente de seu nível de conhecimento, um sistema operacional recheado com todos os programas necessários para o dia-à-dia. Tudo isso pronto para uso após instalação do sistema em seu computador. Mas qual o grau de Liberdade que essas distribuições GNU/Linux realmente oferecem para seus usuários?

Facilidade com Restrição de Liberdade? Não, Obrigado!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Atualmente, muitas das distribuições GNU/Linux tem oferecido um grau crescente de facilidade de instalação e uso do seu sistema para seus usuários. Porém, em troca de toda essa facilidade, muitos deixam de perceber que uma grande fatia de sua Liberdade original está sendo retida ao ter que aceitar um grupo pré-definido de software composto por ambiente gráfico, softwares diversos, configuração e design.

Quantos de nos, após instalar uma distribuição, percebeu que não precisa de metade dos programas instalados? Ou que o design da interface/tema não o agrada? Isso não ocorre quando você usa o Arch, porque após a instalação básica você terá que escolher cada pacote que será instalado no seu novo sistema. Isso parece trabalhoso, mas se torna até divertido e, ao final, gratificante pois, este é o "seu" Arch Linux.

Liberdade no Desenvolvimento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Além de todas essas liberdades, existe algo que eu prezo muito no Arch (e em algumas outras distribuições): ser mantido por uma comunidade.  Para muitos isso pode ser surpresa, mas por trás de algumas distribuições existem empresas e/ou corporações. Não duvido da boa intenção de algumas empresas/corporações, muitas delas fazem um excelente trabalho, mas todos sabemos qual equipe de desenvolvimento será mandada embora quando "o cinto apertar".

O desenvolvimento do Arch Linux é comandado Aaron Griffin e seu time de desenvolvedores, consequentemente não existe "corporativismo" ou interesses comerciais por traz dele. Muitos vão alegar que o apoio de uma empresa, como a Canonical, é fundamental para manter um ritmo de desenvolvimento e o investimento em divulgação e parcerias. Mas eu tenho um certo receio das "clausulas contratuais", pode ser bobeira, mas me sinto mais seguro em uma distribuição "pura": mantida, dirigida e desenvolvida por uma comunidade e suas doações.

Somente Liberdade?
------------------

Claro que esse não é o único motivo para se usar o Arch Linux. Além da liberdade total, o Arch me oferece uma **leveza**, **estabilidade** e **"atualidade"** que eu não havia encontrado em outras distribuições, isso porque ele é uma distribuição *rolling release* **otimizada** para a minha plataforma (x86). Um bom exemplo da facilidade que uma *rolling release* oferece, pode ser constatada no meu último artigo sobre a `atualização do Firefox 5`_.

Pra que utilizar diversos "canais de software não oficiais" e correr o risco de ter seus sistema "quebrado" por incompatibilidade de pacotes, se eu posso utilizar uma distribuição que inclui rapidamente todos os lançamentos recentes (e testados) em seus repositórios oficiais?

O exemplo do Firefox me leva a outra vantagem consagrada no Arch Linux: **pacman**. Ao passear nos fóruns do Arch é possível ler, mais de uma vez, que "possivelmente" o pacman é um dos grandes responsáveis pelo sucesso do Arch Linux, pois ele é um gerenciador de pacotes extremamente rápido, robusto o simples de se usar.

É verdade que nem todos os programas necessários podem ser encontrados nos repositórios oficiais, mas para isso existe o **AUR**. O AUR é um repositório mantido pela comunidade do Arch. Você (isso mesmo, você usuário comum) que deseja contribuir pode incluir um pacote no AUR que, caso ele seja bem votado, posteriormente será incluído no repositório oficial do Arch. E para os aficionados por linha de comando, foram criadas as ferramentas ***yaourt*** e o ***aurvote*** que auxiliam e automatizam o processo de instalação e votação de pacotes pelo AUR. Eu vejo o AUR como uma ferramente única que aproxima os desenvolvedores da comunidade de usuários. Quer um bom exemplo disso? Eu sou um desenvolvedor de fim de semana e (na época que desenvolvia para Debian) criei um programa chamado USBManager, imaginem minha surpresa ao ver isto há alguns dias:

.. code-block:: bash

    $ yaourt -Ss usbmanager
     aur/usbmanager 1.0.0-1 (13)
     An USB storage management interface.

Após isso, afirmo sem sombra de dúvidas que o AUR é uma ferramenta valiosa para desenvolveres e usuários, facilitando a entrega de uma enorme gama de softwares. Minha "aparição" no AUR me leva a outro ponto: O Arch Linux **se importa com seus usuários**! Digo isso por experiência própria, como pode ser visto `nesse meu artigo`_. Diferente de outras distribuições, o Arch tenta manter contato com os usuários, através de um `fórum oficial`_, de `agregadores do tipo "Planeta"`_, do `portal de notícias`_, do próprio `AUR`_ (que já foi citado) e com uma `wiki completa e bem detalhada`_, que é referência mesmo para os usuários GNU/Linux que adotam outras distribuições.

Além de todas essas vantagens, o Arch Linux possui algo similar a um **código de conduta** - `The Arch Way`_ - ao qual me identifiquei muito, inclusive me lembra o `Zen of Python`_.

Por que não o Arch
------------------

Este é um exercício mental que eu acho muito valioso nesses casos, uma **anti-pergunta**. Ao me perguntar "Por que não usar o Arch Linux?" a única resposta que me ocorre é definida em uma única palavra: **comodismo**. O comodismo faz com que o usuário se acostume com a sua ausência de liberdade e todos os outros problemas pois, temem a "dor" do processo de mudança e adaptação a uma nova realidade.

Sair da "**zona de conforto**" é um ótimo exercício para manter sua mente afiada e o ceticismo bem longe. Arrisco afirmar que a pior prisão é aquela que o próprio usuário cria, tornando-o cego para qualquer vantagem que uma mudança venha a oferecer.

E **você**, caro leitor, por que você usa o Arch Linux? Para aqueles que não usam (me arrisco) a propor o **desafio** de responder a minha anti-pergunta (por que não usar o Arch) com algo que não seja comodismo.  Caso consigam, edito a seção e incluo a resposta.

.. _|image1|: {filename}/images/arch-linux-logo2.png
.. _atualização do Firefox 5: /pt/atualizand-o-firefox-5-no-arch-linux/
.. _nesse meu artigo: /pt/ola-planeta-arch-linux-brasil/
.. _fórum oficial: http://forum.archlinux-br.org/
.. _agregadores do tipo "Planeta": http://planeta.archlinux-br.org/
.. _portal de notícias: http://archlinux-br.org/
.. _AUR: https://aur.archlinux.org/
.. _wiki completa e bem detalhada: http://www.archlinux-br.org/wiki
.. _The Arch Way: https://wiki.archlinux.org/index.php/The_Arch_Way_%28Portugu%C3%AAs%29
.. _Zen of Python: http://www.python.org/dev/peps/pep-0020/

