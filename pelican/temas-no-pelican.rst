Temas no Pelican
################
:date: 2014-03-17 17:46
:category: Pelican
:tags: pelican, temas, blog
:image: /images/pelican/flying_pelican.png
:series: Migrando Para o Pelican

Muito bem, agora que temos nosso site com o conteúdo migrado, e os plugins ativados está na hora de definir a aparência do nosso site e de quebra 75% da funcionalidade do seu site. Sim isso mesmo, o tema que você adota para o Pelican influencia (e muito) as funcionalidades do seu site, como por exemplo, o sistema de comentários utilizado, onde serão apresentadas os ícones das redes sociais, onde e como serão apresentadas as tags, categorias, arquivos e tudo mais.

.. image:: {filename}/images/pelican/flying_pelican.png
        :target: {filename}/images/pelican/flying_pelican.png
        :alt: Pelican
        :align: center

Não sabe do que eu estou falando? Então, antes de prosseguir, descubra `o que é o Pelican`_, `como instalá-lo`_, `como configurá-lo`_, `como migrar artigos antigos do Wordpress`_ e `quais plugins utilizar`_.

.. more

Lista de Temas Populares
------------------------

De forma semelhando aos plugins, existe um repositório que armazena uma `lista de temas`_ submetido por seus desenvolvedores.

Claro que você pode navegar pelo repositório pelo seu browser favorito e ver as screenshots dos temas existentes, mas eu pessoalmente prefiro ver meu tema renderizado nos temas. Então fiz o seguinte:

.. code-block:: bash

        $ mkdir ~/mindbending/temas
        $ cd ~/mindbending/temas
        $ git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes

Ao final do processo tenho todos os temas listados para o Pelican no meu diretório. Agora posso testar um por um, bastando editar a seguinte linha de configuração:

.. code-block:: python

        THEME = './temas/<nome do tema>'

Em seguida é necessário gerar seu site novamente:

.. code-block:: bash

        $ make html && make serve


Principais Destaques
--------------------

Em minha humilde opinião os seguintes temas se destacam dos demais:

* `BT3-Flat`_;
* `Just-Read`_;
* `SOMA`_;
* `Bootlex`_;
* `Built-texts`_;
* `Cebong`_;
* `Pelican-Chunk`_;
* `Crowsfoot`_;
* `Foundation`_;
* `Fresh`_;
* `Elegant`_;
* `Html5-Dopetrope`_;
* `Lannisport`_;
* `Neat`_;
* `Bootstrap3`_;
* `Cait`_;
* `Pelipress`_;
* `Plumage`_;
* `Pure`_;
* `Storm`_;

Indo Além
---------

Não se esqueçam que isso é um repositório no GitHub, então novos temas podem estar em estágio de aprovação. Consulte-os na seção `Pull Requests`_.

Além disso, se você tem um  conhecimento básico de HTML, Python e Jinja, você pode fazer seu próprio tema tomando como exemplo o `tema basic`_ e lendo a `documentação oficial`_.

.. _o que é o Pelican: /pt/adeus-wordpress
.. _como instalá-lo: /pt/instalando-o-pelican
.. _como configurá-lo: /pt/configurando-o-pelican
.. _como migrar artigos antigos do Wordpress: /pt/migrando-do-wordpress-para-o-pelican
.. _quais plugins utilizar: /pt/plugins-no-pelican
.. _lista de temas: http://github.com/getpelican/pelican-themes

.. _BT3-Flat: https://github.com/KenMercusLai/BT3-Flat
.. _Just-Read: https://github.com/getpelican/pelican-themes/tree/master/Just-Read
.. _SOMA: https://github.com/getpelican/pelican-themes/tree/master/SoMA
.. _Bootlex: https://github.com/getpelican/pelican-themes/tree/master/bootlex
.. _Built-texts: https://github.com/getpelican/pelican-themes/tree/master/built-texts
.. _Cebong: https://github.com/getpelican/pelican-themes/tree/master/cebong
.. _Pelican-Chunk: https://github.com/tbunnyman/pelican-chunk
.. _Crowsfoot: https://github.com/porterjamesj/crowsfoot
.. _Foundation: https://github.com/getpelican/pelican-themes/tree/master/foundation-default-colours
.. _Fresh: https://github.com/jsliang/pelican-fresh
.. _Elegant: https://github.com/talha131/pelican-elegant
.. _Html5-Dopetrope: https://github.com/PierrePaul/html5-dopetrope
.. _Lannisport: https://github.com/siovene/lannisport
.. _Neat: https://github.com/BYK/pelican-neat
.. _Bootstrap3: https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
.. _Cait: https://github.com/hdra/pelican-cait
.. _Pelipress: https://github.com/jjimenezlopez/pelipress
.. _Plumage: https://github.com/kdeldycke/plumage
.. _Pure: https://github.com/PurePelicanTheme/pure
.. _Storm: https://github.com/redVi/storm
.. _Pull Requests: https://github.com/getpelican/pelican-themes/pulls
.. _tema basic: https://github.com/getpelican/pelican-themes/tree/master/basic
.. _documentação oficial: http://docs.getpelican.com/en/3.3.0/themes.html
