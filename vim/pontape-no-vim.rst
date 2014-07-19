Pontapé Inicial no VIM
######################
:date: 2014-07-17 19:13
:category: VIM
:tags: vim, inicio, .vimrc, github
:image: /pt/images/vim.png
:series: Hacking VIM
:description: Eu sempre enrolo e enrolo para falar de VIM aqui. Agora a coisa ficou séria, explodi uma bomba no meu ~/.vim e estou criando ele do zero. Porquê? Porque agora eu vou ser forçado a reconstruí-lo e a escrever sobre ele aqui!

Sim, eu faço tudo no VIM. Programo, escrevo e-mails, escrevo artigos, tomo notas, faço traduções, edição em massa, edição em lotes e acreditem, até calculo e ordenação/arranjo de dados. Como? Aprendendo a ferramenta!

.. image:: {filename}/images/vim_cat.png
        :target: {filename}/images/vim_cat.png
        :alt: VIM Cat
        :align: center

Assim como o `Fernando`_ diz nos seus artigos, também acredito que você deve conhecer bem seu ambiente de trabalho. Por isso dediquei um tempo e resolvi aprender esse editor onipresente, e agora vou repassar algumas coisas pra vocês.

.. more

Antes de começarmos, o negócio é o seguinte. Eu não tenho esse conteúdo pronto, eu vou escrever aos poucos (dividindo o tempo com o `Hack 'n' Cast`_). E não vou passar detalhadamente sobre todos os tópicos. Vou tentar dar uma ideia inicial do que é o VIM e passar algumas dicas de configurações, fica a critério de vocês expandirem o conhecimento acerca desse editor.

Porquê o VIM
------------

Primeiramente porquê ele está em todo lugar, sempre disponível e ele é a IDE que você faz. Uma vez acharam um escrito do Evangelho apócrifo de Tomé, e o traduziram errado. Essa é a tradução correta:

        A IDE Perfeita está dentro de Você e à Sua volta

        não em interfaces pesadas escritas em Java.

        Rache uma lasca de madeira e o VIM estará lá

        Levante uma pedra e o VIM você encontrará

Brincadeiras à parte, o VIM é o que você faz dele, se o seu VIM inútil e feio a culpa é toda sua. O meu VIM é assim:

.. image:: {filename}/images/vim/meu-vim.png
        :target: {filename}/images/vim/meu-vim.png
        :alt: Meu VIM
        :align: center

E para aqueles que falam que o VIM não tem funcionalidade de IDE, eu vou acenar positivamente com a cabeça. Seguido de um "Ele não tem porquê você não quer!". O VIM possui uma linguagem poderosa de *scripting* chamada **Vimscript** (nessa série de artigos vou tentar mostrar como criar um pequeno plugin). Com ela as pessoas desenvolvem diversos plugins, capazes de dar ao vim funcionalidade excelentes como:

- Autocompletar;
- Busca de arquivos com *Fuzzy Search*;
- Snippets (que expandem para códigos pre escritos);
- Atalhos para alternar entre arquivos *Model*, *View*, *Controllers*, *header files*, *test files* e documentações;
- Integração com o GIT;
- Além de milhares de funcionalidades únicas do VIM e temas (*colorschemes*).

Mas definitivamente, o que me mantém no VIM é o seu paradigma de Modos, o *keymap* ergonômico, os *spits*, *jumplists*, *marks*, *macros*, *windows*, *commands* e etc. Acho que deu pra ter uma ideia como o conteúdo é extenso... Mas vamos começar do básico!

O Seu Problema Com o VIM é Que Você Não o Entende
-------------------------------------------------

Todo mundo que usa o VIM pela primeira vez sofre para conseguir sair e acha estranho ter que pressionar o ``i`` antes de fazer qualquer inserção. Então vamos logo esclarecer uma coisa. *Keep your damn hands in the Home Row* (mantenha a droga dessa mão na *Home Row*):

.. image:: {filename}/images/vim/home-rows.png
        :target: {filename}/images/vim/home-rows.png
        :alt: Home Row
        :align: center

O VIM foi idealizado para manter a postura ergonômica em um tempo que os teclados não tinham a seção numérica ou as *"setinhas"*, por isso ele tem um comportamento um pouco diferente, e a regra principal é essa que falei aí em cima. Pode parecer estranho a princípio, mas você consegue fazer qualquer operação no VIM sem mover as mãos desse lugar. Como? Utilizando o paradigma de modos.

Modos no VIM
^^^^^^^^^^^^

.. image:: {filename}/images/vim/modos-simples-1.jpg
        :target: {filename}/images/vim/modos-simples-1.jpg
        :alt: Modos Simples
        :align: right

O VIM possui pouco mais de uma dezena de modos (é sério, são 13 ao todo), mas por enquanto vamos aprender dois modos, o ``Insert Mode`` e o ``Normal Mode``. O ``Insert Mode`` é o modo de inserção, é onde você insere textos. Já o ``Normal Mode`` é o modo onde você navega no texto e o transforma. O grande problema de todos os iniciantes é entender que no modo normal **cada letrinha do seu teclado** desempenha uma função específica (e muito específica).

Assim que você abre o VIM, ele está no ``Normal Mode``. Vamos começar com a tecla básica, o ``i``, quando no modo normal essa tecla tem a função de *inserção*. Quando pressionada ela te leva para o modo de inserção e põe o cursor à esquerda do caractere que você estava. A partir desse momento você por inserir textos normalmente. Para voltar ao modo normal, pressione a tecla ``ESC``.


.. _fernando: http://mindbending.org/pt/author/fernando-almeida
.. _Hack 'n' Cast: /pt/sobre-hack-n-cast
