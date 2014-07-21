Aberto a contribuições
######################
:date: 2014-07-21 13:40
:category: Mind Bending Blog
:tags: open source, software livre, contribuições, github, git, pull request, blog
:image: /images/MB_Logo_2014.png
:description: É isso mesmo, estou oficializando que este blog está aberto a contribuições. Mas claro, como é de costume nada por aqui é da maneira tradicional (ainda mais agora que abandonei o Wordpress).

Desde que me envolvi com o Software Livre e o mundo Open Source, acabei adotando essa filosofia e aplicando seus princípios em muitos aspectos da minha vida, e este site é só uma dessas consequências.

.. image:: {filename}/images/software-livre/sl-cloud.png
        :target: {filename}/images/software-livre/sl-cloud.png
        :alt: Software Livre - Cloud
        :align: center

Apesar deste site servir para manter o conhecimento que adquiro aberto e acessível para a comunidade, eu nunca tinha bolado uma boa forma de tornar o site 100% livre, isto é, aberto para outras pessoas e disponibilizado seu conteúdo sem restrições. Se você não tiver paciência para ler e quiser logo saber como contribuir, clique `aqui`_.

.. more

Curiosamente, as tecnologias web são naturalmente abertas. Por mais que alguém queira restringir o acesso ao seu conteúdo, um simples ``ctrl-c``/``ctrl-v`` ou um *printscreen* já burla os controles de acesso implementados. E acaba que toda forma de controle se tornam ridículas e infantis.

Como Publico Atualmente
-----------------------

Há algumas semanas o `Fernando Almeida`_ começou a publicar algumas artigos por aqui. Curiosamente, ele apareceu justamente quando eu comecei a criar uma forma de incentivar contribuições. Desde que abandonei o Wordpress isso pareceu mais distante, já que com o `Pelican`_ eu escrevo todos os artigos em `reStructured Text`_ em um repositório Git localizado no meu servidor. Quando faço um `git push` o próprio processo do Git se encarrega de recompilar o código fonte e atualizar o site. Em resumo meu fluxo de trabalho é o seguinte:

.. code-block:: bash

        $ vim articles/novo-artigo.rst
        $ git add articles/novo-artigo.rst
        $ git commit -m "Adiconado artigo XYZ"
        $ git push origin master

O que?! Você esperava mesmo que eu fizesse algo da maneira tradicional? E onde ficaria o espírito Hacker?

Como todo o processo de compilação é realizado no servidor, eu preciso que o repositório Git esteja armazenado no servidor, por isso não podia simplesmente jogar todo o site no GitHub.

Mas depois de algum tempo brincando com algumas ideias, consegui fazer um *script* `post-commit` para o Git que funciona com submodulos. Dessa forma pude mover todos os artigos para um repositório no GitHub, e no meu repositório privado ficam somente as configurações do site, o tema, plugins e algumas outras coisas mais.

Contribuindo
------------

Para contribuir com o site basta você ter uma conta no `GitHub`_, saber `reStructured Text`_, ter um bom português e fazer um *fork* desse `repositório`_.

O repositório está organizado por categorias, caso não encontre uma que se encaixe com seu objetivo, crie uma nova e comece a escrever. Se tiver dúvidas na sintaxe você tem 155 artigos  (na presente data) para consultar, ou simplesmente entre em contato comigo que eu te dou uma mão.

Escrito o novo artigo faça um *commit* com uma mensagem citando o título do artigo, por exemplo `git commit -m "Adicionando artigo 'Aberto a Contribuições'"`, e envie o *pull request* através do próprio GitHub. Se tiver dúvidas o próprio GitHub tem uma ótima orientação sobre `como fazer forks e pull requests`_.

A única coisa que merece explicação é o cabeçalho que uso para os artigos. Veja o exemplo abaixo:

.. code-block:: rst

        Aberto a contribuições
        ######################
        :date: 2014-07-19 11:02
        :category: Mind Bending Blog
        :tags: open source, software livre, contribuições, github, git, pull request, blog
        :image: /images/MB_Logo_2014.png
        :description: É isso mesmo, estou oficializando que este blog está aberto a contribuições. Mas claro, como é de costume nada por aqui é da maneira tradicional (ainda mais agora que abandonei o Wordpress).

A primeira linha especifica o título do artigo e logo abaixo são as *metatags*. Nelas são definidas a data de publicação do artigo (``:date:``), a categoria (``:category:``) e as *tags* (``:tags:``). As últimas duas foram criadas por mim e são implementadas no tema deste site. A primeira (``:image:``) especifica uma imagem que será utilizada para representar o artigo nas redes sociais e na página de autores (`veja a minha`_ como exemplo, são essas imagens quadradas). Já a segunda (``:description:``) define a descrição inicial do artigo que aparece logo abaixo da meta informação do artigo e também é utilizado pelo Google e redes sociais para apresentar e indexar o artigo.

Não deixe que isso te assuste, com certeza quando você enviar algum artigo novo eu irei revisar, corrigir e adequar qualquer *tag* faltando ou até mesmo o texto, estritamente quando necessário.

Imagens
-------

Lembrando que algumas imagens utilizadas no site podem possuir direitos autorais diferentes dos atribuídos neste site (`Creative Commons Attribution-ShareAlike 4.0 International`_), a estas a licença deste site não se aplica e são mantidos os direitos autorais atribuídos pelo criador.

Conclusão
---------

Bem, é isso aí pessoal. Sei que a forma de contribuição não é das melhores, mas segue a risca o `princípio deste site`_ e (creio que) será agradável para aqueles acostumados a desenvolver.

Até mais...

.. _aqui: /pt/aberto-a-contribuicoes#contribuindo
.. _Fernando Almeida: http://mindbending.org/pt/author/fernando-almeida
.. _Pelican: /pt/tag/pelican
.. _reStructured Text: http://docutils.sourceforge.net/rst.html
.. _GitHub: http://github.com/
.. _repositório: https://github.com/magnunleno/MindBending-pt
.. _como fazer forks e pull requests: https://help.github.com/articles/using-pull-requests
.. _veja a minha: http://mindbending.org/pt/author/magnun
.. _Creative Commons Attribution-ShareAlike 4.0 International: http://creativecommons.org/licenses/by-sa/4.0/
.. _princípio deste site: /pt/dobrando-o-mundo
